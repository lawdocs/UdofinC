# Equator Resolution — Build Prompt Pack v1.1

**Prepared:** 19 October 2026 · **Revised:** 20 October 2026 (v1.1 — management decisions applied, [VERIFY] research closed, full error review) · **Owner:** Company Secretary, Infrabyx Group · **Product:** Equator Resolution (equatorresolution.in) — ODR institution + web and mobile platform
**Stack (locked):** Next.js web · NestJS (TypeScript) modular monolith · PostgreSQL (Aurora) with RLS · Temporal · Redis · OpenSearch · S3 Object Lock · React Native (Expo) mobile · AWS Mumbai (DR Hyderabad)

---

## 1. What this pack is

A paste-ready, phase-by-phase build prompt for a coding agent (Claude Code, Antigravity or equivalent) to build Equator Resolution end to end. It consolidates the existing Equator corpus (551 documents: EQR-00 to EQR-43, the institution-wide platform pack, five vertical frameworks, website forms, university pack, strategy and marketing playbooks) with fresh research as of October 2026 on competitors, Indian and international law, integrations and go-to-market.

**Scope delivered by the pack**

- **Six dispute verticals:** Financial & Loan (FIN) · Commercial & Business (COM) · Family, Marital & Property incl. partition/succession (FAM) · Insurance (INS) · Workplace & HR (WRK) · **International Commercial (INT)** — plus **SEBI SMART ODR as an optional connector (SEC, flag OFF)**.
- **Mechanisms:** negotiation (incl. blind-bid), conciliation, mediation (contractual + feature-flagged Mediation Act 2023 statutory mode), arbitration (fast-track, expedited, emergency, optional appeal tier), **med-arb, arb-med, arb-med-arb**, expert determination, grievance (GRM), POSH inquiry, signposting.
- **Product lines:** Equator Institution · Private ADR Chambers SaaS · Enterprise API & bulk intake · **Grievance Redressal SaaS** (lenders→borrowers, listed companies→shareholders, employers→employees, universities→students) · POSH/IC SaaS · Equator ADR Academy & campus programmes.
- **Login screens, onboarding for every persona, and the directory of mediators/arbitrators/conciliators/experts** (P01, P03, Appendix C).
- **Fee structure:** deterministic fee engine and default rate cards for every vertical and product line, **INR by default, with USD/EUR/GBP/SGD/AED for international matters** (P05, Appendix B).
- **Integrations:** ElevenLabs AI voice agents (Sarvam fallback), WhatsApp/SMS/email/push, Leegality/Digio/SignDesk eSign and eStamp, Surepass KYC/KYB, Razorpay/Cashfree payments with split settlement, bank escrow, LiveKit video, Claude via Amazon Bedrock India (P07, P11, Appendices D–E).
- **Website remediation:** every risky item on the live site, with paste-ready replacement copy (Appendix H §5; P13 FR-P13-01).

## 2. Files

| File | Purpose | Words (approx.) |
|---|---|---|
| `00_README.md` | This guide | 2,100 |
| `01_MASTER_PROMPT.md` | Constitution: product definition, 23 non-negotiable rules (NN-01–NN-23), architecture, domain model, customisability, fees, integrations, AI, phase plan, quality bar, precedence and cross-file resolutions | 8,800 |
| `phases/P00_Foundations_Platform_Core.md` | Monorepo, CI/CD, IaC, tenancy + RLS, audit chain, design system, Ruleset Studio, flags, observability | 12,400 |
| `phases/P01_Identity_Login_Onboarding_Consent.md` | Login screens and onboarding for all personas, OTP/passkeys/SSO/DigiLocker, KYC/KYB, DPDP consent, mobile shell | 14,400 |
| `phases/P02_Case_Core_Intake_Forms_Routing_Notices_DMS.md` | Dispute Explorer, form engine, filing/response, scrutiny, routing & signposting, clocks, notices, DMS, case tracker | 13,000 |
| `phases/P03_Neutrals_Directory_Marketplace_Empanelment_Allocation.md` | Public neutral directory, marketplace, empanelment, disclosures/challenges, allocation engine, defensibility | 9,800 |
| `phases/P04_Resolution_Engines_Virtual_Hearings.md` | Negotiation, conciliation, mediation, arbitration, med-arb/arb-med, expert determination, appeal tier, hearing rooms | 11,800 |
| `phases/P05_Fees_Payments_Escrow_MultiCurrency.md` | Fee engine, quotes, payments, splits, payouts, GST/TDS, refunds, escrow, instalments, multi-currency | 11,800 |
| `phases/P06_Outcomes_Drafting_eSign_eStamp_Awards_Enforcement.md` | Settlement/award builders, maker–checker, eSign, eStamp, registration route, BSA s.63, enforcement packs | 9,900 |
| `phases/P07_Omnichannel_Communications_AI_Voice.md` | Journey orchestrator, WhatsApp/SMS/email/push, ElevenLabs/Sarvam voice agents, calling-conduct compliance | 12,100 |
| `phases/P08_Six_Vertical_Packs.md` | FIN, COM, FAM (incl. property/succession), INS, WRK, INT rule packs, forms, calculators, templates, dashboards | 22,200 |
| `phases/P09_Enterprise_GRM_POSH_SaaS.md` | APIs, bulk intake, clause API, consoles, GRM SaaS (4 variants), POSH IC SaaS, SEC connector, government connectors | 12,000 |
| `phases/P10_Private_Chambers_Academy_Campus.md` | Private ADR Chambers SaaS, ADR Academy LMS & certification, university and campus programmes | 11,500 |
| `phases/P11_Agentic_AI_Layer.md` | AI gateway, agents, RAG, AI-drafted award pipeline, eval harness, governance console | 8,500 |
| `phases/P12_Mobile_Apps_Parity_and_Release.md` | Expo apps: parity, offline, biometrics, hearings, payments, store release | 10,800 |
| `phases/P13_Public_Website_CMS_SEO_Growth.md` | New website, website remediation, CMS + claims register, programmatic SEO, free tools, CRM, referrals | 7,600 |
| `phases/P14_Hardening_Compliance_GoLive.md` | Security, CERT-In, DPDP, performance, DR, UAT, migration, legal sign-off, launch | 9,300 |
| `appendices/A_Workflows_and_State_Machines.md` | Case and mechanism state machines, ladders per vertical, compliance clock reference | 13,700 |
| `appendices/B_Fee_Engine_and_Rate_Cards.md` | Fee-engine spec and default rate cards (INR; USD/EUR/GBP/SGD/AED for INT), taxes, refunds, concessions | 13,800 |
| `appendices/C_Screen_Inventory_and_UX.md` | ~350 screens by portal, navigation maps, dashboards, design system, UX principles | 10,400 |
| `appendices/D_Integration_Adapter_Specifications.md` | TypeScript port interfaces, providers, webhooks, failover, Infrabyx and government connectors | 10,900 |
| `appendices/E_AI_and_Voice_Agent_Specification.md` | Agent contracts, guardrail register, evals, 40+ red-team scenarios, voice scripts (EN/HI), AI Governance Rule | 12,300 |
| `appendices/F_Data_Model_Events_and_Errors.md` | Canonical PostgreSQL DDL, 160 domain events, 115 error codes, API resource map | 17,500 |
| `appendices/G_Legal_Rules_Register.md` | 246 product-enforceable legal rules with sources, status (Oct 2026), enforcement points and flags | 20,400 |
| `appendices/H_Competitive_Differentiation_GTM_and_Website_Corrections.md` | Competitor matrix, differentiators D1–D12, GTM features, **60 website corrections with replacement copy**, safe-claims library | 9,700 |
| `appendices/I_Acceptance_Tests_and_UAT_Catalogue.md` | NN-rule test suite, 27 UAT journeys, non-functional tests, sign-off matrix | 7,400 |
| `appendices/J_Verification_Log_and_Open_Items.md` | Research log for all 514 [VERIFY] flags, material corrections, outcome of management decisions M-05/M-06, open-items register by owner | 8,200 |
| `Equator_Build_Prompt_Pack_v1.docx` | Consolidated Word copy of all of the above for review and sign-off | — |

## 3. How to run the build

1. Create an empty repository and open the coding agent in it.
2. For each phase, start a session by pasting **`01_MASTER_PROMPT.md`**, then the **phase file**, then attach (or paste) the appendices the phase cites. Phase order: **P00 → P14** (P13 may run in parallel with P08–P11 with a second squad; mobile work starts in P01 and closes in P12).
3. The agent must produce `docs/phases/PXX-plan.md` before coding, and stop at the phase exit gate (§13 of each phase file).
4. Review the demo and open-items file at each gate; approve before starting the next phase.
5. Where a phase is long, instruct the agent to split it into sub-iterations (P08a FIN+COM, P08b FAM+INS, P08c WRK+INT) without dropping requirements (Master §15, X-17).

Indicative effort: 14 phases ≈ 30–36 two-week sprints with two squads (platform + verticals), plus a growth/website squad for P13.

## 4. Decisions and approvals needed from Equator management before go-live

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Rate cards are customisable in the fee editor and approval-gated (decided, M-01); Board approval of the default schedules (Appendix B) before publication | Board / CFO | P05 go-live, P13 fees page |
| 2 | Entity confirmed as **Equator Resolution Service Private Limited** (decided, M-02); supply CIN, registered office, GSTIN, DPO and Grievance Officer (Master X-15) | Company Secretary | P13, P14 |
| 3 | Approve Equator Rules of Arbitration, Mediation Rules, vertical rules and Code of Conduct for neutrals (versioned rulebooks) | Board / Legal | P04, P08 |
| 4 | Decided 19 Oct 2026 (Master §16): M-03 lender-arbitration defensibility position (NN-03); M-04 Mediation Act statutory mode behind a flag and Singapore Convention consent-award route (NN-05, NN-19); **M-05** Equator places its own automated/AI calls under the NN-12 design — DLT Principal Entity with CPaaS as telemarketers, lender 1600-number mode by default for FIN/INS regulated-tenant matters, Equator's own DID numbers declared as A2P CLI ranges behind `voice.equator_service_number.enabled` = OFF, 1601 application once legal/ODR services are notified; **M-06** voluntary pre-suit mediation and A&C Part III conciliation live now, mandatory s.12A PIMS stays with the Legal Services Authority (Form-1 pack) until the four gates close, `com.s12a_equator_authorised` = OFF. Remaining legal checks: (a) operator written confirmation and telecom-counsel opinion on the CLI type for Equator's own service calls (M-05); (b) med-arb same-neutral practice; (c) cross-border data transfer for INT; (d) notification watch for the M-06 gates (Mediation Act Ninth Schedule, MCI regulations and MSP recognition, Central Government notification under the new s.12A(2)(ii), new rules) and for Mediation Act ss.27–28 | General Counsel / external counsel | P07, P08, P13 |
| 5 | Close the remaining **[VERIFY — open]** items (about 170 after research closed most of the original 514; register in Appendix J §J.5, by owner) and set Legal Rules Register status | Legal counsel / tax adviser / CTO | Feature flags |
| 6 | Vendor contracts: ElevenLabs (Enterprise, India residency), Exotel/Plivo, Gupshup, MSG91, Leegality, Digio, Surepass, Razorpay (Route, Escrow+), Castler, LiveKit, AWS (Bedrock India) | CTO / Procurement | P05–P07 |
| 7 | Panel strategy: initial panel sizes per vertical, concentration cap (default 40% per counterparty per 24 months), neutral fee norms | Head of Institution | P03 |
| 8 | Apply the website corrections in Appendix H §5 **now** on the live site (independent of the build) | Marketing + Legal | Immediate |

## 5. Requirement coverage map

| User requirement | Where addressed |
|---|---|
| Six dispute types incl. international commercial disputes (arbitration/mediation under international law; WTO position) | Master §1.2, §5.2; P08 §4 (INT); Appendix A; Appendix G (INT rules); Appendix B (USD schedule) |
| Arbitration, mediation, med-arb | Master §1.3, §5.3; P04; Appendix A |
| Competitor parity and differentiation (Jupitice, Presolv360, Sama, SMART ODR, Sahamati and others) | Master §2; Appendix H §1–2; differentiators traced to phases |
| Latest technology, agentic AI | Master §4, §9; P11; Appendix E |
| Automated calling like ElevenLabs; Equator places its own calls (M-05) | Master NN-12, §16 M-05; P07; Appendix D (VOICE/TELEPHONY ports); Appendix E (voice scripts and policies) |
| Pre-suit (pre-litigation) mediation by Equator (M-06) | Master §1.2 (COM), §16 M-06; P08 §4.2 (FR-P08-25 row 2, FR-P08-27, F-COM-24 Form-1 pack); P13 FR-P13-16 (PIMS fee tool); Appendix H WC-59; Appendix G (LR-MED-013–015, LR-MED-018) |
| eStamp, eSign (Leegality, Digio, Surepass and others) | P01 (KYC), P06; Appendix D |
| Payment gateway | P05; Appendix B; Appendix D |
| Web and mobile platforms, backend logic and workflows | Master §4; P00–P14; P12; Appendices A, F |
| Login screens, onboarding, directory of mediators and arbitrators | P01; P03; Appendix C |
| Fee structure for resolving disputes; INR with foreign currency for international; customisable, approval-gated rate cards (M-01) | Master §7, §16 M-01; P05; Appendix B |
| Fully customisable | Master §6 (Ruleset Studio); P00; every phase §9 |
| Grievance redressal SaaS (lenders, listed companies, employers, universities) | P09 (GRM); Appendix A (grievance machine) |
| POSH/IC SaaS, Private ADR Chambers, Enterprise API, Academy | P09, P10 |
| SEBI optional | Master §1.2 (SEC, flag OFF); P09 (connector); Appendix B (SMART ODR schedule) |
| Remove/modify risky website content | Appendix H §5 (60 corrections, replacement copy) and §6 (safe claims); P13 FR-P13-01 |
| Marketing-led commercial success | P13; Appendix H §3–4; growth loops in P13 |

## 6. Key judgments embedded (read before approving)

- **AI never advises, predicts or values** a party's case (NN-01). The Dispute Explorer gives a readiness and pathway report, process cost and time from the fee engine, limitation flags and free-forum options — not merit predictions. This replaces the "viability" idea in older drafts, which carried legal and reputational risk.
- **Lender arbitration is built to survive challenge** after CORE (2024), Bhadra International (2026) and the 2025–26 Bombay and Delhi High Court rulings: clause names Equator at sanction; Equator appoints; post-dispute written s.12(5) waivers; Independence Evidence Pack per case.
- **Mediation Act 2023** core provisions (including ss.27–28 on enforcement) are treated as not yet in force (statutory mode behind a flag; MCI established 27 Aug 2026 by S.O. 4781(E), no regulations yet); India has signed but **not ratified the Singapore Convention** (25 parties as of Oct 2026), so international mediated settlements are offered conversion to consent awards for New York Convention enforcement.
- **Pre-suit mediation (M-06):** Equator runs voluntary pre-suit mediation and Part III conciliation now; it never represents that its process or report satisfies Commercial Courts Act s.12A, which stays with the Legal Services Authority until the four gates close.
- **Calling (M-05):** Equator places its own automated/AI calls only under the NN-12 telecom design (DLT registration, declared CLI ranges, consent and DND scrubbing, first-utterance disclosure).
- **WTO dispute settlement is state-to-state only**: the INT vertical handles private commercial disputes under international commercial law and rules (UNCITRAL, IBA, institutional rules), records trade-measure impacts, and signposts trade-remedy matters (DGTR/DGFT/Ministry of Commerce); no WTO or investor-state cases.
- **Settlement money never passes through Equator's merchant account** (bank escrow with trustee), per the RBI Payment Aggregator Directions (15 Sep 2025).
- **POSH, health and family-safety data are sealed** in separate schemas with separate keys.
