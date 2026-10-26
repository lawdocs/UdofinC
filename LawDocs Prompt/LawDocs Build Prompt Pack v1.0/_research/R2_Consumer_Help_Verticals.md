# R2: Consumer-Help Verticals (Loan Grievances and Debt Help, Insurance Claims, Traffic Challans, Vehicle Transactions)

**Stream:** R2, research input for the LawDocs build-prompt pack
**Prepared:** 25 October 2026
**Scope:** Consumer-help verticals that will run under a **separate brand and legal entity** on the LawDocs platform, with an ethical wall from the group's lender-facing products (Finbyx, Udofin, LawDocsComply). Source: Owner Brief, 25 Oct 2026, para 89–90.
**Conventions:** `[VERIFY]` marks any fact not confirmed against a first-party or official source in this session. Citations appear as (Sn), which refer to the numbered source list in Section 8. All sources were accessed on 25 Oct 2026.

**Research limitations (read first)**

- The session's web-search budget ran out before vehicle-loan foreclosure, OLX Autos and stamp-duty searches could run. Those sections rely on sources already fetched plus analyst knowledge, and are marked `[VERIFY]`.
- Five sites refused or failed automated fetch: claimbuddy.in (robots), finchannel.com (robots), ibsintelligence.com (error), the parivahan.gov.in data-sharing policy PDF (robots), and the RBI compromise-settlement framework PDF (bot-check). Facts on these come from search snippets or secondary reports, as noted at each point. No bypass was attempted.
- No live site or press coverage for **"ChallanWallah"** could be found. The likely intended comparators are **ChallanPay (by Lawyered)** and **Challan Sathi**, and both are covered below. `[VERIFY]` the brand name with the owner.

---

## 0. Executive summary: ten decisions for the build prompt

1. **Advocates cannot represent complainants before the RBI Ombudsman.** Under RB-IOS 2026 (in force 1 July 2026), a complaint may be filed through an authorised representative "other than an advocate", unless the advocate is the aggrieved person (Cl. 3(1)(c), 10(1)(b)) (S1, S2). The banking-grievance workflow must therefore be **self-filed by the user with LawDocs drafting**, or filed by a **non-advocate case manager** holding a written authorisation. Advocates on the panel must not file.
2. **The insurance ombudsman route is different.** Rule 14(1) lets the insured file "himself or through his legal heirs, nominee or assignee" (S8). The Karnataka High Court (DB, 1 July 2026) held that a complainant may engage an advocate once the matter moves from mediation to adjudication under Rule 17 (S10). Outside Karnataka, treat this as persuasive only. `[VERIFY]` whether the Council for Insurance Ombudsmen has issued guidance.
3. **Consumer commissions:** non-advocate agents may appear only under the 2014 agent regulations, on a "duly authenticated authorisation" from the party. Authority letters issued by advocates to non-advocates were barred by the Delhi HC in *Anuj Kumar Chauhan* (Dec 2024) (S14).
4. **Success fees.** Advocates cannot charge contingency or success fees (BCI Rules, Part VI Ch. II Sec. II, Rules 20–21) (S27). Non-advocate claim consultants do charge them. Insurance Samadhan charges ₹999 to register, then **20% + GST** of the amount recovered (22% at the "legal level"), plus withdrawal charges (S5). The recommended structure: the consumer-help entity, a non-advocate, earns any success-linked fee for non-legal case management. Panel advocates are paid **fixed fees** only, through a separate invoice. They must never share in the success fee.
5. **Do not pool or hold borrowers' settlement money.** Debt-settlement firms are unregulated. FREED itself says no settlement company can truthfully claim RBI registration (S20). On 4 May 2026, RBI **reiterated** its caution against entities that promise loan waivers or issue "debt waiver certificates" for a fee (S19). LawDocs must never market a "waiver" or "settlement guarantee". It must never collect funds meant for lenders. `[VERIFY]` exposure under the Banning of Unregulated Deposit Schemes Act, 2019 if funds are pooled.
6. **New recovery-conduct rules start 1 January 2027.** These are the RBC Fourth Amendment Directions for commercial banks and the Third Amendment Directions for NBFCs, both dated 6 Aug 2026. They set calling hours of 08:00–19:00, require an IIBF certificate for agents, and require agency details to reach the borrower at least one day before the first visit (S11, S12). These rules supply the evidence checklist for the harassment module.
7. **No official third-party e-challan API.** MoRTH told an RTI applicant that only **government organisations** have API access to vehicle data. The 2019 bulk-data policy was scrapped in 2020 (S33). Private challan APIs such as Surepass do not name their data source (S31). **Recommended:** a user-initiated lookup that sends the user to the official portal, or parses a challan SMS or PDF the user uploads, or uses a DigiLocker pull for RC/DL `[VERIFY]`. Do not scrape.
8. **Do not collect challan fines into a LawDocs account.** Doing so is likely to make LawDocs a payment aggregator or intermediary for government receipts `[VERIFY]`. Fines go to e-Treasury through the court or state gateway (S29). The user pays on the official gateway, and LawDocs charges only its own service fee. Park+ is the benchmark: ₹199 legal fee for an online challan and ₹1,999 for a court challan (S28).
9. **Vehicle sale is a document-and-deadline product, and fits LawDocs' core.** It needs a sale agreement, a delivery note time-stamped to the hour, Forms 29/30 (Form 28 if interstate, Form 35 if hypothecated), an RC transfer application within 14 days (same state) or 45 days (other state), and challan, blacklist and hypothecation checks before sale (S35, S36). Stamp duty on vehicle sale agreements varies by state and must be driven by the rule engine `[VERIFY]`.
10. **Ethical wall (structural).** Use a separate company, separate tenant and database, and separate staff and advocates. Run a one-way, hashed conflict check against the lender-client lists of Finbyx, Udofin and LawDocsComply. Never use lender-side data in consumer cases, or consumer data in lender products. DPDP purpose limitation and the confidentiality clauses in outsourcing agreements both require this.

---

## 1. Vertical A: Loan and lending grievances and debt help

### 1(a) Competitor teardown

| Player | Legal entity / status | Core model | Fees (as published) | Harassment / legal features | Notes and red flags |
|---|---|---|---|---|---|
| **FREED** (freed.care) | FREED India Pvt Ltd, Gurugram (S3, S20) | Unsecured-debt programmes: "Settle My Loans" (settlement), "Reduce My EMI" (consolidation), "Improve Credit Score", "EMI Score" (free), and **"FREED Shield / Stop Harassment"** (S3, S4) | No public rate card. FAQ: "costs will vary depending on the program". Blog: "fees only on successful settlement, not upfront" (S3, S4, S20). A syndicated article describes a savings corpus held in a "special purpose account managed by a trusteeship firm" (S21) `[VERIFY]` | Counsellors help prepare complaints. FREED handles the paperwork and lender conversation for settlement (S4) | Does not handle secured loans such as home, car or gold (S4). Self-reported numbers conflict: 60k vs 75k customers, "20 lakh+ counselled" (S3). Settlement takes 12–36 months and harms the credit score (S21) |
| **SingleDebt** | City Credit Management LLP (LLPIN AAN-6607), Mumbai (S22) | Debt Management Plan: one consolidated monthly payment, plus settlement, MSME business debt, and a free counselling tie-up (SOS with Mann Talks) | Free first consultation. "Enroll Today for ₹599" (scope not stated). Further fees only after the plan is approved (S22) | "In-house advocates" negotiate and reply to legal notices. After enrolment it sends notices to creditors redirecting communications to SingleDebt (S22) | Legal advice offered by an LLP that is not a law firm is a Bar-rule and Advocates Act risk `[VERIFY]` |
| **Settle Loan** (settleloan.in) | No legal entity disclosed (S23) | Settlement for personal loans, cards, home, vehicle and education loans. OTS guidance. Credit builder | Fees "outlined" in the enrolment contract and not published (S23) | Members may forward lender calls to the Settle Loan team. "Legal advisors" negotiate (S23) | No entity disclosure. Warns users to pay only through official links (S23) |
| **CredSettle, SettleMyLoan, Debt Relief India, Debtkart, CreditQ** | Various | Settlement and anti-harassment | Generic market fee models (from a CredSettle-hosted article): monthly retainer ~₹500–2,000, upfront 1–3% of enrolled debt, success fee ~10–15% of the amount saved (S24) `[VERIFY]` | "24/7 anti-harassment", legal notices to banks (S24, S25) | Comparison pages come from interested parties (S24, S25) |
| **AMA Legal Solutions** | Advocate-led firm (S26) | Loan settlement by advocates | Not published | Advocates negotiate | Advocate firm marketing settlement online is a Rule 36 advertising exposure (see §5) |

**Market observations**
- The category has no RBI licence, registration or code of conduct. FREED states this itself (S20).
- RBI has twice warned against fee-charging "loan waiver" campaigns: on 11 Dec 2023 (S18) and again on **4 May 2026** (S19). The 2026 notice covers "debt waiver certificates" and "fee collection under various pretexts".
- Customer complaints about non-refund are visible on consumer-complaint sites for FREED and SingleDebt (search results only) `[VERIFY]`. Refund terms and fee transparency are where competitors are weak.
- Product gap: none of the players examined turn the harassment evidence and RB-IOS escalation into a self-serve legal workflow. Their model is "hand everything to us". LawDocs can be the **documented, user-controlled** alternative.

### 1(b) Official process maps

**A. RBI-regulated lender grievance ladder (banks, NBFCs, PPI issuers, CICs)**

| Step | Forum | Eligibility / trigger | Timeline | Authority |
|---|---|---|---|---|
| 1 | RE's grievance redressal officer or nodal officer (for digital loans, the RE/LSP nodal grievance officer named on the DLA and in the KFS) | Any deficiency in service | Respond within 30 days (DL Directions para 11) | DL Directions 2025, para 11 (S13) |
| 2 | **Internal Ombudsman** (auto-escalation; the customer does not file) | Complaint rejected in full or part by the RE | IO gets at least 10 days where an RBI, NPCI or card-network TAT applies, otherwise 20 days. Final reply to the customer within 30 days of receipt | RBI Internal Ombudsman Directions, 2026, announced 14 Jan 2026 (S16). Covers banks with 10+ outlets, deposit-taking NBFCs with 10+ branches, NDSI NBFCs ≥ ₹5,000 cr with customer interface, SFBs, payments banks, PPIs, CICs (S16). Effective date `[VERIFY]` |
| 3 | **RBI Ombudsman under RB-IOS 2026** via **cms.rbi.org.in**, crpc@rbi.org.in, or post to CRPC, RBI, Central Vista, Sector 17, Chandigarh 160017 | Complaint first made to the RE. No reply in 30 days (or a longer RBI/NPCI/card-network TAT), or unsatisfactory reply. Complaint to the RE made within limitation. Not pending or decided elsewhere (Cl. 10(1)(a)–(l)) | File **within 90 days** after the reply period expires or after the RE's last communication, whichever is later (Cl. 10(1)(g)). RE responds within 15 days (Cl. 14(2)) | RB-IOS 2026, issued 16 Jan 2026, effective **1 July 2026**. Repeals RB-IOS 2021 (Cl. 1(2), 20(1)) (S1, S2) |
| 4 | Award → acceptance → compliance | — | Complainant accepts within 30 days of receiving the award or it lapses (Cl. 15(4)). RE complies or appeals within 30 days of acceptance (Cl. 15(5)) | (S2) |
| 5 | Appellate Authority (ED in charge, CEPD) | Appeal against an award only | Complainant: 30 days from the award, extendable by 30 days (Cl. 17(3)). RE: 30 days from acceptance, extendable by 30 days | (S1, S2) |
| 6 | Civil court / DRT / consumer commission / police (for criminal intimidation) | If dissatisfied, or where the matter falls outside the Scheme | Limitation Act. Consumer Protection Act s.69: 2 years `[VERIFY]` | — |

**RB-IOS 2026 facts the product must encode**
- **Covered REs (Cl. 1(3)):** commercial banks, RRBs, state and central co-operative banks, scheduled UCBs, non-scheduled UCBs with deposits ≥ ₹50 cr; NBFCs that take deposits, or have a customer interface **and** assets ≥ ₹100 cr (excluding HFCs, CICs-as-core-investment-companies, IDF-NBFCs, NBFC-IFCs, NOFHCs, PDs, mortgage guarantee cos.); non-bank PPI issuers; **credit information companies** (S1, S2). *Product rule:* an NBFC below ₹100 cr assets without deposits is **out of scope**. Route those users to the NBFC's grievance officer, then RBI CEPD/CMS for general complaints, then a consumer commission `[VERIFY]` the residual route.
- **Compensation:** no cap on the disputed amount. Up to **₹30 lakh** for consequential loss, plus up to **₹3 lakh** for loss of time, expenses, harassment or mental anguish (Cl. 8(3)) (S1, S2).
- **Representation:** in person or through an authorised representative other than an advocate, appointed in writing (Cl. 3(1)(c), 10(1)(b)) (S1, S2).
- **Excluded:** commercial judgment, vendor disputes, management grievances, actions under legal orders, employer–employee disputes, **CICRA s.18 matters** (Cl. 10(2)) (S1). Criminal or police proceedings do **not** count as "the same grievance" (S1).
- **Language:** CMS accepts Hindi and English. Email and post accept any language (S1). Contact centre **14448** gives information only and cannot take complaints (S1).
- **Transition:** complaints received before 1 July 2026 stay under RB-IOS 2021 (S1).

**B. Recovery-agent harassment**

| Rule | Banks | NBFCs | Source |
|---|---|---|---|
| Calling and visiting hours | 08:00–19:00, unless the borrower expressly authorises otherwise | 08:00–19:00 (para 100). **Microfinance: 09:00–18:00 (para 91)** | S11; S12; S15 `[VERIFY para nos. against RBI text]` |
| Prohibited conduct | Abuse, threats, public shaming, posting borrower details on social media, false statements about the debt | Same, plus harassing relatives, friends or co-workers, and anonymous or excessive calls | S11, S12 |
| Identification | ID card, authorisation letter, copy of the bank's notice | ID card, authorisation, notice, with agency and grievance-officer contacts | S11, S12 |
| Agent certification | IIBF Debt Recovery Agent certificate | Same; existing agents get one year from 1 Jan 2027 | S11, S12 |
| Advance disclosure | Agency details at least 1 day before the first in-person visit. Website list updated within 7 days | Same | S11, S12 |
| Call records | Recorded and kept 6 months (longer if sub judice) | `[VERIFY]` | S11, S17 |
| No referral while a grievance is open | Draft: a case cannot go to an agency while a related grievance is unresolved | `[VERIFY]` final text | S17 |
| Digital loans | Agent particulars emailed or SMSed to the borrower **before** contact (DL Directions para 8(v)) | Same | S13 |
| Effective | **1 Jan 2027** (Fourth Amendment, 6 Aug 2026, RBI/2026-27/223) | **1 Jan 2027** (Third Amendment, 6 Aug 2026) | S11, S12 |

Criminal overlay: threatening arrest over an unsecured civil debt may amount to criminal intimidation under BNS 2023 s.351 (cited by FREED, S4) `[VERIFY]`. Recording a call one is party to is generally permissible as evidence (S4) `[VERIFY]` the admissibility requirements under BSA 2023 s.63 certificate.

**C. Illegal and unregistered loan apps**
- The RE must report every DLA on RBI's **CIMS**, certified by the CCO. RBI publishes this data automatically **without verifying it** (DL Directions para 17, Annex I; deadline 15 June 2025) (S13). *Product rule:* the "Is my lender legit?" check looks up the RBI-published DLA list and the RE's registration. It must show the disclaimer that inclusion is not RBI endorsement.
- DLAs may not access files, media, contacts, call logs or telephony. Camera, microphone and location are allowed once only, for KYC (para 12) (S13). Contact-list harassment is therefore evidence of a breach.
- Disbursal must go only into the borrower's account, and LSP fees cannot be charged to the borrower (para 9) (S13).
- Where to report unregulated lenders: RBI **Sachet** portal (sachet.rbi.org.in) for unauthorised entities `[VERIFY URL behaviour]`. National Cyber Crime Reporting Portal / 1930 for extortion or morphing `[VERIFY]`. The local police. RBI's December 2023 and May 2026 cautions direct the public to law-enforcement agencies (S18, S19).

**D. Settlement and foreclosure (borrower-side facts)**
- Compromise settlements by REs need a board-approved policy (RBI Framework for Compromise Settlements and Technical Write-offs, 8 June 2023). A cooling period applies before fresh credit, and settled accounts are reported to CICs as "settled" (S38, fetched only through a search snippet) `[VERIFY all]`. The borrower has **no right** to a settlement. Product copy must never imply one.
- After full repayment, the NBFC must release original documents and remove registered charges within **30 days**. It pays **₹5,000/day** for delay attributable to it (NBFC RBC Directions 2025, paras 35–41) (S15). `[VERIFY]` that this expressly covers vehicle hypothecation NOC and Form 35.
- Prepayment charges: none on floating-rate loans to individuals for non-business purposes sanctioned or renewed on or after 1 Jan 2026 (NBFC RBC Directions para 34) (S15) `[VERIFY]`.

**E. Credit-report disputes (CIBIL, Experian, Equifax, CRIF High Mark)**

| Step | Rule | Source |
|---|---|---|
| Dispute raised with the CIC (online) or the credit institution | — | S39 |
| CI sends the correction to the CIC | Within **21 calendar days** | RBI/2023-24/72, 26 Oct 2023, para 2(b) (S40) |
| CIC resolves | Within the remaining **9 days**, total **30 calendar days** from filing (para 2(a), (c)) | S39, S40 |
| Compensation | **₹100 per calendar day** beyond 30 days, apportioned between CI and CIC, credited automatically within 5 working days of resolution to the account given at filing (para 2(a), (e), (k)). Effective 26 Apr 2024 | S39, S40 |
| Rejection | Reasons must be given (para 2(d)) | S40 |
| Escalation | RBI Ombudsman (CICs are covered REs under RB-IOS 2026), except matters under CICRA s.18 | S1, S40 |

### 1(c) Recommended LawDocs workflow (consumer-help entity, "Vertical A")

**Case stages (state machine; each state shows a status chip and a "Waiting on…" owner)**
`INTAKE → TRIAGE → EVIDENCE → RE_COMPLAINT_SENT → (wait 30d) → [IO_AUTO] → RBIO_READY → RBIO_FILED → RBIO_RESPONSE → SETTLED | AWARD | REJECTED → APPEAL_WINDOW (30d) → CONSUMER_COMMISSION / COURT (referral) → CLOSED`.
Parallel tracks: `HARASSMENT_LOG`, `POLICE_COMPLAINT`, `CREDIT_REPORT_DISPUTE`, `SETTLEMENT_NEGOTIATION`.

**Triage rules (rule-engine data, not code)**
1. Is the lender an RE? Check the RBI NBFC list or the DLA directory. If it is unregistered, go to the illegal-app track (Sachet, cyber cell, police) and offer no RB-IOS route.
2. Is the RE in RB-IOS scope? Apply the Cl. 1(3) thresholds. If the user cannot tell, show "unknown – file anyway; the RBI system validates" and record the uncertainty.
3. Limitation clock: start the 30-day wait when the RE acknowledges receipt. Fix the 90-day RBIO window from the later of reply-expiry or last communication.
4. Duplicate check: is anything pending in a court, DRT, consumer commission or arbitration? If yes, RBIO is not maintainable (Cl. 10(1)(h)–(k)).
5. Harassment severity: threats, violence or morphing trigger the police and cyber track immediately and in parallel.

**Documents to collect**
Loan agreement, sanction letter and KFS. Repayment statement and EMI proofs. NOC (if closed). Recovery call logs, recordings and screenshots, auto-timestamped by an in-app evidence locker with hash and time, and exportable with a BSA s.63 certificate template `[VERIFY form]`. Agent name, ID and agency. Prior complaints with acknowledgements. Credit report (PDF). ID proof. A **written authorisation** for a non-advocate representative (if used).

**Letters and templates (Vidhi AI drafts; the user edits and sends)**
- T-A1 Complaint to the RE's grievance or nodal officer, citing the specific direction breached.
- T-A2 Recovery-conduct breach notice, citing 08:00–19:00, IIBF certification, ID and authorisation, 1-day prior agency disclosure, and a request for the call recordings the RE must keep.
- T-A3 RB-IOS 2026 complaint pack, pre-structured to the CMS fields, with a relief computation that shows the ₹30 lakh and ₹3 lakh heads separately.
- T-A4 Authorisation letter in favour of a **non-advocate** representative (Cl. 3(1)(c)).
- T-A5 CIC dispute letter plus a tracker for ₹100/day compensation.
- T-A6 Settlement proposal letter. Disclaimers: no guarantee, credit impact, the lender's discretion.
- T-A7 Police and cyber complaint (criminal intimidation, extortion, morphing).
- T-A8 Request for release of documents and charge satisfaction after closure (the 30-day / ₹5,000-per-day rule).
- T-A9 Consumer-commission complaint draft (referral to a panel advocate, fixed fee).

**User vs LawDocs responsibilities**

| Task | User | LawDocs consumer-help entity (non-advocate staff) | Panel advocate (separate engagement) |
|---|---|---|---|
| Sign and send RE complaint | ✔ (or authorise) | Draft, track deadlines | — |
| File RB-IOS complaint | ✔ self-file (recommended) | May file as an authorised **non-advocate** representative with written authority | **✘ barred** (Cl. 10(1)(b)) |
| Speak to lender / negotiate settlement | ✔ | Through a written authority. No promises of waiver | Advise for a fixed fee |
| Hold settlement corpus | In the user's own bank account or RD | **✘ never** | ✘ |
| Police complaint | ✔ files | Draft | Advise |
| Consumer commission / court | — | Refer only | Appears on vakalatnama, fixed fee |

**Escalation ladder (UI ribbon):** RE GRO → (auto) Internal Ombudsman → RBI Ombudsman (CMS) → Appellate Authority → Consumer Commission / Civil Court / DRT → police and cyber (parallel, for criminal conduct).

### 1(d) Revenue options and legality

| Option | Description | Legality note |
|---|---|---|
| Freemium DIY | Free triage and templates. ₹199–₹499 per premium pack (RB-IOS pack, harassment pack) | Low risk. Document drafting without representation `[VERIFY]` the Advocates Act s.33 "practise" boundary. Keep it as a document service with user filing |
| Case-management subscription | ₹299–₹999/month for deadline tracking, evidence locker, case manager chat | Low–medium. Must not be marketed as legal representation |
| Success fee (non-advocate entity) | e.g., 10–15% of amounts recovered as RBIO compensation or refunds | Medium. Not barred for non-advocates, but champerty and unconscionability challenges are possible (§5). Advocates must not share in it (BCI Rules 20–21). Cap it, disclose in a KFS-style fee sheet, refund on withdrawal per a published scale |
| Fixed-fee advocate consults and notices | Marketplace (₹999 notice, ₹1,999 consult) | Fees set by the advocate. The platform fee must not be a share of legal fees in a way that breaches advocate rules `[VERIFY]` (see R-marketplace stream) |
| Settlement fee on savings | % of the amount "saved" | **High risk.** Draws the RBI-caution pattern (S19) and misleading-advertising risk. If offered at all, charge only after the lender's settlement letter is issued, and never take custody of funds |
| Lead fees from lenders | — | **Prohibited by design.** Direct conflict of interest under the ethical wall |

### 1(e) Risk register: Vertical A

| # | Risk | L | I | Mitigation |
|---|---|---|---|---|
| A1 | An advocate files or represents before RBIO, so the complaint is non-maintainable and a misconduct risk | M | H | Role-based block: advocate profiles cannot be added as "representative" on an RBIO case |
| A2 | Marketing implies "loan waiver" or "stop EMIs", hitting the RBI caution (May 2026) | M | H | Banned-phrase list in the CMS and ad copy. Legal review gate. Mandatory credit-impact disclaimer |
| A3 | Custody of borrower funds (BUDS Act, PSS Act) | L | Critical | Architecture: no wallet and no pooled account. Settlement payment goes directly to the lender |
| A4 | Conflict: the opposite party is a Finbyx, Udofin or LawDocsComply client | H | H | Separate entity. Hashed conflict check. Disclosure to the user. Staff segregation. No data flows. Board COI policy |
| A5 | Missed 90-day RBIO window | M | M | Deadline engine with T-15, T-7, T-1 alerts. Computes the "later of" date |
| A6 | Evidence inadmissible (unsigned or unhashed recordings) | M | M | Hash at capture. BSA s.63 certificate template `[VERIFY]` |
| A7 | Unauthorised practice of law by case managers | M | H | Scripts limited to procedural assistance. Legal opinions only by panel advocates |
| A8 | Rule change (RB-IOS 2026 replaced 2021; Internal Ombudsman 2026; RBC amendments 2027) | H | M | Rules held as versioned data with effective-from dates. Ops can edit without a code release |
| A9 | Refund disputes (a competitor weakness) | M | M | Published withdrawal scale. Pro-rata refunds. Auto-generated invoice and credit note |

---

## 2. Vertical B: Insurance claims and grievances

### 2(a) Competitor teardown

| Player | Model | Fees | Regulatory disclosure | Notes |
|---|---|---|---|---|
| **Insurance Samadhan** (Noida; app "Polifyx") | Policyholder complaints: mis-selling, rejection, delay, short settlement, reimbursement filing, "Know Your Policy". Escalates GRO → Bima Bharosa → Ombudsman (up to ₹50 lakh) → consumer court (S5) | ₹999 one-time registration (whether GST is included is unclear). **Success fee 20% + GST** of amount received at company or ombudsman level, **22% + GST** at legal level. ₹799 reimbursement filing. Withdrawal charges 10% / 15% / 15% + GST, or the full success fee if already resolved (S5). In 2020 the fees were ₹500 and 9% (S6) | The site does not state IRDAI status or name a legal entity, and has no advocate disclaimer (S5) | Selective intake: in 2020 it accepted "3–4 cases out of 100" and resolved ~90% at insurer level (S6). Raised seed and pre-Series A funding (search results) |
| **ClaimBuddy** (Gurugram) | Health-claim assistance for patients **and hospitals**: cashless and reimbursement processing. 250+ partner hospitals, 35k+ patients, ₹500 cr+ claims processed (2024) (S7) | Not published (site blocked automated fetch) `[VERIFY]` | IRDAI status not stated in coverage `[VERIFY]` (corporate-agent or TPA-adjacent?) | Mostly B2B2C through hospitals. Series A $5 m led by Bharat Innovation Fund (S7) |
| **Policybazaar claim assistance, broker-led help desks** | Claim support bundled with policy sale | Free to the customer, paid through commission | IRDAI-registered broker | Conflict: the broker is paid by insurers `[VERIFY]` |
| **Bima Bharosa** (IRDAI) | Official grievance portal. Insurer CMS integrated (S9) | Free | Regulator | Toll-free 155255 / 1800-4254-732. complaints@irdai.gov.in. 12 languages (S9) |

**Observation:** IRDAI regulation and public notices found in this session concern **unregistered sellers of insurance** and impostor Bima Bharosa sites (search results). No IRDAI regulation of post-sale claim consultants was found `[VERIFY]`. Two boundaries apply. First, a claim-help entity must not solicit or procure insurance business (that needs registration as agent or broker). Second, a business that also earns insurer commissions while acting "for" the policyholder has a conflict. "Insurance consultant" as an intermediary category under the Insurance Act `[VERIFY current s.2 / s.42D wording]`.

### 2(b) Official process maps

| Step | Forum | Eligibility | Timeline | Source |
|---|---|---|---|---|
| 1 | Insurer GRO / complaints cell (logged in insurer CMS linked to Bima Bharosa) | Any grievance | Acknowledge immediately. Seek details within 7 days. **Resolve within 14 days**, with reasons if rejected | IRDAI PPHI Regs 2024 and Master Circular, 5 Sep 2024 (S41); IANS 14 Aug 2026 (S9) |
| 2 | IRDAI (Bima Bharosa / PP&GR Dept.) | No response within a reasonable time, or dissatisfied | Not defined (S9) | S9 |
| 3 | **Insurance Ombudsman** (cioins.co.in online; email; walk-in) | Written representation to the insurer first. No reply in **one month**, or rejection / unsatisfactory reply (R.14(3)(a)). File **within one year** (R.14(3)(b)); delay condonable (R.14(4)). Not pending or decided before a court, consumer forum or arbitrator (R.14(5)). Filed by the complainant or through legal heirs, nominee or assignee (R.14(1)) | Mediation recommendation within 1 month of mutual consent. Acceptance within 15 days. Insurer compliance within 15 days (R.16). Award within **3 months** of receiving all requirements (R.17(4)). Insurer complies within **30 days** (R.17(6)). Late compliance: ₹5,000/day to the complainant (PPHI Master Circular) (S41) | Insurance Ombudsman Rules 2017, as amended to 09.11.2023 (S8) |
| 3a | Ombudsman limit | Award capped at **₹50 lakh including expenses** (R.17(3)(ii)) | — | S8 |
| 3b | Hearing mode | Video-conference on the Ombudsman's own motion or on request (R.15(5)) | — | S8 |
| 3c | Representation | No express right in the Rules. Karnataka HC DB (*Office of Insurance Ombudsman v. M V Narasimha Prasad*, WA 1534/2026, 1 Jul 2026): an advocate may be engaged at the adjudicatory (Rule 17) stage, relying on Advocates Act s.30 | — | S10 (full judgment awaited at the time of reporting) |
| 4 | **Consumer Commission** (e-Jagriti) | Deficiency in service. District ≤ ₹50 lakh; State > ₹50 lakh to ₹2 crore; National > ₹2 crore | 2 years (s.69 CPA 2019) `[VERIFY]` | PIB backgrounder, Dec 2025 (S42) |
| 4a | e-Jagriti | Launched 1 Jan 2025. Integrates OCMS, e-Daakhil, NCDRC CMS, CONFONET. Online filing, fees through Bharat Kosh/PayGov, virtual hearings, NRI filing | — | S42 |
| 4b | National Consumer Helpline (pre-litigation) | 1915, WhatsApp, SMS, app, UMANG. 1,169 convergence companies. 17 languages | Many complaints resolved in ~21 days | S42 |

**Claim-settlement TATs to encode as rules (PPHI Master Circular, 5 Sep 2024) (S41)**
- Life death claim: 15 days from intimation if no investigation; 45 days with investigation.
- Health cashless: pre-authorisation within 1 hour. Final discharge authorisation within **3 hours**; the insurer bears excess hospital charges from shareholder funds if late.
- General insurance: surveyor appointed within 24 h (retail). Final survey report within 15 days. Claim paid or rejected within **7 days** of the survey report.
- Delay interest: bank rate + 2%, from intimation to payment, payable without demand.

### 2(c) Recommended LawDocs workflow (Vertical B)

**Stages:** `INTAKE → POLICY_READ (AI extracts sum insured, exclusions, waiting periods, sub-limits) → MERIT_SCORE → INSURER_GRO_SENT → (14d) → BIMA_BHAROSA → (30d from GRO / 1-month rule) → OMBUDSMAN_READY → FILED → MEDIATION | HEARING → AWARD → COMPLIANCE_WATCH (30d) → CONSUMER_COMMISSION (if >₹50 lakh or rejected) → CLOSED`.

**Documents:** policy schedule and wording, proposal form (mis-selling and non-disclosure defences), claim form, rejection or short-settlement letter, discharge summary, bills, investigation reports, surveyor report, prior correspondence, KYC, nominee or legal-heir proof (for death claims), and an authority letter.

**Templates:** T-B1 GRO complaint citing the PPHI TAT breached. T-B2 penal-interest computation (bank rate + 2%). T-B3 Ombudsman complaint in the CIO format plus Annexure VI-A style declaration `[VERIFY current form]`. T-B4 request for video hearing (R.15(5)). T-B5 mediation acceptance or rejection (15-day clock). T-B6 award-compliance demand with the ₹5,000/day reminder. T-B7 consumer complaint for e-Jagriti (panel advocate, fixed fee).

**User vs LawDocs:**
- The **user** signs and files the Ombudsman complaint. Rule 14(1) does not list agents as filers.
- **LawDocs (non-advocate)** drafts, organises evidence, tracks deadlines and prepares the user for the hearing.
- A **panel advocate** may appear at the Rule 17 adjudication stage where permitted (Karnataka HC; elsewhere `[VERIFY]`). Advocate fees are fixed, not a share of the award.

**Escalation ladder:** Insurer GRO (14 days) → Bima Bharosa / IRDAI → Insurance Ombudsman (≤ ₹50 lakh, 1 year) → Consumer Commission (e-Jagriti) → civil court. NCH 1915 runs in parallel for pre-litigation.

### 2(d) Revenue options

| Option | Benchmark | Legality note |
|---|---|---|
| Registration fee | ₹999 (Insurance Samadhan) | Low risk. Refundable if the case is not accepted |
| Success fee (non-advocate entity) | 20–22% + GST (Insurance Samadhan) | Permissible for a non-advocate consultant `[VERIFY]`. Risks: unconscionability, consumer-protection "unfair contract" (CPA 2019 s.2(46)) `[VERIFY]`. **Recommendation:** undercut at 10–15% with a cap (e.g., ₹1.5 lakh). No fee on penal interest or on the ₹5,000/day compliance penalty |
| Withdrawal charge | 10–15% (Insurance Samadhan) | High consumer-complaint risk. Use a time-based fee instead |
| B2B hospital desk (ClaimBuddy-like) | — | Separate product. Conflict if the consumer entity is also paid by hospitals. Wall it off |
| Advocate representation | Fixed fee through the marketplace | BCI Rules 20–21: no share in the award |

### 2(e) Risk register: Vertical B

| # | Risk | Mitigation |
|---|---|---|
| B1 | Acting as an unregistered insurance intermediary (sale or advice on buying) | Do not sell, compare or recommend policies in the consumer-help entity. Post-claim services only |
| B2 | Representation refused by the Ombudsman | Default: user self-files. Advocate only at the Rule 17 stage, with a request letter citing the Karnataka HC |
| B3 | ₹50 lakh cap exceeded | Automatic forum routing to the State Commission |
| B4 | Success fee seen as unfair by commission or press | Fee cap, plain-language fee sheet, cooling-off cancellation |
| B5 | Health data (sensitive) | DPDP: specific consent, purpose limitation, retention rule. Encrypt at field level |
| B6 | Impostor-site and phishing risk (IRDAI has warned of fake Bima Bharosa sites) | Show only official URLs. Never ask for portal passwords. Domain-verified links |

---

## 3. Vertical C: Traffic challans

### 3(a) Competitor teardown

| Player | Lookup | Pay | Contest / lawyer | Monetisation | Notes |
|---|---|---|---|---|---|
| **ChallanPay (Lawyered)** | Pan-India consolidation of national, state and RTO data. Real-time alerts (S30) | Yes | Guided court process. Lawyered's LOTS (Lawyer-On-The-Spot) network (S32) | Not disclosed. Fleet and B2B focus. Claims ₹350 cr processed in 2 months and 98% resolution (S30) | Partnered with **Cars24** (Oct 2024) to clear challans before used-car sale and contest "excessive" challans (S32) |
| **Park+** | National challan check | Penalty plus legal fee in the app (card, UPI, net banking) (S28) | "Lawyer will perform all tasks on your behalf." Court challan appearance (S28, S43) | **₹199 legal fee (online challan); ₹1,999 (court challan)** (S28) | No lawyer credentials or refund policy shown. How the penalty is forwarded is not explained (S28) |
| **Spinny** (Valuedrive Technologies Ltd) | OTP-verified lookup by registration number. Multi-challan payment. PDF receipt (S34) | Yes, through a gateway | Says a lawyer is not needed to pay. Contest needs a lawyer. No legal service | No stated service fee (S34) | User reviews mention amount and date mismatches vs the official portal (S34) |
| **Challan Sathi** (Delhi-NCR, Sep 2025) | User submits vehicle details and RC | — | A "representative" appears in court. Records updated in 10–15 working days | "Nominal convenience fee" (S44) | Unclear whether representatives are advocates (S44) |
| **CarInfo, Cars24** | Challan check in vehicle-info apps | Cars24 eChallan service (search results) | Cars24 through Lawyered | Lead generation for car services `[VERIFY]` | Vehicle-info apps face privacy scrutiny over the source of Vahan data (S33) |
| **"ChallanWallah"** | Not found | — | — | — | `[VERIFY]` name with the owner |
| **API vendors (e.g., Surepass)** | Challan by RC number, with pay-through API | Yes | — | B2B API | Data source and authorisation not disclosed (S31) |

### 3(b) Official process map

| Stage | Detail | Source |
|---|---|---|
| Issue | e-Challan through the Parivahan e-Challan / NextGen application (echallan.parivahan.gov.in). SMS to the registered mobile | S29, S43 |
| Voluntary payment (compounding) | Compoundable offences (MV Act **s.200** as amended 2019: ss.177–182, 182A(1),(3),(4), 182B, 183(1)–(2), 184 (handheld device only), 186, 189, 190(2), 192, 192A, 194–194F, 196, 198) are compounded by officers and for amounts notified by the State. Community service may be added. Compounding does not discharge s.206(4) proceedings | S45 |
| Virtual Court | Unpaid challans go to the designated Virtual Court. The court issues summons under **MV Act s.208** by SMS with a link to **vcourts.gov.in/virtualcourt/**. The violator pays online (taken as an admission of guilt) or opts to contest. Fine is credited to e-Treasury (eGRAS) under "Fines and Forfeitures" (Tripura notification, 1 Jun 2022) | S29 |
| Timing to Virtual Court / physical court | Park+ reports: unpaid after **60 days** → Virtual Court; after **90 days** → physical court. Varies by state | S43 `[VERIFY by state; check any CMVR Rule 167 amendment of 2025–26]` |
| Contest | "Request to Contest" sends the case to a regular court hearing. The violator may plead or contest with an advocate | S43 |
| Non-compoundable offences | e.g., s.185 drunk driving, s.184 dangerous driving (except handheld device), s.199A juvenile offences → physical court | S45, S43 |
| Lok Adalat | Periodic National/State Lok Adalats settle compoundable challans, often at reduced amounts. Delhi: OTP-based slot booking at traffic.delhipolice.gov.in/lokadalat. Only compoundable items. Commercial vehicle challans < ₹10,000. Limit of 5 notices + 2 challans (private) per appointment. The user undertakes not to contest on vcourts (S46) | S46 |
| State multiplier | s.210A lets states multiply fines by 1–10× | S45 |
| Penalty examples (post-2019) | s.181 no licence: ₹5,000. s.183 overspeeding (LMV): ₹1,000–2,000. s.185 drunk driving: ₹10,000 / 6 months (first offence). s.194C triple riding / s.194D helmet: ₹1,000 + 3-month disqualification. s.196 uninsured: ₹2,000 (first). s.199A juvenile: ₹25,000 on the guardian or owner + registration cancellation | S45 |

**API and data access**
- MoRTH (RTI reply reported June 2025): **government organisations** have API access to vehicle data. MoRTH did not answer questions about private entities (S33).
- The 2019 Bulk Data Sharing Policy, which sold Vahan/Sarathi data at ₹3 cr/year to commercial entities, was **scrapped in June 2020** (S33).
- The Parivahan data-sharing policy PDF could not be fetched (robots) `[VERIFY current policy terms]`.
- Third-party "vehicle info" apps that expose owner data face privacy scrutiny. Possible IT Act s.43 exposure for scraping (S33).
- **Conclusion:** no verifiable lawful bulk API for e-challan data is available to LawDocs today `[VERIFY with MoRTH/NIC; ask about API Setu listings]`.

**Payment on the user's behalf**
- Fines are government receipts paid into e-Treasury through the court or state gateway (S29).
- If LawDocs collects the fine into its own account and remits it, it intermediates payments to a third-party beneficiary. That may need RBI payment-aggregator authorisation `[VERIFY: RBI Payment Aggregator Directions, current version]`. It also creates reconciliation and liability exposure: Spinny users report amount mismatches (S34).
- **Recommended:** the user pays on the official vcourts or e-challan gateway, using a deep link LawDocs launches. LawDocs records the receipt (upload or auto-parse) and charges only its own service fee through Razorpay.

### 3(c) Recommended LawDocs workflow (Vertical C)

**Stages:** `VEHICLE_ADDED (RC via DigiLocker pull [VERIFY] or upload) → CHALLAN_DISCOVERY (user-initiated official lookup / SMS-PDF parse) → CLASSIFY (compoundable? online / virtual / physical court / Lok Adalat-eligible) → DECIDE (pay | Lok Adalat | contest) → PAY_ON_OFFICIAL (deep link) → RECEIPT_CAPTURED → or → LOK_ADALAT_SLOT (user books; LawDocs reminds) → or → CONTEST (panel advocate; vakalatnama; hearing date) → DISPOSED → RECORD_UPDATE_CHECK (10–15 working days) → CLOSED`.

**Documents:** RC, DL, insurance, PUC, the challan or notice PDF and photo evidence, Lok Adalat appointment printout, vakalatnama (for contest), proof of sale and delivery note time-stamp (if the challan post-dates the sale; links to Vertical D).

**Templates:** T-C1 grievance to the e-Challan portal (wrong vehicle, cloned plate, sold vehicle). T-C2 representation to the traffic police with the delivery-note evidence. T-C3 vakalatnama and memo of appearance (panel advocate). T-C4 application for compounding / Lok Adalat checklist. T-C5 fleet challan register export.

**User vs LawDocs:** the user looks up (OTP to their own mobile), pays on the official gateway, and books the Lok Adalat slot (OTP). LawDocs classifies, reminds, drafts and coordinates. The advocate appears in contested matters.

**Escalation:** pay or compound → Lok Adalat → Virtual Court contest → physical court → revision/appeal (rare).

### 3(d) Revenue options

| Option | Benchmark | Note |
|---|---|---|
| Free lookup + alerts | Spinny, Park+ | Acquisition funnel for the vehicle and legal vault |
| Per-challan service fee (online assist) | Park+ ₹199 | Must be clearly separate from the government fine |
| Court-challan advocate package | Park+ ₹1,999 | Fixed fee paid to the advocate. Platform fee kept separate `[VERIFY marketplace fee legality]` |
| Fleet subscription | ChallanPay B2B | Per-vehicle per month. Strong recurring line. Keep separate from lender clients (fleet financiers) |
| Convenience fee on the fine | — | **Avoid** unless the payment-aggregator question is cleared `[VERIFY]` |

### 3(e) Risk register: Vertical C

| # | Risk | Mitigation |
|---|---|---|
| C1 | Unauthorised data scraping (IT Act s.43; DPDP; portal ToS) | User-initiated lookups only. No server-side bulk crawling. Legal sign-off before any API vendor is used |
| C2 | Holding government fines (PA authorisation; reconciliation) | Deep-link payment. LawDocs never touches the fine |
| C3 | Mis-stated "discount" claims about Lok Adalat | Copy: "Lok Adalat may settle at a reduced amount at the court's discretion; no guarantee" |
| C4 | Advocate advertising (Rule 36, Madras HC 2024) | Platform lists advocates neutrally. No "best lawyer" ranking ads (§5) |
| C5 | Wrong-owner challans after vehicle sale | Integrate with the Vertical D delivery note (timestamp) and RC-transfer tracking |
| C6 | State variance (timelines, Lok Adalat dates, multiplier) | Rules held as per-state data. Ops-editable Lok Adalat calendar |

---

## 4. Vertical D: Vehicle transactions

### 4(a) Competitor teardown

| Player | Document flow | Observations |
|---|---|---|
| **Cars24** | Buys the car. Clears challans through Lawyered before resale (S32). Handles RC transfer `[VERIFY]` | Challans must be cleared before a used-car sale can complete (S32) |
| **Spinny** (Valuedrive Technologies) | Guides on hypothecation removal (Form 35, NOC usually valid ~90 days, online Vahan) and challan payment (S34, S36) | Content-led SEO funnel. Lok Adalat city pages (search results) |
| **OLX Autos** | Reported to have exited India car-buying in 2023 `[VERIFY]` | C2C classifieds (OLX) leave paperwork to the parties. This is the LawDocs opportunity |
| **CarInfo, Park+** | RC lookup, challans, insurance renewal | Lead generation for insurance and loans. Conflict-sensitive |
| **LegalKart / Vakilsearch** | Generic vehicle sale agreement templates `[VERIFY]` | None tie the agreement to the RC-transfer deadline engine |

### 4(b) Official process map

| Step | Rule | Source |
|---|---|---|
| Pre-sale checks | Pending challans (official portal), blacklist status, hypothecation in RC, insurance and PUC validity, tax clearance | S35, S36, S32 |
| Hypothecation removal | Pay off and obtain the bank NOC + **Form 35** (signed by owner and financier) → online Vahan application → RC updated. NOC often valid ~90 days. Some lenders send e-NOC directly to Vahan | S36 |
| Lender obligation | Release documents and remove the charge within 30 days of full repayment. ₹5,000/day for delay attributable to the NBFC | S15 `[VERIFY movable-property applicability]` |
| Foreclosure | Request a foreclosure statement. Prepayment charges per KFS. No charges on floating-rate non-business individual loans sanctioned on or after 1 Jan 2026 (most vehicle loans are fixed-rate) | S15 `[VERIFY]` |
| Sale documents | Sale agreement / sale letter. **Delivery note** with date and time of handover (shifts the practical burden for later challans and accidents). Receipt of consideration | Practice `[VERIFY]`. Owner liability: until the RC is transferred, the registered owner may remain liable to third parties `[VERIFY case law]` |
| Transfer forms | **Form 29** (seller's notice), **Form 30** (application for transfer, seller and buyer), **Form 28** (NOC for another state or RTO), Form 35 (if hypothecated) | S35 |
| Deadlines | Apply within **14 days** (same state) / **45 days** (vehicle from another state). Legal heir: inform within 30 days of death, transfer within 3 months. Auction buyer: 30 days. Insurance transfer: buyer applies to insurer within 14 days | S35 (statutory basis MV Act s.50 / CMVR r.55 `[VERIFY]`) |
| Online | vahan.parivahan.gov.in/vahanservice → Basic Service → chassis last 5 digits + OTP → Transfer of Ownership → pay → application number. Some states still require physical submission | S35 |
| Fees | Central fee: half the registration fee (≈ ₹150 motorcycle, ₹300 car) under CMVR r.81. Late fees ₹300/₹500 per month. State penalties | S35 |
| Aadhaar-based contactless services | MoRTH notified Aadhaar-authenticated contactless RC services (2020–21) `[VERIFY]` | — |
| **Stamp duty** | Varies by state. Questions: (i) is a sale of goods effected by delivery chargeable at all; (ii) is the agreement an "agreement" (residuary article) or a "conveyance" of movable property (some state schedules, e.g., Maharashtra Art. 25, cover movable property at an ad valorem rate) `[VERIFY each state]`; (iii) e-stamp availability (SHCIL) | Analyst note. The Supreme Court on agreements for sale with possession as conveyance concerns immovable property under the Maharashtra Act (search result) `[VERIFY]` |

### 4(c) Recommended LawDocs workflow (Vertical D)

**Stages:** `LISTING_PREP (pre-sale checks pack) → TERMS_AGREED → AGREEMENT_DRAFTED (Vidhi AI; state stamp rule) → eSTAMP/STAMP_ATTACH → eSIGN (both parties, Aadhaar eSign) → PAYMENT_CONFIRMED (user-to-user; LawDocs doesn't escrow [VERIFY escrow licensing]) → DELIVERY_NOTE (time-stamped, geo-tagged photos of odometer, keys, RC) → FORMS_29_30 (pre-filled PDFs; wet or as accepted by the RTO) → VAHAN_APPLIED (application no. captured) → 14/45-DAY WATCH → RC_TRANSFERRED → INSURANCE_TRANSFERRED → CLOSED`.

Hypothecated vehicle branch: `FORECLOSURE_REQUEST → PAID → NOC + FORM 35 → (30-day release watch, ₹5,000/day claim template) → HYPOTHECATION_REMOVED` before or concurrently with transfer.

**Templates:** T-D1 vehicle sale agreement (with challan-responsibility cut-off, hypothecation warranty, indemnity, no-accident declaration, RC-transfer cooperation covenant with 14/45-day timeline). T-D2 delivery note with timestamp. T-D3 receipt. T-D4 Forms 29/30/28/35 auto-fill. T-D5 foreclosure request and NOC demand. T-D6 seller's intimation to the RTO and the police if the buyer does not transfer (protective) `[VERIFY state practice]`. T-D7 Power of attorney / authority for an agent to file at the RTO `[VERIFY stamp]`.

**User vs LawDocs:** the parties sign, pay each other and submit to Vahan (OTP to the owner's mobile). LawDocs drafts, e-stamps (through an e-stamp partner, see the separate stream), runs eSign, pre-fills forms and tracks deadlines. Advocates are needed only for disputes.

### 4(d) Revenue options
Free basic agreement (owner brief: free AI drafting on every page). ₹199–₹499 "Sale Kit" (agreement + delivery note + forms + tracker). ₹999 "Assisted Transfer" (case manager). Advocate review at a fixed fee. B2B kit for dealers and fleet. E-stamp pass-through at cost plus a disclosed convenience fee `[VERIFY state e-stamp vendor rules]`.

### 4(e) Risk register: Vertical D

| # | Risk | Mitigation |
|---|---|---|
| D1 | Wrong stamp duty → the instrument is inadmissible until duty and penalty are paid | State rule table, legal-reviewed and versioned. Show "duty basis" on the document |
| D2 | Seller remains the registered owner (challans, accident liability) | Delivery note with timestamp. 14/45-day alerts to both parties. Protective intimation template |
| D3 | Escrow or holding of the sale price | No escrow unless through a licensed bank or escrow partner `[VERIFY]` |
| D4 | Conflict: the financier is a Finbyx/Udofin client | Ethical wall. The NOC demand is generated by the consumer entity only |
| D5 | Forms change or state variance | Forms stored as versioned templates per state |

---

## 5. Business model, conflicts and professional-conduct guidance

### 5.1 Fees: advocates vs non-advocates

| Question | Position | Source |
|---|---|---|
| Can an advocate take a % of the claim or a success fee? | **No.** BCI Rules Part VI Ch. II Sec. II, **Rule 20** (no fee contingent on results, no share in proceeds) and **Rule 21** (no buying or trafficking in, or share in, an actionable claim). *In re Mr 'G'* (SC 1954) | S27 |
| Can a non-advocate consultant take one? | Not barred by BCI rules, which bind advocates only (*K.L. Gauba*, as cited). Courts have historically viewed contingency arrangements through Contract Act s.23 public policy and champerty, and have since upheld third-party funding (Delhi HC, as cited) | S27. `[VERIFY]` *BCI v. A.K. Balaji* (2018) observation on non-lawyer funding |
| Can the platform share a success fee with a panel advocate? | **No.** Indirect breach of Rules 20–21, and of fee-sharing with non-advocates `[VERIFY Rule 2 of Sec. IV / Rule 37]` | S27 |
| **Structure** | Consumer-help entity (non-advocate) charges for case management, which may be success-linked. A panel advocate is engaged directly by the user through a separate fixed-fee invoice, and the platform collects it as a disclosed pass-through `[VERIFY]`. No referral fee to or from advocates | — |

### 5.2 Advertising and solicitation
- **BCI Rule 36** bars advocates from soliciting or advertising, directly or indirectly. The 2008 relaxation allows websites with limited information plus a disclaimer (S47).
- On 3 Jul 2024 the **Madras HC** (*P.N. Vignesh v. Bar Council*, 2024 MHC 2515) directed action against advocates advertising through online platforms (S48, search result). BCI then issued directions to State Bar Councils, demanded removal of online legal-service ads within 4 weeks, and sent cease-and-desist notices to Quikr, Sulekha, JustDial and Grotal (S48). Sulekha's SLP: the Supreme Court issued notice to BCI on the scope of online listings (search result) `[VERIFY status]`.
- **Platform rules:** advocate profiles hold only Rule 36-permitted information. No ratings-based "best lawyer" ads, testimonials about advocates, or outcome claims. The consumer brand advertises its **own non-legal services** only. Owner brief: testimonials without photos. For advocate-related content, use none.
- Consumer-protection overlay: CCPA Guidelines on misleading advertisements (2022) and dark patterns (2023) `[VERIFY citations]`. No "100% success" or "guaranteed waiver".

### 5.3 Who may represent where (product permission matrix)

| Forum | Self | Non-advocate representative | Advocate |
|---|---|---|---|
| RE grievance / insurer GRO | ✔ | ✔ with authorisation | ✔ |
| RBI Ombudsman (RB-IOS 2026) | ✔ | ✔ written authorisation | **✘** unless the advocate is the aggrieved person (S1, S2) |
| Insurance Ombudsman | ✔ (or legal heir, nominee, assignee) | ✘ not provided for in R.14(1) `[VERIFY CIO practice]` | At the Rule 17 adjudication stage (Karnataka HC, S10) |
| Consumer Commission | ✔ | Only under the 2014 agent regulations, on a party-issued authorisation. Not on an advocate's authority letter (S14) | ✔ |
| Virtual Court / magistrate | ✔ | ✘ | ✔ vakalatnama |
| Lok Adalat (traffic) | ✔ | `[VERIFY]` | ✔ |

### 5.4 Authority letters and POA
- **RBIO:** a written authorisation from the complainant naming the non-advocate representative, the complaint subject and the RE, with signature or eSign. `[VERIFY]` whether CMS accepts Aadhaar eSign.
- **Consumer Commission:** a party-issued authenticated authorisation in the form under the 2014 regulations `[VERIFY form]`.
- **Lender negotiation:** a limited authority letter (non-POA) to correspond and negotiate. No authority to bind the borrower to a settlement without in-app confirmation by the borrower. AMA Legal notes that a firm cannot bind a borrower without a POA (S26).
- **RTO filing:** an authority letter or POA per state practice `[VERIFY stamp]`.
- All authorities must be revocable in-app, time-bound, scoped, and logged in the audit trail.

### 5.5 DPDP Act 2023 and Rules 2025
- **Timeline:** Rules notified 14 Nov 2025. Rules 1, 2 and 17–21 apply immediately. Rule 4 (Consent Managers) after 1 year (≈ Nov 2026). Rules 3, 5–16, 22–23 (core obligations: notice, security, 72-hour breach report, retention and erasure with 48-hour warning, children) after **18 months (≈ May 2027)** (S49, S50). Build to the final standard now.
- **Consent:** itemised notice per purpose (case handling, sending to the RE, sharing with a panel advocate, analytics). Separate opt-in for each. Health data (insurance) and financial data at the highest sensitivity tier internally.
- **Legal-claims exemption:** processing necessary to enforce a legal right or claim may be exempt from parts of the Act (s.17(1)(a)) `[VERIFY scope]`. Do not rely on it for marketing or analytics.
- **Third-party personal data** (agent names, numbers, recordings): process only for the claim. Restrict access and set a retention limit.
- **No cross-entity sharing:** consumer-help data must never flow to Finbyx, Udofin or LawDocsComply. This follows from DPDP purpose limitation and the ethical wall.

### 5.6 Ethical wall design (for the architecture stream)
1. **Separate legal entity and brand.** The owner brief contemplates a new entity and renaming LawDocsComply. Use its own GSTIN, bank account, Razorpay merchant ID, privacy policy and grievance officer.
2. **Separate tenant / database / encryption keys.** Platform services (eSign, DMS, Vidhi AI) are shared as **stateless** services with per-tenant keys.
3. **Conflict check:** the consumer entity submits a salted hash of the opposite party's legal name, CIN or RBI registration number. The group service returns only "conflict / no conflict". No client list is exposed. On a conflict, the case is accepted on a "self-serve only" basis or declined, and the user is told why in generic terms.
4. **People wall:** no shared staff, advocates or RMs between consumer-help and lender-facing ops hubs. Access recertification quarterly.
5. **Commercial wall:** no lender referral fees, no lead-selling, no borrower data monetisation.
6. **Governance:** board-approved COI policy. Annual independent review. Breach register in LawDocsComply, holding metadata only.

---

## 6. Cross-vertical product requirements (for the build prompt)

- **Rule engine data sets (versioned, ops-editable, effective-dated):** RB-IOS 2026 eligibility and clocks. Internal Ombudsman TATs. RBC recovery-conduct rules (effective 1 Jan 2027). CIC 21/9/30-day + ₹100/day. IO Rules 2017 clocks and the ₹50 lakh cap. PPHI TATs. CPA 2019 pecuniary limits. MV Act compounding list and state multipliers. State Lok Adalat calendar. RC-transfer deadlines. State stamp-duty table.
- **Deadline engine:** computes "later-of" windows (RBIO 90 days), 30-day acceptance windows (RBIO award, IO award compliance), and 14/45-day RC windows. Notifies by WhatsApp, SMS and email. Shows a "Waiting on: Bank / You / Ombudsman" chip (owner brief: waiting-for-someone-else items).
- **Evidence locker:** capture hash and time. Call-recording import. WhatsApp screenshot OCR with an editable typed copy (owner brief para 53). Export bundle with index.
- **Official-link registry:** cms.rbi.org.in, sachet.rbi.org.in, cioins.co.in, Bima Bharosa, e-Jagriti, NCH 1915, vcourts.gov.in, echallan.parivahan.gov.in, vahan.parivahan.gov.in, Delhi Traffic Lok Adalat. Weekly link-health monitor to defeat phishing clones.
- **"i" tooltips** for each term (Ombudsman, Award, Compounding, Form 35 and similar), per the owner brief.
- **Reporting:** case outcomes by forum, average days per stage, recovery amounts. Feeds the Savings page (owner brief para 71): money recovered, compensation obtained, challan amounts reduced.

---

## 7. Open questions for the owner

1. What does "ChallanWallah" refer to? It may be ChallanPay or Challan Sathi.
2. Will the consumer-help entity employ **non-advocate case managers** (required for RBIO representation) or operate DIY-only?
3. What success-fee appetite do you have? The recommended cap is 10–15% in the non-advocate entity only, with no success fee on the debt "savings" product.
4. Should the B2B fleet challan subscription sit in the consumer entity, or in a separate mobility entity? Fleet financiers may be Finbyx clients.
5. Does LawDocs want an escrow partner for vehicle sales, or should payment remain party-to-party?

---

## 8. Sources (all accessed 25 Oct 2026)

| # | URL | Title / description |
|---|---|---|
| S1 | https://www.rbi.org.in/commonman/Upload/English/FAQs/PDFs/RBIOS01072026.pdf | RBI, FAQs: Reserve Bank – Integrated Ombudsman Scheme, 2026 |
| S2 | https://taxguru.in/rbi/rbi-issues-reserve-bank-integrated-ombudsman-scheme-2026.html | TaxGuru, RBI issues RB-IOS 2026 (text and clause summary) |
| S3 | https://freed.care/ | FREED homepage |
| S4 | https://freed.care/blog/how-to-handle-bank-recovery-agents-know-your-rights | FREED blog, Recovery agents: know your rights 2026 |
| S5 | https://www.insurancesamadhan.com/ | Insurance Samadhan homepage (fees, process) |
| S6 | https://www.businesstoday.in/money/insurance/this-startup-helps-customers-fight-insurance-claim-rejection/story/394833.html | Business Today (Jan 2020), Insurance Samadhan profile |
| S7 | https://yourstory.com/2024/04/claimbuddy-secures-5-mn-in-series-a-funding | YourStory (Apr 2024), ClaimBuddy Series A |
| S8 | https://www.cioins.co.in/notification/Insurance%20Ombudsman%20Rules,%202017(%20as%20amended%20till%2009.11.2023).pdf | Insurance Ombudsman Rules 2017 (as amended till 09.11.2023) |
| S9 | https://ianslive.in/policyholders-can-approach-insurer-irdai-for-redress-of-insurance-related-grievances--20260814154803 | IANS (14 Aug 2026), insurance grievance redress, Bima Bharosa |
| S10 | https://www.livelaw.in/high-court/karnataka-high-court/karnataka-high-court-dismisses-appeal-policyholder-right-insurance-ombudsman-adjudicatory-proceedings-539486 | LiveLaw (1 Jul 2026), Karnataka HC on lawyer before Insurance Ombudsman |
| S11 | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=13665 | RBI (Commercial Banks – RBC) Fourth Amendment Directions, 2026 (6 Aug 2026) |
| S12 | https://www.indialaw.in/blog/banking-and-finance/rbi-nbfc-loan-recovery-amendment-2026/ | IndiaLaw (16 Oct 2026), NBFC RBC Third Amendment Directions 2026 |
| S13 | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848 | RBI (Digital Lending) Directions, 2025 (8 May 2025) |
| S14 | https://www.livelaw.in/amp/high-court/delhi-high-court/delhi-high-court-bars-non-advocates-from-appearing-before-consumer-courts-279456 | LiveLaw (Dec 2024), *Anuj Kumar Chauhan v. LG NCT Delhi* |
| S15 | https://www.indialaw.in/blog/banking-and-finance/rbi-nbfc-responsible-business-conduct-directions-2025/ | IndiaLaw, NBFC RBC Directions 2025 (28 Nov 2025) summary |
| S16 | https://www.business-standard.com/finance/news/rbi-mandates-auto-escalation-of-unresolved-complaints-to-internal-ombudsman-126011401228_1.html | Business Standard (14 Jan 2026), Internal Ombudsman auto-escalation |
| S17 | https://www.rbi.org.in/scripts/bs_viewcontent.aspx?Id=5029 | RBI Draft (Commercial Banks – RBC) Amendment Directions 2026 |
| S18 | https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=56909 | RBI PR 2023-24/1459 (11 Dec 2023), caution on loan-waiver campaigns |
| S19 | https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62677 | RBI PR (4 May 2026), reiterated caution on loan-waiver campaigns |
| S20 | https://freed.care/blog/debt-settlement-companies-vetting-checklist | FREED blog, vetting debt settlement companies |
| S21 | https://www.freepressjournal.in/latest-news/how-long-does-the-loan-settlement-process-take-in-india | Free Press Journal (syndicated), loan settlement timeline |
| S22 | https://www.singledebt.in/ | SingleDebt homepage |
| S23 | https://settleloan.in/ | Settle Loan homepage |
| S24 | https://www.credsettle.com/which-companies-offer-loan-settlement-services-in-india | CredSettle, settlement companies 2025 guide (interested party) |
| S25 | https://www.mymudra.com/blog/best-debt-settlement-companies-in-india | My Mudra (May/Sep 2026), debt settlement companies list |
| S26 | https://www.amalegalsolutions.com/blog/why-not-trust-loan-settlement-companies-rbi-guidelines | AMA Legal Solutions blog (internally inconsistent; low reliability) |
| S27 | https://legalblogs.wolterskluwer.com/arbitration-blog/feevolution-the-need-to-embrace-contingent-fee-arrangements-in-the-indian-arbitration-regime/ | Kluwer Arbitration Blog (Aug 2024), contingent fees in India (BCI Rules 20–21) |
| S28 | https://parkplus.io/blog/challan/clear-your-traffic-challans-online-with-parkplus-expert-lawyer-support | Park+, challan lawyer support (₹199 / ₹1,999) |
| S29 | https://www.thc.nic.in/notification/THC_13542_43_01062022.pdf | Tripura High Court notification (1 Jun 2022), Virtual Court for traffic challans |
| S30 | https://evindia.online/news/lawyered-launches-challanpay-new-platform-resolves-98-of-350-cr-in-indian-traffic-challans | EVIndia (Nov 2025), Lawyered launches ChallanPay |
| S31 | https://surepass.io/challan-payment-api/ | Surepass, Challan Payment API |
| S32 | https://autocarpro.in/NEWS/cars24-partners-with-lawyered-for-streamlined-traffic-challan-resolution-122989 | Autocar Pro (9 Oct 2024), Cars24–Lawyered partnership |
| S33 | https://www.medianama.com/2025/06/223-api-access-vehicle-data-sharing-raising-privacy-concerns/ | MediaNama (17 Jun 2025), API access to vehicle data |
| S34 | https://www.spinny.com/court-challan/ | Spinny, court challan / e-challan payment |
| S35 | https://www.autocarindia.com/auto-features/how-to-transfer-vehicle-ownership-in-india-process-documents-fees-explained-441160 | Autocar India (10 Oct 2026), vehicle ownership transfer |
| S36 | https://www.spinny.com/blog/rc-hypothecation-how-to-remove-car-loan-hypothecation/ | Spinny blog, RC hypothecation removal |
| S37 | https://www.cioins.co.in/ | Council for Insurance Ombudsmen homepage |
| S38 | https://rbidocs.rbi.org.in/rdocs/notification/PDFs/FRAMEWORKCOMPROMISE97202CBAA1374268BA9AAA616D239890.PDF | RBI Framework for Compromise Settlements (8 Jun 2023); **not fetched** (bot-check) |
| S39 | https://www.cibil.com/framework-for-compensation | TransUnion CIBIL, compensation framework |
| S40 | https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12554 | RBI/2023-24/72 (26 Oct 2023), compensation for delayed credit-information updation |
| S41 | https://www.mondaq.com/india/insurance-laws-and-products/1536672/irdai39s-update-on-turnaround-times-for-insurance-companies | Mondaq / Tuli & Co (Oct 2024), IRDAI PPHI TATs |
| S42 | https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/dec/doc20251223743001.pdf | PIB backgrounder (Dec 2025), e-Jagriti, NCH, consumer commissions |
| S43 | https://parkplus.io/blog/challan/how-to-pay-challan-in-court | Park+, how to pay challan in court |
| S44 | https://www.outlookindia.com/amp/story/hub4business/challan-sathi-launches-as-indias-first-one-stop-platform-for-traffic-fine-settlements | Outlook (29 Sep 2025), Challan Sathi launch |
| S45 | https://www.taxmann.com/post/blog/offences-and-punishment-fine-under-motor-vehicles-act | Taxmann, MV Act offences and penalties; https://lawx.in/acts/section/46/470/4508 (MV Act s.200 text) |
| S46 | https://traffic.delhipolice.gov.in/lokadalat/assets/Instructions.pdf | Delhi Traffic Police, Lok Adalat instructions |
| S47 | https://ksandk.com/regulatory/indian-lawyers-no-ads-allowed-per-bar-council-rules/ | King Stubb & Kasiva (Apr 2023), BCI Rule 36 |
| S48 | https://www.scconline.com/blog/post/2024/07/09/bci-bans-illegal-solicitation-of-legal-services-by-lawyers-on-online-portals-after-madras-hc-decision/ | SCC Online (9 Jul 2024), BCI action after Madras HC |
| S49 | https://www.storyboard18.com/digital/breaking-govt-notifies-final-dpdp-rules-sets-staggered-rollout-with-key-obligations-for-data-fiduciaries-84201.htm | Storyboard18 (14 Nov 2025), DPDP Rules 2025 phased rollout |
| S50 | https://www.deccanherald.com/amp/story/india%2Fcentre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465 | Deccan Herald (14 Nov 2025), DPDP Rules phases |
| S51 | https://www.lawrbit.com/article/reserve-bank-of-india-digital-lending-directions-2025/ | Lawrbit, Digital Lending Directions 2025 summary |

**Not fetchable (search snippets only):** claimbuddy.in (robots); finchannel.com "Top 5 loan settlement companies 2026" (robots); ibsintelligence.com debt-management startups (error); parivahan.gov.in data-sharing policy PDF (robots); RBI compromise-settlement FAQ PDF (redirect / bot-check); verdictum.in report of *P.N. Vignesh v. Bar Council* (2024 MHC 2515) and the Sulekha SLP (titles seen in search only).
