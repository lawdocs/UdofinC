# Appendix P — Website Copy, Health-Check Question Bank, Glossary Priorities, Tutorial and Video Plan, SEO/GEO System

> Binding for P23 (and for P20/P21 where they render public copy). Prepared 25 October 2026. Every number, customer name, certification and regulatory statement in this copy deck must be bound to an approved Claims Register entry before publication (NN-19). Where a statement depends on a regulatory fact, the citation is given and must be re-verified at publication ([VERIFY]). Placeholders in `{{double braces}}` are filled from platform registries, never typed by hand.


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §P.7 copy deck for global, market and v1.1 module pages; §P.8 global health-check question bank (20 questions); §P.9 tutorials T-45–T-62 (agents, MCP, global entities, legal matters, ESG/BRSR, AI governance, reports, access transparency); §P.10 SEO/GEO clusters, structured data and AI-answer prompts for global and new modules.

---

## P.1 Voice, style and claim rules

1. **Audience first.** Lead with who the page is for and the job they need done ("For compliance officers of Middle Layer NBFCs…"), then the outcome, then the feature.
2. **Plain Indian English.** Short sentences; active voice; define every acronym on first use and link the "i" glossary term; reading grade ≤ 9 for help and health-check text, ≤ 12 for solution pages.
3. **Exact, cited regulation.** Name the instrument and paragraph when referring to a requirement (e.g., "Companies Act, 2013, s.173(1)"); never paraphrase an obligation more strongly or weakly than the source; show "Last reviewed {{date}}".
4. **No overclaiming.** Never: "RBI-approved", "100% compliant", "guaranteed", "certified" (until held), "audit-ready" as a promise, "AI lawyer", "connected to CIMS/DAKSH/PRAVAAH". Prefer: "helps you prepare", "tracks", "reminds", "prepares upload-ready files for you to submit".
5. **Respect professional rules.** No testimonials or success claims about advocates; professional bios use permitted fields only (BCI r.36); marketplace copy describes services, not "best lawyer" rankings.
6. **Inclusive and accessible language.** "Persons with disabilities"; link text that makes sense out of context ("Read the Fair Practices Code guide", not "click here"); no instructions that rely on sensory characteristics ("the green button") — use names.
7. **Disclaimers placed where decisions happen** — health check, regulatory updates, savings estimates, AI drafts — not hidden in the footer only.
8. **Consistency with the product.** Module names, plan names, counts and integration names come from registries (`{{module.name}}`, `{{library.count.obligations[family]}}`).

---

## P.2 Copy deck

### P.2.1 Home (`/`)

**Meta title:** Compliance, Risk & Governance Software for Indian Regulated Entities | LawDocsComply
**Meta description:** Track every RBI, SEBI, IFSCA, IRDAI and Companies Act obligation with owners, evidence and maker-checker approval. Free compliance health check and 7-day trial.

**Hero**
- Eyebrow: Governance · Risk · Compliance for India's regulated entities
- H1: Know what applies to you. Prove you did it. Stay ahead of every change.
- Sub: LawDocsComply turns RBI, SEBI, IFSCA, IRDAI, co-operative, Companies Act, labour and data-protection requirements into clear tasks with owners, due dates and evidence — reviewed by a checker, reported to your board.
- Primary CTA: Take the free compliance health check (10 minutes)
- Secondary CTA: Start your 7-day free trial
- Trust line (claims-bound): `{{library.count.instruments}}` instruments and `{{library.count.obligations}}` obligations mapped · Hosted in India · `{{claims.security_posture_short}}`

**"Who it's for" tiles** (each links to its solution page and a preset health check): NBFCs · Banks & SFBs · Urban & rural co-operative banks · Credit co-operative societies · Other co-operative societies · Asset reconstruction companies · Listed companies · Mutual funds, AIFs, REITs & InvITs · Market intermediaries · IFSCA (GIFT City) entities · Insurers & insurance intermediaries · Companies & LLPs

**How it works (3 steps)**
1. *Tell us who you are.* Enter your PAN or CIN; we fetch your registered details and suggest the instruments that apply to your entity type, layer and size.
2. *Assign and evidence.* Every obligation becomes a task for a maker, reviewed by a checker, with the evidence stored and hashed.
3. *Report and stay current.* Board-ready reports in one click; a daily 8 PM scan of regulator updates shows what changed, what it replaces and what you need to do.

**Module band** (`{{modules[]}}` cards with one-line value): Compliance Workspace — "Every obligation, owner, due date and proof in one register." · Regulatory Change — "See what changed from the previous direction, side by side." · Governance & Secretarial — "Board and committee meetings, agendas, minutes and registers aligned with SS-1 and SS-2." · Policies & Documents — "Version-controlled policies drafted in Word with tracked changes." · Risk Management — "Risk register, KRIs and a dashboard for your CRO." · Risk Assessment Lab — "ICAAP, stress tests and scenario analysis with exportable reports." · Audit — "Internal, risk-based, IS and secretarial audits with findings tracked to closure." · Return Studio — "Turn Tally, Excel or LMS data into upload-ready return files." · Data Protection & Cyber — "DPDP, GDPR, CERT-In and sector cyber frameworks in one place." · HR & Labour — "HRMS, labour-code registers and the POSH Internal Committee." · Grievance Redressal — "Help desk to GRO to escalation, with every timeline tracked." · Vidhi AI — "An AI assistant that drafts, summarises and answers from your regulations — with citations, and always with your approval."

**Vidhi AI band**
- H2: Meet Vidhi — the AI colleague that does the first draft
- Copy: Ask Vidhi what a master direction requires and get an answer with the paragraph cited. Ask it to draft board minutes from your notes, align a policy with the latest direction (with tracked changes), or read a handwritten letter and prepare a typed copy. Vidhi drafts; your people approve. Nothing is filed, signed or sent without a human.

**Marketplace & academy band**
- H2: Need hands, not just software?
- Copy: Hire LawDocs professionals for policy drafting, ICAAP documents, stress testing, secretarial work, returns filing or a retainer — with or without a subscription. Learn through FinLegal Academy courses for compliance officers, CISOs and DSAs.
- CTAs: Explore the marketplace · See academy courses

**Regulatory updates band:** latest five published updates (`{{updates.latest(5)}}`) with regulator badge, date and "What changed" one-liner; link "All regulatory updates".

**Closing CTA:** "Ten minutes to your compliance baseline." [Take the free health check] [Book a demo]

### P.2.2 Solution page — NBFCs (`/solutions/nbfc-compliance-software`)

**Meta title:** NBFC Compliance Software — RBI Scale-Based Regulation, Returns & Risk | LawDocsComply
**Meta description:** For Base, Middle and Upper Layer NBFCs: every RBI direction mapped to owners and evidence, CIMS return calendars, CIC files, ICAAP and stress testing, grievance redressal and board reporting.

- H1: NBFC compliance software built around RBI's Scale-Based Regulation
- Sub: Whether you are a Base Layer NBFC-ICC or an Upper Layer lender, LawDocsComply shows exactly which RBI directions apply to your layer and type, who owns each obligation, and the proof that it was done.
- **What applies to you** (live block): `{{library.instruments(family="NBFC", group_by="layer")}}` — title, issued, last amended, obligations count; filter by layer (Base, Middle, Upper, Top) and type (ICC, MFI, HFC, CIC, P2P, AA, Factor, IDF, MGC, NOFHC).
- **Problems we solve** (H2 "Why NBFC compliance is getting harder"): consolidation of RBI's NBFC directions and frequent amendments; layer upgrades that bring new obligations overnight; supervisory returns across CIMS with tight timelines; fortnightly credit-information reporting to four CICs; board scrutiny of compliance, risk and audit functions.
- **What you get** (H2): obligation register by layer and type · compliance calendar with T-30/T-7/T-1 reminders · maker-checker evidence with checker comments · "What changed" diff for every amended direction · Return Studio for CIMS and CIC files (prepare, validate, export — you submit) · capital adequacy, ALM and ratio dashboards for the CFO and CRO · ICAAP and stress-testing lab · fair practices, KFS and grievance redressal workflows · board and committee packs.
- **Works with your systems:** Finbyx, Udofin and third-party LOS/LMS through APIs; Tally Prime and Excel imports; Microsoft 365 and Google Workspace calendars and storage.
- **Proof** (only when claim-approved): case study, metrics.
- **FAQ** (examples; answers ≤ 80 words, cited): "Does LawDocsComply file returns on the RBI portal for us?" → "No. LawDocsComply prepares and validates upload-ready files and keeps the acknowledgement as evidence; an authorised officer of your NBFC uploads them on the RBI portal." · "Can we change the questions and actionables?" → "Yes. Your admin can edit any actionable or add your own for your company; the change applies only to you and is recorded in the audit trail, while LawDocs keeps the base content current." · "What happens when RBI amends a direction?" → "Our content team reviews the change, publishes an update showing the old and new text and the affected actionables, and your users are notified to assess impact. Your past compliance records stay unchanged."
- CTAs: Take the NBFC health check · Start 7-day trial · Talk to an NBFC specialist

### P.2.3 Other solution pages (headline, sub, three proof bullets; full pages follow the NBFC template)

| Page | H1 | Sub | Three bullets |
|---|---|---|---|
| Banks & SFBs | Compliance and risk management for banks and small finance banks | Map RBI directions, Basel capital and liquidity requirements and board governance to owners and evidence. | Compliance-function workflows with CCO oversight · ICAAP, stress testing and Pillar 3 disclosure support · Supervisory return calendars and data lineage |
| Urban & rural co-operative banks | Compliance software for UCBs, StCBs and DCCBs | Tier-wise RBI requirements, dual regulation and board-of-management governance in one place. | Tier-based applicability · Board of Management and Board of Directors governance · Audit and returns tracking |
| Credit co-operative societies | Run your credit co-operative society's compliance and governance in one place | State Act or Multi-State Act, bye-laws, AGMs, elections, audits and returns — with member grievance handling. | Society governance: members, office bearers, elections, meetings · Statutory registers and audits · Pairs with Finbyx for loans and deposits |
| Other co-operative societies | Governance and compliance for housing, consumer, dairy and multi-purpose societies | Membership, meetings, elections, registers and returns under your State co-operative law. | Member register and share capital · AGM and committee meetings with minutes · Returns and audit calendar |
| Asset reconstruction companies | ARC compliance — RBI directions, SARFAESI and trust governance | Track ARC-specific obligations from acquisition to resolution, and board oversight of trusts. | ARC instrument packs · Trust and security-receipt governance tasks · Returns and audit tracking |
| Listed companies | SEBI LODR, PIT and secretarial compliance without spreadsheets | Board, committee, disclosure and insider-trading obligations with a secretarial calendar. | LODR calendar and disclosure tracking · Board portal with agendas and minutes · Structured digital database workflows for PIT |
| Mutual funds, AIFs, REITs & InvITs | Compliance for funds and investment vehicles | Scheme- and manager-level obligations with trustee and investment-committee governance. | Category-specific packs (AIF I/II/III) · Trustee and committee meetings · Investor grievance and reporting |
| Market intermediaries | Compliance for brokers, DPs, investment advisers, research analysts and PMS | Registration conditions, cyber resilience (CSCRF), investor grievances and periodic reporting. | Intermediary-type packs · SEBI CSCRF controls · SCORES grievance workflow |
| IFSCA entities | GIFT City compliance for IFSCA-regulated entities | From finance companies and fund managers to IBUs and insurance offices — IFSCA regulations mapped clause by clause. | 30+ IFSCA entity types · Clause-level actionables · Change tracking for IFSCA circulars |
| Insurers & intermediaries | IRDAI compliance for insurers, brokers and corporate agents | Corporate governance, solvency, product and distribution obligations with board reporting. | Insurer and intermediary packs · Solvency and risk dashboards · Bima Bharosa grievance tracking |
| Companies & LLPs | Companies Act and LLP compliance, done on time | Board meetings, minutes, registers, ROC filings, DIR-3 KYC and secretarial standards, for private, public, OPC and Section 8 companies and LLPs. | Secretarial calendar · Registers and minutes per SS-1/SS-2 · MCA filing tracker |
| Data protection & cyber | DPDP, GDPR and cyber-security compliance in one register | Notices, consents, rights requests, breach response and CERT-In reporting, alongside RBI, SEBI and IRDAI cyber frameworks. | DPDP Rules timeline built in · 6-hour CERT-In incident workflow · Records of processing and DPIAs |
| Labour, HR & POSH | Labour-code compliance and HRMS for Indian employers | Registers, returns, wage compliance, POSH Internal Committee and employment agreements with eSign — also available on its own. | Labour-code registers · POSH IC case handling (sealed) · Payroll and leave with statutory deductions |

### P.2.4 Pricing page copy (data from P20/Appendix N; package names configurable)

- H1: Simple plans. Pay for the modules you use.
- Sub: Start with a base plan, add the components you need, and see your price update as you go. All prices in INR; GST at the applicable rate is shown before you pay.
- Package cards (suggested names; final names in the catalogue): **Essentials** — "For smaller entities and single-entity companies getting organised." · **Professional** — "For growing regulated entities with multiple departments, makers and checkers." · **Enterprise** — "For groups, banks and large entities that need custom packs, SSO, data residency options and integrations." (Price: "Custom — talk to us".)
- Configurator steps (Apple-style): 1 Choose your plan → 2 Choose your entity family and regulators → 3 Add components (e.g., HR & Labour, Risk Assessment Lab, Return Studio, Vidhi AI credits, additional legal entities, additional users) → 4 Billing period (monthly / annual — annual saves `{{catalogue.annual_discount}}`) → 5 Review: line items, GST, total per month and per year, trial terms.
- Under the total: "7-day free trial on every self-serve plan. No card needed to start {{if catalogue.trial_requires_card=false}}. Cancel any time before the trial ends."
- Services-only band: "Only need help with a policy, a return or an ICAAP? Buy professional services without a subscription." → Marketplace.
- FAQ: What counts as a user? · Can I change plans later? (Yes; upgrades take effect immediately with proration; downgrades at the next renewal) · What happens to my data if I leave? (Download everything in folders of Word, Excel and PDF files; see Data portability) · Is GST charged? · Do you offer discounts for co-operative societies or startups? (`{{catalogue.programmes}}`) · Do you store card details? (No — payments are processed by our payment partner's hosted checkout).

### P.2.5 Health-check copy

**Start page (`/health-check`)**
- H1: Free compliance health check
- Sub: About 50 questions, 10 minutes, an instant score across ten areas of compliance — and a board-ready summary you can download and share.
- What you'll get: overall score and band · scores for governance, registration, compliance function, policies, risk, audit, returns, customer protection, data and cyber, people and POSH · your top gaps with the rule behind each · a 30-60-90-day action plan.
- Privacy note: "You can take the check without giving your name. If you want the PDF report emailed, we'll ask for your email and tell you exactly how we'll use it."
- Disclaimer (always visible): "This is an indicative self-assessment based on your answers. It is not legal advice, an audit, an assurance report or a certificate of compliance."

**Lookup step:** "Find your organisation (optional) — Enter your company name, CIN, LLPIN or PAN. We fetch your registered details from public records through our data partner to tailor the questions. Your PAN is shown masked and is not stored unless you start a trial."

**Answer-scale help:** Yes — "This is in place and you could show evidence today." · Partly — "Some of it is in place, or it is done but not documented." · No — "This is not in place." · Not sure — "You don't know; we'll count it as a gap and lower your confidence score." · Not applicable — "This requirement doesn't apply to you (pick the reason)."

**Consent notice (layered; first layer):**
> **How we use your details.** LawDocs Comply uses your email{{, name and phone}} to send your health-check report and to let you reopen it. We keep your answers and report for up to 12 months unless you start a trial. With your separate permission, we'll also send you guides and offers by email{{ or WhatsApp}}, and/or let a LawDocs relationship manager call you about your results. You can withdraw any permission at any time from the link in every message or at /my/reports, and ask us to correct or delete your data. Contact our Data Protection Officer at {{dpo.email}}. Read the full notice.
> ☐ Email me my report (required to send the PDF) ☐ Send me compliance guides and product news by email ☐ Contact me on WhatsApp/SMS ☐ Ask a LawDocs relationship manager to call me about my results

**Band texts (configurable):**
- *Strong foundation (85–100):* "Most of the essentials are in place. Focus on keeping evidence current and on the gaps listed below."
- *Adequate, with gaps (70–84):* "Your basics are in place, but some gaps could attract regulatory observations. Start with the critical items below."
- *Needs attention (50–69):* "Several important requirements are missing or undocumented. Use the 30-60-90-day plan to close the critical gaps first."
- *At risk (0–49):* "Many core requirements are not in place. We recommend prioritising the critical gaps immediately and getting expert help."
- *Critical-gap banner:* "You have {{n}} critical gap(s). These relate to requirements where non-compliance can lead to penalties or regulatory action."
- *Confidence low:* "You answered 'Not sure' to {{x}}% of questions. Your score may change once you check these items."

**Board-ready summary (PDF page 2) template:**
> **Compliance health check — summary for the Board / management of {{org_name}}**
> Self-assessed on {{date}} by {{respondent_role}} using LawDocsComply Health Check v{{bank_version}} (scoring model v{{model_version}}).
> Overall: **{{score}} / 100 — {{band}}** · Confidence: {{confidence}}.
> Top gaps: 1 … 5 (requirement, rule, recommended action, suggested owner).
> Recommended next steps: (i) assign owners for the critical gaps within 7 days; (ii) adopt or update the policies listed; (iii) set up a tracked obligation register; (iv) re-assess in 90 days.
> *This is an indicative self-assessment based on the respondent's answers. It is not legal advice, an audit, an assurance report or a certificate of compliance.*

### P.2.6 Marketplace and academy landing (`/marketplace`, `/academy`)

- Marketplace H1: Compliance, risk and governance experts — on demand
- Sub: Buy fixed-price services or set up a retainer with LawDocs professionals. No subscription needed. Every engagement has a defined scope, deliverables, timeline and a service-level agreement you sign online.
- Categories (from P21/Appendix O): Policies & documentation · Returns & filings · Secretarial & board support · Risk, ICAAP & stress testing · Audit & compliance testing · Data protection & cyber (incl. SOC 2 / ISO 27001 readiness, accessibility audits) · Virtual CXOs (CFO, CS, CCO, CISO, CTO) · Retainers · Training.
- Note under provider cards: "Services are provided by {{provider.legal_entity}}. Professionals list only the information their professional rules permit."
- Academy H1: Learn compliance from practitioners — FinLegal Academy
- Sub: Courses for compliance officers, company secretaries, CISOs, DSAs/DMAs and POSH committee members, delivered on trainings.lawdocs.in.

### P.2.7 Trust Centre (`/trust`)

- H1: Security, privacy and reliability at LawDocsComply
- Sections: Where your data lives ("Tenant data is stored in India (Mumbai) with disaster recovery in Hyderabad.") · How we isolate your data ("Every record is tagged to your organisation and protected by row-level security in the database…") · Encryption · Access by our staff ("Our team can see your data only when you grant access or through an emergency procedure that is time-limited, reason-coded and shown to you.") · Audit trail ("Every change is recorded in a tamper-evident log. Corrections never erase the original.") · AI and your data ("We do not use your data to train AI models…") · Sub-processors (table) · Certifications and assessments (`{{claims.certifications}}` — only recorded statuses) · Uptime and status · Accessibility · Report a vulnerability (security.txt).

### P.2.8 Accessibility statement (template, `/accessibility`)

> **Accessibility statement for LawDocsComply**
> LawDocs Comply is committed to making LawDocsComply usable by everyone, including people who are blind or have low vision, are deaf or hard of hearing, have motor or cognitive disabilities, or use assistive technologies.
> **Our target:** WCAG 2.2 Level AA and IS 17802 (Part 1): 2021 for our website, web application, documents and videos.
> **Current status:** {{status: "Partially conforms"/"Conforms"}} — see our Accessibility Conformance Report ({{acr.version}}, {{acr.date}}) for details and known exceptions.
> **What we do:** automated and manual testing with screen readers (NVDA, JAWS, VoiceOver, TalkBack), keyboard-only and voice-control testing, an annual independent audit by an IAAP-certified professional (last audit: {{audit.date}}), captions and transcripts for all videos, Indian Sign Language for selected videos, and accessible PDF and Word exports.
> **Your preferences:** change text size, spacing, contrast, motion, captions and keyboard shortcuts under Profile → Accessibility and display.
> **Tell us about a problem:** use the accessibility feedback form, email {{a11y.email}}, call {{a11y.phone}}, or request a video call with an ISL interpreter. We acknowledge within 1 working day and aim to resolve within 15 working days. Accessibility nodal officer: {{a11y.officer}}.
> **Escalation:** if you are not satisfied with our response, contact {{escalation}}. You may also approach the Chief Commissioner for Persons with Disabilities.
> Last reviewed: {{date}}.

### P.2.9 Nurture sequence templates (sent from the Operations Hub; LDC supplies tokens)

| # | Timing | Subject | Purpose and content |
|---|---|---|---|
| N1 | Immediately | Your compliance health check report — {{band}} | Report link and PDF; top three gaps; "what to do this week" |
| N2 | Day 2 | How to close "{{top_gap.title}}" in 30 minutes | The rule, a 3-step fix, tutorial video, template (from guides) |
| N3 | Day 4 | What changed for {{family}}s this month | Digest of published regulatory updates for the family |
| N4 | Day 7 | How {{peer_type}} entities track every obligation (case study, claim-bound) | Story; link to trial |
| N5 | Day 10 | Your 7-day trial is ready when you are | Trial benefits; pre-filled profile; what happens after the trial |
| N6 | Day 14 | Want an expert to review your results? | Expert review offer (marketplace price); retainer option |
| N7 | Day 30 | Re-check your score | Retake link; trend once retaken |

Each message: plain-text part, unsubscribe and preference link, sender identity, no tracking pixel unless analytics consent exists, WhatsApp variants only with consent and DLT-registered templates.

### P.2.10 Microcopy library (selected)

| Context | Copy |
|---|---|
| Empty obligation register | "No obligations yet. Add an instrument pack to see what applies to you." [Browse instrument catalogue] |
| Evidence rejected | "Your checker returned this for rework: '{{comment}}'. Update the evidence and resubmit." |
| Update received | "RBI amended {{instrument}}. 3 of your actionables changed. Review what changed." |
| AI draft label | "Draft by Vidhi AI — review before you use it." |
| Upload-ready return | "Your file passed {{n}} validation checks. Download it and upload it on {{portal}} yourself, then attach the acknowledgement here." |
| Session timeout warning | "You'll be signed out in 2 minutes to protect your account. Your work is saved." [Stay signed in] |
| Error with code | "We couldn't save this change. Please try again. If it keeps happening, contact support and quote {{error_code}}." |
| "i" fallback | "We're writing an explanation for this term." (never shipped on release builds) |
| Accessibility feedback thanks | "Thank you. We've logged your report as {{ticket}} and will reply within 1 working day." |

---

## P.3 Free Compliance Health Check — families, question bank and scoring

### P.3.1 Launch families and type lists

| Family code | Family | Types / layers offered in Step 1 | Default regulators | Template families (Appendix E; overlays DATA-PRIV, CYBER, LAB-POSH, TAX-GST apply to all) |
|---|---|---|---|---|
| NBFC | Non-banking financial companies | Base / Middle / Upper / Top layer × ICC, MFI, HFC, CIC, P2P, AA, Factor, IDF, MGC, NOFHC, Gold-loan focus, Digital lender | RBI, MCA, FIU-IND, CERT-In | RBI-NBFC |
| BANK | Banks | Public sector, private sector, foreign bank, small finance bank, payments bank, regional rural bank, local area bank | RBI, MCA/SEBI where listed | RBI-SCB |
| COOPBANK | Co-operative banks | UCB Tier 1–4; State co-operative bank; District central co-operative bank | RBI, NABARD (StCB/DCCB), RCS | RBI-UCB, RBI-RCB |
| CCS | Credit co-operative societies | State Act society; Multi-State (MSCS Act 2002) society | RCS/CRCS, State election authority | COOP-CCS |
| COOP | Other co-operative societies | Housing, consumer, dairy/agri, multi-purpose, employees' society (State or Multi-State) | RCS/CRCS | COOP-GEN |
| ARC | Asset reconstruction companies | ARC (registered under SARFAESI s.3) | RBI, MCA | RBI-ARC |
| SEBI-LISTED | Listed entities | Main board equity, SME platform, debt-listed only | SEBI, stock exchanges, MCA | SEBI-LISTED |
| SEBI-FUND | Funds & vehicles | Mutual fund/AMC/trustee; AIF Cat I/II/III; REIT; InvIT; PMS | SEBI | SEBI-MF, SEBI-AIF, SEBI-REIT-INVIT |
| SEBI-INT | Market intermediaries | Stockbroker, depository participant, investment adviser, research analyst, merchant banker, RTA, debenture trustee, credit rating agency | SEBI, exchanges, depositories | SEBI-INT |
| IFSCA | IFSCA-regulated entities | Entity type list from the IFSCA template (Appendix E): FC/FU, IBU, FME, broker-dealer, insurance office, etc. | IFSCA | IFSCA-GEN, IFSCA-FCFU, IFSCA-FME |
| IRDAI | Insurance | Life, general, health, reinsurer; broker, corporate agent, web aggregator, IMF, TPA | IRDAI | IRDAI-INS, IRDAI-INT |
| CO | Companies & LLPs | Private, public unlisted, OPC, Section 8, small company, LLP | MCA | MCA-CO, MCA-LLP |

The twelve health-check families are a simplified front door; each maps to one or more of the 24 template families (master §1.2, X-09), so a trial created from a report pre-selects the matching packs (P23 FR-P23-60, P20 §4C). Payment-system entities, AIFIs and CICs (template `RBI-OTH`) are offered under BANK/NBFC "Other RBI-regulated entity" until a dedicated health-check family is added.

### P.3.2 Core question bank v1.0 (50 questions)

Columns: **Code** · **Weight** (3 = penalty or regulatory action likely / licence-critical; 2 = significant; 1 = good practice or lower consequence) · **Question (default wording)** · **Rule (citation, re-verify at publication)** · **Family variants / N/A rules** · **LDC module · Marketplace service**.

#### Segment 1 — Governance and board (GOV)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-GOV-01 | 3 | Did your Board meet at least four times in the last financial year, with no gap of more than 120 days between two meetings? | Companies Act 2013 s.173(1); SS-1 | OPC/small/dormant company: at least one meeting in each half of the year with ≥ 90 days gap (s.173(5)); CCS/COOP: "Did the managing committee meet as often as your bye-laws and State Act require?"; LLP: "Is your LLP agreement (Form 3) up to date for all current partners?" (LLP Act 2008 s.23) | Governance · Secretarial retainer |
| HC-GOV-02 | 2 | Are minutes of every board and committee meeting finalised, signed and entered in the minutes book within 30 days? | s.118; Companies (Management and Administration) Rules 2014 r.25; SS-1 para 7 | CCS/COOP: minutes as per bye-laws; LLP: N/A → reserve | Governance (minutes) · Minutes drafting |
| HC-GOV-03 | 2 | Have you constituted every board committee that applies to you (for example Audit, Nomination and Remuneration, Risk Management, Stakeholders' Relationship, IT Strategy) with written terms of reference? | ss.177–178; SEBI LODR Regs 18–21; RBI governance requirements for the entity type [VERIFY current para] | BANK/NBFC: include RBI-mandated committees for the layer; private company below thresholds: "Do you have any board committees, and are their roles documented?" (weight 1) | Governance (committees) · Governance review |
| HC-GOV-04 | 3 | Have all directors completed annual KYC (DIR-3 KYC) and given their annual declarations (interest, independence and fit-and-proper as applicable)? | Companies (Appointment and Qualification of Directors) Rules 2014 r.12A; s.184(1); s.149(7); RBI fit-and-proper requirements for NBFC/bank directors [VERIFY]; SEBI Intermediaries Regs 2008 Sch. II | CCS/COOP: "Do office bearers meet the eligibility conditions of your State Act and bye-laws, with declarations on file?"; LLP: designated partners' DIR-3 KYC | Governance (directors & KMP) · Fit-and-proper documentation |
| HC-GOV-05 | 2 | Are your statutory registers (members, directors and KMP, charges, contracts with related parties, loans and investments) maintained and up to date? | ss.88, 170, 85, 189, 186; Rules thereunder | CCS/COOP: member register, share register and other registers under State Act; LLP: register of partners | Governance (registers) · Registers compilation |

#### Segment 2 — Registration, licensing and fit-and-proper (REG)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-REG-01 | 3 | Do you hold a valid registration or licence for every regulated activity you carry on, and do you operate within its conditions? | RBI Act 1934 s.45-IA (NBFC); Banking Regulation Act 1949 s.22; SEBI Act 1992 s.12; IFSCA Act 2019 and entity regulations; Insurance Act 1938 s.3 / IRDAI regulations; State Co-operative Act / MSCS Act 2002 s.7; SARFAESI s.3 (ARC) | CO: "Do you hold every business registration you need (GST, Shops and Establishments, trade licences)?" (weight 2) | Compliance (registration pack) · Licensing support |
| HC-REG-02 | 3 | Did you obtain prior approval or give the required intimation for every change in control, shareholding, management or directors in the last two years? | RBI directions on change in control/management of NBFCs [VERIFY para]; SEBI Intermediaries Regs (change in control); Companies Act (DIR-12 within 30 days) | CO: "Were director and KMP changes filed with the ROC within 30 days?" | Governance · Regulatory approvals support |
| HC-REG-03 | 2 | Is your net owned fund / minimum capital / net worth always above the regulatory minimum, and is it checked at least quarterly? | NBFC NOF requirements under Scale-Based Regulation (phased) [VERIFY current figures and glide path]; SEBI net-worth requirements per intermediary type; IRDAI capital; IFSCA entity regulations | CO/COOP: N/A → reserve HC-RES-01 | Risk Lab (capital) · Capital computation review |
| HC-REG-04 | 2 | Have changes in your registered office, name, objects or key particulars been updated with the regulator and the Registrar within the time allowed? | Companies Act s.12 (INC-22 within 30 days); regulator intimation requirements | CCS/COOP: amendments of bye-laws registered with the Registrar | Governance · Secretarial filings |
| HC-REG-05 | 1 | Are your regulator-portal and MCA logins held by named, authorised officers, with access reviewed when people change roles? | Good practice; RBI/SEBI IT governance on access control [INTERP] | All families | Service Delivery (credential vault) · — |

#### Segment 3 — Compliance function and calendar (CMP)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-CMP-01 | 3 | Have you appointed a compliance officer (Chief Compliance Officer where required) with a defined role, independence and reporting line to the Board? | RBI Compliance Function and Role of CCO for NBFCs (Middle and Upper Layer) and banks [VERIFY current instrument, incl. 2026 NBFC Compliance Function directions]; SEBI LODR Reg 6; SEBI intermediary regulations; IRDAI corporate governance; IFSCA | CO (unlisted): "Is a named person (company secretary or other) responsible for tracking all compliances?"; CCS/COOP: secretary/CEO responsibility | Compliance Workspace · Virtual CCO |
| HC-CMP-02 | 3 | Do you keep a single register of every legal and regulatory obligation that applies to you, with an owner, a due date and the evidence of completion? | Expectation under RBI compliance-function requirements and ISO 37301 practice [INTERP] | All families | Compliance Workspace · Compliance mapping |
| HC-CMP-03 | 2 | Does the Board (or its committee) approve a compliance policy and receive a compliance report at least quarterly? | RBI compliance-function requirements [VERIFY]; LODR Reg 17(3) (compliance report on laws placed before the Board) | CO: "Does management review a compliance status report at least quarterly?" (weight 1) | Reports · Board reporting support |
| HC-CMP-04 | 2 | When a regulator issues a new or amended direction, do you assess its impact and assign actions within a defined time (for example 15 days)? | Good practice; RBI expectation of compliance-function change tracking [INTERP] | All | Regulatory Change · Regulatory update service |
| HC-CMP-05 | 2 | Is every regulatory filing and response reviewed by a second person (maker–checker) before it is submitted? | Internal-control expectation [INTERP] | All | Compliance Workspace (maker–checker) · Compliance testing |

#### Segment 4 — Policies and procedures (POL)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-POL-01 | 3 | Do you have every Board-approved policy your regulator requires for your entity type (for example Fair Practices Code, KYC/AML, grievance redressal, ALM, investment, IT/cyber, outsourcing)? | Entity-specific RBI/SEBI/IFSCA/IRDAI requirements (Appendix G) | CO: "Do you have the policies the Companies Act requires for you (for example CSR policy (s.135), vigil mechanism (s.177(9)), related-party policy where listed)?" | Policies · Policy drafting |
| HC-POL-02 | 2 | Is each policy reviewed at least annually (or as required), with version history, owner and Board approval date recorded? | Entity-specific review periodicity [VERIFY]; good practice | All | Policies (version control) · Policy review |
| HC-POL-03 | 2 | Do you have a KYC/AML policy, a Principal Officer and a Designated Director, and are you registered with FIU-IND for reporting? | PMLA 2002 s.12; PML (Maintenance of Records) Rules 2005; RBI KYC Master Direction 2016 (as amended); SEBI/IFSCA AML guidelines | CO/COOP (non-credit): N/A unless a reporting entity → reserve | Policies; Returns (FIU) · AML review |
| HC-POL-04 | 2 | Before outsourcing any material activity or IT service, do you carry out due diligence, sign a contract with the required clauses and keep a register of outsourced arrangements? | RBI Outsourcing of IT Services Directions 2023; RBI outsourcing of financial services directions [VERIFY current]; SEBI outsourcing guidelines; IRDAI outsourcing regulations | CO: weight 1 | TPRM · Vendor due diligence |
| HC-POL-05 | 1 | Are your policies made available to staff, and do relevant staff acknowledge them? | Good practice | All | Policies (attestations) · — |

#### Segment 5 — Risk management and capital (RSK)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-RSK-01 | 3 | Do you have a Board-approved risk management policy with a risk appetite, a risk management committee and (where required) a Chief Risk Officer? | RBI requirements on risk management and CRO for NBFCs (by size/layer) and banks [VERIFY]; LODR Reg 21 (top 1,000 listed); IRDAI CG guidelines | CO (unlisted): "Do you identify and review your key business risks at least annually?" (weight 1) | Risk Management · Risk framework design |
| HC-RSK-02 | 3 | Do you compute your capital adequacy (or solvency/net-worth) ratio at the required frequency and keep it above the minimum? | NBFC CRAR 15% with Tier 1 ≥ 10% for applicable NBFCs [VERIFY layer-wise]; Basel III for banks; UCB capital norms; IRDAI solvency ratio 150%; SEBI net worth | CO/COOP/SEBI-LISTED (non-financial): N/A → reserve | Risk Lab (capital & ratios) · Capital adequacy review |
| HC-RSK-03 | 2 | Do you monitor liquidity and asset-liability mismatches (structural liquidity, interest-rate sensitivity) and report them to your ALCO/Board? | RBI Liquidity Risk Management Framework for NBFCs (2019) and ALM requirements [VERIFY]; bank LCR/NSFR | CO/COOP (non-credit): N/A → reserve | Risk Lab (ALM) · ALM review |
| HC-RSK-04 | 2 | Do you run stress tests or scenario analyses at least once a year and present the results to the Board (and, where required, prepare an ICAAP)? | RBI stress-testing guidelines; ICAAP for banks and Upper Layer NBFCs [VERIFY] | CO: weight 1 | Risk Lab (stress testing, ICAAP) · ICAAP drafting, stress testing |
| HC-RSK-05 | 2 | Do you keep a risk register with key risk indicators and record incidents, losses and frauds, reporting frauds to the regulator within the required time? | RBI Fraud Risk Management Directions (2024; NBFC directions 2026) [VERIFY]; operational-risk practice | CO: "Do you record incidents and frauds and act on them?" | Risk Management · Fraud risk review |

#### Segment 6 — Audit and assurance (AUD)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-AUD-01 | 3 | Is your statutory auditor appointed, eligible and rotated as required (including RBI's auditor-appointment rules where they apply)? | Companies Act ss.139–141; RBI guidelines on appointment of statutory auditors (2021) for NBFCs and UCBs above thresholds [VERIFY]; State Act audit (co-operatives) | CCS/COOP: "Is your annual audit done by an auditor from the Registrar's panel and placed before the general body?" | Audit · Audit coordination |
| HC-AUD-02 | 3 | Do you have an internal audit (risk-based internal audit where required) with an annual plan approved by the Audit Committee? | Companies Act s.138 and Companies (Accounts) Rules 2014 r.13; RBI RBIA requirements for specified NBFCs/UCBs [VERIFY incl. 2026 NBFC internal-audit directions] | CO below s.138 thresholds: weight 1 | Audit (RBIA) · Internal audit outsourcing |
| HC-AUD-03 | 2 | Do you obtain a secretarial audit (or compliance audit) where required, and act on its observations? | s.204; LODR Reg 24A | CCS/COOP: N/A; private companies below threshold: N/A | Audit (secretarial) · Secretarial audit |
| HC-AUD-04 | 2 | Are all audit and inspection findings tracked to closure with owners and target dates, and reviewed by the Audit Committee? | Audit Committee role (s.177(4)); RBI inspection compliance expectations | All | Audit (findings) · Compliance testing |
| HC-AUD-05 | 2 | Has an information-systems (IS) or IT audit been carried out in the last 12 months? | RBI IT Governance, Risk, Controls and Assurance Practices Directions 2023 [VERIFY applicability]; SEBI CSCRF | CO: weight 1 | Audit (IS) · IS audit |

#### Segment 7 — Returns and regulatory reporting (RET)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-RET-01 | 3 | Have all periodic regulatory returns for the last four quarters been filed on time (for example on RBI's CIMS portal, SEBI, IFSCA, IRDAI or Registrar of Co-operative Societies portals)? | RBI supervisory-returns directions and return list [VERIFY]; respective regulator requirements | CO: N/A → covered by HC-RET-02 | Return Studio · Returns filing support |
| HC-RET-02 | 3 | Were your annual financial statements and annual return filed with the Registrar of Companies within the due dates last year? | Companies Act s.137 (AOC-4) and s.92 (MGT-7/7A); LLP Act s.34–35 (Form 8, Form 11) | CCS/COOP: annual return to Registrar under State Act / MSCS Act s.120 | Governance (MCA filings) · Annual filings |
| HC-RET-03 | 2 | Do you report credit information to all four credit information companies at the required frequency and correct rejections promptly? | Credit Information Companies (Regulation) Act 2005; Credit Information Companies Regulations 2006; RBI directions on credit reporting frequency [VERIFY] | Lenders only (NBFC, BANK, COOPBANK, CCS where member of CICs, ARC); others N/A → reserve | Return Studio (CIC files) · CIC reporting support |
| HC-RET-04 | 2 | Are GST and TDS returns filed on time and reconciled with your books? | CGST Act 2017 ss.37, 39; Income-tax Act 2025 TDS return provisions [VERIFY form numbers] | All | Return Studio (GST/TDS) · Tax compliance |
| HC-RET-05 | 2 | Before submission, is return data reconciled to your trial balance or loan system, checked by a second person, and the acknowledgement kept? | Accuracy expectations in RBI returns directions [VERIFY]; good practice | All | Return Studio (validation) · Return review |

#### Segment 8 — Customer protection and grievance redressal (CUS)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-CUS-01 | 3 | Do you have a grievance redressal mechanism with a named grievance officer whose details are displayed on your website, app and offices? | RBI Fair Practices Code and Reserve Bank – Integrated Ombudsman Scheme [VERIFY 2026 version]; SEBI SCORES; IRDAI (Protection of Policyholders' Interests) regulations; LODR Reg 13; IFSCA | CO: "Do you have a published way for customers/stakeholders to complain and a person responsible?" (weight 1); CCS/COOP: member complaints mechanism | Grievance Redressal · Grievance set-up |
| HC-CUS-02 | 2 | Are complaints acknowledged and resolved within the required timelines, escalated when they are not, and analysed for root causes? | Regulator timelines (e.g., 30 days for RBI REs before Ombudsman route) [VERIFY]; Internal Ombudsman where applicable | All | Grievance Redressal · — |
| HC-CUS-03 | 2 | Do you give borrowers/customers a Key Fact Statement and agreement in a language they understand, with all charges and the annual percentage rate disclosed? | RBI KFS requirements (2024) and digital lending directions [VERIFY current consolidated directions] | Lenders only; SEBI/IRDAI: "Do you give customers the disclosures your regulator requires before sale (risk-o-meter, KIM, policy documents)?"; CO: N/A → reserve | Compliance (conduct pack) · Documentation review |
| HC-CUS-04 | 2 | If you use lending service providers, digital lending apps or other agents, have you done due diligence, reported them as required and monitored their conduct? | RBI Digital Lending Directions 2025 [VERIFY]; outsourcing directions | Lenders only; others: "Do you supervise agents/distributors who deal with your customers?" | TPRM · LSP due diligence |
| HC-CUS-05 | 1 | Do your collections and customer communications follow conduct rules (permitted hours, no harassment, recorded calls where required, DND/consent for marketing)? | RBI conduct requirements on recovery; TRAI TCCCPR 2018 (as amended) | Non-lenders: marketing consent and DND only | Compliance (conduct) · — |

#### Segment 9 — Data protection and cyber security (DPC)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-DPC-01 | 3 | Do you have a process to report cyber-security incidents to CERT-In within 6 hours of noticing them, and to your regulator within its timeline? | CERT-In Directions under IT Act s.70B(6), 28 Apr 2022; RBI/SEBI/IRDAI incident reporting [VERIFY timelines] | All | Data & Cyber (incidents) · Incident response retainer |
| HC-DPC-02 | 2 | Do you have a Board-approved information/cyber security policy and an IT governance framework appropriate to your regulator (for example RBI IT governance directions, SEBI CSCRF, IRDAI information-security guidelines)? | RBI IT Governance Directions 2023; SEBI CSCRF (20 Aug 2024, as clarified); IRDAI IS & Cyber Security Guidelines 2023 | CO: "Do you have a written information-security policy?" (weight 1) | Data & Cyber (ISMS) · Cyber policy drafting |
| HC-DPC-03 | 2 | Do you know what personal data you collect, for what purpose and where it is stored, and do you give DPDP-compliant notices and take consent where needed? | DPDP Act 2023 ss.4–6, 8; DPDP Rules 2025 r.3 (phased commencement; full obligations from 13 May 2027) [VERIFY] | All | Data & Cyber (RoPA, notices) · DPDP readiness |
| HC-DPC-04 | 2 | Do you keep ICT system logs for at least 180 days within India and synchronise clocks with the NTP servers specified by CERT-In? | CERT-In Directions 28 Apr 2022 paras (iv) and (i) [VERIFY numbering] | All | Data & Cyber · Log review |
| HC-DPC-05 | 2 | Do you review user access at least every six months, use multi-factor authentication for privileged and remote access, and run a vulnerability assessment and penetration test at least annually? | RBI IT governance/cyber directions; SEBI CSCRF; ISO/IEC 27001:2022 A.5.18, A.8.5, A.8.8 | CO: weight 1 | Data & Cyber · VAPT |

#### Segment 10 — People, labour and POSH (PPL)

| Code | W | Question | Rule | Variants / N/A | Module · Service |
|---|---|---|---|---|---|
| HC-PPL-01 | 3 | If you have 10 or more employees, have you constituted an Internal Committee under the POSH Act with an external member, displayed its details, and filed the annual report? | Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 ss.4, 19, 21, 22 | Fewer than 10 employees: "Do your employees know how to approach the Local Committee?" (weight 1) | HR & Labour (POSH IC, sealed) · POSH IC external member / training |
| HC-PPL-02 | 2 | Are you registered for and paying provident fund, ESI, professional tax and labour welfare fund contributions on time, where applicable? | EPF & MP Act 1952 / Code on Social Security 2020 (effective 21 Nov 2025) [VERIFY transition]; State PT and LWF Acts | All employers | HR & Labour (payroll) · Payroll compliance |
| HC-PPL-03 | 2 | Have you updated wages, appointment letters, registers and working-hour practices for the four Labour Codes that took effect on 21 November 2025? | Code on Wages 2019; Industrial Relations Code 2020; Code on Social Security 2020; OSH and Working Conditions Code 2020; central and State rules [VERIFY State rules] | All employers | HR & Labour (registers) · Labour-code readiness |
| HC-PPL-04 | 2 | Does every employee have a signed appointment letter or employment agreement, and are HR policies (leave, working hours, code of conduct) communicated? | OSH Code s.6 (appointment letters) [VERIFY]; good practice | All employers | HR & Labour (agreements with eSign) · Employment agreement drafting |
| HC-PPL-05 | 1 | Do you deliver and record mandatory training (KYC/AML, POSH awareness, cyber hygiene, code of conduct) for relevant staff? | POSH Act s.19(c); PMLA/KYC training expectations; cyber directions | All | HR & Labour (training records) · FinLegal Academy courses |

#### Reserve questions (substituted when a core question is N/A for the family)

| Code | W | Segment | Question | Rule |
|---|---|---|---|---|
| HC-RES-01 | 2 | RSK | Do you monitor key financial covenants (net worth, borrowings, lender covenants) and report breaches to the Board? | Good practice; s.180 borrowing limits |
| HC-RES-02 | 2 | GOV | Are related-party transactions identified, approved as required and disclosed? | Companies Act s.188; Rules r.15; LODR Reg 23 (listed) |
| HC-RES-03 | 2 | GOV | Have you identified significant beneficial owners and filed the required declarations? | s.90; Companies (Significant Beneficial Owners) Rules 2018 (BEN-1/BEN-2) |
| HC-RES-04 | 2 | CMP | If you have foreign investment or overseas investment, are FEMA filings (FC-GPR/FC-TRS, FLA return, ODI) up to date? | FEMA 1999; NDI Rules 2019; ODI Rules 2022; RBI FLA return |
| HC-RES-05 | 2 | GOV | Is there a vigil (whistle-blower) mechanism with protection against victimisation? | s.177(9)–(10); r.7 Companies (Meetings of Board) Rules; LODR Reg 22 |
| HC-RES-06 | 1 | RSK | Do you have a business continuity plan that is tested at least annually? | Good practice; sector BCP requirements |
| HC-RES-07 | 2 | RET | If you meet the CSR threshold, do you spend and report CSR as required (CSR-2)? | s.135; CSR Rules 2014 |
| HC-RES-08 | 1 | CUS | Do you keep a register of litigation and legal notices with next dates and owners? | Good practice |
| HC-RES-09 | 2 | RET | If you are a top-1,000 listed entity, do you prepare the Business Responsibility and Sustainability Report? | LODR Reg 34(2)(f) |
| HC-RES-10 | 1 | POL | Do you have a document-retention schedule that meets your statutory retention periods? | Companies Act s.128(5) (8 years books); PMLA r.3 records (5 years) |

### P.3.3 Segment weights by family (Σ = 100)

| Segment | NBFC | BANK | COOPBANK | CCS | COOP | ARC | SEBI-LISTED | SEBI-FUND | SEBI-INT | IFSCA | IRDAI | CO |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GOV | 10 | 10 | 12 | 15 | 20 | 10 | 15 | 10 | 8 | 10 | 10 | 20 |
| REG | 10 | 8 | 8 | 10 | 12 | 10 | 5 | 12 | 12 | 12 | 10 | 8 |
| CMP | 12 | 12 | 10 | 10 | 8 | 12 | 12 | 12 | 12 | 12 | 12 | 10 |
| POL | 10 | 10 | 10 | 8 | 6 | 10 | 8 | 10 | 10 | 10 | 10 | 8 |
| RSK | 12 | 15 | 12 | 10 | 5 | 12 | 8 | 12 | 8 | 10 | 12 | 5 |
| AUD | 10 | 10 | 12 | 12 | 12 | 10 | 10 | 8 | 8 | 10 | 10 | 10 |
| RET | 12 | 12 | 12 | 10 | 10 | 12 | 10 | 10 | 10 | 12 | 10 | 12 |
| CUS | 10 | 10 | 10 | 10 | 7 | 8 | 10 | 10 | 12 | 8 | 10 | 5 |
| DPC | 8 | 8 | 8 | 7 | 8 | 8 | 10 | 8 | 12 | 10 | 8 | 10 |
| PPL | 6 | 5 | 6 | 8 | 12 | 8 | 12 | 8 | 8 | 6 | 8 | 12 |

Weights are Governed settings in scoring model v1.0; changes require a new model version (FR-P23-55).

### P.3.4 Profile refiners (Step 3)

| Family | Refiners (≤ 6) |
|---|---|
| NBFC | Asset size band (< ₹100 cr; ₹100–1,000 cr; ₹1,000–5,000 cr; ₹5,000–50,000 cr; > ₹50,000 cr) · deposit-taking? · customer interface? · digital lending/LSPs? · listed debt/equity? · employees band |
| BANK | Category · assets band · listed? · foreign operations? · employees band |
| COOPBANK | Tier · deposits band · number of branches · State(s) · employees band |
| CCS | State Act or Multi-State · members band · deposits band · branches · States of operation |
| COOP | Type · members band · State(s) · employees band |
| ARC | AUM band · listed? · employees band |
| SEBI-LISTED | Market-cap band (top 100/500/1,000/other) · SME platform? · debt-listed? · employees band |
| SEBI-FUND | Vehicle type · AUM/corpus band · investor count band |
| SEBI-INT | Intermediary type(s) · client-count band · qualified stockbroker/MII-linked? |
| IFSCA | Entity type(s) · unit or company · parent jurisdiction |
| IRDAI | Insurer/intermediary type · gross written premium/revenue band · employees band |
| CO | Constitution · paid-up capital and turnover bands (small-company test) · employees band · foreign investment? · CSR threshold met? |

### P.3.5 Action-plan rules (deterministic)

- **0–30 days:** all critical gaps (weight-3 No/Not sure), ordered by segment weight.
- **31–60 days:** weight-2 No answers, then Partly answers on weight-3 questions.
- **61–90 days:** weight-2 Partly, weight-1 No, and all Not sure answers ("verify and document").
- Each line: "{{action}} — Owner suggestion: {{role}} — Helpful in LDC: {{module}} — Need help? {{service}} (from ₹{{price}})".

---

## P.4 Glossary — first 152 terms by priority

Tier A (launch day, 60 terms): Actionable · Applicability · Annual Percentage Rate (APR) · Asset-Liability Management (ALM) · Audit Committee · Audit trail · Base Layer · Board meeting · Capital adequacy ratio (CRAR) · Checker · Chief Compliance Officer (CCO) · Chief Risk Officer (CRO) · CIMS (RBI's Centralised Information Management System) · Circular · Compliance calendar · Compliance instance · Correction entry · Credit information company (CIC) · Critical gap · Daksh (RBI supervisory platform) · Data fiduciary · Data principal · Department head · Designated Director (PMLA) · DIR-3 KYC · Due date · Evidence · Exception · Fair Practices Code · FIU-IND · Fit and proper · Frequency · Grievance Redressal Officer (GRO) · ICAAP · Independent director · Internal Committee (POSH) · Internal Ombudsman · Key Fact Statement (KFS) · Key Managerial Personnel (KMP) · Key risk indicator (KRI) · KYC · Maker · Maker–checker · Master Direction · Middle Layer · Minutes · NBFC · Net Owned Fund (NOF) · Notification (in LDC) · Obligation · Pravaah (RBI applications portal) · Principal Officer (PMLA) · Regulatory update · Return · Risk appetite · Risk register · Scale-Based Regulation (SBR) · Secretarial Standards (SS-1, SS-2) · Stress test · Upper Layer.

Tier B (by end of P23, 92 terms): Accessibility Conformance Report · AIF categories · AOC-4 · Asset reconstruction company · Attestation · Basel III · Basel Pillar 1 / 2 / 3 · Board pack · Break-glass access · BRSR · Business continuity plan · CERT-In · CSCRF (SEBI) · CSR · Committee terms of reference · Concentration risk · Consent artefact · Consent manager · Co-operative society · Credit risk · Cyber incident · Data Protection Officer · Debenture trustee · Deposit-taking NBFC · Designated partner · Digital lending app (DLA) · DPDP Act · DPIA · Effective date · Expected credit loss (ECL) · Gross NPA · Net NPA · Gap analysis · GDPR · Horizon scanning · IFSC · IFSCA · Ind AS · Information-systems audit · Insider trading (PIT) · Interest-rate risk in the banking book (IRRBB) · Internal audit · Investment Committee · IRACP norms · IRDAI · LCR · Leverage ratio · Liquidity risk · LLP · LODR · Loss event · Lending service provider (LSP) · Market risk · Material outsourcing · MGT-7 · Model risk · Multi-State Co-operative Society · NSFR · One Person Company · Operational risk · Outsourcing · PCA (Prompt Corrective Action) · People risk · Policy owner · Provision coverage ratio · Quorum · RBIA (risk-based internal audit) · Record of processing activities · Related-party transaction · Reputational risk · Residual risk · Inherent risk · Returning officer (co-operative elections) · Risk and control self-assessment (RCSA) · Risk Management Committee · ROC · Scenario analysis · SCORES · Secretarial audit · Section 8 company · Security receipt · Significant beneficial owner · Small company · Solvency ratio · Statutory auditor · Statutory register · Strategic risk · Structured digital database (SDD) · Third-party risk · Tier 1 / Tier 2 capital · Vigil mechanism · WCAG.

---

## P.5 Tutorial and video catalogue (launch set, 44 videos)

Columns: ID · Title · Role · Module · Length · Social cut-downs (V = 9:16 ≤ 60 s, S = 1:1 ≤ 90 s, W = 16:9) · ISL (priority) · Script outline.

| ID | Title | Role | Module | Len | Cuts | ISL | Script outline |
|---|---|---|---|---|---|---|---|
| T-01 | LawDocsComply in 2 minutes | All | Overview | 2:00 | V,S,W | ✓ | Problem → three steps → modules → health check CTA |
| T-02 | Take the free compliance health check | Prospect | Health check | 2:30 | V,S | ✓ | Choose family → lookup → answer → result → PDF/share |
| T-03 | Start your trial with your PAN or CIN | Admin | Onboarding | 2:00 | V | ✓ | Trial → lookup → confirm profile → suggested packs |
| T-04 | Set up departments, users and roles | Admin | Settings/IAM | 3:30 | S | ✓ | Departments → invite users → assign maker/checker → HRMS link |
| T-05 | Add instrument packs from the catalogue | Admin/CCO | Content catalogue | 2:30 | V | ✓ | Browse → filter by family → applicability info → add → obligations created |
| T-06 | Edit an actionable for your company | Admin/CCO | Compliance (overlay) | 2:30 | V | | Open item → edit → reason → audit trail → base vs tenant diff |
| T-07 | Upload your own question sheet (Excel) | Admin | Template import | 3:00 | S | | Download template → fill → upload → preview → fix errors → commit |
| T-08 | Your first week as a maker | Maker | Compliance | 3:00 | V,S | ✓ | My tasks → open → control activity → upload evidence → submit |
| T-09 | Your first week as a checker | Checker | Compliance | 3:00 | V,S | ✓ | Review queue → evidence → approve/reject/reallocate → comments |
| T-10 | The CCO dashboard | CCO | Dashboards | 2:30 | S | ✓ | Status by department → overdue → drill down → board report |
| T-11 | Board-ready compliance report in one click | CCO/CS | Reports | 1:30 | V | | Select period → generate → PDF/DOCX → share |
| T-12 | What changed? Reading a regulatory update | CCO | Regulatory Change | 2:30 | V,S | ✓ | Update → side-by-side diff → affected actionables → assign impact |
| T-13 | Updates vs notifications | All | Inbox | 1:30 | V | ✓ | Two inboxes → why separate → preferences |
| T-14 | Sync your calendar (Outlook, Google, Apple) | All | Calendar | 2:00 | V | ✓ | Connect M365/Google → ICS for others → what appears |
| T-15 | Assign a task to Vidhi AI | Any | Vidhi AI | 2:00 | V,S | | Ask → draft → review → approve → audit log |
| T-16 | Ask Vidhi about a master direction | Any | Vidhi notebooks | 2:00 | V,S | | Question → cited answer → open source paragraph |
| T-17 | Draft a policy with tracked changes | Policy owner | Policies | 3:00 | S | | Template → Vidhi align with direction → Word redline → approval → upload signed |
| T-18 | Schedule a board meeting and send the agenda | CS | Governance | 3:00 | S | | Meeting → agenda items → notice period check → board pack |
| T-19 | Draft minutes from your notes | CS | Governance | 2:30 | V | | Upload notes/recording transcript → Vidhi draft → SS-1 checks → circulate |
| T-20 | Committees: members, terms of reference and meetings | CS | Governance | 2:30 | S | | Create committee → link HRMS people → meetings → action items |
| T-21 | Maintain statutory registers | CS | Governance | 2:30 | S | | Registers list → auto-updates → export |
| T-22 | Build your risk register | CRO | Risk | 3:00 | S | | Taxonomy → add risk → inherent/residual → controls → KRIs |
| T-23 | The CRO dashboard | CRO | Risk | 2:00 | V | | Heat map (with table) → KRI breaches → appetite |
| T-24 | Run a stress test | CRO/CFO | Risk Lab | 3:30 | S | | Choose scenario → shocks → run → results → export |
| T-25 | Prepare your ICAAP document | CRO/CFO | Risk Lab | 3:30 | S | | Data import → capital → stress → Vidhi draft → board approval |
| T-26 | The CFO ratio dashboard | CFO | Ratios | 2:00 | V | | CRAR, NPA, ALM, leverage → trends → thresholds |
| T-27 | Plan a risk-based internal audit | Internal auditor | Audit | 3:00 | S | | Audit universe → risk score → plan → approval |
| T-28 | Record and close an audit finding | Auditor/Owner | Audit | 2:30 | V | | Finding → rating → management response → closure evidence |
| T-29 | Prepare an upload-ready return | Returns maker | Return Studio | 3:30 | S | | Import Tally/Excel → map → validate → checker → download → attach acknowledgement |
| T-30 | Prepare CIC files for four bureaus | Credit ops | Return Studio | 3:00 | S | | Data → layout per CIC → validation → rejection handling |
| T-31 | Handle a cyber incident (6-hour clock) | CISO | Data & Cyber | 2:30 | V,S | ✓ | Log incident → clocks → CERT-In report draft → regulator |
| T-32 | DPDP notices and consents | DPO | Data & Cyber | 3:00 | S | | Data inventory → notice → consent records → rights requests |
| T-33 | Handle a data-principal request | DPO | Data & Cyber | 2:00 | V | | Request → verify → fulfil → close within timeline |
| T-34 | Labour registers under the new codes | HR admin | HR & Labour | 3:00 | S | | Employee data → registers generated → export |
| T-35 | POSH Internal Committee: setting up and handling a complaint | IC presiding officer | HR & Labour | 3:30 | — | ✓ | IC constitution → sealed case → timelines → annual report (no real case data) |
| T-36 | Issue and eSign an employment agreement | HR admin | HR & Labour | 2:00 | V | | Template → fill → Aadhaar eSign → stored |
| T-37 | Run payroll and leave | Payroll maker/checker | HRMS | 3:30 | S | | Attendance → leave → payroll → checker approval → bank file |
| T-38 | Handle a customer complaint end to end | GRO/Support | Grievance | 3:00 | V,S | ✓ | Ticket → GRO → resolution → escalation → closure → rating |
| T-39 | Add the grievance form to your website | Admin | Grievance/Integrations | 2:00 | V | | Embed code → branding → test |
| T-40 | Download all your data | Admin | Portability | 2:00 | V,S | ✓ | Export scope → folders of Word/Excel/PDF → manifest → BYO storage |
| T-41 | Upload documents with a folder | Any | DMS | 2:00 | V | | Folder upload → mapping preview → dedupe → confirm |
| T-42 | Translate and type-copy a handwritten document | Any | DMS/Vidhi | 2:00 | V,S | | Upload image → OCR → type copy → edit → attach |
| T-43 | Choose and change your plan | Admin | Billing | 2:30 | V | | Plans → add-ons → proration → invoices with GST |
| T-44 | Hire an expert from the marketplace | Admin/Buyer | Marketplace | 2:30 | V,S | | Browse → scope → SLA eSign → pay → track deliverables |
| T-45 | Accessibility settings that make LDC easier to use | All | Accessibility | 2:00 | V,S | ✓ | Text size → contrast → motion → captions → shortcuts → read-aloud |

Production standards: 1920 × 1080 master; brand intro ≤ 3 s; narrator speaks every on-screen action (reduces need for audio description); captions corrected to ≥ 99%; ISL interpreter window bottom-right at ≥ 1/4 frame height where produced; end card with tutorial URL; vertical cuts reframed (not letterboxed) with safe areas; music never louder than −20 LUFS under speech, and a no-music version available.

---

## P.6 SEO / GEO system

### P.6.1 Keyword and question clusters (seed; refresh quarterly with Search Console and the AI answer panel)

| Cluster | Head terms | Long-tail / questions (H2 candidates) | Target page |
|---|---|---|---|
| NBFC compliance | NBFC compliance software; RBI compliance tool for NBFC | Which RBI directions apply to a Base Layer NBFC? · NBFC compliance calendar · NBFC-ICC compliance checklist · Middle Layer NBFC CCO requirements · NBFC returns list | /solutions/nbfc-compliance-software; guides |
| RBI returns | RBI CIMS returns; NBFC supervisory returns | How to file RBI returns on CIMS · NBFC return due dates · XBRL returns RBI · DAKSH vs CIMS vs PRAVAAH | /platform/return-studio; guides |
| CIC reporting | CIC reporting NBFC; CIBIL data submission format | How often must NBFCs report to CICs · CIBIL, CRIF, Experian, Equifax file formats · rejection handling | /platform/return-studio#cic |
| Co-operative societies | credit cooperative society software; society compliance | AGM requirements co-operative society · co-operative society audit · MSCS Act compliance · society election process | /solutions/credit-cooperative-society-software |
| UCB | urban cooperative bank compliance | UCB tier classification · UCB board of management | /solutions/cooperative-bank-compliance |
| SEBI LODR | LODR compliance software; secretarial compliance tool | LODR compliance calendar · Reg 30 disclosure timelines · SDD software for PIT | /solutions/listed-company-compliance |
| AIF/MF | AIF compliance software; mutual fund compliance | AIF Category II compliance checklist · AIF annual reporting | /solutions/fund-compliance |
| IFSCA | IFSCA compliance; GIFT City compliance software | IFSCA finance company compliance · IFSCA fund management compliance | /solutions/ifsca-compliance |
| IRDAI | insurance broker compliance; IRDAI compliance software | IRDAI corporate agent compliance · insurer board committees | /solutions/insurance-compliance |
| Companies Act | ROC compliance software; board meeting software India | Board meeting requirements Companies Act · minutes SS-1 · DIR-3 KYC due date · annual filing due dates | /solutions/company-llp-compliance |
| Risk & ICAAP | ICAAP software India; stress testing NBFC | How to prepare ICAAP · stress testing scenarios for NBFC · Basel Pillar 2 risks | /platform/risk-assessment-lab |
| Data & cyber | DPDP compliance tool; CERT-In compliance | DPDP Rules 2025 timeline · CERT-In 6-hour reporting · SEBI CSCRF compliance | /solutions/data-protection-cyber-compliance |
| Labour & POSH | labour code compliance software; POSH compliance | Labour codes registers · POSH internal committee rules · POSH annual report | /solutions/labour-hr-posh-compliance |
| Accessibility | SEBI accessibility compliance; RPwD website compliance | SEBI digital accessibility circular · accessibility audit IAAP India | /solutions/data-protection-cyber-compliance#accessibility; marketplace |
| Health check | compliance health check; compliance assessment free | Free NBFC compliance checklist · compliance score | /health-check |
| Marketplace | virtual CFO for NBFC; virtual company secretary; ICAAP drafting services | Hire compliance consultant NBFC · retainer compliance services | /marketplace/* |

### P.6.2 Structured data by page type

| Page type | JSON-LD types | Notes |
|---|---|---|
| Home | Organization, WebSite (SearchAction), SoftwareApplication | `sameAs` list; `offers` only if a public starting price exists |
| Solution | WebPage, SoftwareApplication (audience), BreadcrumbList, ItemList (instruments) | `audience` = BusinessAudience with family description |
| Module | WebPage, SoftwareApplication (featureList), BreadcrumbList, VideoObject (if video) | |
| Pricing | WebPage, Product or SoftwareApplication with Offer/AggregateOffer (INR, `priceSpecification` with `valueAddedTaxIncluded` per display), BreadcrumbList | Regenerated on catalogue publish |
| Marketplace service | Service (provider, areaServed IN, offers), BreadcrumbList | Provider is the legal entity; no ratings markup |
| Academy course card | Course (provider FinLegal Academy, `hasCourseInstance` where scheduled) | Canonical points to trainings.lawdocs.in when the course page lives there |
| Regulatory update | NewsArticle (author, reviewedBy, dateModified), `about` → Legislation (legislationIdentifier, legislationDate, legislationPassedBy, legislationJurisdiction "IN") | |
| Glossary term | DefinedTerm (inDefinedTermSet → DefinedTermSet "LawDocsComply Compliance Glossary"), WebPage | `termCode` for abbreviations |
| Guide / article | Article, BreadcrumbList, (HowTo for step guides — kept for non-Google consumers) | |
| Tutorial | VideoObject (transcript, captions via `caption`, `hasPart` Clip chapters), HowTo, BreadcrumbList | |
| Webinar | Event (eventAttendanceMode Online, organizer, offers if paid) | |
| Trust centre | WebPage, Organization (knowsAbout), no certification claims in markup unless held | |
| Health check | WebApplication (free), WebPage | Result and share pages `noindex` |

### P.6.3 Editorial checklist (every page)

1. Title answers a buyer question or names the audience; ≤ 60 characters.
2. First paragraph answers the page's main question in ≤ 60 words.
3. Every H2 section stands alone when extracted.
4. Every regulatory statement cites the instrument and paragraph and shows "Last reviewed".
5. Every number/name/logo is Claims-bound.
6. At least three internal links (glossary, module, solution) and one primary-source external link.
7. Structured data validates; canonical set; hreflang if translated.
8. Images have alt text; video has captions and transcript.
9. Reading level within target; acronyms expanded.
10. Accessibility scan clean; preview approved by checker.

### P.6.4 AI answer panel — 30 fixed prompts (run monthly)

1 best compliance management software for NBFC in India · 2 RBI compliance software for NBFC · 3 how do NBFCs track RBI master directions · 4 NBFC compliance calendar tool · 5 how to file RBI CIMS returns for NBFC · 6 software to prepare CIC data submission for CIBIL CRIF Experian Equifax · 7 credit cooperative society compliance software India · 8 software for urban cooperative bank compliance · 9 SEBI LODR compliance software · 10 board meeting software for Indian companies · 11 secretarial compliance software India · 12 AIF compliance software India · 13 IFSCA GIFT City compliance software · 14 IRDAI compliance software for insurance brokers · 15 ICAAP software for NBFC · 16 stress testing tool for NBFC India · 17 risk management software for NBFC · 18 DPDP Act compliance tool India · 19 CERT-In incident reporting tool · 20 SEBI CSCRF compliance tool · 21 labour code compliance software India · 22 POSH compliance software India · 23 regulatory change management software India · 24 compliance health check free India · 25 Lawrbit alternatives · 26 TeamLease RegTech alternatives · 27 Komrisk alternatives · 28 GRC software for Indian financial services · 29 virtual compliance officer for NBFC · 30 what is LawDocsComply.

Record per engine: AI answer shown (Y/N), LawDocsComply named (Y/N), LawDocsComply page cited (URL), competitors named, sources cited. Report "named" and "cited" separately; trend over 90 days before acting.

## P.7 Copy deck additions for v1.1 *(v1.1)*

All copy is claims-gated (NN-19); bracketed items are filled from registries at render time.

| Page | Headline | Sub-headline | Three proof bullets (only with evidence) |
|---|---|---|---|
| `/legal-matters-and-contracts` | Every case, notice and contract — one register, no missed dates | Track litigation, regulator inspections, notices, contracts and licences with limitation and hearing calendars your board can trust | Hearing and limitation reminders; Reg 30 disclosure prompts for listed companies; contract renewal alerts before notice dates |
| `/esg-brsr` | BRSR without the spreadsheet chase | Collect ESG data once, calculate emissions with versioned factors, and draft your BRSR for review | Data requests with evidence; GHG Scope 1–2 with factor library versions; BRSR XBRL-ready output |
| `/ai-governance` | Govern your AI before your regulator asks | Inventory AI systems, assess risk, record validations and incidents against FREE-AI, MeitY guidelines, the EU AI Act and ISO/IEC 42001 | AI system register; impact assessments; board AI report |
| `/global-entity-management` | Your group, every country, one calendar | Foreign subsidiaries, officers, registers and filings with local packs reviewed by named local firms | Coverage statements per country; home-region data residency; local experts on call |
| `/reports-and-board-packs` | Board packs in minutes, numbers you can re-run | One-page summaries, MIS packs and board packs from a governed data snapshot | Re-run "as at" any date; maker-checker on reports; DOCX/PPTX/PDF |
| `/vidhi-ai-agents` | An AI team that prepares — your people approve | Hire role agents like a Returns Preparer or Board Pack agent, set their autonomy, and see every draft before it counts | Agents propose, humans approve; kill switch per agent; India-region AI for your data |
| `/connect-your-ai-assistant` | Ask LawDocsComply from Copilot, Claude or ChatGPT | Connect your company's AI assistant to see what's due and what changed — only what you can see, nothing it can approve | Admin-approved connection; sealed data never shared; every access logged |
| `/<market>/` (market home) | Compliance for [market] entities of Indian groups — and for [market] companies | [Coverage line from pack registry] | [Published pack count]; [partner firms]; [data residency option] |

**Global group positioning line:** "From Mumbai to Dubai to Singapore: one compliance system for your whole group — with each entity's data kept in its own region."

## P.8 Global health-check question bank v1.0 (20 questions) *(v1.1)*

Weights as §P.3.2. Jurisdiction-specific citations come only from PUBLISHED packs; otherwise the generic wording applies and the report is labelled generic (NN-53).

| Code | W | Question (generic wording) | Segment |
|---|---|---|---|
| G-01 | 3 | Has the entity filed its most recent annual return / confirmation statement with the company registry on time? | Corporate |
| G-02 | 3 | Are the registered office and (where required) registered agent details current with the registry? | Corporate |
| G-03 | 3 | Is the beneficial-ownership / registrable-controller register maintained and filed where required? | Corporate |
| G-04 | 2 | Are statutory registers (members, directors/officers, charges) up to date? | Corporate |
| G-05 | 2 | Were board meetings and shareholder approvals held and minuted as the local law and articles require? | Governance |
| G-06 | 3 | Have audited financial statements been prepared and filed within the local deadline (where audit is required)? | Finance |
| G-07 | 3 | Are corporate-tax returns filed and taxes paid on time? | Tax |
| G-08 | 3 | Is the entity registered for VAT/GST where thresholds are met, and are returns current? | Tax |
| G-09 | 2 | Is transfer-pricing documentation prepared for transactions with group companies? | Tax |
| G-10 | 3 | Where economic-substance rules apply, has the notification/report been filed? | Tax / Corporate |
| G-11 | 3 | Are payroll taxes and social-security contributions registered and paid for all employees? | People |
| G-12 | 2 | Are employment contracts and mandatory workplace registrations in place? | People |
| G-13 | 3 | Does the entity hold every licence/permit its activities need, with renewals tracked? | Licences |
| G-14 | 3 | Is the entity compliant with the local data-protection law (registration, notices, transfer mechanisms)? | Data |
| G-15 | 2 | Are records kept for the locally required retention period? | Records |
| G-16 | 3 | Where the entity is in a regulated sector, are AML/CFT registrations and reporting in place? | AML |
| G-17 | 2 | Are sanctions screening controls applied to customers and counterparties? | AML |
| G-18 | 3 | (Indian parent) Has the Indian parent completed ODI reporting for this investment (e.g., annual performance report) with its AD bank? [VERIFY current FEMA ODI forms] | India link |
| G-19 | 2 | (Indian parent) Are related-party approvals and disclosures for transactions with this subsidiary in place? | India link |
| G-20 | 1 | Is there a named person responsible for local compliance with a calendar of filings? | Governance |

## P.9 Tutorials added in v1.1 (T-45–T-62) *(v1.1)*

| ID | Title | Role | Module | Len | Cuts | ISL | Script outline |
|---|---|---|---|---|---|---|---|
| T-45 | Meet your Vidhi agent team | Admin/CCO | Vidhi agents | 2:30 | V,S,W | ✓ | Roster → hire an agent → sponsor → autonomy → first mission |
| T-46 | Set an agent's autonomy level | Admin | Vidhi agents | 2:00 | V | | L0–L4 explained → per-skill setting → kill switch |
| T-47 | Review what an agent prepared | Checker | Vidhi agents | 1:30 | V | ✓ | Work Inbox → agent draft → evidence → approve/return |
| T-48 | Connect Copilot / Claude / ChatGPT to LawDocsComply | Admin | MCP | 2:30 | S | | Enable → approve client → user consent → ask "what's due" |
| T-49 | Add a foreign subsidiary | Admin/CS | Global entities | 2:30 | V,S | | Entity wizard → registry look-up → home region → pack |
| T-50 | Read a coverage statement | CCO | Global packs | 1:30 | V | | Authorities → instruments → reviewer → freshness |
| T-51 | Ask a local expert | CS/CCO | Partner query desk | 1:30 | V | | From checkpoint → question draft → answer as expert note |
| T-52 | Log a court case and never miss a hearing | Legal | Legal matters | 2:30 | V,S | ✓ | New matter → hearing dates → tasks → board report |
| T-53 | Track regulator inspection observations | CCO | Legal matters | 2:00 | S | | Inspection → observations → owners → closure evidence |
| T-54 | Catch contract renewals before notice dates | Legal/Finance | Contracts | 1:30 | V | | Import contracts → obligations → renewal alerts |
| T-55 | Collect ESG data for BRSR | Sustainability | ESG | 2:30 | S | | Data requests → evidence → validations |
| T-56 | Calculate Scope 1 and 2 emissions | Sustainability | ESG | 2:30 | S | | Activity data → factor library version → results → lineage |
| T-57 | Draft your BRSR for review | CS/Sustainability | ESG | 2:00 | V | | Workbook → Vidhi narrative draft (no figures) → review → XBRL |
| T-58 | Register your AI systems | AIO/CRO | AI governance | 2:00 | S | ✓ | Register → classify → owner → assessment |
| T-59 | Build a one-page compliance summary | CCO | Reports | 1:00 | V | ✓ | Choose entity/period → generate → share |
| T-60 | Create a board pack in minutes | CS | Reports/Board | 2:00 | V,S | | Template → auto MIS → freeze & hash → circulate |
| T-61 | Re-run a report "as at" a past date | CFO/Auditor | Reports | 1:30 | V | | Run history → re-run → identical figures |
| T-62 | See who accessed your data | Admin/DPO | Access transparency | 1:30 | V | ✓ | Transparency page → filters → alerts |

## P.10 SEO / GEO additions for global and new modules *(v1.1)*

**Keyword and question clusters (seed):** UAE company compliance calendar for Indian groups · ODI annual performance report reminder software · economic substance filing tracker UAE · Singapore annual return ACRA reminder · global entity management software India · subsidiary governance software · BRSR software India · BRSR Core data collection tool · GHG scope 1 2 calculator India · litigation management software NBFC · regulator inspection observations tracker · contract renewal tracker India · AI governance software India FREE-AI · ISO 42001 readiness tool · connect Copilot to compliance software (MCP).

**Structured data:** `SoftwareApplication` with `areaServed` per market page; `Service` for partner services with `areaServed` and `provider` (organisations only, never individual professionals where rules restrict); `FAQPage` markup kept for answer engines even though Google FAQ rich results ended (May 2026); `Dataset` not used for regulatory content.

**AI answer panel additions:** add prompts 31–40 (e.g., "best global entity management software for Indian companies", "BRSR software India", "AI governance tool for NBFC FREE-AI", "how to track UAE economic substance deadlines") to the monthly run (§P.6.4).
