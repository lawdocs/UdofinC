# Appendix K — Dispute Explorer v2 and Dispute-Type Plug-in Framework

> **Binding for** P02 (Explorer v2, exclusion engine, result types, form resolution, pack registry), P04 (pre-litigation proceedings), P07 (invitation cadence), P08 (vertical question trees plug into §2), P09 (portfolio protocols, ecosystem connectors), P11 (`intake_assistant` v2), P13 (public Explorer pages, expansion landing pages). **Read with** master §3 (NN-01, NN-02, NN-06, NN-12, NN-20, NN-21, NN-24, NN-27, NN-29), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-04, R-05, R-09, R-11, R-13; D2-01, D2-03, D2-04, D2-18), Appendices A, B, C, E, F, G and V1–V6 §5 and §8. Version 2.0, 21 October 2026. Law stated as at 21 October 2026.

---

## 0. Scope, precedence and conventions

**What this appendix specifies.** (1) The Dispute Explorer v2: the free, anonymous, pre-litigation front door that tells a person whether alternative dispute resolution (ADR) suits their dispute, and if not, where to go instead. (2) The exclusions and signposting engine. (3) The result types and the Readiness & Pathway Report v2, and the rule that resolves which form a user sees. (4) The cross-vertical pre-litigation mediation and conciliation product. (5) The dispute-type plug-in framework that lets Equator add new dispute types as configuration. (6) An expansion catalogue of sixteen further dispute types with suitability notes and law.

**Precedence.** Master prompt → Appendix G (any legal rule) → this appendix (Explorer flow, exclusions, result types, form resolution, pre-litigation product, pack framework) → V1–V6 §5 (vertical question content) and §8 (vertical pre-litigation overrides) → P02 v1 text. Where P02 v1 (FR-P02-01 to FR-P02-06) and this appendix differ, this appendix supersedes P02 v1 and the P02 v2 addendum at the end of this file is the build instruction.

**Legend.** [V] verified in the v2 research or the verification log · [K] settled law, not re-fetched · **[VERIFY — open: reason]** unverified; the dependent rule enters Appendix G with `verification = VERIFY_PENDING` and follows the G.1 fail-safe principle (protective rules may activate; permissive rules may not).

**ID scheme.**

| Prefix | Meaning | Owner |
|---|---|---|
| `EXU-nn` | Universal Explorer question | This appendix §2 |
| `EXV-<VERT>-<L1>-Qnn` | Vertical question (e.g. `EXV-FIN-PL-Q03`) | V1–V6 §5 |
| `EXC-nn` | Exclusion register entry | §3 |
| `URG-nn` | Urgent / safety trigger | §3 |
| `RES-nn` | Explorer result type | §4 |
| `PL-*` | Pre-litigation product element (state, cadence, KPI) | §5 |
| `PK-<CODE>` | Dispute pack (plug-in) | §6–§7 |
| `K-D-nn` | Decision recorded in this appendix | §0.1 |
| `LR-EXCL-nnn`, `LR-XPN-nnn` | New Appendix G rule areas created by this appendix | §8.6 |

### 0.1 Decisions recorded in this appendix

| ID | Decision | Reason |
|---|---|---|
| K-D-01 | Universal page order puts **safety and criminal-element questions before** the other-side, contract, value and time questions | GOV.UK "eligibility first"; collect the least data before a hard stop; FAM-G-01, WP-G-03 |
| K-D-02 | Explorer v2 is **one question per page** for individuals and respondents; a task list for business users with documents ready (S9 §5.2 rule) | GOV.UK question pages; WCAG 2.2 AA (NN-23) |
| K-D-03 | Quick exit target becomes configurable `explorer.quick_exit_url`, default `https://www.google.co.in/` (an external neutral page), superseding P02 FR-P02-01's `/` | Returning to Equator's home page is not neutral for a person at risk |
| K-D-04 | Criminal matters are classified three ways: **exclude** (non-compoundable, sexual, POCSO, triple talaq, dowry, threats), **split** (compoundable offence with a civil/money dimension — only the civil part is mediated; the court alone compounds, withdraws or quashes), **parallel-aware** (FIR exists but the dispute is civil) | NN-24; D2-04 |
| K-D-05 | Every result is one of nine **result types** (RES-01…RES-09) with fixed precedence; a matter can be "partly suitable" and the report says which part goes where | Honest signposting (NN-20); avoids all-or-nothing refusals |
| K-D-06 | Form resolution is a **deterministic, specificity-ranked binding lookup** over (vertical, L2 subtype, mechanism, party role, jurisdiction, purpose) inside the pinned ruleset version; ambiguous bindings are rejected at publish time, never at run time | R-04; NN-21 |
| K-D-07 | Pre-litigation default mechanism: **A&C Part III conciliation** where the respondent is an organisation and an enforceable outcome is wanted; contractual mediation otherwise | s.73/s.74 is the strongest lawful pre-suit output today (S4 B1; M-06) |
| K-D-08 | New dispute types are **dispute packs** (config packages) hosted either in an existing vertical or in one new extension vertical code `XPN` with a pack-level case code; mechanism guardrails of `XPN` default to the most restrictive set | R-05 without code changes; master §6 guardrails |
| K-D-09 | No Explorer output ever contains a merits view, viability band, likely outcome or value — including for "suitable" results; "suitable" means *the process can be used*, never *you will win or settle* | NN-01; GX-1/2/3 |
| K-D-10 | The Explorer never states or implies that Equator mediation pauses limitation; it shows dates to watch and the standstill option only where counsel has cleared it (flag OFF) | S4 finding 10; IN-G-06; counsel question Q-C1 |

---

## 1. Dispute Explorer v2 — purpose and principles

### 1.1 Purpose

The Explorer helps a person **before any case exists** to answer four questions in plain language, in under five minutes for most matters:

1. *What kind of dispute is this?* (classification into vertical → L1 → L2, confirmed by the user)
2. *Is anyone in danger, or does this need the police or a court first?* (urgent and safety triggers; exclusions)
3. *Which free or statutory places can help, and by when must I act?* (signposting with last date to act — NN-20)
4. *Can mediation, conciliation, negotiation or arbitration help, what would it involve, what does it cost and how long does it take?* (route options from the deterministic engine — NN-01)

It then offers one clear next step: invite the other side, file, go to the free forum, download a letter, talk to a person, save, or stop.

**Users.** (a) Individuals and small businesses with a problem; (b) respondents who received an Equator notice or a demand from someone else; (c) representatives (family member, advocate, HR officer, CA/CS, company officer); (d) businesses (claimant or respondent side). Enterprise bulk intake does not use the Explorer (P09).

### 1.2 Principles (each is a build rule with a test)

| # | Principle | Build rule | Test (Appendix I / §9) |
|---|---|---|---|
| EP-01 | **Information, not advice** | No merits, odds, value, range or "should" on the merits. The words "strong", "weak", "good case", "likely", "chance", "worth", "you will get" are blocked by copy-lint in every Explorer string and by the GX-1/2/3 output filter | `NN-01_explorer_*`, K-AT-01 |
| EP-02 | **Deterministic core** | Routes, exclusions, clocks, signposting and fees come only from `packages/rules` tools; the AI classifies and restates. With AI off, the questionnaire gives identical results | `NN-02_parity_*`, K-AT-03 |
| EP-03 | **Free and statutory forums first** | The report lists free/statutory forums **above** Equator options whenever the router returns any; each with its last date to act | `NN-20_*`, K-AT-08 |
| EP-04 | **Plain language** | English copy at or below Flesch–Kincaid grade 8; ≤ 20 words per sentence; legal terms behind a glossary pop-over; Hindi and other locales reviewed by a human for the same reading level (NN-23) | Pack validator VAL-07 |
| EP-05 | **One thing per page** | Question = page heading (`h1`/legend); one primary button "Continue"; "Back" link on every page; optional fields say "(optional)"; date as three fields (day, month, year); amounts with live Indian grouping preview (₹1,27,500) | axe + Playwright, K-AT-14 |
| EP-06 | **Quick exit** | Visible "Leave this page" button on every page; `Esc` twice; replaces location with `explorer.quick_exit_url` via `location.replace`; wipes local state; calls `DELETE /v1/explorer/sessions/{id}`; mandatory on FAM, WRK and any session with a safety cue; never logged with content | K-AT-05 |
| EP-07 | **Save and resume** | "Save and come back later" issues a magic link plus OTP to a contact the user chooses; no account needed; FAM/safety sessions never receive reminders | K-AT-06 |
| EP-08 | **Anonymous start** | No login, no name, no identity document before the route and fee are shown; CAPTCHA and rate limits only | K-AT-07 |
| EP-09 | **Safety interrupts first** | Safety and criminal-element questions come early (K-D-01); a cue anywhere (answer or free text) interrupts the flow (§3.4) | K-AT-04 |
| EP-10 | **Honest about time** | "Dates to watch", never "you are time-barred" or "you are in time"; never "Equator pauses your deadline" (K-D-10) | K-AT-10 |
| EP-11 | **Both sides equal** | A respondent path with the same tools and the same information; nothing in the Explorer favours the side that arrived first | K-AT-12 |
| EP-12 | **No dark patterns** | No countdown timers, no pre-ticked paid options, no confirm-shaming on "Stop" or "Go to the free forum"; the free forum button has equal visual weight to Equator buttons (NN-29; CCPA Dark Patterns Guidelines 2023) | Copy/UX lint |
| EP-13 | **Versioned and pinned** | Every session pins `ruleset_version_id`, `explorer_tree_version_id`, active `dispute_pack_version_id`s and `fee_schedule_version_id` at start; a report always shows them (NN-21) | K-AT-20 |
| EP-14 | **Data minimisation** | Only router-required facts are asked; free text is optional; uploads are used for extraction and discarded unless the user files (P02 FR-P02-02) | `sensitive_data_scan` |

### 1.3 What the Explorer must never do

| Never | Why | Enforcement |
|---|---|---|
| Say whether the user's case is good, bad, strong or weak | NN-01, GX-1 | Copy-lint + output filter (ZT) |
| Predict what any forum, neutral or the other side will do | NN-01, GX-2 | ZT |
| Estimate what a claim, offer or property is worth | NN-01, GX-3 | No valuation tool exists (architectural) |
| Imply Equator is a court, regulator, government body or legal aid authority | GX-4; NN-17 | Copy-lint blocks "court", "decree", "judge", "tribunal" (for Equator), "official", "government-approved" |
| File, send, accept or pay anything for the user | GX-7 | No such tool in the Explorer |
| Ask for Aadhaar number, card details, passwords or OTPs (other than its own OTP) | GX-6; NN-14; NN-31 | Field allow-list |
| Collect POSH complaint content, abuse details beyond a cue code, or health details beyond the category | NN-07; WP-G-04; IN-G-10 | Field allow-list; cue codes only |
| Tell anyone that private mediation stops limitation | IN-G-06; K-D-10 | ZT copy-lint |
| Offer arbitration where the route matrix forbids it | NN-06; master §5.2 | Route absent from returnable set |

### 1.4 Save, resume and anonymous start — specification

| Item | Rule |
|---|---|
| Session token | Signed, opaque, `HttpOnly` cookie on web; SecureStore on mobile; 7-day idle expiry for unsaved sessions (P02 default) |
| Save | User chooses email or mobile; DPDP notice for purpose `explorer_resume` (itemised; consent recorded in `core.consent_records`); magic link valid 30 days, single-device-bound after first use; OTP on resume |
| Resume page | Shows a neutral title "Your saved answers" — never the dispute category in the link preview, email subject or SMS text (FAM-G-07); SMS text: "Your Equator link: {short_url}. It expires on {date}." |
| Safety sessions | If any URG cue or FAM category: save allowed only to a contact the user confirms is safe ("Only use an email or phone that nobody else checks"); no reminders; link expiry 7 days |
| Respondent sessions | Started from a notice link; pre-linked to the notice; resume uses the notice code + OTP to the served contact (P01 FR-P01-13) |
| Anonymous key | `anonymous_key_hash` = HMAC of the session token; no IP stored beyond 24-hour rate-limit window |
| Discard | "Delete my answers" on every page footer; also automatic at expiry; deletion is hard for unsaved, unsubmitted sessions (not a case record) |
| Hand-over to filing | Only after the user confirms; answers map to form fields through `pack.explorer_tree.maps_to` (§6); the user re-confirms pre-filled values on the filing "Check your answers" page (WCAG 3.3.7 redundant entry avoided) |

---

## 2. Universal question flow

### 2.1 Page order and branching overview

```
START (SCR-P02-01: notice + consent + language + Quick exit)
 └─ EXU-01 Who are you in this?
     ├─ respondent ──────────────► Respondent path (§2.5)
     ├─ representative ─► EXU-01A Who are you helping? ─┐
     ├─ business ───────► EXU-01B Is your business raising or answering it? ─┤
     └─ individual claimant ─────────────────────────────┘
 └─ EXU-02 What is it about? (life-area tiles + search)          ── category picker
 └─ EXU-03 Which of these is closest? (L1 list of chosen area)    ── narrows to L1
 └─ EXU-04 Is anyone in danger, or is something urgent?           ── URG interrupt (§3.4)
 └─ EXU-05 Has any of this involved…? (criminal elements)         ── EXC split/exclude (§3.2)
 └─ EXU-06 Who is the other side?
 └─ EXU-07 Where are you, and where are they?
 └─ EXU-08 Is there a written agreement? Does it say how disputes are handled?
 └─ EXU-09 How much money is involved?
 └─ EXU-10 When did this start? (time since dispute → limitation screen)
 └─ EXU-11 Is a case or complaint already going on anywhere?
 └─ EXU-12 What would you like to happen? (optional)
 └─ EXU-13 Tell us in your own words (optional; AI classification suggestion; cue scan)
 └─ VERTICAL TREE  EXV-<VERT>-<L1>-Q01…Qnn  (V1–V6 §5; 2–8 pages)
 └─ CHECK YOUR ANSWERS (SCR-P02-24)
 └─ RESULT + READINESS & PATHWAY REPORT v2 (SCR-P02-03 upgraded; §4)
```

Hard stops: an URG trigger at any page shows the interrupt (§3.4) and offers "Get help now" or "Continue later"; an EXC `exclude` hit after EXU-05 or inside a vertical tree jumps straight to the result page with RES-05 (no further questions asked — data minimisation).

### 2.2 Universal questions — full specification

Every question page carries: heading = question; one-sentence hint; answer control; "Continue"; "Back"; "Leave this page"; "Save and come back later"; "Why are we asking?" disclosure (question protocol text, ≤ 30 words).

| ID | Page heading (en) | Hint | Type | Options (code — label) | Req. | Fact key | Branching / effect | Why we ask (shown) |
|---|---|---|---|---|---|---|---|---|
| EXU-01 | Who are you in this? | Choose the one that fits best. | radio | `claimant_individual` — I have a problem with someone and want it sorted · `respondent` — Someone has a complaint or claim against me · `representative` — I am helping someone else · `business` — I am answering for a business or organisation · `joint` — We both want help to settle this together | Y | `entry_role` | `respondent` → §2.5; `representative` → EXU-01A; `business` → EXU-01B; `joint` → sets `joint_intent=true`, both-party CTA in report | "So we show you the right options for your side." |
| EXU-01A | Who are you helping? | You will need their permission before anything is filed. | radio | `family_member` — A family member or friend · `advocate` — My client (I am an advocate) · `employee_rep` — An employee or worker (I am a union or HR representative) · `company_officer` — My company or employer · `ca_cs` — A client (I am a CA, CS or adviser) · `other` — Someone else | Y | `rep_kind` | Shows NN-27 info: "To act for them, you will need a signed letter of authority (or vakalatnama for advocates)." `advocate` → note that Bar Council enrolment is checked at filing (P01) | "Representatives can only act within the authority the person gives them." |
| EXU-01B | Is your business raising this, or answering it? | — | radio | `raising` — We are raising a complaint or claim · `answering` — Someone has a claim against us · `both` — We want to settle together | Y | `business_side` | `answering` → respondent path with business framing; others continue | — |
| EXU-02 | What is it about? | Pick an area, or search. Examples are shown under each one. | tiles + search | See §2.3 (life-area tiles) | Y | `life_area` | Maps to a vertical or pack; search returns L1/L2 suggestions with the user choosing; "Something else" → EXU-13 then human review | "So we ask only the questions that matter for your kind of problem." |
| EXU-03 | Which of these is closest? | If none fits, choose "Something else". | radio list (from active taxonomy for the area, max 12 shown + "Show more") | L1 codes from V1–V6 §2 and active packs (e.g. FIN: `personal_loan`, `credit_card`, `digital_lending`, `gold_loan`, `vehicle_loan`, `home_loan`, `msme_loan`, `microfinance`, `recovery_conduct`, `cheque_bounce`, `credit_report`, `payment_failure`) | Y | `l1_code` | Loads the vertical tree for that L1 | — |
| EXU-04 | Is anyone in danger, or is something urgent? | Choose all that apply. | checkbox | `danger_now` — Someone is in danger right now · `violence_threats` — There has been violence or threats · `self_harm` — I am thinking of hurting myself · `child_removal` — A child may be taken away or out of India · `child_harm` — A child is being harmed · `elder_harm` — An older person is being harmed or abandoned · `fraud_ongoing` — Money is being taken from me by fraud right now · `deadline_7d` — I must act in the next 7 days (for example an auction, eviction, or a bank guarantee being cashed) · `none` — None of these | Y | `urgent_codes[]` | Any code except `none`/`deadline_7d` → URG interrupt (§3.4). `deadline_7d` → URG-09 banner, flow continues | "Mediation is not the right first step when someone is unsafe. We will show you who can help straight away." |
| EXU-05 | Has any of this involved any of the following? | Choose all that apply. You do not need to give details. | checkbox | `cheque_bounce` — A cheque that bounced · `cheating_forgery` — Cheating, fraud or forged documents · `police_case` — A police complaint or FIR · `dowry` — Demands for dowry · `instant_talaq` — Instant triple talaq (talaq-e-biddat) · `sexual_harassment_work` — Sexual harassment at work · `sexual_offence` — Sexual assault or abuse · `harm_to_child` — Harm to a child · `none` — None of these | Y | `criminal_elements[]` | Evaluated by the exclusion engine (§3.2): `sexual_offence`, `harm_to_child` → exclude + URG; `sexual_harassment_work` → POSH signpost (sealed; no details collected); `dowry`, `instant_talaq` → exclude the offence, offer civil-terms route only where §3.3 allows; `cheque_bounce` → split (NI Act s.147); `cheating_forgery`, `police_case` → parallel-aware note | "Equator does not deal with crimes. Some disputes have a money part we can help with, while the police or court deal with the rest." |
| EXU-06 | Who is the other side? | — | radio | `individual` — A person · `family` — A family member or relative · `employer` — My employer or former employer · `employee` — An employee or worker · `business` — A company, shop or business · `lender` — A bank, NBFC, lending app or microfinance lender · `insurer` — An insurance company, TPA or agent · `builder` — A builder or developer · `landlord_tenant` — A landlord or tenant · `platform` — An online platform or app · `government` — A government department, PSU or public body · `foreign` — A person or business outside India · `unknown` — I do not know who | Y | `other_side_kind` | `lender` with unregistered app → FIN tree asks RE name (PI-FIN-10); `government` → COM DoE track (R-COM-13) or EXC-15/16 check; `foreign` → INT gates (NN-19) or PK-XBE; `unknown` → address-research note, RES-08 if needed | "Some places can only hear complaints against certain kinds of organisations." |
| EXU-07 | Where are you, and where is the other side? | We use this to find the right local office and rules. | 2 selects + optional district | You: 36 States/UTs + `outside_india`. Other side: `same_state` · `other_state` (then select) · `outside_india` (then country, ISO 3166) · `dont_know` | Y | `user_state`, `other_side_location`, `district?` | Drives signposting directory jurisdiction, state stamp/registration blocks, state packs (e.g. MahaRERA card), INT/XBE; `outside_india` user → INT or PK-XBE checks | "Free forums and rules differ from state to state." |
| EXU-08 | Is there a written agreement between you? | For example a loan agreement, policy, offer letter, contract, invoice or WhatsApp messages. | radio + follow-up | `signed_contract` — Yes, a signed agreement · `docs_only` — Only bills, purchase orders or messages · `oral` — No, it was spoken · `none` — There was no agreement · `dont_know` — I am not sure. Follow-up (if any document): "Does it say how disputes must be handled?" `arbitration` · `mediation` · `tiered` (talk first, then mediation or arbitration) · `courts_only` · `no_clause` · `dont_know` (optional upload: extraction only). Follow-up: "Is the relationship still going on?" `ongoing` · `ended` · `never_started` | Y (follow-ups conditional) | `agreement_kind`, `dispute_clause`, `relationship_status` | Arbitration options require `dispute_clause = arbitration` or a post-dispute agreement; unilateral-appointment clause flagged (NN-03); `ongoing` raises mediation priority in the route-ordering rule (never in merits) | "The agreement can decide which process is available." |
| EXU-09 | How much money is involved? | Your best estimate is fine. It does not need to be exact. | radio + optional exact amount | `upto_50k` — Up to ₹50,000 · `50k_3l` — ₹50,001 to ₹3 lakh · `3l_20l` — ₹3 lakh to ₹20 lakh · `20l_50l` — ₹20 lakh to ₹50 lakh · `50l_1cr` — ₹50 lakh to ₹1 crore · `1cr_2cr` — ₹1 crore to ₹2 crore · `2cr_10cr` — ₹2 crore to ₹10 crore · `above_10cr` — More than ₹10 crore · `not_money` — It is not about money · `dont_know` — I do not know. INT/XBE: currency select (INR, USD, EUR, GBP, SGD, AED) with INR equivalent shown | Y | `value_band`, `value_minor?`, `currency` | Thresholds read from Appendix G CFG rules, never hard-coded: ₹3 lakh specified value (Commercial Courts Act 2015 s.2(1)(i) as amended 2018; s.12A PIMS banner), ₹20 lakh RDB Act (DRT), ₹50 lakh / ₹2 crore Consumer Commission tiers (LR-CONS-001), ₹50 lakh Insurance Ombudsman award cap (r.17(3)), ₹1 crore IBC CIRP and PLA limit, ₹10 crore DoE OM (3 Jun 2024). If the band straddles a threshold that matters for the matter, the page asks for the exact amount | "Some forums only hear claims up to a certain amount. This also sets the fee." |
| EXU-10 | When did this start? | Think of the date things went wrong, or the last time they replied or paid. | radio + optional dates (day/month/year fields) | `under_1m` — Less than a month ago · `1m_6m` — 1 to 6 months ago · `6m_1y` — 6 months to a year ago · `1y_2y` — 1 to 2 years ago · `2y_3y` — 2 to 3 years ago · `over_3y` — More than 3 years ago · `dont_know` — I am not sure. Optional exact dates: `cause_date`, `last_ack_or_payment_date`, `last_reply_date` | Y | `time_band`, dates | `screen.limitation(facts)` computes "dates to watch" from Appendix G limitation rules and vertical clocks (§2.4); bands near a limit trigger a request for exact dates | "Many places have a last date to apply. We will show the dates to watch." |
| EXU-11 | Is a case or complaint already going on anywhere? | Choose all that apply. | checkbox | `none` · `civil_court` — A civil or commercial court case · `criminal_court` — A criminal case (including cheque bounce) · `police` — A police complaint or FIR · `consumer` — A consumer commission complaint · `ombudsman` — A banking or insurance ombudsman complaint · `tribunal` — A tribunal (DRT, NCLT, MACT, RERA, labour authority, rent authority, senior citizens tribunal) · `arbitration` — An arbitration · `lok_adalat` — A Lok Adalat · `regulator` — A complaint to a regulator (RBI, IRDAI, SEBI, TRAI and others) · `employer_or_company_grievance` — A grievance with the company or employer · `dont_know` | Y | `pending_forums[]` | Parallel-proceedings rules (§2.4 table): e.g. RB-IOS non-maintainable if a court or arbitrator is seized; Insurance Ombudsman r.14(5) bar; court-pending → court-recording pack; arbitration pending → s.30 settlement inside it | "If a case is already going on, any settlement may need to go back to that court or forum." |
| EXU-12 | What would you like to happen? (optional) | Choose up to three. | checkbox | `payment` — Get paid or get money back · `time_to_pay` — More time or a payment plan · `fix_or_redo` — Get something repaired, replaced or done properly · `stop_behaviour` — Stop calls, messages or behaviour · `documents_release` — Get documents, NOC or property released · `correct_record` — Correct a record (credit report, policy, salary slip) · `exit_agreed` — End the relationship on agreed terms · `arrangement` — Agree an arrangement (care, parenting, use of property) · `apology` — An apology or explanation · `not_sure` | N | `outcomes[]` | Used only to order mechanism explanations and choose templates; never to score merits | "So we can explain which process can deliver that kind of result." |
| EXU-13 | Tell us in your own words (optional) | Do not include bank, card or Aadhaar numbers. | textarea (≤ 1,000 chars) + voice input | — | N | `narrative_enc` (encrypted; discarded at session end unless filed) | `intake_assistant` proposes ≤ 3 classification candidates with confidence; the user picks or keeps EXU-03 answer; cue lexicon + classifier scan → URG; never echoed back verbatim | "Optional. It can help us check we chose the right category." |

**Validation.** Exact amounts: integer minor units, ≥ 0, ≤ ₹10,000 crore; dates: not in the future, not before 1 Jan 1950; "I do not know" is always accepted and produces a conservative rule result (e.g. limitation "check the date with a lawyer or the forum").

### 2.3 Category picker (EXU-02) — life-area tiles, examples and search

| Tile code | Tile label (en) | Examples under the tile (shown) | Maps to | Status |
|---|---|---|---|---|
| `money_loans` | Loans, cards and payments | EMI or loan settlement · recovery agent calls · credit card charges · gold not returned · UPI money stuck · wrong credit report · cheque bounced | FIN | Live |
| `business` | Business and contracts | Unpaid invoice · supplier did not deliver · partner dispute · shareholder or founder dispute · construction bill · software project · franchise | COM | Live |
| `family_property` | Family, marriage and family property | Divorce terms · maintenance · children's arrangements · dividing family property · inheritance · family business split · care of parents | FAM | Live |
| `insurance` | Insurance claims | Health claim rejected or cut · cashless denied · car claim · death claim · policy mis-sold | INS | Live |
| `work` | Job and workplace | Salary or full and final not paid · gratuity · termination · non-compete · gig app deactivation · ESOP | WRK | Live |
| `cross_border` | Business across borders | Foreign buyer or seller · export or import contract · overseas partner · international project | INT | Live |
| `home_housing` | Home, rent and housing society | Flat possession delay · deposit not returned · rent · society or RWA charges · neighbour problems | COM.RE + PK-TEN, PK-COP, PK-CMY | Live for COM.RE; packs per §7 |
| `shopping_services` | Shopping, online orders and services | Online order or refund · phone or internet bill · hospital bill · course fee refund | PK-CNS, PK-HLT, PK-EDU | Pack-gated (shown only when the pack is published) |
| `something_else` | Something else | — | Free text → classification suggestion → human review if unresolved | Live |

**Search.** Deterministic synonym index `core.explorer_synonyms` (locale, term, target L1/L2 codes, weight), not the LLM. Includes Hindi and common Hinglish terms (e.g. "EMI", "loan settle", "salary nahi mila", "gratuity", "talaq", "batwara", "virasat", "claim reject", "builder possession", "kiraya"). Results show at most 6 matches with the life-area label; zero results → "Try different words" + "Something else". Typo tolerance: trigram similarity ≥ 0.4. Search terms are not logged with session IDs; aggregated zero-result terms feed the taxonomy backlog weekly.

### 2.4 Rule tables used by the universal flow

**Limitation screen (`screen.limitation`) — representative anchors** (full list in Appendix G; vertical clocks in V1–V6 §3).

| Anchor | Period | Source | Shown as |
|---|---|---|---|
| Contract / money suits | 3 years | Limitation Act 1963 Sch. Arts. 55, 113 [K] | "Dates to watch: about {date} for a court claim — confirm with a lawyer" |
| Applications incl. IBC ss.7/9 | 3 years from default | Limitation Act Art. 137; *B.K. Educational Services v Parag Gupta* (2019) 11 SCC 633 [K] | Same pattern |
| Consumer complaint | 2 years (condonable) | CPA 2019 s.69 (LR-CONS-002) | "Consumer Commission: file by about {date}" |
| Cheque dishonour | Notice within 30 days of return memo; 15 days to pay; complaint within 1 month | NI Act 1881 s.138(b)–(c), s.142(1)(b) [K] | Three dated pills |
| Insurance Ombudsman | 1 year from insurer's reply (calendar year; condonable r.14(4)) | Insurance Ombudsman Rules 2017 r.14(3)–(4) [V] | "needs condonation" state after expiry, never "ineligible" |
| RBI Ombudsman | 30 days after complaint to RE, then within 90 days | RB-IOS 2026 (master X-13; `LR-RBI-*`) [V] | Two pills |
| Wage claims | 3 years (condonable) | Code on Wages 2019 s.45 [V] | Pill |
| GRC (IR Code) | 1 year | IR Code 2020 s.4 [V] | Pill |
| POSH complaint | 3 months from last incident (+3 months for recorded reasons) | POSH Act 2013 s.9 [V] | Pill (sealed route only) |
| Motor accident claim | 6 months | MV Act 1988 s.166(3) [K]; Supreme Court direction not to reject for delay **[VERIFY — open: order date in *ICICI Lombard v Ayiti Navaneetha*]** | Pill + note shown only after verification |
| SARFAESI appeal to DRT | 45 days | SARFAESI Act 2002 s.17(1) [K] | Pill |
| Challenge to arbitral award | 3 months + 30 days | A&C Act 1996 s.34(3) [K] | Pill (post-award only) |

Fixed copy below every limitation block: "Private mediation or conciliation does **not** stop these dates running. If a date is close, think about protecting your position first (for example by filing, or by asking a lawyer)." Exception copy appears only where a rule applies: the s.12A PIMS period is excluded from limitation (Commercial Courts Act s.12A(3)); limitation does not apply to MSEFC conciliation under MSMED s.18(2) (*Sonali Power Equipments*, 2025 INSC 864 [V]).

**Parallel-proceedings rules (`screen.parallel`).**

| Pending forum (EXU-11) | Effect | Copy |
|---|---|---|
| `civil_court` | Mediation allowed; output = court recording pack (CPC O.XXIII r.3 compromise) or s.89 referral note | "If you settle, the court will need to record it." |
| `criminal_court` with cheque bounce | Split: civil settlement + s.147 compounding pack; cost slabs per *Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158 [V] | "Only the court can close the cheque case." |
| `police` | Parallel-aware: civil part only; no Equator contact about the criminal complaint | "We cannot help with the police complaint itself." |
| `ombudsman` (RBI/insurance) | Equator conciliation/mediation not offered while the Ombudsman is seized unless both parties ask; Ombudsman route shown first | "The Ombudsman is free and already has your complaint." |
| `consumer` | Mediation allowed only with the Commission's knowledge; settlement to be placed before the Commission | "Any settlement should be filed with the Commission." |
| `arbitration` | Mediation inside arbitration (consent award s.30) only with the tribunal's knowledge | — |
| `tribunal` (DRT, NCLT, MACT, RERA, labour, rent, senior citizens) | Signpost the tribunal as decision-maker; ADR only for settlement terms to be recorded there; NCLT IBC rules per R-COM-04 to R-COM-07 | "This tribunal decides. A settlement can be taken to it." |
| `lok_adalat` | Signpost; Equator may prepare terms only | — |

**Arbitration gate (`screen.arbitrability`).** Arbitration appears as an option only if all hold: (1) mechanism permitted for the vertical/L2 (master §5.2; V §2 table); (2) `dispute_clause = arbitration` or a post-dispute arbitration agreement is available; (3) no EXC entry with `blocks_arbitration = true`; (4) the party is not a retail policyholder, consumer under an adhesion clause, IR Code "worker" for termination, or borrower under a unilateral-appointment clause without a valid post-dispute agreement (NN-03, NN-06). Output labels: `arbitrable` / `not_arbitrable` / `doubtful` (shown as "screening flag, not a determination — an arbitral tribunal rules on its own jurisdiction (A&C Act 1996 s.16)").

### 2.5 Respondent, representative and business paths

**Respondent path** (BC CRT "a claim was made against you" pattern; S9 §5.2).

| Page | Heading | Options |
|---|---|---|
| EXU-R1 | Did you get a notice or message about this? | `equator_notice` — Yes, from Equator (enter or scan the code) · `other_notice` — Yes, from someone else (lawyer, bank, company) · `no_notice` — No, I just know there is a problem |
| EXU-R2 (Equator notice) | Is this about you? | `yes` · `not_me` — This is not about me / wrong person · `not_sure` |
| EXU-R3 | What do you want to do? | `respond` — Reply and take part · `more_time` — Ask for more time (once, ≤ 14 days) · `ask_question` — Ask a question first · `free_forum` — See other places that can deal with this · `decline` — I do not want to take part · `not_involved` — Tell you I was not involved |
| then | EXU-04, EXU-05, EXU-11 (safety, criminal, parallel) | as §2.2 |

`not_me` / `not_involved` → identity-mismatch workflow (case manager task, 2 working days; no further contact until resolved). `decline` → private optional reason (sealed; never shown to the claimant) and the non-commencement path (§5). A respondent who received a non-Equator demand continues through the universal flow from EXU-02 with `entry_role = respondent`, and the report shows the respondent options for that L1 (e.g. "If a lender is calling you outside 08:00–19:00, you can complain to the lender's grievance officer, then the RBI Ombudsman").

**Representative path.** After EXU-01A the flow is the universal flow in the third person ("Who is the other side?" becomes "Who is the other side in their dispute?"). The report adds an "Authority you will need" block: Letter of Authority (non-advocate) or vakalatnama (advocate), scope flags (file, respond, attend, settle up to a limit, receive notices, sign), and the party's own e-sign above the settlement limit (NN-27; App. S §4). Non-advocate representation is shown only where the mechanism's rules allow it (D2-24).

**Business path.** For `business` with `raising`, after EXU-03 the user may switch to the **task-list intake** (Parties · Dispute details · Claim and relief · Documents · Fees · Declarations) instead of one-question pages (K-D-02). Extra fields: entity type, CIN/LLPIN/GSTIN/Udyam (optional at Explorer stage; verified at filing), and the Udyam micro/small check that triggers the MSEFC signpost (CM-G-03; R-COM-09).

### 2.6 Hand-off to vertical trees (contract for V1–V6 §5)

Each V file §5 defines, per L1: question IDs `EXV-<VERT>-<L1>-Qnn`, text (≤ class 8), options with codes, branching, outcome codes and free-forum disclosures. To plug into this flow every vertical tree must:

1. Start only after EXU-13 and end at "Check your answers".
2. Read universal facts (never re-ask `entry_role`, `other_side_kind`, `user_state`, `value_band`, `time_band`, `pending_forums`, `criminal_elements`).
3. Emit facts in the pack's fact schema (`facts.<vert>.*`) used by the vertical rule pack.
4. Use only these outcome hooks: `exclude(EXC-code)`, `split(EXC-code, civil_route)`, `urgent(URG-code)`, `free_forum_first(forum_code)`, `condition(code)` (e.g. `needs_safety_screening`, `needs_arbitration_agreement`, `needs_authority`, `needs_court_recording`, `needs_regime_review`), `human_review(reason)`.
5. Ask ≤ 8 pages per L1 in the 80th-percentile path (pack validator VAL-09).
6. Ship EN and HI text and a golden fact-set file (≥ 20 sets per L1) for parity tests.

The vertical rule pack, not the tree, decides the result. Trees only collect facts.

---

## 3. Exclusions and signposting engine

### 3.1 Evaluation order (deterministic, in `packages/rules/exclusions`)

```
evaluate(facts, rulesetVersion):
  1. URGENT   — any URG trigger from EXU-04, EXU-05, vertical tree or cue scan  → RES-06 (interrupt; §3.4)
  2. EXCLUDE  — any EXC entry with behaviour = exclude                         → RES-05 for that matter
  3. SPLIT    — any EXC entry with behaviour = split                           → RES-03 (civil part continues)
  4. FREE-FIRST — rule pack returns a forum with must_approach_first or free_and_equivalent → RES-04
  5. CONDITIONS — rule pack conditions (safety screening, authority, agreement, court recording) → RES-02
  6. ADR      — otherwise                                                       → RES-01
  overlays: low confidence / regime conflict / customary law / unknown other side → RES-08 flag
  always: signposting.lookup() for every forum named; each naming writes a signposting event (NN-20)
```

Every hit returns `{exc_code, behaviour, reason_code, legal_rule_ids[], forum_codes[], ldta: {rule_id, date|null, basis_text}, blocks_arbitration, blocks_mediation, civil_route?}`. The engine is total: every fact set yields at least one forum or route ("never declined without a route", FR-P02-20).

**Behaviours.**

| Behaviour | Meaning | UI |
|---|---|---|
| `exclude` | Equator will not undertake any process on this matter (or this part) | RES-05 card: "Equator cannot help with this. Here is who can." Forum cards first; no Equator fee shown |
| `split` | Equator can help only with the civil/money part; another forum deals with the rest | RES-03 card: two columns "What Equator can help with" / "What only {forum} can do" |
| `arbitration_blocked` | Mediation/conciliation/negotiation allowed; arbitration never offered | Route card shows arbitration as unavailable with reason |
| `signpost_first` | A free or statutory forum should normally be approached first or in parallel | RES-04 card; Equator option shown second with "You can still use Equator alongside, if both sides agree" where lawful |

### 3.2 Exclusion register (full list of matters Equator does not undertake)

Forum codes refer to `core.signposting_directory` (FR-P02-22; new codes marked ⁺ are added by this appendix). "Last date to act" (LDTA) is computed from the cited rule where one exists; otherwise the fixed text shown.

| Code | Matter | Law / reason | Behaviour | Forum (code) and link | Last date to act |
|---|---|---|---|---|---|
| EXC-01 | Non-compoundable offences (any offence not listed as compoundable in BNSS 2023 s.359) | NN-24; Mediation Act 2023 First Schedule item 3 (policy mirror; Schedule not in force for this purpose) [V RES_A1a Q03] | exclude | Police (`police`): 112 / State police e-FIR portal; Magistrate (`magistrate`⁺) | "Report as soon as possible." For petty offences, courts may take cognizance only within the periods in BNSS s.514 [K] **[VERIFY — open: confirm BNSS section numbering for limitation on cognizance]** |
| EXC-02 | Sexual offences against any person, and any offence under the POCSO Act 2012 | NN-24; BNS 2023 Chapter V [K]; POCSO Act 2012 s.19 (mandatory reporting), s.21 (penalty) [K] | exclude + URG-04 | Police 112; Childline 1098 [K]; NCW (`ncw`⁺) ncw.nic.in | "Act now." No Equator contact with the other side |
| EXC-03 | Instant triple talaq (talaq-e-biddat) — recording, drafting or facilitating it | Muslim Women (Protection of Rights on Marriage) Act 2019 ss.3–4, 7 [V S1 §2] | exclude the talaq; split for civil consequences (mahr, s.5 subsistence allowance, s.6 custody, return of goods) — FAM tree only, at the wife's request, with safety screening | Magistrate (`magistrate`⁺); Family Court (`family_court`) | — (offence is compoundable only at the wife's instance with the Magistrate's permission, s.7(b)) |
| EXC-04 | Dowry offences, dowry death, cruelty | Dowry Prohibition Act 1961 ss.3–4 [K]; BNS 2023 ss.80, 85 [K] (non-compoundable; quashing only by the High Court — *Gian Singh v State of Punjab* (2012) 10 SCC 303 [V RES_A1a Q23]) | exclude the offence; split for civil terms (streedhan return, maintenance, residence) only on the aggrieved woman's request after safety screening (PWDV Rules 2006 r.14 safeguards adopted as policy, S1 §5) | Police 112; Protection Officer (`protection_officer`); Family Court | "Act now." |
| EXC-05 | Threats, violence, stalking, intimidation, criminal coercion (including by recovery agents) | NN-24; FL-G-02; WP-G-03 | exclude the conduct + URG-01/06; a civil money dispute between the same parties may continue later only with a shuttle format and safety plan | Police 112; for regulated lenders also the RE's grievance officer and the RBI Ombudsman (`rbi_ios`) | "Act now." |
| EXC-06 | Matters needing urgent police or court protection first (protection orders, injunctions, stay of auction/sale/eviction, freezing orders, habeas corpus) | NN-24; ADR cannot compel or restrain | signpost_first (URG-09); Equator may run in parallel later; emergency arbitrator only for arbitrable commercial matters with an arbitration agreement (Equator Rules) | Civil court / Commercial Court (`civil_court`, `commercial_court`⁺); DRT for SARFAESI (`drt`); High Court (`high_court`⁺); A&C s.9 court | Computed where a clock exists (e.g. SARFAESI s.17: 45 days) |
| EXC-07 | Compoundable offences with a civil/money dimension: NI Act s.138 (compoundable, s.147); MW(PRM) Act s.4 (s.7(b)); offences compoundable under BNSS s.359 | NN-24; D2-04 | split — Equator mediates the money/civil terms only; prepares the compounding/withdrawal papers; **the court alone decides** | Magistrate / trial court (`magistrate`⁺); Lok Adalat (`lok_adalat`) | NI Act clocks (30 days / 15 days / 1 month); compounding cost by stage (*Sanjabij Tari*, 2025 INSC 1158 [V]) |
| EXC-08 | Matrimonial status: divorce decree, nullity, judicial separation, restitution of conjugal rights | NN-06; *Booz Allen & Hamilton v SBI Home Finance* (2011) 5 SCC 532 para 36 [K] | arbitration_blocked; mediation/conciliation of **terms** allowed; the decree comes from the Family Court | Family Court (`family_court`); Parsi Matrimonial Court where applicable | Regime-specific (e.g. HMA 1955 s.13B: one year's separation; second motion after the statutory period unless waived — *Amardeep Singh v Harveen Kaur* (2017) 8 SCC 746 [K]) |
| EXC-09 | Custody and guardianship decisions | NN-06; *Booz Allen* para 36; GWA 1890 s.17 [K] | arbitration_blocked; parenting-plan mediation allowed; plan binding only when recorded by the court | Family Court / GWA court; High Court (habeas corpus) | — ; URG-03 if removal risk |
| EXC-10 | Testamentary matters: grant of probate, letters of administration, succession certificates, validity of a will | NN-06; *Booz Allen* para 36 [K]; probate no longer mandatory in Mumbai/Kolkata/Chennai after omission of ISA s.213 (D2-25) **[VERIFY — open: Act number and Gazette reference]** | exclude validity/grant; split — Equator may mediate distribution among heirs, withdrawal of objections or a family settlement *around* the will | District Judge / High Court probate jurisdiction (`probate_court`) | Limitation Act Art. 137 (3 years from when the right to apply accrues) — *Kunvarjeet Singh Khandpur v Kirandeep Kaur* (2008) 8 SCC 463 [K] |
| EXC-11 | Insolvency adjudication: CIRP admission, moratorium, resolution plans, liquidation, personal insolvency orders | NN-06; *Vidya Drolia v Durga Trading Corpn* (2021) 2 SCC 1 [K]; *Indus Biotech v Kotak India Venture* (2021) 6 SCC 436 [K]; IBC 2016 s.14 | exclude adjudication; split — pre-admission settlement, s.12A IBC withdrawal settlement support within the 2026 window (D2-02), out-of-court workouts | NCLT (`nclt`) efiling.nclt.gov.in; NCLAT; IBBI | Art. 137: 3 years from default [K]; IBC s.12A window clocks (S2 §6) |
| EXC-12 | Statutory company reliefs: oppression and mismanagement (CA 2013 ss.241–242), winding up (s.271), schemes (ss.230–232), LLP winding up | *Haryana Telecom v Sterlite* (1999) 5 SCC 688 [V-sec]; *Rakesh Malhotra* (Bom HC 2014) [V-sec] | split — arbitration of shareholder-agreement claims and mediation of the whole dispute allowed; statutory reliefs only by NCLT; s.442 panel mediation only by individually empanelled neutrals on reference | NCLT (`nclt`); MCA Regional Director (`mca_rd`⁺) | — |
| EXC-13 | Rights in rem and registry actions: grant, revocation or rectification of patents, trade marks, designs, copyright registration; declarations of title against Government or with effect in rem | *Vidya Drolia* [K]; Mediation Act First Schedule item 2 (policy mirror) [V] | exclude registry/in rem relief; licence, royalty and assignment disputes continue (COM.TECH) | IP Office (`ipo`) ipindia.gov.in; High Court IP Division; civil court | — |
| EXC-14 | Tax: levy, assessment, collection, penalties, prosecutions (direct and indirect) | Mediation Act First Schedule item 7 [V] | exclude | Income-tax appellate authorities (`it_appeal`⁺); GST appellate authority (`gst_appeal`⁺) under CGST Act 2017 s.107 (3 months, +1 month condonable) [K]; customs | Income-tax appeal period **[VERIFY — open: Income-tax Act 2025 section and period for first appeal]**; GST: 3 months from communication of the order [K] |
| EXC-15 | Constitutional and public-law remedies: fundamental rights, writs against the State, public-interest litigation | Arts. 32, 226 Constitution of India [K] | exclude | High Court (`high_court`⁺); Supreme Court | No fixed period; delay and laches apply — "act promptly" |
| EXC-16 | Government service matters of public servants | Administrative Tribunals Act 1985 s.21 (1 year) [K] | exclude | CAT / State Administrative Tribunal (`cat`⁺) | 1 year from final order (s.21) [K] |
| EXC-17 | Elections, citizenship, immigration, RTI, public-records correction | RP Act 1951 s.81 (45 days) [K]; RTI Act 2005 s.19(1) (30 days first appeal) [K] | exclude | High Court (election petitions); CIC/SIC (`rti_commission`⁺); Bureau of Immigration/FRRO | Computed from the cited sections |
| EXC-18 | Consumer reliefs only a Commission or the CCPA can grant: product-liability action (CPA 2019 Chapter VI), punitive damages, class or representative complaints (s.35(1)(c)), recalls and action on unfair trade practices or misleading advertisements (CCPA, ss.18–21) | CPA 2019 [K]; LR-CONS-003/004 | split — Equator may mediate an individual refund/repair/compensation with a willing business; statutory reliefs only via the Commission/CCPA; never presented as mandatory before filing (*Emaar MGF*, LR-CONS-003) | Consumer Commission (`consumer_district`/`consumer_state`/`ncdrc`) via e-Jagriti (`e_jagriti`) e-jagriti.gov.in; National Consumer Helpline 1915 / WhatsApp 8800001915 (`nch`⁺) [V S4 B2.4]; CCPA | 2 years from cause of action (CPA s.69; LR-CONS-002) |
| EXC-19 | Medical negligence causing death or grievous hurt, in consumer-mediation terms; criminal medical negligence; professional discipline of doctors | CP (Mediation) Rules 2020 r.4 (LR-CONS-004); BNS 2023 s.106(1) [K]; *Jacob Mathew v State of Punjab* (2005) 6 SCC 1 [K]; NMC Act 2019 / State Medical Councils [K] | exclude criminal and disciplinary parts; split — civil compensation or billing may be mediated only by consent, with health data sealed (NN-07), human review and an independent-advice prompt (PK-HLT) | Consumer Commission; State Medical Council (`smc`⁺); police | CPA s.69: 2 years |
| EXC-20 | Third-party motor accident compensation adjudication | MV Act 1988 ss.165–166, 175 (civil courts barred) [K]; s.149 insurer settlement offer [V S4 B2.8] | exclude adjudication; Equator may prepare a quantum brief for a MACT-recorded compromise or MACT Lok Adalat; minors' claims need court sanction (CPC O.XXXII r.7) [K]; no Equator award | MACT (`mact`); DLSA (`dlsa_pims` / `lok_adalat`) | s.166(3): 6 months [K] (note on SC direction shown only after verification — see §2.4) |
| EXC-21 | Statutory labour benefits and worker-termination adjudication: minimum/statutory wages, deductions, equal pay, statutory bonus, gratuity, PF, ESI, employees' compensation; reinstatement of an IR Code "worker" | Code on Wages 2019 ss.45, 57 [V]; CoSS 2020 ss.23, 58, Ch. VII [V]; IR Code 2020 ss.2(zs), 4, 53 [V]; S4 A1.2 `wrk_arbitrability()` | arbitration_blocked for statutory components and worker termination; mediation allowed **without any waiver below the statutory floor** (HB-WRK-FLOOR-01); IR Code settlement conversion for workers | CoW claims authority (`cow_claims`⁺); gratuity competent authority (`gratuity_ca`⁺); EPFO (`epfo`⁺, EPFiGMS); ESI Court; GRC (`grc_ir_code`); conciliation officer (`labour_conciliation_officer`); Industrial Tribunal | WC-03 (3 years), WC-05 (1 year), WC-07 (60 days), WC-10 (90 days) per S4 A2 |
| EXC-22 | POSH complaints (sexual harassment at the workplace) | POSH Act 2013 ss.4, 6, 9–13; NN-07; WP-G-01/02/04 | exclude from core and from AI; Explorer collects **no details**; signposts the employer's Internal Committee or the district Local Committee; s.10 conciliation only at the aggrieved woman's written request and never on a monetary basis (in the sealed POSH module, for employers) | IC of the employer (`ic_posh`); Local Committee (`lc_posh`); She-Box **[VERIFY — open: current She-Box URL and status]**; police 112 if danger | POSH s.9: 3 months from last incident (+3 months) |
| EXC-23 | Bank/financial-institution debt recovery ≥ ₹20 lakh adjudication; SARFAESI enforcement measures | RDB Act 1993 ss.17–18 [K]; SARFAESI Act 2002 s.17 [K]; *Vidya Drolia* [K] | arbitration_blocked (bank/FI claimant); OTS/compromise mediation and conciliation allowed (FIN) | DRT (`drt`); DRAT | SARFAESI s.17: 45 days from the measure [K] |
| EXC-24 | Proceedings before sector regulators and specialised tribunals: CCI/DG; SEBI/SAT; TRAI/TDSAT; Electricity Regulatory Commissions/APTEL; PNGRB; NGT; land acquisition and compensation | Mediation Act First Schedule items 6, 8–12 [V]; Competition Act 2002 s.61 [K] | exclude regulatory proceedings; private contract layer may continue (e.g. distributor termination) | CCI (`cci`⁺); SEBI SCORES (`sebi_scores`⁺); TDSAT; Electricity Ombudsman/Commission; NGT; Land Acquisition Authority | Per forum rules (shown when a rule exists) |
| EXC-25 | Professional disciplinary complaints (advocates, doctors, chartered accountants, company secretaries and others before statutory bodies) | Mediation Act First Schedule item 4 (policy mirror) [V]; Advocates Act 1961 s.35 [K] | exclude | State Bar Council (`bar_council`⁺); State Medical Council (`smc`⁺); ICAI / ICSI | — |
| EXC-26 | Claims by or against minors, persons with mental illness, persons of unsound mind or with high-support-needs disability, or deities, without a court-appointed guardian or next friend | Mediation Act First Schedule item 2 (policy mirror) [V]; CPC O.XXXII rr.1–7 [K]; HMGA 1956 s.8(2) [V RES_A1a Q23] | exclude unless a lawful guardian acts and court sanction will be obtained for any compromise; then condition `needs_court_sanction` | Civil / Family Court | — |
| EXC-27 | Eviction and standard rent of tenancies protected by a State rent-control law | *Vidya Drolia* (overruling *Himangni Enterprises*) [K] | arbitration_blocked; mediation allowed; Rent Controller decides | Rent Controller / Rent Authority (`rent_authority`⁺) | State law **[VERIFY — open: per-State rent law table]** |
| EXC-28 | Disputes assigned by statute to an exclusive co-operative forum | e.g. Maharashtra Co-operative Societies Act 1960 s.91 [K]; Multi-State Co-operative Societies Act 2002 s.84 [K] | arbitration_blocked unless the statute or bye-laws permit Equator; mediation by consent allowed | Co-operative Court / Registrar (`coop_registrar`⁺) | State law |
| EXC-29 | Waqf property and religious-endowment disputes assigned to statutory tribunals | Waqf Act 1995 s.83 [K] (as amended by the Waqf (Amendment) Act 2025 **[VERIFY — open: amendment commencement and effect on s.83]**); State endowment Acts | exclude adjudication; mediation of private family arrangements only where no statutory bar | Waqf Tribunal (`waqf_tribunal`⁺); State endowment authority | — |
| EXC-30 | Senior-citizen Tribunal reliefs (maintenance orders, voiding of transfers under s.23) | MWPSC Act 2007 ss.5, 6(6), 23, 27 [V S1 §8] | arbitration_blocked; conciliation allowed (including as Tribunal-nominated conciliator under s.6(6)) | Maintenance Tribunal (`senior_citizens_tribunal`); Elderline 14567 [K] | s.5(4): Tribunal disposal 90 days (+30) — informational |
| EXC-31 | Domestic-violence protection, residence and monetary-relief orders | PWDVA 2005 ss.18–23 [K]; PWDV Rules 2006 rr.13–14 [V S1 §5] | exclude the orders (Magistrate only); DV-adjacent mediation only if the aggrieved person asks, after screening, shuttle only, with a non-recurrence undertaking | Protection Officer (`protection_officer`); Magistrate; 181 Women Helpline [K]; One Stop Centre [K] | — ; URG-02 |
| EXC-32 | Adoption, surrogacy and assisted reproduction status, appointment of guardians | JJ Act 2015 Chapter VIII [K]; Surrogacy (Regulation) Act 2021 [K]; GWA 1890 [K] | exclude | District Magistrate / court; CARA (`cara`⁺) | — |
| EXC-33 | Debts claimed by unregistered or illegal lending apps, unregulated deposit schemes, chit or Ponzi schemes | PI-FIN-10; Banning of Unregulated Deposit Schemes Act 2019 [K] | exclude the "debt" mediation; signpost | Cybercrime 1930 / cybercrime.gov.in [V]; police; RBI Sachet (`sachet`⁺) sachet.rbi.org.in [K]; BUDS Competent Authority | "Act now." |
| EXC-34 | Trafficking, bonded labour, child labour | Bonded Labour System (Abolition) Act 1976 [K]; Child and Adolescent Labour (Prohibition and Regulation) Act 1986 [K] | exclude + URG-13 | Police 112; District Magistrate; Childline 1098 | "Act now." |
| EXC-35 | State-to-state (WTO) and investor–state (ISDS) disputes | Master §1.2 INT; INT-G-08 | exclude | Ministry of Commerce/DGTR (`dgtr`); Department of Economic Affairs | — |
| EXC-36 | Sanctioned parties or transactions | NN-19; INT-G-01/02 | exclude pending compliance review (`compliance_officer`) | — | — |
| EXC-37 | Securities-market disputes of investors against SEBI-registered market participants (while the `SEC` connector is OFF) | SEBI master circular SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2023/195 (31 Jul 2023, updated 28 Dec 2023) [V] | signpost_first (mandatory SCORES → SMART ODR route) | SEBI SCORES (`sebi_scores`⁺) scores.sebi.gov.in; SMART ODR (`smart_odr`⁺) smartodr.in | SMART ODR/SCORES timelines per circular |
| EXC-38 | Agricultural-land revenue matters: mutation, revenue-court partition, land ceiling, tenancy under State revenue codes | e.g. UP Revenue Code 2006 s.116; Rajasthan Tenancy Act 1955 s.53 **[VERIFY — open: revenue-court partition provisions per launch State (carried from V0470)]** | split — family settlement terms mediable; revenue entries only by the revenue authority | Tehsildar / revenue court (`revenue_court`⁺) | State law |
| EXC-39 | Disputes with no identifiable lawful counterparty, or requests for information only | — | out of scope → RES-09 with information links | — | — |
| EXC-40 | Any matter the Central Government notifies under Mediation Act 2023 First Schedule item 13, and any matter a tenant or the Rules Sub-Committee adds to the tenant exclusion list (stricter only) | Mediation Act First Schedule item 13 [V]; master §6 guardrails | exclude | Per entry | Per entry |

**Equator policy exclusions (not statutory).** Serious fraud, forgery, impersonation and coercion allegations that go to the root of the agreement trigger RES-08 (human review) rather than automatic exclusion, labelled "Equator policy" — the enacted First Schedule does not contain them (GLOBAL_CORRECTIONS #2). Fraud alleged by an insurer in an INS claim → no Equator mediation of that claim (FR-P02-20; IN-G-12).

### 3.3 Criminal-element nuance table (NN-24 applied)

| Situation | What Equator may do | What Equator must not do | Output | Copy (en) |
|---|---|---|---|---|
| Cheque bounced, no complaint filed yet | Negotiate/mediate payment inside the 15-day notice window; payment link to escrow or direct | Threaten prosecution or arrest (FL-G-08); draft a "withdrawal" of a case that does not exist | Settlement + receipt | "Paying within 15 days of the notice can avoid a criminal complaint. Equator can help you agree how." |
| Cheque complaint pending | Mediate the money terms; prepare joint compounding application (NI Act s.147) and the stage cost note | Close or withdraw the case; promise the court will accept | Settlement deed + compounding pack | "Only the court can close the cheque case. We prepare the papers you file." |
| Matrimonial dispute with a parallel FIR (cruelty, dowry) | Mediate civil terms (maintenance, streedhan, residence, children's arrangements, divorce terms) if the aggrieved spouse asks and screening passes | Mediate the offence; draft terms that trade money for withdrawal of a non-compoundable FIR; promise quashing | MSA + note that quashing is for the High Court (*Gian Singh*) | "Some criminal cases can only be closed by the High Court. A settlement can be placed before it, but the court decides." |
| Instant triple talaq pronounced | Mediate mahr, subsistence allowance, custody and return of goods on the wife's request | Record or facilitate the talaq; describe the marriage as ended by it | Civil terms MSA; compounding note (s.7(b)) | "Instant triple talaq is void and illegal. The Magistrate decides allowance and custody. You can still agree other matters." |
| Recovery agent threats | Signpost police and the RE's grievance officer and RBI Ombudsman; a separate loan-settlement mediation may continue with contact blocks | Mediate the threats | Grievance pack | "Threats are a police matter. You can also complain to the lender and the RBI Ombudsman." |
| Fraud allegation in a commercial contract | Continue civil process with a warning (arbitrable unless it vitiates the arbitration agreement — *Avitel Post Studioz v HSBC PI Holdings* (2021) 4 SCC 713 [K]) | Investigate or make findings of crime | Normal outputs | "We can help with the contract dispute. A police complaint is separate." |
| Cyber fraud or unauthorised bank debit | Signpost 1930 and the bank first; a later dispute with the bank about liability can be mediated | Pursue the fraudster | Signposting certificate | "Call 1930 and your bank now. Fast reporting can help recover money." |

### 3.4 Urgent and safety triggers

Triggered by EXU-04, EXU-05, vertical tree answers, the cue lexicon/classifier on free text or voice, or a case manager. On trigger: interrupt page (SCR-P02-25), Quick exit made prominent, joint-session routes suppressed for the session, cue code written to `safety_sealed` (no text), human task created, signposting event recorded. The user may choose "Get help now" (call/links) or "Continue later" (session saved only if the user chooses, §1.4).

| Code | Trigger | Helplines / forums shown (state-aware from directory) | Human task | Copy (heading / body) |
|---|---|---|---|---|
| URG-01 | Immediate danger to life or safety | Emergency 112 (ERSS) [V] | `safeguarding_lead`, 1 hour (business hours) / next business hour | "If you are in danger now, call 112." / "Mediation is not safe or right while someone is in danger. You can come back later." |
| URG-02 | Domestic violence or abuse | 112; Women Helpline 181 [K]; Protection Officer for your district (directory); One Stop Centre (Sakhi) [K]; NCW (`ncw`⁺) | `safeguarding_lead`, 24 h | "You do not have to put up with abuse." / "A Protection Officer or the police can help you get a protection order. This is free." |
| URG-03 | Child may be taken away or out of India; passport being applied for | Family Court / High Court for an urgent order; Regional Passport Office representation (minor's passport normally needs both parents' consent [K]); 112 | `safeguarding_lead`, 4 h | "Mediation cannot stop a child being taken abroad. A court can, often on the same day." |
| URG-04 | Child being harmed, including sexual abuse | Childline 1098 [K]; 112; POCSO Act 2012 s.19 reporting duty (shown to staff) | `safeguarding_lead`, 1 hour; mandatory reporting workflow | "A child's safety comes first. Call 1098 or 112." |
| URG-05 | Thoughts of self-harm or suicide | Tele-MANAS **14416** or 1-800-891-4416 (24×7, multilingual) [V]; 112 | Warm human handoff offered immediately; no further questions on that page | "You matter, and help is available now. Call Tele-MANAS on 14416 — it is free and open all the time." |
| URG-06 | Threats or harassment (including recovery agents) | 112; police station; for regulated lenders: RE grievance officer, RBI Ombudsman (cms.rbi.org.in) | `case_manager`, 24 h | "Threats are never acceptable. Report them to the police." |
| URG-07 | Older person harmed, neglected or abandoned | Elderline 14567 [K]; 112; Maintenance Tribunal (MWPSC s.5) | `safeguarding_lead`, 24 h | "Older people have legal protection. Elderline 14567 can help." |
| URG-08 | Ongoing cyber or financial fraud | 1930 / cybercrime.gov.in [V]; own bank's fraud line; Chakshu (Sanchar Saathi) for fraud calls/messages [V] | none (self-help) | "Call 1930 straight away. Reporting quickly can help stop the money." |
| URG-09 | Deadline within 7 days (auction, eviction, BG encashment, limitation date) | Relevant court/tribunal for urgent relief (civil court; DRT under SARFAESI s.17; A&C s.9 court); free legal aid (DLSA) | `case_manager`, 1 working day (only if the user asks for a call) | "Something may happen in the next few days. A court or tribunal may be able to act quickly. Mediation usually takes longer." (flow continues) |
| URG-10 | Medical emergency | 108 ambulance [K]; 112 | none | "Call 108 or 112 for a medical emergency." |
| URG-11 | Sexual harassment at work (POSH) | Employer's Internal Committee; district Local Committee; 112 if in danger | none in core (sealed) | "You can complain to your employer's Internal Committee within three months of the last incident. We do not take these complaints, and we will not ask for details." (never discouraging — WP-G-01) |
| URG-12 | Cannot afford food, shelter or legal help | Free legal aid: DLSA (LSA Act 1987 s.12 eligibility) [K]; NALSA helpline **15100** **[VERIFY — open: confirm NALSA national helpline number]** | none | "You may be able to get a free lawyer through the Legal Services Authority." |
| URG-13 | Missing person, trafficking, bonded or child labour | 112; Childline 1098; District Magistrate | `safeguarding_lead`, 1 hour | "Call 112 now." |

Helpline numbers are rows in `core.urgent_triggers.helplines` (config, `last_verified_at`, re-verify every 90 days); an unverified number is never displayed (the forum name and website are shown instead). Rows marked [K] above must be verified by the `legal_reviewer` before P02 go-live (fail-safe: protective — may display once verified; until then show the forum name only).

### 3.5 Exclusion and interrupt copy patterns

| Pattern | Heading | Body | Buttons (equal weight) |
|---|---|---|---|
| Full exclusion (RES-05) | "Equator cannot help with this — but {forum} can" | "{One-sentence reason in plain words}. {Forum} {what it does}. It is {free / costs ₹x}. {Last date sentence}." | "Go to {forum}" · "Download this information" · "Leave this page" |
| Split (RES-03) | "We can help with part of this" | Two columns: "Equator can help you agree: {civil items}" / "Only {forum} can: {statutory/criminal items}" | "See how Equator can help" · "Go to {forum}" |
| Arbitration blocked | "Arbitration is not available for this" | "{Reason, e.g. 'Arbitration cannot decide a divorce or who children live with.'} Mediation can still help you agree the arrangements." | — |
| Interrupt (RES-06) | Per URG row | Per URG row | "Call {number}" · "See more help" · "Continue later" |

Blocked words in all exclusion copy: "reject", "refuse", "ineligible", "not allowed to", "your case fails". Use "Equator cannot help with this" and name who can.

---

## 4. Result types, the Readiness & Pathway Report v2 and form resolution

### 4.1 Result types (precedence top to bottom; one primary result per matter, overlays allowed)

| Code | Result | When | Headline (en) | Primary CTA | Secondary CTA |
|---|---|---|---|---|---|
| RES-06 | `URGENT_HELP` | Any URG trigger except URG-09 | Per URG row (§3.4) | Call / open helpline | Continue later |
| RES-05 | `SIGNPOST_ONLY` | An `exclude` hit covers the whole matter | "Equator cannot help with this — but {forum} can" | Go to {forum} | Download information |
| RES-03 | `PARTLY_SUITABLE` | A `split` hit, or a multi-classified matter where one part is excluded | "We can help with part of this" | See how Equator can help with {part} | Go to {forum} for {other part} |
| RES-04 | `FREE_FORUM_FIRST` | Router returns a free/statutory forum with `must_approach_first` (e.g. insurer GRO before the Ombudsman; RE before RB-IOS) or `free_and_equivalent` | "Start with {forum} — it is free" | Get the free letter / go to {forum} | "You can also use Equator if the other side agrees" (only where lawful) |
| RES-02 | `SUITABLE_WITH_CONDITIONS` | ADR available subject to conditions (`needs_safety_screening`, `needs_arbitration_agreement`, `needs_authority`, `needs_court_recording`, `needs_court_sanction`, `needs_registration`, `needs_regime_review`) | "Mediation can help, with some steps first" | Start (with the steps listed) | Talk to a person |
| RES-01 | `SUITABLE` | ADR routes available, no conditions | "Mediation and other options can help with this" | Invite the other side / file | Save the report |
| RES-07 | `RESPONDENT_OPTIONS` | `entry_role = respondent` | "Your options" | Respond | See free forums |
| RES-08 | `HUMAN_REVIEW` (overlay) | Classification confidence < 0.6 top-1 after questions; regime conflict (D2-03); customary/ST law; Goa/UCC edge cases; unknown counterparty; Equator-policy fraud flag | "We would like a person to check this with you" | Request a free call-back (process questions only) | Continue anyway |
| RES-09 | `OUT_OF_SCOPE` | No dispute / information request / EXC-39 | "This does not look like a dispute we can help with" | Useful links | Something else |

"Suitable" copy is constrained: allowed — "can help", "is available", "you can use"; blocked — "will resolve", "good chance", "recommended for your case", "best option" (K-D-09). Route ordering on the report is by a published, non-merits rule: (1) free forum first where `must_approach_first`; (2) least formal Equator process first (negotiation → mediation/conciliation → arbitration); (3) the user's EXU-12 outcome only re-orders explanations, never availability.

### 4.2 Readiness & Pathway Report v2 (`explorer_report.v2`; supersedes v1 section order in FR-P02-04)

| # | Section | Content rules | Example copy (FIN digital loan, borrower, Rajasthan, ₹1–3 lakh band) |
|---|---|---|---|
| 0 | Result banner | RES code headline + one sentence; versions chip (ruleset, tree, packs, fees) | "Start with your lender's grievance officer — it is free." |
| 1 | What you told us | ≤ 3-sentence neutral restatement, user-confirmed; edit link to "Check your answers" | "You took a loan through a lending app. You say you are being charged more than agreed and receive calls late at night." |
| 2 | Get help now (if any) | URG cards | "Calls before 8 am or after 7 pm on a recovery matter are not allowed from 1 January 2027 under RBI rules. You can report threats to the police." |
| 3 | Free and statutory options first | Each forum card: what it can do · cost · whether a lawyer is needed · how to apply (link) · **last date to act** (computed) · documents to take | "RBI Ombudsman — free — no lawyer needed. First complain to the lender. If they do not reply in 30 days, or you are not satisfied, complain to the RBI Ombudsman within 90 days. Dates to watch: complain to the lender now; RBI Ombudsman by about 18 Feb 2027." |
| 4 | What Equator can do | Route cards (§4.3) for each available mechanism | Negotiation card; Conciliation (Part III) card |
| 5 | What Equator cannot do here | Blocked routes with reason codes and plain reasons | "Arbitration is not shown because your loan agreement gives the lender alone the power to choose the arbitrator. That kind of clause is not valid for appointments (CORE v ECI-SPIC-SMO-MCML, 8 Nov 2024)." |
| 6 | Dates to watch | Pills from `screen.limitation` with the fixed "mediation does not stop these dates" sentence | — |
| 7 | Documents checklist | From the pack (§6) by L2: mandatory/optional, "you have / you need" ticks (user-held, not uploaded) | "Loan agreement or Key Fact Statement · statement of account · screenshots of call logs and messages · your complaint to the lender and its reply" |
| 8 | How it would work | Stage list for the chosen route (from Appendix A) with time bands from config | "1 Invite the lender (they have 30 days to accept) · 2 Choose a conciliator · 3 Online sessions · 4 Signed settlement with the status of an arbitral award (s.74)" |
| 9 | Cost | `fees.quote` result: who pays, GST-inclusive total for consumers (NN-29), free first session where configured (§5.7), concessions | "You pay nothing for the first information session. If both sides go ahead: ₹{x} including GST, shared equally (subject to Board approval)." |
| 10 | Your next step | CTAs (§4.4) | — |
| 11 | Caveat and versions | Fixed caveat (GX-4/GX-7) + `rule_trace_id`, versions, generated time | "This is information, not legal advice. Equator Resolution is a private ADR institution, not a court, regulator or government body. Nothing has been filed or decided for you." |

Delivery: HTML (web/app), PDF (download; A4; hash in footer; verification QR to `/verify`), and "Share with the other side" link (shows sections 1, 3, 4, 8, 9, 11 only; no limitation pills about the sharer's position; no private answers).

### 4.3 Route option card anatomy

| Field | Source | Example |
|---|---|---|
| Mechanism name + one-line description | i18n catalogue | "Conciliation — a neutral conciliator helps you both reach an agreement." |
| Who decides | Mechanism constant | "You and the other side decide. Nobody can force an agreement." / arbitration: "The arbitrator decides, and the decision is binding." |
| What you get | Output label from §5.6 (copy-lint list) | "A settlement agreement under section 73 of the Arbitration and Conciliation Act 1996, which has the status of an arbitral award (section 74)." |
| What is needed | Conditions from rule pack | "The other side must accept the invitation in writing." |
| Time | `config.time_bands.<mechanism>.<vertical>` | "Usually 30–60 days from acceptance (Equator target)." |
| Cost | `fees.quote` | "₹{x} incl. GST" |
| Confidentiality | Mechanism constant | "Private. What is said cannot be used later in court (A&C Act s.81)." (conciliation) |
| Unavailable reason (if blocked) | `reason_code` → plain text | — |

### 4.4 Next-step CTAs (rules)

| CTA code | Label | Shown when | Action |
|---|---|---|---|
| `start_prelit_invitation` | Invite the other side | Claimant; consensual mechanism available; other side identifiable | Opens pre-litigation flow (§5) with pre-filled facts |
| `file_case` | Start a case | Arbitration with an agreement, joint filing, or court-referred mode | Filing wizard / task list (FR-P02-12) |
| `go_to_free_forum` | Go to {forum} | Any free/statutory forum card | Deep link + downloadable letter where a template exists (representation to insurer GRO, complaint to RE, MSME ODR export pack, Form-1 PIMS pack) — free of charge |
| `download_letter` | Download a free letter | Template exists for that forum | Generates DOCX/PDF from user's answers; user edits; never sent by Equator (GX-7) |
| `talk_to_human` | Ask a person about the process | Always (hidden only in RES-06 until help shown) | Free call-back, 10 minutes, process information only, 08:00–19:00; case manager script forbids merits (GX-1) |
| `request_human_review` | Get your report checked by a case manager | RES-08 or user request | One-time product (D2-18), flat fee from Appendix O; free for vulnerable users (`concession.explorer_review_free`); process review only, never advice |
| `invite_joint` | Ask the other side to use the Explorer with you | `joint_intent` or RES-01/02 | Sends a neutral share link (not the private answers) |
| `save_report` | Save this report | Always | §1.4 |
| `stop` | I do not want to go further | Always | Ends session; offers delete |

### 4.5 Form-resolution rule

**Rule.** `form = f(vertical, l2_code, mechanism, party_role, jurisdiction, purpose, ruleset_version)`. The function returns an **ordered composition** of form-schema versions (blocks), not a single form, and is pure and deterministic.

| Input | Values |
|---|---|
| `vertical` | `FIN` · `COM` · `FAM` · `INS` · `WRK` · `INT` · `SEC` · `XPN` (pack-hosted) |
| `l2_code` | Taxonomy code (V §2 / pack taxonomy) or `*` |
| `mechanism` | `negotiation` · `conciliation` · `mediation` · `arbitration` · `med_arb` · `arb_med` · `arb_med_arb` · `expert_determination` · `grievance` · `signposting` or `*` |
| `party_role` | `claimant` · `respondent` · `joint` · `rep_claimant` · `rep_respondent` · `enterprise_bulk` or `*` |
| `jurisdiction` | ISO 3166-2:IN state code (e.g. `IN-RJ`), `IN`, seat code for arbitration (e.g. `IN-GIFT`), foreign country code for INT, or `*` |
| `purpose` (mandatory, never `*`) | `request` (negotiation/mediation/conciliation request) · `statement_of_claim` · `response` · `statement_of_defence` · `counterclaim` · `consent` (Agreement to Mediate / s.62 acceptance) · `settlement_terms` · `vertical_specific:<code>` |
| `ruleset_version` | Pinned at session start or filing (NN-21) |

**Algorithm.**

```
candidates = form_bindings where ruleset_version_id = pinned
             and purpose = input.purpose
             and each of (vertical, l2_code, mechanism, party_role, jurisdiction) ∈ {input value, '*'}
score(b)   = 32·[b.l2_code≠'*'] + 16·[b.mechanism≠'*'] + 8·[b.party_role≠'*'] + 4·[b.jurisdiction≠'*'] + 2·[b.vertical≠'*']
winner     = argmax score; publish-time validator guarantees uniqueness of the max for every reachable key
blocks     = base(purpose) ⊕ winner.blocks ⊕ jurisdiction_overlay(jurisdiction) ⊕ mechanism_overlay(mechanism)
guard      = mechanism permitted for (vertical, l2_code, party facts)? else 422 MECHANISM_NOT_PERMITTED_FOR_VERTICAL
return { form_schema_version_ids: blocks, binding_id, score, rule_trace_id }
```

Jurisdiction overlays add state-specific fields only (e.g. stamp-duty state of execution, registration office, State rent/RERA authority, State Shops & Establishments Act). Mechanism overlays add the mechanism's legal consents (e.g. arbitration: seat, tribunal size, s.12(5) waiver capture where the dispute has arisen; conciliation: s.62 invitation text). The validator (VAL-05) enumerates every reachable key from the taxonomy × permitted mechanisms × roles × active jurisdictions and fails publication if any key resolves to zero bindings or to a tie.

**Examples.**

| Key | Resolved blocks | Note |
|---|---|---|
| FIN / `digital_lending` / conciliation / claimant / IN-RJ / request | `base.request` + `fin.core` + `fin.digital_lending` + `mech.conciliation.s62_invitation` | RE name and LSP mandatory (PI-FIN-10) |
| FAM / `partition_coparcenary` / arbitration / claimant / IN-MH / statement_of_claim | `base.soc` + `fam.core.regime_block` + `fam.partition` + `mech.arbitration.core` + `overlay.IN-MH.stamp_registration` | NN-08 physical execution and registration step added |
| INS / `health_reimbursement` / arbitration / claimant / IN-DL / statement_of_claim | — | 422 `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` (`rule` = `INS_RETAIL_ARBITRATION`; retail policyholder; IN-G-02) |
| WRK / `manager_contract` / arbitration / respondent / IN-KA / statement_of_defence | `base.sod` + `wrk.core` + `wrk.contractual_split` + `mech.arbitration.core` | Statutory components split out (HB-WRK-ARB-01) |
| XPN / `cns.ecommerce_refund` / mediation / claimant / IN-UP / request | `base.request` + `pk_cns.core` + `pk_cns.ecommerce` + `mech.mediation.contractual` | Pack-hosted (§7) |

---

## 5. Pre-litigation mediation and conciliation product (cross-vertical)

Source: S4 Part B (B1–B5), management decision M-06, master NN-05/NN-12. Vertical overrides live in V1–V6 §8; this section is the common engine.

### 5.1 What Equator may lawfully offer today (21 Oct 2026)

| Route | Equator role | Output strength (strongest first) |
|---|---|---|
| A&C Act 1996 Part III conciliation (ss.61–81) | **Full**: commences when the other party accepts the written invitation (s.62(2)); no reply within 30 days may be treated as rejection (s.62(4)) | 1 — s.73 settlement agreement, signed by the parties and authenticated by the conciliator, with the status of an arbitral award on agreed terms (s.74), enforceable under s.36 |
| Consent award | Full, where an arbitration agreement exists or is signed after the dispute; arbitrator different from the mediator by default (master §5.3) | 2 — arbitral award on agreed terms (s.30) |
| Lok Adalat recording | Conversion channel only: joint application to the DLSA under LSA Act 1987 s.20(2) for a pre-litigation matter (s.19(5)(ii)) | 3 — award deemed a civil-court decree, final, no appeal (s.21) [K]. Equator never claims NALSA partnership |
| IR Code settlement (WRK workers) | Draft memorandum; signature before the conciliation officer option (IR Code s.53) | 4 — binding IRC settlement once completed per the Code **[VERIFY — open: Q-C3 binding-effect section]** |
| Contractual mediation (Equator Mediation Rules) | **Full** | 5 — Mediated Settlement Agreement (contract) |
| Statutory pre-litigation mediation (Mediation Act s.5) | None until notified; flag `mediation_statutory_mode` OFF (NN-05) | — |
| Commercial Courts Act s.12A PIMS | Assist only: Form-1 pack for the Legal Services Authority (PIMS Rules 2018, G.S.R. 606(E), 3 Jul 2018); flag `com.s12a_equator_authorised` OFF (M-06) | — (never represented as satisfying s.12A) |

**Mechanism selector (PL-02, K-D-07).**

```
IF vertical ∈ {FAM} OR safety_screen_required OR relationship_status = ongoing_family   → mediation (contractual)
ELSE IF respondent_kind ∈ {organisation} AND outcomes ∩ {payment, documents_release, time_to_pay} ≠ ∅ → conciliation (Part III)
ELSE IF value_band ≥ 3l_20l AND dispute_clause = arbitration                            → conciliation, with consent-award option
ELSE                                                                                    → mediation (contractual)
User may switch between mediation and conciliation before the invitation is sent; the choice is recorded
(`mechanism_mode`) because it fixes the output (s.73/s.74 only if run as Part III from the start — S3 A0.4).
```

### 5.2 Pre-litigation engagement state machine (`core.prelit_engagements.state`)

```
draft → suitability_check ─┬─► signposted (terminal; forum pack + signposting event)
                           └─► notice_ready (claimant approves; e-sign by claimant/authorised signatory)
notice_ready → invitation_sent → { delivered | bounced → address_research → invitation_sent (max 2 re-sends) }
delivered → viewed → responded{accept | accept_with_conditions | decline | counter_offer | object_forum |
                               request_info | request_extension (once, ≤ 14 days)}
  accept / accept_with_conditions → consent_pending_signature → consented
  counter_offer                   → negotiation_assisted (structured offers, no neutral) → consented | non_commencement
  decline | object_forum          → non_commencement
no response by deadline (D14 individual; D30 organisation or s.62(4) conciliation) → non_commencement
consented → neutral_appointed (disclosure; challenge window 3 working days) → pre_session (separate intake calls;
            authority-to-settle check; safety screen) → in_session (joint | caucus | shuttle; online default)
in_session → { settled_in_principle → drafting → signed | partial_settlement → signed + not_settled(rest) |
               not_settled | suspended (safety, incapacity, parallel urgent proceedings) }
signed → output_conversion → compliance_tracking → { closed_performed | closed_breached → enforcement pack }
non_commencement | not_settled → closed (Non-Commencement Notice / Closure Report; signposting re-issued)
```

**Mapping to the case machine (master §5.1).** The case is created at `notice_ready` with `source = self_filed` and `core.cases.is_prelit = true`; `invitation_sent…responded` = case `awaiting_respondent`; `consented` → proceeding created (mediation or conciliation, Appendix A) and case `neutral_appointment`; `in_session` = `in_proceedings`; `signed` = `outcome_drafted → outcome_executed`; `compliance_tracking` = `in_compliance`; `non_commencement` = case `closed` with `closure_reason = prelit_non_commencement`.

**Guards.** `notice_ready → invitation_sent` requires: suitability result ∈ {RES-01, RES-02, RES-03 civil part, RES-04 where lawful}; no active URG; respondent contact point lawfully obtained (DPDP s.17(1)(a) basis recorded — GLOBAL_CORRECTIONS #13); notice copy-lint passed; claimant fee status per §5.7. `consented → neutral_appointed` requires the Agreement to Mediate or s.62 acceptance e-signed by every party (or authorised signatory) and fee allocation recorded.

### 5.3 Invitation (notice) content — mandatory fields

| Field | Rule |
|---|---|
| Sender | "Equator Resolution Service Private Limited — Case Administrator", named case manager, case ID, QR and "Verify this notice" URL (`/v/{code}`, the App. R §5 verification service; `/verify/notice/{code}` redirects to it) |
| Nature | "Invitation to mediation" or "Invitation to conciliation under Part III of the Arbitration and Conciliation Act, 1996" — states it is **voluntary** |
| Parties | Claimant name; respondent name as known; representative (if any) |
| Subject | 2–3 line neutral summary, claimant-approved and case-manager-edited for neutrality; amount if any; list of documents (viewable after identity check) |
| What it means | ≤ 60 words + 60-second vernacular video + language selector |
| Options | Accept · Propose other dates or neutral · Ask a question · Ask for more time · Decline (optional private reason) |
| Deadline | D14 (individual respondent) / D30 (organisation; and the s.62(4) 30-day rule for conciliation) |
| Cost | "Your first session is free" or the exact fee including GST and who pays (NN-29) |
| Confidentiality | Summary of Equator Rules confidentiality; for conciliation A&C ss.75 and 81 |
| Other options | Neutral list of statutory/free forums for the vertical (NN-20) |
| Limitation notice | "This invitation does not stop any time limit running unless both of you sign a separate standstill agreement." (standstill template only when flag `prelit.standstill_template` is ON — Q-C1) |
| Data notice | Itemised DPDP notice for respondent data (s.17(1)(a) context); grievance officer contact |
| Channel opt-out | "Reply STOP to stop messages on this channel." DND respected (NN-12) |

**Copy-lint (PL-15) — blocked in every pre-litigation template:** "legal action will follow", "final warning", "court", "decree", "Lok Adalat by Equator", "NALSA/MCPC partnered", "court-annexed", "statutory pre-litigation mediation", "s.12A compliant", "pauses limitation", "registered settlement", any arrest/criminal consequence wording (FL-G-08), "defaulter".

**SMS/WhatsApp short form (en; DLT/WhatsApp utility template):** "Equator Resolution (case {ID}) invites you to a free, voluntary online {mediation|conciliation} about a matter raised by {claimant}. See details and reply by {date}: {short_url}. Verify: equatorresolution.in/verify. STOP to opt out." FAM matters use the neutral form: "You have a message from Equator Resolution about case {ID}. Open securely: {short_url}." (FAM-G-07).

### 5.4 Delivery and reminder cadence (defaults; `prelit.cadence.<vertical>` config)

| Day | Action | Channels |
|---|---|---|
| D0 | Invitation | Email (PDF + link) + WhatsApp utility template + DLT SMS; Speed Post via `POSTAL_PORT` for organisations or value ≥ ₹3 lakh |
| D2 | Delivery check; bounce → address research (MCA master data for companies; claimant alternates) | — |
| D3 | Reminder 1 (soft, FAQ link) | WhatsApp/SMS |
| D7 | Reminder 2 + case-manager call (08:00–19:00; disclosure; M-05/NN-12) | Voice |
| D10 | Final notice (individual respondents) | Email + WhatsApp + SMS |
| D14 | Close as `non_commencement` (individual) unless an extension was requested | — |
| D21, D28 | Organisation reminders | Email + post |
| D30 | Close as `non_commencement` (organisation; s.62(4)) | — |
| Post-consent | Session reminders T-48 h and T-2 h; one free reschedule | WhatsApp/SMS |

Hard limits: ≤ 6 outbound contacts per respondent before consent (`prelit.contact_cap = 6`, error `PRELIT_CONTACT_CAP_REACHED`); calls and messages only 08:00–19:00 local time (`CONTACT_OUTSIDE_WINDOW`); no contact on national/State public holidays (Equator policy); every template vernacular-paired; one primary conversational channel chosen by the respondent (web assistant **or** WhatsApp), not parallel bots (S4 E9).

### 5.5 Consent capture (legal-grade)

| Element | Rule |
|---|---|
| Instrument | Agreement to Mediate (Equator Mediation Rules version hash) or written acceptance of the conciliation invitation (A&C s.62(2)) |
| Signature | Aadhaar eSign or DSC (organisations); OTP-verified mobile and email; IP, timestamp, Rules version hash, notice hash stored (evidence ledger, NN-10/NN-22) |
| Authority | Organisation: board resolution or authority letter (upload; required before signing any settlement); representative: Letter of Authority / vakalatnama with scope and settlement limit (NN-27) |
| Sub-consents (each separate, unticked by default) | Online mode · no recording (NN-11) · language · interpreter · fee allocation · optional standstill agreement (flag) · optional arbitration agreement for a consent award (separate signature; independent-advice prompt; for consumers and individual employees the screen states "You do not have to sign this to mediate") |
| Vertical specifics | WRK: statutory dues cannot be waived; statutory forums stay open; POSH never enters this flow. FAM: safety screen passed; DV-adjacent only at the aggrieved person's request. INS retail: arbitration agreement never offered (IN-G-02) |

### 5.6 Engagement design (what makes respondents join — S4 B4)

| Lever | Product feature | Config / requirement |
|---|---|---|
| Neutral institutional sender | Notice from Equator's named case manager; verify page; QR | PL-03 |
| Understanding | ≤ 60-word explainer + 60-second vernacular video; "What happens if I say no?" answered neutrally | `prelit.explainer_video.<locale>` |
| Choice | Respondent picks 1 of 3 time slots, 1 of 3 neutrals (from the published allocation shortlist, NN-28), language, online/in-person; option "prefer a woman neutral" | Respects allocation rules: the shortlist is generated by the allocation engine, never by the claimant |
| Low friction | ≤ 3 screens from link to signed consent; mobile-first; one link | PL-06 |
| Cost asymmetry, stated neutrally | Free first session; fees shared only after consent; neutral facts on statutory alternatives with sourced time/cost | No figures without a Claims Register entry (NN-17) |
| Respondent-side benefits | Confidentiality; without-prejudice protection (A&C s.81 in conciliation); control over the outcome | Fixed copy |
| Organisations | Route to the designated grievance officer/legal head; **portfolio protocol** (pre-agreed acceptance of Equator invitations for repeat disputes, with SLAs and a funding-neutrality statement) | PL-16; P09 |
| Reliability | Auto-reschedule once; T-48 h/T-2 h reminders; phone dial-in fallback | E3 |
| Respect and safety | No recovery-style tone; POSH/DV screening before any joint session; contact cap | FL-G-02; FAM-G-01 |
| Structured offers | Singapore Rules of Court 2021 Order 5 model: written offer object open ≥ 14 days, without-prejudice flag, sealed decline reasons | PL-08; `core.offers.min_open_days >= 14` for prelit offers |

### 5.7 Free first session options

| Option | Who pays | Eligibility | Disclosure |
|---|---|---|---|
| FFS-1 Respondent-free information and options meeting (default) | Claimant (included in the claimant's registration fee) or enterprise tenant | All prelit matters | "The first session is free for you. {Claimant/Organisation} has paid for it. The mediator is not on their side." |
| FFS-2 Free for both sides | Equator access fund (Board-approved budget, M-01) | Pro bono band (`concession.prelit_pro_bono`): individual parties with value ≤ ₹3 lakh and a vulnerability flag or income below the configured threshold | "This session is free for both of you." |
| FFS-3 Portfolio-funded | Enterprise tenant under a portfolio protocol | Lender/insurer/employer/platform programmes | Funding-neutrality statement (NN-16): "The organisation pays Equator's fee. This does not affect who the mediator is or how they act." |
| FFS-4 Joint-start | Both, at a reduced combined fee; first session free | Joint applications (`entry_role = joint`) | Fee shown including GST before consent |

The first session is 30 minutes (configurable 30–45): process explanation, ground rules, each side's priorities, and the choice to continue. It may continue into substantive mediation the same day only if both sides consent and the fee allocation for the next stage is accepted on screen. Neutral fees are identical whatever the outcome (X-07). No countdown or "offer ends" messages (NN-29).

### 5.8 Mediation conduct and conversion

- Neutral appointed within 3–5 working days of consent; separate pre-session calls; authority-to-settle check; safety screen.
- Time box: Appendix A clock `med_contract_timebox` (FIN 60, COM 60, INS 45, WRK 45, FAM 120 days — FAM property and elder tracks 90 days, X-40 — INT 60 days, from first appearance), extendable by written consent of all parties by up to 60 days; Equator's WRK target is 30–45 days; no matter exceeds the outer contractual cap of 120 + 60 days, which mirrors Mediation Act s.18 as Equator policy.
- Settlement drafting checklist (cross-vertical): performance schedule; escrow/milestones (NN-13); default clause (acceleration; consent to consent-award or Lok Adalat recording on default); confidentiality with regulatory carve-outs; signatures; stamp duty by State of execution (NN-09; GLOBAL_CORRECTIONS #12); immovable property → physical execution and registration route (NN-08).

**Conversion options (`output_conversion`; choose one or more).**

| Code | Instrument | Preconditions | Allowed label (copy-lint) | Blocked labels |
|---|---|---|---|---|
| `msa_contract` | Mediated Settlement Agreement | Any vertical | "Mediated Settlement Agreement (contract) under the Equator Mediation Rules" | "MSA under section 19 of the Mediation Act", "enforceable as a decree" (until NN-05 flag ON) |
| `conciliation_s73` | Settlement agreement | Proceeding ran as Part III from the start; conciliator authenticates (s.73(4)) | "Settlement Agreement under section 73 of the Arbitration and Conciliation Act, 1996, having the status of an arbitral award on agreed terms (section 74)" | — |
| `consent_award_s30` | Arbitral award on agreed terms | Arbitration agreement exists/signed; tribunal constituted; arbitrator ≠ mediator by default (master §5.3) | "Arbitral award on agreed terms (section 30)" | "Award" issued by a mediator |
| `lok_adalat_pack` | Joint application pack to the DLSA | Both parties willing to appear; matter within LSA s.19(5)(ii) | "Application for recording before the Lok Adalat (prepared for the parties)" | "Lok Adalat by Equator", "NALSA-partnered" |
| `irc_settlement_pack` | Draft IR Code memorandum | WRK; party is an IR Code worker | "Draft memorandum of settlement for submission under the Industrial Relations Code, 2020" | "Registered settlement" (until registered) |
| `court_recording_pack` | Compromise papers (CPC O.XXIII r.3); HMA s.13B annex for FAM | A court case is pending or intended | "Terms of compromise for filing before {court}" | "Decree" |
| `s12a_form1_pack` | Form-1 application to the Legal Services Authority | COM; suit intended; value ≥ ₹3 lakh; no urgent relief; not settled | "Application under the PIMS Rules 2018 (to be filed by you with the Legal Services Authority)" | "s.12A compliant", "Non-starter report" |

**Non-settlement outputs.** "Equator Non-Commencement Notice" (with PIMS disclaimer footer) — blocked: "Non-starter report", "s.12A". "Equator Mediation Closure Report" (no reasons, no conduct comments) — blocked: "Failure report". "Record of pre-action steps" (genuine-steps log: notices, offers, attendance; for costs under CPC s.35 or urgency arguments) — blocked: "Certificate of compliance".

### 5.9 Outcome labels (closure taxonomy) and KPIs

**Outcome labels** (`core.prelit_engagements.outcome`): `signposted` · `non_commencement_declined` · `non_commencement_no_response` · `non_commencement_unreachable` · `withdrawn_by_claimant` · `settled_full` · `settled_partial` · `not_settled` · `suspended_safety` · `performed` · `breached`. Respondent decline reasons are sealed and never used in neutral grading, allocation or marketing (NN-16, NN-28).

| KPI | Definition | Initial Y1 target | Benchmark basis (S4 B3/B5.7) |
|---|---|---|---|
| Delivery rate | Invitations with ≥ 1 confirmed delivery / sent | ≥ 95% | Multichannel + post |
| View rate | Respondents opening the link / delivered | ≥ 60% | Instrumented |
| Engagement rate | Any response (accept, decline, question, counter) / delivered | ≥ 50% individual-v-organisation; ≥ 40% individual-v-individual | Italy 54.8% appearance (mandatory); UK 31% (voluntary opt-out) |
| Consent rate | Consent signed / delivered | ≥ 35% B2C voluntary; ≥ 70% portfolio/clause programmes | UK 27%→31% |
| Time to consent | Median days D0 → consent | ≤ 7 | PIMS 10-day window |
| Session attendance | First sessions held / scheduled | ≥ 85% | UK up to 3 in 10 did not happen |
| Settlement rate (commenced) | Full or partial settlements / matters with ≥ 1 substantive session | ≥ 55% WRK money; ≥ 45% COM | Italy 53.1%; UK 55–61% |
| Settlement rate (filed) | Settlements / all filed | Report only — never a target | Selection-sensitive |
| Time to settlement | Median days consent → signature | ≤ 30 WRK; ≤ 45 COM | — |
| Compliance rate | Settlements fully performed on time / settlements | ≥ 85% | Escrow lifts this |
| Conversion rate | Settlements converted to s.73/s.74, consent award, Lok Adalat award or IRC settlement / eligible settlements | ≥ 50% | — |
| Signposting accuracy | QA sample where the forum named was correct | ≥ 98% | — |
| Procedural-justice score | Post-case survey, each side separately | ≥ 4.2/5 both sides; gap ≤ 0.4 | — |
| Complaint rate | Harassment/coercion complaints / invitations | ≤ 0.1% | M-05 |
| Breach rate | Breach notices within 6 months / settlements | ≤ 10% | — |

Dashboards (P09 enterprise MIS, institution admin): by vertical, respondent type, channel, language; "commenced" and "filed" denominators always shown separately; public anonymised statistics only after n ≥ 100 closed matters per vertical with methodology published (NN-17), and every published cell n ≥ 10 (X-28). A/B tests only on copy wording and timing, never on legal content, consent text or forum lists.

---

## 6. Dispute-type plug-in framework ("dispute packs")

### 6.1 Concept

A **dispute pack** is a versioned configuration package that adds or changes a dispute type end to end — taxonomy, rules, Explorer tree, forms, templates, clocks, fees, panels, calculators, integrations, copy and tests — **without application code**. Packs are authored and approved in the Ruleset Studio (master §6), stored in `core.dispute_pack_versions`, and activated per tenant behind a flag. The six verticals are themselves expressed as platform packs (`PK-FIN` … `PK-INT`), so new and existing types use one mechanism.

**Hosting (K-D-08).** A pack either (a) extends a host vertical (`host_vertical ∈ {FIN, COM, FAM, INS, WRK, INT}`), inheriting that vertical's mechanism matrix, staff queues, sealed-data rules and case-number code; or (b) is hosted in the extension vertical `XPN`, with its own three-letter `case_code` used in the case number (`EQ/{case_code}/{CITY}/{YYYY}/{NNNNN}`, e.g. `EQ/CNS/JAI/2027/00012`). `XPN` default mechanism set: negotiation, conciliation, mediation, signposting; arbitration and expert determination only where the pack declares them **and** the legal reviewer approves a permissive Appendix G rule (fail-safe principle G.1).

### 6.2 Pack manifest (`dispute-pack.yaml`, stored as JSON)

```yaml
pack: PK-CNS                      # stable code
version: 1.2.0                    # semver (§6.5)
title_i18n: { en: "Consumer and digital commerce", hi: "उपभोक्ता और डिजिटल वाणिज्य" }
host_vertical: XPN
case_code: CNS
requires_platform: ">=2.0.0"      # minimum platform contract (engine features used)
depends_on: [ PK-COM@>=2.0.0 ]    # optional
taxonomy:        { file: taxonomy.json }          # L1/L2 codes, labels, arbitrable flag, default ladder, signpost forums
rules:           { file: rules.jsonlogic.json }   # routing rules, exclusions (EXC refs), conditions, route ordering
legal_rules:     [ LR-CONS-001, LR-CONS-002, LR-CONS-003, LR-CONS-004, LR-XPN-001 ]
explorer_tree:   { file: tree.json }              # EXV-XPN-<L1>-Qnn pages, options, branching, maps_to
forms:           { schemas: [forms/*.json], bindings: bindings.json }   # §4.5
templates:       [ templates/notice.hbs, templates/msa.hbs ]            # Handlebars + clause refs; legal review per locale
clocks:          { file: clocks.json }            # clock defs referencing LR ids; owners; alert policy
fees:            { schedule_ref: FS-CNS-2027-01 } # Appendix B fee schedule (approved separately, M-01)
panels:          { file: panels.json }            # eligibility filters, endorsements, languages, co-mediation rules
calculators:     { file: calculators.json }       # formula DSL + golden vectors; labelled indicative
integrations:    { file: integrations.json }      # bindings to existing ports/connectors and deep-link catalogue only
signposting:     { file: directory_rows.json }    # forum rows with last_verified_at
guardrails:      { file: guardrails.json }        # vertical AI guardrail pack (prohibited intents, abstain topics)
copy:            { i18n: [en.json, hi.json], cms_blocks: cms/*.md }      # Explorer, report, landing-page blocks (P13)
documents:       { file: checklists.json }        # per L2 document checklist codes
confidentiality: { default_tier: high, sealed_triggers: [health_data] }
retention:       { class: case_record }
kpis:            { file: kpis.json }
tests:           { golden_facts: tests/facts/*.json, gherkin: tests/*.feature, parity_sets: tests/parity/*.json }
evidence:        { counsel_memo_refs: [CM-2027-014], dpia_ref: DPIA-CNS-01, claims_register: [] }
```

### 6.3 Artefact types and the no-code boundary

| Artefact | Authored in | No-code? | Constraints |
|---|---|---|---|
| Taxonomy | Studio taxonomy editor | Yes | Codes `^[a-z][a-z0-9_]{2,40}$`; immutable once used by a case; retire, never delete |
| Rules | Studio rule editor (JSONLogic + allow-listed function registry: `ageYears`, `daysBetween`, `workingDaysBetween`, `inEnum`, `lookup`, `sum`, `minor`, `fxConvert`) | Yes | Cannot widen master §5.2 matrix (`422 MECHANISM_NOT_PERMITTED_FOR_VERTICAL`); cannot disable NN rules or mandatory disclosures |
| Exclusions | References to EXC codes + pack-specific EXC rows | Yes | Every NN-24 category must resolve to an exclusion in every tree (VAL-08) |
| Explorer tree | Studio tree editor (visual graph) | Yes | ≤ 8 pages on the 80th-percentile path; EN + HI; readability ≤ grade 8 |
| Forms + bindings | Form designer (`equator-form/1.0`) | Yes | Field types from FR-P02-08 only; bindings unambiguous (VAL-05) |
| Templates | Template editor (Handlebars, clause library) | Yes | Legal review per locale; copy-lint |
| Clocks | Clock editor | Yes | Must reference an Appendix G rule; owner role mandatory (NN-04); cannot shorten statutory periods |
| Fees | Fee editor (Appendix B) | Yes | Separate maker–checker with Board approval reference (M-01); NN-18 limits |
| Panels | Panel/eligibility editor (App. N) | Yes | Allocation policy stays platform-wide (NN-28); packs add filters/endorsements only |
| Calculators | Formula DSL + golden vectors | Yes | Pure functions over user-supplied figures; output labelled "indicative computation"; no valuation (GX-3) |
| Integrations | Binding editor | Yes, **only** to existing ports/connectors and deep links | A new external system needs a new adapter → code change (P09/D) |
| Copy and CMS blocks | i18n editor / CMS | Yes | Copy-lint; claims need Claims Register evidence (NN-17) |
| Guardrails | AI governance console | Yes (config) | Approved by AI Oversight Sub-Committee; eval suite must pass (E.7) |
| Tests | Test-set uploader | Yes | Mandatory for publication |

**Requires code (change request through the normal phase process):** a new state machine or mechanism; a new field type or JSONLogic function; a new external adapter or port; a new sealed store; new payment rails; any change to NN rules.

### 6.4 Validation pipeline (runs on submit; all must pass before `in_review`)

| ID | Check |
|---|---|
| VAL-01 | Manifest and every artefact validate against their JSON Schemas |
| VAL-02 | All referenced Appendix G rules exist; permissive rules are `VERIFIED` (G.1 fail-safe) |
| VAL-03 | Mechanism × vertical/host guard: no widening of master §5.2; `XPN` arbitration only with an approved permissive rule |
| VAL-04 | Taxonomy codes unique and stable; no deletion of codes used by any case or session |
| VAL-05 | Form-binding completeness and uniqueness over every reachable key (§4.5) |
| VAL-06 | i18n completeness: EN + HI for every string; other enabled locales or fallback declared |
| VAL-07 | Readability: EN Explorer/report copy ≤ Flesch–Kincaid grade 8; sentences ≤ 20 words; HI marked human-reviewed |
| VAL-08 | NN-24 coverage: every tree yields EXC/URG outcomes for each criminal-element and safety code; POSH never collected |
| VAL-09 | Tree length ≤ 8 pages at the 80th percentile across golden fact sets |
| VAL-10 | Copy-lint: GX-1/2/3/4 terms, PL-15 list, dark-pattern list (NN-29), court/decree terms |
| VAL-11 | Golden fact sets: routing 100%, clocks 100%, exclusions 100%, fees 100% against expected outputs |
| VAL-12 | Parity: AI-assisted vs questionnaire identical routes/clocks (NN-02) in EN and HI |
| VAL-13 | Signposting rows verified within 180 days; helplines within 90 days |
| VAL-14 | Fee schedule referenced is `approved` (Appendix B lifecycle) |
| VAL-15 | Templates legal-reviewed per locale (NN-23) |
| VAL-16 | DPIA reference present if the pack introduces a new personal-data category or sealed trigger (NN-15, NN-30) |
| VAL-17 | Guardrail pack passes the zero-tolerance eval suite (E.7) |

### 6.5 Governance, versioning and rollout

**Lifecycle.** `draft → validating → in_review → approved → pilot → published → deprecated → retired`. Maker–checker throughout (checker ≠ maker, P00).

| Step | Who | Evidence |
|---|---|---|
| Propose a new dispute type | `institution_admin` or `panel_manager` | Business case; taxonomy draft; counsel memo reference |
| Legal review | `legal_reviewer` (`config.approve.legal`) | Appendix G rules created/verified; exclusions; templates |
| Rules approval | Equator Institutional Committee — Rules Sub-Committee (D2-15) | Minutes reference |
| AI guardrails | AI Oversight Sub-Committee | Eval run ID |
| Fees | Board approval reference (M-01) | Resolution number/date |
| Privacy | `dpo` | DPIA reference |
| Publication | `institution_admin` (checker) | All VAL checks green |

**Semver.** Patch = copy/i18n fix, signposting-row update, helpline update; Minor = new optional question, new L2, new template, new calculator; Major = removed/renamed code, changed routing outcome for an existing fact set, changed required form field, changed clock or exclusion. Major versions require a migration note and a 14-day notice to tenants using the pack.

**Pinning (NN-21).** Sessions pin pack versions at start; cases pin at filing; later versions never alter them. Open sessions on a retired version are offered a "restart with the latest questions" prompt; open cases continue on their pinned version.

**Rollout.** `pilot` = enabled for named tenants and/or a percentage of anonymous Explorer traffic behind `pack.<code>.enabled`; minimum 30-day pilot or 200 sessions, whichever later, with KPI and QA review (signposting accuracy ≥ 98%) before `published`. **Emergency change** (e.g. a law changes overnight): patch through `propagation_mode = emergency_block` (Appendix G.4) — protective changes only.

**Deprecation.** `deprecated` packs stop accepting new sessions after a notice period (default 30 days); `retired` packs remain readable for pinned cases for the retention period.

---

## 7. Expansion catalogue (roadmap of further dispute types)

Benchmark: competitors publish broad category lists — Jupitice (BFSI portfolios, MSME "digital court", marketplace; full list not capturable — OI-S3-01), Sama (family, property, banking, insurance, employment, commercial, co-founder), CORD (banking/NBFC, tenancy/housing society, workplace, insurance, e-commerce, MSME, consumer, healthcare, SEBI) and Presolv360 (money recovery, property, insurance, employment, civil) [V S3 C2]. Equator's differentiation is not the length of the list but that **each type ships with statutory-ladder-aware signposting, exclusions and dated forum cards** (S3 C2 analysis). Each entry below becomes a dispute pack (§6); none goes live until its pack passes VAL-01…VAL-17 and counsel sign-off on the items marked VERIFY.

Mechanism key: N negotiation · C conciliation (Part III) · M mediation · A arbitration · E expert determination · S signposting only. "B2B only" = never against a consumer, patient, student, tenant-occupier or worker under a standard-form clause (NN-03/NN-06 principle).

### 7.1 Summary

| Pack | Name | Host / case code | Wave | Mechanisms | Flag (default OFF) |
|---|---|---|---|---|---|
| PK-CNS | Consumer goods and services | XPN / CNS | 1 | N, C, M, S | `pack.cns.enabled` |
| PK-RE2 | RERA and real estate (homebuyer extension) | COM (extends `COM.RE`) | 1 | N, C, M, A (B2B only), S | `pack.re2.enabled` |
| PK-ECM | E-commerce and ONDC | XPN / CNS | 1 | N, C, M, S | `pack.ecm.enabled` |
| PK-TEL | Telecom and internet services | XPN / CNS | 2 | N, C, M, S | `pack.tel.enabled` |
| PK-HLT | Healthcare and medical (mediation only) | XPN / HLT | 2 | N, M, S | `pack.hlt.enabled` |
| PK-EDU | Education | XPN / EDU | 2 | N, C, M, A (B2B only), S | `pack.edu.enabled` |
| PK-TEN | Tenancy and rent | XPN / TEN | 1 | N, C, M, A (non-rent-control only), S | `pack.ten.enabled` |
| PK-COP | Co-operative societies and RWAs | XPN / COP | 2 | N, C, M, A (where statute permits), S | `pack.cop.enabled` |
| PK-MAC | Motor accident (signpost MACT) | INS (extends motor TP) | 1 | S (+ quantum brief) | `pack.mac.enabled` |
| PK-BOS | Banking ombudsman support | FIN | 1 | S (+ free complaint pack), N | `pack.bos.enabled` |
| PK-SPT | Sports | COM (`COM.SPORTS`) | 3 | N, C, M, A (commercial contracts), S | `pack.spt.enabled` |
| PK-MDE | Media and entertainment | COM (`COM.MEDIA`) | 2 | N, C, M, A, E, S | `pack.mde.enabled` |
| PK-IPC | IP and creative work (freelancers, creators) | COM (extends `COM.TECH`) | 2 | N, C, M, A, E, S | `pack.ipc.enabled` |
| PK-GOV | Government contracts | COM (extends `COM.CON.epc_government`) | 2 | N, M, A (< ₹10 crore by norm), S | `pack.gov.enabled` |
| PK-XBE | Cross-border e-commerce | XPN / CNS (B2C); INT (B2B) | 3 | N, M, S (B2C); N, M, A (B2B) | `pack.xbe.enabled` |
| PK-CMY | Community and neighbourhood | XPN / CMY | 2 | N, M, S | `pack.cmy.enabled` |

### 7.2 Entries

**PK-CNS — Consumer goods and services.**
- *L1/L2 seeds:* `goods_defect` (repair, replacement, refund) · `service_deficiency` (salons, travel, courier, repairs) · `warranty` · `hidden_charges` · `subscription_cancellation` · `delivery_failure`.
- *Suitability:* Voluntary B2C mediation/conciliation with a willing business, sitting **between** the business's grievance officer and the Commission; never presented as mandatory before filing.
- *Law:* CPA 2019 ss.2(7), 34–35, 37, 69, 74–81 [K]; Jurisdiction Rules 2021 (LR-CONS-001); limitation 2 years (LR-CONS-002); arbitration cannot oust the Commission (*Emaar MGF*, LR-CONS-003); CP (Mediation) Rules 2020 r.4 exclusions (LR-CONS-004); National Consumer Helpline pre-litigation convergence (1915; WhatsApp 8800001915; 17 languages) [V S4 B2.4].
- *Signpost / exclusions:* NCH first (free); Commission via e-Jagriti; EXC-18 statutory reliefs; CCPA for unfair trade practices.
- *Build notes:* Business-side "convergence-style" tenant onboarding; consumer fee ≤ the configured cap and GST-inclusive (NN-29); FFS-1 funded by the business tenant.

**PK-RE2 — RERA and real estate (homebuyer extension of `COM.RE`).**
- *Seeds:* `possession_delay` · `refund_withdrawal` · `structural_defects` · `carpet_area_shortfall` · `plan_change` · `society_handover` · `allottee_group`.
- *Suitability:* Mediation useful for possession-with-compensation, unit swap, phased refund; group mediation for many allottees; arbitration B2B only (JDA, brokerage, commercial lease); homebuyer arbitration only on informed post-dispute election.
- *Law:* RERA 2016 ss.31, 71, 79, 32(g) [K]; *Imperia Structures v Anil Patni* (2020) 10 SCC 783 [K]; *Newtech Promoters v State of UP* (2021) 18 SCC 1 [K]; MahaRERA Conciliation & Dispute Resolution Forum (Circular 15 of 2018, 29 Jan 2018; Circulars 31/2021, 38/2021) [V-sec S2 §3.4]; IBC s.7 allottee threshold (*Manish Kumar v UoI* (2021) 5 SCC 1) [K].
- *Signpost / exclusions:* RERA Authority/AO; Consumer Commission at the buyer's election; NCLT if the promoter is in CIRP (moratorium banner); civil court barred for RERA matters (s.79). Equator cannot self-designate as a s.32(g) forum (S2 interpretation).
- *Build notes:* MahaRERA card when `user_state = IN-MH`; RERA delay-interest calculator (SBI highest MCLR + 2%, State-configurable) labelled indicative; CERSAI check prompt before any refund-for-unit settlement.

**PK-ECM — E-commerce and ONDC.**
- *Seeds:* `order_not_delivered` · `refund_not_received` · `counterfeit_or_misdescribed` · `seller_platform_b2b` (seller vs marketplace payouts, delisting) · `ondc_buyer_issue` · `ondc_network_participant_b2b`.
- *Suitability:* B2C — mediation as an escalation after the platform's grievance officer; B2B seller–marketplace and network-participant disputes — N/C/M and arbitration where the participant agreement provides.
- *Law:* Consumer Protection (E-Commerce) Rules 2020 r.4(5) grievance officer: acknowledge 48 h, redress 1 month (LR-CONS-006); CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023 [V S9]; ONDC Issue & Grievance Management (IGM) framework with escalation to ODR providers **[VERIFY — open: current ONDC network-policy chapter on IGM and the ODR-provider onboarding process]**.
- *Signpost / exclusions:* NCH; Commission; platform grievance officer first (RES-04 when not yet approached).
- *Build notes:* `CONNECTOR_PORT.ondc_igm` (master D10) for issue status sync; never present Equator as ONDC-mandated unless onboarded (copy-lint).

**PK-TEL — Telecom and internet services.**
- *Seeds:* `billing_dispute` · `porting_failure` · `service_outage_compensation` · `broadband_installation` · `value_added_service_charges`.
- *Suitability:* Consumer mediation with willing operators/ISPs; low values → FFS-3 operator-funded programmes.
- *Law:* Telecom consumers may use the Consumer Commission despite the old arbitration provision of the Indian Telegraph Act 1885 s.7B — *Vodafone Idea Cellular Ltd v Ajay Kumar Agarwal* (SC, 16 Feb 2022) [K]; Telecommunications Act 2023 repeals the Telegraph Act **[VERIFY — open: commencement of the repeal and any replacement dispute provision]**; TRAI Telecom Consumers Complaint Redressal Regulations 2012 (complaint centre → appellate authority) [K]; TRAI/TDSAT proceedings excluded (Mediation Act First Schedule item 8; EXC-24).
- *Signpost / exclusions:* Operator complaint centre → appellate authority → Commission; Sanchar Saathi/Chakshu for fraud calls [V].
- *Build notes:* Operator-appellate-authority directory rows per circle.

**PK-HLT — Healthcare and medical (mediation only).**
- *Seeds:* `hospital_billing` · `package_overcharge` · `discharge_delay` · `communication_complaint` · `civil_compensation_by_consent`.
- *Suitability:* **Mediation and negotiation only**; never arbitration against a patient; co-mediation with a medically qualified neutral; health data sealed (`health_sealed`, NN-07); mandatory human review where death or grievous hurt is involved.
- *Law:* Medical services are "services" under consumer law — *Indian Medical Association v V.P. Shantha* (1995) 6 SCC 651 [K]; consumer-mediation exclusion for negligence causing death/grievous hurt (CP (Mediation) Rules 2020 r.4; LR-CONS-004); criminal negligence standard *Jacob Mathew v State of Punjab* (2005) 6 SCC 1 [K]; BNS s.106(1) [K]; Clinical Establishments (Registration and Regulation) Act 2010 [K]; NMC Act 2019 [K].
- *Signpost / exclusions:* EXC-19 (criminal and disciplinary parts); Consumer Commission; State Medical Council; PM-JAY CGRMS for scheme patients (INS signposting row).
- *Build notes:* Hospital tenant programmes must carry funding-neutrality disclosure; no AI on clinical records beyond extraction with `requires_human_review`.

**PK-EDU — Education.**
- *Seeds:* `fee_refund_withdrawal` · `hostel_charges` · `certificate_withholding` · `edtech_subscription` · `placement_or_internship_contract` · `institution_vendor_b2b`.
- *Suitability:* Mediation for students and parents; arbitration only for B2B (institution–vendor, edtech–institution); the University GRM SaaS (L4) handles statutory SGRC workflows.
- *Law:* UGC (Redressal of Grievances of Students) Regulations 2023 (F.1-13/2022 (CPP-II), 11 Apr 2023): SGRC 15 working days; appeal 15 days; Ombudsperson 30 days [V GLOBAL_CORRECTIONS #11]; AICTE (Redressal of Grievance of Students) Regulations 2019 [V RES_A3 Q19]; UGC equity regulations 2026 stayed by the Supreme Court, 2012 regulations operative [V RES_A3 Q20]; consumer status of education services is contested (*Maharshi Dayanand University v Surjeet Kaur* (2010) 11 SCC 159 [K]) **[VERIFY — open: current NCDRC/SC position on coaching and edtech as "services"]**.
- *Signpost / exclusions:* SGRC/Ombudsperson first for enrolled students (RES-04); ragging and discrimination → institution's statutory committees/police (exclude); RTE Act 2009 school matters → SCPCR/authority (exclude).
- *Build notes:* Minor students: guardian-led sessions; DPDP Rule 10 verifiable parental consent [V].

**PK-TEN — Tenancy and rent.**
- *Seeds:* `security_deposit_return` · `rent_arrears` · `repairs_maintenance` · `lock_in_exit` · `eviction_by_agreement` · `commercial_lease_b2b`.
- *Suitability:* Mediation for residential tenancies; arbitration only where the tenancy is not protected by a rent-control law (EXC-27) and the lease has an arbitration clause.
- *Law:* Transfer of Property Act tenancies are arbitrable; rent-control tenancies are not (*Vidya Drolia* (2021) 2 SCC 1, overruling *Himangni Enterprises*) [K]; Model Tenancy Act 2021 (Rent Authority, Rent Court, Rent Tribunal; model law for States) [K]; State adoptions **[VERIFY — open: list of States that have enacted Model-Tenancy-type laws and their forum/time rules]**; leases > 1 year need registration (Registration Act 1908 s.17(1)(d)) [K] and stamping (NN-09).
- *Signpost / exclusions:* Rent Authority/Controller; police for unlawful dispossession or threats (EXC-05).
- *Build notes:* Deposit-deduction calculator (itemised, user figures only); move-out photo evidence checklist.

**PK-COP — Co-operative societies and RWAs.**
- *Seeds:* `maintenance_charges` · `parking_and_common_areas` · `repairs_contribution` · `membership_transfer` · `society_management_conduct` · `redevelopment_terms`.
- *Suitability:* Mediation and group mediation; arbitration only where the statute and bye-laws permit (EXC-28); co-mediation with a member-nominated and an independent neutral on request (MahaRERA mixed-bench lesson, S4 B2.7).
- *Law:* State co-operative laws with exclusive forums (e.g. Maharashtra Co-operative Societies Act 1960 s.91 Co-operative Court) [K]; Multi-State Co-operative Societies Act 2002 s.84 [K] as amended 2023 **[VERIFY — open: Co-operative Ombudsman provision and section number after the 2023 amendment]**; apartment ownership Acts (e.g. Maharashtra Apartment Ownership Act 1970) [K]; Societies Registration Act 1860 [K]; Mediation Act 2023 ss.43–44 community mediation — not in force [V R2 §1].
- *Signpost / exclusions:* Registrar/Co-operative Court; RERA for promoter-handover issues; police for threats.
- *Build notes:* Multi-party sessions (up to 50 participants; managing-committee authority check).

**PK-MAC — Motor accident (signpost MACT).**
- *Seeds:* `tp_injury` · `tp_death` · `hit_and_run` · `own_damage` (routes to INS `motor_od`).
- *Suitability:* **No Equator adjudication or award.** Equator signposts MACT/DLSA and, if both claimant and insurer want, prepares a quantum brief for an MACT-recorded compromise or MACT Lok Adalat; minors' and dependants' claims always through the Tribunal (CPC O.XXXII r.7).
- *Law:* MV Act 1988 ss.149 (insurer offer within 30 days; Tribunal records), 164 (no-fault compensation), 165–166, 166(3) (6 months), 175 (civil courts barred) [K/V S4 B2.8]; Mediation Act s.5(6)–(8) MACT mediation not in force [V].
- *Signpost / exclusions:* EXC-20; hit-and-run solatium scheme through the claims enquiry officer **[VERIFY — open: current solatium amounts and process]**; touts warning ("Equator never charges a percentage of compensation").
- *Build notes:* Signpost-only pack: no fee screen; free document checklist (FIR, DAR, medical records, income proof).

**PK-BOS — Banking ombudsman support.**
- *Seeds:* `re_no_reply_30d` · `re_unsatisfactory_reply` · `digital_payment_failure` · `card_charge_dispute` · `credit_report_correction`.
- *Suitability:* Free complaint-ready pack (complaint to the RE, Internal Ombudsman reminder, RB-IOS draft fields) — the complainant files; Equator is not a representative before the RBI Ombudsman; optional Equator conciliation only if both the RE and the customer prefer it and no RB-IOS complaint is pending.
- *Law:* RB-IOS 2026 effective 1 Jul 2026 (30-day RE window; 90-day filing window; caps ₹30 lakh + ₹3 lakh) — master X-13 [V]; RE-specific Internal Ombudsman Directions 14 Jan 2026 (auto-escalation within 20 days; final reply 30 days) [V GLOBAL_CORRECTIONS #7]; RB-IOS not maintainable where a court or arbitrator is seized [V S3 A0.1]; authorised-representative rules under RB-IOS 2026 **[VERIFY — open: whether a non-advocate authorised representative may file]**.
- *Signpost / exclusions:* RBI CMS portal (cms.rbi.org.in) [K]; 1930 for fraud.
- *Build notes:* No fee for the pack (D2-18 "free routes first"); grievance-ladder clock engine PI-FIN-01.

**PK-SPT — Sports.**
- *Seeds:* `sponsorship_contract` · `player_agency_contract` · `league_franchise` · `event_services` · `selection_or_eligibility` (signpost) · `anti_doping` (exclude).
- *Suitability:* Commercial sports contracts are arbitrable and mediable (COM rules); governance, selection and eligibility disputes go to sports bodies, the statutory sports tribunal or the courts; anti-doping excluded.
- *Law:* National Sports Governance Act 2025 (National Sports Tribunal) **[VERIFY — open: Act number, commencement notification and Tribunal constitution]**; National Anti-Doping Act 2022 [K]; Court of Arbitration for Sport for international-federation matters [K].
- *Signpost / exclusions:* Sports body grievance mechanism → statutory tribunal/High Court; NADA appeal panels (exclude).
- *Build notes:* Panel endorsement `sports_law`; confidentiality ring for athlete medical data (sealed).

**PK-MDE — Media and entertainment.**
- *Seeds:* `production_agreement` · `distribution_ott_licence` · `royalty_accounting` · `music_licensing` · `talent_contract` · `civil_defamation_settlement`.
- *Suitability:* Contract, licence and royalty disputes arbitrable; expert determination for royalty audits; civil defamation mediable; criminal defamation excluded.
- *Law:* Copyright Act 1957 (assignment ss.18–19; licences s.30; copyright societies s.33) [K]; appellate functions of the abolished IPAB moved to High Courts/Commercial Courts by the Tribunals Reforms Act 2021 [K]; licence disputes arbitrable (*Eros International v Telemax Links*, Bom HC, 12 Apr 2016 [K]); BNS s.356 criminal defamation (exclude) [K]; IT Rules 2021 Part III grievance levels for digital media content (signpost) [K]; certification under the Cinematograph Act 1952 (exclude) [K].
- *Signpost / exclusions:* EXC-13 registry actions; content-regulation complaints to the publisher's grievance officer/self-regulatory body.
- *Build notes:* Royalty-statement reconciliation calculator (user figures); escrow for minimum guarantees.

**PK-IPC — IP and creative work (freelancers, designers, creators, influencers).**
- *Seeds:* `unpaid_creative_fees` · `ip_assignment_dispute` · `usage_beyond_licence` · `brand_collab_contract` · `attribution_credit`.
- *Suitability:* N/M first (relationship and small values); arbitration where agreed; expert determination for usage valuation of the parties' own figures only (no Equator valuation).
- *Law:* Licence/royalty/assignment disputes arbitrable; registry grant/revocation in rem (*Vidya Drolia*) [K]; MSMED Act route if the creator is a Udyam-registered micro/small enterprise (MSEFC; CM-G-03) [V]; CCPA Guidelines on endorsements (regulatory complaints excluded) **[VERIFY — open: instrument name and date]**.
- *Signpost / exclusions:* EXC-13; MSEFC; Commercial Court for urgent injunctions (URG-09).
- *Build notes:* Evidence capture of posts/screens with hash (NN-10) and type copies (App. L).

**PK-GOV — Government contracts.**
- *Seeds:* `bill_payment_delay` · `ld_deduction` · `termination_and_bg` · `price_variation` · `procurement_blacklisting` (exclude: public-law).
- *Suitability:* Negotiation and a mediation brief for the counterparty's High-Level Committee; arbitration normally only where the dispute value is < ₹10 crore or approval is uploaded (R-COM-13).
- *Law:* Department of Expenditure (Procurement Policy Division) OM dated 3 Jun 2024 on arbitration and mediation in domestic public procurement [V S2 F6] (file number to be read from the original **[VERIFY — open: OM file number]**); Mediation Act ss.48–49 (government) not in force [V]; blacklisting/debarment challenges are public-law matters (EXC-15).
- *Signpost / exclusions:* HLC of the ministry/CPSE; MSEFC where the supplier is micro/small; High Court writ for blacklisting.
- *Build notes:* `govt_counterparty` flag; DoE threshold calculator CAL-17; approval-evidence upload.

**PK-XBE — Cross-border e-commerce.**
- *Seeds:* `b2c_foreign_seller` (Indian consumer v foreign online seller) · `b2c_indian_seller_foreign_buyer` · `b2b_marketplace_cross_border` (routes to INT).
- *Suitability:* B2C — mediation only, never arbitration against a consumer; B2B — INT rules (consent-award conversion for enforceability, NN-19).
- *Law:* E-Commerce Rules 2020 apply to e-commerce entities not established in India that systematically offer goods/services to consumers in India [V RES_A1b Q18]; UNCITRAL Technical Notes on Online Dispute Resolution (2016) [K]; Singapore Convention excludes consumer disputes (Art. 1(2)) [K]; EU ODR platform discontinued **[VERIFY — open: Regulation (EU) 2024/3228 and platform closure date]**; FEMA route for refunds (INT-G-07).
- *Signpost / exclusions:* Indian Consumer Commission; card-network chargeback through the issuing bank; sanctions gate (EXC-36).
- *Build notes:* Multi-currency quotes (INR + USD/EUR/GBP/SGD/AED, D7); DPDP s.16 transfer record; GDPR notice for EU parties (NN-30).

**PK-CMY — Community and neighbourhood.**
- *Seeds:* `noise_nuisance` · `boundary_or_wall` · `drainage_or_water` · `pets` · `parking` · `shared_staircase_or_terrace`.
- *Suitability:* Mediation only, low or no fee (FFS-2 eligible); optional panel including a respected local person chosen by both sides (mirrors the community-mediation design of Mediation Act s.44, not in force).
- *Law:* Mediation Act 2023 ss.43–44 (community mediation; not in force) [V R2]; public nuisance — Magistrate's powers under BNSS 2023 s.152 [K] and CPC s.91 suits [K]; Indian Easements Act 1882 [K].
- *Signpost / exclusions:* Police 112 for threats or violence (EXC-05); municipal authority for building-rule violations; civil court for injunctions (URG-09).
- *Build notes:* RWA tenant programmes; Hindi-first copy; outcome = neighbourhood agreement (contract), no award.

---

## 8. Data model, APIs, events, errors and configuration

Conventions per Appendix F (UUIDv7 `id`, `std_cols`, tenant RLS via `rls.enable_tenant_rls`, encrypted `*_enc`, retention columns). These tables are additions to Appendix F §F.4.3/§F.4.11 (to be merged by P02).

### 8.1 DDL

```sql
-- 8.1.1 Explorer v2 (extends core.explorer_sessions from P02 §7.2)
ALTER TABLE core.explorer_sessions
  ADD COLUMN schema_version text NOT NULL DEFAULT 'v2' CHECK (schema_version IN ('v1','v2')),
  ADD COLUMN entry_role text CHECK (entry_role IN ('claimant_individual','respondent','representative','business','joint')),
  ADD COLUMN tree_version_id uuid,                                   -- explorer tree pinned (NN-21)
  ADD COLUMN pack_versions jsonb NOT NULL DEFAULT '[]',              -- [{pack, version_id}]
  ADD COLUMN ruleset_version_id uuid, ADD COLUMN fee_schedule_version_id uuid,
  ADD COLUMN result_code text CHECK (result_code IN ('RES-01','RES-02','RES-03','RES-04','RES-05','RES-06','RES-07','RES-08','RES-09')),
  ADD COLUMN overlay_codes text[] NOT NULL DEFAULT '{}',
  ADD COLUMN exclusion_codes text[] NOT NULL DEFAULT '{}',           -- EXC-nn only, never narrative
  ADD COLUMN urgent_codes text[] NOT NULL DEFAULT '{}',              -- URG-nn only; detail in safety_sealed
  ADD COLUMN saved_at timestamptz, ADD COLUMN resume_token_hash char(64), ADD COLUMN resume_contact_hmac char(64),
  ADD COLUMN resume_consent_record_id uuid REFERENCES core.consent_records(id),
  ADD COLUMN respondent_notice_id uuid,                              -- respondent path from an Equator notice
  ADD COLUMN quick_exit_count int NOT NULL DEFAULT 0,
  ADD CONSTRAINT saved_needs_consent CHECK (saved_at IS NULL OR resume_consent_record_id IS NOT NULL);

CREATE TABLE core.explorer_answers (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  session_id uuid NOT NULL REFERENCES core.explorer_sessions(id), question_id text NOT NULL,   -- EXU-nn / EXV-...
  tree_version_id uuid NOT NULL, answer_codes text[], answer_value_enc bytea,                  -- codes for choices; enc for amounts/dates/text
  source text NOT NULL CHECK (source IN ('user','ai_suggestion_confirmed','prefill_confirmed')),
  superseded_at timestamptz, answered_at timestamptz NOT NULL DEFAULT now(),
  retention_class text NOT NULL DEFAULT 'explorer_session', retain_until date, legal_hold boolean NOT NULL DEFAULT false);
SELECT rls.enable_tenant_rls('core','explorer_answers');
CREATE UNIQUE INDEX explorer_answers_current ON core.explorer_answers(session_id, question_id) WHERE superseded_at IS NULL;

CREATE TABLE core.explorer_categories (                -- EXU-02 life-area tiles
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, label_i18n jsonb NOT NULL, examples_i18n jsonb NOT NULL,
  targets jsonb NOT NULL,                                -- [{vertical, pack, l1_codes[]}]
  sort_order int NOT NULL, pack_flag text, active boolean NOT NULL DEFAULT true, UNIQUE (tenant_id, code));

CREATE TABLE core.explorer_synonyms (                  -- deterministic search index (not AI)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, locale text NOT NULL, term citext NOT NULL,
  target_vertical text NOT NULL, target_l1 text, target_l2 text, weight numeric(5,2) NOT NULL DEFAULT 1,
  pack_version_id uuid, UNIQUE (tenant_id, locale, term, target_vertical, target_l1, target_l2));
CREATE INDEX explorer_synonyms_trgm ON core.explorer_synonyms USING gin (term gin_trgm_ops);   -- requires pg_trgm

-- 8.1.2 Exclusions and urgent triggers
CREATE TABLE core.exclusion_catalogue (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL, version int NOT NULL,              -- EXC-nn
  title_i18n jsonb NOT NULL, behaviour text NOT NULL CHECK (behaviour IN ('exclude','split','arbitration_blocked','signpost_first')),
  blocks_arbitration boolean NOT NULL, blocks_mediation boolean NOT NULL,
  civil_route_i18n jsonb, forum_codes text[] NOT NULL, legal_rule_ids text[] NOT NULL CHECK (cardinality(legal_rule_ids) > 0),
  ldta_rule_id text, copy_i18n jsonb NOT NULL, verticals text[] NOT NULL, tenant_id uuid,   -- tenant rows may only be stricter
  status text NOT NULL CHECK (status IN ('draft','in_review','active','superseded')), UNIQUE (tenant_id, code, version));

CREATE TABLE core.urgent_triggers (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL UNIQUE,                             -- URG-nn
  title_i18n jsonb NOT NULL, copy_i18n jsonb NOT NULL, task_role text, task_sla_minutes int,
  suppress_joint_session boolean NOT NULL DEFAULT true, force_quick_exit boolean NOT NULL DEFAULT true);
CREATE TABLE core.helplines (
  id uuid PRIMARY KEY DEFAULT uuidv7(), trigger_code text NOT NULL REFERENCES core.urgent_triggers(code),
  scope text NOT NULL,                                   -- 'IN' or ISO 3166-2 state code
  name_i18n jsonb NOT NULL, number text, url text, hours text, languages text[],
  last_verified_at date, verified_by uuid, reverify_due_at date NOT NULL,
  display_allowed boolean GENERATED ALWAYS AS (last_verified_at IS NOT NULL) STORED);         -- unverified numbers never shown

ALTER TABLE core.signposting_directory
  ADD COLUMN is_free boolean, ADD COLUMN must_approach_first boolean NOT NULL DEFAULT false,
  ADD COLUMN ldta_rule_id text, ADD COLUMN urgent_capable boolean NOT NULL DEFAULT false,
  ADD COLUMN letter_template_code text, ADD COLUMN pack_version_id uuid;

-- 8.1.3 Dispute packs and form bindings
CREATE TABLE core.dispute_packs (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL UNIQUE CHECK (code ~ '^PK-[A-Z0-9]{2,4}$'),
  host_vertical core.vertical_code NOT NULL, case_code char(3),                                -- case_code required when host = 'XPN'; may be shared by related packs
  title_i18n jsonb NOT NULL, owner_user_id uuid NOT NULL, feature_flag text NOT NULL,
  CHECK (host_vertical <> 'XPN' OR case_code IS NOT NULL));
CREATE TABLE core.dispute_pack_versions (
  id uuid PRIMARY KEY DEFAULT uuidv7(), pack_id uuid NOT NULL REFERENCES core.dispute_packs(id),
  semver text NOT NULL CHECK (semver ~ '^[0-9]+\.[0-9]+\.[0-9]+$'), manifest jsonb NOT NULL, manifest_sha256 char(64) NOT NULL,
  lifecycle text NOT NULL CHECK (lifecycle IN ('draft','validating','in_review','approved','pilot','published','deprecated','retired')),
  validation_report jsonb, maker_id uuid NOT NULL, checker_id uuid, legal_approval_ref text, rules_committee_ref text,
  ai_oversight_eval_run_id uuid, board_fee_approval_ref text, dpia_ref text,
  published_at timestamptz, deprecated_at timestamptz,
  CHECK (checker_id IS NULL OR checker_id <> maker_id),
  CHECK (lifecycle NOT IN ('approved','pilot','published') OR (checker_id IS NOT NULL AND legal_approval_ref IS NOT NULL)),
  UNIQUE (pack_id, semver));
CREATE TABLE core.dispute_pack_artifacts (
  pack_version_id uuid NOT NULL REFERENCES core.dispute_pack_versions(id), artifact_type text NOT NULL
    CHECK (artifact_type IN ('taxonomy','rules','legal_rule_ref','explorer_tree','form_schema','form_binding','template','clock',
                             'fee_schedule_ref','panel_policy','calculator','integration_binding','signposting_row','guardrail_pack',
                             'copy','document_checklist','kpi','test_set')),
  ref_id uuid, ref_code text, sha256 char(64) NOT NULL, PRIMARY KEY (pack_version_id, artifact_type, sha256));
CREATE TABLE core.pack_activations (
  id uuid PRIMARY KEY DEFAULT uuidv7(), pack_version_id uuid NOT NULL REFERENCES core.dispute_pack_versions(id),
  tenant_id uuid REFERENCES core.tenants(id),           -- NULL = platform-wide
  mode text NOT NULL CHECK (mode IN ('pilot','live')), traffic_percent int CHECK (traffic_percent BETWEEN 0 AND 100),
  starts_at timestamptz NOT NULL, ends_at timestamptz, approved_by uuid NOT NULL);
CREATE TABLE core.explorer_tree_versions (
  id uuid PRIMARY KEY DEFAULT uuidv7(), pack_version_id uuid NOT NULL REFERENCES core.dispute_pack_versions(id),
  vertical text NOT NULL, l1_code text NOT NULL, tree jsonb NOT NULL, golden_set_ref text NOT NULL, UNIQUE (pack_version_id, vertical, l1_code));
CREATE TABLE core.form_bindings (
  id uuid PRIMARY KEY DEFAULT uuidv7(), ruleset_version_id uuid NOT NULL, pack_version_id uuid REFERENCES core.dispute_pack_versions(id),
  purpose text NOT NULL, vertical text NOT NULL DEFAULT '*', l2_code text NOT NULL DEFAULT '*', mechanism text NOT NULL DEFAULT '*',
  party_role text NOT NULL DEFAULT '*', jurisdiction text NOT NULL DEFAULT '*',
  blocks uuid[] NOT NULL CHECK (cardinality(blocks) > 0),                                      -- ordered core.form_schema_versions ids
  specificity int GENERATED ALWAYS AS ((CASE WHEN l2_code<>'*' THEN 32 ELSE 0 END)+(CASE WHEN mechanism<>'*' THEN 16 ELSE 0 END)
     +(CASE WHEN party_role<>'*' THEN 8 ELSE 0 END)+(CASE WHEN jurisdiction<>'*' THEN 4 ELSE 0 END)+(CASE WHEN vertical<>'*' THEN 2 ELSE 0 END)) STORED,
  UNIQUE (ruleset_version_id, purpose, vertical, l2_code, mechanism, party_role, jurisdiction));
-- vertical_code enum: migration adds 'XPN' (K-D-08); core.verticals row XPN with enabled_by_default=false, feature_flag 'vertical.xpn.enabled'.

-- 8.1.4 Pre-litigation engagement (§5)
CREATE TABLE core.prelit_engagements (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  case_id uuid NOT NULL UNIQUE REFERENCES core.cases(id),
  mechanism_mode text NOT NULL CHECK (mechanism_mode IN ('mediation_contractual','conciliation_part3')),
  state text NOT NULL CHECK (state IN ('draft','suitability_check','signposted','notice_ready','invitation_sent','delivered','bounced',
    'address_research','viewed','responded','consent_pending_signature','consented','negotiation_assisted','non_commencement',
    'neutral_appointed','pre_session','in_session','suspended','settled_in_principle','drafting','signed','partial_settlement',
    'not_settled','output_conversion','compliance_tracking','closed')),
  respondent_kind text NOT NULL CHECK (respondent_kind IN ('individual','organisation')),
  invitation_sent_at timestamptz, response_deadline date, extension_used boolean NOT NULL DEFAULT false,
  response_type text CHECK (response_type IN ('accept','accept_with_conditions','decline','counter_offer','object_forum','request_info','request_extension')),
  decline_reason_enc bytea,                                -- sealed to case manager; never shown to claimant (NN-16)
  contact_count int NOT NULL DEFAULT 0 CHECK (contact_count <= 6),
  ffs_option text CHECK (ffs_option IN ('FFS-1','FFS-2','FFS-3','FFS-4')), funding_source text,
  funding_disclosure_shown_at timestamptz,
  standstill_signed boolean NOT NULL DEFAULT false, arbitration_agreement_signed boolean NOT NULL DEFAULT false,
  consent_document_id uuid, outcome text CHECK (outcome IN ('signposted','non_commencement_declined','non_commencement_no_response',
    'non_commencement_unreachable','withdrawn_by_claimant','settled_full','settled_partial','not_settled','suspended_safety','performed','breached')),
  output_instruments text[] NOT NULL DEFAULT '{}' CHECK (output_instruments <@ ARRAY['msa_contract','conciliation_s73','consent_award_s30',
    'lok_adalat_pack','irc_settlement_pack','court_recording_pack','s12a_form1_pack']),
  ruleset_version_id uuid NOT NULL,
  CHECK (standstill_signed = false OR state <> 'draft'),
  CHECK (NOT ('conciliation_s73' = ANY(output_instruments)) OR mechanism_mode = 'conciliation_part3'));
SELECT rls.enable_case_rls('core','prelit_engagements');
ALTER TABLE core.cases ADD COLUMN is_prelit boolean NOT NULL DEFAULT false;          -- §5.2 mapping
ALTER TABLE core.offers ADD COLUMN min_open_days int CHECK (min_open_days IS NULL OR min_open_days >= 14),
                        ADD COLUMN without_prejudice boolean NOT NULL DEFAULT true;   -- PL-08 (prelit offers)
```

### 8.2 APIs (`/v1`; OpenAPI 3.1)

| Method & path | Purpose | Auth | Idempotency |
|---|---|---|---|
| POST `/explorer/sessions` | Start v2 session (consent ref, locale, entry hints, `respondent_notice_code?`) | anonymous + CAPTCHA / party | I |
| GET `/explorer/sessions/{id}/next` | Next page definition (question schema, options, i18n) from pinned tree | session token | — |
| PUT `/explorer/sessions/{id}/answers/{questionId}` | Record/replace one answer; returns next page id and any interrupt | session token | — |
| GET `/explorer/categories?locale=&q=` | Tiles and deterministic search results | anonymous | — |
| POST `/explorer/sessions/{id}/narrative` | Optional free text → classification candidates (AI) + cue scan | session token | I |
| POST `/explorer/sessions/{id}/save` | Save with resume contact (consent ref) → sends magic link | session token | I |
| POST `/explorer/resume` | Exchange magic link + OTP for a session token | anonymous | — |
| POST `/explorer/sessions/{id}/result` | Compute result + report v2 (deterministic) | session token | I |
| GET `/explorer/sessions/{id}/report?format={html, pdf or share}` | Fetch report | session token / share token | — |
| DELETE `/explorer/sessions/{id}` | Quick exit / delete answers | session token | — |
| POST `/forms/resolve` | Resolve form composition for a key (§4.5) | party, staff, machine | — |
| GET `/signposting/forums?vertical=&l1=&state=` | Directory lookup (public subset) | anonymous | — |
| POST `/prelit/engagements` | Create engagement from a report (`explorer_session_id`) | party | I |
| POST `/prelit/engagements/{id}/notice:approve` | Claimant approves notice (OTP/e-sign intent) | party | I |
| POST `/prelit/engagements/{id}/invitation:send` | Dispatch D0 invitation (journey start) | case_manager / system | I |
| GET `/prelit/invitations/{code}` | Respondent view (after OTP) | notice link | — |
| POST `/prelit/invitations/{code}/responses` | Accept / propose / ask / extend / decline | respondent | I |
| POST `/prelit/engagements/{id}/consent:sign` | Start e-sign of Agreement to Mediate / s.62 acceptance | party | I |
| POST `/prelit/engagements/{id}/offers` | Structured offer (≥ 14 days open) | party | I |
| POST `/prelit/engagements/{id}/conversion` | Choose output instruments | party (both) + case_manager | I |
| GET `/prelit/engagements/{id}/genuine-steps-log` | "Record of pre-action steps" PDF | party | — |
| POST `/admin/dispute-packs` · POST `/admin/dispute-packs/{code}/versions` | Create pack / upload version (manifest + artefacts) | institution_admin | I |
| POST `/admin/dispute-packs/{code}/versions/{v}:validate` · `:submit` · `:approve` · `:pilot` · `:publish` · `:deprecate` · `:retire` | Lifecycle transitions (maker–checker) | per §6.5 roles | I |
| GET `/admin/dispute-packs/{code}/versions/{v}/validation-report` | VAL-01…VAL-17 results | staff | — |

### 8.3 Domain events (`equator.<context>.<entity>.<verb>.v1`; payloads carry codes and IDs only — never narrative, names or safety detail)

| Event | Key payload | Consumers |
|---|---|---|
| `equator.intake.explorer_session.started.v1` (exists) | session_id, entry_role, locale, versions | RPT |
| `equator.intake.explorer_answer.recorded.v1` | session_id, question_id, answer_codes (no values for sensitive items) | RPT (funnel), TMP |
| `equator.intake.explorer_interrupt.shown.v1` | session_id, urg_codes | AUD, safeguarding queue |
| `equator.intake.explorer_exclusion.triggered.v1` | session_id, exc_codes, behaviour | RPT, AUD |
| `equator.intake.explorer_result.computed.v1` | session_id, result_code, overlay_codes, route_codes, forum_codes, rule_trace_id | RPT, AUD |
| `equator.intake.explorer_session.saved.v1` / `.resumed.v1` | session_id | RPT |
| `equator.intake.explorer_report.generated.v1` (exists) | session_id, report_id, schema `v2` | RPT |
| `equator.routing.signposting.recorded.v1` (exists) | forum_code, ldta, source=`explorer` | AUD, CLK |
| `equator.forms.binding.resolved.v1` | key hash, binding_id, score | RPT |
| `equator.prelit.engagement.created.v1` | engagement_id, case_id, mechanism_mode | AUD, TMP |
| `equator.prelit.invitation.sent.v1` / `.delivered.v1` / `.bounced.v1` / `.viewed.v1` | engagement_id, channel | NOT, RPT, CLK |
| `equator.prelit.response.received.v1` | engagement_id, response_type | NOT, TMP, RPT |
| `equator.prelit.engagement.consented.v1` | engagement_id, consent_document_id | P04 proceeding creation, BIL |
| `equator.prelit.engagement.non_commenced.v1` | engagement_id, outcome | NOT, RPT |
| `equator.prelit.session.held.v1` | engagement_id, session_no, format | RPT |
| `equator.prelit.settlement.signed.v1` | engagement_id, partial (bool) | P06, RPT, WH |
| `equator.prelit.outcome.converted.v1` | engagement_id, instrument | P06, RPT |
| `equator.prelit.compliance.closed.v1` | engagement_id, performed/breached | RPT, ENT |
| `equator.rules.dispute_pack.version_submitted.v1` / `.approved.v1` / `.published.v1` / `.deprecated.v1` / `.retired.v1` | pack_code, semver, manifest_sha256 | AUD, cache invalidation, SRCH |

Webhook-eligible (W): `prelit.invitation.sent`, `prelit.response.received`, `prelit.engagement.consented`, `prelit.settlement.signed`, `prelit.compliance.closed` — never for `sealed` tier.

### 8.4 Errors (Appendix F.10 format; new codes to be registered in F.10 per X-20, plus existing canonical codes marked "exists")

| Code | HTTP | Message (en) | Source |
|---|---|---|---|
| `EXPLORER_SESSION_EXPIRED` | 410 | This session has ended. You can start again. | §1.4 |
| `EXPLORER_QUESTION_NOT_CURRENT` | 409 | Please answer the current question first. | §2 |
| `MATTER_EXCLUDED` | 422 | Equator cannot take this matter. See the forums listed. (`rule` = EXC code; `available_routes` = signposts) | §3 |
| `URGENT_INTERRUPT_ACTIVE` | 409 | Please see the help options before continuing. | §3.4 |
| `FORM_BINDING_NOT_FOUND` | 500 (alerts) | Form configuration missing. Reference: {instance}. | §4.5 (should be impossible after VAL-05) |
| `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` (exists, F.10.1) | 422 | This mechanism is not available for this type of dispute. | §4.5 |
| `PRELIT_CONTACT_CAP_REACHED` | 409 | The contact limit for this invitation has been reached. | §5.4 |
| `CONTACT_OUTSIDE_WINDOW` (exists, F.10.1) | 409 | Contact is allowed only between 08:00 and 19:00 local time. | NN-12 |
| `PRELIT_CONSENT_INCOMPLETE` | 409 | All parties must sign before a mediator is appointed. | §5.2 |
| `PRELIT_OFFER_PERIOD_TOO_SHORT` | 422 | An offer must stay open for at least 14 days. | §5.6 |
| `PRELIT_CONVERSION_NOT_ELIGIBLE` | 422 | This form of settlement is not available for this matter. (`rule` = missing precondition) | §5.8 |
| `PACK_VALIDATION_FAILED` | 422 | The dispute pack failed validation. (`violations` = VAL ids) | §6.4 |
| `PACK_WIDENS_MATRIX` | 422 | A pack cannot allow a process the platform forbids. | §6.3 |
| `PACK_CODE_IN_USE` | 409 | This code is used by existing matters and cannot be removed. | VAL-04 |
| `HELPLINE_UNVERIFIED` | 409 | This helpline must be verified before it is shown. | §3.4 |

### 8.5 Feature flags and configuration keys

| Key | Default | Notes |
|---|---|---|
| `explorer.v2.enabled` | ON (staging) / OFF (prod until K-AT suite green) | v1 remains as fallback for 90 days |
| `explorer.respondent_path.enabled` | ON | §2.5 |
| `explorer.save_resume.enabled` | ON | §1.4 |
| `explorer.task_list_mode.enabled` | ON | Business path (K-D-02) |
| `explorer.quick_exit_url` | `https://www.google.co.in/` | K-D-03 |
| `explorer.session_ttl_days` / `explorer.saved_ttl_days` / `explorer.safety_saved_ttl_days` | 7 / 30 / 7 | §1.4 |
| `explorer.max_vertical_pages_p80` | 8 | VAL-09 |
| `copy.readability_max_grade` | 8 | VAL-07 |
| `vertical.xpn.enabled` | OFF | K-D-08 |
| `pack.<code>.enabled` | OFF | §7 |
| `prelit.enabled` | ON | §5 |
| `prelit.cadence.<vertical>` | §5.4 defaults | per vertical overrides in V §8 |
| `prelit.contact_cap` | 6 | Anti-harassment |
| `prelit.default_mechanism_rule` | `K-D-07` | §5.1 |
| `prelit.free_first_session.enabled` | ON | FFS-1 |
| `concession.prelit_pro_bono` | ON (Board-approved budget required) | FFS-2 |
| `prelit.standstill_template` | OFF | Counsel Q-C1 |
| `prelit.lok_adalat_pack` | OFF | Counsel Q-C8 |
| `prelit.irc_settlement_pack` | OFF | Counsel Q-C3 |
| `mediation_statutory_mode` / `com.s12a_equator_authorised` | OFF | Existing (NN-05, M-06) |

### 8.6 New Appendix G rule areas

Extend the `area` list (G.3) with `EXCL` (exclusions/signposting) and `XPN` (expansion packs); extend the CHECK `rule_id ~ '^LR-[A-Z]+-[0-9]{3}$'` (already compatible). Seed rows: `LR-EXCL-001…040` mirroring EXC-01…EXC-40 (effect `protective`; may activate with VERIFY markers per G.1), and `LR-XPN-001…` per pack (permissive rules — e.g. "XPN pack may offer arbitration for B2B commercial lease" — stay inactive until verified).

---

## 9. Acceptance tests (Gherkin; `tests/acceptance/explorer_v2/*.feature`)

```gherkin
Feature: Dispute Explorer v2, exclusions, result types, pre-litigation and dispute packs

  Scenario: K-AT-01 NN-01_explorer_v2_no_merits_on_suitable_result
    Given a completed session classified FIN personal_loan with result RES-01
    When the report v2 is generated in en and hi
    Then no string contains any term in the GX-1/GX-2/GX-3 lexicon ("strong", "weak", "chance", "likely", "worth", "you will get")
    And the result headline is "Mediation and other options can help with this"

  Scenario: K-AT-02 Universal page order puts safety before value
    Given a new anonymous session
    When the user answers EXU-01, EXU-02 and EXU-03
    Then the next page is EXU-04 "Is anyone in danger, or is something urgent?"
    And EXU-09 has not been shown

  Scenario: K-AT-03 NN-02_parity_explorer_v2
    Given the 200 golden fact sets for all six verticals in en and hi
    When each set is run through the AI-assisted flow and through the questionnaire with the AI kill switch ON
    Then result_code, route_codes, exclusion_codes, forum_codes, clocks and fee quotes are identical for every set

  Scenario: K-AT-04 Self-harm cue interrupts and hands off
    Given a session in any vertical
    When the user selects "I am thinking of hurting myself" at EXU-04
    Then the interrupt page shows "Tele-MANAS 14416" and "112"
    And a warm human handoff is offered on the same page
    And no further questions are shown on that page
    And only the code URG-05 is stored in core.explorer_sessions.urgent_codes and no text is logged

  Scenario: K-AT-05 Quick exit leaves no trace
    Given a FAM session with two answers recorded
    When the user presses Esc twice
    Then the browser location is replaced with the configured explorer.quick_exit_url
    And DELETE /v1/explorer/sessions/{id} is called
    And local storage for the session is empty
    And the back button does not return to the Explorer page

  Scenario: K-AT-06 Save and resume without revealing the dispute
    Given a FAM session where the user chooses "Save and come back later" with a mobile number
    When the resume SMS is sent
    Then the SMS text does not contain the words "family", "divorce", "custody", "maintenance" or the category name
    And the link expires after explorer.safety_saved_ttl_days days
    And no reminder message is ever scheduled for the session

  Scenario: K-AT-07 Anonymous start
    Given a visitor who is not logged in
    When the visitor completes the universal flow and a vertical tree
    Then no name, identity document or other-party name was required
    And the report with route, forums and fee is shown

  Scenario: K-AT-08 NN-20_free_forum_first_insurance
    Given an INS retail health reimbursement claim whose written representation to the insurer was rejected by a reply dated 02 Apr 2026
    When the result is computed
    Then the result is RES-04
    And "Insurance Ombudsman — free" is listed above every Equator option with last date 02 Apr 2027
    And arbitration is absent from the route set with reason "retail policyholder"
    And a signposting event is recorded with source "explorer"

  Scenario: K-AT-09 NN-24_sexual_offence_excluded
    Given a session where EXU-05 includes "sexual_offence"
    When the result is computed
    Then the result is RES-06 then RES-05 with exclusion EXC-02
    And no Equator fee, invitation or filing CTA is shown
    And forum cards show police 112 and Childline 1098 only if their helpline rows are verified

  Scenario: K-AT-10 NN-24_cheque_bounce_split
    Given a COM matter where a cheque bounced and a complaint is pending at the evidence stage
    When the result is computed
    Then the result is RES-03 with exclusion EXC-07
    And "Equator can help you agree" lists payment terms
    And "Only the court can" lists closing the cheque case
    And the compounding pack and the stage cost note citing Sanjabij Tari (2025 INSC 1158) are offered

  Scenario: K-AT-11 Mediation does not pause limitation
    Given any report with a limitation pill
    Then the text "Private mediation or conciliation does not stop these dates running" appears under the pills
    And no Explorer or prelit template contains "pause", "stop the clock" or "extend your deadline"

  Scenario: K-AT-12 Respondent path from an Equator notice
    Given a respondent opens a notice link and passes OTP
    When the respondent selects "This is not about me"
    Then an identity-mismatch task is created for the case manager with a 2-working-day SLA
    And no further invitation reminders are sent until the task is resolved

  Scenario: K-AT-13 Triple talaq is never recorded
    Given a FAM session where EXU-05 includes "instant_talaq"
    When the result is computed
    Then EXC-03 is triggered
    And no template, form or route that records or describes the talaq as effective is available
    And civil terms (mahr, subsistence allowance, custody, return of goods) are offered only after the safety screen

  Scenario: K-AT-14 Accessibility of question pages
    Given every universal and vertical question page in en and hi
    Then axe reports no WCAG 2.2 AA violations
    And each page has exactly one h1 equal to the question, a Back link and a single primary "Continue" button
    And date questions use three separate day, month and year fields

  Scenario: K-AT-15 Form resolution is deterministic and specific
    Given bindings for FIN/*/conciliation/*/*/request and FIN/digital_lending/conciliation/claimant/*/request
    When /v1/forms/resolve is called for FIN, digital_lending, conciliation, claimant, IN-RJ, request
    Then the binding with specificity 58 is returned
    And the same call with the same pinned ruleset always returns the same blocks

  Scenario: K-AT-16 Prohibited mechanism has no form
    When /v1/forms/resolve is called for INS, health_reimbursement, arbitration, claimant, IN-DL, statement_of_claim
    Then the response is 422 MECHANISM_NOT_PERMITTED_FOR_VERTICAL

  Scenario: K-AT-17 Pre-litigation default mechanism for a company respondent
    Given a COM b2b supply_goods claim of ₹4,20,000 against a company with outcome "payment"
    When the claimant starts a pre-litigation invitation
    Then the mechanism_mode defaults to conciliation_part3
    And the invitation states "Invitation to conciliation under Part III of the Arbitration and Conciliation Act, 1996"
    And the response deadline is 30 days from D0

  Scenario: K-AT-18 NN-12_prelit_contact_cap_and_window
    Given an invitation to an individual respondent with 6 outbound contacts already made
    When the cadence engine schedules another reminder
    Then the reminder is refused with PRELIT_CONTACT_CAP_REACHED
    And any contact scheduled at 19:30 local time is refused with CONTACT_OUTSIDE_WINDOW

  Scenario: K-AT-19 s.73 label only for Part III conciliation
    Given a prelit engagement with mechanism_mode mediation_contractual that settles
    When the parties choose output instruments
    Then conciliation_s73 is not selectable
    And the MSA template label is "Mediated Settlement Agreement (contract) under the Equator Mediation Rules"

  Scenario: K-AT-20 NN-21_explorer_pins_versions
    Given a session started under ruleset v14 and pack PK-FIN 2.3.0
    When PK-FIN 2.4.0 is published during the session
    Then the session's report shows ruleset v14 and PK-FIN 2.3.0
    And the routes are computed under the pinned versions

  Scenario: K-AT-21 Pack cannot widen the mechanism matrix
    Given a draft PK-HLT version whose rules offer arbitration to a patient
    When the version is validated
    Then validation fails with PACK_WIDENS_MATRIX and VAL-03

  Scenario: K-AT-22 Pack publication requires all approvals
    Given a PK-TEN version with VAL-01 to VAL-17 green but no legal_approval_ref
    When an institution_admin attempts to publish it
    Then the transition is refused
    And the maker cannot act as checker

  Scenario: K-AT-23 NN-24 coverage in every pack tree
    Given any pack version submitted for validation
    When VAL-08 runs
    Then for each criminal-element code and each URG code the tree resolves to the expected EXC or URG outcome

  Scenario: K-AT-24 Unverified helpline is never shown
    Given helpline row "NALSA 15100" with last_verified_at null
    When URG-12 is triggered
    Then the number is not displayed and the forum name and website are shown instead

  Scenario: K-AT-25 Funding-neutrality disclosure on FFS-3
    Given a portfolio-funded invitation from a lender tenant
    Then the respondent invitation shows "The organisation pays Equator's fee. This does not affect who the mediator is or how they act."
    And funding_disclosure_shown_at is recorded before consent can be signed

  Scenario: K-AT-26 POSH details are never collected
    Given a WRK session where EXU-05 includes "sexual_harassment_work"
    Then no free-text field is shown on the following pages
    And the report names the Internal Committee and Local Committee with the 3-month date to watch
    And no POSH content is stored in core or sent to the AI gateway
```

---

## 10. Open items and counsel questions (this appendix)

| # | Item | Effect until resolved |
|---|---|---|
| K-OI-01 | BNSS 2023 section numbers for compounding (s.359) and limitation on cognizance (s.514) **[VERIFY]** | Copy shows section numbers only after verification; behaviour unaffected |
| K-OI-02 | Helplines marked [K]: 181, 1098, 14567, 108, NCW; NALSA 15100 **[VERIFY]** | Rows stay `display_allowed = false` until verified (K-AT-24) |
| K-OI-03 | Income-tax Act 2025 first-appeal section and period (EXC-14) | LDTA shown as "check the date on your order" |
| K-OI-04 | ISA s.213 omission — Act number and Gazette reference (D2-25) | Probate copy as per V3 |
| K-OI-05 | Waqf (Amendment) Act 2025 commencement and effect on s.83 (EXC-29) | Signpost only |
| K-OI-06 | Revenue-court partition provisions per launch State (EXC-38; carried from V0470) | Split behaviour with generic revenue-authority card |
| K-OI-07 | ONDC IGM/ODR provider onboarding (PK-ECM); Telecommunications Act 2023 repeal commencement (PK-TEL); National Sports Governance Act 2025 commencement (PK-SPT); Multi-State Co-operative Ombudsman section (PK-COP); State tenancy law list (PK-TEN); EU ODR platform closure (PK-XBE); CCPA endorsement guidelines (PK-IPC); DoE OM file number (PK-GOV); MACT solatium (PK-MAC); RB-IOS 2026 representation rule (PK-BOS) | Packs stay OFF; permissive rules inactive |
| K-OI-08 | *ICICI Lombard v Ayiti Navaneetha* order date and text (MV Act s.166(3)) | SC note hidden; 6-month pill shown with "confirm with the Tribunal" |
| Q-C1 | Standstill/tolling agreement validity during private mediation or Part III conciliation (Contract Act s.28; Limitation Act; A&C s.81 and Limitation Act s.18 acknowledgements) | `prelit.standstill_template` OFF |
| Q-C3 | Binding effect of an Equator-mediated settlement for an IR Code "worker"; form and filing needed | `prelit.irc_settlement_pack` OFF |
| Q-C8 | Which DLSAs accept joint pre-litigation applications with pre-agreed terms under LSA Act s.20(2); stamp-duty position of Lok Adalat awards per State | `prelit.lok_adalat_pack` OFF |
| Q-C9 | Whether a pending Equator conciliation engages the Insurance Ombudsman r.14(5) bar or RB-IOS non-maintainability | Explorer treats an Ombudsman-seized matter as "Ombudsman first" (§2.4) |
| Q-C10 | DPDP s.17(1)(a) coverage of Equator contacting respondents pre-consent on the claimant's instruction | Lawful-basis record mandatory before `invitation_sent` |
| Q-K1 | Whether the paid "Explorer human review" (D2-18) by non-advocate case managers, limited to process information, raises any Advocates Act 1961 / BCI issue; required disclaimers | Product live with process-only script; counsel memo before scaling |
| Q-K2 | Whether Equator may offer B2C consumer mediation in a way that a Consumer Commission will treat as relevant to costs or conduct, and the form of the settlement memo the Commission will record | PK-CNS stays OFF |

---

## Phase addendum (paste into P02)

> Scope addition to P02 (Case Core). These requirements supersede FR-P02-01 to FR-P02-06 where they differ and are part of the P02 exit gate. Screens SCR-P02-23 onward are allocated here (Appendix C to be updated in the same PR).

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P02-V2-01 | **Explorer v2 flow engine.** Implement the universal flow EXU-01…EXU-13 (App. K §2.2) as a page-per-question engine driven by `core.explorer_tree_versions`, with the page order of K-D-01, branching per §2.1, and hand-off to vertical trees per §2.6. | K-AT-02, K-AT-14 pass; every page has one `h1`, Back link, one "Continue", "Leave this page", "Save and come back later"; per-question funnel events emitted |
| FR-P02-V2-02 | **Category picker and search.** Life-area tiles (§2.3) from `core.explorer_categories`; deterministic synonym search from `core.explorer_synonyms` with trigram tolerance (add `pg_trgm` to Appendix F §F.2 extensions); ≤ 6 results; zero-result terms aggregated weekly without session IDs. | Search for "salary nahi mila" returns WRK `wages_ff` in top 3; "EMI settle" returns FIN OTS; no LLM call made by search |
| FR-P02-V2-03 | **Respondent, representative and business paths** (§2.5), including identity-mismatch task (2 working days) and task-list mode for businesses (K-D-02). | K-AT-12 passes; representative report shows the "Authority you will need" block (NN-27) |
| FR-P02-V2-04 | **Save, resume, anonymous start, quick exit** per §1.4 and K-D-03; consent purpose `explorer_resume` added to the P01 catalogue; neutral SMS/email copy; safety-session limits. | K-AT-05, K-AT-06, K-AT-07 pass |
| FR-P02-V2-05 | **Exclusion engine** (`packages/rules/exclusions`) with the evaluation order of §3.1 and the register EXC-01…EXC-40 seeded into `core.exclusion_catalogue` and Appendix G as `LR-EXCL-001…040` (protective). | K-AT-09, K-AT-10, K-AT-13, K-AT-26 pass; every fact set yields ≥ 1 forum or route; each forum named writes a signposting event |
| FR-P02-V2-06 | **Urgent and safety triggers** URG-01…URG-13 with `core.urgent_triggers` and `core.helplines`; interrupt page SCR-P02-25; cue codes only in core, detail in `safety_sealed`; safeguarding tasks with SLAs; unverified helplines never displayed. | K-AT-04, K-AT-24 pass; verified helplines: 112, 14416/1-800-891-4416, 1930 at launch; others after `legal_reviewer` verification |
| FR-P02-V2-07 | **Criminal-element handling** per §3.3 (exclude / split / parallel-aware), including compounding packs for NI Act s.147 and the "court alone decides" copy. | K-AT-10 passes; copy-lint blocks arrest/prosecution wording (FL-G-08) |
| FR-P02-V2-08 | **Result types RES-01…RES-09** with precedence and copy (§4.1); blocked "suitable" wording (K-D-09). | K-AT-01 passes; every computed session stores `result_code` and overlays |
| FR-P02-V2-09 | **Readiness & Pathway Report v2** (`explorer_report.v2` JSON schema; sections 0–11, §4.2), HTML/PDF/share variants; route cards (§4.3); limitation block with the fixed "does not stop these dates" sentence. | K-AT-08, K-AT-11 pass; PDF carries hash + `/verify` QR; share view omits private answers and limitation pills |
| FR-P02-V2-10 | **Next-step CTAs** (§4.4) including free letter downloads, free process call-back (08:00–19:00) and paid `request_human_review` (fee from Appendix O; free for vulnerable users). | Free forum button has equal visual weight (NN-29 lint); call-back script contains no merits language (GX-1 eval) |
| FR-P02-V2-11 | **Limitation and parallel-proceedings screens** (§2.4) reading only Appendix G rules; "needs condonation" state for Insurance Ombudsman; exceptions copy for s.12A(3) and MSEFC conciliation. | Golden vectors for each anchor in §2.4 pass; no hard-coded periods in code (static check) |
| FR-P02-V2-12 | **Form-resolution service** `POST /v1/forms/resolve` (§4.5) over `core.form_bindings`, with composition of base + binding blocks + jurisdiction and mechanism overlays; mechanism guard. | K-AT-15, K-AT-16 pass; VAL-05 enumerates all reachable keys in CI |
| FR-P02-V2-13 | **Dispute-pack registry** (`core.dispute_packs`, `core.dispute_pack_versions`, `core.dispute_pack_artifacts`, `core.pack_activations`), lifecycle API (§8.2) and validation pipeline VAL-01…VAL-17 (§6.4); the six verticals re-expressed as platform packs `PK-FIN`…`PK-INT`. | K-AT-21, K-AT-22, K-AT-23 pass; maker ≠ checker enforced by DB CHECK |
| FR-P02-V2-14 | **`XPN` extension vertical** (K-D-08): enum migration, `core.verticals` row (flag `vertical.xpn.enabled` OFF), pack-level `case_code` in case numbering, most-restrictive default mechanism set. | Creating an XPN case without an active pack fails; case number `EQ/CNS/JAI/2027/00001` generated for a PK-CNS pilot case |
| FR-P02-V2-15 | **Pinning** of ruleset, tree, pack and fee-schedule versions on every session and case (NN-21). | K-AT-20 passes |
| FR-P02-V2-16 | **Pre-litigation engagement core** — `core.prelit_engagements` (§8.1.4), state machine §5.2 with guards, case-state mapping, creation from an Explorer report. | Engagement cannot reach `invitation_sent` without lawful-basis record, copy-lint pass and no active URG; transitions audited and evented (§8.3) |
| FR-P02-V2-17 | **Invitation builder** (§5.3) with claimant approval, case-manager neutrality edit, verify page `/v/{code}` (App. R §5; `/verify/notice/{code}` redirects), vernacular pairing and copy-lint PL-15. | Lint blocks every term in §5.3 list; verify page shows case ID, sender and status only |
| FR-P02-V2-18 | **Respondent response portal** (≤ 3 screens to consent; accept / propose / ask / extend once ≤ 14 days / decline with sealed reason), choice of 1 of 3 slots and 1 of 3 allocation-generated neutrals, language and mode. | Decline reason never visible to claimant or used in grading/allocation (NN-16, NN-28); median screens to consent ≤ 3 in usability test |
| FR-P02-V2-19 | **Consent capture** (§5.5): Agreement to Mediate or s.62 acceptance via eSign/DSC with sub-consents unticked by default; organisation authority; representative scope. | `consented` impossible without every party's signature (`PRELIT_CONSENT_INCOMPLETE`); arbitration-agreement sub-consent shows "You do not have to sign this to mediate" for consumers and individual employees |
| FR-P02-V2-20 | **Free first session options** FFS-1…FFS-4 (§5.7) with fee display including GST and funding-neutrality disclosure. | K-AT-25 passes; no countdown/urgency copy (NN-29 lint) |
| FR-P02-V2-21 | **Genuine-steps log** export ("Record of pre-action steps") and Non-Commencement Notice / Closure Report templates with allowed labels (§5.8). | Blocked labels absent; PIMS disclaimer footer present on Non-Commencement Notice |
| FR-P02-V2-22 | **Pre-litigation KPIs** (§5.9) as read models with "commenced" and "filed" denominators shown separately; public statistics gated at n ≥ 100 per vertical and n ≥ 10 per published cell (X-28). | Dashboard shows both denominators; publication blocked below threshold |
| FR-P02-V2-23 | **Screens**: SCR-P02-23 Universal question page (template) · SCR-P02-24 Check your answers · SCR-P02-25 Urgent help interrupt · SCR-P02-26 Exclusion / split result · SCR-P02-27 Report v2 · SCR-P02-28 Respondent options · SCR-P02-29 Save and resume · SCR-P02-30 Pre-litigation invitation (respondent view) · SCR-P02-31 Pack registry (Studio) · SCR-P02-32 Pack validation report. Mobile parity for SCR-P02-23 to SCR-P02-30. | axe clean (WCAG 2.2 AA); EN/HI parity; Playwright and Maestro journeys for claimant, respondent and representative |
| FR-P02-V2-24 | **Seed and tests**: 200 golden Explorer fact sets (all verticals, EN + HI) incl. ≥ 40 exclusion/urgent sets; K-AT-01…K-AT-26 in CI; NN tests `NN-01`, `NN-02`, `NN-20`, `NN-21`, `NN-24` extended to v2. | All green; zero ZT guardrail failures |

## Phase addendum (paste into P04)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P04-V2-K01 | On `equator.prelit.engagement.consented.v1`, create the proceeding matching `mechanism_mode` (contractual mediation or Part III conciliation) with pinned rules; `negotiation_assisted` creates a `negotiation` proceeding for structured offers. | Proceeding exists within 1 minute of consent; mode immutable after the first session |
| FR-P04-V2-K02 | Structured pre-litigation offers: `min_open_days ≥ 14`, without-prejudice flag, sealed decline reasons (Singapore O.5 model). | `PRELIT_OFFER_PERIOD_TOO_SHORT` on < 14 days |
| FR-P04-V2-K03 | Free first session (30–45 min) session type `information_and_options` with continuation only on both parties' on-screen consent and fee acceptance. | No substantive session starts without recorded consent |
| FR-P04-V2-K04 | Time standards per App. K §5.8 (Appendix A `med_contract_timebox` values by vertical) with outer contractual cap 120 + 60 days (policy mirror of Mediation Act s.18) as owned clocks (NN-04). | Clock owner mandatory; T-30 escalation fires in tests |
| FR-P04-V2-K05 | Conversion guards: `conciliation_s73` only if the proceeding ran as Part III from the start; consent award only with an arbitration agreement and a different neutral by default (master §5.3). | K-AT-19 passes |

## Phase addendum (paste into P07)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P07-V2-K01 | Pre-litigation cadence journey (§5.4) as configurable `prelit.cadence.<vertical>` with contact cap 6, 08:00–19:00 window, public-holiday block and DND/consent checks. | K-AT-18 passes |
| FR-P07-V2-K02 | DLT/WhatsApp utility templates for invitation, reminders and final notice in EN, HI and each enabled locale; FAM neutral template. | Template approval IDs stored; FAM SMS contains no category words (K-AT-06 pattern) |
| FR-P07-V2-K03 | One primary conversational channel per respondent (web assistant or WhatsApp). | A second bot channel cannot be opened for the same engagement |
| FR-P07-V2-K04 | Speed Post via `POSTAL_PORT` for organisation respondents or value ≥ ₹3 lakh; proof stored in the evidence ledger. | Tracking number and delivery proof attached to the genuine-steps log |

## Phase addendum (paste into P08)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P08-V2-K01 | Each vertical spec V1–V6 §5 tree is authored as an `explorer_tree_versions` artefact inside its platform pack and meets the §2.6 contract. | VAL-08, VAL-09, VAL-11, VAL-12 green for every L1 |
| FR-P08-V2-K02 | Each vertical's §8 pre-litigation overrides are expressed as `prelit.cadence.<vertical>` and conversion-eligibility rules, not code. | Overrides visible in the pack manifest |
| FR-P08-V2-K03 | Vertical exclusions not in EXC-01…EXC-40 are added as pack EXC rows with Appendix G `LR-EXCL-*` rules. | No exclusion exists only in code |

## Phase addendum (paste into P09)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P09-V2-K01 | Portfolio protocols (PL-16): enterprise tenants pre-agree acceptance of Equator invitations, SLAs and FFS-3 funding with the funding-neutrality statement. | Disclosure shown to every respondent (K-AT-25) |
| FR-P09-V2-K02 | Webhooks for the W-marked prelit events (§8.3), never for sealed tier. | Subscription to a sealed event type rejected |
| FR-P09-V2-K03 | `CONNECTOR_PORT.ondc_igm` behind `pack.ecm.enabled` once K-OI-07 is resolved. | Connector disabled while flag OFF |

## Phase addendum (paste into P11)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P11-V2-K01 | `intake_assistant` v2 operates only at EXU-13 and on clarifying questions; outputs `IntakeResult.v2` classification candidates mapped to taxonomy codes; may not set result codes, exclusions or routes. | Eval `explorer_routing` 100%; `guardrails_zt` 100% |
| FR-P11-V2-K02 | Cue classifier for URG codes in EN, HI and enabled locales; recall ≥ 0.98 on the safety eval set; no cue text logged. | Eval report attached to the model card |
| FR-P11-V2-K03 | Pack guardrail packs (§6.3) loaded per classification; AI Oversight approval recorded per pack version. | Release blocked without `ai_oversight_eval_run_id` |

## Phase addendum (paste into P13)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P13-V2-K01 | Public `/explore` pages server-rendered entry with Explorer CTA on home and vertical pages; "free forum first" block on every vertical landing page (NN-20). | Build check passes (no client-only shell) |
| FR-P13-V2-K02 | Expansion landing pages generated from pack CMS blocks only when the pack is `published`; no "coming soon" claims without a Claims Register entry (NN-17). | Unpublished packs produce no indexable pages |
| FR-P13-V2-K03 | Exclusion explainer page ("What Equator does not do") listing EXC categories in plain language with forum links. | Page passes readability ≤ grade 8 |

## Phase addendum (paste into P00)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P00-V2-K01 | Ruleset Studio gains editors for taxonomy, explorer trees, form bindings and pack manifests with maker–checker (P00 config-change pattern). | Maker cannot approve own change (DB CHECK) |
| FR-P00-V2-K02 | Appendix G areas extended with `EXCL` and `XPN`; activation validator applies the G.1 fail-safe principle to `LR-EXCL-*` (protective) and `LR-XPN-*` (permissive). | Permissive `LR-XPN-*` row with VERIFY pending cannot be activated |
