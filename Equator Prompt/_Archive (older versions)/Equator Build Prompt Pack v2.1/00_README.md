# Equator Resolution — Build Prompt Pack v2.1

**Prepared:** 19 October 2026 · **Revised:** 20 October 2026 (v1.1) · **v2.0:** 22 October 2026 (dispute-type specifications, ten new binding appendices, full v2 review) · **v2.1:** 22 October 2026 (all 469 open items researched and dispositioned; Appendix U policy baselines from the old Equa site) · **Owner:** Company Secretary, Infrabyx Group · **Entity:** Equator Resolution Service Private Limited · **Product:** Equator Resolution (equatorresolution.in), an ODR institution with web and mobile platforms
**Stack (locked):** Next.js web · NestJS (TypeScript) modular monolith · PostgreSQL (Aurora) with RLS · Temporal · Redis · OpenSearch · S3 Object Lock · React Native (Expo) mobile · Keycloak · AWS Mumbai (DR Hyderabad)

---

## 1. What this pack is

This is a paste-ready, phase-by-phase build prompt for a coding agent (Claude Code, Antigravity or equivalent) to build Equator Resolution end to end. It brings together the Equator corpus (551 documents) and research current to October 2026 (v1: R1–R5, C1–C5 and the verification of 514 flags; v2: research streams S1–S9).

**What v2.1 adds (22 October 2026)**

- **Appendix J rebuilt.** Every one of the 469 open items now has:
  - a disposition: verified, corrected, provisional, counsel sign-off, vendor confirmation, product decision or watch;
  - the evidence;
  - the residual uncertainty;
  - an approver;
  - a production gate;
  - a recheck trigger.

  The totals: **129 closed** (89 verified, 40 corrected), 90 provisional, and 250 awaiting counsel, vendors, decisions or a regulatory event.
- **355 in-place corrections and confirmations** across the pack. §J.5.2 lists **19 launch gates**. §J.7 answers management's comments of 22 October item by item.
- **Appendix U — Institutional Rules, Codes & Policy Baselines**, built from the old Equa site (rules, code, privacy, terms, refunds, disclaimer, security, accessibility, model clauses). It is corrected for current law, and it lists 17 old-site items that must not reappear.
- **Code of Conduct ECC-2026.1** gains five rules carried from the Equa Code.
- **Requirements R-41–R-43, decisions D2-28–D2-29, and five new counsel questions.**
- **A new role,** `neutral_facilitator`, for assisted negotiation.

**What v2.0 adds to v1.1**

- **One specification per dispute type** (`verticals/V1–V6`). Each covers:
  - subtypes and the law for each subtype;
  - ADR suitability rules and Dispute Explorer question trees;
  - **separate intake forms for negotiation, mediation and arbitration**, with every dropdown value;
  - documents, modus operandi and practical difficulties;
  - integrations and APIs, calculators, outputs, KPIs and tests.
  
  The coverage within each type:
  - Family includes inheritance and property division for every community (Hindu, Muslim, Christian, Parsi, Jewish, special-marriage and Uttarakhand UCC regimes).
  - Commercial includes IBC/NCLT, pre-pack and liquidation, company-law and MSME matters.
  - International includes international commercial arbitration and international mediation.
- **Dispute Explorer v2** with a criminal-matter exclusion, plus a **dispute-type plug-in framework** so new types can be added later, Jupitice-style, without a rebuild (Appendix K).
- **Documents:** an advanced DMS with selective sharing, Supreme Court A4 court formats, editable AI type copies of handwritten pages and WhatsApp screenshots, and translation across 28 languages (Appendix L).
- **AI Pleadings Studio:** drafts a statement of claim or defence from the party's documents, with index, list of dates, synopsis and affidavit, then the party's review, e-sign and submission. The AI model provider is pluggable (Claude or another) (Appendix M).
- **Neutral governance:**
  - grades A/B/C and a Qualifying Assessment Programme;
  - an Equator Code of Conduct, complaints and ratings;
  - transparent, rules-based allocation;
  - training pathways and Private ADR Chambers SaaS (Appendix N).
- **Revenue, plans, billing and settings pages** (Appendix O).
- **Website copy deck** with taglines, microcopy and SEO/GEO/AI-search structure (Appendix P).
- **Privacy, security and certification readiness:** GDPR, CCPA/CPRA, DPDP, IT Act, PCI DSS SAQ A, SOC 2 and the ISO family (Appendix Q).
- **Outcomes:** a case-status portal, consent-based publication of awards and settlements, and execution and registration support (Appendix R).
- **Identity:** separate login portals for parties, representatives, mediators, arbitrators and case managers; onboarding integrations (Aadhaar OVSE, PAN, DigiLocker, MCA); representatives; dashboards; RBAC (Appendix S).
- **Benchmarks:** competitors (including ClaimBuddy and Insurance Samadhan), SIAC, SIMC and world institutions, training providers, and a Reliance Jio AI evaluation (Appendix T).
- **Governance records:**
  - `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`: requirements R-01–R-40, decisions D2-01–D2-27, assumptions, counsel questions and the v2 review log.
  - Master additions: NN-24 to NN-32 and cross-file resolutions X-19 to X-42.

**What v1.1 already covered (unchanged unless superseded):**

- six verticals plus SEBI SMART ODR as an optional connector (flag OFF);
- every mechanism, including med-arb and arb-med-arb;
- Private ADR Chambers, Enterprise API and bulk intake, GRM SaaS (lenders, listed companies, employers, universities), POSH/IC SaaS and the Academy;
- the fee engine (INR default, with USD/EUR/GBP/SGD/AED for international matters; rate cards customisable and approval-gated);
- voice and omnichannel communications, eSign/eStamp, payments and escrow;
- website remediation with paste-ready replacement copy.

## 2. Files

| File | Purpose | Words (approx.) |
|---|---|---|
| `00_README.md` | This guide | 2,600 |
| `01_MASTER_PROMPT.md` | Constitution: product, **NN-01–NN-32**, architecture, domain model, customisability, fees, integrations, AI, phase plan, precedence and cross-file resolutions **X-01–X-42**, management decisions, v2 reading order | 9,800 |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | Requirements map R-01–R-40, decision log D2-01–D2-27, assumptions, counsel questions, dependencies, phase mapping, v2 review log | 4,000 |
| `phases/P00–P14` (15 files) | Build phases. Each ends with a **v2 addendum**, which is part of that phase's scope and exit gate | 175,000 in total (P08 ≈ 19,800) |
| `verticals/V1_FIN_Financial_and_Loan.md` | Loans, cards, NBFC/MFI, co-lending, gold, NI Act s.138, SARFAESI/DRT signposting, RB-IOS | 18,600 |
| `verticals/V2_COM_Commercial_and_Business.md` | B2B contracts, MSME delayed payments, IBC/NCLT, pre-pack, liquidation, company law, s.442 panel, IP, construction | 27,400 |
| `verticals/V3_FAM_Family_Marital_and_Property.md` | Marital, children, maintenance, inheritance and property division for every community, MWPSC, NRI matters, UCC Uttarakhand | 19,200 |
| `verticals/V4_INS_Insurance.md` | Retail and commercial lines, Ombudsman and consumer forums, TPA, surveyor, MACT signposting, reinsurance and B2B | 20,100 |
| `verticals/V5_WRK_Workplace_and_HR.md` | Labour Codes, full and final settlement, GRC, executive disputes, POSH routing to the sealed IC | 16,200 |
| `verticals/V6_INT_International_Commercial.md` | ICA, international mediation, Singapore Convention position, FEMA, sanctions, multi-currency, WTO boundary | 19,500 |
| `appendices/A–J` | v1 binding specifications: workflows (A), fees (B), screens (C), integrations (D), AI and voice (E), data model, events and errors (F), legal rules register (G; **329 rules** after v2), competitors, GTM and website corrections (H), tests (I), verification log (J) | 108,000 |
| `appendices/K` | Dispute Explorer v2 and dispute-type plug-in framework | 22,200 |
| `appendices/L` | DMS, court formats, type copies, translation | 17,500 |
| `appendices/M` | AI Pleadings Studio | 16,300 |
| `appendices/N` | Neutral governance, grading, QAP, training, Private Chambers | 18,600 |
| `appendices/O` | Revenue, plans, billing and settings | 18,600 |
| `appendices/P` | Website copy deck and SEO/GEO content system | 30,200 |
| `appendices/Q` | Privacy, security and certification readiness | 17,600 |
| `appendices/R` | Case status, publication, execution, registration | 15,300 |
| `appendices/S` | Identity, logins, onboarding, representatives, dashboards, RBAC | 16,500 |
| `appendices/T` | Benchmarks: competitors, institutions, training, Jio AI | 15,200 |
| `appendices/U` | Institutional rules, codes and policy baselines (v2.1) | 8,200 |
| `Equator_Build_Prompt_Pack_v2.docx` | Consolidated Word copy of all of the above for review and sign-off | — |

Earlier versions stay in their own folders for reference (`Equator Build Prompt Pack v1`, `Equator Build Prompt Pack v2`); v2.1 supersedes them. Appendix J is now about 70,000 words, because it holds the full register.

## 3. How to run the build

1. Create an empty repository and open the coding agent in it.
2. **At the start of every phase session,** paste `01_MASTER_PROMPT.md`, then `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, then the phase file (including its v2 addendum). Attach the appendices and vertical files that the phase cites.
3. **Phase order** is P00 → P14:
   - P08 runs as six sub-iterations, P08a FIN → P08f INT. Each starts by reading the matching `verticals/V<n>` file end to end.
   - P13 may run in parallel with P08–P11 using a second squad.
   - Mobile work starts in P01 and closes in P12.
4. **Before coding,** the agent writes `docs/phases/PXX-plan.md`. It stops at the phase exit gate (§13 of each phase file plus the addendum's acceptance tests).
5. **Precedence on conflict** follows master §15 (master and 02 → Appendix G for law → B for fees → F for names and codes → phase file → other appendices). The X-resolutions record the conflicts already resolved.
6. **Unverified rules:** any feature that depends on a legal rule still marked `UNVERIFIED` or **[VERIFY — open]** ships behind a flag that is OFF.

**Indicative effort:** 30–36 two-week sprints with two squads (platform + verticals), plus a growth/website squad. The v2 scope adds about 6–8 sprints, mostly in P02, P03, P06, P08 and P10.

## 4. Decisions and approvals needed before go-live

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | **Rate cards and fee schedules.** Rate cards are customisable and approval-gated (decided, M-01). The Board approves the default fee schedules (Appendix B) and the plans and one-time products (Appendix O). | Board / CFO | P05, P13 fees and plans pages |
| 2 | **Entity particulars** for Equator Resolution Service Private Limited (M-02): CIN, registered office, GSTIN, DPO, Grievance Officer, Nodal Officer. | Company Secretary | P13, P14, invoices, privacy notices |
| 3 | **Rulebooks:** Equator Rules (arbitration, mediation, conciliation, negotiation), vertical rules, Code of Conduct for neutrals, Institutional Committee charter (majority external) and complaints procedure. | Board / Legal | P03, P04, P08, App. N |
| 4 | **Neutral grading policy** (A/B/C), QAP design and fees, assessor panel, and the published allocation formula (D2-12, D2-13). | Head of Institution | P03, P10 |
| 5 | **Equator ADR Institute (D2-17):** confirm its operating entity and correct its public accreditation claims. The site presents itself as Equa Trainings / Equa.Law, operated by Infrabyx Consultancy (OPC) Pvt Ltd. Its IMI listing found in research is a recognised training programme, not a QAP. The Institute referral card stays OFF until this is done. Any referral fee is a related-party transaction: s.188 approval, s.177 only where an Audit Committee is required, and s.184 disclosure (X-29) **[CS to confirm]**. | Company Secretary / Institute | P10, P13 |
| 6 | **UIDAI and DigiLocker:** OVSE registration with UIDAI for Aadhaar offline verification, and DigiLocker requester partnership. No CIBIL or bureau pulls at onboarding (D2-06, App. S). | CTO / Compliance | P01 |
| 7 | **Counsel opinions** in 02 §5. Key items: s.42A and publication consent; AI self-help drafting and the Advocates Act; s.442 panel mediations; MSMED 2026 commencement and the s.18 text; Insurance Act intermediary question; "Court" in Chambers names. | General Counsel / external counsel | Flags in P06, P08, P10, P13 |
| 8 | **Telecom and calling (M-05):** DLT Principal Entity registration, CPaaS contracts, CLI opinion for Equator's own service numbers. Jio as a carrier, and a Jio Haptik RFP (D2-23). | CTO / telecom counsel | P07 |
| 9 | **Pre-suit mediation (M-06):** voluntary pre-suit mediation is live now. Mandatory s.12A PIMS stays with the Legal Services Authority until the four gates close (watch list in Appendix G LR-MED-019). | General Counsel | P08 COM |
| 10 | **Vendor contracts** (all names are candidates, not commitments): ElevenLabs Enterprise (India residency), Sarvam, Exotel/Plivo, Gupshup, MSG91, Leegality, Digio, SignDesk, Surepass, Razorpay (Standard Checkout, Route, Escrow+), Castler, LiveKit, AWS Bedrock India, OCR and translation providers. | CTO / Procurement | P01, P05–P07, P11 |
| 11 | **Policy set** for certification readiness (management will prepare the documents): information security, access control, incident response, vendor risk, retention, privacy notices, cookie policy. | Company Secretary / CISO | P14, App. Q |
| 12 | **Live website corrections:** apply Appendix H §5 and the Appendix P replacement copy on the live sites now, independent of the build. This includes "court-ready", guaranteed-outcome and accreditation claims. | Marketing + Legal | Immediate |
| 13 | **Open items:** work through the register in Appendix J §J.5.3, starting with the 19 launch gates in §J.5.2. Two need action within weeks: (a) A2P call declarations to each originating operator **before 17 Nov 2026** (LG-03); (b) counsel's view on recovery-agency status before any lender-paid FIN programme (LG-01). Then run the second-pass research list (§J.8). Set Legal Rules Register status as items close. | Legal counsel / tax adviser / CTO | Feature flags |

## 5. Requirement coverage map

The full map with status (specified, legal sign-off, vendor-dependent, configurable) is in `02` §2 (R-01–R-40). Summary by area:

| Area of the management briefs (19, 20, 21 Oct) | Where addressed |
|---|---|
| Six dispute types, subtypes, separate law, rules, process, forms per mechanism, dropdowns, integrations and APIs | V1–V6; Master §1.2, §5.2; P08 (P08a–f); App. K §4 form-resolution rule |
| Add further dispute types later | App. K §6 plug-in framework and expansion catalogue |
| Arbitration, mediation, med-arb, negotiation, conciliation; pre-litigation mediation | Master §1.3, §5.3; P04; App. A; App. K §5; V1–V6 §8 |
| Dispute Explorer, ADR suitability, criminal exclusion | App. K §1–§3; NN-24; V1–V6 §5 |
| AI drafting of claims, defences and affidavits; pluggable AI | App. M; NN-25; P11 addendum; LLM port (App. D) |
| Separate logins, onboarding APIs (Aadhaar, PAN, DigiLocker, MCA, credit reports), representatives, dashboards, RBAC | App. S; P01 addendum; NN-14, NN-27 |
| DMS, A4 Supreme Court format, type copies, translation | App. L; NN-32 |
| Case status, publication with consent, execution and registration | App. R; NN-26 |
| Neutral onboarding, directory, grades, QAP, Code of Conduct, complaints, ratings, allocation; Private ADR Courts SaaS | App. N; P03 and P10 addenda; NN-28 |
| Training providers, Equator ADR Institute, IMI QAP, specialisation and country add-ons | App. N §9–§10; App. T §3; D2-17 |
| Competitors (ClaimBuddy, Insurance Samadhan, Jupitice, Presolv360, Sama, SMART ODR); SIAC, SIMC and world institutions; Reliance Jio AI | App. T; App. H; V4 §13 |
| Revenue streams, subscriptions vs one-time products, billing and membership settings | App. O; NN-29 |
| Privacy laws (GDPR, CCPA, DPDP, IT Act); PCI DSS, SOC 2, ISO readiness; Razorpay security | App. Q; NN-30, NN-31; P05, P14 addenda |
| Copywriting, catch lines, SEO/GEO/AI search; clean minimal UI | App. P; App. C |
| Web and mobile | Master §4; P12; App. C, S |
| Fees in INR with foreign currency for international; customisable, approval-gated rate cards | Master §7; App. B; P05; V6 |
| Grievance redressal SaaS, POSH/IC SaaS, Enterprise API, Academy | P09, P10 |
| SEBI optional; Equator places its own calls; pre-suit mediation | Master §1.2, NN-12, §16 (M-05, M-06) |
| Remove risky website content | App. H §5; App. P; P13 |
| Policies from the old Equa site (privacy, code of conduct, institutional rules); research and response on every open item (22 Oct) | App. U; App. N §5 (ECC v2.1); App. J §J.5–§J.8 |
| Re-read the corpus; review and fix errors | `02` §8; Appendix J; review logs summarised in `02` §8 |

## 6. Key judgments embedded (read before approving)

- **No legal advice.** AI never advises, predicts or values a party's case (NN-01). The Dispute Explorer reports suitability and pathways, process cost and time, limitation flags and free-forum options. It never predicts the merits.
- **AI Pleadings Studio is self-help.** It is available on identical terms to both sides and grounded only in the party's own documents and a verified legal corpus. Equator staff never draft for a party (NN-25, D2-07). Counsel should confirm the Advocates Act position.
- **Criminal matters are excluded** (NN-24). Where the law allows, the civil dimension may be settled (for example the NI Act s.138 amount); Equator never mediates the offence.
- **Publication of awards and settlements** needs every party's consent, given after the outcome. Redaction and a cooling-off period apply. A&C s.42A confidentiality governs India-seated arbitral awards, so arbitral publication stays OFF until counsel rules (NN-26, X-35).
- **Aadhaar** is used only through offline verification (OVSE). Equator does not pull credit-bureau reports at onboarding. PAN, DigiLocker and MCA lookups run with purpose-bound consent (D2-06).
- **Pre-suit mediation (M-06):** Equator runs voluntary pre-suit mediation and conciliation now. It never claims to satisfy Commercial Courts Act s.12A until the four legal gates close.
- **Lender arbitration** is built to survive challenge after *CORE* (2024) and *Bhadra* (2026): the clause is pinned at origination, Equator appoints, s.12(5) waivers are post-dispute, and an Independence Evidence Pack is kept for each case.
- **Mediation Act 2023:** only partly in force; statutory mode stays behind a flag. India has signed but **not ratified** the Singapore Convention, so international mediated settlements are offered conversion to a consent award.
- **IBC and in-rem matters** are never decided by Equator (D2-02). It supports s.12A withdrawal settlements under the IBC Amendment Act 2026, pre-pack negotiation and creditor-debtor mediation.
- **MSME:** the referral of MSEFC matters to a mediation service provider comes from Mediation Act s.62 and the Seventh Schedule, as amended by MSMED (Amendment) Act 2026 s.8. Neither has commenced, so the original MSMED s.18 still operates and the referral track stays behind a flag (D2-26, corrected 22 Oct 2026).
- **Probate:** the Repealing and Amending Act 2025 omitted Indian Succession Act s.213, so copy must not say probate is mandatory in the presidency towns (D2-25; Act number to verify).
- **Neutral grades** follow management's definition (C entrants, B > 15 years, A retired judges or > 30 years). A competence gate applies, through the QAP or equivalent. Allocation rules are published, there are no paid listings, and the directory shows no outcome statistics (NN-28).
- **Honest pricing:** prices are GST-inclusive. All 13 CCPA dark patterns are linted, cancelling is as easy as subscribing, and there are no outcome-contingent fees (NN-18, NN-29).
- **Certification readiness, not certification.** The pack never claims PCI DSS, SOC 2 or ISO certification, or DPDP/GDPR "compliance", before an independent assessment. Card data never touches Equator (SAQ A, NN-31).
- **Settlement money never passes through Equator's merchant account.** It goes through bank escrow with a trustee, or directly between the parties (NN-13).
- **POSH, health and family-safety data are sealed.** Each sits in a separate schema with its own keys and is never sent to AI (NN-07).

## 7. Completion checklist

**Complete in this pack (specified and cross-checked)**

- [x] Six vertical specifications V1–V6, with subtypes, law, suitability rules, question trees, forms per mechanism, dropdowns, integrations, calculators, outputs, KPIs, tests and golden vectors (about 150 vectors recomputed in review)
- [x] Appendices K–T and a v2 addendum in every phase file
- [x] Master NN-24–NN-32 and X-19–X-42; `02` requirements map, decision log, assumptions and counsel questions
- [x] Appendix G extended to 329 rules (§G.6); Appendix F extended with the v2 error-code register (§F.10.3) and the 20-worker workplace size band
- [x] Six independent review passes plus a final cross-file pass (about 285 fixes; summary in `02` §8)
- [x] v2.1: all 469 open items researched and dispositioned (Appendix J); 355 in-place corrections; Appendix U policy baselines

**Depends on vendors or registrations** (flags OFF until contracted or registered)

- [ ] UIDAI OVSE; DigiLocker partner; MCA/KYB aggregator
- [ ] DLT/telecom: CPaaS, Jio carrier, CLI declarations; ElevenLabs India residency; Jio Haptik RFP
- [ ] eSign/eStamp providers by state; payment gateway (Standard Checkout, Route) and bank escrow
- [ ] LLM in India (Bedrock India) for case content; OCR and translation providers meeting the residency rules in App. L/M
- [ ] Independent assessors: PCI DSS ASV scans and SAQ A attestation; SOC 2 auditor; ISO 27001/27701 certification body

**Needs qualified counsel or management sign-off before launch**

- [ ] Counsel questions in `02` §5 and Appendix J (v1)
- [ ] Every Legal Rules Register row marked `UNVERIFIED` and every open item in Appendix J §J.5.3 (19 launch gates in §J.5.2)
- [ ] Board and counsel approval of the policy set in Appendix U (Rules, privacy notice, terms, refund policy, grievance policy) before publication
- [ ] Rulebooks, Code of Conduct, Committee charter, grading policy, fee schedules and plans (§4 items 1–4)
- [ ] Institute entity and claims; related-party approvals (§4 item 5)
- [ ] Policy documents for certification readiness (§4 item 11)

## 8. Not in this pack

- Legal opinions (the pack lists the questions).
- Signed vendor contracts.
- The policy documents management will prepare.
- Final rulebook text approved by the Board.
- Translated copy beyond the English and Hindi samples given (the translation workflow is specified).
