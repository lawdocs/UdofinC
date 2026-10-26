# Equator Resolution — Website Content Deck v1.0 *(v3.2, 26 October 2026)*

**Prepared:** 26 October 2026 · **Owner:** Company Secretary, Infrabyx Group · **Entity:** Equator Resolution Service Private Limited · **Status:** Draft copy for legal review (Appendix P §7.3 checklist) before any page is published · **Companions:** Appendix P (copy deck, lint rules LINT-001–LINT-051, SEO/GEO system), Appendix AG §AG.2.1 (public mega-menu), Appendix AF §AF.6 (REC-01–REC-20), Appendix U (policy baselines), IPB-04 (standard pages, footer, CMP), IPB-05 (policy templates), IPB-07 (help and glossary)

---

## 0. How to use this deck

### 0.1 What this deck is

Full, publish-ready English copy for every public page of equatorresolution.in that the v3.1 pack specified by structure only, plus the pages IPB-04 §04.3.7 adds (Team, Leadership, Investors, Documentation hub, Resources library, Blog landing with user posts, Changelog, Accessibility statement, Partners, Press and media kit). Pages that Appendix P already writes in full (P-01 to P-54) are **not** rewritten here; this deck gives them a one-paragraph "v3.2 delta" where IPB-04 or the Jupitice review (Appendix AF; `_research/R_Jupitice_and_ODR_Websites.md`) changes a section, and otherwise points to the P-nn entry. Where this deck and Appendix P differ on a locked line (brand line, identity strip, never-say list), Appendix P prevails; where they differ on page structure, this deck prevails for the pages it owns (P-55 onwards) and Appendix P §3.1 is updated to list them.

### 0.2 Rules every page obeys

| Rule | Source |
|---|---|
| No fact is typed into copy. Entity particulars, fees, counts, dates and names render from tokens (`{{entity.*}}`, `{{fee:*}}`, `{{metric:*}}`, `{{rule:*}}`, `{{person:*}}`) or from the Claims Register. A page with an unresolved token cannot publish. | Appendix P §0.2; NN-17 |
| Claims Register binding: every statistic, badge, logo, testimonial, certification or regulatory-status statement links to an evidence record with owner, source date and expiry. Statistics expire in 35 days by default. | FR-P13-10; IPB-04 §04.3.1 |
| Never-say list: "RBI-approved", "RBI audited", "ISO certified" (until certified), "100% secure", "guaranteed", "legally binding in every case", "court", "judge", "decree" for Equator's own outputs, "world's first", "India's largest", "only", "#1", any competitor name outside the Appendix P §0.2 benchmark rule, any success or settlement rate. | Appendix P §1.4; LINT-001–LINT-026; REC-11 |
| Identity strip on every vertical, subtype, mechanism and Explorer page: "Equator Resolution is a private dispute resolution institution — not a court, regulator or government body. We will tell you when a free public forum may suit you better." | Appendix P §3.0; NN-20 |
| Signposting before selling: every dispute page names the free or statutory forum first where one exists. | NN-20; FR-P13-04 |
| Prices: GST-inclusive totals shown before payment for consumers; the pricing page states the GST label; no drip pricing, no countdowns, no "only N left". | NN-29; IPB-04-35, IPB-04-36 |
| Fees before booking: neutral fee, administrative fee, any processing fee and GST are published on the fee page and in the calculator before any booking step. | REC-03 |
| Server-rendered trust sections: badges, advisory council, governance, investors and team never render client-side only; empty sections show an honest empty state, never a spinner. | Appendix AF §AF.1.7 W1, W10; IPB-04 §04.3.7 |
| Date everything: every page shows "Last reviewed" in its footer region; every policy shows version and effective date; every statistic shows its as-of date and method link. | IPB-04-70; Appendix P §6.9 |
| Plain English, active voice, British/Indian spelling, sentences ≤ 25 words in heroes, answer-first FAQs (first sentence answers in ≤ 25 words). | Appendix P §1.3, §3.0 |
| Accessibility: one H1; headings in order; alt text for every image; no text in images; link text says where it goes; forms label every field; videos have captions and transcripts. | NN-23; IPB-06 |
| No copy is taken from any competitor site. Structures were studied (Appendix AF, `_research/R_Jupitice_and_ODR_Websites.md`); words are Equator's own. | Brief §1 |

### 0.3 Tags used

[LAW] statutory rule · [INTERP] interpretation · [REC] recommendation · [VERIFY] fact to confirm before publish · [OWNER] owner decision needed · [COUNSEL] counsel wording required. Every [VERIFY] in this deck has a row in Appendix J §J.10 (V32-OI series) and renders behind a default-OFF block until closed.

### 0.4 Page register (this deck's IDs continue Appendix P's P-nn series)

| ID | Route | Page | Status in v3.1 | This deck |
|---|---|---|---|---|
| P-01 | `/` | Home | Full copy in Appendix P | Full rewrite below (v3.2 structure: proof row, trust teaser, resources teaser, FAQ) |
| P-02, P-21–P-27 | `/how-it-works`, `/mechanisms/*` | Resolve | Full copy | Delta: timelines table, "fees before booking" block, hybrid page |
| P-04–P-19 | `/disputes/*` | Disputes | Full copy | Delta: vertical landing lead copy aligned to the v3.2 hub pattern |
| P-35, P-36, P-54 | `/neutrals`, `/neutrals/join`, `/neutrals/panels` | Neutrals | Full copy | New: "How neutrals are graded" and "Independence Evidence Pack" pages (P-62, P-63) |
| P-49 | `/marketplace` | Marketplace | Full copy | Delta only |
| P-28–P-33 | `/for/*` | For organisations | Full copy | Delta only |
| P-34 | `/private-adr-chambers` | Chambers | Full copy | Delta only |
| P-37 | `/training` | Training | Full copy | Delta: Institute arm's-length block |
| P-44 | `/about`, `/about/governance` | About, Governance | Partial | Full rewrite (P-55 About; P-56 Governance) |
| P-57 | `/about/advisory-council` | Advisory Council | Empty state only | Full copy |
| P-58 | `/team` | Team | Missing | Full copy with placeholders |
| P-59 | `/leadership` | Leadership | Missing | Full copy with placeholders |
| P-60 | `/investors` | Investors (toggle) | Missing | Full copy [COUNSEL] |
| P-47 | `/careers` | Careers | Partial | Full rewrite (P-61) |
| P-62 | `/neutrals/how-we-grade` | How neutrals are graded | Missing | Full copy |
| P-63 | `/trust/independence-evidence-pack` | Independence Evidence Pack | Missing | Full copy |
| P-64 | `/docs` | Documentation hub | Developer portal only | Full copy |
| P-51 | `/press` | Press and media kit | Route copy | Full rewrite (P-65) |
| P-66 | `/partners` | Partners | Partner programme form only | Full copy |
| P-43 | `/trust` | Trust & Security | Full copy | Delta: Vendor Assurance Room entry, certifications block from `TRUST` port |
| P-46 | `/help` | Help | Full copy | Delta: tutorials, video, "Ask Vidhi" |
| P-38, P-39 | `/fees`, `/pricing/*` | Pricing | Full copy | Delta: Pricing Studio copy layer |
| P-67 | `/resources` | Resources library | Missing | Full copy |
| P-68 | `/blog` | Blog landing (with user-post programme) | Missing | Full copy |
| P-45 | `/contact` | Contact | Full copy | Delta: Delhi/Noida/Jaipur blocks, WhatsApp consent button |
| P-69 | `/changelog` | Changelog | Missing | Full copy |
| P-70 | `/accessibility` | Accessibility statement | Appendix U §U.10 baseline | Page copy (statement text from U-10) |
| P-71 | `/vlog` | Vlog | Missing | Full copy |
| — | footer, cookie banner | Sitewide | Partial | Full copy |

---

## 1. Home — `/` (P-01, v3.2 rewrite)

| Field | Copy |
|---|---|
| SEO title | Online Dispute Resolution in India \| Equator Resolution |
| Meta description | Mediation, conciliation and arbitration online, administered by an independent institution. Clear fees, published rules, independent neutrals. |
| H1 | Resolve disputes, not relationships. |
| Hero one-liner | Equator Resolution is an independent institution for mediation, conciliation and arbitration, online, under published rules, with fees you see before you start. |
| Hindi hero | विवाद सुलझाइए, रिश्ते नहीं। |
| Primary CTA | Understand your options → `/dispute-explorer` |
| Secondary CTA | Respond to a notice → `/respond` |
| Schema | `WebSite`, `Organization` (legal name, logo, `sameAs` from footer social, `contactPoint` support and grievance) |

**Section 1 — Hero.** H1 and one-liner above. Beneath the CTAs, a single line of small text: "Not a court. Not a regulator. We say so on every page, and we tell you when a free forum may suit you better."

**Section 2 — What Equator does (feature grid, four tiles).**

- **Mediation.** A trained, independent mediator helps both sides reach terms they choose. Nothing is imposed. Sessions are private and are not recorded.
- **Conciliation.** Under Part III of the Arbitration and Conciliation Act 1996, a conciliator can propose terms; a signed settlement has the status of an arbitral award (s.74) [LAW].
- **Arbitration.** An arbitrator appointed from Equator's panel by published rules hears the matter and issues an award. Clients never choose or veto the arbitrator (NN-03).
- **Hybrid and staged processes.** Negotiation first, then mediation, then arbitration if needed — each step a choice, each with its own fee, published in advance.

**Section 3 — Who it is for (three columns).**

- **People and families.** Loan settlements, insurance claims, workplace issues, family property. Plain language, Hindi and English, help to understand your options before you pay anything.
- **Businesses and MSMEs.** Unpaid invoices, contract disputes, shareholder and partnership matters, cross-border commercial disputes. Model clauses you can put in your contracts today.
- **Organisations.** Lenders, insurers, employers, universities and marketplaces that need a defensible, independent process for many disputes at once, with grievance redressal and POSH Internal Committee tools.

**Section 4 — How it works (five steps).**

1. **Understand your options.** Answer a few questions. The Dispute Explorer tells you which processes fit, what they cost, how long they usually take, and whether a free public forum is the better route.
2. **File or respond.** Upload your documents; we pre-fill what we can and you confirm. The other side receives a notice through verified channels.
3. **A neutral is appointed by rule.** Mediators and arbitrators come from Equator's independent panel through a published allocation process with conflict checks.
4. **Meet online.** Secure video rooms built for hearings and private sessions, with captions, interpreters on request, and no recording of mediation.
5. **Settle or decide.** Settlement agreements and awards are drafted, e-signed and e-stamped where the law allows, with a verifiable copy and a hash you can check on this site.

**Section 5 — Proof row (`StatBand`; claims-register only).** Default empty state until the first transparency report: "We will publish our first statistics after {{metric:first_report_month}}, with the method we used." When live, three tiles maximum: median days from filing to first session; share of cases where a free forum was signposted; number of published rules versions. Never a success or settlement rate (NN-28, X-28). Each tile shows "as of {{metric:as_of}}" and a "How we count" link to `/trust/outcomes`.

**Section 6 — Why an institution, not just a platform (three proof points, each with a link).**

- **Independent appointments.** No party chooses the neutral. Our allocation rules are published and every appointment carries an Independence Evidence Pack. → `/trust/how-we-stay-neutral`
- **Published rules and fees.** The Equator Resolution Rules, Code of Conduct and fee schedules are versioned, dated and free to read. → `/rules`, `/fees`
- **Governance kept apart from commerce.** Case decisions sit with an Institutional Committee with a majority of external members. The company's board takes no case decisions. → `/about/governance`

**Section 7 — Security and trust teaser.** "Your documents stay in India. Evidence is hash-sealed. Mediation is never recorded. Read what we do, what we hold and what we do not claim." → `/trust`. Badges render only for certifications actually held, from the Vendor Assurance Room, with issuer and scope on hover (IPB-04-68). Empty state: "Certification status: readiness programme in progress — see our Trust Centre for what is complete."

**Section 8 — Pricing teaser.** "Fees are published before you book. Use the calculator for an indicative total including GST." → `/fees/calculator`. No figures in this block (Appendix P §3.0 field rules).

**Section 9 — Resources teaser (three cards from the Resources library and Blog).** Latest transparency report (when published), latest guide, latest rules version. Cards carry type, date and reading time.

**Section 10 — For organisations strip.** "Running disputes at scale? Grievance redressal, POSH Internal Committee tooling, bulk filing and an API — with the same independent panel." → `/for`

**Section 11 — FAQ accordion (answer-first; six items from the FAQ bank §12: F-01, F-02, F-05, F-09, F-14, F-22).**

**Section 12 — Final CTA.** "Start with your options, not with a fee." Buttons: Understand your options · Talk to our case team (process questions only — we cannot advise on your case).

---

## 2. Resolve — `/how-it-works` and `/mechanisms/*` (P-02, P-21–P-27 deltas; new P-72 hybrid)

### 2.1 How it works — `/how-it-works` (delta to P-02)

Add after the ladder explainer:

**Timelines you can plan around (table; values from `{{rule:*}}` tokens, never typed).**

| Process | Typical first session | Usual completion window | Clock that applies | Who sets the pace |
|---|---|---|---|---|
| Negotiation (assisted) | {{rule:neg.first_contact_days}} working days from the other side's acceptance | {{rule:neg.timebox_days}} days (FIN default 21) | Equator's procedural time-box | The parties |
| Mediation (contractual mode) | {{rule:med.first_session_days}} days from appointment | {{rule:med.window_days}} days, extendable by consent | Mediation agreement; Mediation Act statutory mode not yet in force for us (NN-05) | The parties with the mediator |
| Conciliation (A&C Act Part III) | {{rule:con.first_session_days}} days | {{rule:con.window_days}} days | A&C Act ss.61–81 [LAW] | The parties with the conciliator |
| Arbitration (documents-only or hearing) | Procedural conference within {{rule:arb.po1_days}} days of constitution | Award within 12 months of completion of pleadings, extendable by 6 months by consent (A&C s.29A) [LAW] | Statutory | The tribunal |
| Expert determination (COM, INS, INT) | {{rule:exp.first_days}} days | {{rule:exp.window_days}} days | Contractual | The expert |

"We publish these windows so you can plan. They are not promises about your matter: the other side, the documents and the law set the real pace, and we will tell you when a statutory clock is running."

**Fees before booking (block).** "Before you book anything you will see: the administrative fee, the neutral's fee for the step you are choosing, any payment-processing fee, and GST — as one total. Nothing is added later. If a step does not go ahead, our refund rules say what comes back and when." → `/fees`, `/fees/refunds`

### 2.2 Mechanism pages (P-21–P-27 delta)

Each mechanism page gains, under the hero, a four-cell **"At a glance"** row: *Who decides* (`WhoDecidesChip`), *Is it confidential*, *Is the outcome enforceable and how* (from `{{rule:*}}`; conciliation s.74; arbitration s.36; mediation settlement — contract, or consent award where the parties convert it), and *Typical window*. Each page ends with "What this process is not" (two bullets; e.g., mediation: "Not a hearing where someone rules against you. Not recorded.").

### 2.3 Hybrid and staged processes — `/mechanisms/hybrid` (P-72, new)

| Field | Copy |
|---|---|
| SEO title | Med-Arb, Arb-Med and Staged Dispute Resolution |
| Meta description | How staged processes work at Equator: negotiate, mediate, then arbitrate if needed, with separate consent, separate neutrals where required, and separate fees. |
| H1 | One dispute, more than one way through |
| Hero one-liner | Start with the lightest step. Move to the next only if you both choose to, with the rules for each step published in advance. |

**Sections.** *Why staged:* most disputes settle when people are given a structured chance to talk; arbitration is there if they do not. *How we keep the steps apart:* a mediator does not become the arbitrator in the same matter unless every party gives informed written consent after the mediation ends and the Rules permit it for that dispute type (master §5.3); caucus information never reaches an arbitrator. *Med-arb and arb-med explained in plain words* (two short paragraphs each, with the "sealed award" concept described as "the arbitrator writes the award first and seals it; you then try mediation; the award is opened only if you do not settle"). *Fees:* each step has its own published fee; moving to the next step is a new booking. *When staged processes are not offered:* matters that cannot be arbitrated (NN-06), POSH matters, family status matters. *FAQ:* F-31, F-32, F-33.

---

### 2.5 Fees page — "Fees before booking" full block (P-38 delta; REC-03)

**H2.** Every fee, before you book.

"Here is how a fee at Equator is built, for any process and any step:

1. **Administrative fee.** Equator's charge for running the step — registration, notices, scheduling, the case manager, the hearing room. Banded by the amount in dispute and the process; the band and the figure render from the published fee schedule version in force on the day you book.
2. **Neutral's fee.** The mediator's, conciliator's, arbitrator's or expert's fee for the step, by band and track (documents-only or hearing). Neutrals are paid the same whether or not your matter settles; there is no outcome-linked component anywhere (X-07).
3. **Payment-processing fee.** If the payment provider charges one for your chosen method, it is shown as its own line. Card and UPI details are entered only on the provider's page; Equator never sees them (NN-31).
4. **GST.** Shown as a line and in the total.

The calculator adds these up and shows one total before you book. What you see is what you pay; nothing is added at checkout, and there are no 'processing', 'convenience' or 'urgent' surcharges that appear later.

**If a step does not go ahead.** Our Fees, Deposits, Cancellation and Refund Policy says, for each step, what is refunded and within how many days — for example when the other side does not accept mediation, when a session is cancelled by the neutral, or when a case is withdrawn before the first procedural conference. → `/fees/refunds`

**Who pays.** In mediation and conciliation the parties usually share fees equally unless they agree otherwise; in arbitration the tribunal may allocate costs in the award under the Rules and A&C s.31A [LAW]. In lender and insurer programmes the organisation pays the administrative fee and the neutral's fee; the individual pays nothing unless the fee schedule for that programme says so, and never a success fee.

**Settlement money.** Sums you agree to pay each other never pass through Equator. They go to a bank escrow with a trustee, or directly between you with proof uploaded (NN-13).

**Foreign currency (INT).** Fees may be quoted in USD, EUR, GBP, SGD or AED; the FX snapshot date is shown and the INR equivalent is stated for GST."

**Calculator fields.** Process · Dispute type · Amount in dispute · Track · Number of parties · Currency → Output: itemised lines, total including GST, the fee schedule version, "as of" date, and a link to the refund rules for that step.

---

## 3. Disputes — six vertical landing pages (P-04–P-09 deltas)

The v3.1 copy for each hub stands. The v3.2 delta applies a common lead pattern to all six, in this order (FR-P13-04 order is mandatory): (1) identity strip; (2) **free forum first** card, naming the forum, cost "Free", how to apply and the last date to act from `{{rule:*}}`; (3) "What Equator can do here" — three to five situations with the mechanism that fits; (4) "What we never do here" (criminal, in-rem, status matters as applicable); (5) fee teaser (tokens only); (6) subtype links; (7) FAQ (three from the bank). Lead copy per vertical:

**Loans, cards and payments (FIN) — `/disputes/loans-and-finance`.** "If a bank or NBFC has not resolved your complaint in 30 days, the RBI Integrated Ombudsman is free [LAW: RB-IOS 2026, X-13]. If you want to settle a loan, restructure, or resolve a dispute with a lender who uses Equator, we run negotiation, conciliation and arbitration on terms that protect you: contact only in permitted hours, no success fee charged to borrowers, and arbitrators the lender cannot pick."

**Business and commercial (COM) — `/disputes/business-and-commercial`.** "Unpaid invoices, broken supply contracts, partner and shareholder fallouts, franchise and licensing disputes. MSMEs can use the free MSEFC route for delayed payments [LAW: MSMED Act ss.15–19] — we tell you when that fits better. For everything else, mediation in weeks, or arbitration with a published fee."

**Family, marriage and family property (FAM) — `/disputes/family-and-property`.** "We mediate the terms of mutual-consent arrangements, maintenance, property and inheritance settlements. We do not decide status: divorce, custody and guardianship are for courts. Property settlements that need stamping and registration get a checklist and a human to walk you through it. Safety first: a quick-exit button sits on every page in this section."

**Insurance (INS) — `/disputes/insurance`.** "Claim rejected or delayed? The Insurance Ombudsman is free for individuals up to the limit in the Rules [LAW: Insurance Ombudsman Rules 2017; cap verified per Appendix G]. Where your insurer uses Equator, or your dispute is between businesses, we offer conciliation and arbitration. There is never a success fee on an insurance claim."

**Workplace and employment (WRK) — `/disputes/workplace`.** "Unpaid wages, full-and-final settlements, workplace conflict, separation terms. Workmen's disputes under the labour codes have statutory forums first. Sexual-harassment complaints go to your employer's Internal Committee under the POSH Act; we provide that committee with tools, never a substitute."

**International commercial (INT) — `/disputes/international-commercial`.** "Cross-border contracts with Indian and foreign parties: mediation and arbitration under Equator's Rules, with neutral-nationality presiding arbitrators where parties differ, sanctions and KYC checks before registration, and fees in INR, USD, EUR, GBP, SGD or AED. Enforcement depends on the seat and the New York Convention — we explain, we do not promise."

---
### 2.4 Process pages — full copy for the four core processes (supersedes the P-21–P-24 body copy where the two differ; P-21–P-24 field rows, routes and Hindi heroes stand)

#### 2.4.1 Mediation — `/mechanisms/mediation`

**H1.** Mediation: you decide, with help.

**Hero one-liner.** A trained, independent mediator helps both sides talk, understand each other's position and build terms you both choose. Nothing is imposed, and nothing is recorded.

**At a glance.** Who decides: you and the other side. Confidential: yes — private sessions, sealed caucus notes, no recording. Outcome: a signed settlement agreement (a contract), which the parties may convert into a consent award where the Rules allow. Typical window: {{rule:med.window_days}} days from appointment, extendable by consent.

**How it works.**
1. **Agreement to mediate.** Both sides accept the mediation agreement (Equator's standard form, versioned). It sets confidentiality, the mediator's role, who attends and how fees are shared.
2. **Appointment.** A mediator is appointed from the panel by the allocation policy — eligibility, conflicts, rotation — with the Independence Evidence Pack on the file.
3. **Preparation.** Each side uploads a short position statement and the documents that matter. Vidhi can help you organise them; the mediator reads them before the first session.
4. **Joint and private sessions.** A joint session sets the agenda; private sessions (caucus) let you speak frankly with the mediator alone. What you say in caucus stays with the mediator unless you say otherwise.
5. **Terms.** When terms emerge the mediator helps you write them plainly. You see the draft, take advice if you wish, and sign only when you are ready. Family matters carry a seven-day reflection window before signing (X-40).
6. **After signing.** The agreement is e-signed and e-stamped where the law requires; property transfers and partitions route to a physical stamping and registration step with a checklist (NN-08). You receive a verifiable copy with a hash.

**What mediation is not.** It is not a hearing where someone rules against you. It is not recorded. The mediator never gives either side legal advice or a view on who would win.

**Statutory note (switches automatically with the flag — X-16).** "The Mediation Act 2023 is partly in force. Sections 27 and 28, which would give a mediated settlement the effect of a court decree and set the enforcement route, have not yet been notified. Until they are, your mediated settlement is a contract, and you may convert it to a consent award where the Rules allow. We will update this page the day that changes." (NN-05)

**Fees.** The administrative fee and the mediator's fee for the first session are shown, with GST, before you book; later sessions are booked and paid the same way. If a session does not go ahead, the refund rules apply. → `/fees`

**Who it suits.** Ongoing relationships (families, business partners, employers and employees), disputes where both sides want a say in the result, matters where speed and privacy matter more than a public ruling.

**FAQ.** F-11, F-12, F-22.

#### 2.4.2 Conciliation — `/mechanisms/conciliation`

**H1.** Conciliation: proposals you can accept, a settlement with the status of an award.

**Hero one-liner.** Under Part III of the Arbitration and Conciliation Act 1996, a conciliator may propose terms. If you both sign, the settlement has the same status and effect as an arbitral award.

**At a glance.** Who decides: you and the other side, with proposals from the conciliator. Confidential: yes (A&C Act s.75) [LAW]. Outcome: a settlement agreement with the status of an arbitral award on agreed terms (s.74) [LAW]. Typical window: {{rule:con.window_days}} days.

**How it works.** Invitation and acceptance (s.62) → appointment from the panel → written statements of the dispute (s.65) → sessions, joint and separate, in which the conciliator may make proposals orally or in writing (s.67(4)) → settlement drafted by the conciliator or the parties (s.73) → signatures, authentication by the conciliator, e-stamping → the proceedings end (s.76).

**How it differs from mediation.** The conciliator can suggest terms; a mediator does not. A conciliated settlement is enforceable as an award; a mediated one is a contract unless converted. Conciliation is governed by a statute in force today; the Mediation Act is only partly notified.

**What conciliation is not.** The conciliator does not decide anything and cannot bind you. There is no finding of fault. The conciliator may not act as arbitrator in the same dispute unless you both agree otherwise (s.80) [LAW].

**Fees and window.** As mediation; the conciliator's fee band is published per step. → `/fees`

**Who it suits.** Lender–borrower settlements, insurer–business disputes, commercial matters where the parties want an enforceable result without a hearing.

**FAQ.** F-12, F-21, F-24.

#### 2.4.3 Arbitration — `/mechanisms/arbitration`

**H1.** Arbitration: an independent decision, under published rules.

**Hero one-liner.** An arbitrator appointed from Equator's panel by rule hears both sides and issues a reasoned award that can be enforced under section 36 of the Arbitration and Conciliation Act 1996 once the challenge period has passed [LAW]. The parties never pick the arbitrator. *(v3.2 review, 26 Oct 2026: reworded — the earlier "enforceable as a court decree" tripped this deck's own never-say rule (§0.2 "court/decree for Equator's own outputs") and omitted the s.34 qualifier.)*

**At a glance.** Who decides: the arbitrator (`WhoDecidesChip`: "The arbitrator decides"). Confidential: yes (A&C Act s.42A) [LAW]; hearings recorded only with everyone's consent. Outcome: an award enforceable under s.36 after the challenge period [LAW]. Typical window: procedural conference within {{rule:arb.po1_days}} days of constitution; award within 12 months of completion of pleadings, extendable by 6 months by consent (s.29A) [LAW].

**How it works.**
1. **Arbitration agreement.** Your contract's clause, or a fresh agreement, refers the dispute to arbitration under the Equator Resolution Rules.
2. **Filing and response.** The claimant files; the respondent replies within the time in the Rules; both see the fee for every step first.
3. **Constitution of the tribunal.** A sole arbitrator (or three, for larger or international matters) is appointed by the allocation policy with conflict checks and disclosures; parties may challenge under the Rules; the Independence Evidence Pack is on the file.
4. **Procedural conference and timetable.** The tribunal fixes pleadings, documents, witness statements and hearing dates; a documents-only track is available for smaller claims.
5. **Hearing.** Online, in Equator's hearing rooms, with captions and interpreters on request; recorded only with the consent of all parties and the tribunal.
6. **Award.** A reasoned, signed award. The Scrutiny Sub-Committee reviews awards for form (never merits) before issue. E-stamped per the state's law. A verifiable copy with a hash.
7. **After the award.** Enforcement under s.36 once the s.34 challenge period passes; execution support packs and a professional chooser if you need help.

**The defensibility point.** "Indian courts have set aside awards where one party controlled who the arbitrator was. At Equator no party, lender, insurer or client chooses or vetoes the arbitrator — ever. That is why we document every appointment." → `/trust/independence-evidence-pack`

**Matters we never arbitrate.** Matrimonial status, custody and guardianship, testamentary questions, criminal matters, insolvency in rem, and any matter the law reserves for a court or tribunal (NN-06). Consumer clauses cannot shut out the Consumer Commission; we say so.

**Emergency and expedited lanes.** An emergency arbitrator for urgent interim relief, and an expedited procedure for claims under the published threshold, each with its own published fee.

**Fees.** Administrative fee by claim band, arbitrator's fee by band and track, hearing-room fee if any, GST — all before you file. Borrowers never pay a success fee; there is no outcome-linked fee in any arbitration (X-07). → `/fees`

**AI in arbitration.** Vidhi may help the tribunal summarise and index the record and check an award's format. It never drafts reasons, findings or the operative part, and never predicts an outcome. The tribunal signs an attestation; the parties are told what AI help was used. → `/rules/ai-governance`

**FAQ.** F-09, F-10, F-23, F-25.

#### 2.4.4 Negotiation (assisted) — `/mechanisms/negotiation`

**H1.** Assisted negotiation: structured, time-boxed, on the record.

**Hero one-liner.** Before anyone is appointed, a structured negotiation space lets both sides exchange offers within a time-box, with a case manager keeping the process fair and the clock visible.

**At a glance.** Who decides: you and the other side. Confidential: yes, within the platform's rules. Outcome: a settlement agreement if you reach one, e-signed and e-stamped; otherwise you choose the next step. Typical window: {{rule:neg.timebox_days}} days (FIN default 21).

**How it works.** The claimant opens a negotiation and states what is sought; the other side accepts or declines within {{rule:neg.first_contact_days}} working days; offers and counter-offers are exchanged in a structured form (amounts, schedules, non-money terms) with every move time-stamped; a case manager watches the clock and the conduct rules but takes no side; Vidhi can turn agreed heads into plain-language draft terms for you to review; if the time-box ends without agreement, you may move to mediation, conciliation or arbitration — each a fresh choice with its own fee.

**Conduct rules that apply.** Contact hours for borrowers (08:00–19:00; 09:00–18:00 for microfinance) are enforced by the platform (NN-12) [LAW: RBI Directions]. No threats, no harassment; a complaint route is one click away. The other side's private parameters are never shown to you.

**What it is not.** Not a hearing, not mediation (no neutral is appointed), not a collections channel.

**Fees.** A single administrative fee for the negotiation window, with GST, shown before you start. → `/fees`

**FAQ.** F-33, F-34.

---

### 3.7 Vertical landing pages — full sections (complements the lead copy in §3)

Each hub follows the FR-P13-04 order; the sections below give the full copy for the three middle blocks ("Situations we handle", "What we never do here", "Free forums first") and the hub FAQ picks.

#### FIN — Loans, cards and payments

*Free forums first.* RBI Integrated Ombudsman (free; after 30 days at the lender or when dissatisfied; within 90 days) [LAW: RB-IOS 2026]; the lender's Internal Ombudsman; Debt Recovery Tribunal for secured-debt recovery matters (signpost only); Lok Adalat for compromise where the lender agrees; consumer commission for deficiency in service.

*Situations we handle.* One-time settlement of a loan or card balance (negotiation, conciliation); restructuring terms; disputes about charges, statements or foreclosure amounts (conciliation, arbitration under the loan agreement); guarantor and co-borrower disputes; recovery-related complaints routed through the lender's grievance programme; cheque-dishonour civil terms (only the money side; the court alone deals with the s.138 case — NN-24).

*What we never do here.* Decide a criminal complaint; contact you outside permitted hours; let the lender choose the arbitrator; charge you a success fee; pull your credit report without the lender's regulated consent artefacts (NN-14).

*Hub FAQ.* F-10, F-20, F-24.

#### COM — Business and commercial

*Free forums first.* MSEFC and the MSME Samadhaan portal for delayed payments to registered MSMEs [LAW: MSMED Act ss.15–19]; the Legal Services Authority for mandatory pre-institution mediation under the Commercial Courts Act s.12A (Equator prepares the Form-1 pack and never claims to satisfy s.12A — M-06); Lok Adalat.

*Situations we handle.* Unpaid invoices and delayed payments; supply, distribution and franchise disputes; partnership and shareholder disputes (not winding up or insolvency in rem — D2-02); construction and services contracts; IP licensing payment disputes (not validity); pre-insolvency settlements between a company and a creditor where both want to avoid the IBC route.

*What we never do here.* Decide insolvency or in-rem matters; hold settlement money; promise that our report satisfies s.12A; publish anything about your case without every party's consent.

*Hub FAQ.* F-21, F-12, F-33.

#### FAM — Family, marriage and family property

*Free forums first.* Family Courts and court-annexed mediation centres; Protection Officers and the DV Act route for safety; Legal Services Authorities for free legal aid; women's helplines (listed with numbers on the page).

*Situations we handle.* Terms of a mutual-consent arrangement (maintenance, residence, assets, child-related practical arrangements the parents agree to present to the court); inheritance and family property settlements, partition terms and buy-outs; elder-care and shared-property arrangements. Property transfers and partitions route to physical stamping and registration (NN-08); an advocate-drafted deed is recommended and a professional chooser is offered.

*What we never do here.* Decide divorce, custody, guardianship or the validity of a will (NN-06); mediate where there is a current safety risk without the safety protocol; record any session; publish any family matter (NN-26).

*Safety.* "A quick-exit button sits on every page in this section and clears your screen. If you are in danger, call 112."

*Hub FAQ.* F-18, F-13, F-11.

#### INS — Insurance

*Free forums first.* Insurance Ombudsman for individuals within the limit in the Rules (Bima Bharosa for complaints to the insurer) [LAW: Insurance Ombudsman Rules 2017 as amended]; consumer commissions; IRDAI's grievance system.

*Situations we handle.* Rejected or delayed health, motor, life and property claims where the insurer uses Equator or both sides agree; quantum disputes between businesses and insurers; broker and intermediary disputes; surveyor-assessment disputes (expert determination where the policy allows).

*What we never do here.* Charge a success fee on an insurance claim (NN-18); let the insurer choose the arbitrator; apply a policy's arbitration clause to shut out the Ombudsman or consumer commission where the law keeps those routes open — we say so (NN-06, Emaar MGF line).

*Hub FAQ.* F-19, F-10, F-25.

#### WRK — Workplace and employment

*Free forums first.* Labour authorities and conciliation officers under the labour codes for workmen; the employer's Internal Committee for sexual-harassment complaints [LAW: POSH Act 2013]; the Payment of Wages authority.

*Situations we handle.* Full-and-final settlements; wage and incentive disputes for non-workman contracts; separation terms and non-compete disputes; workplace conflict mediation between colleagues or teams; grievance programmes for employers (GRM SaaS); POSH Internal Committee tooling (sealed).

*What we never do here.* Arbitrate a workman's dispute that the labour codes reserve (X-18); run a POSH inquiry — the Internal Committee does, on our tooling, with content sealed from analytics, AI and exports (NN-07); conciliate a POSH matter on a monetary basis or without the aggrieved woman's written request.

*Hub FAQ.* F-17, F-22, F-36.

#### INT — International commercial

*Gates before registration.* Sanctions screening (UN, OFAC, EU, UK, MHA lists), KYC and UBO of foreign parties, DPDP s.16 transfer check, FEMA payment-route flag, and the test for "international commercial arbitration" under A&C s.2(1)(f) or international mediation under the Mediation Act s.3 (NN-19).

*Situations we handle.* Cross-border sale and distribution contracts; technology and licensing agreements; joint-venture disputes; shipping and logistics payment disputes; arbitration seated in India or abroad under the Equator Rules; international mediation with a consent-award route (the Singapore Convention is signed, not ratified by India — NN-19, M-04).

*What we never do here.* Promise enforcement in any country — it depends on the seat, the New York Convention and local law; appoint a presiding arbitrator of either party's nationality where parties differ, unless they agree; take a matter that fails the gates above.

*Fees and currency.* INR, USD, EUR, GBP, SGD or AED, with the FX snapshot date shown; expedited procedure under the published threshold with an opt-in highly-expedited lane (X-38).

*Hub FAQ.* F-12, F-14, F-25.

---

### 5.1 Marketplace — fuller copy for the landing hero and three panels (P-49 delta continued)

**H1.** Find a private practice, on your terms.

**Hero one-liner.** Independent mediators, arbitrators, chambers and dispute-resolution services you can engage directly. Separate from Equator's institutional panel; every fee shown before you book.

**Panel 1 — What this is.** "Private practitioners and chambers list their own services here. You choose, you book, you pay the fee shown — the provider's fee, Equator's service fee, processing and GST, as one total. Matters you start here are the provider's matters, run on Equator's tooling."

**Panel 2 — What this is not (locked).** "The Marketplace is separate from Equator's institutional panel. Nothing here affects Equator appointments. Listing, plan or sponsorship never touches eligibility, grading, allocation or conflict checks."

**Panel 3 — How ranking works.** "Results are ordered by the parameters published on this page, in order of significance, with a 'Why am I seeing this?' link on every result. Outcomes and settlement rates are never used. Reviews, where shown, are process-only, verified after a closed engagement, and displayed only at n ≥ 10. Regulated professionals (advocates, CAs, CSs, CMAs) carry no ratings, labels or paid placement."

**Transparency report strip.** "Every quarter: listings by type, verification rejections, delistings by reason, sponsored revenue share (if any), review removals, payout times, fee disputes." → `/resources?type=transparency_report`

---

### 6.1 For organisations — fuller copy (hub P-28 delta continued)

**H1.** Disputes at scale, with independence you can show.

**Hero one-liner.** Lenders, insurers, employers, universities, marketplaces and public bodies use Equator to run many disputes through one defensible process — bulk filing, APIs, grievance redressal and POSH tooling, with neutrals nobody on your side chooses.

**Three reasons (cards).**
- **Defensible by design.** Allocation by rule with an Independence Evidence Pack per matter. No panel of "your" arbitrators; no veto. Speed comes from the engine and the bulk tooling.
- **Compliance you can hand to your auditor.** Vendor Assurance Room with security, privacy, continuity and audit documents on a published cadence; SEBI CSCRF and IRDAI presets for MIIs and insurers; DPDP evidence; evidence-pack export and auditor grants.
- **Honest to your customers.** Contact-hour rules enforced, free forums signposted first, no success fees to borrowers, plain-language notices in Hindi and English. Your customers see the same identity strip we show everyone.

**Products (list with one line each).** Enterprise API and bulk intake · Grievance Redressal SaaS (four variants) · POSH Internal Committee SaaS (sealed) · Model clause generator and clause seal · Consoles and MIS (aggregates only; no neutral win-rates) · Vendor Assurance Room.

**Pricing.** "Plans are published with GST shown; above {{plan:contact_sales_threshold}} matters a month we will quote. Nothing you pay affects who is appointed." → `/pricing/organisations`

**Request a demo.** Volume band, dispute types, systems to integrate, consent. "We reply within {{rule:sales.reply_days}} working days."

---
## 4. Neutrals — `/neutrals/*` (P-35, P-36, P-54 deltas; new P-62, P-63)

### 4.1 Find a neutral — `/neutrals` (delta to P-35)

The directory is public, needs no login and is server-rendered (REC-02). *(v3.2 review, 26 Oct 2026)* Profiles of advocate-neutrals carry only the particulars an advocate may publish under Bar Council of India Rules, Part VI, Chapter II, Rule 36 [LAW] — name, enrolment particulars, qualifications, areas and languages of practice, panel grade and availability — with no ratings, testimonials, fee advertising or "contact for legal advice" prompts; the directory is an institutional panel listing, not a solicitation channel (X-62; Appendix P §1.4). Add under the hero: "Every profile here is a member of Equator's institutional panel. Order is randomised on each visit. There are no paid positions, no featured labels and no outcome statistics (NN-28). If you are looking for a private practice to engage directly, that is a different surface: the Private Practice Marketplace, which never affects Equator appointments." Profile fields shown: name, tier label (Distinguished / Principal / Associate Neutral — X-26), panels, languages, dispute types, empanelment date, training and endorsements, disclosures summary; no fee negotiation on the page (IPB-04 EQ note).

### 4.2 How neutrals are graded — `/neutrals/how-we-grade` (P-62, new)

| Field | Copy |
|---|---|
| SEO title | How Equator Grades and Appoints Neutrals |
| Meta description | Grades A, B and C, the Qualifying Assessment Programme, the Quality Index built from process measures only, and how appointments are allocated by rule. |
| H1 | How neutrals are graded and appointed |
| Hero one-liner | Grades follow a published policy. Appointments follow published rules. Neither can be bought. |

**Sections.**
- *Three eligibility tiers.* Grade A (public label Distinguished Neutral), Grade B (Principal Neutral) and Grade C (Associate Neutral) are eligibility tiers under `grading_policy.v2` (Appendix N; X-26). Each tier states the verified experience, training, assessment and conduct record required. "Senior" is not used as a label (Advocates Act s.16 designation) [LAW].
- *The Qualifying Assessment Programme (EQAP).* Every panel member passes an assessment of process skill: role-plays, written exercises and an ethics module, marked by an assessor panel against a 0–100 rubric. The rubric score is a pass gate and an input to quality review, not the grade itself. Fees for EQAP are identical for every candidate whatever their training provider (X-29, REC-17).
- *The Quality Index.* Built only from process measures: timeliness of procedural steps, completeness of disclosures, compliance with the Code of Conduct, feedback on process (not outcome) from both sides at n ≥ 5. Settlement rates, who won, enterprise preference and training purchases never enter it (NN-28).
- *How appointments are made.* Eligibility filters (dispute type, language, panel, grade band for the claim size), conflict checks, rotation, concentration caps (no neutral may take more than the published share of one counterparty's matters) and a capped Quality Index weighting. The formula is published at `/rules/allocation-policy`. No party, lender or enterprise client chooses or vetoes a neutral (NN-03).
- *Challenge and complaint.* Any party may challenge an appointment under the Rules; a Challenge Sub-Committee decides. Complaints about conduct go to the Ethics & Complaints Sub-Committee; outcomes are published in aggregate in the transparency report.
- *What this page is not.* "It is not a ranking of neutrals. We do not publish individual performance figures."

**FAQ.** F-40, F-41, F-42.

### 4.3 Independence Evidence Pack — `/trust/independence-evidence-pack` (P-63, new)

| Field | Copy |
|---|---|
| SEO title | The Independence Evidence Pack \| Equator Resolution |
| Meta description | Every Equator appointment ships a dated record of how the neutral was chosen: rules version, filters, rotation state, conflict checks and disclosures. |
| H1 | Evidence of independence, for every appointment |
| Hero one-liner | An appointment you can defend is one you can show. Each Equator matter carries a pack that explains exactly how its neutral was chosen. |

**Sections.** *Why this exists:* Indian courts have set aside awards where one side controlled the appointment (CORE, 2024; Bhadra International, 2026) [LAW — Appendix G LR-ARB rows]; organisations need speed without taking that risk (REC-08). *What is in the pack:* the Rules and allocation-policy versions pinned at filing; the eligibility filters applied; the rotation position; the concentration-cap check; the conflict-check result against both parties, counsel and related entities; the neutral's disclosure statement; the timestamps and hashes of each step; the Institutional Committee confirmation where the Rules require one. *Who can see it:* every party and the tribunal, from the case file, at any time; a court or regulator on request through the party. *What it does not contain:* nothing about the merits; nothing about any other case. *For organisations:* "If you bring us many disputes, the pack is the same for each. You get the speed of a structured process without ever touching the choice of neutral."

---

## 5. Marketplace — `/marketplace` (P-49 delta)

The P-49 copy stands. v3.2 adds the Jupitice-review safeguards as visible copy: a fixed panel note "The Marketplace is separate from Equator's institutional panel. Nothing here affects Equator appointments." (L; NN-34); "How ranking works" link in every result list (REC-04); "Every fee you will pay — the provider's fee, Equator's service fee, processing and GST — is shown before you book" (REC-03); sponsored slots, when the flag is ever ON, labelled "Sponsored — paid placement. Does not affect Equator appointments." and capped at two per page and 20% of results; quarterly Marketplace Transparency Report linked from the page header (REC-13). Advocates, CAs, CSs and CMAs are never offered placement, featured labels or ratings (X-62).

---

## 6. For organisations — `/for/*` (P-28–P-33 deltas)

The P-28–P-33 copy stands. v3.2 deltas:

- **Hub (`/for`).** Add a "Defensibility first" block: "Speed comes from our allocation engine and bulk tooling, never from letting you pick the neutral. Each matter carries an Independence Evidence Pack." → `/trust/independence-evidence-pack`. Add a "Vendor documents for your compliance team" block: "Enterprise and institution clients get a Vendor Assurance Room inside their settings: our security, privacy, business-continuity and audit documents, with cadenced updates and auditor access." → `/trust#vendor-assurance`.
- **GRM SaaS (`/grievance-redressal`).** Add the regulator-clock table with tokens for RB-IOS 2026 (30 days at the RE; Ombudsman within 90 days), IRDAI grievance TATs, Consumer Protection (E-Commerce) Rules r.4 (48-hour acknowledgement, one-month redress) [LAW; rule tokens]; add "Vidhi drafts, your officer sends" — AI drafts a reply with the regulatory checklist; a human always sends.
- **POSH IC SaaS (`/posh-internal-committee`).** Keep the sealed-data statement first: "Complaint content never leaves the sealed workspace: not to analytics, not to AI, not to exports." (NN-07). Add the IC composition rule (at least one-half women; external member) with the statutory citation token.
- **Enterprise API (`/for/developers`).** Point to the Documentation hub (P-64).

---

## 7. Chambers — `/private-adr-chambers` (P-34 delta)

The P-34 copy stands. Add a plain line on independence: "A Private ADR Chambers workspace is your practice, under your name and domain, on Equator's tooling. Matters you bring in yourself are yours. Equator panel appointments are made by Equator's rules and never by your listing or your plan." Add the HR add-on caveat "subject to availability" and the portability promise: "Leave with everything: your matters, documents, templates and records as Word, Excel and PDF folders with a manifest, free, at any time." (NN-37)

---

## 8. Training and the Institute — `/training` (P-37 delta)

The P-37 copy stands. v3.2 adds the arm's-length block that must appear above any link to the Equator ADR Institute: "Training is separate from Equator's panel. Completing any course — ours or anyone else's — gives no advantage in empanelment, grade, allocation or the EQAP fee. The programme catalogue shows at least three recognised providers." The Institute card renders only when `academy.institute_referral` is ON (D2-17, D3-38) and then shows the operating entity name from its token and "opens equatoradr.com — leaving this site". Corrections C1–C20 (Appendix AF §AF.4.3) must be complete on the Institute site before the flag is turned on.

---

## 9. About — `/about` (P-55, full rewrite of P-44 About)

| Field | Copy |
|---|---|
| SEO title | About Equator Resolution |
| Meta description | An independent dispute resolution institution for India, operated by Equator Resolution Service Private Limited, part of the Infrabyx Group. Our mission, story and what we never do. |
| H1 | An institution built so that resolving a dispute does not take years |
| Hero one-liner | We bring mediation, conciliation and arbitration to the places disputes begin — loan agreements, policies, contracts, workplaces, families — and run them online under published rules. |
| Hindi hero | लोगों को केंद्र में रखकर विवाद समाधान। |
| Schema | `AboutPage` + `Organization` |

**Mission.** "To make a fair, independent and affordable route to resolution available to anyone in India with a dispute — in their language, on their phone, with the rules in front of them."

**What we are.** "Equator Resolution is a private dispute resolution institution. We administer mediation, conciliation, arbitration, negotiation support and expert determination under the Equator Resolution Rules. Our neutrals are independent professionals empanelled through a published process. We are operated by {{entity.legal_name}} (CIN {{entity.cin}}), registered office {{entity.registered_office}}. Equator is part of the Infrabyx Group." (`id.group`)

**What we are not.** "We are not a court, tribunal, regulator or government body. We do not give legal advice. We do not decide criminal matters, insolvency, matrimonial status, custody or testamentary questions. We will tell you when a free public forum — an ombudsman, a consumer commission, a Lok Adalat, a labour authority — is the better route for you, and we record that we did."

**Our story (timeline; dates from `{{milestone:*}}` tokens — every entry sourced).**

| Date | Milestone |
|---|---|
| {{milestone:incorporation}} | {{entity.legal_name}} incorporated [VERIFY — CIN record] |
| {{milestone:rules_v1}} | Equator Resolution Rules ERR-2026.1 approved by the Board on the Rules Sub-Committee's recommendation |
| {{milestone:panel_first}} | First panel of neutrals empanelled after EQAP assessment |
| {{milestone:platform_live}} | Online platform opened for filing and response |
| {{milestone:first_report}} | First transparency report published with method notes |

Empty state when a milestone token is unset: the row is omitted, never shown with a placeholder date.

**Values (five, each one sentence).**
- **Independence.** Nobody who pays us chooses who decides.
- **Candour.** We say what we are not, and when someone else can help you for free.
- **Proportion.** The lightest process that can work comes first.
- **Access.** Hindi and English from day one; more languages by configuration; captions, interpreters and plain-language help.
- **Evidence.** Numbers come with dates and methods or they do not appear.

**The Equator Standard (three proofs with links).** Impartial → `/trust/how-we-stay-neutral` · Expert → `/neutrals/how-we-grade` · Efficient → `/trust/outcomes` (published time standards; metrics when available).

**Leadership teaser.** Three cards from `team_member` (`group=leadership`) with role and one line; "Meet the team" → `/leadership`. Empty state: "Leadership profiles are being prepared." (never a loading spinner).

**Group context.** "Equator works alongside other Infrabyx Group products — LawDocs (documents and e-signing), LawDocsComply (regulatory compliance), Finbyx and Udofin (lending software) — through controlled, consented interfaces. Case and appointment data are never shared with group lenders' software (NN-38)."

**Offices and contact.** Delhi · Noida · Jaipur (addresses from `office` records) → `/contact`.

**FAQ.** F-01, F-03, F-04.

---

## 10. Governance — `/about/governance` (P-56, full rewrite of P-44 Governance)

| Field | Copy |
|---|---|
| SEO title | Governance: Board, Institutional Committee and Rules |
| Meta description | How Equator is governed: a company board that takes no case decisions, an Institutional Committee with a majority of external members, versioned rules and a transparency report. |
| H1 | How Equator is governed |
| Hero one-liner | Decisions about cases are kept apart from the company's commercial side, by structure, not by promise. |

**Section — Two bodies, one wall.** "The **Board** of {{entity.legal_name}} runs the company: strategy, finance, people, technology, risk. The **Institutional Committee** runs the institution's case functions: appointments, challenges, scrutiny of awards for form, ethics and complaints, rules, AI oversight and transparency. A majority of Committee members are external to the company. The Board cannot direct the Committee on any case."

**Section — The Board (team_grid `group=board`).** Name, role, DIN (optional), one-line bio; independent directors marked. Empty state: "Board composition will be published after the Company Secretary's confirmation." [OWNER]

**Section — Institutional Committee and sub-committees (table).**

| Sub-committee | What it decides | Who sits |
|---|---|---|
| Appointments | Confirms appointments and nominations under the allocation policy | External majority; Registrar in attendance |
| Challenge | Decides challenges to neutrals | External members only |
| Scrutiny | Reviews awards for form before issue (never merits) | Senior panel members not involved in the matter |
| Ethics & Complaints | Conduct complaints against neutrals; sanctions ladder | External chair |
| Rules | Proposes rule changes; publishes drafts for comment | Mixed |
| AI Oversight | Approves AI uses, reviews evaluations, holds the kill switch | Includes the DPO and an external technologist |
| Transparency | Approves publications and statistics; signs the transparency report | External chair |

**Section — Rules, versioned.** "Every rule, code and policy we apply is published with a version and effective date. A case is pinned to the versions in force when it was filed; later changes never reach it. Drafts of rule changes are posted for public comment for at least {{rule:rules.comment_days}} days." → `/rules`

**Section — Policies adopted (list; each links to the published page or states "adopted — available on request").** Code of Conduct for Neutrals; Code of Conduct for Case Managers and Staff; Allocation Policy; Publication Policy; AI Governance Rule; AI Use & Transparency Policy; Information Security Statement; Privacy Notice; Grievance Redressal Policy; Whistle-blower Policy [OWNER: confirm adoption]; Related-Party Transactions Policy [OWNER]; POSH Policy (internal). "Where a policy is not yet adopted we say so rather than omit it."

**Section — Transparency report.** "Each quarter the Transparency Sub-Committee publishes process statistics (never outcome statistics), complaints handled, rules changed and AI evaluations summarised, with the method for every number and small-number suppression (n ≥ 10)." → `/resources?type=transparency_report`

**Section — Auditor and officers.** Statutory auditor {{entity.auditor}} [VERIFY]; Grievance Officer {{gro.name}}; Data Protection Officer {{dpo.name}}; Company Secretary {{entity.cs_name}}.

**FAQ.** F-06, F-07.

---

## 11. Advisory Council — `/about/advisory-council` (P-57, new)

| Field | Copy |
|---|---|
| SEO title | Advisory Council \| Equator Resolution |
| Meta description | Who advises Equator, what the Council does and — just as important — what it does not do: it has no role in appointing neutrals or deciding cases. |
| H1 | Advisory Council |
| Hero one-liner | Experienced voices who advise on rules, standards and access. The Council appoints nobody and decides no case. |

**Sections.** *Role:* "The Council advises the Board and the Institutional Committee on rules, training standards, access to justice and public interest. It meets {{rule:council.meeting_frequency}} times a year. Its advice is published in summary." *What it does not do (REC-18, locked text):* "The Council has no role in appointing, grading or removing neutrals, and no role in any case." *Members (team_grid `group=advisory`):* name, former role, one-line bio, term dates, declaration of interests on file. Empty state: "The Council is being constituted. Members, terms and the charter will appear here." *Charter* → `/about/governance/charter`.

**FAQ.** F-08.

---

## 12. Team — `/team` (P-58, new; placeholders)

| Field | Copy |
|---|---|
| SEO title | Our Team \| Equator Resolution |
| Meta description | The people who run Equator's case services, panel relations, technology and operations. Roles and responsibilities, with photos only where consent is recorded. |
| H1 | The team behind the institution |
| Hero one-liner | Case managers, registry staff, engineers and panel-relations colleagues — the people a party or neutral actually deals with. |

**Grid (`team_member`, `group=team`).** Cards show name, role, team, languages spoken, one line. Photos render only with `photo_consent = true` (IPB-04-69); otherwise an initials tile. Names and roles are text, never only in images.

**Role descriptions (placeholders; owner fills names).**

| Placeholder | Role description |
|---|---|
| {{person:registrar}} — Registrar | Heads case services; custodian of the Rules in operation; supports the Institutional Committee; owns scrutiny of awards for form. |
| {{person:head_institution}} — Head of Institution | Panel strategy, grading policy, EQAP, Code of Conduct, relations with neutrals and training providers. |
| {{person:case_services_lead}} — Case Services Lead | Runs the case-manager team; owns deadlines, scheduling and service standards for parties. |
| {{person:panel_relations}} — Panel Relations Manager | Empanelment, disclosures, availability, complaints intake. |
| {{person:cto}} — Chief Technology Officer | Platform, security, data residency, AI governance engineering. |
| {{person:dpo}} — Data Protection Officer | Privacy programme, data-principal rights, breach handling; statutory contact. |
| {{person:grievance_officer}} — Grievance Officer | Complaints about Equator's service; statutory contact; level-2 review by the Company Secretary. |
| {{person:cs}} — Company Secretary | Governance, Board and Committee secretariat, statutory compliance, Investor relations contact. |
| {{person:cfo}} — Finance Lead | Fees, refunds, payouts, escrow oversight, maker-checker controls. |
| {{person:ops_director}} — Operations Director | Onboarding, customer success, support and the Operations Platform. |
| {{person:marketing}} — Marketing and Communications | Public content under the Claims Register; press contact. |
| {{person:case_managers}} — Case Managers (n) | Named team members by vertical, with languages. |

"Open roles are listed on Careers." → `/careers`

---

## 13. Leadership — `/leadership` (P-59, new; placeholders)

| Field | Copy |
|---|---|
| SEO title | Leadership \| Equator Resolution |
| Meta description | Equator's leadership, board and advisory council, with verifiable bios and declared interests. |
| H1 | Leadership |
| Hero one-liner | Accountable people, verifiable bios. |

**Tier 1 — Executive leadership (team_grid `group=leadership`).** Portrait (consented), name, title, bio of ≤ 120 words with verifiable facts (enrolment, qualifications, past roles), LinkedIn link, declaration-of-interests note "on file". Placeholders: {{person:ceo}} — Chief Executive; {{person:registrar}} — Registrar; {{person:head_institution}} — Head of Institution; {{person:cto}} — CTO; {{person:cs}} — Company Secretary.

**Tier 2 — Board (`group=board`).** As on Governance; DIN optional.

**Tier 3 — Advisory Council (`group=advisory`).** As on the Advisory Council page, with the "appoints nobody" line repeated.

Rule: no empty or client-rendered "advisory board" block (Appendix AF W10; IPB-04 §04.3.7). An empty group renders "Being constituted — see Governance."

---

## 14. Investors — `/investors` (P-60, new; toggle `web.investors.enabled`, default OFF) [COUNSEL]

> **Publication rule.** This page exists in the CMS from day one and is hidden by setting. Turning it on requires the locked disclaimer block, legal review before every publish, E2+ evidence for every number, and the Board's decision on which documents are gated (README §4 item 22; IPB-04-66). The words "guarantee", "assured", "will achieve", "projected", "returns" trigger `IPB-CMS-012`. Wording below is drafted to be informational only and not an offer or invitation to subscribe for securities; counsel must confirm against Companies Act 2013 s.42 and the Companies (Prospectus and Allotment of Securities) Rules 2014 r.14, and SEBI norms on public solicitation [COUNSEL].

| Field | Copy |
|---|---|
| SEO title | Investor Information \| Equator Resolution |
| Meta description | Information for existing and prospective institutional investors in Equator Resolution Service Private Limited: vision, market context, governance, leadership and milestones. Not an offer. |
| H1 | Investor information |
| Hero one-liner | What Equator is building, why dispute resolution in India needs an institution of this kind, and how the company is governed. This page is informational and is not an offer of securities. |
| Robots | `noindex` until the Board decides otherwise [OWNER] |

**Disclaimer block (locked; top and bottom of page; IPB-05 Annex wording to be confirmed by counsel).** "This page is provided for information only to persons who have asked for it or who are existing shareholders. It is not a prospectus, offer document, private placement offer letter, invitation or solicitation to subscribe for or purchase any securities of {{entity.legal_name}} or any Infrabyx Group company, in India or elsewhere. Any issue of securities would be made only to identified persons under Section 42 of the Companies Act 2013 and the rules made under it, by a private placement offer letter and application form, and never through this website. Statements about plans, markets or future activity are our current intentions and expectations; they are not promises or forecasts and may change. Past activity is not an indicator of future results. Nothing here is investment, legal or tax advice." [COUNSEL]

**Section — Vision.** "Most disputes in India are small, personal and slow. The people in them cannot afford years in court and should not have to. Equator is building the institution that sits where disputes begin — in loan agreements, policies, contracts and workplaces — and resolves them online, under published rules, with independent neutrals and fees known in advance. Our aim is to be the institution that lenders, insurers, employers and ordinary people trust because its independence can be shown, not just claimed."

**Section — Market context (every figure E2 with a dated source; shown only when the Claims Register entry is active).**

| Fact | Figure | Source and as-of |
|---|---|---|
| Pending cases in Indian courts | {{claim:njdg_pending}} | National Judicial Data Grid, {{claim:njdg_pending.as_of}} [VERIFY] |
| Share of pending cases older than one year | {{claim:njdg_pending_1y}} | NJDG [VERIFY] |
| Mediation Act 2023 status | Partially notified; Mediation Council of India established 27 Aug 2026 (S.O. 4781(E)); regulations pending | Gazette notifications (NN-05) |
| RBI expectation of ODR for lender grievances | {{claim:rbi_odr_reference}} | RBI circular reference [VERIFY] |
| SEBI SMART ODR | Operational for securities-market disputes since 2023; 2.0 consultation {{claim:sebi_smart_odr_consultation}} [VERIFY] | SEBI |

"We do not publish market-size estimates. Where a third party has published one, we will cite it with its method."

**Section — Products and revenue streams.** "Equator earns from administrative fees on cases, from subscriptions to its organisation products (Grievance Redressal, POSH Internal Committee, Enterprise API), from Private ADR Chambers subscriptions, from training delivered at arm's length, and from the Private Practice Marketplace service fee. Every stream is listed in a Revenue Stream Registry with a kill switch and a neutrality rating; streams that could influence appointments are prohibited (NN-16, NN-34). We never take a success fee from an individual borrower or on an insurance claim." → `/trust/how-we-earn`

**Section — Governance.** Summary of `/about/governance` with the Board, the Institutional Committee wall, maker-checker on money and authority (NN-36), and the policies list. Statutory auditor {{entity.auditor}} [VERIFY].

**Section — Leadership.** Cards from `group=leadership` as on `/leadership`.

**Section — Milestones.** The About timeline plus funding events, if any, each dated and sourced: "{{milestone:funding_round}} — {{claim:funding_round_text}}" [VERIFY; publish only with the investor's written consent].

**Section — Documents (gated).** "Existing shareholders and persons the Board has identified may request access to: audited financial statements; the Information Memorandum (if any); the shareholders' agreement summary; the Vendor Assurance Room (security and compliance documents). Access is granted by login after verification, backed by the same room our enterprise clients use (IPB-08), and logged." Gating levels: `login` with NDA flag. Never an email-gate for financial documents [COUNSEL].

**Section — Investor relations contact.** "{{person:cs}}, Company Secretary — {{entity.ir_email}} (direct). We do not operate an investor mailing list. We respond within {{rule:ir.response_days}} working days."

**Section — FAQ.** "Can I invest in Equator through this website?" — No. Equator does not offer securities to the public or through its website. Any issue of securities would be made privately to identified persons under the Companies Act 2013 [COUNSEL]. "Are there plans to list?" — We do not comment on plans of that kind. "Who are the existing investors?" — {{claim:investors_text}} with each investor's consent [VERIFY], otherwise "Not disclosed."

**Footer repeat of the disclaimer block.**

---

## 15. Careers — `/careers` (P-61, full rewrite of P-47)

| Field | Copy |
|---|---|
| SEO title | Careers at Equator Resolution |
| Meta description | Open roles in case services, panel relations, engineering, operations and legal at Equator Resolution. Delhi, Noida, Jaipur and remote. Equal-opportunity employer. |
| H1 | Work on the hardest problem in Indian civil justice |
| Hero one-liner | We are building an institution, not just a product. If you care about fairness, plain language and systems that can be audited, we would like to hear from you. |

**Culture (four short paragraphs, facts only).** *Independence is a job:* case-services staff follow the Code of Conduct for Case Managers and Staff and may never influence an appointment. *Transparent measurement:* we measure outcomes and quality, not keystrokes; there is no covert monitoring (NN-35), and you see your own data. *Remote and office:* case managers may work from home; offices in Delhi, Noida and Jaipur. *Maker-checker everywhere:* nobody can move money or authority alone (NN-36) — it protects you as much as the company.

**Open roles (list from `job` items; filters department / location / type).** Each role: title, department, location, type, "apply by" date, link. Closed roles return 410 with a link to open roles; `JobPosting` JSON-LD with `validThrough`. Empty state: "No open roles today. Leave your details below and we will write when something fits."

**Benefits (facts from `{{hr:*}}` tokens only).** Leave policy per the Code on Wages and state rules; health insurance {{hr:health_cover}} [VERIFY]; learning budget {{hr:learning_budget}} [VERIFY]; work email and equipment; parental leave per statute and policy.

**Internships.** "Stipend and certificate terms per the policy the Board adopts [OWNER: IPB open item 7]."

**Application form → Operations Hub HR (`HR` port).** Fields: name, email, phone (optional), role, CV upload (PDF/DOCX ≤ 5 MB, scanned), LinkedIn (optional), consent text: "We will use your details to consider you for roles at Equator Resolution and, with your consent, keep them for {{rule:hr.candidate_retention_months}} months. Privacy Notice." Equal-opportunity statement: "We hire without regard to gender, caste, religion, disability, age or marital status. Tell us about any accommodation you need for an interview."

---
## 16. Documentation hub — `/docs` (P-64, new)

| Field | Copy |
|---|---|
| SEO title | Documentation: Rules, Forms, Fees, API and Data Protection |
| Meta description | Everything written down: the Equator Resolution Rules and codes, forms library, fee schedules, decisions library, developer portal and data-protection documents, all versioned. |
| H1 | Documentation |
| Hero one-liner | An institution is its documents. Here they all are, versioned and dated. |

**Six tiles, each with a one-line description and a "versioned by year" badge where applicable.**

1. **Rules & Codes library** → `/rules`. "The Equator Resolution Rules (ERR), Code of Conduct for Neutrals (ECC), staff code (ESC), Allocation Policy, Publication Policy and AI Governance Rule. Pick a version, read the diff, download a hash-stamped PDF."
2. **Forms library** → `/docs/forms`. "Every form we use, by process and dispute type: notice of dispute, response, mediation agreement, arbitration agreement and terms of reference, letter of authority, settlement checklist, Form-1 pack for pre-institution mediation [LAW: PIMS Rules 2018; Legal Services Authority route until the M-06 gates close]. Fillable PDFs and DOCX; the platform pre-fills most of them for you."
3. **Fee schedules** → `/fees`. "Administrative fees, neutral fee bands, enterprise and chambers plans, refund rules, by version. Figures render from the fee engine; nothing here is typed."
4. **Decisions library** → `/decisions`. "Published awards and settlements — only with every party's consent and after redaction (NN-26). Citation format `EQR/<YYYY>/AWD/<NNNN>`. Searchable; never a win-rate."
5. **Developer portal and API** → `{{web.docs.url}}`. "REST `/v1` (OpenAPI 3.1), webhooks (Standard Webhooks signatures), sandbox keys, SDKs, changelog, status page. Case events for your systems; hearing recordings only through time-boxed, masked URLs."
6. **Data-protection documents** → `/trust`. "Privacy Notice, Cookie Notice, Data Processing Addendum, sub-processor list, retention schedule, transfer register summary, DPIA summaries where published."

**Also on this page:** "How a case proceeds" (link to `/how-it-works`), glossary (`/glossary`), help centre (`/help`), accessibility documents (GIGW/STQC artefacts for court-facing deployments, from the Vendor Assurance Room when published).

### 16.1 Forms library — `/docs/forms` (sub-page)

Table columns: Form · Process · Dispute types · Version · Effective · Download (PDF, DOCX) · "Pre-filled in the platform?" Each form row shows its legal basis token where one exists. Note under the table: "Forms are templates. Filling one does not start a case; filing on the platform does."

---

## 17. Press and media kit — `/press` (P-65, full rewrite of P-51)

| Field | Copy |
|---|---|
| SEO title | Press and Media \| Equator Resolution |
| Meta description | Press releases, coverage, media kit and a named spokesperson. Facts about Equator appear only with a dated source. We do not comment on individual cases. |
| H1 | Press |
| Hero one-liner | Dated releases, named contact, approved facts. We do not comment on individual cases. |

**Sections.** *Releases:* list of `press_item kind=release`, each dated, with Claims Register links for every figure. *Coverage:* dated items with outlet name and a link to the article itself (never an outlet homepage); no undated "coverage walls" (Appendix AF W-pattern). *Media kit (downloads from the brand pack):* logo SVG and PNG on light and dark, colour tokens (teal `#0E6E6E`, coral `#F26B5B`), typeface note (Manrope), boilerplate BP-01 (Appendix Y §Y.5.4), leadership photos with recorded consent, product screenshots (seeded demo data only), usage rules ("do not alter the mark; do not imply endorsement"). *Spokesperson:* {{person:spokesperson}}, {{entity.press_email}}, response within one working day. *Facts you may use (claims-register extract):* legal name, CIN, offices, founding date, number of published rules versions, panel size band (n ≥ 10 cells), languages supported. *What we will not do:* comment on a case, name a party, publish a success rate.

---

## 18. Partners — `/partners` (P-66, new)

| Field | Copy |
|---|---|
| SEO title | Partners: Institutions, Universities and Bar Associations |
| Meta description | How Equator works with institutions, universities, bar associations, training providers and technology partners — and the lines we do not cross. |
| H1 | Partners |
| Hero one-liner | Partnerships that widen access without touching independence. |

**Partner types (five cards).**
- **Institutions and ODR bodies.** Mutual referral of matters outside our scope; shared training standards; joint research. No exclusivity.
- **Universities and law schools.** Campus mediation cells, clinics, competitions and internships on Equator's platform at no charge to students (P10); faculty on the Advisory Council by invitation.
- **Bar associations and professional bodies.** Information sessions, model-clause adoption, EQAP access for members at the identical fee. No referral fees to advocates, CAs, CSs or CMAs, ever (X-62).
- **Technology partners.** Identity, e-sign, payments, video and AI providers behind ports with Indian data residency; listed in the sub-processor list.
- **Relationship partners (lenders, insurers, marketplaces).** Disclosed on every matter to the other side (NN-16); "priority" means administrative speed only, never neutral selection.

**Logo wall.** Only with each partner's written permission (`claims_ref`). Empty state: "Partner logos appear here with each partner's permission."

**Become a partner (form → CRM).** Organisation, type, contact, purpose, consent. "We reply within {{rule:partners.reply_days}} working days."

**What a partnership never includes.** "A say in who is appointed. Access to case data. A ranking or label on the neutrals directory. A fee for referring a dispute."

---

## 19. Trust and security — `/trust` (P-43 delta)

The P-43 copy stands. v3.2 adds:

- **Certifications block from the Vendor Assurance Room** (`TRUST` port; IPB-04-68): each certification actually held shows name, issuer, scope, certificate ID or "available on request", valid until. Empty state (locked copy): "Certification readiness: Equator runs ISO/IEC 27001 and 27701, SOC 2 and PCI DSS SAQ A readiness programmes. We will list each certificate here only when it is issued, with its scope." (NN-17, NN-31)
- **Vendor Assurance Room entry.** "Enterprise and institution clients: your security, privacy and audit documents are in Settings › Security & trust › Vendor documents, with cadenced updates, an evidence pack export and auditor grants." Login link.
- **Sub-processor list** with change-notice subscription; **VAPT summary** (date, scope, severity counts, remediation status — never the raw report); **data residency statement** ("Case data is stored and processed in India; AI inference for case content runs on India-resident, zero-retention endpoints"); **status page** link; **security.txt** and responsible disclosure link; **DPA request** form.
- **AI transparency** → `/rules/ai-governance`: "Vidhi, our AI assistant, never decides, advises, predicts or values. Here is the list of things it is locked out of."

---

## 20. Help — `/help` (P-46 delta)

The P-46 copy stands. v3.2 adds three strips: **Tutorials** ("Short videos with captions and transcripts, regenerated every release so the screens match what you see") → `/tutorials`; **Learning paths** ("Party: your first case · Neutral: your first appointment · Organisation admin: first 30 days"); **Ask Vidhi** ("Answers only from our help content and public rules, labelled AI-generated, with links. Vidhi cannot see your case here and does not give legal advice."). Also: keyboard shortcuts page, glossary link, "Report a problem" (feedback widget), and the idea board link when enabled ("Suggest an improvement and vote on others").

---

## 21. Pricing — `/fees`, `/pricing/*` (P-38, P-39 deltas; Pricing Studio copy layer)

Copy lives in the Pricing Studio; **figures never do** — they render from the fee engine and plan catalogue (Appendix B, Appendix O; IPB-04 §04.3.3). Copy layer:

- **Intro line (fees for parties).** "Every fee you pay is shown here before you book: administrative fee, neutral fee for the step you choose, payment-processing fee if any, and GST. Nothing is added at checkout."
- **GST label rule.** Consumer prices show "incl. GST"; organisation plans show "+ 18% GST" with the total payable before checkout (IPB-04-35).
- **Plan taglines (organisations).** Starter — "For a first programme: one dispute type, bulk filing, standard reports." Growth — "For several programmes with APIs and SSO." Institution — "For regulated clients: dedicated case team, Vendor Assurance Room, audit grants." (names and entitlements from the catalogue; the Studio maps bullets to feature keys so a removed feature cannot stay on the page).
- **Plan taglines (professionals, Chambers).** Lite/Solo — "Your practice page and matters, one seat." Pro — "Team seats, templates, invoicing." Institution — "Multiple practices, verified domain, HR add-on where available."
- **Trial text.** "14 days, no card, no automatic conversion. We email you before it ends; if you do nothing, it ends." (UDF never-auto-convert pattern; NN-29)
- **Refunds and cancellation.** One line linking to `/fees/refunds`: "Cancelling takes no more steps than signing up."
- **"Talk to sales" threshold.** Above {{plan:contact_sales_threshold}} seats or matters per month the CTA becomes "Talk to us".
- **What is never on this page.** Countdown timers, "only N left", pre-ticked add-ons, prices for sponsored placement (lives on the Marketplace rate card only when the flag is ON).

---

## 22. Resources library — `/resources` (P-67, new)

| Field | Copy |
|---|---|
| SEO title | Resources: Reports, Transparency Reports, Briefs and Presentations |
| Meta description | Equator's transparency reports, research briefs, presentations, templates and checklists — versioned, dated, cite-able. |
| H1 | Resources |
| Hero one-liner | Reports, briefs and templates you can cite, each with a version, a date and an author. |

**Filters.** Type (transparency report · report · brief · presentation · template · checklist · webinar · policy sample · rules and fees · other) · Topic · Dispute type · Language · Year · Access (public / email / login / plan — shown on the card before click).

**Card anatomy.** Title · type badge · abstract (≤ 40 words) · authors · published date · version · pages or duration · language · access badge · "Cite as" (APA-style auto string with version) · download or open.

**Featured collections.**
- **Transparency reports.** "Quarterly. Process statistics with methods and n ≥ 10 suppression, complaints handled, rules changed, AI evaluations summarised, Marketplace report (REC-13). Never outcome statistics."
- **Briefs.** "Short, sourced explainers for organisations: RB-IOS 2026 and ODR; the Mediation Act's notification status; defensible appointments after CORE and Bhadra; POSH Internal Committee timelines."
- **Presentations.** "Decks from events and partner sessions, with speaker notes. Slides carry alt text and a transcript."
- **Templates and checklists.** "Model dispute-resolution clauses (EMC-2026.1), settlement checklists, registration and stamping checklist for property settlements, Form-1 pack."

**Rules shown on the page.** "Gated downloads (email) use our Resources Download Terms; we send a double-opt-in email and never add you to marketing without a separate consent." Versions: "A new upload creates a new version; earlier versions stay available unless withdrawn." Review: "Each item is reviewed within 12 months; items past review show 'Under review — may be out of date'."

**Empty state.** "The first transparency report is due {{metric:first_report_month}}. Briefs appear as they clear legal review."

---

## 23. Blog landing — `/blog` (P-68, new; toggle `web.blog.enabled`)

| Field | Copy |
|---|---|
| SEO title | Blog: Mediation, Arbitration and Dispute Resolution in India |
| Meta description | Articles from Equator's team and invited neutrals and academics on how disputes get resolved in India — plain language, sourced, legally reviewed, never about live cases. |
| H1 | Blog |
| Hero one-liner | Writing about how disputes actually get resolved. Plain language, sources shown, reviewed before publishing. |

**Layout.** Featured post · latest posts (category chips: Mediation · Arbitration · Lenders and borrowers · Insurance · Workplace · Family · International · Institution news · For neutrals · Research) · series rail · author box per post (credential card; neutrals' enrolment verified through P03) · RSS/Atom links · newsletter block (unticked consent; double opt-in).

**Post anatomy (template rules).** First published and last updated both shown · reading time · table of contents · "Last legally reviewed" stamp · related glossary terms · related posts · `Article` JSON-LD with `dateModified`. Statute citations link to the Legal Rules Register entry; a citation to a repealed instrument fails import lint (IPB-04-45).

**User-post programme (`web.blog.user_posts.enabled`): "Write for Equator".**

Block copy: "Panel neutrals, academics and students of dispute resolution may write for the Equator blog. We publish pieces that explain process, law and practice in plain language. We do not publish anything about a live or identifiable case, any merits view on a dispute, or any marketing of a practice."

*Who can write:* empanelled neutrals (verified), faculty and researchers at partner universities, invited practitioners. Eligible roles are a setting (`web.blog.user_posts.eligible_roles`). *How it works:* accept the Blog and User-Content Terms (IPB-05 template 12; version recorded) → write in the platform editor (same sanitiser as staff posts) → submit → moderation queue (editor review; legal check if lint flags statutes, statistics, named parties or comparisons) → scheduled → published under your name with your credential card. *What is checked:* Claims Register for any figure; no case details (lint for case-number patterns, party names from the platform, "my client", "a matter I am hearing"); no competitor names; links capped at five, `rel="ugc nofollow"`; images scanned; a Vidhi pre-screen flags, never publishes. *Takedown:* any published post can be unpublished at once by the content editor with a reason; the author is told; the page returns 410 with a dated notice. *What authors get:* a byline, a credential card, a stable URL. Nothing else — no fee, no advantage in grade or allocation (NN-28), and no listing benefit.

**Comments.** Off by default (`web.blog.comments.enabled`); pre-moderated when on; no third-party comment service.

---

## 24. Vlog — `/vlog` (P-71, new)

| Field | Copy |
|---|---|
| SEO title | Video: How Dispute Resolution Works \| Equator Resolution |
| Meta description | Short explainers on mediation, arbitration, fees and the platform, with captions, transcripts and Indian Sign Language where available. |
| H1 | Watch and understand |
| Hero one-liner | Short videos with captions in English and Hindi, full transcripts and, where available, an Indian Sign Language rendition. |

Rules: click-to-load posters (no request to the video provider before consent); `youtube-nocookie.com`; captions en/hi mandatory; transcript page per video at `/vlog/{slug}/transcript`; ISL toggle where a rendition exists; never autoplay with sound; `VideoObject` JSON-LD. Series: "Your first case" · "For neutrals" · "For organisations" · "Rules explained".

---

## 25. Contact — `/contact` (P-45 delta)

The P-45 copy stands. v3.2 adds the three office blocks as `office` records (editable, not deletable):

| Office | Block copy |
|---|---|
| Delhi | **Delhi** · {{office.delhi.address}} · {{office.delhi.hours}} · Map (click to load) · "Case-team meetings by appointment." |
| Noida | **Noida** · {{office.noida.address}} · {{office.noida.hours}} · Map (click to load) · "Operations and technology." |
| Jaipur | **Jaipur** · {{office.jaipur.address}} · {{office.jaipur.hours}} · Map (click to load) · "Registry and case services." |

Registered office rendered separately with "exactly as on the GST registration". **WhatsApp button:** labelled "Message us on WhatsApp"; opens `wa.me` only after an explicit click; shows the opt-in notice (IPB-05 template 18): "By messaging us on WhatsApp you agree that we may reply there about your enquiry. We never send marketing on WhatsApp without a separate consent, and never discuss a case's merits." Map images are static until clicked (no provider request before consent). Form consent is purpose-wise; the form posts server-side to the CRM with the consent receipt.

---

## 26. Changelog — `/changelog` (P-69, new)

| Field | Copy |
|---|---|
| SEO title | Changelog \| Equator Resolution |
| Meta description | What changed on the Equator platform, release by release, with dates and links to help articles. |
| H1 | What's new |
| Hero one-liner | Every release, dated, in plain words, with the article or tutorial that explains it. |

Entry anatomy: release version · date · area filter (Parties · Neutrals · Organisations · Chambers · Rules · Security · Accessibility · API) · summary in ≤ 60 words · "Learn more" to the help article · RSS. Rules: public audience only (tenant-only entries render in-app); breaking API changes carry the notice period from Appendix AE §AE.4.9; security fixes are described without exploit detail. Tenants may suppress minor-release cards in-app (`tut.whats_new.min_level`).

---

## 27. Accessibility statement — `/accessibility` (P-70)

Page renders Appendix U §U.10 (EAS-2026.1) as a `legal_page` with version and effective date, plus: conformance target (WCAG 2.2 AA; IS 17802; GIGW 3.0 for court-facing deployments; EN 301 549 referenced for international parties); what works (keyboard, screen readers tested, captions, ISL interpreter booking, plain-language mode, dyslexia-friendly font option, text scaling to 200%); **known issues table** from the accessibility backlog (issue · pages affected · workaround · target fix release); feedback channel (`{{entity.accessibility_email}}`, phone, form) with a reply within {{rule:a11y.reply_days}} working days; "Last reviewed" at least every six months. Hero one-liner: "If something here does not work for you, tell us; we will fix it or give you another way."

---

## 28. Footer (binding text; IPB-04 §04.3.8 structure)

**Brand block.** Logo · "Equator Resolution — mediation, conciliation and arbitration online, under published rules, with independent neutrals." · "Part of the Infrabyx Group" → `{{web.footer.group_url}}`

**Columns.**
- *Resolve:* Understand your options · File a case · Respond to a notice · Track a case · Verify a document · How it works · Fees · Rules
- *Disputes:* Loans and finance · Business and commercial · Family and property · Insurance · Workplace · International
- *Organisations:* For organisations · Grievance redressal · POSH Internal Committee · Developers and API · Pricing for organisations
- *Neutrals and chambers:* Find a neutral · Become a neutral · How we grade · Private ADR Chambers · Marketplace
- *Resources:* Documentation · Resources library · Blog · Video · Help and tutorials · Glossary · Decisions library · Transparency reports · Changelog
- *Company:* About · Governance · Advisory Council · Team · Leadership · Investors (when enabled) · Careers · Press · Partners · Contact · Trust and security
- *Legal:* Privacy Notice · Cookie Notice · Terms of Service · Fees, Deposits, Cancellation and Refund Policy · Disclaimer · AI Use and Transparency · Grievance Redressal Policy · Acceptable Use · Accessibility Statement · Security and Responsible Disclosure · Data Processing Addendum (request) · Rules, Procedures and Fees · Publication Policy · Allocation Policy · Blog and User-Content Terms · Resources Download Terms · Marketplace Terms

**Contact region.** Registered office {{entity.registered_office}} · Offices: Delhi · Noida · Jaipur · Phone {{entity.phone}} · WhatsApp (button with consent notice) · {{entity.email_support}} · {{entity.email_sales}}

**Entity line.** "{{entity.legal_name}} · CIN {{entity.cin}} · GSTIN {{entity.gstin}}" (text, copyable) [LAW: Companies Act 2013 s.12(3)(c)]

**Officers line.** "Grievance Officer: {{gro.name}}, {{gro.email}} · Data Protection Officer: {{dpo.name}}, {{dpo.email}}" → `/grievance`, Privacy Notice [LAW: DPDP Act 2023 s.8(9), s.13; IT Rules 2021 r.3(2)]

**Social (CMS-managed list; each with `aria-label="Equator Resolution on LinkedIn (opens in new tab)"`).** LinkedIn · X · YouTube · Instagram · WhatsApp Channel. At least one.

**Utilities.** Status · Language (English · हिन्दी) · Cookie settings · Accessibility · Sitemap · Report a problem

**Disclaimer (locked; [COUNSEL]).** "Equator Resolution is a private dispute resolution institution and technology platform. It is not a court, tribunal, regulator or government body and does not give legal advice. Neutrals appointed through Equator are independent professionals. Where a free public forum may suit you better, we will say so."

**Copyright.** "© {year} {{entity.legal_name}}. All rights reserved."

---

## 29. Cookie banner and preference centre (DPDP wording default; IPB-04 §04.3.9)

**Banner (three equal buttons).** Title: "Cookies and similar tools." Body: "We use necessary cookies to run this site. With your consent we also use functional cookies (remembering your language and preferences), analytics (first-party, to see which pages help) and, on marketing pages only, marketing cookies. You can change your choice at any time from 'Cookie settings' in the footer. Closing this notice without choosing means only necessary cookies are set." Buttons: **Accept all** · **Reject all** · **Manage**. Links: Cookie Notice · Privacy Notice.

**GPC variant.** Add: "Your browser sent a Global Privacy Control signal, so analytics and marketing are off unless you turn them on."

**Preference centre.** Four categories with plain descriptions and the vendor list drawn from the Cookie Notice table. *Necessary (always on):* "Sign-in, security, your consent choice, load balancing." *Functional:* "Language, saved preferences, click-to-load video and maps." *Analytics:* "First-party analytics to understand which pages help. No advertising use." *Marketing (public pages only):* "Measuring campaigns. Never set on case, hearing, payment, grievance or POSH pages." Footer: "Changing your choice writes a new consent record; we keep a receipt you can request."

**Authenticated routes.** No marketing category is ever requested; the banner, if shown, offers necessary and first-party analytics only (IPB-04-82).

---

## 30. One-liner bank (v3.2 additions; the Appendix P §2 bank stands)

Numbered G-01 onwards to avoid collision with Appendix P §2 series A–F. Each passed the Appendix P §2.1 legal-accuracy checks.

| ID | Line | Use |
|---|---|---|
| G-01 | Resolve disputes, not relationships. | Brand line (D2-20) |
| G-02 | Not a court. Not a regulator. Independent, and we show it. | Identity |
| G-03 | Fees you see before you book. | Pricing |
| G-04 | Nobody who pays us picks who decides. | Neutrality |
| G-05 | Published rules, versioned, dated, free to read. | Rules |
| G-06 | The lightest process that can work comes first. | Staged processes |
| G-07 | Mediation is private and never recorded. | Mediation |
| G-08 | An appointment you can defend is one you can show. | Independence Evidence Pack |
| G-09 | We tell you when a free forum is the better route. | Signposting |
| G-10 | Your documents stay in India. | Residency |
| G-11 | Hindi and English from day one. | Access |
| G-12 | Captions on. Interpreters on request. | Accessibility |
| G-13 | Numbers come with dates and methods, or they do not appear. | Transparency |
| G-14 | Independence is a job, not a slogan. | Careers |
| G-15 | Vidhi drafts. People decide. | AI |
| G-16 | An AI that never says who is right. | AI |
| G-17 | Leave with everything, free, any time. | Portability |
| G-18 | Grades follow a policy. Appointments follow rules. Neither can be bought. | Neutrals |
| G-19 | One dispute, more than one way through. | Hybrid |
| G-20 | Settle in weeks, not years — when both sides are ready. | Mediation (no promise of outcome) |
| G-21 | A conciliated settlement has the status of an award. | Conciliation [LAW s.74] |
| G-22 | Borrowers never pay a success fee. | FIN (X-07) |
| G-23 | There is never a success fee on an insurance claim. | INS |
| G-24 | Complaint content never leaves the sealed workspace. | POSH |
| G-25 | We mediate terms. Courts decide status. | FAM |
| G-26 | Enforcement depends on the seat. We explain; we do not promise. | INT |
| G-27 | Speed from the engine, never from choosing the neutral. | Enterprise |
| G-28 | Grievance clocks you can see, drafts you approve. | GRM |
| G-29 | Your practice, your name, your domain — on institution-grade tooling. | Chambers |
| G-30 | Training gives no advantage in appointments. | Institute |
| G-31 | Governance kept apart from commerce. | Governance |
| G-32 | The Council advises. It appoints nobody. | Advisory Council |
| G-33 | Dated releases, named contact, approved facts. | Press |
| G-34 | Partnerships that widen access without touching independence. | Partners |
| G-35 | An institution is its documents. | Documentation |
| G-36 | Every release, dated, in plain words. | Changelog |
| G-37 | If it does not work for you, tell us. We will fix it or give you another way. | Accessibility |
| G-38 | Sponsored never means appointed. | Marketplace |
| G-39 | Reports you can cite, with a version and an author. | Resources |
| G-40 | Written by people who do the work, reviewed before it is published. | Blog |
| G-41 | What we are building, how it is governed. Not an offer. | Investors [COUNSEL] |
| G-42 | Start with your options, not with a fee. | Home CTA |
| G-43 | Evidence hash-sealed. Awards you can verify on this site. | Trust |
| G-44 | Three equal buttons. Your choice, recorded. | Cookie banner |

**Rejected lines (linter seeds):** "India's most trusted ODR platform" (unprovable); "Court-approved" (GX-4); "Guaranteed settlement" (NN-17); "Faster than court — 90% settle" (statistic without register); "Certified secure" (NN-31); "Judges on our panel" (title misuse unless former judges with consent and accurate description).

---

## 31. FAQ bank (v3.2; ≥ 50; answer-first; IDs F-01 onwards for this deck; Appendix P §3 FAQs stand)

| ID | Question | Answer (first sentence ≤ 25 words) | Pages |
|---|---|---|---|
| F-01 | Is Equator a court? | No. Equator is a private dispute resolution institution; it administers mediation, conciliation and arbitration under its published Rules. Courts and tribunals remain available to you as the law provides. | Home, About |
| F-02 | Do I need a lawyer? | No, but you may have one. Parties can act for themselves; a representative acts under a signed letter of authority you can narrow or revoke at any time. | Home, Help |
| F-03 | Who owns Equator? | {{entity.legal_name}}, part of the Infrabyx Group. Ownership is separate from case decisions, which sit with the Institutional Committee. | About |
| F-04 | Does Equator give legal advice? | No. We explain processes, costs, timelines and free alternatives; we never tell you whether your case is strong or what it is worth. | About, Help |
| F-05 | How much does it cost? | It depends on the process and the amount in dispute; the fee calculator shows the full total including GST before you book. | Home, Fees |
| F-06 | Who decides cases — the company's board? | No. The Board takes no case decisions. Appointments, challenges, scrutiny and complaints sit with an Institutional Committee with a majority of external members. | Governance |
| F-07 | Can I read the rules before I start? | Yes. Every rule, code and fee schedule is published with a version and effective date at `/rules` and `/fees`. | Governance, Docs |
| F-08 | Does the Advisory Council appoint neutrals? | No. The Council advises on rules, standards and access; it has no role in appointments or in any case. | Advisory Council |
| F-09 | How is a mediator or arbitrator chosen? | By rule, from Equator's panel: eligibility filters, conflict checks, rotation and concentration caps. No party or client picks or vetoes the neutral. | Home, Neutrals |
| F-10 | Can my bank or insurer choose the arbitrator? | No. Indian courts have set aside awards where one side controlled the appointment; Equator's allocation is independent and documented in an Independence Evidence Pack. | FIN, INS |
| F-11 | Is mediation recorded? | No. Mediation is private and is not recorded; caucus notes are sealed to the mediator. Arbitration hearings are recorded only with everyone's consent. | Mechanisms |
| F-12 | Is a settlement enforceable? | A conciliated settlement signed under Part III of the Arbitration and Conciliation Act 1996 has the status of an award; a mediated settlement is a contract unless converted by consent; an award is enforceable under s.36. [LAW] | Mechanisms |
| F-13 | What is e-stamping and do I need it? | Domestic awards and settlement instruments are stamped per the state's stamp law at signing; the platform handles it and shows the duty before you sign. | Outcomes |
| F-14 | Where is my data stored? | In India. Documents, recordings and AI processing for case content stay on India-resident infrastructure. | Home, Trust |
| F-15 | What does Equator do with AI? | Our assistant Vidhi summarises, extracts, drafts for a human and explains process. It never decides, advises, predicts or values, and it is locked out of a published list of actions. | Trust, Help |
| F-16 | Can I object to AI being used on my case? | Yes. Tell your case manager; the deterministic path produces the same routes, clocks and fees without a model. | Help |
| F-17 | What if my dispute is criminal? | We do not take it. Where the law allows the civil or money side to be settled, only that side is mediated; the court alone decides on the criminal case. | Disputes |
| F-18 | Can Equator decide my divorce or custody? | No. Status, custody and guardianship are for courts. We can mediate the terms of a mutual-consent arrangement, maintenance and property. | FAM |
| F-19 | My insurance claim was rejected — is Equator my only option? | No. Individuals can approach the Insurance Ombudsman free of charge within the limits in the Rules; we tell you so first. | INS |
| F-20 | My bank has not resolved my complaint — what next? | After 30 days without a reply, or if dissatisfied, you may complain to the RBI Integrated Ombudsman free of charge within 90 days. [LAW: RB-IOS 2026] | FIN |
| F-21 | Are MSME delayed-payment disputes handled here? | We can mediate or arbitrate them, but the statutory MSEFC route is free and may suit you better; we signpost it first. | COM |
| F-22 | How long does it take? | Mediation usually completes within the published window of {{rule:med.window_days}} days; arbitration awards are due within 12 months of completed pleadings (extendable by 6). Your matter sets the real pace. | Home, How it works |
| F-23 | What happens if the other side ignores the notice? | We serve through verified channels and record proof. In arbitration the tribunal may proceed as the Rules and the Act allow; in mediation nothing can be imposed. | Respond |
| F-24 | Can I pay in instalments? | Platform fees are paid per step before the step begins; settlement sums between parties never pass through Equator and may follow any schedule the parties agree. | Fees |
| F-25 | Does Equator hold settlement money? | No. Settlement sums go to a bank escrow with a trustee or directly between parties with proof; they never touch Equator's merchant account. | Fees, Trust |
| F-26 | What are the grades of neutrals? | Grades A, B and C are eligibility tiers under a published policy — labelled Distinguished, Principal and Associate Neutral. They are not rankings of outcomes. | Neutrals |
| F-27 | Can I see how a neutral has performed? | We publish process measures in aggregate, never individual outcome statistics or win rates. | Neutrals |
| F-28 | Can I pick a specific neutral from the directory? | You can request a panel neutral; the request is checked against conflicts and the Rules, and both sides must agree. Equator appointments otherwise follow the allocation policy. | Neutrals |
| F-29 | What is the Private Practice Marketplace? | A separate surface where private practitioners and chambers list their own services. Nothing there affects Equator appointments. | Marketplace |
| F-30 | Are there paid positions in the directory? | No. The institutional directory has no paid listings. Sponsored slots, if ever enabled, exist only on the Marketplace, labelled and capped. | Neutrals, Marketplace |
| F-31 | What is med-arb? | Mediation first; if it fails and every party gives informed written consent, arbitration follows under the Rules — with the safeguards on the hybrid page. | Hybrid |
| F-32 | Can the same person mediate and then arbitrate? | Only with informed written consent of every party after the mediation ends, and only where the Rules allow it for that dispute type; caucus information never reaches the arbitrator. | Hybrid |
| F-33 | Do I pay for every step separately? | Yes. Each step has its own published fee and its own booking; nothing moves to the next step without your choice. | Hybrid, Fees |
| F-34 | How do I respond to a notice I received? | Enter the notice code at `/respond`, confirm "this is me", read the claim and the options, and reply within the time shown. | Respond |
| F-35 | Can I use Equator in Hindi? | Yes. English and Hindi are live; other languages are enabled by configuration; legal templates in any language are human-reviewed before use. | Help |
| F-36 | I am deaf or hard of hearing — can I join a hearing? | Yes. Live captions, transcripts where consented, visual alerts and Indian Sign Language interpreter booking are available. | Accessibility |
| F-37 | How do I complain about Equator's service? | Write to the Grievance Officer at {{gro.email}}; we acknowledge within 48 hours and aim to resolve within one month, with a level-2 review by the Company Secretary. | Help, Grievance |
| F-38 | How do I complain about a neutral? | Through the complaints route under the Code of Conduct; the Ethics & Complaints Sub-Committee decides. Challenges to an appointment are a separate route under the Rules. | Neutrals |
| F-39 | Can I get my data out? | Yes, free, at any time: a folder package of Word, Excel and PDF files with a manifest and checksums. | Trust |
| F-40 | How do I become a neutral? | Apply, verify credentials, complete the Qualifying Assessment Programme, accept the Code of Conduct. Training from any recognised provider counts equally. | Neutrals |
| F-41 | Does Equator's own training help me get empanelled faster? | No. No provider's training — including the Equator ADR Institute — gives any advantage in empanelment, grade, allocation or the assessment fee. | Training |
| F-42 | How often are grades reviewed? | On the cycle in the grading policy, using process measures only; you see your own data and may dispute it. | Neutrals |
| F-43 | What is a Vendor Assurance Room? | A space inside an organisation's settings holding Equator's security, privacy, continuity and audit documents, updated on a published cadence, with auditor access. | Trust, For organisations |
| F-44 | Is Equator ISO 27001 certified? | We run a readiness programme; we list a certificate here only when it is issued, with its scope. | Trust |
| F-45 | Is Equator approved by the RBI or SEBI? | No regulator "approves" Equator. Where a regulated scheme applies (for example SEBI SMART ODR), we say so and apply its rules exactly; otherwise we make no regulatory-status claim. | Trust |
| F-46 | Can I invest in Equator through this site? | No. Equator does not offer securities to the public or through its website; any issue would be made privately to identified persons under the Companies Act 2013. [COUNSEL] | Investors |
| F-47 | Who can write for the blog? | Empanelled neutrals, partner-university academics and invited practitioners, under the User-Content Terms, after editorial and legal review. Never about a live case. | Blog |
| F-48 | Do blog authors get paid or preferred? | No. Authors get a byline and a credential card — no fee and no advantage in grade, allocation or listing. | Blog |
| F-49 | Where do I report a security vulnerability? | Through the responsible-disclosure page linked from Trust and `security.txt`; we acknowledge within the published time. | Trust |
| F-50 | Which cookies do you use? | Necessary cookies always; functional, analytics and marketing only with your consent, listed by vendor in the Cookie Notice. | Cookie |
| F-51 | Can I change my cookie choice later? | Yes. "Cookie settings" in the footer reopens the preference centre; withdrawing is as easy as consenting. | Cookie |
| F-52 | Do you share my data with other Infrabyx companies? | Not for cases. Case and appointment data are never shared with group lending products; any other sharing needs a documented lawful basis and is listed in the Privacy Notice. | Trust |
| F-53 | What is the Decisions Library? | Published awards and settlements, only with every party's consent and after redaction, cited as `EQR/<YYYY>/AWD/<NNNN>`. It is a research resource, not a predictor. | Docs |
| F-54 | Do you publish success rates? | No. We publish process statistics with methods; outcome and settlement rates are never published and never influence grades or appointments. | Trust, Resources |
| F-55 | Can an organisation use its own branding? | White-label plans allow a brand pack — name, logo, colours within contrast rules — and a display name for the AI assistant. The institution's rules and independence do not change. | For organisations, Chambers |

---

## 32. SEO titles and descriptions — register for the pages this deck owns

| Route | Title (≤ 60) | Description (≤ 155) |
|---|---|---|
| `/` | Online Dispute Resolution in India \| Equator Resolution | Mediation, conciliation and arbitration online, administered by an independent institution. Clear fees, published rules, independent neutrals. |
| `/mechanisms/hybrid` | Med-Arb, Arb-Med and Staged Dispute Resolution | How staged processes work at Equator: negotiate, mediate, then arbitrate if needed, with separate consent and fees. |
| `/neutrals/how-we-grade` | How Equator Grades and Appoints Neutrals | Grades A, B and C, the Qualifying Assessment Programme, a process-only Quality Index and rule-based allocation. |
| `/trust/independence-evidence-pack` | The Independence Evidence Pack \| Equator Resolution | Every appointment ships a dated record of how the neutral was chosen: rules version, filters, rotation, conflicts, disclosures. |
| `/about` | About Equator Resolution | An independent dispute resolution institution for India, operated by Equator Resolution Service Private Limited (Infrabyx Group). |
| `/about/governance` | Governance: Board, Institutional Committee and Rules | A board that takes no case decisions, an Institutional Committee with an external majority, versioned rules, a transparency report. |
| `/about/advisory-council` | Advisory Council \| Equator Resolution | Who advises Equator and what the Council does not do: it has no role in appointing neutrals or deciding cases. |
| `/team` | Our Team \| Equator Resolution | The people who run case services, panel relations, technology and operations — roles, languages, responsibilities. |
| `/leadership` | Leadership \| Equator Resolution | Equator's leadership, board and advisory council, with verifiable bios and declared interests. |
| `/investors` | Investor Information \| Equator Resolution | Vision, market context, governance, leadership and milestones for existing and identified investors. Not an offer of securities. |
| `/careers` | Careers at Equator Resolution | Open roles in case services, panel relations, engineering, operations and legal. Delhi, Noida, Jaipur and remote. |
| `/docs` | Documentation: Rules, Forms, Fees, API and Data Protection | The Rules and codes, forms library, fee schedules, decisions library, developer portal and data-protection documents, versioned. |
| `/docs/forms` | Forms Library \| Equator Resolution | Every form by process and dispute type, versioned, with legal basis and download in PDF and DOCX. |
| `/press` | Press and Media \| Equator Resolution | Press releases, dated coverage, media kit and a named spokesperson. We do not comment on individual cases. |
| `/partners` | Partners: Institutions, Universities and Bar Associations | How Equator works with institutions, universities, bar associations and technology partners, and the lines it does not cross. |
| `/resources` | Resources: Reports, Transparency Reports, Briefs and Presentations | Transparency reports, research briefs, presentations, templates and checklists — versioned, dated, cite-able. |
| `/blog` | Blog: Mediation, Arbitration and Dispute Resolution in India | Plain-language, sourced, legally reviewed articles from Equator's team and invited neutrals and academics. |
| `/vlog` | Video: How Dispute Resolution Works \| Equator Resolution | Short explainers with captions, transcripts and Indian Sign Language where available. |
| `/changelog` | Changelog \| Equator Resolution | What changed on the platform, release by release, with dates and links to help. |
| `/accessibility` | Accessibility Statement \| Equator Resolution | Our conformance target, what works, known issues and how to tell us when something does not. |
| `/trust` | Trust and Security \| Equator Resolution | What we hold, where it lives, who processes it, what we have and have not certified, and how to report a vulnerability. |
| `/contact` | Contact Equator Resolution | Email, phone, WhatsApp, offices in Delhi, Noida and Jaipur, Grievance Officer and Data Protection Officer. |

---

## 33. Image placeholder list (owner replaces from Brand Studio; all with alt text; no text in images)

| ID | Page | Placeholder | Alt text | Size (px) |
|---|---|---|---|---|
| IMG-01 | Home hero | Abstract illustration: two paths meeting at a calm horizon line in teal and coral; no people | Two lines converging on a horizon, representing agreement | 1600×900 |
| IMG-02 | Home "How it works" | Five-step line diagram (SVG, inline) | Five steps from options to outcome | SVG |
| IMG-03 | Home trust teaser | Icon set: shield, document with hash, India outline | Security, evidence and India residency icons | 96×96 each |
| IMG-04 | Mechanism pages | One icon per process (handshake, bridge, gavel-free scale, stepped path) | Process icon | 128×128 |
| IMG-05 | Vertical hubs | Six muted photographs of everyday contexts (a loan statement, a shop counter, a family table, a policy document, a workplace, a port) — stock with licence; no faces where avoidable | Context photograph described per hub | 1200×675 |
| IMG-06 | About | Office photographs Delhi, Noida, Jaipur (consented staff or empty rooms) | Equator office, {city} | 1200×800 |
| IMG-07 | Governance | Diagram: Board and Institutional Committee separated by a wall (SVG) | Two bodies separated; Committee owns case functions | SVG |
| IMG-08 | Team, Leadership | Portraits (consent recorded) or initials tile | {Name}, {Role} | 600×600 |
| IMG-09 | Investors | None (text page); optional milestone timeline SVG | Timeline of dated milestones | SVG |
| IMG-10 | Careers | Workplace photographs, consented | Team at work, {city} | 1200×800 |
| IMG-11 | Docs hub | Six tile icons (rules, forms, fees, decisions, API, data) | Tile icon | 96×96 |
| IMG-12 | Press | Logo pack preview on light and dark | Equator Resolution logo on light and dark backgrounds | 1200×630 |
| IMG-13 | Partners | Partner logos (permission on file) | {Partner} logo | 240×120 |
| IMG-14 | Trust | Data-flow diagram (SVG) | How case data moves and where it stays | SVG |
| IMG-15 | Resources | Cover thumbnails auto-generated from title and type | Cover of {title} | 600×800 |
| IMG-16 | Blog | Per-post cover, deterministic template from title and category | Cover of {post title} | 1200×630 |
| IMG-17 | Vlog | Poster frames with captions badge | Poster for {video title} | 1280×720 |
| IMG-18 | OG default | Brand mark on teal with the brand line | Equator Resolution — Resolve disputes, not relationships | 1200×630 |
| IMG-19 | Favicon set | Mark on teal, maskable | Equator Resolution | 16–512 |
| IMG-20 | Accessibility | None (text); optional ISL interpreter photo with consent | ISL interpreter in a hearing | 1200×800 |

---

## 34. Policy page list (Appendix U set + IPB-05 inserts; footer "Legal" column)

| # | Page | Route | Registry key (Appendix U) | Source template | Status |
|---|---|---|---|---|---|
| 1 | Privacy Notice | `/privacy` | EPN-2026.1 | U-4; IPB-05 template 1 | Draft — counsel |
| 2 | Cookie Notice | `/privacy/cookies` | ECN-2026.1 | U-5; IPB-05 template 5 | Draft |
| 3 | Terms of Service | `/terms` | ETS-2026.1 | U-6; IPB-05 template 2 with EQ insert | Draft — counsel |
| 4 | Payment and Subscription Terms | `/legal/payment-terms` | EPT-2026.1 *(v3.2 new)* | IPB-05 template 3 with EQ insert | New |
| 5 | Fees, Deposits, Cancellation and Refund Policy | `/fees/refunds` | ERP-2026.1 | U-7; IPB-05 template 4 | Draft — Board |
| 6 | Disclaimer and Use of the Word "Court" | `/disclaimer` | EDS-2026.1 | U-8 | Draft |
| 7 | AI Use and Transparency Policy | `/legal/ai-use` | EAU-2026.1 *(v3.2 new)* | IPB-05 template 6 with EQ insert; links `/rules/ai-governance` | New |
| 8 | Grievance Redressal Policy | `/grievance` | EGP-2026.1 | U-12; IPB-05 template 7 | New |
| 9 | Acceptable Use Policy | `/legal/acceptable-use` | EAP-2026.1 *(v3.2 new)* | IPB-05 template 8 with EQ insert (no recording or sharing of hearings; no off-platform contact with neutrals; no tampering) | New |
| 10 | Retention Policy (public summary) | `/legal/retention` | ERT-2026.1 *(v3.2 new)* | IPB-05 template 9; Appendix Q §2.8 | New |
| 11 | Accessibility Statement | `/accessibility` | EAS-2026.1 | U-10; IPB-05 template 10 | Draft |
| 12 | Security and Responsible Disclosure | `/trust/security`, `/.well-known/security.txt` | ESS-2026.1 | U-9; IPB-05 template 11 | Draft |
| 13 | Blog and User-Content Terms | `/legal/user-content` | EUC-2026.1 *(v3.2 new)* | IPB-05 template 12 | New |
| 14 | Resources Download Terms | `/legal/resources-terms` | ERD-2026.1 *(v3.2 new)* | IPB-05 template 13 | New |
| 15 | Marketplace Terms (users, providers) | `/marketplace/terms` | AA-1, AA-2 | Appendix AA; IPB-05 template 14 | Draft |
| 16 | Data Processing Addendum (request) | `/trust/dpa` | EDP-2026.1 *(v3.2 new)* | IPB-05 template 15 | New |
| 17 | Service Level Terms (organisations) | `/legal/sla` | ESL-2026.1 *(v3.2 new)* | IPB-05 template 16 | New |
| 18 | Vendor Assurance Statement | `/trust#vendor-assurance` | EVA-2026.1 *(v3.2 new)* | IPB-05 template 17 | New |
| 19 | Consent texts (cookie, marketing, WhatsApp, DPDP purposes) | in-product | ECT-2026.1 *(v3.2 new)* | IPB-05 template 18 | New |
| 20 | Equator Resolution Rules; Code of Conduct; Staff Code; Allocation, Publication Policies; Model Clauses; Charter | `/rules/*`, `/about/governance/charter` | U-1, U-2, U-3, U-11, U-13, U-14, U-15 | Appendix U | Draft |

Each page renders from the policy registry (`core.procedure_rules`), carries version, effective date, "what changed" and the prior-version archive link; the footer build fails if any adopted template is missing (IPB-04-71).

---

## 35. What the owner must decide before publishing (summary; rows also in README §4 and Appendix J §J.10)

1. Investors page: publish or keep hidden; which documents are gated; counsel wording of the disclaimer [OWNER, COUNSEL].
2. Names for every `{{person:*}}` placeholder and photo consents [OWNER].
3. Board composition and Advisory Council members and terms [OWNER].
4. Statutory auditor name and the policies "adopted — available on request" [OWNER].
5. Milestone dates and the first transparency report month [OWNER].
6. Blog user-post programme: eligible roles and the editorial board [OWNER].
7. Social accounts to list in the footer [OWNER].
8. Market-context figures for the Investors page: which to cite and from where [VERIFY].

*End of Website Content Deck v1.0.*
