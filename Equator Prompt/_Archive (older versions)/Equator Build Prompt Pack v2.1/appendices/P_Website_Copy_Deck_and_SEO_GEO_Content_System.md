# Appendix P — Website Copy Deck and SEO/GEO Content System

> **Binding for P13** (public website, CMS, SEO and growth) and for every copy surface in P01, P02, P05, P07 and P12 (in-product microcopy, §4). Read with: master §1 (positioning), NN-01, NN-05, NN-16, NN-17, NN-20, NN-23, NN-26–NN-29, X-14–X-16, M-06; 02 D2-12, D2-14–D2-20; Appendix H §5–§6 (live-site corrections WC-01–WC-60 and the safe-claims library remain binding — this appendix extends them); Appendix C §E–§G (tokens, UX principles, status vocabulary); Appendix K (Explorer copy rules EP-01–EP-14, PL-15 lint list); V1–V6 §1 (vertical facts). Version 2.0 · 21 October 2026. Research base: S9 §5–§8; C4 A–B; R4.
>
> **Hindi.** Every Hindi line in this appendix is a draft for the P13 FR-P13-25 workflow and must pass qualified legal-translator review before publication (NN-23). The marker is stated once here and applies to all Hindi text below.

---

## 0. Scope, precedence and conventions

### 0.1 What this appendix owns

| Owns | Does not own |
|---|---|
| Final public website copy (page by page), catch-lines, in-product microcopy, voice and terminology, SEO/GEO/AI-search rules, structured-data policy, content governance cadence, copy-lint rules | Live-site remediation list (Appendix H §5, executed by FR-P13-01); fee figures (Appendix B, rendered by tokens only); legal rules (Appendix G); status state set (master §5.1); Explorer logic (Appendix K) |

Where a vertical specification's "value proposition / copy anchor" (V1–V6 §1.2) differs from this appendix, **this appendix prevails** for public copy (V3 §1.2 already defers to it). Where this appendix and Appendix H's safe-claims library differ, the stricter text applies.

### 0.2 Token conventions (no hard-coded facts in copy)

| Token | Resolves from | Example |
|---|---|---|
| `{{entity.<field>}}` | `core.tenant_branding.legal_profile` (X-15) | `{{entity.legal_name}}` → Equator Resolution Service Private Limited |
| `{{fee:<CARD>.<LINE>}}` | Published fee schedule (Appendix B §B.11; FR-P13-06) | `{{fee:ANC.CONSULT}}` |
| `{{metric:<key>}}` | Approved PR metrics snapshot (FR-P13-21) | `{{metric:active_neutrals}}` |
| `{{claim:<claim_key>}}` | Claims Register (FR-P13-10; §7.2) | `{{claim:law.award_s36}}` |
| `{{rule:<LR-ID>.<field>}}` | Legal Rules Register (Appendix G) | `{{rule:LR-RBI-001.window_days}}` |
| `{{flag:<key>}}` block | Statute-commencement / feature flag swap (FR-P13-09(e); §7.4) | Mediation Act ss.27–28 note |
| `{{locales_live}}` | CMS locale registry | "English and Hindi" |
| `{{config:<key>}}` | Platform configuration (time bands, relationship statements) | `{{config:time_bands.mediation.default}}`; a value used as a time or speed statement is an Equator target, never a promise, and needs a Claims Register record before it renders (P-D02) |

Status markers used in this appendix: **[LIVE]** usable at launch once legally approved · **[GATED: condition]** publish only when the condition and its Claims Register entry exist · **[HOLD]** never publish until management decides.

### 0.3 Decisions recorded in this appendix

| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| P-D01 | **Messaging hierarchy.** Primary tagline "Resolve disputes, not relationships." (D2-20) is the brand line (logo lock-up, home eyebrow, footer, OG image, `Organization.slogan`). The master positioning line "Resolve disputes online — fairly, quickly and enforceably." is the home H1 (WC-40). The D2-20 descriptor is the meta/OG/schema description line | Master §1; D2-20; S9 §7.4 | §1.2 |
| P-D02 | "Fast", "quickly" and "efficient" may appear only as unquantified process descriptors in the locked lines (descriptor, positioning line and its COM variant "Resolve business disputes online — fairly, quickly and enforceably.", Equator Standard). Any number of days, percentage, comparison with courts or "faster than" needs a Claims Register record | NN-17; CPA 2019 s.2(28); WC-21/22 | LINT-011 |
| P-D03 | **Structured data**: sitewide `Organization`; service pages use `Service` (provider = Organization). `LegalService` is **not emitted by default** because schema.org defines it around "advice and representation", which Equator does not provide (NN-01; Advocates Act 1961 ss.29, 33); flag `seo.schema.legalservice_enabled` = OFF, switchable only by a legal reviewer. Where ON, use `knowsLanguage` and `contactPoint.availableLanguage` (never `availableLanguage` on LegalService) | S9 G-4; amends FR-P13-13 | §6.4 |
| P-D04 | `FAQPage` markup optional (no Google rich results since 7 May 2026); `HowTo` not emitted (flag `seo.schema.howto_enabled` = OFF); JSON-LD validated with the schema.org validator, not the Rich Results Test, for types Google no longer supports | S9 G-2, G-3; amends FR-P13-13 and P13 exit gate | §6.4 |
| P-D05 | **Routes.** `/training` is the canonical training-referral page (`/academy` 301 → `/training`) because the Institute is a separate entity (D2-17); `/decisions` (consented publication Library, NN-26; App. R §3.9.1 canonical route, with `/published-outcomes` 301 → `/decisions`) is distinct from `/settlements-and-awards` (OTP retrieval of a party's own document); `/about/governance` added for the Institutional Committee (D2-15); vertical hubs use readable slugs (`/disputes/loans-and-finance` etc.) with the FR-P13-03 code routes (`/disputes/fin` …) 301-redirecting to them; bare `/pricing` keeps the WR-02 301 → `/fees`, while `/pricing/organisations` and `/pricing/professionals` are live (S9 §2.2) | D2-15, D2-17, NN-26, S9 FR-S9-10 | §3 route table |
| P-D06 | Vertical copy anchors corrected: V4 §1.2 "settles, fast" → "helps settle what an award cannot reach"; V3 §1.2 "Separate without a courtroom fight" kept only on FAM pages and never adjacent to a time claim; V2 §1.2 uses the master positioning line | NN-17; P-D02 | §3 pages P-04–P-09 |
| P-D07 | **AI-crawler policy**: search/answer bots allowed on public pages; training bots allowed on institutional explainers, rules and fees but **disallowed** on neutral profiles, published outcomes, careers and people pages — default subject to Board approval (`seo.ai_crawler_policy_version`) | S9 G-5; DPDP minimisation | §6.12 |
| P-D08 | Training page shows **at least three** recognised training options; the Equator ADR Institute card is shown only when flag `academy.institute_referral` is ON (assumption A-03) with the relationship disclosed; no copy may say Institute training is needed for empanelment or that Equator's assessment is IMI-approved | D2-17; S6 | P-37 |
| P-D09 | Appendix C §E.1 tokens (navy/teal/gold) prevail over the Marketing Playbook palette (forest green #1A3C34, gold #9B7522) | Master §15 precedence (App. C binding) | §5 |
| P-D10 | "The Equator Standard: impartial, expert, efficient." adopted as the service standard (not a hero line), each word linked to a proof page | S9 §7.3; C4 B.4 | §1.2, §1.6 |

---

## 1. Brand voice and messaging architecture

### 1.1 Positioning statement (internal — not published verbatim)

For people and organisations in India who have a dispute and want it settled without a long court fight, **Equator Resolution** is a private dispute resolution institution, running on an online platform, that offers negotiation, conciliation, mediation and arbitration across six kinds of dispute. Unlike recovery platforms and many ODR providers, Equator names the free public forum first, represents nobody, publishes its fees, rules and appointment policy, and lets AI draft only while people decide.

### 1.2 Messaging hierarchy (locked lines)

| Slot | English | Hindi | Where it is used | Status |
|---|---|---|---|---|
| Brand line (primary tagline, D2-20) | Resolve disputes, not relationships. | विवाद सुलझाइए, रिश्ते नहीं। | Logo lock-up, home eyebrow, footer, OG images, social bios, email signature, `Organization.slogan` | [LIVE] |
| Descriptor (D2-20) | Online mediation, conciliation and arbitration — fair, fast and on the record. | ऑनलाइन मध्यस्थता, सुलह और माध्यस्थम् — निष्पक्ष, शीघ्र और रिकॉर्ड पर। | Home meta description, OG description, app-store subtitle, press boilerplate first line | [LIVE] |
| Positioning line (master §1; WC-40) | Resolve disputes online — fairly, quickly and enforceably. | विवादों का समाधान ऑनलाइन — निष्पक्ष, शीघ्र और प्रवर्तनीय। | Home H1; business-page sub-headline (V2) | [LIVE] |
| Identity line (`id.private_institution`) | Equator Resolution is a private dispute resolution institution. It is not a court, tribunal, regulator or government body. | इक्वेटर रिज़ॉल्यूशन एक निजी विवाद समाधान संस्था है। यह न्यायालय, अधिकरण, नियामक या सरकारी निकाय नहीं है। | Home hero sub, footer, every vertical page footer strip, Explorer report caveat | [LIVE] |
| Brand promise (neutrality) | We represent nobody. That's the point. | हम किसी का पक्ष नहीं लेते। यही हमारी पहचान है। | Trust band, `/trust/how-we-stay-neutral` H1 sub, About | [LIVE] |
| Service standard (P-D10) | The Equator Standard: impartial, expert, efficient. | इक्वेटर मानक: निष्पक्ष, विशेषज्ञ, कुशल। | About, neutrals pages, enterprise decks — each word links to its proof page (§1.6) | [LIVE] once proof pages publish |
| Free-forum promise | A free public option may suit you better. Here it is. | एक निःशुल्क सरकारी विकल्प आपके लिए बेहतर हो सकता है। यह रहा। | SignpostCard heading on every vertical page and Explorer report | [LIVE] |
| Fees promise | Our fees, in full, before you start. | शुरू करने से पहले, हमारी पूरी फ़ीस। | `/fees` H1, checkout header | [LIVE] |
| AI promise (`ai.humans_decide`) | AI helps organise and draft. Every decision is made by a person. | एआई व्यवस्थित करने और मसौदा बनाने में मदद करता है। हर निर्णय एक व्यक्ति लेता है। | AI Governance page, Pleadings Studio, enterprise pages | [GATED: AI Governance Rule published] |

### 1.3 Voice

Six anchors from the Unified Brand, Voice & Certification Guide (July 2026), each turned into a writing rule.

| Anchor | Rule | Write | Never write |
|---|---|---|---|
| Plain | Class-8 reading level; ≤ 20 words per sentence; legal terms on first use get a one-line meaning | "An arbitrator is a neutral person who decides the dispute after hearing both sides." | "The arbitral tribunal shall adjudicate inter se disputes…" |
| Honest | State limits next to benefits; name what Equator cannot do | "We can help you agree the terms. Only the Family Court can grant the divorce." | "Get divorced online." |
| Neutral | Address both sides equally; no "your opponent", "defaulter", "recover" | "the other side" | "make them pay", "defaulting borrower" |
| Calm | No urgency devices; no exclamation marks; no pressure verbs | "When you are ready, start with Dispute Explorer." | "Act now!", "Don't miss out" |
| Specific | Absolute dates, rupee amounts from tokens, named forums | "Your last date is 2 April 2027." | "Act soon." |
| Humble | No superlatives without a claim record; no "India's first/leading/best" | "We publish our fees and rules." | "India's most trusted ODR platform" |

**Brand test (CMS reviewer checklist item; S9 C-01).** Before approval the reviewer answers: *"Would this still be true, and still feel calm, if the reader were having the worst week of their life and had no lawyer?"* A "no" blocks approval.

### 1.4 Never-say list (seeds LINT-001–LINT-026, §8)

From the Brand Guide, Appendix H §6.3, Appendix K §1.3 and PL-15: "You have a strong case" · "You'll probably get about ₹X" · "Don't worry about the deadline" · "good chance", "likely to win", "worth pursuing" · "The People's Court" · any "court", "judge", "decree", "tribunal", "official", "government-approved" describing Equator, its neutrals or outputs · "RBI/SEBI/IRDAI approved, audited, certified, compliant, designated, preferred" · "100% legally binding" · "guaranteed outcome", "we will win/recover" · "You have to arbitrate" (to a retail insurance party or worker) · anything discouraging a POSH complaint · anything treating a child's welfare as a bargaining point · "s.27 decree", "enforceable as a decree" for mediated settlements, "MCI registered/recognised", "Mediation Act compliant" (while NN-05 flag OFF) · "s.12A compliant", "satisfies s.12A", "non-starter report" (while M-06 flag OFF) · "Singapore Convention enforceable" · "pauses limitation", "stops the clock" · "final warning", "legal action will follow", "defaulter" · "Global", foreign offices · "Equa", "Equa.Law", "Private ADR Court" · "free trial" (except Private ADR Chambers 14-day trial, Card CH) · "consultation" for any Equator call (implies advice — WC-44) · "Resolution Expert" (S9 §7.3).

### 1.5 Audience tracks

| | Track A — Individuals | Track B — Businesses (SMEs and enterprises) | Track C — Neutrals (and counsel) |
|---|---|---|---|
| Who | Borrowers, policyholders, employees and workers, spouses and parents, heirs, small traders, NRIs; often stressed, often on a phone, often without a lawyer | MSMEs and companies; lenders (banks, NBFCs, HFCs, MFIs, fintechs), insurers, employers, listed companies, universities, developers; buyers: CEO, legal, compliance, CHRO, Company Secretary | Mediators, conciliators, arbitrators (advocates, retired judges, CAs, CSs, engineers, HR and family professionals); independent chambers; advocates representing parties |
| What they fear | Cost, being cheated, losing a deadline, the other side's power, shame, the court | Regulator scrutiny, challenge to awards (CORE), reputation, volume and cost, data leakage | Being used as a captive of repeat players, unpaid work, tech burden, unfair allocation |
| Promise | "Understand your options free, see the free public forum first, and settle only if you agree." | "Fair to your customers. Defensible to your regulator." (process aspiration; never placed next to a regulator's name — S9 §7.4) | "Resolve disputes. Build your practice. On your terms." (WC-42) |
| Pillars | 1 Free information first · 2 You decide (mediation/conciliation) · 3 Published fees incl. GST · 4 Your language, your phone | 1 Appointment independence and evidence (NN-03) · 2 Regulator-mapped clocks and MIS · 3 Integration (clause, API, bulk) · 4 Honest disclosure to counterparties (NN-16) | 1 Published, merit-based grading and allocation (NN-28) · 2 No paid listings, ever · 3 Tools that remove admin (case, payments, e-sign) · 4 Training choice and a fair assessment |
| Proof points (claim keys, §1.6) | `svc.explorer_free`, `law.free_forums_exist`, `law.mediation_voluntary`, `fee.published`, `fee.b2c_total_incl_gst`, `lang.live`, `law.divorce_court_only`, `law.property_registration` | `ind.appointment_policy`, `ind.disclosures`, `money.no_pass_through`, `svc.independence_pack`, `host.india`, `pay.no_card_data`, `svc.regulator_clocks` | `grade.policy_published`, `dir.no_paid_listing`, `alloc.published_rules`, `ch.trial_14d`, `qap.not_yet_imi_approved` |
| CTA verbs | Understand · See · Start · Respond · Track | Talk to us · Request a demo · Get the clause · Try the sandbox | Apply · Explore · Start 14-day trial |
| Tone notes | Second person; one idea per sentence; reassurance through facts, never adjectives | Direct, compact, evidence-led; regulation cited exactly; no "harvest", "recover faster", "collections" | Collegial; respect for experience; no flattery; process facts |
| Banned frames | "fight", "beat", "get justice", "make them pay" | "recover more", "reduce write-offs by X%" (unless claim), "our neutrals understand lenders" | "deliver justice", "be a judge", "earn from referrals" |

### 1.6 Proof points permitted (claims register binding, NN-17)

A proof point may appear only through a `{{claim:...}}` node. Existing keys are in Appendix H §6.1–6.2; the keys below are **new** and must be created in `growth.claims_register` (type, evidence, owner, review) before use.

| claim_key (new) | Approved statement (en) | Type | Condition / evidence | Owner / review |
|---|---|---|---|---|
| `fee.b2c_total_incl_gst` | "Prices for individuals include GST. The full amount is shown before you pay." | legal_effect | B2C checkout test `ECOM_total_price_breakup` green (FR-S9-11) | Finance / 6 months |
| `svc.free_forum_first` | "Where a free public forum may suit you better, we tell you first, with the last date to act." | legal_effect | NN-20 tests green; Explorer report §3 live | Legal / 12 months |
| `svc.first_session_free_respondent` | "If someone invites you to mediation through Equator, your first session is free for you." Fallback: "The cost, if any, is shown in your invitation before you agree." | service | FFS-1 default live (K §5.7) | Product / 6 months |
| `svc.independence_pack` | "Every arbitration we administer has an Independence Evidence Pack showing how the arbitrator was appointed." | legal_effect | P03 allocation + pack generator live | Registrar / 12 months |
| `svc.regulator_clocks` | "Grievance desks track the response times set by RBI, SEBI, the Industrial Relations Code and UGC rules." | regulatory_status (descriptive) | GRM variants live (P09); wording reviewed so it is not an endorsement | Legal / 6 months |
| `dir.no_paid_listing` | "No neutral can pay to be listed higher or to receive more cases." | legal_effect | `NO_PAID_PLACEMENT` CI test (FR-S9-03) | Panel manager / 12 months |
| `alloc.published_rules` | "Cases are allocated under published rules: eligibility, rotation, limits on concentration and a capped quality score based on process, never on outcomes." | legal_effect | Appendix N §6 policy published | Registrar / 12 months |
| `grade.policy_published` | "Our grading policy for Grade A, B and C neutrals is published." | legal_effect | Grading policy page live | Panel manager / 12 months |
| `qap.not_yet_imi_approved` | "The Equator Qualifying Assessment is modelled on the International Mediation Institute's QAP criteria. It is not IMI-approved; we intend to apply." | regulatory_status | Assessment published; switch to `qap.imi_approved` only with IMI letter | Legal / 6 months |
| `pay.no_card_data` | "Card and UPI payments are handled on our payment provider's secure checkout. We never see or store your full card number." | legal_effect | PCI SAQ A boundary attested (NN-31; App. Q) | Security / 12 months |
| `rep.loa_revocable` | "You can see, narrow or cancel your representative's authority at any time." | legal_effect | App. S §4 live | Product / 12 months |
| `pub.consent_only` | "We publish an award or settlement only if every party agrees, after removing names and details." | legal_effect | App. R §3 builder live | Legal / 12 months |
| `ch.trial_14d` | "Try Private ADR Chambers for 14 days. No card needed; we won't charge you unless you choose a plan." | statistic-free | Card CH trial; `trial_converts_automatically = false` (FR-S9-02) | Finance / on change |
| `svc.grievance_sla` | "We acknowledge complaints within 48 hours and aim to resolve them within one month." | legal_effect | Grievance ticket clocks live (E-Commerce Rules 2020 r.4; P14) | Grievance Officer / 12 months |
| `ai.no_training_case_data` | "Case data is not used to train AI models." | legal_effect | AI Governance Rule + provider DPA clauses on file (App. E, Q) | AI Oversight / 12 months |
| `conf.caucus_sealed` | "What you tell the mediator privately stays with the mediator unless you agree to share it." | legal_effect | NN-11 caucus RLS test | Legal / 12 months |
| `svc.languages_notices` | "Notices can be read in {{locales_live}}, with a short video explainer." | statistic-free | Locale parity check | Product / 6 months |

### 1.7 Approved terminology

| Use | Not | Note |
|---|---|---|
| Equator Resolution (first mention), Equator (after) | Equa, Equa.Law, EQR (public) | WC-41 |
| private dispute resolution institution | court, centre of justice, tribunal | GX-4 |
| neutral (generic); mediator, conciliator, arbitrator, expert (specific) | judge, panelist, adjudicator (for mediators) | — |
| case team; case manager; Registrar | officer, clerk | — |
| Institutional Committee (and its sub-committees) | Court of Arbitration, Board of Arbitration | D2-15 |
| Private ADR Chambers | Private ADR Court(s) | D2-16 |
| Equator ADR Institute (separate entity) | Equator Academy (as if Equator's own), Equa Trainings | D2-17 |
| matter (before filing) / case (after filing) | lawsuit, suit | — |
| the other side | opponent, defaulter, accused (outside s.138 explanations) | — |
| session (mediation, conciliation); hearing (arbitration) | trial, court date | — |
| settlement agreement; award; consent award | decree, order of Equator, judgment | NN-05 |
| free public forum / statutory forum | government court (for ombudsmen) | NN-20 |
| Dispute Explorer | AI lawyer, consultation, case assessment | WC-44 |
| pre-litigation (pre-suit) mediation — voluntary | statutory pre-litigation mediation, s.12A mediation | M-06 |
| fees | charges (except pass-through "at actuals") | — |

---

## 2. Catch-line and one-liner bank

### 2.1 Legal-accuracy checks applied to every line

| Code | Check | Basis |
|---|---|---|
| LC-1 | No guaranteed outcome, speed, saving or success; no number without a claim record | CPA 2019 s.2(28); CCPA Misleading Advertisements Guidelines 2022; NN-17 |
| LC-2 | No court, judge, tribunal, official or government framing of Equator | Master §1; GX-4; CPA s.2(47) |
| LC-3 | No "binding decree", "100% binding", "final and binding" for mediation | NN-05; NN-17; A&C s.34 |
| LC-4 | No claim that unnotified Mediation Act provisions (ss.4–25, 27–30), MCI recognition or s.12A authority apply to Equator | NN-05; X-16; M-06 |
| LC-5 | No advice, merits view, prediction or valuation | NN-01 (GX-1/2/3); Advocates Act 1961 ss.29, 33 |
| LC-6 | No regulator endorsement or compliance certification | NN-17; WC-08–WC-10 |
| LC-7 | No superlative or statistic outside a claim node | FR-P13-10 |
| LC-8 | Neutral to both sides; no side-taking verbs (win, recover, fight, beat) | NN-16; Brand Guide |

"✔ all" means LC-1 to LC-8 pass. Lines marked **G** are gated (condition in Notes). Every line here is short enough for a hero, card or social post; long-form body copy is in §3.

### 2.2 Brand and home (A)

| ID | Line | Use | Checks | Notes |
|---|---|---|---|---|
| A-01 | Resolve disputes, not relationships. | Brand line | ✔ all | D2-20 |
| A-02 | Resolve disputes online — fairly, quickly and enforceably. | Home H1 | ✔ all | "quickly" unquantified (P-D02); "enforceably" true for awards and s.74 settlements, explained in body |
| A-03 | Online mediation, conciliation and arbitration — fair, fast and on the record. | Descriptor | ✔ all | P-D02 |
| A-04 | We represent nobody. That's the point. | Trust band | ✔ all | — |
| A-05 | Before you go to court, see what else can work. | Home band 2 | ✔ all | Mentions court as the alternative, not Equator |
| A-06 | Understand your options — free. | Explorer CTA band | ✔ all | WC-44; `svc.explorer_free` |
| A-07 | A free public option may suit you better. Here it is. | SignpostCard | ✔ all | NN-20 |
| A-08 | Settlement only with your consent. | Mediation tiles | ✔ all | S9 §7.3 |
| A-09 | Your dispute. Your terms. | Mediation/conciliation pages only | ✔ all | Never on arbitration pages (the tribunal decides — S9 §7.3) |
| A-10 | Dispute resolution, redesigned around people. | About H1 | ✔ all | Replaces "Justice, redesigned" |
| A-11 | Built so that resolving a dispute doesn't have to take years. | About story | ✔ all | No comparative figure |
| A-12 | Find common ground before court. | Pre-litigation band | ✔ all | S9 §7.3 |

### 2.3 Trust and neutrality (B)

| ID | Line | Use | Checks | Notes |
|---|---|---|---|---|
| B-01 | How we stay neutral — and how you can check. | `/trust` H1 | ✔ all | — |
| B-02 | No one can pay to choose your arbitrator. | Lender/enterprise pages, trust band | ✔ all | G: `ind.appointment_policy` (P03 live) |
| B-03 | Every appointment leaves a trail you can inspect. | Lender page | ✔ all | G: `svc.independence_pack` |
| B-04 | Our fees are published. Our rules are published. So is how we choose neutrals. | Trust band | ✔ all | G: `fee.published`, `alloc.published_rules` |
| B-05 | No paid listings. No featured neutrals. Ever. | Directory, Become a Neutral | ✔ all | G: `dir.no_paid_listing` |
| B-06 | Settlement money never passes through our account. | Trust, payments | ✔ all | G: `money.no_pass_through` |
| B-07 | What you say in mediation stays in mediation. | Mediation page | ✔ all | Contractual + A&C s.75/s.81 for conciliation; body names exceptions (law, safety) |
| B-08 | AI drafts. People decide. | AI page, enterprise | ✔ all | G: `ai.humans_decide` |

### 2.4 Verticals (C)

| ID | Line | Vertical / page | Checks | Notes |
|---|---|---|---|---|
| C-01 | Loan dispute? Start with your lender's grievance desk — then talk it through with a neutral. | FIN hub | ✔ all | NN-20 order; RB-IOS 2026 |
| C-02 | A neutral conciliator, not a recovery agent. | FIN borrower | ✔ all | V1 §1.1 |
| C-03 | Settle your loan in writing — with release of documents and credit-report updates tracked to the end. | OTS page | ✔ all | No promise the lender agrees; tracking is a product fact |
| C-04 | Arbitration your borrowers can trust, and your auditors can check. | Lenders | ✔ all | G: `svc.independence_pack`; no regulator named in the same block |
| C-05 | Unpaid invoice? Talk first. Settle in writing. | COM / MSME | ✔ all | — |
| C-06 | MSME supplier? See your MSEFC option and your statutory interest before you decide. | MSME page | ✔ all | MSMED Act ss.15–18; NN-20 |
| C-07 | Settle a business dispute before insolvency papers are filed — or before they are admitted. | IBC page | ✔ all | Equator never decides insolvency (D2-02) |
| C-08 | Shareholder deadlock? Mediate the commercial terms; leave statutory reliefs to the NCLT. | COM corporate | ✔ all | R-COM-08 |
| C-09 | Separate with dignity. Agree the terms; the Family Court grants the divorce. | FAM hub | ✔ all | `law.divorce_court_only` |
| C-10 | One family tree, every heir, a clear schedule of who gets what. | Inheritance page | ✔ all | V3 §1.2 |
| C-11 | Children's arrangements are about the child — never a bargaining point. | FAM parenting | ✔ all | Brand never-say inverse |
| C-12 | Agree how the property is shared. Then sign on paper, stamp and register — we show you how. | Property page | ✔ all | NN-08 |
| C-13 | Claim rejected or cut? The Insurance Ombudsman is free. We help you use it on time. | INS hub | ✔ all | P-D06 |
| C-14 | For things an Ombudsman award can't fix — reinstatement, records, continuity — try mediation. | INS hub | ✔ all | V4 §2.3 L4 reliefs |
| C-15 | We never ask a policyholder to arbitrate. | INS hub | ✔ all | IRDAI circular 27 Oct 2023; master §5.2 |
| C-16 | Insurer-to-insurer disputes, settled privately. | INS B2B | ✔ all | — |
| C-17 | Your full and final, explained line by line. | WRK employee | ✔ all | Calculator is indicative; CoW wages basis |
| C-18 | Statutory dues are paid in full. Only the rest is negotiated. | WRK | ✔ all | HB-WRK-ARB-01; `STATUTORY_DUES_WAIVER_BLOCKED` |
| C-19 | Workplace conflict, handled privately and with respect. | Workplace mediation | ✔ all | — |
| C-20 | Sexual harassment complaints go to the Internal Committee. We give it the tools — never the decision. | POSH | ✔ all | NN-07; POSH Act 2013 |
| C-21 | Cross-border disputes, in your language, under the law you agreed. | INT hub | ✔ all | S9 §7.3 |
| C-22 | An award packaged for the New York Convention. | INT arbitration | ✔ all | Enforcement depends on the enforcing court; body says so |
| C-23 | Mediate across borders; record the settlement as a consent award where you need enforcement. | INT mediation | ✔ all | NN-19 (India has not ratified Singapore Convention) |
| C-24 | Published fees in US dollars, with the rupee equivalent shown. | INT fees | ✔ all | Card INT-USD; D7 |

### 2.5 Mechanisms (D)

| ID | Line | Page | Checks | Notes |
|---|---|---|---|---|
| D-01 | Negotiation: make and answer offers in writing, at your pace. | Negotiation | ✔ all | — |
| D-02 | Offers stay private until both sides agree. | Negotiation (blind-bid) | ✔ all | Blind-bid off where V1/V4 block it |
| D-03 | Conciliation: a neutral helps you agree; a signed settlement has the status of an arbitral award. | Conciliation | ✔ all | A&C ss.73–74 |
| D-04 | Without prejudice: what you propose can't be used against you later. | Conciliation | ✔ all | A&C s.81 |
| D-05 | Mediation: you decide. Nobody can force a settlement. | Mediation | ✔ all | `law.mediation_voluntary` |
| D-06 | Mediation sessions are not recorded. | Mediation | ✔ all | G: `conf.no_mediation_recording` |
| D-07 | A signed mediated settlement binds you both as a contract. | Mediation | ✔ all | `law.settlement_contract`; ss.27–28 note bound to flag |
| D-08 | Arbitration: a neutral arbitrator hears both sides and decides. | Arbitration | ✔ all | — |
| D-09 | Binding, enforceable arbitration — online. | Arbitration | ✔ all | `law.award_s36` in body incl. s.34 limit |
| D-10 | Arbitrators are appointed by Equator under published rules — never chosen by one side alone. | Arbitration | ✔ all | G: `ind.appointment_policy`; NN-03 exception for equal-footing B2B explained in body |
| D-11 | Try to agree first. If you can't, a different neutral decides. | Med-arb | ✔ all | Master §5.3 different neutral default |
| D-12 | Voluntary pre-suit mediation — before anyone files a case. | Pre-litigation | ✔ all | M-06; body states s.12A PIMS stays with the Legal Services Authority |
| D-13 | Mediation does not stop legal deadlines. We show you the dates to watch. | Pre-litigation, Explorer | ✔ all | K §1.3 |
| D-14 | An independent expert decides the number; you keep control of the rest. | Expert determination | ✔ all | Contractual, not an award |

### 2.6 Features and product (E)

| ID | Line | Surface | Checks | Notes |
|---|---|---|---|---|
| E-01 | Describe what happened. See your options in minutes. | Explorer | ✔ all | "minutes" unquantified; median claim only via metrics |
| E-02 | Information, not advice. Free, and you don't need to sign up. | Explorer | ✔ all | EP-01, EP-08 |
| E-03 | Start online. Save and come back any time. | Filing | ✔ all | WC-22 replacement |
| E-04 | Received a notice? Read it and give your side. | `/respond` | ✔ all | WC-43 |
| E-05 | Know where your matter stands — every step, date and document in one place. | `/track` | ✔ all | S9 §5.4 |
| E-06 | Our fees, in full, before you start. | `/fees` | ✔ all | — |
| E-07 | Sign online with Aadhaar eSign or DSC. Property deeds and wills still need paper. | e-sign band | ✔ all | WC-52; NN-08 |
| E-08 | Pay in instalments. Track every payment. | Settlement loop | ✔ all | Instalments via e-mandate (RBI E-mandate Framework 2026) |
| E-09 | Your language, your channel — web, WhatsApp, phone. | Languages | ✔ all | G: `lang.live` lists live locales only |
| E-10 | Draft your statement from your own documents. You approve every line. | AI Pleadings Studio | ✔ all | NN-25; same tool for both sides |
| E-11 | Published only if everyone agrees. Names removed. | `/decisions` | ✔ all | G: `pub.consent_only` |
| E-12 | Appoint a representative. Change or cancel their authority any time. | Representatives | ✔ all | G: `rep.loa_revocable` |

### 2.7 Audiences and products (F)

| ID | Line | Page | Checks | Notes |
|---|---|---|---|---|
| F-01 | Fair to your customers. Defensible to your regulator. | Enterprise H1 | ✔ all | Never beside RBI/IRDAI/SEBI names (S9 §7.4) |
| F-02 | Add Equator to your contracts and your grievance desk. | Enterprise | ✔ all | Replaces "Integrate your business, free" |
| F-03 | Plans that count what you use — never the outcome. | `/pricing/organisations` | ✔ all | X-07 |
| F-04 | Grievance desks with the regulator's clock built in. | GRM SaaS | ✔ all | "regulator's clock" = timelines in the rules; not endorsement |
| F-05 | Your Internal Committee, organised: sealed files, 90-day clocks, annual report. | POSH SaaS | ✔ all | POSH Act s.11(4), s.21 |
| F-06 | Resolve disputes. Build your practice. On your terms. | Become a Neutral | ✔ all | WC-42 |
| F-07 | Practise ADR, independently. | Private ADR Chambers | ✔ all | S9 keep |
| F-08 | Run your practice on Equator's case, payment and e-sign tools. | Chambers | ✔ all | Replaces "Equator Assurance" |
| F-09 | Graded on experience and assessment — not on who wins. | Grades | ✔ all | NN-28 |
| F-10 | You represent your client. We run a fair process. | Counsel | ✔ all | Replaces "You represent; we resolve" |
| F-11 | Choose your training. We assess the skill. | Training | ✔ all | D2-17 |
| F-12 | Focus on growth, not on disputes. | B2B ads only | ✔ all | S9 keep (B2B only) |

### 2.8 Rejected lines (do not reuse; linter seeds)

| Line (source) | Failing checks | Replacement |
|---|---|---|
| "The People's Court." (EQR-10) | LC-2 | A-01 |
| "Mediation Act 2023-compliant … settlements become binding decrees." (Playbook) | LC-3, LC-4 | WC-57 text |
| "From Conflict to Closure — In Days, Not Years." (Strategy) | LC-1, LC-7 | [HOLD] until a metrics claim exists |
| "File Your Dispute in Under 5 Minutes" (Strategy) | LC-1 | E-03 |
| "Where Justice Meets Technology" (Strategy) | LC-2 | A-10 |
| "Resolve loan disputes in 90 days" (Playbook) | LC-1, NN-20 | C-01 |
| "Silence means consent — speak up, now." (EQR-10) | LC-8, legally wrong (A&C s.25(b)) | E-04 |
| "Talk to a Resolution Expert Today →" (Strategy) | LC-5 | "Talk to our case team" |
| "Trusted by Leaders Across the Ecosystem" (live) | LC-7 | "Built for" |
| "Up to 80% saving on litigation cost" (EQR-10) | LC-1, LC-7 | "Fees published in advance · Hearings online · Free public forums explained first" |

---

## 3. Page-by-page copy deck (public website)

### 3.0 Sitewide elements and field rules

**Field rules (enforced by LINT-040–LINT-048, §8).** SEO title ≤ 60 characters, unique, pattern `{intent phrase} | Equator Resolution` (drop the suffix when the phrase needs the space; site name is supplied by `WebSite` markup). Meta description ≤ 155 characters, unique, contains no fee figure, no statistic and no promise. One H1 per page that matches the user's question or the page's single purpose. Hero one-liner ≤ 25 words. FAQs are **answer-first**: the first sentence answers yes/no/what in ≤ 25 words; the rest explains. Every legal page carries the review stamp "Last legally reviewed on {date} by {reviewer name}, {credential}" (FR-P13-09(c)).

**Header.** Navigation (FR-P13-03): Resolve · Disputes · For Organisations · Neutrals · Fees · Rules · Learn · About. Persistent actions: **Understand your options** (primary, → `/dispute-explorer`) · Respond to a notice · Track · language switcher (English · हिन्दी · others only when live) · **Log in** menu: Parties (`/login`) · Representatives and advocates (`/counsel/login`) · Mediators (`/mediator/login`) · Arbitrators (`/arbitrator/login`) · Organisations (`/enterprise/login`) · Private ADR Chambers (`/chambers/login`) · Partners (`/partners/login`) (App. S §2). Staff and committee portals are not linked publicly.

**Identity strip** (all vertical, subtype, mechanism and Explorer pages, directly under the hero): "Equator Resolution is a private dispute resolution institution — not a court, regulator or government body. We will tell you when a free public forum may suit you better." Hindi: "इक्वेटर रिज़ॉल्यूशन एक निजी विवाद समाधान संस्था है — न्यायालय, नियामक या सरकारी निकाय नहीं। यदि कोई निःशुल्क सार्वजनिक मंच आपके लिए बेहतर हो, तो हम आपको बताएँगे।"

**Footer** (config-driven, WC-47): brand line A-01 · "Equator Resolution is a brand of {{entity.legal_name}} (CIN {{entity.cin}}), registered office: {{entity.registered_office}}. Offices: {{entity.offices}}." · "Email: {{entity.email_general}} · Phone/WhatsApp: {{entity.phone}}" · "Grievance Officer: {{gro.name}}, {{gro.email}} · Data Protection Officer: {{dpo.name}}, {{dpo.email}}" · link groups (Resolve, Disputes, Organisations, Neutrals, Rules and policies, Trust, About, Legal) · "Part of the Infrabyx Group" (`id.group`) · "© {year} {{entity.legal_name}}". The build fails if CIN is missing (FR-P13-08).

**Reusable blocks.** `AnswerFirst` (§6.3) · `SignpostCard` (heading A-07; forum name, cost "Free", "Do I need a lawyer?", how to apply, last date to act from `{{rule:...}}`) · `WhoDecidesChip` ("You and the other side decide" / "The arbitrator decides") · `FeeTeaser` (fee tokens only) · `ReviewStamp` · `StatBand` (metrics-feed claims only; empty state: "We will publish our first statistics after {{metric:first_report_month}}, with the method we used.") · `TrustBand` (B-02, B-04, B-06 with claim gates; hidden per item until its claim is active).

### 3.1 Route and page index

| ID | Page | Route (en; Hindi under `/hi/…`) | Primary schema |
|---|---|---|---|
| P-01 | Home | `/` | Organization, WebSite |
| P-02 | How it works | `/how-it-works` | WebPage, BreadcrumbList |
| P-03 | Dispute Explorer landing | `/dispute-explorer` | WebPage, Service |
| P-04 – P-09 | Six vertical hubs | `/disputes/loans-and-finance` · `/disputes/business-and-commercial` · `/disputes/family-and-property` · `/disputes/insurance` · `/disputes/workplace` · `/disputes/international-commercial` (code aliases `/disputes/fin` etc. 301 to these) | Service, BreadcrumbList |
| P-10 – P-19 | Subtype landing pages | under each hub | Service, BreadcrumbList |
| P-20 | Respond to a notice | `/respond` | WebPage |
| P-21 – P-27 | Mechanism pages | `/mechanisms/{negotiation, conciliation, mediation, arbitration, med-arb, pre-litigation-mediation, expert-determination}` | Service, BreadcrumbList |
| P-28 – P-31 | Organisations hub, lenders, insurers, employers | `/for` · `/for/lenders` · `/for/insurers` · `/for/employers` | Service |
| P-32 – P-33 | GRM SaaS, POSH SaaS | `/grievance-redressal` · `/posh-internal-committee` | Service (+ SoftwareApplication) |
| P-34 | Private ADR Chambers | `/private-adr-chambers` | Service, SoftwareApplication |
| P-35 – P-36 | Find a Neutral, Become a Neutral | `/neutrals` (+ `/neutrals/{slug}`) · `/neutrals/join` | CollectionPage + Person; WebPage |
| P-37 | Training | `/training` (`/academy` 301) | WebPage (+ Course only for Equator's own modules) |
| P-38 – P-39 | Fees; pricing for organisations and professionals | `/fees` (+ `/fees/calculator`) · `/pricing/organisations` · `/pricing/professionals` | WebPage (+ OfferCatalog) |
| P-40 | Track your case | `/track` | WebPage |
| P-41 | Published awards and settlements | `/decisions` (+ `/decisions/{citation-slug}`; `/published-outcomes` 301) — App. R §3.9.1 | CollectionPage; CreativeWork per item |
| P-42 | Rules and Code of Conduct | `/rules` (+ `/rules/{ruleset}/{version}`) | WebPage; DigitalDocument |
| P-43 | Trust and security | `/trust` (+ sub-pages) | WebPage |
| P-44 | About and governance | `/about` · `/about/governance` · `/about/advisory-council` | AboutPage, Organization |
| P-45 | Contact | `/contact` | ContactPage |
| P-46 | Help Centre and FAQs | `/help` (+ `/help/{topic}`) | WebPage (FAQPage optional) |
| P-47 | Careers | `/careers` (+ `/careers/{id}`) | WebPage; JobPosting |
| P-48 | Legal pages | `/terms` · `/privacy` · `/cookies` · `/disclaimer` · `/grievance-officer` · `/accessibility` | WebPage |

---

### P-01 Home — `/`

| Field | Copy |
|---|---|
| SEO title | Online Mediation & Arbitration in India \| Equator Resolution |
| Meta description | Mediation, conciliation and arbitration for loan, insurance, workplace, family and business disputes in India. Fees published in advance. |
| Eyebrow | Resolve disputes, not relationships. |
| H1 | Resolve disputes online — fairly, quickly and enforceably. |
| Hero one-liner | Equator Resolution is a private dispute resolution institution for India. We are not a court, and we will tell you when a free public forum may suit you better. |
| Hindi hero | विवादों का समाधान ऑनलाइन — निष्पक्ष, शीघ्र और प्रवर्तनीय। |
| CTAs | Primary: **Understand your options — free** → `/dispute-explorer` · Secondary: **Received a notice? Respond** → `/respond` · Text link: "For organisations" → `/for` |
| Schema | `Organization` (sitewide: `name`, `legalName`, `identifier` CIN, `url` https://equatorresolution.in, `logo`, `slogan` = A-01, `description` = descriptor, `contactPoint` with `contactType` "customer support" and `availableLanguage`, `sameAs` owned profiles only, `parentOrganization` Infrabyx Group only if approved — §6.2) · `WebSite` (`name`, `url`, `inLanguage`) · optional `FAQPage` |
| Internal links | Six vertical hubs, `/how-it-works`, `/fees`, `/trust/how-we-stay-neutral`, `/for`, `/neutrals/join`, `/respond`, `/track` |

**Sections.**
1. **What happened?** (tiles; one line each) — *Loans, cards and payments:* "EMI, settlement, recovery calls, credit report." · *Business and contracts:* "Unpaid invoices, suppliers, partners, shareholders." · *Family, marriage and property:* "Divorce terms, maintenance, children, inheritance." · *Insurance claims:* "Rejected, cut or delayed claims." · *Job and workplace:* "Salary, full and final, gratuity, exit terms." · *Business across borders:* "Foreign buyers, sellers, partners and projects." Each tile → vertical hub; "Not sure? Describe it in your own words" → Explorer.
2. **Free public forums come first.** "{{claim:law.free_forums_exist}} Dispute Explorer shows you which one fits and the last date to use it — before it shows you anything we offer."
3. **How it works** (four steps). "1 Tell us what happened — free, no sign-up. 2 See your options, free forums first, with fees and dates. 3 Invite the other side, or respond to an invitation. 4 Agree terms with a mediator or conciliator, or receive an arbitrator's award — then sign, stamp and act on it." Link: "See every step" → `/how-it-works`.
4. **Ways to resolve.** Four cards with `WhoDecidesChip`: Negotiation ("You both decide, with or without a neutral"), Conciliation ("You both decide; a signed settlement has the status of an arbitral award"), Mediation ("You both decide; nobody can force a settlement"), Arbitration ("The arbitrator decides; the award is binding and enforceable, subject to limited court challenge").
5. **Our fees, in full, before you start.** "Dispute Explorer: free. A 30-minute process call: {{fee:ANC.CONSULT}}, credited if you file within 30 days. Individuals see the total including GST before paying." CTA "See all fees" → `/fees`. Banner while unapproved: "Fee schedule subject to Board approval."
6. **How we stay neutral.** B-04 · B-02 · B-06 · A-04 (each shown only when its claim is active). Link → `/trust/how-we-stay-neutral`.
7. **StatBand** (metrics feed only; honest empty state).
8. **For organisations.** F-01 + "Grievance desks, POSH tools, clause and API integration for lenders, insurers, employers, listed companies and universities." Links to P-29–P-33.
9. **For neutrals.** F-06 + "Join our panel, or run your own Private ADR Chambers on our platform. Appointments follow published rules." Links P-34, P-36.
10. **In your language.** E-09 with `{{locales_live}}`.

**FAQs.**
- *Is Equator Resolution a court?* No. It is a private dispute resolution institution run by {{entity.legal_name}}. Courts, ombudsmen and other public forums stay open to you, and we will say when one may suit you better.
- *Is Dispute Explorer free?* Yes. It explains the processes, free forums, documents, dates and fees that may apply. It does not assess your case or give legal advice.
- *Is a settlement reached through Equator binding?* Yes, once both of you sign it. A mediated settlement binds you as a contract; a conciliation settlement under section 73 of the Arbitration and Conciliation Act, 1996 has the status of an arbitral award (section 74). {{flag:mediation_act.s27.in_force → note}}
- *Do I need a lawyer?* Not for negotiation, mediation or conciliation. You may appoint an advocate or another representative at any stage, and you may want one in arbitration.
- *What will it cost?* Fees are published on our fees page. If you are an individual, you see the total including GST before you pay, and you can ask for a fee waiver.

---

### P-02 How it works — `/how-it-works`

| Field | Copy |
|---|---|
| SEO title | How Online Dispute Resolution Works \| Equator Resolution |
| Meta description | From describing your dispute to signing a settlement or receiving an award: each step, who decides, what it costs and what we never do. |
| H1 | How it works |
| Hero one-liner | Every step, who decides at each one, and what happens next — in plain words. |
| Hindi hero | यह कैसे काम करता है — हर चरण, हर निर्णय कौन लेता है, और आगे क्या होता है। |
| CTAs | Primary: **Understand your options — free** · Secondary: **See fees** |
| Schema | `WebPage`, `BreadcrumbList` (HowTo not emitted — P-D04) |
| Internal links | Mechanism pages P-21–P-27, `/fees`, `/rules`, `/track`, `/trust` |

**Sections.**
1. **Before anything is filed.** "Use Dispute Explorer to see free public forums, Equator's options, documents and dates to watch. Nothing is filed or sent until you choose." (AnswerFirst block.)
2. **Inviting the other side.** "We send a neutral invitation from Equator's case team — by email, WhatsApp, SMS and, for organisations, post. It says the process is voluntary, what it costs and which free forums exist. The other side can accept, ask questions, propose other dates or decline." Note: "Invitations do not stop any legal deadline."
3. **Choosing a neutral.** "Neutrals come from our panel under published allocation rules. In mediation the other side can choose from a shortlist. In arbitration Equator appoints, after conflict checks and written disclosures." Link → `/rules/appointment-policy`.
4. **Sessions and hearings** (table): Negotiation — structured offers online · Mediation and conciliation — joint and private sessions by video, phone or in person; not recorded · Arbitration — documents-only or hearings; recorded only if all parties and the tribunal agree.
5. **Outcomes.** Settlement agreement (contract) · Settlement under s.73 (status of an arbitral award, s.74) · Arbitral award (enforceable under s.36, subject to challenge under s.34) · Consent award (s.30) · No agreement: a closure note and your free-forum options again.
6. **Signing, stamping and registration.** "We help you sign online with Aadhaar eSign or a DSC and pay e-stamp duty for your state. Deeds that transfer or partition land or a house, wills and powers of attorney must be signed on paper, stamped and, where required, registered — we give you the checklist." (`law.property_registration`)
7. **After the outcome.** "Track payments and promised actions. If terms are not kept, we prepare an enforcement pack for you to take to court; we do not represent you in court."
8. **What we never do.** "We never decide whether your case is strong, predict a result or value your claim. We never act for either side. We never handle criminal matters." (NN-01, NN-24.)

**FAQs.**
- *Who decides the outcome?* In negotiation, conciliation and mediation, you and the other side decide. In arbitration, the arbitrator decides and the award binds both sides.
- *Can I stop midway?* Yes in mediation and conciliation; either side may end the process. In arbitration, the rules and the tribunal decide how the case continues.
- *Is anything recorded?* Mediation and conciliation sessions are not recorded. Arbitration hearings are recorded only with the consent of all parties and the tribunal.

---

### P-03 Dispute Explorer landing — `/dispute-explorer`

| Field | Copy |
|---|---|
| SEO title | Dispute Explorer: Understand Your Options Free \| Equator |
| Meta description | Answer a few questions to see free public forums, Equator's options, documents and dates to watch. Information, not legal advice. No sign-up. |
| H1 | Understand your options — free |
| Hero one-liner | Describe what happened. Dispute Explorer shows the processes and forums that may apply, the documents you'll need, dates to watch and our fees. |
| Hindi hero | अपने विकल्प समझें — निःशुल्क। |
| CTAs | Primary: **Start** → Explorer (SCR-P02-01) · Secondary: **I received a notice** → `/respond` · Tertiary: "Ask a person about the process" (free call-back, 10 minutes, 08:00–19:00) |
| Schema | `WebPage`, `Service` (`serviceType` "Dispute information tool", `offers.price` 0, `provider` Organization) |
| Internal links | Six hubs, `/help`, `/privacy`, `/letters-library`, `/fees` |

**Sections.**
1. **What you'll get** — "A Readiness & Pathway Report: what you told us · help now (if anyone is unsafe) · free and statutory options first, each with its last date · what Equator can and cannot do · documents checklist · how it would work · cost including GST · your next step." (K §4.2)
2. **What it won't do** — "It does not say whether your case is strong, predict what a forum will decide, or estimate what your claim is worth. It does not file or send anything for you."
3. **Your privacy** — "No account or ID needed to see your options. Save and come back with a link and code. Delete your answers at any time. On family and workplace topics, a 'Leave this page' button is always visible."
4. **If you are helping someone** — "Family members, advocates, HR or union representatives and CAs/CSs can use the Explorer. To act for someone, you will need their signed letter of authority (or vakalatnama for advocates)."
5. **If someone is in danger** — "If anyone is in danger now, call 112. For a cyber fraud in progress, call 1930. The Explorer will show these first if you tell us something is urgent."

**FAQs.**
- *Is this legal advice?* No. It is information about processes, forums, dates and fees. For advice on the merits, speak to your own advocate.
- *Will the other side see my answers?* No. Your answers stay private unless you choose to share a summary or file a case.
- *Does using the Explorer stop any deadline?* No. Legal deadlines keep running; the report shows the dates to watch.
- *Can I use it in Hindi?* Yes. Choose हिन्दी at the top of any page; other Indian languages are added as they go live.

---

### Vertical hub template (P-04 – P-09; FR-P13-04 order is mandatory)

1 Hero + identity strip → 2 **Free and statutory options first** (SignpostCards, last date from the register) → 3 What Equator can do (route cards with `WhoDecidesChip`) → 4 What Equator cannot do (plain reasons) → 5 How it works here (stage list from Appendix A) → 6 Fees (tokens) → 7 Documents you will usually need → 8 Popular topics (subtype links) → 9 FAQs → 10 CTA to Explorer → ReviewStamp. Schema: `Service` (`serviceType`, `provider` → Organization `@id`, `areaServed` "IN" (INT: worldwide B2B), `availableChannel` online) + `BreadcrumbList`; optional `FAQPage`.

### P-04 Loans, cards and payments (FIN) — `/disputes/loans-and-finance`

| Field | Copy |
|---|---|
| SEO title | Loan, Credit Card & Payment Disputes \| Equator Resolution |
| Meta description | Loan settlement, charges, recovery conduct and payment disputes: see free RBI routes first, then conciliation or mediation with a neutral. |
| H1 | Loan, card and payment disputes |
| Hero one-liner | Loan dispute? Start with your lender's grievance desk — then talk it through with a neutral. |
| Hindi hero | ऋण विवाद? पहले अपने ऋणदाता की शिकायत डेस्क से शुरू करें — फिर किसी तटस्थ व्यक्ति के साथ बात करें। |
| CTAs | **Understand your options — free** · **Received a notice from Equator? Respond** · For lenders → P-29 |
| Schema / links | `Service` (`serviceType` "Loan and payment dispute conciliation and mediation") · links P-12, P-21–P-24, `/fees`, `/for/lenders`, `/letters-library` |

**Free and statutory options first.** (1) *Your lender's grievance officer* — free; complain in writing and keep the reference. (2) *RBI Ombudsman* — {{claim:law.rbios_window}} (3) *Failed transactions and unauthorised debits* — your bank must reverse or compensate within RBI-set timelines (WC-13 text). (4) *Credit report errors* — dispute with the lender and the credit bureau; compensation applies if they miss the deadline (RBI/2023-24/72). (5) *Lok Adalat* through your District Legal Services Authority — free. (6) *Fraud or threats* — call 1930 or report at cybercrime.gov.in; in danger, call 112.

**What Equator can do.** "Negotiation with written offers · Conciliation under Part III of the Arbitration and Conciliation Act, 1996 — a signed settlement has the status of an arbitral award · Mediation · Arbitration only where your agreement allows it and the arbitrator is appointed independently by Equator · Civil settlement in cheque-bounce cases, with papers for the court to decide on compounding · One-time settlements with release of documents, NOC and credit-report updates tracked to completion."

**What Equator cannot do.** "We are not a recovery agent or collection agency. We do not decide SARFAESI or DRT matters, fraud or wilful-defaulter classification, or anything criminal. We do not offer arbitration where the lender alone chose the arbitrator, for bank or financial-institution claims of ₹20 lakh or more, or for microfinance loans."

**Contact conduct note.** "If we call you about a loan matter, we call only between 8 am and 7 pm, tell you the call is recorded, give you the lender's grievance-officer details, and stop if you ask."

**Popular topics.** Loan settlement (OTS) · credit cards · loan apps · gold loans · vehicle loans · home loans · MSME loans · microfinance · recovery-agent calls · cheque bounce · credit report · stuck UPI or bank transfer.

**FAQs.**
- *Will Equator collect money for my lender?* No. Equator is neutral. Settlement money goes directly to the lender or to a bank escrow, never through Equator's account.
- *Can my lender choose the arbitrator?* No. A clause letting one side alone pick the arbitrator is not valid for appointments (*CORE v ECI-SPIC-SMO-MCML*, Supreme Court, 8 Nov 2024). Equator appoints from its panel under published rules.
- *Do I pay if my lender invited me?* Not under a lender programme. The lender pays Equator's fees and they are never added to your dues.
- *I'm getting threatening recovery calls. Can you help?* Yes, as a grievance — but call 112 if you are in danger. Complain to the lender's grievance officer; if unresolved, the RBI Ombudsman is free.

### P-05 Business and commercial (COM) — `/disputes/business-and-commercial`

| Field | Copy |
|---|---|
| SEO title | Commercial Mediation & Arbitration \| Equator Resolution |
| Meta description | Unpaid invoices, supply, construction, technology, partnership and shareholder disputes: conciliation, mediation and institutional arbitration. |
| H1 | Business and commercial disputes |
| Hero one-liner | Resolve business disputes online — fairly, quickly and enforceably. |
| Hindi hero | व्यावसायिक विवादों का समाधान ऑनलाइन — निष्पक्ष, शीघ्र और प्रवर्तनीय। |
| CTAs | **Understand your options — free** · **Get a dispute clause** → `/clause-generator` · **Talk to our case team** |
| Schema / links | `Service` ("Commercial mediation, conciliation and arbitration") · P-14, P-15, P-21–P-27, `/rules`, `/fees`, `/clause-generator` |

**Free and statutory options first.** "Commercial suits of ₹3 lakh or more that do not need urgent interim relief must first go through pre-institution mediation under section 12A of the Commercial Courts Act, 2015, conducted by the Legal Services Authority. We can help you prepare that application." (WC-59) · MSE suppliers: the MSE Facilitation Council through the MSME ODR portal · Homebuyers: RERA authority and Consumer Commission · Insolvency: NCLT · Competition: CCI · Government contracts: the department's dispute committee (Department of Expenditure guidelines, 3 Jun 2024).

**What Equator can do.** "Negotiation · Conciliation under Part III (a signed settlement has the status of an arbitral award) · Voluntary pre-suit mediation · Institutional arbitration — standard, expedited, documents-only, emergency arbitrator and an optional appeal tier · Med-arb with a different neutral by default · Expert determination of accounts, measurements and SLA metrics · Settlement support before insolvency proceedings · Civil settlement in cheque-bounce cases."

**What Equator cannot do.** "Decide insolvency, oppression or mismanagement reliefs, IP validity or registration, competition matters, regulatory penalties or consumer complaints. Conduct the statutory section 12A pre-institution mediation (only the Legal Services Authority can, as the law stands)."

**Appointments note.** "Between businesses dealing on equal terms, each side may nominate one co-arbitrator, subject to disclosure, conflict checks and confirmation by Equator's Appointments Committee. The presiding or sole arbitrator is always appointed by Equator."

**FAQs.**
- *Does mediation at Equator satisfy section 12A of the Commercial Courts Act?* No. As the law stands, only the Legal Services Authority conducts section 12A pre-institution mediation. Equator's mediation is voluntary and does not replace that step.
- *Can we name Equator in our contracts?* Yes. Use the free clause generator to choose a ladder (negotiation, mediation, arbitration), seat, language and tribunal size.
- *Is an Equator award enforceable?* {{claim:law.award_s36}}
- *Can a government body be the other side?* Yes. Government contracts usually require the department's own dispute committee first, and arbitration is normally used only below ₹10 crore.

### P-06 Family, marriage and family property (FAM) — `/disputes/family-and-property`

| Field | Copy |
|---|---|
| SEO title | Family Mediation: Divorce Terms, Property & Inheritance |
| Meta description | Mediation for separating couples and families: maintenance, children, streedhan, partition and inheritance. Only a court grants a divorce. |
| H1 | Mediation for separating couples and families — private and respectful |
| Hero one-liner | Agree on maintenance, children's arrangements, stridhan and property with a trained mediator, online and in your language, including from abroad. |
| Hindi hero | अलग हो रहे दंपतियों और परिवारों के लिए मध्यस्थता — गोपनीय और सम्मानजनक। |
| CTAs | **Understand your options — free** · **Leave this page** (QuickExit, always visible) |
| Schema / links | `Service` ("Family mediation") · P-10, P-11, P-23, `/fees`, `/help/safety` |

**Safety first (above the fold).** "If you are not safe, call 112 or the Women Helpline 181. We screen every family matter before any joint session. Where there has been violence, we do not hold joint sessions; mediation goes ahead only if the person affected asks for it, with separate rooms." (V3 §1.3; PWDV Rules r.14.)

**Free and statutory options first.** Family Court counselling and its mediation centre · District Legal Services Authority (free legal aid, Lok Adalat) · Protection Officer under the Protection of Women from Domestic Violence Act, 2005 · Maintenance Tribunal for parents and senior citizens (Senior Citizens Act, 2007).

**What Equator can do.** "Mutual-consent divorce terms under your personal law · maintenance · parenting plans · streedhan and mahr · the shared home and joint loans · inheritance among heirs for every community · HUF partition and family settlements · separating a family business · care and maintenance of parents · arbitration only for property and partition rights."

**What Equator cannot do.** "Grant a divorce, decide custody or guardianship, decide whether a will is valid, or deal with any criminal matter, including dowry offences and instant triple talaq. Where a criminal case is pending, we help with civil terms only; the court alone decides on that case."

**How property terms take effect.** {{claim:law.property_registration}} "We give you the checklist and help you book the sub-registrar appointment."

**FAQs.**
- *Can Equator grant a divorce?* No. {{claim:law.divorce_court_only}} We help you agree the terms you then file with the Family Court.
- *Do I have to tell you my religion?* No. We ask which law your marriage was registered under, or the law that applied to the person who died, and explain why.
- *Can a pending criminal case be settled through Equator?* Only the civil terms. Whether a criminal case ends is for the court alone, and no payment can be made conditional on withdrawing a complaint except as the law permits.
- *Is it confidential?* Yes. Family matters are never published, sessions are not recorded and messages to your phone never mention the subject.

### P-07 Insurance (INS) — `/disputes/insurance`

| Field | Copy |
|---|---|
| SEO title | Insurance Claim Rejected or Cut? Your Options \| Equator |
| Meta description | Health, motor, life and property claim disputes: insurer's grievance desk and the free Insurance Ombudsman first, then mediation if it helps. |
| H1 | Insurance claim disputes |
| Hero one-liner | Claim rejected or cut? The Insurance Ombudsman is free. We help you use it on time — and mediate what an award can't reach. |
| Hindi hero | दावा अस्वीकार हुआ या कम मिला? बीमा लोकपाल निःशुल्क है। हम समय पर उसका उपयोग करने में मदद करते हैं। |
| CTAs | **Understand your options — free** · **Get your free Ombudsman pack** · For insurers → P-30 |
| Schema / links | `Service` ("Insurance claim mediation") · P-13, P-23, `/for/insurers`, `/fees` |

**Free and statutory options first.** (1) Insurer's grievance officer — complain in writing. (2) Bima Bharosa, IRDAI's grievance portal. (3) Insurance Ombudsman — free, no lawyer needed; awards up to {{rule:LR-IRDAI-003.award_cap}}; generally within one year of the insurer's final reply (late complaints can ask for condonation). (4) Consumer Commission through e-Jagriti. (5) Motor accident injury or death claims: only the Motor Accidents Claims Tribunal. (6) Crop insurance: Krishi Rakshak helpline 14447. (7) PM-JAY: helpline 14555.

**What Equator can do.** "Prepare your Ombudsman complaint pack free · mediation with an insurer officer whose authority to settle is confirmed in writing · outcomes an award can't easily deliver: reinstatement with continuity, correction of records, withdrawal of an adverse remark · deadline tracking so you don't lose the Ombudsman, Consumer Commission or tribunal window · for businesses and insurers: commercial mediation, quantum-only arbitration and surveyor expert determination."

**What Equator never does.** "Ask a policyholder to arbitrate · charge a percentage of your claim · deal with alleged insurance fraud or third-party motor accident claims."

**FAQs.**
- *Is the Insurance Ombudsman free?* Yes. You don't need a lawyer, and you can go there whether or not you use Equator.
- *Can my insurer make me go to arbitration?* No. Retail general insurance policies no longer carry arbitration clauses (IRDAI circular of 27 Oct 2023), and Equator never offers arbitration to individual policyholders.
- *Do you take a share of my claim?* No. Our fees are flat and published. If your insurer referred you, you pay nothing.
- *Will my health details be shared?* No. Health data is kept in a sealed store, seen only by people in your case, and never used for analytics.

### P-08 Workplace and employment (WRK) — `/disputes/workplace`

| Field | Copy |
|---|---|
| SEO title | Workplace & Employment Disputes \| Equator Resolution |
| Meta description | Salary, full and final, gratuity, exit terms and workplace conflict: statutory routes shown first; statutory dues are never negotiated away. |
| H1 | Workplace and employment disputes |
| Hero one-liner | Resolve work disputes privately — with your statutory rights intact. |
| Hindi hero | काम से जुड़े विवाद गोपनीय रूप से सुलझाएँ — आपके वैधानिक अधिकार सुरक्षित रहते हैं। |
| CTAs | **Understand your options — free** · **Check your full and final** (calculator) · For employers → P-31 |
| Schema / links | `Service` ("Employment mediation and conciliation") · P-18, P-19, P-21–P-24, `/tools/full-and-final` |

**Free and statutory options first.** Your employer's Grievance Redressal Committee (establishments with 20 or more workers, Industrial Relations Code, 2020 s.4) · Conciliation officer · Wage claims authority under the Code on Wages, 2019 s.45 (claims within 3 years) · Gratuity controlling authority · EPFiGMS for provident fund · ESIC grievance · Internal or Local Committee for sexual harassment · State gig-worker boards where notified.

**What Equator can do.** "Negotiation · mediation · conciliation under Part III · a draft settlement memorandum for signature before the conciliation officer (for workers under the Industrial Relations Code) · facilitated team-conflict conversations · arbitration only for contractual claims of managers, executives and founders, where there is a valid agreement."

**What Equator never does.** "Negotiate away statutory dues — wages, gratuity, PF, bonus and minimum wage are paid in full · arbitrate a worker's termination or an industrial dispute · handle a sexual harassment complaint as an ordinary case · agree terms that stop someone reporting wrongdoing."

**FAQs.**
- *Can a settlement reduce my gratuity or PF?* No. Statutory dues are paid in full. Only other amounts, such as notice pay or a severance package, are negotiated.
- *When must full and final be paid?* Within two working days of leaving, under section 17(2) of the Code on Wages, 2019. Our calculator shows an indicative breakdown; it is not advice.
- *My contract has an arbitration clause. Will Equator arbitrate my termination?* Not if you are a "worker" under the Industrial Relations Code. Equator offers arbitration only for contractual claims of managers and executives.
- *Will my employer know I used Dispute Explorer?* No. Nothing is shared until you choose to invite them.

### P-09 International commercial (INT) — `/disputes/international-commercial`

| Field | Copy |
|---|---|
| SEO title | International Commercial Arbitration & Mediation \| Equator |
| Meta description | Cross-border commercial arbitration and mediation administered from India: published USD fees, independent appointments, enforcement-ready awards. |
| H1 | International commercial disputes |
| Hero one-liner | Cross-border disputes, in your language, under the law you agreed. |
| Hindi hero | सीमा-पार वाणिज्यिक विवाद — आपकी भाषा में, उस कानून के तहत जिस पर आपने सहमति दी। |
| CTAs | **Start an international case** · **See USD fees** · **Get a model clause** |
| Schema / links | `Service` (`areaServed` worldwide; `serviceType` "International commercial arbitration and mediation") · P-16, P-17, `/fees?currency=USD`, `/rules` |

**Scope.** "Business-to-business disputes only: sale of goods, services, distribution, JVs and shareholder agreements, technology licensing, construction and EPC, shipping, trade finance, energy and private investment agreements. We do not handle investor-state, WTO or consumer disputes."

**What Equator can do.** "Administer arbitration seated in India (including GIFT City IFSC as an Indian seat) or abroad · international mediation · med-arb and arb-med-arb with a consent award · expert determination · emergency arbitrator · time-zone-fair hearings with interpretation · invoices in USD, EUR, GBP, SGD or AED with the rupee equivalent shown."

**Enforcement, honestly.** {{claim:law.singapore_status}} "Awards are prepared for the New York Convention. Whether a foreign award can be enforced in India depends on the Government's reciprocity notifications — for example, the UAE is not a notified territory for foreign awards. We check the enforcement country with you at the start."

**Appointments.** "Where the parties are of different nationalities, the sole or presiding arbitrator is by default of a neutral nationality. Each side may nominate a co-arbitrator in equal-footing disputes, subject to disclosure and confirmation."

**FAQs.**
- *Can a mediated settlement be enforced in India under the Singapore Convention?* No. India has signed but not ratified it. Record the settlement as a consent arbitral award for enforcement under the New York Convention.
- *Can we choose GIFT City as the seat?* Yes. An arbitration seated in GIFT City IFSC is an Indian-seated arbitration under Part I of the Arbitration and Conciliation Act, 1996. No dedicated arbitration institution for the IFSC has been established as of {{rule:LR-INT-021.status_date}}.
- *Can foreign lawyers appear?* Yes, within Bar Council of India rules (as amended 13 May 2025): on foreign or international law, for clients whose principal office is abroad.
- *Which law applies?* The law in your contract. India is not a party to the CISG, so it applies only if you chose it or the governing law brings it in.

---

### Subtype landing template (P-10 – P-19)

Hero + identity strip → AnswerFirst block (question H1 or topic H1, ≤ 2-sentence answer naming the free forum first) → key-facts table (deadlines, forum, documents — from the register) → how Equator helps → what Equator cannot do → documents → fees → FAQs → CTA (Explorer pre-filled with the vertical and L1) → ReviewStamp. Each page must have ≥ 250 words of unique, legally reviewed copy (FR-P13-12 rule applied to hand-written pages too). Schema: `Service` + `BreadcrumbList` (Home › Disputes › Hub › Page).

### P-10 Inheritance and family property — `/disputes/family-and-property/inheritance-and-family-property`

| Field | Copy |
|---|---|
| SEO title | Inheritance & Family Property Mediation \| Equator Resolution |
| Meta description | Heirs and co-owners: agree how family property and estates are shared, under the law that applies to your family. Deeds stamped and registered. |
| H1 | Inheritance and family property |
| Hero one-liner | One family tree, every heir, a clear schedule of who gets what — then the right deed, stamped and registered. |
| Hindi hero | एक पारिवारिक वृक्ष, हर उत्तराधिकारी, किसे क्या मिलेगा — इसकी स्पष्ट सूची; फिर सही विलेख, स्टाम्प और पंजीकरण के साथ। |
| CTAs | **Understand your options — free** · **Invite family members** |

**Sections.** *Who it is for:* siblings, widows, coparceners and the karta, legal heirs including NRIs and OCIs, co-owners. *How shares are worked out:* "We identify the law that applied to the person who died — by their community, the way their marriage was registered and where the property is — and show an indicative share table from a published calculator. The table is information, not a decision; the family agrees the final schedule." *Daughters:* "Under the Hindu Succession Act, 1956 as amended in 2005, a daughter is a coparcener by birth with the same rights as a son (*Vineeta Sharma v Rakesh Sharma*, (2020) 9 SCC 1)." *What we cannot decide:* "Whether a will is valid, probate and letters of administration go to the court. Succession certificates are issued by the District Judge and legal-heir certificates by the revenue office. Families can, instead of contesting a will, agree a family settlement through mediation." *Making it legal:* "{{claim:law.property_registration}} A partition deed for immovable property is compulsorily registrable (Registration Act, 1908 s.17(1)(b)) and must be presented within four months of signing (s.23). A memorandum recording a family arrangement already made may not need registration (*Kale v Deputy Director of Consolidation*, (1976) 3 SCC 119) — the sub-registrar or your advocate will confirm." *Documents:* death certificate, family tree, title documents, property tax records, bank and demat statements, any will, existing court papers. *Fees:* registration {{fee:FAM-STD.PROPERTY.REG}}; administration by declared value {{fee:FAM-STD.PROPERTY.ADMIN}}; registration-route help {{fee:ANC.REGN.FACIL}}.

**FAQs.**
- *Do all heirs have to take part?* For a settlement that binds everyone, yes. Any heir who does not sign is not bound, so we help you identify and invite every heir.
- *Can we avoid a court case over a will?* Often, yes, if everyone agrees a family settlement. Whether the will itself is valid remains a question only a court can decide.
- *Can family members abroad take part?* Yes. Sessions are online across time zones; deeds may need signing before an Indian consulate or a notary with apostille, then stamping and registration in India.

### P-11 Mutual-consent divorce terms — `/disputes/family-and-property/mutual-consent-divorce-terms`

| Field | Copy |
|---|---|
| SEO title | Mutual Consent Divorce: Agree the Terms \| Equator Resolution |
| Meta description | Agree maintenance, children, streedhan and property for a joint divorce petition. We help with the terms; the Family Court grants the divorce. |
| H1 | Mutual-consent divorce: settlement terms |
| Hero one-liner | We help you agree the terms for a joint petition. How long mediation takes depends on you; the court process then follows its own timeline. |
| Hindi hero | आपसी सहमति से तलाक: समझौता शर्तें। |
| CTAs | **Understand your options — free** · **Leave this page** |

**Sections.** *Steps (WC-36):* "1 Tell us about your situation (free). 2 Both of you agree to mediate. 3 Online sessions with a trained mediator. 4 Settlement terms drafted and signed. 5 Next, in court: file the joint petition with the Family Court, which decides on the decree." *What the terms cover:* maintenance or a one-time amount, children's residence and contact (subject to the court's approval in the child's best interests), streedhan and gifts, the shared home and loans, withdrawal of pending civil cases. *The law, briefly:* "Under section 13B of the Hindu Marriage Act, 1955 you must have lived separately for at least a year; the court may waive the further six-month period in suitable cases (*Amardeep Singh v Harveen Kaur*, (2017) 8 SCC 746). Similar routes exist under the Special Marriage Act, 1954 (s.28), the Divorce Act, 1869 (s.10A) and the Parsi Marriage and Divorce Act, 1936 (s.32B); khula and mubarat follow Muslim personal law." *Safety:* screening before any joint session. *Fees:* {{fee:FAM-STD.MUTUAL.REG}} + {{fee:FAM-STD.MUTUAL.ADMIN}}, shared equally unless you agree otherwise.

**FAQs.**
- *How long will it take?* It depends on how quickly you both agree. The court then applies its own statutory periods before granting the divorce.
- *Can we sign online?* Yes for the settlement terms, using Aadhaar eSign or DSC. Any transfer of a house or land needs a paper deed, stamping and registration, and the petition is filed under the court's own rules.
- *What if one of us lives abroad?* Sessions are online. The court decides how the person abroad appears for the petition.

### P-12 Loan settlement (OTS) — `/disputes/loans-and-finance/loan-settlement-ots`

| Field | Copy |
|---|---|
| SEO title | Loan Settlement (OTS): Agree Terms in Writing \| Equator |
| Meta description | Negotiate a one-time settlement with your lender through a neutral conciliator. Written terms, NOC and credit-report updates tracked to the end. |
| H1 | Loan settlement (one-time settlement) |
| Hero one-liner | Settle your loan in writing — with release of documents and credit-report updates tracked to the end. |
| Hindi hero | अपने ऋण का समझौता लिखित में करें — दस्तावेज़ वापसी और क्रेडिट रिपोर्ट अपडेट अंत तक ट्रैक किए जाते हैं। |
| CTAs | **Understand your options — free** · **Start a settlement request** |

**Sections.** *Before you start:* "A settlement is not a right. Your lender decides under its Board-approved policy. What we offer is a neutral, written process." *How it works:* "1 Make or answer an offer in writing. 2 If needed, a neutral conciliator helps you both. 3 Signed settlement under section 73 of the Arbitration and Conciliation Act, 1996 — it has the status of an arbitral award. 4 Pay in one go or instalments (bank e-mandate; your bank notifies you at least 24 hours before each debit). 5 We track the NOC, release of documents and the credit-report update." *What a good settlement states:* amount and dates, what happens to charges and interest, NOC date, return of documents or collateral, how the credit report will be updated, and what happens if a payment is missed. *Release of documents:* "For loans covered by RBI's 13 Sep 2023 directions, the lender must release property documents within 30 days of full repayment or settlement, or pay compensation for each day of delay." *Fees:* "Under a lender programme you pay nothing. Otherwise: {{fee:FIN-R.F1}} registration, and administration by amount — total including GST shown before payment."

**FAQs.**
- *Will a settlement affect my credit report?* It can. Lenders often report a settled loan as "settled" rather than "closed". Ask your lender in writing how it will report before you sign.
- *Can I pay in instalments?* Yes, if your lender agrees. Instalments are collected by bank e-mandate or payment link, never through Equator's account.
- *Is the settlement binding on the lender?* Yes, once both sides sign. A conciliation settlement has the status of an arbitral award (section 74).

### P-13 Health insurance claim rejected — `/disputes/insurance/health-claim-rejected`

| Field | Copy |
|---|---|
| SEO title | Health Insurance Claim Rejected? Free Routes First \| Equator |
| Meta description | Cashless denied, claim rejected or deducted? Complain to the insurer, then the free Insurance Ombudsman. Mediation for what an award can't fix. |
| H1 | Health insurance claim rejected or cut |
| Hero one-liner | See your free options and dates first. Use mediation only if it helps. |
| Hindi hero | स्वास्थ्य बीमा दावा अस्वीकार हुआ या कटौती हुई? पहले निःशुल्क रास्ते देखें। |
| CTAs | **Get your free complaint pack** · **Understand your options — free** |

**Sections.** *In hospital now?* "Ask the hospital's insurance desk to escalate the cashless request to the TPA and insurer at once, and get any denial in writing. Do not delay treatment; you can claim reimbursement later." *Common reasons insurers give:* non-disclosure at proposal, pre-existing disease or waiting period, exclusions, proportionate deductions and non-payable items, late intimation, incomplete documents. "After continuous cover for the moratorium period set by IRDAI ({{rule:LR-IRDAI-005.moratorium_months}} months), a claim cannot be contested for non-disclosure except for proven fraud." *Your free route:* insurer's grievance officer → Bima Bharosa → Insurance Ombudsman (free; within one year of the insurer's final reply) → Consumer Commission. *Free self-help pack:* representation letter, ground-by-ground schedule, line-item deduction table — you send it; we never send it for you. *Where mediation helps:* reinstatement with continuity, correction of records, a written explanation, a structured payment. *Privacy:* health data sealed (NN-07).

**FAQs.**
- *Is there a time limit for the Insurance Ombudsman?* Generally one year from the insurer's final reply. If you are late, you can ask the Ombudsman to condone the delay.
- *Does using Equator stop the Ombudsman deadline?* No. We show the date and remind you; you can go to the Ombudsman at any time.
- *What does mediation cost?* A flat fee by claim amount, shown including GST before you pay: {{fee:INS-RET.I3}}. If your insurer referred you, you pay nothing.

### P-14 Unpaid invoices and MSME delayed payments — `/disputes/business-and-commercial/unpaid-invoices-msme`

| Field | Copy |
|---|---|
| SEO title | Unpaid Invoices & MSME Delayed Payments \| Equator Resolution |
| Meta description | MSE supplier with unpaid invoices? See your Facilitation Council option and statutory interest first, then negotiate or conciliate with the buyer. |
| H1 | Unpaid invoices and MSME delayed payments |
| Hero one-liner | MSME supplier? See your MSEFC option and your statutory interest before you decide. |
| Hindi hero | बकाया बिल? पहले बात करें। समझौता लिखित में करें। |
| CTAs | **Calculate statutory interest** → `/tools/msme-interest` · **Understand your options — free** |

**Sections.** *Your statutory position:* "Under the MSMED Act, 2006, a buyer must pay a micro or small supplier by the agreed date, and never later than 45 days after accepting the goods or services (s.15). Late payment carries compound interest with monthly rests at three times the RBI bank rate (s.16) — currently {{rule:LR-MSME-016.rate_pct}}% a year." *The free statutory route:* "File with the MSE Facilitation Council through the MSME ODR portal (s.18)." *Equator's route:* "Negotiation with the full statutory interest shown to both sides, then conciliation under Part III before any Council reference. Flat fee {{fee:COM-STD.C10}}. If it doesn't settle, we prepare your MSME ODR pack free." *Not a micro or small enterprise?* Use the commercial route (P-05). *Changes coming:* {{flag:com.msefc_referral_msp → "The MSMED (Amendment) Act, 2026 lets Facilitation Councils refer matters to mediation providers once the relevant provisions commence. We will update this page when they do."}}

**FAQs.**
- *Do I need Udyam registration?* The Facilitation Council route is for micro and small enterprises registered on Udyam. When your registration took effect can matter; check it before you file.
- *Can the buyer be a government company?* Yes. The same statutory interest applies, and government buyers often follow their own dispute committee process.
- *Does conciliation stop me going to the Council later?* No. You can file with the Council if conciliation does not settle the matter.

### P-15 Pre-insolvency (IBC) settlement — `/disputes/business-and-commercial/pre-insolvency-settlement`

| Field | Copy |
|---|---|
| SEO title | Pre-Insolvency (IBC) Settlement Mediation \| Equator |
| Meta description | Creditor–debtor settlement before or during IBC proceedings: mediation, withdrawal-window support and pre-pack facilitation. The NCLT decides. |
| H1 | Settlement before and during insolvency proceedings |
| Hero one-liner | Settle a business debt before insolvency papers are filed — or before they are admitted. |
| Hindi hero | दिवाला कार्यवाही से पहले और उसके दौरान समझौता। |
| CTAs | **Talk to our case team** · **Understand your options — free** |

**Sections.** *Before filing:* "Default must be at least ₹1 crore for a creditor to start insolvency against a company. A short mediation after a demand notice can settle dues with instalments and a revival clause." *Filed, not yet admitted:* "Parties can settle and ask the NCLT to allow withdrawal." *After admission:* "Under section 12A of the IBC as amended in 2026, withdrawal is possible only after the Committee of Creditors is formed and before the first invitation for resolution plans, with 90% of the Committee's vote; the NCLT then decides. We prepare the settlement and the Committee pack through the resolution professional." *MSME pre-packs:* facilitated talks with unrelated financial creditors before a pre-packaged insolvency filing (default of at least ₹10 lakh). *Personal guarantors:* settlement before an application under sections 94–95. *What we never do:* "Decide admission, claims or any insolvency matter — that is the NCLT's role. We do not offer arbitration once insolvency is admitted."

**FAQs.**
- *Can Equator stop an insolvency case?* No. Only the NCLT can allow withdrawal or close the case. We help the parties reach and document a settlement.
- *Is mediation compulsory before an insolvency filing?* No. A pre-filing mediation proposal has been discussed by the IBBI, but no regulation requires it as of {{rule:LR-IBC-009.status_date}}.
- *Who can take part after admission?* The corporate debtor or promoter, the applicant creditor and, through the resolution professional, the Committee of Creditors.

### P-16 International arbitration — `/disputes/international-commercial/international-arbitration`

| Field | Copy |
|---|---|
| SEO title | International Arbitration Administered from India \| Equator |
| Meta description | India-seated or foreign-seated commercial arbitration with published USD fees, neutral-nationality appointments and New York Convention-ready awards. |
| H1 | International commercial arbitration |
| Hero one-liner | An award packaged for the New York Convention, from a published USD fee schedule and independent appointments. |
| Hindi hero | अंतरराष्ट्रीय वाणिज्यिक माध्यस्थम् — प्रकाशित शुल्क और स्वतंत्र नियुक्तियों के साथ। |
| CTAs | **Start an international case** · **Get the model clause** · **See USD fees** |

**Sections.** *Tracks:* streamlined documents-only (smaller claims), expedited, standard, emergency arbitrator before the tribunal is formed, optional internal appeal tier by agreement. *Seat:* "Your agreement decides. For an India-seated international commercial arbitration, Indian courts supervise under Part I of the Arbitration and Conciliation Act, 1996." *Appointments:* Appointments Committee; neutral nationality default; disclosures under the IBA Guidelines on Conflicts of Interest 2024. *Before registration:* sanctions screening, KYC and beneficial ownership, data-transfer basis and payment route — "so that fees and awards can be paid through banks." *Fees:* registration {{fee:INT-USD.I1}}, administration {{fee:INT-USD.I2}}, arbitrator scale {{fee:INT-USD.I3}}, INR equivalent shown.

**FAQs.**
- *Can hearings be fully online?* Yes. We schedule fairly across time zones and provide interpretation channels and electronic bundles.
- *Will the award be enforceable abroad?* An India-seated award can be enforced in other New York Convention states, subject to the enforcing court's review. We prepare the documents that court will ask for.
- *Can we use UNCITRAL Rules?* Yes. Equator can act as administering institution or appointing authority.

### P-17 International mediation — `/disputes/international-commercial/international-mediation`

| Field | Copy |
|---|---|
| SEO title | International Commercial Mediation \| Equator Resolution |
| Meta description | Cross-border mediation for businesses, online and in your language. Settlements can be recorded as consent awards for New York Convention use. |
| H1 | International commercial mediation |
| Hero one-liner | Mediate across borders; record the settlement as a consent award where you need enforcement. |
| Hindi hero | अंतरराष्ट्रीय वाणिज्यिक मध्यस्थता — सीमाओं के पार, आपकी भाषा में। |
| CTAs | **Invite the other side** · **See mediation fees (USD)** |

**Sections.** *When it fits:* continuing supply, distribution or JV relationships; quality and payment disputes; deadlock. *How it works:* "Under Equator's Mediation Rules (or the UNCITRAL Mediation Rules 2021 if you choose), with a mediator acceptable to both, online, with co-mediation across cultures where useful." *Status of the law:* "The Mediation Act, 2023 defines international mediation, but most of its procedure is not yet in force; mediation runs under the parties' agreement. {{claim:law.singapore_status}}" *Enforcement:* consent award by a separately constituted tribunal (arb-med-arb). *Fees:* filing {{fee:INT-MED.FILING}}, administration and mediator per session-day from the INT-MED card.

**FAQs.**
- *Is a mediated settlement binding?* Yes, as a contract once signed. For cross-border enforcement, convert it into a consent award.
- *Can we mediate during an arbitration?* Yes. The tribunal can pause the arbitration while you mediate, and any settlement can become a consent award.

### P-18 Workplace mediation — `/disputes/workplace/workplace-mediation`

| Field | Copy |
|---|---|
| SEO title | Workplace Mediation for Employees & Employers \| Equator |
| Meta description | Exit terms, unpaid dues, team conflict and executive disputes, mediated privately. Statutory dues paid in full; statutory forums stay open. |
| H1 | Workplace mediation |
| Hero one-liner | Workplace conflict, handled privately and with respect. |
| Hindi hero | कार्यस्थल के विवाद, गोपनीय और सम्मानजनक तरीके से। |
| CTAs | **Understand your options — free** · Employers: **Talk to us** |

**Sections.** *For employees:* exit terms, notice pay, relieving letters, bonus, ESOPs; "Statutory dues are paid in full. Only the rest is negotiated." *For employers:* "A record of genuine steps, full and final within two working days of exit (Code on Wages, 2019 s.17(2)), and a draft settlement memorandum for the conciliation officer where the employee is a 'worker'." *Team conflict:* "Separate conversations first, then a facilitated joint conversation, a written working agreement and a review after 60 days. No money, no blame." *Executives and founders:* mediation, then arbitration of contractual claims if your agreement provides for it. *Gig and platform workers:* platform grievance desk first; State boards where notified. *Not here:* sexual harassment complaints (→ P-19), whistle-blowing reports.

**FAQs.**
- *Who pays?* In individual matters the default split is 75% employer, 25% employee, and employees can ask for a concession. Fees are shown including GST before payment.
- *Is it confidential?* Yes. Sessions are not recorded, and settlement terms cannot stop anyone from reporting wrongdoing to an authority.

### P-19 Workplace sexual harassment (POSH) — `/disputes/workplace/posh-sexual-harassment`

| Field | Copy |
|---|---|
| SEO title | Workplace Sexual Harassment (POSH): Where to Go \| Equator |
| Meta description | Sexual harassment at work is handled by the Internal or Local Committee under the POSH Act. How to complain, and how we support Committees. |
| H1 | Sexual harassment at work: where to go |
| Hero one-liner | Complaints go to your employer's Internal Committee or the Local Committee. Equator gives Committees secure tools — never the decision. |
| Hindi hero | कार्यस्थल पर यौन उत्पीड़न: शिकायत कहाँ करें। |
| CTAs | **Leave this page** (QuickExit) · Employers: **POSH Committee tools** → P-33 |

**Sections.** *Where to complain:* "Your employer's Internal Committee (employers with 10 or more employees must have one), or the Local Committee through the District Officer. You can also use the SHe-Box portal. If a crime has been committed, you can go to the police at any time." *Time limits:* "A written complaint is made within three months of the incident (or the last incident); the Committee can extend this by three months for reasons recorded (POSH Act, 2013 s.9(1))." *What the Committee must do:* "Complete its inquiry within 90 days (s.11(4)) and keep your identity confidential (s.16)." *Conciliation:* "Only if you ask for it in writing, and never on the basis of money (s.10(1))." *What Equator does:* provides Committees with a sealed case workspace, clocks, trained external members and annual-report tools. *What Equator does not do:* "We do not take complaints, investigate or decide. Dispute Explorer does not ask for any details."

**FAQs.**
- *Can Equator investigate my complaint?* No. Only the Internal or Local Committee can inquire into it. We can show you how to reach them.
- *Can I be pushed to settle?* No. Conciliation happens only at your written request and cannot involve a money settlement.
- *Will anyone know I visited this page?* We do not tell anyone. Use "Leave this page" to exit quickly; we do not place advertising trackers on this page.

### P-20 Respond to a notice — `/respond`

| Field | Copy |
|---|---|
| SEO title | Received a Notice from Equator? Respond Here |
| Meta description | Check the notice is genuine, read it in your language and give your side. Mediation is voluntary, and free public forums are listed too. |
| H1 | Received a notice? Read it and give your side. |
| Hero one-liner | Taking part lets you put your position on record. Not responding is not an admission, but an arbitration may continue without you. |
| Hindi hero | नोटिस मिला है? उसे पढ़ें और अपना पक्ष रखें। |
| CTAs | **Enter your notice code** → `/r/{code}` · **Verify a notice** → `/verify` |
| Schema / links | `WebPage` · `/verify`, `/how-it-works`, `/fees`, `/help/representatives` |

**Sections.** *Is it genuine?* "Every Equator notice has a case number and a code you can check at equatorresolution.in/verify. We never ask for your OTP, passwords, card or Aadhaar number, and we never threaten arrest." *What kind of notice?* "An invitation to mediation or conciliation is voluntary — you can say yes, ask questions or say no. A notice in an arbitration means a tribunal may decide even if you don't take part." *Your choices:* accept · ask a question · propose other dates or a different neutral from the shortlist · ask for more time (once, up to 14 days) · decline (reason optional and private) · tell us you are not the right person · go to a free public forum instead. *Cost:* "{{claim:svc.first_session_free_respondent}}" *Help:* "You can appoint an advocate or a family member to act for you." *Your data:* "We received your contact details from the person who raised the matter, to pursue their claim. Read our privacy notice; reply STOP to stop messages on any channel."

**FAQs.**
- *Do I have to take part?* Not in mediation or conciliation; they are voluntary. In arbitration, the tribunal can continue without you; responding puts your side on the record.
- *Is ignoring the notice an admission?* No. But in arbitration, an award can be made on the material the tribunal has.
- *Does the invitation stop any deadline?* No, unless both sides sign a separate agreement about time limits.

---

### Mechanism page template (P-21 – P-27)

Hero with `WhoDecidesChip` → identity strip → AnswerFirst ("What is {mechanism}?") → how it works (stages from Appendix A) → what you get (output labels from K §5.8, copy-lint list) → confidentiality → where it is and isn't available (from master §5.2 — rendered from the routing matrix, not typed) → governing law with section citations bound to Appendix G rule IDs → fees (tokens) → FAQs → CTA. Schema: `Service` (`serviceType` = mechanism) + `BreadcrumbList`.

### P-21 Negotiation — `/mechanisms/negotiation`

| Field | Copy |
|---|---|
| SEO title | Online Negotiation: Structured Offers \| Equator Resolution |
| Meta description | Make and answer offers in writing, with or without a neutral. Agreed terms become a signed settlement with payments tracked. |
| H1 | Negotiation |
| Hero one-liner | Make and answer offers in writing, at your pace. You both decide. |
| Hindi hero | बातचीत — लिखित प्रस्ताव, आपकी अपनी गति से। निर्णय आप दोनों का। |

**Sections.** *How it works:* "One side makes a written offer; the other accepts, rejects or counters. Offers in a pre-litigation invitation stay open for at least 14 days. A case manager or neutral can help, but no one decides for you." *Blind-bid (money claims only):* "Each side enters a confidential figure. If the figures come within the range you both agreed in advance, the matter settles on the formula you agreed; if not, neither side sees the other's figure." *Not available:* blind-bid for retail insurance, microfinance, statutory employment dues, or maintenance where a party is vulnerable. *Outcome:* a settlement agreement you both e-sign, with instalments and documents tracked.

**FAQs.** *Does a rejected offer bind me?* No. An offer binds only when accepted and the settlement is signed. · *Can the other side see my blind bid?* No. Neither figure is shown unless the matter settles under the formula you both agreed.

### P-22 Conciliation — `/mechanisms/conciliation`

| Field | Copy |
|---|---|
| SEO title | Conciliation (A&C Act Part III) Online \| Equator Resolution |
| Meta description | A neutral conciliator helps both sides agree. A signed settlement under section 73 has the status of an arbitral award (section 74). |
| H1 | Conciliation |
| Hero one-liner | A neutral helps you agree; a signed settlement has the status of an arbitral award. |
| Hindi hero | सुलह — एक तटस्थ व्यक्ति आपको सहमति तक पहुँचने में मदद करता है। |

**Sections.** *The law:* "Conciliation is governed by Part III of the Arbitration and Conciliation Act, 1996 (sections 61–81)." *Starting:* "It begins when the other side accepts a written invitation (s.62). If there is no reply within 30 days, the invitation may be treated as rejected (s.62(4))." *During:* "The conciliator may suggest terms (s.67). Everything is confidential (s.75), and views, proposals and admissions cannot be used later in arbitration or court (s.81)." *Outcome:* "{{claim:law.conciliation_s74}} It can be enforced under section 36." *Deadlines:* "Conciliation does not stop limitation. You may start proceedings if needed to protect your rights (s.77)." *Afterwards:* "The conciliator does not act as arbitrator or counsel in the same dispute unless all parties agree (s.80); Equator requires that agreement in writing after conciliation ends."

**FAQs.** *Is a conciliation settlement enforceable?* Yes. Once signed by the parties and authenticated by the conciliator, it has the same status as an arbitral award on agreed terms. · *When is conciliation better than mediation?* It is the route Equator offers by default where an organisation is the other side and you want an enforceable written outcome; you can choose either before the invitation is sent.

### P-23 Mediation — `/mechanisms/mediation`

| Field | Copy |
|---|---|
| SEO title | Online Mediation in India \| Equator Resolution |
| Meta description | A trained mediator helps you both reach your own agreement. Voluntary, confidential and not recorded. A signed settlement binds you as a contract. |
| H1 | Mediation |
| Hero one-liner | You decide. Nobody can force a settlement. |
| Hindi hero | मध्यस्थता — निर्णय आपका है। किसी को समझौते के लिए बाध्य नहीं किया जा सकता। |

**Sections.** *How it works:* "You both sign an agreement to mediate. The mediator speaks to each of you separately first, then holds joint and private sessions online, by phone or in person. In family and safety-sensitive matters, sessions can be held in separate rooms." *Choosing the mediator:* "The other side chooses from a shortlist produced under our published allocation rules; either of you can ask for a woman mediator." *Confidentiality:* B-07 + "{{claim:conf.no_mediation_recording}} {{claim:conf.caucus_sealed}}" *Outcome:* "{{claim:law.settlement_contract}} Where the law allows, we can help record it as a settlement under section 73 (if the process ran as conciliation), a consent arbitral award, a Lok Adalat award (you apply to the Legal Services Authority) or terms of compromise in a pending court case." *The Mediation Act, 2023:* {{flag:mediation_act.s27.in_force}} OFF text: "The Mediation Act, 2023 is only partly in force. Its sections on enforcing mediated settlements (27–28) have not yet been notified. Until they are, a mediated settlement is a binding contract." ON text (legal reviewer activates with the notification reference): "Under section 27 of the Mediation Act, 2023, a mediated settlement agreement is enforced in the same manner as a court judgment, subject to challenge on the limited grounds in section 28." *Time:* "Equator aims to finish mediations within {{config:time_bands.mediation.default}} of the first session. This is a target, not a promise."

**FAQs.** *Is mediation binding?* Only if you both sign a settlement. Until then, either side can walk away. · *Can I bring a lawyer or a support person?* Yes, with notice to the mediator; a support person does not speak for you unless authorised. · *What if we don't agree?* The mediator closes the mediation with a short note that gives no reasons, and we show your other options again.

### P-24 Arbitration — `/mechanisms/arbitration`

| Field | Copy |
|---|---|
| SEO title | Online Arbitration in India: Institutional Rules \| Equator |
| Meta description | Institutional arbitration under published Equator Rules: independent appointments, online hearings, documents-only and expedited tracks. |
| H1 | Arbitration |
| Hero one-liner | A neutral arbitrator hears both sides and decides. Binding, enforceable arbitration — online. |
| Hindi hero | माध्यस्थम् — एक तटस्थ मध्यस्थ दोनों पक्षों को सुनकर निर्णय देता है। |

**Sections.** *When it's available:* "When there is a written arbitration agreement (s.7) — in your contract or signed after the dispute arises — and arbitration is allowed for your kind of dispute." *Appointment:* "{{claim:ind.appointment_policy}} Every arbitrator discloses conflicts in writing before appointment (s.12). A waiver of the statutory ineligibility rules is valid only if made expressly in writing after the dispute arises (s.12(5))." *Tracks:* documents-only, expedited, fast track by written agreement (s.29B), emergency arbitrator, optional appeal tier for higher-value matters by agreement. *Time limit:* "For domestic arbitrations the award is due within 12 months of the end of pleadings, extendable by 6 months by consent; after that only a court can extend (s.29A)." *Award:* "{{claim:law.award_s36}} We publish how many Equator awards courts have set aside." (`stats.set_aside` gate) *Confidentiality:* "Arbitral proceedings are confidential except the award where needed for enforcement (s.42A). Hearings are recorded only with everyone's consent." *Not available:* divorce, custody, guardianship, wills and probate, criminal matters, retail insurance claims, workers' termination disputes, consumer complaints that belong to the Consumer Commission.

**FAQs.** *Can I challenge the award?* Yes, but only on the limited grounds in section 34, generally within three months of receiving it (extendable by 30 days by the court). · *Can we choose the arbitrator?* In disputes between businesses on equal terms, each side may nominate a co-arbitrator; Equator appoints the presiding or sole arbitrator. In loan, insurance, employment and consumer matters, Equator appoints. · *Is the arbitrator a judge?* No. Arbitrators are private neutrals appointed under the Arbitration and Conciliation Act, 1996 and Equator's Rules.

### P-25 Med-arb — `/mechanisms/med-arb`

| Field | Copy |
|---|---|
| SEO title | Med-Arb and Arb-Med-Arb Explained \| Equator Resolution |
| Meta description | Try mediation first; if it fails, arbitration decides. A different neutral by default, private information firewalled, consent awards where agreed. |
| H1 | Med-arb, arb-med and arb-med-arb |
| Hero one-liner | Try to agree first. If you can't, a different neutral decides. |
| Hindi hero | पहले सहमति का प्रयास करें। न हो पाए तो कोई दूसरा तटस्थ व्यक्ति निर्णय देता है। |

**Sections.** *Med-arb:* "Mediation first; unresolved issues go to arbitration. A different neutral arbitrates by default. The mediator may continue as arbitrator only if every party agrees afresh, in writing, after mediation ends, and the mediator makes a new disclosure. What you said privately in mediation never goes to the arbitrator." *Arb-med:* "The arbitrator writes and seals the award before mediation begins. If you settle, a consent award replaces it; if not, the sealed award is released." *Arb-med-arb:* "Arbitration is paused for mediation; a settlement becomes a consent award (s.30) — the main route for cross-border enforcement." *Where available:* loans and business (all), international (all), family (property only), insurance (business-to-business only), workplace (non-worker contracts only).

**FAQs.** *Why a different neutral?* So nothing said in confidence during mediation can influence the decision. · *Is a consent award enforceable?* Yes, like any arbitral award (s.30, s.36).

### P-26 Pre-litigation mediation — `/mechanisms/pre-litigation-mediation`

| Field | Copy |
|---|---|
| SEO title | Pre-Litigation Mediation (Voluntary, Pre-Suit) \| Equator |
| Meta description | Settle before anyone files a case: a neutral invitation, a free first session for the person invited, and a written settlement. Always voluntary. |
| H1 | Pre-litigation mediation |
| Hero one-liner | Voluntary pre-suit mediation — before anyone files a case. |
| Hindi hero | मुकदमे से पहले मध्यस्थता — स्वैच्छिक, किसी के मामला दायर करने से पहले। |

**Sections.** *How it works:* "You describe the dispute; we send the other side a neutral invitation from our case team, explaining that it is voluntary, what it costs and which free forums exist. We contact them no more than six times, only between 8 am and 7 pm. If they agree, both sides sign, a neutral is appointed and sessions begin." *Cost:* "{{claim:svc.first_session_free_respondent}} The person who starts pays a registration fee shown before payment." *Outcomes:* settlement agreement; section 73 settlement if run as conciliation; consent award; Lok Adalat application pack; court compromise papers. *What it is not:* "Commercial suits of ₹3 lakh or more without urgent interim relief must first go through pre-institution mediation under section 12A of the Commercial Courts Act, 2015, conducted by the Legal Services Authority. Equator's mediation does not replace that step; we can help you prepare the application." {{flag:com.s12a_equator_authorised → ON text drafted by legal reviewer when all four M-06 gates close}} *Deadlines:* D-13. *Statute status:* "The Mediation Act, 2023's provisions on pre-litigation mediation are not yet in force; this service runs under the parties' agreement and Equator's Rules."

**FAQs.** *Is it compulsory?* No. Either side can decline, and nothing changes in your legal rights if they do. · *What if they don't reply?* We close the invitation after 14 days for an individual or 30 days for an organisation and give you a non-commencement notice listing your other options. · *Does this satisfy section 12A?* No, as the law stands. Only the Legal Services Authority conducts section 12A mediation.

### P-27 Expert determination — `/mechanisms/expert-determination`

| Field | Copy |
|---|---|
| SEO title | Expert Determination for Technical Disputes \| Equator |
| Meta description | An independent expert decides a technical, quantum or valuation question you both agreed to refer. Contractual, not an arbitral award. |
| H1 | Expert determination |
| Hero one-liner | An independent expert decides the number; you keep control of the rest. |
| Hindi hero | विशेषज्ञ निर्धारण — एक स्वतंत्र विशेषज्ञ तकनीकी प्रश्न तय करता है। |

**Sections.** *Uses:* completion accounts and valuation, construction measurement, SLA metrics, insurance quantum by a licensed surveyor or loss assessor, cause of failure. *How it binds:* "As agreed in your contract; it is not an arbitral award and is not enforced under section 36." *Insurance:* "For individual policyholders, an expert's view is non-binding unless both sides choose, after full disclosure, to be bound — and it is never the surveyor who assessed the original claim." *Available in:* business, insurance and international disputes.

**FAQs.** *Can an expert decide who is liable?* No. Experts decide facts, figures or technical questions; questions of liability or coverage stay with the parties or a tribunal.

---

### Organisation page rules (P-28 – P-34)

Every organisation page carries, in the first screen below the hero, the **regulatory-status disclaimer** for its segment (never a badge): lenders — WC-09 text; insurers — "Equator is a private dispute resolution institution. It is not regulated, approved or audited by IRDAI and does not act as an insurance intermediary for either side."; employers/GRM/POSH — WC-31 text. F-01 ("Fair to your customers. Defensible to your regulator.") is never placed in the same visual block as a regulator's name or logo. Demo form (all segments): organisation, segment, contact name, corporate email, phone, monthly dispute volume band (`<100 | 100–500 | 500–2,000 | >2,000`), message (optional), purpose-wise consent (FR-P13-19). Schema: `Service` (+ `SoftwareApplication` for P-32–P-34 with `offers` only from the fee engine).

### P-28 For organisations (hub) — `/for`

| Field | Copy |
|---|---|
| SEO title | Dispute Resolution for Organisations \| Equator Resolution |
| Meta description | Lenders, insurers, employers, listed companies and universities: grievance desks, POSH tools, clause and API integration, independent appointments. |
| H1 | For organisations |
| Hero one-liner | Fair to your customers. Defensible to your regulator. Add Equator to your contracts and your grievance desk. |
| Hindi hero | आपके ग्राहकों के लिए निष्पक्ष। समीक्षा में टिकाऊ। |
| CTAs | **Request a demo** → `/request-demo` · **Try the API sandbox** → `/developers` · **Get the clause** |

**Sections.** *Choose your segment:* Lenders · Insurers · Employers · Listed companies · Universities · Marketplaces and fintech · Government and legal services. *What you can use:* administered cases (negotiation to arbitration) · grievance desks · POSH Committee tools · bulk intake by CSV, SFTP or API · clause library and clause API · dashboards and MIS · Private ADR Chambers for institutions. *Integrations:* "REST APIs and webhooks, a JS widget and SDKs for LOS/LMS, HRMS and claims systems, with native connectors for Finbyx and Udofin (both Infrabyx Group companies — relationship disclosed)." *What a contract never buys:* "Any say in which neutral hears a case, any veto over an appointment, or any change to the procedure. Service levels affect administrative speed only. We tell the other side when you pay Equator under a programme."

**FAQs.** *Can we choose which neutrals hear our cases?* No. Equator appoints under published rules; organisations cannot select or veto neutrals (NN-03). · *Does an enterprise plan give our cases priority?* Only for administrative tasks such as faster registration. It never affects who decides or how. · *Do you tell the other side about our contract?* Yes. Notices disclose that the organisation pays Equator's fees and that this does not affect the neutral.

### P-29 For lenders — `/for/lenders`

| Field | Copy |
|---|---|
| SEO title | Dispute Resolution & Grievance Desks for Lenders \| Equator |
| Meta description | For banks, NBFCs, HFCs, MFIs and digital lenders: clause at sanction, bulk conciliation, independent arbitration and grievance desks. |
| H1 | Dispute resolution for lenders |
| Hero one-liner | Arbitration your borrowers can trust and your auditors can check — with an Independence Evidence Pack for every case. |
| Hindi hero | ऋणदाताओं के लिए विवाद समाधान — उधारकर्ताओं के लिए निष्पक्ष, समीक्षा में टिकाऊ। |
| CTAs | **Request a lender demo** · **See programme pricing** → `/pricing/organisations?segment=lender` |

**Disclaimer (first screen).** "Built to support lenders' grievance-redressal and fair-practices obligations under RBI directions. Equator is a private dispute resolution institution and is not regulated, approved or audited by the Reserve Bank of India."

**Sections.** *Why appointment matters:* "Courts have held that a clause letting one side alone appoint the arbitrator is not valid for appointments (*CORE v ECI-SPIC-SMO-MCML*, Supreme Court, 8 Nov 2024; *Bhadra International v Airports Authority of India*, Supreme Court, 5 Jan 2026). Equator appoints from an independent panel under published rules; you never choose or veto." *What you get:* clause at sanction through the LOS (Finbyx first) · post-dispute consent and section 12(5) waiver capture from each party · rule-based allocation with conflict checks · a Defensibility Score that shows which procedural safeguards are present (it is not a prediction of any court's view) · the Independence Evidence Pack · bulk intake · a ladder of digital notice and negotiation, conciliation and documents-only arbitration · settlement loop with e-mandate instalments and escrow · NOC and document-release tracking. *Contact conduct built in:* "Calls and messages only between 8 am and 7 pm, recording with disclosure, your grievance officer's details in every message, blackout dates honoured — the RBI conduct rules effective 1 Jan 2027 applied now." *Borrower fairness:* "Borrowers pay nothing under a programme, and Equator's fees are never added to their dues. Borrowers see the free RBI routes first and can object to an appointment." *Grievance desk:* see P-32. *What we never do:* collections, field visits, credit decisions or a success fee charged to borrowers.

**FAQs.** *Can our loan agreement name Equator?* Yes, as the administering institution that appoints the arbitrator from its panel. A clause giving the lender the choice will not be accepted. · *Does the Defensibility Score mean an award will survive challenge?* No. It records which safeguards were followed; only a court decides a challenge. · *Is this a collection service?* No. Equator is neutral, and settlement money goes to you directly or through bank escrow, never through Equator.

### P-30 For insurers — `/for/insurers`

| Field | Copy |
|---|---|
| SEO title | Insurance Dispute Resolution for Insurers & TPAs \| Equator |
| Meta description | Protocol mediation, batched settlement days, insurer grievance desks, surveyor expert determination and B2B arbitration. Never against policyholders. |
| H1 | Dispute resolution for insurers |
| Hero one-liner | Settle the settleable early — with independent neutrals and policyholders' free routes shown first. |
| Hindi hero | बीमा कंपनियों के लिए विवाद समाधान — स्वतंत्र तटस्थ व्यक्तियों के साथ। |
| CTAs | **Request an insurer demo** · **See insurer plans** |

**Disclaimer (first screen).** Insurer text (organisation page rules above).

**Sections.** *Protocol matters:* claim file within 14 days; settlement authority confirmed in writing before every session; non-monetary outcomes. *Batched settlement days:* "A neutral works through a batch of files against your confidential settlement grid. Policyholders pay nothing and are free to decline." *Grievance desk:* insurer GRO desk with IRDAI timelines tracked; escalation to mediation. *Business-to-business:* co-insurance, double insurance, facultative and treaty reinsurance, subrogation against carriers, inter-insurer motor recovery, TPA and hospital disputes — mediation, arbitration by agreement, expert determination. *Independence:* "No single insurer's matters may exceed 40% of a neutral's insurance caseload. Insurers never nominate neutrals in policyholder matters." *Transparency:* [GATED: counsel opinion on aggregated publication, S9 §10 Q11] "We publish quarterly anonymised statistics for each insurer; subscription contracts cannot suppress them."

**FAQs.** *Can our retail policies refer disputes to Equator arbitration?* No. Retail general insurance policies carry no arbitration clause (IRDAI circular of 27 Oct 2023), and Equator never arbitrates against an individual policyholder. Commercial lines may use a separate arbitration agreement. · *Is a success fee available?* No. Insurance matters carry no success fee of any kind.

### P-31 For employers — `/for/employers`

| Field | Copy |
|---|---|
| SEO title | Workplace Dispute Tools for Employers \| Equator Resolution |
| Meta description | Grievance committees, HR desks, POSH Committee tools, exit mediation and executive arbitration — with employees' statutory dues protected. |
| H1 | For employers |
| Hero one-liner | One console for grievance committees, POSH Committees and workplace mediation — with your employees' statutory rights protected. |
| Hindi hero | नियोक्ताओं के लिए — शिकायत समितियाँ, आंतरिक समिति और कार्यस्थल मध्यस्थता, एक ही जगह। |
| CTAs | **Request a demo** · **Free POSH compliance check** → `/tools/posh-checker` |

**Disclaimer (first screen).** WC-31 text.

**Sections.** *Grievance Redressal Committee:* "For establishments with 20 or more workers (Industrial Relations Code, 2020 s.4): committee set-up, intake, 30-day tracking and the worker's next step to the conciliation officer." *HR-policy desks* for other employees. *POSH Committee tools* (P-33). *Exit and dispute mediation* (P-18) with full-and-final computation on the Code on Wages basis. *Executive and founder disputes:* mediation, then arbitration under a valid agreement. *Platform workers:* an independent tier above your internal grievance desk. *Employer-funded programmes:* "Every notice tells the employee that you pay Equator's fee and that this does not affect the neutral." *Integrations:* HRMS sync, SSO.

**FAQs.** *Can mediation we pay for be neutral?* Yes. Neutrals are allocated under published rules you cannot influence, and the funding is disclosed to the employee. · *Can a settlement include confidentiality?* Yes, but it cannot stop anyone reporting wrongdoing to an authority or waive statutory dues.

### P-32 Grievance Redressal SaaS — `/grievance-redressal`

| Field | Copy |
|---|---|
| SEO title | Grievance Redressal Software (GRM) \| Equator Resolution |
| Meta description | Grievance desks for lenders, listed companies, employers and universities, with response timelines from the rules built in and escalation to ODR. |
| H1 | Grievance desks with the regulator's clock built in |
| Hero one-liner | Receive, track and answer grievances on time — and escalate unresolved ones to independent dispute resolution. |
| Hindi hero | शिकायत निवारण डेस्क — नियमों की समय-सीमा पहले से शामिल। |
| CTAs | **Request a demo** · **Free grievance SLA health check** → `/tools/grievance-sla-check` |

**Sections.** *Four desks:* (1) Lender → borrower: RB-IOS 2026 (in force 1 Jul 2026) and the Internal Ombudsman Directions of 14 Jan 2026 — 30-day final reply, auto-escalation of rejected complaints to the Internal Ombudsman. (2) Listed company → investor: SEBI LODR and SCORES 2.0 (from 1 Apr 2024), RTA hand-off, quarterly investor-grievance statement. (3) Employer → employee: IR Code Grievance Redressal Committee and HR-policy desks. (4) University → student: UGC (Redressal of Grievances of Students) Regulations, 2023 — SGRC within 15 working days, Ombudsperson within 30 days. *Features:* web, email, WhatsApp and phone intake; clocks with owner and alerts; reply templates; AI-drafted replies with a regulatory checklist that a person approves; white-label complainant portal; MIS and regulator-format reports; one-click escalation to mediation or conciliation. *Complainants:* "Complainants pay nothing, and every reply tells them their right to go to the regulator or ombudsman." *Disclaimer:* WC-31.

**FAQs.** *Does using Equator mean we comply with RBI or SEBI rules?* No. The tools help you meet the timelines; compliance stays your responsibility. · *Can a complainant still go to the RBI Ombudsman or SCORES?* Yes, always. Every reply states that right. · *What happens if our subscription lapses?* Ticket intake and running clocks are never blocked for non-payment.

### P-33 POSH Internal Committee SaaS — `/posh-internal-committee`

| Field | Copy |
|---|---|
| SEO title | POSH Internal Committee Software \| Equator Resolution |
| Meta description | Sealed case workspace, 90-day inquiry clocks, annual-report generator and vetted external members for your Internal Committee. Your Committee decides. |
| H1 | Your Internal Committee, organised |
| Hero one-liner | Sealed files, 90-day clocks and the annual report — so your Internal Committee can do its statutory job properly. |
| Hindi hero | आपकी आंतरिक समिति, व्यवस्थित — सीलबंद फ़ाइलें, 90-दिन की समय-सीमा, वार्षिक रिपोर्ट। |
| CTAs | **Free POSH compliance check** · **Request a demo** · **Find an external member** |

**Sections.** *Constitution register:* Presiding Officer a senior woman employee, at least one-half women members, an external member, terms of up to three years (POSH Act, 2013 s.4). *Sealed workspace:* "Separate encryption keys, no analytics, no AI training, no shared dashboards. Access is limited to Committee members; any emergency access is logged and reported to the Data Protection Officer." *Clocks:* complaint within 3 months (+3) (s.9) · copy to respondent within 7 working days (Rules r.7(2)) · reply within 10 working days (r.7(3)) · inquiry within 90 days (s.11(4)) · report within 10 days (s.13(1)) · employer action within 60 days (s.13(4)). *Conciliation:* "Only at the aggrieved woman's written request, and never on a monetary basis (s.10)." *Annual report* under s.21 and the Board-report disclosure under Companies (Accounts) Rules, 2014 r.8(5)(x) (as amended w.e.f. 14 Jul 2025). *External members:* vetted professionals at published fees ({{fee:WRK-POSH.EXT}}). *Plans:* {{fee:WRK-POSH.SME}} onwards.

**FAQs.** *Does the software decide complaints?* No. The Internal Committee decides; the software keeps records, clocks and reports. · *Can Equator staff read our POSH files?* No. Only your Committee members have access; any emergency access is logged and notified. · *Will an unpaid invoice block an inquiry?* Never. Open inquiries stay accessible within their 90-day clock.

### P-34 Private ADR Chambers — `/private-adr-chambers`

| Field | Copy |
|---|---|
| SEO title | Private ADR Chambers: Practice Software for Neutrals |
| Meta description | Run your own mediation and arbitration practice on Equator's case, video, payment and e-sign tools, under your own rules and brand. 14-day trial. |
| H1 | Private ADR Chambers |
| Hero one-liner | Practise ADR, independently. Run your practice on Equator's case, payment and e-sign tools. |
| Hindi hero | निजी एडीआर चैंबर्स — स्वतंत्र रूप से अपनी प्रैक्टिस चलाइए। |
| CTAs | **Start 14-day trial** · **Compare plans** → `/pricing/professionals` |

**Sections.** *Who it's for:* independent mediators and arbitrators, law firms, chambers of commerce, bar associations, universities. *What you get:* your brand and domain · your rules and fee schedules (checked by our validators) · case management, video rooms with private breakout rooms, documents, e-sign and e-stamp, payments with automatic splits and GST invoices · statutory clocks · templates. *Your terms, our safeguards:* "You run proceedings your way. A few platform rules always apply: no 'court' or 'judge' branding, statutory clocks stay on, AI drafts need human approval, and personal data is protected." *Not Equator's cases:* "Matters on your Chambers are yours. Equator does not administer or vouch for them unless you refer a case to us." *Naming:* "Names using 'Court' need a legal review first; we recommend 'Chambers' or 'Centre'." *Trial:* {{claim:ch.trial_14d}} *Plans:* {{fee:CH.SOLO}} · {{fee:CH.PRO}} · {{fee:CH.INST}}.

**FAQs.** *Will my Chambers listing get me Equator panel cases?* No. Panel allocation follows published rules and never reads plan or billing data. · *What happens if I cancel?* Your open cases stay accessible and you can export your workspace for 90 days.

---

### P-35 Find a Neutral (directory) — `/neutrals`

| Field | Copy |
|---|---|
| SEO title | Find a Mediator or Arbitrator in India \| Equator Resolution |
| Meta description | Verified profiles of Equator's mediators, conciliators and arbitrators: grade, languages, sectors and availability. No paid listings, no win rates. |
| H1 | Find a neutral |
| Hero one-liner | Verified profiles, shown in random order within your filters. No paid listings. No win rates. |
| Hindi hero | तटस्थ व्यक्ति खोजें — सत्यापित प्रोफ़ाइल, बिना भुगतान वाली सूची के। |
| CTAs | Filters; per profile: **View profile** (and "Request this neutral" **only** where the case's agreement allows nomination — never in FIN, INS-retail, WRK-worker or consumer matters) |
| Schema | `CollectionPage` + `ItemList`; profile pages `Person` (`name`, `jobTitle`, `memberOf` → Organization `@id`, `knowsLanguage`, `knowsAbout`, `hasCredential` for verified credentials); **no `aggregateRating` or `Review`** |

**Sections.** *Filters:* dispute type, mechanism, grade (A/B/C), language, city, endorsements, availability. *Profile anatomy:* name and photo (with consent) · grade and roles · verified credentials (e.g., Bar enrolment, former judicial office) with "Verified on {date}" · endorsements · languages · cities · CPD status · availability · fee band (from the fee engine) · "Conflict disclosures are made for every appointment" (`ind.disclosures`). *Never shown:* win rates, settlement rates, outcome counts, "lender-friendly" or "borrower-friendly" tags, paid badges. *Ratings:* only from verified participants of closed cases, moderated, shown only when there are at least 10. *Count:* `{{claim:panel.count}}` shown only when n ≥ 25; otherwise no number. *Profile page title pattern:* `{Name} — {Primary role}, {City} | Equator` (truncate the city first to stay ≤ 60).

**FAQs.** *Can I choose my neutral?* In mediation, you choose from a shortlist made under our allocation rules. In arbitration, Equator appoints, except that businesses dealing on equal terms may each nominate a co-arbitrator. · *Why don't you show success rates?* Outcomes depend on the parties and the facts. Publishing them would put pressure on neutrals to push settlements, so we never do.

### P-36 Become a Neutral — `/neutrals/join`

| Field | Copy |
|---|---|
| SEO title | Become a Mediator or Arbitrator on Equator's Panel |
| Meta description | Join Equator's panel as a mediator, conciliator or arbitrator. Published grades, a fair assessment and rule-based allocation. No paid listings. |
| H1 | Join our panel |
| Hero one-liner | Resolve disputes. Build your practice. On your terms. Appointments follow our published allocation rules. |
| Hindi hero | विवाद सुलझाएँ। अपनी प्रैक्टिस बनाएँ। अपनी शर्तों पर। |
| CTAs | **Apply to join** → `/mediator/login` or `/arbitrator/login` (applicant mode) · **Read the grading policy** |

**Sections.** *Grades (published policy, D2-12):*

| Grade | Who | Requirements |
|---|---|---|
| A — Distinguished Neutral | Retired judges of the Supreme Court, High Courts or equivalent tribunals, or professionals with more than 30 years' verified experience | Subject training waived; Equator Tech Readiness module required; eligible for international and high-value matters with the relevant endorsement. Retired judges acting as mediators complete 40 hours of mediation training |
| B — Senior Neutral | More than 15 years' verified professional experience | Competence gate (assessment or recognised accreditation) |
| C — Associate Neutral | New entrants and professionals with up to 15 years' experience | Recognised training plus the Equator Qualifying Assessment |

"Experience is counted from your verified start date — Bar enrolment, professional membership or judicial service." *Steps:* apply → identity and credential checks (including Bar Council enrolment where relevant) → conflict and interest declarations → assessment → sign the Code of Conduct → onboarding and tech readiness → profile live. *How cases are allocated:* {{claim:alloc.published_rules}} "Settling more cases, or who wins, never affects your grade or your allocation." *Fees and payouts:* published neutral fee bands; payouts on published milestones with TDS. *Code of Conduct essentials:* disclose conflicts before and throughout; keep confidences; no fees or gifts outside the published schedule on Equator-administered cases; communicate with parties only through the platform. *Training:* "Choose any recognised provider. Training with the Equator ADR Institute is never required." → P-37. *Panel workspace cost:* [GATED: Appendix O card NEU approved] "The panel workspace is free."

**FAQs.** *Do retired judges need training?* For mediation, yes — 40 hours of mediation training. For arbitration, subject training is waived; the tech readiness module is required for everyone. · *Will I get more cases if more of my cases settle?* No. Allocation uses eligibility, rotation, caps and process-quality measures only. · *Can I advertise my Equator empanelment?* Factually, yes. Advocates must also follow Bar Council rules on advertising.

### P-37 Training — `/training`

| Field | Copy |
|---|---|
| SEO title | ADR Training Pathways for Neutrals \| Equator Resolution |
| Meta description | Training pathways for mediators and arbitrators: compare recognised providers, then take Equator's Qualifying Assessment. No provider is required. |
| H1 | Training pathways |
| Hero one-liner | Choose your training. We assess the skill. |
| Hindi hero | प्रशिक्षण चुनें — कौशल का मूल्यांकन हम करते हैं। |
| CTAs | **Compare training options** · **About the Equator Qualifying Assessment** |
| Schema | `WebPage`; `Course` **only** for Equator's own modules (Tech Readiness, Code of Conduct), `provider` = Organization; external courses are plain links |

**Sections.** *How training fits empanelment:* "Grade C applicants need recognised mediation or arbitration training; the 40-hour mediation course standard applies to mediators. Equator then runs its own assessment." *Options (at least three, random order):* provider cards rendered from configuration with neutral facts only — hours, mode, recognition held (with evidence), fee range, link. *Equator ADR Institute card* [GATED: flag `academy.institute_referral`, A-03]: "Equator ADR Institute is a separate organisation. {{config:institute.relationship_statement}} Choosing it gives no advantage in empanelment, grading or allocation." *Equator Qualifying Assessment:* {{claim:qap.not_yet_imi_approved}} *Equator's own modules:* Tech Readiness (all Grade A), Code of Conduct, CPD.

**FAQs.** *Do I have to train with the Equator ADR Institute?* No. Any recognised provider is accepted, and the choice never affects your application. · *Is the Equator assessment IMI-approved?* No. It is modelled on IMI's QAP criteria, and we intend to apply for approval.

### P-38 Fees — `/fees` (and `/fees/calculator`)

| Field | Copy |
|---|---|
| SEO title | Fees for Mediation, Conciliation & Arbitration \| Equator |
| Meta description | Published fees in Indian rupees for every kind of dispute. Individuals see the total including GST before paying. Fee waivers available. |
| H1 | Our fees, in full, before you start. |
| Hero one-liner | Choose your kind of dispute to see what you would pay, who pays it and what is included. |
| Hindi hero | शुरू करने से पहले, हमारी पूरी फ़ीस। |
| CTAs | **Calculate your fee** · **Ask for a fee waiver** |
| Schema | `WebPage` + `OfferCatalog` generated from the published schedule (prices only from the fee engine; `priceCurrency` INR or the INT currency) |

**Sections.** *Free options first:* SignpostCard for the chosen vertical. *Calculator:* the same deterministic quote as checkout (FR-P13-06). *Rate cards per vertical:* Included / Not included, refund summary, GST treatment, who pays, schedule version and effective date; banner "Fee schedule subject to Board approval" until approved. *Always free:* Dispute Explorer · a 10-minute process call-back · signposting reports and free-forum letters · the first session for a person invited to pre-litigation mediation · interpretation in enabled Indian languages for individuals · your first certified copy. *Charges at actual cost:* stamp duty, speed post, e-sign provider charge plus {{fee:ANC.ESIGN}} handling. *Waivers:* "Can't afford this? Ask for a fee waiver." *INT:* USD, EUR, GBP, SGD, AED with rupee equivalent and FX time. *Organisations:* → P-39.

**FAQs.** *Are prices shown with GST?* Yes for individuals: you see the total including GST before you pay. Businesses see prices plus GST. · *Do you take a percentage of my settlement?* Not from individuals. Business parties may opt in to a settlement administration fee only if every party agrees at filing. · *Can fees change after I file?* No. Your case follows the fee schedule in force on the day you filed.

### P-39 Pricing for organisations and professionals — `/pricing/organisations`, `/pricing/professionals`

| Field | Organisations | Professionals |
|---|---|---|
| SEO title | Plans for Lenders, Insurers & Employers \| Equator Resolution | Plans for Neutrals, Chambers & Counsel \| Equator Resolution |
| Meta description | Grievance desk, POSH, API and programme plans priced by usage, never by outcome. Compliance features in every tier. Prices plus GST. | Free panel workspace, Private ADR Chambers plans for independent practice, and counsel plans with no procedural advantage. Prices plus GST. |
| H1 | Plans that count what you use — never the outcome. | Plans for neutrals, chambers and counsel |
| Hero one-liner | Choose your segment to see plans, what's included and what happens at renewal. | Tools for your practice. Never visibility, never more cases. |
| Hindi hero | ऐसे प्लान जो उपयोग गिनते हैं — परिणाम नहीं। | तटस्थ व्यक्तियों, चैंबर्स और अधिवक्ताओं के लिए प्लान। |

**Sections (organisations).** Segment selector (Lender · Insurer · Employer · Listed company · University · Developer) → 3–4 plan cards per S9 §2.3 anatomy: name + "Best for" · price "₹X / month + GST" (annual toggle shows "₹Z billed yearly") · 3–5 numbered entitlements · overage line · CTA ("Talk to us", "Start sandbox") · renewal line. Comparison table per S9 §2.4: statutory and regulator-clock features appear in **every** tier; differences-only toggle; text values, never ticks alone.

**Sections (professionals).** Columns: Neutral (Panel [GATED NEU-PANEL] · Chambers Lite · Solo · Pro · Institution) · Counsel (Free · Pro · Firm — "No counsel plan gives any procedural advantage") · Membership (where approved, App. O). "What is always free" box: panel workspace, counsel access to their own cases.

**FAQs (both).** *Can I cancel any time?* Yes, from Settings in three steps or fewer. Your open cases stay open. · *Will my plan renew automatically?* For individual and small-business plans, auto-renew is off unless you switch it on; we remind you 30, 7 and 1 day before the term ends. · *Does a paid plan get me more cases or a better listing?* No. Allocation and directory order never read plan or billing data.

### P-40 Track your case — `/track`

| Field | Copy |
|---|---|
| SEO title | Track Your Case Status Online \| Equator Resolution |
| Meta description | Check the stage and next date of an Equator case with your case number and a one-time password. Details stay private to the parties. |
| H1 | Know where your matter stands |
| Hero one-liner | Every step, date and document in one place. |
| Hindi hero | जानिए आपका मामला किस चरण में है — हर चरण, तारीख और दस्तावेज़ एक जगह। |
| CTAs | **Track** (case number → OTP) · **Sign in for full details** · **Verify a document** → `/verify` |

**Sections.** *How it works:* "Enter your case number. We send a one-time password to a phone or email already on the case. You can see the status for 30 minutes." *What you'll see:* stage (labels per Appendix C §G.2), last updated, next scheduled date, mechanism, public-safe timeline. *What we never show here:* party names beyond initials, amounts, documents, allegations or the arbitrator's identity. "Family, health-insurance and certain other matters show only 'Status available to parties in their account'." *By message:* "Send STATUS and your case number on WhatsApp or SMS from a registered number." *Who decides now:* `WhoDecidesChip` beside the current stage.

**FAQs.** *Why can't I see the arbitrator's name here?* Arbitration is confidential under section 42A of the Arbitration and Conciliation Act, 1996; parties see full details after signing in. · *I've lost my case number.* Sign in to your account, or contact the case team with your registered phone or email.

### P-41 Published awards and settlements — `/decisions` (`/published-outcomes` 301)

| Field | Copy |
|---|---|
| SEO title | Published Awards & Settlements (With Consent) \| Equator |
| Meta description | Selected awards and settlements, published only with every party's consent and with names and identifying details removed. |
| H1 | Published awards and settlements |
| Hero one-liner | Published only if everyone agrees. Names removed. |
| Hindi hero | सभी की सहमति से ही प्रकाशित। नाम हटाए गए। |
| CTAs | Search and filters (dispute type, mechanism, year, outcome type) |
| Schema | `CollectionPage`; each item `CreativeWork` with `identifier` = citation (`about` the mechanism; no party `Person` markup; never `LegalCase` — App. R §3.13) |

**Status.** [GATED: flags `publication.arbitral.enabled` (ON only after the counsel opinion on A&C s.42A consent, App. R Q-R1 / 02 §5 Q1) and `publication.consensual.enabled` (App. R Q-R3), plus the App. R §3 builder pass]. Empty state: "We will publish outcomes only where every party has agreed. None are published yet."

**Sections.** *Consent:* "Every party must give informed, written consent — and, for awards, the tribunal too. Consent can be withdrawn; we then remove the item from our website, though we cannot recall copies others have already made." *Redaction:* names, addresses, account numbers, amounts where identifying, and any detail that could identify a person are removed under a published redaction profile. *Never published in full:* family matters, POSH, health insurance, matters involving children, safety-flagged matters; anonymised digests of reasoning only with consent. *Not precedent:* "Published outcomes do not bind any other case, party or neutral." *Citation:* neutral citation `EQR/{YYYY}/{TYPE}/{NNNN}` (e.g., `EQR/2027/AWD/0001`; App. R §3.9.2; X-35) with a document hash.

**FAQs.** *Can I withdraw my consent later?* Yes. We remove the item from our website promptly after you withdraw consent. · *Are these binding on future cases?* No. They show how matters were resolved; each case is decided on its own facts.

### P-42 Rules and Code of Conduct — `/rules`

| Field | Copy |
|---|---|
| SEO title | Equator Rules, Code of Conduct & Policies \| Equator |
| Meta description | Arbitration, mediation and conciliation rules, the Code of Conduct for neutrals, appointment policy and AI governance rule — versioned, with history. |
| H1 | Rules and policies |
| Hero one-liner | Everything that governs an Equator case, published and versioned. Your case follows the version in force when it was filed. |
| Hindi hero | नियम और नीतियाँ — प्रकाशित और संस्करणबद्ध। |
| Schema | `WebPage`; each ruleset `DigitalDocument` (`version`, `datePublished`, `encodingFormat` PDF with SHA-256 in `identifier`) |

**Sections.** List with version, effective date, "What changed": Arbitration Rules · Mediation Rules · Conciliation Rules · vertical rulebooks · Code of Conduct for Neutrals · Appointment and Independence Policy · Grading Policy · Allocation Policy · AI Governance Rule · Publication Policy · Fee rules, refunds and waivers · Complaints about Equator · Data retention summary. *Code of Conduct in brief:* impartiality and independence · disclosure before appointment and throughout · confidentiality · competence and diligence · respectful conduct and accessibility · no fees, gifts or side dealings outside the published schedule · communication through the platform · complaints to the Ethics & Complaints Sub-Committee. *Complaints:* "Tell us about a neutral, a case manager or our service at {{entity.email_grievance}} or through your case page. {{claim:svc.grievance_sla}}" 

**FAQs.** *Which version applies to my case?* The version in force on the day your case was filed, even if the rules change later. · *Who decides complaints about neutrals?* The Ethics & Complaints Sub-Committee of the Institutional Committee, under the published complaints procedure.

### P-43 Trust and security — `/trust` (sub-pages: `/trust/how-we-stay-neutral`, `/trust/security`, `/trust/sub-processors`, `/trust/dpa`, `/trust/outcomes`)

| Field | Copy |
|---|---|
| SEO title | Trust, Security & Neutrality \| Equator Resolution |
| Meta description | How we stay neutral, protect your data and handle money: published commitments, security practices, sub-processors, and certifications only when held. |
| H1 | How we stay neutral — and how you can check |
| Hero one-liner | We represent nobody. That's the point. |
| Hindi hero | हम निष्पक्ष कैसे रहते हैं — और आप कैसे जाँच सकते हैं। |

**Sections.** *Neutrality:* no client choice or veto of neutrals · paid relationships disclosed to the other side · no paid listings (`dir.no_paid_listing`) · no win rates · people served with notices are never marketed to · awards-set-aside count (`stats.set_aside`). *Your data:* WC-27 text; "{{claim:host.india}}" [GATED]; your rights and the DPO's contact. *Security:* WC-10 text; WC-11 text; "{{claim:sec.vapt}}" [GATED]; certificates only with a claim record; status page. *Money:* "{{claim:money.no_pass_through}} {{claim:pay.no_card_data}}" *AI:* "{{claim:ai.humans_decide}} {{claim:ai.no_training_case_data}}" [GATED: AI Governance Rule]. *Sub-processors and DPA:* versioned list with change notifications.

**FAQs.** *Is Equator ISO 27001 certified?* Not yet. Our infrastructure provider's data centres are certified, and we are building our own programme to ISO/IEC 27001; we will publish our certificate number here once certified. · *Where is my data stored?* In India, on servers in Mumbai with a backup region in Hyderabad [GATED: `host.india`].

### P-44 About and governance — `/about`, `/about/governance`

| Field | About | Governance |
|---|---|---|
| SEO title | About Equator Resolution | Governance: Equator's Institutional Committee |
| Meta description | Equator Resolution is a private dispute resolution institution for India, operated by Equator Resolution Service Private Limited (Infrabyx Group). | Case decisions sit with an Institutional Committee with a majority of external members. The company board takes no case decisions. |
| H1 | Dispute resolution, redesigned around people | How Equator is governed |
| Hero one-liner | Built so that resolving a dispute doesn't have to take years. | Decisions about cases are kept apart from the company's commercial side. |
| Hindi hero | लोगों को केंद्र में रखकर विवाद समाधान। | इक्वेटर का संचालन कैसे होता है। |
| Schema | `AboutPage` + `Organization` | `WebPage` + `Organization` (`member` only for consenting members) |

**Sections (About).** Who we are (identity line; `id.group`; entity block); the Equator Standard with proof links — *impartial* → `/trust/how-we-stay-neutral`, *expert* → grading policy, *efficient* → published time standards and (when available) metrics; what we never do (NN-01, NN-24); Advisory Council (empty state "being constituted"); offices; press.

**Sections (Governance).** *Institutional Committee:* a majority of external members, supported by the Registrar. *Sub-committees:* Appointments (confirms appointments and nominations), Challenge (decides challenges to neutrals), Scrutiny (reviews awards for form before issue), Ethics & Complaints, Rules (proposes rule changes and publishes them for public comment), AI Oversight (approves AI uses and reviews evaluations), Transparency (approves publications and statistics). *Separation:* "The company board approves budgets and fees; it takes no decision in any case." *Members:* published with each member's consent; until appointed: "The Committee is being constituted. We will publish members and the charter here." [Charter GATED: counsel Q9.]

**FAQs.** *Is the Institutional Committee a court?* No. It is Equator's internal governance body for appointments, challenges, scrutiny and complaints under Equator's Rules.

### P-45 Contact — `/contact`

| Field | Copy |
|---|---|
| SEO title | Contact Equator Resolution |
| Meta description | Contact Equator Resolution by email, phone or WhatsApp. Registered office, office addresses, Grievance Officer and Data Protection Officer details. |
| H1 | Contact Equator Resolution |
| Hero one-liner | Talk to our case team about the process, or reach the right person below. |
| Hindi hero | इक्वेटर रिज़ॉल्यूशन से संपर्क करें। |
| Schema | `ContactPage` + Organization `contactPoint` (customer support, grievance, data protection) |

**Sections.** Entity block (WC-47 tokens) · contact routes: case team (process questions only — "we can't advise on your case"), organisations, neutrals, press, partners · hours `{{entity.support_hours}}` · Grievance Officer ("We acknowledge complaints within 48 hours and aim to resolve them within one month" — `svc.grievance_sla`, E-Commerce Rules r.4) · Data Protection Officer · offices with addresses exactly as on GST registration · contact form with purpose-wise consent · "If you are in danger, call 112."

### P-46 Help Centre and FAQs — `/help`

| Field | Copy |
|---|---|
| SEO title | Help Centre and FAQs \| Equator Resolution |
| Meta description | Answers on filing, responding, fees, payments, signing, sessions, representatives, privacy and accessibility, plus free letter templates. |
| H1 | How can we help? |
| Hero one-liner | Search, browse by topic, or ask our case team about the process. |
| Hindi hero | हम आपकी कैसे मदद कर सकते हैं? |

**Sections.** Topics: Getting started · Responding to a notice · Fees, payments and refunds · Sessions and hearings · Signing, stamping and registration · After the outcome · Representatives · Privacy and your data · Languages and accessibility · Staying safe. *Letters library* (`/letters-library`): free templates to your lender, insurer, employer or the other side, with the banner "This is not legal advice. You can ask an advocate to check it." *Deadlines that matter:* rendered from the clocks registry. *Glossary.*

**FAQ bank (answer-first; reused across pages).**
- *How long does mediation take?* It depends on you both. Equator aims to finish mediations within {{config:time_bands.mediation.default}} of the first session; nobody is pressed to settle by a date.
- *What if the other side doesn't respond?* In mediation or conciliation, the invitation closes and we give you a non-commencement notice listing your other options. In arbitration, the tribunal may continue.
- *Can I change my mind after signing a settlement?* A signed settlement binds you. Ask an advocate if you think it was signed under pressure or mistake.
- *Is my information shared with the other side?* Only what you choose to file or share. Private conversations with a mediator stay private.
- *Do you accept cash?* No. Payments are online through UPI, cards or net banking on our payment provider's secure checkout.
- *Can someone fill the forms for me?* Yes. A case manager or a person you trust can help in assisted mode; you confirm with a one-time password on your own phone.
- *What languages can I use?* {{locales_live}} at present, with more Indian languages being added.
- *Who do I complain to about Equator?* Our Grievance Officer, {{gro.name}}, at {{gro.email}}.

### P-47 Careers — `/careers`

| Field | Copy |
|---|---|
| SEO title | Careers at Equator Resolution |
| Meta description | Work on fair, accessible dispute resolution for India: engineering, legal operations, case management and design. See open positions. |
| H1 | Careers |
| Hero one-liner | Help build dispute resolution people can trust. |
| Hindi hero | ऐसा विवाद समाधान बनाने में मदद करें जिस पर लोग भरोसा कर सकें। |
| Schema | `WebPage`; each role `JobPosting` (`hiringOrganization` = Organization, `jobLocation` from config offices, `datePosted`, `validThrough`) |

**Sections.** What we value (the six voice anchors applied to work) · how we hire (steps, timelines) · open roles (empty state: "No open roles right now. Check back, or follow us for updates.") · equal opportunity ("We welcome applications from people with disabilities and from all genders, including transgender persons, and provide reasonable accommodation.") · "We never charge candidates any fee." · applicant privacy notice.

### P-48 Legal pages

| Route | SEO title | Meta description | H1 | Must contain |
|---|---|---|---|---|
| `/terms` | Terms of Use \| Equator Resolution | The terms that apply when you use Equator Resolution's website, apps and services, with version and effective date. | Terms of Use | Server-rendered full text, version, effective date, entity block, PDF with hash (WR-16; IT Act 2000 s.10A) |
| `/privacy` | Privacy Notice \| Equator Resolution | Who processes your data, why, for how long, your rights and how to contact our Data Protection Officer. | Privacy Notice | Data fiduciary and DPO (WC-48; DPDP Rules 2025 r.9), itemised purposes, retention, rights, complaint to the Data Protection Board, jurisdiction sections for INT parties (App. Q) |
| `/cookies` | Cookie Notice \| Equator Resolution | The cookies and similar tools we use, why, and how to change your choices. No advertising tools on case pages. | Cookie Notice | Categories, consent manager link, statement that analytics and ad tools never load on case, notice or POSH pages |
| `/disclaimer` | Disclaimer \| Equator Resolution | Equator provides information and dispute resolution services. It does not give legal advice and is not a court or regulator. | Disclaimer | Identity line; information-not-advice; no advocate–client relationship; regulator non-endorsement |
| `/grievance-officer` | Grievance Officer \| Equator Resolution | How to raise a complaint about Equator's service, who handles it and how quickly we respond. | Grievance Officer | Name, designation, contact (config); 48-hour acknowledgement and one-month redress (E-Commerce Rules r.4); escalation |
| `/accessibility` | Accessibility Statement \| Equator Resolution | Our commitment to WCAG 2.2 AA, known issues, and how to request help or report a barrier. | Accessibility Statement | WCAG 2.2 AA conformance status, RPwD Act 2016 ss.40, 42, 46, known issues with dates, contact for help, sign-language interpreter on request |

---

## 4. In-product microcopy library

### 4.1 Rules

- Keys: `{namespace}.{area}.{item}[.{variant}]`, stored in `packages/i18n/messages/{locale}.json`, ICU MessageFormat (`{caseNo}`, plurals with `{n, plural, one {# day} other {# days}}`). Strings flagged **L** carry legal effect and need `legal_reviewer` approval in every locale before activation (NN-23); all others need translator review.
- Dates `12 Nov 2026`; times with zone where parties differ; money with Indian grouping and the GST basis stated (`incl. GST` for individuals, `+ GST` for businesses — NN-29).
- Sensitive matters (FAM, POSH-linked, INS health, safety-flagged): notification bodies use the neutral variant `*.sensitive` — no subject, party name or amount in SMS, push previews or email subject lines (Appendix C §F.5).
- Buttons: verb + object ("Sign settlement", "Pay {amount}"); never "Submit", "OK", "Click here". Secondary action has equal weight where it is a legitimate choice (decline, go to free forum, cancel plan) — no confirm-shaming (NN-29).
- Errors follow: what happened · what you can do · reference (`{traceId}`) — never blame the user; entered data is preserved (Appendix C §F.9).

### 4.2 Onboarding (`onb`)

| Key | String (en) | Notes |
|---|---|---|
| `onb.welcome.title` | Welcome. Let's get you to the right place. | — |
| `onb.welcome.body` | Tell us who you are in this matter. You can change it later. | — |
| `onb.role.party` | I have a dispute, or someone has raised one with me | — |
| `onb.role.representative` | I'm helping someone else | NN-27 |
| `onb.role.business` | I'm acting for a business or organisation | — |
| `onb.role.neutral` | I'm a mediator, conciliator or arbitrator | — |
| `onb.verify.why` | We check identity only when a step needs it, such as signing or paying. For this step: {reason}. | App. S §3.1 |
| `onb.verify.aadhaar_ovse` | Verify with your Aadhaar QR code or offline e-KYC file. We never store your full Aadhaar number. | L; D2-06; NN-14 |
| `onb.verify.digilocker` | Fetch documents from DigiLocker. You choose what to share. | — |
| `onb.verify.fallback` | Can't verify online? Choose another way, such as a video call with our team. | App. S §3.15 |
| `onb.consent.intro` | Choose how we may use your information. Each choice is separate, and only the first is needed to use the service. | L; DPDP s.6 |
| `onb.consent.marketing` | Send me updates about Equator's services (optional). I can stop any time. | L; unticked by default |
| `onb.lang.choose` | Choose your language. Notices can come in a different language from the app. | NN-23 |
| `onb.save_return` | Save and come back later — we'll send a link and a code to a contact you choose. | K EP-07 |
| `onb.neutral.apply.intro` | You can save and return at any time. We verify every credential before your profile goes live. | — |
| `onb.org.sso` | Your organisation uses single sign-on. Continue with {provider}. | — |

### 4.3 Empty states (`emp`)

| Key | String (en) |
|---|---|
| `emp.cases.none` | No cases yet. When you start or respond to a matter, it will appear here. |
| `emp.cases.none.cta` | Understand your options |
| `emp.documents.none` | No documents yet. Upload what supports your side — we keep your original untouched. |
| `emp.messages.none` | No messages. Messages from the case team and the neutral will appear here. |
| `emp.sessions.none` | No sessions scheduled. We'll tell you as soon as a date is set. |
| `emp.payments.none` | Nothing to pay right now. |
| `emp.directory.no_results` | No neutrals match these filters. Try removing one. |
| `emp.outcomes.none` | We publish outcomes only where every party has agreed. None are published yet. |
| `emp.stats.none` | We will publish our first statistics after {month}, with the method we used. |
| `emp.grm.queue_clear` | No open grievances. New ones will appear here with their response clocks. |
| `emp.notifications.none` | You're up to date. |

### 4.4 Case status explanations (`sts`) — one row per case state (master §5.1; labels = Appendix C §G.2)

Each state renders three strings: `sts.{state}.label`, `sts.{state}.explain` and `sts.{state}.next`, plus the `WhoDecidesChip` value. `{…}` values come from the clocks service and case read model; the UI never computes dates (Appendix C §G.3).

*v2 alignment (one engine with Appendix R).* (1) The "Who decides now" column states the intent; the chip text actually rendered is the matching `DD-R-WHO-DECIDES` value from Appendix R §1.4.12, the single vocabulary (for example "Case team (process only)" renders as "The case team checks the papers", "You" as "You decide", "The court" as "A court decides"). (2) The viewer-specific sentences in Appendix R §1.4.11 are added to this deck as `sts.{state}.next.{viewer_side}` variants (one per viewer side used in the Appendix R §1.4.11 rule table); where no variant exists, the `.next` string below is the default. (3) Strings are legal-approved copy, never AI-generated (NN-01).

| State | `.label` | `.explain` | `.next` | Who decides now |
|---|---|---|---|---|
| `draft` | Draft — not filed | Only you can see this. Nothing has been sent. | Finish and file when you're ready, or delete it. | You |
| `filed` | Filed — awaiting review | Your matter has reached our case team. | We'll check it within {n} working days and tell you if anything is missing. | Case team (process only) |
| `under_scrutiny` | Under review by the case team | We're checking the details, the documents and whether a free public forum suits it better. | If we need anything, we'll ask by {date}. | Case team (process only) |
| `deficient` | Information requested from the filing party | Something is missing or unclear: {items}. | Add it by {date} to keep your matter moving. | You |
| `accepted` | Accepted — other party being notified | We've accepted the matter and are sending the invitation or notice. | The other side has until {date} to respond. | — |
| `signposted` | Directed to a more suitable forum | {forum} is the right place for this, because {reason}. | Go to {forum} by about {date}. Your free letter is ready. | You |
| `rejected` | Not accepted | We can't take this matter: {reason}. | Your other options are below. Any fee is refunded under the refund policy. | — |
| `awaiting_respondent` | Awaiting response | We've sent the invitation or notice to the other side. | They have until {date}. {mechanism, select, mediation {If they don't reply, the invitation closes and you'll get a notice listing your options.} arbitration {If they don't reply, the tribunal may continue.} other {We'll tell you what happens next.}} | The other side |
| `neutral_appointment` | Neutral being appointed | We're selecting a neutral under our published rules and checking for conflicts. | You'll see their written disclosure and can object within {n} working days. | Equator (Appointments) |
| `in_proceedings` | In progress | Sessions or hearings are under way. | Your next date: {date}. | {mechanism, select, arbitration {The arbitrator decides} other {You and the other side decide}} |
| `outcome_drafted` | Outcome being finalised | The settlement or award is being prepared for review and signature. | Please review it by {date}. Nothing is final until it is signed. | {mechanism, select, arbitration {The arbitrator} other {You and the other side}} |
| `outcome_executed` | Outcome signed and stamped | Everyone has signed and the stamp duty is paid. | Download your copy. Payments and promised actions are tracked here. | — |
| `in_compliance` | Agreed terms being carried out | Payments and actions under the outcome are being tracked. | Next due: {item} on {date}. | Each party, as agreed |
| `closed` | Closed | This case is complete. | Your documents stay available to download. | — |
| `on_hold` | On hold | The case is paused. {reasonPartyOnly} | We'll tell you when it restarts. Legal deadlines may still run. | — |
| `withdrawn` | Withdrawn | The case was withdrawn by {party}. | Your other options are listed below. | — |
| `lapsed` | Process ended without an outcome | The process ended because {reason}. | We'll explain your options, including going to court. | — |
| `challenged` | Outcome under challenge before a court | A party has applied to a court about the outcome. | The court decides. We'll update you when we're told of its order. | The court |
| `in_execution` | Enforcement steps under way | A party is taking steps in court to enforce the outcome. | The court handles enforcement. Your enforcement pack is here. | The court |

**Pre-litigation sub-states (`sts.prelit.*`, K §5.2):** `invitation_sent` — "Invitation sent. The other side has until {date} to reply." · `viewed` — "The other side has opened the invitation." · `consented` — "Both sides have agreed to {mechanism}. We'll appoint a neutral within {n} working days." · `settled_in_principle` — "You've agreed in principle. Final terms are being drafted for both of you to check." · `non_commencement` — "The other side did not take part. Your non-commencement notice and other options are ready."

### 4.5 Notifications (`ntf`) — SMS bodies ≤ 160 characters; DLT template tag in brackets

| Key | String (en) | Tag / notes |
|---|---|---|
| `ntf.case.filed` | Equator Resolution: matter {caseNo} filed. We'll review it within {n} working days. Track: {url} | service |
| `ntf.invite.standard` | Equator Resolution (case {caseNo}) invites you to a free, voluntary online {mechanism} about a matter raised by {claimant}. Reply by {date}: {url} Verify: equatorresolution.in/verify. STOP to opt out | service; K §5.3 |
| `ntf.invite.sensitive` | You have a message from Equator Resolution about case {caseNo}. Open securely: {url} | service; FAM-G-07 |
| `ntf.session.t48` | Reminder: your {mechanism} session for {caseNo} is on {date} at {time}. Join: {url} | service |
| `ntf.session.t2` | Your session for {caseNo} starts at {time}. Join: {url} | service |
| `ntf.document.new` | New document in case {caseNo}. Sign in to view it. | service |
| `ntf.clock.t7` | Date to watch for {caseNo}: {clockName} on {date}. Details: {url} | service; NN-04 |
| `ntf.outcome.to_sign` | Your settlement for {caseNo} is ready to review. Nothing is final until everyone signs. {url} | service |
| `ntf.payment.due` | Payment of {amountInclGst} for {caseNo} is due on {date}. Pay securely: {url} | service_billing |
| `ntf.payment.received` | Received {amount} for {caseNo}. Receipt: {url} | service_billing |
| `ntf.mandate.predebit` | Instalment of {amount} for {caseNo} will be debited on {date} under mandate {ref}. To stop it, use your bank's app or {url} | service_billing; RBI E-mandate Framework 2026 |
| `ntf.instalment.missed` | An instalment of {amount} for {caseNo} was not received on {date}. The settlement says what happens next: {url} | service; neutral tone |
| `ntf.neutral.appointed` | A {role} has been appointed for {caseNo}. Read their disclosure: {url} | service |
| `ntf.status.changed` | Update on {caseNo}: {statusLabel}. {next} | service |
| `ntf.status.sensitive` | You have an update from Equator Resolution. Open securely: {url} | service; sensitive variant |
| `ntf.recovery.footer` | {lender} grievance officer: {groName}, {groContact}. Reply STOP to opt out. | appended to every recovery-related message (NN-12) |
| `ntf.optout.confirm` | You won't get more messages on this channel for {caseNo}. Formal notices may still come by post or email where the rules require. | service |

### 4.6 Errors (`err`) — mapped to Appendix F §F.10.1 canonical codes (K §8.4 codes where noted)

| Key | String (en) | Code |
|---|---|---|
| `err.generic` | Something went wrong on our side. Your work is saved. Try again, or contact support with reference {traceId}. | `INTERNAL` |
| `err.offline` | You're offline. We'll send this when you're back online. | — |
| `err.upload.type` | This file type can't be uploaded. Use PDF, JPG, PNG or DOCX. | `UPLOAD_TYPE_NOT_ALLOWED` |
| `err.upload.size` | This file is larger than {maxMb} MB. Try a smaller file or split it. | `VALIDATION_FAILED` (violation `file_too_large`) |
| `err.upload.scan` | We couldn't accept this file because our security check flagged it. Try another copy. | `UPLOAD_QUARANTINED` |
| `err.otp.invalid` | That code didn't match. Check the latest message and try again. | `VALIDATION_FAILED` (violation `otp_mismatch`) |
| `err.otp.expired` | That code has expired. We've sent a new one. | `VALIDATION_FAILED` (violation `otp_expired`) |
| `err.otp.limit` | Too many attempts. For your security, try again after {minutes} minutes. | `OTP_LOCKED` |
| `err.session.expired` | You were signed out to keep your case safe. Sign in again — your work is saved. | `UNAUTHENTICATED` |
| `err.access.denied` | You don't have access to this. If you think you should, ask your case manager. | `FORBIDDEN` |
| `err.contact_window` | This can't be sent now. Messages on this matter can go only between 8 am and 7 pm. | `CONTACT_OUTSIDE_WINDOW` |
| `err.prelit.contact_cap` | We've already contacted the other side the most times allowed before they reply. | `PRELIT_CONTACT_CAP_REACHED` (new, K §8.4) |
| `err.mechanism.not_permitted` | This process isn't available for this kind of dispute. Here's why: {reason}. | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` |
| `err.authority.limit` | This settlement is above the amount your representative can agree. {partyName} needs to sign it. | `OFFER_ABOVE_AUTHORITY` (NN-27) |
| `err.esign.excluded` | By law, this document can't be signed electronically. We'll guide you through signing on paper, stamping and registration. | `ESIGN_EXCLUDED_INSTRUMENT` (NN-08) |
| `err.payment.failed` | Your payment didn't go through. If your account shows a debit, it is normally reversed by your bank; contact us with reference {ref} if it isn't. | — (gateway status `failed`) |
| `err.quote.changed` | The price has changed since your quote because {reason}. Please check the new total before paying. | `QUOTE_EXPIRED` |
| `err.date.future` | Enter a date in the past. | `VALIDATION_FAILED` |
| `err.amount.format` | Enter the amount in rupees, for example 1,27,500. | `VALIDATION_FAILED` |

### 4.7 Confirmations (`cnf`)

| Key | String (en) |
|---|---|
| `cnf.filed` | Your matter is filed. Reference {caseNo}. We've emailed you a copy. |
| `cnf.invite.sent` | Invitation sent to {respondent}. They have until {date} to reply. Sending an invitation doesn't stop any legal deadline. (L) |
| `cnf.consent.signed` | You've agreed to {mechanism}. Next, we appoint a neutral within {n} working days. |
| `cnf.settlement.signed_self` | You've signed. The settlement takes effect when everyone has signed. (L) |
| `cnf.settlement.signed_all` | Everyone has signed and the stamp duty is paid. Download your settlement here. |
| `cnf.payment.success` | Payment received: {amountInclGst}. Your receipt and GST invoice are on their way to {email}. |
| `cnf.withdraw.title` / `.body` | Withdraw your case? / This closes your case. Fees already used are refunded only as the refund policy says. You can still go to {forum}. Buttons: "Withdraw case" · "Keep case open" |
| `cnf.plan.cancel.title` / `.body` | Cancel your plan? / You can cancel any time. Your open cases stay open. Your plan ends on {date}; download your data by {exportDate}. Buttons: "Cancel plan" · "Keep plan" (equal weight) |
| `cnf.answers.deleted` | Your answers are deleted. |
| `cnf.rep.appointed` | {repName} can now act for you within the authority you set. You can change or cancel it any time. |
| `cnf.decline.recorded` | We've told the other side you've declined. Your reason stays private. |

### 4.8 Payment (`pay`)

| Key | String (en) | Notes |
|---|---|---|
| `pay.quote.title` | What you'll pay | — |
| `pay.quote.total_b2c` | Total payable, including GST: {total} | NN-29; first line for individuals |
| `pay.quote.breakup` | {feeName}: {amount} · GST: {gst} · Stamp duty (paid to the State): {stamp} | — |
| `pay.quote.b2b` | {amount} + GST | business buyers |
| `pay.quote.who_pays` | Who pays: {payerRule} | — |
| `pay.quote.board` | This fee schedule is subject to Board approval. | while `board_approved = false` |
| `pay.method.intro` | Pay by UPI, card or net banking on our payment provider's secure page. We never see your full card number. | L; NN-31 |
| `pay.mandate.setup` | Set up automatic instalments. Your bank will notify you at least 24 hours before each debit, and you can cancel any time. | L; RBI E-mandate Framework 2026 |
| `pay.mandate.afa` | Your bank will ask you to approve this payment because it is above ₹15,000. | L |
| `pay.escrow.explain` | Settlement money goes into a bank escrow account held by {trustee}, not to Equator. It is released when {milestone}. | L; NN-13 |
| `pay.refund.status` | Refund of {amount} approved. It will go back to your original payment method within {n} working days. | — |
| `pay.waiver.cta` | Can't afford this? Ask for a fee waiver. | S9 |
| `pay.waiver.submitted` | We've received your waiver request. We usually decide within {n} working days. Your case deadlines keep running. | — |
| `pay.dunning.d0` | We couldn't take your payment of {amount} for {plan} (due {date}). Your cases are not affected. Update your payment method. | S9 §3.3 |
| `pay.dunning.d7` | Payment still due. From {date}, new private matters will pause. Existing cases, hearings and deadlines continue. | S9 §3.3 |
| `pay.receipt.invoice` | Tax invoice {invoiceNo} · GSTIN {gstin} · SAC 998215 | B.10 |

### 4.9 Consent (`con`)

| Key | String (en) | Notes |
|---|---|---|
| `con.notice.title` | How we use your information | L |
| `con.notice.summary` | We use your details to {purposes}. We keep them for {retention}. You can ask to see, correct or erase them, or complain to the Data Protection Board of India. | L; DPDP s.5 |
| `con.purpose.service` | Run my case (needed) | L |
| `con.purpose.marketing` | Updates about Equator's services (optional) | L; unticked |
| `con.agree_to_mediate` | I agree to mediate under the Equator Mediation Rules (version {version}). I understand mediation is voluntary and I can stop at any time. | L |
| `con.s62.accept` | I accept the invitation to conciliation under Part III of the Arbitration and Conciliation Act, 1996. | L; s.62(2) |
| `con.no_recording` | I understand that mediation sessions are not recorded. | L; NN-11 |
| `con.online_mode` | I agree to take part online. | L |
| `con.arb_agreement.optional` | Optional: agree that a settlement can be recorded as an arbitral award. You don't have to sign this to mediate. You may want independent advice first. | L; K §5.5 |
| `con.s12_5.waiver` | Now that this dispute has arisen, I expressly agree in writing to waive the ineligibility of {arbitratorName} under section 12(5) of the Arbitration and Conciliation Act, 1996, for the reasons in the disclosure I have read. | L; NN-03 |
| `con.recording.arbitration` | Do you agree to this hearing being recorded? It will be recorded only if every party and the tribunal agree. | L; NN-11 |
| `con.age` | Are you 18 or older? | DPDP s.9 |
| `con.withdraw` | Withdraw consent for {purpose}. This stops future use; it doesn't undo what was lawfully done before. | L; DPDP s.6(4) |

### 4.10 AI-draft labels (`ai`)

| Key | String (en) | Notes |
|---|---|---|
| `ai.banner.draft` | Drafted by AI — requires human review | NN-01; AiDraftBanner |
| `ai.banner.detail` | Prepared from {sources}. Check every line. Nothing is sent until you approve it. | NN-25 |
| `ai.source.anchor` | Source: {document}, page {page} | NN-25 |
| `ai.gap` | Not found in your documents — add the fact or leave it out. | NN-25 |
| `ai.section.approve` | I've checked this section and I am its author. | L; NN-25 |
| `ai.award.outline` | AI-prepared outline. The arbitrator writes, decides and signs the award. | NN-01 |
| `ai.translation.label` | Translation for convenience. The original in {language} prevails. | NN-32 |
| `ai.typecopy.label` | Type copy prepared from {original}. Confidence: {band}. Uncertain words are marked. | NN-32 |
| `ai.unavailable` | AI help is unavailable right now. Continue with the step-by-step form — your result will be the same. | NN-02 |
| `ai.no_merits` | This tool organises your facts. It can't tell you whether your case is strong; an advocate can advise you. | NN-01 |

### 4.11 Publication consent (`pub`)

| Key | String (en) |
|---|---|
| `pub.ask.title` | May we publish this outcome? |
| `pub.ask.body` | If every party agrees, we'll publish a version with names and identifying details removed. You'll see that version before anything is published. (L) |
| `pub.option.full` | Yes, publish the redacted version |
| `pub.option.digest` | Only a short anonymised summary |
| `pub.option.no` | No, don't publish |
| `pub.no_effect` | Your choice doesn't affect your case or how anyone treats you. |
| `pub.waiting` | Waiting for the other parties. Nothing is published unless everyone agrees. |
| `pub.withdraw` | Withdraw consent. We'll remove it from our website; we can't recall copies others have already made. (L) |
| `pub.blocked` | Outcomes in family, health and similar matters are never published in full. |

### 4.12 Representative authority (`rep`)

| Key | String (en) |
|---|---|
| `rep.appoint.title` | Appoint someone to act for you |
| `rep.type.advocate` | An advocate — we'll check their Bar Council enrolment |
| `rep.type.other` | Someone else — a family member, HR officer or company officer |
| `rep.scope.intro` | Choose what they can do. You can change this at any time. (L) |
| `rep.scope.file` | File and respond on my behalf |
| `rep.scope.attend` | Attend sessions and hearings |
| `rep.scope.notices` | Receive notices for me (you'll get copies too) |
| `rep.scope.sign` | Sign procedural papers, such as filings and replies (not a settlement or other instrument) (L; X-21) |
| `rep.scope.settle` | Negotiate and agree settlement terms up to {amount} (L) |
| `rep.limit.explain` | Above this amount, you'll need to approve it yourself. You sign the settlement yourself unless a stamped, notarised power of attorney has been verified. (L; NN-27; X-21) |
| `rep.pending` | Waiting for {repName} to accept. |
| `rep.revoke` | Cancel their authority. They lose access straight away; what they did before stays valid. (L) |
| `rep.foreign_counsel` | Foreign lawyers may act only in international commercial arbitration, on foreign or international law, for clients whose principal office is abroad. (L) |

### 4.13 Signposting, safety and clocks (`sig`, `saf`, `clk`)

| Key | String (en) |
|---|---|
| `sig.card.title` | A free public option may suit you better. Here it is. |
| `sig.card.cost` | Cost: free |
| `sig.card.lawyer` | Do I need a lawyer? {answer} |
| `sig.card.last_date` | Last date to act: about {date}. Confirm it with the forum or an advocate. |
| `sig.no_stop` | Mediation does not stop these dates. (L) |
| `saf.quick_exit` | Leave this page |
| `saf.danger` | If you're in danger now, call 112. |
| `saf.fraud` | Money being taken by fraud right now? Call 1930. |
| `saf.safe_contact` | Only use an email or phone that nobody else checks. |
| `clk.pill` | {n, plural, one {# day left} other {# days left}} — {state} |
| `clk.expired` | Expired on {date}. See your remaining options. |
| `clk.owner` | Owner: {owner} |
| `clk.not_paused` | Talking with the other side doesn't pause this date. (L) |

**Count:** 16 + 11 + 57 (19 states × 3) + 5 + 17 + 19 + 11 + 16 + 13 + 10 + 9 + 13 + 13 = **210 strings**.

---

## 5. UI/UX copy and minimalist design principles

Appendix C §E (tokens, type, spacing, components) and §F (UX principles) remain binding; this section adds the copy-design rules and measurable budgets for the website and the apps.

### 5.1 Principles, rules and tests

| ID | Principle | Rule | Test / measure |
|---|---|---|---|
| UX-01 | Calm minimalism | One primary action per screen; one accent colour (`brand.teal` for actions) on a white or `surface.alt` field; no carousels, autoplay video, pop-up modals on entry, countdowns or chat bubbles that open by themselves | Visual-regression snapshots; LINT-033 (timers), LINT-034 (auto-open modal) |
| UX-02 | Fewer clicks | Journey budgets below; any change that adds a step needs a product-owner ADR | Playwright step counters per journey |
| UX-03 | Progressive disclosure | Lead with what the person must decide; put legal detail behind "Why?" disclosures, glossary pop-overs and a "Sources" accordion. **Never** hide fees, limits, "what we can't do", free-forum cards or consent text behind a disclosure | Content audit; LINT-036 (consent text inside collapsed element) |
| UX-04 | Plain language | English at Flesch–Kincaid grade ≤ 8, ≤ 20 words per sentence, ≤ 4 sentences per paragraph on party-facing pages; Hindi reviewed for the same level; legal terms explained on first use | LINT-050 readability gate (warn on enterprise pages, block on party pages) |
| UX-05 | Ask once | Carry Explorer answers into filing; prefill from DigiLocker/MCA/GSTIN lookups; never ask for identity documents before the route and fee are shown (WCAG 3.3.7; S9 FR-S9-19) | E2E redundant-entry test |
| UX-06 | Accessible by default | WCAG 2.2 AA floor incl. 2.4.11, 2.5.7, 2.5.8 (44 × 44 px touch), 3.2.6, 3.3.7, 3.3.8; RPwD Act 2016 ss.40, 42, 46; captions and transcripts for all video; no meaning by colour alone | axe CI zero serious/critical; manual NVDA/VoiceOver/TalkBack scripts |
| UX-07 | Vernacular and low bandwidth | Language switch on every page; notice-link pages ≤ 50 KB and usable without JavaScript; text-first lists; images off in low-bandwidth mode | Lighthouse throttled runs; payload budget CI |
| UX-08 | Status first | Every case screen leads with the current stage, the "what happens next" sentence with a date, and the `WhoDecidesChip` (S9 §5.4) | Snapshot test per state (§4.4) |
| UX-09 | Show the evidence | Hash, timestamp, e-stamp and signature badges on every outcome document; AiDraftBanner until a human accepts; ReviewStamp on legal pages | Component tests |
| UX-10 | No dark patterns | None of the 13 CCPA patterns (Dark Patterns Guidelines 2023): equal visual weight for decline/cancel/free-forum choices; no pre-ticked boxes; no basket sneaking; no nagging (≤ 1 upgrade prompt per user per 7 days; none in case or hearing views) | LINT-031–LINT-037; quarterly self-audit export (FR-S9-12) |
| UX-11 | Safety | QuickExit on FAM, POSH-linked, safety-flagged and sealed screens; neutral notification text; no trackers on those pages | E2E QuickExit test; tag-manager allow-list test |
| UX-12 | Consistent help | "Help" in the same place on every screen; "Talk to our case team" reachable within two taps from any party screen | WCAG 3.2.6 check |
| UX-13 | Neutral interface | Directory in seeded-random order within filters; no outcome statistics; enterprise screens never offer neutral selection | NN-16/NN-28 tests |
| UX-14 | Calm errors | What happened · what you can do · reference; entered data preserved; no red full-screen error pages for recoverable errors | Error-state snapshots |

**Journey budgets (UX-02).**

| Journey | Budget |
|---|---|
| Home → first Explorer question | 1 tap |
| Explorer start → result page (typical matter) | ≤ 13 universal pages + ≤ 8 vertical pages; most users under five minutes (K §1.1) |
| Notice link → signed consent (respondent) | ≤ 3 screens (K PL-06) |
| Quote → payment confirmation | ≤ 3 screens |
| Settlement ready → signed (one signer) | ≤ 3 screens plus the eSign provider's own steps |
| Reminder message → in the session room | ≤ 2 taps |
| `/track` → status shown | 3 steps (number → OTP → status) |
| Settings → plan cancelled | ≤ 3 steps (S9 §3.4) |
| Appoint a representative | ≤ 5 screens including e-sign |

### 5.2 Visual and content style

- **Tokens:** Appendix C §E.1 (navy/teal/gold, clock tokens, sealed token) prevail (P-D09); tenants may change `brand.*` only.
- **Type:** Inter + Noto families; body 15 px Latin / 16 px Indic; reading pages max line length 72 characters; marketing grid max 1,200 px.
- **Imagery:** real, consented photographs of people across India in ordinary settings, or simple line illustrations of conversation and documents. **Never** gavels, scales of justice, courtrooms, judges' robes, handcuffs or police imagery for Equator (brand rule; GX-4). No stock "handshake over money".
- **Icons:** Lucide, 1.5 px stroke, always labelled.
- **Motion:** 150–250 ms ease-out; none under `prefers-reduced-motion`.
- **Numbers and dates:** Indian grouping (₹1,27,500); "12 Nov 2026"; times with zone where parties differ.

### 5.3 Writing patterns

| Element | Pattern | Example |
|---|---|---|
| Page heading (task pages) | The user's question or task | "Who are you in this?" |
| Button | Verb + object | "Sign settlement" · "Pay ₹2,950" |
| Link | Says where it goes | "See all fees", never "Click here" |
| Hint text | One sentence | "Your best estimate is fine." |
| Optional field | "(optional)" in the label; no asterisks | "Your PAN (optional)" |
| Dates to act | Absolute date + days left + source | "2 Apr 2027 (164 days) — RBI Ombudsman scheme" |
| Who decides | Chip text | "You and the other side decide" |
| Limits | Next to the benefit, same size | "We help you agree the terms. Only the Family Court can grant the divorce." |
| Free forum | Before Equator options, equal visual weight | SignpostCard |

### 5.4 Content components (CMS blocks and app components)

| Component | Props (required) | Rules |
|---|---|---|
| `AnswerFirst` | `question`, `answer` (≤ 2 sentences), `reviewedOn`, `reviewer`, `facts[]`, `steps[]`, `sources[]` (citation IDs), `cta` | Answer must name the free forum first where one exists (LINT-021) |
| `SignpostCard` | `forumCode` (from routing directory), `lastDateRuleId` | Text from the signposting directory only; no free-text forum names |
| `WhoDecidesChip` | `mechanism` | Text is a constant per mechanism |
| `FeeTeaser` / `FeeTable` | `tariffItemCodes[]`, `audience` (b2c/b2b) | Values only from the fee engine; b2c shows incl. GST |
| `ClaimNode` (inline) | `claimKey` | Publish blocked if claim inactive (FR-P13-10) |
| `LegalCitation` | `legalRuleId` or `citationId` | Renders instrument, section, date, source link |
| `FlagSwapBlock` | `flagKey`, `offContent`, `onContent` | Swaps on flag change; both variants legally approved before publish |
| `ReviewStamp` | `reviewedOn`, `reviewerName`, `credential` | Mandatory on `legal_content = true` |
| `StatBand` | `metricKeys[]` | Metrics feed claims only; honest empty state |
| `IdentityStrip` | — | Fixed text (§3.0) |

---

## 6. SEO, GEO and AI-search content system

### 6.1 Operating principles (2026)

1. **Classic SEO fundamentals first.** Google states that AI Overviews and AI Mode need no special schema, files or optimisation; structured data must match visible text; control with `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` (S9 G-1). Equator therefore invests in crawlable SSR pages, clear entities, answer-first content, citations and speed — not "GEO markup".
2. **Citable, verifiable content wins generative answers.** Research on generative-engine optimisation found that adding citations, quotations and statistics improved visibility in AI answers, while keyword stuffing did not (Aggarwal et al., *GEO: Generative Engine Optimization*, KDD 2024; S9 G-7). Equator's statute-cited, register-bound style is the strategy; statistics appear only from the metrics feed.
3. **One entity, described the same way everywhere** (§6.2).
4. **No scaled thin content.** Programmatic pages only where real local facts exist (§6.7; Google spam policies on scaled content abuse, March 2024).
5. **Honesty beats position.** A page that would need a misleading claim to rank is not published (NN-17).

### 6.2 Entity consistency (config `seo.entity`, single source)

| Item | Value / rule |
|---|---|
| Legal name | `{{entity.legal_name}}` = Equator Resolution Service Private Limited; `Organization.legalName`; `identifier` = CIN (PropertyValue `propertyID` "CIN") — identical on MCA, GST, LinkedIn, Google Business Profile, press kit |
| Brand | "Equator Resolution" only (never Equa, Equa.Law) |
| URL | `https://equatorresolution.in` canonical; `.com` 301 → `.in` (X-14) |
| Slogan / description | A-01 / A-03 |
| Parent | `parentOrganization` Infrabyx Group only if approved by the Company Secretary |
| Training arm | Equator ADR Institute as a separate `EducationalOrganization` only on its own site; on Equator's site, a plain link with disclosure (P-D08) |
| `sameAs` | Only owned, verified profiles (LinkedIn, YouTube, X, Wikidata if created); reviewed quarterly |
| NAP | Office addresses exactly as on GST registration, from `{{entity.offices}}` |
| Neutral and author profiles | `Person` with `memberOf` Equator; credentials as `hasCredential`; no `aggregateRating` |
| Logo | One SVG/PNG set; `logo` ImageObject 512 × 512 |

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://equatorresolution.in/#org",
  "name": "Equator Resolution",
  "legalName": "{{entity.legal_name}}",
  "identifier": {"@type": "PropertyValue", "propertyID": "CIN", "value": "{{entity.cin}}"},
  "url": "https://equatorresolution.in",
  "logo": "https://equatorresolution.in/brand/logo-512.png",
  "slogan": "Resolve disputes, not relationships.",
  "description": "Online mediation, conciliation and arbitration — fair, fast and on the record.",
  "contactPoint": [{"@type": "ContactPoint", "contactType": "customer support", "email": "{{entity.email_general}}", "telephone": "{{entity.phone}}", "availableLanguage": ["en", "hi"]}],
  "sameAs": ["{{entity.same_as[]}}"]
}
```

### 6.3 Answer-first content block (mandatory on hubs, subtypes, mechanisms and help articles)

| Slot | Rule | Example |
|---|---|---|
| H1 / question | The user's words | "My NBFC sent me a legal notice. What can I do?" |
| Answer | ≤ 2 sentences; neutral; names the free forum first | "You can reply to the lender, complain to its grievance officer and then to the RBI Ombudsman for free, or try conciliation if both sides agree. Equator is a private institution; we can host a conciliation but we do not act for either side." |
| Review line | "Last legally reviewed on {date} by {name}, {credential}" | "…by [legal reviewer], Advocate" |
| Key facts | Table of deadlines, cost, documents, each with a citation | RB-IOS 2026 timelines; fee tokens |
| Steps | Numbered, one action each | — |
| Sources | Statute/regulator links via citation IDs | India Code; rbi.org.in |
| CTA | One primary | "Understand your options — free" |

### 6.4 Structured-data policy (amends FR-P13-13; P-D03, P-D04)

| Page type | Emit | Required properties | Never emit |
|---|---|---|---|
| All pages | `Organization` (by `@id` reference), `BreadcrumbList` (except home) | — | `LegalService` (unless flag ON), `Review`, `AggregateRating` |
| Home | `Organization` (full), `WebSite` | `name`, `url`, `inLanguage` | `SearchAction` (no sitelinks search box value) |
| Hubs, subtypes, mechanisms, organisation pages | `Service` | `serviceType`, `provider` → `#org`, `areaServed`, `availableChannel`, `termsOfService` → `/rules` | `offers` with any price not from the fee engine |
| SaaS pages (P-32–P-34) | `Service` + `SoftwareApplication` | `applicationCategory` "BusinessApplication", `operatingSystem` "Web" | `aggregateRating` |
| Fees | `OfferCatalog` | Items generated from the published schedule, `priceCurrency` | Prices from CMS text |
| FAQs (any page) | `FAQPage` **optional** (no Google rich result since 7 May 2026) | Q/A text identical to visible text | Marketing claims inside answers without claim nodes |
| Neutral profiles, authors | `Person` | `name`, `jobTitle`, `memberOf`, `knowsLanguage`, `hasCredential` | Ratings, outcome statistics, `telephone` (personal) |
| Careers | `JobPosting` | `datePosted`, `validThrough`, `hiringOrganization`, `jobLocation`, `employmentType` | Salary unless approved |
| Training | `Course` only for Equator's own modules | `provider` → `#org` | `Course` for third-party providers |
| Rules | `DigitalDocument` | `version`, `datePublished`, `identifier` (SHA-256) | — |
| Published outcomes | `CreativeWork` (App. R §3.13) | `identifier` (citation), `datePublished`, `about` | Party `Person`/`Organization` markup; `LegalCase`/`Legislation` |
| How-to content | No `HowTo` markup (flag `seo.schema.howto_enabled` OFF) | — | — |

Validation: schema.org validator in CI on the 40 top templates; a parity test fails if any JSON-LD text value is absent from the rendered page text (G-1). `LegalService`, when the legal reviewer turns it ON, uses `knowsLanguage` and `contactPoint.availableLanguage` (never `availableLanguage` on the LegalService node).

### 6.5 `llms.txt` and Markdown twins (optional, low cost; flag `seo.llms_txt.enabled` ON after legal approval of listed pages)

`/llms.txt` follows the llmstxt.org proposal: H1 "Equator Resolution"; a blockquote summary (identity line + A-03); H2 sections listing links to Rules, Fees, Code of Conduct, How we stay neutral, the six hubs, mechanism pages, Glossary; an "Optional" section for help articles. Every listed page has a `.md` twin generated from the CMS, linked with `<link rel="alternate" type="text/markdown">`. Google ignores the file (G-1); it serves non-Google agents. The twins carry the same ReviewStamp and claim text; sealed, case and profile pages are never listed.

### 6.6 Multilingual and hreflang

One URL per language (`/hi/...`); never redirect by IP or browser language; `hreflang` en-IN, hi-IN (+ regional as published) and `x-default` → English; reciprocal links on every alternate; emitted only when both versions are `published` (FR-P13-13); translated `title` and meta description; `inLanguage` in JSON-LD per page; Devanagari slugs not used (ASCII slugs, translated H1); human legal review before any legal page goes live in a new language (NN-23). Hinglish search terms (e.g., "loan settle kaise kare", "salary nahi mila", "batwara") are covered in Hindi and English copy and the Explorer synonym index (K §2.3), not by separate Hinglish pages.

### 6.7 Programmatic pages governance (extends FR-P13-12)

| Rule | Detail |
|---|---|
| Eligibility | Dispute type enabled for the vertical; city in `growth.cities` with **real** local data from the signposting directory (DLSA, Consumer Commission, Family Court, DRT, MSEFC, Maintenance Tribunal, labour office addresses) |
| Uniqueness | ≥ 250 words of legally approved unique copy per (dispute type × language) plus ≥ 3 local FAQs; similarity to any sibling page ≤ 40% (5-word shingle Jaccard) — else not generated |
| Human sign-off | Each template and each unique block has a named author and legal reviewer; AI may draft, never publish (P13 §11) |
| Waves | ≤ 500 pages per week; indexation monitored; pages with no clicks after 3 months of impressions → `noindex` |
| Local honesty | Equator office NAP only where an office exists; no "near me" claims for cities without an office |
| Sample audit | 5% of live programmatic pages re-reviewed each quarter; one legal error suspends the template (kill switch `seo.programmatic.<template>.enabled`) |
| Exclusions | No programmatic pages for POSH, criminal-adjacent topics, child custody or any signpost-only subtype |

### 6.8 E-E-A-T, authorship and citations

Every article and explainer shows author and legal reviewer with credential cards (enrolment number verified through P03 where the author is a neutral), a conflicts statement and `Person` markup (FR-P13-11). Statute and case references use citation fields linked to the Legal Rules Register (FR-P13-09(b)); quotations from statutes are verbatim with section and source link (India Code, regulator site). An editorial policy page (`/about/editorial-policy`) explains authorship, review, AI use (drafting assistance only, human-authored and reviewed) and the corrections policy (§7.6).

### 6.9 Freshness

`dateModified` changes only on substantive edits (not on rebuilds); sitemap `<lastmod>` from content `updated_at`; "What changed" note on rules and legal pages; a statute-flag change (§7.4) or a Legal Rules Register update automatically queues every page citing that rule for re-review and shows "Updated for {instrument} on {date}" once approved.

### 6.10 Internal linking model

Hub-and-spoke: Home → six hubs → subtypes; every subtype links up to its hub, across to the two most relevant mechanism pages, and to `/fees` and `/rules`; every mechanism page links to the hubs where it is available (rendered from the routing matrix); organisation pages link to the matching hub and to GRM/POSH/API pages. Rules: every indexable page reachable within three clicks of Home; no orphans (CI crawl); descriptive anchor text (no "click here", LINT-045); breadcrumbs on every page except Home; related-content blocks chosen by taxonomy, not by "popular" counts.

### 6.11 Core Web Vitals and technical SEO

FR-P13-27 budgets apply (p75 LCP < 2.5 s on 4G mid-range Android, INP < 200 ms, CLS < 0.1, TTFB < 0.8 s; ≤ 170 KB JS per public route). Add: hero images ≤ 80 KB AVIF with explicit dimensions and `fetchpriority="high"` only on the LCP image; no client-side rendering of copy (FR-P13-14); canonical on every route; `noindex` on `/track`, `/verify/*`, `/r/*`, `/preferences/*`, `/app`, `/console`, search-result pages and thin filter combinations of the directory; IndexNow ping to Bing on publish (optional adapter).

### 6.12 AI-crawler policy (P-D07; Board approval required; `seo.ai_crawler_policy_version`)

| Agent (examples) | Purpose | Public explainers, rules, fees, hubs | Directory profiles, published outcomes, careers, people pages | Case, verify, account, preference routes |
|---|---|---|---|---|
| Googlebot, Bingbot | Search indexing | Allow | Allow (profiles indexable with consent; outcomes per publication policy) | Disallow + `noindex` |
| OAI-SearchBot, PerplexityBot, Claude-SearchBot | AI search answers | Allow | Allow | Disallow |
| ChatGPT-User, Perplexity-User and similar user-initiated fetchers | Fetch on a user's request (robots rules may not apply) | — (cannot be controlled reliably; rely on `noindex`/auth) | — | Authenticated only |
| GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot | Model training | **Allow** (default proposal) | **Disallow** | Disallow |

Robots rules change only through a Board-approved policy version; the change and its effective date are logged; the policy is reviewed every six months. OpenAI's crawlers are independently controllable and changes take about 24 hours to apply (S9 G-5).

### 6.13 Intent clusters (seed list for content planning)

| Vertical | Head intents (en) | Hindi / Hinglish intents |
|---|---|---|
| FIN | loan settlement letter; recovery agent harassment complaint; RBI ombudsman complaint loan; credit card dispute | लोन सेटलमेंट कैसे करें; रिकवरी एजेंट शिकायत; loan settle kaise kare |
| COM | unpaid invoice MSME interest; arbitration clause India; section 12A pre-institution mediation | बकाया भुगतान एमएसएमई; व्यापार विवाद मध्यस्थता |
| FAM | mutual consent divorce settlement terms; ancestral property division daughters; family settlement deed registration | आपसी सहमति तलाक; पैतृक संपत्ति बँटवारा; virasat batwara |
| INS | health insurance claim rejected what to do; insurance ombudsman complaint; motor claim depreciation dispute | बीमा दावा अस्वीकार; बीमा लोकपाल शिकायत; claim reject ho gaya |
| WRK | full and final settlement not paid; gratuity not paid complaint; workplace mediation | फुल एंड फाइनल नहीं मिला; ग्रेच्युटी शिकायत; salary nahi mila |
| INT | international arbitration India seat; mediation cross-border dispute; enforce foreign award India | — |

### 6.14 Measuring AI visibility (S9 §6.5)

Monthly panel of 50 fixed prompts per vertical in English and Hindi, run against ChatGPT search, Perplexity, Gemini and Google AI Mode; record: Equator cited (yes/no), URL cited, whether the answer is legally accurate, and whether the free forum is named. An inaccurate AI answer triggers a content fix on Equator's page (clearer answer-first block, citation), never a new claim. Results live in the growth database only (NN-16) and feed a monthly content backlog.

---

## 7. Content governance

### 7.1 Roles (RACI)

| Activity | Author (`cms_editor`) | Legal reviewer | Publisher | Claims owner | Translator | SEO lead | DPO |
|---|---|---|---|---|---|---|---|
| New or changed legal content | R | A (≠ author) | C | C | — | C | — |
| Claim creation / renewal | C | A for `legal_effect`, `regulatory_status` | — | R | — | — | — |
| Hindi / regional version | C | A (legal content) | C | — | R | C | — |
| Programmatic template | R | A | C | — | C | R | — |
| AI-crawler policy | — | C | — | — | — | R | C; Board approves (A) |
| Corrections | R | A | R | C | C | I | I (if personal data) |
| Privacy, cookie, DPA pages | R | A | C | — | C | — | A (joint) |

### 7.2 Claims Register in operation

Seed the register with Appendix H §6.1–6.2 keys plus the §1.6 keys before P13 go-live. Every claim has: canonical text per locale, type, evidence object (SHA-256) or source snapshot, owner, approver (≠ owner), `valid_from`, `expires_at` (statistics 35 days; others ≤ 12 months), permitted surfaces and a **fallback text** that renders when the claim expires (or the block is removed). Usage is tracked in `growth.claim_usages` so an expiring claim lists every page affected; owners are alerted at T-7. Gated lines in §2 and §3 (marked G / [GATED]) do not render until their claim is `active`.

### 7.3 Legal review checklist (reviewer must tick each before approval)

1. No line fails LC-1 to LC-8 (§2.1); lint report attached and clean (or overrides justified).
2. Every statute or case reference uses a citation field linked to an Appendix G rule ID.
3. Free or statutory forum named before Equator's options where the routing directory returns one (NN-20).
4. Limits stated next to benefits ("only a court…", "not regulated by…").
5. No fee figure, statistic, logo or testimonial outside a token or claim node.
6. Statute-commencement blocks use `FlagSwapBlock` with both variants approved (§7.4).
7. Sensitive topics (FAM, POSH, health, safety) carry QuickExit, no trackers, neutral notifications.
8. Hindi version (if any) has the same claim IDs, fee tokens and rule IDs (parity check passed).
9. **Brand test:** "Would this still be true, and still feel calm, if the reader were having the worst week of their life and had no lawyer?"
10. Reading level within §5.1 UX-04 limits, or justified for enterprise/legal documents.

### 7.4 Statute and feature-flag registry bound to copy

| Flag / rule | Copy while OFF (current) | Copy when ON | Who switches | Evidence required |
|---|---|---|---|---|
| `mediation_statutory_mode` / `mediation_act.s27.in_force` (NN-05, X-16) | "Sections 27–28 of the Mediation Act, 2023 are not yet notified; a mediated settlement is a binding contract." | P-23 ON text (s.27 enforcement, s.28 challenge); "MSA under section 19" label allowed | `legal_reviewer` + `institution_admin` (maker–checker) | Gazette notification S.O. number and date |
| `com.s12a_equator_authorised` (M-06) | WC-59 text; "does not replace that statutory step" | Legal reviewer drafts new copy only after all four M-06 gates close | Legal reviewer + Board | Ninth Schedule notification; MCI recognition; Central Government authorisation; new rules |
| `reg.mci` claim | "We will seek recognition from the Mediation Council of India when its registration framework is notified." (WC-28) | "Recognised by the Mediation Council of India as {status}." | Legal reviewer | MCI certificate |
| India's Singapore Convention ratification (`LR-INT-010`) | `law.singapore_status` text | Revised enforcement copy for INT pages | Legal reviewer | Instrument of ratification + implementing law |
| `com.msefc_referral_msp` (D2-26) | P-14 "changes coming" text | "Facilitation Councils can refer matters to Equator as a mediation provider." — only if Equator is listed | Legal reviewer | Commencement S.O.; Council listing |
| `fam.ucc_uk`, `fam.s15_prelit` (D2-27; V3) | No Uttarakhand UCC or s.15 pre-litigation copy | Module copy drafted by counsel | Legal reviewer | Official text; order text |
| Probate s.213 omission (D2-25) `copy.probate_s213_note` | No statement about probate being or not being compulsory | "Since 20 December 2025, probate is no longer legally required for wills that used to need it under section 213 of the Indian Succession Act (mainly wills made in, or dealing with property in, Mumbai, Kolkata and Chennai). Banks, housing societies and buyers may still ask for it." | Legal reviewer | [Verified 22 Oct 2026: Repealing and Amending Act, 2025 (No. 37 of 2025), s.3 and Second Schedule Sl. 3, India Code] |
| `ins.retail_conciliation` (V4) | Retail INS pages offer mediation only | Conciliation route cards appear | Legal reviewer | Counsel opinion Q-C9 |
| `academy.institute_referral` (A-03) | Institute card hidden | Card with relationship disclosure | Legal reviewer + Company Secretary | Institute website corrected; entity confirmed |
| `publication.arbitral.enabled`, `publication.consensual.enabled` (NN-26; App. R §3) | P-41 empty state | Library live | Legal reviewer | Counsel opinions Q-R1 (s.42A; 02 §5 Q1) and Q-R3; App. R §3 builder pass |
| `voice.equator_service_number.enabled` (NN-12) | "Calls about lender- or insurer-referred matters may come from your lender's or insurer's official number." | Adds Equator's declared numbers list on `/verify` | Legal + telecom | Operator confirmation; counsel opinion |
| `sec.smart_odr.enabled` | No SEC pages; WC-32 applies | SEC explainer and regulated fee table | Legal reviewer | SEBI empanelment letter |
| RBI NBFC conduct rules effective 1 Jan 2027 | "…under RBI rules that take effect on 1 January 2027 — we apply them now." | "…under RBI rules." (date-based auto-swap on 1 Jan 2027) | Scheduler + legal check | Rules `LR-RBI-005` to `LR-RBI-008` status |
| `seo.schema.legalservice_enabled`, `seo.schema.howto_enabled`, `seo.llms_txt.enabled` | P-D03/P-D04 defaults | As configured | Legal reviewer (LegalService); SEO lead (others) | ADR |

### 7.5 Update cadence

| Content | Review interval | Automatic triggers |
|---|---|---|
| Terms, privacy, cookies, DPA | 12 months | Law or processing change; sub-processor change |
| Regulatory explainers (RBI, IRDAI, SEBI, Labour Codes, POSH, UGC) and FIN/INS pages | 6 months | Legal Rules Register update for any cited rule |
| Other hubs, subtypes, mechanism pages | 12 months | Cited rule update; flag change |
| Fees and pricing | On every fee-schedule publish (event-driven ISR) | `equator.billing.fee_schedule.published.v1` |
| Statistics | Claim expiry 35 days | Monthly metrics snapshot |
| Neutral profiles | Annual re-verification | Credential change, grade change, complaint outcome |
| Programmatic pages | Quarterly 5% sample | Template change; local-data change in the signposting directory |
| Help and FAQs | 12 months | Product change touching the answer |
| AI-crawler policy | 6 months | New major crawler; Board decision |
| Translations | With the source | Parity check failure |
| Microcopy (§4) | With each release | Key added or changed; L-strings re-approved |

### 7.6 Corrections and takedown

A public corrections log at `/about/corrections` lists material corrections (date, page, what changed). Content with a legal-effect, regulatory-status or safety error is unpublished or corrected within **24 hours** of detection; other factual errors within **7 days** (mirrors Appendix H §5.0). Linter hits on the nightly production crawl page the on-call engineer (FR-P13-01(b)).

---

## 8. Acceptance checks — copy-lint rules and tests

### 8.1 Copy-lint rules (`packages/content-lint`; run in CMS on save, in CI on templates and i18n catalogues, nightly on the production crawl)

Severity **B** = blocks publish/merge; **W** = warning shown to reviewer. Overrides need a legal reviewer's reason and are audited; rules marked † cannot be overridden. The deck in §3 writes statutory periods and thresholds in plain text for readability; at CMS entry each is wrapped in a `LegalCitation` or `{{rule:…}}` token bound to its Appendix G rule ID, otherwise LINT-011, LINT-020 or LINT-024 fire. LINT-001's allow-list also passes sentences in which the reader or a public forum, not Equator, is the subject ("Before you go to court", "only a court can"). IDs LINT-027–LINT-030 and LINT-038–LINT-039 are reserved (unused).

| ID | Rule | Detection (en; Hindi equivalents in `lint/hi.yaml`) | Sev. |
|---|---|---|---|
| LINT-001 | Court/judge/decree/tribunal framing of Equator | `\b(court\|judge\|decree\|tribunal\|judicial)\b` (+ न्यायालय, अदालत, न्यायाधीश, डिक्री) unless inside `LegalCitation`, a quoted statute, or a sentence whose subject matches the public-forum allow-list ("Family Court", "Consumer Commission", "only a court", "the court decides", "the tribunal"/"arbitral tribunal" meaning the arbitrators…), or a credential phrase ("retired judge of", "former judicial office", "judicial service") on directory, grading or neutral-profile content | B |
| LINT-002 | Retired brands and court naming | "People's Court", "Equa", "Equa.Law", "Private ADR Court", "Equator Assurance", "Global presence" | B† |
| LINT-003 | Regulator endorsement | `(RBI\|Reserve Bank\|SEBI\|IRDAI\|MCA\|UGC\|NALSA)\W+(\w+\W+){0,3}(approved\|audited\|certified\|compliant\|designated\|preferred\|recognised\|registered\|partnered)` (+ आरबीआई द्वारा अनुमोदित) | B† |
| LINT-004 | Over-binding | "100% (legally )?binding", "final and binding" within 10 words of mediat* | B† |
| LINT-005 | Guarantees and side-taking | guarante*, "we will (win\|recover\|get you)", "make them pay", "fight for you" | B |
| LINT-006 | Unnotified Mediation Act effects | "section 27", "s\.? ?27", "enforceable as a (decree\|judgment)", "MCI (registered\|recognised\|accredited)", "Mediation Act (2023 )?compliant", "statutory (pre-litigation )?mediation", "MSA under section 19" — while `mediation_statutory_mode` OFF | B† |
| LINT-007 | s.12A claims | "12A (compliant\|certificate\|report)", "satisf\w+ (section\|s\.) ?12A", "non-starter report", "pre-institution mediation" with Equator/we as subject — while `com.s12a_equator_authorised` OFF | B† |
| LINT-008 | Singapore Convention | "Singapore Convention" within 8 words of enforc* unless followed by "not (yet )?ratified" | B† |
| LINT-009 | Limitation | "(pause\|stop\|freeze\|suspend)s? (the )?(limitation\|clock\|deadline\|time limit)" without negation | B† |
| LINT-010 | Merits, prediction, valuation | "strong case", "weak case", "good chance", "likely to (win\|succeed\|get)", "worth (pursuing\|₹)", "you will get", "recommended for your case", "best option" | B† |
| LINT-011 | Quantified speed, time, saving | `\d+\s*(day\|week\|month\|hour\|minute)s?` or `\d+\s?%` or "faster\|quicker\|cheaper than" outside `ClaimNode`, `LegalCitation`, `FeeToken` or clock components | B |
| LINT-012 | Superlatives | "best" (except the plan-card label "Best for:" and the legal phrase "best interests"), "leading", "No\.? ?1", "(India's\|the) (first\|largest\|only\|top\|biggest)", "most trusted", "world-class" outside `ClaimNode` | B |
| LINT-013 | Recovery and threat tone | "final warning", "legal action will follow", defaulter, arrest, "police will", "last chance" | B† |
| LINT-014 | Advice framing | consultation, "legal advice" (allowed only in "not legal advice"), "Resolution Expert", "our lawyers", "AI lawyer" | B |
| LINT-015 | Free trial | "free trial" outside `/private-adr-chambers` and `/pricing/professionals` | B |
| LINT-016 | POSH discouragement | "settle (it )?informally", "avoid the (IC\|Internal Committee)", "mediate (the )?harassment", "drop the complaint" | B† |
| LINT-017 | Children as bargaining | custody/access/children within 10 words of (payment\|money\|in exchange\|waive) in a proposal context | B |
| LINT-018 | Probate compulsion | "probate (is )?(mandatory\|compulsory\|required)" while `copy.probate_s213_note` OFF | B |
| LINT-019 | IFSC centre | "IFSC arbitration centre", "GIFT City (arbitration )?centre" | B† |
| LINT-020 | Typed fees | `₹\s?\d` on CMS pages outside `FeeToken`, `ClaimNode` or `LegalCitation` (statutory thresholds) | B |
| LINT-021 | Answer-first and free forum | Hub/subtype/mechanism/help page without `AnswerFirst`, or whose answer omits the signposting forum returned for that vertical/L1 | B |
| LINT-022 | Identity strip | Missing on hub, subtype, mechanism, Explorer pages | B |
| LINT-023 | Review stamp | `legal_content = true` without `ReviewStamp`, or review older than the cycle in §7.5 | B |
| LINT-024 | Free-text citations | Statute pattern (`Act,? \d{4}`, `s\.\s?\d+`, `section \d+`) outside a citation field | B |
| LINT-025 | Locale parity | Translated version references different claim IDs, fee tokens or rule IDs than the source | B |
| LINT-026 | Inactive claim | `ClaimNode` referencing a claim not `active` | B |
| LINT-031 | Confirm-shaming | "No thanks, I", "I don't (care\|want to save)", "risk losing", "I'll pay more" | B† |
| LINT-032 | Pre-ticked options | Checkbox/toggle for consent, marketing or paid add-on with default `true` | B† |
| LINT-033 | False urgency | Timer or countdown components; "offer ends", "only \d+ left" not bound to the promo ledger | B† |
| LINT-034 | Nagging | Auto-open modal on entry; > 1 upgrade prompt per user per 7 days; any upgrade prompt in case or hearing views | B |
| LINT-035 | Interface interference | Decline/cancel/free-forum action styled with lower emphasis than accept/continue where both are legitimate choices | B |
| LINT-036 | Hidden terms | Fee, consent or limitation text inside a collapsed element | B |
| LINT-037 | Bait and switch | Checkout amount ≠ quote hash without `QUOTE_EXPIRED` re-quote | B† |
| LINT-040 | Title length | `<title>` > 60 characters | B |
| LINT-041 | Meta length | Meta description > 155 characters or < 70 | B |
| LINT-042 | Uniqueness | Duplicate title or meta description across indexable routes | B |
| LINT-043 | Headings | Not exactly one `h1`; heading levels skipped | B |
| LINT-044 | Canonical | Missing or non-self canonical on indexable route | B |
| LINT-045 | Anchor text | "click here", "read more", "here" as full link text | W |
| LINT-046 | JSON-LD parity | Any JSON-LD string value not present in visible text | B |
| LINT-047 | Prohibited schema | `Review`, `AggregateRating`; `LegalService` or `HowTo` while their flags are OFF | B† |
| LINT-048 | hreflang | Missing reciprocal link, or alternate pointing to an unpublished locale | B |
| LINT-049 | Orphans | Indexable page with no internal inbound link, or > 3 clicks from Home | B |
| LINT-050 | Readability | FK grade > 8 or sentence > 30 words on party-facing pages (B); > 10 on enterprise pages (W) | B/W |

### 8.2 Acceptance tests (Gherkin; `tests/acceptance/p13/copy_*.feature`)

```gherkin
Feature: Appendix P copy deck, microcopy and SEO/GEO system

Scenario: P-D01 messaging hierarchy rendered
  When "/" renders in en-IN
  Then the eyebrow reads "Resolve disputes, not relationships."
  And the H1 reads "Resolve disputes online — fairly, quickly and enforceably."
  And Organization JSON-LD has slogan "Resolve disputes, not relationships."

Scenario: NN-17 quantified speed claim blocked
  Given an author writes "Settle your loan in 30 days" on the FIN hub
  When the page is saved
  Then LINT-011 fails with CLAIM_NOT_EVIDENCED
  And the page cannot enter in_legal_review

Scenario: NN-05 Mediation Act copy swaps with the flag
  Given mediation_statutory_mode is OFF
  When "/mechanisms/mediation" renders
  Then it states that sections 27–28 of the Mediation Act, 2023 are not yet notified
  When a legal reviewer and an institution admin switch the flag ON with a Gazette reference
  Then the approved ON text renders after ISR revalidation
  And every page citing LR-MED-012 is queued for re-review

Scenario: M-06 section 12A claim blocked in Hindi and English
  Given com.s12a_equator_authorised is OFF
  When an author adds "Equator's mediation satisfies section 12A" to "/mechanisms/pre-litigation-mediation"
  Then LINT-007 blocks publish and cannot be overridden

Scenario: NN-20 answer-first block names the free forum
  When "/disputes/insurance/health-claim-rejected" renders
  Then the AnswerFirst answer names the Insurance Ombudsman before any Equator service

Scenario: Structured data policy
  Given seo.schema.legalservice_enabled is OFF
  When any vertical hub renders
  Then its JSON-LD contains a Service with provider "#org"
  And contains no LegalService, Review, AggregateRating or HowTo node
  And every JSON-LD string value appears in the visible page text

Scenario: Title and meta limits across the deck
  When the SEO lint runs over every route in §3.1
  Then no title exceeds 60 characters and no meta description exceeds 155 characters
  And no two indexable routes share a title or meta description

Scenario: AI-crawler policy applied
  Given AI-crawler policy version 1 is Board-approved
  When "/robots.txt" is fetched
  Then OAI-SearchBot and PerplexityBot are allowed on "/disputes/"
  And GPTBot and CCBot are disallowed on "/neutrals/" and "/decisions/"
  And all agents are disallowed on "/app", "/r/" and "/verify/"

Scenario: Training page neutrality
  Given academy.institute_referral is OFF
  When "/training" renders
  Then at least three recognised training options are shown in random order
  And no Equator ADR Institute card is shown
  And the page states that no provider is required for empanelment

Scenario: Sensitive notification variant
  Given a FAM case moves to "in_proceedings"
  When the status notification is sent by SMS
  Then the body equals ntf.status.sensitive with no party name, amount or subject

Scenario: Status explanation coverage
  When the i18n coverage test runs for en-IN and hi-IN
  Then every case state in master §5.1 has sts.<state>.label, .explain and .next
  And every L-flagged string has a legal approval record in both locales

Scenario: Dark pattern — cancel plan has equal weight
  When "Settings → Billing → Cancel plan" renders
  Then "Cancel plan" and "Keep plan" use the same button variant
  And the flow completes in no more than 3 steps

Scenario: Published outcomes gated
  Given publication.arbitral.enabled and publication.consensual.enabled are OFF
  When "/decisions" renders
  Then the empty state "We will publish outcomes only where every party has agreed. None are published yet." is shown
  And the page has no CreativeWork item JSON-LD

Scenario: Respondent first-session claim gate
  Given claim svc.first_session_free_respondent is not active
  When "/respond" renders
  Then the cost sentence falls back to "The cost, if any, is shown in your invitation before you agree."

Scenario: Programmatic similarity guard
  Given a city page whose unique block shares 55% of 5-word shingles with a sibling
  When the weekly wave runs
  Then the page is not generated and the template owner is notified
```

---

## Phase addendum (paste into P13)

**FR-P13-V2-01 — Copy deck implementation.** Build every page in §3.1 (P-01–P-48) with the §3 copy as CMS seed content (en; hi hero lines), the field set (SEO title, meta, H1, hero, sections, CTAs, FAQs, schema, internal links) and the templates in §3 (hub, subtype, mechanism, organisation rules). *Acceptance:* every route returns SSR HTML with the seeded H1 and hero; each page version has a legal approval record; Hindi hero lines exist for every page and pass translator + legal review before `/hi/` publication.

**FR-P13-V2-02 — Messaging hierarchy (P-D01, P-D02).** Brand line A-01 in the logo lock-up, home eyebrow, footer, OG images and `Organization.slogan`; descriptor A-03 as home meta/OG description; positioning line A-02 as home H1; identity strip on every hub, subtype, mechanism and Explorer page. *Acceptance:* §8.2 "P-D01 messaging hierarchy rendered" passes; LINT-022 green.

**FR-P13-V2-03 — Catch-line library.** Load §2 lines into a CMS snippet library with fields `line_id`, text, use, check codes, gate/claim key, status; gated lines render only when their claim is `active`; rejected lines (§2.8) seed the deny-list. *Acceptance:* inserting any §2.8 line fails lint; a gated line with an inactive claim renders nothing.

**FR-P13-V2-04 — Routes and redirects (P-D05).** Readable vertical slugs with 301s from `/disputes/{fin,com,fam,ins,wrk,int}`; `/training` canonical with `/academy` 301; `/published-outcomes` 301 → `/decisions` (App. R §3.9.1); `/about/governance`, `/about/corrections`, `/about/editorial-policy`, `/pricing/organisations`, `/pricing/professionals` live; bare `/pricing` keeps the WR-02 301 to `/fees`. *Acceptance:* redirect map test covers every legacy and alias route; no redirect chains longer than one hop.

**FR-P13-V2-05 — Organisation disclaimers.** Segment-specific regulatory-status disclaimer component in the first screen of P-28–P-34; F-01 never rendered in a block containing a regulator name or logo. *Acceptance:* DOM test for each organisation page; lint rule fails when F-01 and a regulator name share a block.

**FR-P13-V2-06 — Claims Register seeds.** Create the §1.6 claim keys (including fallbacks) alongside Appendix H §6 keys; wire `ClaimNode` usages from §2–§3. *Acceptance:* every `{{claim:…}}` in the seeded content resolves to a register row; expired-claim fallback test passes for `svc.first_session_free_respondent`.

**FR-P13-V2-07 — Copy-lint expansion.** Implement LINT-001–LINT-050 (§8.1) in `packages/content-lint` for en and hi, running in the CMS on save, in CI on templates and i18n catalogues, and nightly on the production crawl; † rules non-overridable; overrides audited. *Acceptance:* a fixture corpus with one violating sentence per rule yields exactly the expected rule IDs; zero false positives on the §3 seed content.

**FR-P13-V2-08 — Brand test and review checklist.** Add the §7.3 ten-item checklist (including the brand test) as mandatory reviewer ticks in the `in_legal_review → legally_approved` transition. *Acceptance:* approval API rejects with `VALIDATION_FAILED` when any item is unticked.

**FR-P13-V2-09 — Content components.** Ship `AnswerFirst`, `SignpostCard`, `WhoDecidesChip`, `FeeTeaser/FeeTable`, `ClaimNode`, `LegalCitation`, `FlagSwapBlock`, `ReviewStamp`, `StatBand`, `IdentityStrip` per §5.4, shared by web and the docs portal. *Acceptance:* Storybook stories with axe checks; LINT-021 enforces `AnswerFirst` on hubs, subtypes, mechanisms and help articles.

**FR-P13-V2-10 — Structured-data policy (amends FR-P13-13 and the P13 exit gate).** Emit types per §6.4; `LegalService` behind `seo.schema.legalservice_enabled` (OFF); `HowTo` behind `seo.schema.howto_enabled` (OFF); `FAQPage` optional; validation with the schema.org validator and a JSON-LD/visible-text parity test (replaces the Rich Results Test item in the exit gate). *Acceptance:* §8.2 "Structured data policy" passes on all templates.

**FR-P13-V2-11 — Entity configuration.** `seo.entity` single source (§6.2) feeding footer, contact page, Organization JSON-LD, OG tags and press kit; build fails on missing CIN or a non-domain email. *Acceptance:* changing `entity.legal_name` in config updates every surface in one deploy; snapshot test.

**FR-P13-V2-12 — `llms.txt` and Markdown twins.** Generate `/llms.txt` and `.md` twins for listed pages from the CMS when `seo.llms_txt.enabled` is ON; never list sealed, case, profile or outcome pages. *Acceptance:* file validates against the llmstxt.org structure; each listed URL has a reachable twin with the same ReviewStamp.

**FR-P13-V2-13 — AI-crawler policy.** Versioned, Board-approved robots policy per §6.12 rendered into `/robots.txt` and page-level meta robots; change log with effective date. *Acceptance:* §8.2 "AI-crawler policy applied" passes; policy version shown in `/trust`.

**FR-P13-V2-14 — Programmatic governance additions.** Similarity threshold (≤ 40%, 5-word shingles), human sign-off per template and unique block, quarterly 5% sample audit, per-template kill switch, and exclusion of POSH, criminal-adjacent, custody and signpost-only subtypes. *Acceptance:* §8.2 "Programmatic similarity guard" passes; excluded subtypes never generate pages.

**FR-P13-V2-15 — Freshness and re-review triggers.** Legal Rules Register updates and flag changes queue every citing page for re-review; `dateModified` only on substantive change; "What changed" notes on rules and legal pages; cadence jobs per §7.5. *Acceptance:* updating `LR-IRDAI-003` queues P-07 and P-13 for review within 5 minutes; sitemap `lastmod` unchanged by a no-content rebuild.

**FR-P13-V2-16 — Internal linking CI.** Crawl-based checks for orphans and > 3-click depth, related-links by taxonomy, descriptive anchors (LINT-045, LINT-049). *Acceptance:* CI fails when a new indexable page has no inbound link.

**FR-P13-V2-17 — AI visibility panel.** Monthly job running 50 prompts × vertical × (en, hi) against configured AI search engines; stores citation, URL, accuracy and free-forum mention in the growth DB; generates a content backlog. *Acceptance:* first panel report produced in staging with synthetic runs; no case data in prompts or results (NN-16 schema validator).

**FR-P13-V2-18 — Statute/flag copy registry.** Implement §7.4 rows as `FlagSwapBlock` bindings with both variants approved before publish; date-based swap for the RBI conduct rules on 1 Jan 2027. *Acceptance:* §8.2 "NN-05 Mediation Act copy swaps with the flag" passes; a `FlagSwapBlock` lacking an approved ON variant cannot publish.

**FR-P13-V2-19 — Corrections log and takedown SLA.** `/about/corrections` page and workflow; legal-effect/safety corrections within 24 hours, others within 7 days; nightly linter hits page on-call. *Acceptance:* a seeded legal-effect error opened at 10:00 shows an SLA breach alert at 10:00 next day if not closed.

**FR-P13-V2-20 — Training referral page.** `/training` with ≥ 3 provider cards from configuration in random order, Institute card gated by `academy.institute_referral` with disclosure, Equator QAP status from `qap.not_yet_imi_approved`, `Course` markup only for Equator's own modules. *Acceptance:* §8.2 "Training page neutrality" passes.

**FR-P13-V2-21 — Published outcomes copy.** Copy layer (P-41) for the `/decisions` Library built under FR-P13-V2-R01 (App. R §3.9), gated by `publication.arbitral.enabled` / `publication.consensual.enabled`, with honest empty state, consent-only items, redaction profile, "not precedent" notice and citation format. *Acceptance:* §8.2 "Published outcomes gated" passes; no item renders without an all-party consent record.

**FR-P13-V2-22 — Editorial policy page.** `/about/editorial-policy` covering authorship, legal review, AI assistance, claims and corrections (§6.8). *Acceptance:* page live, legally approved and linked from every article footer.

**FR-P13-V2-23 — App-store and social copy.** Store listings: name "Equator Resolution"; iOS subtitle "Mediation & arbitration online"; Google Play short description "Resolve disputes online: mediation, conciliation and arbitration in India."; full description built from A-03, the identity line and §3 P-01 sections; social bios use A-01 + A-03. All pass LINT-001–LINT-020. *Acceptance:* store-listing text stored in CMS with legal approval; lint report attached to the release ticket.

## Phase addendum (paste into P02)

**FR-P02-V2-P01 — Case status explanations.** Wire §4.4 `sts.*` strings (label, explain, next, who-decides) for every case state and the pre-litigation sub-states into the party workspace, `/track` and mobile, with values from the clocks service and read model. *Acceptance:* §8.2 "Status explanation coverage" passes in en-IN and hi-IN; no state renders without its "what happens next" sentence.

> FR-P02-V2-P01 and FR-P02-V2-R05 are one engine: Appendix R §1.4.11–§1.4.12 rule tables select the Appendix P `sts.*` strings (viewer-specific `.next` variants added to the P deck), and `DD-R-WHO-DECIDES` is the only who-decides vocabulary.

**FR-P02-V2-P02 — Respondent landing copy.** `/respond` and `/r/{code}` use P-20 copy, including the verification panel and the decline/"not involved"/free-forum choices with equal visual weight. *Acceptance:* LINT-035 green; a respondent reaches signed consent in ≤ 3 screens.

**FR-P02-V2-P03 — Explorer and filing microcopy.** Onboarding, consent, AI-draft, error and signposting keys in §4 are used verbatim (no inline strings); `L`-flagged keys require legal approval per locale. *Acceptance:* i18n lint finds zero hard-coded user-facing strings in Explorer and filing components.

## Phase addendum (paste into P05)

**FR-P05-V2-P01 — Payment and billing microcopy.** Quote, checkout, mandate, escrow, refund, waiver and dunning screens use §4.8 keys; individuals see `pay.quote.total_b2c` as the first line; businesses see `pay.quote.b2b`; the Board-approval banner renders while unapproved. *Acceptance:* checkout snapshot test shows total incl. GST first for a B2C quote; `ECOM_total_price_breakup` green.

**FR-P05-V2-P02 — Cancellation and confirmation copy.** Cancel-plan and withdraw-case dialogs use §4.7 strings with equal-weight buttons. *Acceptance:* §8.2 "Dark pattern — cancel plan has equal weight" passes.

## Phase addendum (paste into P07)

**FR-P07-V2-P01 — Notification templates.** Register §4.5 templates on DLT (service/service_billing tags) and as WhatsApp utility templates in en and hi; sensitive variants for FAM, POSH-linked, INS-health and safety-flagged matters; `ntf.recovery.footer` appended to every recovery-related message (NN-12). *Acceptance:* §8.2 "Sensitive notification variant" passes; a recovery-related SMS without the footer fails with `GRO_DETAILS_MISSING`.

## Phase addendum (paste into P12)

**FR-P12-V2-P01 — Mobile microcopy parity.** The mobile app consumes the same `packages/i18n` keys (§4) with no app-only strings for legal-effect content; push previews use the neutral variants for sensitive matters. *Acceptance:* key-coverage test shows 100% parity for `sts`, `pay`, `con`, `ai`, `pub`, `rep` namespaces between web and mobile.

---

## Open items and counsel questions (this appendix)

1. Board approval of the AI-crawler policy (P-D07) — default proposal in §6.12.
2. Counsel opinion on aggregated per-insurer quarterly statistics (S9 §10 Q11) before the P-30 transparency line goes live.
3. Counsel opinion on A&C s.42A consent for publication (02 §5 Q1; App. R Q-R1) before `publication.arbitral.enabled`.
4. "Court-ready" removed from the P-06 H1 (v2 review: unverified-profile and court-framing risk; X-34). Appendix H WC-33 replacement H1 must be aligned to "private and respectful" (the stricter text applies, §0.1).
5. Resolved 22 Oct 2026: Repealing and Amending Act, 2025 (No. 37 of 2025; 20 Dec 2025), s.3 and Second Schedule Sl. 3 (India Code) for the omission of Indian Succession Act s.213 before `copy.probate_s213_note` is switched ON.
6. Equator ADR Institute relationship statement and referral-fee position (A-03; D2-17) for the Training page card.
7. Appendix B line codes for `{{fee:FAM-STD.*}}`, `{{fee:WRK-POSH.*}}`, `{{fee:CH.*}}` and `{{fee:INT-MED.FILING}}` tokens used in §3 are created by the P05 seed with these names (the card tables define the amounts).
8. P-38, P-39 and P-41 were re-checked in the v2 review against Appendix R (route `/decisions`, citation `EQR/{YYYY}/{TYPE}/{NNNN}`, flags `publication.arbitral.enabled`/`publication.consensual.enabled`) and Appendix O (plan codes NEU-PANEL, CH-LITE…CH-INST, COUNSEL-FREE/PRO, FIRM-ENT; B2B-only opt-in settlement administration fee S-02); re-check again only if R or O change.
