# Appendix N — Neutral Governance, Grading, Qualifying Assessment, Code of Conduct, Allocation, Complaints, Training Pathways and Private ADR Chambers

> **Binding reference specification** (v2.0, 21 October 2026). Read with `01_MASTER_PROMPT.md` (NN-03, NN-16, NN-17, NN-28, NN-29), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-30 to R-35; D2-12 to D2-17), phases P03 and P10, Appendices B (fee figures), C (screens), E §9 (AI Governance Rule), F (canonical tables), G (Legal Rules Register), O (plans), P (copy), S (portals, RBAC). Research base: S6 (primary), S5 Part C1–C3, S9 §1.3–§1.5. Precedence follows master §15: where this appendix changes a P03 or P10 requirement, the **Phase addendum** at the end of this file is the instrument of change and the phase file's original text is superseded to that extent.
>
> **v3.0 and v3.1 reading (24 October 2026).** Read with NN-33 to NN-40 and master X-26, X-29, X-31, X-47–X-49, X-54, X-59–X-62. Appendix W (v3) is canonical for the Chambers workspace, practice pages, chambers settings and practice HR; Appendix AA for the Private Practice Marketplace and the Professional Registry; Appendix AB for revenue streams; Appendix O for plan entitlements. Where §8 of this appendix differs from them, they prevail and §8 is the v2 baseline. Reconciliations are CN-13 to CN-17 below; v3.1 changes are marked *(v3.1)*.

---

## 0. Scope, how to use, and conflicts resolved

### 0.1 What this appendix specifies

| § | Subject | Implementing phase |
|---|---|---|
| 1 | Institutional governance: Equator Institutional Committee, sub-committees, Registrar, Users' Forum, charter, decision records | P03 (objects, portal), P14 (charter adoption) |
| 2 | Neutral onboarding journey (apply → verify → assess → committee → induction → probation) and public directory | P03, P12, P13 |
| 3 | Grades A/B/C, competence gates, endorsements, probation, CPD, labels, re-grading | P03 |
| 4 | Equator Qualifying Assessment Programme (EQAP), case-allocation eligibility by grade | P03, P10 |
| 5 | Equator Code of Conduct for Neutrals (publishable text) | P03, P13 |
| 6 | Allocation and performance: filters → rotation → caps → capped Quality Index; Transparency Report | P03, P13 |
| 7 | Feedback, ratings and complaints | P03 |
| 8 | Private ADR Chambers (management's "private ADR courts") | P10, P13 |
| 9 | Training pathways, Equator ADR Institute, specialisations, country add-ons, CPD, referral model | P10, P03 |
| 10 | Equator Tech Readiness (ETR) and the Grade A Tech Concierge | P10, P04 |
| 11 | Data model, APIs, events, errors, flags, configuration keys | P03, P10 |
| 12 | Acceptance tests | P03, P10 |
| 13 | Open items and counsel questions | — |

### 0.2 Conflicts found and how this appendix resolves them

| # | Conflict | Resolution (binding) | Basis |
|---|---|---|---|
| CN-01 | P03 FR-P03-06 makes the grade a **score** (A ≥ 80, B 65–79, C 50–64). D2-12 makes the grade a **status tier** (entrant / > 15 years / retired judge or > 30 years). | Grade = status tier gated by competence (`grading_policy.v2`, §3). The P03 0–100 rubric survives as the **Assessment Score** (pass gate and Quality Index input), never as the grade. | D2-12; S6 §5.1 diagnosis |
| CN-02 | P03 FR-P03-12 public labels "Senior (A) / Experienced (B) / Associate (C)". | Public labels are **Distinguished (A) / Principal (B) / Associate (C) Neutral** (master X-26); grade letters stay internal. "Senior" is never used for a neutral tier because of confusion with "Senior Advocate" (Advocates Act 1961 s.16); copy lint blocks it (`LABEL_FORBIDDEN_TERM`) and the tier sub-label (§3.7) still applies. *(v3.1: v2 "Senior" label corrected to X-26)* | S6 S6-15; master X-26; J2-002 |
| CN-03 | P03 FR-P03-05 "Academy fast-track: holders of the vertical credential or ECM-A skip the role-play". This gives the affiliated Institute's graduates an assessment advantage. | Fast-track is available for **any** credential whose issuer supplies an observed-assessment evidence pack meeting the EQAP integrity standard (two assessors, ≥ 1 independent, published rubric), whoever the provider (§4.6). Ethics is never waived. | D2-17; IMI QAP criterion 7 (diversity) |
| CN-04 | S9 E-1 proposes an assessment fee "only for applicants without Academy certification". | **One fee for all candidates**, regardless of training provider (§4.8). Charging only non-Institute graduates is a tie-in signal (Competition Act 2002 s.3(4)(a)) and breaches D2-17. | D2-17; S6 §6.3 |
| CN-05 | Ratings threshold: P03 FR-P03-33 publishes after ≥ 5; P13 FR-P13-05 shows only at n ≥ 10. | Aggregates are **computed and shown to the neutral and committees at n ≥ 5**; the **public profile** process-rating aggregate and every **public Transparency Report / dashboard cell** require **n ≥ 10** (master X-28; stricter rule wins for public display). P03 text is amended by FR-P03-V2-17. | NN-28; IS 19000:2022 practice (S9 E-4) |
| CN-06 | Appendix G LR-ARB-007 sets a lender-portfolio rotation cap "default 2 per lender per neutral per 36 months"; P03 FR-P03-23 sets a relative 40%/24-month cap. A 2-per-36-months cap cannot be met in FIN bulk programmes. | Both caps exist as configuration. The **Fifth Schedule item 22 disclosure is always made** (legal rule). Default: LR-ARB-007 absolute cap applies to non-bulk FIN/COM/INS seats; the relative cap governs `source ∈ {bulk, api, clause_auto}` programmes pending the Board decision recorded in P03 OI-01. A `legal_reviewer` must confirm before FIN bulk go-live. | Master §15 precedence (G on legal rules; cap figure is configuration) |
| CN-07 | D2-12 requires retired judges acting as **mediators** to complete 40 hours of training; S6 §5.2 allows "40 h **or** ≥ 20 court-annexed mediations". | D2-12 prevails: **40 hours is mandatory**; MCPC 40-hour certificates satisfy it; a mediation record alone does not. | D2-12; MCPC Manual "irrespective of his background" |
| CN-08 | V6 uses a single endorsement `END-INT`; S6 uses `END-INT-MED` and `END-INT-ARB`. | `END-INT` is an **alias** that resolves to `END-INT-MED` for mediator/conciliator seats and `END-INT-ARB` for arbitrator seats (§3.6). | Consistency |
| CN-09 | S5 C1 names the body "Equator Court" with grades G1–G4. | Body = **Equator Institutional Committee** (D2-15); grades A/B/C (D2-12). "Court" never used (NN-17). | D2-15 |
| CN-10 | P03 committees: "Empanelment", "Appointments", "Ethics & Complaints", "Appeals". D2-15 lists seven sub-committees without Empanelment or Appeals. | Empanelment and grading decisions sit with the **Appointments Sub-Committee — Panel Bench**; case appointments with its **Case Bench**; appeals go to an **EIC Review Panel** of three members who did not sit below (§1.3). Old names map in §1.3. | D2-15 |
| CN-11 | P14 says rules and Code are approved "by the Board (or its Rules Committee where delegated)". | The Board adopts the Charter once; thereafter the **Rules Sub-Committee** approves the Code of Conduct, grading policy and allocation policy; the Board approves only fee schedules (Appendix B) and budgets. | D2-15 |
| CN-12 | Per-neutral set-aside counts appear in `core.neutral_scorecards` (Appendix F). | Set-asides and challenge outcomes are **not Quality Index inputs** (they depend on party choice to challenge and on court outcomes); they feed internal quality review only (P03 FR-P03-35). | NN-28; D2-13 |
| CN-13 *(v3.1)* | §2.5 and §6.1 (v2) say "no paid listings" without qualification; v3.0 permits labelled sponsored slots on the separate Private Practice Marketplace. | The **institutional directory `/neutrals`, allocation, eligibility, grading, Quality Index and conflict checks are never paid** (NN-28 v3.0 sentence; D2-14 retained). Paid placement exists only on the Private Practice Marketplace surface (Appendix AA), only for non-advocate private-practice neutrals and chambers, in a labelled slot, behind `marketplace.paid_placement` = OFF (NN-34, D3-01, D3-37). `NO_PAID_PLACEMENT` is extended to `mkp` sponsorship, ad and provider-subscription tables and to `rev` (Appendix AA §AA.10.6; AB RA-11). | NN-28; NN-34; D3-01 |
| CN-14 *(v3.1)* | §8.2 shows a percentage marketplace take for every Chambers plan. | The plan-dependent take (15/15/12/10%, X-31) applies on the Private Practice Marketplace only, and only to **non-advocate** providers; advocate-neutrals pay a flat fee for Equator's own services and no share of their fee is taken, pending counsel (X-59(c), X-62(d), D3-35). | BCI Rules Part VI Ch. II r.36, Ch. III r.2 |
| CN-15 *(v3.1)* | §8.3 "advocates/bar bodies get non-cash credits only" for referrals. | **No referral reward of any kind** — cash, credit, discount or priority — to advocates, CAs, CSs or CMAs or their firms; bar bodies and professional firms may be relationship partners without reward (X-54, X-60(b), X-62(a); D3-27). | NN-17 (as read with X-62); NN-34 |
| CN-16 *(v3.1)* | §9.6 contemplates "a fixed referral fee of ₹{x} per enrolment" from the Institute; §9.1 lists corrections C1–C11. | Training through equatoradr.com is a related-party stream booked at **₹0 to Equator by default**; any fee needs Board approval of an arm's-length arrangement under Companies Act 2013 s.188 (s.184 disclosure; s.177 only where an Audit Committee is mandatory) and the RS-22 registry record going `live` (D3-38; Appendix AB). The referral card stays OFF until corrections **C1–C20** (Appendix AF §AF.4.3, which renumbers and extends §9.1) are evidenced. | D3-38; X-29 |
| CN-17 *(v3.1)* | §8 (v2) specifies Chambers features, onboarding and terms. | Appendix W is canonical for the v3 workspace, practice pages (`/chambers/{slug}`, never linked from `/neutrals`, D3-15), roles `chambers_owner`, `chambers_case_manager`, `chambers_staff`, `chambers_hr`, `chambers_accounts` (X-47) and practice HR (X-49); §8 stays as the v2 baseline for anything W does not restate. | X-47–X-49 |

---

## 1. Institutional governance (D2-15)

### 1.1 Principle

Equator separates three things, as SIAC, ICC, LCIA and HKIAC do (S5 C1, B2): (i) the **company** (Equator Resolution Service Private Limited, "ERSPL") — budget, fees, staff, technology; (ii) the **institutional decision-maker** — the Equator Institutional Committee (EIC) and its sub-committees, which take every decision about neutrals and cases that the Equator Rules reserve to "the institution"; (iii) the **Registrar and Secretariat** — day-to-day administration. The ERSPL Board takes **no case decisions** and no decision on an individual neutral. No body is called a "Court" (NN-17; label validator §1.8).

### 1.2 Bodies

| Body | Composition | Powers | Independence safeguards |
|---|---|---|---|
| **ERSPL Board** | Directors under the Companies Act 2013 | Adopts the Charter by resolution; approves budgets and fee schedules (Appendix B, M-01); appoints EIC members on the Nominations Panel's recommendation (§1.5) | Board resolution delegates institutional powers to the EIC for the Charter term and records that it will not give directions on any case or neutral; directors may not be EIC members |
| **Equator Institutional Committee (EIC)** | Chair + Vice-Chair + 9–15 members. **Majority external** (§1.4). At least one-third women (target parity). At least 3 members with international practice for `INT`. At least 1 member each with financial-sector, insurance, labour and family-law experience | All institutional powers under the Equator Rules: appointments where the Rules reserve them, challenges, prima facie jurisdiction and consolidation before constitution (V6), time extensions within the Rules, fee fixing/reductions within schedules, scrutiny approvals, empanelment, grading, discipline, Rules and policy | 3-year terms, max 2 consecutive, one-third retire each year; annual conflict declaration; automatic recusal (§1.6); members do not sit as neutrals in Equator-administered matters while in office except with Review Panel approval recorded with reasons |
| **Sub-committees** (seven) | Drawn from EIC members; each ≥ 3 members, ≥ 1 external; Challenge and Ethics & Complaints: majority external and ≥ 1 member external to both EIC staff and Board | See §1.3 terms of reference | Written terms of reference; quorum; reasoned decisions; minutes |
| **Registrar** | Legally qualified (advocate ≥ 10 years or former judicial officer); Deputy Registrars per vertical; case counsel | Administration, scrutiny of form, deposits, notices, SLA monitoring, agenda and papers for sub-committees, issue of IEPs (P03 FR-P03-30) | Reports to the EIC Chair on case matters and to the CEO on HR only; cannot vote |
| **Users' Forum** (advisory) | Paying members: companies ₹1,50,000/yr, law firms ₹75,000/yr, MSMEs/associations ₹25,000/yr ("Subject to Board approval"; S9 N-4; Appendix O) plus invited consumer groups, bar and academia at no fee | Feedback on rules, fees, platform; rules-consultation seat; quarterly briefing on **published** statistics only | **No case powers**; nothing touching a pending case; member list published at `/trust/how-we-stay-neutral`; members cannot nominate EIC members |

### 1.3 Sub-committees — terms of reference

| Code | Sub-committee | Decides | Clocks | Mapping to P03 names |
|---|---|---|---|---|
| `APPT` | **Appointments** — two benches | **Panel Bench:** empanelment, grade, endorsements, probation completion, re-grading (§3.8), assessor roster. **Case Bench:** appointments the Rules reserve to the institution, `manual_exception` approvals, objections to disclosure before confirmation (P03 FR-P03-27), co-arbitrator confirmations in equal-footing matters (NN-03), three-failure offer escalations | Panel Bench ≤ 30 days of interview/assessment; objection ≤ 7 days; manual exception ≤ 2 business days (EA ≤ 1 business day) | "Empanelment Committee" → Panel Bench; "Appointments Committee" → Case Bench |
| `CHAL` | **Challenge** | Challenges under the Equator Rules (A&C Act 1996 s.13(1) agreed procedure; s.13(4)–(5) preserved) and mediation challenges | Reasoned order ≤ 15 days of the last submission | P03 FR-P03-28 "Appointments Committee" for challenges → `CHAL` |
| `SCRU` | **Scrutiny** | Approval of award form for `INT` and for domestic awards > ₹5,00,00,000; policy for Registrar scrutiny below that (S5 C6) | Streamlined 5 working days; standard 10 working days | New |
| `ETHC` | **Ethics & Complaints** | Neutral conduct complaints, interim measures, sanctions (§7), Code interpretation notes | Outcome ≤ 45 days of triage | "Ethics & Complaints Committee" (unchanged) |
| `RULE` | **Rules** | Equator Rules, Code of Conduct (§5), grading policy (§3), allocation policy (§6), EQAP standards (§4), endorsement catalogue; publishes consultation drafts to the Users' Forum (21 days) | Annual review; urgent change with reasons | New |
| `AIOV` | **AI Oversight** | AI Governance Rule (Appendix E §9), model/prompt releases that touch neutral workflows, eval results, AI incidents, neutral AI-use disclosures | Quarterly; incident ≤ 5 business days | New |
| `TRNS` | **Transparency** | Annual Transparency Report and dashboard (§6.7), Claims Register entries for institutional statistics (NN-17), first-time-appointee and diversity targets | Report by 30 June for the prior financial year; dashboard quarterly | New |
| `REVW` | **EIC Review Panel** (ad hoc, 3 EIC members who did not sit below) | Appeals from Panel Bench (grade, empanelment refusal, re-grading), from `ETHC` sanctions, and from EQAP results on procedural grounds | ≤ 30 days | "Appeals Committee" → `REVW` |

### 1.4 "External member" test (machine-checkable)

A member is **external** only if all are true, re-attested annually (`core.committee_members.external_attested_at`):
1. Not a director, key managerial personnel, employee or consultant of ERSPL or any Infrabyx Group company (including Infrabyx Consultancy (OPC) Private Limited and Equator ADR Institute) in the last 3 years.
2. Not a "related party" of ERSPL within Companies Act 2013 s.2(76), and holds < 1% of the shares of any Infrabyx Group company.
3. Received < ₹5,00,000 in aggregate from Infrabyx Group companies in the last 3 financial years other than EIC honoraria.
4. Not an employee, director or retained counsel of an Equator enterprise client, GRM/POSH SaaS client or Users' Forum member.
5. Not a trainer, coach or assessor of the Equator ADR Institute (S6 §6.3 conflict wall).

`committee_composition_valid(committee_id)` returns false if externals ≤ 50% (EIC) or the sub-committee minimum is not met; a decision recorded while false is rejected with `COMMITTEE_COMPOSITION_INVALID`.

### 1.5 Appointment of members

A **Nominations Panel** (EIC Chair + 2 external members + 1 Board nominee without vote) publishes a call, shortlists against a published skills matrix, and recommends; the Board appoints by resolution. Members sign the Charter undertaking, the Code of Conduct (§5, applied *mutatis mutandis*) and a confidentiality undertaking. Honoraria are fixed per sitting by the Board for the Charter term and **never vary with case outcomes or volumes**. Non-resident members: honoraria subject to Income-tax Act 2025 s.393(2) withholding and FEMA current-account rules **[VERIFY — open: S5 Part F Q14]**.

### 1.6 Recusal engine

A member is auto-recused (cannot open papers or vote) when the conflict graph (P03 FR-P03-22) finds any edge between the member and a party, counsel, funder, neutral or witness in the matter, or when the member has declared a conflict. If a **challenged neutral, a party or counsel is an EIC member, Equator director or employee**, the matter goes to a special panel with an external majority including at least one person who is not an EIC member (mirrors SIAC r.28.6 model, S5 B3). Recusals are logged (`core.committee_recusals`) and shown in the decision record.

### 1.7 Decision records

Every EIC/sub-committee decision is a `core.institutional_decisions` row: `decision_no` (`EIC/{CODE}/{YYYY}/{NNNN}`), type (§11.2 enum), matter refs, members present, recusals, votes (for/against/abstain per member), reasons (mandatory, ≥ 200 characters for adverse decisions), documents considered (evidence-ledger IDs), e-signature of the chair (`aal2-pr`, Appendix S §2.10), `publication_class` ∈ {`never`, `anonymised_after_12m`, `statistics_only`}, `published_at`. Challenge decisions default to `anonymised_after_12m` under the Rules' deemed-consent clause **[VERIFY — open: A&C s.42A waiver; 02 §5 Q1]**; neutral-discipline outcomes to `statistics_only` plus anonymised digest (§7.9). Decisions are immutable; corrections create a new decision that `supersedes` the old one.

### 1.8 Naming guardrail

The label validator (P10 FR-P10-01 list) applies to every governance object name, page, document and email: "Court", "Bench" (except the internal term "Panel Bench"/"Case Bench", never shown publicly — public labels: "Panel decisions", "Appointment decisions"), "Judge" (except the honorific "Justice (Retd.)" on a retired judge's own profile, §3.7), "Tribunal" (except "arbitral tribunal"), "Registrar of Court", "decree". Test `NN-17_no_court_naming_governance`.

### 1.9 Charter (outline; full text approved by the Board and published at `/about/governance/charter`)

| Art. | Heading | Key content |
|---|---|---|
| 1 | Purpose | Independent exercise of institutional functions under the Equator Rules |
| 2 | Delegation | Board delegates institutional powers irrevocably for the Charter term (3 years); Board reserves budget and fee approval only |
| 3 | Composition and external majority | §1.2, §1.4 |
| 4 | Appointment, term, removal | §1.5; removal only for misconduct or incapacity by ≥ two-thirds of the EIC, never by the Board alone |
| 5 | Sub-committees | §1.3 terms of reference |
| 6 | Conflicts and recusal | §1.6 |
| 7 | Procedure | Quorum (3 for sub-committees; one-third of EIC with external majority present), circulation resolutions (72-hour window), virtual meetings, e-sign |
| 8 | Reasons and records | §1.7 |
| 9 | Confidentiality | A&C Act s.42A; Equator Rules; watermarking |
| 10 | Transparency | Annual report; publication classes |
| 11 | Funding and honoraria | Fixed; outcome-neutral |
| 12 | Registrar | Appointment by the EIC Chair with Board concurrence; reporting lines §1.2 |
| 13 | Amendment | By the Board only on a two-thirds EIC recommendation; amendments apply prospectively |
| 14 | Immunity and good faith | Rules exclusion of liability; A&C Act s.42B (arbitrators) **[VERIFY — open: S5 Part F Q12 — institution's own protection]** |

Counsel question: whether the Charter's independence makes Equator an "independent institution" for appointment-defensibility purposes after *CORE v ECI-SPIC-SMO-MCML (JV)* (SC, 8 Nov 2024) (02 §5 Q9).

---

## 2. Neutral onboarding journey and public directory (R-31, D2-14)

### 2.1 Design goals

1. **Smooth and short**: one account (Appendix S §1), one application form, autosave, resumable on mobile, pre-fill from DigiLocker/KYC and document AI with human confirmation (NN-01). Target: a complete application in ≤ 25 minutes for an applicant who has their documents.
2. **Transparent**: the applicant sees their provisional grade, the competence route, every step, the owner and the date by which Equator will act (status tracker, §2.4).
3. **Independent of any training purchase**: no step requires a course from the Equator ADR Institute (D2-17).
4. **Free**: no empanelment or listing fee (S9 E-1). The only fee is the EQAP sitting fee for candidates who need an assessment (§4.8), identical for all.

### 2.2 Journey and service levels

| # | Step (public name) | System state(s) (`core.neutral_applications.status`) | Actor | What happens | Equator SLA | Applicant clock |
|---|---|---|---|---|---|---|
| 1 | **Apply** | `draft → submitted` | Applicant | 7-step form (§2.3); grade pre-check runs on submit | Acknowledge ≤ 2 working days with `EQ/NEU/{YYYY}/{NNNNN}` | Draft kept 90 days |
| 2 | **Verify** | `under_verification ⇄ info_requested` | `panel_manager`; referees | Credential checks (P03 FR-P03-03), experience log verification (§3.4), ≥ 2 references (window 7 days), consented background checks (P03 FR-P03-04), sanctions screen for `INT` | ≤ 10 working days from complete documents | Reply to an information request ≤ 14 days (one reminder at day 7); else `paused` |
| 2a | **Training** (only if needed) | `training_required` | Applicant | Grade C (and any mediator) without 40 hours chooses a provider (§9.6) | — | 180 days, then `archived` (resumable within 12 months) |
| 3 | **Assess** | `assessment_route_set → qap_scheduled → qap_passed / qap_failed`; or `fast_track_review`; or `waiver_confirmed` (Grade A) | Applicant; 2 assessors | EQAP sitting (§4) or fast-track (§4.6) or waiver (Grade A) + ethics scenarios (never waived) | Sitting offered ≤ 15 working days after verification; results ≤ 10 working days after sitting | Re-sit after 60 days, max 2 in 24 months |
| 4 | **Committee** | `committee` | `APPT` Panel Bench | Grade, panels, endorsements, probation terms; reasons for any refusal | Decision ≤ 30 days of assessment result | Appeal to `REVW` ≤ 15 days |
| 5 | **Induction** | `approved → inducting` | Neutral | Sign Code (§5); 3-hour orientation; ETR-1, ETR-2 (live mock), ETR-4 (§10); bank (penny-drop, step-up); availability; per-field display consents; sandbox offer | Orientation slots weekly | Complete ≤ 60 days or `approved_lapsed` |
| 6 | **Probation** | `empanelled_probation` | Neutral; `quality_officer` | C: first 5 matters co-mediated/supervised, 100% audited; B: first 3 audited; A: first 2 audited + Tech Concierge on first 3 hearings | Audit ≤ 10 working days after each matter closes | — |
| 7 | **Active** | `active` | — | Allocation-eligible; profile published if consented | — | Term 2 years; recertification opens T−90 |

Additional states: `withdrawn`, `rejected`, `waitlisted` (windowed panels), `paused`, `archived`, `approved_lapsed`. Every transition writes audit and emits `equator.neutrals.application.status_changed.v1`.

**Panel-manager work queue *(v3.1)*.**

| Element | Rule |
|---|---|
| Order | Applications nearest their Equator SLA breach first; then items "Waiting for Equator" over "Waiting for you"; ties by submission time. Order never uses the applicant's training provider, Chambers plan or Users' Forum membership (NN-28) |
| SLA pause reasons | The Equator SLA clock pauses only for a recorded reason: `waiting_applicant`, `waiting_referee`, `waiting_issuing_body` (credential issuer, Bar Council, institute), `waiting_background_check`; each pause shows on the applicant's tracker with the date it began; total pause is reported per application |
| Duplicate check | On submit, the system compares hashed PAN, Bar enrolment or institute membership number and verified email/mobile with existing applications and panel members; a match blocks a second active application (`NEUTRAL_APPLICATION_DUPLICATE`, 409) and links the applicant to the existing record |
| Bulk actions | Send referee reminders, request a missing document, schedule EQAP sittings for a selected group, move to `committee` — each with a preview and per-item result; reminders respect the applicant's notification preferences |
| Delegation | When the assigned `panel_manager` is on approved leave (Appendix Z; trigger `equator.hr.leave.started.v1`, return on `.ended.v1` / `.cancelled.v1`) *(v3.1)*, open items move to the delegate in `access.delegations`, else to the team queue; SLA clocks do not pause for staff leave |
| KPIs | Median days submit → decision (target ≤ 45 calendar days excluding applicant-side pauses); % of steps within Equator SLA (≥ 95%); duplicate applications blocked; appeals upheld on procedural grounds (watch) |

### 2.3 Application form `eqr.form.neutral_application.v3` (extends P03 v2)

Seven steps, each ≤ 12 fields on mobile; progress saved per field. Only the **additions and changes** to v2 are listed; all v2 fields remain.

| Step | field_id | Label | Type | Req. | Options / validation | Help text |
|---|---|---|---|---|---|---|
| 1 About you | `display_name` | Name as you want it shown | text | ✔ | 2–80 chars; lint blocks "Judge", "Hon'ble", "Justice" unless `retired_judge = true` and verified | "Use your professional name." |
| 1 | `honorific_requested` | Honorific | select | — | `none`, `Dr`, `Prof`, `Justice (Retd.)` (only if retired SC/HC judge — verified), `Adv` | "Shown only after we verify it." |
| 2 Roles | `roles[]` | Roles you are applying for | multi | ✔ | P03 list | — |
| 2 | `verticals[]`, `sectors[]` | Areas | multi | ✔ | P03 taxonomy | — |
| 3 Experience | `experience_basis` | Your main professional basis | select | ✔ | `advocate`, `judicial_service`, `retired_sc_hc_judge`, `retired_tribunal_hc_level`, `retired_district_judge`, `ca_cs_cma`, `ibbi_ip`, `senior_management_regulated`, `academic_law`, `civil_servant_group_a`, `mental_health_or_medical` (FAM), `engineer_or_technical` (expert), `other_professional` | "We count years from a date we can verify." |
| 3 | `experience_start_date` | Date your professional experience starts | date | ✔ | ≤ today; source required | "Bar enrolment, membership date or date of joining service." |
| 3 | `experience_start_source` | Proof of that date | select + upload | ✔ | `bar_enrolment_certificate`, `cop`, `institute_membership`, `service_order`, `retirement_order`, `appointment_letter`, `other` | — |
| 3 | `judicial_service[]` | Judicial service | repeater | if basis is judicial | court/tribunal, post, from, to, retirement order upload | — |
| 3 | `adr_matters[]` | ADR matters you have handled | repeater | — | role (`mediator`, `co_mediator`, `conciliator`, `sole_arbitrator`, `presiding`, `co_arbitrator`, `ea`, `expert`, `ic_external`), mechanism, vertical, year, hours, value band, verification source (`court_certificate`, `lsa_certificate`, `institution_letter`, `referee`, `self_declared`) | "Do not enter party names. Outcomes are never used to grade you." |
| 3 | `awards_authored_samples[]` | Redacted awards you wrote (arbitrators) | upload | — | PDF ≤ 20 MB; redaction checklist ticked | — |
| 4 Training and credentials | `trainings[]` | Training completed | repeater | ✔ for mediator role | provider (search `core.training_providers` or "other"), course, hours (≥ 1), mode, completion date, assessed (y/n), certificate no., upload | "Any recognised provider is accepted." |
| 4 | `accreditations[]` | Accreditations and panel memberships | repeater | — | `accreditation_body` enum (§11.4) + number + valid until | — |
| 4 | `declared_code` | Code of conduct you also follow | select | — | `EQUATOR` (always), `IMI`, `CIARB`, `CMC`, `OTHER` | — |
| 5 Practice | languages, cities, modes, time zone, availability, fee band per role (within grade, §3.9) | | | ✔ | P03 | — |
| 6 Integrity | conflicts grid, disciplinary history, pending criminal proceedings (self-declaration), PI cover, referees (3), `institute_relationship` | Relationship with Equator ADR Institute | select | ✔ | `none`, `learner`, `trainer`, `coach`, `assessor`, `employee`, `director_or_shareholder` | "We ask so we can keep training and empanelment separate." |
| 7 Profile and consents | bios, video (non-advocates only until OI-03 closes), per-field display consents, Code e-sign (at induction), DPDP notice, `feedback_digest_optin` | | | | | |

**Grade pre-check** (deterministic, `rules` package, no AI): computes `provisional_grade` and `competence_route` from **verified fields only**; until verification, self-declared years never place an applicant above C (S6 §5.2 note). Output is shown on submit with the explanation text from §3.2.

### 2.4 Status tracker (SCR-P03-04, mobile-first)

Vertical stepper with seven steps; each step shows status chip (`Not started` · `In progress` · `Waiting for you` · `Done` · `Not needed`), owner ("Equator panel team", "You", "Your referees", "Assessors", "Panel decision"), and "We will act by {date}". A single primary action per screen. Push/email/SMS on each change (DLT template `NEU_STATUS_01`); no sensitive content in notifications.

| State | Tracker copy (en) | Hindi (hi) |
|---|---|---|
| submitted | "We have your application. Reference {ref}. Next: we check your documents by {date}." | "आपका आवेदन मिल गया है। संदर्भ {ref}। अगला कदम: हम {date} तक आपके दस्तावेज़ जाँचेंगे।" |
| info_requested | "We need one more thing from you: {item}. Please reply by {date}." | "हमें आपसे एक और जानकारी चाहिए: {item}। कृपया {date} तक जवाब दें।" |
| training_required | "You need 40 hours of mediation training before your assessment. Choose any recognised provider." | "आकलन से पहले 40 घंटे का मध्यस्थता प्रशिक्षण आवश्यक है। कोई भी मान्यता प्राप्त प्रदाता चुनें।" |
| qap_scheduled | "Your assessment is on {date} at {time} (online). You will need a laptop or tablet and a stable connection." | — |
| qap_failed | "You did not pass {component} this time. You can re-sit it after {date}. Your feedback report is ready." | — |
| committee | "Your file is with the Panel decision group. Decision by {date}." | — |
| approved | "Welcome to the Equator panel as {label}. Finish induction by {date} to start receiving matters." | — |
| rejected | "We cannot offer empanelment now. Reasons: {reasons}. You may appeal by {date} or apply again after {date}." | — |
| empanelled_probation | "You are on probation for your first {n} matters. Each is reviewed to help you settle in." | — |

### 2.5 Public directory `/neutrals` (SCR-P03-01) and profile `/neutrals/{slug}` (SCR-P03-02)

**Filters** (facets; all optional): role (mediator, conciliator, arbitrator, expert, POSH external member) · vertical · sector · **grade label** (Associate / Senior / Distinguished) · endorsements (§3.6 public names) · languages (with proficiency ≥ "professional") · city/seat · mode (online, in-person, hybrid) · international (nationality, time zone, rate-card currency) · availability ("can start within 7/14/30 days") · accepting new matters · fee range. **Sort**: seeded-random per session (default) or alphabetical. No other sort exists; any `sort` parameter not in the allow-list returns `400 DIRECTORY_SORT_NOT_ALLOWED`.

**Profile fields (allow-list; anything else fails CI lint `NN-28_directory_allow_list`)**

| Field | Source | Display rule |
|---|---|---|
| Name, honorific | `core.neutrals` | Honorific only if verified |
| Photo, short/long bio, captioned video | neutral | Per-field consent; video and ratings off for advocate-neutrals until OI-03 closes |
| Grade label + grade basis in generic words | `core.neutral_grades` | e.g., "Distinguished Neutral — retired High Court judge"; basis shown only with display consent |
| Roles and panels | memberships | Active only |
| Endorsements | `core.neutral_endorsements` (verified, unexpired) | Public names (§3.6) |
| Verified badges | `core.neutral_accreditations` | Popover: credential type, verification method, verified date, valid until; never the document |
| Languages, cities, modes, time zone | neutral | — |
| Availability indicator | availability engine | "Usually can start within {n} days" |
| Fee range | fee band (§3.9) | Range only; INT currency with indicative INR (P03 FR-P03-09) |
| CPD current, Tech Readiness current | CPD ledger, ETR | Tick only |
| Process ratings | §7.6 aggregation | n ≥ 10 on public profile; process items only |
| Declared code and complaint route | profile | "Bound by the Equator Code of Conduct. To complain, use {link}." |
| Institutional statement | fixed | P03 FR-P03-13 text |

**Never displayed or stored in the directory index** (NN-16, NN-28): settlement or success rates; win/loss; outcome distributions; amounts; awards upheld/set aside; "lender-/borrower-/employer-/insurer-friendly" or equivalent tags; client names or logos; number of matters for any named organisation; any paid, sponsored, "featured", "top", "recommended" or "spotlight" marker; Quality Index; Assessment Score.

**The institutional directory is never paid (D2-14 retained; NN-28; NN-34; CN-13).** Directory and allocation queries must not read any billing, subscription, plan, partner, Users' Forum, marketplace or revenue table. CI test `NO_PAID_PLACEMENT` (extended) fails if a read path exists from `directory.neutral_public_view`, the allocation service, eligibility, grading, the Quality Index or conflict checks to `core.subscriptions`, `core.plans`, `core.memberships`, `growth.*`, `chambers.subscriptions`, `chm.*`, `mkp.sponsorship_*`, `mkp.ad_*`, `mkp.provider_subscriptions` or any `rev` table (Appendix AA §AA.10.6; AB RA-11). A neutral's own Chambers plan (§8), practice page or marketplace sponsorship never changes their Equator profile, order or allocation, and `/neutrals` never links to a practice page or marketplace listing (D3-15). Sponsored listings, where Board and counsel ever allow them, exist only on the separate Private Practice Marketplace with the label "Sponsored — paid placement. Does not affect Equator appointments." (NN-34). *(v3.1)*

**Directory header copy:** "Every neutral on this list has had their qualifications checked by Equator. The order is random each time you visit, so no one can pay to appear first. In matters administered by Equator, neutrals are appointed under our published rules — you cannot hire them for the other side."

---

## 3. Grades A/B/C (D2-12; S6 §5.2) — `grading_policy.v2`

### 3.1 Principle

A grade is an **eligibility tier**: it decides which matters a neutral may be offered (§4.9). It combines an entry gate (status and verified experience), a competence gate (training and assessment) and a technology gate (ETR, §10). It is **never** based on settlement rates, outcomes, who won, enterprise-client preference or the purchase of any course (NN-28). Benchmarks: MCPC Model Rules (15 years' standing; retired judges), Law Society of Singapore (Senior Mediator ≥ 15 years' PQE), IMI (Certified ≥ 200 hours / 20 mediations + QAP), CIArb (Chartered ≥ 10 years + peer interview) (S6 §3.3, §5.1).

### 3.2 Definitions and entry criteria

| | **Grade C — Associate Neutral** | **Grade B — Principal Neutral** (X-26) | **Grade A — Distinguished Neutral** |
|---|---|---|---|
| Who | Entrants, including professionals with up to 15 years' verified experience (assumption A-01) | **> 15 years'** verified professional experience | **(i)** retired judge of the Supreme Court or a High Court, or of a tribunal at High Court-judge level (e.g., NCLAT judicial member, NCDRC President/member at HC-judge level, DRAT Chairperson) — automatic eligibility; **(ii)** retired District & Sessions Judge with ≥ 30 years' combined judicial and legal experience; **(iii)** **> 30 years'** professional experience **and** a demonstrated ADR record (≥ 50 matters as neutral, or designated Senior Advocate, or FCIArb/C.Arb, or IMI Certified Mediator) |
| Minimum age | 25 (P03) | — | — |
| `grade_basis` enum | `entrant` | `professional_15y` | `retired_judge_sc_hc`, `retired_tribunal_hc_level`, `retired_district_judge_30y`, `professional_30y_adr` |
| Years counted from | `experience_start_date` verified (A-02): Bar enrolment, institute membership (ICAI/ICSI/ICMAI), judicial service, Group A service, appointment as Professor/Associate Professor of law, senior management in a regulated sector | same | same |
| Explainer copy | "Associate Neutrals are trained and assessed entrants." | "Principal Neutrals have over 15 years of verified professional experience and assessed mediation or arbitration competence." | "Distinguished Neutrals are retired judges or professionals with over 30 years of experience and a substantial ADR record." |

Common copy (Join page, §2): "Tiers decide which matters a neutral may be offered. They are never based on settlement rates or case outcomes, and no course purchase affects them."

### 3.3 Competence gates

| Gate | Grade C | Grade B | Grade A |
|---|---|---|---|
| **Mediator / conciliator** | **Mandatory** 40 hours' mediation training from any recognised provider (MCPC/High Court/LSA programme, IMI RMTP, HKMAAL, NMAS/AMDRAS, CMC-registered course, or equivalent assessed by the Panel Bench) **+ EQAP** (role-play ≥ 65, impartiality & ethics criterion ≥ 6/12, written test ≥ 60%, ethics scenarios ≥ 10/12 with no critical fail) | 40 hours **and either** (a) EQAP role-play ≥ 70 with the other C thresholds, **or** (b) fast-track (§4.6) on a recognised experienced credential: IMI Certified, SIMI Certified (legacy; SIMI sunsets 31 Mar 2027 → IMI), AMDRAS Advanced/Leading, CMC Registered, HKMAAL General/Family, MCPC trained mediator (40 h + ≥ 20 mediations conducted; any settlement count on the certificate is recorded for the file only and is never a gate or a score — NN-28) → ethics scenarios only | **40 hours mandatory** (MCPC certificate suffices; CN-07); EQAP **waived**; mandatory 3-hour ethics & Equator Rules module; **ETR-2 live mock mandatory** before activation |
| **Arbitrator** | Arbitration fundamentals ≥ 16 hours (e.g., CIArb ACIArb route, IIAC Arbitration Academy, any recognised provider) **+ award-writing exercise ≥ 65** (§4.4) + 12 independence scenarios ≥ 10/12 | FCIArb or MCIArb, **or** ≥ 5 arbitrations as tribunal member with one redacted authored award reviewed, **or** award-writing ≥ 70; + independence scenarios | Retired judges: subject training waived. Others: ≥ 10 arbitrations as tribunal member, or C.Arb. Independence scenarios **always required**; ETR-2 and ETR-3 mandatory |
| **Expert** | Domain qualification + technical file review (P03) | same | same |
| **POSH external member** | Statutory eligibility (POSH Act 2013 s.4(2)(c); POSH Rules 2013 r.4) + `END-POSH` — grade-neutral by statute | same | same |
| **Technology** | ETR-1, ETR-2 (before first online matter), ETR-4 | same | ETR-1, **ETR-2 before activation**, ETR-3 (arbitrators), ETR-4 |

### 3.4 Experience log (QAP criterion 1)

`core.neutral_experience_log` rows (§11.2) are created from the application, imported from Equator case history (`verification_source = equator_record`) or added later. Verification sources rank: `equator_record` = `court_certificate` = `lsa_certificate` > `institution_letter` > `referee` > `self_declared`. Hours and matter counts used for IMI Certified eligibility (≥ 200 hours or ≥ 20 mediations) and B/A thresholds count **only** non-self-declared rows. The field `outcome_recorded` exists for the neutral's own records and IMI Feedback Digest context; it is excluded from every score by CI lint `NN-28_outcome_never_scored`.

### 3.5 Probation, term, CPD

| | Grade C | Grade B | Grade A |
|---|---|---|---|
| Probation | First **5** matters co-mediated with a B/A lead or supervised; 100% file audit | First **3** matters audited | First **2** matters audited; Tech Concierge on the first 3 hearings |
| Probation exit | All audits "satisfactory" or better; 1 remedial matter allowed | same | same |
| Term | 2 years, renewable (P03 FR-P03-36) | 2 years | 2 years; age-neutral; annual fitness-to-practise self-declaration |
| CPD per year (grade base) | **12 h** (≥ 4 ethics/skills) | **10 h** | **6 h** (≥ 2 tech/ODR) |
| Plus | Endorsement CPD (§3.6, per 2-year term), or the vertical-credential CPD of P03 FR-P03-36 where held — **the higher of the two, not both** | same | same |
| ETR-R refresher | Annual; counts 0.5 h tech CPD | same | same |
| Lapse | 90-day grace, then allocation-ineligible (not a down-grade) | same | same |

### 3.6 Endorsement catalogue (`core.endorsement_catalogue`, Ruleset object, versioned)

Endorsements sit on top of a grade and are read by hard filter `HB_SPECIALISM_REQUIRED` (P03 FR-P03-26). Minimum hours may be met through **any** provider; the endorsement needs a verifiable certificate and the stated Equator assessment.

| Code | Public name | Vertical | Minimum (any provider) | Equator assessment | CPD / 2-yr term | Engine trigger |
|---|---|---|---|---|---|---|
| `END-FAM-CORE` | Family mediation | FAM | 40 h core + 24 h family module (Hindu Marriage Act 1955, Special Marriage Act 1954, Muslim personal law, Indian Divorce Act 1869, Parsi Marriage & Divorce Act 1936, BNSS 2023 s.144 maintenance, Guardians and Wards Act 1890) + 2 co-mediated family cases | Role-play with safety-screening station | 12 h (4 DV) | `vertical = FAM` |
| `END-FAM-DA` | Domestic-abuse aware | FAM | END-FAM-CORE + 12 h DV & coercive control (PWDVA 2005) + screening protocol | Scenario test; any safety failure = fail | 6 h | `fam.safety_flag` |
| `END-FAM-CHILD` | Child-inclusive | FAM | END-FAM-CORE + 12 h child development and voice of the child + supervised consultation | Observed | 4 h | `fam.child_issues` |
| `END-PROP` | Property & real estate | COM/FAM | 16 h: TPA 1882; Registration Act 1908 s.17; RERA 2016; partition, HUF; stamp duty | Case-file exercise | 6 h | sector ∈ real_estate, partition, succession |
| `END-WRK` | Workplace & HR | WRK | 16 h: IR Code 2020, Code on Wages 2019, standing orders, power imbalance | Role-play | 8 h | `vertical = WRK` |
| `END-POSH` | POSH external member | WRK | Statutory eligibility + 12 h inquiry procedure (POSH Act ss.9–13; s.10 no monetary settlement) | Boundary scenarios | 8 h | `posh_inquiry` |
| `END-COM` | Commercial & MSME | COM | 16 h: Commercial Courts Act 2015 s.12A; MSMED Act 2006 ss.18–19; contract remedies | Role-play | 8 h | `vertical = COM` |
| `END-IBC` | Insolvency-adjacent | COM | IBBI IP registration or 16 h IBC module | Case exercise | 6 h | sector = ibc |
| `END-CONST` | Construction & infrastructure | COM/INT | 16 h: EPC, FIDIC 2017, delay and quantum, DAAB | Quantum exercise | 6 h | sector = construction |
| `END-FIN` | Banking & lending | FIN | ECFC or 16 h: RBI fair practices, SARFAESI s.13, RB-IOS 2026, NI Act s.138 civil dimension, OTS, vulnerability | Voluntariness/affordability scenarios (must pass) | 16 h/yr | `vertical = FIN` |
| `END-INS` | Insurance | INS | ECIN or 16 h: policy wording, IRDAI (Protection of Policyholders' Interests) Regulations 2024, health data (NN-07), surveyor reports | Role-play + data-handling test | 12 h | `vertical = INS` |
| `END-IP` | Intellectual property | COM/INT | 12 h: licensing; Patents Act 1970 / Copyright Act 1957 basics | Role-play | 6 h | sector = ip |
| `END-INT-MED` | International mediation | INT | IMI Intercultural, **or** 16 h cross-border module (Singapore Convention Art. 4 formalities; UNCITRAL Model Law on International Commercial Mediation 2018) + INT role-play with interpreter or in a second language | Observed | 8 h | INT, mediator seat |
| `END-INT-ARB` | International arbitration | INT | FCIArb, **or** ≥ 3 international arbitrations as tribunal member, **or** CIArb Diploma + award-writing ≥ 70 | Award exercise | 10 h | INT, arbitrator seat |
| `END-INT` | (alias) | INT | Resolves to `END-INT-MED` or `END-INT-ARB` by seat (CN-08) | — | — | V6 references |
| `END-ODR` | Online hearings | All | ETR-1, ETR-2, ETR-4 + online role-play with breakout caucus | Observed online | 4 h | Online matters (default ON) |
| `END-MEDARB` | Med-arb / arb-med | COM/INT | 16 h: role-switch consent, caucus confidentiality, A&C s.30, s.80, Mediation Act 2023 s.17 bar in statutory mode, *Gao Haiyan v Keeneye* (HKCA 2011) | Ethics scenarios | 4 h | mechanism ∈ med_arb, arb_med |
| `END-ADVOCATE` | Mediation advocate (counsel badge, not a neutral grade) | All | 12 h | Role-play as advocate | — | None |
| `CTY-{ISO2}` | Country practice (§9.4) | INT | Country add-on | Quiz ≥ 80% | per add-on | `jurisdiction_eligibility_rules` |

### 3.7 Labels and honorifics

| Internal | Public label (en) | Public label (hi) | Mandatory sub-label |
|---|---|---|---|
| A | Distinguished Neutral | विशिष्ट तटस्थ | "Equator panel tier" |
| B | Principal Neutral (X-26; "Senior" never used) | प्रधान तटस्थ (Hindi label to be confirmed by the language reviewer, NN-23) | "Equator panel tier — not a court designation" *(v3.1)* |
| C | Associate Neutral | सहयोगी तटस्थ | "Equator panel tier" |

"Justice (Retd.)" is shown only for verified retired Supreme Court/High Court judges and only if the judge opts in **[VERIFY — open: OLQ-10, propriety and any post-retirement engagement guidelines]**. The word "Judge" never appears as a title for anyone else.

### 3.8 Re-grading

| Trigger | Direction | Rule | Decided by | Clock |
|---|---|---|---|---|
| Verified experience crosses 15 years + ≥ 10 matters (Equator or verified external) + B competence gate met | C → B | Auto-eligible; Panel Bench confirms on the papers | `APPT` Panel Bench | ≤ 30 days |
| Retirement as SC/HC judge or equivalent; or > 30 years + ADR record | B/C → A | On application | Panel Bench | ≤ 30 days |
| IMI Certified obtained (via EQAP or elsewhere) | Supports B | Counts as competence gate (b) | `panel_manager` verifies | ≤ 10 WD |
| Audit "below satisfactory" on 2 consecutive audits | Remedial plan or down one grade | 6 h targeted CPD + 2 supervised matters; failure → down-grade | `quality_officer` → Panel Bench | Plan ≤ 14 days |
| Upheld complaint (§7) | Sanction ladder; down-grade possible as ancillary | §7.8 | `ETHC` | ≤ 45 days |
| CPD lapse > 90 days | Ineligible (not down-grade) | — | System | — |
| ETR lapse (no online hearing in 12 months + failed ETR-R) | `online_ineligible` flag | Re-take 1 h refresher | System | — |
| "Pressured to settle" ≥ 3 in 12 months | Quality review only | — | `quality_officer` | ≤ 30 days |
| **Never** | — | Settlement rate; who won; amounts recovered; enterprise preference; any training purchase; Chambers plan; Users' Forum membership | — | — |

Every change writes `core.neutral_grade_history` (from, to, reason code, evidence IDs, decision ID, effective date), notifies the neutral with reasons, and opens a 15-day appeal to `REVW`. Reason codes: `EXPERIENCE_THRESHOLD`, `JUDICIAL_RETIREMENT`, `CREDENTIAL_OBTAINED`, `AUDIT_REMEDIAL`, `COMPLAINT_UPHELD`, `VOLUNTARY`, `POLICY_CHANGE`.

**Migration from P03 v1 grades.** Existing neutrals keep their allocation eligibility for 90 days; the Panel Bench re-grades each under `grading_policy.v2` on the papers; nobody is down-graded solely by the policy change without a review and reasons.

### 3.9 Fee bands by grade

A neutral chooses one band per panel within the grade ceiling (Appendix B figures prevail; "Subject to Board approval"): **C → Bands I–II; B → I–III; A → I–IV**. Grade does not alter FIN bulk-programme fees (master X-06). Regulated schedules override (NN-18).

---

## 4. Equator Qualifying Assessment Programme (EQAP) and eligibility by grade

### 4.1 Status and wording

EQAP is **owned by Equator Resolution** (not the Institute) and **designed to the IMI Mediator Assessment Program (QAP) Standards** (https://imimediation.org/docs/imi-standards-program-recognition/imi-standards/mediator-assessment-program-standards-qap/). Until IMI's Independent Standards Commission approves it, the only permitted public wording (Claims Register entry `CLM-EQAP-STATUS`) is: *"Equator's competence assessment is designed to the International Mediation Institute's assessment-programme standards. Equator is not yet an IMI Qualifying Assessment Program."* After approval: *"Equator's assessment is recognised by IMI as a Qualifying Assessment Program. Successful candidates with at least 200 hours or 20 mediations may be submitted to IMI for Certified Mediator status."* Lint blocks "IMI accredited", "IMI certified course", "QAP" (bare) and "MCI-registered" unless the verified claim exists (S6-16).

### 4.2 Components

| Component | Who takes it | Format | Duration | Marks / pass |
|---|---|---|---|---|
| **R — Observed role-play** | Mediator/conciliator candidates (C; B assessment route) | Live online, two-party (or three-party for COM/FAM) simulation from the EQAP bank; candidate mediates, trained role-players act parties; 1 private caucus required | **90 min** + 15 min self-reflection + 15 min debrief (debrief is not scored) | Rubric /100 (§4.3). Pass: C ≥ 65, B route ≥ 70; criterion "Impartiality & ethics" ≥ 6/12 (non-compensable) |
| **W — Written test** | All mediator/conciliator candidates | Closed-book online, proctored | 60 min | 40 MCQ (1 mark) + 2 short essays (10 each) = 60 → % ; pass ≥ 60% |
| **E — Ethics / independence scenarios** | Everyone, every grade (never waived) | 12 scenarios; mediator set or arbitrator set (Fifth/Seventh Schedule mapping) | 30 min | ≥ 10/12 and **zero critical fails** (e.g., accepting a gift from a party; continuing despite an undisclosed relationship; suggesting monetary settlement in POSH) |
| **A — Award-writing exercise** | Arbitrator candidates (C; B route) | Documents-only file (≈ 40 pages); write a reasoned award | 90 min | Rubric /100 (§4.4). Pass: C ≥ 65, B ≥ 70; non-compensable minima |
| **X — Endorsement modules** | Per endorsement (§3.6) | Scenario, case-file or observed exercise | 30–60 min | Per catalogue |

**Written test blueprint** (bank ≥ 120 items, versioned, 3 forms rotated): Equator Rules and Code 20%; Mediation Act 2023 (status map, ss.17, 22–23 when notified; NN-05) and A&C Act Part III 15%; A&C Act 1996 ss.11–13, 18, 29A, 31, 42A, 73–75 15%; UNCITRAL Model Law on International Commercial Mediation 2018 / Singapore Convention 10%; process stages and skills 20%; vulnerability, safeguarding and NN-24 criminal exclusion 10%; data protection and confidentiality (DPDP Act 2023; NN-11) 10%. Essays: one ethics dilemma, one process-design question.

### 4.3 Role-play rubric (/100) with behavioural anchors

Each criterion needs **≥ 3 recorded behavioural observations** per assessor (system-enforced). Level anchors: **Not yet** (< 50% of criterion marks) · **Developing** (50–64%) · **Competent** (65–84%) · **Strong** (≥ 85%).

| Criterion | Marks | "Competent" anchor (examples) |
|---|---|---|
| Opening and process explanation | 12 | Explains role, voluntariness, confidentiality and its limits, caucus rules, in plain language; checks understanding |
| Active listening | 14 | Summarises each party accurately; reflects emotion and content; no interruptions that cut off a party |
| Questioning | 14 | Open questions to uncover interests; avoids leading questions that favour a side |
| Interests and issues | 14 | Converts positions into interests; builds an agreed issues list |
| Process management | 12 | Manages time, power imbalance and escalation; uses caucus purposefully |
| Option generation and reality testing | 12 | Helps parties generate and test options without imposing; evaluative comments only on invitation and even-handed |
| Impartiality & ethics (non-compensable ≥ 6) | 12 | Even-handed; handles confidentiality from caucus correctly; recognises a conflict or safety issue and acts |
| Closure | 10 | Records agreement or next steps accurately; checks informed consent; no pressure |

**Settlement is not evidence of competence**: a role-play that ends without settlement can score "Strong". Assessors score independently; divergence > 10 → third assessor; final = mean of the closest two (P03 FR-P03-06 mechanics retained).

### 4.4 Award-writing rubric (/100)

| Criterion | Marks | Non-compensable minimum |
|---|---|---|
| Framing of issues | 15 | — |
| Findings on evidence with references to the record | 20 | — |
| Reasoning (A&C Act s.31(3)) | 20 | ≥ 10 |
| Jurisdiction and procedural fairness (s.18; notice; opportunity) | 10 | ≥ 5 |
| Interest pre- and post-award (s.31(7)) and computation annex | 10 | — |
| Costs (s.31A) | 5 | — |
| Operative part: clear, enforceable, severable | 15 | ≥ 8 |
| Form: date, seat (s.31(4)), signatures (s.31(1)), stamp-duty note (NN-09), AI non-delegation attestation (Appendix E §9) | 5 | — |

### 4.5 Assessors and integrity

| Rule | Detail |
|---|---|
| Roster | ≥ 6 active assessors; criteria: ≥ 5 years as a neutral and ≥ 50 matters (or IMI Certified / FCIArb), plus assessor accreditation — Academy ECM-S **or any equivalent** (CIArb assessor, IMI QAP assessor, AMDRAS assessor) **or** Equator's free assessor calibration course |
| Pairing | Two assessors per candidate per component; **≥ 1 external** (§1.4 test applied to assessors) |
| Bars | An assessor who trained or coached the candidate (`conflict_edges.relation = trainer_of`), any Institute trainer/coach for its own trainees, a member of the Panel Bench deciding the same file, or anyone with a P03 conflict edge → blocked (`ASSESSOR_CONFLICT`) |
| Declaration | Per-candidate independence declaration before the sitting (e-signed) |
| Calibration | Quarterly benchmark video; assessor > 8 marks from benchmark on any criterion → retrain, blocked from scoring until passed |
| Monitoring | Inter-rater reliability report per assessor (mean absolute divergence, third-assessor rate) to `RULE` quarterly |
| Fees | ₹6,000 per role-play scored, ₹4,000 per award exercise scored ("Subject to Board approval"); TDS under Income-tax Act 2025 s.393(1) Table Sl. 6(iii) |
| Records | Recording hash in evidence ledger; recording kept **1 year then deleted**; scores and observations 3 years; candidate gets a written feedback report ≤ 10 working days |

### 4.6 Fast-track (any provider)

A candidate holding a credential whose issuer supplies an **observed-assessment evidence pack** — published rubric, ≥ 2 assessors with ≥ 1 independent, assessed simulation ≥ 60 minutes, verifiable certificate — may skip component R (and W where the pack covers knowledge). Ethics scenarios (E) are never skipped. Accepted packs are listed in `core.training_providers.recognitions` with `fast_track_eligible = true` after Panel Bench review; the Institute's courses are assessed on exactly the same criteria (CN-03).

### 4.7 Re-sits and appeals

- Re-sit only the failed component after **60 days**; maximum **2 re-sits in 24 months**; then a 12-month wait.
- Appeal on procedural grounds only (irregularity, rubric not followed, assessor conflict, technical failure, new mitigating evidence) — never academic judgement: lodge ≤ 14 days → `REVW` decides ≤ 30 days → outcomes: dismissed, re-sit at no fee, or re-mark by a fresh pair. Appeal fee ₹2,000 refunded if upheld.
- After IMI approval, the IMI complaints route (Professional Conduct Assessment Process, administered by the ISC) is stated on the EQAP page.

### 4.8 Fees (identical for every candidate; "Subject to Board approval"; GST 18%, SAC 999293 **[VERIFY — open: SAC for assessment-only services, tax memo]**)

| Item | Fee ex-GST | Incl. GST |
|---|---|---|
| Mediator sitting (R + W + E) | ₹9,500 | ₹11,210 |
| Arbitrator sitting (A + E) | ₹7,500 | ₹8,850 |
| Combined mediator + arbitrator | ₹15,000 | ₹17,700 |
| Re-sit (one component) | ₹4,500 | ₹5,310 |
| Grade A ethics module + ETR | ₹0 | ₹0 |
| Fast-track review | ₹0 | ₹0 |
| Concession | 50% for full-time students, LSA panel mediators and applicants with a disability certificate; full waiver at the Panel Bench's discretion for hardship | — |

Total price including GST is shown before payment (NN-29); refunds: 100% if cancelled ≥ 7 days before the sitting; one free reschedule.

### 4.9 Case-allocation eligibility by grade (hard filter `grade_eligible()`, error `HB_GRADE_INELIGIBLE`)

Defaults; per-panel overrides only through maker–checker with `RULE` approval; endorsements always additionally required where listed.

| Seat / matter | Grade C | Grade B | Grade A |
|---|---|---|---|
| FIN conciliation/mediation ≤ ₹10,00,000 | ✓ after probation (+`END-FIN`) | ✓ | ✓ |
| FIN arbitration, documents-only, ≤ ₹5,00,000 (bulk) | ✓ only on `ARB-FIN` with award-writing pass **[VERIFY — open: OLQ-3, s.12(3)(b) risk]** | ✓ | ✓ |
| FIN arbitration > ₹5,00,000 to ₹1,00,00,000 | ✗ | ✓ | ✓ |
| Sole/presiding arbitrator > ₹1,00,00,000 (COM, FIN) | ✗ | ✓ up to ₹10,00,00,000 | ✓ any value |
| Co-arbitrator (three-member) | ✗ | ✓ | ✓ |
| Emergency arbitrator (`EA-COM`), appellate tier (`APP-ARB`) | ✗ | ✗ | ✓ |
| COM mediation ≤ ₹1,00,00,000 | ✓ after probation (+`END-COM`) | ✓ | ✓ |
| COM mediation > ₹1,00,00,000; IBC-adjacent | Co-mediator only | ✓ (+`END-IBC` for IBC) | ✓ |
| FAM mediation, no safety flag | Co-mediator with B/A lead | ✓ (+`END-FAM-CORE`) | ✓ (+`END-FAM-CORE`) |
| FAM with safety flag / child issues | ✗ | ✓ with `END-FAM-DA` / `END-FAM-CHILD` | ✓ same (never waived) |
| WRK mediation/conciliation | ✓ (+`END-WRK`) | ✓ | ✓ |
| POSH external member | Grade-neutral: statutory eligibility + `END-POSH` | ✓ | ✓ |
| INS retail (policyholder) mediation/conciliation | ✗ | ✓ (+`END-INS`) | ✓ (+`END-INS`) |
| INT mediation | Co-mediator only | ✓ (+`END-INT-MED`) | ✓ (+`END-INT-MED`) |
| INT arbitration sole/presiding | ✗ | ✓ up to USD 3,000,000 (+`END-INT-ARB`) | ✓ any (+`END-INT-ARB`) |
| Med-arb / arb-med | ✗ | ✓ (+`END-MEDARB`) | ✓ (+`END-MEDARB`) |
| Expert determination | Domain-qualified; grade-neutral | ✓ | ✓ |

The soft score no longer rewards a higher grade on small matters ("value band ↔ grade 20" in P03 FR-P03-21 is replaced, §6.4), so Grade A capacity is preserved for complex matters and C/B pipelines grow.

### 4.10 IMI submission path

| Step | Action | Owner | Evidence |
|---|---|---|---|
| 1 | Build the 10-point readiness pack (S6 §6.2): experience-verification SOP; test bank ≥ 120 items; published competency framework, scoring and thresholds; public page `/neutrals/assessment` with fees, frequency, mode; ≥ 6 assessors with ≥ 1 external per sitting; calibration and monitoring; non-discrimination statement (open to graduates of any trainer); re-sit policy; DPDP/GDPR privacy notice; logo-use limit | `RULE`; Registrar | Pack v1 approved by `RULE` |
| 2 | Run ≥ 2 pilot sittings with external assessors | Registrar | Pilot report |
| 3 | Apply on the IMI portal for QAP (and an ODR-QAP variant) | Registrar | Application ID; fees per IMI **[VERIFY — open (vendor): fee not published; applications only via IMI portal; separate ODR-QAP standard exists]** |
| 4 | On approval: switch Claims Register wording (§4.1); IMI QAP logo only on `/neutrals/assessment` | `TRNS` | Approval letter |
| 5 | Submit candidates with ≥ 200 hours or ≥ 20 mediations (verified log rows) to IMI with their consent; the neutral pays IMI's listing (€165/yr Certified) directly | Registrar; neutral | Submission record |
| 6 | Biennial IMI audit booked in the compliance tracker | `RULE` | Audit report |
| 7 | Offer an **IMI Feedback Digest export** (§7.10) | P03 | — |

---

## 5. Equator Code of Conduct for Neutrals (publishable text)

> Publish at `/rules/code-of-conduct` as `core.procedure_rules` kind `code_of_conduct`, version `ECC-2026.1`, approved by the Rules Sub-Committee, effective from the date shown; cases pin the version in force at the neutral's appointment (NN-21). Hindi and regional versions need legal review before activation (NN-23). Sources consolidated: A&C Act 1996 s.12 and Fifth/Sixth/Seventh Schedules; Mediation Act 2023 (provisions in force and, in statutory mode, as notified); IBA Guidelines on Conflicts of Interest in International Arbitration 2024; SIAC Rules 2025 r.20 and SIMC Code of Ethics; ICC Rules 2026 Art. 12; CIArb Guideline on the Use of AI in Arbitration 2025; IMI Code of Professional Conduct (cross-map, §5.15). Bracketed numbers are clause numbers.

**EQUATOR CODE OF CONDUCT FOR NEUTRALS (ECC-2026.1)**

**Part 1 — Application**

1.1 This Code binds every mediator, conciliator, arbitrator, expert and POSH external member who accepts an appointment in a matter administered by Equator Resolution Service Private Limited ("Equator"), and every member of the Equator Institutional Committee when acting as such. Private ADR Chambers tenants must adopt this Code or a code no less protective (§8.6).
1.2 This Code supplements the law. Where the law imposes a stricter duty, the law applies. Nothing in this Code makes Equator a court or gives a neutral any power the law or the parties have not given.
1.3 "Matter" means any proceeding administered by Equator; "party" includes a party's representative where the context allows.

**Part 2 — Independence and impartiality**

2.1 You must be, and remain, independent of the parties and their representatives and impartial in the matter.
2.2 You must not accept an appointment if any circumstance in the Seventh Schedule to the Arbitration and Conciliation Act 1996 applies to you, unless every party has, after the dispute arose, expressly waived it in writing (s.12(5)). For mediation and conciliation, Equator applies the same standard as policy.
2.3 You must not show favour to any party, including a party that brings many matters to Equator. You must not seek or accept any benefit, future work or referral from a party or representative in a matter you are handling.
2.4 You must not have any discussion with a party about a possible future appointment, employment or engagement while the matter is pending and for **12 months** after it closes, if that party is a repeat user of Equator (lender, insurer, employer, platform).

**Part 3 — Disclosure**

3.1 Before accepting, you must disclose in writing every circumstance likely to give rise to justifiable doubts about your independence or impartiality, or your ability to devote enough time to complete the matter (for arbitrators, in the form in the Sixth Schedule, answering every item in the Fifth Schedule).
3.2 If in doubt, disclose. A disclosure is not an admission of a conflict.
3.3 The duty continues to the end of the matter. You must disclose promptly when a new party, representative, funder or witness joins, or when your circumstances change.
3.4 You must disclose any relationship with Equator, its group companies (including Equator ADR Institute) and Equator's office-holders that a reasonable party would want to know, including teaching or assessing for the Institute.
3.5 You must disclose if you lack any qualification the parties' agreement requires.

**Part 4 — Confidentiality**

4.1 You must keep confidential everything about the matter, including its existence where the parties so agree, except where disclosure is required by law, needed to implement or enforce an award (A&C Act s.42A), or permitted by all parties.
4.2 In mediation and conciliation you must not disclose what a party tells you in private session without that party's permission. You must not record a mediation session or allow it to be recorded (NN-11).
4.3 You must use Equator's platform for case communication and storage. You must not keep case documents on personal devices or personal cloud storage, or forward them to personal email.
4.4 After the matter closes you must return or delete case material as Equator directs, except what the law requires you to keep.
4.5 You may disclose confidential information to the extent necessary to prevent death or imminent serious bodily harm to an identifiable person. Unless the law requires immediate disclosure, you must first make a good-faith effort to have the party concerned remedy the situation, and you must tell Equator. *(v2.1, from the Equa Code §5.1.1(v))*

**Part 5 — Competence**

5.1 You must accept only matters you are competent and qualified to handle, including any endorsement Equator requires.
5.2 You must keep your knowledge and skills current and complete the continuing professional development and technology refreshers Equator requires.
5.3 You must tell Equator promptly if your health, workload or circumstances may affect your ability to act.
5.4 Before the first session you must tell the parties your relevant background and experience; the platform shows your verified profile for this purpose. *(v2.1, from the Equa Code §1.3.1)*

**Part 6 — Diligence and conduct of proceedings**

6.1 You must conduct the matter fairly, efficiently and without unnecessary delay or expense, giving each party a full and equal opportunity to present its case (A&C Act s.18) and meeting every time limit, including s.29A.
6.2 You must not communicate with one party about the matter in the absence of the other, except in a mediation or conciliation caucus or as the rules permit, and you must then follow the caucus rules.
6.3 In mediation you must respect each party's right to decide. You must not pressure any party to settle. You may give a view on the merits only if all parties ask for it and you do so even-handedly.
6.4 You must check that each party understands the process and any settlement, and must pause or end the process if a party appears unable to participate freely or safely (including where a safety concern arises in a family or workplace matter).
6.5 You must not mediate or adjudicate any criminal offence. Where a matter has a criminal dimension, you deal only with the civil or money dispute, and the court alone decides compounding or withdrawal (NN-24).
6.6 You must give reasons for an award unless the parties have agreed otherwise or it is an award on agreed terms (s.31(3)).
6.7 In mediation and conciliation you must withdraw if the process appears headed to an outcome that is illegal or unconscionable — for example, one produced by undue pressure, duress or exploitation of a power imbalance. *(v2.1, from the Equa Code §4.3.2)*

**Part 7 — Fees and money**

7.1 Your fees are those fixed under Equator's published fee schedule for the matter. You must not ask for, receive or agree any other fee, gift, expense or benefit from a party, directly or indirectly.
7.2 You must not collect fees directly from parties in an Equator-administered matter; all payments go through Equator.
7.3 Your fee never depends on whether the matter settles, on its outcome, or on which party prevails.
7.4 You must not handle settlement money between parties.
7.5 If you withdraw or are removed, fees paid for the period after your withdrawal are refunded to the parties through Equator. *(v2.1, from the Equa Code §4.5.1)*

**Part 8 — Use of artificial intelligence and technology**

8.1 You may use only the AI tools Equator provides or approves for the matter, under the Equator AI Governance Rule (Appendix E §9).
8.2 You must not delegate any decision, finding, evaluation or reasoning to an AI tool. You remain responsible for every word you adopt.
8.3 You must verify every fact, citation and quotation in any AI-assisted draft against the record or the source before adopting it.
8.4 You must not upload case material to any AI tool or service that Equator has not approved.
8.5 Where the AI Governance Rule requires it, you must tell the parties how AI was used, and you must sign the non-delegation attestation in every award.

**Part 9 — Conflicts during and after the matter**

9.1 You must not act, during or after the matter, as representative, counsel, adviser or witness for any party in any proceeding about the same dispute (and, in statutory-mode mediation, as arbitrator in it — Mediation Act 2023 s.17).
9.2 A mediator or conciliator may act as arbitrator in the same dispute only where the law allows it and all parties have given fresh, informed, written consent after the mediation or conciliation ends, with a renewed disclosure.
9.3 You must not accept a new appointment from, or engagement by, a party to a matter you decided for **2 years** after it closes if the work would be adverse to another party to that matter.
9.4 For **12 months** after a matter ends you must not act as adviser to, or take employment with, any party in the same or a substantially related matter, unless all parties consent in writing after full disclosure. Serving as a neutral in another matter involving the same party is not advisory work. *(v2.1, from the Equa Code §3.7)*

**Part 10 — Social media and public statements**

10.1 You must not comment publicly, including on social media, on any pending matter, or on a closed matter in a way that could identify the parties.
10.2 You must not describe your outcomes, settlement rates or "wins", or claim to favour any category of party.
10.3 You must not use Equator's name, logo or your Equator tier in advertising except in the factual form Equator provides ("Empanelled with Equator Resolution — {tier label}"). Advocate-neutrals must also follow the Bar Council of India Rules on advertising.
10.4 You must not connect with, follow or message a party on social media while their matter is pending.

**Part 11 — Gifts and hospitality**

11.1 You must not accept any gift, hospitality or favour from a party or representative in a pending matter, or within 12 months after it closes.
11.2 From a repeat user of Equator you must not accept gifts or hospitality worth more than ₹2,000 in aggregate in a year, and you must declare any you accept to Equator.
11.3 Sponsored training or travel paid by a repeat user of Equator is prohibited.

**Part 12 — After the matter**

12.1 Your duties of confidentiality continue after the matter ends.
12.2 You must respond to Equator's requests about the matter, including for scrutiny, correction, interpretation or a challenge, within the time Equator sets.
12.3 You must co-operate with any court proceedings about the matter only as the law requires, and must inform Equator.

**Part 13 — Relationship with Equator**

13.1 You must declare annually any interest in, or engagement with, Equator, its group companies or office-holders.
13.2 You must not seek to influence your allocation, grade or any Institutional Committee decision except through the published procedures.
13.3 Buying a course, membership or subscription from Equator or any group company does not affect your tier or allocation, and you must not suggest that it does.

**Part 14 — Breach**

14.1 A breach of this Code may lead to advice, a warning, required training, suspension or removal from the panel, decided by the Ethics & Complaints Sub-Committee with reasons and a right of appeal (Appendix N §7).
14.2 Where you have agreed that Equator may do so, or where the law requires it, Equator may inform a professional body of a sanction.

**Part 15 — Acceptance**

15.1 By accepting empanelment and each appointment you agree to this Code as amended from time to time; amendments apply to appointments made after they take effect.

### 5.15 Cross-map (for neutrals declaring another code)

| ECC Part | IMI Code of Professional Conduct | A&C Act 1996 | Mediation Act 2023 |
|---|---|---|---|
| 2–3 | Impartiality; conflicts **[VERIFY — open: IMI Code clause numbers, OLQ-12]** | s.12(1)–(5), Fifth–Seventh Schedules | Conflict and disclosure provisions (statutory mode) |
| 4 | Confidentiality | s.42A; s.75 | ss.22–23 (when notified) |
| 6 | Mediation process; self-determination | s.18; s.29A | — |
| 7 | Fees | Fourth Schedule reference; s.11(14) | — |
| 9 | Post-mediation roles | s.80 | s.17 |

---

## 6. Allocation and performance (D2-13; NN-03, NN-16, NN-28)

### 6.1 Pipeline (published at `/rules/allocation-policy`; pinned per case)

```
Pool (active members of required panels)
 → Stage 1  Hard eligibility filters        (exclusions counted; IDs sealed)
 → Stage 2  Concentration caps              (hard; never relaxed)
 → Stage 3  Rotation window                 (least-recently-appointed first; first-time appointee guarantee)
 → Stage 4  Capped Quality Index weighting  (process metrics only; weight bounded)
 → Stage 5  Seeded draw (commit–reveal)     (P03 FR-P03-21 steps 1, 5, 6)
 → Offer → disclosure → objection window → confirmation (hard blocks) → IEP
```

Nothing from billing, partner status, Users' Forum, Chambers plans, AI or any outcome enters any stage (`NN-16_priority_never_in_allocation`, `NO_PAID_PLACEMENT`, `NN-01_ai_never_selects_neutral`).

### 6.2 Stage 1 — hard filters (in order; each records an exclusion count)

1. Good standing: active term, credentials and PI cover valid, CPD within grace, not suspended (`HB_NOT_IN_GOOD_STANDING`).
2. `grade_eligible(seat, vertical, value_band, flags)` per §4.9 (`HB_GRADE_INELIGIBLE`).
3. Required endorsements (`HB_SPECIALISM_REQUIRED`); sealed safety details never read (NN-07).
4. `jurisdiction_eligibility_rules` (§9.4) — e.g., Saudi seat: sole/presiding arbitrator must hold a law or Shari'a degree (Saudi Arbitration Law 2012, Art. 14) (`HB_JURISDICTION_INELIGIBLE`).
5. Conflict graph `hard` class (P03 FR-P03-22); `trainer_of` is informational for parties.
6. Capacity (QI-adjusted ceiling, §6.5) and availability in the first-session window.
7. Shared working language with every party (else interpreter flag); city/seat for in-person.
8. Role segregation and role-switch rules (master §5.3).
9. INT nationality (NN-19).
10. `online_ineligible` flag for online matters.
11. Upheld objections/strikes in this case.

### 6.3 Stage 2 — concentration caps

| Cap | Default | Applies to | Guardrail |
|---|---|---|---|
| Relative | ≤ 40% of a neutral's appointments in a rolling 24 months involve one counterparty group (after ≥ 10 appointments; absolute 3 below that) — P03 FR-P03-23 | All | ≤ 50%; window ≥ 12 months |
| Absolute (LR-ARB-007) | 2 appointments per lender/insurer group per neutral per 36 months | Non-bulk FIN/COM/INS seats (CN-06) | Configurable; `legal_reviewer` sign-off |
| Volume fairness | No neutral receives more than **2.0 ×** the panel-queue median of new appointments in a rolling quarter while another eligible neutral in the queue has capacity | All institutional methods | Range 1.5–3.0 |

A projected breach excludes the neutral; an empty set returns `ALLOCATION_POOL_EXHAUSTED`; caps are never relaxed to fill a seat. Fifth Schedule item 22 counts are always disclosed.

### 6.4 Stages 3–5 — rotation, capped Quality Index, draw

**Rotation window.** Sort the post-cap set `E` by `last_appointed_at` in the panel queue (never-appointed first), then by the persisted queue pointer. Window `W` = first `w` candidates (`allocation.rotation_window`, default **5**). **First-time appointee guarantee:** if the panel's first-time-appointee share for the current quarter is below target (`allocation.first_time_target_pct`, default **15%**, HKIAC benchmark 20.5%, S5 B1) and `W` contains no eligible neutral without a prior Equator appointment, the earliest such neutral in `E` is added to `W`.

**Selection weight** for each `i ∈ W`:

```
w_i = clamp( 1 + β · (QI_i − QI_med) / 50 ,  1 − β ,  1 + β )
```

- `QI_i` = neutral's Quality Index (0–100, §6.5); `QI_med` = median QI of the panel queue.
- `β` (`allocation.qi_beta`) = **0.30** for `rules_weighted`; **0.00** for `rotation` (FIN bulk documents-only — pure rotation maximises defensibility; "best performers" benefit there through the capacity ceiling, §6.5). Guardrail: `β ≤ 0.40`. With β = 0.30 the highest-weighted candidate is at most 1.86 × as likely to be drawn as the lowest in the window.
- Sector fit, language depth, city/seat and earliest availability are applied as **tie-break ordering inside the window** for `rules_weighted` (P03 FR-P03-21 soft score, with "value band ↔ grade" removed).
- **Draw**: probability `p_i = w_i / Σ w`; random number from the committed seed (SHA-256 commitment stored before evaluation; seed revealed after selection; reproduction script in the IEP).
- `rotation` method: select the first candidate in `W` (QI does not apply).

**Worked example (golden vector GV-N-01).** Window of 4 with QI 82, 64, 58, 46; `QI_med = 61`; β = 0.30 → weights 1.126, 1.018, 0.982, 0.910; Σ = 4.036; probabilities 27.9%, 25.2%, 24.3%, 22.5%. A seed whose first 8 bytes map to u = 0.40 (u × Σ = 1.614) selects candidate 2.

### 6.5 Quality Index (QI) — process metrics only

Computed quarterly (`QualityIndexJob`) over the last 24 months, per neutral per role family (mediation/conciliation; arbitration), stored in `core.quality_index_snapshots` with inputs and formula version.

| Component | Weight | Measure (0–100) | Source |
|---|---|---|---|
| T — Timeliness | 30 | % of owned milestones met on time (first session within target, orders, MSA/award drafts vs Equator target, s.29A milestones), minus 5 per neutral-caused adjournment (floor 0) | `clocks`, `proceedings` |
| A — Audit & scrutiny | 25 | Mean file-audit score; award form scrutiny: −5 per minor point, −15 per major point (P04/S5 C6) | `quality`, `outcomes` |
| F — Conduct feedback | 20 | Mean of moderated **conduct items** only (§7.2 items N1–N8), mapped `(mean − 1)/3 × 100`; requires n ≥ 5 else panel median | `core.neutral_reviews` |
| R — Responsiveness | 10 | % offers answered within SLA; % disclosures signed on time | `appointments` |
| K — Complaint record | 10 | 100 − 40 per upheld S2 − 20 per upheld S3 in 24 months (floor 0) | `ETHC` decisions |
| C — CPD & ETR currency | 5 | 100 current; 50 in grace | CPD ledger |

`QI_raw = Σ weight × component / 100`. **Shrinkage** for low volume: `QI = (n·QI_raw + 5·QI_med) / (n + 5)` where `n` = closed matters in the window — new neutrals start at the panel median, never at a penalty.

**Excluded (CI allow-list lint `NN-28_qi_inputs_allow_list`)**: settlement or success rate; who won; amounts awarded or recovered; awards set aside or upheld (CN-12); challenge outcomes; enterprise-client ratings above 20% weight; the "pressured to settle" item (review trigger only); any billing, plan, partner, Users' Forum or training-purchase data; Assessment Score older than 24 months.

**Capacity ceiling by QI** (the second lever for "more cases to the best performers"): QI ≥ 75 → capacity +20%; 40–74 → standard (P03 FR-P03-10); < 40 → capacity −25% and a quality review. Changes apply from the next quarter; the neutral sees their QI, components and the effect on capacity in the scorecard (SCR-P03-19). QI is never public.

### 6.6 Published allocation policy (copy for `/rules/allocation-policy`, summary block)

"**How Equator chooses a neutral.** 1. We list every neutral on the right panel who is eligible: right tier for the matter, right specialist training, no conflict, the language you need, and time available. 2. We remove anyone who already has too many matters involving the same organisation. 3. We take the neutrals who have waited longest since their last Equator appointment, and we make sure new panel members get a fair share. 4. Among them, neutrals with a better record of running matters on time, careful work and courteous conduct have a slightly better chance — never more than a fixed limit. We never look at who won, how much was paid or whether a case settled. 5. A computer makes the final draw using a code we lock in before we start, so anyone can check it later. Businesses that use Equator cannot choose, rank or veto neutrals."

### 6.7 Transparency dashboard and annual Transparency Report (S5 C3)

Generated by `reporting` from immutable event data with a reproducible query pack; cells with **n < 10 suppressed** (master X-28); POSH and family-safety data excluded (NN-07); approved by `TRNS`; every published number is a Claims Register entry (NN-17). Dashboard `/trust/statistics` refreshes quarterly; report published by 30 June for the prior financial year.

| # | Section | Measures |
|---|---|---|
| 1 | Caseload | By vertical, mechanism, procedure tier, seat, language, state/country |
| 2 | Sums in dispute | Total, median by vertical and currency |
| 3 | Procedure use | EA applications/granted, expedited, early determination, AMA referrals |
| 4 | Appointments | By grade; by method (institutional / list / joint / equal-footing nomination); **first-time appointee %**; gender split by method; language and regional diversity; nationality (INT); Gini of appointments per neutral |
| 5 | Challenges | Filed, decided, upheld, withdrawn; median decision days |
| 6 | Awards and scrutiny | Issued; scrutiny median days; % with substantive points; % within Equator target; s.29A extensions sought |
| 7 | Service levels | Median time to acknowledge filing, first notice, constitution, EA decision |
| 8 | Costs and duration | Median by tier |
| 9 | Complaints | Neutral-conduct complaints by category, severity and outcome (anonymised); service complaints; data-protection incidents |
| 10 | Panel | Size by grade × vertical × endorsement × language; Grade C→B progression; EQAP sittings, pass rates by component, assessor-independence compliance %; **share of panel trained by each provider** (to evidence no Institute tie-in) |
| 11 | AI | Matters using AI features; human-override rate; AI incidents |
| 12 | Institution set-asides | Equator's own count of awards set aside (D12) |

---

## 7. Feedback, ratings and complaints (R-32)

### 7.1 Principles

Feedback improves process; it never measures outcomes. Only verified participants of closed matters rate; no incentives for feedback; moderation applies regardless of sentiment; the neutral has a right of reply; nothing reaches a public surface below the threshold (n ≥ 5 for internal aggregates; n ≥ 10 on the public profile and in every public statistic, CN-05, master X-28). Practice reference: IS 19000:2022 *Online Consumer Reviews — Principles and Requirements for their Collection, Moderation and Publication* (BIS, voluntary) (S9 E-4).

### 7.2 Post-case feedback forms (sent 48 hours after closure; 30-day window; one per person per matter; tokenised link + OTP)

**F1 `eqr.form.feedback_party.v2`** (party and party_org_user; plain language, class-8 reading level; en/hi + regional; mobile-first, ≤ 3 minutes)

| field_id | Label | Type | Req. | Options |
|---|---|---|---|---|
| N1 | The neutral explained the process clearly | scale 1–4 | ✔ | Strongly disagree · Disagree · Agree · Strongly agree · Not applicable |
| N2 | The neutral listened to me | scale 1–4 | ✔ | same |
| N3 | The neutral treated both sides equally | scale 1–4 | ✔ | same |
| N4 | The neutral was polite and respectful | scale 1–4 | ✔ | same |
| N5 | The neutral kept to time and started sessions on time | scale 1–4 | ✔ | same |
| N6 | I understood what was decided or agreed, and what happens next | scale 1–4 | ✔ | same |
| N7 | The neutral gave opinions only when we asked (mediation/conciliation only) | scale 1–4 | — | same |
| N8 | The neutral kept what I said in private session confidential (mediation only) | scale 1–4 | — | same |
| P1 | Did you feel pressured to settle? | select | ✔ | No · A little · Yes · Prefer not to say |
| M1–M3 | Case manager: reachable; explained next steps; responded on time | scale 1–4 | — | same |
| X1 | Equator platform was easy to use | scale 1–5 | — | 1–5 |
| T1 | Anything else? (do not include names, amounts or case details) | textarea ≤ 1,000 | — | PII auto-redaction preview |
| C1 | Share my comments with the neutral (anonymised) | checkbox | — | default unticked |
| C2 | My scores may be counted in the neutral's public rating | checkbox | — | default unticked |

There is no item about the result, amount or who won; a form schema lint rejects such items (`NN-28_feedback_no_outcome_items`).

**F2 `eqr.form.feedback_counsel.v2`** — items N1–N8 plus: CO1 "Procedural directions were clear and even-handed"; CO2 "Disclosures were complete and timely"; CO3 "The award/settlement record was clear and accurately reflected the record" (scale 1–4); T1, C1, C2.

**F3 `eqr.form.feedback_case_manager.v1`** (internal; not public; not counted in F) — CM1 responded to Registry requests on time; CM2 disclosures and orders filed on time; CM3 hearing conduct and platform use; CM4 escalations needed (count); free text. Feeds component T/R corroboration and audit sampling.

**F4 `eqr.form.feedback_co_neutral.v1`** (co-mediator / co-arbitrator / presiding; internal) — CN1 shared preparation; CN2 collegial deliberation; CN3 drafting contribution on time; CN4 respect for confidentiality; free text. Used for probation reviews and audits; never public.

### 7.3 Moderation (`quality_officer` queue; target ≤ 72 hours)

| Check | Action |
|---|---|
| PII, party names, amounts, case facts in free text | Redact; if unredactable, withhold text (scores kept) |
| Abuse, threats, discrimination | Withhold text; safety escalation if a threat |
| Allegation of misconduct | Withhold from neutral view; open a complaint intake on the rater's consent (§7.7) |
| Rater from a repeat-player organisation | Flag `is_repeat_player_org`; capped at 20% of any aggregate weight; enterprise-side ratings in bulk matters excluded |
| Suspected coordinated or retaliatory rating | Hold; Quality Officer review |

Moderation decisions are logged with reason codes; moderation policy published at `/trust/feedback-policy`.

### 7.4 Right of reply

The neutral sees aggregated scores (n ≥ 5) and moderated comments shared under C1. The neutral may (a) file a reply to any comment (≤ 1,000 characters) that is stored with it and accompanies it into any quality review or complaint; (b) request re-moderation once per comment; (c) attach a short public statement to their profile rating panel (≤ 300 characters, linted). Replies are never sent to the rater unless the rater opted in.

### 7.5 "Pressured to settle"

Any "Yes" → quality review ticket; ≥ 3 "Yes" in 12 months → structured review with file audit (S6 §5.4); never automatic sanction or grade change.

### 7.6 Aggregation

| Surface | Minimum n | Content |
|---|---|---|
| Neutral's scorecard | 5 | Item means, distribution, trend; comments shared under C1 |
| Committees, Quality Officer | 5 (individual responses visible to Quality Officer under audit log) | Full |
| Quality Index F component | 5 (else panel median) | Conduct items N1–N8 |
| Public profile | **10** published ratings with C2 consent | Overall process score (one decimal) + per-item bars for N1–N5; date range; "Ratings come only from people who took part in closed matters." No stars schema (`aggregateRating` never emitted) |
| Transparency Report and `/trust/statistics` | 10 per cell (master X-28) | Institution-level only |

### 7.7 Complaint intake (public form `/complaints/neutral` — `eqr.form.neutral_complaint.v2`; also via portal, email to the published address, or phone-assisted)

| field_id | Label | Type | Req. | Options / validation |
|---|---|---|---|---|
| CP1 | Who are you? | select | ✔ | party · representative/counsel · witness · co-neutral · Equator staff · member of the public |
| CP2 | Case reference (if any) | text | — | `EQ/...` pattern; verified against identity for party/counsel |
| CP3 | Neutral's name | search | ✔ | Directory lookup or free text |
| CP4 | What is the complaint about? | multi | ✔ | conflict of interest or bias · conduct or language · delay · confidentiality · fees or side payment · pressure to settle · competence · AI misuse · social media · gifts/hospitality · other |
| CP5 | What happened? | textarea | ✔ | ≥ 50 chars; ≤ 5,000 |
| CP6 | Evidence | upload | — | ≤ 10 files, 20 MB each |
| CP7 | Is this urgent (hearing within 7 days, safety risk)? | yes/no | ✔ | Yes → immediate triage |
| CP8 | What outcome are you seeking? | select | — | explanation · apology · review of the neutral's conduct · other |
| CP9 | Contact details | text | ✔ unless anonymous | Anonymous complaints accepted but may limit investigation |
| CP10 | Consent to share the complaint with the neutral | checkbox | ✔ to proceed with investigation | DPDP notice (purpose `neutral_complaint_handling`) |

Copy at the top: "This form is for complaints about how a neutral behaved. It is not an appeal against a decision or award. To challenge an arbitrator's independence in a pending case, use **Challenge** in your case (the deadline is 15 days from when you learn of the reason)."

### 7.8 Triage, investigation, hearing, sanctions

| Severity | Definition (examples) | Interim measure | Clocks |
|---|---|---|---|
| **S1** | Undisclosed Seventh Schedule relationship; side payment; sexual harassment; breach of sealed data; threat | Immediate suspension of allocation and active matters reviewed; parties notified where it affects their case | Triage ≤ 1 working day |
| **S2** | Bias or pressure to settle with evidence; serious confidentiality breach; repeated delay causing clock breach; AI misuse of case data | Pause new offers | Triage ≤ 3 working days |
| **S3** | Discourtesy; isolated delay; minor procedural lapse | None | Triage ≤ 5 working days |
| **S0** | Not about a neutral (service, fees, platform) | Route to service complaints | ≤ 2 working days |

**Process.** Acknowledge ≤ 2 working days → triage by `quality_officer` → investigation by an investigating officer independent of the case team (evidence: case record, recordings where lawful, audit log, statements) ≤ 30 days → neutral's written response ≤ 14 days → `ETHC` hearing (online; neutral may be accompanied; complainant may attend for their part) → reasoned decision **≤ 45 days from triage** → appeal to `REVW` ≤ 15 days, decided ≤ 30 days. Where a complaint overlaps a pending challenge or a court proceeding, `ETHC` may stay it; the complaint is never disclosed to parties mid-case unless it affects their case.

**Sanctions ladder** (proportionate; reasons mandatory; may combine with ancillary measures):

| Level | Sanction | Effect |
|---|---|---|
| L1 | Advice / guidance letter | Recorded; no allocation effect |
| L2 | Formal warning | K component of QI; visible to Panel Bench at renewal |
| L3 | Required training (specified hours/module) + supervised matters | Allocation continues; completion ≤ 90 days or escalation |
| L4 | Suspension from new appointments for 3–12 months | `HB_NOT_IN_GOOD_STANDING`; active matters reviewed/replaced |
| L5 | Removal from the panel (de-empanelment) | Profile 410; re-application after ≥ 3 years at `REVW` discretion |
| Ancillary | Grade down-grade; fee reduction on the matter; report to professional body (only where the Code or law requires, or the neutral consented — **[VERIFY — open: OLQ-6]**) | — |

### 7.9 Publication of outcomes

Quarterly counts by category, severity and outcome on `/trust/statistics`; annual anonymised digests (no names, no case identifiers, no dates narrower than the quarter) in the Transparency Report; L4/L5 decisions additionally update the neutral's directory status ("not currently accepting appointments" / removed) without stating reasons. Complainants receive the outcome and reasons relevant to them.

### 7.10 IMI Feedback Digest export

Neutral-initiated export (`GET /v1/neutrals/me/feedback-digest`): per-item aggregates and moderated free text from raters who ticked C1, with a time-limited Reviewer access token; no identities, amounts or case facts (S6-13).

---

## 8. Private ADR Chambers (management's "private ADR courts"; R-30, D2-16)

### 8.1 What it is

A subscription SaaS (`chambers` module, P10 FR-P10-01 to FR-P10-12) on which an independent mediator or arbitrator, a group of neutrals, a law firm, a chamber of commerce, a bar association, a university centre or a trade body runs **its own** ADR practice or centre: its own rules, fee schedules, panel and branding, on Equator's engines. Matters in a Chambers tenant are **not** administered by Equator; the tenant is the administering institution (or the neutral acts ad hoc) and Equator is the technology provider. Naming: public product name "Private ADR Chambers"; the word "Court" is never used by Equator, and a tenant may use it only after counsel review and the Emblems and Names (Prevention of Improper Use) Act 1950 check (D2-16; P10 FR-P10-01; 02 §5 Q6) — default: blocked by the label validator.

### 8.2 Plans (figures and entitlements are owned by **Appendix O**; Appendix B Card CH; all "Subject to Board approval")

| Plan | For | Price (ex-GST) | Marketplace take on bookings [U — Board] | Key entitlements |
|---|---|---|---|---|
| `NEU-PANEL` | Every Equator-empanelled neutral | ₹0 | — | Full workspace for **Equator-administered** matters (never sold; S9 N-1) |
| `CH-LITE` | Neutral with occasional private matters | ₹699/month or ₹6,990/year | 15% | 2 private matters/month, own-brand workspace on sub-domain, fee notes with GST, client intake link, eSign at ancillary rates, 50 GB |
| `CH-SOLO` | Solo practice | ₹1,499/seat/month or ₹14,990/seat/year (1–2 seats) | 15% | 5 matters/month; Equator Rules template; standard templates |
| `CH-PRO` | Groups, boutiques | ₹2,999/seat/month or ₹29,990/seat/year (min 3) | 12% | 25 matters/month; custom domain; own rules and fee schedules; own panel with allocation engine; overflow listings |
| `CH-INST` | Institutions | ₹4,999/seat/month or ₹49,990/seat/year (min 10) | 10% | 100 matters/month; SSO; API; own committees; public panel directory; MIS; bulk intake (≥ 5 arbitrators per panel) |
| `CH-IAAS` | Chambers of commerce, bar bodies, universities | ₹3,00,000–₹8,00,000/yr + revenue share | Contracted | Managed secretariat; hearing support; co-branded rules |

The take column applies only on the Private Practice Marketplace and only to non-advocate providers; advocate-neutrals pay a flat fee for Equator's own services (CN-14). *(v3.1)*

Rules carried from S9: anything a neutral needs to serve an **Equator-administered** case is free; a Chambers plan never changes the neutral's Equator profile, tier or allocation (`NO_PAID_PLACEMENT`); cancellation takes no more steps than sign-up (NN-29); GST-inclusive totals shown to individual buyers.

### 8.3 Features

| Feature | Detail | Guardrail |
|---|---|---|
| Own rules | Fork the Equator Rules template or upload own rules into the Rulebook editor; published on the tenant site; pinned per case | Validator rejects reduced statutory clocks, prohibited mechanism × vertical combinations, removal of disclosures, objection window < 15 days for arbitration, unilateral-appointment clauses, mediation recording ON by default, success fees on insurance claims, claims of statutory enforceability while NN-05 is OFF (P10 FR-P10-07) |
| Own fee schedules | Fee editor with maker–checker; INR and, for INT, USD/EUR/GBP/SGD/AED | NN-18; NN-29 honest pricing; fees never outcome-contingent where prohibited |
| Own panel | P03 engines in tenant scope: application, verification, rubric, committees, allocation, disclosures, challenges | NN-03 applies in every tenant; < 5 active arbitrators → no bulk/API/clause_auto arbitration |
| Code of conduct | Adopt the Equator Code (§5) or one no less protective (validator checks the 15 Parts' minimum content) | — |
| Branding | Logo, colours (contrast-validated), letterhead, sender domain, custom domain | Non-removable footer: "This centre is not a court and does not exercise judicial power" |
| Case management | Intake, forms, clocks, notices, DMS with hash ledger, e-bundles | NN-04, NN-10, NN-22 |
| Hearing rooms | LiveKit rooms with caucus, waiting room, interpreter channel | NN-11 |
| Outcomes | Settlement and award builders, eSign, eStamp, registration route | NN-08, NN-09 |
| AI tools | Same AI Governance Rule; premium drafting add-on for the tenant's neutrals | NN-01, NN-25; no paid AI advantage to one side inside a case |
| Billing to their clients | Tenant is merchant of record via its own Razorpay Route linked account; Equator platform fee split at source; GST invoices in the tenant's name | NN-13: settlement money never via merchant accounts; NN-31 |
| Overflow and referral | Request a neutral from Equator's panel (blind conflict check); refer matters to Equator with all-party consent | Referral never changes who appoints; no referral reward of any kind to advocates, CAs, CSs, CMAs or their firms (CN-15) *(v3.1)* |
| Run-off guarantee | 90-day run-off on suspension/cancellation; transfer or export with hash manifest | P10 FR-P10-04 |

### 8.4 Onboarding (target: live in one working day for CH-LITE/SOLO)

`Sign up (OTP) → choose applicant type and plan → KYB (PAN, GSTIN, CIN/LLPIN/registration; authorised signatory) → name/label validation → branding → rules (template or own; validator) → fee schedule → panel (≥ 1 neutral per enabled mechanism; P03 verification for each) → payment linked account (Route KYC) → DLT/WhatsApp sender (only if sending notices in own name) → go-live checklist`. 14-day trial, no payment method needed, sandbox mode (watermarked "SIMULATED"; no notices to real parties). Each step has an inline explanation and a "Do this later" option where not blocking.

### 8.5 Terms of service — key clauses (Chambers Subscription Terms, `CH-TOS-2026.1`)

1. **Roles.** The tenant is the administering institution (or the neutral acts ad hoc) and the **data fiduciary** for its matters; Equator is the **data processor** under a written contract (DPDP Act 2023 s.8(2); GDPR Art. 28 terms for INT data). Equator does not administer, supervise or endorse tenant matters.
2. **Representations.** The tenant must not state or imply that matters are Equator-administered, that it is a court, regulator or statutory body, or that it is MCI-registered or recognised.
3. **NN rules.** Platform guardrails (NN-01 to NN-40, and every Locked setting under NN-33) cannot be disabled; Equator may suspend features that a tenant configuration would use unlawfully.
4. **Code.** Tenant neutrals are bound by the Equator Code or an equivalent adopted code; no side payments on matters run on the platform.
5. **Fees.** Subscription, per-matter and add-ons per the plan; price changes with 30 days' notice; no lock-in beyond the paid term; pro-rata refund on Equator's termination for convenience.
6. **Parties first.** Party access, statutory clocks and records are never withheld for tenant non-payment (run-off, §8.3).
7. **Data ownership and portability.** Tenant owns its case data, rules, templates and branding; full export (JSON + PDF/A + hash manifest + BSA 2023 s.63(4) certificate) at any time and on exit; deletion within 30 days after run-off unless legal hold; Equator uses tenant data only to provide the service — never for marketing, model training, benchmarking across tenants or Equator's own allocation (NN-16). Aggregate, non-identifying platform metrics (uptime, feature usage) only.
8. **Security.** Equator's controls (Appendix Q); breach notice to the tenant without undue delay and within the time needed for the tenant to meet DPDP Rules 2025 and CERT-In timelines.
9. **Liability.** Capped at 12 months' fees; no liability for the tenant's decisions or its neutrals' conduct.
10. **Governing law** India; disputes by arbitration administered by an institution other than Equator (to avoid self-administration) — default: a named independent institution **[VERIFY — open: choose institution]**.

### 8.6 Marketing page — `/private-adr-chambers` (P13; separate from the Equator institution pages; SSR)

**Outline**: Hero → Who it is for (4 cards) → What you get (feature grid) → How it stays fair (guardrails) → Plans (from Appendix O; GST-inclusive toggle) → How it works (5 steps) → Comparison: "Equator-administered vs your own chambers" → FAQ → CTA.

**Copy (en)**

- **H1:** "Run your own ADR practice — on a platform built for fairness."
- **Sub:** "Private ADR Chambers gives independent mediators, arbitrators and institutions their own branded workspace: your rules, your fees, your panel. Hearings, documents, e-signing, e-stamping and billing included."
- **Primary CTA:** "Start a 14-day free trial" · **Secondary:** "See plans and prices"
- **Who it is for:** "Independent mediators and arbitrators" · "Law firms and chambers" · "Chambers of commerce and trade bodies" · "Universities and bar associations"
- **Feature grid headings:** "Your rules, published and versioned" · "Your fee schedule, with GST invoices" · "Your panel, with conflict checks" · "Secure online hearing rooms with private sessions" · "Documents with a tamper-evident record" · "E-sign and e-stamp in a few clicks" · "AI drafting help — you stay the decision-maker" · "Payments straight to your account"
- **Fairness block:** "Some things cannot be switched off: conflict disclosures, statutory time limits, confidentiality of mediation, and the rule that one side cannot pick the neutral in standard-form disputes. These protect your parties — and your awards."
- **Plans note:** "Prices exclude GST unless shown. Cancel any time from Settings in the same number of steps it took to subscribe."
- **Comparison:** "**Equator-administered:** Equator's Institutional Committee appoints neutrals and supervises the case under the Equator Rules. **Private ADR Chambers:** you are the institution (or act ad hoc). Equator provides the technology only."
- **FAQ (selected):** "Can I call my chambers a 'court'? — No. Names that suggest a court, government body or regulator are not allowed." · "Do I need to be on Equator's panel? — No. Being on Equator's panel and subscribing to Chambers are separate; a subscription never affects appointments to Equator matters." · "Who owns the data? — You do. Export it any time." · "Can my matters be enforced? — Arbitral awards made under your rules are enforceable under the Arbitration and Conciliation Act 1996, subject to its limited challenges. Mediated settlements are contracts unless converted into a consent award; a settlement in conciliation under section 73 has the status of an arbitral award (section 74)."
- **Hindi H1:** "अपना ADR अभ्यास चलाएँ — निष्पक्षता के लिए बने प्लेटफ़ॉर्म पर।"

---

## 9. Training pathways (R-34, D2-17)

### 9.1 Equator ADR Institute — facts and position

| Item | Finding (S6 §1, verified 21 Oct 2026) | Consequence |
|---|---|---|
| Operator | equatoradr.com trades as "Equa Trainings / Equa.Law", "a Brand owned by Infrabyx Consultancy (OPC) Private Limited", Jaipur; the name "Equator ADR Institute" does not appear on the pages fetched; no CIN/GSTIN displayed | Treat the Institute as a **separate legal entity** (management, D2-17) but **reconcile** trading name, legal entity, GSTIN and merchant account before any link or integration goes live (P10 OI-12; assumption A-03) |
| IMI status | IMI recognised the 40-hour programme as a **Certified Mediator Training Program (CMTP)**, announced 1 Jun 2024; IMI now calls this tier **Recognized Mediator Training Program (RMTP)**. Graduates may *apply* to be **IMI Qualified** Mediators. **No IMI QAP** found | Equator may state only the exact IMI wording with link and verified date (Claims Register) |
| Group relationship | Common Infrabyx ownership likely [U] | Disclose on every referral surface; related-party controls (Companies Act 2013 s.184 disclosure and s.188 approval; s.177 Audit Committee approval only if ERSPL is required to constitute one — master X-29) |

**Required website corrections (to be made by the Institute; Equator's referral card stays OFF until done — flag `academy.institute_referral` = OFF).** C1–C11 below are the v2 list; the binding v3 list is **C1–C20** in Appendix AF §AF.4.3 (C12–C20 added), and the flag reads its benchmark-register rows (CN-16). *(v3.1)*

| # | Current claim | Correct to |
|---|---|---|
| C1 | "IMI Accredited and Certified Mediation Training Program"; category "IMI Certified Mediation Training" | "40-hour mediation training recognised by the International Mediation Institute (IMI) as a Recognized Mediator Training Program. Graduates may apply to IMI to be listed as IMI Qualified Mediators. IMI Certified Mediator status requires separate assessment by an IMI Qualifying Assessment Program and at least 200 hours or 20 mediations." |
| C2 | "Qualifying Assessment Program" heading | Remove until IMI approves a QAP |
| C3 | "Be a Certified Mediator"; "certified and accredited mediators through EQUA" | "Certificate of Completion — 40-hour Mediation Training" |
| C4 | "Various dispute resolution platforms have accredited this training, especially Equa.Law" | Delete |
| C5 | "Grade B Mediators/Arbitrators", "Refresher for Grade A" | "Advanced Practitioner Course" / "Senior Practitioner Refresher" + "Completion does not confer any panel grade or empanelment with any institution." |
| C6 | "ISO 27001:2018"; "meets HIPAA, SOC 2 Type 1" | Show certificate number, body and validity, or remove (no ISO/IEC 27001:2018 edition exists) |
| C7 | USD prices, no GST; blanket "non-refundable" | INR price incl. GST (18%, SAC 999293); pro-rata refund before session 2 |
| C8 | Lorem-ipsum "Training Centres"; empty Membership | Remove until live |
| C9 | "Industry-ready" contract-review copy on the mediation course | Fix copy |
| C10 | Trainer bios citing Supreme Court / Australian standards | Keep in bios only ("trainer holds…"); never imply course approval |
| C11 | Course URL slug `accredited-certified-Mediation-Training-by-Equa-Law-…` repeats C1 | Create a neutral slug (e.g., `/courses/40-hour-mediation-training`) with a 301 redirect; Equator's config then points to the new URL |

Counsel question OLQ-7: Equator's exposure from linking before the corrections are made (Consumer Protection Act 2019 s.2(28), s.2(47); CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements 2022).

### 9.2 The 40-hour mediation pathway

Grade C mediators (and Grade A mediators without a 40-hour certificate, CN-07) need ≥ 40 contact hours with an assessed role-play, from **any** recognised provider. The Institute's course is one option at the configured URL `academy.institute.course_url.t40` = `https://www.equatoradr.com/courses/accredited-certified-Mediation-Training-by-Equa-Law-64e597aee4b0024818f69e23` (update to the corrected slug when C11 is done). Link text is fixed by the Claims Register — never the words in the slug: **"40-hour mediation training — Equator ADR Institute (Equa Trainings). IMI Recognized Mediator Training Program (verified {date})."** The Institute's own courses still need its own GST-inclusive INR pricing before display (C7).

### 9.3 Specialisation tracks (feed §3.6 endorsements; any provider)

| Track | Endorsement | Minimum hours | Known options (shown alphabetically; Claims Register badges only) |
|---|---|---|---|
| Property & real estate | `END-PROP` | 16 | Institute "Property Disputes" (hours not published — must publish); other providers |
| Family | `END-FAM-CORE`, `-DA`, `-CHILD` | 24 / +12 / +12 | Institute "Family Mediation Training" (hours not published); court-annexed family mediation programmes |
| Workplace | `END-WRK` | 16 | CEDR Employment & Workplace Modules (UK, £1,600 / £3,450); Institute "Workplace & HR" |
| Commercial | `END-COM` | 16 | CIArb; Institute "Commercial & Business" |
| Construction | `END-CONST` | 16 | CIArb construction routes; FIDIC training |
| Banking & lending | `END-FIN` | 16 | Academy ECFC (82 h) or equivalent |
| Insurance | `END-INS` | 16 | Academy ECIN (84 h); Institute "Healthcare & Insurance" |
| IP | `END-IP` | 12 | WIPO AMC programmes |
| International | `END-INT-MED` / `END-INT-ARB` | 16 / FCIArb or equivalent | CIArb Diploma in International Commercial Arbitration; CEDR International Accreditation (£4,050); IMI Intercultural |
| Online / tech | `END-ODR` | ETR (§10) | Equator ETR (free to empanelled neutrals) |

An Institute course counts only if it publishes hours ≥ the minimum, has an assessed component and issues a verifiable certificate (S6 §4.1). No Institute course yet exists for DA-aware, child-inclusive, POSH, IBC, construction, IP, FIN, med-arb or ODR — accept equivalents.

### 9.4 Country add-ons and `jurisdiction_eligibility_rules`

| Code | Market | What a neutral needs to practise (summary) | Equator add-on content | Engine rule |
|---|---|---|---|---|
| `CTY-IN` | India | No licence for private mediation; court-annexed/LSA panels need MCPC 40 h; Mediation Act statutory mode will need MCI registration (no regulations yet); arbitrators: A&C s.12 independence, Seventh Schedule; ACI not operational | 8 h: Mediation Act status map; s.12A CCA; Lok Adalat; MSA stamping/registration; Fifth/Seventh Schedules | Default for all domestic matters |
| `CTY-AE` | UAE | Federal Law No. 6 of 2021 on Mediation: court Lists of Mediators; special mediators' fee ≤ 5% of dispute value; mediator barred from later acting as arbitrator/expert/attorney; Federal Arbitration Law No. 6 of 2018 [K/U] | 6 h | Warn: role bar after UAE-venue mediation; fee cap check on special mediators |
| `CTY-SG` | Singapore | Mediation Act 2017: no licence; court-recordable MSA if administered by a designated provider or certified mediator [K/U]; SIMI sunsets 31 Mar 2027 → IMI | 6 h | Warn if parties want a court-recordable MSA and neither condition is met |
| `CTY-GB` | UK | No statutory licence; CMC Registered (6 h CPD, £1m PI, EU Model Code); Arbitration Act 1996 as amended by Arbitration Act 2025 (statutory disclosure duty) [K/U: commencement] | 6 h | Soft preference for CMC-registered mediators for UK-venue mediations |
| `CTY-US` | USA | State-by-state; court rosters need state certification (e.g., Florida 100-point system); Uniform Mediation Act in some states; FAA | 6 h | Flag only |
| `CTY-AU` | Australia | AMDRAS (Accredited/Advanced/Leading/Specialist); FDRP family regime separate (not covered) | 6 h | Flag only |
| `CTY-HK` | Hong Kong | Mediation Ordinance Cap 620 confidentiality; HKMAAL accreditation; Arbitration Ordinance Cap 609 | 6 h | Flag only |
| `CTY-SA` | Saudi Arabia | Arbitration Law 2012 (Royal Decree M/34) Art. 14: sole/presiding arbitrator needs a degree in law or Shari'a; good conduct; full capacity [V-secondary] | 6 h | **Hard**: Saudi seat + sole/presiding → `degree_in ∈ {law, sharia}` (`HB_JURISDICTION_INELIGIBLE`) **[VERIFY — open: OLQ-11, any revised Saudi law]** |
| `CTY-KE-NG` | Kenya / Nigeria | Kenya: court-annexed mediation needs Mediation Accreditation Committee registration (Civil Procedure Act s.59A); Nigeria: Arbitration and Mediation Act 2023; no national mediator licence [U] | 6 h (later) | Flag only |
| `CTY-CA` | Canada | No licence for private mediation; ADRIC Q.Med/C.Med/C.Med-Arb; provincial Arbitration Acts | 6 h (later) | Flag only |

Add-on quiz ≥ 80%; validity 2 years; CPD 2 h per term.

### 9.5 CPD

| Category | Accepted sources | Evidence | Cap |
|---|---|---|---|
| Skills | Courses, workshops, role-play coaching | Certificate with hours | — |
| Ethics | Ethics modules, Equator Code updates | Certificate / quiz | ≥ 4 h/yr for Grade C |
| Law and procedure | Webinars, conferences, Equator Rules updates | Attendance record | — |
| Tech/ODR | ETR-R (0.5 h), other ODR training | Completion record | ≥ 2 h/yr for Grade A |
| Teaching and writing | Teaching ADR, published articles | Programme / publication | ≤ 50% of annual requirement |
| Peer activity | Co-mediation observation, supervision, peer review | Countersigned log | ≤ 4 h/yr |

CPD from any provider counts equally; Academy CPD flows in with the learner's consent (P10 FR-P10-25). Sponsored CPD paid by a repeat user of Equator does not count (Code Part 11.3).

### 9.6 Referral model (provider picker at `training_required`)

| Rule | Implementation |
|---|---|
| ≥ 3 providers | Picker shows at least three recognised options; seed list: **Equator ADR Institute (Equa Trainings)** — IMI RMTP; **ILS Centre for Arbitration and Mediation, Pune** — IMI recognised training programme (announced 23 May 2023; ₹35,400 students / ₹47,200 professionals incl. GST as published in 2022 — re-verify before display); **High Court Mediation & Conciliation Centres / State Legal Services Authorities (MCPC 40-hour programmes)**; **CIArb India** (arbitration); others added by Panel Bench review. Card fields: name, legal entity, hours, mode, price incl. GST (as published, with date), recognition (Claims Register), link |
| Order | **Alphabetical or randomised per session**; never Institute-first by default; no pre-selection |
| Disclosure (persistent) | "Equator ADR Institute is a separate company within the Infrabyx group. {Only if the Board has approved a fee and RS-22 is `live` (CN-16):} Equator Resolution receives a fixed referral fee of ₹{x} per enrolment from it. You may train with any recognised provider. Your choice does not affect your assessment, tier, empanelment or allocation." |
| No requirement to buy | Empanelment, EQAP fee and fast-track are identical whichever provider is chosen (CN-03, CN-04) |
| Mechanics | Outbound link `?ref=eqr&t={opaque_token}`; no PII in the URL; Institute's own checkout, merchant and GSTIN; Equator never collects course fees |
| Data | Equator → Institute: nothing by default; optional "pre-fill my details" with itemised consent (name, email, mobile; purpose `training_enrolment`). Institute → Equator: only `{certificate_no, holder_name, course_code, hours, completion_date, assessment_result: pass/fail, issuer_signature, status}` after consent captured on Equator's side; never recordings, scores, attendance or payment data (DPDP Act 2023 ss.5–6) |
| Verification | Institute `GET /verify/{certificate_no}` or a signed W3C Verifiable Credential; nightly revocation polling |
| Conflict walls | Institute trainers/coaches/assessors cannot sit on `APPT`, assess their own trainees in EQAP or review complaints about them (`trainer_of` edge) |
| Commercials | **None (₹0) by default** (D3-38); a flat referral fee per enrolment only after Board approval under s.188 and the RS-22 registry record going `live`; never tied to empanelment or allocation; arm's-length agreement approved by both boards; related-party disclosure where directors are common; GST on any commission (OLQ-8) |
| Monitoring | Transparency Report §6.7 row 10 shows the share of panel by training provider |

---

## 10. Equator Tech Readiness (ETR) and the Grade A Tech Concierge

ETR is **run by Equator Resolution** (not the Institute), free to empanelled neutrals and applicants, delivered in the Academy LMS in Equator's own tenant scope (`issuing_entity = EQUATOR_RESOLUTION`).

| Module | Duration | Content | Assessment | Required for |
|---|---|---|---|---|
| ETR-1 Platform basics | 60 min, self-paced, en/hi | Login, passkey/MFA and step-up; neutral dashboard; offers; e-signing disclosures; bundle navigation | Click-through checklist | All, before activation |
| ETR-2 Online hearing room | 90 min live sandbox with a tech coach | Waiting room, breakout caucus, screen-share, muting, recording-consent controls (NN-11), interpreter channel, low-bandwidth audio fallback | **Live mock**: 20-min opening + caucus switch, observed | **Grade A before activation**; everyone before the first online matter |
| ETR-3 Digital procedure | 60 min | Remote-hearing protocol; witness-room checks; cybersecurity directions; e-award and e-MSA signing (IT Act 2000 s.3A; Aadhaar eSign; DSC) | Quiz ≥ 80% | All arbitrators |
| ETR-4 AI and confidentiality | 45 min | AI Governance Rule; non-delegation (CIArb AI Guideline 2025); DPDP Act 2023 duties; no personal devices; caucus-note sealing | Attestation | All |
| ETR-R Refresher | 30 min annually | Release notes + 5-question check | Quiz ≥ 80% | All (0.5 h tech CPD) |

**Tech Concierge** (role `tech_concierge`; Appendix S §6 matrix):

| Item | Rule |
|---|---|
| Assignment | Named concierge for every Grade A neutral for the first 3 hearings, and on request thereafter; any neutral may request one for a complex hearing |
| Scope | Operates controls **only on the neutral's instruction**: admit/move participants, mute, open/close breakout rooms, share bundle pages, troubleshoot. No content edits, notes, drafting, signing, or presence in a caucus unless the neutral and the caucusing party agree; never present in a sealed tier |
| Logging | Every action logged "on instruction of {neutral}" in the hearing log; parties see a "Technical assistant present" banner |
| SLA | Pre-hearing tech check T−24 h (15 min); on-call during the hearing; response ≤ 2 minutes in session |
| Assisted mode | Case manager or concierge drives screen controls; the neutral retains every decision |
| Accessibility | Large-font UI preset; keyboard shortcuts card; desktop/tablet sufficient (mobile parity not required for Grade A) |
| Security | Assisted hardware-key enrolment over video (concierge never sees credentials; Appendix S §2.4) |
| Conflicts | Concierge runs the P03 conflict check against the case before assignment |

---

## 11. Data model, APIs, events, errors, flags and configuration

### 11.1 Tables (schema `core` unless stated; RLS tenant isolation; audit on every write; aligns with Appendix F §F.4.7 and P03 §7.2)

```sql
-- governance
core.committees(id, tenant_id, code CHECK (code IN ('EIC','APPT','CHAL','SCRU','ETHC','RULE','AIOV','TRNS','REVW','NOMS')),
  bench text NULL CHECK (bench IN ('panel','case')), name, terms_of_reference_doc_id, quorum smallint, min_external_pct numeric(5,2))
core.committee_members(id, committee_id, person_id, role CHECK (role IN ('chair','vice_chair','member')), is_external boolean,
  external_attested_at timestamptz, term_from date, term_to date, gender_optional text, status)
core.committee_meetings(id, committee_id, scheduled_at, mode, agenda_doc_id, minutes_doc_id, quorum_met boolean)
core.committee_recusals(id, meeting_id, member_id, matter_ref, source CHECK (source IN ('declared','graph')), reason_code)
core.institutional_decisions(id, tenant_id, decision_no UNIQUE, committee_id, meeting_id NULL,
  type CHECK (type IN ('empanelment','grade','regrade','endorsement','probation_exit','appointment','manual_exception','objection',
    'co_arbitrator_confirmation','challenge','scrutiny_approval','complaint_outcome','sanction','appeal','rules_approval',
    'policy_approval','ai_release','transparency_report','assessor_roster')),
  matter_refs jsonb, members_present uuid[], votes jsonb, reasons text NOT NULL, evidence_ids uuid[],
  publication_class CHECK (publication_class IN ('never','anonymised_after_12m','statistics_only')),
  supersedes_id NULL, signed_by uuid, signed_at, published_at NULL, prev_hash char(64), row_hash char(64))
core.users_forum_members(id, organisation_id, tier CHECK (tier IN ('company','law_firm','msme_association','invited')), from_date, to_date, published boolean)

-- grading
core.grading_policies(id, version, rules_json, effective_from, approved_decision_id, status)
core.neutral_grades(neutral_id PK, grade CHECK (grade IN ('A','B','C')), basis CHECK (basis IN ('entrant','professional_15y',
  'retired_judge_sc_hc','retired_tribunal_hc_level','retired_district_judge_30y','professional_30y_adr')),
  policy_version, assessment_score numeric(5,2) NULL, decided_at, decision_id)
core.neutral_grade_history(id, neutral_id, from_grade, to_grade, reason_code, evidence_ids uuid[], decision_id, effective_at)
core.neutral_experience_log(id, neutral_id, role, mechanism, vertical, sector, matter_date, hours numeric(5,1), mode, value_band,
  co_neutral boolean, verification_source CHECK (verification_source IN ('equator_record','court_certificate','lsa_certificate',
  'institution_letter','referee','self_declared')), outcome_recorded text NULL)   -- never scored (lint NN-28_outcome_never_scored)
core.endorsement_catalogue(code PK, version, public_name, min_hours, assessment_kind, cpd_hours_per_term, trigger_expr, alias_of NULL)
core.neutral_endorsements(id, neutral_id, code, status CHECK (status IN ('pending','granted','expired','revoked')), valid_until, evidence_ids uuid[], decision_id)

-- training, EQAP, ETR
core.training_providers(id, name, legal_entity, country, recognitions jsonb, is_affiliate boolean, fast_track_eligible boolean,
  referral_terms_id NULL, claims_register_ids uuid[])
core.neutral_trainings(id, neutral_id, provider_id, course_code, hours numeric(5,1), mode, completion_date, assessed boolean,
  certificate_no, verification_method CHECK (verification_method IN ('verify_endpoint','verifiable_credential','issuer_email','manual')), status)
core.qap_sittings(id, sitting_date, mode, component CHECK (component IN ('R','W','E','A','X')), rubric_version, bank_form)
core.qap_assessor_assignments(id, sitting_id, candidate_neutral_id, assessor_person_id, is_external boolean,
  independence_declared_at, conflict_check_result CHECK (conflict_check_result IN ('clear','blocked')))
core.qap_results(id, sitting_id, candidate_neutral_id, roleplay_score, ethics_criterion, written_pct, ethics_scenarios smallint,
  critical_fail boolean, award_score, pass boolean, resit_no smallint, recording_hash char(64), recording_delete_after date)
core.neutral_tech_readiness(id, neutral_id, module CHECK (module IN ('ETR-1','ETR-2','ETR-3','ETR-4','ETR-R')), completed_at, score, mock_session_id NULL, valid_until)
core.tech_concierge_assignments(id, neutral_id, concierge_user_id, case_id NULL, hearing_id NULL, from_ts, to_ts, conflict_cleared boolean)

-- allocation and quality
core.quality_index_snapshots(id, neutral_id, role_family, period daterange, n_matters, t, a, f, r, k, c, qi_raw, qi, formula_version)
core.allocation_runs   -- P03 canonical + columns: rotation_window jsonb, first_time_inserted boolean, qi_beta numeric(3,2), weights jsonb
core.jurisdiction_eligibility_rules(id, country char(2), seat_role, condition_expr, severity CHECK (severity IN ('hard','warn','soft')), legal_rule_id)

-- feedback and complaints
core.neutral_reviews   -- Appendix F + respondent_kind CHECK (respondent_kind IN ('party','counsel','case_manager','co_neutral')),
                       --   item_scores jsonb, pressured text, share_with_neutral boolean, publish_consent boolean, is_repeat_player_org boolean
core.review_replies(id, review_id, neutral_id, body text CHECK (length(body) <= 1000), created_at)
core.neutral_complaints(id, ref, complainant_kind, case_id NULL, neutral_id, categories text[], severity CHECK (severity IN ('S0','S1','S2','S3')),
  status CHECK (status IN ('received','triaged','investigating','awaiting_response','hearing','decided','appealed','closed','stayed')),
  interim_measure, decision_id NULL)
core.complaint_sanctions(id, complaint_id, level CHECK (level IN ('L1','L2','L3','L4','L5')), ancillary text[], effective_from, effective_to)
core.transparency_reports(id, period, query_pack_version, dataset_hash, approved_decision_id, published_at)
```

### 11.2 APIs (`/v1`; Idempotency-Key on POSTs; RFC 9457 errors)

| Method & path | Purpose | Role |
|---|---|---|
| GET /v1/public/governance/committees · …/decisions?class=published | Public governance pages | public |
| POST /v1/committees/{id}/meetings · POST …/meetings/{mid}/decisions | Agenda; reasoned decision (e-sign `aal2-pr`) | registrar; committee_member/chair |
| POST /v1/neutral-applications/{id}/grade-precheck | Deterministic provisional grade + route | system (on submit); applicant read |
| GET /v1/neutral-applications/{id}/tracker | Status tracker payload | applicant |
| GET /v1/training-providers?for=mediation_40h | Provider picker (≥ 3; order param ignored; server randomises/alphabetises) | applicant |
| POST /v1/neutrals/{id}/trainings · POST …/trainings/{tid}/verify | Record and verify training | neutral; panel_manager |
| POST /v1/qap/sittings · POST /v1/qap/sittings/{id}/bookings · POST …/scores · POST …/appeals | EQAP lifecycle | registrar; candidate; assessor; candidate |
| POST /v1/neutrals/{id}/regrade-requests · POST /v1/neutrals/{id}/grade-decisions | Re-grading | neutral; Panel Bench |
| GET /v1/neutrals/me/quality-index | Own QI with components | neutral |
| GET /v1/public/allocation-policy | Published policy and current parameters | public |
| POST /v1/feedback/{token} · POST /v1/reviews/{id}/replies · POST /v1/moderation/{id}/decision | Feedback, reply, moderation | participant; neutral; quality_officer |
| POST /v1/public/complaints/neutral · POST /v1/complaints/{id}/triage · …/response · …/decision · …/appeal | Complaints | public/party; quality_officer; neutral; ETHC; parties/neutral |
| GET /v1/neutrals/me/feedback-digest | IMI digest export | neutral |
| POST /v1/neutrals/{id}/tech-readiness/{module} · POST /v1/concierge/assignments | ETR; concierge | neutral/LMS machine; registrar |
| GET /v1/public/transparency/dashboard · GET …/reports/{year} | Transparency | public |
| POST /v1/referrals/institute/click | Opaque-token referral | applicant |

### 11.3 Events (`equator.<ctx>.<entity>.<verb>.v1`; no sealed data or narratives in payloads)

`equator.governance.decision.recorded.v1` · `equator.governance.member.recused.v1` · `equator.governance.decision.published.v1` · `equator.neutrals.application.status_changed.v1` · `equator.neutrals.grade.prechecked.v1` · `equator.neutrals.training.required.v1` · `equator.neutrals.training.verified.v1` · `equator.neutrals.qap.booked.v1` · `equator.neutrals.qap.passed.v1` · `equator.neutrals.qap.failed.v1` · `equator.neutrals.grade.changed.v1` · `equator.neutrals.endorsement.granted.v1` · `equator.neutrals.endorsement.expired.v1` · `equator.neutrals.tech_readiness.completed.v1` · `equator.neutrals.quality_index.computed.v1` · `equator.neutrals.review.moderated.v1` · `equator.neutrals.review.replied.v1` · `equator.neutrals.complaint.received.v1` · `equator.neutrals.complaint.triaged.v1` · `equator.neutrals.complaint.decided.v1` · `equator.neutrals.sanction.applied.v1` · `equator.referral.institute.clicked.v1` (token only) · `equator.reporting.transparency_report.published.v1`.

### 11.4 Enumerations

`accreditation_body`: IMI_QUALIFIED, IMI_CERTIFIED, IMI_INTERCULTURAL, IMI_ODR, IMI_ADVOCATE, SIMI_L1, SIMI_L2, SIMI_L3, SIMI_CERTIFIED (legacy; `superseded_by` IMI from 31 Mar 2027), CIARB_ACIARB, CIARB_MCIARB, CIARB_FCIARB, CIARB_CARB, CMC_ASSOCIATE, CMC_REGISTERED, CMC_FELLOW, CEDR_ACCREDITED, AMDRAS_ACCREDITED, AMDRAS_ADVANCED, AMDRAS_LEADING, AMDRAS_SPECIALIST, NMAS (legacy → AMDRAS), HKMAAL_GENERAL, HKMAAL_FAMILY, ADRIC_QMED, ADRIC_CMED, ADRIC_CMEDARB, ADRIC_QARB, ADRIC_CARB, FLORIDA_COUNTY, FLORIDA_FAMILY, FLORIDA_CIRCUIT, FLORIDA_DEPENDENCY, FLORIDA_APPELLATE, MCPC_40H, MCPC_TRAINED_MEDIATOR, HC_PANEL, LSA_PANEL, KENYA_MAC, IIAC_PANEL, MCIA_PANEL, SIAC_PANEL, ICA_PANEL, IBBI_IP, EQUATOR_ACADEMY (ECM-B/ECM-A/ECxx), OTHER; hidden until flags ON: MCI_REGISTERED (`mci_regs_in_force`), ACI_ACCREDITED (`aci_operational`).

### 11.5 Error codes (new canonical codes — add to Appendix F §F.10.1 per master X-20)

`HB_GRADE_INELIGIBLE` (409) · `HB_JURISDICTION_INELIGIBLE` (409) · `NEUTRAL_APPLICATION_DUPLICATE` (409, *v3.1*) · `COMMITTEE_COMPOSITION_INVALID` (422) · `COMMITTEE_MEMBER_RECUSED` (403) · `DECISION_REASONS_REQUIRED` (422) · `ASSESSOR_CONFLICT` (409) · `ASSESSOR_EXTERNAL_REQUIRED` (422) · `QAP_RESIT_TOO_EARLY` (422) · `QAP_RESIT_LIMIT` (422) · `GRADE_PRECHECK_UNVERIFIED` (422) · `DIRECTORY_SORT_NOT_ALLOWED` (400) · `FEEDBACK_OUTCOME_ITEM_FORBIDDEN` (422) · `REVIEW_REPLY_TOO_LONG` (422) · `COMPLAINT_CONSENT_REQUIRED` (422) · `QI_INPUT_NOT_ALLOWED` (500, CI) · `TRAINING_PROVIDER_PICKER_MIN` (500, config) · `LABEL_FORBIDDEN_TERM` (422).

### 11.6 Feature flags and configuration keys

Tiers per NN-33 and Appendix V §V.1 (allocation and grading values are platform G, changed by the Rules Sub-Committee through maker–checker; no tenant may change them for Equator-administered matters — NN-03, NN-28). *(v3.1: tier column added)*

| Key | Default | Tier | Guardrail |
|---|---|---|---|
| `grading.policy_version` | `v2` | G (platform) | maker–checker; `RULE` decision |
| `grading.c_pass_roleplay` / `b_pass_roleplay` | 65 / 70 | G (platform) | may rise, not fall below 60 |
| `qap.resit_wait_days` / `qap.max_resits_24m` | 60 / 2 | G (platform) | — |
| `qap.imi_recognised` (flag) | OFF | G (claims flag) | switches Claims Register wording; ON only with the IMI approval letter |
| `allocation.rotation_window` | 5 | G (platform) | 3–10 |
| `allocation.qi_beta.rules_weighted` / `.rotation` | 0.30 / 0.00 | G (platform) | ≤ 0.40 (L ceiling) |
| `allocation.first_time_target_pct` | 15 | G (platform) | 5–30 |
| `allocation.volume_fairness_multiple` | 2.0 | G (platform) | 1.5–3.0 |
| `allocation.lr_arb_007_absolute_cap.enabled` | ON (non-bulk) | G (legal) | `legal_reviewer` |
| `quality.qi_shrinkage_k` | 5 | G (platform) | ≥ 3 |
| `quality.capacity_uplift_qi75_pct` / `capacity_cut_qi40_pct` | 20 / 25 | G (platform) | ≤ 30 / ≤ 50 |
| `feedback.min_n_aggregate` / `min_n_public_profile` | 5 / 10 | T≥L | ≥ 5 / ≥ 10 (X-28 floors locked) |
| `feedback.repeat_player_weight_cap_pct` | 20 | L ceiling (lower only) | ≤ 20 |
| `complaints.decision_days` | 45 | T≤L | ≤ 60 |
| `academy.institute_referral` (flag) | OFF | G (Board + counsel) | ON only after corrections C1–C20 (Appendix AF §AF.4.3), entity reconciliation (A-03) and, for any fee, the RS-22 record `live` (CN-16) |
| `academy.institute.course_url.t40` | URL in §9.2 | G (claims) | Claims Register-controlled link text |
| `training.picker_min_providers` | 3 | T≥L | ≥ 3 (X-29) |
| `chambers.court_label_override` (flag) | OFF | G (legal, per tenant) | counsel opinion attached |
| `mci_regs_in_force`, `aci_operational` (flags) | OFF | G (legal flag) | legal admin with notification reference |

---

## 12. Acceptance tests (Gherkin; `tests/acceptance/appendix-n/`)

```gherkin
Feature: Neutral governance, grading, EQAP, allocation, feedback, complaints, training and Chambers

Scenario: NN-17_no_court_naming_governance
  When an institution_admin creates a committee named "Equator Court of Appointments"
  Then the response is 422 with code "LABEL_FORBIDDEN_TERM"

Scenario: EIC decision rejected without external majority
  Given the Challenge sub-committee has 3 members of whom 1 is external and 1 external member is recused
  When the chair signs a challenge decision
  Then the response is 422 with code "COMMITTEE_COMPOSITION_INVALID"

Scenario: Recused member cannot open papers
  Given committee member M formerly acted as counsel for the respondent in case C
  When M opens the agenda item for case C
  Then the response is 403 with code "COMMITTEE_MEMBER_RECUSED" and a recusal row with source "graph" exists

Scenario: Adverse decision needs reasons
  When the Panel Bench records a "grade" decision refusing empanelment with reasons of 40 characters
  Then the response is 422 with code "DECISION_REASONS_REQUIRED"

Scenario: Self-declared experience never grades above C
  Given an applicant declares 22 years at the Bar with experience_start_source unverified
  When the grade pre-check runs
  Then provisional_grade is "C" and the tracker says verification may change the tier

Scenario: Retired High Court judge is Grade A but must hold 40 hours to mediate
  Given a verified retired High Court judge applying as mediator without a 40-hour certificate
  When the grade pre-check runs
  Then provisional_grade is "A", competence_route is "waiver" for EQAP
  And state is "training_required" for the mediator role until a 40-hour certificate is verified

Scenario: NN-28_no_course_purchase_advantage
  Given two Grade C candidates with identical records, one trained by Equator ADR Institute and one by another IMI RMTP provider
  When each books an EQAP sitting
  Then both are quoted ₹11,210 including GST and both must take components R, W and E

Scenario: Fast-track available on equal terms
  Given a provider whose evidence pack meets the EQAP integrity standard is marked fast_track_eligible
  When a Grade B candidate holding its certificate applies
  Then component R is skipped and component E is still required

Scenario: Assessor who trained the candidate is blocked
  Given assessor X has a conflict edge "trainer_of" to candidate Y
  When the registrar assigns X to Y's role-play
  Then the response is 409 with code "ASSESSOR_CONFLICT"

Scenario: Each sitting has an external assessor
  When the registrar confirms a sitting whose two assessors are both Equator employees
  Then the response is 422 with code "ASSESSOR_EXTERNAL_REQUIRED"

Scenario: Re-sit wait enforced
  Given candidate Y failed component W on 1 Nov 2026
  When Y books component W on 15 Dec 2026
  Then the response is 422 with code "QAP_RESIT_TOO_EARLY"

Scenario: HB_GRADE_INELIGIBLE for emergency arbitrator
  Given an EA application in a COM matter and a Grade B neutral at the head of the EA-COM roster
  When the allocation run executes
  Then the Grade B neutral is excluded with filter "grade_eligible" and only Grade A neutrals are offered

Scenario: Saudi seat degree rule
  Given an INT arbitration seated in Riyadh and a Grade A candidate without a law or Shari'a degree
  When the run selects a sole arbitrator
  Then that candidate is excluded with code "HB_JURISDICTION_INELIGIBLE"

Scenario: Golden vector GV-N-01 reproduces the QI-weighted draw
  Given a rules_weighted window with QI 82, 64, 58, 46, panel median 61 and beta 0.30
  When the published script runs with a seed mapping to u = 0.40
  Then the weights are 1.126, 1.018, 0.982, 0.910 and candidate 2 is selected

Scenario: NN-28_qi_inputs_allow_list
  Given a developer adds "settlement_rate" to the Quality Index inputs
  When CI runs
  Then the build fails with "QI_INPUT_NOT_ALLOWED"

Scenario: First-time appointee guarantee
  Given the ARB-COM panel's first-time share this quarter is 8% against a 15% target
  And the rotation window contains no never-appointed neutral
  When a run starts
  Then the earliest eligible never-appointed neutral is added to the window and first_time_inserted = true

Scenario: Rotation method ignores QI
  Given a FIN bulk run with method "rotation"
  When two candidates differ only in QI
  Then the candidate earlier in the queue is selected regardless of QI

Scenario: NO_PAID_PLACEMENT (extended, v3.1)
  When CI analyses query plans and grants for the directory, allocation, eligibility, grading, Quality Index and conflict services
  Then no read path reaches core.subscriptions, core.plans, core.memberships, chambers.subscriptions, chm, growth, mkp sponsorship, ad or provider-subscription tables, or any rev table

Scenario: Grade B public label is Principal (v3.1)
  When the directory renders a Grade B neutral in en
  Then the label is "Principal Neutral" and copy lint rejects "Senior Neutral" with LABEL_FORBIDDEN_TERM

Scenario: Directory refuses paid-style sort
  When a client calls GET /v1/public/neutrals?sort=featured
  Then the response is 400 with code "DIRECTORY_SORT_NOT_ALLOWED"

Scenario: NN-28_feedback_no_outcome_items
  When a form author adds the item "Did you get the result you wanted?" to feedback_party.v2
  Then form validation fails with code "FEEDBACK_OUTCOME_ITEM_FORBIDDEN"

Scenario: Public rating appears only at ten
  Given neutral N has 9 published ratings with publish consent
  When the public profile is requested
  Then no rating aggregate is returned and the scorecard shows item means to N

Scenario: Right of reply travels with the comment
  Given a moderated comment shared with neutral N and N's reply
  When the comment is attached to a quality review
  Then the reply is attached to the same review record

Scenario: S1 complaint suspends allocation immediately
  When a complaint alleging an undisclosed Seventh Schedule relationship is triaged S1
  Then the neutral is not offered new matters within 5 minutes, active matters are listed for review and parties in affected cases are notified

Scenario: Sanction decided within 45 days with appeal right
  Given an S2 complaint triaged on 1 Dec 2026
  Then the ETHC decision clock expires on 15 Jan 2027 and the decision letter states the 15-day appeal right

Scenario: Provider picker shows three and is not Institute-first
  Given the academy.institute_referral flag is ON
  When 100 applicants open the provider picker
  Then each sees at least 3 providers, none is pre-selected, and Equator ADR Institute is first for no more than the share expected from randomisation or alphabetical order

Scenario: Institute referral hidden until corrections confirmed
  Given academy.institute_referral is OFF
  When an applicant reaches training_required
  Then the Institute card is not displayed and at least 3 other providers are shown

Scenario: Credential payload minimised
  When the Institute posts a verification payload containing "roleplay_score"
  Then the field is rejected and not stored

Scenario: ETR-2 required before Grade A activation
  Given a Grade A neutral who has completed ETR-1 and ETR-4 only
  When induction completion is attempted
  Then activation is blocked with the missing module "ETR-2"

Scenario: Concierge cannot enter a caucus without consent
  Given a tech_concierge assigned to a hearing
  When the concierge joins caucus room 2 without recorded consent of the neutral and the caucusing party
  Then access is denied and the attempt is logged

Scenario: Chambers tenant cannot be called a court
  When a chambers_admin sets the display label "Sharma Private ADR Court"
  Then the response is 422 with code "LABEL_FORBIDDEN_TERM"

Scenario: Chambers plan never changes Equator allocation
  Given neutral N on CH-PRO and neutral M on no plan, otherwise identical
  When an Equator run with a fixed seed executes
  Then ranked candidates are identical to a run where N has no plan
```

---

## 13. Open items and counsel questions

| # | Item | Default until closed |
|---|---|---|
| OI-N-01 | EIC Charter text and Board resolution; legal effect on appointment defensibility (02 §5 Q9) | P03 committees operate under interim terms of reference; Charter flag `governance.charter_adopted` OFF blocks public "Institutional Committee" claims |
| OI-N-02 | OLQ-2: status-based grades and grade-based allocation vs A&C ss.11–12 and *CORE*; diversity safeguard | First-time appointee target and diversity reporting ON |
| OI-N-03 | OLQ-3: Grade C sole arbitrators in ≤ ₹5,00,000 documents-only FIN matters (s.12(3)(b)) | Allowed only with award-writing pass; Board may switch to B-only per panel |
| OI-N-04 | OLQ-4/5/7/8: Institute tie-up — Competition Act s.3(4)/s.4, CPA 2019 and CCPA 2022 disclosures, DPDP roles, GST on referral fees | Referral flag OFF |
| OI-N-05 | OLQ-6: notifying IMI/professional bodies of sanctions | Only with the neutral's prior consent in the Code acceptance |
| OI-N-06 | OLQ-10: "Justice (Retd.)" honorific (OLQ-9 closed by master X-26: label "Principal Neutral") | Sub-label shown; honorific opt-in |
| OI-N-07 | OLQ-11: Saudi Art. 14 scope; UAE mediator lists | Hard rule for sole/presiding only |
| OI-N-08 | OLQ-12 research follow-ups (IMI Code clauses, QAP fees, Indian QAP holders, SIAC/HKIAC/MCIA criteria, AMDRAS dates) | Marked [VERIFY] |
| OI-N-09 | CN-06 cap reconciliation for FIN bulk | Relative cap for bulk; absolute cap for non-bulk |
| OI-N-10 | s.42A and publication of challenge decisions | `anonymised_after_12m` held behind `governance.publish_challenge_decisions` = OFF until counsel opines |
| OI-N-11 | Assessment fee SAC/GST treatment; IMI QAP application fee | Quote "exclusive of applicable taxes" internally; consumer display GST-inclusive at 18% |
| OI-N-12 | Chambers ToS dispute-resolution institution (§8.5 cl. 10) | Choose an unaffiliated institution |

---

## Phase addendum (paste into P03)

> P03 — v2 addendum from Appendix N. These requirements are part of P03 scope and exit gate. Where they conflict with P03 §1–§14, they prevail (CN-01 to CN-12).

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P03-V2-01 | Governance objects: committees (EIC, APPT Panel/Case benches, CHAL, SCRU, ETHC, RULE, AIOV, TRNS, REVW, NOMS), members with external test, meetings, recusals, `core.institutional_decisions` hash-chained (App. N §1, §11.1) | Composition check rejects decisions without required external share; every decision has reasons, votes, e-sign `aal2-pr`; Gherkin "EIC decision rejected…", "Recused member…", "Adverse decision needs reasons" pass |
| FR-P03-V2-02 | Rename/mapping: Empanelment Committee → APPT Panel Bench; Appointments Committee → APPT Case Bench; challenges → CHAL; Appeals Committee → REVW (App. N §1.3) | No UI string, route or code identifier uses "Court"; label validator test `NN-17_no_court_naming_governance` green |
| FR-P03-V2-03 | Committee portal integration (App. S §2.10, SCR-S-D07): agendas, watermarked papers, vote, declare conflict, sign | Member sees only matters granted by the Registrar's agenda; conflicts auto-block |
| FR-P03-V2-04 | Replace FR-P03-06 score-as-grade with `grading_policy.v2` (App. N §3); keep the /100 rubric as `assessment_score` | Grades derive from basis + gates; migration re-grades all existing neutrals within 90 days with reasons; no down-grade without review |
| FR-P03-V2-05 | Application form `neutral_application.v3` (App. N §2.3) incl. experience basis, start-date source, ADR matters log, trainings, `institute_relationship` | Form schema versioned; en/hi; mobile autosave; Doc-AI pre-fill needs human confirm |
| FR-P03-V2-06 | Deterministic grade pre-check from verified fields only | Self-declared years never yield above C; output shown on submit with §3.2 explainer |
| FR-P03-V2-07 | Journey states incl. `training_required` (180 days), `qap_scheduled`, `qap_passed/failed`, `fast_track_review`, `waiver_confirmed`, `inducting`, `approved_lapsed` and the SLAs in App. N §2.2 | Every transition audited and emits `equator.neutrals.application.status_changed.v1`; SLA breaches raise registrar tasks |
| FR-P03-V2-08 | Status tracker SCR-P03-04 v2 with owner, "act by" date and §2.4 copy (en/hi) | WCAG 2.2 AA; one primary action per screen; push/SMS via DLT template `NEU_STATUS_01` |
| FR-P03-V2-09 | Experience log with verification sources and Equator-record import; outcome stored, never scored | CI lint `NN-28_outcome_never_scored` green |
| FR-P03-V2-10 | EQAP: sittings, components R/W/E/A/X, rubrics and anchors (§4.3–§4.4), two assessors with ≥ 1 external, independence declaration, `trainer_of` bar, calibration, recording deletion after 1 year, feedback report ≤ 10 WD | Gherkin "Assessor who trained…", "Each sitting has an external assessor", "Re-sit wait enforced" pass |
| FR-P03-V2-11 | Fast-track on equal terms for any provider meeting the evidence-pack standard; supersedes FR-P03-05 "Academy fast-track" | Gherkin "Fast-track available on equal terms" and `NN-28_no_course_purchase_advantage` pass |
| FR-P03-V2-12 | EQAP fees identical for all (§4.8), GST-inclusive display, concessions by rule | Quote engine returns same amount irrespective of training provider |
| FR-P03-V2-13 | Endorsement catalogue (§3.6) as versioned Ruleset objects incl. `END-INT` alias and `CTY-*` add-ons; `HB_SPECIALISM_REQUIRED` reads it | Alias resolves by seat; expired endorsement removes eligibility within 5 minutes |
| FR-P03-V2-14 | Hard filter `grade_eligible()` (§4.9) with `HB_GRADE_INELIGIBLE`; `jurisdiction_eligibility_rules` with `HB_JURISDICTION_INELIGIBLE` | One `NN-03_*`/`NN-28_*` test per code; Saudi and EA scenarios pass |
| FR-P03-V2-15 | Allocation pipeline v2 (§6): caps incl. LR-ARB-007 absolute cap for non-bulk (CN-06) and volume fairness; rotation window; first-time guarantee; capped QI weighting (β 0.30 rules_weighted, 0 rotation); remove "value band ↔ grade" from the soft score | Golden vector GV-N-01 reproduces; first-time and rotation scenarios pass; IEP shows window, weights, β and seed |
| FR-P03-V2-16 | Quality Index job, components, shrinkage, capacity ceiling effects; neutral view of own QI | `NN-28_qi_inputs_allow_list` green; QI never in public API |
| FR-P03-V2-17 | Feedback forms F1–F4 (§7.2); moderation ≤ 72 h; right of reply; aggregation thresholds 5 (internal) / 10 (public profile) — amends FR-P03-33 | `NN-28_feedback_no_outcome_items`; "Public rating appears only at ten"; "Right of reply" pass |
| FR-P03-V2-18 | Public complaint form v2, severity S0–S3, investigation, ETHC hearing, sanctions L1–L5, appeal to REVW, anonymised publication (§7.7–§7.9) — amends FR-P03-37 | S1 suspends within 5 minutes; decision clock 45 days from triage; appeal 15 days |
| FR-P03-V2-19 | Re-grading engine and grade history with reason codes and 15-day appeal (§3.8) | "Never" triggers are absent from rule inputs (static check) |
| FR-P03-V2-20 | Directory v2: grade labels Distinguished/Principal/Associate with sub-label (master X-26; "Senior" blocked by copy lint); allow-list fields; sort only random/alphabetical; `NO_PAID_PLACEMENT` CI test | Gherkin "Directory refuses paid-style sort", `NO_PAID_PLACEMENT` pass; advocate-neutral video/ratings OFF until OI-03 closes |
| FR-P03-V2-21 | Code of Conduct ECC-2026.1 (§5) published as `core.procedure_rules`, e-signed at induction and accepted per appointment | Version pinned per appointment; Hindi version blocked until legal review |
| FR-P03-V2-22 | CPD per grade + endorsement (higher of), ETR-R 0.5 h credit, sponsored-CPD exclusion | Lapse → ineligible after 90-day grace |
| FR-P03-V2-23 | Transparency dashboard data feed and annual report generator (§6.7) with n < 10 suppression (master X-28) and Claims Register binding | Reproducible query pack hash stored; sealed data excluded |
| FR-P03-V2-24 | IMI Feedback Digest export (§7.10) | Export contains no identities, amounts or case facts |
| FR-P03-V2-25 | Seed data: 3 EIC sub-committee sittings, 12 EQAP candidates (incl. 2 failures and 1 appeal), 120 neutrals graded A/B/C with endorsements, 4 complaints across S1–S3 | `P03-demo.md` extends the click-path: apply → pre-check → training picker → EQAP → Panel Bench → induction → probation → rules_weighted run with QI → complaint → sanction |
| FR-P03-V2-26 | *(v3.1)* Panel-manager work queue (§2.2): SLA-ordered queue, recorded SLA pause reasons on the tracker, duplicate-application check (`NEUTRAL_APPLICATION_DUPLICATE`), previewed bulk actions, leave delegation; `NO_PAID_PLACEMENT` extended to `chm`, `mkp` and `rev` (CN-13); Grade B label "Principal Neutral" (CN-02) | Duplicate application by the same Bar enrolment number returns 409; tracker shows each pause with its start date; extended `NO_PAID_PLACEMENT` and "Grade B public label is Principal" scenarios pass |

**Exit gate additions:** all App. N §12 scenarios green; 1,000-case FIN bulk and 200-case COM rules_weighted simulations show zero cap breaches, first-time share ≥ target where eligible first-timers exist, and no allocation difference attributable to any billing/plan attribute.

---

## Phase addendum (paste into P10)

> P10 — v2 addendum from Appendix N. Part of P10 scope and exit gate.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P10-V2-01 | Private ADR Chambers marketing page `/private-adr-chambers` (outline and copy, App. N §8.6), SSR, plans pulled from Appendix O; `/chambers` redirects | Lighthouse SEO ≥ 95; GST-inclusive toggle; no "court" wording; Claims Register binds any statistic |
| FR-P10-V2-02 | Add plan `NEU-PANEL` (₹0) to the plan catalogue. `CH-LITE` (₹699/month; ₹6,990/year; 2 private matters/month) and the plan-dependent marketplace take (15/15/12/10% [Board]) are specified once, in FR-P10-V2-O1 and FR-P10-V2-O2 (Appendix O §10A) | Entitlements enforced; cancellation steps ≤ sign-up steps (NN-29) |
| FR-P10-V2-03 | Chambers Subscription Terms `CH-TOS-2026.1` (§8.5) versioned and e-accepted; DPA with tenant as fiduciary and Equator as processor | Acceptance stored per tenant; export endpoint delivers JSON + PDF/A + hash manifest + BSA s.63(4) certificate |
| FR-P10-V2-04 | Code adoption: tenant adopts ECC or an equivalent passing the 15-Part minimum-content validator | Tenant cannot go live without an adopted code |
| FR-P10-V2-05 | Separation guarantee: a neutral's Chambers plan never affects Equator profile, tier or allocation | Gherkin "Chambers plan never changes Equator allocation" passes |
| FR-P10-V2-06 | Onboarding wizard per §8.4 with "do this later" for non-blocking steps; target go-live ≤ 1 working day for LITE/SOLO | Median time-to-live measured; KYB failures route to manual review |
| FR-P10-V2-07 | Equator Tech Readiness ETR-1…ETR-4, ETR-R in the LMS under `issuing_entity = EQUATOR_RESOLUTION`, free to empanelled neutrals and applicants; ETR-2 live mock observed | Completion emits `equator.neutrals.tech_readiness.completed.v1`; Grade A activation blocked without ETR-2 |
| FR-P10-V2-08 | Tech Concierge role, assignment, scope limits, logging and assisted mode (§10) | Gherkin "Concierge cannot enter a caucus without consent" passes; banner shown to parties |
| FR-P10-V2-09 | Provider picker (≥ 3, alphabetical/randomised, persistent disclosure, no pre-selection) and Institute referral with opaque token behind `academy.institute_referral` = OFF; Appendix O FR-P10-V2-O6 (referral card) is implemented within this requirement | Picker scenarios pass; no PII in referral URLs (DAST check) |
| FR-P10-V2-10 | Credential verification intake from any provider (verify endpoint or Verifiable Credential), minimised payload, nightly revocation polling | Payload with scores/recordings rejected; revocation removes eligibility ≤ 5 minutes |
| FR-P10-V2-11 | Academy and Institute copy compliance: certificates and catalogue never say "IMI accredited/certified course", "QAP" or "Grade A/B" course names; ECM-B described as IMI-recognised only if it is the IMI RMTP programme | Claims-lint passes on all academy templates; Institute course names mapped to "Advanced Practitioner"/"Senior Practitioner Refresher" in any Equator surface |
| FR-P10-V2-12 | Specialisation tracks and country add-ons catalogue (§9.3–§9.4) with hours, assessment and CPD; Institute courses accepted only when hours are published and assessed | Catalogue objects versioned; add-on quiz ≥ 80% grants `CTY-*` for 2 years |
| FR-P10-V2-13 | Close P10 OI-12 with the entity reconciliation in App. N §9.1 (Equa Trainings / Infrabyx Consultancy (OPC) Private Limited vs "Equator ADR Institute"): legal entity, GSTIN, merchant account, privacy notice | Referral flag cannot be switched ON while `institute.entity_reconciled` = false |
| FR-P10-V2-14 | IMI QAP readiness pack (§4.10) prepared by Ops with Registrar; EQAP public page `/neutrals/assessment` with fees, rubric, re-sit rules, calendar, non-discrimination statement | Page published; wording matches `CLM-EQAP-STATUS` |

**Exit gate additions:** a CH-LITE tenant goes from sign-up to first simulated matter in one session; ETR-2 mock observed and recorded for 3 seeded Grade A neutrals; provider picker audit over 1,000 sessions shows no Institute-first bias.
