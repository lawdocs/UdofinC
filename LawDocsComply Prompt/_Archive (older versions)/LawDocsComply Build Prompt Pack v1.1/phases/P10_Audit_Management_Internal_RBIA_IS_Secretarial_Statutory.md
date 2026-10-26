# Phase P10 — Audit Management: Internal Audit, RBIA, Concurrent, IS/IT, Secretarial, Statutory-Audit Support and Specialised Audits

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, hash-chained audit ledger and Correction Entries, object storage with Object Lock, outbox);
> - **P01** (identity, step-up MFA, roles `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view`, external-access grants);
> - **P02** (settings registry, rule packs, terminology, Locked/Governed/Tenant tiers);
> - **P04** (obligations, control tests, evidence, tasks, calendar, notifications — audit consumes and writes these);
> - **P07** (DMS evidence vault, OCR, eSign envelopes, Word/PDF rendering);
> - **P08** (risk register, RCSA, KRIs, loss events, risk appetite — the second line that audit reads);
> - **P06** (Audit Committee, Board, meetings, minutes, resolutions — where audit reports are tabled; directors and KMP register).
>
> **Sequencing:** P10 starts after P04 and P08 reach their sprint-2 freeze (obligation, control and risk read models). It runs in parallel with P11 (shared evidence and data-snapshot services) and P12 (IS audit consumes the P12 control library and VAPT register). P17 (Vidhi AI) adds the audit drafting agents; P10 ships the deterministic engine and the AI hooks behind flags.
>
> **Binding appendices:** A (state machines), B (data model, events, error codes), C (screens), D (access matrix), G (legal rules register — LR-RBI-IAF, LR-RBI-SA, LR-RBI-AUD, LR-RBI-CYB, LR-MCA-138, LR-MCA-143, LR-MCA-204, LR-SEBI-24A, LR-ICAI, LR-ICSI), J (accounting, auditing and secretarial standards map), L (integration adapters: Finbyx Part 7D, Udofin RA2/RA4), M (export package), Q (security). Ecosystem: Infrabyx Ecosystem Integration Specification v1.1 §4.7 (external access) and §6.21 (`audit` events).
>
> **Requirements covered:** R-055 (audit module), R-013 (complete compliance tool incl. reports and maker-checker), R-018 (auditor, external auditor, board, supervisor roles), R-057 (regulator read-only), R-052/R-053 (data from Finbyx and Udofin), R-075 (event audit trail), R-076/R-081 (download), R-097 (AI employee for audit drafting), R-054 (secretarial standards checks), R-012/R-059 (Internal Auditor and Audit Committee dashboards), R-021 (export folders).
>
> **Estimated effort:** 10 two-week sprints *(v1.1: +2 for §4R)* for a squad of 8 (audit core 3; programmes and type packs 2; workpapers, sampling and evidence 2; reports and dashboards 1), plus one domain analyst (CA with bank/NBFC audit experience) and one CS for the secretarial pack.
>
> **v1.1 changes (25 October 2026)**
> - New §4R (FR-P10-89 – FR-P10-108): scope-level auditor sharing (IMP-083), request-list generator with auto-chasing (IMP-084), auto-linking of existing compliance evidence to requests (IMP-085), AI plan and scoping-memo drafts (IMP-086, IMP-087), cross-engagement ACB summary (IMP-088), bidirectional finding ↔ compliance-issue links (IMP-089), preparer/reviewer sign-off with lock (IMP-090); full second-line compliance-testing programme (testing universe and risk scoring, cycles by risk, triggered tests, five-phase method, sampling table and tolerable deviation, root-cause taxonomy, issue SLAs with re-test, critical escalation, reliance, QA); continuous control monitoring tests run by the Control Monitor agent (VA-14) feeding workpapers; group audits of foreign subsidiaries through `gem` (P25); Audit Assistant (VA-07) under autonomy levels (NN-47, NN-50).
> - Regulatory inspections: the inspection, observation and regulator-proceeding records are owned by P26 (D-41); P10 keeps the inspection room, ATR/MAP roll-up, closure verification testing and audit-committee reporting (FR-P10-74 amended).
> - Special-investigation hand-off now goes to the P26 legal-matter register (not P07).
> - New screens SCR-AUD-31 – SCR-AUD-37, tables, settings, Gherkin scenarios and open items OI-P10-15 – OI-P10-21. Effort +2 sprints.
---

## 1. Objective and business outcome

LawDocsComply is sold to NBFCs, banks, UCBs, co-operative societies, ARCs, IFSCA entities, SEBI- and IRDAI-regulated entities, listed and unlisted companies and LLPs. Each of them must plan and evidence audits that a regulator, a statute or a professional standard requires, and most of them run those audits today in spreadsheets, e-mail and shared drives. This phase delivers **one assurance workspace** for every audit type a tenant runs or supports, built on the same obligation, control, risk and evidence base as the compliance and risk modules, so that audit work is not re-keyed and every finding drives remediation.

LawDocsComply is the **tool**. The tenant's auditors own every opinion, rating, finding and report. Neither LawDocs nor any Infrabyx company performs a tenant's internal audit through the tool (RBI (NBFC – Internal Audit Function) Directions, 2026, RBI/DoS/2026-27/464 ("IAF"), para 39: internal audit cannot be outsourced; contract experts only where the Board/ACB is assured the expertise is unavailable internally, and report ownership stays with regular IA staff) — the Marketplace (P21) may sell co-sourced specialist support only within those limits, and the product enforces the limits (§4C.3).

| Outcome | Exit-gate measure |
|---|---|
| One audit universe and risk-based plan for every tenant type | An ML NBFC, a scheduled UCB, a listed company and a credit co-operative society can each be onboarded with an auto-seeded universe (from the entity profile, departments, products, branches, IT systems, outsourcing register, obligations) and an ACB-approved annual plan in ≤ 2 working days of data being available; ten IAF para 31 parameters are locked for RBIA tenants |
| Every audit type has a governed pack | Programmes, checklists, report templates and timelines exist for: internal audit (Companies Act s.138), RBIA (IAF; RBI (Commercial Banks – Internal Audit Function) Directions 2026, RBI/DoS/2026-27/413; UCB RBIA instructions [VERIFY]), concurrent audit (RBI (Commercial Banks – Concurrent Audit) Directions 2026, RBI/DoS/2026-27/409), IS audit (RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026, RBI/DoS/2026-27/461 ("CYB"); SEBI CSCRF; IRDAI cyber guidelines), IT general controls, VAPT tracking, secretarial audit (s.204, Rule 9, LODR Reg 24A), statutory-audit support (PBC, CARO 2020, Rule 11(g), NBFC Auditor's Report Directions 2026, LFAR for banks), stock and receivables audit, branch audit, data-protection audit (DPDP Rules 2025 r.13 for SDFs), regulatory inspection management, tax-audit support, special investigation, outsourcing/vendor audit, co-operative statutory audit support |
| Evidence without re-keying | ≥ 80% of evidence items in a seeded RBIA engagement are system evidence links (LDC compliance records, policies, minutes, risk data, Finbyx/Udofin records by reference and hash) rather than uploads; every link is hash-pinned and drift-detected |
| Reproducible sampling and analytics | Re-running any sample with the stored snapshot and seed returns identical items; full-population tests run on imported or connected data |
| Findings drive remediation | Every issued finding creates action items in the P04 task engine, a risk-register link (P08) and, where a regulatory breach is flagged, a `ComplianceIssueRaised` event; overdue High findings escalate to the ACB pack automatically |
| Reports in the legally required shape | Report engine produces RBIA, internal-audit, concurrent, IS-audit, MR-3, Secretarial Compliance Report (Reg 24A), CARO clause pack, NBFC Auditor's Report Directions checklist, LFAR question bank (banks), and inspection-response packs as DOCX and PDF/A, with locked mandatory sections; AI may draft narrative, a named human signs |
| Audit Committee ready | One-click ACB pack (plan status, findings by rating and ageing, repeat findings, ATR, HIA in-camera tracker, QAIP, VAPT status, concurrent-audit summary) frozen with hash and tabled through P06 |
| External auditors and supervisors work inside the tool | Time-boxed, read-only, purpose-bound grants (D-12; Ecosystem Spec §4.7) for statutory, IS, secretarial, concurrent and co-operative auditors and supervisors; watermarked capped exports; daily activity report |
| Portability | Every engagement exports to `LDC-EXPORT-1.0` under `10 Audits and Inspections/<Audit type>/<FY>/<Engagement name> - <Period>/` with planning, workpapers, evidence, findings register (XLSX), report and manifest (Appendix M §M.3, X-27) |

---

## 2. Scope (in / out)

**In scope**
- Audit universe (auto-seeded, maintained by change triggers), risk assessment engine, risk-audit matrix, annual and rolling plans, capacity planning, plan approval and amendments.
- Methodology registry (scales, weights, scope tiers, sampling tables, rating definitions, report templates) with versioning and ACB approval.
- Engagement engine for all audit types listed in §4B, one lifecycle with type-specific states and gates.
- Programme and test-step library per audit type and per entity family; control-to-obligation mapping.
- Electronic working papers (index, review hierarchy, review notes, sign-off, file assembly and lock, addenda).
- Sampling (population freeze, methods, seeded PRNG, size calculators, evaluation) and computer-assisted audit techniques (CAATs) over LDC, connected-product and imported data.
- Evidence linking with hash pinning and drift detection; document evidence via the P07 vault.
- Findings lifecycle (condition–criteria–cause–effect, rating, root cause, management response, action plans, extensions, closure packs, independent retest, risk acceptance, repeat detection).
- Action Taken Reports (ATR) for internal, concurrent, IS, statutory, secretarial and regulatory-inspection sources; Risk Mitigation Plan (RMP)/Monitorable Action Plan (MAP) tracking for RBI inspections.
- Auditor registers: statutory auditor (NBFC SA Directions eligibility, tenure, rotation), concurrent auditor (bank directions), secretarial auditor (Reg 24A, CSAS), internal auditor eligibility (s.138, Rule 13), IS auditor (CERT-In empanelment where required), co-operative auditor panels.
- HIA register, independence controls, in-camera meeting tracker, QAIP.
- Statutory-audit support: PBC lists, query log, Auditor's Report Directions checklists, DNBS10 timer, exception-report register, CARO 2020 clause packs, Rule 11(g) evidence pack retrieval, branch-coverage calculator, LFAR question bank (banks), Form A/Form B generation for NBFC auditor appointments.
- Secretarial audit: applicability resolver, SS-1/SS-2 automated checks over P06 meeting data, MR-3 and Secretarial Compliance Report rendering, prohibited-services and tenure checks.
- IS audit, ITGC library, VAPT tracker, continuous auditing jobs.
- Report engine with locked legal sections and tenant customisation.
- Audit dashboards (Internal Auditor, HIA, ACB, CISO view of IS findings, CFO view of statutory audit) and ACB pack builder.
- External-access workspace for auditors and supervisors (shared with P01 grants; audit-specific rooms here).
- Ecosystem bridge: consume Finbyx/Udofin `AuditEngagementOpened`, `AuditFindingRaised`, `AuditFindingClosed`; publish the same events when LDC hosts the engagement; evidence requests by document reference.
- AI touchpoints (P17 agents) for drafting, summarising and suggesting — behind flags.

**Out of scope (owned elsewhere)**
- Performing audits or issuing opinions on behalf of tenants (never).
- Statutory auditors' own working-paper systems and firm-level quality management (SQM 1) — LDC stores only what the firm uploads.
- Fraud classification and reporting (P04/P12 and Finbyx FRM; audit raises a signal only).
- Supervisory-return preparation (P11), though audit may test it.
- Board-meeting conduct and minutes (P06), though secretarial audit tests them.
- Cyber incident response (P12), though IS audit tests it.
- Audit of LawDocsComply itself (SOC 2, ISO — P24 and Appendix Q); LDC's own internal audit uses the Operations Hub assurance room.

---

## 3. Personas and permissions touched

| Role code | What they do in P10 | Key restrictions |
|---|---|---|
| `ten_internal_auditor` (incl. HIA sub-flag `is_hia`) | Maintain universe, assess risk, build plan, run engagements, prepare and review workpapers, raise findings, retest, build ATR and ACB packs | Writes audit objects only (SoD); cannot hold a business target or business reporting line if HIA (IAF para 43); cannot retest a finding they remediated or advised on |
| `ten_external_auditor` | Statutory, concurrent (external), stock, branch, tax, co-operative auditor through an engagement-scoped grant | Read-only on tenant records; writes only PBC queries, auditor comments, checklist results, uploads; masked PII by default |
| `ten_is_auditor` | IS/IT audits, VAPT review, CAATs on IT data | As above if external; internal IS auditors are `ten_internal_auditor` with IS skill tag |
| `ten_secretarial_auditor` | Secretarial audit (MR-3, Reg 24A), SS checks | Engagement-scoped; cannot be appointed if a prohibited service exists (§4H) |
| `ten_committee_member` (Audit Committee) | Approve plan, methodology, risk acceptances above threshold; read all reports and packs | Read and approve only |
| `ten_board_member` | Read ACB pack summaries, annual consolidated major-risk view (IAF para 11) | Read only |
| `ten_kmp` (CEO/MD, CFO, CRO, CCO, CS, CISO) | Auditee owners; respond to findings; CFO runs statutory-audit support; CS runs secretarial engagement admin; CISO owns IS findings | Cannot edit audit workpapers or ratings |
| `ten_dept_head`, `ten_maker`, `ten_checker` | Finding owners and action owners; submit closure evidence | See only findings and actions assigned to them or their department |
| `ten_cco` | Receives regulatory-breach findings; concurs on risk acceptance of regulatory breaches | — |
| `ten_supervisor_view` | Inspection room (read-only, time-boxed, D-12) | No writes; exports only if the grant allows |
| `ten_admin` | Configure audit settings (Tenant tier), invite external auditors (creates grant requests) | Cannot approve own grant; cannot alter locked regulatory items |
| `dlv_professional` / `dlv_rm` | Co-sourced specialist under a Marketplace engagement acting as `ia_contributor` | Can prepare workpapers; cannot sign reports or rate findings; requires Board/ACB reference (IAF para 39) and conflict declaration |
| `svc_vidhi` | Drafts narratives, summarises evidence, proposes samples and mapping on behalf of a named auditor | Never rates, signs, issues or closes (NN-14) |
| `plt_super_admin` | Publishes global programme libraries, report base templates and rule packs (with content maker-checker) | No access to tenant audit data except break-glass (NN-30); overrides only via Correction Entry (D-02) |

Default SoD rules (Locked tier, Appendix D): the same user cannot be preparer and reviewer of a workpaper; the remediator cannot be the retester; the finding owner cannot accept their own risk; the HIA cannot approve a plan they drafted without ACB approval; an auditor with an operational role in the unit within the cooling period (default 12 months) cannot be assigned to the engagement.

---

## 4. Functional requirements

### 4A. Audit host modes and ecosystem position

**FR-P10-01 Host mode per tenant and per engagement type.** Setting `aud.host.mode` (Governed tier) with values:
- `LDC_NATIVE` (default for tenants without Finbyx): LawDocsComply is the audit system of record; evidence comes from LDC records, uploads and connected sources (P18) by reference.
- `FINBYX_HOSTED`: the tenant runs loan-book, ledger and operational audits inside Finbyx Part 7D (AU1–AU7). LDC mirrors engagements and findings read-only from `AuditEngagementOpened`, `AuditFindingRaised` and `AuditFindingClosed` (Ecosystem Spec §6.21), shows them on the ACB dashboard and ATR, links them to obligations and risks, and never edits them.
- `HYBRID`: per engagement type (e.g., IS audit, secretarial audit, data-protection audit and governance audits in LDC; RBIA of credit and collections in Finbyx).
Every engagement record carries `owner_system` (`LDC`, `FINBYX`, `UDOFIN`, `EXTERNAL`) and only the owner system may change it. A mirrored finding shows a banner "Owned by Finbyx — changes are made there" with a deep link.

**FR-P10-02 One universe, many owners.** The audit universe is always held in LDC when the tenant uses LDC as its GRC tool (compliance mode `LDC_EXTERNAL` or `LDC_GROUP`, Ecosystem Spec §9.1); units that Finbyx audits are tagged `audited_in = FINBYX`. Plan builder includes them for capacity and coverage reporting but schedules them as "external-system engagements".

**FR-P10-03 Evidence requests to connected products.** An LDC auditor can request evidence from Finbyx or Udofin through `POST /v1/evidence-requests` (P18 gateway → product evidence API): the request names dataset, period, filters, fields and masking level; the product returns a document reference, hash and masked sample keys. Raw PII never lands in LDC unless the procedure is identity-related and the grant allows it (NN-12, NN-13).

**FR-P10-04 Audit of service providers.** Tenants can open `OUTSOURCED_PROVIDER_AUDIT` engagements on any service provider, including Finbyx, Udofin, LawDocs and LawDocsComply itself, consistent with RBI outsourcing directions (RBI (NBFC – Managing Risks in Outsourcing) Directions, 2025, RBI/DOR/2025-26/363 ("OUT"), paras 34(vii)–(ix), 74(ii), 74(xii) [VERIFY paragraph numbers in LDC's own copy]). LDC's provider-assurance room (SOC reports once issued, VAPT summaries, BCP/DR evidence, sub-processor list) is published through P24 and shown here read-only.

### 4B. Audit type catalogue

**FR-P10-05** The engagement engine supports the following `engagement_type` codes. Each type has a pack (programme library, checklist, report template, timeline rules, required roles) loaded from rule packs; packs are Locked for regulatory minimums and Tenant-extendable elsewhere.

| Code | Audit | Mandatory for (as of 25 Oct 2026) | Basis | Pack contents |
|---|---|---|---|---|
| `IA_GENERAL` | Internal audit (companies) | Every listed company; unlisted public company with paid-up capital ≥ ₹50 crore, turnover ≥ ₹200 crore, borrowings ≥ ₹100 crore or deposits ≥ ₹25 crore; private company with turnover ≥ ₹200 crore or borrowings ≥ ₹100 crore [VERIFY: Rule 13(1) thresholds] | Companies Act 2013 s.138; Companies (Accounts) Rules 2014 r.13 | Process programmes (procure-to-pay, order-to-cash, payroll, treasury, fixed assets, inventory, statutory dues, IT), report per SIA 370 |
| `RBIA_UNIT`, `RBIA_THEMATIC` | Risk-based internal audit | NBFC-D and HFC-D; NBFC-ND and HFC-ND with assets ≥ ₹5,000 crore (IAF para 3); commercial banks (CB-IA, RBI/DoS/2026-27/413, para 3; excludes SFB, PB, LAB); UCBs per UCB internal-audit directions [VERIFY: 2026 UCB IAF direction number and threshold — legacy RBIA circular of 3 Feb 2021 covered UCBs ≥ ₹500 crore] | IAF paras 5–43; CB-IA | Ten locked parameters (IAF para 31), risk-audit matrix (para 32), scope tiers (para 34), report contents (para 35), ACB reporting (paras 9, 11, 36, 37), system audit to ITSC (para 34) |
| `CONCURRENT` | Concurrent audit | Commercial banks (CB-CA, RBI/DoS/2026-27/409); UCBs/StCBs/DCCBs per their instructions [VERIFY] | CB-CA; ICAI Manual on Concurrent Audit of Banks | Minimum scope areas (cash, advances, KYC/AML/FATCA/CRS, remittances and SWIFT, housekeeping and reconciliations, treasury, non-fund-based, forex, clearing, merchant banking, cards, employee conduct, mis-selling, RBI/internal policy compliance), all CPCs covered, quarterly key-findings to ACB, tenure checks (external auditor ≤ 5 years continuous; ≤ 3 years on one unit; retired staff ≤ 70 years) |
| `IS_AUDIT` | Information systems audit | NBFC BL ≥ ₹500 crore (CYB Ch IV) and ML/UL/TL excl. core investment companies (CYB Ch V) [VERIFY paragraph numbers in the 2026 text]; commercial banks (bank IT governance directions); SEBI REs under CSCRF (cyber audit by CERT-In empanelled auditor at the frequency the category requires) [VERIFY]; insurers under IRDAI Information and Cyber Security Guidelines 2023 [VERIFY]; IFSCA REs [VERIFY] | CYB; SEBI CSCRF (20 Aug 2024, with clarifications); IRDAI 2023 guidelines; ISO/IEC 27001:2022 | Scope library by control family (governance, access, change, operations, BCP/DR, cryptography, logging, third party, data protection), IS audit policy, timing before statutory audit, continuous-audit jobs |
| `ITGC` | IT general controls for financial reporting | Supports statutory auditor (SA 315), IFC reporting (s.143(3)(i)) and Rule 11(g) | SA 315; ICAI GN on Audit of IFC; Rule 11(g) | Access, change, operations, development controls; key reports |
| `VAPT_REVIEW` | VAPT tracking and review | ML and above: VA ≥ 6-monthly, PT ≥ 12-monthly for critical and DMZ systems (CYB) [VERIFY para]; SEBI CSCRF; CERT-In | CYB; CSCRF | Engagement and vulnerability register, SLA engine, recurrence detection, release gate hook |
| `SECRETARIAL` | Secretarial audit (MR-3) | Listed companies; public companies with paid-up ≥ ₹50 crore or turnover ≥ ₹250 crore; companies with bank/PFI borrowings ≥ ₹100 crore (Rule 9(1), as amended w.e.f. 1 Apr 2020); listed entities and their material unlisted Indian subsidiaries (LODR Reg 24A) | CA13 s.204; Rule 9; LODR Reg 24A (substituted 12 Dec 2024); ICSI Auditing Standards CSAS-1 to CSAS-4 (Revised Edition 2026, approved 28 Aug 2026 [VERIFY effective date]) | Law-wise checklists (CA13 and rules, SEBI regulations, FEMA, specific laws from the P04 register), SS-1/SS-2 automated checks, MR-3, Annual Secretarial Compliance Report |
| `SECRETARIAL_INTERNAL` | Internal secretarial review | Optional for every company and LLP [REC] | ICSI guidance | Same checklists without MR-3 |
| `STATUTORY_SUPPORT` | Statutory-audit support | All companies; NBFC-specific overlays (SA Directions RBI/DoS/2026-27/465; Auditor's Report Directions RBI/DoS/2026-27/468 ("AUD")) | CA13 ss.139–148; CARO 2020; AUD paras 5–12; SA Directions | PBC lists by profile, query log, AUD checklists, DNBS10 timer, exception-report register, branch-coverage calculator, Form A/B |
| `LFAR_SUPPORT` | Long Form Audit Report support (banks) | Commercial banks, SFBs, UCBs per RBI LFAR formats [VERIFY current format] | ICAI Guidance Note on Audit of Banks (2026 Edition, 16 Mar 2026) | LFAR question bank, branch LFAR, evidence links |
| `RULE_11G` | Audit-trail (edit-log) evidence | Every company keeping books electronically, from FY 2023-24 | Companies (Accounts) Rules r.3(1); Companies (Audit and Auditors) Rules r.11(g); ICAI Implementation Guide (Revised Jan 2024) | Software inventory, configuration snapshots, seal verification, exception register (from Finbyx AC7 or the tenant's own systems), SOC report register |
| `IFC_ICFR` | Internal financial controls testing | Listed and other companies where s.143(3)(i) applies [VERIFY exemptions for small/private companies] | s.134(5)(e), s.143(3)(i); ICAI GN on Audit of IFC | Risk-control matrix, walkthroughs, test of design and operating effectiveness |
| `TAX_AUDIT_SUPPORT` | Tax audit support | Persons crossing turnover/receipt limits under Income-tax Act 2025 s.63 (Form 26) [VERIFY]; FY 2025-26 and earlier under 1961 Act s.44AB (Forms 3CA/3CB/3CD) | ITA25; ITA61 | Clause-wise data pack from P11 |
| `STOCK_AUDIT` | Stock and receivables audit of borrowers | Lender-commissioned (banks under consortium norms; NBFC credit policy) [REC] | Lender policy; ICAI guidance on stock audit [VERIFY] | Drawing-power recomputation, stock statement verification, ageing of receivables, insurance, physical verification checklist |
| `BRANCH_AUDIT` | Branch / unit audit | Banks (statutory branch audit), NBFCs (internal), co-operatives | GN Audit of Banks Section B; tenant policy | Branch checklist, cash, documents, KYC, security, attendance |
| `DATA_PROTECTION_AUDIT` | DPDP / privacy audit | Significant Data Fiduciaries: annual DPIA and audit (DPDP Act 2023 s.10(2); DPDP Rules 2025 r.13, applicable from 13 May 2027 [VERIFY commencement]); GDPR Art. 28(3)(h), 32 where applicable | DPDP; GDPR; P12 control library | Notice/consent tests, rights handling, retention, breach readiness, processor contracts, cross-border, children's data |
| `CYBER_AUDIT_CERTIN` | Cyber security audit by CERT-In empanelled auditor | Where a sector regulator or contract requires (SEBI CSCRF; government entities; CERT-In Directions 28 Apr 2022 for logs and incident reporting) [VERIFY] | CERT-In; CSCRF | Scope letter, empanelment check, findings import |
| `COOP_STATUTORY_SUPPORT` | Co-operative statutory audit support | Every co-operative society (MSCS Act 2002 s.70 as amended 2023 for multi-state; State Acts, e.g. Maharashtra Co-operative Societies Act 1960 s.81) [VERIFY per Act] | MSCS; State Act | Audit classification, rectification report tracking, panel auditor checks |
| `SEBI_INTERMEDIARY_IA` | Internal audit of SEBI intermediaries (stock brokers, DPs, RTAs, PMS, IA/RA) and AMC/MF internal audit | Per SEBI master circulars (e.g., half-yearly internal audit of stock brokers by an independent CA/CS/CMA; MF/AMC internal audit) [VERIFY each frequency] | SEBI master circulars | Exchange/depository checklists [VERIFY formats] |
| `AIF_COMPLIANCE_TEST` | AIF compliance test report / audit | AIF Managers (SEBI AIF Regulations 2012 and master circular) [VERIFY current CTR requirement] | SEBI | Placement memorandum compliance, investment conditions, reporting |
| `INSURER_IA` | Internal/concurrent audit of insurers and intermediaries | IRDAI corporate governance and investment regulations (e.g., concurrent audit of investment operations) [VERIFY current 2024 IRDAI master circular references] | IRDAI | Investment, claims, underwriting, distribution checklists |
| `ESG_ASSURANCE_SUPPORT` | BRSR Core reasonable assurance support | Top listed entities by market capitalisation on the SEBI glide path [VERIFY current threshold year] | SEBI LODR Reg 34(2)(f); SEBI BRSR circulars | KPI data lineage, evidence, assurance-provider room |
| `REGULATORY_INSPECTION` | Supervisory inspection management | RBI (incl. Risk Based Supervision letters, RMP/MAP), NHB, NABARD, SEBI, IFSCA, IRDAI, Registrar of Co-operative Societies | Respective Acts | Inspection room, information-request register, response packs, MAP tracker, compliance submissions (filed by the RE on DAKSH or the regulator's channel — D-13) |
| `SPECIAL_INVESTIGATION` | Special investigation / fraud examination | Tenant policy; FRM directions | FRM; SIA 11 | Restricted access, sealed workpapers, hand-off to fraud function |
| `OUTSOURCED_PROVIDER_AUDIT` | Audit of service providers | OUT paras 34(vii), 74(ii) [VERIFY] | OUT | Provider questionnaire, SOC report review, on-site checklist |
| `COMPLIANCE_TESTING` | Second-line compliance testing (run by compliance, recorded in the same engine) | CMP (RBI/DoS/2026-27/460) for ML/UL NBFCs; bank compliance function directions | CMP | Pulls P04 obligations; results feed `ControlTestResultPublished` |
| `QAIP_REVIEW` | Quality assurance of the IA function | IAF para 6 (QAIP); IIA Global Internal Audit Standards (effective 9 Jan 2025) [VERIFY] | IAF; IIA | Self-assessment checklist, external assessment record |

**FR-P10-06 Applicability resolver.** At onboarding, each FY start and on any profile change (P15 entity logic), the resolver evaluates each type's applicability rule (CEL, with citation) against the entity profile (legal form, listed, layer, deposit-taking, asset size, paid-up capital, turnover, borrowings, regulator, sector flags, SDF flag) and writes `audit_applicability_decision` rows (rule version, inputs hash, result, citation). Mandatory types appear on the plan builder as "required"; recommended types as "suggested". Removing a mandatory type requires a Correction Entry with CCO and HIA approval (NN-29, D-02).

### 4C. Audit universe, risk assessment, plan and methodology

**FR-P10-07 Universe units.** `audit_universe_unit` types: legal entity, branch/office, department/function (from P13 org structure), process, product, IT system (from P12 asset inventory), outsourced arrangement (P12 TPRM register), regulatory theme (instrument from P03 catalogue), committee (P06), co-lending/LSP arrangement (from Finbyx/Udofin via P18), project, subsidiary/group company, co-operative society unit (P16). Risk Management, Compliance and every critical IT system are mandatory units for RBIA tenants (IAF paras 26, 34) and cannot be archived.

**FR-P10-08 Auto-population and change triggers.** The universe is seeded from masters and kept current by events: a new branch, product, department, critical system, material outsourcing, committee, subsidiary or instrument raises a "universe change" task to the HIA within 1 working day (setting `aud.universe.change_task_sla_days`, Tenant tier). The HIA adds, merges or archives units (archive needs reason and reviewer approval).

**FR-P10-09 Unit attributes.** Owner (HRMS person), line of defence, last audit date and rating, policy maximum interval, regulatory touchpoints (obligation IDs from P04), linked risks and KRIs (P08), volume measures (AUM, accounts, transactions, cash handled, headcount), open findings count by rating, coverage clock `next_audit_due = last_audit_end + min(policy_max_interval, frequency_for_risk_tier)`.

**FR-P10-10 Risk assessment engine.** At least annually and on triggers (new product, regulatory observation, fraud classification, KRI breach, key-personnel change, significant incident) (IAF para 25). Two dimensions — inherent (business) risk and control risk — scored on the tenant scale (default 1–5) and mapped to H/M/L with trend (increasing/stable/decreasing) and documented basis (IAF paras 28–29). For RBIA tenants the ten IAF para 31 parameters are Locked and pre-filled:

| # | Parameter (IAF para 31) | LDC pre-fill source | Dimension |
|---|---|---|---|
| 1 | Previous internal audit reports and compliance | Open and repeat findings, ATR ageing (this phase) | Control |
| 2 | Proposed changes in business lines or focus | Product approvals (P04 new-product obligation), Board resolutions (P06) | Inherent |
| 3 | Significant change in management or key personnel | KMP/director change events (P06, P13) | Control |
| 4 | Results of regulatory examination | Inspection observations and MAP status (`REGULATORY_INSPECTION`) | Control |
| 5 | Reports of external auditors | Statutory, IS, concurrent, secretarial findings | Control |
| 6 | Industry trends and macro factors | Tenant register; P09 macro scenario library | Inherent |
| 7 | Time elapsed since last audit | Coverage clock | Control |
| 8 | Volume of business and complexity | Volume measures (Finbyx/Udofin by reference or P11 imports) | Inherent |
| 9 | Variances between actual and budgeted performance | Budget vs actual (P11 accounting bridge) | Inherent |
| 10 | Business strategy vis-à-vis risk appetite | Risk-appetite utilisation (P08) | Inherent |

Tenant parameters may be added with weights (fraud cases, complaints per 10,000 accounts, DPD migration, cash intensity, cyber incidents, outsourcing materiality, data-quality issues, compliance overdue rate from P04). Non-RBIA tenants use a simplified default (inherent × control, five optional parameters) that they can extend. The auditor confirms or overrides each pre-fill with a reason; the HIA approves; the ACB notes.

**FR-P10-11 Risk-audit matrix and priority.** Magnitude × frequency matrix; planning priority for RBIA tenants follows IAF para 32 in the Locked order H/H, H/M, H/L, M/H, M/M, L/H; M/L, L/M, L/L units are covered only by the policy-maximum clock. Scope tiers low, medium, high, very high, extremely high (IAF para 34) mapped from the three-level assessment; the mapping is stored in the methodology version.

**FR-P10-12 Plan builder.** Inputs: ranked universe, capacity in person-days by skill (credit, IT/IS, treasury, KYC/AML, forensic, secretarial, data protection, actuarial for insurers), mandatory inclusions (policy-maximum breaches, regulatory requests, ACB asks, IS audit before statutory audit — CYB "preferably" rule), calendar constraints (quarter closes, AGM date, Board calendar from P06), external-system engagements (Finbyx-hosted). Output: draft annual plan (unit, quarter, scope tier, days, team, skills), capacity-gap report, deferred-unit list with reasons, and a Gantt view. Drag-and-drop between quarters re-checks capacity.

**FR-P10-13 Plan approval and amendments.** HIA → MD & CEO or WTD (information, where the reporting line requires) → ACB or Board (approval with minute reference from P06) (IAF para 5). Published plan versions are immutable; in-year amendments carry reasons and require ACB noting. A unit past its policy maximum cannot be removed without an ACB minute reference.

**FR-P10-14 Methodology registry.** `audit_methodology_version`: rating scales and definitions, weights, scope-tier mapping, sampling tables, finding rating SLAs, report templates, engagement timers. Drafted by HIA, reviewed by a second IA reviewer, approved by the ACB (minute reference), effective from a stated date. In-flight engagements keep their version unless migrated with reason. Locked regulatory items (ten parameters, matrix order, mandatory report sections) cannot be removed in any version (NN-28).

**FR-P10-15 Policy registry link.** IA/RBIA policy (IAF paras 12–15), IS audit policy, concurrent audit policy, audit charter and statutory-auditor appointment policy (SA Directions; published on the website) are P07 policy records with owner, version, Board/ACB approval date and next review date; P10 reads the current approved version and blocks plan approval if the policy is overdue for review (warning, configurable to block).

### 4C.3 Function controls — HIA, independence, outsourcing, QAIP

**FR-P10-16 HIA register.** Appointment date, reporting line (Board, ACB, MD & CEO or WTD — IAF para 42), tenure start, planned tenure (≥ 3 years preferable, IAF para 41, flag suppressed where career auditors run IA), Board/ACB approval references, appraisal reviewer (ACB/Board must review and accept the HIA appraisal where the MD & CEO/WTD is the reporting authority — IAF para 42).

**FR-P10-17 Independence enforcement.** The role-assignment service (P01) blocks assigning business targets or a business reporting line to the HIA (IAF para 43) and blocks incentive plans tied to business results for IA staff where the client HRMS (P13) is used (IAF para 22 [VERIFY para]). Every engagement member signs an independence declaration before fieldwork (no operational responsibility for the unit within the cooling period, no relative in the unit, no results-linked incentive).

**FR-P10-18 No-outsourcing rule.** For RBIA tenants under IAF, report-owner and engagement-lead fields accept only tenant employees with the internal-auditor role. External experts (including LawDocs Marketplace professionals and former employees) get a time-boxed `ia_contributor` scope: they can prepare workpapers but cannot sign reports or rate findings; the system requires a Board/ACB reference that expertise is unavailable internally and a conflict-of-interest declaration (IAF para 39). For non-RBIA tenants (e.g., companies under s.138, where the internal auditor may be an external CA/CMA firm under Rule 13), the engagement lead may be external — the rule pack switches by entity.

**FR-P10-19 In-camera meetings.** Where the MD & CEO or WTD is the reporting authority, the ACB/Board meets the HIA at least quarterly without senior management (IAF para 42). The P06 calendar schedules them; a quarter-end without a minuted meeting raises an exception to the CS and ACB chair on day 1 of the next quarter.

**FR-P10-20 Full access.** The HIA and IA staff have tenant-wide read-only access to all records (IAF para 40) through an internal audit-mode role (no expiry, fully logged, visible to the ACB chair on request); sealed classes (POSH, whistle-blower identity, credentials) need an additional unseal approval by their custodian (NN-13).

**FR-P10-21 QAIP.** Annual self-assessment against a configurable checklist (Board/ACB oversight, independence, risk-assessment quality, coverage, documentation, supervision, follow-up), optional external assessment record, results and improvement actions to the ACB (IAF para 6). Checklist seeded from IIA Global Internal Audit Standards domains and ICAI SIA 7 / Framework Governing Internal Audits [REC].

### 4D. Engagements and programme library

**FR-P10-22 Engagement record.** Type, legal entity, units, period under audit, objectives, scope, exclusions, criteria (obligation IDs from P04 with instrument and paragraph; policy IDs from P07; standards), timeline, team with roles (lead, member, reviewer, external expert, `ia_contributor`), independence declarations, methodology version, budget days, engagement letter (external engagements; eSigned through P07), related prior findings, `owner_system`, confidentiality class (normal, restricted, sealed for special investigations).

**FR-P10-23 Creation wizard (≤ 6 steps, pre-filled).** Type → unit(s) (from plan line, pre-filled) → scope (pre-filled from the pack and the unit's obligations and risks; auditor removes or adds) → team (skills matched to the scope; conflicts and cooling period flagged inline) → declarations (sent to each member, one-click attest) → submit for HIA approval. Ad hoc engagements (ACB or regulator request) start from "Request" and need HIA approval before planning.

**FR-P10-24 Programme library.** `audit_programme` (versioned) → `audit_step` with objective, criteria reference, procedure text, test type (inquiry, inspection, observation, re-performance, recomputation, analytics, confirmation), population source, expected evidence pattern, default sample method, risk and control links, obligation links, estimated hours. Seed libraries (Platform content, maker-checker published; tenants copy and extend):
- **NBFC RBIA** by area, seeded from the ICAI Technical Guide on Risk Based Internal Audit of NBFC (2024) [ICAI, recommendatory]: sourcing and DSA/LSP management, KYC/AML (RBI KYC Directions 2025), credit appraisal and sanction, disbursement and KFS, loan book and asset classification (IRACP RBI/DOR/2025-26/356), ECL governance (FS RBI/DOR/2025-26/359 para 12), collections and recovery conduct (Responsible Business Conduct directions), fair practices and grievance, ALM and treasury, investments (incl. NBFC-ICC investment caps and AIF investment rules [VERIFY current RBI circular]), co-lending and digital lending (DLA register, DLG caps), securitisation and transfers, outsourcing, IT and cyber (CYB), fraud risk management (FRM RBI/DoS/2026-27/463), governance and committees (GOV RBI/DOR/2025-26/344), compliance function (CMP, ML/UL), regulatory returns (SR), CIC reporting (CIR), finance and tax, HR and staff accountability.
- **Bank RBIA and concurrent** seeded from ICAI Technical Guide on RBIA in Banks and Manual on Concurrent Audit of Banks [ICAI] with CB-CA minimum areas.
- **UCB, StCB/DCCB** (RBI/NABARD), **credit co-operative society** (State Act/MSCS; member loans, share capital, thrift deposits, election compliance, by-law compliance, statutory reserves, audit rectification).
- **ARC** (acquisition and valuation of financial assets, SR issuance and NAV, resolution strategies, SARFAESI actions, management fee recognition — RBI (ARC) Directions 2025 [VERIFY paragraph numbers]).
- **IFSCA FC/FU** (USD books, permissible activities, governance circulars), **SEBI intermediaries** (exchange/depository internal-audit checklists [VERIFY formats]), **AMC/MF**, **AIF**, **listed company** (LODR, PIT, SAST, RPT), **insurer and insurance intermediary** (IRDAI) [VERIFY each].
- **Companies and LLPs** (s.138 process audits; LLP Act 2008 compliance).
- **IS/IT/cyber** (CYB families; CSCRF; IRDAI cyber; ISO 27001:2022 Annex A controls mapping from P12).
- **Data protection** (DPDP Act and Rules; GDPR; CCPA where profiled) from the P12 control library.
- **Labour and POSH** (P13 registers and IC records — sealed rules apply).
Every step maps to obligation IDs, so the coverage report shows "obligations tested this year / applicable obligations" per instrument.

**FR-P10-25 Engagement states.** `PLANNED → SCOPED → APPROVED → FIELDWORK → DRAFT_REPORT → MANAGEMENT_RESPONSE → FINAL_REPORT → ISSUED → FOLLOW_UP → CLOSED`, plus `ON_HOLD`, `CANCELLED`; type-specific sub-states (e.g., `SECRETARIAL`: `CHECKLISTS_RUN → OPINION_DRAFTED → SIGNED`; `STATUTORY_SUPPORT`: `PBC_OPEN → FIELDWORK_SUPPORT → REPORT_SIGNED → DNBS10_FILED`). Full table in §5.1.

### 4E. Working papers

**FR-P10-26 Workpaper structure (SA 230; SIA 330).** Reference index (e.g., `B.3.2`), engagement, area, step (from programme or ad hoc), objective, criteria, population and sample reference, procedures performed, results, exceptions, conclusion, preparer and date, reviewer and date, review notes with clearance, evidence links, version, sign-off (eSign event: user, time, content hash). Permanent-file section per unit (charter, prior reports, process notes, standing data, regulatory references).

**FR-P10-27 Review hierarchy.** Preparer → reviewer → engagement lead → HIA (for high-risk areas) — two-person review is a Locked floor (SIA 350). A workpaper with open review notes cannot be signed off; the block shows the open notes.

**FR-P10-28 Assembly and lock.** On report issue the engagement file is assembled and locked. Default assembly deadline 60 days from report date for statutory-style files and 45 days from signing for secretarial audits (CSAS-2 [VERIFY in Revised Edition 2026]). After lock, changes are append-only addenda with reason, author and date; the original is never altered (SA 230 treatment of post-assembly changes; NN-02).

**FR-P10-29 Retention.** Default ≥ 8 years from lock for internal and secretarial files (CA13 s.128(5) analogy; CSAS-2), legal hold respected; statutory-auditor workpapers belong to the firm — LDC keeps only what the firm uploads.

**FR-P10-30 Workpaper editor UX.** Split view: left = step and procedure, right = live source record and pinned snapshot side by side; keyboard shortcuts (next item `J`, previous `K`, mark "no exception" `N`, raise finding `F`, add review note `R`); templates for walkthrough notes, test of design, test of operating effectiveness, recomputation sheets (XLSX embedded viewer), confirmation letters (DOCX).

### 4F. Sampling and computer-assisted audit techniques

**FR-P10-31 Population freeze.** A saved, versioned, parameterised population query runs against a point-in-time snapshot (LDC data, a P11 imported dataset, or a connected-product dataset by reference); LDC stores row count, control totals, query text and SHA-256 of the ordered key list (`population_hash`).

**FR-P10-32 Methods.** Simple random (seeded PRNG), systematic (random start), stratified (amount, product, branch, DPD bucket, department), monetary-unit sampling, attribute sampling, top-N and key items, judgemental (reason per item). Method, parameters and seed stored; same snapshot + seed → identical items (NN-22).

**FR-P10-33 Size calculators and evaluation.** Attribute (confidence, tolerable deviation, expected deviation) and MUS (confidence, tolerable misstatement, expected misstatement) calculators; SA 530 prescribes no sizes, so tables live in the methodology version [ICAI]. Evaluation: deviations, projected misstatement, upper deviation limit; auditor's conclusion recorded.

**FR-P10-34 CAAT library (`analytic_test`, versioned).** Full-population tests over imported or connected data. Seed tests:
- Lending (any lender, via P11 loan-tape import or Finbyx by reference): disbursement before sanction; duplicate disbursements; interest accrual before disbursement value date; KFS not issued before execution; penal charges vs policy; NPA flag timing vs IRACP day-end rule; restructured accounts without approval; related-party loans above materiality without Board approval; DLG above 5% cap; loans to directors/relatives (BR Act s.20 for banks; NBFC GOV/CRM limits [VERIFY]).
- Finance: journal entries posted on holidays or after period lock; manual JEs above threshold; round-sum entries; vendor master duplicates (same PAN/bank account); payments to employees' bank accounts; GST rate mismatches; TDS short deduction; Benford first-digit test.
- Access and IT: users with conflicting roles; dormant accounts with recent logins; privileged access outside change windows; configuration changes without change ticket; audit-trail gaps (Rule 11(g)).
- Compliance: obligations closed without evidence; evidence uploaded after due date; checker = maker anomalies; overdue obligations by department (P04 data).
- HR/payroll (P13): ghost employees (no attendance, active pay), duplicate bank accounts, pay above grade band, minimum-wage shortfall vs rule pack.
Each run stores snapshot, test version, parameters, exceptions; exceptions convert to sample items or findings; tests can be scheduled (continuous auditing) and each run publishes `ControlTestResultPublished`.

**FR-P10-35 Data access for analytics.** Analytics run in a governed, masked, read-only analytics schema per tenant (no PII unless the test needs it and the auditor records the reason); exports from analytics follow the same masking.

### 4G. Evidence

**FR-P10-36 System evidence links.** `(source_system, source_type, source_id, source_version | event_seq)` + canonical JSON snapshot of fields used + SHA-256 + snapshot time + ledger chain position. Sources: LDC (obligation instances, evidence files, policy versions, minutes, registers, risk records, HR records, returns runs, grievances), connected products (Finbyx, Udofin, Equator by document reference and hash, Ecosystem Spec §6.13), imported datasets (P11).

**FR-P10-37 Drift detection.** If the source changes after linking, the link shows "source changed since evidence" with a diff; the evidence is never updated; dependent workpapers are flagged.

**FR-P10-38 Document evidence.** Uploads go to the P07 evidence vault (WORM, SHA-256, malware scan, PII tag, classification, OCR text). De-duplication by hash keeps separate link records.

**FR-P10-39 Integrity verification.** "Verify file" recomputes all hashes in an engagement and checks against the ledger chain; the result is itself an evidence item; failures raise a P1 integrity alert (NN-09).

**FR-P10-40 Evidence requests (PBC-style) to auditees.** Auditor creates requests (item, owner, due date, format) → auditee uploads or links → auditor accepts or queries; ageing shown to the department head and CFO.

### 4H. Findings, management responses, actions, ATR

**FR-P10-41 Finding structure.** Condition, criteria (obligation/policy/standard reference), cause (root-cause category: people, process, system, policy, external, governance), effect/risk, rating (tenant scale; default Critical/High/Medium/Low with definitions), financial impact estimate, regulatory-breach flag with obligation ID, repeat flag (same root cause and unit within 24 months, configurable), recommendation, evidence links, masked sample refs.

**FR-P10-42 States** `DRAFT → DISCUSSED → ISSUED → RESPONSE_RECEIVED → ACTION_AGREED → IN_REMEDIATION → CLOSURE_SUBMITTED → RETEST → CLOSED`, branches `RISK_ACCEPTED`, `REOPENED`, `WITHDRAWN` (§5.2). Corrections after `ISSUED` create a new finding version and re-emit `AuditFindingRaised` (version n+1); closure date is the retest date — no back-dated closure (NN-07).

**FR-P10-43 Management response.** Agree / partly agree / disagree with reasons; action items each with owner, due date, evidence required. Unresolved disagreement → HIA decides; the ACB sees both views.

**FR-P10-44 Remediation clocks.** Default due dates by rating: Critical 15, High 30, Medium 90, Low 180 days (Tenant tier); a tighter regulatory or contractual date wins. Extension by next-level approver; second extension of a High/Critical finding needs ACB noting. Reminders T−7, T−1, daily when overdue.

**FR-P10-45 Closure and retest.** Closure pack requires evidence per action item and owner attestation; retest by a user who did not remediate or advise (Locked floor); population findings need a fresh sample. Pass → `CLOSED` (`AuditFindingClosed`); fail → `REOPENED` (repeat counter, new due date ≤ original SLA).

**FR-P10-46 Risk acceptance.** Delegated-authority matrix (P02), rationale, compensating controls, expiry ≤ 12 months (configurable), RMC/ACB noting for High and Critical, CCO concurrence for regulatory breaches (Locked floor); renewal or return to remediation at expiry.

**FR-P10-47 Cross-module effects on `ISSUED`.** Action items become P04 tasks with calendar entries; a P08 risk-register link (new or existing risk; control rating downgraded); `ComplianceIssueRaised` where regulatory-breach is flagged; a fraud signal to P12/FRM owner where suspected fraud is flagged (auditor cannot classify fraud); people-risk indicator to P08 where root cause = people (aggregated, no names).

**FR-P10-48 ATR register.** One ATR per source: IA, RBIA, concurrent, IS audit, statutory auditor's management letter, secretarial audit observations, RBI inspection (RMP/MAP), NHB/NABARD/SEBI/IFSCA/IRDAI/Registrar inspections, CERT-In audit, customer-service audit, Finbyx-hosted findings (mirrored). Per item: observation, rating, response, action, owner, due date, status, evidence, auditor validation, ageing (0–30, 31–90, 91–180, > 180 days). Items closed without auditor validation show "management-closed, unvalidated".

**FR-P10-49 Board/ACB reporting.** All pending High and Medium findings and persisting irregularities (IAF para 37); closure status within timelines (IAF para 9); annual consolidated major-risk view from all audits and inspections (IAF para 11); concurrent audit quarterly key findings (CB-CA); IS audit critical issues to ACB/ITSC (CYB).

### 4I. Statutory-audit support

**FR-P10-50 Auditor register and eligibility (NBFC).** Applicability: SA Directions apply to all NBFCs including HFCs; NBFC-ND with assets < ₹1,000 crore may continue extant procedure (SA para 3) — resolver shows "SA Directions optional" with checks as recommendation. Joint audit by at least two firms with no common partners/network where assets ≥ ₹15,000 crore at previous year-end (SA para 11); eligibility bands by asset size (Form B data: FTPs, FCAs, CISA/ISA, experience, staff — SA para 14), conditions (s.141; no partner who is a director of an RBI-regulated group entity — para 15), independence (concurrent auditor ineligible; non-audit work 1-year gap either side; network extension — paras 18–20), term 3 years continuous (para 23), cooling-off 6 years (para 24), firm-wide cap of 8 NBFCs (para 25); Form A within one month of appointment (para 30(1)); shortlist ≥ 2 firms per vacancy (para 30(2)); annual performance review and reporting of serious lapses (para 8) [VERIFY each paragraph number against RBI/DoS/2026-27/465 — numbers carried from Finbyx v1.5 Part 7D AU5.1]. For banks: statutory central/branch auditor rules per RBI bank SCA/SA directions [VERIFY 2026 number]; UCBs per UCB SA directions [VERIFY]; companies generally: CA13 ss.139–141 rotation (5-year individual, 2×5-year firm for listed and prescribed classes, Rule 5) [LAW].

**FR-P10-51 PBC lists.** Templates by profile (Ind AS NBFC Div III, AS NBFC Div I, HFC, bank Forms A/B, UCB, co-operative, core investment company, ARC, IFSC entity, listed company, unlisted company, LLP, Section 8 company). Item: description, owner, source (auto-generated from P11/P04/P06/P13 or upload), due date, status `REQUESTED → IN_PREPARATION → PROVIDED → AUDITOR_QUERY → ACCEPTED`, auditor comments, file hash. Auto-generated items include trial balance and Schedule III mapping (P11), loan-book listing with classification and provisions (P11 or Finbyx), IRACP vs Ind AS table, NPA movement, related-party register (P06), borrowings and covenants, investment register, fixed-asset register, GST/TDS reconciliations (P11), litigation and contingent liabilities, fraud register, CERSAI/CKYC status, statutory registers (P06), Board/committee minutes index (P06), compliance certificates (P04), POSH annual report numbers (P13, counts only), CSR spend (P06).

**FR-P10-52 Query log.** Auditor queries against PBC items or areas, response owner, due date, resolution, ageing to CFO.

**FR-P10-53 NBFC Auditor's Report Directions checklists.** Under AUD (RBI/DoS/2026-27/468, 31 Jul 2026; s.45MA(1A); supersedes 2016 Directions): para 5 separate report to the Board in addition to s.143; para 6 (all NBFCs: CoR held or required under Principal Business Criteria; continued entitlement as on 31 March; NOF compliance); para 7 items for deposit-taking NBFCs (deposit limits, credit rating, defaults, CRAR, prudential norms, liquid assets, DNBS01 and DNBS03 timeliness, branch opening/closing and agents); para 8 for non-deposit NBFCs (Board resolution on non-acceptance of deposits, no deposits accepted, prudential norms, CRAR and timely DNBS03 for ML and above, correct MFI classification); para 9 for companies advised by RBI that CoR is not required; para 10 reasons for unfavourable/qualified statements; paras 11–12 exception report to the Senior Supervisory Manager / DoS Regional Office reporting contraventions only. Each checklist line links the computation that answers it (Principal Business Criteria from P11 accounting bridge — financial assets > 50% of total assets and financial income > 50% of gross income, bank FDs excluded [VERIFY current wording]; NOF from P09; DNBS03 filing evidence from P11). The auditor marks favourable / unfavourable / qualified with reasons.

**FR-P10-54 DNBS10 timer.** Due within 5 working days of the date of signing of the auditor's report and not later than 31 December (AUD; SR para 21 item 7 and para 23 [VERIFY]); tenant holiday calendar; reminders T−3, T−1, T; the auditor compiles and files on CIMS with credentials the NBFC creates — LDC never stores or scripts CIMS credentials (D-04 default client-only; D-13; NN-08); acknowledgement uploaded as evidence. ARC equivalent under RBI (ARC – Supervisory Returns) Directions 2026 (RBI/DoS/2026-27/469).

**FR-P10-55 Exception-report register (AUD paras 11–12).** Records receipt of the auditor's copy, links the underlying finding, opens a compliance issue; contraventions only, no editorial fields.

**FR-P10-56 CARO 2020 clause packs.** Applicability (CARO applies to companies except banks, insurers, s.8 companies, OPCs and small companies, and private companies meeting the exemption tests [VERIFY exemption criteria]); clauses 3(i)–3(xxi) each with data pack (from P11 accounting bridge, P06 registers, P04 compliance, P12 fraud register), auditor remark field, lineage. NBFC-specific 3(xvi)(a)–(d) (registration under s.45-IA, NBFI activity without CoR, core investment company status, number of CICs in group) with Principal Business Criteria computation.

**FR-P10-57 Rule 11(g) evidence.** For tenants on Finbyx, retrieve the Finbyx AC7.3 Rule 11(g) evidence pack by reference; for tenants on Tally or other software, an evidence checklist (software inventory; audit-trail enabled throughout the year — e.g., TallyPrime "Edit Log" edition/configuration [VERIFY]; database-level change logging; vendor SOC reports; exception register) per ICAI Implementation Guide (Revised Jan 2024). LDC's own audit trail (for records LDC keeps) is evidenced by P00 seals.

**FR-P10-58 Branch-coverage calculator (NBFC SA para 13 [VERIFY]).** Top 20 branches, or top 20% where fewer than 100 branches, by outstanding advances, covering ≥ 15% of gross advances; extends until coverage met; signed selection record (data from P11 import or Finbyx).

**FR-P10-59 LFAR support (banks).** LFAR question bank (central and branch) from the ICAI Guidance Note on Audit of Banks (2026 Edition) [VERIFY current RBI LFAR format]; each question links to evidence; ACB submission tracking; bank forwards LFAR with Board views to RBI within the RBI timeline [VERIFY].

### 4J. Secretarial audit and Secretarial Standards checks

**FR-P10-60 Applicability.** s.204 resolver from paid-up capital, turnover, bank/PFI borrowings and listing (Rule 9(1); thresholds measured on the last date of the latest audited financial statements); LODR Reg 24A for listed entities and material unlisted Indian subsidiaries; optional internal review for others.

**FR-P10-61 Secretarial auditor eligibility, tenure and prohibited services.** Peer-review certificate for listed engagements; Reg 24A tenure: individual one term of 5 years, firm up to two terms of 5 years, 5-year cooling-off (extending to firms with common partners), casual vacancy filled within 3 months, tenure before 31 Mar 2025 ignored; prohibited services (internal audit, design of compliance/IS/policy systems, investment advice, investment banking, outsourced compliance or record-keeping, management services to the entity, holding company or subsidiaries) [LAW: LODR Reg 24A as substituted 12 Dec 2024; VERIFY exact list]. **Group rule [REC]:** where LawDocsComply or any Infrabyx entity implements compliance systems or provides retainer compliance services (P21/P22) to a listed tenant, an Infrabyx-linked PCS cannot be its secretarial auditor — the check reads the Service Delivery Console engagement register and the Operations Hub group register. CSAS-1 engagement checks (previous auditor communication and waiting period; annual engagement caps) [ICSI; VERIFY in Revised Edition 2026].

**FR-P10-62 Law-wise checklists.** CA13 and rules; SEBI regulations (LODR, PIT, SAST, ICDR, NCS/debt listing, DP, BRSR) where applicable; FEMA where applicable; RBI Act Chapter IIIB and NBFC Directions or other sector laws "specifically applicable" (pulled from P04 register); SS-1 and SS-2 (mandatory under CA13 s.118(10)); SS-3 and SS-4 where adopted [VERIFY status]. Evidence comes from P06 (directors and KMP, meetings, minutes, registers, MCA filings, LODR filings) through links — nothing is re-keyed.

**FR-P10-63 Automated SS-1 and SS-2 checks (per meeting).** Notice period and mode; agenda notes; quorum incl. interested-director exclusion; electronic attendance declarations; minutes circulation (draft within 15 days), signing (within 30 days), entry and pagination; general-meeting notice, place, e-voting and scrutiniser timelines (revised SS-1/SS-2 effective 1 Apr 2024) [ICSI; VERIFY each clock against the standard text]. Each check is an `ss_compliance_check` (result, evidence link, exception text) and failed checks appear as draft observations.

**FR-P10-64 Opinion and reports (CSAS-3).** Unmodified or modified opinion; observations; MR-3 rendered from the engagement; Annual Secretarial Compliance Report (listed) due within 60 days of FY end with the observations and action-taken table carried from the prior year; file collated within 45 days and retained 8 years [CSAS-2; VERIFY].

### 4K. IS audit, ITGC and VAPT

**FR-P10-65 IS audit framework.** IS audit policy (mandate, universe, periodicity, reporting; reviewed annually), ACB-approved framework where required, resourcing (internal; external IS auditors only where skills are lacking, reason and ACB approval recorded), timing preferably before the statutory audit (planner warns), findings to Board/ACB/ITSC, management accountability per finding, CAATs and continuous auditing [CYB 2026 — VERIFY paragraph numbers; Finbyx v1.5 AU4.1 cites the 2026 CYB paras 47–58 and 149–154].

**FR-P10-66 Scope library.** Control families mapped to CYB, SEBI CSCRF (for SEBI REs: governance, identify, protect, detect, respond, recover; cyber audit and cyber capability index where applicable [VERIFY]), IRDAI guidelines, IFSCA cyber guidelines [VERIFY], CERT-In Directions 2022 (log retention 180 days in India, 6-hour incident reporting, NTP sync [LAW]), ISO/IEC 27001:2022 Annex A (93 controls) via P12 mapping, DPDP Rules r.6 security safeguards.

**FR-P10-67 ITGC library.** Access to programs and data, program change, computer operations, program development; per control: design, owner, frequency, test steps, population query, evidence pattern; key reports (SoD conflicts, access-review completion, change log, configuration changes, audit-trail gaps, backup/restore logs with India location).

**FR-P10-68 VAPT tracker.** `vapt_engagement` and `vulnerability_finding` (CVE/CWE, CVSS base/environmental, asset from P12 inventory, severity band: Critical ≥ 9.0 or CISA KEV-listed, High 7.0–8.9, Medium 4.0–6.9, Low < 4.0; first seen; due date by SLA; fix evidence; retest; recurrence flag). Cadence engine: next VA = last VA + 6 months, next PT = last PT + 12 months for critical/DMZ systems (Locked for ML+ NBFC tenants; Tenant tier otherwise); major change creates pre-production VAPT task. Default SLAs Critical 15, High 30, Medium 90, Low 180 days (Tenant tier); recurrence after closure becomes a High audit finding. Imports: CSV, SARIF, Nessus XML, OpenVAS XML, Burp XML [REC]. LDC's own platform VAPT items appear read-only as `provider_vapt` (P24).

### 4L. Concurrent audit

**FR-P10-69 Concurrent-audit units and cycles.** Units (branches, treasury, CPCs, digital channels); monthly or fortnightly cycles; checklists by CB-CA minimum areas; all CPCs mandatory for commercial banks; HIA sets scope with ACB approval; random transaction testing on a sufficiently large sample (CB-CA).

**FR-P10-70 Transaction queue.** Feed of high-value or exception transactions per unit (from Finbyx core events, P11 imports or bank CBS extracts by SFTP): high-value disbursements, rate overrides, waivers, reversals, user-limit breaches, manual journals, back-dated entries, forex deals, SWIFT messages without matching CBS entries [REC]. Each item: "reviewed — no exception" (`N`) or raise finding (`F`); bulk clear of low-value items with a sampling note.

**FR-P10-71 Concurrent-auditor rules.** Tenure: external auditor continuous tenure ≤ 5 years with the bank; no auditor on one branch/unit > 3 years; retired staff ≤ 70 years; a CA firm whose partner is on the bank's Board cannot be appointed (CB-CA); conflict rules with statutory audit (NBFC SA para 18; bank SCA directions [VERIFY]). Rectification: minor on the spot; major to HO/controlling office immediately; fraud immediately to IA, CVO and branch manager (unless involved). Quarterly key-findings report and zone-wise findings to ACB; annual ACB review of effectiveness and auditor performance; serious lapses by external auditors → hearing, cancellation, report to ACB, RBI and ICAI (CB-CA).

### 4M. Specialised and other audit types

**FR-P10-72 Stock and receivables audit.** For lender tenants: borrower stock statements (P11 import or Udofin/Finbyx by reference), drawing-power recomputation against margin and ageing rules from the sanction terms, physical verification checklist with geo-tagged photos (P07 upload with EXIF retention), insurance adequacy, receivables ageing and debtor confirmation sampling; report to credit/risk with DP shortfall alert.

**FR-P10-73 Data-protection audit.** Pulls the P12 ROPA, consent records, notices, DPIAs, rights-request logs, breach register, processor contracts and cross-border transfer register; checklist per DPDP Act ss.4–17 and Rules 2025 (notice r.3, consent manager r.4, security safeguards r.6, breach intimation r.7, retention r.8 and Third Schedule, children's data r.10–12, SDF duties r.13) [VERIFY rule numbering against G.S.R. 846(E)]; GDPR Arts. 5–49 overlay when profiled; outputs an SDF annual audit report draft for the independent data auditor's signature.

**FR-P10-74 Regulatory inspection management.** Inspection record (regulator, type — RBS/ISE/thematic/snap, team, period, reference date), information-request register (request, owner, due, response pack hash, submitted-by and channel), inspection room (D-12 grant), draft inspection findings import (RBI RAR/IR, Risk Mitigation Plan, MAP; SEBI inspection report; IRDAI; IFSCA; Registrar), compliance submission tracker (submitted by the RE on DAKSH or the regulator's channel — LDC records reference and hash only), MAP items as P04 obligations with due dates; penalty and enforcement linkage to P04 consequences. Supervisor correspondence never leaves the tenant's sealed `REGULATOR_CORRESPONDENCE` class. *(v1.1, D-41)* The inspection record, information requests, observations, MAP/RMP items and compliance submissions are **owned by the P26 regulator-engagement register** (`lit.reg_engagements`, `lit.reg_rfis`, `lit.reg_observations`); P10 reads and annotates them through the P26 API, keeps the inspection room (FR-P10-86), rolls observations into the ATR register (FR-P10-48) and the ACB pack, and runs closure-verification tests (FR-P10-97). The P10 tables `inspection`, `inspection_request`, `inspection_map_item` become read projections of the P26 records (expand-contract migration, NN-11).

**FR-P10-75 Special investigation.** Restricted engagement (sealed workpapers, named-only access, no AI unless the HIA enables per engagement), evidence chain-of-custody (who, when, hash, location), interview notes with consent text, hand-off to the fraud function and to legal (P26 legal-matter register; *v1.1*) — the investigation never classifies fraud.

**FR-P10-76 Tax-audit support.** Clause-wise data pack (P11 accounting bridge): under the Income-tax Act 2025 tax-audit provision and form (s.63 / Form 26 as researched; [VERIFY]) for tax year 2026-27 onwards and 1961 Act s.44AB / Form 3CD for earlier years [VERIFY Form 26 clause list]; auditor workspace with PBC and query log.

**FR-P10-77 Co-operative statutory audit support.** Auditor from the Registrar's panel or as the Act provides; audit classification (A/B/C/D where the State uses it [VERIFY per State]); audit memo import; rectification report within the statutory period (e.g., Maharashtra s.82 [VERIFY]) tracked as ATR; for multi-state societies, auditor from the Central Registrar panel and CAG-style requirements for large societies under MSCS (Amendment) Act 2023 [VERIFY]; outputs to P16 society governance.

**FR-P10-78 Compliance testing (second line).** The compliance function (CMP for ML/UL NBFCs: testing of compliance, annual compliance risk assessment, reporting to Board) records tests in the same engine with `line_of_defence = 2`; results publish `ControlTestResultPublished`; findings follow the same lifecycle but route to the CCO; internal audit can rely on or re-perform (SIA 240-style reliance record).


### 4R. v1.1 enhancements — less audit admin, deeper second-line testing *(v1.1)*

**Faster external and internal audits (IMP-083 – IMP-090)**

**FR-P10-89 — Scope-level sharing (IMP-083).** Instead of sharing files one by one, the HIA or CFO shares an **engagement scope** once: legal entities, periods, instruments/checkpoint sets, registers, return packages and document classes. All evidence that falls inside the scope is visible in the auditor room for the grant period (≤ 90 days, D-12); new evidence entering the scope during the grant appears automatically with a "new" badge; sealed and privileged classes are excluded unless named explicitly. Journey J-15: share a statutory-audit scope in ≤ 4 clicks.

**FR-P10-90 — Request-list generator and auto-chasing (IMP-084).** From the scope, last year's PBC list and the risk assessment, the system generates the request list (PBC items with owner, due date and evidence pattern) in under a minute; owners receive grouped requests; reminders follow `aud.pbc.reminder_ladder`; the status board shows each item as Requested › Linked › Uploaded › Accepted › Query raised. The auditor accepts or rejects each item; rejection reopens it with a comment.

**FR-P10-91 — Auto-link existing evidence (IMP-085).** For every request, the matcher proposes evidence already held in LDC (compliance-instance evidence, policies, minutes, registers, returns, reconciliations) by evidence pattern, period and hash; the owner accepts a suggestion in one click instead of re-uploading. Re-use is recorded, so the same file is never stored twice.

**FR-P10-92 — AI plan and scoping drafts (IMP-086, IMP-087).** VA-07 drafts: the annual audit-plan proposal from the risk register, prior findings, regulatory requirements (RBIA coverage rules) and resource capacity, with the rationale for each unit's frequency; and a scoping memo per engagement (objectives, risks, processes, key controls, work steps, data requests). Both are labelled drafts; the HIA edits and approves; the plan still needs ACB approval (§4C).

**FR-P10-93 — Cross-engagement summary (IMP-088).** For each ACB meeting, a summary across engagements issued since the last meeting: themes (root-cause categories, recurring controls, units), repeat findings, overdue actions, emerging risks, with links to the underlying findings; VA-07 drafts the narrative, figures are bound values (NN-37).

**FR-P10-94 — Findings ↔ compliance issues (IMP-089).** Issuing a finding that relates to a regulatory checkpoint creates or links a P04 compliance issue and marks the affected checkpoints "audit observation open"; closure of the compliance issue offers re-test to the auditor; closure of the finding updates the issue. Neither side closes the other automatically without the owner's action.

**FR-P10-95 — Workpaper sign-off and lock (IMP-090).** Each workpaper has preparer and reviewer sign-offs (different persons, NN-05), review notes that must be cleared before reviewer sign-off, and a lock on reviewer sign-off; post-lock edits create a new version with reason and re-review. Sign-off status is visible on the engagement dashboard and in the file index.

**Compliance-testing programme — second line (extends FR-P10-78; owner's methodology defaults, Tenant tier, not law)**

**FR-P10-96 — Testing universe and risk scoring.** The compliance function's testing universe lists every obligation/control area (from P03/P04 checkpoints grouped by instrument, process and department). Each area is scored on: inherent regulatory risk (penalty and consequence from column Q/R), breach frequency in the industry (content tag), recency of regulatory change (P05), business materiality (volumes/exposures from Finbyx/P11), and control maturity (last test result, automation level). The score sets the testing cycle: High at least annually, Medium every 18 months, Low every 24–36 months; the annual testing plan is approved by the CCO and reported to the Board/committee (Compliance Function Directions 2026, RBI/DoS/2026-27/460 **[VERIFY paras]**).

**FR-P10-97 — Triggered testing.** Tests are created outside the plan on: a material breach or complaint cluster (P14), closure of a regulatory inspection observation (P26 — closure verification before reporting closure to the regulator), a whistle-blower case (P26 sealed link, counts only), a regulatory change (P05) affecting a High area, and a business change (new product, branch, system). Each triggered test cites its trigger.

**FR-P10-98 — Five-phase method.** Plan (objective, criteria from the checkpoint and policy clause, population, period) → walkthrough (process narrative, key controls identified) → design effectiveness → operating effectiveness → conclude (rating, issues, report). Test types: inquiry, observation, inspection, re-performance, CAAT/data analytics. Templates per instrument family are seeded from Part-2 column V (control activity) and U (evidence).

**FR-P10-99 — Sampling table and tolerable deviation.** Default second-line sampling: continuous/automated controls — 100% via CCM; manual high-frequency (daily/multiple per day) — 25; medium-frequency (weekly/monthly) — 12; low-frequency (quarterly) — 5; annual — 100%. Tolerable deviation: ≤ 5% for High-risk areas, ≤ 10% Medium, ≤ 15% Low; on a deviation the sample expands by 25% before concluding. All values are tenant-configurable (`cmp.testing.*`) and the sample is drawn by the P10 sampling engine (seed recorded, reproducible; NN-22).

**FR-P10-100 — Root cause and issues.** Every exception gets a root-cause analysis (5 Whys guide) with category (people, process, technology, documentation, knowledge, vendor, external) and scope (isolated vs systemic). Issue SLAs by severity: Critical 30 days, High 60, Medium 90, Low 180 (tenant-configurable); closure requires re-test evidence. Critical findings are escalated within 5 business days to the MD/CEO, the Audit Committee chair and the Board chair, and recorded for the next Board pack (P06 agenda auto-suggest).

**FR-P10-101 — Reliance and coordination.** Second-line tests can be relied on by internal audit (reliance record: competence, objectivity, re-performance sample) and shared with the statutory auditor where the tenant chooses; duplicate testing is shown on a coverage map (first/second/third line per area) to avoid over- and under-testing.

**FR-P10-102 — Links to risk and capital.** Testing results feed the compliance-risk assessment (P08 RCSA and KRIs: exceptions rate, overdue issues) and, for ICAAP tenants, the compliance-risk add-on inputs (P09); loss events from compliance failures link to P08 loss data.

**FR-P10-103 — Programme QA.** Annual internal-audit review of the testing programme and an external quality review at least every three years (owner's methodology), recorded as an engagement of type `QA_REVIEW` with findings.

**Continuous control monitoring and automation**

**FR-P10-104 — CCM tests in the workpaper.** Automated checkpoint tests (P04 IMP-015 – IMP-018) and CCM scripts run by the Control Monitor agent (VA-14) over Finbyx/Udofin/connected data (e.g., KYC completeness, sanctions-screening hits cleared within SLA, KFS issued before execution, interest-rate band breaches, contact-hour breaches) appear in the engagement as test populations with full results, exceptions and lineage. Auditors can rely on them after validating the script version (recorded) or re-perform. VA-14 opens issues on failures as drafts; ratings remain human (NN-47).

**FR-P10-105 — Audit Assistant (VA-07).** Default autonomy L1: drafts test steps, sampling notes, workpaper summaries, finding text (condition, criteria, cause, effect, recommendation), report sections and scoping memos; it can propose but never issue a finding, choose a rating, accept a risk, sign, close or share (NN-14, NN-47, NN-50). In independence-sensitive engagements (special investigation, statutory audit rooms operated by external auditors) it runs at L0 unless the HIA or the external auditor enables it for that engagement. It never drafts management responses inside an auditor's run (Appendix K VG-24).

**Group and global**

**FR-P10-106 — Group audits and foreign subsidiaries.** The audit universe can include units of foreign subsidiaries held in global entity management (`gem`, P25); their local statutory audit calendar and auditor details come from the jurisdiction pack or tenant data; group internal-audit engagements run in the same engine with local-language evidence (official text retained, translation labelled, NN-54); findings roll up to the parent's Audit Committee with entity tags. Local auditor independence rules are captured as tenant data until a jurisdiction pack provides them.

**FR-P10-107 — Audit-trail (edit log) testing for Rule 3(1).** For companies required to use accounting software with an edit log (Companies (Accounts) Rules r.3(1) and the auditor's reporting under r.11(g) Audit and Auditors Rules), a test pack checks that the edit log was enabled throughout the year, not disabled, and retained, using evidence from the accounting bridge (P11) and vendor edit-log exports; exceptions feed the auditor room.

**FR-P10-108 — Audit calendar to Work Inbox.** Every audit milestone (plan approval, fieldwork window, PBC due dates, draft report, management response due, ACB meeting, ATR due) is a calendar item for the people involved (P04 calendar sync), and every pending action appears in their Work Inbox with one-click actions (upload, accept, respond, sign off).

### 4N. Report engine

**FR-P10-79 Base templates (Platform content, versioned).** RBIA unit report and annual summary (IAF para 35: objectives, scope, results, recommendations, action plans; risk rating and direction by unit); internal audit report (SIA 370; s.138); concurrent audit report (monthly/quarterly; CB-CA); IS audit report (CYB; CSCRF; ISO); ITGC/IFC support memo; MR-3 (Form MR-3 as prescribed); Annual Secretarial Compliance Report (Reg 24A format as prescribed by SEBI [VERIFY current format]); CARO clause pack; AUD Board report and exception report (paras 5–12); LFAR responses (banks); stock audit report; data-protection audit report; inspection response pack; QAIP report; ACB pack.

**FR-P10-80 Customisation with guardrails.** Tenant may add, remove, reorder narrative sections, annexures and exhibits; set rating scales and colours; scope and materiality statements; branding and language; distribution and sign-off path; entity-specific templates in a group. Mandatory legal sections and fields are Locked and visibly badged; removal attempts fail with the citation.

**FR-P10-81 Production.** Assemble (findings, ratings, scope, responses from the engagement snapshot) → select template (type × entity × tenant customisation) → draft (Vidhi may draft narrative from findings, never ratings; NN-14) → maker-checker review with annotations → issue (eSign by authorised signatories via P07; DSC where a regulator form requires [VERIFY]) → render DOCX and PDF/A → distribute (auditee, ACB via P06 agenda, ITSC for system audits) → archive with template version, findings snapshot hash and approvals so the report regenerates byte-identically.

**FR-P10-82 Submission timelines.** Scheduler creates generation tasks ahead of: ACB meeting dates (P06 calendar), DNBS10, Annual Secretarial Compliance Report (60 days), MR-3 (with the Board's report), LFAR (bank timelines), concurrent audit quarterly ACB review, inspection response deadlines, SDF annual audit. Overdue items flag to the ACB pack.

### 4O. Dashboards and ACB pack

**FR-P10-83 Dashboards (role-specific, widget-configurable per P02/Appendix C).**
- **Internal Auditor / HIA:** plan progress (planned vs completed by quarter), coverage of mandatory units, engagements by state, budget vs actual days, open findings by rating and age, repeat findings, overdue ATR, retest queue, CAAT exceptions trend, IS/VAPT SLA breaches, QAIP status, upcoming ACB items.
- **Audit Committee:** risk heatmap of the universe with trend arrows, plan status, High/Critical open findings with owner and age, management disagreements, risk acceptances expiring, statutory-auditor status (PBC completion, AUD checklist, DNBS10), secretarial audit status, regulator inspection MAP compliance, concurrent audit summary, in-camera meetings held.
- **CFO:** statutory-audit PBC progress, query ageing, CARO and AUD readiness, Rule 11(g) pack status, tax-audit support status.
- **CISO / ITSC:** IS audit findings, VAPT open by severity/age, recurring vulnerabilities, continuous-audit exceptions.
- **CS:** secretarial audit checks failed by meeting, auditor tenure alerts, MR-3 status.
- **Board:** annual consolidated major-risk view (IAF para 11), audit opinion summary.

**FR-P10-84 ACB pack builder.** Select meeting (P06) → pack sections (plan status, reports issued since last meeting, High/Medium pending (IAF para 37), ATR with comparison to previous pack, risk acceptances, disagreements, VAPT, concurrent audit, secretarial, statutory audit, inspection MAP, QAIP, in-camera tracker) → preview → freeze with hash → attach to the P06 agenda as a board paper → after the meeting, ACB decisions recorded in P06 minutes write back to findings (e.g., extension noted, risk acceptance noted) with minute reference.

### 4P. External-access rooms

**FR-P10-85 Engagement rooms.** For each external engagement an auditor room shows: engagement letter, PBC portal, query log, read-only datasets in scope, internal-audit reports the tenant chooses to share (SA 610), upload area for management letters and reports. Provisioned only through a P01 grant (basis code, scope, PII level, export level, validity ≤ 90 days, maker-checker approval; D-12; Ecosystem Spec §4.7); sessions end ≤ 60 s after expiry/revocation; daily activity report; watermarked, capped exports.

**FR-P10-86 Inspection room.** Pre-loaded for a supervisory inspection: reference-date snapshot of compliance register and evidence, returns filed with acknowledgements (P11), policies and versions (P07), minutes index (P06), risk and capital metrics with lineage (P08/P09), fraud and complaint registers (counts and masked lists), large exposures (by reference to Finbyx/P11), related-party register, audit reports and ATR. Supervisor information requests are logged and answered through the tenant's official channel (D-13).

**FR-P10-87 Provider-assurance room.** For auditors of the tenant auditing LawDocsComply as a service provider: LDC's SOC reports (once issued), VAPT summaries, BCP/DR evidence, sub-processor list, policy summaries — published by P24; never asserted as tenant compliance (NN-19).

### 4Q. Exports

**FR-P10-88 Export.** Per engagement and per FY, using the Appendix M §M.3 folder `10 Audits and Inspections/` (X-27): `<Audit type folder>/<FY>/<Engagement name> - <Period>/` (audit type folders as in Appendix M: `Internal Audit`, `Risk Based Internal Audit`, `Concurrent Audit`, `IS Audit`, `Secretarial Audit`, `Statutory Audit support`, `Regulatory Inspections`) containing `01 Planning/` (engagement letter, scope, risk assessment, programme), `02 Fieldwork/` (workpapers as DOCX/XLSX/PDF by area, samples, original evidence files and `evidence_index.xlsx` with hashes and source references), `03 Findings.xlsx`, `04 Management responses.xlsx` (with ATR), `05 Report - FINAL <date>.pdf / .docx` (PDF/A), `06 Follow-up and closure.xlsx`; engagement identifiers, hashes and versions are in the package manifest, not in folder names, and a BSA 2023 s.63 certificate template (NN-09, NN-10; Appendix M). Universe, plan, methodology versions and ACB packs export under `10 Audits and Inspections/Audit universe and plans/`; the cross-audit `Findings tracker - all audits.xlsx` sits at the folder root. Exports respect sealed classes (excluded unless the custodian approves).


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P10-X01 — Executive reporting through P28.** The cross-engagement executive summary (IMP-088) and repeat-finding analysis (IMP-057) are rendered as P28 pack sections MIS-AUD-02 and MIS-AUD-03; figures come only from the P28 semantic layer (NN-37).

**FR-P10-X02 — Accounting edit-log evidence.** For the Companies (Accounts) Rules r.3(1) edit-log test (FR-P10-107), P11 supplies the accounting-software edit-log evidence extracted from Tally or the client's ERP; P10 records the test result and the auditor's conclusion.

---

## 5. Workflows and state machines

Every transition is a server-side command (`POST /v1/audit/<object>/{id}/commands/<command>`) with idempotency key `(object_id, version, command)`, writes a ledger event, emits the domain event where listed and returns 409 `LDC-AUD-409` from an invalid state. Timers are settings (§9).

### 5.1 Engagement

| State | Entry condition | Owner | Default timer | Exits |
|---|---|---|---|---|
| `PLANNED` | Plan line published or ad hoc request approved | HIA | Planned quarter | → `SCOPED`; → `CANCELLED` (reason; ACB noting if the unit is past its policy maximum) |
| `SCOPED` | Objectives, scope, criteria, team, budget, methodology version recorded | Engagement lead | 10 working days before fieldwork | → `APPROVED` (HIA); rejection returns with comments |
| `APPROVED` | HIA approval; engagement letter eSigned for external engagements; `AuditEngagementOpened` emitted | HIA | — | → `FIELDWORK` only when every member's independence declaration is on file |
| `FIELDWORK` | Opening meeting recorded | Lead | Budget days (alerts at 80% and 100%) | → `DRAFT_REPORT`; → `SCOPED` (re-scope with HIA approval, workpapers kept); → `ON_HOLD` |
| `ON_HOLD` | Scope limitation, auditee unavailable, data outage, fraud signal | Lead | 30 days then HIA escalation | Back to prior state; persistent limitation reported in final report and to ACB |
| `DRAFT_REPORT` | All workpapers reviewed, no open review notes | Lead, reviewer | 10 working days | → `MANAGEMENT_RESPONSE` after closing meeting |
| `MANAGEMENT_RESPONSE` | Draft shared | Auditee owner | 15 working days; reminders T−5, T−1; escalation T+1 | → `FINAL_REPORT`; missing response recorded "no response" |
| `FINAL_REPORT` | Responses incorporated, rating confirmed | HIA | 5 working days | → `ISSUED` on eSign; → `DRAFT_REPORT` |
| `ISSUED` | Report hash stored; distribution logged; ATR items and P04 tasks created | HIA | — | → `FOLLOW_UP` |
| `FOLLOW_UP` | ≥ 1 finding open | Finding owners | Finding due dates | → `CLOSED` when all findings `CLOSED`, `RISK_ACCEPTED` or `WITHDRAWN` |
| `CLOSED` | File assembled and locked | HIA | — | Reopen only as addendum (never edits the file) |

Type overlays: `SECRETARIAL` inserts `CHECKLISTS_RUN → OPINION_DRAFTED → SIGNED` between `FIELDWORK` and `ISSUED`; `STATUTORY_SUPPORT` uses `PBC_OPEN → FIELDWORK_SUPPORT → REPORT_SIGNED → POST_AUDIT_FILINGS (DNBS10, AOC-4 inputs) → CLOSED`; `REGULATORY_INSPECTION` uses `NOTIFIED → ROOM_PROVISIONED → ON_SITE/OFF_SITE → DRAFT_FINDINGS_RECEIVED → RESPONSE_SUBMITTED → FINAL_REPORT_RECEIVED → MAP_TRACKING → CLOSED`.

### 5.2 Finding

| State | Entry | Owner | Timer | Exits |
|---|---|---|---|---|
| `DRAFT` | Condition, criteria, cause, effect, rating, evidence | Preparer | — | → `DISCUSSED` (reviewer approval) |
| `DISCUSSED` | Closing meeting; auditee comments | Lead | — | Re-rate with reason; → `ISSUED` with report; → `WITHDRAWN` (factual error, reviewer approval) |
| `ISSUED` | `AuditFindingRaised` emitted | Auditee owner | Response 15 working days | → `RESPONSE_RECEIVED`; overdue escalates |
| `RESPONSE_RECEIVED` | Agree / partly / disagree with reasons | Lead | 5 working days to accept | Disagreement → HIA decides (ACB sees both); → `ACTION_AGREED` |
| `ACTION_AGREED` | Action items with owners, dates, evidence required | Owner | Rating SLA | → `IN_REMEDIATION` |
| `IN_REMEDIATION` | Work started | Action owners | T−7, T−1, daily overdue | Extension (rules §4H); → `CLOSURE_SUBMITTED`; → `RISK_ACCEPTED` |
| `CLOSURE_SUBMITTED` | Evidence per action + attestation | Owner | Auditor pick-up 10 working days | Incomplete → returned (clock continues) |
| `RETEST` | Independent retester assigned | Retester | 10 working days | Pass → `CLOSED` (`AuditFindingClosed`); fail → `REOPENED` |
| `REOPENED` | Retest fail or recurrence | Owner | ≤ original SLA | Repeat counter +1; → `IN_REMEDIATION` |
| `RISK_ACCEPTED` | Authority, rationale, compensating controls, expiry ≤ 12 months | Risk acceptor | Reminder 30 days before expiry | Renew or → `IN_REMEDIATION`; never for regulatory breach without CCO |
| `WITHDRAWN` | Factual error confirmed | Reviewer | — | Terminal |

### 5.3 Plan and methodology

`DRAFT → HIA_SUBMITTED → MGMT_NOTED (optional) → ACB_APPROVED (minute ref) → PUBLISHED`; amendments `AMENDMENT_DRAFT → ACB_NOTED → PUBLISHED (v n+1)`. Methodology: `DRAFT → PEER_REVIEWED → ACB_APPROVED → EFFECTIVE (date) → SUPERSEDED`.

### 5.4 External grant (audit rooms; shared with P01)

`REQUESTED → BASIS_RECORDED → SCOPE_DEFINED → TENANT_APPROVED (maker ≠ checker; second approval for FULL PII/export) → PROVISIONED → ACTIVE ⇄ EXTENDED → EXPIRED | REVOKED → ARCHIVED` (Ecosystem Spec §4.7; validity ≤ 90 days).

### 5.5 VAPT finding

`OPEN → ASSIGNED → FIX_IN_PROGRESS → FIX_SUBMITTED → RETEST → CLOSED | REOPENED (recurrence → High audit finding) | RISK_ACCEPTED (expiry)`.

### 5.6 Sample run (pseudo-code)

```text
snapshot   = freeze(population_query, as_of)          # stores row_count, control_total, population_hash
assert snapshot.population_hash == stored_hash         # on re-run
rng        = PRNG(seed)                                 # seed stored with the sample
items      = method(snapshot, params, rng)              # random | systematic | stratified | MUS | attribute | topN | judgemental
store(sample_id, method, params, seed, snapshot_id, items_hash)
# Evaluation
for item in items: record(result ∈ {NO_EXCEPTION, DEVIATION, MISSTATEMENT(amount)}, evidence_links)
projected = evaluate(method, results)                   # MUS projection or upper deviation limit
conclusion = auditor_input(required=true)               # never AI-generated
```

---

## 6. Screens and UX

Menu root: **Audit** (tenant app `apps/web`), visible to roles in §3. All lists support saved views, column chooser, bulk actions with preview and undo window (Appendix C patterns), CSV/XLSX export within permission, and `i` help keys `help.aud.*`.

| Screen ID | Name | Menu path | Key elements | Roles |
|---|---|---|---|---|
| SCR-AUD-01 | Audit home | Audit › Home | Role dashboard (§4O), next-best actions ("3 findings due this week", "Plan Q3 has capacity gap 12 days") | All audit roles |
| SCR-AUD-02 | Universe | Audit › Universe | Unit list (filters: type, owner, risk, due, overdue, audited_in), unit detail with coverage clock and change-task queue; "Seed from masters" empty state | HIA, IA (edit); ACB (read) |
| SCR-AUD-03 | Risk assessment | Audit › Risk assessment | Parameter-by-parameter wizard with pre-fill and source link; heatmap with trend arrows; "why blocked" inline | IA, HIA |
| SCR-AUD-04 | Plan builder | Audit › Plan | Ranked list, capacity bars by skill, Gantt by quarter, deferred list, versions, amendment queue | HIA (edit), ACB (approve) |
| SCR-AUD-05 | Methodology | Audit › Methodology | Version list, diff, locked badges | HIA, ACB |
| SCR-AUD-06 | Engagements | Audit › Engagements | Kanban by state and list; create wizard | IA team; HIA |
| SCR-AUD-07 | Engagement detail | Audit › Engagements › {id} | Tabs: Scope, Team, Programme, Workpapers, Samples, Analytics, Evidence, Requests, Findings, Report, Log | Team, HIA |
| SCR-AUD-08 | Workpaper editor | … › Workpapers › {ref} | Split view live vs pinned; review notes; eSign sign-off; shortcuts | Preparer, reviewer |
| SCR-AUD-09 | Sampling | … › Samples | Method picker, size calculator, seed, population hash, evaluation | IA |
| SCR-AUD-10 | Analytics (CAAT) library | Audit › Analytics | Test library, run history, exception queue, schedules | IA, IS auditors |
| SCR-AUD-11 | Evidence vault | Audit › Evidence | Search, verify file, integrity report | IA; external via room |
| SCR-AUD-12 | Findings | Audit › Findings | Saved views (My open, Overdue, High/Critical, Repeat, Regulatory breach, Finbyx-owned), detail with timeline | IA, owners (own items), ACB (read) |
| SCR-AUD-13 | Retest queue | Audit › Findings › Retest | Packs awaiting retest with SLA | Retesters |
| SCR-AUD-14 | ATR | Audit › ATR | Register by source, ageing, comparison | HIA, CS; ACB read |
| SCR-AUD-15 | ACB pack builder | Audit › Committee packs | Section picker, preview, freeze, send to P06 agenda | HIA, CS |
| SCR-AUD-16 | HIA and QAIP | Audit › Function | HIA register, in-camera tracker, QAIP | HIA, CS, ACB chair |
| SCR-AUD-17 | Statutory auditors | Audit › Statutory › Auditors | Firm register, Form B eligibility, tenure, non-audit service log, Form A | CFO office, CS, ACB |
| SCR-AUD-18 | PBC tracker | Audit › Statutory › PBC | PBC list by owner/status, query log | CFO office; auditors (room) |
| SCR-AUD-19 | Auditor's Report Directions & CARO | Audit › Statutory › Checklists | AUD para 6–9 runs, DNBS10 timer, exception register, CARO clauses | Auditors, CFO, CCO |
| SCR-AUD-20 | Branch coverage | Audit › Statutory › Branch coverage | Calculator, selection record | CFO, auditors |
| SCR-AUD-21 | Secretarial audit | Audit › Secretarial | Engagements, SS check results per meeting, auditor register and tenure, MR-3/ASCR | CS, secretarial auditor |
| SCR-AUD-22 | IS audit & ITGC | Audit › IS & IT | Scope library, ITGC tests, continuous-audit exceptions | IS auditors, CISO (read) |
| SCR-AUD-23 | VAPT | Audit › VAPT | Engagements, vulnerabilities (filters severity/asset/SLA/recurring/provider), import | CISO office, IA |
| SCR-AUD-24 | Concurrent audit | Audit › Concurrent | Unit queue (daily), monthly report, tenure tracker | Concurrent auditors |
| SCR-AUD-25 | Inspections | Audit › Inspections | Inspection record, information requests, MAP tracker, room status | CCO, HIA |
| SCR-AUD-26 | Stock audit | Audit › Stock audit | Borrower list, DP recomputation, field checklist | Credit/risk, auditors |
| SCR-AUD-27 | External access (audit) | Audit › External access | Requests, grants, activity reports (links to P01) | CCO, CISO, CFO |
| SCR-AUD-28 | Auditor room | `apps/web` external landing | Engagement letter, PBC, datasets, uploads, export centre (watermarked) | External auditors |
| SCR-AUD-29 | Inspection room | `apps/web` external landing | Snapshot, returns with lineage, registers, requests | `ten_supervisor_view` |
| SCR-AUD-30 | Report studio | … › Report | Template, sections (locked badges), Vidhi draft panel, annotations, issue | Lead, HIA |
| SCR-AUD-31 *(v1.1)* | Share scope wizard | Audit › Engagement › Share | Pick entities, periods, checkpoint sets, registers, document classes; preview of what the auditor will see; grant period | HIA, CFO |
| SCR-AUD-32 *(v1.1)* | Request list & chase board | Audit › Engagement › Requests | Generated PBC list; owner columns; status Kanban; reminder log; suggested evidence with accept buttons | HIA, auditee owners, external auditor |
| SCR-AUD-33 *(v1.1)* | Testing universe & plan | Compliance › Testing › Universe | Areas with scores and cycles; plan year grid; CCO approval | CCO, compliance testers |
| SCR-AUD-34 *(v1.1)* | Test workspace (5 phases) | Compliance › Testing › {test} | Stepper Plan › Walkthrough › Design › Operating › Conclude; sample panel; exceptions with RCA | Compliance testers |
| SCR-AUD-35 *(v1.1)* | CCM results | Audit › Continuous monitoring | Script runs, populations, exceptions, script versions, reliance status | HIA, CCO, CRO |
| SCR-AUD-36 *(v1.1)* | Coverage map | Audit › Assurance map | First/second/third-line coverage per area; gaps and overlaps | HIA, CCO, ACB |
| SCR-AUD-37 *(v1.1)* | ACB cross-engagement summary | Audit › ACB › Summary | Themes, repeat findings, overdue actions with links; VA-07 draft narrative | HIA, ACB members |

**Fewer-click patterns.** Engagement from plan line pre-fills scope, team and programme (one confirmation); "Raise finding" from a CAAT exception or sample deviation pre-fills condition, criteria and evidence; bulk-assign owners; "Send all overdue reminders" with preview; command palette entries (`Ctrl/Cmd+K`: "new engagement", "open finding AUD-F-…", "freeze ACB pack"). **Accessibility:** heatmaps carry text labels and patterns, not colour alone; tables keyboard-navigable; workpaper diff announced to screen readers (NN-21).

**Empty and error states.** Universe empty → "Seed from masters (branches 42, departments 11, systems 18, outsourcing 9)"; plan blocked → lists exact missing items (ACB minute reference, overdue IA policy review); sign-off blocked → lists open review notes with links.

---

## 7. Backend design

### 7.1 Modules

`aud` (owner), reads `cmp`, `erm`, `gov`, `pol`, `dms`, `hr`, `dpc`, `tpr`, `ret`, `acc`, `int`; writes tasks via `wf`, issues via `cmp`, risk links via `erm`.

Shared packages (master OP-1, X-26): approvals, maker-checker, escalations and SLAs use `packages/workflow`; reminders, digests and the Work Inbox use `packages/notify`; calendar entries and external sync use `packages/calendar` (all owned by P04); settings via `packages/config` (P02); documents via `packages/docgen` and `packages/redline` (P07); AI via `packages/ai` (P17); exports via `packages/export` (P19). This phase builds no parallel implementation.

### 7.2 Tables (schema `aud`; all with `tenant_id`, `legal_entity_id`, RLS, `created_at`, `recorded_at`, `version`, ledger pointer)

| Table | Key columns |
|---|---|
| `audit_universe_unit` | id, unit_type, ref_type/ref_id (branch, dept, system, product…), owner_person_id, lod, mandatory_flag, audited_in, policy_max_interval_days, last_audit_end, last_rating, next_audit_due, status |
| `audit_risk_assessment` | id, unit_id, cycle, methodology_version_id, inherent_score, control_score, level, trend, basis_text, approved_by, approved_at |
| `audit_risk_parameter_value` | assessment_id, parameter_code, locked, prefill_value, prefill_source_ref, final_value, override_reason |
| `audit_plan`, `audit_plan_line` | plan: fy, version, state, acb_minute_ref; line: unit_id, quarter, scope_tier, days, skills, team, deferred_reason, external_system |
| `audit_methodology_version` | scales JSONB, weights, scope_mapping, sampling_tables, rating_slas, templates, locked_items, effective_from, acb_minute_ref |
| `audit_engagement` | id, type, owner_system, external_ref, plan_line_id, period_from/to, objectives, scope, exclusions, criteria_refs[], methodology_version_id, budget_days, state, confidentiality_class |
| `audit_team_member` | engagement_id, person_id, role, independence_declaration_id, cooling_check_result |
| `audit_programme`, `audit_step` | programme versioned; step: objective, criteria_ref, procedure, test_type, population_ref, evidence_pattern, sample_default, risk_ids[], control_ids[], obligation_ids[] |
| `audit_workpaper` | id, engagement_id, index_ref, step_id, content (structured + rich text), preparer, reviewer, signed_hash, state, locked_at |
| `audit_review_note` | workpaper_id, author, text, cleared_by, cleared_at |
| `audit_population`, `audit_sample`, `audit_sample_item` | population: query_ref, snapshot_ref, row_count, control_total, population_hash; sample: method, params, seed, items_hash; item: key, result, amount, evidence_link_ids |
| `analytic_test`, `analytic_run`, `analytic_exception` | test versioned; run: snapshot_ref, params, counts; exception: key, values (masked), disposition |
| `evidence_link` | source_system, source_type, source_id, source_version, snapshot_json, sha256, ledger_pos, drift_state |
| `audit_finding`, `audit_finding_version` | finding: engagement_id, current_version, state, rating, repeat_count, reg_breach_obligation_id, owner_person_id, owner_system; version: condition, criteria, cause_category, cause_text, effect, recommendation, financial_impact |
| `audit_management_response`, `audit_action_item` | response: agreement, reasons; action: owner, due_date, evidence_required, status, wf_task_id |
| `audit_extension`, `audit_risk_acceptance` | approver chain, reasons, expiry, acb_noting_ref |
| `audit_retest` | finding_id, retester_id, sample_id, result |
| `atr_item` | source_type, source_ref, finding_id?, observation, status, validation_state, ageing_bucket |
| `audit_report` | engagement_id, template_version, findings_snapshot_hash, docx_object, pdf_object, sha256, signatories, issued_at, distribution |
| `acb_pack` | meeting_id (P06), sections, frozen_hash, decisions_writeback |
| `hia_register`, `incamera_meeting`, `qaip_assessment` | as §4C.3 |
| `stat_auditor_firm`, `stat_auditor_assignment`, `stat_eligibility_check`, `non_audit_service_log` | Form B data, partners, tenure, cooling, cap counts |
| `pbc_item`, `pbc_query` | as §4I |
| `aud_directions_check_run`, `aud_directions_check_line` | para, result (FAV/UNFAV/QUAL), reasons, computation_ref |
| `exception_report_register`, `caro_clause_response`, `branch_coverage_selection` | as §4I |
| `sec_audit_engagement`, `ss_compliance_check`, `sec_auditor_register` | as §4J |
| `itgc_control`, `itgc_test`, `vapt_engagement`, `vulnerability_finding` | as §4K |
| `concurrent_unit`, `concurrent_queue_item`, `concurrent_auditor_tenure` | as §4L |
| `inspection`, `inspection_request`, `inspection_map_item` | as §4M — *(v1.1)* read projections of P26 `lit.reg_engagements`, `lit.reg_rfis`, `lit.reg_observations` (D-41) |
| `stock_audit`, `stock_audit_borrower`, `dp_computation` | as §4M |
| `share_scope` *(v1.1)* | engagement_id, entity_ids[], period, checkpoint_set_ids[], register_codes[], doc_classes[], excluded_classes[], grant_id |
| `pbc_request_list`, `pbc_reminder_log` *(v1.1)* | generated_from (scope, prior_year_list_id, risk_assessment_id), items; reminders sent |
| `evidence_match_suggestion` *(v1.1)* | pbc_item_id, candidate_document_version_id, score, state (PROPOSED, ACCEPTED, REJECTED) |
| `workpaper_signoff` *(v1.1)* | workpaper_id, version, preparer_id, prepared_at, reviewer_id, reviewed_at, review_notes_open, locked |
| `testing_universe_area`, `testing_area_score`, `testing_plan` *(v1.1)* | area (instrument/process/department), score components, cycle_months, plan year, CCO approval |
| `test_trigger` *(v1.1)* | test_id, trigger_type (BREACH, INSPECTION_CLOSURE, WHISTLEBLOWER, REG_CHANGE, BUSINESS_CHANGE), source_ref |
| `root_cause` *(v1.1)* | finding_id, category, scope (ISOLATED, SYSTEMIC), five_whys jsonb |
| `ccm_test_run` *(v1.1)* | script_id, script_version, population_ref, run_at, exceptions_count, result_ref, executed_by_agent (VA-14) |
| `finding_issue_link` *(v1.1)* | finding_id, cmp_issue_id, link_state |

### 7.3 APIs (REST, `/v1/audit/...`, OpenAPI 3.1; cursor pagination; `Idempotency-Key` on POST)

`GET/POST /universe-units`, `POST /universe-units/{id}/commands/{archive|merge}`; `POST /risk-assessments`, `POST /risk-assessments/{id}/commands/approve`; `GET/POST /plans`, `POST /plans/{id}/commands/{submit|approve|publish|amend}`; `GET/POST /engagements`, `POST /engagements/{id}/commands/{approve|start-fieldwork|hold|resume|draft-report|send-for-response|finalise|issue|close}`; `GET/POST /engagements/{id}/workpapers`, `POST /workpapers/{id}/commands/{submit-review|sign-off}`; `POST /populations` (freeze), `POST /samples`, `POST /samples/{id}/rerun` (must reproduce); `POST /analytic-tests/{id}/runs`; `POST /evidence-links`, `POST /engagements/{id}/commands/verify-file`; `GET/POST /findings`, `POST /findings/{id}/commands/{issue|respond|agree-actions|extend|submit-closure|assign-retest|retest-pass|retest-fail|accept-risk|withdraw|new-version}`; `GET /atr`; `POST /acb-packs`, `POST /acb-packs/{id}/commands/freeze`; `GET/POST /statutory/auditors`, `POST /statutory/eligibility-checks`, `POST /statutory/form-a`; `GET/POST /pbc-items`, `/pbc-queries`; `POST /aud-directions-runs`; `POST /caro-runs`; `POST /branch-coverage/calculate`; `POST /secretarial/ss-checks/run?meeting_id=`; `POST /vapt/imports` (multipart: CSV/SARIF/XML); `GET /concurrent/queue?unit=`; `POST /inspections`, `/inspection-requests`; `POST /evidence-requests` (to connected products via P18). Ecosystem inbound: webhook receiver for `audit` domain events (P18).

### 7.4 Domain events (CloudEvents; `source = urn:infrabyx:ldc:<tenantid>`)

Published to the ecosystem by `int` only, with Ecosystem Spec §6.21 names and types `in.infrabyx.audit.<EventName>.v1` (X-01): `AuditEngagementOpened.v1`, `AuditFindingRaised.v1` (finding_id, version, engagement_id, rating, criteria citation, owner role, due date, masked sample refs; no PII), `AuditFindingClosed.v1`, `ControlTestResultPublished.v1`, `EvidenceSubmitted.v1`, `ComplianceIssueRaised.v1` (regulatory-breach findings; `in.infrabyx.grc.*` per Spec §6.15); internal (`in.lawdocscomply.aud.<EventName>.v1`): `AuditPlanPublished.v1`, `AuditReportIssued.v1`, `AcbPackFrozen.v1`, `RiskAcceptanceExpiring.v1`, `VulnerabilitySlaBreached.v1`, `DNBS10Due.v1`, `SecretarialCheckFailed.v1`, `InspectionRequestDue.v1`. Consumed: `AuditEngagementOpened`, `AuditFindingRaised`, `AuditFindingClosed` from Finbyx/Udofin (mirror), `ExternalAccessGranted/Used/Revoked`, `ObligationPublished`, `PeriodClosed`, `FinancialStatementsApproved` (starts DNBS10 and statutory post-audit clocks), `ReturnFiled` (AUD checklist evidence), P06 `MeetingMinutesSigned`, P13 `EmployeeRoleChanged` (independence and universe triggers), P12 `AssetRegistered`, `OutsourcingArrangementApproved`.

### 7.5 Jobs and Temporal workflows

`UniverseSyncWorkflow` (event-driven + nightly reconciliation); `RiskReassessmentTrigger`; `PlanCapacityRecalc`; `EngagementTimerWorkflow` (per engagement; timers and escalations); `FindingRemediationWorkflow` (per finding; reminders, overdue, extension, risk-acceptance expiry); `ContinuousAuditScheduler` (cron per analytic test); `VaptCadenceJob` (daily); `DNBS10Clock` (from `FinancialStatementsApproved` + auditor report date); `SecretarialAnnualReportClock`; `InCameraQuarterCheck`; `EvidenceDriftDetector` (hourly, by source change events); `IntegrityVerifier` (nightly hash re-verification sample + on demand); `AcbPackScheduler` (T−10 working days before each ACB meeting).

---

## 8. Integrations (ports and adapters)

| Port | Adapter(s) | Use |
|---|---|---|
| `ECOSYSTEM_EVENTS` (P18) | Finbyx, Udofin | Mirror Finbyx-hosted engagements and findings; publish LDC-hosted ones |
| `EVIDENCE_REQUEST` (P18) | Finbyx evidence API, Udofin `re_audit_pack_v1`, Equator (dispute statistics only) | Evidence by reference and hash |
| `DATASET_IMPORT` (P11) | Loan tape, TB, GL, payroll, vendor master, access logs, CBS extracts | CAAT and sampling populations |
| `ESIGN_PORT` (P07) | Aadhaar eSign via ASP adapters (Leegality, Digio, SignDesk, Surepass, Protean) to CCA-empanelled ESPs; DSC (X-04) | Engagement letters, report issue, workpaper sign-off where external signature needed |
| `CALENDAR_PORT` (P04) | M365, Google, ICS | ACB meetings, fieldwork, deadlines |
| `VULN_IMPORT` | CSV, SARIF 2.1.0, Nessus `.nessus`, OpenVAS XML, Burp XML | VAPT tracker |
| `STORAGE_PORT` (P19) | S3/Azure/GCS/SharePoint/OneDrive/Drive | Export of audit files to tenant storage |
| `AI_PORT` (P17) | Claude API via provider adapter | Drafting and summarisation (flags) |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds / notes | Changed by |
|---|---|---|---|---|
| `aud.host.mode` | G | `LDC_NATIVE` (or `HYBRID` when Finbyx linked) | `LDC_NATIVE`, `FINBYX_HOSTED`, `HYBRID` + per-type map | ten_admin + HIA (maker-checker) |
| `aud.universe.change_task_sla_days` | T | 1 | 1–10 | HIA |
| `aud.universe.policy_max_interval_days.<unit_type>` | T | low 1095, medium 730, high 365 | must exist per unit type (floor) | HIA (ACB approval via methodology) |
| `aud.risk.scale` | T | 1–5; H ≥ 4, M 2.5–3.99, L < 2.5 | level + trend + basis mandatory | HIA |
| `aud.risk.iaf_parameters_locked` | L | true for RBIA tenants | — | — |
| `aud.plan.matrix_priority_order` | L | IAF para 32 order (RBIA tenants) | tie-breakers T | — |
| `aud.plan.approval_chain` | G | HIA → MD&CEO (info) → ACB | ACB/Board approval floor | ten_admin + ACB |
| `aud.engagement.timers.*` | T | as §5.1 | ≥ 1 working day each | HIA |
| `aud.independence.cooling_months` | T | 12 | 6–36 | HIA |
| `aud.workpaper.review_levels` | T | 2 (+HIA for high-risk) | ≥ 2 (floor) | HIA |
| `aud.workpaper.assembly_days` | T | 60 (statutory style), 45 (secretarial) | within standard | HIA |
| `aud.sampling.default_confidence` | T | 95% | 80–99% | HIA |
| `aud.finding.rating_scale` | T | Critical/High/Medium/Low | High/Medium pending always to ACB (floor) | HIA |
| `aud.finding.sla_days.<rating>` | T | 15/30/90/180 | tighter regulatory date wins | HIA |
| `aud.finding.response_window_wd` | T | 15 | 5–30 | HIA |
| `aud.finding.max_extensions_before_acb` | T | 1 (High/Critical) | ≥ 0; second always ACB (floor) | HIA |
| `aud.finding.repeat_lookback_months` | T | 24 | 12–60 | HIA |
| `aud.risk_acceptance.max_months` | T | 12 | 1–12 | ACB |
| `aud.atr.ageing_buckets` | T | 0–30, 31–90, 91–180, >180 | — | HIA |
| `aud.vapt.cadence_months` | L/T | VA 6, PT 12 (L for ML+ NBFC critical systems) | — | CISO |
| `aud.vapt.sla_days.<sev>` | T | 15/30/90/180 | — | CISO |
| `aud.is_audit.before_statutory_warning` | T | on | warning only | HIA |
| `aud.statutory.sa_mode_small_nd` | T | optional-with-checks | SA para 3 | CFO |
| `aud.statutory.dnbs10_reminders` | T | T−3, T−1, T | due rule L | CFO |
| `aud.statutory.branch_coverage_min_pct` | T | 15 | ≥ 15 (floor) | CFO |
| `aud.secretarial.tenure_alert_months` | T | 6 | 1–12 | CS |
| `aud.secretarial.group_conflict_check` | L | on for listed tenants | — | — |
| `aud.external.export_row_cap` | T | 50,000 | ≤ 200,000 | CCO |
| `aud.ai.drafting.enabled` | T | off | requires P17 | ten_admin |
| `aud.ai.special_investigation.enabled` | T | off | per engagement HIA override | HIA |
| `aud.acb_pack.lead_wd` | T | 10 | 3–20 | CS |
| `aud.pbc.reminder_ladder` *(v1.1)* | T | [3, 1, 0, -2] days to due | — | HIA |
| `aud.evidence_match.min_score` *(v1.1)* | T | 0.75 | 0.5–0.95 | HIA |
| `aud.share_scope.include_new_evidence` *(v1.1)* | T | ON | — | HIA |
| `aud.workpaper.lock_on_review` *(v1.1)* | L | true | — | — |
| `cmp.testing.cycle_months.{high,medium,low}` *(v1.1)* | T | 12 / 18 / 30 | 6–36 | CCO |
| `cmp.testing.sample.{continuous,high_freq,medium_freq,low_freq,annual}` *(v1.1)* | T | 100% / 25 / 12 / 5 / 100% | ≥ 1 | CCO |
| `cmp.testing.tolerable_deviation_pct.{high,medium,low}` *(v1.1)* | T | 5 / 10 / 15 | 0–20 | CCO |
| `cmp.testing.expand_on_deviation_pct` *(v1.1)* | T | 25 | 0–100 | CCO |
| `cmp.testing.issue_sla_days.{critical,high,medium,low}` *(v1.1)* | T | 30 / 60 / 90 / 180 | ≥ 7 | CCO |
| `cmp.testing.critical_escalation_bd` *(v1.1)* | T | 5 | 1–10 | CCO |
| `aud.ai.va07.autonomy_ceiling` *(v1.1)* | T | L1 | L0–L1 | HIA (NN-50) |

---

## 10. Security, privacy and audit

- SoD floors (§3) enforced server-side (NN-05); maker ≠ checker on plans, methodology, risk acceptance, grants.
- Workpapers, findings and reports are ledger-backed; locked files accept addenda only; Correction Entries (D-02) are the only way any platform role changes an issued report or finding, and both versions remain visible to the tenant and its auditors (NN-02).
- Evidence integrity: SHA-256, WORM storage, nightly verification, BSA 2023 s.63 certificate template in exports (NN-09).
- PII minimisation in evidence snapshots and analytics (masked by default; unmask per item with reason; NN-12); sealed classes (special investigations, whistle-blower, POSH, regulator correspondence) use separate keys and named-only access (NN-13).
- External rooms: read-only database roles, no write API reachable with external tokens, session limits (15 min idle, 8 h absolute), anomaly alerts, watermarked exports, daily activity report (NN-18).
- No regulator-portal credential is stored or scripted by this module; DNBS10 and inspection submissions are human filings (NN-08, NN-17).
- Logs: no PII or secrets (NN-32); every read of a sealed workpaper is logged and visible to the custodian.

## 11. AI touchpoints and guardrails (P17 agents; all behind `aud.ai.*` flags)

| Touchpoint | What Vidhi does | Guardrail |
|---|---|---|
| Scope suggestion | Proposes steps from the unit's obligations, risks, prior findings | Auditor accepts each step; no auto-add |
| Population/query helper | Turns a plain-English test into a governed query draft | Query reviewed and saved by auditor; executes only in masked schema |
| Exception triage | Clusters CAAT exceptions and drafts explanations to ask the auditee | Disposition is human |
| Finding drafting | Drafts condition–criteria–cause–effect text from workpaper notes with citations | Rating, criteria choice and issue are human; draft labelled AI (NN-04, NN-14) |
| Report narrative | Drafts executive summary from issued findings | Locked sections untouched; signatory approves |
| Management-response summariser | Summarises responses for ACB pack | Original text always shown |
| Evidence reader | Extracts fields from uploaded PDFs/scans (OCR via P07) for checklist lines | Extracted values flagged for confirmation; confidence shown |
| SS check explainer | Explains a failed SS-1/SS-2 check with the clause | Citation to stored standard text only (NN-06) |
| Plan and scoping drafts *(v1.1)* | VA-07 drafts the annual plan rationale and scoping memos | HIA edits and approves; ACB approves plan |
| Request-list generator *(v1.1)* | Proposes PBC items and matches existing evidence | Auditor/owner accepts each; nothing auto-accepted |
| Cross-engagement summary *(v1.1)* | Drafts themes narrative for ACB | Figures are bound values (NN-37); HIA approves |
| CCM *(v1.1)* | VA-14 runs validated scripts and drafts issues | Ratings and closure are human (NN-47) |
| Prohibited actions | — | Cannot rate, sign, issue, close, accept risk, change access, file or send externally; no AI in sealed engagements unless HIA enables per engagement; no training on tenant data (NN-15) |

## 12. Acceptance criteria (`tests/acceptance/p10/*.feature`)

```gherkin
Feature: RBIA risk assessment uses locked IAF parameters
  Scenario: Assessment cannot be approved with a blank locked parameter
    Given an ML NBFC tenant with RBIA applicable
    And a universe unit "Retail Lending – North" with parameter 4 "Results of regulatory examination" blank
    When the HIA submits the assessment for approval
    Then the request fails with "LDC-AUD-012 locked parameter missing basis"
    And the response cites "IAF para 31"

Feature: Plan priority order
  Scenario: Units are ordered by the IAF para 32 matrix
    Given 40 seeded units across all nine matrix cells
    When the plan builder generates a draft
    Then the order is H/H, H/M, H/L, M/H, M/M, L/H before capacity fill
    And a unit past its policy maximum appears regardless of cell

Feature: No outsourcing of internal audit for RBIA tenants
  Scenario: Marketplace professional cannot sign an RBIA report
    Given a dlv_professional with ia_contributor scope on an RBIA engagement
    When they attempt to sign the final report
    Then the command fails with "LDC-AUD-021 report owner must be tenant internal-audit staff (IAF para 39)"

Feature: Reproducible sampling
  Scenario: Re-running a sample with the stored seed
    Given a frozen population with hash H and a random sample with seed 4471
    When the sample is re-run
    Then the same 60 item keys are returned
    And adding one row to the source changes the population hash and the re-run is refused

Feature: Finding retest independence
  Scenario: Remediator cannot retest
    Given finding AUD-F-2026-118 remediated by user U1
    When U1 is assigned as retester
    Then the assignment fails with "LDC-AUD-031 retester must be independent of remediation"

Feature: DNBS10 clock
  Scenario: Due date from auditor's report signing
    Given an NBFC whose auditor's report is signed on Friday 25 Sep 2026 and 2 Oct 2026 is a holiday
    Then DNBS10 is due on Monday 5 Oct 2026
    And for a report signed on Thursday 24 Dec 2026 DNBS10 is due on 31 Dec 2026

Feature: Secretarial auditor group conflict
  Scenario: Infrabyx-linked PCS blocked for a listed retainer client
    Given a listed tenant receiving retainer compliance services through the Service Delivery Console
    When the CS proposes an Infrabyx-linked PCS as secretarial auditor
    Then the appointment is blocked with a citation to LODR Reg 24A prohibited services

Feature: Finbyx-hosted findings are read-only in LDC
  Scenario: Mirrored finding cannot be edited
    Given aud.host.mode = HYBRID with RBIA_UNIT hosted in Finbyx
    And an AuditFindingRaised event from Finbyx for finding F-77
    When an LDC user attempts to change its rating
    Then the request fails with "LDC-AUD-040 owned by FINBYX"
    And the finding appears in the ATR and ACB pack with source "Finbyx"

Feature: External auditor room is read-only and time-boxed
  Scenario: Grant expiry terminates sessions
    Given a statutory auditor grant valid to 23:59 IST
    When the clock passes 23:59 IST
    Then active sessions end within 60 seconds and ExternalAccessRevoked is emitted
    And any INSERT through the room's database role fails

Feature: SS-1 minutes signing check
  Scenario: Late signing flagged
    Given a Board meeting held on 1 Aug 2026 whose minutes were signed on 4 Sep 2026
    When the secretarial SS checks run
    Then an observation "Minutes not signed within 30 days (SS-1)" is created with the evidence link

Feature: Correction of an issued report
  Scenario: Super admin cannot edit in place
    Given an issued internal audit report R1
    When plt_super_admin attempts to modify a finding rating in R1
    Then the change is rejected unless submitted as a Correction Entry with reason and second approval
    And after approval both versions are visible to the tenant HIA with timestamps
```

```gherkin
# v1.1 scenarios
Feature: Faster external audit
  Scenario: Share once by scope
    Given the CFO shares scope "FY 2026-27, entity Alpha Finance, all RBI-NBFC checkpoints, registers MGT-1 and MBP-4, returns" with the statutory auditor for 60 days
    When a new evidence file for an in-scope checkpoint is uploaded on day 10
    Then it appears in the auditor room with a "new" badge
    And POSH case files never appear in the room

  Scenario: Existing evidence is suggested for a request
    Given PBC item "Board minutes approving ALM policy" is generated
    And sealed minutes of 12 Aug 2026 approving the ALM policy exist in LDC
    When the owner opens the request
    Then the sealed minutes are suggested with a match score
    And accepting links the existing file without a new upload

Feature: Second-line compliance testing
  Scenario: Deviation expands the sample
    Given a medium-frequency control test with sample 12 and tolerable deviation 10%
    When 2 exceptions are found
    Then the sample expands by 25% to 15 items before a conclusion can be recorded

  Scenario: Inspection closure needs verification test
    Given RBI observation O-7 in P26 is marked "complied" by the owner
    When the CCO tries to report closure to the regulator
    Then a closure-verification test is required and must pass first

  Scenario: Workpaper locks on review
    Given workpaper WP-12 is signed off by preparer P1 and reviewer R1
    When P1 edits WP-12
    Then a new version is created with a reason and requires re-review

Feature: Audit Assistant autonomy
  Scenario: VA-07 cannot issue findings
    Given VA-07 drafted finding F-3 for engagement E-9
    When VA-07 attempts the issue-finding action
    Then the action is not exposed to the agent (NN-50)
```

NN tests: `NN-02_audit_report_addendum_only`, `NN-05_retester_independence`, `NN-09_verify_file_detects_tamper`, `NN-13_special_investigation_sealed`, `NN-14_ai_cannot_issue_finding`, `NN-18_external_room_readonly`, `NN-22_sample_reproducible`, `NN-23_mirror_finding_owner_system`.

## 13. Deliverables and exit gate

1. `aud` schema migrations (expand-contract), seed programme libraries (NBFC RBIA, bank RBIA/concurrent, UCB, co-operative, ARC, companies s.138, IS/ITGC, data protection, secretarial, statutory support), report base templates, CAAT library v1 (≥ 30 tests), methodology v1.
2. All screens in §6 with empty/error states and `help.aud.*` content.
3. Applicability resolver with citations for all §4B types; decision log visible to CCO and HIA.
4. Engagement, finding, plan, methodology, grant, VAPT state machines with Temporal timers.
5. ACB pack builder integrated with P06 agenda and minutes write-back.
6. Ecosystem mirror and publish for `audit` events; evidence-request client.
7. Export to `LDC-EXPORT-1.0` (§4Q) with contract test.
8. Gherkin suites (§12) green; NN tests green; WCAG 2.2 AA audit of audit screens.
9. Documentation: `docs/modules/aud.md` (domain model, events, settings), auditor user guide, ACB user guide, external-auditor onboarding guide.

*(v1.1)* Additional exit evidence: scope share with auto-visible new evidence; request list generated in < 1 min with ≥ 50% of items matched to existing evidence on the demo tenant; one second-line test run through all five phases with sample expansion and RCA; one CCM script result relied upon after validation.

Exit gate: a demo tenant (ML NBFC) completes universe seeding, risk assessment, ACB-approved plan, one RBIA engagement with sampled workpapers and three findings through retest, an ACB pack frozen and tabled, a statutory-audit PBC cycle with AUD checklist and DNBS10 timer, one secretarial audit with SS checks, and a VAPT import with an SLA breach — all exported and re-imported into a sandbox with matching hashes.

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P10-01 | Paragraph numbers of NBFC SA Directions 2026 (RBI/DoS/2026-27/465) used in §4I | Carried from Finbyx v1.5; LDC to verify against PDF | Domain analyst | Rule pack rows `ACTIVE_UNVERIFIED`; checks run as warnings |
| OI-P10-02 | UCB internal audit / RBIA 2026 direction number and threshold | Not fetched | Domain analyst | Use legacy 3 Feb 2021 RBIA thresholds (≥ ₹500 crore) as `ACTIVE_UNVERIFIED` |
| OI-P10-03 | CYB 2026 paragraph numbers for IS audit and VAPT | Carried from Finbyx | Domain analyst | As above |
| OI-P10-04 | Rule 13 internal-audit thresholds | Confirm current text | CS | Resolver flags "verify" in decision log |
| OI-P10-05 | ICSI CSAS Revised Edition 2026 effective date and changed clauses (caps, waiting period, file timelines) | Approved 28 Aug 2026, effective date not published | CS | Use CSAS 2021 values flagged [VERIFY] |
| OI-P10-06 | LODR Reg 24A prohibited-services list and ASCR format | Confirm against SEBI notification and circular | CS | Block list as REC with override by CS + ACB |
| OI-P10-07 | SEBI CSCRF cyber-audit frequency by category; IRDAI and IFSCA cyber audit rules | Instruments evolving | CISO | Tenant-set cadence |
| OI-P10-08 | Bank LFAR current format and RBI submission timeline | Verify against ICAI GN 2026 and RBI | Domain analyst | LFAR pack off (`aud.pack.lfar.enabled = OFF`) |
| OI-P10-09 | DPDP Rules r.13 SDF audit commencement and auditor qualification | DPDP phase 3 from 13 May 2027 [VERIFY] | DPO | Data-protection audit runs as voluntary |
| OI-P10-10 | Co-operative audit classification and rectification periods per State | 28 States + MSCS | Co-op analyst | Per-State rule packs `ACTIVE_UNVERIFIED` |
| OI-P10-11 | Income-tax Act 2025 Form 26 clause list | New Act | Tax adviser | Pack off for TY 2026-27 until verified |
| OI-P10-12 | TallyPrime edit-log evidence for Rule 11(g) | Vendor feature by edition | Product | Manual checklist |
| OI-P10-13 | Whether DSC is required on any audit report submitted to a regulator | Varies | CS | eSign default |
| OI-P10-14 | Group-conflict rule (Infrabyx-linked PCS) — counsel confirmation | [REC] interpretation | General Counsel | Rule ON (stricter) |
| OI-P10-15 *(v1.1)* | Compliance Function Directions 2026 (RBI/DoS/2026-27/460) paragraphs on testing plan, frequency and Board reporting | Para mapping | RBI analyst | Owner methodology defaults (Tenant tier) |
| OI-P10-16 *(v1.1)* | Bank and UCB compliance-function testing requirements in the 2025/2026 consolidated sets | Catalogue lookup | RBI analyst | Same engine; values Tenant tier |
| OI-P10-17 *(v1.1)* | CCM script validation standard (who validates, evidence, frequency) | Method | HIA + CRO | Manual re-performance required before reliance |
| OI-P10-18 *(v1.1)* | Edit-log (r.3(1)) evidence formats by accounting software vendor | Vendor | Product | Manual checklist |
| OI-P10-19 *(v1.1)* | Foreign subsidiary audit calendars and auditor rules | P25 pack coverage | Global content lead | Tenant data, labelled |
| OI-P10-20 *(v1.1)* | Ecosystem `POST /v1/evidence-requests` (audit evidence pull from Finbyx/Udofin) | Ecosystem Spec v1.2 change request | Integration lead | CSV/manual upload |
| OI-P10-21 *(v1.1)* | Migration of `inspection*` tables to P26 projections | Sequencing with P26 | Tech lead | P10 keeps tables until P26 exits; dual-write |

## 15. Sources (accessed 25 Oct 2026 unless stated)

- RBI (NBFC – Internal Audit Function) Directions, 2026, RBI/DoS/2026-27/464, 31 Jul 2026 — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13589 ; summary https://taxguru.in/rbi/rbi-issues-2026-internal-audit-function-directions-nbfcs-hfcs.html
- RBI (NBFC – Auditor's Report) Directions, 2026, RBI/DoS/2026-27/468 — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13585
- RBI (Commercial Banks – Concurrent Audit) Directions, 2026, RBI/DoS/2026-27/409 — https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=13644
- RBI press release 2026-2027/787 (64 DoS Master Directions, 31 Jul 2026) — https://rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63265
- RBI (ARC – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/469 — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13584
- Finbyx Master Prompt v1.5, Part 7D (AU1–AU7) and Part 7C AC7 (owner's corpus, 23 Oct 2026) — instrument codes IAF, SA, AUD, CYB, CB-IA, OUT
- Infrabyx Ecosystem Integration Specification v1.1 §§4.7, 6.21, 9.1–9.3
- ICAI Guidance Note on Audit of Banks (2026 Edition), 16 Mar 2026 — https://publication.icai.org/post-data/guidance-note-on-audit-of-banks-2026-edition
- ICAI Internal Audit Standards Board publications (SIA list) — https://internalaudit.icai.org/publications/ ; Technical Guide on RBIA of NBFC (2024) — https://internalaudit.icai.org/wp-content/uploads/2024/07/final-pub.-57-4_TG-on-Risk-Based-Internal-Audit-of-NBFC-24.pdf
- ICSI Auditing Standards Revised Edition 2026 (Council approval 28 Aug 2026) — https://taxguru.in/company-law/icsi-council-approves-revised-auditing-standards-cseet-eligibility-student-fund.html ; ICSI revised SS-1/SS-2 announcement (13 Feb 2024) — https://www.icsi.edu/media/webmodules/Announcement_on_Revised_Secretarial_Standards_13022024.pdf
- Companies Act 2013 ss.138, 139–148, 204; Rule 9 (Managerial Personnel Rules) — https://ca2013.com/rule-9-companies-appointment-and-remuneration-of-managerial-personnel-rules2014/
- Owner's baseline: LawDocs Comply Architecture Part 3, "Internal & External Audit Management" and following sections; Part 3 §15 compliance-testing methodology (universe scoring, cycles, sampling, tolerable deviation, RCA, SLAs, escalation, QA) ported in §4R *(v1.1)*
- *(v1.1)* Appendix Z — G2 feedback (Hyperproof auditor sharing, Diligent AuditAI request lists, Optro scoping memos and cross-audit summaries); Companies (Accounts) Rules 2014 r.3(1) proviso and Companies (Audit and Auditors) Rules 2014 r.11(g) — https://www.mca.gov.in

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-37, NN-39; X-16 (`aud.host.mode`), X-19 (`ia_contributor`), X-30 (co-sourced IA only for RBIA-bound REs).

**Added in v1.1:** NN-47; X-48.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
