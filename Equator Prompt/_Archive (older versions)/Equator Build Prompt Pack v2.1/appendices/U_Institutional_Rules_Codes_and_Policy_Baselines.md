# Appendix U — Institutional Rules, Codes and Policy Baselines (v2.1, 22 October 2026)

## U.0 Purpose, sources and status

**What this appendix does.** It turns the rules, codes and policies of Equator's earlier website (the "Equa" site, `sites.google.com/view/equalaw`, a brand of Infrabyx Consultancy (OPC) Private Limited, © 2022) into the baseline policy set for **Equator Resolution Service Private Limited**. For every document it records what is carried forward, what is corrected, and what is added to meet the law and the binding rules of this pack. It also gives the coding agent the CMS keys, versioning and approval workflow for each document.

**Sources.**
- The Equa site as captured on 22 October 2026: the Institutional Rules (cll.1–17), the Neutrals' Code of Professional Conduct, the Privacy Policy (cll.1–30), the Terms & Conditions (cll.1–18), Data Security & Compliance, the Pricing & Refund Policy, the Schedule of Fee, the Disclaimer, the ADR Clauses, How it works, Accreditation, Register as a Neutral, Private ADR Courts, the Council and Secretariat pages, the Resolve pages, Grievance Portals and Accessibility.
- **Not captured:** the Google Forms, `.docx` templates and the sample-settlements folder could not be loaded. Treat them as unavailable and do not reproduce them.
- The pack's binding texts:
  - master NN-01–NN-32 and X-01–X-42;
  - Appendix B (fees);
  - Appendix G (legal rules);
  - Appendix N §1 (governance) and §5 (Code of Conduct ECC-2026.1);
  - Appendix O (plans, refunds and billing copy);
  - Appendix Q (privacy and security);
  - Appendix R (publication);
  - Appendix S (identity and representatives);
  - Appendix J §J.5 (research of 22 Oct 2026).

**Status.** Every document here is a **draft for Board approval and review by qualified counsel**. None is legal advice, and none may be published until its approver in §U.1 has signed it off in the policy registry. Statutory references were checked as recorded in Appendices G and J. Any reference still marked **[VERIFY — open]** there stays open here.

**Precedence.** The master and `02` → Appendix G (law) → Appendix B (fees) → Appendix F (names and codes) → phase files → Appendix N §5 (the Code) → this appendix. Where this appendix restates a rule set elsewhere, the other file governs; this appendix only adds the policy wording.

---

## U.1 Document set, owners and approval

All documents live in the policy registry (`core.procedure_rules`, P00 FR-P00 Ruleset Studio; Appendix F §F.4.11). Rules:
- Each version is immutable once approved.
- A case pins the versions in force when it is filed or when a neutral is appointed (NN-21).
- Public pages render from the registry. Nobody edits rule or policy text in the CMS.

| # | Document (registry kind · version key) | Public URL | Equa source | Owner (maker) | Approver (checker) | Status | Product hooks |
|---|---|---|---|---|---|---|---|
| U-1 | Equator Resolution Rules (`procedure_rules` · `ERR-2026.1`) | `/rules` | Institutional Rules cll.1–17; How it works; File a claim / response | Registrar | Rules Sub-Committee, then Board | Draft (§U.2) | P02 intake, P04 engines, A clocks |
| U-2 | Code of Conduct for Neutrals (`code_of_conduct` · `ECC-2026.1`) | `/rules/code-of-conduct` | Neutrals' Code §§1–6 | Head of Institution | Rules Sub-Committee | Drafted in App. N §5; Equa additions in §U.3 | P03 appointment, N §7 complaints |
| U-3 | Code of Conduct for Case Managers and Staff (`staff_code` · `ESC-2026.1`) | `/rules/staff-code` | Rules cl.7.3 (Case Manager role); Secretariat page | Registrar | Board | New (§U.4) | Staff onboarding, P00 RBAC attestations |
| U-4 | Privacy Notice (`privacy_notice` · `EPN-2026.1`) | `/privacy` | Privacy Policy cll.1–30 | DPO | General Counsel | Draft (§U.5) | P01 consent, Q DSR flows |
| U-5 | Cookie Notice (`cookie_notice` · `ECN-2026.1`) | `/privacy/cookies` | None (the Equa link pointed to the Privacy Policy) | DPO | General Counsel | New (§U.5.9) | P13 consent banner |
| U-6 | Terms of Service (`terms_of_service` · `ETS-2026.1`) | `/terms` | T&C cll.1–18 | Company Secretary | General Counsel, then Board | Draft (§U.6) | P01 sign-up click-wrap |
| U-7 | Fees, Deposits, Cancellation and Refund Policy (`refund_policy` · `ERP-2026.1`) | `/fees/refunds` | Pricing & Refund Policy; Schedule of Fee notes | CFO | Board | Draft (§U.7) | P05, App. O RP-* codes |
| U-8 | Disclaimer and Use of the Word "Court" (`disclaimer` · `EDS-2026.1`) | `/disclaimer` | Disclaimer cll.1–5 | Company Secretary | General Counsel | Draft (§U.8) | P13 footer |
| U-9 | Information Security Statement (`security_statement` · `ESS-2026.1`) | `/trust/security` | Data Security & Compliance | CISO | CTO and General Counsel | Draft (§U.9) | P14 trust page |
| U-10 | Accessibility Statement (`accessibility` · `EAS-2026.1`) | `/accessibility` | Accessibility page | Head of Product | CEO | Draft (§U.10) | P13, P12 |
| U-11 | Model Dispute Resolution Clauses (`model_clauses` · `EMC-2026.1`) | `/rules/clauses` | ADR Clauses A–C and drafting checklist | Registrar | General Counsel | Draft (§U.11) | P09 clause API, P13 clause builder |
| U-12 | Grievance Redressal Policy for users of Equator (`grievance_policy` · `EGP-2026.1`) | `/grievance` | Privacy cl.30; Data Security grievance line | Grievance Officer | Company Secretary | New (§U.6.4) | P13 footer, Q DSR |
| U-13 | Publication Policy (`publication_policy` · `EPP-2026.1`) | `/rules/publication` | Rules cl.10.4 (unresolved note); Settlements & Awards page | Registrar | Transparency Sub-Committee; counsel on s.42A | Specified in App. R §3; summary §U.2.10 | App. R |
| U-14 | Allocation Policy (`allocation_policy`) | `/rules/allocation-policy` | Register as a Neutral; Grading | Panel manager | Appointments Sub-Committee | Specified in App. N §6 | P03 |
| U-15 | Institutional Committee Charter (`charter`) | `/about/governance/charter` | Equa Council and Secretariat pages | Company Secretary | Board | Outline in App. N §1.9; Equa lessons in §U.12 | N §1 |

The policy documents that management will prepare for certification readiness (information security policy set, vendor risk, incident response, retention schedule, business continuity) are listed in Appendix Q. They are internal and are not public pages. U-9 is the only public security text.

**Workflow (P00).** `draft → legal_review → approved → published → superseded`.
- Maker and checker are always different users.
- Approval records the approver, the date, the source references and the effective date.
- Publication writes a CloudEvent `equator.rules.policy.published.v1` and a hash-stamped PDF of the version to the evidence store.
- Material changes to U-4, U-6 or U-7 trigger a user notice 30 days before they take effect. Where the change needs fresh consent (DPDP s.6), they also trigger a re-consent prompt.

---

## U.2 Equator Resolution Rules (ERR-2026.1) — clause plan

The Equa Rules (17 clauses) give a usable skeleton:
- two routes into a case;
- electronic service;
- an early consultation call;
- a Case Manager;
- appointment and disclosure;
- NDAs;
- data-protection directions;
- cost heads;
- a New Delhi seat.

They lack most of the procedure an arbitral institution must publish, and several clauses conflict with the law. The plan below keeps the skeleton and fixes the defects. Clocks and numbers come from Appendix A §6.3. Do not restate them in the Rules text; render them from the clock catalogue so that the two can never diverge.

### U.2.1 Part A — General (applies to every process)

| Clause | Content | Equa 2022 → Equator 2026 |
|---|---|---|
| A1 Title, scope, version | "Equator Resolution Rules", version pinned per case (NN-21). They apply where (a) a contract names Equator, or (b) a party files and every other party accepts the invitation in writing or electronically. | Kept (Equa cl.1.3). Proceedings start on *acceptance of the Rules and the case terms*, not on acceptance of website T&C (Equa cl.1.4 corrected). |
| A2 Definitions | Party, representative, neutral, Case Manager, Registrar, Institutional Committee, communication, platform, award, settlement agreement, closure report, business day. | Equa cl.2 kept and extended. **Corrected:** an award is made by the arbitral tribunal, not "rendered by Equa" (A&C s.31). "Proceedings" is defined. |
| A3 Communications and service | Communications go through the platform. Notice by email and SMS/WhatsApp counts only where the receiving party has agreed to that channel or the contract provides for it. Deemed receipt follows the notice rules in P02 (Appendix A `deemed_service`). Time runs from the day after receipt. | Equa cll.3.4–3.6 ("deemed received on dispatch"; WhatsApp/Telegram for everyone) are **narrowed**. Deemed receipt on dispatch is unsafe against an unregistered respondent (A&C s.3), so the Rules use delivery evidence. |
| A4 Time | Computation excludes the first day. If the last day is not a business day, it rolls to the next business day. Statutory limits are never extended by the Rules (NN-04). | New. |
| A5 Language | English by default. Parties may agree any language Equator supports (App. L §7); translations are certified as App. L requires. | New (Equa gave English only in the T&C). |
| A6 Representation | Parties may act in person or appoint a representative under a Letter of Authority with defined scopes (App. S §4, NN-27). Advocates must be verified. Changes are notified to all parties. | Equa cl.14 kept and made specific. |
| A7 Case Manager and early call | A Case Manager is assigned within the Appendix A `cm_assign` time, and an orientation call is offered to every party. The Case Manager handles process only and gives **no advice on the merits** (NN-01). | Equa cl.7 (7-day consultation) kept as an orientation call. The truncated sentence on the site is completed. |
| A8 Confidentiality | Proceedings, documents and outcomes are confidential, subject to the law, enforcement needs and the Publication Policy (§U.2.10). Participants accept confidentiality terms by e-sign. Mediation sessions are never recorded (NN-11). | Equa cll.10.1–10.3 kept. **Corrected:** cl.10.4 (the "Whether we should publish an award" note) and the "decision posted on website" step on How it works are **deleted** and replaced by the opt-in Publication Policy. |
| A9 Data protection | Equator processes personal data under the Privacy Notice (U-4). Tribunals and mediators may issue data-security directions binding on participants. | Equa cl.12 kept. |
| A10 Costs | Cost heads: neutral fees, Equator administration fees, expert fees, legal and other costs, stamp duty and government charges. Arbitral allocation follows A&C s.31A. A pre-dispute "costs in any event" clause is void (s.31A(5)) and is never used in Equator templates. Mediation and conciliation costs are shared equally unless agreed otherwise. | Equa cll.11, 13 and 15 merged. The undecided "Option 1/Option 2" (cl.15 "Decide") is resolved. Who decides arbitral costs: the tribunal, not Equator. |
| A11 Fees and deposits | Fees under the published schedule for the case (Appendix B) and the Refund Policy (U-7). Deposits are payable before the stage they fund. | Equa Schedule of Fee figures (₹1,000 registration, graded per-session neutral fees) are **superseded** by Appendix B. See §U.7.3 for the mapping. |
| A12 Exclusion of liability | Equator, its staff and neutrals are not liable for acts or omissions in good faith in the conduct of a matter, except for fraud, wilful misconduct or gross negligence, or where the law does not allow exclusion. Nothing excludes a party's statutory rights. | Equa cl.16 and Disclaimer kept in substance. The site's typo ("international wrongdoings") is read as **intentional** wrongdoing and widened to gross negligence. The waiver "to the fullest extent under the A&C Act" is restated neutrally. Counsel to confirm against A&C s.42B (protection for good-faith acts of arbitrators). |
| A13 Seat and venue | For arbitration, the seat is New Delhi, India, unless the parties agree otherwise. Hearings are online by default; the venue does not change the seat. | Equa cl.17 kept; "facts and circumstances warrant otherwise" deleted (only the parties or the law change the seat). |
| A14 Exclusions | Equator does not administer criminal matters or any matter in the exclusion register (App. K §3; NN-24). It does not adjudicate in-rem or statutorily reserved matters. | New. **Corrected:** the Equa Dispute Explorer listed domestic violence, child custody and cheque-bounce cases as dispute categories, and File a claim listed eviction proceedings as suitable. These go to K's signposting and civil-dimension rules instead. |
| A15 Non-participation | If a respondent does not respond, the claimant receives a **non-participation record** stating the dates of notice and delivery. It is **not** a Commercial Courts Act s.12A non-starter report (that is issued only by the Legal Services Authority — LR-MED-014). | Equa "Failure Report … submitted to a Court" and "certificate of non-participation usable in Court" **corrected**. |
| A16 Silence | Silence or non-response is **never** consent or acceptance of a claim. | Equa "silence is treated as acceptance" (File a response page) **deleted**: it is wrong in law and coercive. |
| A17 Amendments | The Rules Sub-Committee amends the Rules; the Board approves. Amendments apply only to matters filed after they take effect. | Equa "Advisory Council can amend the Rules" **replaced**: the Council had no charter, quorum or terms (App. N §1). |

### U.2.2 Part B — Negotiation

Content:
- B1 invitation and opt-in window (`neg_optin`);
- B2 structured offers, blind-bid rounds and offer validity (`offer_validity`);
- B3 time box (`neg_timebox`);
- B4 optional `neutral_facilitator` (App. S §6.2, v2.1), who has no decision or recommendation power;
- B5 the outcome is a settlement agreement signed by the parties through P06;
- B6 failure → closure record and the offer of mediation.

Equa Part IV (cl.6) mirrored the arbitration text and had no procedure; this Part replaces it.

### U.2.3 Part C — Mediation (contractual mode)

| Clause | Content |
|---|---|
| C1 Agreement to mediate | A signed agreement is required for every mediation, as the Equa Code §4.1 already recommended. It covers: confidentiality, no recording, voluntariness, the time box, fees, the mediator's role, online mode, and what happens on settlement or failure. |
| C2 Appointment | From the panel under the Allocation Policy, or by party choice where the rules allow (App. N §6). Disclosure follows ECC Part 3. |
| C3 Conduct | Joint and private sessions; shuttle-only where a safety flag applies (NN-07); no evaluation of the merits unless all parties ask (ECC 6.3); a party may withdraw at any time. |
| C4 Time box | `med_contract_timebox` per vertical (Appendix A §6.3), extendable by consent up to the outer cap (X-40). |
| C5 Settlement | A written settlement agreement signed by the parties and authenticated by the mediator. Where an arbitration agreement exists or is signed, a consent award may follow under the safeguards in LR-MED-021 and P04. Statutory-mode effects (Mediation Act ss.27–28) apply only when those sections are notified (LR-MED-012). |
| C6 Failure and closure | Closure report stating only the dates and that no settlement was reached. It is never a s.12A report (A15). |
| C7 Confidentiality and privilege | Statements, offers and documents prepared for the mediation cannot be relied on in later proceedings, to the extent the law allows. The mediator does not testify (ECC 9.1). |
| C8 Statutory mode | Mediation Act 2023 procedure (ss.15–27) is built behind `med_statutory_mode` (OFF) until the relevant sections commence. As of 22 Oct 2026 only ss.1, 3, 26, 31–38, 45–47, 50–54 and 56–57 are in force (J.5, A3_COM). |

The Equa site said mediated settlements can be "produced before any Court and executed". That is **corrected**: a contractual settlement is enforceable as a contract unless it is recorded as a consent award, a s.74 settlement, or (once in force) a Mediation Act settlement. Execution copy follows App. R §4.

### U.2.4 Part D — Conciliation (A&C Act Part III)

Conciliation follows A&C ss.61–81. A settlement signed under s.73 has the status of an arbitral award (s.74). The conciliator may not act as arbitrator or representative in the same dispute (s.80) without the consent safeguards in master §5.3.

Sunset: Part III will be replaced by the Mediation Act when s.61 of that Act commences. The registry carries a watch trigger `mediation_act_s61` (J.5).

### U.2.5 Part E — Arbitration

| Clause | Content | Source / clock |
|---|---|---|
| E1 Commencement | Request for arbitration; commencement on the respondent's receipt (A&C s.21). | P04; Appendix A §3.5 |
| E2 Number of arbitrators and appointment | Sole arbitrator unless agreed otherwise. For three members, each side nominates one and the two choose the presiding arbitrator (Equa cl.8.3 kept). No party, including a lender, insurer or employer, unilaterally appoints a sole arbitrator (*CORE* 2024; NN-03). | P03, N §6 |
| E3 Disclosure and eligibility | Sixth Schedule disclosure; Fifth and Seventh Schedule checks; s.12(5) waiver only in writing after the dispute arises. | ECC Part 3 |
| E4 Challenge | Written challenge within **15 days** of learning of the appointment or the grounds (A&C s.13(2)). Decided by the tribunal under s.13(3); Equator's Challenge Sub-Committee may invite withdrawal. | **Corrected:** Equa cl.9 gave 7 days with no decision procedure. |
| E5 Substitution | A substitute arbitrator is appointed under the same procedure (s.15). | New |
| E6 Pleadings | Statement of claim and defence; counterclaim; amendments; the s.23(4) six-month completion. The Equa claim and defence checklists (13 and 16 points) become field guidance in the intake forms (V1–V6 §6). | Appendix A `arb_pleadings_6m` |
| E7 Hearings, evidence, experts | Online by default; documents-only on agreement; tribunal-appointed experts (s.26). | P04 |
| E8 Interim measures | s.17 by the tribunal. Emergency arbitrator under Schedule 1 is contractual only (`arb_statutory_ea` OFF). | Appendix A §3.6 |
| E9 Award | In writing, signed, reasoned unless agreed (s.31(3)), dated, seat stated; stamped as state law requires (NN-09). AI use only as the AI Governance Rule allows, with attestation (ECC Part 8). | P06 |
| E10 Time limits | s.29A (12 months from completion of pleadings, +6 by consent); s.29B fast track on agreement. | Appendix A |
| E11 Correction and interpretation | s.33 within 30 days. | Appendix A |
| E12 Scrutiny | Equator scrutinises only for form. It does not review the merits. | App. N §1 |
| E13 Appeal tier | A contractual appellate tribunal is available **only** when `arb_appeal_tier_contractual` is switched ON after a counsel opinion (J-003/J-034/J-148). | P04 |

### U.2.6 Part F — Med-arb and arb-med

Safeguards from master §5.3:
- separate mandates;
- a caucus firewall;
- fresh written consent before the same neutral arbitrates;
- a renewed disclosure.

In statutory mode the Mediation Act s.17 bar applies. The Equa Med-Arb clause had no time box and no definition of "fails". The model clause in §U.11 adds both.

### U.2.7 Part G — Expert determination

Available only where the contract provides for it. The determination binds contractually, not as an award. The vertical limits in master §5.2 apply.

### U.2.8 Part H — Equator's role

Equator administers; it does not decide. Specifically:
- Equator does not give legal advice.
- It does not represent any party.
- It does not hold settlement money (escrow sits with a regulated bank and trustee under NN-13).
- It does not guarantee any outcome or enforcement.

**Corrected:** the Equa "SmartExecution" escrow described Equa itself holding disputed sums. That model is replaced by the bank escrow in P05, and the word "escrow" is used only for a bank–trustee arrangement (J.5, A9_ID_VENDOR).

### U.2.9 Part I — Institutional Committee and Registrar

Composition, sub-committees, recusal and decisions follow App. N §1. The Registrar is a named officer, published on `/about/governance`.

### U.2.10 Part J — Publication

Publication is opt-in only:
- every party must give informed consent **after** the outcome;
- redaction and a cooling-off period apply;
- consent may be withdrawn before publication, and corrections can be made afterwards;
- arbitral publication is OFF until counsel rules on A&C s.42A (App. R §3; X-35; NN-26).

---

## U.3 Code of Conduct for Neutrals — what the Equa Code adds to ECC-2026.1

Appendix N §5 holds the publishable Code (ECC-2026.1). The Equa Code (2022) was mediation-centred but had five rules that ECC lacked. They are now inserted into App. N §5 as clauses **4.5, 6.7, 7.5, 9.4 and 5.4** (v2.1), and recorded here:

| Equa Code | Rule carried forward | ECC clause (v2.1) |
|---|---|---|
| §5.1.1(v) | A neutral may disclose confidential information to prevent death or imminent serious bodily harm to an identifiable person, after a good-faith effort to have the party remedy the situation unless the law requires immediate disclosure. | 4.5 |
| §4.3.2 | A mediator must withdraw if the negotiation appears headed to an unconscionable or illegal outcome (undue pressure, exploitation of a power imbalance, duress). | 6.7 |
| §4.5.1 | A neutral who withdraws refunds any fee paid for the period after withdrawal, through Equator. | 7.5 |
| §3.7 | For 12 months after a matter ends, a neutral must not act as adviser to, or take employment with, any party in the same or a substantially related matter unless all parties consent after full disclosure. (ECC 2.4 and 9.3 already cover repeat users and adverse work; this adds the general rule.) | 9.4 |
| §1.3.1 | Before the first session the neutral tells the parties their relevant background and experience. The platform shows it from the verified profile. | 5.4 |

The Equa Code's "Reviewer", "Feedbook" and "Professional Conduct Assessment Process" were never published. They are replaced by:
- the moderated feedback system (App. N §7.2–§7.6);
- the complaints procedure (App. N §7.7–§7.9);
- a published Ethics & Complaints Sub-Committee.

The eight international codes the Equa Code credited are kept as an acknowledgement on the Code's page:
- CPR-Georgetown (2002);
- UIA (2003);
- European Code of Conduct for Mediators (2004);
- AAA/ABA/ACR Model Standards (2005);
- Law Council of Australia (2006);
- JAMS;
- CIArb;
- Swiss Rules.

They are listed as **sources consulted, not as a claim of endorsement**.

---

## U.4 Code of Conduct for Case Managers and Staff (ESC-2026.1) — new

The Equa Rules made the Case Manager central (cl.7.3) but set no standards. Every staff member signs this Code at onboarding and every year after (P00 attestation record).

1. **Process, not merits.** Staff explain the process, forms, fees, clocks and free forums. They never advise a party on the merits, predict outcomes, or suggest what to claim or accept (NN-01; Advocates Act ss.29 and 33). The Equa "Case Assessment … likely outcomes" and "Neutral Opinion Service" offers are discontinued.
2. **Equal treatment.** The same information and the same response times go to every party, including the side that did not choose Equator. No private discussion of a case with one party about matters that affect the other.
3. **No influence on neutrals.** Staff never discuss the merits with a neutral and never suggest an outcome. They do not influence allocation outside the published policy (App. N §6).
4. **Confidentiality and data.** Least-privilege access only (App. S §6). No case data on personal devices, in personal email or in unapproved AI tools. Report any suspected breach at once (U-9).
5. **Conflicts.** Declare any relationship with a party or representative and step aside from the case. No gifts or hospitality from parties.
6. **Money.** Staff never receive money from a party except through the platform's payment flows. They never handle settlement sums.
7. **Safety.** Follow the safeguarding procedure (NN-07) when a party discloses a risk of harm. Signpost emergency services where needed.
8. **Accuracy of statements.** Never describe Equator as a court, never promise enforcement or a timeline, and never claim an accreditation or certification Equator does not hold (NN-17).
9. **Breach.** Breach is a disciplinary matter under Equator's HR policy. Breaches affecting a party are reported to the Registrar and recorded.

---

## U.5 Privacy Notice baseline (EPN-2026.1)

The Equa Privacy Policy cited only the GDPR. It also listed card CVV and the Aadhaar number as data collected, and named no data fiduciary, Grievance Officer, retention periods or cross-border rules. EPN-2026.1 is rebuilt on the legal position verified in J.5:
- DPDP Act 2023 and DPDP Rules 2025: partly in force since 13 Nov 2025; core duties from 13 May 2027.
- IT Act s.43A and the SPDI Rules 2011: continue until DPDP s.44(2) commences on 13 May 2027.
- GDPR, UK GDPR and other foreign law only where they apply (App. Q §1).

Equator builds to the DPDP standard now (NN-30).

| § | Heading | Content (plain language; App. Q §2 has the control detail) | Equa clause |
|---|---|---|---|
| 1 | Who we are | Equator Resolution Service Private Limited, CIN, registered office, contact; the DPO; the Grievance Officer. | Equa cl.3 "Equa acts as controller" corrected: Equa named no entity. |
| 2 | Our role | Equator is data fiduciary for its own institutional case administration and for the website. For enterprise GRM and POSH SaaS tenants, Equator is the processor and the tenant is the fiduciary. The role table is subject to counsel sign-off (J-099). | New |
| 3 | What we collect | **Contact and account data:** name, email, mobile, address, credentials. **Identity:** verification results, last-four digits and reference IDs; the Aadhaar number is never stored, because only offline verification is used (D2-06; NN-14). **Case data:** pleadings, evidence, recordings where allowed, outcomes. **Payment data:** order and transaction references only. Card details are entered on the payment provider's page; Equator never sees or stores the card number or CVV (NN-31). **Device and usage data.** **Special categories** in sealed stores: health, POSH, family safety (NN-07). | Equa cll.11–16 corrected: CVV and card number removed; Aadhaar number removed. |
| 4 | Why we use it | Running the matter; identity and conflict checks; communications; fees and invoices; security and fraud prevention; legal obligations; improving the service with de-identified data; marketing only with separate consent. | Equa cll.5–8 kept. "Analysis of profiles submitted to the AI" is replaced by the AI notice in §7. |
| 5 | Legal basis | Consent (DPDP s.6) for identity verification, marketing and optional AI features; legitimate uses (s.7) where the law permits, as mapped per purpose in the lawful-basis register (LR-DPDP-001). For GDPR-covered parties: contract, legal obligation and legitimate interests, as App. Q maps them. | New |
| 6 | Other people's data | A party who uploads another person's data confirms they may lawfully share it for the dispute. Equator gives notice to the other party when it is served. | Equa cll.18.1–18.5 kept; the "presumed permission" in cl.18.5 is softened to a confirmation. |
| 7 | AI | Which AI features exist, where they run (India region for case content; X-32), that a human always reviews AI output, the option to opt out of optional AI features, and that no decision about a party is made by AI alone. | New |
| 8 | Sharing | With neutrals and other parties as the Rules require; with processors under contract (published sub-processor list); with courts or authorities where the law requires; never sold. | New |
| 9 | Cookies | Essential cookies only, unless the visitor consents to analytics or marketing cookies. Preference centre; Global Privacy Control honoured (App. Q). | Equa cll.20–21 kept; separate Cookie Notice (U-5). |
| 10 | Cross-border | Data is stored in India (AWS Mumbai, DR Hyderabad). Transfers abroad happen only where a matter requires it (e.g., a foreign party or neutral) and as DPDP s.16 permits, with safeguards for GDPR data. | Equa Data Security "AWS Mumbai" kept. |
| 11 | Retention | Case records: 8 years after closure. Awards, settlements and certified copies: at least 13 years (X-36). Account data: while the account is active, plus 3 years. Marketing data: until consent is withdrawn. Logs: as App. Q and CERT-In require (180 days minimum, in India). | New: Equa gave no periods. |
| 12 | Your rights | Access, correction, completion, update and erasure; grievance redressal; nominating a person (DPDP ss.11–14); withdrawing consent as easily as giving it; data portability in CSV/JSON where feasible (an Equa cl.26 commitment kept as Equator policy); for GDPR and CCPA users, the rights those laws give. Response time: as the DPDP Rules require, and within 30 days at most as Equator policy. | Equa cll.19, 23, 25–27 kept and mapped. |
| 13 | Children | Services are for adults. A minor's matter proceeds only through a guardian, with verifiable consent (DPDP s.9). | Equa T&C cl.3.1 (age 18) kept. |
| 14 | Security and breaches | Summary of safeguards (U-9). Breaches are notified to affected persons and the Data Protection Board as the DPDP Rules require, and to CERT-In within 6 hours. | New |
| 15 | Grievances | Grievance Officer: name, email, address; acknowledgement within 48 hours, resolution within 30 days (Equator policy, aligned with IT Rules 2021 and E-Commerce Rules 2020). Escalation to the Data Protection Board once its complaint functions are available. | Equa cl.30 "Data Compliance Officer … act immediately" corrected: the officer is named and time limits are set. |
| 16 | Changes | 30 days' notice of material changes; versions archived. | New |

**Domains.** All legacy contacts (`vdrc.io`, `equa.law`, `support@vdrc.io`, `help@vdrc.io`, `info@vdrc.io`, `registrar@equa.law`, `grievance@equa.law`) are retired. They redirect, or auto-reply with the Equator contacts, for 12 months (P13 redirect map).

### U.5.9 Cookie Notice (ECN-2026.1)

The notice lists each cookie with its name, provider, purpose, category (essential, analytics or marketing) and expiry. Only essential cookies load until the visitor chooses. Rejecting is as easy as accepting (CCPA dark-pattern guidelines; App. P lint).

---

## U.6 Terms of Service baseline (ETS-2026.1)

The Equa T&C left blanks:
- cl.3.1 (age);
- cll.6.1–6.3 (the dispute body, period and seat);
- the domain.

It had no cl.17 and named LawDocs as technology provider without a data-processing agreement. ETS-2026.1 fills each gap.

| Clause | Content | Equa clause |
|---|---|---|
| 1 Acceptance | Click-wrap acceptance at sign-up, with the version recorded (P01). Electronic acceptance is valid (IT Act s.10A). | Equa 1.1–1.4 kept; "deemed agreement on first use" of the website is replaced by acceptance at account creation. Browsing needs no acceptance. |
| 2 Who we are | Entity particulars, contact, Grievance Officer. | Equa had none. |
| 3 Eligibility | 18 or over, with capacity; organisations through an authorised user. Minors only through a guardian. | Equa 3.1 completed. |
| 4 Our service | Equator provides case administration and technology for dispute resolution. Neutrals are independent. Equator does not give legal advice, does not represent anyone and does not guarantee any outcome. | Equa 8.4 and 14.1 kept. |
| 5 Your obligations | Accurate information; lawful uploads; no misuse; keep credentials safe; honour the Rules. | Equa 13.1–13.3 kept. |
| 6 Fees | Per the published fees, plans and Refund Policy (U-7); prices shown inclusive of GST. | New |
| 7 Content and IP | The user owns their uploads and gives Equator a licence to use them only to provide the service. Equator owns the platform. | Equa 12 kept and balanced. |
| 8 Third-party services | eSign, payment, KYC and video providers; links to their terms. | Equa 5 kept. |
| 9 Availability and changes | Reasonable efforts on availability; scheduled maintenance notices; changes with 30 days' notice for material terms. | Equa 15–16: termination "for any reason without notice" narrowed to reasons stated and notified, except for urgent security or legal reasons. |
| 10 Liability | Equator is not liable for neutrals' decisions or for parties' conduct. Its aggregate liability to a user is capped at the greater of the fees that user paid in the 12 months before the claim and ₹50,000 **[Board to confirm figure]**, except where the law does not permit a cap (fraud, wilful misconduct, gross negligence, death or personal injury, data-protection liability that cannot be limited). | Equa 11.1 cap (fees paid, excluding even direct loss) revised to reduce unfair-term risk (CPA 2019 s.2(46)). Equa 11.5 (no liability for LawDocs) deleted: Equator answers for its own processors. |
| 11 Indemnity | Limited to losses from a user's fraud or wilful breach. | Equa 10.1 narrowed. |
| 12 Governing law and disputes with Equator | Indian law. A user who has a complaint about Equator's own service first uses the Grievance Policy (U-12). Disputes about Equator's own service (not the user's case) go to the courts at New Delhi, without prejudice to a consumer's right to use the Consumer Commission or any statutory forum. Equator does not ask users to arbitrate disputes against Equator before its own panel. | Equa 6.1–6.3 blanks resolved. An Equa-administered arbitration of disputes with Equa itself would raise an independence problem (s.12(5), Seventh Schedule), so it is not used. |
| 13 Translations | English prevails. | Equa 7.1 kept. |
| 14 Grievance Officer | Name and contact; acknowledgement within 48 hours, resolution within 30 days (IT Rules 2021 r.3(2); E-Commerce Rules 2020 r.4(4), where applicable — J-109). | New |
| 15 Suspension and closure | Grounds, notice and appeal; the user's data-export window before closure. | Equa 15 revised. |

### U.6.4 Grievance Redressal Policy for users (EGP-2026.1)

The policy covers complaints about Equator's service: staff conduct, billing, privacy and accessibility. Complaints about a neutral go to App. N §7.7, and the decision in a case is challenged only as the law allows.
- **Channels:** web form, email, post.
- **Process:** acknowledgement within 48 hours, a ticket number, resolution within 30 days, and escalation to the Company Secretary.
- **Reporting:** a quarterly summary is published in the Transparency Report (App. N §6.7).

---

## U.7 Fees, Deposits, Cancellation and Refund Policy (ERP-2026.1)

### U.7.1 What changes from the Equa policy

The Equa policy had three problems:
- it said Equator's fees were "non-refundable" with no timeline, method or cancellation window;
- its cl.2 (neutral's fee refunded if no effective hearing) and cl.3 sat awkwardly together;
- it never mentioned GST.

ERP-2026.1 adopts the refund codes already specified in Appendix O (RP-SUB, RP-STD-MED, RP-STD-ARB, RP-INS-RET, RP-INS-COM, and the delivery-failure auto-refunds) and Appendix B §B.8. It states them on one page in plain language, with every amount inclusive of GST.

### U.7.2 Policy text (summary; amounts from Appendix B / O render live)

1. **Before you pay** you see the total, GST included, and what it covers (NN-29).
2. **Registration fee.**
   - Refunded in full if the other party declines or does not respond and the matter does not proceed beyond notice, *where the vertical card says so*; otherwise it is retained.
   - The card for each vertical shows which rule applies before payment (Appendix B §B.8).
3. **Neutral's fee.**
   - Charged only for sessions or stages that take place.
   - If a session does not happen for a reason not caused by the payer, the fee is refunded or carried to the next session, at the payer's choice. This keeps the Equa "effective hearing" rule.
4. **Neutral withdraws.** Fees for the period after withdrawal are refunded (ECC 7.5).
5. **Subscriptions and plans:**
   - 14-day cooling-off refund on a first purchase if no entitlement has been used;
   - auto-renew OFF by default;
   - cancel in three steps or fewer (App. O RP-SUB).
6. **Timing and method.**
   - Approved refunds go back to the original payment method.
   - Initiated within 7 working days of approval **[CFO to confirm]**; bank credit times depend on the bank.
7. **Disputes about a charge** go to the Grievance Policy (U-12). Chargebacks are handled under the payment provider's rules.
8. **Third-party charges**, e.g. stamp duty, government fees and certified courier, are passed through at cost and shown separately. They are refundable only if the third party refunds them.

### U.7.3 Mapping the Equa Schedule of Fee (2022) to the pack

| Equa item (2022) | Equa figure | Treatment in v2.1 |
|---|---|---|
| Registration fee (one-time; covers pre-litigation call) | ₹1,000 / USD 20 | Superseded by Appendix B registration fees per vertical card. The free orientation call is kept (A7). The paid Explorer call is in App. O at ₹999 / ₹1,999, credited against registration. |
| Case management fee per 3-hour session | ₹1,000 / USD 20 | Replaced by stage-based administration fees (Appendix B). Sessions are no longer the billing unit for administration. |
| Arbitrator fee, Grade A (minimum) / Grade B per session | ₹10,000 / ₹5,000 | Replaced by ad valorem and band fees (Appendix B; App. N §3.9 bands I–IV by grade). The Equa "each party pays the neutral separately" model is replaced by payment through Equator (ECC 7.2). |
| Mediator fee, Grade A / B / C per session | ₹8,000 / ₹4,000 / ₹2,000 | Same as above. Equa's three-grade structure carries into App. N grades A/B/C with the management definitions (D2-12). |
| Conference room (3 hours) | ₹5,000 | Optional physical-venue add-on, at cost (App. O). |
| Government fee and stamp duty | At actuals, shared equally | Kept: pass-through, shown separately (NN-09). |
| Outstation neutral fee and travel | Neutral's fee plus actuals | Kept as an optional add-on, with prior written agreement of the paying parties. |
| Worked example: family mediation, 5 sessions, about ₹27,000; failure in session 1, ₹6,000 | — | Replaced by the fee calculator (SCR-P05-01) and Appendix B worked examples. |

---

## U.8 Disclaimer and use of the word "Court" (EDS-2026.1)

**Carried from the Equa Disclaimer:**
- no warranties beyond those the law implies;
- services "as is" except where the law gives the user rights;
- Equator does not practise law;
- good-faith protection for neutrals and staff (subject to A12).

**Added:**
- **"Court".** Equator is not a court, and nothing it issues is a court order or decree. The word "Court" does not appear in Equator's own product names, page titles or domains. The Equa terms "Private ADR Courts", `court.equa.law`, "ADR judge" and "Set up your private Court" are **retired**. Private practice tools are offered as **Private ADR Chambers** (D2-16; App. N §8), and a tenant may use "Court" in its name only as App. N §1.8 allows.
- **No outcome claims.** Equator does not say "Where there is a right, there is always a remedy". It does not describe AI as "surprisingly correct", and it does not quote success rates without a Claims Register record (NN-17; App. P copy lint).
- **No unverifiable presence claims.** The Equa footer listed "Singapore | New Delhi | New York | London" offices. It is replaced by the registered office and any verified operating addresses.

---

## U.9 Information Security Statement (ESS-2026.1)

**What the Equa page did.** It showed SOC 2 Type 1 and Type 2, HITRUST, ISO 9001, ISO 27001, HIPAA, CCPA and GDPR badges without scope, auditor or report. It also presented the hosting provider's attestations as Equa's own, and called ISO 9001 a security standard.

**Rule.** Until an independent assessment is complete, the statement uses **readiness language only** (NN-17; App. Q §5). It never uses certification logos.

**Content:**
- Hosting in AWS Mumbai with DR in Hyderabad. The AWS attestations are named as AWS's, with a link to AWS Artifact.
- Encryption in transit and at rest.
- Phishing-resistant MFA for staff and neutrals.
- Least-privilege access.
- Logging and 24×7 monitoring.
- Backups:
  - recovery point objective: as App. Q sets it;
  - the Equa "every 3 hours" backup interval is kept only if engineering confirms it.
- Vulnerability management and penetration tests.
- Incident reporting:
  - CERT-In within 6 hours;
  - logs kept for 180 days in India (LR-CERTIN-001–004, verified);
  - affected users and the Data Protection Board as the DPDP Rules require.
- Card data never touches Equator (SAQ A, NN-31).
- A responsible-disclosure address (`security@`).

**Removed claims.** "Three-factor authentication at least three times to enter data-centre floors" (that is AWS's function, not Equator's) and "audit trail embedded in a blockchain algorithm" are removed. The audit trail is the hash-chained ledger in App. F §F.5; it is described accurately and not as a blockchain.

---

## U.10 Accessibility Statement (EAS-2026.1)

- **Target:** WCAG 2.2 Level AA on web and mobile, measured against GIGW 3.0 and IS 17802 where they apply, and the RPwD Act 2016 (ss.40 and 46). This updates the Equa "WCAG 2.0 AA" commitment.
- **Status:** the date of the last audit and its known exceptions are published. Equator does not claim conformance before the audit (P14).
- **Accommodations, available on request without charge:** sign-language or real-time captioning in hearings; screen-reader-friendly bundles; extra time; a support person in sessions (App. C).
- **Contact:** an accessibility contact, with a response within 5 working days.
- **Removed claims:** the Equa reference to "wheelchair ramps, elevators" is removed until a physical venue is named and checked.

---

## U.11 Model dispute resolution clauses (EMC-2026.1)

Each clause has a plain-language note and a "when not to use" line. Every clause is offered in English and Hindi (App. L locked-term glossary).

| Code | Clause | Key terms (blanks shown as `{…}`) | Notes |
|---|---|---|---|
| MC-1 | Arbitration | "Any dispute arising out of or in connection with this contract, including its existence, validity or termination, shall be referred to and finally resolved by arbitration under the Arbitration and Conciliation Act, 1996, administered by Equator Resolution Service Private Limited under the Equator Resolution Rules in force on the date of the request. The tribunal shall consist of {one / three} arbitrator(s) appointed under those Rules. The seat shall be {New Delhi}, India. The language shall be {English}. Proceedings may be conducted online. Notices may be sent to {email IDs of each party}." | Built from Equa clause A. "All disputes about construction, meaning, scope or validity" is widened to "arising out of or in connection with". The award is "final and binding" only as the Act allows; that wording is removed from the clause body. **Not for:** retail insurance policyholders (R1), workmen (s.42 IR Code applies instead), consumer standard-form contracts without the NN-03 safeguards. |
| MC-1F | Arbitration — lender variant | MC-1, plus: appointment by Equator only; no unilateral appointment by the lender; pinned at sanction; s.12(5) waiver only after the dispute arises; borrower's district as the default venue; costs under s.31A. No pre-dispute costs clause (s.31A(5)). | NN-03; V1 §6; J.5 A6_FIN. |
| MC-2 | Mediation | "The parties shall first try in good faith to settle any dispute arising out of or in connection with this contract by mediation administered by Equator Resolution Service Private Limited under the Equator Resolution Rules. Mediation shall start when a party sends a request through Equator and shall end {60} days after the first session unless the parties extend it in writing. Either party may withdraw at any time. Nothing in this clause prevents a party from seeking urgent interim relief from a court or from protecting a limitation period." | Built from Equa clause B. Adds the time box, withdrawal and urgent-relief carve-out the Equa clause lacked. Avoid mandatory wording where a party is a consumer. |
| MC-3 | Mediation, then arbitration | MC-2, then: "If the dispute is not settled within the mediation period, or if a party withdraws, the dispute shall be referred to arbitration under clause MC-1. The mediator shall not act as arbitrator unless every party agrees in writing after the mediation ends." | Built from Equa clause C. Adds the definition of "fails" and the same-neutral safeguard (master §5.3). |
| MC-4 | Negotiation first | "Before starting mediation or arbitration, the parties shall exchange written proposals through the Equator platform for {21} days from an invitation by either party." | New (named but absent on the Equa site). |
| MC-5 | Multi-tier | Negotiation (MC-4) → mediation (MC-2) → arbitration (MC-1), with fixed periods and a limitation carve-out. | New (named but absent on the Equa site). |
| MC-6 | Expert determination | For technical or valuation questions only; the expert's determination is binding contractually; a fraud or manifest-error carve-out. | New (named but absent on the Equa site). Master §5.2 limits apply. |
| MC-7 | Submission agreement (existing dispute) | Post-dispute agreement to mediate or arbitrate under MC-1 or MC-2, signed by e-sign, with each party's s.12(5) waiver where relevant. | Equa "executed contracts can adopt the mechanism" note made into a clause. |

**Placement guidance** (kept from the Equa site): put the clause under a "Dispute resolution" heading; remove conflicting clauses; use email IDs each party checks.

**Drafting checklist** (Equa's 11 points, kept):
- scope;
- the number of arbitrators;
- institutional or ad hoc;
- rules;
- seat and venue;
- disclosure limits;
- governing and procedural law;
- mediation first;
- costs;
- representation.

**Added to the checklist:**
- consumer and standard-form cautions;
- stamp duty on the main contract where the clause sits in it;
- limitation;
- language;
- the vertical exclusions in App. K §3.

---

## U.12 Remediation register — Equa material that must not reappear

The P13 copy lint blocks these patterns. The website migration (App. H §5) removes them from any live Equa or Equator page.

| # | Equa material (2022) | Risk | Replacement |
|---|---|---|---|
| E-01 | "Private ADR Courts", `court.equa.law`, "Set up your private Court", "choose your own fee" | Implies a court; unpublished "Procedural Rules"; neutrality risk | Private ADR Chambers (D2-16), published plan terms (App. O) |
| E-02 | "ADR judge at the British international court" and similar titles in Council bios | Unverifiable, misleading | Verified credentials only (App. N §2.5) |
| E-03 | Offices "Singapore, New Delhi, New York, London" | Unverifiable presence | Registered office and verified addresses |
| E-04 | SOC 2, HITRUST, ISO 9001/27001, HIPAA, CCPA, GDPR badges | Certification claims without assessment | Readiness language (U-9) |
| E-05 | "Silence is treated as acceptance" | Wrong in law; coercive | A16 |
| E-06 | "Decision posted on the website" | Breach of confidentiality; A&C s.42A | Opt-in Publication Policy (U-13) |
| E-07 | "Failure Report … submitted to a Court" / "certificate of non-participation usable in Court" | Confused with a s.12A report | Non-participation record (A15) |
| E-08 | Mediated settlements "produced before any Court and executed" | Overstates enforceability | §U.2.3 note; App. R §4 |
| E-09 | Dispute Explorer categories: domestic violence, child custody, cheque bounce; "eviction proceedings" suitable | Non-arbitrable or reserved matters | App. K exclusion and civil-dimension rules |
| E-10 | "Equator AI weighs your claim", "surprisingly correct", "likely outcomes", "Neutral Opinion Service" | Merits advice; outcome prediction; Advocates Act risk | Suitability and pathway report only (NN-01) |
| E-11 | SmartExecution: "disputed amount deposited with Equa"; blockchain "smart contracts" | Holding client money; misleading technology claim | Bank–trustee escrow (NN-13); accurate ledger description |
| E-12 | Privacy Policy collecting CVV and Aadhaar numbers | RBI CoFT rules; Aadhaar Act | U-5 §3 |
| E-13 | 7-day challenge to arbitrators | Conflicts with A&C s.13 (15 days) | E4 |
| E-14 | "Train with us to qualify"; free year of Private Courts with training | Neutrality and related-party concerns (X-29) | Training neutrality: at least three providers; no grade advantage (App. N §4.6) |
| E-15 | "Equa Advisory Council can amend the Rules" | No charter; owner control of the rules | Institutional Committee and Rules Sub-Committee (App. N §1) |
| E-16 | Legacy domains and contacts (`vdrc.io`, `equa.law`, phone 9928168300 on public pages) | Confusion over the operating entity | Redirects and auto-replies for 12 months (P13) |
| E-17 | "Equa Certified Neutral"; "EQP/QAP" with no published standards | Accreditation claim | EQAP per App. N §4 and the IMI status wording (D2-17) |

**Personal data on the old Secretariat page.** Names and student status of interns and staff are published there. Remove them unless each person consents to remain listed (DPDP s.6).

---

## U.13 Build requirements (phase mapping)

**FR-P00-V2-U01 — Policy registry.** `core.procedure_rules` gains kinds:
- `staff_code`
- `privacy_notice`
- `cookie_notice`
- `terms_of_service`
- `refund_policy`
- `disclaimer`
- `security_statement`
- `accessibility`
- `model_clauses`
- `grievance_policy`
- `publication_policy`

Each has the maker–checker workflow in §U.1, version pinning, a hash-stamped PDF on publish, and a 30-day change notice for U-4, U-6 and U-7. Acceptance: no policy page renders from a non-approved version.

**FR-P01-V2-U02 — Acceptance records.** Sign-up records the ETS and EPN versions accepted. Case filing records ERR and any case-specific terms. Re-acceptance is prompted only for material changes.

**FR-P02-V2-U03 — Rules-driven guidance.** The Equa claim (13-point) and defence (16-point) checklists become field-level help in the vertical intake forms, with the criminal-allegation guidance rewritten under NN-24. The 15-day reply is replaced by the vertical `response_window`.

**FR-P13-V2-U04 — Public pages and lint.**
- Pages: `/rules`, `/rules/code-of-conduct`, `/rules/staff-code`, `/rules/clauses`, `/privacy`, `/privacy/cookies`, `/terms`, `/fees/refunds`, `/disclaimer`, `/trust/security`, `/accessibility`, `/grievance`.
- The copy lint adds patterns E-01–E-17.
- The legacy redirect map covers `equa.law`, `vdrc.io` and the Google Sites URLs.

**FR-P14-V2-U05 — Go-live gate.** Launch is blocked until:
- U-1, U-4, U-6, U-7 and U-12 are approved;
- the Grievance Officer and DPO are named;
- the entity particulars are on every policy page (J-170).
