# Appendix R — Case-Status Portal, Case Desk, Publication of Awards and Settlements, Execution and Registration Support, Certified Copies

> Binding reference (master §17) for **P02** (§1, §2, §5 verification hooks), **P06** (§3, §4, §5), **P04** (applications, sessions and orders that feed §1), **P12** (mobile layouts) and **P13** (public Decisions Library pages). Read with the master (NN-01, NN-04, NN-07, NN-08, NN-09, NN-10, NN-11, NN-16, NN-17, NN-20, NN-26, NN-27, NN-30), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-25, R-26, R-27, R-36; D2-10, D2-11), Appendix A (§2 case machine), C (§G tracker), F (DDL, events, errors), G (legal rules), L (visibility model, court formats), S (portals, representatives, RBAC). Requirements map: R-25 → §3; R-26 → §4; R-27 → §1–§2; R-36 → §4.

---

## 0. Scope, precedence and reconciliations

**What this appendix adds.** (1) A full case-status portal — the "Know where your matter stands" experience — modelled on the information architecture of the Supreme Court and e-Courts case-status services (case details, papers, applications, listings, orders, office report, tagged matters) but **access-controlled**, because ADR is private (A&C Act 1996 s.42A; s.75; Mediation Act 2023 s.22 applied as policy until notified); (2) the per-case working desk for parties, neutrals and case managers; (3) the publication programme for awards, settlements and digests with consent, redaction and a public Decisions Library; (4) the execution, implementation and registration support layer; (5) certified copies and verification. It extends — never repeats — P02 FR-P02-43/44/48, P06 FR-P06-17/18/20–27 and Appendix C §G.

**Precedence.** Master → Appendix G (legal rules) → Appendix F (names, types, events, errors) → this appendix → phase files (master §15). New tables, events and error codes listed in §6 are added to Appendix F in the same PR that creates them.

**Copy principle (binding on every string in this appendix).** Equator is never a court. Banned when describing Equator, its people, processes or outputs (UI, documents, URLs, identifiers): "court", "judge", "bench", "coram", "cause list", "decree" (for Equator outputs), "judgment", "listed before", "INSC", "Hon'ble". Approved substitutes: *tribunal* (arbitration only), *mediator*, *conciliator*, *expert*, *session list*, *registry note*, *application*, *order or direction*, *award*, *settlement*, *decision*. A court is named only when a court acts (challenge, execution, compounding, registration, s.13B decree). Copy lint rule `R-LINT-01` enforces this (P13 claims/copy linter; NN-17).

| ID | Reconciliation / decision | Reason | Effect |
|---|---|---|---|
| R-R1 | Human references stay as the master defines: filing reference `FR-{YYYYMMDD}-{6 Crockford}` at filing (the SC "diary number" analogue) and case number `EQ/{VERT}/{CITY}/{YYYY}/{NNNNN}` at acceptance (FR-P02-48). S8's 16-character "ECN" is **not adopted**. | Master §4.4 prevails; two numbering systems confuse parties and courts. | SMS keyword and IVR accept the case number with or without slashes (`EQFINJAI202700042`). |
| R-R2 | FR-P02-44 tracker is extended: the second factor may be **either** an OTP to a contact point on the case **or** the party's **Case Verification Code (CVC)** printed on that party's acknowledgement and notices. Party-name search exists only for authenticated users and returns only matters where the user is a party or holds an active authority. | Brief (search by reference + verification code; party name with OTP); s.42A; anti-enumeration. | §1.2. |
| R-R3 | Arbitrator identity is **not** shown in the verified public view (L1), only to case members (L2+). | FR-P02-44, Appendix C §G.1 (s.42A). | Header field `neutrals` is L2+. |
| R-R4 | Publication is **opt-in by every party** for every vertical and seat. S5's ICC-style opt-out for foreign-seated INT awards and its "template consent in the enterprise MSA" for FIN/INS digests are **rejected**. | NN-26 (every party's informed, recorded, revocable consent); D2-10. | §3.4. |
| R-R5 | Publication **modes** keep the S8/V3/V6 codes P0–P4 + E. Redaction is a separate axis: **redaction profiles RP-1…RP-8** (derived from S8 classes R1–R6). | The brief's "redaction profiles (P0–P4)" conflated the two; V3 §13.5 and V6 §13.5 already use P0–P4 as modes. | §3.2, §3.6. |
| R-R6 | Statistics suppression threshold is **n < 10** per cell (k ≥ 10), not S5's n < 5. | P06 FR-P06-27 and V6 §14 already fixed k ≥ 10. | §3.2. |
| R-R7 | Takedown after consent withdrawal: **within 2 working days and never later than 72 hours**. | Harmonises FR-P06-27 (2 WD) and S8 (72 h). | §3.11. |
| R-R8 | New canonical table `core.case_applications` (applications register). P04's `POST /proceedings/{pid}/applications` writes to it; V6 `intl.procedural_applications` becomes a 1:1 extension keyed by `case_application_id`. | P04 defines the API but no table; the SC "IA" view needs one register. | §6.1; P04 addendum. |
| R-R9 | Institutional challenge-decision publication (SIAC r.28.7 model) stays behind flag `publication.challenge_decisions.enabled` = OFF until counsel answers Q-R1/Q-R2. | s.42A risk; V6 flag `intl.publish_challenge_decisions` is merged into this flag. | §3.10. |
| R-R10 | Screen IDs reserved: `SCR-P02-80…99`, `SCR-P06-60…79`, `SCR-P13-60…69`. | Appendix C rule; L-D-13 reserved 60–79 (P02) and 40–59 (P06). | Appendix C updated in the same PR. |

---

## 1. Case-status portal — "Know where your matter stands"

### 1.1 Access layers

| Layer | Who | How they get in | Session | What they see |
|---|---|---|---|---|
| **L0 Public** | Anyone | No verification | — | Tracker entry page; Decisions Library (§3.9); document verification (§5). Nothing about any specific case. |
| **L1 Verified status** | A person holding the reference and a second factor | Case number or filing reference + CAPTCHA + (CVC **or** OTP to a contact point already on the case) | 30 minutes, read-only, no cookies beyond the session | Status card, plain-language stage, next date and purpose, mechanism, "what happens next" (generic form), "who decides" chip, public-safe events (Appendix C §G.3). Party names as initials only. |
| **L2 Case member** | Parties, `party_org_user`, representatives within scope (NN-27; App. S §4.3 `view_documents` scope), enterprise users of an organisational party | Portal login (App. S §2) + case membership | Portal session | Full portal (§1.4) filtered by the document audience model (App. L §2) and §1.5 matrix |
| **L3 Neutral** | Appointed, confirmed neutrals; `tech_concierge` (metadata only) | Neutral portal + confirmed appointment | Neutral session | Full portal + neutral-only items (own caucus notes, deliberation room, draft orders) |
| **L4 Registry** | `case_manager`, `registrar`, `deputy_registrar`, `case_counsel`, `quality_officer` | Staff portal (aal2-pr) | Staff session | Everything except caucus notes, sealed stores and blind-bid values |
| **L5 Scoped audit** | `auditor` under a time-bound grant | Admin portal | ≤ 90-day grant | Read-only, watermarked, logged |

Restricted matters return at L1 only the sentence "Status available to parties in their account": confidentiality tier `sealed`, every FAM case, INS cases carrying a `health_data_token`, cases with `safety_flag = true`, and any matter linked to a POSH token (FR-P02-44 retained).

### 1.2 Search modes

| Mode | Route | Inputs (field_id · type · validation) | Who | Returns |
|---|---|---|---|---|
| S1 Reference + CVC | `/track` | `trk.ref` text — matches `^EQ/[A-Z]{3}/[A-Z]{3}/\d{4}/\d{5}$`, the slash-less form, or `^FR-\d{8}-[0-9A-HJKMNP-TV-Z]{6}$`; `trk.cvc` text 10 chars Crockford base32, case-insensitive, hyphen optional (`XXXXX-XXXXX`); `trk.captcha` (audio alternative) | Anyone holding the notice | L1 view |
| S2 Reference + OTP | `/track` → "Send a code instead" | `trk.ref`; `trk.channel` radio {SMS, WhatsApp, Email} showing only masked contact points already on the case (`98****3210`); `trk.otp` 6 digits, 5-minute TTL | Party or representative | L1 view |
| S3 My matters (party name) | `/app/matters/search` | `srch.name` text ≥ 3 chars; `srch.role` {any, claimant side, respondent side}; `srch.vertical`; `srch.status`; `srch.year` | Authenticated (≥ K1, OTP-verified mobile) | Only cases where the caller's person/organisation is a `core.case_parties` row or the caller holds an active authority (App. S §4) — never a global search |
| S4 Representative search | `/app/counsel/matters` | client name, case number, organisation, status, next-date range | `counsel`, `representative`, firm admin | Matters under active authorities only |
| S5 Registry search | `/console/search` | case number, filing reference, party name, PAN-HMAC, CIN, CNR of a linked court case, neutral, case manager, status, clock state | L4 | Tenant cases (OpenSearch, non-sealed index) |
| S6 SMS / WhatsApp / IVR | keyword `STATUS <case number>`; IVR menu 3 | Sender number must be a verified contact point on the case; IVR adds OTP | Parties | Stage and next date in the notice language (Appendix C §G.1) |

**CVC rules.** One CVC per `case_party` (so every L1 view is attributable to a party), generated at acceptance (or at filing for the filing side), 50 bits of entropy, stored as HMAC-SHA-256 with a tenant pepper, printed on the acknowledgement, every notice to that party and the case-history statement. Rotated on request (`POST /v1/cases/{caseId}/parties/{partyId}/cvc:rotate`, step-up), automatically on revocation of a representative authority, and on a safety flag. Five failed CVC attempts on one reference lock S1 for that reference for 60 minutes; the lock is silent (uniform response).

**Anti-enumeration (all modes).** Identical response text and timing (±50 ms jitter) whether or not a case exists; 5 lookups/hour/IP; 3 OTPs/hour/case; L1 views logged to `audit.access_log` with `purpose = status_l1`, mode and party; a burst of > 20 distinct references per IP per day blocks the IP for 24 hours and raises a security event.

### 1.3 Case header (`CaseHeader` component; SCR-P02-80)

| Field id | Label (en) | Source | L1 | L2 | L3 | L4 |
|---|---|---|---|---|---|---|
| `hdr.case_number` | Case number | `core.cases.case_number` (CaseNumber component with copy + QR) | ✔ | ✔ | ✔ | ✔ |
| `hdr.filing_ref` | Filing reference | `filing_reference` | ✔ | ✔ | ✔ | ✔ |
| `hdr.vertical` | Type of dispute | vertical label (FIN "Financial & loan", COM "Commercial & business", FAM "Family & property", INS "Insurance", WRK "Workplace", INT "International commercial") | ✔ | ✔ | ✔ | ✔ |
| `hdr.subtype` | Category | L1 › L2 taxonomy labels (App. K) | — | ✔ | ✔ | ✔ |
| `hdr.mechanism` | How it is being resolved | current proceeding mechanism ("Mediation", "Arbitration (documents only)", "Conciliation", …) | ✔ | ✔ | ✔ | ✔ |
| `hdr.filed_on` | Filed on | `filed_at` (date, IST) | ✔ | ✔ | ✔ | ✔ |
| `hdr.registered_on` | Accepted on | `accepted_at` | ✔ | ✔ | ✔ | ✔ |
| `hdr.status` | Status | public label (Appendix C §G.2) | ✔ | ✔ | ✔ | ✔ |
| `hdr.stage` | Stage | proceeding-state label (§1.8.2), e.g., "Pleadings — statement of defence due" | — | ✔ | ✔ | ✔ |
| `hdr.next_date` | Next date | next session or deadline relevant to the viewer: date, time, purpose | ✔ (date + purpose only) | ✔ | ✔ | ✔ |
| `hdr.neutrals` | Tribunal / Mediator / Conciliator / Expert | confirmed appointments; label by mechanism; grade badge and profile link (App. N) | — | ✔ | ✔ | ✔ |
| `hdr.case_manager` | Your case manager | name + case desk contact (role mailbox and desk number; never a personal phone) | — | ✔ | ✔ | ✔ |
| `hdr.seat_venue` | Seat / venue | arbitration: "Seat: Jaipur · Venue: online"; other mechanisms: "Online" or venue city | — | ✔ | ✔ | ✔ |
| `hdr.language` | Language | `languages[]` with interpreter flag | — | ✔ | ✔ | ✔ |
| `hdr.rules` | Rules applying | pinned procedure-rules version with link (NN-21) | — | ✔ | ✔ | ✔ |
| `hdr.value` | Value in dispute | claim + counterclaim totals (₹ Indian grouping; INT currency + INR equivalent) | — | ✔ | ✔ | ✔ |
| `hdr.tier` | Confidentiality | badge `standard`/`high`/`sealed` (SealedBanner) | — | ✔ | ✔ | ✔ |
| `hdr.who_decides` | Who decides at this step | chip (§1.4.12) | ✔ | ✔ | ✔ | ✔ |
| `hdr.next_sentence` | What happens next | sentence (§1.4.11) | ✔ (generic) | ✔ | ✔ | ✔ |

### 1.4 Panels (tabs on web; cards on mobile)

Panels render from the CQRS read model `core.case_status_views` (one JSON document per case per audience class, rebuilt on every relevant event, p95 < 2 s lag). Every row carries `as_of` and a hash link to its evidence-ledger entry where one exists.

**1.4.1 Parties and representatives (SCR-P02-81).** Columns: party label (Claimant 1, Respondent 2 …) · name (organisation name; individuals' full names to L2+ only) · role · joined on · service status (served / deemed served on {date} under {rule} / not yet served) · representatives (name, type badge "Advocate — Bar Council of Rajasthan R/1234/2015" or "Authorised representative — HR officer", scope chips, valid until) · contact for service (masked). Never shown to the other side: vulnerability flags, screening outcomes, safety addresses, KYC level, personal phone/email of the party (service contacts are masked to the other side and visible to the registry).

**1.4.2 Papers filed register (SCR-P02-82).** One row per document version that has entered the case record (`visibility_state ∈ {FILED, RETURNED, ON_RECORD, SERVED, SUPERSEDED, WITHDRAWN, ISSUED}`; App. L §2.1):

| Column | Content |
|---|---|
| Paper no. | `P-{n}` gap-free per case in order of filing (not exhibit numbers; exhibits shown in a sub-row `C-1…C-14`) |
| Document | title + `doc_kind` label (Statement of claim, Statement of defence, Counterclaim, Reply, Application, Evidence affidavit, Expert report, Written submissions, Settlement draft, Order, Award, Notice, Registry note …) |
| Filed by | side label (Claimant 1 / Respondent / Tribunal / Mediator / Registry); representative name if filed under authority |
| Filed on | date and time IST (and viewer zone if different) |
| Pages | page count; volume count for bundles |
| Status | Received · Under check · Returned for correction (with defects list) · On record · Served on {date} · Withdrawn on {date} · Superseded by P-{n} |
| Visibility | All parties · Own side · Mediator only · Registry only · Sealed (label from audience keys; App. L §2.2) |
| Actions | View (watermarked per tier), Download (policy), Verify hash, Request certified copy (§5) |

Rows a viewer may not see are **absent**, not greyed (existence of a caucus share or another side's private filing is itself confidential). Filters: filed by, kind, status, date range, has exhibits. Sort default: newest first; "Chronological" toggle.

**1.4.3 Applications register (SCR-P02-83).** From `core.case_applications`. Columns: App. no. (`A-{n}` per case) · type · filed by · filed on · relief sought (≤ 200 characters, filer-written) · response due by · status · decision (order link) · decided on. Type dropdown (`DD-R-APP-TYPE`): `adjournment` · `extension_of_time` · `s29a_consent_extension_record` · `interim_measure_s17` · `emergency_arbitrator` · `document_production` · `amendment_of_pleadings` · `additional_evidence` · `condonation_of_delay_rules` · `joinder` · `consolidation` · `security_for_costs` · `early_determination` · `preliminary_issue` · `recording_consent` · `interpreter_or_accessibility` · `change_of_mode_or_venue` · `non_advocate_representation_leave` · `protective_order_confidentiality` · `s33_correction_interpretation_additional` · `neutral_challenge_s13` (opens the P03 challenge workflow) · `mediator_replacement_request` · `recall_after_s38_termination` · `withdrawal_of_claim` · `stay_record_court_order` · `other`. Status values (`DD-R-APP-STATUS`): `filed` · `returned_for_correction` · `response_invited` · `response_received` · `for_session` · `allowed` · `allowed_in_part` · `rejected` · `withdrawn` · `not_pressed` · `infructuous`. Mediation proceedings show only logistics applications (adjournment, interpreter, mode, replacement); substantive requests in mediation are discussed in session, not docketed.

**1.4.4 Notices and service history (SCR-P02-84).** Columns: notice no. · type (notice of commencement, s.21 request, invitation to mediate, s.62 invitation to conciliate, session notice, order service, award delivery, deficiency notice, default notice) · to (party label) · language and "Translation for convenience" label where machine-translated (NN-32) · channels attempted (icons with result chips: delivered/read/bounced/refused/returned) · served on / deemed served on + rule (A&C s.3; Rules art.) · certificate (service certificate PDF with hash). Each party sees notices addressed to any party (service is not confidential between parties) but **not** the other party's contact addresses.

**1.4.5 Hearings and sessions (SCR-P02-85).** Columns: date · time (IST + viewer zone) · kind (joint session, case management meeting, evidence hearing, final hearing, documents-only determination, mediation session, site visit) · mode (video, audio, phone dial-in, in person, hybrid) · purpose (`DD-R-SESSION-PURPOSE`: first meeting/procedural meeting · pleadings timetable · interim application · evidence — claimant witnesses · evidence — respondent witnesses · expert evidence · final submissions · mediation session · settlement signing · award delivery meeting) · neutral(s) · attendance (per side: attended / did not attend / excused; individual names L2+) · result (held · adjourned — reason category · cancelled · part-heard) · record (arbitration: minutes or the procedural order of that day; transcript only where recorded with all-party and tribunal consent — NN-11) · next date. **Caucus meetings** appear only to the side concerned and the mediator, labelled "Separate meeting"; the other side sees nothing. **Mediation sessions have no minutes**: the row shows "No record is kept of what is said in mediation" and only logistics (date, attendance, next date) (NN-11; Mediation Act s.22 policy mirror; A&C s.75).

**1.4.6 Orders and directions (SCR-P02-86).** From `core.orders` + institutional decisions. Columns: order no. · date · kind (procedural order, direction, interim measure s.17, extension, adjournment, termination, jurisdiction ruling s.16, costs, consolidation, emergency arbitrator order) · issued by (Tribunal / Emergency arbitrator / Registrar / Challenge Committee) · one-line summary (written by the issuer; AI may draft the summary, human approves — NN-01) · signed PDF (QR, hash) · service status · directions it creates (each a row in the directions tracker, §2.2). A separate sub-section **Institution decisions** lists appointment confirmations, challenge decisions, extensions under the Rules and consolidation decisions with reasons (S5 C1 `InstitutionalDecision`).

**1.4.7 Final outcome (SCR-P02-87).** One card per outcome instrument: type (award · consent award (A&C s.30) · additional/corrected award (s.33) · conciliation settlement (s.73, status under s.74) · mediated settlement agreement (contract) · non-settlement report · non-commencement report · signposting record) · date · signed by (roles; names L2+) · e-stamp certificate no. (NN-09) · delivered to each party on (s.31(5)) · windows (s.33 request until; s.34 challenge until — per party) · status (delivered · final · under challenge · set aside · in execution · satisfied) · actions (download — parties and representatives in scope; request certified copy; open execution desk §4; verify). Award text and settlement terms are visible only to the parties, their representatives in scope, the neutral(s) and the registry (s.42A; s.75). L1 shows only "Outcome issued on {date}" and never for restricted matters.

**1.4.8 Payments and deposits (SCR-P02-88).** Timeline rows: fee quotes and invoices (filing, administration, neutral fee deposits per party share), payments, refunds and credit notes, deposit directions under s.38, escrow account events (funded, milestone evidence submitted, released, paused — NN-13), instalment plan status, stamp-duty pass-through, certified-copy fees. Each party sees its own invoices and payments in full; for shared deposits it also sees the other side's share as "Paid / Not paid" (needed for the s.38(2) right to pay the defaulting party's share). Neutrals see deposit status per side (paid/unpaid) and their own fee notes only. Amounts in ₹ with Indian grouping; INT in invoice currency with INR equivalent and FX snapshot date.

**1.4.9 Registry note (office-report analogue; SCR-P02-89).** Auto-generated at T-2 working days before every session and on demand; signed by the case manager; versioned. Sections: (1) header — case number, session date/time/mode, neutral(s); (2) linked matters to be taken together; (3) last session and last order (date, one-line); (4) papers since last session ("No new paper has been filed since {date}" when true); (5) service status per party; (6) compliance with each open direction (due, complied on / not complied / extension sought); (7) pending applications with response status; (8) deposits status per side; (9) clocks — days left on s.29A, s.23(4), mediation period, response windows (with owner role); (10) defects outstanding; (11) logistics — interpreter, accessibility accommodations (never the reason), dial-in; (12) **registry-only notes** (L4 only, never rendered into the party/neutral version). Template `eqr.tpl.registry_note.v1`, render profile `EQR_TRIBUNAL`.

**1.4.10 Linked and earlier matters (SCR-P02-90).** `core.linked_matters` rows (consolidated, parent/child, related, parallel forum, sequenced, escalated from GRM) and **earlier/parallel proceedings** in other forums (forum, case number, CNR where available, stage, last date) — mandatory capture for FIN (DRT/SARFAESI), COM (NCLT/commercial court), FAM (family court) per S8 §2.1. Court case numbers are public records and shown to L2+; an eCourts CNR status lookup is offered through `CONNECTOR_PORT` (`ecourts`) where available, else manual entry. A POSH link is an opaque token and is never displayed (NN-07).

**1.4.11 What happens next (sentence engine).** Deterministic, rule-table driven (`dashboard_pack.next_sentence` config, legal-approved; never AI-generated — NN-01). Inputs: case state, proceeding state, mechanism, viewer side, next clock due date. Strings live in the Appendix P copy deck (`sts.*` keys, §4.4): this rule table selects the key, and the viewer-specific rows below are added there as `sts.{state}.next.{viewer_side}` variants; where no variant exists, P's `sts.{state}.next` default is shown (one string source, FR-P02-V2-P01 and FR-P02-V2-R05 build one engine). Examples (en):

| Condition | Sentence |
|---|---|
| `awaiting_respondent`, viewer = claimant | "The other party has until {due} to respond. If they don't, we will tell you your options." |
| `awaiting_respondent`, viewer = respondent | "Please tell us by {due} whether you will take part. You can ask questions before you decide." |
| arbitration, `pleadings`, SoD due | "The statement of defence is due on {due}. The tribunal will then fix the next steps." |
| mediation, session scheduled | "Your next mediation session is on {date} at {time}. Nothing is decided unless you both agree." |
| award `delivered`, s.34 window open | "The award was delivered on {date}. A court challenge, if any, must be filed by {s34_due}." |
| settlement `executed`, obligations open | "The next payment of {amount} is due on {due}. We will remind both sides 7 days before." |
| `signposted` | "This matter suits {forum}. The last date to approach it is {date}." |
| `in_execution` | "Enforcement is with the court. Update the latest court step here so we can remind you." |

**1.4.12 Who decides chip.** Values (`DD-R-WHO-DECIDES`; the single vocabulary for the `WhoDecidesChip`, including Appendix P §4.4's "Who decides now" column): "You decide together" (negotiation, mediation, conciliation sessions) · "You decide" (accepting an offer or signing) · "The other party decides whether to take part" (invitation stage) · "The case team checks the papers" (scrutiny — form, never merits) · "The arbitral tribunal decides" · "The emergency arbitrator decides" · "The expert decides the questions referred" · "The Equator Challenge Committee decides" (s.13 agreed procedure) · "A court decides" (challenge, execution, compounding, s.13B decree, registration refusal) · "The Sub-Registrar registers" (registration).

**1.4.13 Clocks.** ClockPills (Appendix C §G.3 rule 3) for every clock relevant to the viewer: response window, deficiency cure, s.23(4) pleadings (6 months), s.29A (12 + 6 months; ICA advisory — LR-ARB-010), mediation period (Appendix A `med_contract_timebox` by vertical, + up to 60 days by consent; FAM property 90 + 60 days — X-40; App. K §5.8), s.33 (30 days), s.34 (3 months + 30 days, per party), registration (4 months, Registration Act 1908 s.23), compliance milestones, execution information clocks (§4.5). Each pill: name, "N days left", absolute date, state, owner **role** (names only to L4). The UI never computes clock state (NN-04).

**1.4.14 Calendar (ICS).** Per user per case feed `webcal://equatorresolution.in/v1/calendar/{token}.ics` (token 160-bit, revocable, rotates on representative revocation). Contents: sessions (UID stable per session; SEQUENCE increments on reschedule), deadlines relevant to the viewer (all-day events at 10:00 IST on the due date with `VALARM` T-7 days and T-1 day). Event title pattern: `{case_number} · {session kind} ({mode})` — no party names, no amounts; description: portal deep link only (never a meeting token). FAM, safety-flagged and sealed matters use the neutral title "Equator appointment". An "all my matters" feed exists per user.

**1.4.15 Notifications subscription (SCR-P02-91).** Per user per case: events (new paper served · order issued · session scheduled/changed · deadline T-7/T-1 · outcome issued · payment due · execution milestone reminder) × channels (in-app, email, SMS, WhatsApp, push) × frequency (instant / daily digest 18:00 IST / weekly) × language. Legal-service notices are not suppressible (they go out regardless of preference). Quiet hours and NN-12 windows apply to borrower contact in recovery-related matters. FAM/WRK/safety/sealed: content-free text "You have an update from Equator" (Appendix C §F.5). L1 viewers can only opt into "Get updates" on a contact point already on the case.

**1.4.16 Case history statement (PDF; SCR-P02-92).** "Case History Statement — for information": generated on request by L2+ (`POST /v1/cases/{caseId}/history-statements`), A4, render profile `EQR_TRIBUNAL`, sections mirroring §1.3–§1.4 as visible to the requester at generation time, watermark (requester, timestamp, case number), footer QR to §5 verification, SHA-256 in the ledger. Footer text: "This statement shows the case record as visible to {requester role} on {date}. It is not a certified copy." A **certified** version (registrar DSC) can be ordered for court use (§5; fee ANC.CERT.COPY).

### 1.5 Visibility matrix (panel × viewer)

✔ full · ◐ partial (rule) · — none. "Own" = viewer's side; "Other" = other side's party users and representatives.

| Panel | L1 | Party (own) | Party (other) | Representative | Neutral | Case manager / registrar | Enterprise operator (org party) |
|---|---|---|---|---|---|---|---|
| Header | ◐ L1 fields | ✔ | ✔ | ✔ [view scope] | ✔ | ✔ | ✔ [org] |
| Parties & reps | initials | ✔ | ◐ masked contacts | ✔ [scope] | ✔ | ✔ | ✔ |
| Papers filed | — | ✔ own + served | ◐ served only | ✔ [scope] | ◐ audience incl. NEUTRAL | ✔ (metadata of NEUTRAL_ONLY) | ✔ [org] |
| Applications | — | ✔ | ✔ (served) | ✔ | ✔ | ✔ | ✔ |
| Notices & service | — | ✔ | ✔ (no addresses) | ✔ | ✔ | ✔ | ✔ |
| Sessions | next date | ✔ (own caucus) | ✔ (own caucus) | ✔ [attend] | ✔ | ✔ (caucus metadata) | ✔ |
| Orders | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Final outcome | "issued on" | ✔ | ✔ | ✔ [scope] | ✔ | ✔ | ✔ [auth] |
| Payments | — | ✔ own; others paid/unpaid | ✔ own; others paid/unpaid | ◐ [pay scope] | ◐ deposit status | ✔ | ✔ [org] |
| Registry note | — | ✔ party version | ✔ party version | ✔ | ✔ party version | ✔ incl. internal | ✔ party version |
| Linked matters | — | ✔ | ✔ (non-confidential links) | ✔ | ✔ | ✔ | ✔ |
| Clocks | — | ✔ relevant | ✔ relevant | ✔ | ✔ | ✔ | ✔ |
| History PDF | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

Witnesses, interpreters, observers and support persons (secure-link roles) see only their session join page and documents expressly shared with them (App. L `EXTERNAL_LINK`).

### 1.6 Confidential categories (never rendered outside their audience)

| Category | Rule | Basis |
|---|---|---|
| Caucus notes and caucus shares | Author neutral only / sharing side + neutral; never in arbitral record | NN-11; A&C s.70 proviso, s.81; master §5.3 |
| Without-prejudice offers, blind bids | Parties to the negotiation; blind values never displayed until crossed | P04; A&C s.81 |
| Vulnerability flags, screening, safety addresses | Registry + safeguarding lead; never other side | NN-07 |
| POSH | Not in the core portal at all; opaque token | NN-07; POSH Act 2013 s.16 |
| Health data (INS) | `health_sealed` via token; panel shows "Medical records held securely — visible to authorised persons" | NN-07 |
| KYC documents | Owner + registry (metadata) | NN-14 |
| Settlement terms, award text | Parties, representatives in scope, neutral, registry | s.42A; s.75 |
| AA-derived summaries | Neutral sees derived summary only | D6; NN-14 |
| Registry-only notes, quality scores, complaints | L4 only | NN-28 |

Placeholder for redacted fields in lists that are shown: "Not visible to you" (never blank; Appendix C §E.5).

### 1.7 Mobile layout (P12)

Single-column. Collapsible header card (case number, status chip, next date, who-decides chip, what-happens-next sentence) pinned at top; panels as a horizontally scrollable segmented control (Overview · Papers · Applications · Sessions · Orders · Outcome · Payments · More) with the remaining panels under "More". Rows render as cards (title, two meta lines, status chip, chevron). Primary action bar (bottom, thumb reach): the case's next action (Respond / Upload / Pay / Join / Sign). Offline: last-opened case view cached encrypted in SQLite (P12), banner "Last updated {time}"; documents cached only if opened. Pull-to-refresh; push deep links land on the relevant row. Screen capture blocked on `high`/`sealed` tiers (P12). Targets: 44×44 touch; LCP < 2.5 s on 4G; ≤ 4 API calls on open.

### 1.8 Copy deck

**1.8.1 Page copy (en; hi requires legal-translator review — NN-23).**

| Key | Text |
|---|---|
| `trk.h1` | Know where your matter stands |
| `trk.sub` | Every step, date and document in one place. Enter your case number and the code on your notice. |
| `trk.cvc.help` | The 10-character code printed under the QR on your notice or acknowledgement. |
| `trk.otp.alt` | No code? We can send a one-time code to a phone or email already on this case. |
| `trk.uniform` | If these details match a case, you will see its status. Check the details and try again. |
| `trk.restricted` | Status available to parties in their account. Sign in to see it. |
| `trk.not_court` | Equator is a private dispute-resolution institution. It is not a court. |
| `portal.papers.empty` | No papers yet. When anyone files, it appears here with the date and page count. |
| `portal.mediation.norecord` | No record is kept of what is said in mediation. Only dates and attendance are shown. |
| `portal.outcome.private` | The outcome is private to the parties. Ask for a certified copy if a bank, registrar or court needs it. |
| `portal.history.disclaimer` | This statement is for information. It is not a certified copy. |

**1.8.2 Stage labels (proceeding level; examples).** Arbitration: "Tribunal being formed" · "Tribunal formed" · "Procedural meeting" · "Statement of claim due" · "Statement of defence due" · "Evidence" · "Final hearing" · "Award being prepared" · "Award under institutional check (form only)" · "Award delivered". Mediation: "Agreement to mediate pending" · "Sessions in progress" · "Settlement being drafted" · "Settlement signed" · "Ended without settlement". Conciliation: "Invitation sent (30-day reply window)" · "Conciliation in progress" · "Settlement signed (has award status — A&C s.74)".

### 1.9 Performance, accessibility, security

Public tracker page ≤ 60 KB, no third-party scripts, works without JavaScript for S1 (server-rendered form POST). Portal panels paginate by cursor (50 rows). WCAG 2.2 AA: tables have captions and scope headers; status changes announced politely; registers have "Download as CSV" (L2+, own visibility) for screen-reader users. Every L2+ view of a `high` or `sealed` panel writes `audit.access_log`. Read model never stores sealed content; it stores tokens and labels only.

---

## 2. Case Desk — the internal working dashboard per case

The persona home dashboards are Appendix S §5 (SCR-S-D01…D14). The **Case Desk** is the per-case working surface that opens from those dashboards (route `/app/cases/{caseId}/desk`, `/neutral/cases/{caseId}/desk`, `/console/cases/{caseId}/desk`; SCR-P02-93/94/95). It sits on the same read model as §1 and adds actions. Design rules: one primary action per state; every action reachable in ≤ 2 clicks from the desk; destructive actions use a confirmation screen; keyboard palette (`Ctrl/Cmd+K`) on neutral and registry desks (App. S §5 fewer-clicks rules).

### 2.1 Party and representative desk (SCR-P02-93)

| Feature | Behaviour | Rule |
|---|---|---|
| Action inbox | Ordered list: respond, cure defect, upload requested document, pay deposit, sign, join session, confirm attendance, approve representative's proposal (above authority limit) | Sorted by due date; each item shows due date, days left and "who decides" |
| Document requests tracker | Each request (from tribunal direction, registry deficiency or mediator) with checklist of items, accepted formats, upload button, status | Upload goes to `PRIVATE_DRAFT` → "File" (App. L §2.4 share dialog) |
| Session preparation | Device and bandwidth test, join link (live 15 min before), interpreter confirmed, documents for the session (bundle link with page numbers), "what to expect" text by session kind | Mediation: confidentiality reminder; no recording |
| Drafts | Own drafts (incl. AI Pleadings Studio output — App. M) with "requires your review" banner | Never visible to others until filed (L-D-01) |
| Messages | Case thread with the registry; messages to the tribunal are copied to every party automatically (**ex parte guard**); mediator messages may be one-side only in mediation (caucus channel) | A&C s.24(3); master §5.3 firewall |
| Representatives | Who acts for me, scope chips, limits, valid until, narrow/revoke (App. S §4.4) | NN-27 |
| Money | What this has cost so far, what is due next, refundable amounts, escrow balance, instalment schedule | NN-29 honest pricing |
| Compliance | Obligations owed to me / by me, evidence upload, dispute an obligation, calendar | §4.7 |
| Execution and registration | Entry to §4 desks when the outcome needs them | §4 |
| Help | "Ask the case manager" (logistics only), assisted-mode request, free-forum reminder (NN-20) | Staff never advise on merits |

### 2.2 Neutral desk (SCR-P02-94)

| Feature | Behaviour | Rule |
|---|---|---|
| Case brief | `case_summariser` brief with bundle-page citations, AiDraftBanner until accepted | NN-01 |
| Procedural calendar | Gantt of timetable (pleadings, evidence, hearings, award target) linked to orders; drag with keyboard alternative | WCAG 2.5.7 |
| Directions tracker | Every direction from every order as a row: obligor, due, complied on, extension sought, status; one-click "issue reminder" (served by registry) | Feeds registry note §1.4.9(6) |
| Applications queue | Pending applications with response windows, response received flag, draft order button | `core.case_applications` |
| Drafting | Orders and awards (P04/P06 builders), s.31 validators live, scrutiny feedback (form only) | FR-P06-08, FR-P06-13 |
| s.29A cockpit | Days left, extension history, consent-extension record, "court-application pack" when ≤ 60 days | NN-04; LR-ARB-009 |
| Hearing controls | Join, rooms, recording consent status (arbitration only), witness queue, bundle page-sync | P04 |
| Private notes | Arbitrator working notes (sealed to author); mediator caucus notes (author only) | NN-11 |
| Deposits | Paid/unpaid per side; s.38 notice draft | LR-ARB-022 |
| Disclosures | Continuing-disclosure prompts when a party, representative or funder joins | LR-ARB-005 |
| Time record | Hourly-fee matters: time entries per session/activity; fee note draft | Appendix B |
| Publication | Tribunal consent request (§3.5) after award is final | NN-26 |

### 2.3 Case manager desk (SCR-P02-95)

| Feature | Behaviour | Rule |
|---|---|---|
| Readiness checklist per stage | Auto-evaluated items with green/red: service complete for all parties; deposits paid; neutral confirmed; interpreter booked; bundle current; registry note generated; accessibility requests actioned; clocks owned | Blocks "Confirm session" when red items are mandatory |
| Task list with SLA | Scrutiny (2 WD; INS 1 WD), deficiency cure, service failures, deemed-service decisions, document requests, certified-copy requests | Appendix A clocks `sla_*` |
| Registry note generator | One click → draft from §1.4.9 template → edit internal section → e-sign → serve | Version history |
| Session logistics | Room creation, PSTN dial-in, interpreter booking, witness links, reminders | P04/P07 |
| Notice composer | Templates by type and language; channel plan; NN-12 guards | P02 §4.8 |
| Serve order | Issued order → service to all parties → service certificates | — |
| Clock owner assignment | Unowned statutory clocks list with assign action | NN-04 |
| Escalate | To registrar (with reason codes: appointment, challenge, deposit default, safety, complaint) | — |
| Handover | Structured handover note when reassigning a case | Audit |
| Publication and execution queues | Consent status per party, redaction tasks; execution milestones reported by parties needing check | §3, §4 |
| Bulk actions | Across cases: assign owner, send reminder, regenerate registry notes, export MIS | App. S §5 rule 5 |

### 2.4 Shared desk services

Activity feed (append-only, hash-linked) · in-case search (OpenSearch, non-sealed, respects audience) · saved filters · "Copy case reference" and "Share status link" (generates an L1 link only for the requester's own CVC) · print view · keyboard shortcuts (`g p` papers, `g o` orders, `g s` sessions, `n` next action).

---

## 3. Publication of awards, settlements and decisions (R-25; D2-10; NN-26)

### 3.1 Legal position and Equator's design answer

| Instrument | Text / effect | Design consequence |
|---|---|---|
| A&C Act 1996 **s.42A** (ins. by Act 33 of 2019, w.e.f. 30 Aug 2019) | "Notwithstanding anything contained in any other law … the arbitrator, the arbitral institution and the parties to the arbitration agreement shall maintain confidentiality of all arbitral proceedings except award where its disclosure is necessary for the purpose of implementation and enforcement of award." | Binds Equator as "arbitral institution" and every neutral, independent of contract. There is **no express consent exception**. Parties may waive their own duty; whether all-party consent also releases the institution's statutory duty is unsettled (Q-R1). The award is itself confidential save for implementation/enforcement disclosure. |
| s.42A territorial reach | Part I applies where the seat is in India (s.2(2); LR-INT-002) | Foreign-seated awards administered by Equator fall outside s.42A but still under NN-26 and the Equator Rules confidentiality clause. |
| A&C **s.75** | Conciliator and parties keep all matters relating to conciliation confidential; the settlement agreement is confidential except where disclosure is necessary for implementation and enforcement | Same gate as s.42A for s.73 settlements. |
| A&C **s.81** | Views, admissions, proposals not to be relied on in other proceedings | Never published; firewall applies to digests. |
| Mediation Act 2023 **s.22** (not in force; policy mirror — NN-05, NN-11) | Confidentiality of mediation communications and bar on recording | MSA terms are published only in the limited modes of §3.3. |
| POSH Act 2013 **s.16** | Contents of complaint, identity and addresses of aggrieved woman, respondent and witnesses, inquiry proceedings, recommendations and action not to be published | POSH: P0 only, no statistics in this module (NN-07). |
| BNS 2023 **s.72**; POCSO Act 2012 **s.23**; JJ Act 2015 **s.74**; HMA 1955 **s.22**; Family Courts Act 1984 **s.11** | Identity of sexual-offence victims, children and matrimonial parties protected | RP-SEX, RP-MINOR, RP-FAM; FAM P3/P4 disabled. *Nipun Saxena v Union of India* (2019) 2 SCC 703 masking standard. |
| *Laksh Vir Singh Yadav v Union of India*, Del HC, 29 May 2026 (2026 LiveLaw (Del) 552) | Distinguishes **masking** (identifiers replaced by neutral placeholders; reasoning stays) from de-indexing; matrimonial and purely private civil disputes have no claim to name-based retrievability once concluded (applied in *R.S.S. Estate LLP v State*, Del HC, 13 Jul 2026, refusing masking for commercial information) | Equator's P3 standard = masking; P2/P3 pages carry `noindex` for 12 months (§3.13). |
| DPDP Act 2023 | Publication of personal data is processing; s.17(1)(a) (legal claims) does not cover publication; anonymised data is outside the Act (counsel Q-R4 on the threshold) | Consent of every named Data Principal or effective anonymisation; withdrawal must be honoured (s.6(4)). |
| GDPR (EU parties in INT; Art. 3(2)(a)) | Pseudonymised data is personal data (Art. 4(5)); anonymous data is outside (Recital 26); special categories need Art. 9(2)(a) explicit consent | EU/UK parties: explicit consent fields; special-category content removed. |

**Equator's answer.** Default P0 (nothing). Publication of any award, settlement or order requires: (a) every party's express, informed, e-signed, revocable consent given **after** the outcome (a filing-stage preference is not consent); (b) tribunal or neutral consent; (c) completion of the applicable redaction profiles; (d) two-person redaction review and `legal_reviewer` sign-off; (e) the outcome is final (s.34 window lapsed or challenge disposed; settlements executed and compliance complete or 6 months passed); (f) eligibility under §3.3. Arbitral publication (P2–P4 of India-seated awards) stays behind flag `publication.arbitral.enabled` = OFF until counsel answers Q-R1 in writing; conciliation and mediation digests behind `publication.consensual.enabled` = OFF until Q-R3. P1 statistics may run with the flags OFF.

### 3.2 Publication modes (`DD-R-PUB-MODE`)

| Mode | Published | Gates | Embargo default |
|---|---|---|---|
| **P0** None (default) | Nothing | — | — |
| **P1** Statistics | Aggregated counts and medians (vertical, mechanism, procedure tier, duration buckets, outcome type for the institution as a whole) with k ≥ 10 per cell; small cells suppressed or merged | Automatic; no personal data; sealed classes excluded | Quarterly |
| **P2** Digest of reasoning | Neutral-approved summary of issues and reasoning, no identifying facts (template §3.9.4) | All-party consent; neutral approval; RP profiles; legal review | 6 months after finality |
| **P3** Redacted decision | Full reasoning with identifiers masked (*Laksh Vir* masking) | All-party consent; tribunal consent; two-person redaction; re-identification test; party preview 30 days; legal review | 24 months after the last delivery (ICC benchmark); parties may unanimously choose 6 or 12 |
| **P4** Full decision | Unredacted, real names | All-party express consent incl. every named individual; tribunal consent; Transparency sub-committee approval; B2B only | As P3 |
| **E** Enforcement disclosure | To a court, executing officer, Sub-Registrar, bank or regulator, only to the extent necessary | s.42A/s.75 implementation carve-out; DPDP s.7(e) / s.17(1)(a); logged in the Disclosure Register | — |

When parties choose different modes, the **most restrictive** applies.

### 3.3 Eligibility matrix (deterministic rule `pub.eligibility`)

| Matter | P1 | P2 | P3 | P4 |
|---|---|---|---|---|
| FIN (individual borrower) | ✔ | ✔ | ✔ (RP-FIN) | ✖ |
| FIN (B2B: lender and corporate borrower) | ✔ | ✔ | ✔ | ✖ (D2-10 keeps P4 to COM/INT/INS B2B) |
| COM | ✔ | ✔ | ✔ | ✔ B2B only, no individual party |
| FAM (all subtypes) | ✔ | ✔ (RP-FAM; V3 §13.5) | ✖ | ✖ |
| INS retail (non-health) | ✔ | ✔ | ✔ (RP-FIN) | ✖ |
| INS health (`health_data_token`) | ✔ (within INS totals only) | ✔ only if the digest contains no health data (RP-HEALTH certified) | ✖ | ✖ |
| INS B2B (insurer–insurer, reinsurer, subrogation) | ✔ | ✔ | ✔ | ✔ |
| WRK (non-POSH) | ✔ | ✔ | ✔ non-workman contracts only | ✖ |
| WRK POSH | ✖ | ✖ | ✖ | ✖ |
| INT | ✔ | ✔ | ✔ | ✔ B2B |
| Any minor party, witness or child-related term | ✔ | ✔ (RP-MINOR) | ✖ | ✖ |
| `safety_flag = true` or tier `sealed` | ✖ | ✖ | ✖ | ✖ |
| NI Act s.138 compounding settlement; matters with a parallel criminal case | ✔ | ✔ (no reference to the offence or the accused) | ✖ | ✖ |
| Mediated settlement (contractual MSA) | ✔ | ✔ (structure of solution; no amounts linked to parties) | ✔ COM/INT B2B only | ✖ |
| Orders (procedural rulings of general interest, e.g., s.16 jurisdiction) | — | ✔ | ✔ | ✔ B2B |
| Outcome set aside by a court | ✔ | ✖ | ✖ (withdraw if published) | ✖ |

### 3.4 Consent capture

**Three moments.**

| Moment | Form | Effect |
|---|---|---|
| Filing / response | `F-PUB-01` Publication preference (in BLK-CONSENT; V2 `consent.publication`, V6 `F-INT-23`): `pub.pref` radio {No (default), Statistics only, Maybe — ask me after the outcome}; help: "This is not consent. We will ask again after the outcome, when you can see what would be published." | Non-binding; drives whether §3.4 consent request is sent; never a precondition for anything (no bundling — DPDP s.6(1); NN-29) |
| After finality | `F-PUB-02` Publication consent (per party, e-signed, K2 identity; organisations by an authorised signatory; representatives may **not** sign unless the LoA scope expressly includes `publication_consent` (a new scope key to be added to the App. S §4.3 catalogue; default OFF) and the party re-confirms by OTP) | Binding consent for the stated mode, embargo and redactions |
| Before go-live | Party preview (30 days) of the exact redacted text | Party may withdraw, request further redaction, or confirm |

**F-PUB-02 fields.**

| field_id | Label | Type | Req | Options / validation |
|---|---|---|---|---|
| `pub.mode` | What may be published | radio | Y | P0 / P1 only / P2 / P3 / P4 — options outside §3.3 eligibility are not rendered |
| `pub.items` | Which documents | multiselect | Y if mode ≥ P2 | award · consent award · settlement terms (structure only for MSA) · procedural ruling |
| `pub.embargo_months` | Earliest publication | select | Y if mode ≥ P3 | 6 · 12 · 24 (default) · 36 |
| `pub.names` | How names appear | radio | Y | Role labels (default) · Real organisation names (P4 only) |
| `pub.amounts` | How amounts appear | radio | Y | Bands (default) · Exact (P4 only) |
| `pub.redaction_requests` | Anything else to hide | repeater (text + document anchor) | N | ≤ 20 entries |
| `pub.counsel_names` | Show my representative's name | checkbox | N | Default unchecked; P4 only; representative's own consent captured separately |
| `pub.gdpr_explicit` | Explicit consent for EU/UK data (if any) | checkbox | Y if party is EU/UK-resident or established | GDPR Art. 6(1)(a), Art. 9(2)(a) |
| `pub.notice_ack` | I have read the publication notice | checkbox | Y | DPDP s.5 itemised notice version recorded |
| `pub.withdrawal_ack` | I understand I can withdraw before publication, and ask for removal after | checkbox | Y | — |
| `pub.sign` | E-sign | esign | Y | Aadhaar eSign / DSC; virtual sign not allowed |

**Consent state machine** (`core.publication_consents.status`): `requested → given → (withdrawn)` before `published`; `given → superseded` (party changes mode); after publication `given → withdrawn` triggers takedown (§3.11). Request expires after 60 days without action (`expired`, treated as P0). Reminders: one at day 30; never more (no nagging — NN-29). Withdrawal is one click + OTP from the portal or by email to the DPO address.

### 3.5 Tribunal and neutral consent

`F-PUB-03` (neutral, DSC): consent yes/no; for P2 the neutral writes or approves the digest; for P3/P4 the tribunal confirms the redacted text does not misstate the reasoning. For a three-member tribunal, the presiding arbitrator plus a majority; a dissenting opinion is published only with its author's consent. Neutral identity is shown in published decisions (accountability — S8 R6) unless the neutral records a safety risk accepted by the registrar.

### 3.6 Redaction profiles and pseudonymisation rules

| Profile | Applies when | Remove / mask | Replace with |
|---|---|---|---|
| **RP-1 BASE** | Always (P2–P3) | Names of persons and organisations; addresses; phone; email; URLs; PAN, Aadhaar (never present), CIN, GSTIN, LEI, DIN, Udyam; bank, loan, policy, claim, invoice and vehicle numbers; other forums' case numbers and CNRs; Equator case number and filing reference; contract titles and unique product names; exact dates (keep month/year and intervals); signatures, stamps, QR codes; witness and employee names; metadata in the PDF | Role labels (`Claimant`, `Respondent`, `Supplier A`, `Lender L`, `Borrower B`, `Insurer I`, `Employer E`, `Employee W`, `Individual 1`); "[address]"; "[identifier]"; month and year |
| **RP-2 AMOUNTS** | Always unless P4 with consent | Exact sums | Bands: < ₹1 lakh; ₹1–10 lakh; ₹10–50 lakh; ₹50 lakh–₹1 crore; ₹1–5 crore; ₹5–25 crore; > ₹25 crore (INT: USD bands) |
| **RP-3 PLACE** | Always unless P4 | City, district, branch, site | State; for INT, country |
| **RP-4 FIN** | FIN, INS retail | Account histories, repayment records, credit scores, income, bureau data (CICRA 2005 s.20), collection-agent names | "[financial details]" |
| **RP-5 FAM** | FAM | All names incl. children; community, caste, religion (personal law named only as the statute applied, e.g., "Hindu Succession Act 1956"); relationships beyond the generic; health; employer; property identifiers | "Party A/B", "Heir 1", "the property" |
| **RP-6 HEALTH** | INS health, any medical content | Diagnoses, treatment, hospital, doctor, disability | Nothing — digest must not need them; legal reviewer certifies "no health data" |
| **RP-7 MINOR** | Any person < 18 or child-related term | Name, school, age, address, images | "Child 1" |
| **RP-8 COMSEC** | COM, INT, INS B2B on party request | Trade secrets, pricing, technical data, counterparties | "[commercially sensitive — redacted]" |
| **RP-SEX** | Any allegation of a sexual offence surfaces | — | **Block publication entirely** (BNS s.72; *Nipun Saxena*) |

**Pseudonymisation mechanics.** A per-decision token map (entity → label) is generated by the NER pass, stored encrypted in `core.publication_redactions.token_map_enc` (registry-only; never published, never exported) so that the same entity carries the same label throughout. Labels never encode initials. Quasi-identifier generalisation: subtype at L1 level only where the L2 subtype × state × year combination has fewer than 10 decisions in the Library.

### 3.7 Never published (any mode above P1)

POSH matters (all); sexual-offence allegations; safety-flagged and sealed-tier matters; caucus material and anything inadmissible under s.81; without-prejudice offers; AA-derived data; KYC; health data; children's identities; criminal-case details; any decision set aside by a court; any decision where a party, neutral or legal reviewer has an unresolved objection; any document a court has ordered sealed.

### 3.8 Pipeline, roles and SLAs (`PublicationWorkflow`, P06)

| Step | Actor | SLA | Output |
|---|---|---|---|
| 1 Eligibility | Rules engine | instant | `eligible_modes[]`, blocking reasons |
| 2 Consent requests | System → parties, tribunal | sent on finality | `core.publication_consents` |
| 3 Draft redaction | NER (Doc AI/LLM via AI Gateway, India region; sealed data never sent — NN-07) → `quality_officer` (or `case_counsel`) | 10 working days | Redacted rendition v1, token map |
| 4 Second review | A different `quality_officer`/`case_counsel` (two-person rule) | 5 WD | Diff approved |
| 5 Re-identification test | Reviewer checklist: (a) search the five most distinctive facts on a public search engine and in eCourts; (b) facet uniqueness check (§3.6); (c) cross-check against public court records of any s.34/s.37 proceedings; (d) counsel names; result recorded | within step 4 | `reid_test` JSON + attestation |
| 6 Digest (P2) | Neutral writes or approves; AI may draft from the **redacted** text only, AiDraftBanner, neutral accepts (NN-01) | 10 WD | Digest |
| 7 Party preview | Parties see exact text; may withdraw or request more redaction | 30 days | Comments resolved |
| 8 Legal review | `legal_reviewer` sign-off (S); P4 adds Transparency sub-committee approval | 5 WD | Approval |
| 9 Publish | `registrar` (X) on or after embargo date | scheduled | Library entry, citation, hash |

Nothing is published if any step is incomplete (`PUBLICATION_GATES_INCOMPLETE`). AI never decides eligibility, never removes a redaction, never publishes (NN-01).

### 3.9 Equator Decisions Library (public; P13; SCR-P13-60…63)

**3.9.1 Routes.** `/decisions` (search), `/decisions/{citation-slug}` (decision page, e.g., `/decisions/eqr-2027-awd-0001`), `/decisions/digests`, `/decisions/statistics` (P1 dashboard), `/decisions/about` (policy, consent, takedown, how to cite). SSR; no login; mobile-first; ≤ 150 KB first load.

**3.9.2 Neutral citation.** Format **`EQR/{YYYY}/{TYPE}/{NNNN}`** — `YYYY` = year of publication; `TYPE` ∈ `AWD` (award, redacted or full), `CAW` (consent award), `STL` (settlement — s.73/s.74 or MSA), `DIG` (digest of reasoning), `ORD` (procedural ruling), `ICD` (institutional challenge decision, flag-gated); `NNNN` = gap-free sequence per (year, type) from `core.citation_sequences` under row lock, widening to 5 digits after 9999. Pinpoints: `EQR/2027/AWD/0001 ¶23`. The citation never encodes the case number, vertical, city or parties, and never imitates court styles (no "INSC", "SCC", "AIR", no "v."). Titles use role labels joined by "and": "Supplier A and Distributor B — supply of goods (delayed payment)". Corrections create version suffix `/v2` with the original citation unchanged.

**3.9.3 Search and filters.** Full-text over published redacted text only; filters: vertical · category (L1) · mechanism · decision type (award, consent award, settlement, digest, ruling) · year of decision · year of publication · tribunal size · neutral (only where the neutral is shown) · seat (state; INT country) · governing law · procedure (expedited, documents-only, fast-track s.29B, emergency) · language · statutes cited (tags from the verified legal corpus) · issue tags (taxonomy `pub.issue_tags`, e.g., "interest — s.31(7)", "limitation", "s.12(5) waiver", "repudiation — non-disclosure", "MSMED s.16 interest"). **No outcome facet and no party-type × outcome view** (NN-16, NN-28): the Library never lets a user count wins by lenders, insurers or employers.

**3.9.4 Decision page anatomy.** Banner: "This decision was made under the Equator Rules and is published with the consent of all parties. It is not a judgment of a court and binds only the parties." · citation (copy button) · decision type · date (month/year) · vertical/category · mechanism and procedure · tribunal/neutral names (if shown) · seat · language (with "Translation for convenience" label where applicable — NN-32) · digest (if any) · redacted text or full text (HTML + PDF/A with hash) · statutes and cases cited (links to the verified corpus) · version history · "Report a concern" (takedown request form) · verification block (SHA-256, published date). **Digest template (P2):** issues (bullets, ≤ 5) · short facts (≤ 150 words, generalised) · reasoning summary (≤ 400 words) · result in neutral terms ("claim allowed in part with interest" is permitted inside the digest; no party-type labels in titles) · provisions and authorities.

**3.9.5 Statistics page (P1).** Quarterly dashboard and annual Transparency Report data (S5 C3): caseload by vertical/mechanism/tier, median durations, appointments by method and grade, first-time appointees %, challenges filed/decided, awards scrutinised and median scrutiny days, s.29A extensions sought, awards set aside under s.34 (D12), complaints received/decided, AI-assisted feature use. k ≥ 10; POSH excluded; sealed and safety-flagged matters excluded; INS health counted only within INS totals; INS per-insurer quarterly aggregates where Insurance Rules r.25 requires them (S9 C-12) are generated in P09 under the same k rule.

### 3.10 Challenge decisions and court outcomes

| Item | Rule |
|---|---|
| Equator Challenge Committee decisions on arbitrator challenges (s.13(1) agreed procedure; S5 C1) | Redacted (RP-1…RP-3), 12-month lag, citation type `ICD`, publication basis = Equator Rules clause + all-party consent recorded at constitution; flag `publication.challenge_decisions.enabled` = OFF until counsel answers Q-R2 (s.42A; whether a rules-based deemed consent suffices) |
| Court decisions on Equator outcomes (s.34, s.37, s.36 stay, s.47–s.49, execution) | Court judgments are public records. Equator records the outcome in `core.court_outcomes` (forum, case number, date, result: upheld / set aside / modified / remanded / stay granted / stay refused; court's neutral citation where reported) and publishes **counts** (D12 "awards set aside"). It never links a court judgment to a pseudonymised Library entry (cross-linking would re-identify) and removes any Library entry whose decision is set aside |

### 3.11 Withdrawal, takedown and correction

| Trigger | Action | SLA |
|---|---|---|
| Party withdraws consent before publication | Cancel scheduled publication; notify others | Immediate |
| Party withdraws after publication (NN-26 revocable) | Unpublish; replace page with tombstone ("This decision has been withdrawn") keeping the citation and no content; purge CDN; remove from sitemap; submit removal to search engines; delete PDF from public bucket (retain internal record) | **Earlier of 2 working days and 72 hours** (R-R7) |
| Non-party Data Principal request (witness, employee named) | Verify; apply further redaction; republish as new version | 5 WD |
| Court order, regulator direction, IT Rules 2021 r.3(1)(d)-type notice | Comply as directed; log | As ordered, ≤ 36 h for takedown notices |
| Re-identification discovered | Unpublish immediately; incident ticket; DPO review (possible personal-data breach — DPDP s.8(6), 72-hour Board report under Rule 7(2)(b)) | Immediate |
| Error in text | Correction as `/v2` with errata note | 5 WD |

### 3.12 DPDP / GDPR / multi-law handling (App. Q control set; NN-30)

Purpose code `publication` in the consent ledger, separate from `dispute_administration`; itemised notice (DPDP s.5; Rule 3) in the party's language; consent per named individual (organisational consent by an authorised signatory covers the organisation only — an individual director or employee named in the decision must be removed or give separate consent); children: never named (DPDP s.9). Withdrawal propagation within the R-R7 SLA (DPDP s.6(4); GDPR Art. 7(3)); erasure requests (DPDP s.12; GDPR Art. 17) honoured unless the item is retained only internally under legal hold; objection (GDPR Art. 21) treated as withdrawal. Cross-border: the Library is served from India; CDN edge caching outside India carries only published, redacted content. DPIA (UCS-15) required before enabling P3/P4 for any vertical. Records of processing entry: `ROPA-PUB-01`.

### 3.13 Indexing and SEO

P2 and P3 pages: `noindex, noarchive` for the first 12 months after publication, then indexable unless a party asked otherwise in `F-PUB-02`; P4: indexable from publication. Structured data: `schema.org/CreativeWork` with `identifier` = citation (never `LegalCase`/`Legislation` court types). Canonical URL per version. Sitemaps exclude withdrawn entries. No advertising or third-party trackers on Library pages (NN-16).

---

## 4. Execution, implementation and registration support (R-26; R-36; D2-11)

### 4.1 Equator's role and its limits

Equator prepares court-format documents (never labelled "court-ready" under an unverified render profile — X-34; App. L L-D-05), computes figures deterministically, tells the party which forums the law points to, books registration appointments, and tracks progress with the party. Equator **does not** file in court, appear, sign pleadings for a party, advise which remedy to choose, or represent anyone (Advocates Act 1961 ss.29, 33; A-04). Execution petitions are filed by the party in person or by an advocate of the party's choice (§4.8). Copy on every execution screen (`exe.role_note`): "We prepare your papers and track progress with you. Filing and appearing in court are done by you or your advocate. This is information, not legal advice."

### 4.2 Route matrix by outcome type (rule pack `execution.routes`; each row a Legal Rules Register entry)

| # | Outcome | Legal character | Route to enforce / implement | Forum | Timing and limitation | Equator pack (P06 FR-P06-23 + new) | Status |
|---|---|---|---|---|---|---|---|
| X1 | Domestic arbitral award (Part I) | Enforceable under CPC "as if it were a decree" once the s.34 time has expired (s.36(1)); filing a s.34 petition is **no automatic stay** (s.36(2)); stay on conditions (s.36(3)); unconditional stay where the award was induced by fraud or corruption (proviso) | Execution application under CPC O.XXI r.11(2) with the award; no transfer of decree needed — file where assets are (*Sundaram Finance Ltd v Abdul Samad* (2018) 3 SCC 622) | §4.3 resolver: Commercial Court/Division where a commercial dispute of specified value ≥ ₹3 lakh (CCA 2015 s.2(1)(i), s.10(3)) **[VERIFY — open (counsel): Q-R5 whether s.10(3) covers execution (execution is under CPC via s.36, not an A&C Act application) in every State]**; otherwise civil court of competent jurisdiction where assets are | Not before s.34(3) window (3 months + 30 days from receipt, per party) unless no challenge; execution limitation 12 years, Limitation Act 1963 Art. 136 (domestic award is deemed a decree under s.36(1); contrast *Vedanta* (2020) 10 SCC 1, Art. 137 for foreign awards) **[VERIFY — open (counsel): Art. 136 vs Art. 137 for domestic awards (V0124)]** | `ac_s36_domestic_award` | Live |
| X2 | Consent award (s.30) incl. arb-med-arb conversion | Same status as any award (s.30(4)) | As X1 | As X1 | As X1 | `ac_s36_domestic_award` (consent variant) | Live |
| X3 | Conciliation settlement (s.73) | Same status and effect as an arbitral award on agreed terms (s.74) | As X1 | As X1 | As X1; challenge route as for a s.30 award (Equator clock: from each party's receipt of the s.73(4) authenticated copy) **[VERIFY — open (counsel): limitation start for s.74 settlements]** | `ac_s74_conciliation` | Live |
| X4 | Mediated settlement — contractual mode (today) | Contract (LR-MED-012) | (a) Suit on the agreement (summary suit CPC O.XXXVII where it is a written contract for a liquidated sum); commercial suits ≥ ₹3 lakh need s.12A PIMS unless urgent interim relief (LR-MED-013); (b) **conversion** at signing into a s.73 conciliation settlement (if run as Part III) or a consent award (s.30) where an arbitration agreement exists or is signed; (c) where a suit is pending, compromise recorded under CPC O.XXIII r.3 → consent decree (exempt from registration for suit property only — LR-STAMP-006) | Civil / Commercial Court | Contract limitation 3 years (Limitation Act Art. 55) | `mediation_contractual` | Live |
| X5 | MSA under Mediation Act s.27 | Final and binding; enforceable under CPC as if a judgment or decree (s.27); challenge only on s.28 grounds within 90 days (+90) | Execution under CPC | Court of competent jurisdiction | s.28 window | `mediation_s27` | **Flag OFF** (NN-05; `mediation.s27_decree_enforcement`) |
| X6 | Lok Adalat award / PLA award | Deemed decree of a civil court; final, no appeal (LSA Act 1987 s.21; PLA s.22E) | Execution petition | Civil court having jurisdiction (cheque cases executable as civil decree — *K.N. Govindan Kutty Menon v C.D. Shaji* (2012) 2 SCC 51) | Art. 136 | `lok_adalat_award_execution` (new: checklist + O.XXI annexures; Equator never conducts Lok Adalat — LR-MED-010) | Live (support only) |
| X7 | Foreign award — New York Convention | Enforceable once the court is satisfied; then deemed a decree of that court (s.49); refusal only on s.48 grounds; appeal s.50 | Petition under s.47 with the original or authenticated award, the agreement and evidence of foreign-award status (LR-INT-007); seat must be a s.44(b) notified territory (UAE is not — NN-19) | High Court per s.47 Explanation; Commercial Division (CCA s.10(1)) | 3 years, Art. 137 (*Government of India v Vedanta Ltd* (2020) 10 SCC 1) | `ac_s47_foreign_award_india` | Live |
| X8 | India-seated award to be enforced abroad | NYC Art. IV formalities in the enforcement country | Authenticated award + agreement + certified translation + apostille/legalisation | Foreign court | Per foreign law | `nyc_art_iv` | Live |
| X9 | Award from a non-reciprocating seat | No Part II route | Suit on the award or the underlying claim | Civil/Commercial Court | Per suit | `foreign_award_non_reciprocating_brief` (new) | Live |
| X10 | Emergency-arbitrator order / s.17 interim order | India-seated EA order enforceable as a s.17 order (*Amazon.com NV Investment Holdings v Future Retail* (2022) 1 SCC 209; LR-ARB-025); s.17(2): enforceable under CPC as if an order of the court | Application to court | Court per s.2(1)(e) | Immediate | `ac_s17_enforcement` (new) | Live |
| X11 | IBC — settlement before admission | Withdrawal of a s.7/s.9 application before admission (NCLT Rules 2016 r.8) | Withdrawal application by the applicant, with settlement terms | NCLT | Before admission (s.7(5) 14-day admission duty) | `ibc_r8_withdrawal` (new; V2 `com.ibc.desk.v1`) | Live (support only) |
| X12 | IBC — settlement after admission | Withdrawal under IBC s.12A as substituted by the IBC (Amendment) Act 2026: application through the IRP/RP, approval of 90% of the CoC, NCLT decides within 30 days; window only after CoC constitution and before the first invitation for resolution plans (D2-02; V2) **[VERIFY — open: sub-clause mapping (V2 §3)]** | Settlement deed + CoC engagement pack + application annex via RP | NCLT | `ibc_s12a_window`, `ibc_s12a_decision` clocks (V2 §16.4) | `ibc_s12a_withdrawal` (new) | Live (support only) |
| X13 | NI Act s.138 — civil settlement | Offence compoundable (NI Act s.147); the court alone compounds (NN-24); compounding costs per *Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158 (LR-RBI-018) | Joint compounding application filed **by the parties**; settlement deed; payment proof | Trial court / appellate court where pending | Next court date | `ni_s147_compounding` | Live |
| X14 | HMA s.13B consent terms | Decree of divorce by the Family Court; terms incorporated by the court | Joint petition first and second motion (*Amardeep Singh v Harveen Kaur* (2017) 8 SCC 746 for waiver) | Family Court | 6 months (waivable) | `hma_s13b` | Live |
| X15 | Expert determination | Contract | Suit on the determination; or consent award where an arbitration agreement exists | Civil/Commercial Court | Contract limitation | `expert_determination_brief` (new) | Live |
| X16 | Internal appeal-tier award (contractual two-tier — LR-ARB-026) | The final award after appeal is the award for s.34/s.36 | As X1 | As X1 | s.34 runs from receipt of the final (appellate) award (*Centrotrade* (2017) 2 SCC 228 upholds two-tier arbitration) **[VERIFY — open (counsel): Q-R6 — protective first-tier challenge; s.29A clock per tier]** | `ac_s36_domestic_award` | Live |
| X17 | MSME supplier claim | MSEFC reference under MSMED Act 2006 s.18; MSEFC award challenge needs 75% pre-deposit (s.19) | Reference pack | MSEFC / MSME ODR portal | — | `msme_msefc` | Live (signpost) |
| X18 | Outcome involving immovable property | Registration Act 1908 s.17(1)(b) (awards are not exempt — *Lachhman Dass v Ram Lal* (1989) 3 SCC 99); unregistered instrument does not affect the property (s.49) | Physical execution + stamping + registration (§4.6) before enforcement | Sub-Registrar (s.28) | 4 months from execution (s.23; s.25 up to 4 more on fine) | Registration task (FR-P06-17) | Live |

### 4.3 Forum resolver (`execution.forum_resolver`; SCR-P06-60)

**Inputs** (`exe.*`): outcome type (X-code); seat (city/state/country); `is_ica` (s.2(1)(f)); `is_commercial` (CCA s.2(1)(c)) and specified value (₹, computed under CCA s.12); asset schedule rows — asset type (`bank_account`, `immovable`, `vehicle`, `receivable`, `shares_securities`, `salary`, `movable_goods`, `other`), state, district, PIN; judgment-debtor residence/business district; any pending court proceeding (CNR).

**Decision table (deterministic; data in `core.court_jurisdiction_rules`).**

| Rule | Condition | Candidate forum(s) shown |
|---|---|---|
| FR-1 | X1–X3, not ICA, commercial, specified value ≥ ₹3 lakh, asset in a district within the ordinary original civil jurisdiction of a High Court having one (Delhi, Bombay, Calcutta, Madras, Himachal Pradesh) | Commercial Division of that High Court if value ≥ its pecuniary limit; otherwise the Commercial Court in that city (values from `core.court_jurisdiction_rules`, each **[VERIFY — open: pecuniary limits per HC]**) |
| FR-2 | X1–X3, not ICA, commercial ≥ ₹3 lakh, other districts | Commercial Court designated for that district under CCA s.3 (s.10(3)) — with Q-R5 caveat |
| FR-3 | X1–X3, non-commercial or < ₹3 lakh | Civil court of competent pecuniary jurisdiction where the asset is (*Sundaram*) |
| FR-4 | X1–X3 for an India-seated ICA award | High Court per s.2(1)(e)(ii) **[VERIFY — open: whether *Sundaram* asset-situs filing applies to ICA awards]** |
| FR-5 | X7 | High Court per s.47 Explanation for the asset/subject-matter location; Commercial Division where commercial |
| FR-6 | X6 | Civil court with jurisdiction over the judgment-debtor or assets |
| FR-7 | Assets in several States | One candidate per State; banner: "Parallel execution in more than one place is possible; every petition must disclose the others (CPC O.XXI r.11(2)(f))." |
| FR-8 | Any court proceeding already pending between the parties on the same subject | Warning: "Tell the court about the pending matter ({CNR})." |

**Output**: ranked list (by asset value entered by the party, never by any predicted success — NN-01), each with court name, establishment code (eCourts), e-filing portal, court-fee rule reference, and "Confirm with your advocate". Every resolver run is stored (`core.forum_resolutions`) with the rule IDs used.

### 4.4 Execution pack generator (extends FR-P06-23; SCR-P06-61)

**Readiness guards.** (1) Outcome is signed, stamped (NN-09) and delivered (s.31(5)); (2) for X1–X3: every party's s.34 window has lapsed **or** a challenge was dismissed **or** the user acknowledges "A challenge is pending without a stay order; the court may hear a stay application" (s.36(2); LR-ARB-017) — the pack is then stamped "s.34 pending — no stay on record as of {date}"; (3) registration done where X18 applies (`REGISTRATION_REQUIRED`); (4) no court stay uploaded (`EXECUTION_STAYED`).

**Inputs collected (`F-EXE-01`).**

| field_id | Label | Type | Req | Options / validation |
|---|---|---|---|---|
| `exe.decree_holder` | Applicant (award-holder) | prefilled party | Y | From case; organisation signatory required |
| `exe.judgment_debtor` | Against whom | party picker | Y | Must be a party bound by the outcome |
| `exe.amount_basis` | Amount due | computed + editable deductions | Y | Principal heads + pre-award interest + post-award interest s.31(7)(b) to the filing date (rate from award or statutory default; Interest Act 1978 s.2(b) reference rate from the register) + costs s.31A − payments recorded (escrow ledger + party-entered with proof) |
| `exe.payments_after` | Payments or adjustments after the award | repeater | Y (may be none) | date, amount, mode, proof (O.XXI r.11(2)(e)) |
| `exe.previous_applications` | Earlier execution applications | repeater | Y (may be none) | court, number, date, result (r.11(2)(f)) |
| `exe.assistance_mode` | Help asked from the court | multiselect | Y | `attach_sell_movable` · `attach_sell_immovable` · `attach_debt_bank_account` (O.XXI r.46) · `attach_salary` (r.48; CPC s.60 exemptions apply) · `arrest_detention` (s.51, ss.55–58; O.XXI r.37 notice) · `receiver` (s.51(d); O.XL) · `delivery_movable` (r.31) · `delivery_immovable` (r.35) · `specific_act` (r.32) |
| `exe.assets` | Assets known to you | repeater | N (recommended) | type, description, location (state/district/PIN), identifiers (masked: last 4), estimated value (party's own figure, labelled), source of knowledge; immovable: survey/khasra no., boundaries (O.XXI r.13), Collector's register extract where required (r.14) |
| `exe.asset_affidavit_prayer` | Ask the court to direct the judgment-debtor to disclose assets on affidavit | checkbox | N (default on) | *Rahul S. Shah v Jinendra Kumar Gandhi* (2021) 6 SCC 418 |
| `exe.forum_choice` | Court | from §4.3 | Y | One pack per forum |
| `exe.filing_mode` | Who will file | radio | Y | Advocate · Myself (party-in-person) |
| `exe.language` | Court language | select | Y | Per court profile; translations required for vernacular annexures (App. L §7) |

**Generated documents** (DOCX canonical + PDF/A-2b per App. L L-D-04; render profile = the forum's district/HC e-filing profile, `unverified` profiles carry "Check the forum's current filing rules"):
1. Execution application in the O.XXI r.11(2) particulars (a)–(j), with the CPC Appendix E execution form layout **[VERIFY — open: form number and State amendments]**.
2. Supporting affidavit of the decree-holder (deponent block; to be sworn — L-D-12, NN-25).
3. Application for direction to disclose assets on affidavit (*Rahul S. Shah*; affidavit-of-assets proforma used by the Delhi High Court in *Bhandari Engineers & Builders v Maharia Raj Joint Venture* (2016) **[VERIFY — open (provisional): Bhandari citation; generated documents cite *Rahul S. Shah* (2021) 6 SCC 418 only]**).
4. Registrar-certified copy of the award/settlement (§5, class CC-COURT) + e-stamp certificate + arbitration/conciliation agreement + per-party delivery proofs.
5. **Registry statement** (Equator, signed by the registrar): dates of award, delivery to each party, s.33 requests and disposal, any s.34 petition notified to Equator, and payments recorded on the platform — titled "Statement of facts from Equator's records", never a certificate about court records.
6. Computation sheet (deterministic engine output with inputs and rule IDs).
7. List of documents and index with bookmarks; annexure re-labelling to the court series (L-D-10); BSA 2023 s.63(4) certificate Part A + manifest (NN-10).
8. Court-fee note (State Court Fees Act article reference from `core.court_jurisdiction_rules`; party confirms) and vakalatnama placeholder page.
9. e-Filing checklist (below) and a plain-language "What happens in court" sheet.

**e-Filing checklist — district/commercial courts on e-Courts eFiling 3.0 (`filing.ecourts.gov.in`) [VERIFY — open (counsel): State variations — each High Court's e-filing rules; Telangana Notification 15/SO/2020 is the only verified baseline].** ☐ Advocate (or party-in-person) registered and verified on the portal · ☐ Establishment selected (State → district → court complex → establishment code from the pack) · ☐ Case type "Execution Petition" / "Arbitration Execution" as the establishment names it · ☐ Parties entered exactly as in the award (decree-holder/judgment-debtor) · ☐ Act and section: "Arbitration and Conciliation Act 1996 s.36; CPC O.XXI r.11" (X1–X3) / "LSA Act 1987 s.21" (X6) · ☐ PDFs text-searchable, within the portal's size limit (split at bookmarks; ≤ 20 MB per file default), file names ≤ 45 characters, no watermark or password (S8 §1.2) · ☐ e-Vakalatnama or party-in-person declaration · ☐ Court fee paid online (State e-court-fee/e-stamp facility) · ☐ Documents e-signed (Aadhaar eSign/DSC) · ☐ Affidavit sworn (video oath where offered, else notarised original filed within the period the rules prescribe — e.g., 7 working days under the Telangana model rules) · ☐ Submit → note the e-filing number → after scrutiny note the **CNR** and execution petition number → enter both in Equator (§4.5).

**Pack fee**: ANC.EXEC.PACK (Appendix B). Pack generation emits `equator.execution.pack.generated.v1` (F #110).

### 4.5 Execution tracking with party-entered milestones (SCR-P06-62)

State machine `core.execution_proceedings.status`:

| State | Entered by | Evidence | Next |
|---|---|---|---|
| `pack_ready` | System | Pack manifest | `filed` |
| `filed` | Party/advocate: e-filing number, date, court | Filing acknowledgement | `registered`, `returned_for_defects` |
| `returned_for_defects` | Party | Defect memo | `filed` |
| `registered` | Party: CNR, EP number | Registration screenshot/order | `notice_to_jd`, `asset_disclosure_ordered`, `attachment_ordered` |
| `notice_to_jd` | Party (O.XXI r.22 notice where the law requires it) | Order | `jd_objection`, `attachment_ordered` |
| `jd_objection` | Party (CPC s.47 objection / O.XXI r.58 third-party claim) | Copy of objection | `attachment_ordered`, `dismissed` |
| `asset_disclosure_ordered` | Party | Order | `attachment_ordered` |
| `attachment_ordered` → `attachment_effected` | Party | Order / warrant return | `sale_proclaimed`, `amount_deposited` |
| `sale_proclaimed` → `sale_held` → `sale_confirmed` | Party (O.XXI rr.66, 84–85, 92) | Orders | `amount_deposited` |
| `amount_deposited` | Party | Order / receipt | `satisfied_part`, `satisfied_full` |
| `satisfied_part` / `satisfied_full` | Party; payment out of court must be certified to the court (O.XXI r.2) — reminder generated | Satisfaction order | `closed` |
| Side states | `stayed` (s.36(3) / appellate stay), `dismissed`, `dismissed_for_default` → `restored`, `withdrawn`, `transferred` | Orders | — |

Each milestone: date, court order PDF (hashed), optional next court date (creates a calendar entry and a reminder T-3), note. Optional sync: eCourts CNR lookup through `CONNECTOR_PORT` (`ecourts`; P09 D10) proposes milestones from the court's case-history table ("Business on date", "Next hearing date", "Purpose"); the party confirms — never auto-applied. Clocks (informational, owner = award-holder): `execution_disposal_6m` from `registered` (*Rahul S. Shah*; *Periyammal v V. Rajamani*, 2025 INSC 329, 6 Mar 2025) with a T+6 months note "Execution courts have been directed to decide within six months; your advocate may bring this to the court's attention"; `execution_limitation` (12 years, X1–X3, Art. 136 [VERIFY]); `foreign_award_petition_3y` (X7, Art. 137). Case state: open execution record → `in_execution` (Appendix A §2.3); `satisfied_full` → C43 `closed`; amounts recovered update `exe.amount_basis` and the compliance view.

### 4.6 Registration workflow (extends FR-P06-16/17; NN-08; SCR-P06-63)

**Instrument chooser** (`reg.instrument`; legal basis per row; FAM/COM/FIN):

| Instrument | Registration | Basis | Stamp article (state matrix, LR-STAMP-007) |
|---|---|---|---|
| Memorandum recording a past oral family arrangement | Not compulsory (records, does not create rights) | *Kale v Deputy Director of Consolidation* (1976) 3 SCC 119 | Usually none/nominal **[VERIFY — open: per State]**; lawyer-review flag |
| Deed of family settlement (creates/declares rights) | Compulsory | Registration Act s.17(1)(b); *Kale* | Settlement article (family concession where provided) |
| Partition deed / partition award | Compulsory | s.17(1)(b); *Lachhman Dass* | Partition article (Maharashtra Art. 12 excludes partition awards from award duty — GLOBAL §12) |
| Release / relinquishment deed among heirs | Compulsory | s.17(1)(b) | Release article |
| Gift deed of immovable property | Compulsory | Transfer of Property Act 1882 s.123; s.17(1)(a) | Gift article |
| Sale / conveyance | Compulsory (≥ ₹100) | TPA s.54; s.17(1)(b) | Conveyance article; TDS 1% where consideration ≥ ₹50 lakh (Income-tax Act 2025 s.393(1) Table Sl. 3(i); FR-P06-17) |
| Lease > 1 year | Compulsory | s.17(1)(d) | Lease article |
| Award or s.74 settlement affecting immovable property ≥ ₹100 | Compulsory | s.17(1)(b) | Award/settlement article |
| Compromise decree on suit property | Exempt | s.17(2)(vi); *Mohammade Yusuf* (2020) 10 SCC 264; *Mukesh v State of MP*, 2024 INSC 1026 | — |
| Statutory MSA (Mediation Act s.20) | Optional within 180 days with the notified authority; excludes court-referred, Lok Adalat and PLA settlements | LR-MED-005 | — | 

**Steps** (FR-P06-17 retained; additions in bold): duty computation on the market/guidance value **entered by the party from the State portal** (never estimated by AI — NN-01) → stamp procurement → **Sub-Registrar locator** (jurisdiction where the property or any portion is situate — s.28; `core.sub_registrar_offices`; lookup by State, district, tehsil/village or PIN) → **appointment booking** deep link to the State portal (configured per State in `core.registration_portals`: portal name, URL, slot-booking supported, online stamp/fee payment supported, document pre-upload supported; seeded for Delhi, UP, Rajasthan, Maharashtra, Karnataka with `verification_status = UNVERIFIED` until checked) → physical execution checklist (executants' identity, two witnesses, photographs and fingerprints — s.32A; presentation by the persons in s.32; appearance and admission — ss.34–35) → **NRI executants**: execution abroad before an Indian consular officer and presentation within 4 months of arrival of the document in India (s.26) or through an attorney authenticated under s.33 **[VERIFY — open: current consular practice]** → presentation within 4 months (s.23; s.25 extension up to 4 more months on fine) → registered deed uploaded and hashed → certified copy → optional mutation follow-up obligation.

**Clock**: `registration_s23` from physical execution (owner = case manager; T-30, T-7 reminders; `presentation_overdue` blocking task with the s.25 path). Escrow releases may be conditioned on `registration_task.completed`. Closure guard `registration_pending` (F.4.3) applies.

### 4.7 Settlement compliance and default escalation (extends FR-P06-20/22; SCR-P06-64)

Party-facing compliance view: obligations owed **by me** and **to me**, due dates (ICS), evidence upload, "mark as done" (beneficiary confirms or disputes within 7 days; silence = verified with notice), dispute button, instalment grid. Default ladder (FR-P06-22) applies, with the route-specific last step:

| Outcome route | On breach after cure period | Equator output |
|---|---|---|
| X1–X3 (award, consent award, s.74) | Execution pack offered immediately | §4.4 pack |
| X4 with arbitration agreement + consent-to-conversion at signing | Consent-award conversion (s.30) by a tribunal constituted for that purpose, then X2 | Conversion request |
| X4 without | One return-to-mediation session (fee per Appendix B) → contract-enforcement brief + signposting to the civil/commercial court (s.12A PIMS note for commercial suits) | Brief + signposting event (NN-20) |
| X6 Lok Adalat | Execution | `lok_adalat_award_execution` |
| X11/X12 IBC | Default statement for the creditor; settlement's revival/re-filing clause | Statement; signposting to NCLT |
| X13 NI Act | "Default statement" to both parties for the court's next date; the court decides (NN-24) | Statement |
| X14 HMA s.13B / maintenance terms | Signposting to the Family Court; maintenance remedy before the Family Court or Magistrate (BNSS 2023 s.144) | Signposting event |
| FIN NOC/document return | RBI compensation ₹5,000 per day of delay attributable to the RE (RBI/2023-24/60, 13 Sep 2023); signposting to the RE's grievance desk and RB-IOS 2026 | Signposting |
| INS settlement | Signposting to Insurance Ombudsman / Bima Bharosa | Signposting |
| WRK F&F | Claim under Code on Wages 2019 s.45 (3 years) before the authority | Signposting |
| Registration not done | Escrow hold; reminders; closure blocked | Task |

### 4.8 Advocate directory (SCR-P06-65; route `/advocates`)

| Item | Rule |
|---|---|
| Purpose | Help a party find an independent advocate for court steps (execution, s.34 defence, s.47, registration conveyancing, Family Court, NCLT) |
| Eligibility | Advocate verified (Bar enrolment and State Bar Council — App. S §4.5); current certificate of practice; self-declaration of no subsisting disciplinary order |
| Listing data | Only information an advocate may furnish under BCI Rules Part VI Ch. II Section IV r.36 (as amended): name, address, telephone, email; enrolment number, date of enrolment, State Bar Council of original and current enrolment; Bar Association; professional and academic qualifications; areas of practice (BCI Resolution 50/2008, per SC AOR material) **[VERIFY — open (counsel): verbatim r.36 text; whether languages/courts may be used as filter metadata]** |
| Not allowed | Ratings, reviews, success rates, fees advertised, "recommended", paid or featured placement, referral fees, fee-sharing (BCI Rules Section IV rr.36–37; A-04; NN-17) |
| Order | Seeded-random within filters (State, district, court, language, area) |
| Conflicts | Advocates who acted as neutral, or for any party, in the case are hidden for that case; Equator staff and neutrals of the case cannot be listed for it (Mediation Act s.17 policy; A&C s.12) |
| Disclosure | "Equator does not recommend, refer or pay any advocate. Choose freely. Equator receives nothing from listed advocates." |
| Sharing | The party shares the pack by adding the chosen advocate as representative with scope `view_documents` + `court_steps_support` (App. S §4.3; `court_steps_support` is a new scope key to be added to the S §4.3 catalogue) or by a secure link (App. L §2.6) |
| Free routes | Link to Legal Services Authorities (free legal aid under LSA Act 1987 s.12 eligibility) shown first for individuals |

---

## 5. Certified copies and verification (extends FR-P06-18; S8-FR-15; S5-R23)

### 5.1 Copy classes (`core.certified_copies.copy_class`)

| Class | Use | Content and endorsement | Signature | Watermark |
|---|---|---|---|---|
| `CC-CERT` | General certified true copy for a party | Final endorsement page: "Certified to be a true copy of the {instrument} dated {date} in case {case_number}, as held in the records of Equator Resolution Service Private Limited. Copy no. {n} issued to {party label} on {date} for {purpose}." | Registrar DSC (PAdES-B-LT, LTV-enabled) | Footer: case number, copy no., QR |
| `CC-COURT` | Court filing (execution, s.34 defence, s.47) | As CC-CERT; no watermark, no encryption, no annotations (e-filing rules; S8 §1.2) | Registrar DSC | None (QR in footer only) |
| `CC-NYC` | Enforcement abroad (NYC Art. IV(1)(a)) | Authentication certificate + certified copy; feeds apostille workflow (FR-P06-24) | Registrar DSC + wet-ink counterpart on request | None |
| `CC-SR` | Sub-Registrar / revenue office | Certified copy of the award/settlement with the registration annexure | Registrar DSC | Footer |
| `CC-PARTY` | Party's own uncertified copy | Download from portal | Neutral/party signatures only | Viewer name + timestamp |

Release guards: stamp certificate attached (NN-09); s.39 lien cleared (FR-P06-12); requester is a party or a representative with `view_documents` scope; first copy per party free, further copies ANC.CERT.COPY (Appendix B). A copy of a superseded version shows "Corrected — see version {n}" on verification.

### 5.2 QR and code

QR payload: `https://equatorresolution.in/v/{verify_code}` — `verify_code` 26 characters Crockford base32 (128-bit random, FR-P06-18); no case data in the URL; the FR-P06-18 route `/verify/{code}` remains as a permanent redirect so that copies already issued keep working. Printed text under the QR: "Verify at equatorresolution.in/v — code {code}". The same QR appears on orders, notices (with the CVC printed separately for the addressee only), case-history statements and published decisions (Library pages use `/v/` with a public code).

### 5.3 Verification page (`/(public)/v/[code]`; SCR-P06-12 extended; server-rendered, works without JavaScript)

| Shown (L0) | Never shown |
|---|---|
| Document type; issuing institution (legal entity name); case number; date of instrument; date of issue; copy class and number; signatories' **roles** (names only for published decisions or where the instrument is not confidential); e-stamp certificate number; SHA-256; current status (`valid` · `superseded_by_correction` · `stayed_by_court` · `set_aside` · `revoked_issued_in_error`); status date | Content; parties' names; amounts; addresses; any other document of the case |

**File match.** "Check a file" computes SHA-256 **in the browser** (Web Crypto) and sends only the hash; the page answers "Matches" / "Does not match this record". No upload. Signature validation help text explains how to validate the PAdES signature in a PDF reader.

**Third-party verification (banks, Sub-Registrars, courts' staff).** A party generates a **one-time verification code** (`OVC`; 8 characters; valid 7 days; single use; bound to a named recipient organisation and purpose `ENFORCEMENT` · `REGISTRATION` · `BANK_NOC` · `COURT_FILING`) from the portal (`POST /v1/cases/{caseId}/verification-grants`). Entering code + OVC shows, in addition: party names, operative-part summary (amounts and obligations as stated in the instrument), and stamp details. Each use is recorded in the **Disclosure Register** (`core.disclosures`, purpose code, recipient) as an E-mode disclosure (s.42A implementation carve-out; DPDP s.7(e)). Institutional verifiers (banks, registries) may use `GET /v1/verify/{code}?ovc=` with an API key (tenant `machine` principal, scope `verify:read`, 60 requests/minute).

**Abuse controls.** 30 lookups/hour/IP; uniform "not found" response; codes never guessable; the page never asks anyone to sign in or pay; anti-phishing note: "Equator's verification pages are only on equatorresolution.in."

---

## 6. Data model, APIs, events, errors and configuration

### 6.1 Tables (new or additive; Appendix F conventions; tenant RLS + case RLS unless stated)

| Table | Key columns | Constraints / notes |
|---|---|---|
| `core.case_status_views` | case_id, audience_class (`l1`,`party`,`neutral`,`registry`), case_party_id NULL, doc jsonb, version bigint, built_at | CQRS read model; never contains sealed content; rebuilt by `CaseStatusProjector` |
| `core.case_access_codes` | id, case_id, case_party_id, cvc_hmac char(64), issued_at, rotated_at, revoked_at, failed_attempts int, locked_until | UNIQUE (case_id, case_party_id) WHERE revoked_at IS NULL |
| `core.case_applications` | id, case_id, proceeding_id, app_no int, type text CHECK (DD-R-APP-TYPE), filed_by_case_party_id, filed_at, relief_text_i18n jsonb, response_due_at, status text CHECK (DD-R-APP-STATUS), decided_order_id, decided_at, document_id | UNIQUE (case_id, app_no); mediation proceedings allow only logistics types (trigger) |
| `core.case_papers` (view) | paper_no, document_version_id, filed_by, filed_at, pages, status, audience_label | Materialised from `core.documents`/`document_versions`/`document_shares`; `paper_no` from `core.case_paper_sequences` |
| `core.registry_notes` | id, case_id, session_id, version, party_version_document_id, internal_notes_enc bytea, signed_by, signed_at | Internal notes readable by L4 only |
| `core.prior_proceedings` | id, case_id, forum_code, external_case_no, cnr, stage, last_date, outcome, source (`party`,`ecourts_lookup`) | — |
| `core.status_subscriptions` | id, user_id, case_id NULL (all matters), events text[], channels text[], frequency, language | Legal-service notices not suppressible |
| `core.calendar_feeds` | id, user_id, case_id NULL, token_hmac char(64), created_at, revoked_at | Token shown once |
| `core.history_statements` | id, case_id, requested_by, audience_class, document_version_id, sha256, certified boolean | — |
| `core.publication_requests` (P06; additive) | + `mode` (P1–P4), `eligible_modes text[]`, `embargo_until date`, `citation text UNIQUE`, `status` (`proposed`,`awaiting_consents`,`redacting`,`second_review`,`party_preview`,`legal_review`,`scheduled`,`published`,`withdrawn`,`blocked`) | CHECK `status <> 'published' OR (legal_signoff_at IS NOT NULL AND all_consents_given)` (trigger) |
| `core.publication_consents` | id, publication_request_id, case_party_id NULL, neutral_id NULL, mode, items text[], embargo_months, names_mode, amounts_mode, redaction_requests jsonb, gdpr_explicit boolean, notice_version, esign_request_id, status, given_at, withdrawn_at | Exactly one of case_party_id/neutral_id |
| `core.publication_redactions` | id, publication_request_id, version, profiles text[], redacted_document_version_id, token_map_enc bytea, reviewer_1, reviewer_2, reid_test jsonb, approved_at | CHECK reviewer_1 <> reviewer_2 |
| `core.published_decisions` (platform-public projection) | citation PK, type, version, published_at, withdrawn_at, vertical, category_l1, mechanism, year_decided, tribunal_display jsonb, digest_i18n jsonb, html_ref, pdf_sha256, tags text[], noindex_until | No tenant/case identifiers; served by the CMS read API |
| `core.citation_sequences` | year, type, last_value | Row lock |
| `core.court_outcomes` | id, case_id, award_id, forum, court_case_no, cnr, provision (`s34`,`s37`,`s36_stay`,`s47`,`s48`,`execution`), result, decided_on, court_citation | Feeds D12 count |
| `core.disclosures` | id, case_id, purpose (App. L §9.1 CHECK list: `ENFORCEMENT`,`REGISTRATION`,`BANK_NOC`,`COURT_FILING`,`REGULATOR`,`PARTY_COUNSEL`,`PUBLICATION`,`EXPERT`,`INTERPRETER`,`TRANSLATOR`,`BANK_ESCROW`,`SUB_REGISTRAR`), recipient, items jsonb, legal_basis, by_user, at | Append-only; one table shared with App. L secure links (defined in App. L §9.1) |
| `core.verification_grants` | id, case_id, created_by_case_party_id, ovc_hmac, recipient_org, purpose, expires_at, used_at | Single use |
| `core.certified_copies` (P06; additive) | + `copy_class`, `status` value `stayed_by_court` | — |
| `core.court_jurisdiction_rules` | id, state_code, district, court_type (`hc_commercial_division`,`commercial_court`,`district_civil`,`civil_judge_senior`,`civil_judge_junior`,`family_court`,`nclt_bench`), pecuniary_min_minor, pecuniary_max_minor, commercial_designated boolean, ecourts_establishment_code, efiling_portal, court_fee_rule_ref, source_ref, verification_status | Maker–checker; UNVERIFIED rows show the check-forum banner |
| `core.forum_resolutions` | id, case_id, inputs jsonb, rules_applied text[], candidates jsonb, created_by, created_at | Append-only |
| `core.asset_schedules` | id, case_id, execution_pack_id, asset_type, description_enc bytea, state_code, district, pin, identifier_masked, value_minor_party_estimate, source | Tier `high`; visible to the award-holder side and registry |
| `core.execution_proceedings` | id, case_id, execution_pack_id, court, efiling_no, cnr, ep_no, status, next_date, satisfied_minor | — |
| `core.execution_milestones` | id, execution_proceeding_id, status_to, occurred_on, order_document_id, entered_by, source (`party`,`ecourts_lookup_confirmed`), note | Append-only |
| `core.sub_registrar_offices` | id, state_code, district, sro_code, name, address, jurisdiction jsonb, portal_id | Platform data |
| `core.registration_portals` | id, state_code, name, url, slot_booking boolean, online_payment boolean, pre_upload boolean, verification_status | — |
| `core.registration_tasks` (F; additive) | + `instrument`, `sub_registrar_office_id`, `nri_mode`, `s25_fine_path boolean` | — |
| `core.advocate_listings` | id, person_id, enrolment_no, bar_council, enrolled_year, courts text[], states text[], languages text[], areas text[], status (`pending`,`listed`,`suspended`,`withdrawn`), verified_at | No rating columns exist (by design) |

### 6.2 APIs (`/v1`; Idempotency-Key on every creating POST)

| Method and path | Purpose | Auth |
|---|---|---|
| POST `/track/lookup` · POST `/track/verify-cvc` · POST `/track/verify-otp` · GET `/track/status` | L1 flows (S1/S2) | public + CAPTCHA |
| GET `/cases/{caseId}/status` | Portal read model for the caller's audience class | L2+ |
| GET `/cases/{caseId}/papers` · `/applications` · `/notices` · `/sessions` · `/orders` · `/outcomes` · `/payments-timeline` · `/registry-notes` · `/linked-matters` · `/prior-proceedings` | Panels (cursor pagination) | L2+ (policy) |
| POST `/proceedings/{pid}/applications` (P04) · PATCH `/applications/{id}` | Applications register | parties, neutral, registry |
| POST `/cases/{caseId}/registry-notes` · POST `/registry-notes/{id}:sign` | Registry note | case_manager |
| POST `/cases/{caseId}/parties/{partyId}/cvc:rotate` | Rotate CVC | party aal2 / registry |
| GET `/me/matters/search` | S3/S4 search | authenticated |
| PUT `/me/subscriptions/{caseId}` · POST `/me/calendar-feeds` · DELETE `/me/calendar-feeds/{id}` | Notifications and ICS | self |
| GET `/calendar/{token}.ics` | ICS feed | token |
| POST `/cases/{caseId}/history-statements` | Case history PDF | L2+ |
| POST `/publication-requests` · GET `/publication-requests/{id}/eligibility` · POST `/publication-requests/{id}/consents` · POST `/publication-consents/{id}:withdraw` · POST `/publication-requests/{id}/redactions` · POST `/publication-requests/{id}:legal-signoff` · POST `/publication-requests/{id}:publish` · POST `/published-decisions/{citation}:withdraw` | Publication workflow | per §3.8 roles |
| GET `/public/decisions` · GET `/public/decisions/{citation}` · GET `/public/decisions/statistics` · POST `/public/decisions/{citation}/concerns` | Library (CMS read API) | public |
| POST `/cases/{caseId}/forum-resolutions` | Forum resolver | award-holder side, registry |
| POST `/cases/{caseId}/execution-packs` (P06; extended inputs F-EXE-01) | Generate pack | award-holder side, registry |
| POST `/cases/{caseId}/execution-proceedings` · POST `/execution-proceedings/{id}/milestones` · POST `/execution-proceedings/{id}:sync-ecourts` | Execution tracking | award-holder side |
| GET `/registration/sub-registrar-offices?state=&district=&pin=` · POST `/registration-tasks/{id}/appointment` | Registration | parties, case_manager |
| GET `/advocates` · POST `/me/advocate-listing` | Directory | public / counsel |
| POST `/cases/{caseId}/verification-grants` · GET `/public/verify/{code}` · GET `/verify/{code}?ovc=` | Verification | public / party / machine `verify:read` |
| POST `/cases/{caseId}/court-outcomes` | Record court decision | registry |

### 6.3 Events (`equator.<ctx>.<entity>.<verb>.v1`; IDs and codes only)

`equator.cases.status_view.rebuilt.v1` (case_id, audience_class) · `equator.cases.status.l1_viewed.v1` (case_id, mode, case_party_id) · `equator.cases.cvc.rotated.v1` · `equator.proceedings.application.filed.v1` **W** / `.decided.v1` **W** (application_id, type, status) · `equator.cases.registry_note.issued.v1` (registry_note_id, session_id) · `equator.cases.history_statement.generated.v1` · `equator.outcomes.publication.requested.v1` · `equator.outcomes.publication_consent.given.v1` / `.withdrawn.v1` (consent_id, mode) · `equator.outcomes.publication.redaction_approved.v1` · `equator.outcomes.publication.legal_signed_off.v1` · `equator.outcomes.publication.published.v1` (citation, type) · `equator.outcomes.publication.withdrawn.v1` (citation, reason_code) · `equator.execution.forum.resolved.v1` · `equator.execution.proceeding.registered.v1` **W** · `equator.execution.milestone.recorded.v1` **W** (execution_proceeding_id, status_to) · `equator.execution.proceeding.satisfied.v1` **W** · `equator.execution.registration.appointment_booked.v1` · `equator.execution.court_outcome.recorded.v1` **W** (provision, result) · `equator.documents.certified_copy.issued.v1` (copy_class) · `equator.documents.verification.performed.v1` (code_prefix, result, with_ovc boolean) · `equator.documents.disclosure.recorded.v1` (purpose). Consumers: AUD all; NOT for consent, milestone and publication events; RPT for statistics; CMS for `published`/`withdrawn`.

### 6.4 Errors (add to F.10.1 unless shown as sub-codes)

`STATUS_LOOKUP_FAILED` 200-uniform (never an error to the client; logged only) · `CVC_LOCKED` 429 "Too many attempts for this case. Try again in an hour or use a one-time code." · `PUBLICATION_NOT_ELIGIBLE` 422 "This matter cannot be published in that form." · `PUBLICATION_CONSENT_MISSING` 409 "Every party and the tribunal must consent first." (maps P06 sub-code) · `PUBLICATION_GATES_INCOMPLETE` 409 · `PUBLICATION_EMBARGO_ACTIVE` 409 · `PUBLICATION_FLAG_OFF` 409 "Publication is not yet enabled." · `REDACTION_SAME_REVIEWER` 403 · `REPRESENTATIVE_CANNOT_CONSENT_PUBLICATION` 403 · `EXECUTION_NOT_READY` 409 "Enforcement papers are available after the challenge period or a decision on a challenge." · `EXECUTION_STAYED` 409 · `FORUM_RULE_UNVERIFIED` 200 with warning flag (never blocks) · `OVC_INVALID_OR_EXPIRED` 404-uniform · `CERTIFIED_COPY_LIEN_ACTIVE` 409 "The award is held for unpaid deposits (A&C s.39)." · `ADVOCATE_NOT_VERIFIED` 409 · `MEDIATION_APPLICATION_TYPE_NOT_ALLOWED` 422.

### 6.5 Feature flags and config keys

Flags (legal flags default OFF): `publication.arbitral.enabled` (Q-R1) · `publication.consensual.enabled` (Q-R3) · `publication.p4.enabled` · `publication.challenge_decisions.enabled` (Q-R2; supersedes V6 `intl.publish_challenge_decisions`) · `intl.publish_composition_register` (V6; unchanged, OFF) · `mediation.s20_registration` · `mediation.s27_decree_enforcement` · `execution.ecourts_sync.enabled` (needs connector terms) · `portal.notice_requests.enabled` (caveat-analogue notice requests, OFF pending privacy review) · `advocate_directory.enabled`. Release flags: `portal.v2_panels`, `library.public`. Config kinds: `dashboard_pack.next_sentence` (legal), `dashboard_pack.who_decides` (legal), `pub.eligibility` (legal), `pub.redaction_profiles` (legal), `pub.issue_tags` (standard), `execution.routes` (legal), `execution.forum_resolver` (legal), `court_jurisdiction_rules` (legal, data), `registration_portals` (standard), `copy_classes` (legal).

---

## 7. Acceptance tests (Gherkin; `tests/acceptance/appendix-R.feature`)

```gherkin
Feature: Appendix R — case status, case desk, publication, execution, registration, verification

  Scenario: R-01 L1 status by reference and CVC
    Given case "EQ/COM/DEL/2027/00042" in state "in_proceedings" with an arbitration proceeding
    And claimant's CVC "7KQ2M-9XR4T"
    When an anonymous visitor submits the case number, the CVC and a solved CAPTCHA at "/track"
    Then the status card shows "In progress", the next date and purpose, and "The arbitral tribunal decides"
    And party names appear as initials only and no arbitrator name is shown
    And an access-log entry records purpose "status_l1", mode "S1" and the claimant's case_party_id

  Scenario: R-02 Uniform response prevents enumeration
    When a visitor submits a non-existent case number with any CVC
    Then the response text equals the response for an existing case with a wrong CVC
    And the response time differs by no more than 50 ms plus jitter across 100 trials

  Scenario: R-03 CVC lock
    Given 5 wrong CVC attempts on one case number within 10 minutes
    When a sixth attempt is made with the correct CVC
    Then the visitor sees the uniform message and S1 stays locked for 60 minutes
    And S2 (one-time code to a contact point on the case) remains available

  Scenario: R-04 Restricted matters at L1
    Given a FAM case with a correct CVC
    When the visitor completes S1
    Then only "Status available to parties in their account. Sign in to see it." is shown

  Scenario: R-05 Party-name search is limited to own matters
    Given an authenticated party "Meera Iyer" who is a party to 2 cases
    And 40 other cases name a person called "Meera"
    When she searches "Meera" at "/app/matters/search"
    Then exactly her 2 cases are returned

  Scenario: R-06 Papers register hides the other side's private and caucus shares
    Given the respondent filed P-7 with audience "NEUTRAL_ONLY" in a mediation
    When the claimant opens the papers register
    Then no row for P-7 exists and no gap in numbering is explained
    And the mediator sees P-7 labelled "Mediator only"

  Scenario: R-07 Mediation sessions have no minutes (NN-11)
    Given a completed mediation session
    When any party opens the sessions panel
    Then the record column reads "No record is kept of what is said in mediation"
    And no transcript or minutes link exists

  Scenario: R-08 Registry note generated before a session
    Given an arbitration session on 15 Mar 2027 10:30 IST
    When the clock reaches 11 Mar 2027 10:30 IST (T-2 working days)
    Then a registry note draft exists with service status per party, open directions, pending applications and s.29A days left
    And the party version contains no "registry-only notes" section

  Scenario: R-09 ICS feed contains no names
    Given a FAM case session
    When the party's ICS feed is fetched
    Then the event title is "Equator appointment" and the description contains only a portal link

  Scenario: R-10 What-happens-next sentence is deterministic
    Given the LLM is unavailable
    When the claimant opens a case awaiting response due 12 Nov 2026
    Then the sentence reads "The other party has until 12 Nov 2026 to respond. If they don't, we will tell you your options."

  Scenario: R-11 Publication needs every party (NN-26)
    Given a final COM award, flag "publication.arbitral.enabled" ON
    And the claimant consents to P3 and the respondent has not responded
    When the registrar tries to publish
    Then the request fails with "PUBLICATION_CONSENT_MISSING"

  Scenario: R-12 Most restrictive mode wins
    Given claimant consents to P3 and respondent consents to P2, tribunal consents
    When eligibility is computed
    Then the publication mode is "P2"

  Scenario: R-13 FAM never beyond digest
    Given a FAM partition award with all-party consent to P3
    When eligibility is computed
    Then P3 and P4 are not offered and "PUBLICATION_NOT_ELIGIBLE" is returned for P3

  Scenario: R-14 POSH and safety-flagged matters are never published or counted
    Given a case with safety_flag true
    When the quarterly statistics job runs
    Then the case is excluded from every P1 cell
    And no publication request can be created for it

  Scenario: R-15 Representative cannot consent alone
    Given counsel with scope "file, respond, attend" for the respondent
    When counsel submits F-PUB-02 on the respondent's behalf
    Then the request fails with "REPRESENTATIVE_CANNOT_CONSENT_PUBLICATION"

  Scenario: R-16 Two-person redaction review
    Given quality officer Q1 produced redaction v1
    When Q1 attempts the second review
    Then the action fails with "REDACTION_SAME_REVIEWER"

  Scenario: R-17 Withdrawal after publication
    Given "EQR/2027/AWD/0003" was published on 2 Aug 2027
    When a party withdraws consent on Friday 6 Aug 2027 at 17:00 IST
    Then by Monday 9 Aug 2027 17:00 IST (72 hours, which is earlier than 2 working days) the page shows only the withdrawal tombstone
    And the citation still resolves, the PDF is not publicly retrievable and the sitemap omits it

  Scenario: R-18 Citation format and no court styles
    When the first award of 2027 is published
    Then its citation is "EQR/2027/AWD/0001"
    And the page contains the banner "It is not a judgment of a court"
    And lint R-LINT-01 finds none of "INSC", "Hon'ble", "judgment of this", "decree" in Equator-authored text

  Scenario: R-19 Library has no outcome facet
    When the "/decisions" filter list is rendered
    Then no filter or sort relates to who succeeded or to party type by result

  Scenario: R-20 Execution pack guard during s.34 window
    Given an award delivered to the respondent on 1 Feb 2027 and no challenge notified
    When the award-holder requests an execution pack on 15 Apr 2027
    Then the request fails with "EXECUTION_NOT_READY" and shows the s.34 dates per party

  Scenario: R-21 Execution pack after lapse
    Given the s.34 windows of all parties lapsed and no stay is recorded
    When the award-holder submits F-EXE-01 with assets in Jaipur and Pune
    Then two packs are generated, one per forum candidate, each disclosing the other under O.XXI r.11(2)(f)
    And each pack contains the O.XXI r.11(2) application, asset-disclosure application, registrar-certified award (CC-COURT), registry statement, computation sheet, s.63(4) Part A certificate and manifest

  Scenario: R-22 Forum resolver never ranks by predicted success (NN-01)
    When the forum resolver returns candidates
    Then the order is by asset value entered by the party and every row shows "Confirm with your advocate"

  Scenario: R-23 Execution milestones from eCourts are proposals only
    Given flag "execution.ecourts_sync.enabled" ON and a CNR on record
    When the sync finds a new "attachment ordered" entry
    Then the party sees a proposed milestone that is applied only after confirmation

  Scenario: R-24 Registration clock and closure
    Given a partition deed physically executed on 1 Mar 2027
    Then a "registration_s23" clock is due on 1 Jul 2027 with owner case_manager
    And the case cannot close while the registration task is open ("CLOSURE_BLOCKED" with "registration_pending")

  Scenario: R-25 Mediation Act s.27 route hidden while flag OFF (NN-05)
    Given flag "mediation.s27_decree_enforcement" OFF
    When a party opens the execution desk for a contractual MSA
    Then routes X4 options are shown and no text mentions "s.27" enforceability

  Scenario: R-26 Verification shows no content
    Given certified copy code "Q7…" for an award
    When a visitor opens "/v/Q7…"
    Then the page shows document type, case number, dates, roles, stamp number, SHA-256 and status "valid"
    And no party name or amount appears
    And with a valid OVC for purpose "BANK_NOC" party names and the operative summary appear and a disclosure row is written

  Scenario: R-27 Advocate directory neutrality
    When "/advocates" is filtered by "Rajasthan" and "execution"
    Then results are in seeded-random order, show no ratings or fees, and exclude advocates who acted in the viewer's case
```

---

## 8. Open items and counsel questions

| # | Question | Blocks |
|---|---|---|
| Q-R1 | Can all-party consent release **the arbitral institution's** s.42A duty so that Equator may publish a redacted or full India-seated award? Must consent be post-award, and does s.42A cover anonymised digests and statistics? (02 §5 Q1; S8 Q1; S5 F-1, F-2) | `publication.arbitral.enabled` |
| Q-R2 | Is a rules-based deemed consent (SIAC r.28.7 model) sufficient for publishing redacted Challenge Committee decisions, or is express post-dispute consent required? | `publication.challenge_decisions.enabled` |
| Q-R3 | Whether s.75 (conciliation) and contractual mediation confidentiality permit digests of settlements with all-party consent; position once Mediation Act s.22 is notified | `publication.consensual.enabled` |
| Q-R4 | DPDP threshold for "anonymised" publications; whether redaction to RP-1…RP-3 takes P2/P3 outside the Act; Board expectations on re-identification testing (S8 Q9) | DPIA sign-off |
| Q-R5 | Does CCA 2015 s.10(3) route **execution** of commercial domestic awards (specified value ≥ ₹3 lakh) to the Commercial Court in every State? State-wise forum table; HC pecuniary limits (S8 Q3) | `core.court_jurisdiction_rules` verification |
| Q-R6 | In the optional internal appeal tier, from which award does the s.34 period run, and is the first-tier award separately challengeable? | X16 |
| Q-R7 | Limitation for executing domestic awards: Art. 136 vs Art. 137 (V0124); limitation start for s.74 settlements | X1–X3 clocks |
| Q-R8 | Applicability of *Sundaram Finance* asset-situs filing to India-seated ICA awards (s.2(1)(e)(ii)) | FR-4 |
| Q-R9 | BCI Rules r.36 (as amended) — permitted directory fields; whether a free, unranked directory hosted by an ADR institution raises any solicitation issue | `advocate_directory.enabled` |
| Q-R10 | Registry statement: wording that is safe to file in court without implying certification of court records | Execution pack doc 5 |
| Q-R11 | Mediation Act s.20 (when notified): may an MCI-recognised MSP register MSAs on the parties' behalf (S8 Q17) | `mediation.s20_registration` |
| Q-R12 | Whether a caveat-analogue "notice request" (portal.notice_requests) is compatible with DPDP purpose limitation and s.42A | `portal.notice_requests.enabled` |

Open data items: CPC Appendix E form number for execution applications and State amendments; *Bhandari Engineers* affidavit-of-assets proforma citation; State registration portal names and features; e-Courts eFiling 3.0 State variations; family-settlement memorandum stamp treatment per State.

---

## Phase addendum (paste into P02)

**FR-P02-V2-R01 — Tracker v2 (S1/S2/S6).** Extend FR-P02-44 with CVC (`core.case_access_codes`), OTP alternative, lock and uniform responses (§1.2), restricted-matter rule (§1.1). *Acceptance:* R-01, R-02, R-03, R-04 pass; the tracker page works with JavaScript disabled.

**FR-P02-V2-R02 — Case header and panels.** Implement §1.3 header and §1.4.1–§1.4.10 panels on the `core.case_status_views` read model with the §1.5 matrix and §1.6 confidential categories. *Acceptance:* R-06 and R-07 pass; matrix-driven policy tests (one allow, one deny per non-empty cell) are green; read-model lag p95 < 2 s.

**FR-P02-V2-R03 — Papers register numbering.** Gap-free `P-{n}` per case from `core.case_paper_sequences`; hidden rows are absent, not greyed. *Acceptance:* concurrent filings (50 parallel) produce unique, gap-free numbers; R-06 passes.

**FR-P02-V2-R04 — Registry note.** `core.registry_notes`, template `eqr.tpl.registry_note.v1`, T-2 working-day generation and e-sign. *Acceptance:* R-08 passes; holiday calendar respected.

**FR-P02-V2-R05 — What happens next and who decides.** Rule-table engine (`dashboard_pack.next_sentence`, `.who_decides`), en + hi (legal-translator review), no AI. *Acceptance:* R-10 passes; bilingual parity test passes for all seeded rows.

**FR-P02-V2-R06 — Clocks, ICS and subscriptions.** §1.4.13–§1.4.15 with `core.calendar_feeds`, `core.status_subscriptions`. *Acceptance:* R-09 passes; revoking a representative rotates that representative's feeds within 60 s.

**FR-P02-V2-R07 — Case history statement.** §1.4.16 PDF with watermark, QR and ledger hash; certified version via P06. *Acceptance:* the statement contains only rows visible to the requester (diff test against the requester's API view).

**FR-P02-V2-R08 — My-matters search and registry search.** S3, S4, S5 (§1.2). *Acceptance:* R-05 passes; S5 excludes sealed indices.

**FR-P02-V2-R09 — Case Desk.** §2.1 and §2.3 desks (party, case manager) with readiness checklist and action inbox. *Acceptance:* every next action reachable in ≤ 2 clicks from the desk (Playwright click-budget lint); messages to the tribunal are copied to all parties (ex parte guard test).

**FR-P02-V2-R10 — Earlier and parallel proceedings.** `core.prior_proceedings`, mandatory for FIN (DRT/SARFAESI), COM (NCLT/commercial court) and FAM (family court) intake; eCourts CNR lookup behind `CONNECTOR_PORT`. *Acceptance:* FIN intake cannot be submitted without the prior-proceedings question answered (yes with details / no).

**FR-P02-V2-R11 — Mobile portal layout.** §1.7 on Expo (with P12). *Acceptance:* ≤ 4 API calls on open; screen capture blocked on high/sealed.

## Phase addendum (paste into P06)

**FR-P06-V2-R01 — Publication eligibility and modes.** `pub.eligibility` rule (§3.3), modes P0–P4/E (§3.2), most-restrictive merge, flags §6.5 default OFF. *Acceptance:* R-12, R-13, R-14 pass; no publication path exists for POSH or safety-flagged matters (NN-26/NN-07 tests).

**FR-P06-V2-R02 — Consent capture.** F-PUB-01 (filing preference, non-binding), F-PUB-02 (party, e-signed), F-PUB-03 (tribunal), state machine §3.4, withdrawal one click + OTP. *Acceptance:* R-11 and R-15 pass; a filing-stage preference never satisfies the consent gate.

**FR-P06-V2-R03 — Redaction pipeline.** RP-1…RP-8 and RP-SEX (§3.6), token map encrypted, two-person review, re-identification test record, party preview 30 days, legal sign-off (§3.8). *Acceptance:* R-16 passes; seeded test decisions show zero residual identifiers in an automated NER sweep; the token map is unreadable by `eq_app` outside the publication service.

**FR-P06-V2-R04 — Decisions Library back end.** `core.published_decisions`, `core.citation_sequences`, citation format §3.9.2, versioning, withdrawal/tombstone, CDN purge, sitemap and search-engine removal hooks (§3.11). *Acceptance:* R-17 and R-18 pass.

**FR-P06-V2-R05 — Court outcomes register.** `core.court_outcomes`; D12 count; Library entry auto-withdrawn on `set_aside`. *Acceptance:* recording a set-aside unpublishes any Library entry for that award within 2 working days and increments the statistic.

**FR-P06-V2-R06 — Route matrix and forum resolver.** `execution.routes` (§4.2, rows X1–X18 as Legal Rules Register entries) and `execution.forum_resolver` with `core.court_jurisdiction_rules` (UNVERIFIED rows carry the check-forum banner). *Acceptance:* R-22 passes; each X-row has a legal-rule ID and status; X5 hidden while NN-05 flag OFF (R-25).

**FR-P06-V2-R07 — Execution pack v2.** F-EXE-01 inputs, readiness guards, documents 1–9 (§4.4), multi-forum packs, e-filing checklist. *Acceptance:* R-20 and R-21 pass; packs validate with veraPDF and contain the manifest and s.63(4) Part A (NN-10).

**FR-P06-V2-R08 — Execution tracking.** `core.execution_proceedings`, `core.execution_milestones`, state machine §4.5, informational clocks, O.XXI r.2 reminder, optional eCourts sync (proposals only). *Acceptance:* R-23 passes; `satisfied_full` drives Appendix A C43.

**FR-P06-V2-R09 — Registration v2.** Instrument chooser, Sub-Registrar locator, State portal deep links, NRI path, s.23/s.25 clocks (§4.6). *Acceptance:* R-24 passes; a deed of family settlement cannot be routed to e-sign (`ESIGN_EXCLUDED_INSTRUMENT`).

**FR-P06-V2-R10 — Compliance and default escalation by route.** §4.7 table wired into FR-P06-22. *Acceptance:* each route's breach produces the stated output in an integration test per row.

**FR-P06-V2-R11 — Certified copies v2 and verification.** Copy classes §5.1, `/v/{code}` page with in-browser hash match, OVC third-party grants with the Disclosure Register, verification API. *Acceptance:* R-26 passes; CC-COURT copies contain no watermark or encryption; every OVC use writes `core.disclosures`.

**FR-P06-V2-R12 — Advocate directory.** §4.8 with conflicts and BCI-compliant fields behind `advocate_directory.enabled`. *Acceptance:* R-27 passes; schema has no rating or fee columns.

**FR-P06-V2-R13 — Role-limit copy.** `exe.role_note` and R-LINT-01 on all execution and registration screens and documents. *Acceptance:* copy lint passes; no execution document is signed by Equator on a party's behalf.

## Phase addendum (paste into P04)

**FR-P04-V2-R01 — Applications register.** `POST /proceedings/{pid}/applications` writes `core.case_applications` with `DD-R-APP-TYPE`/`DD-R-APP-STATUS`; decisions link to `core.orders`; V6 `intl.procedural_applications` migrates to a 1:1 extension (R-R8). *Acceptance:* a mediation proceeding rejects substantive application types with `MEDIATION_APPLICATION_TYPE_NOT_ALLOWED`.

**FR-P04-V2-R02 — Session records for the portal.** Sessions expose kind, mode, purpose (`DD-R-SESSION-PURPOSE`), per-side attendance and result; arbitration minutes/orders link; caucus sessions visible only to the side concerned. *Acceptance:* R-07 passes.

**FR-P04-V2-R03 — Neutral desk.** §2.2 (directions tracker, applications queue, s.29A cockpit, private notes, deposits, time record, tribunal publication consent). *Acceptance:* every direction in an issued order appears in the tracker within 60 s.

## Phase addendum (paste into P12)

**FR-P12-V2-R01 — Mobile case portal and desk.** §1.7 layout, primary action bar, offline last-view cache, push deep links to panel rows. *Acceptance:* Maestro flow "open case from push → upload requested document" completes in ≤ 5 screens.

## Phase addendum (paste into P13)

**FR-P13-V2-R01 — Decisions Library front end.** `/decisions`, decision pages, digests, statistics, about/policy, "Report a concern" form (§3.9), `noindex` rules and structured data (§3.13), no third-party trackers. *Acceptance:* R-19 passes; Lighthouse ≥ 90 performance and accessibility on a decision page; withdrawn citations render the tombstone.

**FR-P13-V2-R02 — Tracker and verification public pages.** `/track` and `/v/{code}` copy from §1.8 and §5.3; claims linter blocks court framing (R-LINT-01). *Acceptance:* copy lint passes; pages work without JavaScript.

---

*End of Appendix R.*
