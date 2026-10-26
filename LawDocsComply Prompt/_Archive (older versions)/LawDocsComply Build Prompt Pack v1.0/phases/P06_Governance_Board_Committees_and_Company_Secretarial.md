# Phase P06 — Governance, Board, Committees and Company Secretarial

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, hash-chained audit ledger, Correction Entries — D-02, NN-02; feature flags; outbox);
> - **P01** (identity, MFA/step-up, roles `ten_*`, legal-entity scoping, ABAC attributes `legal_entity_id`, `committee_id`, `confidentiality_class`);
> - **P02** (settings registry, rule packs for thresholds and due-date rules, terminology overrides — committee and department names are tenant terms);
> - **P04** (task engine, maker-checker, calendar, Notifications inbox; compliance instances that require Board noting);
> - **P07** (DMS, evidence vault, Word generation, eSign envelopes, DSC signing hand-off) — P06 and P07 are built by the same squad in alternating sprints;
> - **P13** (HRMS person master for directors, KMP and employees). Until P13 exits, P06 ships `gov.persons` as a minimal person master and migrates it to the HRMS projection with expand-contract (NN-11).
>
> **Sequencing:** starts after P04 sprint 2; P15 supplies regulator overlays (RBI, SEBI, IRDAI, IFSCA governance rule packs) — P06 builds the overlay engine and seeds the Companies Act, SEBI LODR, RBI NBFC/UCB/commercial bank and IRDAI governance packs as reference data. P10 (secretarial audit) and P16 (co-operative governance) reuse the P06 meeting, register and declaration engines.
>
> **Binding appendices:** A (state machines), B (data model, events, errors), C (screens, menus), D (access matrix), G (legal rules `LR-MCA-*`, `LR-ICSI-*`, `LR-SEBI-*`, `LR-RBI-*`, `LR-IRDAI-*`), J (ICSI Secretarial Standards map), M (export folder taxonomy `05 Governance - Board, Committees and Meetings/…` and `06 Company Secretarial - Registers, Filings and Resolutions/…`), U (settings).
>
> **Requirements covered:** R-009, R-018, R-053, R-054, R-056, R-057, R-066, R-071, R-086, R-092, R-093, R-094 (governance events), R-095, R-099; contributes to R-013, R-021, R-075.
>
> **Estimated effort:** 9 two-week sprints, squad of 8 (governance core 3, meetings and board portal 3, listed-company and filings 2), plus one company-secretary domain analyst (part-time ICSI member) for content and UAT.

---

## 1. Objective and business outcome

Every client of LawDocsComply — a private company, a listed NBFC, an urban co-operative bank, an insurer in GIFT City, an LLP or a society — must run its internal governance the way its constitution, the Companies Act 2013 (or the LLP Act 2008, the Societies Registration Act 1860 or the co-operative law), the ICSI Secretarial Standards and its sector regulator require. Today this lives in Word files, Excel trackers and the company secretary's memory. P06 turns it into a **Governance Operating System**: it composes the entity's governance blueprint from law and regulation, keeps the board, committee and KMP structure compliant as people change, runs every meeting from calendar to sealed minutes, maintains statutory registers from events, prepares ROC and stock-exchange filings, and drafts the annual report from source data — with the company secretary in control and every step evidenced.

| Outcome | Exit-gate measure |
|---|---|
| Governance blueprint generated, not hand-built | For each of the eight seeded entity profiles (private company; unlisted public company above thresholds; listed equity company; NBFC-ML; NBFC-UL; UCB > ₹5,000 crore assets; life insurer; LLP) the blueprint lists required directors, independent directors, woman director, committees, KMP, policies, meeting cadence, registers and filings, each with an `LR-*` citation, and matches the domain analyst's golden blueprint with zero missing mandatory items |
| Composition breaches caught at source | A change in a person's attributes (independence lapses, tenure ends, directorship count exceeds limit, DIN deactivated, fit-and-proper declaration overdue) raises a composition issue on every affected committee within 1 minute, with the rule cited and a remediation task assigned to the CS |
| Meetings with fewer clicks | A quarterly board meeting is scheduled, noticed, packed and published in ≤ 25 clicks by the CS using the standard agenda template and auto-pulled items; the notice goes out at least 7 clear days ahead (s.173(3)) or the system forces the shorter-notice path with the ID-presence rule |
| SS-1 minutes discipline | Draft minutes circulate within 15 days, comments close in 7 days, minutes are entered and signed within 30 days (SS-1; s.118 read with Rule 25) — timers visible, escalated at T-3 days; signed minutes are sealed and cannot be edited (NN-02) |
| Registers maintained by events | Allotment, transfer, charge creation, loan/investment approval, RPT approval, SBO declaration and director appointment events update the corresponding register automatically; a register snapshot reconciles to its event log with zero differences |
| Filings prepared, not missed | Every ROC, LODR and sector governance filing in the catalogue has a computed due date, an owner, a data sheet and attachments ready before T-5 working days; after filing, the SRN or acknowledgement is captured; overdue filings show accruing additional fee |
| Listed-company controls | Material events detected in the platform (board outcome, credit rating change, auditor resignation) open a Reg 30 disclosure case with the correct clock (30 minutes for board-meeting outcomes; 24 hours otherwise); UPSI shared through board packs creates Structured Digital Database entries automatically |
| Annual report drafted from data | The Board's report (s.134) and, for listed entities, MD&A and the Corporate Governance Report are produced as a DOCX draft with every figure traceable to its source (accounts, Finbyx/Udofin portfolio, registers, HRMS) and every narrative paragraph marked as AI draft until approved |
| Portability | `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` export (Appendix M §M.3, X-27) holds minutes as signed PDF and DOCX, registers as XLSX and PDF, resolutions, notices, packs and filings, readable without LawDocsComply |

---

## 2. Scope (in / out)

**In scope**

- Governance Structure Engine: constitution profile, threshold tests, regulator overlays, tenant charter, Governance Blueprint and its gap report.
- Entity master and group structure (holding, subsidiary, associate, joint venture), MCA master-data pull and diff.
- Directors and KMP registry linked to HRMS: DIN, director KYC, DSC custody log, categories, tenure, directorship limits, disqualification checks, declarations, remuneration links, familiarisation, evaluation.
- Committees: catalogue, terms of reference, composition rules, quorum, cadence, dedicated committee pages, custom committees mapped to statutory roles.
- Meeting lifecycle for Board, committees, independent directors' meetings, AGM, EGM, postal ballot and circular resolutions: planning, notice, agenda, board pack, secure board portal, attendance (physical and video conferencing), conduct, decisions, minutes, signing, sealing, certified copies, action tracking.
- Resolutions and documents library with auto-filled templates and follow-on filing triggers.
- Statutory registers maintained from events (Companies Act, LLP Act, SBO rules, PIT Structured Digital Database), inspection and extracts.
- ROC/MCA e-filing catalogue, due-date engine, data sheets, attachments, SRN capture (human filing with DSC — D-13).
- Annual secretarial cycle planner.
- Director declarations and fit-and-proper workflows (Companies Act, RBI NBFC/UCB/bank, IRDAI, IFSCA overlays), certificates generated for CEO/MD signature, RBI quarterly statements, PRAVAAH approval packs.
- Listed-company module: LODR calendar, Reg 30 disclosure engine, RPT approvals with Schedule XII thresholds, PIT (designated persons, SDD, trading window, pre-clearance, disclosures), SAST disclosures tracker, website (Reg 46) checklist, debt-listed and SME variants, stock-exchange file preparation.
- Secretarial audit hooks (MR-3, Reg 24A annual secretarial compliance report, MGT-8) consumed by P10.
- Annual report and Board's report drafting assisted by Finbyx, Udofin, accounting and HRMS data (R-053).
- CS, board member, chairperson, CEO/MD and committee-chair dashboards; task assignment by hierarchy.
- LLP governance (designated partners, LLP agreement, Form 3/4/8/11, LLP SBO).
- Society governance base (Societies Registration Act 1860 annual list, governing body) — reused and extended by P16 for co-operatives.

**Out of scope (owned elsewhere)**

- Policy authoring and approval lifecycle (P07), though board approval of a policy is captured through a P06 meeting decision.
- Co-operative elections, membership and general body specifics (P16; P06 supplies engines).
- Secretarial audit execution, working papers and audit report (P10).
- Automated filing on MCA21, NSE NEAPS, BSE Listing Centre or RBI portals (prohibited by D-13/NN-08 until an official authorised API exists): P06 prepares and validates, a human files.
- Remote e-voting service itself (provided by SEBI-recognised e-voting agencies; P06 exports and imports) and video-conferencing infrastructure (Teams/Zoom/Meet adapters via P18).
- Share registry/RTA operations beyond register maintenance and BENPOS reconciliation.

---

## 3. Personas and permissions touched

| Role code | What they do in P06 | Key limits |
|---|---|---|
| `ten_kmp` (CS) | Owns the governance workspace: blueprint, registers, meetings, minutes, filings, declarations, LODR | Cannot sign minutes as chairperson; cannot approve own register corrections (checker required) |
| `ten_admin` | Configures entities, committees, custom names, access; assigns CS | Cannot alter sealed minutes or register history (NN-02) |
| `ten_board_member` | Reads board packs, annotates privately, votes (recording), signs declarations, attends | Sees only meetings of bodies they belong to; UPSI acknowledgement on first open |
| `ten_committee_member` | Same for committees; committee chair signs committee minutes | Scoped by `committee_id` |
| `ten_kmp` (CEO/MD/WTD) | Signs fit-and-proper certificates, quarterly RBI statements, presents agenda items, approves agenda drafts with CS | — |
| `ten_kmp` (CFO, CRO, CCO, HIA) | Owns agenda items from their functions; receives actions | Cannot edit others' notes |
| `ten_maker` / `ten_checker` | Prepare and check register entries, filings and data sheets when delegated by CS | Maker ≠ checker (NN-05) |
| `ten_secretarial_auditor` | Read-only auditor workspace (registers, minutes, filings, evidence, SDD extract) | Time-boxed grant; downloads watermarked |
| `ten_external_auditor` / `ten_internal_auditor` | Read minutes, RPT and loan registers relevant to scope | Scoped by engagement |
| `ten_supervisor_view` | RBI/SEBI/IRDAI inspector read-only per D-12 | No UPSI items unless tenant grants; every view logged |
| `dlv_professional` / `dlv_rm` | Retainer CS services delivered as maker (R-072) | Only with a delivery grant approved by the client admin; acts as `ten_maker` with a LawDocs badge; never checker, approver, admin, chairperson, director, board, auditor or supervisor roles; LawDocs is never the sole checker of LawDocs-made drafts (NN-43, X-17) |
| `svc_vidhi` | Drafts agenda notes, board-pack summaries, minutes, resolutions, annual-report narrative | On behalf of a named user; outputs marked draft (NN-04, NN-14) |
| `anon` (shareholder/inspector) | Optional inspection request form on tenant website | Request only; no data shown |

Board-confidential content (agenda papers marked confidential, minutes before sealing, director annotations, voting intentions, UPSI items) is data class **BOARD_CONFIDENTIAL** under NN-13: separate encryption key per tenant, excluded from analytics, search snippets for non-members and AI training; Vidhi may process it only for a user who already has access.

---

## 4. Functional requirements

### 4A. Governance Structure Engine (R-093)

**FR-P06-01 — Layered composition.** The engine composes an entity's governance requirements from five ordered layers. Higher layers add to or tighten lower layers; a tenant charter can tighten but never relax a legal requirement (tier L/G guard, NN-28).

| Layer | Source | Examples of what it contributes |
|---|---|---|
| L0 Constitution profile | Entity master | Form: private company, public unlisted, listed (equity / debt only / SME), OPC, small company (s.2(85)), Section 8, Government company, Nidhi, producer company, LLP, society, trust, co-operative (P16) |
| L1 MCA/ROC and Companies Act | Rule pack `gov.companies_act` | Minimum directors (s.149(1): 3 public, 2 private, 1 OPC), resident director (s.149(3)), woman director (s.149(1) second proviso read with Rule 3 Appointment & Qualification Rules), independent directors (s.149(4), Rule 4), Audit Committee (s.177, Rule 6 Meetings of Board Rules), NRC and SRC (s.178), CSR Committee (s.135), whole-time KMP (s.203, Rule 8) and whole-time CS (Rule 8A), vigil mechanism (s.177(9), Rule 7), secretarial audit (s.204, Rule 9), internal audit (s.138, Rule 13), MGT-8 certification (Rule 11(2) Management & Administration Rules), board meetings (s.173), registers (ss.85, 88, 170, 186, 189), filings |
| L2 Securities law overlay | Rule pack `gov.sebi_lodr` (if listed) | LODR Reg 17 (composition, ≥ 4 meetings, ≤ 120-day gap), Reg 17A (directorship limits), Reg 18–21 (Audit, NRC, SRC, RMC), Reg 23 (RPT, Schedule XII), Reg 24/24A (subsidiaries, secretarial audit), Reg 25 (IDs), Reg 30 (disclosures), Reg 46 (website); PIT Regulations 2015; SAST Regulations 2011; debt-listed Chapter V; SME relaxations (Reg 15(2)) |
| L3 Sector regulator overlay | Rule packs from P15, e.g. `gov.rbi_nbfc_2025`, `gov.rbi_ucb_2025`, `gov.rbi_cb_2025`, `gov.irdai_cg_2024`, `gov.ifsca_<entity>` | RBI (NBFC – Governance) Directions 2025 (RBI/DOR/2025-26/344, 28 Nov 2025): director with bank/NBFC experience (para 8), RMC (para 9), prior approval for change of > 30% directors (paras 10–11), fit-and-proper policy, Annex II declaration, annual declaration as on 31 March, Deed of Covenant (paras 12–13), quarterly statement to the Regional Office within 15 days (para 14), ACB with ≥ 3 members and IS audit oversight (para 17), NRC (para 18), CRO above ₹5,000 crore asset size (paras 19–24), CCO (para 25), KMP restrictions (para 26), ID cap of three ML/UL NBFC boards (para 27), compensation (paras 29–37), whistle-blower (para 38), UL listing within three years (para 43). UCB (Governance) Directions 2025 (RBI/DOR/2025-26/273): two professional directors (para 6), ACB (paras 13–15), RMCB at ≥ ₹5,000 crore assets (paras 16–17), Board of Management (paras 18–28), MD/CEO prior approval under s.35B BR Act through PRAVAAH (paras 29–30), CRO (paras 31–38). IRDAI (Corporate Governance for Insurers) Regulations 2024 and Master Circular 2024: Audit, NRC, CSR, RMC (incl. ALM), Policyholder Protection/Grievance/Claims Monitoring, Investment and With-Profits committees; ≥ 3 IDs; KMP vacancy ≤ 180 days; ID resignation reported within 30 days |
| L4 Tenant charter | Articles/bye-laws, board-approved governance guidelines | Higher ID ratio, additional committees, extra notice days, quorum higher than statutory, internal approval matrix |

**FR-P06-02 — Thresholds as data.** Every threshold (paid-up capital, turnover, borrowings, deposits, asset size, listing status, number of shareholders, layer, net worth) is a rule-pack parameter with effective dates and citation, never a code constant (NN-26 by analogy; NN-07). The Corporate Laws (Amendment) Bill 2026 introduced in the Lok Sabha may move several Companies Act thresholds **[VERIFY: status and enacted text]**; a new pack version is published through P02 without a release. The engine evaluates thresholds on the entity's figures as at the relevant test date (for example, "last date of latest audited financial statements" under Rule 4 and Rule 6) and stores the evaluation with its inputs.

**FR-P06-03 — Governance Blueprint.** Output per legal entity, versioned and dated:

- required organs (Board, Board of Management for UCBs, managing committee for societies, general body) with size bounds;
- required director categories (independent, woman, resident, professional, nominee constraints) with counts;
- required committees with composition, chair, quorum and cadence rules;
- required KMP and function heads (CEO/MD, WTD, CFO, CS, CRO, CCO, HIA, CISO, DPO, GRO, Principal Officer) with eligibility and reporting-line rules;
- required policies (hand-off list to P07 with citation and review frequency);
- meeting cadence rules; registers to maintain; recurring and event-based filings; declarations; disclosures.

Each blueprint line carries `lr_ids[]`, layer, mandatory/recommended, and a status from the live structure: `MET`, `GAP`, `AT_RISK` (will fail within the warning window, e.g. ID term ends in 60 days), `NOT_APPLICABLE` (with reason), `WAIVED` (only where law permits, with evidence).

**FR-P06-04 — Gap report and remediation.** Every `GAP` or `AT_RISK` line creates a compliance issue (P04 `cmp.issues`, source `GOVERNANCE`) with owner CS, due date derived from the rule (e.g. casual vacancy of an ID to be filled within three months or at the next board meeting, whichever is later — s.149 read with Rule 4 and Reg 25(6) for listed entities **[VERIFY wording]**), and a suggested remediation (appointment workflow, committee reconstitution, policy draft). The blueprint is re-evaluated on any change to entity figures, persons, committees, rule packs or charter.

**FR-P06-05 — Explainability.** "Why is this required?" on every line opens the rule chain: the threshold inputs, the rule text excerpt, citation, effective date and the layer that added or tightened it.

### 4B. Entity master and group structure

**FR-P06-06 — Entity profile.** Per legal entity: legal name and former names, CIN/LLPIN/registration number, constitution, date of incorporation, ROC, registered office and other places of keeping registers (s.94), MoA/AoA versions (each a P07 document with effective date and the resolution that adopted it), authorised/issued/subscribed/paid-up capital by class, financial year, AGM history, listing details (exchanges, scrip codes, ISINs, listed securities, RTA, depositories), regulators and licences (RBI CoR with category and layer, IRDAI registration, IFSCA registration, SEBI registration), LEI, PAN (masked, NN-12), GSTIN(s), TAN, statutory/internal/secretarial/cost auditors with terms, bankers, debenture trustees, credit ratings.

**FR-P06-07 — MCA master-data pull.** Through the P18 company-data adapter (licensed MCA data providers; never scraping), the CS can refresh master data, director list, charges and filing status. The system shows a field-level diff; accepted changes are posted as events with source `MCA_PULL`; rejected differences are recorded (a mismatch between MCA records and the company's register is itself a governance issue).

**FR-P06-08 — Group structure.** Interactive group tree: holding (s.2(46)), subsidiary (s.2(87)), associate (s.2(6)), JV, step-downs, foreign entities; shareholding percentages with effective dates; layers of subsidiaries limit check (s.2(87) proviso read with the Restriction on Number of Layers Rules 2017, where applicable **[VERIFY]**); common directors and interlocks; material subsidiary determination for listed entities (Reg 16(1)(c), Reg 24). The group tree drives related-party identification (s.2(76), LODR Reg 2(1)(zb)) used by the RPT module and the MBP-4 register.

### 4C. Directors and KMP registry (R-056)

**FR-P06-09 — Person master.** Directors, KMP, senior management (LODR Reg 16(1)(d)), committee members who are not directors, invitees and designated persons are rows in the HRMS person master (P13) projected into `gov.officer_roles`. Non-employees (independent directors, nominee directors, external committee members) are persons without employment records. Identity fields minimised (NN-12): PAN masked with token; Aadhaar never stored; DIN stored; passport only where required for foreign directors.

**FR-P06-10 — Director record.** DIN and DIN status; director KYC status — the Companies (Appointment and Qualification of Directors) Amendment Rules 2025 (notified 31 Dec 2025, effective 31 Mar 2026) replace annual DIR-3 KYC with a KYC once in three years (for directors compliant to date the next filing is due by 30 June 2028) and use the revised form also to update mobile, e-mail and address and to reactivate DIN **[VERIFY: form name and event-based update timeline]**; DSC class, issuer, serial, expiry and custody log (the system never stores the DSC private key — signing happens on the holder's token or via the ESP); category (executive, non-executive, independent, nominee with nominating institution, woman, resident); date of first appointment, current term, retirement by rotation (s.152(6)), ID terms (s.149(10)–(11): two terms of up to five years, three-year cooling-off); IICA ID databank registration and online proficiency self-assessment status (Rule 6 Appointment & Qualification Rules **[VERIFY exemptions]**); directorships held (s.165: 20 companies including 10 public; LODR Reg 17A: 7 listed entities as director/ID, 3 for a whole-time director of a listed entity; RBI NBFC para 27: ID on at most three ML/UL NBFCs); committee memberships and chairmanships (Reg 26(1): ≤ 10 memberships, ≤ 5 chairs across listed and public companies counting Audit and SRC only **[VERIFY]**); disqualification watch (s.164(1)/(2), s.167); remuneration links (s.197, Schedule V; LODR Reg 17(6)); D&O policy; familiarisation sessions (Reg 25(7)); board evaluation results (s.178(2), Reg 17(10)); skills matrix (LODR Schedule V Part C para 2(h)).

**FR-P06-11 — Limit and eligibility engine.** On any change the engine recomputes: directorship limits, committee limits, ID independence tests (s.149(6) and Reg 16(1)(b) — pecuniary relationships, relatives, KMP history, auditor association), age limits (s.196(3) for MD/WTD), tenure, cooling periods, minimum experience under sector overlays (NBFC para 8), KMP exclusivity (NBFC para 26; IRDAI). A failing test sets `AT_RISK`/`GAP` on the blueprint and on each affected committee and opens a CS task.

**FR-P06-12 — KMP record.** CEO, MD, WTD, manager, CFO, CS (s.2(51), s.203), plus sector-mandated functionaries: CRO, CCO, HIA, CISO, DPO, Grievance Redressal Officer, Principal Nodal Officer, Appointed Actuary (insurers), Principal Officer (IFSCA, FIU-IND), Money-Laundering Reporting Officer. Each has appointment approval chain (Board resolution, shareholder approval where needed, regulator prior approval or intimation), fixed-tenure rules (CRO under NBFC para 22; CRO under UCB paras 31–38), vacancy clocks (s.203(4): fill KMP vacancy within six months; IRDAI KMP ≤ 180 days), and filings (DIR-12, MR-1 within 60 days for MD/WTD/manager, regulator intimations).

**FR-P06-13 — Organisation integration.** Departments and reporting lines come from HRMS (P13); the CS can see which committee or KMP owns which department, and governance tasks can be assigned down the hierarchy (R-095). Department and committee names are tenant terminology (P02), but statutory mapping is preserved underneath (R-086).

### 4D. Committees (R-092)

**FR-P06-14 — Committee catalogue.** Seeded templates (each with ToR template, composition rule, quorum rule, cadence rule, mandatory agenda items, citations): Audit Committee (s.177; Reg 18; NBFC para 17; UCB paras 13–15); Nomination and Remuneration Committee (s.178(1); Reg 19; NBFC para 18); Stakeholders' Relationship Committee (s.178(5); Reg 20); CSR Committee (s.135); Risk Management Committee (Reg 21; NBFC para 9; UCB RMCB paras 16–17; IRDAI RMC incl. ALM); IT Strategy Committee and IT Steering Committee (RBI Master Direction on IT Governance, Risk, Controls and Assurance Practices, 7 Nov 2023, for applicable REs **[VERIFY applicability by layer after 2025 consolidation]**); Customer Service Committee; Asset-Liability Management Committee; Credit Committee; Review Committee for wilful defaulter identification (RBI Master Direction on Treatment of Wilful Defaulters and Large Defaulters, 30 Jul 2024 **[VERIFY 2025 consolidated reference]**); Special Committee of the Board for Monitoring and Follow-up of Frauds (banks) / fraud risk committee (NBFC fraud risk management directions); Investment Committee, Policyholder Protection Committee and With-Profits Committee (IRDAI); Independent Directors' meeting (Schedule IV para VII; Reg 25(3)); Board of Management (UCB); Executive/Banking/Borrowing committee (delegation under s.179(3) proviso); POSH Internal Committee (link to P13 — sealed); Grievance Redressal Committee; Disciplinary committee; custom committees.

**FR-P06-15 — Custom names and multi-role committees.** Tenants rename committees freely (terminology tier T). A committee can be mapped to one or more statutory roles (for example "Audit and Risk Committee" for an unlisted NBFC-ML discharging both s.177 and NBFC para 9). The composition validator checks the **union** of the mapped roles' rules and the meeting cadence of the strictest role. Unmapping a statutory role from a committee requires the CS and a checker, and re-evaluates the blueprint.

**FR-P06-16 — Composition rules engine.** Rules are expressed declaratively, for example:

```yaml
rule_id: CR-REG18-001   # LODR Reg 18(1)
applies_to_role: AUDIT_COMMITTEE
when: entity.listing.equity == true
require:
  - min_members: 3
  - min_fraction: {attribute: category.independent, value: "2/3"}
  - all_members: {attribute: financially_literate, value: true}
  - min_count: {attribute: accounting_or_financial_expertise, value: 1}
  - chair: {attribute: category.independent, value: true}
citation: ["LR-SEBI-018"]
```

Members, chair and secretary are picked from the person master (HRMS-linked), with eligibility attributes shown inline. Alternates are not permitted for committees unless the rule pack allows. Invitees (CFO, HIA, statutory auditor, CRO) are recorded separately and never count for quorum.

**FR-P06-17 — Committee page.** Every committee has a dedicated page (SCR-GOV-08): composition with categories and terms, ToR (current version and history, linked to P07), annual calendar, meetings, decisions register, recommendations to the Board and their status, action items, documents, attendance statistics, evaluation results, KPIs (meetings held vs required, average days to circulate minutes), and its blueprint status. Members see their committees only.

**FR-P06-18 — Quorum and cadence.** Quorum rules per body (s.174: one-third or two directors, whichever is higher, with interested directors excluded for public companies; Reg 18(2)(b): two members or one-third, whichever is greater, with at least two IDs; Reg 19(2A), Reg 20, Reg 21(2A) as applicable; UCB BoM two-thirds; charter overrides). Cadence rules (ACB at least four meetings with ≤ 120-day gap under Reg 18(2)(a); RMC at least twice a year with ≤ 210-day gap **[VERIFY]**; NRC and SRC at least once; ID meeting once per FY). The planner warns when a planned calendar would breach a gap rule.

### 4E. Meeting lifecycle (Board, committees, general meetings)

**FR-P06-19 — Meeting types.** Board; committee; Board of Management (UCB); Independent Directors' meeting; AGM; EGM; postal ballot; circular resolution (Board/committee, s.175); adjourned meeting; managing committee and general body (society/co-operative, consumed by P16). Each type has a rule pack for notice, quorum, voting, minutes and filings.

**FR-P06-20 — Annual planner.** The CS builds the year's calendar: statutory minimums (s.173(1): four Board meetings, ≤ 120 days between consecutive meetings, first within 30 days of incorporation; s.173(5) and revised SS-1: OPC, small, dormant and start-up private companies one meeting in each half of the calendar year with ≥ 90 days' gap), listed-entity results calendar (Reg 33 timelines), committee cadences, AGM window (s.96: within six months of FY end, ≤ 15 months between AGMs; first AGM within nine months of the first FY end), ID meeting, budget meeting, policy-review meetings (from P07 next-review dates), regulator-driven reviews (quarterly compliance and risk reports). A director availability poll proposes dates; chosen dates create calendar holds (P04 calendar sync, R-094) and a pre-meeting task chain.

**FR-P06-21 — Notice.** For Board meetings, written notice of at least seven days to every director at the registered address (s.173(3); SS-1 para 1.3 **[VERIFY para]**), by hand, post, courier or e-mail/portal with proof of delivery captured. Shorter notice for urgent business requires at least one independent director present (where the company has IDs) or ratification by at least one ID afterwards — the system forces this path, records the ground of urgency and blocks circulation of minutes until ratification is recorded. Notice content: date, day, time, venue, video-conferencing facility and link, contact for technical help, agenda, and the option for directors to give their intention to attend electronically (revised SS-1 annual intimation is stored on the director record). General meetings: 21 clear days (s.101), shorter notice with consent of members holding 95% (revised SS-2 thresholds), explanatory statement (s.102), proxies (s.105), e-voting (Rule 20) and VC/OAVM where permitted by the MCA's prevailing general circular **[VERIFY: current MCA circular permitting VC/OAVM general meetings and its validity]** (setting `gov.gm.vc_allowed` effective-dated).

**FR-P06-22 — Agenda builder.** Agenda items are records with: title, item type (noting, approval, discussion, recommendation), owner and presenter, linked committee recommendation, draft resolution (from the library, §4F), notes on agenda, attachments, classification (`NORMAL`, `CONFIDENTIAL`, `UPSI`, `INTEREST_SENSITIVE`), required majority (simple, three-fourths for certain items, unanimous for some s.179/s.186/s.188 items depending on facts **[INTERP — rule pack]**), interested-director flags, required follow-on actions. Sources:

- **Standard templates**: first meeting of FY (MBP-1 disclosures, DIR-8 noting, s.149(7) ID declarations, Reg 25(8) confirmation, appointment of internal auditor, approval of calendar); quarterly meeting (results, compliance certificate, investor grievance statement, RPT statement, ALM/risk/compliance reports, minutes of committees for noting, action-taken report); annual accounts meeting (financial statements, Board's report, MR-3, MGT-8 where applicable, AGM notice, book closure/record date); appointment and resignation templates.
- **Auto-pulled items** from other modules: compliance instances that require Board/committee noting or approval (P04 `requires_body_review`), policies due for review or approval (P07), risk appetite and RCSA reports (P08), ICAAP and stress-test results (P09), internal/IS/secretarial audit reports and ATRs (P10), returns requiring Board approval (P11), data-breach and cyber reports (P12), grievance analytics (P14), regulator inspection reports and compliance (P04/P10), and governance gaps (§4A).
- **Supplementary agenda** and **any other business** items with the chairperson's permission (SS-1); "Any other business" is restricted to items permitted by the charter and law.

**FR-P06-23 — Notes on agenda timing.** Notes are circulated with the notice, at least seven days before the meeting (SS-1); items with UPSI or price-sensitive content may follow later with the reason recorded; papers added after the cut-off are badged "late paper" and the minutes template records the chair's consent for tabling.

**FR-P06-24 — Board pack builder.** One click compiles notice, agenda, notes, annexures and previous minutes into: (a) a portal book with bookmarks, page numbers and item navigation; (b) a paginated, bookmarked, per-recipient watermarked PDF; (c) a DOCX agenda. The builder flags missing papers per item, oversize scans, unreadable OCR, inconsistent figures across papers (simple numeric cross-check), and conflicts: directors with an interest under s.184 (from MBP-1 and the related-party graph) are flagged against items and receive the item with a recusal banner; their access to the item's papers is configurable (`gov.pack.interested_director_access` = `VIEW_WITH_BANNER` | `HIDE`). Versioning is per item; re-publishing notifies only directors whose items changed.

**FR-P06-25 — Secure board portal.** Directors' workspace (web and installable PWA): upcoming meetings, books, private annotations (highlight, note, ink on tablets) that never leave the director's scope unless explicitly shared with the CS or chair; shared annotations; questions to presenters before the meeting; "read" progress; secure messaging among the body's members and the CS (BOARD_CONFIDENTIAL); resolution e-approvals for circular resolutions; declaration and signature requests; personal document library (D&O policy, codes of conduct, familiarisation material); meeting archive limited by the retention and access policy. Downloads are off by default (`gov.portal.download` = `OFF`), printing watermarked; session timeout 15 minutes; step-up MFA for opening UPSI items. Offline encrypted cache and remote wipe are delivered with the mobile app (later release) and are flag-gated.

**FR-P06-26 — Attendance and video conferencing.** Attendance modes: physical, video conferencing or other audio-visual means (s.173(2), Rule 3 of the Companies (Meetings of Board and its Powers) Rules 2014), and leave of absence. Rule 3 duties are implemented as a CS checklist with evidence: roll call at the start and after breaks, each director confirming identity, location, that no one else is present without permission and that they can see and hear the others; the meeting is recorded and the recording kept in safe custody; the place of meeting in the notice is deemed the venue. The MCA's 2021 omission of Rule 4 (matters not to be dealt with through VC) leaves the restricted-matter list empty unless re-notified **[VERIFY]**; revised SS-1 on electronic participation for restricted items where a physical quorum is present is held as rule-pack logic (`gov.vc.restricted_items` list, default empty). Teams/Zoom/Meet links are generated through P18 adapters; attendance can be auto-suggested from the conferencing platform's participant log but is confirmed by the CS. The attendance register (SS-1) is generated, signed by each director electronically or noted by the CS for VC attendees per SS-1, and sealed with the minutes.

**FR-P06-27 — Quorum monitor.** Live quorum indicator during the meeting; it subtracts directors who leave and interested directors for the specific item (s.174(3) and s.184(2) for public companies; private company exemption per revised SS-1 and MCA exemption notification of 5 June 2015 **[VERIFY]**). If quorum is lost, the console offers adjournment per s.174(4) (same day next week, or holiday rule) and records it.

**FR-P06-28 — Conduct console.** For the CS: item-by-item decisions (passed unanimously / by majority with counts / deferred / withdrawn / noted), dissent and abstention names (dissent recorded in minutes on request, SS-1), interested directors leaving and returning (with timestamps), chair changes, invitees present per item, action items with owner and due date (created as P04 tasks on finalisation), and live drafting notes. Optional transcript capture with all participants' recorded consent (`gov.meeting.transcription` = `OFF`; requires consent capture at join).

**FR-P06-29 — Minutes (SS-1 and s.118).**

- Structure per SS-1 para 7: entity name, meeting serial number, type, day, date, venue, time of commencement and conclusion; chairperson; directors present (and mode), leave of absence, invitees and their purpose; the CS; quorum confirmation; disclosures of interest; items with brief background and decision; dissent; resolutions in full; the record of noting of previous minutes; next meeting date where decided.
- **Timelines enforced:** draft minutes circulated to all members within 15 days of the meeting; comments within 7 days of receipt; minutes entered in the minute book within 30 days of the meeting; signed and dated by the chairperson of that meeting or of the succeeding meeting (s.118(1) read with Rule 25 of the Companies (Management and Administration) Rules 2014 and SS-1 para 7 **[VERIFY para numbers]**). Each clock has an owner and escalations at T-3 and T-0 to the CS and chair.
- Draft generation: Vidhi assembles the SS-1 skeleton from the agenda, decisions log, attendance and the CS's notes (and transcript when enabled) — every sentence is a draft until the CS accepts it (NN-04).
- Comments: directors comment inline in the portal; the CS resolves comments; the version history of drafts is retained but drafts are not part of the sealed minute book.
- Signing: the chairperson signs by eSign/DSC through P07; pages are consecutively numbered; the signed PDF/A is hashed and **sealed** (`gov.minutes.status = SEALED`). Minutes kept in electronic form follow Rule 27/28 of the Management and Administration Rules on electronic maintenance and security **[VERIFY rule numbers]**.
- **No alteration after signing** (s.118(8)): there is no edit function on sealed minutes for any role including super admin; an error is handled by a note in the minutes of the next meeting and, where needed, a Correction Entry annotation (D-02) that cross-references the later minutes — the sealed record is never changed.
- Certified true copies of minutes and resolutions are generated on request (directors are entitled to copies of Board minutes, SS-1; members to GM minutes within the s.119 timeline on payment of the prescribed fee), each with a serial number in the CTC register.
- Minutes of committees are placed before the Board for noting at the next meeting (auto-agenda item).

**FR-P06-30 — Circular resolutions (s.175; SS-1).** Draft resolution with notes sent to all directors (or members of the committee) entitled to vote through the portal and e-mail; approval by a majority of those entitled to vote; interested directors excluded from the count; if one-third or more of the directors then in office require the matter be decided at a meeting, the circulation stops and an agenda item is created; the result is recorded and the resolution, with the dissent if any, is noted at the next meeting and in its minutes. Response window per SS-1 / charter (`gov.circular.response_days`, default 7 **[VERIFY]**). Matters that cannot be passed by circulation (e.g., those required to be passed at a meeting under s.179(3) and s.180 where applicable) are blocked by rule.

**FR-P06-31 — General meetings.** AGM/EGM/postal ballot builder: notice with explanatory statement; inspection documents list; book-closure/record-date workflow (s.91; LODR Reg 42 for listed); proxy form MGT-11 and proxy register; attendance slip; e-voting hand-off (Rule 20; LODR Reg 44) — export of resolution text, cut-off date shareholder list (BENPOS from RTA) and scrutiniser details to the selected e-voting agency (NSDL, CDSL, KFin Technologies, MUFG Intime) and import of results; poll (MGT-12 ballot, MGT-13 scrutiniser report); declaration of results within two working days for listed entities (Reg 44(3)) and placement on website; minutes of general meeting per SS-2 within 30 days; MGT-15 report on AGM (listed, within 30 days of AGM); postal ballot (s.110, Rule 22) with the scrutiniser's report.

**FR-P06-32 — Decisions and action tracker.** Every decision is a row in `gov.decisions` with body, meeting, item, resolution text, effective date, follow-on actions and filings. Action items flow to P04 tasks with owners; an Action-Taken Report is auto-generated for the next meeting of the same body. Overdue actions escalate to the chair's dashboard.

### 4F. Resolutions and secretarial documents library

**FR-P06-33 — Template library.** Seeded templates (super-admin model templates, tenant-editable copies, versioned in P07): Board resolutions (appointment/resignation of directors and KMP, borrowing and investment approvals under s.179/s.180/s.186, RPT approvals under s.188, opening bank accounts, authorised signatories, policy approvals, approval of financial statements and Board's report, appointment of auditors, allotment of securities, ESOP grants, CSR spend, shifting registered office, change of name, regulatory approval applications), committee recommendations, ordinary and special resolutions with explanatory statements, circular resolution forms, notices, attendance slips, proxy forms, CTCs, consent letters (DIR-2), declarations (DIR-8, MBP-1, s.149(7), fit-and-proper Annex II, Deed of Covenant Annex III), letters of appointment for IDs (Schedule IV), resignation acknowledgements, intimations to regulators and exchanges.

**FR-P06-34 — Auto-fill and follow-on.** Templates bind to entity, person, meeting and transaction data; the CS sees merged text with variables highlighted. Each template declares follow-on obligations, which are created when the decision is recorded: e.g. director appointment → DIR-12 within 30 days, MR-1 within 60 days for MD/WTD, shareholder regularisation at next GM for additional directors, LODR Reg 30 disclosure, register entries (Register of Directors and KMP), RBI intimation or quarterly statement entry (NBFC para 14), HRMS update; special resolution → MGT-14 within 30 days (s.117).

### 4G. Statutory registers

**FR-P06-35 — Register engine.** Registers are projections over an append-only event store (`gov.register_events`), never free-edited tables. Each register definition declares its legal basis, form, columns, event sources, place of keeping, inspection rules, extract fee, retention and authentication method. Corrections are posted as reason-coded correction events with maker ≠ checker; the original line stays visible with a strike-through and the correction reference (D-02, NN-02).

| Register (form) | Legal basis | Event sources | Notes |
|---|---|---|---|
| Members (MGT-1) | s.88(1)(a); Rule 3 Management & Administration Rules | Allotment (PAS-3 workflow), transfer/transmission, BENPOS upload for demat holdings, buy-back, forfeiture | Index of members where > 50 members (s.88(2)); foreign register (s.88(4), MGT-3) |
| Debenture holders / other security holders (MGT-2) | s.88(1)(b)–(c); Rule 4 | NCD allotments, redemptions | Debenture trustee link |
| Significant beneficial owners (BEN-3) | s.90; Rule 5 SBO Rules 2018 | BEN-1 declarations, BEN-4 notices, group tree changes | BEN-2 filing within 30 days of receiving BEN-1 |
| Charges (CHG-7) | s.85; Rule 10 Registration of Charges Rules | CHG-1/CHG-4/CHG-9 workflows | Charge ID from MCA |
| Directors and KMP (incl. shareholding) | s.170(1); Rule 17 Appointment & Qualification Rules | Appointments, cessation, shareholding changes | Inspection at AGM (s.170(1)) |
| Loans, guarantees, security and acquisitions (MBP-2) | s.186(9); Rule 12(1) Meetings of Board Rules | s.186 approval workflows, treasury feed (Finbyx investment book for NBFCs where s.186 applies; NBFC exemption under s.186(11) recorded **[INTERP]**) | Entries within seven days of the transaction |
| Contracts with related party and contracts with interested directors (MBP-4) | s.189; Rule 16 | RPT approvals, s.184(2) disclosures | Entries placed before the next Board meeting and signed by all present directors |
| Directors' disclosures of interest (MBP-1 file) | s.184(1); Rule 9 | MBP-1 submissions (first meeting of FY, first meeting after change) | Kept as a register-style index of disclosures |
| Register of deposits | s.73; Rule 14 Companies (Acceptance of Deposits) Rules 2014 | Deposit events (for companies permitted to accept deposits) | The register is distinct from the annual DPT-3 return (Rule 16), which is a filing in §4H (X-37) |
| Sweat equity (SH-3), ESOP (SH-6), buy-back (SH-10), renewed/duplicate certificates (SH-2) | Share Capital & Debentures Rules | Respective workflows | ESOP from HRMS grant events |
| Transfers and transmissions | s.56 | Transfer workflow | Physical/demat |
| Postal ballot, proxies, attendance, CTC issued | SS-1, SS-2, Rules 19–22 | Meeting engine | — |
| Structured Digital Database (UPSI) | SEBI PIT Reg 3(5)–(6) | Board-pack sharing, manual entries, external sharing logs | Non-tamperable, time-stamped, audit trail (§4K) |
| Register of designated persons and their immediate relatives | PIT Reg 9 read with Schedule B | HRMS roles, declarations | Disclosure of PAN masked |
| LLP partners and SBO (LLP BEN-4) | LLP Act 2008; LLP (Significant Beneficial Owners) Rules 2023 **[VERIFY form numbers]** | Partner changes (Form 4), declarations | — |
| Penalties, strictures and warnings (internal) | Good practice; inspection readiness | Regulator orders from P04/P10 | — |

**FR-P06-36 — Inspection and extracts.** Inspection requests (members, directors, creditors, public as permitted by s.94 read with Rule 14 Management & Administration Rules) are logged, approved by the CS and checker, scheduled, and fulfilled through a time-boxed read-only view or certified extracts; fees per Rule 14 are invoiced through P20 where configured. Every inspection is an audit event.

**FR-P06-37 — Register reconciliation.** Monthly job compares MGT-1 with BENPOS from the RTA/depositories, MBP-4 with the RPT approvals log and the accounting related-party ledger (P11), CHG-7 with MCA charge data, and Directors/KMP with MCA master data; differences become CS tasks.

### 4H. ROC/MCA e-filing catalogue and calendar

**FR-P06-38 — Filing catalogue.** Data-driven catalogue (`gov.filing_definitions`) with form code, portal (MCA21 V3), trigger (annual/event), due-date rule, fee and additional-fee rule (Companies (Registration Offices and Fees) Rules 2014 as amended — additional fee schedules are rule-pack data **[VERIFY current schedule]**), mandatory attachments, certification requirement (practising CS/CA/CMA), signatory DSCs, linked register updates and downstream LODR/sector intimations. All Companies Act forms now file on MCA21 V3 (the last 38 forms including AOC-4 family, CSR-2, MGT-7/7A/15 and ADT-1 to ADT-4 went live on 14 July 2025).

| Form | Purpose | Trigger / due rule (seed; rule-pack data) |
|---|---|---|
| AOC-4 / AOC-4 CFS / AOC-4 XBRL / AOC-4 NBFC (Ind AS) | Financial statements | Within 30 days of AGM (s.137); XBRL for prescribed classes; NBFC form for Ind AS NBFCs |
| MGT-7 / MGT-7A | Annual return (MGT-7A for OPC/small) | Within 60 days of AGM (s.92(4)) |
| ADT-1 | Auditor appointment | Within 15 days of the meeting (s.139) |
| ADT-3 | Auditor resignation | Within 30 days of resignation (s.140(2)) |
| MGT-14 | Filing of resolutions (s.117) | Within 30 days of passing |
| MGT-15 | Report on AGM (listed) | Within 30 days of AGM |
| DIR-12 / DIR-11 | Change in directors/KMP; director resignation | Within 30 days |
| MR-1 | Appointment of MD/WTD/manager | Within 60 days |
| Director KYC (revised form) | Director KYC | Once every three years from 31 Mar 2026; first triennial cycle due 30 Jun 2028 for compliant directors **[VERIFY]** |
| DPT-3 | Return of deposits / outstanding receipts not deposits | 30 June annually (Rule 16) |
| MSME-1 | Outstanding MSE dues > 45 days | Half-yearly: 30 April and 31 October |
| PAS-3 | Return of allotment | Within 30 days of allotment (s.39(4); Rule 12 PAS Rules); within 15 days of allotment for private placements (s.42(8)) **[VERIFY sub-section after 2017 amendment]** |
| PAS-6 | Reconciliation of share capital audit (unlisted public) | Within 60 days of half-year end **[VERIFY]** |
| SH-7 | Alteration of share capital | Within 30 days |
| SH-11 | Return of buy-back | Within 30 days of completion |
| CHG-1 / CHG-4 / CHG-9 | Creation/modification/satisfaction of charge | Within 30 days, extendable with additional fee per s.77 as amended **[VERIFY extension windows]** |
| BEN-2 | SBO return | Within 30 days of receipt of BEN-1 |
| INC-22 / INC-22A | Registered office change; active company tagging | Within 30 days / as notified |
| INC-20A | Commencement of business | Within 180 days of incorporation |
| CSR-2 | CSR reporting | As notified for the FY **[VERIFY]** |
| CRA-2 / CRA-4 | Cost auditor appointment; cost audit report | 30 days of Board meeting / 30 days of receipt of report |
| NFRA-2 | Annual return to NFRA (applicable companies) | As notified **[VERIFY]** |
| LLP Form 11 / Form 8 | LLP annual return / statement of account & solvency | 30 May / 30 October |
| LLP Form 3 / Form 4 | LLP agreement changes / partner changes | Within 30 days |

**FR-P06-39 — Due-date derivation.** Due dates derive from the triggering event or the AGM date and FY; when the AGM date moves, all dependent filings recompute and the change is logged. Extensions granted by MCA general circulars are effective-dated rule-pack changes (e.g., an extension of annual filings) — the user sees both the statutory and the extended due date with the circular cited.

**FR-P06-40 — Filing preparation (D-13).** Each filing instance has a **data sheet** (field-by-field values mapped to the e-form, generated from registers, accounts and decisions), required attachments (board resolution CTC, consent, list of allottees, financial statements, auditor's report), certification checklist, signatories with DSC readiness check (expiry), and a review step (maker ≠ checker). The CS files on MCA21 V3 with the DSC, then records SRN, challan amount, filing date, status (pending approval / resubmission / approved / rejected) and uploads the challan and acknowledgement. Additional fees accrue on the dashboard from the day after the due date. The system never logs into MCA on the tenant's behalf and never stores MCA passwords outside the credential vault (D-04).

### 4I. Annual secretarial cycle

**FR-P06-41 — Cycle planner.** On FY rollover the system generates the entity's secretarial cycle as a dependency graph of tasks with owners and due dates (P04), composed from the blueprint. Seed for an Indian company with an April–March year (listed and NBFC items appear only where applicable):

| Window | Items |
|---|---|
| April | First Board meeting items (MBP-1, DIR-8, s.149(7)/Reg 25(8) declarations); MSME-1 (Oct–Mar) by 30 April; NBFC annual fit-and-proper declarations as on 31 March and March-quarter statement of director changes (auditor-certified) within 15 days (NBFC Governance Directions para 13(3), para 14); SAST Reg 30/31(4) promoter disclosures within seven working days of FY end; Reg 24A secretarial compliance report within 60 days (listed) |
| April–May | Q4/annual results (Reg 33: 60 days for annual audited results); ACB and Board for accounts; internal financial controls testing hand-off (P10) |
| June | DPT-3 by 30 June; Board's report drafting; secretarial audit fieldwork (P10) |
| July–August | Q1 results within 45 days; AGM notice (21 clear days); e-voting; book closure/record date |
| By 30 September | AGM (within six months of FY end); director KYC where due under the triennial cycle |
| Within 15/30/60 days of AGM | ADT-1 (15), AOC-4 (30), MGT-15 (30, listed), MGT-7/7A (60) |
| October | MSME-1 (Apr–Sep) by 31 October; Q2 results; LLP Form 8 by 30 October |
| Quarterly | Reg 31 shareholding pattern, Reg 13(3) grievance statement, Reg 27(2) CG report (within 21 days); Reg 76 SEBI (D&P) reconciliation of share capital audit; NBFC quarterly statement of director changes (para 14); committee cadences |
| Year-round | ID meeting; board evaluation; familiarisation; policy reviews (P07); CSR annual action plan and spend tracking (s.135, CSR Rules); event filings |

Every timeline is a rule-pack item with citation; listed-entity timelines carry **[VERIFY]** markers until the LODR consolidated text as on the go-live date is checked.

### 4J. Director declarations and fit-and-proper (R-093)

**FR-P06-42 — Declaration campaigns.** A campaign issues pre-filled declaration forms to a population with a deadline: MBP-1 (s.184(1), at the first Board meeting of each FY and the first meeting after any change), DIR-8 (s.164(2), annual), s.149(7) ID declaration and Reg 25(8) confirmation, Reg 26(3) code of conduct affirmation, Reg 26(5) senior management disclosure, PIT Reg 7 initial and continual disclosures, ESG/BRSR personal data where required, sector fit-and-proper declarations (NBFC Annex II with annual declaration as on 31 March and Deed of Covenant Annex III; UCB Annex II for directors and BoM members; IRDAI fit-and-proper for MD/CEO/WTD and KMP; IFSCA principal officer and KMP fit-and-proper as per the entity's regulations). The director reviews pre-filled data (other directorships from MCA pull, shareholdings, relatives), corrects it with reasons, attaches evidence and signs (eSign/DSC through P07). Reminders and escalation per campaign settings.

**FR-P06-43 — NRC review.** Declarations route to the NRC (NBFC para 13(2)) with a reviewer view: changes vs last year highlighted, external checks attached (MCA DIN status, disqualification list match, SEBI debarred entities check, RBI wilful defaulter/CIC match where the tenant supplies results, adverse media — recorded as evidence, not automated decisions **[REC]**), a recommendation field and the committee's decision recorded at a meeting (§4E).

**FR-P06-44 — Certificates generated for CEO/MD signature.** The system generates, for signature by the MD/CEO (and auditors where required): the NBFC quarterly statement of changes in directors and the MD/CEO certificate that fit-and-proper due diligence was done (para 14; to the RBI Regional Office within 15 days of quarter end; the March quarter statement certified by the statutory auditors); UCB declarations; IRDAI annual compliance certificate items; Board resolutions noting declarations. Output DOCX/PDF, signed, filed in `05 Governance - Board, Committees and Meetings/<FY>/Fit and Proper/`, and a task for submission through the channel the regulator prescribes (human submission, D-13).

**FR-P06-45 — Change in management and approvals.** For NBFCs, a proposed change of more than 30% of directors (excluding IDs; re-election on rotation excluded) triggers the prior-approval pack (paras 10–11) — application data sheet, Annex documents and board resolution — prepared for PRAVAAH; for banks and UCBs, MD/CEO appointment, re-appointment and termination require RBI's prior approval under s.35B(1)(b) of the Banking Regulation Act (UCB Governance Directions paras 29–30) via PRAVAAH. The appointment workflow blocks "effective" status until the approval reference is recorded.

### 4K. Listed-company module (R-066, R-099)

Applies when `entity.listing` is equity, debt, SME or InvIT/REIT unit-holder obligations as configured (REIT/InvIT governance detail is sourced from P15 packs).

**FR-P06-46 — LODR compliance calendar.** All periodic LODR filings and certificates as instances with due rules and exchange filing formats (XBRL/JSON/PDF as prescribed by NSE NEAPS and BSE Listing Centre): Reg 31 shareholding pattern; Reg 13(3) investor grievance statement; Reg 27(2) corporate governance report; Reg 33 financial results with Reg 33(3) timelines, limited review/audit report and statement on impact of audit qualifications; Reg 32 deviation statement; Reg 23(9) RPT disclosure; Reg 34 annual report; Reg 24A annual secretarial compliance report; Reg 7(3) compliance certificate on share transfer facility **[VERIFY frequency]**; Reg 40(9)-type certificates where still applicable **[VERIFY]**; Reg 76 SEBI (Depositories and Participants) Regulations 2018 reconciliation of share capital audit; BRSR (Reg 34(2)(f), top 1,000 by market capitalisation) with BRSR Core assurance hand-off; Reg 46 website contents checklist; debt-listed Chapter V items (Reg 50–62) for entities above the high-value debt listed entity threshold **[VERIFY current threshold]**.

**FR-P06-47 — Reg 30 disclosure engine.** Sources of events: Board outcomes recorded in the conduct console (Para A item 4 of Part A of Schedule III — disclosure within 30 minutes of conclusion of the meeting), credit-rating changes (from P04/P11 inputs), auditor/KMP/director changes (registers), fraud/default events (from P08/P12/P14 and Finbyx feeds), litigation (from the litigation module), cyber incidents (P12), regulatory actions (P04). Each event opens a case: deemed-material (Para A) vs materiality test (Para B) using the board-approved materiality policy thresholds (Reg 30(4): lower of 2% of turnover, 2% of net worth, 5% of three-year average absolute profit, configurable as policy values) — result and reasoning recorded; draft announcement from template; approval by the authorised KMP (Reg 30(5)); the CS uploads on the exchange portals and records the acknowledgement time; clocks: 30 minutes for board-meeting outcomes, 24 hours generally, 12 hours where the event emanates from within the entity **[VERIFY Reg 30(6) timelines]**; market-rumour verification (Reg 30(11), applicable top 100 then top 250 entities) workflow. All announcements are retained in `06 Company Secretarial - Registers, Filings and Resolutions/Listed Company Compliance/LODR Filings/<FY>/` (Appendix M §M.3) and on the website checklist (five-year retention, Reg 30(8)).

**FR-P06-48 — RPT workflow.** RPT register fed by the related-party graph (§4B) and Finbyx/accounting transactions; omnibus and specific approvals; ACB prior approval (Reg 23(2)); materiality per the scale-based Schedule XII introduced by the SEBI LODR (Fifth Amendment) Regulations 2025 (No. SEBI/LAD-NRO/GN/2025/273, 18 Nov 2025; RPT changes effective 18 Dec 2025): up to ₹20,000 crore consolidated turnover — 10% of turnover; above ₹20,000 crore to ₹40,000 crore — ₹2,000 crore plus 5%; above ₹40,000 crore — lower of ₹3,000 crore plus 2.5%, or ₹5,000 crore; subsidiary-party RPTs where the listed entity is not a party need ACB approval if above ₹1 crore and the lower of 10% of the subsidiary's standalone turnover or the Schedule XII threshold (with the paid-up capital plus securities premium alternative for subsidiaries without a year of audited financials); omnibus shareholder approval validity AGM-to-next-AGM or one year for EGMs. Running cumulative totals per related party per FY trigger alerts at 80% and 100% of the threshold. Companies Act s.188 approvals and MBP-4 entries are produced from the same record.

**FR-P06-49 — Insider trading (PIT Regulations 2015).** Designated persons and immediate relatives (Reg 9, Schedule B), with PAN masked and stored per NN-12; trading window closure calendar (from end of every quarter until 48 hours after declaration of results, plus event closures declared by the compliance officer); pre-clearance requests with approval, seven-trading-day validity and execution reporting **[VERIFY]**; contra-trade check (six months); trading plans (Reg 5 as amended); initial and continual disclosures (Form B, C, D) with the ₹10 lakh quarterly trigger for continual disclosure and two-trading-day company intimation to exchanges **[VERIFY]**; **Structured Digital Database** (Reg 3(5)–(6)): every sharing of UPSI recorded with nature of UPSI, names and PAN (or other identifier) of persons sharing and receiving, date and time; maintained internally, non-tamperable, time-stamped with audit trail and preserved for at least eight years. **Automation:** when a board-pack item classified `UPSI` is published or opened, or a UPSI document is shared through P07, an SDD entry is written automatically; manual entries for off-platform sharing are allowed; entries cannot be edited (corrections are new entries). The UPSI illustrative list expanded by the SEBI PIT (Amendment) Regulations 2025 (notified 11 Mar 2025, effective 9 Jun 2025) drives the classification prompts.

**FR-P06-50 — SAST tracker.** Holdings of promoters and acquirers vs Reg 29(1)/(2) disclosure triggers (5% and every 2% change thereafter), Reg 31 encumbrance disclosures and annual Reg 30 disclosures; alerts based on BENPOS and declarations; drafts of disclosures for the persons responsible (the company's role is to receive and disseminate).

**FR-P06-51 — Shareholder services hooks.** Investor grievances via SEBI SCORES and the entity's own channel are handled in P14 (SRC reporting pulls P14 statistics). Unclaimed dividend transfers to IEPF (s.124–125) are tracked as obligations with IEPF-1/IEPF-2/IEPF-4 forms in the filing catalogue **[VERIFY]**.

### 4L. Secretarial audit hooks (consumed by P10)

**FR-P06-52 — Auditor workspace.** For the secretarial auditor (s.204, Rule 9; LODR Reg 24A and the Reg 24A appointment and term rules introduced by the SEBI LODR (Third Amendment) Regulations 2024 effective 1 April 2025 **[VERIFY]**), the MGT-8 certifying professional and the PAS-6/Reg 76 auditor: a time-boxed, read-only workspace with registers, minutes (sealed PDFs), attendance registers, filings with SRNs and challans, declarations, SDD extract, LODR filings and acknowledgements, blueprint and gap history, and an auto-built checklist mapped to the MR-3 format. Auditors raise queries in the workspace; responses and evidence are tracked; P10 owns the audit programme and report. Before a secretarial auditor is recorded for a listed tenant, the P10 prohibited-services check runs, and an Infrabyx- or LawDocs-linked practising CS is blocked as secretarial auditor of a listed client that receives LDC retainer or delivery services (LODR Reg 24A; X-30; counsel to confirm).

### 4M. Annual report and Board's report drafting (R-053)

**FR-P06-53 — Data assembly.** The annual report builder assembles a data pack per FY from: audited financial statements and notes (P11 accounting bridge — Ind AS or AS per the entity, NN-22 lineage); Finbyx/Udofin portfolio data through the P18 connectors (disbursements, AUM, asset classification, provisioning, capital adequacy, liquidity and other ratios from P09); registers (meetings, attendance, committee composition, changes in directors and KMP); HRMS (headcount, gender, median remuneration and ratio under Rule 5(1) of the Managerial Remuneration Rules, top-ten employee statement under Rule 5(2) **[VERIFY]**); CSR spend; risk management statements (P08); internal financial controls (P10); vigil mechanism and POSH statistics (P13, counts only — sealed data never leaves P13, NN-13); related-party transactions (AOC-2); loans/investments (s.186 particulars); deposits; conservation of energy and technology absorption inputs (owner-supplied); regulator-specific disclosures (e.g., NBFC disclosures prescribed by RBI **[VERIFY 2025 consolidated reference]**).

**FR-P06-54 — Document generation.** Outputs: Board's report (s.134(3) and Rule 8 of the Companies (Accounts) Rules 2014 checklist, each item either filled from data, filled by an owner, or marked "not applicable" with reason); annexures (AOC-1, AOC-2, MR-3, CSR annual report format, particulars of employees); for listed entities MD&A (Schedule V Part B), Corporate Governance Report (Schedule V Part C) and BRSR; the AGM notice. Generated as DOCX from tenant brand templates (P07) with numbers as merge fields linked to lineage; Vidhi drafts narrative sections (MD&A industry outlook, risk narrative) with citations to the data and documents used, all marked draft; Vidhi never supplies a figure — any number in AI-drafted text must match a lineage-linked merge field or the paragraph is blocked (NN-37); the CS and CFO review; the Board approves; final PDF and DOCX filed in `06 Company Secretarial - Registers, Filings and Resolutions/Annual Reports/<FY>/` (sub-folder to be added to Appendix M §M.3; X-27).

**FR-P06-55 — Minutes and agreements from ecosystem data.** The same data-assembly service drafts: Board/committee notes on agenda from Finbyx dashboards (credit committee portfolio notes, ALCO notes with ALM gaps, risk committee KRI summaries); and hands off agreement drafting requests (e.g., co-lending, outsourcing, RPT agreements) to P07/LawDocs templates through P18, with the decision reference.

### 4N. Dashboards and task assignment

**FR-P06-56 — CS dashboard (SCR-GOV-01).** Widgets: blueprint status by entity; upcoming meetings and pack readiness; minutes clocks (draft due, comments open, signature due); filings due/overdue with accrued additional fee; declarations outstanding; composition gaps and at-risk items; DIN/DSC expiries; Reg 30 cases with live countdown; trading window status; SDD entries this quarter; register reconciliation exceptions; inspection requests; action items overdue by body. Every widget opens a filtered work list with bulk actions (assign, remind, export).

**FR-P06-57 — Other dashboards.** Board member (my meetings, papers to read, declarations to sign, my annotations); Chairperson (agenda approvals, minutes to sign, overdue actions); CEO/MD (certificates to sign, approvals pending with regulators, governance gaps); Committee chair; Group CS (all entities). Dashboards are configurable (widget catalogue, Appendix C).

**FR-P06-58 — Task assignment.** Governance tasks can be assigned by any user above the assignee in the HRMS hierarchy or by the CS/committee chair regardless of hierarchy for their body; tasks can be assigned to Vidhi (draft notes, draft minutes, prepare data sheet) and scheduled as recurring (R-095). All tasks appear in the assignee's calendar (P04).

### 4O. Multi-entity and group governance

**FR-P06-59 — Group view.** A tenant may hold several legal entities; the Group CS sees all; entity-level roles restrict others. Interlocking directorships and common committee members are shown; subsidiary governance requirements (NBFC para 39; LODR Reg 24 for material subsidiaries) are tracked; a group governance calendar aligns meetings to avoid conflicts.

### 4P. LLP, society and co-operative base

**FR-P06-60 — LLP.** Designated partners (minimum two, one resident in India, s.7 LLP Act 2008), DPIN/DIN and KYC, LLP agreement versions and Form 3 filings, partner changes and Form 4 within 30 days, Form 11 (annual return, 30 May), Form 8 (statement of account and solvency, 30 October), audit applicability (turnover above ₹40 lakh or contribution above ₹25 lakh, Rule 24(8) LLP Rules 2009 **[VERIFY]**), LLP SBO register and filings under the LLP (Significant Beneficial Owners) Rules 2023 **[VERIFY]**, partners' meetings minutes (LLP Rules/agreement), the Corporate Laws (Amendment) Bill 2026 changes once enacted **[VERIFY]**.

**FR-P06-61 — Societies.** Societies Registration Act 1860: memorandum and rules versions, governing body, annual list of governing body members filed with the Registrar (s.4), state amendments as rule-pack data (state selector), general body and governing body meetings through the same meeting engine.

**FR-P06-62 — Co-operatives.** P16 consumes the meeting engine (general body, managing committee, Board of Management), register engine (members, share capital), declarations and election hand-off; co-operative-law rule packs are owned by P16.

---

## 5. Workflows and state machines

### 5.1 Meeting

`DRAFT → SCHEDULED → NOTICE_ISSUED → PACK_PUBLISHED → IN_SESSION → (ADJOURNED → SCHEDULED) | CONCLUDED → MINUTES_DRAFTING → DRAFT_CIRCULATED → COMMENTS_CLOSED → FINALISED → SIGNED → SEALED`; `CANCELLED` from `SCHEDULED`/`NOTICE_ISSUED` with reason and notice of cancellation.

| Transition | Guard | Timer / escalation |
|---|---|---|
| SCHEDULED → NOTICE_ISSUED | Notice template complete; ≥ notice days (or shorter-notice path chosen with urgency ground) | T-10 reminder to CS if not issued |
| NOTICE_ISSUED → PACK_PUBLISHED | All mandatory items have papers or are marked "to be tabled" with reason | Notes due T-7; late-paper badge after |
| PACK_PUBLISHED → IN_SESSION | Quorum present (live) | — |
| CONCLUDED → DRAFT_CIRCULATED | Draft minutes complete for every item | Due D+15; alerts D+12, D+15 |
| DRAFT_CIRCULATED → COMMENTS_CLOSED | 7 days from circulation or all members responded | Auto-close at day 7 |
| FINALISED → SIGNED | Chairperson eSign/DSC | Due D+30 (entry in book); alert D+27 |
| SIGNED → SEALED | Hash computed, PDF/A stored with Object Lock (NN-09) | Immediate |
| Any → (shorter-notice ratification pending) | Meeting held at shorter notice without ID present | Ratification at next meeting with ≥ 1 ID; minutes circulation blocked until recorded |

### 5.2 Circular resolution

`DRAFT → CIRCULATED → (DEMAND_FOR_MEETING → converted to agenda item) | PASSED | FAILED | LAPSED → NOTED_AT_NEXT_MEETING`. Guard: matter permitted by circulation; voters = entitled non-interested members; PASSED when approvals > 50% of entitled voters before the deadline; DEMAND_FOR_MEETING when ≥ one-third of directors in office so demand.

### 5.3 Composition validation (pseudo-code)

```ts
function evaluateBody(body: Body, at: Date): CompositionResult {
  const roles = body.statutoryRoles;                 // e.g. [AUDIT_COMMITTEE, RMC]
  const rules = rulePacks.resolve(roles, body.entity, at);  // effective-dated, layered L1..L4
  const members = body.membersAt(at);
  const findings = rules.flatMap(r => r.check(members, body.chairAt(at), body.entity));
  const atRisk = rules.flatMap(r => r.forecast(members, at, settings.get('gov.composition.warning_days'))); // tenure ends, KYC lapses
  return { status: worst(findings, atRisk), findings, atRisk, inputsHash: hash(members, rules.versions) };
}
// Triggered by: person attribute change, membership change, rule-pack publish, entity threshold change, daily job.
// Each failing finding upserts cmp.issue(source='GOVERNANCE', key=body.id+rule.id) with LR citation.
```

### 5.4 ROC filing instance

`IDENTIFIED → DATA_PREP → IN_REVIEW → APPROVED_FOR_FILING → FILED (SRN) → (UNDER_PROCESSING → RESUBMISSION_REQUIRED → FILED) → APPROVED | REJECTED → CLOSED`. Maker ≠ checker between DATA_PREP and APPROVED_FOR_FILING; additional-fee accrual starts at due date + 1; a filing cannot be closed without SRN, challan and acknowledgement evidence.

### 5.5 Reg 30 disclosure case

`DETECTED → ASSESSING (Para A deemed / Para B test) → NOT_MATERIAL (reason, approver) | DRAFTING → APPROVED → DISSEMINATED (exchange ack time) → CLOSED`; clock starts at the event's `occurred_at` (or board conclusion time); breach recorded with delay reasons for the disclosure (Reg 30(6) proviso requires explanation of delay).

### 5.6 Declaration campaign

`PLANNED → ISSUED → (per person: PENDING → SUBMITTED → UNDER_REVIEW → ACCEPTED | RETURNED) → CLOSED`; reminders at configurable intervals; non-submission at deadline escalates to the chair/NRC and opens a compliance issue.

### 5.7 Register entry

`PROPOSED (from event or manual) → VERIFIED (checker) → POSTED`; corrections: `POSTED → CORRECTION_PROPOSED → CORRECTION_POSTED` (the original remains with strike-through; D-02).

---

## 6. Screens and UX

Menu root in the tenant app: **Governance** (icon: gavel), visible to roles with any `gov.*` permission. Every screen has "i" help keys (`hlp.gov.*`) explaining terms such as *quorum*, *circular resolution*, *KMP*, *UPSI*, *SDD*, *Schedule XII*.

| Screen ID | Name | Menu path | Key content and fewer-click design |
|---|---|---|---|
| SCR-GOV-01 | CS Dashboard | Governance › Home | Widgets in §4N; each opens a work list; keyboard `g h` |
| SCR-GOV-02 | Governance Blueprint | Governance › Blueprint | Per entity; lines grouped by organ/committee/KMP/policy/filing; status chips; "Why required?" drawer with rule chain; "Fix" button opens the remediation workflow pre-filled |
| SCR-GOV-03 | Entity Master | Governance › Entities › {entity} | Tabs: Profile, Capital, Listing, Licences, Auditors, Group, Documents (MoA/AoA versions); "Refresh from MCA" with field diff |
| SCR-GOV-04 | Group Structure | Governance › Entities › Group tree | Interactive tree; RP graph overlay; export PNG/PDF/XLSX |
| SCR-GOV-05 | People — Directors & KMP | Governance › People | Grid with category, DIN status, KYC due, DSC expiry, tenure end, limits used; bulk "Request declarations"; filter chips |
| SCR-GOV-06 | Person Governance Profile | Governance › People › {person} | Roles timeline, directorships, committees, declarations, fit-and-proper file, evaluations, training, interests |
| SCR-GOV-07 | Committees | Governance › Committees | Cards per committee with composition status; "New committee" from template; rename inline (tenant terminology) |
| SCR-GOV-08 | Committee Page | Governance › Committees › {committee} | Composition, ToR versions, calendar, meetings, decisions, recommendations, actions, documents, KPIs |
| SCR-GOV-09 | Annual Planner | Governance › Meetings › Planner | Year grid by body; gap-rule warnings; availability poll; drag to reschedule; "Generate cycle" |
| SCR-GOV-10 | Meeting Workspace | Governance › Meetings › {meeting} | Stepper: Notice → Agenda → Pack → Conduct → Minutes → Sign → Filings; status of each step |
| SCR-GOV-11 | Agenda Builder | inside SCR-GOV-10 | Template picker; auto-pulled items panel with "Add all suggested"; drag order; per-item classification; draft resolution editor |
| SCR-GOV-12 | Board Pack Builder | inside SCR-GOV-10 | Missing-paper checklist; preview book; publish; per-recipient watermark; interested-director banners |
| SCR-GOV-13 | Director Portal Home | Board Portal (separate shell for directors) | My meetings, unread papers, sign requests, circulars awaiting vote, messages |
| SCR-GOV-14 | Board Book Reader | Board Portal › Meeting › Book | Paged reader, annotations, item navigation, Q&A to presenter, read progress, step-up MFA for UPSI |
| SCR-GOV-15 | Meeting Conduct Console | Meeting › Conduct | Live attendance/quorum, item decisions, interested-director exit/entry, actions, notes; VC roll-call checklist |
| SCR-GOV-16 | Minutes Editor | Meeting › Minutes | SS-1 skeleton; Vidhi draft paragraphs with accept/reject; director comments pane; timers bar |
| SCR-GOV-17 | Circular Resolution | Governance › Circular resolutions | Create from template; live tally; demand-for-meeting indicator |
| SCR-GOV-18 | General Meeting Builder | Governance › General meetings | Notice + explanatory statement; record date; e-voting export/import; results; MGT-15 |
| SCR-GOV-19 | Resolutions Library | Governance › Library | Templates by category; merge preview; follow-on obligations preview |
| SCR-GOV-20 | Decisions & Actions | Governance › Decisions | Register of decisions; action tracker; ATR generator |
| SCR-GOV-21 | Statutory Registers | Governance › Registers | Register list with last posting and reconciliation status; open register grid; export; inspection requests |
| SCR-GOV-22 | Register Entry Review | Registers › Pending | Maker/checker queue for proposed entries and corrections |
| SCR-GOV-23 | ROC Filings | Governance › Filings | Calendar and list; data sheet; attachments; DSC readiness; SRN capture; additional-fee meter |
| SCR-GOV-24 | Declarations & Fit-and-Proper | Governance › Declarations | Campaigns; per-person status; NRC review pane; certificate generator for CEO/MD |
| SCR-GOV-25 | Regulator Approvals | Governance › Approvals | PRAVAAH packs, change-in-management, MD/CEO approvals with status |
| SCR-GOV-26 | LODR Calendar | Governance › Listed › Calendar | Periodic filings; exchange format files; acknowledgements |
| SCR-GOV-27 | Disclosure Cases (Reg 30) | Governance › Listed › Disclosures | Live clocks; materiality test; draft; approve; acknowledgement capture |
| SCR-GOV-28 | RPT Monitor | Governance › Listed › RPT | Per related party cumulative vs Schedule XII threshold; approvals; subsidiary RPTs |
| SCR-GOV-29 | Insider Trading | Governance › Listed › PIT | Designated persons, trading window, pre-clearance, disclosures, SDD (append-only view) |
| SCR-GOV-30 | Annual Report Builder | Governance › Annual report | Data pack status by source; sections with owners; Vidhi drafts; DOCX export |
| SCR-GOV-31 | Secretarial Audit Workspace | Auditor shell | Read-only evidence; checklist; queries |
| SCR-GOV-32 | LLP Governance | Governance › LLP | Partners, agreement versions, Forms 3/4/8/11 |

Empty states: "No committees yet — apply the blueprint to create the committees your entity needs (2 clicks)". Error states always name the rule and the fix. Bulk actions: request declarations; reschedule meetings; assign filings; export registers. Shortcuts: `n m` new meeting, `n r` new resolution, `/` search within governance.

---

## 7. Backend design

### 7.1 Modules touched

`gov` (owner), `pol` and `dms` (documents, templates, eSign, DSC hand-off), `wf` (tasks, approvals, calendar, notifications), `cmp` (issues and compliance instances), `cfg` (rule packs, terminology), `hr` (person master projection), `int` (MCA data, conferencing, e-voting export, exchange files)

Shared packages (master OP-1, X-26): approvals, maker-checker, escalations and SLAs use `packages/workflow`; reminders, digests and the Work Inbox use `packages/notify`; calendar entries and external sync use `packages/calendar` (all owned by P04); settings via `packages/config` (P02); documents via `packages/docgen` and `packages/redline` (P07); AI via `packages/ai` (P17); exports via `packages/export` (P19). This phase builds no parallel implementation., `ai` (drafting), `rpt` (dashboards), `xpt` (export), `core` (audit ledger, correction entries).

### 7.2 Tables (schema `gov`; all with `tenant_id`, `legal_entity_id`, RLS, bitemporal columns `valid_from`, `valid_to`, `recorded_at`)

| Table | Key columns |
|---|---|
| `gov.entities` | id, constitution, cin_llpin, incorporation_date, fy_start_month, listing_profile jsonb, licences jsonb, capital jsonb, ro_address, register_locations jsonb |
| `gov.entity_relations` | parent_entity_id, child_entity_id, relation_type, holding_pct, effective dates |
| `gov.blueprints` / `gov.blueprint_lines` | blueprint version, entity, generated_at, rule_pack_versions[]; line: requirement_type, requirement_key, lr_ids[], layer, status, inputs_hash, issue_id |
| `gov.officer_roles` | person_id, role_type (DIRECTOR, KMP, SENIOR_MGMT, FUNCTIONARY), category, designation, appointed_on, term_end, ceased_on, approval_refs jsonb |
| `gov.director_profiles` | person_id, din, din_status, kyc_last_filed, kyc_next_due, dsc jsonb (no key material), iicadb_status, limits_snapshot jsonb |
| `gov.bodies` | id, body_type (BOARD, COMMITTEE, BOM, GENERAL_BODY, ID_MEETING), display_name (tenant term), statutory_roles[], tor_document_id, quorum_rule_id, cadence_rule_id |
| `gov.body_memberships` | body_id, person_id, member_role (CHAIR, MEMBER, SECRETARY, INVITEE), valid_from, valid_to |
| `gov.composition_evaluations` | body_id, evaluated_at, status, findings jsonb, inputs_hash |
| `gov.meetings` | id, body_id, meeting_type, serial_no, scheduled_at, venue, vc_link_ref, status, notice_issued_at, shorter_notice jsonb |
| `gov.agenda_items` | meeting_id, seq, title, item_type, classification, owner_id, presenter_id, source_ref (module, id), draft_resolution_id, required_majority, interested_person_ids[] |
| `gov.pack_versions` | meeting_id, version, built_at, item_versions jsonb, pdf_document_id, hash |
| `gov.attendance` | meeting_id, person_id, mode, joined_at, left_at, rollcall_evidence jsonb |
| `gov.decisions` | meeting_id/circular_id, agenda_item_id, outcome, votes jsonb, dissent jsonb, resolution_text, effective_on |
| `gov.minutes` | meeting_id, draft_versions (document refs), circulated_at, comments_close_at, signed_at, signed_by, sealed_hash, status |
| `gov.circular_resolutions` | id, body_id, circulated_at, deadline, status, tally jsonb |
| `gov.register_definitions` / `gov.register_events` / `gov.register_rows` (projection) | definition: code, legal_basis, columns schema; event: register_code, event_type, payload, source_ref, maker, checker, posted_at, correction_of |
| `gov.inspection_requests` | requester, register_codes[], status, fee_invoice_id |
| `gov.filing_definitions` / `gov.filing_instances` | definition: form_code, portal, trigger, due_rule, fee_rule, attachments[]; instance: entity, period/event_ref, due_on, status, srn, challan, filed_on, evidence_ids[] |
| `gov.declaration_campaigns` / `gov.declarations` | campaign type, population, deadline; declaration: person, form_code, payload, signed_document_id, status, reviewer |
| `gov.regulator_approvals` | approval_type, regulator, portal (PRAVAAH, etc.), reference_no, status, documents |
| `gov.lodr_obligations` / `gov.disclosure_cases` | case: event_ref, para (A/B), materiality jsonb, clock_start, disseminated_at, exchange_ack, delay_reason |
| `gov.rpt_transactions` / `gov.rpt_approvals` | related_party_id, nature, amount, fy, cumulative, approval refs |
| `gov.pit_designated_persons` / `gov.pit_trading_windows` / `gov.pit_preclearances` / `gov.pit_disclosures` | — |
| `gov.sdd_entries` | upsi_id, nature, sharer_person_ref, recipient_ref, shared_at, channel, source (AUTO/MANUAL), hash_prev, hash (append-only, separate hash chain) |
| `gov.annual_report_projects` / `gov.annual_report_sections` | fy, template_id, section_key, owner, data_bindings jsonb, draft_document_id, status |

### 7.3 APIs (REST, `/api/v1/gov/...`; all require tenant and legal-entity scope; mutations need `Idempotency-Key`)

`GET /entities/{id}/blueprint` · `POST /entities/{id}/blueprint:evaluate` · `POST /entities/{id}:refresh-mca` · `GET|POST /bodies` · `POST /bodies/{id}/memberships` · `GET /bodies/{id}/composition` · `POST /meetings` · `POST /meetings/{id}:issue-notice` · `POST /meetings/{id}/agenda-items` · `POST /meetings/{id}/pack:build` · `POST /meetings/{id}/pack:publish` · `POST /meetings/{id}/attendance` · `POST /meetings/{id}/decisions` · `POST /meetings/{id}/minutes:draft` (async, Vidhi) · `POST /meetings/{id}/minutes:circulate` · `POST /meetings/{id}/minutes:sign` (returns eSign envelope) · `POST /circulars` · `POST /circulars/{id}/votes` · `GET /registers/{code}` · `POST /registers/{code}/events` · `POST /registers/{code}/corrections` · `GET /filings?due_before=` · `POST /filings/{id}/data-sheet:generate` · `POST /filings/{id}:record-srn` · `POST /declarations/campaigns` · `POST /declarations/{id}:submit` · `POST /disclosures/cases` · `POST /disclosures/{id}:record-dissemination` · `GET /rpt/monitor` · `POST /pit/preclearances` · `GET /pit/sdd?from=&to=` (export only; no update or delete endpoint exists) · `POST /annual-reports/{fy}/sections/{key}:draft`.

### 7.4 Domain events (CloudEvents; internal `type` prefix `in.lawdocscomply.gov.`; events consumed by other products are re-published by `int` as `in.infrabyx.governance.<EventName>.v1` per Ecosystem Spec §6.23 and X-01)

`BlueprintEvaluated`, `GovernanceGapDetected`, `GovernanceGapResolved`, `CommitteeConstituted`, `CommitteeCompositionChanged`, `CompositionBreachDetected`, `DirectorAppointed`, `DirectorCeased`, `KmpAppointed`, `KmpCeased`, `MeetingScheduled`, `NoticeIssued`, `BoardPackPublished`, `MeetingConcluded`, `DecisionRecorded`, `MinutesCirculated`, `MinutesSigned`, `MinutesSealed`, `CircularResolutionPassed`, `RegisterEntryPosted`, `RegisterCorrectionPosted`, `FilingDue`, `FilingFiled`, `FilingOverdue`, `DeclarationSubmitted`, `FitAndProperCertified`, `RegulatorApprovalRecorded`, `DisclosureCaseOpened`, `DisclosureDisseminated`, `DisclosureDelayed`, `RptThresholdApproaching`, `TradingWindowClosed`, `TradingWindowOpened`, `SddEntryRecorded`, `AnnualReportDraftReady`. Ecosystem consumers (Integration Spec v1.1 §6.23 `governance`): Finbyx consumes `DirectorAppointed/Ceased`, `KmpAppointed/Ceased` and `CommitteeCompositionChanged` for its authority matrix; P04 consumes gap and filing events.

### 7.5 Jobs and Temporal workflows

`MeetingLifecycleWorkflow` (timers for notice, notes, minutes 15/7/30-day clocks); `CircularResolutionWorkflow`; `DeclarationCampaignWorkflow`; `FilingInstanceWorkflow` (due, overdue, fee accrual); `DisclosureClockWorkflow` (minute-granularity timers); `BlueprintNightlyEvaluation` (02:00 IST); `RegisterReconciliationMonthly`; `TradingWindowScheduler` (quarter ends, results dates); `DirectorLimitsDaily`; `McaRefreshWeekly` (if enabled); `AnnualCycleGenerator` (on FY rollover).

---

## 8. Integrations (ports and adapters; contracts in Appendix L)

| Port | Adapter(s) | Use |
|---|---|---|
| `COMPANY_DATA_PORT` | Licensed MCA data providers (e.g., Probe42, Signzy, Surepass, Perfios/Karza — selection in P18) | Master data, directors, charges, filing status refresh |
| `CONFERENCING_PORT` | Microsoft Teams (Graph online meetings), Zoom, Google Meet | Links, participant logs, recordings retrieval (Rule 3 custody) |
| `CALENDAR_PORT` | M365, Google, ICS/CalDAV (P04) | Meeting holds and updates |
| `ESIGN_PORT` / `DSC_PORT` | Aadhaar eSign through CCA-empanelled ESPs via ASP adapters (Leegality, Digio, SignDesk, Surepass, Protean) (X-04); DSC signing via signer utility | Minutes, declarations, certificates |
| `EVOTING_PORT` | File-based export/import for NSDL, CDSL, KFin, MUFG Intime | Resolutions, voter lists (BENPOS), results |
| `EXCHANGE_FILES_PORT` | NSE NEAPS / BSE Listing Centre formats (XBRL utilities, PDF) | Prepare files only; human upload |
| `RTA_PORT` | BENPOS and shareholding files (CSV/fixed width) | MGT-1 reconciliation, record-date lists |
| `HRMS_PORT` | P13 internal; external HRMS via P18 | Person master, org, remuneration |
| `ECOSYSTEM_PORT` | Finbyx, Udofin (Integration Spec v1.1) | Portfolio, ratios, investment book, RPT transactions, governance events |
| `ACCOUNTING_PORT` | P11 accounting bridge / Tally import | Financial statements, related-party ledger |

---

## 9. Settings and configuration (registered in P02; tiers per NN-28)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `gov.notice.board_min_days` | G | 7 | ≥ statutory value | CS + checker |
| `gov.notice.shorter_notice_requires_id` | L | true | — | — |
| `gov.notes.min_days_before` | G | 7 | ≥ SS-1 value | CS |
| `gov.minutes.draft_circulation_days` | G | 15 | ≤ SS-1 value | CS |
| `gov.minutes.comment_days` | G | 7 | SS-1 value | CS |
| `gov.minutes.entry_days` | L | 30 | — | — |
| `gov.minutes.reminder_offsets_days` | T | [3, 0] | 0–10 | CS |
| `gov.circular.response_days` | G | 7 | 1–15 | CS |
| `gov.pack.watermark` | T | `name+email+timestamp` | — | CS |
| `gov.pack.interested_director_access` | G | `VIEW_WITH_BANNER` | `VIEW_WITH_BANNER`/`HIDE` | CS + chair |
| `gov.portal.download` | T | OFF | ON/OFF | CS |
| `gov.portal.session_timeout_min` | T | 15 | 5–60 | Admin |
| `gov.portal.upsi_step_up_mfa` | L | true | — | — |
| `gov.meeting.transcription` | T | OFF | requires consent capture | CS |
| `gov.vc.restricted_items` | G | [] | rule pack | Platform content |
| `gov.gm.vc_allowed` | G | per MCA circular (effective-dated) | — | Platform content |
| `gov.composition.warning_days` | T | 60 | 15–180 | CS |
| `gov.filings.reminder_offsets_days` | T | [15, 7, 3, 1] | — | CS |
| `gov.filings.show_additional_fee_meter` | T | ON | — | CS |
| `gov.lodr.materiality_thresholds` | G | per board policy | ≤ Reg 30(4) lower-of test | CS + Board resolution reference |
| `gov.lodr.disclosure_clock_alerts_min` | T | [15, 5] (board outcome) | — | CS |
| `gov.rpt.alert_pct` | T | [80, 100] | 50–100 | CS |
| `gov.pit.trading_window_reopen_hours` | G | 48 | ≥ 48 | Compliance officer |
| `gov.pit.preclearance_validity_trading_days` | G | 7 | ≤ 7 | Compliance officer |
| `gov.declarations.reminder_interval_days` | T | 3 | 1–7 | CS |
| `gov.mca_refresh.enabled` | T | OFF | requires adapter contract | Admin |
| `gov.annual_report.template_id` | T | platform default | tenant template | CS |
| `gov.terminology.*` | T | statutory names | free text | Admin |

---

## 10. Security, privacy and audit

- **BOARD_CONFIDENTIAL** class (NN-13): agenda papers marked confidential, all minutes drafts, annotations, director messages, voting records, UPSI items — separate tenant data key, no AI training (NN-15), excluded from analytics and from search results for non-members; Vidhi only acts for an authorised user.
- **Sealed minutes and registers (NN-36)**: SHA-256 hash, PDF/A, Object Lock WORM (NN-09); signed minutes (`gov.minutes` rows in status `SEALED`) and attendance registers have no update or delete path at the database level (`REVOKE UPDATE, DELETE` from the application role; inserts only, enforced by a trigger that rejects updates to sealed rows), and no edit API; corrections only by a later entry, Correction Entry or later register event (s.118(8); D-02, NN-02). Super-admin overrides on governance data follow D-02 and are visible to the tenant in the governance audit view.
- **SDD**: separate hash chain; append-only table with database-level `REVOKE UPDATE, DELETE`; daily chain verification job; eight-year minimum retention; export with integrity certificate.
- **Signatures**: DSC private keys never touch the platform; Aadhaar eSign through CCA-empanelled ESPs via ASP adapters with consent and transaction evidence (P07, X-04).
- **Access**: directors see only bodies they belong to; interested-director restrictions; step-up MFA for UPSI; watermarks; download off by default; device/session management for the portal; full access log per document (who opened which page when, for UPSI items).
- **Regulator view** (D-12): time-boxed read-only grant; UPSI and BOARD_CONFIDENTIAL items excluded unless the tenant explicitly includes them; every page view logged and visible to the tenant.
- **Identity minimisation** (NN-12): PAN masked; Aadhaar never stored; DIN is not sensitive but personal; relatives' data in PIT records minimised to what Reg 9/Schedule B requires.
- **Audit events**: every view, download, share, sign, decision, register posting, filing status change and override is a ledger event (NN-02).

---

## 11. AI touchpoints and guardrails (Vidhi; Appendix K)

| Touchpoint | What Vidhi does | Guardrail |
|---|---|---|
| Agenda suggestions | Proposes items from due obligations, policies, reports and gaps | Suggestions only; CS adds |
| Notes on agenda | Drafts background notes from linked records (e.g., ALM report summary from Finbyx data) with citations to source records | Numbers are inserted from data bindings, never generated (NN-22); draft badge |
| Board-pack summary | Executive summary per item and for the book; "questions a director may ask" with citations | Visible to members only; labelled AI |
| Minutes draft | SS-1 skeleton filled from decisions, attendance, notes and consented transcript | Every paragraph needs CS acceptance; dissent and interest disclosures are taken from the conduct console, never inferred |
| Resolution drafting | Fills templates and suggests wording for non-standard items | Legal basis must be selected by CS; follow-on obligations computed by rules, not AI |
| Annual report narrative | Drafts MD&A and Board's report narrative sections from the data pack | Every figure is a bound value; narrative marked draft; CFO/CS approval |
| Declarations | Pre-fills from MCA data and registers; explains fields | Director confirms; AI never signs |
| Reg 30 assistance | Explains whether an event is Para A or Para B and drafts the announcement | Materiality decision recorded by an authorised KMP; clock never paused by AI |
| Q&A | "What does SS-1 say about…", "When is MGT-7 due?" from the knowledge notebook (P17) | Cited answers; no source → says so (NN-06) |

AI never: signs, files, disseminates to exchanges, approves minutes, changes composition, posts register entries or decides materiality (NN-14).

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p06/*.feature`)

```gherkin
Feature: Governance blueprint
  Scenario: Listed NBFC-ML blueprint includes sector and LODR overlays
    Given entity "Alpha Finance Ltd" is listed on NSE with equity, RBI layer "NBFC-ML", asset size ₹6,200 crore
    When the CS evaluates the governance blueprint
    Then the blueprint requires an Audit Committee with at least 3 members and two-thirds independent directors citing LR-SEBI-018
    And requires a Chief Risk Officer citing the NBFC Governance Directions para 19
    And requires an annual fit-and-proper declaration as on 31 March citing para 13(3)
    And every line shows at least one LR citation

  Scenario: Independent director tenure ending raises an at-risk line
    Given an independent director's second term ends in 45 days and the warning window is 60 days
    When the nightly evaluation runs
    Then the Audit Committee composition shows AT_RISK
    And a CS task "Plan replacement of independent director" is created with the rule cited

Feature: Board meeting notice
  Scenario: Notice shorter than seven days forces urgency path
    Given a board meeting scheduled 4 days from today
    When the CS issues the notice
    Then the system requires an urgency ground
    And records that ratification by an independent director is pending if none attends
    And blocks circulation of draft minutes until ratification is recorded

Feature: Minutes discipline
  Scenario: Signed minutes cannot be edited by anyone
    Given minutes of meeting BM-2026-07 are SEALED
    When a super admin attempts to update the minutes text through any API
    Then the request is rejected with LDC-GOV-031
    And the only available action is "Add correction note to next meeting"

  Scenario: Draft circulation clock escalates
    Given a meeting concluded 13 days ago and draft minutes are not circulated
    Then the CS and chair receive an escalation notification
    And the CS dashboard shows the minutes clock in red with 2 days remaining

Feature: Interested director handling
  Scenario: Interested director is excluded from quorum on an item
    Given director D has disclosed interest in "XYZ Pvt Ltd" in MBP-1
    And agenda item 6 approves a contract with "XYZ Pvt Ltd"
    When item 6 is taken up in a public company board meeting
    Then the quorum monitor excludes D for item 6
    And the minutes draft records that D did not participate in item 6

Feature: Registers from events
  Scenario: Allotment updates the register of members and opens PAS-3
    Given a board decision allotting 10,000 equity shares to 3 allottees is recorded
    When the decision is finalised
    Then proposed MGT-1 entries are created for checker verification
    And a PAS-3 filing instance is created with the computed due date

Feature: Insider trading
  Scenario: Opening a UPSI board-pack item writes an SDD entry
    Given agenda item 2 "Q2 results" is classified UPSI
    When director D opens the item for the first time
    Then an SDD entry is recorded with nature, sharer, recipient and timestamp
    And the SDD table rejects any update or delete operation

Feature: Reg 30 disclosure
  Scenario: Board outcome disclosure clock
    Given a board meeting of a listed company concludes at 17:42 IST with financial results approved
    Then a disclosure case opens with a 30-minute clock ending 18:12 IST
    And if dissemination is recorded after 18:12 the case requires a delay reason

Feature: RPT thresholds
  Scenario: Schedule XII threshold alert for turnover above ₹20,000 crore
    Given consolidated turnover of ₹30,000 crore
    Then the materiality threshold is ₹3,500 crore
    And cumulative transactions of ₹2,800 crore with one related party raise an 80% alert

Feature: Fit and proper certificate
  Scenario: Quarterly statement generated for MD/CEO signature
    Given an NBFC-ML with one director appointment in Q2
    When the quarter closes
    Then a statement of changes in directors with the MD/CEO certificate is generated
    And a submission task is due 15 days after quarter end

Feature: Annual report lineage
  Scenario: Every figure in the Board's report is traceable
    Given the Board's report draft for FY 2025-26
    When the CFO opens any figure
    Then the source dataset, computation and version are shown
```

NN tests: `NN-02_sealed_minutes_immutable`, `NN-02_register_correction_preserves_original`, `NN-04_minutes_draft_requires_acceptance`, `NN-05_register_maker_not_checker`, `NN-06_blueprint_lines_cited`, `NN-07_threshold_rule_pack_effective_dated`, `NN-08_no_mca_auto_filing`, `NN-09_sealed_minutes_hash_verified`, `NN-13_board_confidential_excluded_from_analytics`, `NN-14_vidhi_cannot_sign_or_disseminate`, `NN-18_regulator_view_excludes_upsi_by_default`.

---

## 13. Deliverables and exit gate

**Deliverables:** `gov` module with migrations; seeded rule packs (Companies Act thresholds, SS-1/SS-2 timelines, LODR, PIT, RBI NBFC/UCB/commercial bank governance, IRDAI CG 2024, LLP, Societies Registration Act base); committee templates; register definitions; filing catalogue; resolution and document templates (DOCX); board portal shell; Temporal workflows; dashboards; Vidhi prompt templates for agenda notes, minutes and annual report; export mapping to `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` (Appendix M); acceptance and NN tests; `docs/phases/P06-plan.md` and `docs/phases/P06-handover.md`.

**Exit gate:**

1. All Gherkin scenarios and NN tests green; domain analyst signs golden blueprints for the eight seeded profiles.
2. One full board-meeting cycle run end to end with a pilot tenant (notice → sealed minutes → MGT-14 data sheet → SRN recorded) with timers verified.
3. Register reconciliation produces zero unexplained differences on the pilot's data.
4. Listed-company module demonstrated on a synthetic listed NBFC: LODR calendar, Reg 30 case, RPT monitor, SDD auto-entries.
5. Accessibility (WCAG 2.2 AA) audit of the board portal and minutes editor passed (NN-21).
6. Export of `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` validated: signed minutes open in a PDF reader, registers open in Excel, folder names self-explanatory.
7. All **[VERIFY]** items for features enabled at go-live closed or behind OFF flags.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P06-01 | Para-level citations of revised SS-1/SS-2 (effective 1 Apr 2024) for notice, notes, minutes timelines, circular resolutions | ICSI text to be checked para by para | CS domain analyst | Use values in §9 (aligned with Act); citations shown as "SS-1 [VERIFY]" |
| OI-P06-02 | Corporate Laws (Amendment) Bill 2026 — enacted status and threshold changes for Companies Act and LLP Act | Bill introduced in Lok Sabha (reported Apr 2026) | Company Secretary | Rule packs carry current thresholds; new pack version on enactment |
| OI-P06-03 | Director KYC revised form name and event-based update timeline under the 2025 amendment rules | ICAI note does not name form | CS analyst | Filing definition `DIR_KYC_TRIENNIAL` with due 30 Jun 2028 |
| OI-P06-04 | RBI (Commercial Banks – Governance) Directions 2025 para mapping | Not yet extracted | P15 stream / RBI analyst | Bank governance pack ships behind `pack.rbi_cb_governance.enabled = OFF` |
| OI-P06-05 | Final status of the June 2026 draft NBFC Governance Amendment Directions (CCO/HIA) and the July 2026 RBI/DoS/2026-27/460–468 directions | Draft proposed effective 1 Jan 2027 | RBI analyst | Seed current 2025 text; draft rules as future-dated version flagged `draft` |
| OI-P06-06 | MCA general circular currently permitting VC/OAVM general meetings and its validity | Circulars are periodically extended | CS analyst | `gov.gm.vc_allowed` default false after last known expiry date |
| OI-P06-07 | Restricted items for VC board meetings after omission of Rule 4 (2021) and revised SS-1 wording | Confirm no re-notification | CS analyst | `gov.vc.restricted_items = []` |
| OI-P06-08 | Reg 30(6) disclosure timelines and Reg 30(11) rumour-verification applicability as on go-live | LODR amended frequently | Listed-company analyst | Clocks as in §4K; flag `gov.lodr.rumour_verification` per entity |
| OI-P06-09 | PIT pre-clearance validity, continual disclosure trigger and trading-plan rules after 2024–2025 amendments | Amendments | Compliance analyst | Settings bounded by current text |
| OI-P06-10 | HVDLE threshold and debt-listed governance applicability | 2025 amendment | Listed-company analyst | Chapter V pack OFF unless entity marks HVDLE |
| OI-P06-11 | MCA additional-fee schedules and CHG-1 extension windows after the 2019/2020 amendments | Fee rules | CS analyst | Fee meter shows "statutory additional fee [VERIFY]" |
| OI-P06-12 | IRDAI Master Circular on Corporate Governance 2024 — board meeting frequency and specific committee quorum rules | Not captured in secondary source | Insurance analyst | Use Companies Act defaults for insurers until verified |
| OI-P06-13 | Licensed MCA data provider selection and terms (no scraping) | Vendor contract | CTO | `gov.mca_refresh.enabled = OFF` |
| OI-P06-14 | E-voting agencies' current file formats | Agency specifications | Integration analyst | Manual CSV template |
| OI-P06-15 | Whether NBFC s.186(11) exemption interpretation for MBP-2 should default ON for NBFCs in the ordinary course of business | Interpretation | Company Secretary | Default: maintain MBP-2 for non-ordinary-course items; [INTERP] banner |

---

## 15. Sources (accessed 25 October 2026; primary sources first)

1. Companies Act, 2013 and Rules (Meetings of Board and its Powers Rules 2014; Management and Administration Rules 2014; Appointment and Qualification of Directors Rules 2014; Accounts Rules 2014; Share Capital and Debentures Rules 2014; Registration of Charges Rules 2014; Significant Beneficial Owners Rules 2018) — https://www.mca.gov.in (Acts & Rules).
2. ICSI, Announcement on Revised Secretarial Standards (SS-1, SS-2) effective 1 April 2024, 13 Feb 2024 — https://www.icsi.edu/media/webmodules/Announcement_on_Revised_Secretarial_Standards_13022024.pdf
3. Lexplosion summary of revised SS-1/SS-2 — https://lexplosion.in/icsi-revises-secretarial-standards-for-board-and-general-meetings-in-conformity-with-companies-act-2013-effective-april-1-2024/
4. RBI (Non-Banking Financial Companies – Governance) Directions, 2025, RBI/DOR/2025-26/344, 28 Nov 2025 — summary at https://taxguru.in/rbi/rbi-non-banking-financial-companies-governance-directions.html
5. RBI (Urban Co-operative Banks – Governance) Directions, 2025, RBI/DOR/2025-26/273, 28 Nov 2025 — https://website.rbi.org.in/documents/d/rbi/urban-cooperative-banks_governance ; https://taxguru.in/?p=1010802
6. RBI (Commercial Banks – Governance) Directions, 2025 — https://website.rbi.org.in/documents/d/rbi/commercial-banks-governance
7. Vinod Kothari, Harmonisation and consolidation of instructions on control and assurance functions for NBFCs (draft amendment directions, June 2026) — https://vinodkothari.com/2026/06/harmonisation-and-consolidation-of-instructions-on-control-assurance-functions-for-nbfcs/
8. SEBI (LODR) (Fifth Amendment) Regulations, 2025, SEBI/LAD-NRO/GN/2025/273, 18 Nov 2025 — summary at https://webiis10.mondaq.com/india/securities/1738326/sebi-has-amended-the-sebi-lodr-regulations-with-significant-changes-in-the-rpt-framework
9. SEBI (Prohibition of Insider Trading) (Amendment) Regulations, 2025 (11 Mar 2025, effective 9 Jun 2025) — https://www.azbpartners.com/bank/sebi-amends-insider-trading-regulations-2/
10. IRDAI (Corporate Governance for Insurers) Regulations, 2024 and Master Circular 2024 — https://www.jsalaw.com/?p=50709 ; https://actuariesindia.org/sites/default/files/inline-files/16.%20Master%20Circular%20on%20Corporate%20Governance%20for%20Insurers%2C%202024.pdf
11. ICAI CLCGC, Director KYC compliance update (2 Jan 2026) — https://www.icai.org/post/clcgc-director-kyc-compliance-02012026
12. Migration of 38 Companies Act forms to MCA21 V3 (14 Jul 2025) — https://ksandk.com/corporate/38-forms-companies-act-2013-mca21-v3-portal/
13. Corporate Laws (Amendment) Bill, 2026 — https://www.scconline.com/blog/post/tag/nfra-reforms/
14. Diligent Boards GovernAI (benchmark only) — https://www.diligent.com/features/boards/boards-ai
15. Owner's baseline: LawDocs Comply Architecture Part 1 (Statutory Registers, Minutes of Meeting) and Part 2 (ROC, Companies, LLP, Secretarial Function Map, Listed-Company Governance, Documents & Forms Library).

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-36, NN-37; X-26, X-30 (LODR Reg 24A conflict check), X-37 (MBP-1/MBP-4/deposit register corrections); committee and KMP seeds come from P15 §4F and are not redefined here**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

