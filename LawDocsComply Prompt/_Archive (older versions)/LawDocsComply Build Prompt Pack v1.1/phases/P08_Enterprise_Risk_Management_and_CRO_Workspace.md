# Phase P08 — Enterprise Risk Management and CRO Workspace

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger and Correction Entries, outbox, feature flags);
> - **P01** (identity, roles, ABAC attributes, step-up MFA);
> - **P02** (settings registry, rule packs, terminology, entity-family resolver — every `erm.*` key is registered before use, NN-28);
> - **P03** (content library — obligations and control library that risks link to);
> - **P04** (workflow engine, tasks, approvals, Notifications inbox, calendar);
> - **P06** (committees and meetings — Risk Management Committee packs and minutes);
> - **P07** (DMS — evidence, policies such as the Risk Management Policy and Risk Appetite Statement).
>
> **Consumes (stated fallbacks if not yet built):** P12 (IT/cyber incidents, TPRM register, DPDP breaches → risk events), P13 (people metrics), P14 (complaint metrics), P15 (entity-family profile and applicability), P18 (inbound Finbyx/Udofin `risk` events), P17 (Vidhi drafting). Until P18 ships, KRI values arrive by Excel upload or manual attested entry (§4E.6).
>
> **Sequencing:** starts after P04 exit; runs in parallel with P06–P07; must exit before P09 (Risk Assessment Lab), which reuses the taxonomy, appetite framework, KRI engine and dashboard shell built here.
>
> **Binding appendices:** H (risk taxonomy, Basel mapping, applicability, KRI library, ratio library IDs), A (canonical approval and breach state machines), C (menus and dashboards), D (role matrix), U (settings catalogue), L (integration contracts; Ecosystem Spec v1.1 §6.22 and §9).
>
> **Requirements covered:** R-010, R-012, R-013 (risk-linked controls), R-015 (people-risk data intake), R-023, R-024, R-028, R-030, R-039, R-056, R-058, R-059 (dashboards; ratios in P09), R-075, R-086, R-088.
>
> **Estimated effort:** 6 two-week sprints, squad of 7 (backend 3, frontend 2, risk domain analyst 1, QA 1).

> **v1.1 changes (25 October 2026)**
> - New §4N *(v1.1)*: versioned risk methodologies that coexist (IMP-123); AI risk suggestions with stored justification under bounded autonomy (IMP-124, IMP-125, NN-47, NN-50); two-way KRI ↔ compliance-issue linkage (IMP-126); risk–control–obligation graph on the common control layer (IMP-013); continuous control monitoring (CCM) hooks; deterministic early-warning signals (EWS); one-click starter kits per entity family; group and multi-currency consolidation (NN-24 amended; P25); later international taxonomy packs; undoable bulk re-assessment (NN-49); tenant customisation of risk forms and registers.
> - Dashboards, the widget framework and committee-pack assembly are now owned by **P28 Reports, MIS and Board-Pack Studio** (module `rpt`, D-47); P08 registers its datasets, metrics and widgets there (FR-P08-46 and FR-P08-42 amended *(v1.1)*).
> - Risk Analyst agent (Appendix AA) defined for this module with default autonomy L1 (suggest) and L2 (draft) ceilings.
> - New screens SCR-ERM-25 to SCR-ERM-30, settings, events, Gherkin scenarios and open items OI-P08-12 to OI-P08-17.

---

## 1. Objective and business outcome

LawDocsComply is sold to banks, small finance banks, UCBs, NBFCs of every layer and category, ARCs, credit co-operative societies, IFSCA entities, SEBI-regulated entities (mutual funds, AIFs, listed companies, REIT/InvIT managers, intermediaries), IRDAI-regulated insurers and intermediaries, and ordinary companies and LLPs. Each has a different risk-management obligation: a commercial bank must run Pillar 2 ICAAP and publish Pillar 3 disclosures; an NBFC-ML must have a Risk Management Committee and a Board-approved risk policy; a top-1,000 listed company must have an RMC under LODR Reg 21; an LLP has no statutory risk function at all but still benefits from a register. This phase delivers **one configurable enterprise risk engine** — taxonomy, appetite, register, RCSA, controls, KRIs, loss events, issues, acceptance, committee packs and the CRO workspace — that switches on exactly what each entity family needs and nothing more.

| Outcome | Exit-gate measure |
|---|---|
| One engine, many entity families | Onboarding a tenant as "NBFC-ICC, Middle Layer, non-deposit, assets ₹2,400 crore" auto-enables the NBFC-ML taxonomy pack, RMC committee template, appetite metric set and 31 seed KRIs; onboarding "Private limited company, unlisted" enables only the corporate taxonomy (strategic, operational, compliance, financial, cyber, people, legal, reputational, ESG) with no prudential categories. Both explainable with the resolver's citation list (§4A.4) |
| Risk appetite that bites | The Board-approved RAS has appetite, tolerance and limit levels per metric; a limit can never be looser than the regulatory floor (test `NN-22_ras_floor`); a red observation opens a breach episode with escalation in ≤ 15 minutes of the value arriving |
| Live register linked to compliance | Every risk links to objectives, processes, controls and obligations (P03/P04). A failed compliance instance, audit finding (P10) or incident (P12) raises or re-rates the linked risk without re-keying |
| RCSA completed in days, not weeks | A 40-unit RCSA campaign is launched in ≤ 10 clicks from a template; units answer on one screen per risk; second-line challenge queue; completion ≥ 90% within the due date on the seeded pilot |
| KRIs fed automatically | For a Finbyx tenant, `RiskSnapshotPublished`, `KriBreached`, `LimitBreached` and `LossEventRecorded` update the CRO dashboard within the Ecosystem Spec SLA (≤ 15 min for breaches); for a non-Finbyx tenant, the same KRIs update from Excel/Tally templates (P11) or manual attested entries with evidence |
| CRO and RMC can run their meeting from LDC | The RMC pack (risk profile, appetite utilisation, top risks, breaches, loss events, RCSA status, emerging risks, cyber and third-party summary, ICAAP and stress summary from P09) is generated, frozen with a hash and distributed through the P06 board portal in ≤ 30 minutes of preparation |
| Fully customisable without a super admin | Tenant admins and CROs rename categories (levels 2–3), change scales, add KRIs, add widgets and edit templates within the Locked/Governed/Tenant tiers (NN-28); every change is audited (NN-02) |

---

## 2. Scope (in / out)

**In scope**

- Risk framework setup: methodology (ISO 31000:2018 process; COSO ERM 2017 components; three lines of defence), entity-family taxonomy packs, scales, matrices, materiality bands and terminology (§4A–4B).
- Risk Appetite Framework: Board-approved Risk Appetite Statement (RAS), qualitative statements, quantitative metrics with appetite/tolerance/limit levels, cascade to departments, products, branches, channels and legal entities (§4C).
- Risk register (enterprise, process, project, emerging) with inherent and residual assessment, trend, velocity, treatment and action plans (§4D).
- Control library and risk–control–obligation linkage with design and operating effectiveness, shared with P04 compliance controls and P10 audit tests (§4D.6).
- RCSA campaigns (questionnaire builder, unit responses, second-line challenge, final ratings) (§4E).
- KRI engine: definitions on governed metrics, thresholds, data sources (Finbyx, Udofin, LDC modules, Excel/Tally, manual attested), breach episodes and workflow (§4F).
- Loss-event and near-miss database with Basel event-type taxonomy, three dates, recoveries, GL reconciliation (§4G).
- Issues, actions and risk acceptance (temporary tolerances with expiry) (§4H).
- Risk committees: RMC, ALCO (structure only; liquidity analytics in P09), IT Strategy Committee (link to P12), Board — terms of reference templates, standing agenda, pack builder, minutes link to P06 (§4I).
- CRO workspace and role dashboards for CRO, risk officers, risk owners, RMC members and Board; configurable widget catalogue (§4J). KMP dashboards with financial ratios (CEO, MD, CFO, CCrO, CCO, IA head) are completed in P09 on the same shell.
- Emerging-risk radar and horizon scanning linked to P05 regulatory change (§4K).
- Pillar 3 / public risk-disclosure drafting workspace (bank Pillar 3; NBFC notes-to-accounts risk disclosures; listed-company board-report risk paragraphs; insurer public disclosures) — drafting, review and evidence, with numbers bound to P09 certified values (§4L).
- Risk-function governance records: CRO appointment, tenure, independence attestations, in-camera meetings, product-vetting records (§4M).
- Exports: register, RCSA, KRI history, loss data, RMC pack — Excel, Word, PDF/A; LDC-EXPORT-1.0 folder mapping (Appendix M).

**Out of scope (other phases)**

- Capital, ratios, ALM, liquidity, stress testing, ICAAP and KMP financial dashboards → **P09**.
- IT/cyber control frameworks, CERT-In incidents, vulnerability ingestion, TPRM lifecycle and outsourcing registers → **P12** (P08 consumes them as risk events and KRIs).
- Fraud case management, EWS alert handling at account level → system of record is Finbyx (FRM) or the tenant's LMS; P08 holds the fraud risk, KRIs and aggregated loss events.
- Compliance obligations and monitoring → P04; audit engagements → P10; policy lifecycle → P07; HR records → P13.
- Account-level credit data: never stored in LDC (Ecosystem Spec §6.22 pseudonymisation; NN-23).

---

## 3. Personas and permissions touched

| Role code (sub-type) | What they do in P08 | Key permissions (server-side, Appendix D) |
|---|---|---|
| `ten_kmp` (CRO) | Owns the framework, RAS drafting, taxonomy, KRI library, RCSA campaigns, challenge, breach review, RMC pack | `erm.framework.*`, `erm.ras.draft`, `erm.kri.define`, `erm.rcsa.launch`, `erm.breach.review`, `erm.pack.build` |
| `ten_maker` (risk officer / risk analyst) | Prepares register entries, KRI definitions, loss-event validation, pack sections | `erm.register.edit`, `erm.loss.validate`, `erm.pack.section.edit` |
| `ten_checker` (second-line reviewer) | Reviews register changes, challenges RCSA, approves KRI threshold versions | `erm.*.approve` (never on own submissions, NN-05) |
| `ten_dept_head` (risk owner, first line) | Owns risks and actions, answers RCSA, submits breach action plans | Own-scope read/write via ABAC (`department_id`, `legal_entity_id`) |
| `ten_maker` (unit respondent / risk champion) | Answers RCSA for a unit; reports loss events and near misses | Minimal forms; no register edit |
| `ten_employee` | Reports a loss event or near miss via the "Report a risk event" quick form | Create-only, own submissions visible |
| `ten_committee_member` (RMC) | Reads packs, comments, approves recommendations | Committee-scoped read, comment, vote (P06) |
| `ten_board_member` | Approves RAS, risk policy, accepts risks above Board threshold | Board-scoped read, approve |
| `ten_kmp` (CEO, MD, CFO, CCO, CCrO, CISO, CS) | Read dashboards; own risks in their domain; CS manages RMC calendar and minutes | Role templates (§4J); CS has meeting rights from P06 |
| `ten_internal_auditor` | Third-line read of framework, register, RCSA, KRI history, loss data; independent assurance notes | Read-all in tenant; cannot edit first/second-line records |
| `ten_external_auditor`, `ten_supervisor_view` | Time-boxed read-only grant (D-12, NN-18) | Grant-scoped read; watermarked exports |
| `ten_admin` | Enables modules, maps departments, sets Tenant-tier settings | `cfg.tenant.*` for `erm` keys of tier T |
| `dlv_rm`, `dlv_professional` | Retainer clients only: act as maker for risk documentation (D-03, R-072) | Tenant grant; never checker on the same record |
| `svc_vidhi` | Drafts risk statements, RCSA questionnaires, pack narratives, emerging-risk summaries on behalf of a user | Inherits the invoking user's permissions; cannot approve (NN-14) |

Segregation-of-duties rules enforced at grant time (Appendix D §SoD): the CRO cannot hold a business-line role or business targets where the entity's rule pack says so (NBFC Governance Directions — CRO independence, GOV paras 21(3)–(4) as read in Finbyx RK1.2 [VERIFY]); a risk owner cannot be the second-line reviewer of their own risk; an internal auditor cannot be a risk owner.

---

## 4. Functional requirements

### 4A. Risk framework, methodology and entity-family packs

**FR-P08-01 — Framework record.** Each legal entity (or the group, in group mode) has one active `risk_framework` version: methodology statement (ISO 31000:2018 clauses 5–6 process: communication, scope/context/criteria, assessment — identification, analysis, evaluation — treatment, monitoring and review, recording and reporting; COSO ERM 2017 five components and 20 principles as an optional mapping), three-lines-of-defence model, scales, matrix, materiality bands, review cycle, owner (CRO or designated risk head), Board approval reference (P06 minute id) and effective dates. A new version never edits the previous one (NN-07).

**FR-P08-02 — Entity-family taxonomy packs.** The platform ships versioned taxonomy packs (Appendix H §H.2) selected by the entity profile from P15:

| Pack code | Entity families | Level-1 categories (locked) | Notes |
|---|---|---|---|
| `TAX-BANK` | Commercial banks, SFBs, payments banks, LABs, RRBs | Credit, concentration, counterparty credit, market, IRRBB, liquidity and funding, operational (7 Basel event types), cyber and technology, third party and outsourcing, model, compliance and legal, conduct, financial crime and fraud, strategic and business, reputational, capital and solvency, climate and environmental, group and contagion, people, data privacy, resilience | Pillar 1/2/3 mapping on (Appendix H §H.3) |
| `TAX-UCB` | UCBs (Tiers 1–4), StCBs/DCCBs (RCB view) | As bank, without counterparty-credit and trading-book market risk by default; adds governance (board of directors/BoM) and political/membership risk | UCB Tier drives defaults |
| `TAX-NBFC` | NBFC-ICC, MFI, Factor, IFC, IDF, HFC, CIC, MGC, P2P, AA, NOFHC, SPD; layers BL/ML/UL/TL | Credit, concentration, market and investment, IRRBB, liquidity and funding, operational, cyber and technology, outsourcing and third party (LSP, co-lender, DSA), model, conduct, compliance and legal, fraud, strategic, reputational, group contagion, people, data privacy, resilience, climate (ICAAP-internal) | Layer and category drive applicability; no Pillar 1 op/market charge (CAP Ch III) |
| `TAX-ARC` | Asset reconstruction companies | Acquisition and valuation risk, resolution/realisation risk, SR investment risk, concentration (originator, sector), liquidity, legal and enforcement (SARFAESI, IBC, DRT), operational, conduct (borrower dealings), compliance, reputational, people, cyber | ARC Directions 2025 |
| `TAX-COOP` | Credit co-operative societies (State Act / MSCS Act), other co-operatives | Credit (member loans), liquidity, deposit concentration, governance and election risk, fraud and misappropriation, compliance (Registrar/State Act), audit-observation risk, operational, cyber, people, reputational, member-relations | Labelled "management practice" where no statute requires an ERM (Finbyx RK1.5) |
| `TAX-IFSCA` | IFSCA FC/FU, IBUs, FMEs, intermediaries | Per activity: credit, FX, market, liquidity, operational, AML/CFT, cyber, outsourcing, home-regulator and cross-border, conduct, compliance | Activity selection from P15 |
| `TAX-SEBI-MF` | AMCs and MF schemes | Investment (market, credit, liquidity of schemes), operational, fraud and front-running, conduct and mis-selling, compliance, cyber (CSCRF), outsourcing (RTAs), people/key-person, reputational, governance (trustee oversight) | SEBI MF Risk Management Framework [VERIFY citation] |
| `TAX-SEBI-AIF` | AIF managers and schemes | Investment, valuation, liquidity, concentration (investee limits), leverage (Cat III), conflicts, compliance, operational, cyber, people | AIF Regulations 2012 |
| `TAX-SEBI-LISTED` | Listed companies (equity/debt), REIT/InvIT managers | Strategic, operational, financial (liquidity, credit, FX, interest, commodity), sustainability/ESG, information and cyber, compliance and legal, governance, reputational, people, third party | LODR Reg 17(9), Reg 21 and Sch II Part C [VERIFY para]; Companies Act s.134(3)(n) |
| `TAX-SEBI-INT` | Brokers, DPs, IAs, RAs, PMS, RTAs, MBs | Client-asset, operational, cyber (CSCRF), market, settlement, conduct, compliance, people, outsourcing | — |
| `TAX-INS` | Life, general, health insurers, reinsurers | Insurance (underwriting, reserving, catastrophe, lapse, mortality/morbidity), market, credit (reinsurance counterparty), liquidity, ALM, operational, cyber, conduct/mis-selling, compliance, strategic, reputational, people, outsourcing | IRDAI corporate governance and AFIF Regs 2024 (solvency control level 150%) |
| `TAX-INS-INT` | Brokers, corporate agents, web aggregators, IMFs, TPAs | Conduct, client-money, operational, cyber, compliance, people, concentration (insurer partners) | — |
| `TAX-CORP` | Private/public companies, OPCs, Section 8 companies | Strategic, operational, financial, compliance and legal, cyber and IT, data privacy, people, ESG, reputational, third party, project | Companies Act s.134(3)(n), s.177(4)(vii), Sch IV |
| `TAX-LLP` | LLPs, partnerships | As `TAX-CORP` minus governance-committee items | No statutory ERM requirement — "management practice" label |

- Level 1 is **Locked** per pack version (NN-28); levels 2–3 are **Tenant** tier (rename, add, merge, hide; never delete a node that has history — it is retired with an effective date, NN-29).
- A tenant may combine packs (a listed NBFC gets `TAX-NBFC` + `TAX-SEBI-LISTED` deduplicated by the cross-walk table in Appendix H §H.2.4; an NBFC with an IFSC unit adds `TAX-IFSCA` scoped to that legal entity).
- Every node carries: code, name, definition, "i"-help text (P23 glossary key), Basel mapping (Pillar 1 / Pillar 2 / Pillar 3 template where applicable), default owner role, default KRIs, default controls, regulatory citations, applicability rule.

**FR-P08-03 — Applicability resolver.** For each legal entity, the resolver (P02 rule engine; P15 entity logic) evaluates the profile (regulator, entity family, layer/tier, deposit-taking, asset size from the last audited balance sheet, listed status, market-cap rank, activities, group membership) and returns: enabled taxonomy nodes, required risk-governance elements (RMC, CRO, ALCO, ITSC, CCO; Appendix H §H.4), required periodic artefacts (risk policy review, RAS approval, RCSA cadence, ICAAP from P09), each with citation and effective date. Example rules (seeded; [VERIFY] each against the current text before activation):

- NBFC, any layer → RMC required (NBFC Governance Directions 2025, RBI/DOR/2025-26/344, para 9 as read in Finbyx RK1.1).
- NBFC ML/UL/TL with assets > ₹5,000 crore → CRO required (GOV para 19).
- NBFC ALM Chapter II applies (assets ≥ ₹100 crore) → ALCO required (NBFC ALM Directions 2025, RBI/DoR/2025-26/355, para 17).
- Commercial bank → Board-approved ICAAP (Commercial Banks Capital Adequacy Directions 2025, RBI/DOR/2025-26/151, Chapter V, paras 6–7) and Pillar 3 disclosures (Chapter V.E, Annex III).
- Listed entity in top 1,000 by market capitalisation or high-value debt-listed entity → RMC under LODR Reg 21 [VERIFY scope as amended]; all listed entities → risk-management plan reviewed by the Board (LODR Reg 17(9)) [VERIFY].
- Every company → Board report statement on development and implementation of a risk-management policy (Companies Act 2013 s.134(3)(n)); companies with an Audit Committee → evaluation of internal financial controls and risk-management systems (s.177(4)(vii)).
- Insurer → RMC and CRO under IRDAI corporate governance norms [VERIFY: IRDAI Master Circular on Corporate Governance for Insurers, 2024].
- Credit co-operative society → no statutory ERM; by-law and Registrar audit observations drive a "management practice" pack.

**FR-P08-04 — Explainability.** A "Why is this on?" panel (SCR-ERM-02) shows each enabled element, the profile attribute that triggered it, the rule version and the citation. Threshold proximity (for example, assets projected to cross ₹5,000 crore within two quarters — R51 in Appendix H) raises a "governance readiness" task to the CS and CRO (mirrors Finbyx RK1.1).

### 4B. Scales, matrices and scoring

**FR-P08-05 — Configurable scales.** Default 5 × 5 likelihood × impact (owner baseline, Architecture Part 2 Table 2-3): likelihood 1 Rare (< 5% in 12 months) … 5 Almost certain (> 75%); impact 1 Negligible … 5 Severe. Impact has **dimensions** (financial ₹ band tied to the entity's materiality threshold — default % of net worth or Tier 1; regulatory; customer; reputational; operational/service; people/safety; legal), and the impact score is the maximum across dimensions (default) or a weighted score (Tenant setting). Scales can be 3 × 3, 4 × 4, 5 × 5 or 6 × 6 (Tenant tier); changing a scale creates a new framework version and offers a mapping table from old to new scores; history is never rescored silently.

**FR-P08-06 — Severity bands.** Default bands on L × I: 1–4 Low (green), 5–9 Medium (yellow), 10–15 High (amber), 16–25 Critical (red), each with a response rule (accept/monitor; treat with owner plan; treat with priority and second-line oversight; immediate action with CRO and Board visibility). Colour is never the only signal (text label and icon, NN-21).

**FR-P08-07 — Additional attributes.** Velocity (speed of onset: immediate / days / months / > 1 year), trend (improving / stable / deteriorating — computed from the last three assessments, overridable with reason), proximity, control-effectiveness rating (design and operating, each Effective / Partially effective / Ineffective / Not tested), confidence in assessment (High/Medium/Low).

**FR-P08-08 — Residual computation.** Residual = inherent reduced by a control-effectiveness factor (default lookup: Effective −2 likelihood steps or −1 impact step per the control type preventive/detective; Partially effective −1; Ineffective 0), then **judgement override** with mandatory rationale and second-line approval. The system shows both the computed and the final rating. A residual better than inherent without at least one linked, tested control is blocked (`LDC-ERM-014`).

**FR-P08-09 — Quantified view (optional).** For risks with loss data or scenario estimates, an expected annual loss and a 1-in-20 / 1-in-100 severe-but-plausible loss can be recorded (from P09 scenario analysis or FAIR-style cyber quantification from P12). Quantified values never replace the matrix rating; they appear beside it.

### 4C. Risk Appetite Framework and RAS

**FR-P08-10 — RAS object.** `risk_appetite_statement` (version, scope legal entity/group, effective dates, Board approval reference, RMC recommendation reference, review due date) → `ras_statement` (qualitative, per Level-1 category: "Low appetite for compliance risk", "Zero tolerance for mis-selling", "Moderate appetite for unsecured retail credit within prudential limits") → `ras_metric` (metric id from the P09 ratio library or a KRI metric, direction, unit, three levels: **appetite** (target zone, green), **tolerance** (amber), **limit** (red)). Aligns with Finbyx RK1.4 so that RAS thresholds approved in LDC flow to Finbyx as new threshold versions (Ecosystem Spec §6.22 inbound rule).

**FR-P08-11 — Regulatory floors.** For metrics typed `regulatory` in the ratio library (Appendix H §H.6), the limit level must be at least as strict as the regulatory minimum for that entity profile (for example NBFC-ML CRAR ≥ 15%, Tier 1 ≥ 10% — NBFC Capital Adequacy Directions 2025, RBI/DOR/2025-26/345, paras 6(2)–(3); NBFC SLS 1–7 day cumulative mismatch ≤ 10% — ALM Directions para 39; UCB Tier 2–4 CRAR ≥ 12% — UCB Capital Adequacy Directions 2025, RBI/DOR/2025-26/275, para 9). Attempting a looser limit returns `LDC-ERM-021` with the citation (test `NN-22_ras_floor`).

**FR-P08-12 — Cascade.** Limits cascade by legal entity, business line, product, department, branch/region, channel (DSA, LSP, co-lender), sector, state and funding source. Children must sum within the parent for additive metrics; non-additive metrics (ratios) inherit the parent level or a stricter one. Each cascade node has an owner and an approver (delegated authority). Utilisation bars show value/limit per node.

**FR-P08-13 — Approval workflow.** RAS draft (CRO, maker) → second-line review (checker) → CFO and CCO concurrence (configurable) → RMC recommendation (P06 meeting item with resolution text drafted) → Board approval (minute reference captured, eSign optional) → effective. Return paths at each step. Annual review reminder 60 days before due (Tenant setting); off-cycle review triggers: material strategy change, layer migration (BL → ML → UL), new business line, merger, persistent breach > 2 quarters, PCA proximity (P09).

**FR-P08-14 — Use test evidence.** The RAS page lists where the RAS is used (pricing policy, product approval records, capital plan, ICAAP, limits in Finbyx, incentive policy) with evidence links — supports the supervisory "use test" expectation for ICAAP (bank Chapter V; NBFC Chapter V).

### 4D. Risk register

**FR-P08-15 — Register types.** Enterprise (top-down), process/department (bottom-up), project/change, product (new product vetting), third party (mirror of P12 TPRM inherent risks), emerging. One data model; type drives default fields and workflow.

**FR-P08-16 — Register entry fields.** Risk ID (`RISK-<L1code>-<seq>`, system), title, statement in **cause – event – consequence** form (Vidhi can propose the wording from a free-text description; user accepts or edits — NN-14), taxonomy node (L1–L3), legal entity, department, process, product, objective at risk, owner (first line), second-line oversight, third-line assurance link, inherent likelihood/impact per dimension, velocity, controls (many-to-many with effectiveness), residual rating (computed + final), trend, appetite reference (RAS statement and metric), status (Draft / Active / Under review / Retired), treatment (Avoid, Reduce/Mitigate, Transfer/Share — insurance, outsourcing with retained accountability, Accept), action plans, KRIs, linked obligations (P04), linked audit findings (P10), linked incidents and loss events, linked policies (P07), review date, confidentiality class (normal / restricted / sealed — e.g., fraud investigations, NN-13), attachments.

**FR-P08-17 — Assessment history.** Every rating change is a new `risk_assessment` row (bitemporal: `valid_from` = effective assessment date, `recorded_at`), with assessor, reviewer, rationale and evidence. Trend charts read the history. A Correction Entry (D-02) is the only way to fix a wrongly entered historical rating; the original stays visible.

**FR-P08-18 — Automatic triggers (no re-keying).** The register listens to:

| Trigger (source) | Effect |
|---|---|
| Compliance instance failed or overdue for a High-risk obligation (P04 `ComplianceIssueRaised`) | Linked compliance risk flagged "re-assess"; risk owner task; KRI "overdue high-risk obligations" updated |
| Audit finding rated High (P10 `AuditFindingIssued`) | Linked control rated "Ineffective — pending re-test"; risk residual re-computed as a proposal for owner confirmation |
| Cyber/IT incident (P12 `SecurityIncidentNotified`), DPDP breach (P12) | Operational loss/near-miss draft created; cyber risk re-assess task |
| Third-party rating downgrade or SLA breach (P12 TPRM) | Outsourcing risk KRI updated; owner task |
| Regulatory change accepted as "impacting" (P05 `RegulatoryChangeAssessed`) | Emerging-risk item or register update proposal |
| Finbyx/Udofin `KriBreached`, `LimitBreached`, `LossEventRecorded` | KRI episode, limit-breach episode, loss event imported (§4F, §4G) |
| Complaint-volume spike (P14 aggregates) | Conduct-risk KRI updated |
| People metric breach (P13 `PeopleMetricPublished`: attrition, key-person vacancy, training overdue) | People-risk KRI updated |

Proposals created by triggers are labelled with their source; nothing changes a final rating without a named human (NN-14 analogue for automated rules: automation proposes, people approve).

**FR-P08-19 — Product and change risk vetting.** New product / process change requests (from P04 tasks or Finbyx product-version events) open a vetting record: risks, mitigants, controls, limits, new KRIs, RAS impact, compliance sign-off (CCO), CRO vetting decision. For NBFC tenants where a CRO is mandatory, a product cannot be marked "approved for launch" in LDC without the CRO vetting record (mirrors Finbyx RK1.2; GOV para 23 [VERIFY]).

**FR-P08-20 — Top-risk and bow-tie views.** Top-N residual risks per entity, heat maps (inherent vs residual), movement arrows between periods, bow-tie diagram (causes → preventive controls → event → mitigating controls → consequences) generated from register links — exported as SVG/PNG for packs.

### 4D.6 Control library and linkage

**FR-P08-21 — One control library.** Controls are shared across P04 (compliance controls derived from the Excel "Control Activity" column V), P08 (risk controls), P10 (audit test programmes) and P12 (ISMS controls, ISO 27001:2022 Annex A, NIST CSF 2.0, RBI/SEBI cyber frameworks). Fields: control ID, name, objective, type (preventive / detective / corrective / directive), nature (manual / IT-dependent manual / automated), frequency, owner, key control flag, linked risks, linked obligations, test procedure, evidence expectation, last test result (design, operating), next test date.

**FR-P08-22 — Control testing sources.** Results arrive from: P04 checker approvals (compliance evidence accepted = control operated for that period), P10 audit tests, P12 continuous control monitoring, Finbyx `ControlTestResultPublished`, and P08 RCSA self-ratings. A self-rating of "Effective" requires a linked test result or evidence item dated within the test frequency (Finbyx RK2.2 rule reused).

### 4E. RCSA campaigns

**FR-P08-23 — Campaign builder.** Template (scope: entity, departments, processes; risk set; questionnaire version; due date; reminders; respondents by role or named users; reviewer). Questionnaire items per risk: confirm/edit risk description, inherent likelihood and impact per dimension, control self-rating with evidence, emerging issues, incidents in the period, action proposals, attestation. Vidhi can draft the questionnaire from the register and the last campaign's results (draft only).

**FR-P08-24 — Unit response UX.** One page per risk with previous ratings shown, inline "i" help for each scale, save-as-draft, bulk "no change since last cycle" (requires a one-line confirmation and is flagged to the reviewer), attach evidence from DMS, keyboard navigation. Mobile-responsive.

**FR-P08-25 — Second-line challenge.** Reviewer queue with filters (ratings improved without evidence, control rated effective but failed test, missed incidents). Actions: accept, challenge (comment, request change), escalate to CRO. Final ratings are written to the register as a new assessment with campaign reference.

**FR-P08-26 — Cadence.** Default annual; semi-annual for risks with residual High/Critical; quarterly optional. Ad hoc campaigns for new products, incidents and regulatory changes. RCSA completion and results feed the P10 risk-based audit universe (risk score per auditable unit).

**FR-P08-27 — RCSA for small tenants.** "Quick RCSA" mode for companies, LLPs and small co-operatives: one questionnaire of ≤ 25 items generated from the `TAX-CORP`/`TAX-LLP`/`TAX-COOP` pack, completed by the admin or a single risk owner in under 30 minutes, producing a register and a one-page risk report.

### 4E.6 Data entry fallbacks

**FR-P08-28 — When no feed exists.** Every KRI and RAS metric can be populated by: (a) inbound event (Finbyx, Udofin, P11–P14 modules); (b) LDC-computed metric from P09 on imported data; (c) Excel upload using the KRI value template (`LDC-DT-KRI-v1.0`, Appendix H §H.8.3) with validation and preview; (d) manual attested entry by a maker with evidence and checker approval. The provenance badge (`FX`, `UD`, `LDC`, `XLS`, `MAN`) shows on every value and dashboard tile; manual values cannot be marked "certified" without a checker.

### 4F. KRI engine

**FR-P08-29 — KRI definition.** KRI ID (`KRI-<L1>-<seq>`), name, linked risks, **metric id** (governed metric from the P09 ratio library or a KRI-specific metric definition with formula text, numerator/denominator sources), unit, polarity (higher-is-worse / lower-is-worse / band), frequency (daily, weekly, monthly, quarterly, event), thresholds (green/amber/red, as a versioned threshold set; linked to RAS levels where the KRI is a RAS metric), data source (provenance per §4E.6), owner, escalation path, leading/lagging flag, applicability rule. KRI library seeds per taxonomy pack (Appendix H §H.8 — 172 KRIs).

**FR-P08-30 — Threshold versioning.** A threshold change is a new version with approver and effective date; historic RAG states keep the version used. Personal alert thresholds may be tighter, never looser (Finbyx RK8.2 rule).

**FR-P08-31 — Observation and breach episodes.** Each observation stores value, as-of, provenance, threshold version and RAG. The first red observation opens a **breach episode** (one open episode per KRI); amber observations before it are attached as history. Inbound Finbyx `KriBreached` (status OPEN/CURED, `episode_id`, `update_seq`) maps one-to-one to an LDC episode; LDC never opens a duplicate.

**FR-P08-32 — Breach workflow (canonical in Appendix A §A.7).** States `OPEN → NOTIFIED → ACTION_PLANNED → CRO_REVIEWED → IN_REMEDIATION → CURED` with exception `ACCEPTED` (RMC, expiry ≤ 6 months) and `INVALIDATED` (source restatement). Timers default: plan within 5 working days; CRO review within 5 working days; missed cure date escalates owner → CRO → RMC chair → Board (all Tenant-configurable above floors). Cure rule: 1 consecutive non-red observation (3 for daily KRIs). Mirrors Finbyx RK2.3 so both products behave identically for the same tenant.

**FR-P08-33 — Limit-breach episodes.** Inbound `LimitBreached` (limit_type REGULATORY, BOARD, INTERNAL, LE, SSE, CME, SLS_TOLERANCE, LCR, HQLA_STRESS, DLG_CAP, SR_SELF_INVESTMENT, INVESTMENT, PCA_RT1–3; `projected` flag) creates a limit-breach episode in the same workflow, with regulatory-reporting tasks where the citation requires (for example LE breach intimation to RBI DoS for NBFC-UL; HQLA use reported to DoS immediately — ALM para 62). LDC drafts the intimation; a human sends it (NN-08).

**FR-P08-34 — Data restatement.** A restated source value re-runs the KRI; if the breach disappears, the episode closes as `INVALIDATED` with the restatement reference — never deleted.

### 4G. Loss-event and near-miss database

**FR-P08-35 — Event capture.** Quick form for any employee ("Report a risk event": what happened, when, where, estimated amount, attachments) → ORM team completes: taxonomy (Basel Level 1 event types — internal fraud; external fraud; employment practices and workplace safety; clients, products and business practices; damage to physical assets; business disruption and system failures; execution, delivery and process management — with Levels 2–3 per Appendix H §H.5), business line, **three dates** (occurrence, discovery, accounting — RBI ORM Guidance Note para 42(2) as read in Finbyx RK2.3 [VERIFY]), gross loss, recoveries (insurance, other), net loss, near miss / gain flags, boundary flags (credit-related operational loss, legal), root cause (people/process/system/external), controls failed, linked incident, fraud case reference, complaint, audit finding, linked risk.

**FR-P08-36 — Validation and reconciliation.** Approval by the ORM team (checker). Quarterly reconciliation with GL write-off and expense accounts (from P11 trial balance or Finbyx) with unreconciled list; recoveries and re-estimates are new versions of the same event. Capture SLA default: 5 working days from discovery. Minimum reporting threshold Tenant-configurable (default: all events including near misses).

**FR-P08-37 — Inbound events.** Finbyx/Udofin `LossEventRecorded` (banded amounts for individual borrowers, pseudonymised references) import as events with provenance `FX`/`UD`; versions update the same event. Fraud losses from the RBI Fraud Risk Management Directions 2026 (RBI/DoS/2026-27/463) are tagged internal/external fraud; LDC tracks FMR filing within 14 days of classification (para 43) as a compliance task (P04), not by filing.

**FR-P08-38 — Analytics.** Loss frequency/severity by event type, business line, cause; trend; loss-to-gross-income ratio (KRI R53 in Appendix H); top losses; time-to-discovery; near-miss ratio. Feeds the operational-risk section of the ICAAP (P09) and scenario calibration.

### 4H. Issues, actions and risk acceptance

**FR-P08-39 — Issues.** Sources: RCSA, KRI breaches, loss events, control test failures, audit findings (P10), regulator observations (P04/P06 inspection module), incidents, self-identified. Fields: severity, root cause, owner, due date, action plan with milestones, evidence, status, validation by second line, closure approval. One issue can link to many risks and controls; duplicates are merged with an audit trail.

**FR-P08-40 — Risk acceptance.** A risk above appetite can be accepted only by the authority level set in the delegation matrix (default: residual High → CRO; Critical → RMC; above-limit or regulatory → not acceptable — must be treated). Acceptance has rationale, compensating controls, expiry (≤ 12 months; ≤ 6 months for KRI episodes), review reminders. Expiry reopens the item. Regulatory-limit breaches cannot be "accepted" (`LDC-ERM-031`).

### 4I. Risk committees and packs

**FR-P08-41 — Committee templates.** Seeded templates (P06 committee engine) for RMC (Board), Executive Risk Committee, ALCO, IT Strategy Committee, Operational Risk Committee, Credit Risk Committee, Investment Committee (MF/AIF/insurer), Product Approval Committee — each with terms of reference drafts citing the entity family's rules (Appendix H §H.4), quorum, frequency, standing agenda. Names, members and frequency are Tenant-configurable; the regulatory minimum frequency and composition are Governed floors.

**FR-P08-42 — RMC pack builder.** Sections bound to live data: executive summary (Vidhi draft for CRO edit), risk profile heat map and movements, RAS dashboard (utilisation by metric with RAG), top 10 risks, new and emerging risks, KRI breaches and episodes, limit breaches and regulatory intimations, loss events and near misses, RCSA status, issues ageing, cyber summary (P12), third-party and outsourcing summary (P12), compliance risk summary (P04), people risk (P13 aggregates), model inventory status (§4M.4), capital/liquidity/stress/ICAAP summaries (from P09 once live), approvals sought. Freeze computes a hash over values, metric versions and narratives; distribution via P06 board portal; late changes create an addendum (Finbyx RK8.3 pattern). *(v1.1)* Pack assembly, versioning, freeze/hash and rendering (DOCX/PDF/PPTX) run on the **P28 pack studio**; P08 supplies the section definitions, mandatory items per family and the narrative-ready result cards (numbers bound to frozen values only, NN-37); the frozen pack is attached to the RMC meeting in P06.

**FR-P08-43 — Standing agenda items from regulation.** The pack template includes mandatory items per entity family, for example: NBFC RMC — overall risks including liquidity (GOV para 9 [VERIFY]), EWS effectiveness (FRM Directions 2026, para 14), quarterly CISO cyber review where required by the NBFC cyber directions [VERIFY para]; listed company RMC — cyber security and ESG-related risks, business continuity plan (LODR Sch II Part D(C) [VERIFY]); MF AMC risk committee items [VERIFY]; insurer RMC — ALM, solvency, reinsurance [VERIFY].

**FR-P08-44 — Decisions and action tracking.** Committee decisions (from P06 minutes) that change the RAS, accept a risk, approve a policy or assign an action write back to P08 records with the minute reference.

### 4J. CRO workspace and dashboards

**FR-P08-45 — CRO home (SCR-ERM-01).** Tiles: overall risk profile (residual heat map), RAS scorecard (metrics by RAG with trend sparkline), open breach episodes by age and stage, top 10 risks with movement, emerging-risk radar, RCSA progress, issues ageing, loss events (month, YTD, vs appetite), regulatory change impacting risks (P05), upcoming committee dates and pack status, data-feed health (Finbyx/Udofin/LDC/manual provenance mix; stale feeds), approvals awaiting me. Each tile: value, RAG text, as-of date, metric version, provenance badge, certification state (from P09).

**FR-P08-46 — Widget catalogue and customisation.** Users add, remove, resize and arrange widgets from a catalogue (heat map, RAG scorecard, KRI trend, bar/line/area charts, table, single value with sparkline, top-N, movement table, map by state/branch, funnel for RCSA status, text note); save views (entity, department, period); set personal alert thresholds (tighter only); share a view within the tenant (view only). Role templates (CRO, risk officer, risk owner, RMC member, Board member) are versioned; changing a standard template requires the CRO's approval (Finbyx RK8.3 rule). Dashboards for CEO, MD, CFO, CCrO, CCO, IA head and Board with financial ratios are built in P09 on the same widget framework. *(v1.1)* The widget framework, dashboard builder, personalisation and subscriptions are owned by **P28** (module `rpt`); P08 registers risk widgets and datasets there (FR-P08-65).

**FR-P08-47 — Drill-down.** Every tile drills tile → segment → record in ≤ 3 clicks; inbound Finbyx values drill to the LDC copy and show a "View source in Finbyx" deep link (opens Finbyx with the user's Finbyx session; LDC never holds account-level data).

**FR-P08-48 — Accessibility.** WCAG 2.2 AA: heat maps have a table alternative and text RAG; charts expose data tables; keyboard navigation across widgets; "why this colour" explainer (threshold version and value) (NN-21).

### 4K. Emerging risks and horizon scanning

**FR-P08-49 — Emerging-risk radar.** Items with category, description, time horizon (0–1, 1–3, 3+ years), likelihood of materialising, potential impact, signals (sources: P05 regulatory updates and consultations, news feed, RBI FSR/Annual Report themes, BCBS publications, sector events, internal incidents), owner, status (watch / assess / promote to register / dismiss). Vidhi drafts a quarterly emerging-risk digest from the P05 Updates feed and approved news sources with citations (draft; CRO approves before it enters a pack).

**FR-P08-50 — Promotion.** "Promote to register" creates a register entry pre-filled from the emerging item, keeping the link.

### 4L. Risk disclosures (Pillar 3 and public disclosures)

**FR-P08-51 — Disclosure workspace.** Templates by entity family:

| Family | Disclosure set | Source of numbers |
|---|---|---|
| Commercial banks, SFBs | Pillar 3 per Commercial Banks Capital Adequacy Directions 2025 Chapter V.E and Annex III (capital composition, RWA overview, credit risk, CCR, securitisation, market risk, operational risk, IRRBB, liquidity LCR/NSFR, leverage ratio templates Ch VII.F, remuneration) [VERIFY template list]; frequency per Annex III | P09 certified values |
| UCBs | Notes-to-accounts disclosures per RBI UCB financial-statement directions [VERIFY] | P09 / P11 |
| NBFCs | Notes-to-accounts risk disclosures per NBFC Financial Statements Directions 2025 (RBI/DOR/2025-26/359) — capital, asset quality, concentration, liquidity (ALM para 15 and Annex I public disclosure; LCR quarterly para 78) | P09 / P11 |
| Listed companies | Board's report risk-management statement (s.134(3)(n)); Management Discussion & Analysis risks and concerns (LODR Sch V Part B [VERIFY]); BRSR risk items (P06/P12) | P08 register |
| Insurers | IRDAI public disclosures (solvency, ALM) [VERIFY forms] | P09 |
| MF AMCs | Risk-o-meter and PRC disclosures (scheme level) — reference only; scheme risk data from the tenant's fund-accounting system | Imported |

Each disclosure item has a narrative (Vidhi may draft from the register; human edits), a bound table (frozen P09 values), reviewer, approver, publication date and evidence of publication (URL, hash). Pillar 3 is public disclosure, not a list of risk types (BCBS DIS); the workspace labels it so.

### 4M. Risk-function governance records

**FR-P08-52 — CRO register.** Appointment (Board resolution reference), tenure, reporting line, removal/transfer (Board approval reference; draft intimation to RBI DoS RO where the rule pack requires — GOV para 22 as read in Finbyx [VERIFY]; listed: stock-exchange disclosure draft for change in senior management), independence attestations (annual), quarterly in-camera meeting tracker where the CRO reports to the MD & CEO (GOV para 21 [VERIFY]); missed quarter raises an exception to the CS and RMC chair.

**FR-P08-53 — Risk policy register.** Risk Management Policy, RAS, ORM policy, model risk policy, stress testing policy, ICAAP policy, BCP policy — owned in P07 with version control; P08 shows status and next review dates.

**FR-P08-54 — Three lines of defence map.** For each risk and control: first-line owner, second-line oversight function, third-line assurance (last audit date and rating from P10). Gaps (no second line, no audit coverage in 3 years for a High residual risk) appear as findings on the CRO dashboard.

**FR-P08-55 — Model inventory (governance only).** Model register: model id, purpose (credit scoring, ECL, pricing, ALM behaviour, fraud, AML, AI/LLM including Vidhi features used by the tenant), owner, developer (in-house / vendor / Finbyx), risk tier, validation dates and results, approval body, monitoring metrics, status (active / inactive / decommissioned; decommissioned retained ≥ 10 years). Aligned to RBI draft Guidance on Regulatory Principles for Model Risk Management, 2026 (press release 24 Jun 2026; draft — [VERIFY] final) — rule pack flag `erm.model_risk.rbi_2026_guidance.enabled = OFF` until final. Validation reports to RMC within 3 months (draft expectation) as a configurable timer.

### 4N. Faster, smarter and more configurable risk management *(v1.1)*

**FR-P08-56 — Coexisting methodology versions (IMP-123).** A tenant may run more than one approved methodology version at a time (for example "Methodology 2025 — 5 × 5, max-impact" for existing risks and "Methodology 2027 — 6 × 6, weighted impact with a climate dimension" for new business lines). Each assessment records the methodology version it used and is never silently re-scored. A **re-rating wizard** converts selected risks from v1 to v2: it proposes a mapped rating using the published translation table (old band → new band), shows the before/after heat map, requires the risk owner's confirmation per risk (or a bulk confirmation with reason for unchanged items) and writes a new assessment with reason `METHODOLOGY_MIGRATION`. Board-level reports show one methodology at a time with a footnote for any risk still on the older version. Settings: `erm.methodology.max_active_versions` (T, default 2).

**FR-P08-57 — AI risk suggestions with justification (IMP-124, IMP-125; NN-47, NN-50).** The **Risk Analyst agent** (Appendix AA, role agent for `erm`/`ral`) proposes: (a) candidate risks for a new process, product, branch or entity, drawn from the taxonomy pack, the tenant's loss events and incidents, audit findings, regulatory updates (P05) and peer-anonymous patterns from platform seed content only (never another tenant's data, NN-01); (b) candidate controls and KRIs from the seed libraries; (c) a draft RCSA questionnaire; (d) a draft emerging-risk digest. Every suggestion carries a **justification record** — sources cited (record ids, clause references, seed-library ids), the reasoning summary, model route and prompt hash — stored in `erm.ai_suggestions` and visible on hover as "Why suggested". Suggestions are **never applied automatically**: the risk owner accepts, edits or rejects each one; ratings (inherent, residual, control effectiveness), materiality and acceptance decisions are always set by a human (NN-47). Default autonomy ceiling for the Risk Analyst agent in this module is **L1 (suggest)**; tenants may raise it to **L2 (draft records in DRAFT state)** but never higher (`erm.ai.autonomy_ceiling`, G, max L2). Any field that an AI suggestion populated keeps a field-level provenance flag (`AI_SUGGESTED_ACCEPTED`, `AI_SUGGESTED_EDITED`) for audit.

**FR-P08-58 — KRI ↔ compliance-issue linkage (IMP-126).** Linkages are configured once on the KRI (`linked_checkpoints[]`, `linked_obligation_refs[]`) and on the checkpoint (`linked_kris[]`):
- A KRI breach episode whose KRI is linked to a regulatory obligation (for example SLS mismatch limits, LCR, concentration limits, CRAR floors) **auto-opens a compliance issue** in P04 (`cmp.issues`, source `KRI_BREACH`) with the citation, owner = compliance owner of the checkpoint, due date = regulatory intimation timeline where one exists; closure of the issue requires the episode to be CURED, ACCEPTED (where acceptance is permitted) or INVALIDATED.
- A compliance instance that ends `not_complied` or `complied_late` on a checkpoint tagged with a risk category creates a **risk observation** on the linked risk (counts toward the "compliance breaches" KRI family and appears in the next RCSA as evidence) and, if the checkpoint is High risk, proposes a loss-event/near-miss record for ORM review.
- Rules are deterministic, Governed at platform level (`erm.link.kri_to_issue.enabled`, `erm.link.noncompliance_to_risk.enabled`) and Tenant-adjustable for which KRI families participate. Duplicate prevention: one open issue per (episode, checkpoint).

**FR-P08-59 — Risk–control–obligation graph (IMP-013).** The control library (FR-P08-21) is the **common control layer**: one control maps to many risks and many checkpoints across instruments and families; one piece of evidence accepted in P04 for that control in a period counts as an operating-effectiveness data point for every mapped risk (each obligation is still reviewed where the law requires its own evidence). SCR-ERM-25 renders the graph (risk ↔ control ↔ checkpoint ↔ instrument clause ↔ evidence ↔ test) with filters, coverage gaps ("risks rated High with no tested key control", "obligations whose only control has failed its last test", "controls mapped to repealed clauses" — NN-55) and one-click remediation tasks. The graph is exportable as CSV edge lists and an XLSX coverage matrix (LDC-EXPORT folder `08 Risk Management/<FY>/Control Coverage/`).

**FR-P08-60 — Continuous control monitoring (CCM) hooks.** Automated control tests come from: P04 automated checkpoints (data-driven tests on connected sources, IMP-015–018), P12 technical control monitors (MFA coverage, patch age, backup success, access reviews), Finbyx `ControlTestResultPublished` (population, exceptions, masked sample ids) and Udofin LSP controls. Each test result posts to `erm.control_test_results` with population, sample, exceptions, threshold and pass/fail. Rules:
- A failed **automated** test on a key control moves the control's operating-effectiveness flag to `UNDER_REVIEW`, notifies the control owner and creates a re-assessment task for linked risks; the residual rating itself changes only when a human re-assesses (NN-47).
- Three consecutive passes over the test frequency clear `UNDER_REVIEW` automatically (deterministic rule, logged).
- CCM coverage % (key controls with automated tests ÷ key controls) is a KRI (`KRI-OPR-011`, Appendix H §H.8.4 *(v1.1)*).

**FR-P08-61 — Deterministic early-warning signals (EWS).** An EWS card is raised when any configured trigger fires; EWS are **signals, not ratings**:

| Trigger family | Default rule (Tenant-adjustable within floors) | Sources |
|---|---|---|
| Threshold proximity | KRI within 10% of its red threshold and trending adverse for 2 observations | KRI engine |
| Velocity | KRI moves by ≥ 2 RAG bands within one period, or slope over last 3 observations exceeds the configured rate | KRI engine |
| Regulatory change | P05 Update affecting obligations linked to a risk rated High+ | P05 |
| Incident cluster | ≥ 3 incidents/loss events of the same Level-2 type in 30 days | P08 §4G, P12 |
| Complaint spike | Complaint volume in a category ≥ 150% of 3-month average | P14 |
| Audit repeat | Same root cause found in two consecutive audits | P10 |
| Funding/market | Spread, rating or top-lender signals from Finbyx risk events | Finbyx, P09 |
| Fraud EWS | Finbyx/Udofin red-flagged accounts per the Fraud Risk Management Directions 2026 (RBI/DoS/2026-27/463) EWS framework [VERIFY para] | Finbyx |

EWS cards route to the risk owner and appear on the CRO home (P28 widget `W-RSK-07` *(v1.1)*). The CRO can promote an EWS to an issue, an emerging risk or an ad hoc RCSA in one click. EWS rules are effective-dated rule packs (P02) with golden test cases.

**FR-P08-62 — Starter kits (one-click set-up).** For each taxonomy pack the platform ships a **starter kit**: seed risk register (30–60 risks with statements, default owners by role, inherent-rating guidance), control set mapped to the family's checkpoints, KRI set (from §H.8), RAS template with regulatory floors pre-filled, RCSA template, RMC pack template. Installation shows a preview with counts and conflicts, runs as one batch reversible within the undo window (NN-49) and assigns owners using the HRMS org chart (P13) where role holders exist; unmapped owners go to a "needs owner" queue. Typical NBFC-ML set-up target: risk register, KRIs and RAS draft ready in ≤ 2 hours.

**FR-P08-63 — Group and multi-currency consolidation.** In group mode (P15), the CRO of the parent sees a consolidated register (de-duplicated by taxonomy node with entity drill-down), a consolidated RAS where the Board sets group metrics, and group KRIs computed from entity values. Monetary values are converted to the group reporting currency at the snapshot FX rate from `FX_RATE_PORT` (P25) with rate source and date shown; ratios are never averaged across entities unless the metric definition says how (sum of numerators ÷ sum of denominators). Entities in other regional cells contribute **aggregates only** (NN-24 amended); drill-down into a foreign entity's records requires a user with a role in that entity's home cell.

**FR-P08-64 — International taxonomy packs (later).** Foreign subsidiaries use `TAX-INTL-CORP` (corporate ERM, ISO 31000/COSO) from P25 jurisdiction packs; prudentially regulated foreign subsidiaries (banks, finance companies, insurers) receive country packs mapping local Basel/IFRS 9 implementations when a reviewed jurisdiction pack exists (NN-53). Until then the subsidiary runs `TAX-INTL-CORP` with a banner "local prudential pack not available".

**FR-P08-65 — Dashboards and packs via P28 (D-47).** P08 publishes its datasets and metrics to the P28 semantic layer (`rpt.datasets`: risk register, assessments, KRIs, episodes, losses, issues, controls, EWS) and registers widgets W-RSK-01…07. The CRO home (FR-P08-45) and the RMC pack builder (FR-P08-42) are rendered by P28; P08 keeps the business rules (which sections are mandatory per family, freeze rules).

**FR-P08-66 — Faster day-to-day work.**
- *Bulk re-assess* (select risks → apply "no change" or a rating delta with reason) with preview and undo window (NN-49).
- *Inline grid editing* of owner, review date, trend and treatment status with keyboard navigation.
- *Copy from last cycle* for RAS, RCSA campaigns and committee packs, with a diff of what changed in the data.
- *One-click refresh* of a KRI's value from its source when a feed is late (records the manual refresh).
- *Templates for issues and action plans* per root-cause type; the Risk Analyst agent drafts an action plan (owners suggested from the org chart, dates) for the issue owner to approve (IMP-055).
- *Saved views and subscriptions* (weekly e-mail of "my risks with movement") handled by P28.

**FR-P08-67 — Tenant customisation.** Without a super admin a tenant can: add custom fields to risks, controls, KRIs, loss events and issues (P02 form builder; type, mandatory flag, picklists, visibility by role); define additional impact dimensions; rename and reorder L2/L3 nodes; set its own RCSA stage sequence (e.g., add a department-head sign-off) within the SoD guard-rails; create **custom risk registers** (for example "Project risks", "IT change risks") with the P02 custom-register builder (IMP-060), which automatically registers export mapping (NN-10); and choose notification budgets per role (P04 fatigue settings). Regulatory floors, Level-1 taxonomy and canonical breach states remain Locked/Governed.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P08-X01 — Legal and climate risk feeds.** P26 publishes legal-risk KRIs (count and value of Critical matters, provision trend, open regulator observations past due) and P27 publishes climate and ESG risks (physical and transition risk scores, financed-emission trend where Finbyx supplies it) as `risk_metric_value` inputs; they enter the register as KRIs with owners, thresholds and the regulatory floors of NN-38.

---

## 5. Workflows and state machines

Canonical definitions live in Appendix A; the P08-specific machines are below. Every transition writes an audit-ledger event (NN-02) and, where marked, a domain event (§7.4).

### 5.1 Risk framework version

`DRAFT → IN_REVIEW (checker) → RMC_RECOMMENDED → BOARD_APPROVED → EFFECTIVE → SUPERSEDED`. Return paths to `DRAFT` with comments from any review step. Guard: `BOARD_APPROVED` requires a P06 minute reference or an uploaded certified extract. Scale changes in a new version require a score-mapping table before `IN_REVIEW`.

### 5.2 RAS version

`DRAFT → SECOND_LINE_REVIEWED → CONCURRED (CFO, CCO; configurable) → RMC_RECOMMENDED → BOARD_APPROVED → EFFECTIVE → SUPERSEDED`. Guards: every regulatory metric limit passes the floor check (FR-P08-11); every cascade child sums within its parent (additive metrics); effective date ≥ approval date (back-dating only through a Correction Entry, D-02). On `EFFECTIVE`, new threshold versions are emitted (`RasThresholdApproved`) for Finbyx to consume via `GET /v1/grc/kris` (Ecosystem Spec §6.22).

### 5.3 Risk register entry

`DRAFT → SUBMITTED → APPROVED (second line) → ACTIVE ⇄ UNDER_REVIEW → RETIRED`. Re-assessment from `ACTIVE` creates a new assessment row; `UNDER_REVIEW` is entered automatically by triggers (FR-P08-18) and exits when the owner confirms or re-rates and the reviewer approves. `RETIRED` requires reason and keeps history (NN-29).

### 5.4 RCSA campaign

```
PLANNED → LAUNCHED → IN_PROGRESS → (per unit: NOT_STARTED → DRAFT → SUBMITTED → CHALLENGED ⇄ RESUBMITTED → ACCEPTED)
        → REVIEW_COMPLETE → FINALISED (ratings written to register) → CLOSED
```
Timers: reminders at T−7, T−3, T−1 days; overdue units escalate to the department head at T+1 and to the CRO at T+5 (Tenant setting). Campaign cannot be `FINALISED` with units in `CHALLENGED` unless the CRO records an override with reason.

### 5.5 KRI / limit breach episode (Appendix A §A.7)

| Step | State | Owner | Default timer | Rule |
|---|---|---|---|---|
| 1 | `OPEN` | System | on observation | Red value or inbound `KriBreached`/`LimitBreached` status OPEN |
| 2 | `NOTIFIED` | System | immediate | KRI owner + CRO; RMC chair for regulatory-linked; channels in-app, e-mail, Teams/Google Chat (P04); breaches ignore quiet hours |
| 3 | `ACTION_PLANNED` | Owner | 5 working days | Root cause, actions, expected cure date; no plan → escalate one level |
| 4 | `CRO_REVIEWED` | CRO | 5 working days | Accept, send back, escalate to RMC, convert KRI breach to RAS limit breach |
| 5 | `IN_REMEDIATION` | Owner | per KRI run | Missed cure date escalates owner → CRO → RMC chair → Board |
| 6 | `CURED` | System, CRO confirms | cure rule | 1 non-red (3 for daily); for inbound episodes, `status = CURED` from producer |
| Exception | `ACCEPTED` | RMC | ≤ 6 months | Not allowed for regulatory limits |
| Exception | `INVALIDATED` | System | on restatement | Restatement reference kept |

Regulatory-reporting sub-task (where the limit citation requires intimation): `DRAFTED → REVIEWED (CCO) → SENT_BY_TENANT (evidence uploaded) → ACKNOWLEDGED`. LDC never sends (NN-08).

### 5.6 Loss event

`REPORTED → TRIAGED (ORM) → UNDER_INVESTIGATION → VALIDATED (checker) → ACCOUNTED (accounting date linked) → CLOSED`; later recoveries create version n+1 (`RECOVERY_UPDATED`). Near misses skip `ACCOUNTED`. Sealed events (internal fraud under investigation) are visible only to the ORM lead, CRO and named investigators (NN-13).

### 5.7 Issue and action

`OPEN → PLAN_APPROVED → IN_PROGRESS → READY_FOR_VALIDATION → VALIDATED (second line) → CLOSED`; `OVERDUE` is a derived flag with escalation; reopened by a failed re-test.

### 5.8 Risk acceptance

`REQUESTED → APPROVED (authority per matrix) → ACTIVE → EXPIRING (T−30) → EXPIRED (reopens risk) | RENEWED | WITHDRAWN`.

### 5.9 RMC pack

`DRAFT → IN_REVIEW (section owners submit; CS completeness check) → FROZEN (hash) → DISTRIBUTED (read receipts) → DISCUSSED (minute ref) → SUPERSEDED (addendum or restatement)`. Default timers: freeze 7 days before the meeting; distribute ≥ 7 days before Board meetings (SS-1 notice of agenda, P06) [REC].

### 5.10 Pseudo-code — residual and RAS evaluation

```ts
function evaluateRisk(risk, controls, framework): RiskRating {
  const inherent = score(risk.likelihood, maxImpact(risk.impacts, framework.impactAggregation));
  const tested = controls.filter(c => c.lastTest && withinFrequency(c.lastTest, c.frequency));
  if (tested.length === 0 && risk.proposedResidual < inherent) throw err('LDC-ERM-014');
  const computed = applyControlFactors(inherent, tested, framework.controlFactorTable);
  return { inherent, computed, final: risk.override ?? computed, needsApproval: risk.override !== undefined };
}

function evaluateRasMetric(value, levels, polarity): RAG {
  // levels: { appetite, tolerance, limit } typed with polarity; regulatory floor checked at approval time
  if (breaches(value, levels.limit, polarity)) return 'RED';
  if (breaches(value, levels.tolerance, polarity)) return 'AMBER';
  return 'GREEN';
}
```

---

## 6. Screens and UX

Menu (tenant app `apps/web`): **Risk** (top-level, visible when the `erm` module is entitled). Screen IDs are registered in Appendix C.

| Screen ID | Name | Menu path | Key content and actions | Fewer-click design |
|---|---|---|---|---|
| SCR-ERM-01 | CRO Home | Risk › Home | Widgets per FR-P08-45; approvals panel; feed health | Opens on the CRO's saved view; `G R` keyboard shortcut |
| SCR-ERM-02 | Framework & applicability | Risk › Framework | Active framework version, scales, matrix editor, taxonomy tree, "Why is this on?" panel | Tree editing in place; drag to reorder L2/L3 |
| SCR-ERM-03 | Risk appetite | Risk › Appetite | RAS versions, statements, metrics with three levels, cascade tree with utilisation, compare versions, submit for approval | Inline floor check as you type; copy last year's RAS |
| SCR-ERM-04 | Risk register | Risk › Register | Grid (filters: taxonomy, entity, department, owner, residual, trend, status, appetite breach); saved views; bulk actions (assign owner, set review date, export, launch RCSA for selection) | Inline edit of owner/review date; side panel detail |
| SCR-ERM-05 | Risk detail | Risk › Register › [risk] | Statement, ratings (inherent/computed/final), history chart, controls, KRIs, obligations, findings, incidents, loss events, actions, acceptance, bow-tie, documents, audit trail tab | "Re-assess" wizard of 3 steps |
| SCR-ERM-06 | Controls | Risk › Controls | Shared control library; test results timeline; coverage map (risks without controls, controls without tests) | Link from risk detail in one click |
| SCR-ERM-07 | RCSA campaigns | Risk › RCSA | Campaign list, builder (template → scope → respondents → schedule), progress funnel | Launch from template in ≤ 10 clicks |
| SCR-ERM-08 | RCSA response | Risk › RCSA › My assessments | One page per risk; previous answers; evidence attach; bulk "no change" with confirmation | Autosave; keyboard `→` next risk |
| SCR-ERM-09 | Challenge queue | Risk › RCSA › Review | Exceptions-first queue; accept/challenge/escalate | Bulk accept unchanged items with reason |
| SCR-ERM-10 | KRI library | Risk › KRIs | Definitions, thresholds versions, data source and provenance, applicability | Add KRI from seed library |
| SCR-ERM-11 | KRI monitor | Risk › KRIs › Monitor | Heat map by category, trend charts, breach episodes (saved views: Open, Awaiting plan, Awaiting CRO review, Accepted, Overdue) | Bulk acknowledge alerts |
| SCR-ERM-12 | Breach episode | Risk › KRIs › [episode] | Timeline, values, plan, CRO review, regulatory sub-task, evidence | Plan template prefilled |
| SCR-ERM-13 | Loss events | Risk › Loss events | List, capture wizard (3 dates mandatory), versions, GL reconciliation | "Report a risk event" quick form from global `+` |
| SCR-ERM-14 | Issues & actions | Risk › Issues | Kanban and list; ageing; validation queue | Drag to change status |
| SCR-ERM-15 | Risk acceptances | Risk › Acceptances | Active, expiring, expired; authority matrix | Renew with diff |
| SCR-ERM-16 | Emerging risks | Risk › Emerging | Radar chart, list, signals, promote to register | Vidhi digest draft |
| SCR-ERM-17 | Committees & packs | Risk › Committees | RMC/ALCO/ITSC/ORC calendar, pack builder, frozen packs, decisions log | Pack from template; auto-bound sections |
| SCR-ERM-18 | Disclosures | Risk › Disclosures | Pillar 3 / notes / board report items, bound tables, review | Copy previous period |
| SCR-ERM-19 | Risk governance | Risk › Governance | CRO register, in-camera tracker, three-lines map, policy status, product vetting queue | — |
| SCR-ERM-20 | Model inventory | Risk › Models | Register, validation schedule, tier | — |
| SCR-ERM-21 | Feed health | Risk › Data feeds | Inbound events by source, lag, breaks, rejected items, manual-entry queue | Replay request to Finbyx (P18) |
| SCR-ERM-22 | Quick RCSA (small tenants) | Risk › Quick assessment | ≤ 25 questions; one-page report | Single page |
| SCR-ERM-23 | Risk owner home | Home (risk owner role) | My risks, my actions, my RCSA, my breaches | Default for `ten_dept_head` |
| SCR-ERM-24 | Board risk view | Board › Risk | One-page RAS RAG, top risks, breaches, approvals | Read-only, print-ready |

Empty states explain the next step ("No KRIs yet — add from the NBFC-ML seed library (31 KRIs) or upload values"). Error states name the failed guard and the citation (for example `LDC-ERM-021: Tier 1 limit 9.5% is looser than the regulatory minimum 10% — NBFC Capital Adequacy Directions 2025, para 6(2)`). Every page header has an "i" button with the glossary key (`hlp.erm.<screen>`), and terms such as *inherent risk*, *residual risk*, *KRI*, *RAS*, *tolerance*, *RCSA*, *bow-tie*, *velocity* have tooltips (P23).

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Key content and actions | Fewer-click design |
|---|---|---|---|---|
| SCR-ERM-25 | Risk–control–obligation graph | Risk › Controls › Coverage graph | Graph and matrix views; gap filters; create remediation task | Gap filters pre-set; one click from gap to task |
| SCR-ERM-26 | Early-warning console | Risk › Early warnings | EWS cards by trigger family, source, age; promote to issue / emerging risk / ad hoc RCSA | Promote in one click with prefilled form |
| SCR-ERM-27 | Starter kit installer | Risk › Framework › Starter kit | Kit preview (counts, conflicts, owner mapping), install, undo | Single "Install" with undo |
| SCR-ERM-28 | Group risk view | Risk › Group | Consolidated register, group RAS, entity contribution table, FX note | Entity switcher retains filters |
| SCR-ERM-29 | Methodology versions | Risk › Framework › Methodologies | Versions, translation table, re-rating wizard, coexistence status | Wizard pre-maps bands |
| SCR-ERM-30 | AI suggestions inbox | Risk › Suggestions | Risk Analyst proposals with "Why suggested", accept/edit/reject, bulk reject | Keyboard accept/reject (`A`/`R` with modifier) |

---

## 7. Backend design

### 7.1 Modules touched

`erm` (owner), `wf` (tasks, approvals, timers), `gov` (committees, minutes), `dms` (evidence), `cfg` (settings, rule packs, taxonomy packs), `int` (inbound risk events), `rpt` (widgets, packs), `ai` (Vidhi drafts), `cmp` (obligation and control links), `aud` (findings), `dpc`/`tpr` (incident and vendor signals), `hr` (people metrics).

### 7.2 Tables (schema `erm`; all with `tenant_id`, `legal_entity_id`, `created_*`, `updated_*`, RLS)

| Table | Key columns |
|---|---|
| `risk_framework` | id, version, methodology jsonb, scale_set_id, matrix jsonb, materiality jsonb, impact_aggregation, owner_user_id, board_approval_ref, valid_from, valid_to, state |
| `taxonomy_pack` (platform, content plane) | code, version, entity_families[], nodes jsonb, crosswalk jsonb, citations jsonb, effective_from |
| `taxonomy_node` (tenant overlay) | id, pack_code, pack_version, parent_id, level, code, name, definition, basel_map jsonb, owner_role, status, retired_at |
| `risk` | id, code, register_type, title, cause, event, consequence, taxonomy_node_id, department_id, process_id, product_ref, objective, owner_user_id, second_line_user_id, status, confidentiality_class, appetite_metric_id, review_due |
| `risk_assessment` | id, risk_id, valid_from, recorded_at, likelihood, impacts jsonb, inherent_score, computed_residual, final_residual, override_reason, velocity, trend, assessor_id, reviewer_id, campaign_id, evidence_ids[] |
| `control` | id, code, name, objective, type, nature, frequency, owner_user_id, key_control, source (P04/P08/P10/P12), test_procedure, evidence_expectation |
| `risk_control_link` | risk_id, control_id, design_rating, operating_rating, last_test_id |
| `control_test_result` | id, control_id, period, result, tester_id, source, evidence_ids[], test_date |
| `ras` / `ras_statement` / `ras_metric` / `ras_cascade_node` | per FR-P08-10/12 incl. levels jsonb, polarity, regulatory_floor_ref, approval refs |
| `kri` / `kri_threshold_version` / `kri_observation` | metric_id, frequency, polarity, provenance, value numeric(24,8), as_of, rag, threshold_version_id |
| `breach_episode` | id, kind (KRI/LIMIT), kri_id or limit_ref, external_episode_id, external_update_seq, state, opened_at, peak_value, plan jsonb, cure_rule, accepted_until, regulatory_subtask jsonb |
| `rcsa_campaign` / `rcsa_unit_response` / `rcsa_item_response` | template_id, scope jsonb, due, state; responses per risk with ratings, evidence, comments |
| `loss_event` / `loss_event_version` | taxonomy L1–L3, business_line, occurrence_date, discovery_date, accounting_date, gross, recoveries jsonb, net, near_miss, boundary_flags, root_cause, controls_failed[], links jsonb, provenance, sealed |
| `issue` / `action` | source, severity, owner, due, milestones, validation |
| `risk_acceptance` | risk_id, authority_level, rationale, compensating_controls, expires_at, state |
| `emerging_risk` | horizon, likelihood, impact, signals jsonb, state, promoted_risk_id |
| `committee_pack` (shared with P06 `gov`) | template, sections jsonb, freeze_hash, state |
| `disclosure_item` | family_template, period, narrative, bound_table_ref, state, publication_evidence |
| `cro_register`, `in_camera_meeting`, `product_vetting` | per §4M |
| `model_inventory` | per FR-P08-55 |
| `dashboard_view` (shared `rpt`) | user_id, role_template_version, widgets jsonb, filters jsonb, personal_thresholds jsonb |

Numeric values use `NUMERIC` and decimal arithmetic (NN-22). Sealed rows use a separate key and are excluded from `rpt` aggregates except as counts (NN-13).

### 7.3 APIs (REST, versioned `/v1`; OpenAPI 3.1)

| Method & path | Purpose |
|---|---|
| `GET/POST /v1/erm/frameworks`, `POST /v1/erm/frameworks/{id}:submit` | Framework versions |
| `GET /v1/erm/applicability?legal_entity_id=` | Resolver result with citations |
| `GET/POST/PATCH /v1/erm/risks`, `POST /v1/erm/risks/{id}/assessments` | Register and assessments |
| `GET/POST /v1/erm/controls`, `POST /v1/erm/controls/{id}/tests` | Controls and test results |
| `GET/POST /v1/erm/ras`, `POST /v1/erm/ras/{id}:submit` | RAS lifecycle |
| `GET/POST /v1/erm/kris`, `POST /v1/erm/kris/{id}/observations` (bulk, idempotent) | KRIs and values |
| `POST /v1/erm/kris/observations:upload` | Excel template upload with preview/validate/commit |
| `GET /v1/erm/breaches`, `POST /v1/erm/breaches/{id}:plan|:review|:accept` | Episodes |
| `GET/POST /v1/erm/rcsa/campaigns`, `POST /v1/erm/rcsa/responses/{id}:submit|:challenge|:accept` | RCSA |
| `GET/POST /v1/erm/loss-events`, `POST /v1/erm/loss-events/{id}/versions` | Loss data |
| `GET/POST /v1/erm/issues`, `/v1/erm/acceptances`, `/v1/erm/emerging` | Issues, acceptance, emerging |
| `POST /v1/erm/packs`, `POST /v1/erm/packs/{id}:freeze|:distribute` | Committee packs |
| **Ecosystem (Spec §6.22):** `GET /v1/grc/kris?updated_since=` and `GET /v1/grc/obligations?updated_since=` | Served by LDC to Finbyx/Udofin (KRI definitions mapped to metric ids; approved thresholds with LDC approval ref) |
| **Inbound webhook:** `POST /v1/int/events` (P18 gateway) | Receives `in.infrabyx.risk.*` CloudEvents; verifies signature, hash chain (`contenthash`, `prevhash`), idempotency key per §6.22 table |

All write APIs require `Idempotency-Key`; maker-checker endpoints refuse approval by the submitter (NN-05).

### 7.4 Domain events

Outbound (`type = in.lawdocscomply.erm.<Name>.v1`, `source = urn:infrabyx:ldc:<tenantid>`): `RiskRegistered`, `RiskAssessed`, `RiskRetired`, `RasApproved`, `RasThresholdApproved` (consumed by Finbyx/Udofin as threshold versions), `KriDefined`, `KriBreachOpened`, `KriBreachCured`, `LimitBreachEpisodeUpdated`, `RcsaCampaignLaunched`, `RcsaCampaignFinalised`, `LossEventValidated`, `RiskIssueRaised` (maps to Ecosystem `ComplianceIssueRaised` where the tenant's GRC destination expects it), `RiskAccepted`, `RiskAcceptanceExpired`, `RmcPackFrozen` (as `EvidenceSubmitted` to RE GRC destinations in group mode), `ControlTestRecorded`.

Inbound (Ecosystem Spec §6.22, envelope `in.infrabyx.risk.<Name>.v<major>`): `KriBreached`, `LossEventRecorded`, `CapitalRatioComputed` (stored for P09), `LimitBreached`, `StressTestCompleted` (P09), `RiskSnapshotPublished`, `RiskSignalRaised`; from LDC modules: `ComplianceIssueRaised` (P04), `AuditFindingIssued` (P10), `SecurityIncidentNotified`, `VendorRiskChanged`, `PersonalDataBreachRecorded` (P12), `PeopleMetricPublished` (P13), `ComplaintMetricPublished` (P14), `RegulatoryChangeAssessed` (P05).

**Event naming (X-01; review R4).** The outbound names above are LDC-internal (`in.lawdocscomply.erm.*`). Every event that leaves LDC — `RasThresholdApproved` to Finbyx/Udofin, `ComplianceIssueRaised` and `EvidenceSubmitted` to an RE GRC destination, and KRI threshold versions — is re-published by the `int` module under the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (`risk` or `grc` domain) via `int.event_type_map`; `erm` never publishes cross-product events directly.

### 7.5 Jobs and Temporal workflows

| Job / workflow | Schedule | Notes |
|---|---|---|
| `KriEvaluationWorkflow` | on observation; batch nightly 02:00 IST for manual/Excel KRIs | Computes RAG, opens/cures episodes |
| `BreachEscalationWorkflow` | per episode | Timers per §5.5 with business-day calendar (P04 holiday calendars by state) |
| `RcsaCampaignWorkflow` | per campaign | Reminders, escalation, finalisation |
| `RasReviewReminder` | daily | 60/30/7-day reminders; off-cycle triggers |
| `InboundRiskFeedConsumer` | streaming | Signature, hash-chain, idempotency, reconciliation counters |
| `FeedReconciliation` | daily 07:00 IST; monthly sample | Counts and hashes vs producer (Ecosystem §6.22); breaks raise `ReconciliationBreakRaised` and a P18 integration incident |
| `AcceptanceExpiry` | daily | T−30 reminder; expiry reopens |
| `EmergingRiskDigest` | quarterly (configurable) | Vidhi draft from P05 Updates |
| `PackFreeze` | on request | Hash computation, PDF/A rendering via Gotenberg |

### 7.6 Backend additions *(v1.1)*

| Table | Key columns |
|---|---|
| `erm.methodology_versions` | methodology_id, version, scale_def jsonb, impact_dimensions jsonb, translation_table jsonb, status, effective_from |
| `erm.ai_suggestions` | suggestion_id, kind (RISK/CONTROL/KRI/RCSA_ITEM/DIGEST/ACTION_PLAN), payload jsonb, sources jsonb, reasoning_summary, model_route, prompt_hash, autonomy_level, state (PROPOSED/ACCEPTED/EDITED/REJECTED), decided_by, decided_at |
| `erm.links` | link_id, from_type, from_id, to_type (CHECKPOINT/OBLIGATION/KRI/RISK/CONTROL), to_id, rule_ref, created_by (RULE/USER) |
| `erm.control_test_results` | result_id, control_id, source (P04_AUTO/P12/FX/UD/P10/MANUAL), period, population, sample_size, exceptions, threshold, outcome, evidence_ref, received_at |
| `erm.ews_cards` | ews_id, trigger_family, rule_version, subject_type, subject_id, signal_values jsonb, state (OPEN/PROMOTED/DISMISSED/EXPIRED), owner_id |
| `erm.starter_kits` / `erm.kit_installations` | kit_code, pack_code, version, contents jsonb / installation_id, batch_id (undo), counts, conflicts, state |

APIs: `POST /v1/erm/methodologies/{id}/rerate` · `GET/POST /v1/erm/suggestions` · `POST /v1/erm/suggestions/{id}:accept|edit|reject` · `GET /v1/erm/graph?root=` · `POST /v1/erm/control-tests` (inbound automated results) · `GET /v1/erm/ews` · `POST /v1/erm/ews/{id}:promote` · `POST /v1/erm/starter-kits/{code}:install` · `POST /v1/erm/batches/{id}:undo` · `GET /v1/erm/group/register`.

Events (internal `in.lawdocscomply.erm.*`): `SuggestionProposed`, `SuggestionDecided`, `ControlUnderReview`, `EwsRaised`, `EwsPromoted`, `StarterKitInstalled`, `BatchUndone`, `KriIssueLinked`. Cross-product: none new (inbound `ControlTestResultPublished` per Ecosystem Spec §9.2).

Jobs: `ews-evaluator` (after each KRI observation and nightly), `ccm-ingest` (stream), `group-consolidation` (nightly and on demand).

---

## 8. Integrations (ports and adapters)

| Port | Adapter(s) | Direction | Contract |
|---|---|---|---|
| `RISK_FEED_PORT` | Finbyx, Udofin (Ecosystem Spec §6.22); third-party LMS via P18 generic connector | Inbound | CloudEvents 1.0.2 with `asof`, `metricversion`, `citation`, `contenthash`, `prevhash`; HMAC-pseudonymised counterparty refs (LDC cannot reverse — by design) |
| `GRC_PULL_API` | Finbyx, Udofin | Outbound (served) | `GET /v1/grc/kris`, `GET /v1/grc/obligations` |
| `SIEM_PORT` / `VULN_PORT` | via P12 | Inbound (aggregates) | Counts and severities for cyber KRIs |
| `HR_METRICS_PORT` | P13 internal; external HRMS via P18 | Inbound | Aggregated people metrics only (no individual data in ERM, NN-13) |
| `ACCOUNTING_PORT` | P11 accounting bridge (Tally Prime, Excel TB, Finbyx GL) | Inbound | GL write-off/expense accounts for loss reconciliation |
| `NEWS_FEED_PORT` | Approved news/regulatory sources (P05) | Inbound | Headlines with URLs for emerging-risk signals |
| `BOARD_PORTAL_PORT` | P06 | Outbound | Frozen packs |
| `WORKSPACE_PORT` | M365 (Teams/Outlook), Google Workspace (P18) | Outbound | Alerts and calendar holds for committee meetings |
| `EXPORT_PORT` | P19 | Outbound | LDC-EXPORT-1.0 folders: `08 Risk Management/<FY>/<Register|RCSA|KRIs|Loss Events|Committee Packs|Risk Appetite>` (Appendix M) |

Group mode (`LDC_GROUP`): one LDC instance per Infrabyx `group_id` or customer group; every record tagged with `reid`/`legal_entity_id`; group roll-up views aggregate by legal entity with drill-down permissions per entity (Ecosystem Spec §9.1).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `erm.framework.scale_size` | T | 5 | 3–6 | CRO (maker-checker) |
| `erm.framework.impact_aggregation` | T | `MAX` | MAX / WEIGHTED | CRO |
| `erm.framework.severity_bands` | T | 1–4/5–9/10–15/16–25 | Monotonic, cover full range | CRO |
| `erm.taxonomy.level1` | L | Pack-defined | — | Platform content team |
| `erm.taxonomy.level2_3` | T | Pack seed | Retire, never delete with history | CRO |
| `erm.residual.control_factor_table` | T | §FR-P08-08 | Cannot reduce without tested control | CRO |
| `erm.residual.override_requires_approval` | G | true | true only | — (floor) |
| `erm.ras.levels` | T | appetite/tolerance/limit | Limit ≥ regulatory floor | Board via workflow |
| `erm.ras.review_cycle_months` | T | 12 | 6–24 | CRO |
| `erm.ras.reminder_days` | T | 60,30,7 | — | CRO |
| `erm.ras.concurrence_roles` | T | CFO, CCO | Any KMP | Tenant admin |
| `erm.rcsa.cadence_default` | T | ANNUAL | QUARTERLY–BIENNIAL | CRO |
| `erm.rcsa.cadence_high_residual` | T | SEMI_ANNUAL | ≤ ANNUAL | CRO |
| `erm.rcsa.self_effective_requires_evidence` | G | true | true only | — |
| `erm.kri.plan_sla_wd` | T | 5 | 1–15 | CRO |
| `erm.kri.cro_review_sla_wd` | T | 5 | 1–15 | CRO |
| `erm.kri.cure_rule_default` | T | 1 (3 daily) | 1–6 | CRO |
| `erm.kri.acceptance_max_months` | G | 6 | ≤ 6 | — |
| `erm.kri.personal_threshold_direction` | L | tighter_only | — | — |
| `erm.loss.capture_sla_wd` | T | 5 | 1–30 | ORM lead |
| `erm.loss.reporting_threshold_inr` | T | 0 | ≥ 0 | ORM lead |
| `erm.loss.three_dates_required` | G | true | true only | — |
| `erm.acceptance.authority_matrix` | T | High→CRO; Critical→RMC | Regulatory limits non-acceptable (L) | Board |
| `erm.acceptance.max_months` | T | 12 | ≤ 12 | Board |
| `erm.pack.freeze_days_before` | T | 7 | 2–21 | CS |
| `erm.pack.require_certified_regulatory_metrics` | G | true | indicative-with-reason exception only | — |
| `erm.emerging.digest_frequency` | T | QUARTERLY | MONTHLY–ANNUAL | CRO |
| `erm.feed.reconciliation_time` | T | 07:00 IST | — | Integration admin |
| `erm.model_risk.rbi_2026_guidance.enabled` | G | OFF | ON after final issued | Platform content (rule pack) |
| `erm.dashboard.template_change_requires_approval` | G | true | — | — |
| `erm.quick_rcsa.enabled` | T | true for CORP/LLP/COOP packs | — | Tenant admin |

All keys registered in Appendix U; every change audited and reversible (NN-28).

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `erm.methodology.max_active_versions` | T | 2 | 1–3 | CRO |
| `erm.ai.autonomy_ceiling` | G | L1 | L0–L2 | CRO with `ten_admin`; platform floor L0 |
| `erm.ai.suggestions.enabled` | T | ON | ON/OFF | CRO |
| `erm.link.kri_to_issue.enabled` | G | ON | ON/OFF | Platform (Governed); tenant chooses KRI families |
| `erm.link.kri_to_issue.families` | T | regulatory-limit KRIs | any subset | CRO, CCO |
| `erm.link.noncompliance_to_risk.enabled` | T | ON | ON/OFF | CRO |
| `erm.ccm.consecutive_passes_to_clear` | T | 3 | 2–6 | CRO |
| `erm.ews.proximity_pct` | T | 10% | 5–25% | CRO |
| `erm.ews.incident_cluster` | T | 3 in 30 days | 2–10 / 7–90 days | CRO |
| `erm.ews.complaint_spike_pct` | T | 150% | 120–300% | CRO, GRO |
| `erm.group.reporting_currency` | T | INR | ISO 4217 | Group CRO |
| `erm.group.fx_rate_source` | G | RBI reference rate / FBIL | provider list (P25 `FX_RATE_PORT`) | Platform |
| `erm.bulk.undo_window_hours` | T | 24 | 1–72 | `ten_admin` |

---

## 10. Security, privacy and audit

- **Isolation and scope:** RLS by `tenant_id`; ABAC by `legal_entity_id`, `department_id`, `confidentiality_class`, committee membership. Directors see only packs of committees they sit on.
- **Sealed classes:** internal-fraud investigations, whistle-blower-linked risks, POSH-linked people incidents (only counts flow from P13), board-confidential strategy risks — separate KMS key, named-user access, excluded from analytics, exports only with CRO approval (NN-13).
- **No account-level PII:** inbound risk feeds carry HMAC pseudonyms and banded amounts; schema tests reject names, PAN, phone, e-mail, account numbers, Aadhaar (Ecosystem §6.22; NN-12, NN-23).
- **Audit:** every create/update/approve/acceptance/threshold change/pack freeze writes a hash-chained ledger event (NN-02); Correction Entries for back-dated or erroneous ratings (D-02). The "Audit trail" tab on each record shows who, what, when, before/after, reason, source (UI, API, trigger, Vidhi draft accepted by user X).
- **Supervisor and auditor access:** time-boxed read-only grants (D-12, NN-18) with watermarked exports; access events logged and visible to the tenant.
- **Retention:** risk records and loss data retained ≥ 10 years by default (Tenant setting, floor from rule pack — e.g., model inventory decommissioned models ≥ 10 years per RBI draft MRM guidance [VERIFY]); legal holds supported (P07/P19).
- **Exports:** watermark with user, time, certification state; sealed sections excluded unless approved.

---

## 11. AI touchpoints and guardrails (Vidhi; Appendix K)

| Touchpoint | What Vidhi does | Guardrail |
|---|---|---|
| Risk statement drafting | Turns free text into cause–event–consequence; suggests taxonomy node, controls and KRIs from the pack | Draft only; user accepts/edits; suggestion source shown (pack id, similar risks) |
| RCSA questionnaire | Drafts items from register and last cycle | Reviewer approves the questionnaire version |
| Breach action plan | Suggests root-cause prompts and actions from similar episodes in the same tenant | Tenant-only retrieval (NN-01, NN-15) |
| Pack narratives | Drafts executive summary, movements commentary from frozen values | Numbers are inserted by binding, never typed by the model; every claim links to a value or record |
| Emerging-risk digest | Summarises P05 Updates and approved news with citations | Citations mandatory; "no source → no statement" (NN-06) |
| Disclosure narrative | Drafts Pillar 3/board-report risk text from register and frozen tables | Human review; regulatory template structure enforced |
| Q&A ("Ask Vidhi about our risks") | Answers from the tenant's register, RAS, packs, policies and regulator notebooks | Role-aware retrieval; refuses outside scope; logs prompt, sources, output (NN-14) |

Vidhi never rates a risk, approves, accepts a risk, changes thresholds or sends regulatory intimations (NN-14). Deterministic fallback: every workflow is fully usable with Vidhi disabled.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p08/*.feature`)

```gherkin
Feature: Entity-family applicability
  Scenario: NBFC-ML tenant gets the NBFC pack and RMC
    Given a tenant profile "NBFC-ICC", layer "ML", deposit-taking false, last audited assets 2400 crore
    When the applicability resolver runs
    Then taxonomy pack "TAX-NBFC" is enabled with level-1 category "Liquidity and funding"
    And "Risk Management Committee" is required with citation "GOV para 9"
    And "Chief Risk Officer" is shown as "not mandatory (assets ≤ ₹5,000 crore)" with citation "GOV para 19"

  Scenario: Private limited company gets no prudential categories
    Given a tenant profile "Private limited company", unlisted
    When the applicability resolver runs
    Then pack "TAX-CORP" is enabled
    And no node of category "Capital and solvency" or "IRRBB" is visible

Feature: Risk appetite floors
  Scenario: Limit looser than regulation is rejected
    Given an NBFC-ML tenant drafting RAS metric "Tier 1 ratio"
    When the CRO sets the limit to 9.5%
    Then the save fails with "LDC-ERM-021" citing "RBI/DOR/2025-26/345 para 6(2)"

  Scenario: RAS approval flows to Finbyx as a threshold version
    Given RAS v3 is approved by the Board with minute reference "BM-2026-11-04/7"
    When RAS v3 becomes effective
    Then event "RasThresholdApproved" is emitted
    And GET /v1/grc/kris returns the new threshold version with LDC approval reference

Feature: KRI breach from Finbyx
  Scenario: Inbound KriBreached opens one episode and cures it
    Given Finbyx sends KriBreached for kri "KRI-CRD-004" episode "E1" update_seq 1 status OPEN
    When the same event is delivered twice
    Then exactly one breach episode exists in state "NOTIFIED"
    When Finbyx sends KriBreached episode "E1" update_seq 2 status CURED
    Then the episode state is "CURED" and the history shows both updates

  Scenario: No action plan escalates
    Given an open KRI breach owned by "Head Collections" with plan SLA 5 working days
    When 5 working days pass without a plan
    Then the episode escalates to the CRO and a Notification is sent

Feature: Residual guard
  Scenario: Residual lower than inherent without tested controls
    Given a risk with inherent score 20 and no tested controls
    When the owner proposes residual score 9
    Then the save fails with "LDC-ERM-014"

Feature: RCSA
  Scenario: Self-rating "effective" requires evidence
    Given an RCSA item for control "CTL-OPS-011" with no test result in the last 12 months
    When the respondent rates the control "Effective" without evidence
    Then submission is blocked with message "Attach evidence or a test result"

Feature: Loss events
  Scenario: Three dates mandatory
    Given a loss event with occurrence and discovery dates but no accounting date
    When the ORM checker tries to validate it as an accounted loss
    Then validation fails with "LDC-ERM-041"

  Scenario: Recovery is a new version
    Given validated loss event "LE-2026-0042" net loss ₹12,00,000
    When an insurance recovery of ₹5,00,000 is recorded
    Then version 2 shows net loss ₹7,00,000 and version 1 is unchanged

Feature: Regulatory limit cannot be accepted
  Scenario: LE breach acceptance blocked
    Given an open limit-breach episode with limit_type "LE"
    When the RMC tries to accept it
    Then the action fails with "LDC-ERM-031"

Feature: Pack integrity
  Scenario: Frozen RMC pack verifies
    Given an RMC pack frozen on 2026-11-01
    When any bound KRI value is restated afterwards
    Then the frozen pack hash still verifies and the pack shows "Superseded by restatement — addendum available"
```

NN tests in this phase: `NN-01_erm_cross_tenant`, `NN-02_erm_ledger_chain`, `NN-05_erm_maker_checker`, `NN-07_erm_bitemporal_assessment`, `NN-13_erm_sealed_fraud_event`, `NN-14_vidhi_cannot_rate_or_accept`, `NN-21_erm_heatmap_text_alternative`, `NN-22_ras_floor`, `NN-23_risk_feed_no_pii`, `NN-28_erm_settings_registered`, `NN-29_retired_node_keeps_history`.

```gherkin
# v1.1 scenarios
Feature: Methodology coexistence (v1.1)
  Scenario: Re-rating keeps history
    Given risk R-101 assessed under methodology 2025 v1 as "High (15)"
    And methodology 2027 v1 is approved with a translation table mapping 15 to 22 on a 6x6 scale
    When the risk owner runs the re-rating wizard and confirms
    Then a new assessment exists under methodology 2027 with reason "METHODOLOGY_MIGRATION"
    And the 2025 assessment remains visible and unchanged in history

Feature: AI suggestions never set ratings (NN-47, NN-50)
  Scenario: Suggested risk is accepted without a rating
    Given the Risk Analyst agent proposes risk "Co-lending partner concentration" with sources
    When the risk owner accepts the suggestion
    Then a risk is created in DRAFT with inherent rating empty
    And the field provenance shows "AI_SUGGESTED_ACCEPTED" with the sources list
  Scenario: Autonomy ceiling cannot exceed L2
    When a tenant admin sets "erm.ai.autonomy_ceiling" to "L3"
    Then the change is rejected with error "LDC-ERM-070"

Feature: KRI breach opens a compliance issue (IMP-126)
  Scenario: SLS limit breach
    Given KRI-LIQ-004 is linked to checkpoint "NBFC ALM – 15–30 day mismatch limit"
    When a red observation of 22% is recorded
    Then a breach episode opens
    And exactly one compliance issue is created with source "KRI_BREACH" and the ALM citation
    And the issue cannot be closed while the episode is OPEN

Feature: Continuous control monitoring
  Scenario: Failed automated test flags the control, not the rating
    Given key control C-ACC-07 has an automated test from P12
    When the test fails
    Then the control's operating flag is "UNDER_REVIEW"
    And a re-assessment task exists for each linked risk
    And no residual rating has changed

Feature: Starter kit with undo (NN-49)
  Scenario: Install and undo
    Given a new NBFC-ML tenant with an empty register
    When the CRO installs the "TAX-NBFC ML" starter kit
    Then 52 risks, 41 controls and 31 KRIs are created in one batch
    When the CRO undoes the batch within 24 hours
    Then all created records are reversed by a compensating batch and the ledger shows both

Feature: Group consolidation in other regions (NN-24 amended)
  Scenario: UAE subsidiary contributes aggregates only
    Given a group with an Indian parent and a UAE subsidiary in the GCC cell
    When the group CRO opens the group register
    Then the UAE entity shows aggregate counts and RAG only
    And opening an individual UAE risk requires a role in the GCC cell
```

---

## 13. Deliverables and exit gate

- `erm` module, schema migrations (expand-contract, NN-11), OpenAPI and AsyncAPI specs, seed taxonomy packs (14) and KRI library (172), RAS templates per family, RCSA templates (enterprise, process, quick), RMC/ALCO/ITSC/ORC pack templates, Excel KRI-value template `LDC-DT-KRI-v1.0`.
- Screens SCR-ERM-01 to SCR-ERM-24 with empty/error states, "i" help keys and keyboard shortcuts; role templates for CRO, risk officer, risk owner, RMC member, Board member.
- Inbound Finbyx/Udofin risk-feed consumer certified against the Ecosystem Spec sandbox (P18), with reconciliation job.
- Documentation: `docs/phases/P08-plan.md` (five inventories: settings, events, error codes, approval actions, export mapping), user guide and video script outlines for P23 (RAS setup, RCSA, KRI breach handling, RMC pack).
- **Exit gate:** all §12 scenarios and NN tests green; pilot tenants (one NBFC-ML on Finbyx feed, one listed company without Finbyx, one credit co-operative society in quick mode) complete RAS setup, one RCSA campaign and one RMC pack end to end; WCAG 2.2 AA audit of SCR-ERM-01/04/08/11 passed; export of `08 Risk Management` opens in Excel/Word/PDF readers without LDC.

- *(v1.1)* Methodology versions and re-rating wizard; Risk Analyst agent integration (suggestions with justification); KRI ↔ issue linkage; risk–control–obligation graph; CCM ingestion; EWS rules pack with golden cases; starter kits for all 14 taxonomy packs; group consolidation; SCR-ERM-25 to 30; datasets and widgets registered in P28. **Exit gate addition:** second-period KRI linkage demo (breach → issue → cure → closure), starter-kit install + undo, and an EWS promoted to an ad hoc RCSA on the pilot NBFC-ML tenant.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P08-01 | NBFC Governance Directions 2025 (RBI/DOR/2025-26/344) paras for RMC (9), CRO (19–24), Board reviews (15) | Paragraph numbers taken from Finbyx v1.5 reading; not re-fetched by this stream | Platform content (RBI) | Rule pack ships with citations marked [VERIFY]; resolver shows "pending verification" badge |
| OI-P08-02 | LODR Reg 21 scope (top 1,000 + HVDLE) and Sch II Part D(C) RMC role text as amended to Oct 2026 | Amendments frequent | Platform content (SEBI) | Seed rule with [VERIFY]; Governed key `pack.sebi_listed.rmc_scope` |
| OI-P08-03 | SEBI MF Risk Management Framework — current Master Circular chapter and paras | Citation not verified | Platform content (SEBI) | Pack text generic until verified |
| OI-P08-04 | IRDAI corporate-governance master circular 2024 — RMC/CRO paras; Ind-RBC timeline | Ind-RBC not final | Platform content (IRDAI) | Solvency KRI uses 150% control level (AFIF Regs 2024) |
| OI-P08-05 | RBI ORM Guidance Note — current reference after 28 Nov 2025 consolidation and para numbers 31–33, 42–43 | Two references in circulation (30 Apr 2024; owner baseline DoR.ORG.REC.301) | Platform content (RBI) | Cite both; [VERIFY] |
| OI-P08-06 | RBI Model Risk Management guidance — final version | Draft 24 Jun 2026; comments closed 24 Jul 2026 | Platform content (RBI) | `erm.model_risk.rbi_2026_guidance.enabled = OFF`; inventory available as best practice |
| OI-P08-07 | RBI climate-risk directions/disclosure framework final status | NBFC climate directions still draft (page updated 1 Oct 2026); bank disclosure framework draft Feb 2024 | Platform content (RBI) | Climate category labelled "ICAAP-internal / voluntary" |
| OI-P08-08 | Pillar 3 template list in Commercial Banks Capital Adequacy Directions 2025 Annex III | Not extracted in research | Platform content (RBI) | Disclosure workspace ships generic BCBS DIS structure behind `erm.disclosure.bank_pillar3.enabled = OFF` |
| OI-P08-09 | UCB risk-management governance (RMC, CRO) current RBI instruction | Not verified | Platform content (RBI) | UCB pack marks governance items "best practice" |
| OI-P08-10 | Inbound `KriBreached` episode mapping when the tenant switches compliance mode mid-period | Dual-publish window semantics (Ecosystem §9.1) | Integration lead | Treat producer `episode_id` as master; LDC episodes keyed by (producer, episode_id) |
| OI-P08-11 | ARC risk-governance specifics in ARC Directions 2025 | Reference number and paras not verified | Platform content (RBI) | `TAX-ARC` governance items marked [VERIFY] |
| OI-P08-12 *(v1.1)* | Fraud Risk Management Directions 2026 EWS paragraph (red-flagged accounts framework) | Paragraph not re-fetched | Platform content (RBI) | EWS fraud trigger ships as advisory (NN-38) |
| OI-P08-13 *(v1.1)* | Methodology translation tables between scale sizes | Needs actuarial/risk review | CRO pilot + risk SME | Wizard requires manual confirmation per risk |
| OI-P08-14 *(v1.1)* | FX reference rate source for group consolidation (FBIL vs RBI reference vs provider) | Licensing and coverage | CFO / P25 | Manual rate entry with evidence |
| OI-P08-15 *(v1.1)* | International prudential taxonomy packs (UAE, Singapore, UK) | Requires reviewed jurisdiction packs (NN-53) | P25 content partners | `TAX-INTL-CORP` only |
| OI-P08-16 *(v1.1)* | CCM test catalogue per family (which automated tests are reliable) | Depends on connector availability | P04/P12 owners | Manual tests remain primary |
| OI-P08-17 *(v1.1)* | EWS default thresholds calibration | No tenant history yet | CRO pilots | Defaults labelled [REC] |

---

## 15. Sources (accessed 25 October 2026)

1. RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/345 (28 Nov 2025; updated 1 Jul 2026) — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=12959
2. RBI (NBFC – Asset Liability Management) Directions, 2025, RBI/DoR/2025-26/355 (28 Nov 2025) — https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=12949
3. RBI (Commercial Banks – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/151 (28 Nov 2025; updated 7 Oct 2026) — https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13159
4. RBI (UCB – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/275 — https://rbi.org.in/SCRIPTS/BS_ViewMasDirections.aspx?id=13030
5. RBI (NBFC – Miscellaneous) Supervisory Directions, 2026, RBI/DoS/2026-27/467 (31 Jul 2026) — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13586
6. RBI (NBFC – Fraud Risk Management) Directions, 2026, RBI/DoS/2026-27/463 (31 Jul 2026) — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13590
7. RBI Guidance Note on Operational Risk Management and Operational Resilience (30 Apr 2024) — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12679
8. RBI press release: draft Guidance on Regulatory Principles for Model Risk Management (24 Jun 2026) — https://rbi.org.in/ScriptS/BS_PressReleaseDisplay.aspx?prid=63006
9. RBI draft (NBFC – Climate Finance and Management of Climate Change Risks) Directions, 2025 — https://rbi.org.in/Scripts/BS_ViewREwiseDraftDirections.aspx?id=207
10. RBI (Asset Reconstruction Companies) Directions, 2025 — summary: https://ksandk.com/newsletter/rbi-asset-reconstruction-companies-2025/ [VERIFY against rbi.org.in]
11. IRDAI (Actuarial, Finance and Investment Functions of Insurers) Regulations, 2024 — summary: https://www.oquilia.com/news/irdai-actuarial-finance-investment-functions-regulations-2024
12. Basel Committee, Basel Framework — SRP (Pillar 2) and DIS (Pillar 3) standards — https://www.bis.org/basel_framework/ ; BCBS 239 Principles (2013) and progress report (Nov 2023) — https://www.bis.org/bcbs/publ/d559.htm ; voluntary climate disclosure framework (Jun 2025) — summary https://www.mayerbrown.com/en/insights/publications/2025/06/out-with-a-whimper-bcbs-publishes-climate-disclosure-framework
13. ISO 31000:2018 Risk management — Guidelines; COSO, Enterprise Risk Management — Integrating with Strategy and Performance (2017).
14. Infrabyx Ecosystem Integration Specification v1.1 §6.22 and §9; Finbyx Master Prompt v1.5 Part 7E (RK1–RK8) — owner's corpus.
15. Owner baseline: LawDocs Comply Architecture Part 2 — Risk Registers, Risk Management, IT & Cyber Risk, TPRM.
16. Benchmarks (features only, no text copied): MetricStream Operational Risk Management — https://www.metricstream.com/products/operational-risk-management.htm ; KPMG India ICAAP tool — https://kpmg.com/in/en/services/advisory/consulting/risk-and-finance-advisory/unlocking-value-with-technology/financial-risk.html ; Vinod Kothari, ICAAP for NBFCs (Jul 2025) — https://vinodkothari.com/2025/07/mind-the-gap-plugging-risk-blind-spots-with-icaap-for-nbfcs/

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-38, NN-39; X-16 (`ral.icaap.host`, `ral.stress.fx_mode`), X-25 (risk kernel, D-22), X-36 (people-risk aggregates k ≥ 5).

**Added in v1.1:** NN-47, NN-50; X-43.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
