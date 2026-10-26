# Appendix S — Consumer Help Rules and Playbooks

**Status:** Binding (rule rows are content data; each row ships advisory-only until verified — NN-38).
**Used by:** P15 (primary), P10 (letter templates), P16 (advocate engagements), P03 (rule engine data load), P05 (evidence), P08 (authority letters, vehicle agreements), P21 (Consumer Help brand pages and copy), P23 (verification log audit).

**How to use.** This appendix is the seed content for the `[Consumer Help Brand]` rule engine and playbooks. Load every table row in §S.3–§S.9 into `rul` as an effective-dated, versioned decision row with a reviewer of record (NN-30). A row tagged `[VERIFY]` loads with `advisory_only = true`: the product may show it as guidance with an "unverified" label, but may not compute a binding deadline, block an action or draft a citation from it until `PLT_LEGAL_REVIEWER` verifies it against the primary source and logs the check in `docs/compliance/verification-log.md`. Research source codes (S1…S51) refer to the source list in `R2_Consumer_Help_Verticals.md` §8; LG-xxx codes refer to R3. Nothing here is legal advice to a consumer. Consumer-facing copy is written separately in P21 and must pass the banned-phrase lint (§S.11.3).

---

## S.1 Rule-row format

| Field | Content |
|---|---|
| `rule_id` | `CHR-<vertical>-<nn>` (A loans, A2 credit reports, B insurance, CC consumer commission, C challans, D vehicles, X cross-vertical) |
| `instrument`, `provision` | Exact instrument and clause, rule or paragraph |
| `effective_from`, `effective_to` | Dates; transition rows where an older instrument still governs earlier cases |
| `parameter`, `value`, `unit` | e.g., `rbio_filing_window`, 90, calendar days |
| `computation` | Clock start event, "later-of" logic, calendar or working days |
| `jurisdiction` | National or State code |
| `source`, `confidence` | R2 source code; `V-REG` (regulator text), `V-SEC` (secondary), `UNVERIFIED` |
| `verify_note` | What to check and where |
| `reviewer_id`, `verified_at` | Reviewer of record |

---

## S.2 Representation and filing matrix (enforced by `chp.representation_matrix`)

| Forum | Who files | Non-advocate case manager | Advocate | Authority document | Source |
|---|---|---|---|---|---|
| RE grievance officer / nodal officer (bank, NBFC, PPI issuer, CIC) | User | May correspond and file with written authority | May act | Limited authority letter (non-POA) | R2 §5.3 |
| Internal Ombudsman of the RE | Not filed by anyone; auto-escalated by the RE | — | — | — | RBI Internal Ombudsman Directions 2026 (S16) |
| RBI Ombudsman (RB-IOS 2026) | User (recommended) | **Yes**, as authorised representative appointed in writing (Cl. 3(1)(c)) | **No**, unless the advocate is the aggrieved person (Cl. 10(1)(b)) | T-A4 | S1, S2 |
| Appellate Authority under RB-IOS 2026 | User | [VERIFY whether representation follows the Ombudsman rule] | [VERIFY] | — | S1 |
| Insurer GRO | User | May correspond with authority | May act | Authority letter | S41 |
| Bima Bharosa / IRDAI | User | [VERIFY] | [VERIFY] | — | S9 |
| Insurance Ombudsman | User or legal heir, nominee or assignee (R.14(1)) | **No** (not provided for) [VERIFY CIO practice] | At the adjudication stage (R.17) per Karnataka HC DB, 1 Jul 2026; persuasive elsewhere [VERIFY] | — | S8, S10 |
| Consumer Commission (e-Jagriti) | User or advocate | Only as an agent under the 2014 agent regulations on the party's own authenticated authorisation; never on an advocate's authority letter (*Anuj Kumar Chauhan*, Delhi HC, Dec 2024) | Yes, vakalatnama | Party authorisation [VERIFY form] | S14 |
| National Consumer Helpline | User | May assist the user to lodge | — | — | S42 |
| Virtual Court (traffic) | User | No | Yes | Vakalatnama for contest | S29, S43 |
| Physical court (traffic, non-compoundable) | User / advocate | No | Yes | Vakalatnama | S43 |
| Traffic Lok Adalat | User (OTP slot booking) | [VERIFY] | Yes | — | S46 |
| Police / cyber-crime complaint | User | Drafts only | Advises | — | R2 §1(c) |
| RTO / Vahan | Owner, buyer (OTP to registered mobile) | Agent per State practice | — | Authority or POA per State [VERIFY stamp] (POA → wet-ink, NN-07) | S35 |

---

## S.3 Vertical A — Loans and lending

### S.3.1 Eligibility and scope rules

| Rule | Content | Source / tag |
|---|---|---|
| CHR-A-01 | Covered REs under RB-IOS 2026 Cl. 1(3): commercial banks, RRBs, State and central co-operative banks, scheduled UCBs, non-scheduled UCBs with deposits ≥ ₹50 crore; NBFCs that take deposits, or have a customer interface **and** assets ≥ ₹100 crore (excluding HFCs, core investment companies, IDF-NBFCs, NBFC-IFCs, NOFHCs, primary dealers, mortgage guarantee companies); non-bank PPI issuers; credit information companies | [LAW] S1, S2 |
| CHR-A-02 | Out-of-scope RE (e.g., non-deposit NBFC with assets < ₹100 crore) → route: RE grievance officer → RBI CEPD/CMS general complaint → consumer commission | [INTERP] S1 [VERIFY residual route] |
| CHR-A-03 | User cannot tell whether the RE is covered → state "unknown — file anyway; the RBI system validates" and record the uncertainty | [REC] R2 §1(c) |
| CHR-A-04 | Maintainability (Cl. 10(1)): complaint first made to the RE; no reply within 30 days (or longer RBI/NPCI/card-network TAT) or unsatisfactory reply; complaint to the RE within limitation; not pending or decided before a court, tribunal, arbitrator, consumer commission or other forum (Cl. 10(1)(h)–(k)); not abusive or frivolous | [LAW] S1, S2 |
| CHR-A-05 | Excluded (Cl. 10(2)): commercial judgment of the RE, vendor disputes, management grievances, actions under legal orders, employer–employee disputes, CICRA s.18 matters. Criminal or police proceedings do not count as "the same grievance" | [LAW] S1 |
| CHR-A-06 | Unregistered lender or app → no RB-IOS route; illegal-app track: RBI Sachet (sachet.rbi.org.in) for unauthorised entities [VERIFY URL behaviour], cyber-crime portal / 1930 for extortion or morphing [VERIFY], local police | S18, S19 |
| CHR-A-07 | Transition: complaints received by RBI before 1 Jul 2026 remain under RB-IOS 2021 | [LAW] S1 |
| CHR-A-08 | Language: CMS accepts Hindi and English; email and post accept any language; contact centre 14448 gives information only | [LAW] S1 |

### S.3.2 Time limits

| Rule | Clock | Value | Start event | Source |
|---|---|---|---|---|
| CHR-A-10 | RE reply period | 30 days (or longer TAT where RBI/NPCI/card network prescribes) | RE receipt of complaint (acknowledgement; else dispatch proof + transit allowance `chp.deadline.transit_days`, default 3 [REC]) | S1; DL Directions 2025 para 11 (S13) |
| CHR-A-11 | Internal Ombudsman | Final reply to customer within 30 days of receipt by the RE; IO gets ≥ 10 or 20 days depending on TAT | RE receipt | S16 [VERIFY effective date] |
| CHR-A-12 | RBIO filing window | 90 days after the later of (a) reply-period expiry or (b) the RE's last communication | Computed | Cl. 10(1)(g) (S1, S2) |
| CHR-A-13 | RE response to Ombudsman | 15 days | RBIO notice to RE | Cl. 14(2) |
| CHR-A-14 | Award acceptance by complainant | 30 days from receipt of award, else lapses | Award receipt | Cl. 15(4) |
| CHR-A-15 | RE compliance or appeal | 30 days from complainant's acceptance | Acceptance | Cl. 15(5) |
| CHR-A-16 | Complainant's appeal | 30 days from award, extendable by 30 days | Award date | Cl. 17(3) |
| CHR-A-17 | Document release and charge removal after closure (NBFC) | 30 days; ₹5,000 per day for delay attributable to the NBFC | Full repayment and closure | NBFC RBC Directions 2025 paras 35–41 (S15) [VERIFY para numbers and application to movable-property hypothecation] |
| CHR-A-18 | Consumer commission limitation | 2 years from cause of action | Cause of action | CPA 2019 s.69 [VERIFY condonation practice] |

### S.3.3 Recovery-conduct rules (effective-dated)

| Rule | Content | Effective | Source |
|---|---|---|---|
| CHR-A-20 | Calling and visiting hours 08:00–19:00 unless the borrower expressly authorises otherwise | Before 1 Jan 2027: existing RBI guidance to REs employing recovery agents [VERIFY circular and date]; from 1 Jan 2027: RBC Fourth Amendment (banks, RBI/2026-27/223) and Third Amendment (NBFCs), both 6 Aug 2026 | S11, S12 |
| CHR-A-21 | Microfinance loans: 09:00–18:00 | [VERIFY para 91 and effective date] | S15 |
| CHR-A-22 | Prohibited conduct: abuse, threats, public shaming, posting borrower details on social media, false statements about the debt; for NBFCs also harassing relatives, friends or co-workers, anonymous or excessive calls | From 1 Jan 2027 (amendment text); earlier fair-practice guidance [VERIFY] | S11, S12 |
| CHR-A-23 | Agent must carry ID card, authorisation letter and copy of the RE's notice; NBFC agents also agency and grievance-officer contacts | From 1 Jan 2027 | S11, S12 |
| CHR-A-24 | IIBF Debt Recovery Agent certificate; existing NBFC agents get one year from 1 Jan 2027 | From 1 Jan 2027 | S11, S12 |
| CHR-A-25 | Agency details to the borrower at least 1 day before the first in-person visit; RE website list updated within 7 days | From 1 Jan 2027 | S11, S12 |
| CHR-A-26 | Bank recovery calls recorded and kept 6 months (longer if sub judice); NBFC equivalent [VERIFY] | From 1 Jan 2027 | S11, S17 |
| CHR-A-27 | No referral to a recovery agency while a related grievance is unresolved | [VERIFY final text] | S17 (draft) |
| CHR-A-28 | Digital loans: agent particulars sent to the borrower by email or SMS before contact | In force (DL Directions 2025 para 8(v)) | S13 |
| CHR-A-29 | Criminal overlay: threats of arrest over a civil debt may be criminal intimidation (BNS 2023 s.351) | [VERIFY]; drafting points only, police decides | S4 |

### S.3.4 Digital lending rules (DL Directions 2025, 8 May 2025; S13)

| Rule | Content |
|---|---|
| CHR-A-30 | DLA may not access files, media, contacts, call logs or telephony; camera, microphone and location only once for KYC (para 12). Contact-list harassment is evidence of breach |
| CHR-A-31 | Disbursal only into the borrower's account; LSP fees not charged to the borrower (para 9) |
| CHR-A-32 | RE/LSP nodal grievance officer named on the DLA and in the KFS; 30-day response (para 11) |
| CHR-A-33 | RBI publishes DLA data reported by REs on CIMS without verifying it (para 17, Annex I); legitimacy check must say inclusion is not endorsement |
| CHR-A-34 | KFS: all-inclusive cost (APR) and charges must be disclosed; charges not in the KFS cannot be levied [VERIFY exact para in the 2025 Directions and the RBC Directions] |

### S.3.5 Settlement, foreclosure and closure (borrower-side)

| Rule | Content | Tag |
|---|---|---|
| CHR-A-40 | Compromise settlements need a board-approved RE policy; cooling period before fresh credit; settled accounts reported to CICs as "settled" (RBI Framework, 8 Jun 2023) | [VERIFY all] S38 |
| CHR-A-41 | The borrower has no right to a settlement. Copy must never imply one | [INTERP] |
| CHR-A-42 | No prepayment charges on floating-rate loans to individuals for non-business purposes sanctioned or renewed on or after 1 Jan 2026 | [VERIFY] S15 para 34 |
| CHR-A-43 | RBI cautions (11 Dec 2023; 4 May 2026) against fee-charging "loan waiver" campaigns and "debt waiver certificates" | [LAW] S18, S19 |

### S.3.6 Documents checklist (by sub-issue)

| Sub-issue | Minimum set before first letter | Additional for escalation |
|---|---|---|
| Recovery harassment | Loan account identifier (masked), lender name and registration, incident log with ≥ 1 evidenced incident (recording, screenshot, message), agent or agency name if known | Prior complaint and acknowledgement, RE reply, call-time analysis, witness statements, police complaint copy if filed |
| Unfair charges / KFS-APR | Sanction letter, KFS, loan agreement, repayment statement showing the charge | Fee schedule published by the RE, computation sheet |
| Digital loan app | App name, screenshots of permissions and messages, disbursal proof, lender behind the app (from the KFS) | Proof of contact-list messages to third parties, LSP details |
| Closure / NOC / documents | Closure statement or final payment proof, request for NOC and documents with date | Follow-ups, per-day delay computation |
| Settlement correspondence | Statement of account, hardship facts (user's own words), user's proposed amount and source of funds | Lender's settlement letter (if any) |
| Illegal app | Screenshots, payment proofs, threats | Cyber-crime acknowledgement, police FIR or complaint number |

All items: hash at capture, typed copies for screenshots, Aadhaar masked (NN-04).

### S.3.7 Playbooks

**PB-A1 Recovery harassment**
1. Triage: covered RE? (CHR-A-01/06). Safety check: threats, violence or morphing → open safety track now (T-A7).
2. Start the harassment log; import recordings and screenshots; mark breaches against rows effective on each incident date (CHR-A-20…28).
3. Draft T-A2 (conduct breach notice) and T-A1 (grievance to the RE's grievance or nodal officer), asking for the agent's identity, authorisation and retained call recordings (CHR-A-26).
4. User approves and sends; capture dispatch proof; start CHR-A-10.
5. On reply or expiry: compute the RBIO window (CHR-A-12); prepare T-A3 pack with relief heads (₹30 lakh consequential loss; ₹3 lakh time, expense, harassment; Cl. 8(3)).
6. User self-files on CMS, or signs T-A4 for the case manager to file as non-advocate representative.
7. Track RE response (CHR-A-13), award and acceptance (CHR-A-14), compliance (CHR-A-15), appeal (CHR-A-16).
8. If dissatisfied or out of scope: refer to a panel advocate for consumer commission or civil court (fixed fee).

**PB-A2 Unfair charges / KFS mismatch** — compare charged items with the KFS (CHR-A-34) → T-A1 citing the specific charge and direction → RBIO if unresolved; never advise the user to stop paying EMIs.

**PB-A3 Digital loan app** — legitimacy check (CHR-A-33); if regulated, T-A1 to the nodal grievance officer citing CHR-A-30/31; if unregistered, illegal-app track (CHR-A-06); in both, preserve evidence of third-party messages.

**PB-A4 Closure, NOC and documents** — T-A8 request citing CHR-A-17; 30-day watch; per-day delay computation shown as "as per RBI Directions [VERIFY]"; escalate to RBIO.

**PB-A5 Settlement support** — explain CHR-A-40/41 and credit impact; T-A6 proposal with mandatory disclaimers; case manager may correspond but cannot bind; user confirms any offer in-app; money goes directly from the user to the lender.

### S.3.8 May / may not (Vertical A)

| LawDocs (Consumer Help entity) may | LawDocs may not |
|---|---|
| Explain forums, deadlines and rights in general terms | Give a legal opinion on the merits (panel advocate only — NN-41) |
| Draft letters and complaint packs for the user to approve | Send any letter without the user's per-letter approval |
| File before RBIO as non-advocate representative with written authority | Let an advocate file or represent before RBIO (CHR-A-04; S2 Cl. 10(1)(b)) |
| Correspond with the RE under a limited authority | Bind the user to a settlement; hold settlement money; run a savings corpus |
| Charge disclosed flat fees (when switched on) | Promise a waiver, settlement, compensation or "stop EMIs"; charge lenders for leads |

### S.3.9 Risk register (Vertical A; from R2 §1(e))

| # | Risk | L | I | Control | Test |
|---|---|---|---|---|---|
| A1 | Advocate files before RBIO | M | H | Representation matrix block | P15-AT-04 |
| A2 | "Waiver" marketing | M | H | Banned phrases; legal review gate | P15-AT-08 |
| A3 | Custody of borrower funds (BUDS Act 2019 [VERIFY exposure]; PSS Act) | L | Critical | No wallet, no pooled account; beneficiary rule `LD-CHP-010` | P15-AT-06 |
| A4 | Opposite party is a group client | H | H | Ethical wall; conflict check; self-serve policy | P15-AT-01/02 |
| A5 | Missed 90-day window | M | M | Deadline engine; T-15/T-7/T-1 | P15-AT-05 |
| A6 | Evidence inadmissible | M | M | Hash at capture; s.63 certificate | P15-AT-10 |
| A7 | Unauthorised practice by case managers | M | H | Script library; QA sampling; opinions only by advocates | QA KPI |
| A8 | Rule change | H | M | Effective-dated rows; ops-editable; recompute job | Rule tests |
| A9 | Refund disputes | M | M | Published scale; auto credit notes | P15-AT-22 |

---

## S.4 Vertical A2 — Credit-report disputes

| Rule | Content | Source |
|---|---|---|
| CHR-A2-01 | LawDocs never pulls a credit report; the user downloads and uploads their own | CICRA 2005; NN-05; CH-05 |
| CHR-A2-02 | Dispute raised with the CIC (online) or the credit institution | S39 |
| CHR-A2-03 | CI sends correction to the CIC within 21 calendar days | RBI/2023-24/72 para 2(b) (S40) |
| CHR-A2-04 | CIC resolves within 30 calendar days of filing in total | para 2(a), (c) |
| CHR-A2-05 | Compensation ₹100 per calendar day beyond 30 days, apportioned CI/CIC, credited automatically within 5 working days of resolution to the account given at filing; effective 26 Apr 2024 | para 2(a), (e), (k) |
| CHR-A2-06 | Rejection must state reasons | para 2(d) |
| CHR-A2-07 | Escalation to RBIO (CICs are covered REs), except CICRA s.18 matters | S1, S40 |

**Documents:** credit report PDF (user-downloaded), identity proof, proof of correct position (closure letter, NOC, payment proof, court order), prior dispute acknowledgement.

**PB-A2-1:** upload report → P05 extracts accounts → user marks wrong entries with reason → T-A5 to CIC + parallel letter to the CI → 30-day tracker with compensation estimate → on rejection or delay, RBIO (PB-A1 steps 5–7). Copy: "Compensation is credited by the CIC/CI under the RBI framework; LawDocs does not collect it." No success fee on CHR-A2-05 compensation (§S.11).

---

## S.5 Vertical B — Insurance

### S.5.1 Eligibility and forums

| Rule | Content | Source |
|---|---|---|
| CHR-B-01 | Insurer GRO first: acknowledge immediately; seek details within 7 days; resolve within 14 days with reasons if rejected | IRDAI PPHI Regulations 2024 and Master Circular 5 Sep 2024 (S41) [VERIFY current] |
| CHR-B-02 | IRDAI Bima Bharosa if no response in reasonable time or dissatisfied; toll-free 155255 / 1800-4254-732; complaints@irdai.gov.in | S9 |
| CHR-B-03 | Insurance Ombudsman: written representation to the insurer first; no reply within one month, or rejection or unsatisfactory reply (R.14(3)(a)) | Insurance Ombudsman Rules 2017 as amended to 9 Nov 2023 (S8) |
| CHR-B-04 | File within one year (R.14(3)(b)); delay condonable (R.14(4)); not pending or decided before a court, consumer forum or arbitrator (R.14(5)) | S8 |
| CHR-B-05 | Award cap ₹50 lakh including expenses (R.17(3)(ii)); above → consumer commission, whose level is fixed by the premium paid (CHR-CC-01), not by the claim | S8; W.9 LA-02 |
| CHR-B-06 | Mediation recommendation within 1 month of consent; acceptance within 15 days; insurer compliance within 15 days (R.16) | S8 |
| CHR-B-07 | Award within 3 months of receiving all requirements (R.17(4)); insurer complies within 30 days (R.17(6)); late compliance ₹5,000 per day to the complainant (PPHI Master Circular) | S8, S41 [VERIFY ₹5,000/day source] |
| CHR-B-08 | Video hearing on request or own motion (R.15(5)) | S8 |
| CHR-B-09 | Representation: see §S.2 | S8, S10 |

### S.5.2 Claim turnaround rules (PPHI Master Circular, 5 Sep 2024; S41) [VERIFY each]

| Rule | Line | TAT |
|---|---|---|
| CHR-B-20 | Life death claim, no investigation | 15 days from intimation |
| CHR-B-21 | Life death claim, investigation | 45 days |
| CHR-B-22 | Health cashless pre-authorisation | 1 hour |
| CHR-B-23 | Health cashless final discharge authorisation | 3 hours; excess hospital charges borne by the insurer from shareholders' funds if late |
| CHR-B-24 | General insurance (retail) surveyor appointment | 24 hours |
| CHR-B-25 | Final survey report | 15 days |
| CHR-B-26 | Claim paid or rejected after survey report | 7 days |
| CHR-B-27 | Delay interest | Bank rate + 2% from intimation to payment, payable without demand |

### S.5.3 Documents

Policy schedule and wording; proposal form (for mis-selling and non-disclosure defences); claim form; rejection or short-settlement letter; discharge summary, bills and prescriptions (health); FIR, surveyor report, repair estimates (motor/property); death certificate, nominee or legal-heir proof (life); investigation report if shared; all prior correspondence; KYC (masked); authority letter (correspondence only).

### S.5.4 Playbooks

**PB-B1 Claim rejection or short settlement** — policy reader summary → identify the rejection ground against wording, exclusions, waiting periods and disclosure → T-B1 to GRO citing CHR-B-01 and any TAT breach → 14-day clock → Bima Bharosa logging guide → after one month or on rejection, T-B3 Ombudsman complaint signed and filed by the user → T-B4 video-hearing request if needed → mediation decision (T-B5, 15-day clock) → award → T-B6 compliance demand with CHR-B-07 → above ₹50 lakh or unsatisfied: T-B7 for e-Jagriti via panel advocate.

**PB-B2 Claim delay** — compute TAT breach and interest (T-B2, CHR-B-27) → GRO letter → as PB-B1.

**PB-B3 Mis-selling** — collect proposal form, illustrations and sales communications → GRO complaint → Ombudsman or consumer commission. Consumer Help never recommends a replacement policy (§S.5.5).

### S.5.5 May / may not (Vertical B)

| May | May not |
|---|---|
| Read and summarise the policy; compute TAT breaches and interest; draft GRO and Ombudsman packs | Sell, compare or recommend insurance; receive insurer commissions (Insurance Act intermediary rules [VERIFY]) |
| Prepare the user for mediation and hearing | File the Ombudsman complaint for the user (R.14(1)) |
| Refer to a panel advocate for adjudication (where permitted) or consumer commission | Promise claim payment; share any award with an advocate |

### S.5.6 Risk register (Vertical B; R2 §2(e))

| # | Risk | Control |
|---|---|---|
| B1 | Acting as an unregistered intermediary | Post-claim services only; no product content |
| B2 | Representation refused by the Ombudsman | User self-files by default; advocate request letter citing the Karnataka HC only at the R.17 stage |
| B3 | ₹50 lakh cap exceeded | Automatic forum routing (P15-AT-14) |
| B4 | Success fee seen as unfair | Cap, fee sheet, cooling-off, OFF by default |
| B5 | Health data | Specific consent, field encryption, retention class |
| B6 | Impostor Bima Bharosa sites | Official-link registry; never ask for passwords |

---

## S.6 Consumer commission and National Consumer Helpline (shared escalation)

| Rule | Content | Source |
|---|---|---|
| CHR-CC-01 | Pecuniary limits by the **value of goods or services paid as consideration** (CPA 2019 ss.34(1), 47(1)(a)(i), 58(1)(a)(i)), not by the compensation claimed: District ≤ ₹50 lakh; State > ₹50 lakh to ₹2 crore; National > ₹2 crore (2021 Rules). For insurance, the consideration is the premium paid | S42; R5 §5; reviewer correction W.9 LA-02 [VERIFY: Rules text] |
| CHR-CC-02 | Limitation 2 years (CPA 2019 s.69) | [VERIFY] |
| CHR-CC-03 | e-Jagriti (from 1 Jan 2025) integrates OCMS, e-Daakhil, NCDRC CMS, CONFONET; online filing; fees via Bharat Kosh/PayGov paid by the complainant; virtual hearings; NRI filing | S42 |
| CHR-CC-04 | Non-advocate agents only under the 2014 agent regulations on a party-issued authorisation; advocate-issued authority letters to non-advocates barred (*Anuj Kumar Chauhan*, Delhi HC, Dec 2024) | S14 [VERIFY current position in other States] |
| CHR-CC-05 | NCH: 1915, WhatsApp, SMS, app, UMANG; convergence companies; 17 languages; pre-litigation | S42 |
| CHR-CC-06 | Affidavits supporting complaints need oath before an oath commissioner or notary; not eSign-eligible (NN-07) | R3 §8 |

**PB-CC1:** compute forum (CHR-CC-01) → check limitation (CHR-CC-02) → T-A9/T-B7 draft, index, annexures → affidavit wet-ink pack → user or panel advocate files on e-Jagriti and pays the fee on the official channel → hearing dates tracked in P11.

---

## S.7 Letter and template catalogue

All templates are P10/P06 content with reviewer of record, versioned citations and mandatory disclaimers. "Signer" is the person who must approve and sign.

| ID | Template | Forum / recipient | Signer | Key citations | Mandatory text |
|---|---|---|---|---|---|
| T-A1 | Grievance to RE grievance or nodal officer | RE | User (or case manager under authority) | Specific direction breached (RBC, DL Directions, KFS) | Request for acknowledgement and complaint number |
| T-A2 | Recovery-conduct breach notice | RE | User | CHR-A-20…28 effective on incident dates | Request to preserve and share call recordings |
| T-A3 | RB-IOS 2026 complaint pack (CMS fields) | RBI Ombudsman | User or non-advocate representative | Cl. 8(3), Cl. 10 | Declaration that the matter is not pending elsewhere |
| T-A4 | Authorisation of non-advocate representative | RBI Ombudsman | User | Cl. 3(1)(c) | Representative is not an advocate; revocable; scope and RE named |
| T-A5 | CIC dispute and CI letter | CIC, CI | User | RBI/2023-24/72 | Compensation credited by CIC/CI |
| T-A6 | Settlement proposal | RE | User | RBI framework 8 Jun 2023 [VERIFY] | No right to settlement; credit-report impact; lender's discretion; not a waiver |
| T-A7 | Police / cyber-crime complaint | Police, cyber portal | User | BNS 2023 s.351 [VERIFY] | Facts only; no legal conclusions |
| T-A8 | Request for documents and charge satisfaction after closure | RE | User | CHR-A-17 [VERIFY] | Per-day delay computation labelled "as per RBI Directions" |
| T-A9 | Consumer complaint draft | Consumer commission | User / panel advocate | CPA 2019 ss.2(11), 35, 69 [VERIFY] | Draft for advocate review |
| T-B1 | GRO complaint with TAT breach | Insurer | User | CHR-B-01, CHR-B-20…27 | Request for written reasons |
| T-B2 | Penal-interest computation | Insurer | User | CHR-B-27 | Computation method shown |
| T-B3 | Insurance Ombudsman complaint (CIO format) | Ombudsman | User | R.14 [VERIFY current form and annexure] | Not pending elsewhere |
| T-B4 | Request for video hearing | Ombudsman | User | R.15(5) | — |
| T-B5 | Mediation acceptance or rejection | Ombudsman | User | R.16 | 15-day clock |
| T-B6 | Award-compliance demand | Insurer | User | R.17(6); CHR-B-07 | — |
| T-B7 | Consumer complaint (e-Jagriti) | Consumer commission | User / panel advocate | CHR-CC-01…03 | Draft for advocate review |
| T-C1 | Grievance to e-challan portal (wrong vehicle, cloned plate, sold vehicle) | Traffic authority | User | MV Act provisions cited by the challan | Evidence index (delivery note, photos) |
| T-C2 | Representation to traffic police with sale evidence | Traffic police | User | — | Delivery-note time-stamp |
| T-C3 | Vakalatnama and memo of appearance | Court | User + advocate | Court rules | Wet-ink where the court requires |
| T-C4 | Compounding / Lok Adalat checklist | User | — | MV Act s.200; State notification | "No guarantee of reduction" |
| T-C5 | Challan register export | User (fleet) | — | — | — |
| T-D1 | Vehicle sale agreement | Buyer, seller | Both | Contract Act; MV Act s.50 [VERIFY]; State stamp | Challan cut-off date and time; hypothecation warranty; transfer covenant |
| T-D2 | Delivery note | Buyer, seller | Both | — | Date and time to the hour; odometer; keys; documents |
| T-D3 | Receipt of consideration | Buyer | Seller | — | Mode of payment |
| T-D4 | Forms 29/30/28/35 pre-fill | RTO | Owner, buyer, financier | CMVR [VERIFY form versions] | "Submit on Vahan or as the RTO requires" |
| T-D5 | Foreclosure statement and NOC / Form 35 demand | Financier | Borrower | CHR-A-17, CHR-A-42 [VERIFY] | — |
| T-D6 | Protective intimation to RTO and police | RTO, police | Seller | [VERIFY State practice] | — |
| T-D7 | Authority or POA for RTO agent | RTO | Owner | State practice [VERIFY stamp] | POA → wet-ink (NN-07) |

---

## S.8 Vertical C — Traffic challans

### S.8.1 Rules

| Rule | Content | Source |
|---|---|---|
| CHR-C-01 | No lawful third-party bulk API for e-challan or Vahan data is known: MoRTH said API access is for government organisations; the 2019 bulk-data policy was scrapped in June 2020 → user-initiated lookup on official portals only | S33 [VERIFY with MoRTH/NIC and API Setu] |
| CHR-C-02 | Fines are government receipts credited to e-Treasury through the court or State gateway; LawDocs never collects them; collecting for a government beneficiary may need PA authorisation | S29; R3 LG-145, LG-150 [VERIFY] |
| CHR-C-03 | Compoundable offences under MV Act s.200 (as amended 2019): ss.177–182, 182A(1),(3),(4), 182B, 183(1)–(2), 184 (handheld device only), 186, 189, 190(2), 192, 192A, 194–194F, 196, 198; amounts notified by the State; compounding does not discharge s.206(4) proceedings | S45 |
| CHR-C-04 | Non-compoundable examples: s.185 (drunk driving), s.184 dangerous driving (other than handheld device), s.199A (juvenile) → physical court | S45, S43 |
| CHR-C-05 | Unpaid challans go to the Virtual Court; summons under s.208 by SMS with a link to vcourts.gov.in; online payment is treated as admission of guilt; "Request to contest" sends the case to a regular court | S29, S43 |
| CHR-C-06 | Timing to Virtual Court and physical court varies by State (one operator reports 60 and 90 days) | S43 [VERIFY by State; CMVR r.167 amendments] |
| CHR-C-07 | State multiplier of fines 1–10× (s.210A) | S45 |
| CHR-C-08 | Lok Adalat: compoundable items only; State-specific limits (e.g., Delhi: OTP slot booking, commercial-vehicle challans < ₹10,000, 5 notices + 2 challans per appointment for private vehicles; undertaking not to contest on vcourts) | S46 [VERIFY per sitting] |
| CHR-C-09 | Record update after payment may take 10–15 working days | S44 [VERIFY] |

### S.8.2 Documents
RC, DL, insurance, PUC, challan PDF or photo, Lok Adalat appointment printout, vakalatnama (contest), sale agreement and delivery note if the challan post-dates a sale.

### S.8.3 Playbooks
**PB-C1 Check and pay** — "Check challans" opens the official portal → user imports result (PDF, screenshot, shared SMS text) → classify (CHR-C-03/04) → pay on the official page → upload receipt → record-update check after CHR-C-09 period.
**PB-C2 Lok Adalat** — eligible items listed → next sitting from the State calendar → user books by OTP → reminders → outcome recorded. Copy per §S.11.3.
**PB-C3 Contest** — Virtual Court "Request to contest" guide, or "Hire an advocate" (neutral Rule 36 list; fixed fee; P16) → T-C3 → hearing tracked → fine (if any) paid by the user officially.
**PB-C4 Wrong owner** — link delivery note → T-C1 and T-C2.

### S.8.4 May / may not
May: guide, classify, remind, draft, coordinate an advocate. May not: scrape portals, store user OTPs, collect fines, add convenience fees to fines, claim "challan cancelled" or guaranteed reductions, rank advocates (NN-21).

### S.8.5 Risk register (R2 §3(e))
C1 scraping (user-initiated only; no vendor API without legal sign-off) · C2 holding fines (deep link; beneficiary rule) · C3 Lok Adalat discount claims (copy rule) · C4 advocate advertising (Rule 36 neutral listing) · C5 wrong-owner challans (delivery note link) · C6 State variance (State rows; ops-editable calendar).

---

## S.9 Vertical D — Vehicles

### S.9.1 Rules

| Rule | Content | Source |
|---|---|---|
| CHR-D-01 | Pre-sale checks: pending challans, blacklist status, hypothecation on RC, insurance and PUC validity, tax clearance | S35, S36, S32 |
| CHR-D-02 | **Seller (transferor)** reports the transfer within 14 days (vehicle registered in the same State) or 45 days (registered in another State, with NOC) — MV Act s.50(1)(a)–(b); **buyer (transferee)** reports within 30 days of transfer — s.50(1); legal heir: intimate within 30 days of death, apply within 3 months; auction buyer 30 days — s.50(2), CMVR r.56; buyer applies to insurer within 14 days [VERIFY: s.157 as amended 2019] | S35; reviewer correction W.9 LA-03 [VERIFY: s.50 and CMVR rr.55–56 current text] |
| CHR-D-03 | Forms: 29 (notice of transfer), 30 (application for transfer), 28 (NOC for another State/RTO), 35 (termination of hypothecation, signed by owner and financier) | S35 [VERIFY current versions] |
| CHR-D-04 | Online route: vahan.parivahan.gov.in/vahanservice → chassis last 5 digits + OTP → transfer of ownership → fee → application number; some States require physical submission | S35 |
| CHR-D-05 | Central fee: half the registration fee (≈ ₹150 motorcycle, ₹300 car) under CMVR r.81; late fees and State penalties | S35 [VERIFY] |
| CHR-D-06 | Financier NOC commonly valid about 90 days; some lenders send e-NOC to Vahan | S36 [VERIFY] |
| CHR-D-07 | NBFC document release and charge removal within 30 days of full repayment; ₹5,000 per day for delay attributable to the NBFC | S15 [VERIFY application to vehicle hypothecation] |
| CHR-D-08 | Until RC transfer, the registered owner may remain liable to third parties | [VERIFY case law] |
| CHR-D-09 | Stamp duty on vehicle sale agreements varies by State: whether chargeable at all, whether an "agreement" or "conveyance of movable property" (e.g., Maharashtra Article 25), e-stamp availability | Analyst note [VERIFY each State] |
| CHR-D-10 | A sale agreement of a movable vehicle is not an excluded instrument under the IT Act First Schedule; eSign permitted subject to stamp | [INTERP] R3 §1 |
| CHR-D-11 | No escrow of the sale price unless through a licensed bank or escrow partner | R2 risk D3 [VERIFY licensing] |

### S.9.2 Playbooks
**PB-D1 Sell my vehicle** — pre-sale checks (CHR-D-01) → terms → T-D1 with State stamp rule (CHR-D-09) → eStamp where needed (NN-08) → eSign in deal room → payment party-to-party, both confirm → T-D2 delivery note (time-stamped) and T-D3 receipt → T-D4 forms → buyer applies on Vahan (CHR-D-04) → 14/45-day watch (CHR-D-02) → RC transferred → insurance transferred → close. Missed deadline → T-D6.
**PB-D2 Remove hypothecation** — foreclosure statement request (T-D5) → payment by the borrower directly to the lender → NOC and Form 35 → 30-day release watch (CHR-D-07) → Vahan application → RC updated. Group-client financier → conflict policy.
**PB-D3 Buy a used vehicle** — buyer-side checklist (same as CHR-D-01 plus engine/chassis match), agreement review, delivery note, transfer within deadline.

### S.9.3 May / may not
May: draft, stamp through authorised channels, eSign, pre-fill forms, track deadlines, store documents. May not: hold the sale price, file on Vahan with the owner's OTP, advise on disputed title (advocate only), promise RC transfer timelines that depend on the RTO.

### S.9.4 Risk register (R2 §4(e))
D1 wrong stamp duty (State table, "duty basis" shown) · D2 seller remains owner (delivery note, alerts, T-D6) · D3 escrow (excluded) · D4 financier is a group client (wall) · D5 forms change by State (versioned per-State templates).

---

## S.10 Official-link registry (seed)

| Code | Purpose | URL | Note |
|---|---|---|---|
| OL-01 | RBI Complaint Management System | cms.rbi.org.in | Hindi/English |
| OL-02 | RBI CRPC postal address | CRPC, RBI, Central Vista, Sector 17, Chandigarh 160017; crpc@rbi.org.in | Any language |
| OL-03 | RBI Sachet | sachet.rbi.org.in | [VERIFY] |
| OL-04 | IRDAI Bima Bharosa | [VERIFY official URL]; 155255 | Warn about impostor sites |
| OL-05 | Council for Insurance Ombudsmen | cioins.co.in | Online complaint |
| OL-06 | e-Jagriti | [VERIFY official URL] | Consumer commissions |
| OL-07 | National Consumer Helpline | 1915; consumerhelpline.gov.in [VERIFY] | Pre-litigation |
| OL-08 | e-Challan | echallan.parivahan.gov.in | Lookup and pay |
| OL-09 | Virtual Courts | vcourts.gov.in/virtualcourt/ | Pay or contest |
| OL-10 | Vahan citizen services | vahan.parivahan.gov.in/vahanservice | RC transfer, hypothecation |
| OL-11 | Delhi Traffic Lok Adalat | traffic.delhipolice.gov.in/lokadalat | Model for State rows |
| OL-12 | Cyber-crime reporting | cybercrime.gov.in; 1930 [VERIFY] | Safety track |

Each link carries `last_checked_at`, owner, and a weekly health check (P15 `OfficialLinkHealthJob`). The app opens registry links only.

---

## S.11 Fees, disclosures and copy rules

### S.11.1 Fee rules
| Rule | Content |
|---|---|
| CHR-X-01 | Flat fees per pack or per case are the default paid model (RS-LD-39; ON only after a legal memo) |
| CHR-X-02 | Success fee only in the non-advocate Consumer Help entity, OFF by default (RS-LD-40), cap 10% and ₹1,50,000 [OWNER], counsel opinion and checker approval required (CH-31; R6 C-3) |
| CHR-X-03 | Success-fee base excludes: statutory penal or delay interest (CHR-B-27), per-day compliance penalties (CHR-A-17, CHR-B-07), CIC compensation (CHR-A2-05), automatic refunds, and amounts recovered without the case manager's work [COUNSEL] |
| CHR-X-04 | Advocates: fixed fees only, separate invoice; no share of awards or success fees; no referral fee either way (BCI Rules Part VI Ch II r.20–21; R2 §5.1) |
| CHR-X-05 | No lead fees, sponsorship or advertising from lenders or insurers (R6 C-6) |
| CHR-X-06 | Government fees, fines and dues are always paid by the user on official channels (NN-22, NN-23) |
| CHR-X-07 | Withdrawal charges are time-based, not percentage-based; pro-rata refunds per published scale |

### S.11.2 Mandatory disclosures (fee sheet and every paid flow)
Entity name and grievance officer; "We are not a law firm and do not give legal advice; legal opinions come from independent advocates you engage"; "We never collect fines, loan dues, settlement amounts or vehicle prices"; "We cannot guarantee any outcome"; fee amounts, caps, exclusions, refund scale, cancellation route; conflict disclosure where applicable.

### S.11.3 Copy rules (banned-phrase seed)
Blocked: "loan waiver", "debt waiver", "waiver certificate", "stop paying EMIs", "we will settle your loan", "guaranteed settlement", "guaranteed claim", "100% success", "challan cancelled", "challan waived", "Lok Adalat discount guaranteed", "RBI-approved", "IRDAI-approved", "government-approved", "best lawyer", "top advocate". Required substitutes: "may", "you can ask", "the forum decides". Lok Adalat line: "Lok Adalat may settle at a reduced amount at the court's discretion; no guarantee."

---

## S.12 Ethical-wall design (controls and tests)

| # | Layer | Control | Evidence / test |
|---|---|---|---|
| W1 | Entity | Separate legal entity, brand, GSTIN, bank account, Razorpay merchant, privacy notice, grievance officer (R2 §5.6.1) | Super Admin entity record; P15-AT-22 |
| W2 | Data | Schema `chp` on a dedicated database instance; separate KMS key ring; RLS on tenant + entity + staff scope | Pen-test; RLS tests |
| W3 | Events | `int` deny rule on any outbound contract with `chp` source; internal events carry IDs only | P15-AT-01 |
| W4 | Retrieval | Separate vector/search namespaces; no cross-entity retrieval | AI eval |
| W5 | People | Realm group `chp`; Cerbos SoD denying combined roles; panel-advocate cooling period; quarterly recertification | P15-AT-19; recertification report |
| W6 | Conflict check | HMAC of opposite-party identifiers with epoch keys; OH answers flag and category only; no consumer data or case ID; fail closed; logged | P15-AT-02/03 |
| W7 | Commercial | No lender/insurer referral fees, leads, sponsorship, ads, data sales; OH8 stream deny-list | Stream registry review |
| W8 | Governance | Board-approved COI policy; annual independent review; monthly breach-log review; breach counts only to LDC register | Board minutes; review report |
| W9 | Reverse wall | Finbyx, Udofin, LDC and Equator staff and services never query or receive Consumer Help data; their support desks cannot open Consumer Help tickets | OH support-scope config |
| W10 | Kill switch | Per vertical and for the whole brand (NN-39) | Drill each release |

**Conflict-check flow.** (1) `chp` normalises each identifier (upper-case, punctuation stripped, legal-form suffix standardised; registration numbers canonicalised). (2) Computes `HMAC-SHA256(k_epoch, id)`; `k_epoch` rotates every `chp.conflict.key_rotation_days` (default 90) and is shared only with the OH conflict service through the key-management service. (3) Calls `int` → OH `POST /v1/conflicts/check` (LawDocs machine client with hashed identifiers; Appendix X §X.10). (4) OH compares against its HMAC'd list of group lender and insurer clients and returns `{conflict, category, as_of}` with categories `LENDER_CLIENT` or `CONSUMER_HELP_ADVERSE` (Appendix X §X.10). (5) `chp` applies `chp.conflict.on_hit_policy`. Residual risk: an HMAC of a public name is guessable by anyone holding the key; mitigation is that only OH and `chp` hold it, OH stores no per-request identifiers beyond the log required for audit, and the request carries no consumer data [REC; OI-P15-09].

---

## S.13 KPIs (Consumer Help)

| KPI | Definition | Target (seed) |
|---|---|---|
| Time to first draft | Intake to first approved-ready letter | ≤ 24 h |
| Missed statutory windows | Managed cases where a CHR deadline passed without action | 0 |
| Escalation readiness accuracy | Cases escalated before eligibility (rejected as premature) | ≤ 1% |
| Stage duration | Median days per stage by forum | Tracked; no target published |
| Evidence completeness | Cases meeting minimum evidence set before first letter | ≥ 90% |
| Representation compliance | Filings by an impermissible representative | 0 |
| Copy compliance | Banned-phrase incidents in sent letters | 0 |
| Wall incidents | Blocked cross-wall attempts (reviewed) / successful breaches | Monitored / 0 |
| Refund disputes | Disputes ÷ paid cases | ≤ 1% |
| User-reported outcome | Resolved in user's favour at any rung (internal only; NN-20) | Tracked, not marketed |

---

## S.14 Triage question sets (seed for `tpl_` questionnaires)

Each set is one question per screen, with "I don't know" allowed unless marked mandatory (M). Answers map to rule rows; the result screen lists which answers drove the outcome.

### S.14.1 Loans (Vertical A)
| # | Question | Type | Drives |
|---|---|---|---|
| A-Q1 | Who gave you the loan? (search box with RBI-registered names; free text allowed) (M) | Lookup + text | CHR-A-01/06; conflict check |
| A-Q2 | What kind of loan? (personal, app-based, credit card, vehicle, home, gold, business, microfinance, BNPL) | Choice | CHR-A-21, PB selection |
| A-Q3 | What is the problem? (recovery calls or visits, threats, contact to family or friends, extra charges, interest higher than agreed, loan closed but no NOC, app misuse of contacts or photos, other) (M) | Multi-choice | Sub-issue playbooks |
| A-Q4 | Has anyone threatened violence, arrest, or shared your photos or details publicly? | Yes/No | Safety track (immediate) |
| A-Q5 | Have you complained to the lender in writing? When? Did they reply? When? | Dates | CHR-A-10/12 clocks |
| A-Q6 | Is this matter already in any court, consumer commission, DRT or arbitration? | Yes/No/Unsure | CHR-A-04 |
| A-Q7 | Do you have recordings, screenshots or messages? | Yes/No | Evidence minimum set |
| A-Q8 | Do you want to file yourself or have a case manager help? | Choice | Representation matrix; conflict check |

### S.14.2 Credit report (A2)
A2-Q1 Which bureau (CIBIL, Experian, Equifax, CRIF High Mark)? · A2-Q2 What is wrong (account not mine, closed shown open, wrong overdue, settled vs closed, duplicate, wrong personal details)? · A2-Q3 Have you raised a dispute? Date and dispute ID? · A2-Q4 Do you have proof (NOC, closure letter, payment proof)? → CHR-A2-02…07.

### S.14.3 Insurance (B)
B-Q1 Type (health, life, motor, home, travel, other) (M) · B-Q2 Problem (rejection, partial settlement, delay, cashless denied, mis-selling, policy cancelled) (M) · B-Q3 Date of claim intimation and of the insurer's decision · B-Q4 Have you written to the insurer's grievance cell? Date, reply date · B-Q5 Amount claimed and amount paid · B-Q6 Is the matter in any court or consumer commission? · B-Q7 Are you the policyholder, nominee, legal heir or assignee? → CHR-B-01…09, CHR-CC-01.

### S.14.4 Challans (C)
C-Q1 Vehicle registration number (M) · C-Q2 Do you already have the challan (PDF, SMS, notice)? · C-Q3 Is it marked for Virtual Court or a court date? · C-Q4 Did you sell the vehicle before the challan date? (→ PB-C4) · C-Q5 Do you want to pay, use Lok Adalat, or contest? → CHR-C-03…08.

### S.14.5 Vehicles (D)
D-Q1 Selling or buying? · D-Q2 Same State or another State? · D-Q3 Is there a loan on the vehicle (hypothecation on RC)? · D-Q4 Is the loan fully paid? Date? · D-Q5 Insurance and PUC valid? · D-Q6 Any pending challans? → CHR-D-01…11.

---

## S.15 Case-manager script boundaries (risk A7)

Case managers are not advocates. Scripts are content data reviewed by `PLT_LEGAL_REVIEWER`; QA samples 10% of conversations per month [REC].

| Topic | Allowed (procedural help) | Not allowed (legal advice or representation) | Route |
|---|---|---|---|
| Forums | "Under the RBI Ombudsman Scheme you can complain if the bank has not replied in 30 days." | "Your case will definitely succeed at the Ombudsman." | — |
| Merits | "Here are the documents the Ombudsman usually needs." | "The lender has no legal right to charge this; you should refuse to pay." | Panel advocate consult |
| Payments | "You can ask the lender for a foreclosure statement." | "Stop paying EMIs until this is resolved." | Panel advocate |
| Settlement | "You can propose a settlement; the lender decides; it affects your credit report." | "We will get you a 50% waiver." | — |
| Criminal conduct | "Threats can be reported to the police; here is a draft complaint for you to file." | "File an FIR under section X against the agent" as a legal conclusion | Police; panel advocate |
| Insurance | "The insurer must give reasons for rejection; here is the policy clause they cited." | "This exclusion is unenforceable." | Panel advocate |
| Court | "The challan can be contested in court; an advocate can appear for you." | Appearing in court or signing pleadings | Panel advocate |

Escalation trigger words in chat or calls ("should I", "is it legal", "will I win", "can they arrest me") prompt the case manager to offer a fixed-fee advocate consult. Calls by case managers to lenders or insurers are one-to-one, made from the Consumer Help entity's declared numbers, logged with the user's authority reference, and never automated (NN-34).

---

## S.16 Evidence standards

| Item | Capture standard | Typed copy / derived | Admissibility support |
|---|---|---|---|
| Call recording (user's own) | Original file imported unchanged; SHA-256; file metadata preserved; user statement of date, time and parties | Transcript (`drv_`), speaker labels editable, language and translation labelled | BSA s.63 certificate draft (Part A by the user; Part B by an expert where needed) [VERIFY format]; legality of recording a call one is party to [VERIFY] |
| WhatsApp / SMS screenshot | Original image; optional chat export file; capture time; device class | Typed copy with region anchors; translation if not English | Certificate as above; export file preferred over screenshot |
| Photo of agent visit, notice, vehicle | Original with EXIF if present; server timestamp; optional geo-tag with consent | Caption | Certificate |
| Letters and emails | PDF or `.eml` with headers | Typed copy for scanned letters | Dispatch proof (postal receipt, email headers) hashed |
| Credit report | Bureau PDF as downloaded | Extracted accounts table | — |
| Policy wording | Insurer PDF | Policy summary with page anchors | — |
| Delivery note | eSigned PDF; time-stamp to the hour; photos | — | P08 evidence pack (NN-10) |

Rules: originals immutable (NN-09); derived renditions never replace originals; every export bundle lists hashes; the user can annotate but not alter an original; third-party personal data in evidence is restricted to the case team (§S.17 retention).

---

## S.17 Authority letters, consents and retention

### S.17.1 Authority letter specification
| Field | Rule |
|---|---|
| Principal | User's name and masked identifier |
| Representative | Named individual case manager (not "the company") for RBIO; entity name plus named manager for correspondence |
| Forum and opposite party | Specific RE, insurer or authority; specific complaint subject |
| Powers | Correspond, receive replies, file (RBIO only), attend hearings where the forum allows; **never** accept a settlement, award or withdrawal for the user |
| Period | Start and end dates; default 12 months; auto-expiry |
| Revocation | In-app, immediate; revocation letter generated for the opposite party |
| Signature | eSign where the gate classifies it as an authorisation (not a POA) [INTERP; COUNSEL]; POA-type instruments → wet-ink and stamp (NN-07, NN-08) |
| Declaration | For RBIO: "The representative is not an advocate" (Cl. 10(1)(b)) |

### S.17.2 Consent purposes (DPDP)
`CHP_CASE_HANDLING` (required for managed service) · `CHP_SEND_TO_OPPOSITE_PARTY` (per letter) · `CHP_SHARE_WITH_ADVOCATE` (per advocate) · `CHP_SHARE_WITH_CASE_MANAGER` · `CHP_HEALTH_DATA` (insurance; specific) · `CHP_ANALYTICS` (off by default) · `CHP_TESTIMONIAL` (only after closure; genuine, verified, no advocate references, no photo by default — NN-49).

### S.17.3 Retention classes
| Class | Items | Period |
|---|---|---|
| `CHP_CASE` | Case record, letters, filings, orders | Closure + 8 years [VERIFY against limitation and tax rules] |
| `CHP_THIRD_PARTY` | Agent names, numbers, voices; third-party messages | Closure + 36 months, unless legal hold |
| `CHP_HEALTH` | Medical records | Closure + 36 months or user deletion request, unless legal hold [REC] |
| `CHP_FEES` | Fee plans, invoices | 8 years (tax) |
| `CHP_CONFLICT_LOG` | Conflict-check log (no consumer data) | 3 years |

---

## S.18 Deadline test fixtures (for `tests/acceptance/p15` and rule-engine unit tests)

| Fixture | Inputs | Expected |
|---|---|---|
| F-01 RBIO, no reply | RE acknowledgement 1 Aug 2026; no reply | Reply period ends 31 Aug 2026; RBIO window closes 29 Nov 2026 |
| F-02 RBIO, late final reply | Acknowledgement 1 Aug 2026; final reply 10 Sep 2026 | Window computed from 10 Sep 2026 (later of); closes 9 Dec 2026 |
| F-03 RBIO, no acknowledgement | Speed-post dispatch 1 Aug 2026; transit allowance 3 days | Reply period ends 3 Sep 2026; flag "computed from dispatch" |
| F-04 RB-IOS transition | Complaint received by RBI on 28 Jun 2026 | Governed by RB-IOS 2021 rows |
| F-05 Award acceptance | Award received 5 Jan 2027 | Acceptance by 4 Feb 2027; lapses after |
| F-06 CIC dispute | Filed 1 Oct 2026; unresolved 5 Nov 2026 | 5 days beyond 30; ₹500 expected compensation |
| F-07 Insurance Ombudsman | Insurer rejection 15 Mar 2026 | File by 15 Mar 2027 (one year); eligible immediately (rejection received) |
| F-08 Insurance, no reply | GRO complaint 1 Feb 2026, no reply | Ombudsman eligible from 1 Mar 2026 (one month) |
| F-09 Ombudsman cap | Claim ₹72 lakh; premium paid ₹48,000 | Insurance Ombudsman skipped (cap); route to the **District** Commission (consideration paid ≤ ₹50 lakh) |
| F-10 NBFC NOC | Loan closed 10 Oct 2026; NOC not received by 15 Nov 2026 | 30-day period ended 9 Nov 2026; 6 days delay shown [advisory until V-S-04] |
| F-11 RC transfer same State | Delivery note 3 Nov 2026 10:00 | Seller reports by 17 Nov 2026; buyer reports by 3 Dec 2026 |
| F-12 RC transfer other State | Delivery note 3 Nov 2026 | Seller reports by 18 Dec 2026; buyer reports by 3 Dec 2026 |
| F-13 Recovery call at 20:15 on 10 Jan 2027 | Bank loan | Breach of CHR-A-20 (post-1 Jan 2027 row) |
| F-14 Recovery call at 20:15 on 10 Dec 2026 | Bank loan | Evaluated against the pre-2027 row [advisory until V-S-03] |

Calendar-day counting excludes the start day and includes the end day [REC: confirm per forum, V-S-01].

---

## S.19 Safety track and illegal-lender playbook

The safety track runs in parallel with any vertical and opens immediately when triage detects threats of violence, threats of arrest over a civil debt, circulation or morphing of photos, extortion, contact with the user's family or employer with defamatory content, or an unregistered lender (CHR-A-06, CHR-A-29).

**PB-S1 steps**
1. Show a calm safety screen: emergency number 112, cyber-crime helpline 1930 and cybercrime.gov.in [VERIFY], and "You do not have to respond to threats; keep the evidence."
2. Evidence first: capture and hash screenshots, recordings and links before the sender deletes them (§S.16).
3. Draft T-A7 (police or cyber-crime complaint) with a facts-only chronology, exhibit index and the user's contact details; the user files online or at the police station and uploads the acknowledgement.
4. If the lender is regulated: send T-A1/T-A2 to the RE in parallel; the conduct breach is also an RB-IOS ground.
5. If the lender is unregistered: guide to RBI Sachet for unauthorised entities [VERIFY]; no RB-IOS route; no negotiation by the case manager with an unregistered lender [REC].
6. Offer a fixed-fee advocate consult for criminal-law advice (NN-41).
7. Never advise the user to pay an extortion demand or to stop paying a regulated lender; never contact the alleged harasser directly.

**Safety-track data handling.** Morphed images and intimate content are stored in a restricted evidence class with no thumbnails in lists, no AI captioning by default, and access limited to the user and named case staff; deletion on request after closure unless a legal hold applies [REC; NN-26].

---

## S.20 Closure codes and outcome taxonomy

Closure codes feed internal MIS only (NN-20). Each closed case carries exactly one primary code and optional secondary codes.

| Code | Meaning | Evidence required |
|---|---|---|
| `RES_AT_RE` | Resolved by the RE, insurer or authority at the first rung | Written reply or proof of correction |
| `RES_AT_IO` | Resolved after Internal Ombudsman review | RE final reply |
| `RES_AT_BIMA_BHAROSA` | Resolved after IRDAI escalation | Insurer reply |
| `OMB_MEDIATED` | Settled through Ombudsman mediation or conciliation | Recommendation and acceptance |
| `OMB_AWARD_COMPLIED` | Award accepted and complied with | Award and compliance proof |
| `OMB_REJECTED` | Complaint rejected or not maintainable | Ombudsman order |
| `APPEAL_DECIDED` | Appellate Authority decision | Order |
| `CC_REFERRED` | Referred to consumer commission or court via advocate | Engagement record |
| `CIC_CORRECTED` | Credit report corrected | Updated report |
| `CHALLAN_PAID` / `CHALLAN_LOK_ADALAT` / `CHALLAN_CONTEST_DISPOSED` | Challan outcomes | Receipt, Lok Adalat order, court order |
| `VEHICLE_TRANSFERRED` / `HYPOTHECATION_REMOVED` | Vehicle outcomes | RC copy, Vahan record |
| `USER_WITHDREW` | User withdrew (24-hour cooling confirmation) | In-app confirmation |
| `SELF_SERVE_ONLY_CONFLICT` | Managed service not provided due to conflict | Conflict-check log reference |
| `DECLINED_OUT_OF_SCOPE` | Not a matter the brand handles | Triage record |
| `ABANDONED` | No user activity for `chp.case.abandon_days` (default 90) after reminders | Reminder log |

Amounts recovered and compensation credited are recorded only with documentary proof and labelled MEASURED (NN-36). Amounts the user hopes to recover are never recorded as outcomes.

---

## S.21 Rule-change management

| Step | Actor | Control |
|---|---|---|
| 1. Watch | `PLT_CONTENT_EDITOR` (Consumer Help scope) monitors RBI notifications, IRDAI circulars, CCPA guidelines, MoRTH and State notifications; LDC's regulatory feed may be read as **public-source metadata only** through `int` (no client data) [REC] | Weekly checklist |
| 2. Draft rows | Editor creates new effective-dated rows; old rows get `effective_to`; transition rows where earlier cases stay under the old instrument (e.g., CHR-A-07) | Maker |
| 3. Review | `PLT_LEGAL_REVIEWER` verifies against primary text; logs in the verification log | Checker (NN-18, NN-30) |
| 4. Impact | System lists open cases whose deadlines or eligibility would change; recomputation preview | `DeadlineRecomputeJob` dry run |
| 5. Publish | No code release (NN-30); recompute; affected users notified with the reason ("RBI changed the rule on …") | Audit ledger |
| 6. Templates | Templates citing the changed provision are re-versioned; drafts in progress show a banner | Lint |

Rule rows never change retroactively for an action already taken; the case keeps the rule version that applied when the action was taken.

---

## S.22 Verification backlog (load as advisory until cleared)

| # | Item | Where to verify |
|---|---|---|
| V-S-01 | RB-IOS 2026 clause numbers used here (1(3), 3(1)(c), 8(3), 10(1)(b),(g)–(k), 10(2), 14(2), 15(4)–(5), 17(3), 20(1)) against the RBI notified text | rbi.org.in Scheme PDF |
| V-S-02 | Internal Ombudsman Directions 2026 effective date and coverage | RBI notification |
| V-S-03 | RBC Fourth Amendment (banks) and Third Amendment (NBFCs) paragraphs, call-record retention for NBFCs, "no referral while grievance open" final text; pre-2027 calling-hours guidance | RBI notifications 6 Aug 2026 |
| V-S-04 | NBFC RBC Directions 2025 paras 34–41 (prepayment, document release, ₹5,000/day) and application to vehicle hypothecation | RBI Master Direction |
| V-S-05 | KFS/APR paragraph references | DL Directions 2025; RBC Directions |
| V-S-06 | Compromise-settlement framework (8 Jun 2023) cooling period and CIC reporting | RBI PDF |
| V-S-07 | PPHI Master Circular TATs; ₹5,000/day late-award-compliance source | IRDAI |
| V-S-08 | Insurance Ombudsman complaint form and annexure; CIO practice on representatives; status of the Karnataka HC judgment | cioins.co.in; judgment text |
| V-S-09 | CPA 2019 s.69 limitation and condonation; 2014 agent regulations form; *Anuj Kumar Chauhan* citation | India Code; Delhi HC |
| V-S-10 | e-Jagriti, NCH and Bima Bharosa official URLs | Government sites |
| V-S-11 | MV Act s.200 list as amended; State compounding notifications; s.210A multipliers; Virtual Court transfer timelines; CMVR r.167 | India Code; State gazettes |
| V-S-12 | Lok Adalat rules per State | State traffic police / legal services authorities |
| V-S-13 | MV Act s.50 / CMVR r.55 transfer deadlines; Forms 28/29/30/35 versions; CMVR r.81 fees | India Code; Parivahan |
| V-S-14 | Stamp duty on vehicle sale agreements per State | State Stamp Acts |
| V-S-15 | BNS 2023 s.351 applicability; BSA s.63 certificate format | India Code |
| V-S-16 | DPDP s.17(1)(a) scope for legal-claims processing | DPDP Act |
| V-S-17 | Payment Aggregator Directions 2025 position on collecting government fines (confirms exclusion) | RBI |
| V-S-18 | Whether CMS accepts an eSigned authorisation | RBI CEPD |
| V-S-19 | Licence terms for reusing RBI-published NBFC and DLA lists | RBI website terms |
| V-S-20 | Comparator name: "ChallanWallah" not found by R2; R1 records challanwala.com | Owner |
