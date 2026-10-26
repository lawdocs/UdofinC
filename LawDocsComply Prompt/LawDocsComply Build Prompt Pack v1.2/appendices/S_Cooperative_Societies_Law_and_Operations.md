# Appendix S — Co-operative Societies: Law and Operations

> **Binding for:** P15 (families `CCS`, `COOP`, `SOCIETY`), P16 (Co-operative Society Operations Suite), P14 (member grievance routing), P11 (Registrar/CRCS returns), P19 (co-operative export profile), Part 2 Excel templates `LDC-TPL-COOP-CCS` and `LDC-TPL-COOP-GEN` (Appendix E).
> **Prepared:** 25 October 2026. Facts carry their status: **[LAW]** statute or rule text as understood; **[REG]** regulator order or circular; **[PRAC]** common practice; **[REC]** our recommendation; **[VERIFY]** check against the primary text before it drives a hard block (Appendix G §G.0 rule 1).
> **Relationship with Finbyx.** Finbyx v1.5 Part 7G (IP1–IP2) is the lender-side specification for credit co-operative societies (members, shares, deposits adapter, loans, prudential monitoring, recovery). This appendix is the governance, compliance and society-affairs counterpart. Where both state a rule, the citation must match; any divergence is a defect to be raised through the Integration Specification change process.

>
> **v1.1 changes (25 October 2026)**
> - New **§S.11A member self-service, multilingual notices and electronic meetings** (State-law constraints flagged for counsel), **§S.11B office-bearer functions incl. Treasurer**, **§S.11C Registrar inspection/inquiry and members' inspection-rights reference**, **§S.11D audit-para tracker data model**, **§S.11E language coverage** — supporting P16 §4R–§4W.
> - Elections remain conducted by the election authority (X-34); co-operative credit books stay in Finbyx (D-16); member SoR switch unchanged (D-23).
---

## S.1 The sector in numbers

| Item | Figure | Source (as of) |
|---|---|---|
| Co-operatives on the National Cooperative Database | ≈ 8.4 lakh across 30 sectors | PIB / Ministry of Cooperation document, Feb 2026 |
| Members | ≈ 32 crore | same |
| PACS computerisation | 79,630 sanctioned in 31 States/UTs; 61,025 onboarded on a common ERP; outlay ₹2,925.39 crore | same |
| New PACS, dairy and fishery societies registered since 15 Feb 2023 | 32,802 (to 20 Jan 2026) | same |
| Multipurpose co-operative societies | 22,283 (20 Jun 2025) | same |
| Elections conducted by the Co-operative Election Authority | > 222 MSCS (to 31 Dec 2025) | same |
| MSCS placed under liquidation since the 2023 amendment | 113 | Indian Cooperative, Dec 2025 |
| Co-operative Ombudsman | notified 5 Mar 2024 (MSCS s.85A); 36 orders by Dec 2025 | PIB; Indian Cooperative |
| National Cooperation Policy | unveiled 24 Jul 2025 — 6 pillars, 16 objectives, 83 recommendations | PIB |
| Ministry of Cooperation | constituted 6 Jul 2021 | PIB |

**Commercial implication [REC].** Credit co-operative societies (urban credit societies, salary-earners' societies, patsansthas, Souharda credit co-operatives, MSCS thrift and credit societies) are a large, under-digitised market whose regulators (Registrars) are tightening oversight after high-profile failures. LDC's value proposition is "run your society lawfully and visibly" — statutory clocks, registers, AGMs, elections, audit rectification, deposit-eligibility discipline and member grievance — with Finbyx for the loan and deposit books and Udofin for members.

---

## S.2 Legal architecture

### S.2.1 Constitutional basis
- **Entry 32, List II (State List):** incorporation, regulation and winding up of co-operative societies — State legislatures enact State co-operative Acts [LAW].
- **Entry 44, List I (Union List):** incorporation, regulation and winding up of corporations whose objects are not confined to one State — the basis for the Multi-State Co-operative Societies Act, 2002 [LAW].
- **Article 19(1)(c)** (right to form co-operative societies) and **Article 43B** (promotion of co-operatives), inserted by the 97th Amendment, 2011 [LAW].
- **Part IXB (Arts. 243ZH–243ZT)**, inserted by the 97th Amendment, prescribes board size (≤ 21), five-year term, elections by an independent authority, audit and returns. In *Union of India v. Rajendra N. Shah* (Supreme Court, 20 July 2021) the Court held Part IXB inoperative for State co-operative societies for want of ratification by half the States (Art. 368(2) proviso), while upholding it for multi-State co-operatives and those in Union Territories [LAW; VERIFY citation]. Product rule: Part IXB-derived checks attach to `CCS_MSCS`, `MSCS_OTHER` and UT societies; State societies rely on their State Act, most of which mirror Part IXB features.

### S.2.2 Multi-State Co-operative Societies Act, 2002 as amended in 2023
Key provisions used by the product (section numbers to be re-verified against the consolidated Act [VERIFY]):

| Area | Provision | Product use |
|---|---|---|
| Registration | Members from at least two States; registration by the Central Registrar | Society master validation |
| Bye-laws | Amendments registered by the Central Registrar | Bye-law workflow (P16 FR-P16-04) |
| Membership | Admission decision within 4 months and communication within 15 days or deemed refusal (s.25(4) as amended); non-voting shareholders (s.26 proviso); expulsion with 3-year bar (2023) | Admission clocks; member classes |
| General body | AGM within 6 months of close of FY (s.39); annual report contents incl. loans to directors/relatives (s.39(3)) | AGM clock; agenda pack |
| Board | ≤ 21 directors; reservation for SC/ST (1) and women (2); co-opted experts; term 5 years (ss.41, 45 as amended) | Composition checks |
| Elections | Co-operative Election Authority (s.45 and the provisions inserted in 2023); board to inform the Authority 6 months before term expiry (s.45J(8)) | Election clocks |
| Disqualification | s.43 incl. failure to hold AGM, file returns or conduct elections; 5-year bar | Disqualification watch |
| Officers | Chief Executive; Compliance Officer; Information Officer (2023 amendment) | KMP seeds |
| Funds | Reserve fund ≥ 25% of net profit; Co-operative Education Fund 1%; reserve for unforeseen losses ≥ 10% (s.63); Co-operative Rehabilitation, Reconstruction and Development Fund — lesser of ₹1 crore and 1% of net profit if profitable in each of preceding 3 years (s.63A) | Appropriation validation |
| Deposits and borrowing | Deposits only from members (voting) and borrowing limits (s.67) | Deposit-eligibility guard |
| Loans | No loans on the security of own shares; restrictions on loans to non-members (s.66) | Guard-rails |
| Audit | Auditor from the Central Registrar's panel; special panel above ₹500 crore turnover/deposits (s.70); concurrent audit above ₹500 crore (s.70A) | Audit workflow |
| Inspection/inquiry | Central Registrar powers (e.g., s.108) | Registrar matters |
| Disputes | Arbitration (s.84) | Signposting; block private arbitration |
| Ombudsman | Co-operative Ombudsman (s.85A) | Grievance routing |
| Returns | Annual return within 6 months of FY close (s.120) via the CRCS portal | Return clock |
| Sick societies | Rehabilitation; liquidation (Chapter on winding up) | Liquidation events |

**MSCS Rules, 2023** prescribe forms, registers, election procedure details, audit and return formats [VERIFY form list]. **CRCS orders** include the prudential norms for credit MSCS (order L-11012/01/2023-Reg, 22 Jan 2024) and a branch-expansion order (July 2025) [REG; VERIFY].

### S.2.3 State co-operative societies Acts (seed list for State packs)

| State | Act and Rules | Election authority | Pack status v1.0 |
|---|---|---|---|
| Maharashtra | Maharashtra Co-operative Societies Act, 1960; MCS Rules, 1961; MCS (Election to Committee) Rules, 2014; Chapter XI-1A for credit societies (ss.144-1A to 144-30A) | Maharashtra State Co-operative Election Authority (s.73CB) | Complete [VERIFY items noted] |
| Gujarat | Gujarat Co-operative Societies Act, 1961 and Rules, 1965 | Gujarat State Co-operative Election Commission [VERIFY] | STUB |
| Rajasthan | Rajasthan Co-operative Societies Act, 2001 and Rules, 2003 | State Co-operative Election Authority [VERIFY] | SEED (§S.7A) |
| Uttar Pradesh | UP Co-operative Societies Act, 1965 and Rules, 1968 | UP State Co-operative Election Commission [VERIFY] | STUB |
| Delhi | Delhi Co-operative Societies Act, 2003 and Rules, 2007 | Committee-supervised elections under s.35 [VERIFY current authority] | SEED (§S.7A) |
| Karnataka | Karnataka Co-operative Societies Act, 1959; Karnataka Souharda Sahakari Act, 1997 | Karnataka State Co-operative Election Authority [VERIFY] | STUB |
| Madhya Pradesh | MP Co-operative Societies Act, 1960 | MP State Co-operative Election Authority [VERIFY] | STUB |
| Telangana / Andhra Pradesh | Co-operative Societies Acts (1964) and Mutually Aided Co-operative Societies Acts (1995) [VERIFY current status in each State] | [VERIFY] | STUB |
| Bihar | Bihar Co-operative Societies Act, 1935; Bihar Self-Supporting Co-operative Societies Act, 1996 | Bihar State Election Authority (co-operative) [VERIFY] | STUB |
| Kerala | Kerala Co-operative Societies Act, 1969 | State Co-operative Election Commission [VERIFY] | STUB |
| Tamil Nadu | Tamil Nadu Co-operative Societies Act, 1983 | TN State Co-operative Societies Election Commission [VERIFY] | STUB |

### S.2.4 Allied statutes
- **Banking Regulation Act, 1949**: s.56 applies the Act (as modified) to co-operative banks; s.7 (with s.56) bars non-bank co-operatives from using "bank", "banker" or "banking" (from the 2020 amendment) [LAW; VERIFY effective date]. RBI public caution (press release, 22 Nov 2021): some co-operative societies were accepting deposits from non-members/nominal/associate members and using "bank" in names; such deposits are not insured by DICGC [REG].
- **Banning of Unregulated Deposit Schemes Act, 2019**: deposits accepted by co-operative societies under their Acts are regulated deposit schemes (First Schedule); deposits outside those permissions are unregulated and banned [LAW].
- **DICGC Act, 1961**: no cover for deposits with credit co-operative societies [LAW].
- **Societies Registration Act, 1860** (and State amendments): governs literary, scientific and charitable societies — **not co-operatives**; the product treats these as family `SOCIETY` (governing body, annual list of members/governing body filed with the Registrar of Societies, accounts, audit, FCRA where foreign contribution) [LAW; VERIFY State variants].
- **Money-lending Acts**: generally exclude co-operative societies (e.g., Maharashtra Money-Lending (Regulation) Act 2014 s.2(13)(e)) [LAW; VERIFY other States]. **State coercive-recovery laws** (Karnataka Act 15 of 2025; Tamil Nadu Act 40 of 2025) exempt co-operatives from registration but may apply coercion prohibitions (TN s.20) [LAW; VERIFY].
- **DPDP Act 2023**: a society is a Data Fiduciary for its members' personal data; statutory processing (registers, audit, Registrar returns) proceeds on legitimate uses for compliance with law (s.7) [INTERP; VERIFY].
- **Income-tax**: the deduction for co-operative societies (s.80P of the 1961 Act; successor provision under the Income-tax Act 2025 [VERIFY]); TDS on interest to members; ITR filing.
- **GST**: where taxable supplies exceed the threshold (housing societies' maintenance above the per-member threshold; marketing/consumer societies) [VERIFY].

---

## S.3 Institutions

| Institution | Role | Product touchpoint |
|---|---|---|
| Ministry of Cooperation (Govt of India) | Policy; administers MSCS Act; schemes (PACS computerisation, new multipurpose PACS, National Cooperative Database, NCP 2025) | Updates feed source (P05) |
| Central Registrar of Co-operative Societies (CRCS) | Registration, bye-laws, audit panel, returns, inspection and inquiry for MSCS | Returns, inspections, bye-law approvals |
| State Registrar (Commissioner/Registrar, Joint, Divisional Joint, District Deputy and Assistant Registrars) | Same functions under State Acts | State packs |
| Co-operative Election Authority (MSCS) | Conducts MSCS board elections | Election support (P16 §4F) |
| State Co-operative Election Authorities/Commissions | Conduct State society elections | Election support |
| Co-operative Ombudsman (MSCS s.85A) | Member complaints | Grievance routing |
| Co-operative Courts / Tribunals; Registrar's nominee/arbitrator | Statutory dispute resolution | Signposting; matter tracker |
| NABARD | Refinance; supervision of StCBs/DCCBs; PACS ERP via StCB/DCCB | PACS adapter |
| NCDC | Development finance to co-operatives | Borrowing records |
| Federations (State federations of urban credit societies; NAFCUB for UCBs and credit societies; NAFSCOB) | Training, representation, model bye-laws | Content partners [REC] |
| Financing banks (DCCB/StCB) | Lenders to societies; sometimes depository of statutory reserves | Society master |
| Panel auditors (CA firms or certified co-operative auditors) | Statutory audit | `ten_external_auditor` users |

---

## S.4 Member classes and rights

| Class | Vote | Deposit (credit societies) | Borrow | Stand surety | Attend general body | Dividend |
|---|---|---|---|---|---|---|
| Ordinary (voting) member | Yes | Yes | Yes | Yes | Yes | Yes |
| Nominal member | No | **No (hard block)** | Per bye-laws (typically limited) | No | No | No (e.g., MCS s.24(2)) |
| Associate member (meaning varies: Maharashtra — a joint holder whose name is not first in the share certificate) | No | **No (hard block)** | Per bye-laws | No | No | Per Act |
| Non-voting shareholder (MSCS s.26 proviso) | No | **No (hard block)** | Per bye-laws | No | No | Per bye-laws |
| Institutional member (another society, government) | Per bye-laws | [VERIFY] | Per bye-laws | No | Through representative | Yes |

"Active member" concepts exist in several State Acts (voting rights tied to minimum use of services or attendance) — e.g., Maharashtra ss.26–27 [VERIFY]; the State pack sets eligibility rules for voter lists.

---

## S.5 Credit co-operative society — operating model (modus operandi)

### S.5.1 Formation and constitution
Promoters (minimum number per Act; MSCS requires members from at least two States) adopt bye-laws (often the Registrar's model bye-laws for thrift and credit/urban credit societies), define the area of operation (city/district/State; employer for salary-earners' societies), raise share capital, and apply for registration. The managing committee/board is elected from members; the society employs a CEO/manager, accountant, clerks and often daily-deposit collection agents ("pigmy" agents) [PRAC].

### S.5.2 Members, shares and deposits
- **Admission:** application with KYC, area/employment proof, introducer (often), admission fee and minimum shares; committee approval.
- **Share capital:** face value (₹10–₹100 typical [PRAC]); minimum holding; loan-linked share holding (e.g., a percentage of the loan or a multiple of share value as the borrowing ceiling) per bye-laws; holding cap (e.g., one-fifth of total capital) [LAW/bye-law].
- **Deposit products (voting members only):** savings, current (some societies), fixed deposits, recurring deposits, cumulative/re-investment deposits, daily deposits collected by agents, special schemes; interest rates set by the board within Registrar guidelines where issued [PRAC; VERIFY State circulars].
- **Liquidity:** statutory liquidity/cash reserve requirements under the State Act or CRCS orders (e.g., Maharashtra SLR ≥ 25% of deposits; CRCS cash ≥ 2% and liquid investments rising to 18% for credit MSCS) [LAW/REG; VERIFY].

### S.5.3 Lending to members
| Product | Typical security | Notes |
|---|---|---|
| Loan against own FD/RD | Lien on deposit (e.g., up to 90% — MCS Rule 45A) | Low risk; most common |
| Gold loan | Pledge of gold ornaments; valuer certificate | Purity testing; auction rules per bye-laws |
| Personal/surety loan | Two (or more) member sureties | Surety liability ledger; live-guarantee caps [PRAC] |
| Salary-deduction loan (salary-earners' societies) | Employer deduction authority | Employer remittance reconciliation |
| Vehicle, consumer durable | Hypothecation | |
| Housing/mortgage (larger societies) | Equitable or registered mortgage; MSCS caps by size class | CRCS housing caps |
| Business/MSME | Hypothecation, mortgage, sureties | Concentration limits |
| Microfinance-style group loans | Peer guarantee (voluntary) | Conduct overlays |

**Process [PRAC]:** application → membership and share-linkage check → document collection → appraisal (income, other society borrowings declaration, e.g., Maharashtra MCS Rule 45) → sureties' consent → loan committee/board sanction (director recusal for related parties) → agreement and security documents → disbursal to the member's bank/savings account → instalment collection (branch, agents, salary deduction, ECS/NACH) → overdue follow-up → statutory recovery.

**Interest:** board-fixed within bye-laws and any Registrar ceilings; penal interest per bye-laws; disclosure of all charges [REC: KFS-equivalent loan disclosure sheet].

### S.5.4 Recovery
Reminders and surety notices → board resolution → statutory route: Maharashtra — recovery certificate under s.101 for notified classes (enforceable as arrears of land revenue) or dispute to the Co-operative Court (s.91) with execution (s.98); MSCS — arbitration (s.84); other States per Act. Civil courts are generally barred for disputes within the statutory forum; SARFAESI and DRT are not available to credit societies (they are not "banks" or "financial institutions" for those statutes) [LAW; VERIFY per State]; s.138 NI Act cheque-dishonour cases remain available.

### S.5.5 Year-end
Provisioning for overdue/NPA loans (State circulars; often 90 days for NPA classification [VERIFY]) → net profit → appropriation (statutory funds) → dividend (within cap; to members on year-end holdings) → audit by panel auditor → audit report and class → AGM approval → annual return to Registrar → rectification report.

### S.5.6 Governance cadence
Monthly or quarterly managing-committee meetings; loan committee weekly; AGM annually; elections every 5 years through the election authority; Registrar inspections; members' right to information (Information Officer in MSCS).

### S.5.7 Relationship with RBI-regulated entities
Credit societies are **not** RBI regulated entities and cannot be co-lending partners, transferors/transferees of loans, or DLG providers for NBFCs (TDCR paras 7, 12(4), 97; CF para 19). Lawful alternatives: wholesale borrowing from an NBFC/bank within the society's borrowing limits; acting as a sourcing agent for an NBFC (NBFC sole lender, under its outsourcing controls); independent parallel loans (Finbyx IP2.13) [REC; counsel to confirm]. A credit society that wishes to become a UCB needs an RBI licence — outside LDC beyond a readiness checklist.

### S.5.8 Annual compliance calendar — credit society (template; State pack sets dates)

| When (FY = April–March) | Item | Owner | Basis |
|---|---|---|---|
| Monthly | Managing-committee/board meeting; loan sanction register review; overdue and NPA review; deposit-eligibility exception review; liquidity/SLR check; staff and agent cash reconciliation | Secretary / CEO | Bye-laws; State Act; CRCS order (MSCS) |
| Quarterly | CRCS prudential return (credit MSCS); CRAR, leverage, exposure and unsecured-loan checks; director/relative loan report to board; TDS statements | CEO / accountant | CRCS order 22 Jan 2024 [VERIFY]; Income-tax |
| 1 April | Year-end cut-off; provisioning; share and deposit interest accruals | Accountant | Bye-laws; State circulars |
| April–June | Draft accounts; appointment/confirmation of panel auditor; audit fieldwork | Board / auditor | MSCS s.70; MCS s.75, 81 |
| By 31 July (MH: within 4 months) | Audit report received | Auditor | MCS s.81 [VERIFY] |
| Within 3 months of audit report (MH) | Rectification report (Form O) | Secretary | MCS s.82 |
| By 30 September (MSCS: within 6 months; MH: by 30 Sep) | AGM: accounts, audit report, appropriation, dividend, budget, auditor, bye-law amendments, write-offs | Board | MSCS s.39; MCS s.75 |
| Within 30 days of AGM | Minutes signed; auditor appointment intimated; dividend paid | Secretary | Bye-laws; MCS s.81 |
| By 30 September (MSCS: within 6 months of FY close) | Annual return to Registrar/CRCS | CEO | MSCS s.120; MCS s.79(1A) |
| By the income-tax due date | ITR with co-operative deduction | Accountant | ITA 2025 [VERIFY] |
| 6 months before board term ends (MSCS) | Inform the Co-operative Election Authority | Board | MSCS s.45J(8) [VERIFY] |
| Event-based | Admission decisions within statutory window; bye-law amendment filings; change in office bearers intimation; Registrar inspection responses; complaint replies | Secretary | Act and Rules |

### S.5.9 Inspection-ready pack (what a Registrar inspector asks for)

Registration certificate and bye-laws (current and amendments with registration letters); member register, share register and nomination register; list of directors with declarations; minutes books (general body, board, committees); audit reports of the last three years with rectification reports and audit class; annual returns filed with acknowledgements; deposit register summary with eligibility confirmation; loan register with director/relative loans; NPA and provisioning working; statutory funds statement; investment register (statutory liquidity); cash and bank reconciliations; staff and agent list; complaints register; Registrar's previous inspection report and compliance. LDC generates this as an **Inspection Pack** export (P19 co-operative profile) with a manifest and hash list (NN-09).

### S.5.10 Registers and forms catalogue (seed)

| Register / form | MSCS (Rules 2023) | Maharashtra (Rules 1961) |
|---|---|---|
| Register of members | Prescribed register [VERIFY form] | Form I; list of members Form J; Form J-1 (members with voting right) [VERIFY] |
| Share register | Yes | Yes |
| Nomination register | Yes | Yes |
| Register of directors/committee members | Yes | Yes |
| Minutes books | General body; board; committees | Same |
| Loans to directors and relatives | Disclosed in annual report (s.39(3)) | Bye-laws; Chapter XI-1A for credit societies |
| Audit class form | — | Form N-2 marks [VERIFY] |
| Rectification report | Per Rules [VERIFY] | Form O |
| Annual return | CRCS online form | Statements under s.79(1A) |
| Election forms | Per CEA rules | Election Rules 2014 forms |

All registers are generated from the event log (P16 FR-P16-26), printable in the prescribed format and exportable as XLSX/PDF with an "as at" date.

---

## S.6 Pain points and product responses

| Pain point (observed) | Consequence | LDC response |
|---|---|---|
| Paper registers, incomplete member records | Disputes, election challenges, audit paras | Register engine; OCR digitisation with verification (P16 §11); immutable history |
| Late AGMs and annual returns | Director disqualification; Registrar action | Clocks with escalation; disqualification watch dashboard |
| Deposits from nominal/associate members or non-members | Unlicensed banking; depositor loss; RBI caution | Deposit-eligibility exceptions mirrored from Finbyx as Critical issues; board agenda item until zero |
| Related-party and director loans | Fraud, evergreening | Director/relative loan register and cap; recusal in minutes; reporting to AGM |
| Unrectified audit paras for years | Downgraded audit class; inspection | Para tracker with owners and Form O/rectification generation |
| Weak liquidity and ALM | Runs on deposits | Prudential monitors (CRCS/State) with board dashboards |
| Bye-laws out of date with the Act | Invalid decisions | Bye-law layer with "loosening blocked" check and amendment workflow |
| Elections delayed or disputed | Administrator appointed | Term tracker; voter-list generation with eligibility reasons; authority notices |
| No member grievance channel | Complaints escalate to media/court | Grievance desk with Ombudsman/Registrar routing |
| Staff turnover; dependence on one accountant | Lost knowledge | Task system, SOPs, Vidhi notebook on the society's Act and bye-laws |
| Vernacular needs | Low adoption | Hindi/Marathi UI and notices; translation workflow |
| Fear of regulators' inspections | Last-minute scramble | Inspection-ready export pack; time-boxed Registrar view |

---

## S.7 State-pack variable matrix

Each State pack fills these variables; MSCS and Maharashtra values are shown (all marked values require final verification before hard blocks).

| Variable | MSCS | Maharashtra |
|---|---|---|
| Governing law | MSCS Act 2002 (am. 2023), MSCS Rules 2023, CRCS orders | MCS Act 1960, MCS Rules 1961, Election Rules 2014 |
| Registrar | Central Registrar (CRCS) | Commissioner/Registrar of Co-operative Societies, Maharashtra; divisional/district registrars |
| Member classes | Ordinary; non-voting shareholder (s.26); nominal/associate per bye-laws | Active/non-active; nominal; associate (joint holder) |
| Admission timeline | 4 months + 15 days communication; deemed refusal (s.25(4)) | Per s.22 and Rules [VERIFY] |
| Board size and reservations | ≤ 21; 1 SC/ST, 2 women; co-opted experts (s.41) | Per s.73AAA [VERIFY] |
| Term | 5 years | 5 years [VERIFY s.73AAA] |
| Election authority and notice | Co-operative Election Authority; 6 months before term (s.45J(8)) | State Co-operative Election Authority (s.73CB); per Election Rules 2014 [VERIFY] |
| AGM deadline | Within 6 months of FY close (s.39) | On or before 30 September (s.75) [VERIFY] |
| AGM notice / quorum | 14 days (7 for special) / one-fifth [VERIFY] | Per bye-laws and Rules [VERIFY] |
| Reserve fund | ≥ 25% (s.63) | ≥ 25%; Registrar may permit ≥ 10% (s.66(2)) |
| Other statutory funds | Education 1%; unforeseen losses ≥ 10%; CRRD (s.63A) | Education fund to federation (s.68) [VERIFY rate] |
| Dividend cap | As prescribed [VERIFY] | ≤ 15% without Registrar sanction (s.67) |
| Auditor | Central Registrar's panel; special panel > ₹500 crore (s.70) | State panel; appointed at AGM; ≤ 3 consecutive years; intimation within 1 month (ss.75, 81) [VERIFY] |
| Audit timeline | Report within 6 months [VERIFY] | Within 4 months of FY end (s.81) [VERIFY] |
| Concurrent audit | > ₹500 crore turnover/deposits (s.70A) | [VERIFY] |
| Audit class | — | A–D (Rule 69, Form N-2) [VERIFY bands] |
| Rectification | Per Rules [VERIFY] | Form O within 3 months (s.82) |
| Annual return | Within 6 months via CRCS portal (s.120) | Within 6 months (s.79(1A)) |
| Dispute forum | Arbitration (s.84) | Co-operative Court (s.91); limitation s.92; appeal s.96 |
| Recovery | Award execution [VERIFY] | s.101 recovery certificate; s.98 execution |
| Credit-society prudential chapter | CRCS order of 22 Jan 2024 | Chapter XI-1A (ss.144-1A–144-30A) |
| Grievance escalation | Co-operative Ombudsman (s.85A) | Registrar [VERIFY other mechanisms] |
| Languages | English, Hindi | Marathi, English, Hindi |
| Portals | CRCS MSCS portal | Maharashtra Sahakar Ayukta portal [VERIFY name] |

---

### S.7A Seed variables for further State packs (review addition, 25 October 2026)

Values below come from the Act text as published by the Registrar (Delhi, extract of 2006) or from secondary summaries (Rajasthan). They are `SECONDARY_ONLY` — later amendments must be checked before any value becomes a hard rule (NN-38). Other stub States (Gujarat, Uttar Pradesh, Karnataka, Madhya Pradesh, Telangana/Andhra Pradesh, Bihar, Kerala, Tamil Nadu) are filled the same way by the content team in the P16 sprint that enables them.

| Variable | Delhi (Delhi Co-operative Societies Act 2003; Rules 2007) | Rajasthan (Rajasthan Co-operative Societies Act 2001; Rules 2003) |
|---|---|---|
| AGM deadline | Within 90 days after the date fixed for making up accounts (s.31(1)); Registrar may convene on default (s.31(2)) | Within three months after the date fixed for preparing annual accounts (Rules r.30 [VERIFY]); notice 7 clear days unless bye-laws differ |
| Committee size and term | Bye-laws fix size, not more than 21 (s.11(2)(t)); elected members serve three years (s.35(3)) [VERIFY amendments after 2011 for a five-year term] | [VERIFY] |
| Reservation | Seats for SC, OBC and women where the Government holds share capital, and two seats for women in all societies (s.35(8)) [VERIFY ST] | [VERIFY] |
| Government nominees | 1 (equity < 26%), 2 (26–51%), 3 (≥ 51%); not more than one-third of the committee or three, whichever is less (s.35(10)) | [VERIFY] |
| Elections | Conducted under the committee's supervision by secret ballot (s.35(1)–(2)); on failure the Registrar appoints an administrator who holds elections within 90 days (s.35(4)–(5)) [VERIFY whether a State election authority now conducts] | State Co-operative Election Authority for notified categories [VERIFY section] |
| Reserve and other funds | ≥ one-fourth of net profit to the reserve fund before distribution (s.53); up to 5% for charitable/co-operative development (s.54); up to 5% to the Co-operative Education Fund (s.55) | [VERIFY] |
| Audit | By an auditor from the Registrar's panel within 60 days of the close of the co-operative year (31 March) (s.60(1)); report placed at the AGM and copied to the Registrar; Registrar arranges a late audit at the cost of responsible officers (s.60(5)–(6)) | Within six months of the close of the financial year by an auditor/firm from the approved panel (s.54 [VERIFY]); continuous appointment limit [VERIFY] |
| Annual return | Within 30 days of the AGM in the prescribed form (s.32) | Within the prescribed period (Rules r.107 [VERIFY]) |
| Inspection | On request of a creditor, one-third of the committee or one-fifth of members (s.61(1)); copy of the report to the society within 90 days of completion (s.61(4)) | [VERIFY] |
| Disputes | Arbitration council of three appointed by the Government (s.71); appeal to the Delhi Co-operative Tribunal (ss.112, 114); appeal against expulsion within 60 days (s.40(4)) | Disputes provisions of the Act [VERIFY sections] |
| Recovery | Loan charges recoverable as arrears of land revenue on the Registrar's certificate (ss.45(vii), 108, 111) [VERIFY full text] | [VERIFY] |
| Languages | Hindi, English | Hindi, English |
| Registrar | Registrar of Co-operative Societies, GNCT Delhi (rcs.delhi.gov.in) | Registrar, Co-operative Societies, Rajasthan |

## S.8 Other society types — operating notes

| Type | Operating essentials | Typical compliance and pain points |
|---|---|---|
| Co-operative housing society | Members are flat/unit owners holding shares; managing committee; maintenance, sinking and repair funds; parking; transfer of flats with transfer fee/premium per bye-laws; NOCs; conveyance/deemed conveyance; redevelopment by special general body with prescribed consent and Registrar directives (State-specific) [VERIFY MH s.154B and redevelopment directives] | Late audits, disputes on maintenance and transfers, redevelopment consent records, AGM quorum |
| PACS (Primary Agricultural Credit Society) | Short-term crop loans via DCCB refinance; increasingly multipurpose (CSC, PDS, fertiliser, Jan Aushadhi, storage); national ERP | Data held in the national ERP; LDC is a compliance/governance layer (adapter) |
| Dairy co-operative | Milk procurement, pricing, payments to members; district unions and State federations | Member records, AGM, audit; FSSAI as overlay |
| Consumer co-operative | Retail stores; members get dividends/rebates | GST, FSSAI, shops and establishments, labour |
| Marketing/processing | Collective marketing; APMC interplay | Licences; GST |
| Fisheries | Licences, leases of water bodies, FFPO conversion | Lease registers; scheme compliance |
| Labour/contract co-operatives | Work contracts with government departments | Labour codes overlay; contract registers |
| Federal co-operatives | Societies as members; delegates | Representation rules; inter-society transactions |


---

## S.9 Data protection for co-operatives
- Member registers contain personal data (name, address, phone, nominee, shareholding, sometimes caste/category for reservation eligibility of directors). Category data is processed only where the Act requires it (board reservations) and is restricted (NN-13 sealed class if sensitive) [REC].
- Aadhaar is never stored in full; use masked reference or offline verification evidence (NN-12).
- Voter lists shared with the election authority under statutory obligation; watermark and log every export.
- Retention follows the Act/Rules (registers and minutes permanently in many Acts [VERIFY]); DPDP erasure requests are refused where statutory retention applies, with a recorded reason.

---

## S.10 Glossary (vernacular terms used in UI and notices)

| Term | Meaning | Language |
|---|---|---|
| Sahakari sanstha / Sahakari samiti | Co-operative society | Marathi / Hindi |
| Patsanstha (nagari / grameen / pagardar) | Credit society (urban / rural / salary-earners') | Marathi |
| Sabhasad | Member | Marathi / Hindi |
| Namdhari sabhasad | Nominal member | Marathi |
| Sanchalak mandal / Prabandh samiti | Board / managing committee | Marathi / Hindi |
| Adhyaksha / Upadhyaksha | Chairperson / Vice-chairperson | Hindi / Marathi |
| Sachiv / Koshadhyaksh | Secretary / Treasurer | Hindi |
| Vaarshik sarvasadharan sabha | Annual general body meeting | Marathi |
| Upvidhi | Bye-laws | Marathi / Hindi |
| Lekhaparikshan / Vaidhanik lekhaparikshan | Audit / statutory audit | Marathi |
| Dosh durusti ahwal | Rectification report | Marathi |
| Nibandhak | Registrar | Hindi / Marathi |
| Thev | Deposit | Marathi |
| Jamindar | Surety | Marathi / Hindi |
| Vasuli | Recovery | Marathi / Hindi |
| Pigmy / Dainik thev | Daily deposit scheme | Common usage |

(Translations are UI labels and must be reviewed by a native speaker before release [REC].)

---

## S.11 Design consequences (summary for engineers)
1. Co-operative law is **per society**: Act + Rules + Registrar orders + bye-laws, layered with tighten-only semantics (P16 FR-P16-03).
2. **System of record** for members and shares is configurable (Finbyx / LDC / external), never duplicated (P16 FR-P16-05).
3. Statutory **clocks** (admission, AGM, election notice, audit, rectification, returns) are first-class and drive disqualification risk for directors.
4. **Guard-rails** (name, deposits, co-lending, own-share security, statutory forum, Ombudsman routing) are Locked and visible.
5. The **election** is the authority's; LDC supports the society's duties and records.
6. **Vernacular** and low-bandwidth operation are product requirements, not translations added later.
7. **STUB** State packs never block operations; they make legal clocks configurable tasks until counsel completes them.

---


## S.11A Member self-service, multilingual notices and electronic meetings *(v1.1)*

| Topic | Position for the product | Status |
|---|---|---|
| Delivery of general-body notices | Bye-laws and Acts prescribe modes (registered post, notice board, newspaper, and increasingly e-mail/SMS); LDC sends on every configured channel and keeps delivery evidence; the State pack lists the minimum legally recognised modes | [LAW] per State; [VERIFY] e-delivery recognition per State |
| Electronic participation in general bodies and committee meetings | Some States and the MSCS framework permit or have permitted video-conference participation and e-voting for certain bodies; others are silent → LDC supports hybrid meetings but marks electronic attendance/voting as "permitted under <citation>" only when the State pack says so | [VERIFY per State — counsel question 9 in `02` §5] |
| Member portal content | Own profile, nominee, share certificate, notices, AGM papers, complaint, inspection request; never other members' personal data (NN-13) | [REC] |
| WhatsApp | Service notices only via approved templates; never demand, recovery or legal notices (X-23) | [REC] |
| Vulnerable members | Large print, audio versions, assisted acknowledgement at branch | [REC] (NN-21) |

## S.11B Office-bearer functions (typical bye-law allocation) *(v1.1)*

| Office | Typical functions under bye-laws (State Act and bye-laws prevail) | LDC workbench (P16 §4S) |
|---|---|---|
| President / Chairperson | Presides over committee and general body; casting vote; signs minutes; represents society | Board agenda, approvals, disqualification watch, audit class trend |
| Vice-President | Acts in President's absence | Delegation |
| Secretary / Chief Executive | Custody of records and registers, correspondence with Registrar, convening meetings on direction, statutory returns, staff supervision | Statutory calendar, registers, returns, complaints, Registrar tracker |
| Treasurer | Custody of cash and securities as allowed by bye-laws, funds and reserves appropriation as resolved by the general body, investment of funds as permitted by the Act, bank reconciliation, presentation of accounts | Funds and reserves view, appropriation status, investment-of-funds compliance, reconciliation evidence (books in Finbyx/accounting system) |
| Managing committee members | Collective decisions; sub-committees (loan, recovery, audit, grievance) | Committee pages (P06 mechanics) |

## S.11C Registrar inspection, inquiry and members' inspection rights — reference *(v1.1)*

| Power / right | MSCS Act 2002 (as amended 2023) | Maharashtra Co-operative Societies Act 1960 | Generic State default |
|---|---|---|---|
| Members' right to inspect records and obtain copies | Section on inspection of documents/members' access [VERIFY section] | s.32 — members may inspect specified documents and obtain copies on payment of fees [VERIFY scope] | Bye-laws; State pack sets documents, fees, response time |
| Inspection of the society's books by the Registrar | Central Registrar's inspection powers [VERIFY section] | s.89A (inspection of working) [VERIFY] | State pack |
| Inquiry into constitution, working and financial condition | s.108 (inquiry) [VERIFY] | s.83 (inquiry) [VERIFY] | State pack |
| Surcharge / recovery from persons responsible for loss | [VERIFY section] | s.88 [VERIFY] | State pack |
| Rectification of audit defects | Report to the general body and Central Registrar [VERIFY section and time limit] | s.82 rectification report within three months of receipt of the audit report [VERIFY form and time] | State pack |

LDC behaviour: tracker items, clocks (NN-33), evidence and draft replies; no legal position is taken by AI (NN-47); contentious proceedings become P26 legal matters.

## S.11D Audit-para tracker data model *(v1.1)*

`coop.audit_reports` (year, auditor, audit class, report file hash, received_at) → `coop.audit_paras` (para no, text (OCR, confirmed), amount, category: accounts/recovery/governance/investments/KYC/other, repeat_of_para_id, owner_id, action, due_at, status OPEN/IN_PROGRESS/RECTIFIED/DISPUTED/CLOSED, evidence_ids[]) → `coop.rectification_reports` (format code per State pack, generated_at, approved_by (committee resolution link), dispatched_at, ack_ref). Roll-ups: paras by category and status; amount at risk; repeat-para ratio (an indicator of governance quality used in P08 KRIs for societies).

## S.11E Language coverage *(v1.1)*

Priority order for templates and member-portal UI: Hindi (all Hindi-belt States; D-30), Marathi (Maharashtra — largest credit-society base), Gujarati, Kannada (Souharda societies), Tamil, Telugu, Bengali, Malayalam, Punjabi, Odia. Each language needs: notice templates, minutes extract template, member letters, vernacular glossary (§S.10) and a human reviewer for statutory text (no unreviewed machine translation of statutory notices).

## S.12 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-S-01 | Verify all MSCS section numbers cited (ss.25, 26, 39, 41, 43, 45, 45J, 63, 63A, 66, 67, 70, 70A, 84, 85A, 108, 120) against the consolidated Act | Co-op counsel | Instrument-level citations |
| OI-S-02 | Obtain CRCS orders (22 Jan 2024; July 2025) and model bye-laws for thrift and credit MSCS | Content | Monitors advisory only |
| OI-S-03 | Maharashtra values: audit-class bands, Chapter XI-1A percentages, AGM/audit/rectification timelines, election-rule classification | MH counsel | Governed values with [VERIFY] |
| OI-S-04 | Nine STUB State packs | Counsel per onboarding | Configurable clocks |
| OI-S-05 | *Rajendra N. Shah* citation and State mirror provisions | Content | Case name only |
| OI-S-06 | Income-tax Act 2025 successor to s.80P | Tax | Generic label |
| OI-S-07 | Registers and minutes retention periods per Act | Content | Permanent retention default |
| OI-S-08 | Virtual general meetings permissibility per Act | Content | Flag OFF |
| OI-S-05 *(v1.1)* | Members' inspection rights, Registrar inspection/inquiry/surcharge and rectification sections for MSCS and each State pack | Co-op law analyst | Advisory tracker with [VERIFY] citations |
| OI-S-06 *(v1.1)* | Electronic meetings and e-voting permissibility per State | Counsel | Hybrid meetings labelled "subject to State law" |

---

## S.13 Sources (accessed 25 October 2026 unless stated)
1. Ministry of Cooperation / PIB document (Feb 2026) on National Cooperation Policy 2025, National Cooperative Database, PACS computerisation, Co-operative Ombudsman (notified 5 Mar 2024), CEA elections — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc202624779801.pdf
2. Indian Cooperative, "Post-MSCS Amend Act 2023: 197 Elections held, 113 Co-ops Liquidated" — https://www.indiancooperative.com/from-states/post-mscs-amend-act-2023-197-elections-held-113-co-ops-liquidated/amp
3. MSCS (Amendment) Act 2023, Gazette — https://egazette.gov.in/WriteReadData/2023/247816.pdf ; Central Registrar of Co-operative Societies — https://crcs.gov.in
4. Maharashtra Co-operative Societies Act, 1960 (India Code) — https://www.indiacode.nic.in/bitstream/123456789/15836/3/maharashtra.pdf
5. Case commentary on s.101 vs s.91 MCS Act — https://www.casemine.com/commentary/in/supremacy-of-section-101-over-section-91-in-maharashtra-co-operative-societies-act/view ; recovery certificate reasons requirement — https://rawlaw.in/recovery-certificate-under-section-101-set-aside-bombay-high-court-holds-that-recording-of-reasons-is-a-fundamental-requirement-and-directs-denovo-inquiry-for-non-compliance-with-ru/
6. Adarsh Credit Co-operative Society — CRCS notices — https://www.indiancooperative.com/featured/massive-fraud-central-registrar-serves-notice-on-adarsh-credit-co-op/amp
7. Finbyx Master Prompt v1.5 Part 7G IP1–IP2 and Integration Specification v1.1 §6.24 (owner's corpus) — verified/secondary positions on MSCS, Maharashtra, CRCS orders, BUDS, DICGC, guard-rails.
8. Constitution of India, Seventh Schedule List I entry 44, List II entry 32; Part IXB; *Union of India v. Rajendra N. Shah* (SC, 2021) [VERIFY].
9. Delhi Co-operative Societies Act 2003, text extracted from the Registrar of Co-operative Societies (NCT Delhi) site, mirrored at https://kangra.bank.in/linksfiles/dcsact2003.htm (accessed 25 Oct 2026).
10. Rajasthan Co-operative Societies Act 2001 summary, https://www.nobrokerhood.com/blog/rajasthan-cooperative-society-act/ (secondary; accessed 25 Oct 2026).
