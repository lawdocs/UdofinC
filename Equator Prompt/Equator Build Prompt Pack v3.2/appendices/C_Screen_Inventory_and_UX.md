# Appendix C — Screen Inventory and UX Specification

> Binding reference for every phase prompt. It lists every screen in Equator Resolution across P00–P14, grouped by portal, with the navigation maps, persona dashboards, design-system summary, UX principles and the case-status tracker specification. Phase prompts own the detailed field lists for their screens; this appendix owns the catalogue, the tokens and the cross-cutting UX rules. *(v3.1)* **Navigation, menus, shells, the Work Inbox, search, the command palette, dashboard composition and the workflow pattern library are owned by Appendix AG** (AG.0.3 rule 3: AG supersedes §C.1–§C.3 below; §D remains the widget defaults, extended by AG.6); screens of v3 phases P15–P21 are catalogued in those phases' §6 tables and placed in menus by AG.2, and the screens AG proposes (AG-SCR-01…27) are registered in AG.2.14.

## A. Conventions

1. **Screen IDs.** `SCR-PXX-NN` where `PXX` is the phase that builds the screen. IDs for P00–P07, P09, P11, P12 and P14 are taken from those phase prompts and are authoritative there. IDs for **P08 and P10** are allocated here; those phase prompts must use them. *(v3.1 correction: the P13 phase IDs SCR-P13-01…19 prevail over the v1 allocation in this appendix (D3-47(c); master X-51 cites SCR-P13-18 in the P13 sense); C IDs without a P13 counterpart are renumbered SCR-P13-40…58 per the Appendix AG §AG.2.1 renumbering map, applied in §B.1, §B.14 and §B.16; SCR-P13-20…22 are aliases of SCR-P13-44 and are not reused; SCR-P13-50 is unallocated. Reserved ranges: SCR-P02-60…79 (Appendix L, L-D-13), SCR-P02-80…99 and SCR-P06-60…79 (Appendix R, R-R10), SCR-P06-40…59 and SCR-P11-40…49 (L-D-13), SCR-P13-60…69 (Decisions Library, R §3.9). Appendix AE's `SCR-AE-01…12` are aliases of the canonical SCR-P21-AE01…AE12 (AG.0.5 #11). A CI script fails if any screen ID has two meanings across the pack (FR-P13-V31-AG02).)* A phase that needs a new screen appends the next number in its own series and updates this appendix in the same PR. Mobile-only variants use `SCR-PXX-Mnn` (party), `Nnn` (neutral) or `Enn` (enterprise-lite) where the phase defines them.
2. **Route roots.** Public site `/(public)`; authenticated portals `/app/...`; staff console `/console/...`; admin `/admin/...` (separate origin `admin.equatorresolution.in`); auth `auth.equatorresolution.in`; white-label GRM portals `{slug}.grievance.equatorresolution.in`; developer portal `developers.equatorresolution.in`; status page `status.equatorresolution.in`. *(v3.1, D3-47; Appendix AG §AG.1.7 governs routes.)* Operations Platform `ops.equatorresolution.in` with host-relative routes (`/crm`, `/mkt`, `/hr`, `/time`, `/pay`, `/controls`, `/org`, `/me`, `/group`, …; no `/ops` prefix, old paths 301; `/audit` = SCR-P16-41 with `/audit/workforce` = SCR-P18-43; `/exports` = SCR-P21-09); auditor workspace `assurance.equatorresolution.in`; chambers workspace `/chambers/*` with shell root `/chambers/work` (`/app/chambers/*` 301s); chambers workspace segments `work`, `workload`, `hr`, `me`, `controls`, `dashboards`, `inbox`, `settings`, `exports`, `offboarding`, `approvals` and `reports` are reserved slugs (`CHM_SLUG_RESERVED`; AG.0.5 #6). Redirected routes are listed in `cfg.route_redirects` for 12 months.
3. **Mandatory states for every screen:** empty, loading (Skeleton), error (InlineAlert with problem `code` and `traceId`), success; plus `sealed/redacted`, `offline/queued` and `read-only` where applicable.
4. **Sealed screens** (POSH IC workspace, health data, family safety data, caucus notes) carry the `SealedBanner`, are screenshot-protected on mobile, never cached offline, require step-up on entry and are excluded from analytics instrumentation (NN-07, NN-11).
5. **"Key widgets"** below name design-system components (§E.4) or domain widgets; the phase prompt specifies fields.

## B. Screen catalogue by portal

### B.1 Public website (indexable, SSR/SSG; P13 unless stated)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P13-01 | Home | public | P13 | "What happened?" single entry; positioning line; trust strip | Hero with Explorer CTA, 6 vertical tiles, free-forum notice, claims-register-backed stats block, LanguageSwitcher |
| SCR-P13-02 | Vertical landing (FIN, COM, FAM, INS, WRK, INT) | public | P13 | Per-vertical explainer naming the free/statutory forum first (NN-20) | SignpostCard list, mechanism explainer, fee teaser, FAQ (FAQPage JSON-LD), QuickExit on FAM |
| SCR-P13-02 | International pages (v1 C ID SCR-P13-18; INT hub, merged) *(v3.1)* | public | P13 | `INT` offer, seats, Singapore Convention status note, NYC enforcement | Currency fee table, model clause, country pages |
| SCR-P13-03 | Programmatic page (dispute type × city × language) | public | P13 | Long-tail landing | Unique copy blocks, local office NAP, Explorer CTA; `LegalService` JSON-LD **off by default** (master X-42) |
| SCR-P13-04 | Enterprise demo request (v1 C ID SCR-P13-15; demo form on `/for/{segment}`) *(v3.1)* | enterprise prospects | P13 | B2B lead | Volume band (<100, 100–500, 500–2,000, >2,000), sector, consent (unbundled) |
| SCR-P13-05 | Grievance Redressal and POSH Internal Committee SaaS pages (`/grievance-redressal`, `/posh-internal-committee`) *(v3.1)* | CS/compliance buyers | P13 | Variant explainer with regulator clocks from the Legal Rules Register | Clock table, tools CTA (SCR-P13-12), no client logos without a claim |
| SCR-P13-06 | Fee card | public | P13 | Published, calculator-driven fees (D7) | Tabs by vertical/mechanism, currency switch (INT), "Subject to Board approval" label, embeds SCR-P05-01 |
| SCR-P05-01 | Fee calculator widget | public | P05 | Indicative quote | MoneyInput, QuoteBreakdown, GST line, disclaimer |
| SCR-P13-07 | Rules, procedure and Code of Conduct (v1 C ID SCR-P13-05) *(v3.1)* | public | P13 | Versioned rulebooks rendered from `core.procedure_rules` | Version picker, diff link, PDF with hash, effective dates |
| SCR-P13-08 | Neutral directory pages (`/neutrals`, `/neutrals/{slug}`, `/neutrals/panels`) *(v3.1)* | public | P13 | Public rendering of SCR-P03-01/-02 | Filters, seeded-random order, no win-rates (NN-03, NN-28) |
| SCR-P13-09 | Trust centre (v1 C ID SCR-P13-11; `/trust/*`) *(v3.1)* | public | P13 | Security, sub-processors, DPA, certificates (only those held), VAPT summary, DPO | Evidence-linked badges (Claims Register), downloads |
| SCR-P13-09 | Published outcomes and statistics (v1 C ID SCR-P13-19; `/trust/outcomes`) *(v3.1)* | public | P13 | Anonymised process KPIs incl. awards set aside count (D12); never win-rates | Charts from Claims Register entries with source/date |
| SCR-P13-10 | About, Council, Secretariat (v1 C ID SCR-P13-12) *(v3.1)* | public | P13 | Institution credibility | Profile cards with roles; no implied regulator status |
| SCR-P13-11 | Contact (`/contact`) *(v3.1)* | public | P13 | Entity block, office NAP, contact form, Grievance Officer and DPO | Contact form with deflection to Help (SCR-P16-43) |
| SCR-P13-12 | Calculators hub (v1 C ID SCR-P13-08; tool variant `calculators`) *(v3.1)* | public | P13 | Litigation vs ODR cost/time, s.12A fee, MSMED interest, limitation checker, arbitration fee | Calculator cards; outputs labelled indicative |
| SCR-P13-12 | POSH compliance checker + Board-report annexure (v1 C ID SCR-P13-09; tool variant `posh-checker`; variant page SCR-P13-05) *(v3.1)* | public, CS buyers | P13 | Compliance-led entry (L5) | Questionnaire, gap list, annexure DOCX |
| SCR-P13-12 | Grievance SLA health check (v1 C ID SCR-P13-10; tool variant `grievance-sla-check`) *(v3.1)* | NBFC/LSP | P13 | Upload complaint log → 30-day breach analysis | FileUpload (CSV), breach chart, RB-IOS risk band, lead capture with consent |
| SCR-P13-13 | Clause generator (v1 C ID SCR-P13-07) *(v3.1)* | public, enterprise | P13 | Model clause with registered clause ID | Form (dispute type, seat, ladder, language, rules version), preview, DOCX/PDF, "adopt" CTA |
| SCR-P13-14 | Book a consultation call (Appendix B `ANC.CONSULT`: ₹999 for 30 min / ₹1,999 for 60 min, credited against registration if filed within 30 days; the v1 "₹1,000" is superseded) | public | P13 | Paid pre-litigation call | Slot calendar, Razorpay checkout, recording-consent toggle, GST invoice |
| SCR-P13-15 | Partner programme page and partner portal shell (`/partners`, `/app/partner/*`; tabs SCR-P13-53…58 in B.14) *(v3.1)* | public, partner | P13 | Programme explainer and portal entry | Professional-rules notice (advocates, CAs, CSs, CMAs get no reward — X-62) |
| SCR-P13-19 | Lead preferences (`/preferences/{token}`) *(v3.1)* | lead | P13 | Consent and channel preferences, withdraw, by signed link without login | PurposeToggle, withdraw button |
| SCR-P13-40 | How it works / methods of ADR (v1 C ID SCR-P13-04) *(v3.1)* | public | P13 | Ladder explainer | Stepper diagram, mechanism cards, "Equator is not a court" note |
| SCR-P13-41 | Mechanism page template (`/mechanisms/{mechanism}`; Appendix P P-21–P-27) *(v3.1)* | public | P13 | Negotiation, conciliation, mediation, arbitration, med-arb, pre-litigation mediation, expert determination | Explorer CTA; med-arb and expert determination per master §5.2 |
| SCR-P13-42 | Dispute subtype page template (P-10–P-19) *(v3.1)* | public | P13 | Popular situations with Explorer CTA | Published only with a legal review stamp |
| SCR-P13-43 | Become a neutral (`/neutrals/join`; P-36) *(v3.1)* | prospective neutrals | P13 | Eligibility and apply (→ SCR-P03-03) | No earnings promises |
| SCR-P13-44 | Pricing (`/pricing/organisations`, `/pricing/professionals`, `/pricing/business-assure`; P-39; aliases SCR-P13-20…22, not reused) *(v3.1)* | buyers, professionals, MSMEs | P13 | Plan cards with GST (Appendix O §3.1) | Plan cards, segment selector |
| SCR-P13-45 | Private ADR Chambers product page (`/private-adr-chambers`; P-34) *(v3.1)* | practitioners | P13 | Product, practice pages, HR add-on "subject to availability" | Trial CTA → SCR-P10-01 |
| SCR-P13-46 | Training overview (`/training`; P-37) *(v3.1)* | learners | P13 | Programmes and dates | Provider cards; Institute card gated by `academy.institute_referral` |
| SCR-P13-47 | Resources and blog (v1 C ID SCR-P13-13) *(v3.1)* | public | P13 | Legal-reviewed content | Article with citation fields, author credential card, "last legally reviewed" stamp |
| SCR-P13-48 | Legal pages (v1 C ID SCR-P13-16) *(v3.1)* | public | P13 | Terms, Privacy (itemised notices from P01), Cookies, Disclaimer, Grievance Officer | Version stamp, language switch |
| SCR-P13-49 | Cookie consent banner (v1 C ID SCR-P13-17) *(v3.1)* | public | P13 | Essential always on; analytics/functional opt-in; no advertising cookies | Accept / Reject (equal prominence) / Settings |
| SCR-P13-60 → SCR-P13-63 | Equator Decisions Library (Appendix R §3.9; SCR-P13-64…69 reserved) *(v3.1)* | public | P13 | Search consented published outcomes (NN-26) | Filters, citation copy, hash |
| SCR-P02-01 | Dispute Explorer — start | anonymous, party | P02 | DPDP notice, consent, language, QuickExit | ConsentCheckbox, "answer questions instead" toggle |
| SCR-P02-02 | Dispute Explorer — guided capture | anonymous, party | P02 | Facts capture, ≤ 3 clarifying questions | Chips, DatePicker, MoneyInput, optional upload |
| SCR-P02-03 | Readiness & Pathway Report | anonymous, party | P02 | Deterministic route, clocks, free forums, cost | SignpostCard, ClockPill, QuoteBreakdown, CTAs |
| SCR-P11-14 | Dispute Explorer with AI (upgrade of P02-01/02) | public, party | P11 | AI-assisted intake with deterministic fallback (NN-02) | DisputeExplorerChat, "Use step-by-step questions instead", AiDraftBanner |
| SCR-P02-17 | Public case-status tracker | anonymous | P02 | Status by reference + OTP (§G) | CaseNumber input, CAPTCHA (audio alt), OTPInput, CaseStatusTimeline (public) |
| SCR-P02-22 | Verify a document (hash/QR) | anonymous | P02 | Integrity check | FileUpload/hash paste, VerifyBadge |
| SCR-P06-12 | Verify an outcome document | public | P06 | Award/settlement verification by code | VerifyBadge, issuing registrar, hash, stamp details |
| SCR-P09-05 | Verify clause seal | public | P09 | Clause registration check | Clause ID, version, adopter (if public) |
| SCR-P03-01 | Neutral directory | public | P03 | Search verified neutrals (D12) | Facets, NeutralCard, seeded-random order (no ranking by outcome) |
| SCR-P03-02 | Neutral public profile | public | P03 | Verified credentials, languages, fees | Badges with method/date/expiry, availability, ratings (aggregate only at n ≥ 10 — master X-28), no win-rates, no paid or featured placement (NN-28) |
| SCR-P03-22 | Request this panel neutral (v1 "Book a neutral"; X-59(a)) | party | P03 | Direct request where rules allow | Eligibility check, quote, payment hold |
| SCR-P01-09 | Notice-link landing `/r/{code}` | respondent | P01 | Minimal preview + possession check | Case number, dates, "This is me / not me" |
| SCR-P07-18 | Opt-out / preference landing `/u/{token}` | recipient | P07 | Channel opt-out without login | Scope confirmation, legal-notice continuation explanation |
| SCR-P14-10 | Status page | public | P14 | Service availability | Component status, incident history |
| SCR-P14-11 | Security / VDP | public | P14 | Vulnerability disclosure | `security.txt`, report form |

### B.2 Authentication and onboarding (all personas; P01)

| ID | Screen | Persona | Purpose | Key widgets |
|---|---|---|---|---|
| SCR-P01-01 | Universal sign-in hub | all | Choose method | Method buttons, SSO link, "I received a notice", LanguageSwitcher |
| SCR-P01-02 / -03 | Mobile OTP request / verify | all | OTP login | PhoneInput, channel choice, OTPInput, resend timer |
| SCR-P01-04 | Email magic link | all | Passwordless email | Cross-device code state |
| SCR-P01-05 / -06 | Password / second factor | professionals | Credential + MFA | Passkey autofill, TOTP, recovery code |
| SCR-P01-07 | SSO discovery | enterprise, staff, university | Domain → IdP | Email field, generic error |
| SCR-P01-08 | DigiLocker sign-in | parties | DigiLocker via licensed provider | Explainer (Aadhaar stays masked) |
| SCR-P01-10 | Sign-up | parties, org, neutral applicants, learners, partners | Persona fork | Persona cards |
| SCR-P01-11 | Itemised privacy notice and purposes | all | DPDP notice + consents | PurposeToggle (unticked optional), accordion items, rights links |
| SCR-P01-12 | Personal profile | party | Minimal profile | Address with PIN lookup, notice language |
| SCR-P01-13 → -17 | KYC chooser, PAN, liveness, video KYC, passport/OCI | identity-verifying users | K1–K3 | Level progress, provider SDK, slot picker, MRZ scan |
| SCR-P01-18 | Guardian consent | minors, PwD | Verifiable guardian consent | Guardian invite, relationship, proof |
| SCR-P01-19 → -22 | Organisation KYB, signatories & authority, members, foreign KYB + UBO | org users, admins | KYB and authority | AuthorityMatrix, MoneyInput limits, UBO repeater |
| SCR-P01-23 | Bank verification | payees | Penny-drop | IFSC lookup, name-match result, cooling-off banner |
| SCR-P01-24 / -25 | Counsel enrolment / mandate | counsel, party | Credential + mandate | Verification badge, scope checkboxes, sign/accept/revoke |
| SCR-P01-26 / -27 | Neutral application start / wizard | applicants | Application (empanelment in P03) | Stepper (7 steps), autosave |
| SCR-P01-28 → -37 | Staff, enterprise, SSO set-up, GRO, IC (sealed), university, student, learner, partner, JIT elevation | respective roles | Persona onboarding | Checklists, undertakings, SSO test, SealedBanner (IC) |
| SCR-P01-38 | Role and tenant switcher | multi-role users | Context switch | Tenant logo + role chip list, step-up marker |
| SCR-P01-39 → -42 | Profile, preferences, security, privacy centre | all | Account self-service | Channel order, quiet-hours range, devices/sessions, consents, DSR |
| SCR-P01-43 | Account recovery | all | Recovery paths | 72-hour hold status |
| SCR-P03-03 / -04 | Neutral application (empanelment wizard) / status | applicants | Full empanelment application and tracker | DOC_AI prefill with confirm, conflict grid, interview booking |

### B.3 Party portal (`/app`, roles `party`, `party_org_user`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P02-04 | Filing wizard | party, party_org_user | P02 | File a case (5 steps) | Stepper, form engine, quote panel, pinned-version footer |
| SCR-P02-07 | Respond to a case | respondent | P02 | Response, counterclaim, objection | Plain-language explainer, deadline ClockPill, free-forum cards |
| SCR-P02-09 | Deficiencies | filer | P02 | Cure defects | Deficiency list with pointers, upload, extension request |
| SCR-P02-10 | Routes and signposting | party | P02 | See allowed/blocked routes | SignpostCard with last date, acknowledgement |
| SCR-P02-13 | Documents | case members | P02 | DMS | Folder tree, upload/scan status, exhibit labels, versions |
| SCR-P02-16 | Case workspace | case members | P02 | Hub: overview, timeline, parties, claims, documents, notices, clocks, tasks, links | Tabs, CaseStatusTimeline, ClockPill |
| SCR-P02-19 | Withdraw | party | P02 | Withdraw (full/partial) | Fee-consequence panel, step-up |
| SCR-P08-01 | FIN loan-dispute intake panel | borrower, lender | P08 | Loan facts (lender type, loan type, outstanding vs disputed, NPA date, SARFAESI 13(2)/13(4), NI Act s.138 status) | Form engine section, SignpostCard (RBI Ombudsman/DRT) |
| SCR-P08-02 | OTS / instalment calculator | borrower, lender | P08 | Indicative OTS and schedule from party-provided parameters (no valuation; NN-01) | MoneyInput, schedule table, "indicative" label |
| SCR-P08-03 | NI Act s.138 compounding panel | parties | P08 | Stage-wise compounding cost display per *Sanjabij Tari* (2025) (nil before defence evidence; 5% before trial judgment; 7.5% Sessions/HC; 10% SC) | Stage selector, cost table |
| SCR-P08-04 | COM MSME panel | MSME claimant | P08 | Udyam check, MSMED s.16 interest, MSEFC sub-track signposting | Interest calculator, SignpostCard (MSEFC/MSME ODR) |
| SCR-P08-05 | s.12A pre-institution mediation panel | commercial parties | P08 | PIMS information and Form-1 pack for the Legal Services Authority; voluntary Equator pre-suit mediation offered separately; never represents an Equator report as satisfying s.12A (master M-06; flag `com.s12a_equator_authorised` OFF) | Clock preview, fee preview (PIMS Rules 2018 Schedule II), Form-1 pack download |
| SCR-P08-06 | FAM family-property builder | heirs, family members | P08 | Family tree + property schedule for partition/HUF/succession | Tree editor (keyboard alternative per WCAG 2.5.7), property list, registration warning (NN-08) |
| SCR-P08-07 | FAM affidavit of assets and liabilities | spouses | P08 | *Rajnesh v Neha* disclosure (F-07) | Tables (income, assets, liabilities, expenses), perjury declaration |
| SCR-P08-08 | FAM parenting-plan builder | parents | P08 | Child arrangements "subject to court approval" | Schedule grid, child-welfare prompts |
| SCR-P08-09 | FAM safety screening (sealed) | party (own), safeguarding_lead | P08 | Confidential screening; never shown to the other side | SealedBanner, QuickExit, safeguards plan |
| SCR-P08-10 | INS policy and claim intake + health-data consent | policyholder | P08 | Policy, claim, repudiation; separate health consent (F-I01) | Form section, PurposeToggle (health), SignpostCard (Bima Bharosa/Ombudsman) |
| SCR-P08-11 | INS Ombudsman eligibility and limitation checker | policyholder | P08 | Deterministic eligibility, last dates | Checklist, ClockPill |
| SCR-P08-12 | WRK F&F and gratuity calculator | employee, employer | P08 | Statutory dues computation (Code on Wages, SS Code) | Calculator, "dues cannot be waived" note |
| SCR-P08-13 | WRK workman / arbitrability panel | parties | P08 | Workman flag gates arbitration | Questionnaire, blocked-route reasons |
| SCR-P08-14 | INT intake gates | foreign/Indian companies | P08 | Seat, laws, enforcement targets, sanctions/FEMA/DPDP s.16 gates (NN-19) | Gate checklist, currency selector |
| SCR-P08-15 | Limitation checker | party | P08 | Indicative limitation dates (Limitation Act 1963 rules as config) | Date inputs, result with legal-rule refs |
| SCR-P04-01 | Proceedings ladder | case members | P04 | Rungs, current, next | Ladder view, consent status |
| SCR-P04-02 | Negotiation | parties, counsel | P04 | Offers and counters | OfferCard, offer timeline, equality-of-arms banner |
| SCR-P04-03 | Blind bid | parties | P04 | Sealed bids | BlindBidInput, round timer, result card |
| SCR-P04-08 | Filings (arbitration) | parties, counsel | P04 | Pleadings and applications | Due list, upload, leave request |
| SCR-P04-10 | Emergency arbitrator application | parties | P04 | EA request | Urgency checklist, tracker |
| SCR-P04-11 | Consent instruments | parties | P04 | Agreement to mediate, s.30 online mode, recording, role switch, s.12(5) waiver, s.29A extension | Explainer, ESignPanel |
| SCR-P04-13 / -14 | Hearing lobby / room | participants | P04 | Join session | Device check, face match, video grid, captions, interpreter channel |
| SCR-P04-15 | E-bundle viewer | participants | P04 | Follow presenter | Page sync, exhibit search |
| SCR-P04-18 | Adjournment | parties | P04 | Request adjournment | Cost-order notice |
| SCR-P04-21 | Internal appeal (D4) | parties | P04 | Appeal notice and record | Grounds, panel status |
| SCR-P03-11 / -12 / -14 / -15 | Appointment list, joint nomination, disclosures, challenges | parties | P03 | Party participation in appointment (NN-03) | Candidate cards, strike toggles, objection form |
| SCR-P03-16 | Independence Evidence Pack | parties, tribunal, enterprise | P03 | D1 evidence | Version list, hash, download |
| SCR-P03-21 / -23 | Complaint about neutral / feedback | parties | P03 | Quality loop | Form, "did you feel pressured to settle?" |
| SCR-P05-02 → -05 | Checkout, receipts, case billing, concession request | parties | P05 | Pay and track fees | QuoteBreakdown, UPI intent, GST invoice, waiver form |
| SCR-P05-09 / -10 | Escrow view / instalments | parties | P05 | Settlement money tracking (NN-13) | Milestones, mandate status |
| SCR-P06-02 / -03 | Heads-of-terms / settlement editor | parties, counsel | P06 | Agree terms | Clause list, settlement linter results |
| SCR-P06-07 | Signing room | signatories | P06 | eSign | ESignPanel, pre-sign summary, hash |
| SCR-P06-09 / -10 | eStamp / physical execution and registration | parties | P06 | NN-08, NN-09 | EStampBadge, registration checklist, appointment booking |
| SCR-P06-13 / -14 / -15 | Evidence export, execution pack, compliance tracker | parties | P06 | Post-outcome | s.63(4) certificate, pack builder, instalment grid |
| SCR-P07-04 | Case communications timeline | party (own) | P07 | Every message attempt with evidence | Channel icons, status chips |
| SCR-P07-06 | Preference centre (case level) | party, counsel | P07 | Purposes, language, time slider (bounded) | PurposeToggle, time range |
| SCR-P07-17 | Notification inbox — list UI superseded by the Work Inbox AG-SCR-01 (data source kept; becomes its Updates tab, FR-P00-V31-AG03) *(v3.1)* | all | P07 | In-app notifications | Unread filter, case filter |
| SCR-P11-09 | Party-validation screen | party, counsel | P11 | Confirm/correct AI-extracted facts (D3) | Item list with source page preview, AiDraftBanner |
| SCR-P11-12 | AI use on this case | parties | P11 | AI-use notice and objection | Tool log, objection form |

### B.4 Counsel (`/app/counsel`, role `counsel`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-30 | Counsel dashboard | counsel | P10 | Client matters across mandates | Matter list with ClockPill, filings due, hearings, mandate expiry |
| SCR-P02-05 | File on behalf of client | counsel | P02 | Filing under mandate | Mandate selector, client OTP confirmation status |
| SCR-P01-25 | Mandates | counsel | P01 | Request/accept/revoke | Scope view, verification badge |
| SCR-P01-24 | Enrolment verification | counsel | P01 | Bar credential | Status chip, re-verification date |
| Shared | SCR-P02-07, -09, -13, -16; SCR-P04-02, -08, -11, -13/-14; SCR-P06-03, -07, -13, -14 | counsel | P02–P06 | Same screens as party, filtered by mandate scope | Scope badge on every action ("Your mandate allows: …") |

### B.5 Neutral workspace (`/app/neutral`, `/neutral/...`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P03-17 | Neutral dashboard | neutral_* | P03 | Today's work | StatCards (active cases, amber/red clocks, hearings, offers, CPD, payouts), task list, calendar strip |
| SCR-P03-13 | Appointment offer | neutral_* | P03 | Accept/decline with disclosure | Countdown, disclosure form (Sixth Schedule for arbitrators), ESignPanel |
| SCR-P03-18 | Availability | neutral_* | P03 | Weekly grid, exceptions | Calendar grid with keyboard entry |
| SCR-P03-19 | Scorecard | neutral_* | P03 | Process KPIs (never win-rates; NN-16) | KPI tiles, feedback aggregates |
| SCR-P03-20 | CPD and recertification | neutral_* | P03 | CPD hours | Progress bar, evidence upload |
| SCR-P03-24 / SCR-P05-06 | Earnings and payouts | neutral_* | P03/P05 | Fee notes, payouts, TDS | Statement table, payout status |
| SCR-P05-07 | Tax and bank profile | neutral_* | P05 | PAN, GST, bank, DTAA (INT) | Bank verification, step-up |
| SCR-P03-25 | Public profile editor | neutral_* | P03 | Per-field display consent | Preview, bio lint warnings |
| SCR-P04-04 | Mediation/conciliation workspace | mediator, conciliator | P04 | Sessions, safeguards, authority confirmations | Session list, agreement status, SealedBanner for safeguards |
| SCR-P04-05 | Caucus notes (sealed to author) | author neutral | P04 | Private notes (NN-11) | Encrypted editor, autosave |
| SCR-P04-06 / -07 | Arbitration console / PO1 builder | tribunal | P04 | Constitution, timetable, s.29A | Gantt timetable, ClockPill (s.29A), PO1 sections |
| SCR-P04-12 | Session scheduling | neutral, case_manager | P04 | Fair slot finding | Per-participant local time, holiday flags |
| SCR-P04-16 | Attendance register | neutral | P04 | Confirm attendance and identity results | Register table |
| SCR-P04-17 | Order composer | neutrals | P04 | Procedural orders | Template picker, AiDraftBanner, sign and serve |
| SCR-P04-19 | Hybrid switch panel | neutral, registrar | P04 | Med-arb role switch, arb-med seal, AMA | Guard status checklist (master §5.3) |
| SCR-P04-20 | Expert determination | neutral_expert | P04 | ToR, site visit, determination | Evidence capture, draft/final |
| SCR-P06-01 | Outcome workspace | neutral | P06 | Draft outcome | Type selector, maker–checker status |
| SCR-P06-05 | Award builder | neutral_arbitrator | P06 | Reasoned award | Sections, citations to bundle pages, sign |
| SCR-P11-10 | Award workbench (AI skeleton) | neutral_arbitrator | P11 | AI drafts, human decides (D3) | Suggestion chips, locked sections, attestation |
| SCR-P11-11 | AI assist panel (component) | neutral, case_manager, GRO | P11 | Run agent with sources | Accept/edit/reject, feedback |

### B.6 Case-manager console (`/console`, role `case_manager`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-31 | Case-manager dashboard | case_manager | P10 | Queue overview (built with P02 data; listed under P10 for consolidation) | Queue counts, SLA breaches, clocks amber/red, service failures |
| SCR-P02-08 | Scrutiny queue | case_manager, registrar | P02 | Accept/deficient/signpost/reject | SLA timers, checklist, rule-trace viewer, duplicate candidates; list keys per AG §AG.5.5 (`J`/`K` next/previous, `X` select, `Enter` open; single-key shortcuts remappable in AG-SCR-11); decision keys only open the decision panel with confirmation — no shortcut accepts, rejects or serves (AG.5.5 rule 3) *(v3.1)* |
| SCR-P02-33 | Pre-litigation case-manager queue (Appendix K §5.10) *(v3.1)* | case_manager | P02 | Exception-first queue of pre-litigation engagements | Saved views, next-best-action panel, previewed bulk actions, leave delegation (PAT-03, PAT-04) |
| SCR-P02-11 | Clocks cockpit | case_manager, registrar | P02 | Owned statutory clocks (NN-04) | ClockPill table, owner assignment, blocking tasks |
| SCR-P02-12 | Notice composer | case_manager | P02 | Notices and service | Template, language, channels, window guard (NN-12), attempt timeline |
| SCR-P02-14 | Bundle builder | case_manager | P02 | E-bundles | Drag-and-drop with keyboard alternative, index preview |
| SCR-P02-15 | Evidence ledger and s.63(4) certificate | case_manager, registrar | P02 | NN-10 | Ledger table, chain verify, certificate generator |
| SCR-P02-18 | Linked matters and consolidation | case_manager, registrar | P02 | Links | Graph, consolidation wizard (maker–checker) |
| SCR-P06-08 | Signing tracker | case_manager | P06 | Envelope status | Signer list, reminders |
| SCR-P06-17 | Closure checklist | case_manager | P06 | Closure guards (owned clocks, signposting, registration) | Checklist with blocking reasons |
| SCR-P07-05 | Service evidence and deemed service | case_manager, registrar | P07 | Service certificate | Evidence viewer, deemed-service evaluation |
| SCR-P07-10 | Call record | case_manager, quality_officer | P07 | Call evidence | Notices played, transcript (where lawful), QA score |
| SCR-P07-13 | Human handoff queue | support_agent, safeguarding_lead | P07 | Live transfers, callbacks | SLA timers, vulnerability flag |
| SCR-P07-14 | Speed-post batches | case_manager | P07 | Physical service | Batch builder, article number capture |
| SCR-P11-13 | Case-manager copilot panel | case_manager | P11 | Next-best actions with rule refs | Task suggestions, clock risks |

### B.7 Registrar, panel manager and institutional officers

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P03-05 | Neutral verification queue | panel_manager | P03 | Credential checks | SLA chips, verify/fail per credential |
| SCR-P03-06 | Assessment | assessor | P03 | Rubric scoring | Rubric (≥ 3 observations), divergence indicator |
| SCR-P03-07 | Committee room | committee | P03 | Empanelment/ethics decisions | Agenda, recusal, vote, e-sign |
| SCR-P03-08 | Panel health | panel_manager | P03 | Coverage and caps | Composition charts, shortage flags |
| SCR-P03-10 | Appointment run | registrar | P03 | Rule-based allocation (NN-03) | Run log (counts only), DefensibilityGauge, hard-block panel |
| SCR-P04-09 | Challenge file | registrar, committee | P04 | s.13 / rules challenges | Timeliness check, decision drafting |
| SCR-P04-22 | Safeguarding screenings | safeguarding_lead | P04 | Screening queue and safeguards | SealedBanner, re-screen schedule |
| SCR-P06-04 | Override decision (modal) | registrar, safeguarding_lead | P06 | Linter override with reasons | Reason field, audit note |
| SCR-P06-06 | Scrutiny of awards | quality_officer | P06 | Pre-issue scrutiny | Checklist, return to tribunal |
| SCR-P06-11 | Certified copies | registrar | P06 | Issue certified copies | QR, hash, register entry |
| SCR-P06-16 | Challenge-window dashboard | registrar | P06 | s.34 / s.28 windows | ClockPill list |
| SCR-P06-18 | Publication review | quality_officer | P06 | Anonymised outcome publication | Redaction checklist |
| SCR-P06-19 | Sealed-award vault | registrar, presiding arbitrator | P06 | Arb-med sealed awards | Hash, release control |
| SCR-P05-08 | Escrow console | escrow_officer | P05 | Milestones, evidence-gated release (NN-13) | Dual-control release, reconciliation |
| SCR-P07-11 | Voice QA sampling | quality_officer | P07 | QA of calls | Scorecard, calibration view |
| SCR-P03-19 (admin view) | Quality dashboard | quality_officer | P03 | Panel quality | Audits, feedback |
| SCR-P03-21 (admin view) | Ethics committee file | committee | P03 | Neutral complaints | Outcome letters |

### B.8 Enterprise console (`/app/enterprise`, roles `enterprise_admin`, `enterprise_operator`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P09-07 | Lender dashboard + ROI | enterprise_* (FIN) | P09 | Portfolio, Defensibility distribution, OTS approvals, ROI | StatCards, distribution chart, board export |
| SCR-P09-08 | Insurer desk | enterprise_admin (INS) | P09 | Claims desk, batched settlement days | Planner (≤ 30 files/day), SPOC, authority limits |
| SCR-P09-09 | Employer dashboard | enterprise_admin (WRK) | P09 | WRK portfolio, GRC, POSH status (aggregate only) | Tiles, compliance status |
| SCR-P09-10 | Listed-company investor desk | enterprise_admin | P09 | SCORES register, SRC pack | Register table, exports |
| SCR-P02-06 | Single-case filing | enterprise_* | P02 | File one case | Clause selector, GRO block (FIN) |
| SCR-P09-06 | Bulk intake | enterprise_operator | P09 | CSV/SFTP/API batches | Upload, validation report, commit/abort, notice funnel |
| SCR-P09-04 | Clause library | enterprise_admin | P09 | Clause adoption and coverage | Coverage %, version map |
| SCR-P09-02 / -03 | API keys / webhooks | enterprise_admin | P09 | Integration | Scope checklist (no sealed scopes), delivery log, replay |
| SCR-P09-11 | SLA and agreements | enterprise_admin, dpo | P09 | SLA policies; DPA status | Locked statutory rows with citation |
| SCR-P07-09 | Campaigns | enterprise_admin | P07 | Voice/WhatsApp campaigns within NN-12 | Live counters, window guard |
| SCR-P05-19 → -34 | Billing settings (`/settings/billing/*`; supersede v1 SCR-P05-11 / -12 enterprise billing and subscriptions — Appendix O O-R3; AG.0.5 #10) *(v3.1)* | enterprise_admin | P05 | Invoices, plans, payment methods, usage | Invoice list, plan cards |
| SCR-P06-15 | Compliance tracker | enterprise_operator | P06 | Settlement compliance | Instalment grid |
| SCR-P01-29 / -30 / -44 | Onboarding / SSO / people | enterprise_admin | P01 | Set-up and users | Checklist, SSO test, member table |
| — (NN-03) | No screen in this portal may list neutrals with select/rank/veto controls | — | all | Hard rule | — |

### B.9 GRM desk (`/app/grm`, roles `grievance_officer`, `internal_ombudsman`, `sgrc_member`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P09-12 | Desk inbox | grievance_officer | P09 | Ticket queue with regulator clocks | ClockPill, channel/category/language filters |
| SCR-P09-13 | Ticket | grievance_officer, internal_ombudsman | P09 | Respond, route to IO, offer ODR escalation (D5) | Timeline, AI draft + checklist (AiDraftBanner), fixed outcome taxonomy |
| SCR-P09-14 | White-label complainant portal | complainant, student | P09 | File and track | Reference + OTP tracking, escalation path to regulator |
| SCR-P09-15 | Reports and committees | GRO, admins | P09 | MIS, regulator exports; GRC/SGRC/Ombudsperson registry | Composition validators, exports |
| SCR-P01-31 | GRO profile | GRO | P01 | Public contact card | Preview |

### B.10 POSH IC workspace (sealed; `/app/posh`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P01-32 | IC onboarding | IC roles | P01 | Factors, s.16 undertaking, conflicts | SealedBanner, QuickExit |
| SCR-P09-16 | IC constitution | ic_presiding_officer, enterprise_admin | P09 | Constitution and validator (≥ one-half women; external member) | Composition validator, orders |
| SCR-P09-17 | Complaint workspace | IC members | P09 | Complaint, 90-day clock, s.10 panel (only on her written request; never monetary), inquiry, report, appeal | SealedBanner, ClockPill, watermarked viewer |
| SCR-P09-18 | External-member pool and reports (not a marketplace surface; no sponsorship — X-59(d)) | enterprise_admin, presiding officer | P09 | Engage external members; s.21/s.22 reports, SHe-Box export | Search, report generator |
| Rule | No POSH screen emits analytics events, appears in global search, or is reachable from shared dashboards (NN-07) | — | P09 | — | — |

### B.11 Private ADR Chambers admin (`/chambers/*`, shell root `/chambers/work`; `/app/chambers/*` 301s — AG.0.5 #7; role `chambers_admin`; P10, workspace v3 P20)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-01 | Chambers sign-up and trial | neutral, institution | P10 | Self-serve tenant (14-day trial) | Plan cards (₹), KYC/KYB, Razorpay subscription |
| SCR-P10-02 | Set-up wizard (F19) | chambers_admin | P10 | Brand, panels, fee schedule, allocation, templates, rules choice | Stepper, branding preview + contrast check, hosting disclaimer |
| SCR-P10-03 | Chambers dashboard — **superseded** by SCR-P20-29 (`workspace_home` dashboard at `/chambers/work`; also replaces SCR-S-D10; AG.0.5 #7, #10; Appendix W §W.7) *(v3.1)* | chambers_admin | P10 | Caseload, clocks, revenue | StatCards, ClockPill list |
| SCR-P10-04 | Overflow listing and referral opt-in (anonymised `chambers.marketplace_listings`, not a public surface — X-59(g); the public Private Practice Marketplace listing is P19) | chambers_admin | P10 | Accept referred matters | Listing editor, referral rules |
| SCR-P10-05 | Members and roles | chambers_admin | P10 | Neutrals and staff of the chamber | Member table, role bundles |
| SCR-P10-06 | Case-number series and letterhead | chambers_admin | P10 | Per-tenant prefixes and templates | Prefix editor, preview |
| Shared | Ruleset Studio (B.17), billing settings SCR-P05-19 → -34 (was SCR-P05-12) *(v3.1)*, B.5 neutral workspace and B.6 console in tenant scope | chambers roles | P10 | Reuse | Tenant branding applied |

### B.12 Academy / LMS (`/academy`, roles `learner`, `trainer`; P10)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-07 | Programme catalogue | public, learner | P10 | Versioned catalogue (T-40-S, T-20-S, workshops) | Course cards (Course JSON-LD), filters |
| SCR-P10-08 | Programme page | public | P10 | Outcomes, hours, fee, dates | Cohort list, member pricing |
| SCR-P10-09 | Enrolment and payment | learner | P10 | Register (F-01 via SCR-P01-35) and pay | Seat count, checkout |
| SCR-P10-10 | Learner dashboard | learner | P10 | Courses, attendance %, assessments, certificates | Progress, gate status (e.g., T-40 90%) |
| SCR-P10-11 | Attendance register | trainer | P10 | Session AM/PM attendance | Register grid, trainer certification |
| SCR-P10-12 | Assessment and submission | learner | P10 | Submit assessments | Upload, timers, accessibility accommodations |
| SCR-P10-13 | Grading and moderation | trainer, assessor | P10 | Marks, moderation | Rubric, second-marker view |
| SCR-P10-14 | Certificate and verification | learner, public | P10 | Issue and verify certificates | QR, register number, status (valid/revoked) |
| SCR-P10-15 | CPD record | learner, neutral | P10 | CPD hours (feeds SCR-P03-20) | Hours log, evidence |
| SCR-P10-16 | Trainer workspace | trainer | P10 | Engagements, materials, payouts | Calendar, statements |
| SCR-P10-17 | Academy admin | academy staff (institution_admin bundle) | P10 | Programmes, cohorts, go/no-go at −7 days | Task clock (−45 … +30), go/no-go panel |
| SCR-P10-18 | University partner dashboard | university_admin | P10 | Delivery vs MOU minimum, participation, scorecard | Four participation numbers (registered/attended/completed/certified), scorecard x/9 |

### B.13 Campus (`/campus`, roles `student`, `university_admin`; P10)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-19 | Cell establishment wizard | university_admin | P10 | 12-item checklist; platform-locked scope boundaries | Checklist, boundary text (read-only) |
| SCR-P10-20 | Cell referral and screening | student coordinator | P10 | Hard-stop routing for POSH, ragging, discrimination, criminal, staff–student, safety | Screening prompts; form refuses and shows referral route |
| SCR-P10-21 | Cell case log (anonymised at entry) | cell members | P10 | Log without personal data | Reference, category, outcome; "not protected by the Mediation Act 2023" notice |
| SCR-P10-22 | Supervision | Equator supervisor | P10 | Monthly supervision export | Anonymised aggregates |
| SCR-P10-23 | Competition registration | students, coaches | P10 | Teams of four, eligibility certification | Team form, Dean certification upload |
| SCR-P10-24 | Problem despatch | competition convenor | P10 | Side-locked brief despatch with logs | Despatch log, leak workflow |
| SCR-P10-25 | Draw and judge allocation | convenor | P10 | Draw rules and automatic judge conflicts | Draw table, conflict flags |
| SCR-P10-26 | Score entry (two-person) | scoring officer | P10 | System-enforced second-person verification | Scoresheet /50, discrepancy flags |
| SCR-P10-27 | Results and rankings | public, teams | P10 | Rule-based ranking signed by convenor | Ranking table |
| SCR-P10-28 | Ambassador portal | student ambassadors | P10 | Content workflow, entitlements | Draft → review → publish |
| SCR-P10-29 | Student sandbox | students, alumni | P10 | Simulated cases only (no live data, separate tenancy) | Simulated case workspace, walkthroughs |

### B.14 Partner portal (`/partners` programme page SCR-P13-15; portal `/app/partner/*`, role `partner`; P13)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P01-36 | Partner application | applicant | P01 | Apply | Professional-rules mode for advocates, CAs, CSs and CMAs (no reward fields; relationship partner, `reward_eligible = false` — X-54, X-62) |
| SCR-P13-53 | Partner dashboard (tab of SCR-P13-15; v1 C ID SCR-P13-27) *(v3.1)* | partner | P13 | Referrals, conversion, earnings (non-professional partners only) | StatCards, lead status table (no case data) |
| SCR-P13-54 | Referral links and codes (tab of SCR-P13-15; v1 C ID SCR-P13-28) *(v3.1)* | partner | P13 | Generate links/codes | Copy, QR, UTM |
| SCR-P13-55 | Co-branded landing builder (tab of SCR-P13-15; v1 C ID SCR-P13-29) *(v3.1)* | partner | P13 | Partner page | Template, logo, preview, legal review status |
| SCR-P13-56 | Clause-adoption tracking (tab of SCR-P13-15; v1 C ID SCR-P13-30) *(v3.1)* | partner | P13 | Clients adopting clauses | Adoption list |
| SCR-P13-57 | Statements (tab of SCR-P13-15; v1 C ID SCR-P13-31) *(v3.1)* | partner | P13 | Commission (TDS/GST) for non-professional partners only; advocates, CAs, CSs and CMAs receive no reward or credit of any kind (NN-17, NN-34, X-62) | Statement table, downloads |
| SCR-P13-58 | Resources (tab of SCR-P13-15; v1 C ID SCR-P13-32) *(v3.1)* | partner | P13 | Approved collateral | Downloads with version |

### B.15 Institution admin (`/admin` in tenant scope, role `institution_admin`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P10-32 | Institution dashboard | institution_admin | P10 | Panel health, allocation, fees, clocks, revenue | Widgets per §D |
| SCR-P01-44 | People and memberships | institution_admin | P01 | Users, roles, SoD | Member table, invite |
| SCR-P01-45 | Verification queue | support_agent, registrar | P01 | KYC/KYB/credentials | Watermarked viewer, two-person decisions |
| SCR-P01-46 | Privacy desk | dpo | P01 | Notices, DSR, withdrawal propagation | SLA clocks |
| SCR-P03-09 | Allocation policies | institution_admin | P03 | Method, weights, caps; dry run | Dry-run on last 500 cases |
| SCR-P07-01 → -03 | Journeys, templates, template editor | institution_admin | P07 | Communications | Journey designer, coverage matrix, SMS segment counter |
| SCR-P07-07 | Contact policy | institution_admin | P07 | Windows, caps within floors (NN-12) | Locked floor rows |
| SCR-P07-08 / -19 | Voice agent studio / helpline | institution_admin | P07 | Agents, IVR | Version list, workflow render |
| SCR-P07-12 | Communication costs | institution_admin | P07 | Cost metering | Budget caps |
| SCR-P08-16 | Vertical MIS dashboards | institution_admin, registrar | P08 | Per-vertical outcomes (settled in full/part, signposted, withdrawn) | Charts, clock-risk table |
| SCR-P05-13 → -16, -18 | Reconciliation, refunds, chargebacks, GL export, FX | finance roles | P05 | Finance operations | Recon tables, approvals |
| SCR-P11-05 / -16 | AI kill switches (tenant) / AI costs | institution_admin | P11 | AI controls | Toggle with step-up |
| SCR-P14-01 | Compliance cockpit | registrar, quality_officer | P14 | Clock risk and closure guards | "Zero expired on our watch" KPI |
| SCR-P09-20 | Lok Adalat sittings | institution_admin (LSA) | P09 | Sitting planner | Bench lists, export |

### B.16 Platform admin (`/admin`, platform scope; roles `platform_admin`, `support_agent`, `dpo`, `auditor`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P00-01 | Platform overview | platform_admin | P00 | Health | StatCards (availability, outbox lag, chain status) |
| SCR-P00-02 → -05 | Tenants, tenant editor, domains, branding | platform_admin | P00 | Tenancy | Mechanism matrix with disabled prohibited cells, contrast checker |
| SCR-P00-06 | Feature flags | platform_admin, legal_reviewer, registrar | P00 | Legal flags (DB) and release flags (Unleash) | Linked legal-rule status chips |
| SCR-P00-12 / -13 | Legal Rules Register | legal_reviewer, registrar, dpo, auditor | P00 | Rules as data | Status chips, next review |
| SCR-P00-14 / -15 / -16 | Audit explorer, chain verification, evidence ledger | platform_admin, dpo, auditor | P00 | NN-22 | Hash drawer, anchors with signature check |
| SCR-P00-17 / -18 | Events and webhook inbox | platform_admin, support_agent | P00 | Messaging backbone | DLQ replay |
| SCR-P00-19 / -20 / -21 | Provider routing, jobs, environment | platform_admin | P00 | Ops | Circuit state, Temporal links |
| SCR-P00-23 | System pages | all | P00 | 403/404/500/maintenance/forced update | ≤ 50 KB pages |
| SCR-P01-37 | JIT elevation | platform_admin | P01 | Time-boxed privileges | Countdown banner |
| SCR-P07-16 | DLT registry | platform_admin | P07 | PE IDs, CPaaS telemarketer links, headers, templates, tenant 1600-series authorisations, Equator A2P CLI range declarations, consent-platform registrations (NN-12/M-05) | Expiry alerts |
| SCR-P09-01 | Developer portal | developers | P09 | API reference, SDKs | OpenAPI viewer, sandbox keys |
| SCR-P09-19 | Connectors | platform_admin | P09 | Government/ecosystem connectors health | Last sync, errors |
| SCR-P11-01 → -08, -15 | AI governance console, prompts, models, evals, kill switches, incidents, red team, corpora, monitoring | quality_officer, platform_admin, auditor | P11 | AI governance (NN-01) | Gate status, signed eval reports |
| SCR-P13-16 | CMS editor (`/admin/cms/*`; v1 C ID SCR-P13-21) *(v3.1)* | CMS bundles, legal reviewer | P13 | Website content (physically separate data, NN-16/NN-17) | Claim nodes, citation panel, lint panel, review queue, preview by locale |
| SCR-P13-17 | Claims Register (`/admin/growth/claims`; v1 C ID SCR-P13-22) *(v3.1)* | claims owner, legal reviewer | P13 | Evidence-backed claims (NN-17) | Register list, evidence viewer, expiry calendar |
| SCR-P13-51 / -52 | SEO metadata / programmatic pages (tabs of SCR-P13-16; v1 C IDs SCR-P13-23 / -24) *(v3.1)* | CMS bundles | P13 | Titles, canonical, JSON-LD; programmatic page sets with thin-content guard | Tabs of the CMS editor |
| — | CRM leads and referral admin (v1 C IDs SCR-P13-25 / -26; P13-sense SCR-P13-18 growth mini-CRM) — **superseded** by the Operations Platform CRM (master X-51) and SCR-P17-23 *(v3.1)* | — | P16 / P17 | Not built in P13 | — |
| SCR-P14-02 → -09 | SLO, incidents, DSR (platform), RoPA/DPIA, launch readiness, migration, UAT, security findings | SRE, dpo, leads | P14 | Go-live operations | Burn-rate charts, checklists |

### B.17 Ruleset Studio (`/admin/studio`)

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P00-07 | Studio home | institution_admin, platform_admin, registrar | P00 | Config catalogue and queues | Kind list, pending CRs |
| SCR-P00-08 | Object detail and versions | same | P00 | History, compare | Version timeline, diff |
| SCR-P00-09 | Draft editor | maker | P00 | Edit draft | Structured editor, validation panel, effective-from |
| SCR-P00-10 | Change-request review | checker | P00 | Maker–checker (NN-21) | Diff, validation, preview, legal refs, step-up approve |
| SCR-P00-11 | Preview runner | maker, checker | P00 | Golden-fixture diff | Per-fixture output diff |
| SCR-P02-20 | Form schema editor | institution_admin | P02 | Intake forms | JSON + visual, web/mobile preview, locale check |
| SCR-P02-21 | Routing and signposting editor | institution_admin | P02 | Rule packs, forum directory | Test-fact runner, re-verification dates |
| SCR-P05-17 | Fee schedule editor | institution_admin, finance checker | P05 | Tariffs | Slab table, quote preview |
| SCR-P08-17 | Vertical rule-pack editor | institution_admin, registrar | P08 | Per-vertical packs (mandatory/prohibited terms, closure policy) | Guardrail report |
| SCR-P08-18 | Stamp-duty matrix editor | registrar | P08 | State × instrument duty formulas (NN-09) | Matrix with legal-rule refs |
| SCR-P10-33 | Document template editor | institution_admin, legal reviewer | P10 | Notices, MSA, awards, orders (clause library) | Merge-field palette, language variants, legal approval |

### B.18 Mobile apps (one Expo binary; role spaces per P12 FR-P12-01)

| ID | Screen | Space | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P01-M01 → M06 | Splash/update, welcome/language, sign-in, device binding, lock, push primer | all | P01 | Shell and auth | Biometric prompt, PIN pad |
| SCR-P01-M08 | Low-bandwidth notice view | party | P01 | Notice link in app | Text-first card |
| SCR-P12-01 | Welcome (parity release) | all | P12 | Language and login | Native-script language list |
| SCR-P12-04 | Party home | party | P12 | Active matters, next actions, deadlines | Case cards with clock text |
| SCR-P12-05 | Case hub | party, counsel | P12 | Timeline, documents, messages, payments, sign | Tabs, sealed watermark |
| SCR-P12-06 | Notice reader | party | P12 | Read, listen (TTS), acknowledge | Read-aloud, language switch |
| SCR-P12-07 | File/respond (form engine) | party | P12 | Offline-capable forms | Stepper, autosave indicator |
| SCR-P12-08 / -09 | Capture / upload queue | all | P12 | Camera capture, resumable uploads | Edge overlay, masking prompt, progress |
| SCR-P12-10 / -11 | Hearing pre-check / room | party, neutral | P12 | Join sessions | Audio-first layout, PSTN fallback |
| SCR-P12-12 | Sign | signatories | P12 | Pre-sign summary → provider | Hash prefix, biometric step-up |
| SCR-P12-13 | Pay | party, enterprise | P12 | UPI intent first | Payment status polling |
| SCR-P12-14 | Case chat | party, neutral | P12 | On-platform messaging | Thread kinds, voice notes |
| SCR-P12-15 → -17 | Neutral today, appointment offer, availability | neutral | P12 | Daily agenda | Disclosure-before-accept |
| SCR-P12-18 → -20 | GRO queue, ticket, insights | enterprise-lite | P12 | Grievance handling | Regulator ClockPill, templates |
| SCR-P12-21 | Privacy settings | all | P12 | Notices, consents, DSR, delete account | PurposeToggle |
| Party M01–M09, Neutral N01–N04 | Phase mobile variants of SCR-P02-04/-07/-13/-16, SCR-P04-02/-03/-08/-11/-13/-14 | party, neutral | P02, P04 | Mobile variants listed in those phases | — |

### B.19 v3 portals — Operations Platform (`ops`), auditor workspace (`assurance`) and v3.1 screen changes *(v3.1)*

The `ops` and `assurance` portals (Appendix S §2.0 rows `ops`, `assurance`; Appendix AG §AG.1.1, §AG.2.8, §AG.2.11) are catalogued in the §6 tables of P15–P21 and placed in menus by Appendix AG; this table records their entry screens and the v3.1 screen changes reported by the owner files.

| ID | Screen | Persona | Phase | Purpose | Key widgets |
|---|---|---|---|---|---|
| SCR-P16-01 | Operations Platform home (`ops.equatorresolution.in/`; client `eq-portal-ops`, aal2-pr) | all `ops` workforce roles | P16 | My work: tasks, tickets, approvals; department switcher | Work Inbox tray (AG-SCR-01), department rail (AG.2.8) |
| SCR-P21-AE09 (alias SCR-AE-09) | Assurance workspace (`assurance.equatorresolution.in`; client `eq-portal-assurance`, aal2-pr passkey) | `internal_auditor`, `auditor` (engagement grant) | P21 | Engagement-scoped evidence, PBC requests, findings (Appendix AE §AE.8.3) | Watermark on every page, grant expiry countdown (AG.2.11) |
| SCR-P19-07 | Marketplace engagement proposal — *v3.1:* Ready-to-pay checklist R1–R7 with who must act; slot-hold time shown as a plain time, never a countdown (Appendix AA §AA.6.6) | buyer, counterparty | P19 | Confirm and pay | Checklist, fee disclosure, unticked confirmation |
| SCR-P19-10 | Provider application (`/provider/apply`) — *v3.1:* progress score, next best action, blocking items, estimated listing date (AA §AA.4.7) | applicant | P19 | Apply and track | Progress tracker, NBA card |
| SCR-P19-19 | Ops: provider onboarding pipeline (new in v3.1) | `provider_verifier`, `marketplace_moderator`, `marketplace_manager` | P19 | Deadline-aware queue by SLA due, then progress score; amber at 80% SLA; bulk assign and request-for-information (never bulk credential approval) | Queue (PAT-04), bulk bar (PAT-03), drop-off by step |
| SCR-P19-AB09 | Revenue viability dashboard — *v3.1:* exception-first RAG (red → amber → grey → green), stop/go proposals that never self-execute (Appendix AB §AB.7.4) | `finance_controller`, revenue owners | P19 | Stream viability and decisions | RAG rows, sparkline, proposals in the Work Inbox |
| SCR-P21-AE02 (alias SCR-AE-02) | Change calendar and CAB queue — *v3.1:* standard-change entry proposals and the daily standard-train approval (one two-person approval per train; Appendix AE §AE.4.2) | CAB, `release_manager` | P21 | Change governance | Train approval panel (also a Work Inbox source) |
| SCR-P21-AE06 (alias SCR-AE-06) | Backup and DR — *v3.1:* restore-test coverage with missed tests counted as failures, RTO headroom and the Restore Assurance Report (Appendix AE §AE.6.5) | `sre`, `security_lead` | P21 | Backup and restore assurance | Coverage grid, headroom chart, report download |

**Screen count:** 374 catalogued IDs in §B.1–§B.18 (P00 23, P01 54, P02 23, P03 25, P04 22, P05 32, P06 19, P07 19, P08 18, P09 20, P10 33, P11 16, P12 19, P13 40, P14 11) plus phase-defined mobile variants (P02 M01–M04, P04 M05–M09 and N01–N04). *(v3.1: v1 count 350; P13 31 → 40 after the AG §AG.2.1 renumbering — superseded v1 C IDs SCR-P13-25/-26 and the P13-sense SCR-P13-18 are not counted; P05 18 → 32 with SCR-P05-19…34 replacing SCR-P05-11/-12; P02 22 → 23 with SCR-P02-33. §B.19 entries and the v3 phase screens P15–P21 are counted in their phases.)*

## C. Navigation maps — superseded by Appendix AG *(v3.1)*

**Owner.** From v3.1, Appendix AG owns navigation: shells, menus, tab bars, the context switcher, deep links, back-navigation, the Work Inbox, search, the command palette, dashboard composition and the workflow patterns (AG.0.3 rule 3). Every menu, tab, palette command and settings-rail entry is a `cfg.nav_items` row resolved per request (D3-45); menus never grant access (AG.1.4 rule R-8). The v1 lists formerly in this section (top navigation "Resolve · Solutions · Neutrals · Academy · Rules & Fees · Resources · About", per-portal side navigation and mobile tabs "Home · Cases · Messages · Payments · Profile") are withdrawn and must not be built (AG.0.5 #8, #9). This section keeps only the pointers below.

### C.1 Web global frame

- **Public site header and footer:** the v3.1 mega-menu of AG.2.1 (Resolve · Disputes · Neutrals · Marketplace · For organisations · Chambers · Training · Resources · About · Help; utility bar with "Understand your options", Respond to a notice, Track, Language and Log in); it keeps every FR-P13-03 destination (FR-P13-V31-AG01). The footer keeps the Appendix P §3.0 link groups and the legal-entity block (entity name, CIN and registered office from `tenant.legal_entity`, master X-15); Grievance Officer, DPO, accessibility and legal links are locked (L).
- **Authenticated shells:** anatomy of AG.1.2 (skip links, context chip and switcher AG-SCR-05 extending SCR-P01-38, header search AG-SCR-04, Work Inbox tray AG-SCR-01 — which replaces the SCR-P07-17 list UI — help AG-SCR-12, me menu, QuickExit slot per §F.5, breadcrumbs from registered route parents) built once in `packages/shell` (FR-P00-V31-AG01).

### C.2 Side navigation per portal

| v1 portal (this appendix §B) | v3.1 shell (AG.1.1) | Menu tree | Home screen |
|---|---|---|---|
| Party (§B.3) | `party` (`/app`) | AG.2.2 | SCR-S-D01 |
| Counsel (§B.4) | `representative` (`/app/counsel`) | AG.2.3 | SCR-S-D02 |
| Neutral (§B.5) | `neutral` (`/app/neutral`, mediation and arbitration spaces) | AG.2.4 | SCR-S-D03 / SCR-S-D04 |
| Case manager, registrar, panel, quality, escrow, safeguarding (§B.6, §B.7) | `console` (`console.equatorresolution.in`) | AG.2.7 | SCR-S-D05 / SCR-S-D06 |
| Enterprise, GRM desk, POSH IC sealed sub-shell (§B.8–§B.10) | `enterprise` (`/app/enterprise`, `/app/grm`, `/app/posh`) | AG.2.6 | SCR-S-D08 / SCR-S-D09 / SCR-P09-17 list |
| Chambers admin (§B.11) | `chambers` (`/chambers/work`) | AG.2.5 | SCR-P20-29 |
| Academy, Campus (§B.12, §B.13) | `academy` / `campus` | AG.1.1 (menus in P10) | SCR-P10-10 / SCR-P10-19 |
| Partner (§B.14) | `partners` (`/partners`) | AG.2.12 | SCR-S-D11 |
| Committee | `committee` (`/committee`) | AG.2.12 | SCR-S-D07 |
| Institution admin (§B.15) | `admin` (tenant scope) | AG.2.7 "Institution administration" | SCR-P10-32 |
| Platform admin, Ruleset Studio (§B.16, §B.17) | `admin` (`admin.equatorresolution.in`) | AG.2.10 | SCR-S-D12 |
| Operations Platform, employee self-service (§B.19) | `ops`, `selfservice` (`ops.equatorresolution.in`, `/me`) | AG.2.8, AG.2.9 | SCR-P16-01 |
| Auditor workspace (§B.19) | `assurance` (`assurance.equatorresolution.in`) | AG.2.11 | SCR-P21-AE09 |

Settings menus follow AG.3 (one settings shell with scoped sections aligned to Appendix V).

### C.3 Mobile bottom tabs (P12 governs implementation)

Tab bars per persona are those of AG.2.13 (at most five slots; slot 5 is **More**; party tabs Home · Cases · Inbox · Pay · More, with Messages moved into the Inbox and the case hub) and are implemented by FR-P12-V31-AG01. Unchanged rules: switching space clears the previous space's in-memory cache; IC roles receive content-free notifications only and the sealed POSH workspace is web-only; no neutral selection on any enterprise tab (NN-03).

## D. Persona dashboards (widgets)

Widgets are configurable through the `dashboard_pack` config kind within these defaults; sealed data never appears in any widget outside the sealed workspace. *(v3.1)* These remain the widget defaults; Appendix AG §AG.6 extends them with the widget catalogue (`cfg.widget_catalogue`), default layouts per role (mandatory widgets cannot be hidden), personalisation rules and next-best-action rules, and v3 personas (Operations Platform, HR self-service, chambers v3, auditor) take their defaults from AG.6.2.

| Persona | Default widgets |
|---|---|
| Party | Next action card (with due date and days left); my cases (status chip + ClockPill); upcoming sessions; payments due; documents requested; messages; signposting reminders (free forum + last date); help and assisted-mode request |
| Counsel | Matters by client; filings due (7/14/30 days); hearings this week; mandate expiries; offers awaiting client decision |
| Mediator / conciliator | Today's sessions with join; pending agreements to mediate; settlement drafts; clocks amber/red; feedback summary; payouts pending |
| Arbitrator | Caseload; s.29A clocks amber/red; drafting queue; hearings; disclosure renewals due; fees and payouts |
| Expert | Determinations due; site visits; submissions received |
| Case manager | **Exceptions first** *(v3.1)*: breached and escalated clocks, service exceptions, recalled notices, cases on hold past review; then queue by stage; scrutiny SLA; clocks owned by me; hearings needing logistics; handoffs; deficiency expiries; items covered for an away colleague |
| Registrar | **Exceptions first** *(v3.1)*: pool exhausted, offers expiring within 4 h, Amber/Red Defensibility, reopen requests (A C51), s.38 recall windows; then appointments pending; challenges and their timeliness; certified-copy requests; challenge windows; unowned clocks (blocks closure) |
| Panel manager | Applications by stage; panel shortages by language/city/vertical; concentration-cap alerts; CPD non-compliance |
| Escrow officer | Milestones awaiting evidence; releases pending dual control; reconciliation breaks |
| Safeguarding lead | Screenings due before joint sessions; safety flags raised; vulnerable callbacks |
| Quality officer | Award scrutiny queue; publication queue; voice QA critical failures; AI eval gate status; complaint rate |
| Institution admin | Panel health; allocation runs (counts); fee and revenue (₹); clock-risk table; verticals MIS; SLA breaches |
| Chambers admin | Caseload; revenue (₹); subscription status; referral inflow; clock risk |
| Enterprise admin / operator | Volumes FY; settled pre-arbitration %; Defensibility distribution (FIN); SLA heatmap; clause coverage; last bulk batch; compliance (instalments on track/overdue); ROI (FIN) |
| GRO / internal ombudsman | Tickets by regulator clock state (T-7, T-3, breached); escalations; resolution rate; ageing; IO referrals |
| IC presiding officer / member (sealed) | Complaints by stage; 90-day inquiry clocks; report due (10 days); employer action due (60 days); constitution validity |
| University admin / SGRC member | Grievances (SGRC 15 working days / appeal 15 days / Ombudsperson 30 days clocks); Ombudsperson appeals; cell activity; partner programme KPIs |
| Student | My grievances; campus cell referrals; competitions; courses |
| Learner / trainer | Learner: courses, attendance gate %, assessments due, certificates, CPD. Trainer: sessions, attendance to certify, grading due, payouts |
| Partner | Referrals by status; conversion; statements (non-professional partners only — no credits, X-62); clause adoptions |
| Platform admin | Availability; outbox lag; chain verification; incidents; tenants provisioning; flags pending; provider circuits |
| DPO | DSR SLA; withdrawal propagation breaches; break-glass events; breach incidents (72-hour timer); notices pending approval |
| Support agent | Verification queue; handoffs; inbox failures |
| Auditor | Scoped audit search; verification reports; evidence ledger; grant expiry |

## E. Design system summary (`packages/design-tokens`, `packages/ui`, `packages/ui-native`)

### E.1 Colour tokens (light theme; dark mode is a later token swap)

| Token | Value | Use and contrast rule |
|---|---|---|
| `brand.navy` | `#0B2E4F` | Headers, primary text on light backgrounds, primary buttons (white text ≥ 12:1) |
| `brand.teal` | `#1F7A8C` | Links, secondary actions, focus ring (≈ 5.0:1 on white) |
| `brand.gold` | `#B98A2E` | Decorative accents and large display text only (≈ 3.1:1; never body text) |
| `ink` | `#1A1A1A` | Body text |
| `muted` | `#5A6B7B` | Secondary text (≈ 5.5:1 on white) |
| `border.subtle` | `#C9D3DC` | Dividers only (decorative) |
| `border.input` | `#7A8A99` | Input and control boundaries (≈ 3.5:1, meets WCAG 1.4.11) |
| `surface` / `surface.alt` | `#FFFFFF` / `#EAF1F6` | Page / panels |
| `clock.green` | `#2E7D5B` | Clock and success icon/border (≈ 5.0:1 on white) |
| `clock.green.text` / `.bg` | `#23624A` / `#E8F3EE` | ClockPill text on tint (≈ 6.3:1) |
| `clock.amber` | `#B9822E` | Clock and warning icon/border (≈ 3.3:1; non-text only) |
| `clock.amber.text` / `.bg` | `#6E4C14` / `#FBF3E6` | ClockPill text on tint (≈ 7.0:1) |
| `clock.red` | `#8A2E4F` | Clock and danger icon/border/text (≈ 8:1 on white) |
| `clock.red.text` / `.bg` | `#8A2E4F` / `#F7E9EE` | ClockPill text on tint (≈ 6.9:1) |
| `success` / `warning` / `danger` | alias `clock.green` / `clock.amber` / `clock.red` | Semantic states; locked (tenants cannot override) |
| `sealed` | `#4B2E83` on `#EFEAF7` | SealedBanner (contrast 8.8:1, passes WCAG AAA) |
| `focus.ring` | `#1F7A8C`, 2 px solid, 2 px offset | Every focusable element; never removed |

Tenant branding may override only `brand.*` tokens and must pass the contrast checker (P00 FR-P00-33). Colour is never the only carrier of meaning: every ClockPill carries text ("12 days left") and an icon.

### E.2 Typography

- Families: Inter (Latin); Noto Sans Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu; Noto Nastaliq Urdu (RTL); mono `JetBrains Mono, Menlo, Consolas, monospace` for case numbers, hashes and amounts in tables. Self-hosted, subset per locale, `font-display: swap`.
- Scale (px): display 32, h1 24, h2 19, h3 16, body 15 (Latin) / 16 (Indic scripts), small 13, caption 12 (never for legal text). Weights 400/600/700. Line height 1.45 Latin, 1.6 Indic scripts (matras and conjuncts). Line length ≤ 80 characters. Legal text never truncated; scales to 200%.
- Numbers: Indian grouping (`₹1,00,000`); dates `12 Nov 2026` (en) with locale equivalents; times with zone where parties differ ("10:30 IST / 09:00 GST").

### E.3 Spacing, layout and motion

4-pt grid: 4, 8, 12, 16, 24, 32, 48, 64. Radius 4 (inputs), 8 (cards), 12 (modals), 999 (pills). Elevation 1 `0 1px 3px rgba(11,46,79,.08)`, 2 `0 8px 24px rgba(11,46,79,.16)`. Breakpoints: min supported 360, sm 640, md 768, lg 1024, xl 1280. z-index: dropdown 100, sticky 200, modal 1000, toast 1100, QuickExit 1200. Motion 150–250 ms ease-out; `prefers-reduced-motion` → no motion. Icons: Lucide, 1.5 px stroke, always labelled or `aria-hidden`.

### E.4 Component inventory

- **Actions:** Button (primary, secondary, ghost, danger), IconButton, Link, Menu, QuickExit.
- **Inputs:** TextField, TextArea, Select, MultiSelect, Combobox, Checkbox, Radio, Switch, DatePicker, TimePicker (zone-aware), FileUpload (scan status, hash chip), MoneyInput (minor units, currency), PhoneInput (E.164, +91 default), OTPInput, ConsentCheckbox, PurposeToggle, AddressInput (PIN lookup), AuthorityMatrix.
- **Data display:** Table (cursor pagination, column chooser), DataList, Card, StatCard, Badge/Chip, Tag, Avatar, Timeline, KeyValue, CaseNumber (mono, copy, QR), MaskedValue (reveal with audit), VerifyBadge, EStampBadge.
- **Feedback:** Toast, InlineAlert, Banner, EmptyState, Skeleton, ProgressBar, ClockPill, SealedBanner, AiDraftBanner ("Drafted by AI — requires human review"; NN-01), AssistedModeBanner, OfflineBanner, ErrorSummary.
- **Navigation:** TopBar, SideNav, BottomTabs (native), Tabs, Breadcrumbs, Pagination, Stepper, RoleSwitcher, LanguageSwitcher.
- **Overlays:** Modal, Drawer, Popover, Tooltip, ConfirmDialog, StepUpDialog.
- **Domain:** CaseStatusTimeline, HearingCard, EvidenceItem, ESignPanel, PaymentSummary, QuoteBreakdown, DisputeExplorerChat, NeutralCard, DefensibilityGauge, OfferCard, BlindBidInput, SignpostCard, DocumentViewer (watermark, page sync), BundleIndex.

### E.5 Component states

default · hover · focus-visible (2 px teal ring) · active · disabled (`aria-disabled`, reason tooltip) · loading (announced via live region) · error (`aria-describedby` message + ErrorSummary) · selected · read-only · redacted/sealed (placeholder text "Not visible to you", never blank) · offline/queued (clock icon + "Will send when online") · stale (data older than refresh interval, with refresh action).

## F. UX principles

1. **Plain language and honesty.** Reading level ≤ class 8 in English and Hindi; short sentences; legal terms from the glossary only, with a one-line explanation on first use. Equator is never described as a court, regulator or government body; never use "court", "decree" or "judge" for Equator. Say who decides at each step. Deadlines always show the absolute date and days left. Free and statutory forums are named where more appropriate (NN-20). No copy predicts outcomes, rates a case or values a claim (NN-01).
2. **Vernacular first.** UI language and notice language are chosen separately; every notice and document view offers read-aloud and a language switch; bilingual documents place the vernacular text alongside English; machine-translated text is labelled "Translation for convenience" unless legal-approved (NN-23). Urdu renders RTL with mirrored layouts.
3. **Low bandwidth.** Budgets: public and auth pages ≤ 150 KB first load, notice-link page ≤ 50 KB and usable without JavaScript, LCP < 2.5 s on 4G and < 5 s on 3G; text-first lists; images lazy and off in low-bandwidth mode; resumable uploads; offline drafts on mobile; SMS/WhatsApp/IVR fallbacks for every critical step (notice, slot booking, payment link, status).
4. **Assisted mode.** A case manager, field agent or kiosk operator may complete forms for a person who asks; each submission requires that person's OTP confirmation on their own number (or recorded IVR consent), the AssistedModeBanner is shown, the operator ID is recorded on consent and audit records, and kiosk sessions auto-clear after 2 minutes idle. Assisted mode is never used to capture marketing consent.
5. **Quick exit and safety.** On FAM, WRK-POSH, safety-flagged and sealed screens a QuickExit button (top-right, and pressing `Esc` twice) immediately replaces the page with a neutral external page, clears session storage and replaces the history entry; on mobile it backgrounds the app and clears the clipboard. Notification text for these matters is neutral ("You have an update from Equator"); no sensitive content in SMS, email subject lines or push previews.
6. **Accessibility: WCAG 2.2 AA floor.** Including the 2.2 additions: 2.4.11 Focus Not Obscured (sticky headers never cover focus), 2.5.7 Dragging Movements (every drag — bundle ordering, family tree, journey designer, channel order — has a button/keyboard alternative), 2.5.8 Target Size (≥ 24×24 CSS px; we use 44×44 on touch), 3.2.6 Consistent Help (help link in the same place on every screen), 3.3.7 Redundant Entry (previously entered data is pre-filled), 3.3.8 Accessible Authentication (OTP paste/autofill allowed, passkeys supported, no cognitive puzzles; CAPTCHA has an audio alternative). Screen-reader scripts for file, respond, pay, sign and join-hearing journeys; captions in hearings; sign-language interpreter on request.
7. **Neutrality in the interface.** No win-rates, "lender-friendly" tags or outcome rankings for neutrals; directory order is seeded-random within filters; enterprise screens never offer neutral selection; paid relationships are disclosed to counterparties (NN-03, NN-16).
8. **Show the trust evidence.** Hash, timestamp, e-stamp and signature badges are visible on every outcome document; every AI-drafted element shows the AiDraftBanner until a human accepts it.
9. **Calm errors.** Errors say what happened, what the user can do, and give the support reference (`traceId`); never blame the user; preserve entered data.
10. **Queues are deadline-ordered and exception-first.** *(v3.1)* Every work queue (scrutiny, clocks, notices, appointments, verification, escrow, handoffs, GRM inbox, approvals) opens on an exception view (breached → escalated → due soon) sorted by the nearest legal or statutory date, then SLA remaining, then age; "all items" is a secondary tab. The canonical order key is Appendix AG §AG.4.4 (`legal_blocking DESC, sla_state_rank DESC, due_at ASC NULLS LAST, priority ASC, created_at ASC`) and every queue is built on pattern PAT-04 (atomic "Next", SLA pauses only with a reason from the fixed list and never for statutory clocks). Saved views, columns and filters follow AG §AG.5.6 (server-side `core.saved_views` / `ops.ws_saved_views` with sharing scope `me`, `team`, `department`, `tenant` or `company`; the viewer's permissions are re-applied at render; a user's view never changes another user's default) — this replaces the v3.1-draft "browser storage only" rule *(v3.1, aligned to AG)*. Acceptance: `UX-Q-01` — with seeded items, the first row is always the item with the earliest statutory `due_at`.
11. **Next-best-action card.** *(v3.1)* Case, ticket and appointment pages show at most one primary "next action" card computed by the rules engine (never AI-decided; NN-01): the action, why it is next (rule reference), who must act, and the due date; secondary actions sit in an overflow menu. A blocked action shows the blocking guard in plain language with a link to the fixing task (e.g., closure guards, P06 SCR-P06-17). Suggestions come from the deterministic `cfg.nba_rules` of Appendix AG §AG.6.4; the object page shows one primary card, while a dashboard "next best action" panel (widget `W-NBA`) shows at most three suggestions ordered by priority then due date *(v3.1, aligned to AG)*.
12. **Bulk actions.** *(v3.1)* Allowed for assignment, reminders, tagging, exports (subject to export controls) and non-legal status changes; each bulk action shows a preview (count and first 10 items), runs idempotently per item, and reports per-item results with retry for failures. Never available for decisions with legal effect: scrutiny accept/reject, deficiency waivers, award or settlement approval, escrow release, appointment confirmation, concessions above auto-approval, or any maker–checker approval (each needs an individual review and step-up). Bulk actions use pattern PAT-03 (dry-run preview with exclusions and reasons, job monitor AG-SCR-19, per-row result file, undo window 10 minutes, T 5–30, for reversible actions only; 5,000 rows per job, staff up to 20,000) *(v3.1, aligned to AG)*.
13. **Undo and irreversible steps.** *(v3.1)* Reversible, low-risk actions (archive a message, dismiss an informational alert, reorder, tag) take effect immediately with a 10-second Undo toast. Irreversible or legally effective actions (sign, serve a notice, confirm an appointment, release escrow, issue a certified copy, close a case, withdraw a claim, publish) use a confirmation **screen** (pattern PAT-16; not a checkbox in a modal) that states the consequence in one sentence — what will happen, to whom, and that it cannot be undone — repeats the context line (acting role and company), shows what will be sent or changed (preview or diff), requires step-up where the phase says so, and for destructive deletes and mass sends requires typing the object's reference (for a case, the case number); no "Are you sure?" dialog without a consequence statement. The irreversible-action list of PAT-16 is locked (L); reversible actions also appear in the AG-SCR-27 "Recent actions" tray while their window is open *(v3.1, aligned to AG)*.
14. **Inline edit and conflicts.** *(v3.1)* Inline edits use optimistic concurrency (`If-Match` ETags); on a 412 conflict the screen shows both values side by side and lets the user keep theirs, take the server value or merge field by field; autosaved drafts are never silently overwritten.
15. **Delegation visibility.** *(v3.1)* When a task, review or clock owner is away (leave or away flag), the item shows "Covered by <delegate> until <date>" and the delegate's queue labels it; the away person sees the items on return with a summary of what changed. Away status and inbox or approval delegation are set in AG-SCR-06 within the Appendix S §6.4 limits (≤ 90 days, depth 1, delegate must hold the permission and an equal or higher authority limit; Appendix AG §AG.4.5) *(v3.1, aligned to AG)*.

## G. Case-status tracker specification

### G.1 Views

| View | Who | Access | Shows | Never shows |
|---|---|---|---|---|
| Public (SCR-P02-17, `/track`) | Anyone with the case number or filing reference | CAPTCHA + OTP to a contact point already on the case; 30-minute view (P02 FR-P02-44) | Plain-language stage, next scheduled date, last updated, mechanism, public-safe events | Party names beyond initials, amounts, documents, allegations, arbitrator identity (A&C Act s.42A confidentiality), anything sealed/high tier |
| Restricted matters | Same | Same | "Status available to parties in their account" | Anything else — applies to tier `sealed`, every FAM case, INS health cases, any POSH-linked matter |
| Party (workspace SCR-P02-16, mobile SCR-P12-05) | Parties and counsel within mandate | Authenticated | Full timeline, orders, documents, clocks, payments, outcome | Other side's private uploads, caucus notes, screening and vulnerability data |
| Institution (SCR-P02-11, SCR-P14-01) | Case managers, registrar | Staff | Portfolio, clock board, SLA | Sealed content outside the sealed workspace |
| Auditor / regulator | Scoped read-only grant | Time-bound | Specified records, immutable | Out-of-scope cases |
| QR verification (SCR-P06-12) | Anyone with the document | Code on document | Document authenticity and status | Case content |
| Messaging and IVR | Registered numbers only | SMS/WhatsApp keyword `STATUS <case number>`; IVR with OTP | Stage and next date in the user's notice language | As public view |

### G.2 Status vocabulary (case-level machine, master §5.1)

| State | Public label (en) | Public label (hi) [legal translator review] | Shown publicly |
|---|---|---|---|
| `draft` | — | — | No |
| `filed` | Filed — awaiting review | दायर — समीक्षा की प्रतीक्षा | Yes |
| `under_scrutiny` | Under review by the case team | केस टीम द्वारा समीक्षा जारी | Yes |
| `deficient` | Information requested from the filing party | दायर करने वाले पक्ष से जानकारी माँगी गई | Yes |
| `accepted` | Accepted — other party being notified | स्वीकार — दूसरे पक्ष को सूचना दी जा रही है | Yes |
| `signposted` | Directed to a more suitable forum | अधिक उपयुक्त मंच की ओर निर्देशित | Yes |
| `rejected` | Not accepted | स्वीकार नहीं किया गया | Yes |
| `awaiting_respondent` | Awaiting response | उत्तर की प्रतीक्षा | Yes |
| `neutral_appointment` | Neutral being appointed | तटस्थ की नियुक्ति प्रक्रिया में | Yes |
| `in_proceedings` | In progress | प्रक्रिया जारी | Yes |
| `outcome_drafted` | Outcome being finalised | परिणाम को अंतिम रूप दिया जा रहा है | Yes |
| `outcome_executed` | Outcome signed and stamped | परिणाम हस्ताक्षरित और स्टाम्प किया गया | Yes |
| `in_compliance` | Agreed terms being carried out | सहमत शर्तों का पालन जारी | Yes |
| `closed` | Closed | बंद | Yes |
| `on_hold` | On hold | रुका हुआ | Yes (reason never public) |
| `withdrawn` | Withdrawn | वापस लिया गया | Yes |
| `lapsed` | Process ended without an outcome | प्रक्रिया बिना परिणाम समाप्त | Yes |
| `challenged` | Outcome under challenge before a court | परिणाम को न्यायालय में चुनौती दी गई है | Yes |
| `in_execution` | Enforcement steps under way | प्रवर्तन की कार्रवाई जारी | Yes |

The label set is configuration (`dashboard_pack.status_labels`, legal approval required); the state set is code.

### G.3 Layout and behaviour

1. **Status card:** CaseNumber (mono, copy), current stage label, "Last updated" (absolute date/time IST and the viewer's zone), next scheduled date (if any), mechanism (e.g., "Mediation").
2. **CaseStatusTimeline:** ordered public-safe events (filed, accepted, notice served, neutral appointed, session scheduled, outcome issued, closed) with dates; future steps shown greyed with expected sequence for the mechanism; stage chips use `clock.*` tokens only for clocks, not for stages.
3. **ClockPills (party view only):** each statutory clock shows name, "N days left — <state>" and owner; state (green/amber/red) is computed server-side by the clocks service from the clock definition's alert thresholds (NN-04: info T-90, blocking T-60, escalation T-30 by default); the UI never computes clock state. Expired clocks show "Expired on DD MMM YYYY" in red with the remaining options link.
4. **Actions:** "Sign in for full details" (party), "Get updates" (WhatsApp/SMS opt-in for case contacts only), "Read in another language", "Download status (PDF)" for parties.
5. **Anti-enumeration and limits:** identical responses whether or not a case exists; 5 lookups/hour/IP; 3 OTPs/hour/case; CAPTCHA with audio alternative; tracker OTP successes are audited.
6. **Performance:** text-first page ≤ 60 KB; works on 2G; PWA-cacheable shell; no third-party scripts.
7. **APIs (P02):** `POST /track/lookup`, `POST /track/verify-otp`, `GET /track/status`; party view from `GET /v1/cases/{caseId}/status` (CQRS read model).
8. **Accessibility:** timeline is an ordered list with dates in text; current step marked with `aria-current="step"`; status changes announced politely.

## H. Open items

1. **P01 mobile tab placeholders** — resolved by master X-03: P12 governs mobile navigation; the P01 placeholders are superseded. *(v3.1)* Tab composition is now Appendix AG §AG.2.13 (party: Home · Cases · Inbox · Pay · More).
2. **ID allocation:** P08 (SCR-P08-01…18) and P10 (SCR-P10-01…33, including counsel, case-manager and institution dashboards consolidated there) IDs are allocated here; those phase writers must adopt them or update this appendix. *(v3.1)* P13 IDs are no longer allocated here: P13 §6 and the Appendix AG §AG.2.1 renumbering map govern (item 6). The P10 phase §6 table currently numbers its screens differently from §B.11–§B.13 (e.g., P10 SCR-P10-03 = branding, here = chambers dashboard); Appendix AG §AG.2.1 uses this appendix's P10 numbering — reconciliation is open for the P10 owner (see §A.1 CI rule).
3. **Header context** — resolved by master X-01: `Equator-Context` (tenant + acting role + acting case, signed by the gateway; P01 FR-P01-02); P12 references to `X-Tenant-Id` are superseded.
4. **Hindi status labels** and glossary terms require qualified legal-translator review before `legal_approved` (NN-23).
5. **`sealed` token colour** contrast is confirmed (8.8:1; all §E.1 ratios recomputed 24 Oct 2026 and correct). QuickExit destination resolved by master X-25: configurable external neutral page (`explorer.quick_exit_url`, default google.co.in); usability testing with family-law and POSH practitioners confirms only the copy and placement.
6. **P13 screen-ID reconciliation** *(v3.1)*. Resolved by Appendix AG (D3-47(c), AG.0.5 #1): P13 §6 IDs SCR-P13-01…19 prevail and this appendix's v1 IDs are renumbered in place in §B.1, §B.14 and §B.16 per the AG §AG.2.1 renumbering map (each row keeps its v1 C ID in brackets; v1 C-25/-26 superseded by X-51 and SCR-P17-23). This replaces the earlier v3.1-draft mapping in this item. Reserved and alias IDs are listed in §A.1.
