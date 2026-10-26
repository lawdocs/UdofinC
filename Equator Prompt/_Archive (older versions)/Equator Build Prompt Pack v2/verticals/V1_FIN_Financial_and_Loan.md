# V1 — Financial & Loan (FIN) — Vertical Specification
> Binding for P08a. Read with master, 02, Appendices A, B, F, G, K, L, M.
> Version 2.0 · law stated as at 21 October 2026 · operator: Equator Resolution Service Private Limited · owner: Head of Legal (rules) + FIN product lead (build).

---

## 0. Scope and how to use

**What this file is.** The single build specification for the `FIN` vertical: every financial-sector dispute subtype Equator accepts, signposts or refuses; the law and clocks behind each; the deterministic suitability rules; the Dispute Explorer question tree; intake forms per mechanism with full dropdown values; the modus operandi per subtype; the pre-litigation journey; document checklists; integrations; calculators with golden vectors; outputs and enforcement routes; dashboards; data-model extensions; and acceptance tests. It extends P08 §4.1 (FR-P08-13 to FR-P08-23) and does not repeat it; where this file is more specific, this file governs P08a (master X-19; §17 item 2).

**Precedence.** Master (NN-01 to NN-32, §5.2, §15, §16) → Appendix G (legal rules) → Appendix B (fees) → Appendix F (tables, events, error codes) → Appendix A (states, clocks) → this file → P08. Where this file proposes a new table, event, error sub-code or legal rule, the agent records it in `docs/adr/` and registers it in Appendix F §F.10.2 / Appendix G before use (§16, §18).

**How the coding agent uses it.**
1. Seed the taxonomy in §2 into `core.dispute_types` (L1/L2 per Appendix K plug-in framework) with the legacy P08 codes kept in `legacy_ref`.
2. Implement §4 as rule packs in `packages/rules/fin/` (pure, deterministic; NN-01, NN-02). Every row cites an Appendix G rule ID; rules not yet in Appendix G are created `status = 'UNVERIFIED'` and the dependent feature stays behind its flag (master §0).
3. Implement §5 as Dispute Explorer v2 nodes (Appendix K) — the AI `intake_assistant` may classify free text into a node answer; the tree, outcomes and clocks are computed by the rules engine.
4. Implement §6 form schemas in `packages/forms/fin/` (P02 form engine; bilingual en/hi at launch; NN-23).
5. Implement §12 calculators in `packages/rules/calculators/fin/` with the golden vectors as unit tests (FR-P08-08).
6. Implement §16 migrations, §11 APIs and events, and §17 acceptance tests (Gherkin in `tests/acceptance/fin/`).

**Out of scope here (owned elsewhere).** Enterprise API, bulk engine, clause registry and lender console (P09 FR-P09-07 to FR-P09-22 — this file specifies only FIN templates and FIN-specific rules for them); GRM `FIN_RBI` desk mechanics (P09 §5.1); fee figures (Appendix B Cards FIN-R, FIN-L, GRM, EAPI); voice-agent prompts (P11); public calculator pages (P13).

**Status markers.** **[VERIFY — open: reason]** = not confirmed against the primary instrument; the dependent feature ships behind the stated flag (default OFF where the rule is permissive, ON where it only adds a warning). `[K]` = settled statutory text not re-fetched in the 2026 research; treat as reliable but keep in the review cycle (Appendix G §G.4.3).

---

## 1. Vertical overview

### 1.1 Who and what

| Item | Content |
|---|---|
| Parties | Borrower, co-borrower, guarantor/surety, legal heir of a deceased borrower, cardholder, payer/payee (payments), merchant; lender regulated entity (RE: scheduled commercial bank, small finance bank, payments bank, RRB, UCB, NBFC-ICC, NBFC-MFI, HFC, gold-loan NBFC, ARC, non-bank PPI issuer, card issuer, payment aggregator, TPAP); lending service provider (LSP) / digital lending app (DLA); co-lending partner RE; P2P platform and its lenders; private lender. |
| Who files | Either side (Rules Art.3 symmetric initiation). Borrower-side filings are self-serve; lender-side filings come one-by-one, through bulk programmes (P09 FR-P09-11) or clause-auto default events (P09 FR-P09-10). |
| Value proposition — borrower | Free routes and deadlines shown first (RB-IOS, Internal Ombudsman, CIC correction, bank chargeback); a neutral conciliator instead of a recovery agent; written settlement with NOC, document/collateral release and bureau-update obligations tracked to completion; ₹0 fee under lender programmes (Card FIN-L). |
| Value proposition — lender | Lower cost-to-resolve than litigation or field collection; Board-policy-compliant OTS governance (approver ≥ one level above sanctioner, wilful-defaulter/fraud gating); appointment-defensible arbitration (NN-03, D1) with Independence Evidence Pack; contact-conduct compliance (NN-12) built into every message; MIS and Board exports (P09 FR-P09-15/16). |
| Equator's role | Neutral institution: administers negotiation, conciliation (A&C Act Part III), contractual mediation and institutional arbitration; signposts. Equator is **not** a recovery agent, collection agency, LSP for credit decisions, credit information company, the RBI Ombudsman, a court or DRT (Rules Art.20; copy lint FR-P08-09). |

### 1.2 Mechanisms allowed (master §5.2, FIN column)

| Mechanism | FIN default | Constraint in this file |
|---|---|---|
| `negotiation` (assisted, blind-bid on money) | ✔ | Blind-bid disabled for `FIN.RET.MF` and when any vulnerability flag is set (§4.4) |
| `conciliation` (A&C Part III) | ✔ | Recommended mode for money settlements where an enforceable outcome is wanted (s.73/s.74; LR-CONC-001) |
| `mediation` (contractual mode; statutory mode behind `mediation_statutory_mode`) | ✔ | NN-05 copy rules; no "s.27 decree" claims |
| `arbitration` | ✔ under NN-03 only | §4.6 eligibility table; blocked for bank/FI ≥ ₹20 lakh (LR-ARB-020); blocked on the offence in s.138 matters (NN-06, NN-24); Equator policy default OFF for microfinance borrowers (`fin.mfi_arbitration_enabled` = OFF) |
| `med_arb` / `arb_med` / `arb_med_arb` | ✔ | Master §5.3; different neutral by default (LR-CONC-003, LR-MED-011) |
| `expert_determination` | — (blocked) | Not offered in FIN. P08 FR-P08-13 row `fin.colending` lists it; master §5.2 prevails. Account reconciliations in co-lending B2B arbitrations use a tribunal-appointed expert under A&C s.26 instead (§18 C-02) |
| `grievance` | ✔ | GRM `FIN_RBI` desk (P09) is rung 0 for service-deficiency subtypes |
| `signposting` | ✔ | First-class outcome; closure blocked until recorded (NN-20; Appendix A §5 FIN `require_signposting = true`) |
| `posh_inquiry` | — | Not applicable |

### 1.3 Status of key laws and instruments (as of 21 October 2026)

| Instrument | Status | Effect in FIN | Register |
|---|---|---|---|
| Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026) | In force 1 Jul 2026; RB-IOS 2021 continues for complaints received before that date | RE first; 30 days; then RBI Ombudsman within 90 days; caps ₹30 lakh consequential loss + ₹3 lakh harassment/time/expenses; matters pending before court/tribunal/arbitrator not maintainable | LR-RBI-001–003 |
| RBI RE-specific Internal Ombudsman Directions, 14 Jan 2026 (NBFC: RBI/CEPD/2025-26/384; Commercial Banks: RBI/CEPD/2025-26/381) | In force (cl.7(2), 14(2), 14(4) from 30 Jun 2026); 2023 IO Master Direction repealed (cl.17) | Auto-escalation of partly/wholly rejected complaints within 20 days (cl.14(1)(b)); final reply 30 days (cl.14(9)) | LR-RBI-004, LR-RBI-022 |
| RBI (NBFC – Responsible Business Conduct) Directions 2025 (28 Nov 2025, updated 1 Jul 2026) + Third Amendment Directions 2026, RBI/2026-27/230, 6 Aug 2026 | Third Amendment effective **1 Jan 2027**; enforced now as Equator policy (NN-12) | 08:00–19:00; recording + 6-month retention; GRO details in every recovery communication; inappropriate occasions; device-lock rules and ₹250/hour compensation | LR-RBI-005–009, LR-RBI-023 |
| RBI (NBFC – Credit Facilities) Directions 2025, RBI/DOR/2025-26/347, 28 Nov 2025 (updated 15 Jul 2026), Ch. III paras 6–30 (ex-Digital Lending Directions 2025, 8 May 2025) | In force | RE responsible for LSP; repayment direct to RE; LSP fees paid by RE; cooling-off ≥ 1 day; nodal GRO; RB-IOS after 30 days | LR-RBI-010 |
| RBI (NBFC – Resolution of Stressed Assets) Directions 2025, RBI/DOR/2025-26/357, 28 Nov 2025 (updated 1 Oct 2026), paras 16, 86–100 (ex-RBI/2023-24/40, 8 Jun 2023) | In force | Compromise not a right (para 87); > 3 months = restructuring (para 89); approver ≥ one level above sanctioner (para 16(5)); wilful defaulter/fraud → Board (16(5)(ii)), without prejudice to criminal proceedings (para 97); cooling ≥ 12 months (para 95) | LR-RBI-011 |
| Master Direction – RBI (Regulatory Framework for Microfinance Loans) Directions 2022, RBI/DOR/2021-22/89, 14 Mar 2022 | In force (fold-in to Nov 2025 Directions not confirmed) | Household income ≤ ₹3,00,000 (para 3.1); repayment ≤ 50% of monthly household income incl. all loans (paras 5.1–5.2) | LR-RBI-014 |
| RBI (Lending Against Gold and Silver Collateral) Directions 2025 (6 Jun 2025) | Compliance by 1 Apr 2026 **[VERIFY — open: instrument number and paragraph numbers; secondary source only]** | Release ≤ 7 working days then ₹5,000/day; auction notice + reserve ≥ 90%; surplus refund; LTV 85/80/75% | LR-RBI-026 (new, §18) |
| RBI (Co-Lending Arrangements) Directions 2025 (6 Aug 2025) | Effective 1 Jan 2026 **[VERIFY — open: instrument number; secondary source only]** | ≥ 10% retention each RE; DLG ≤ 5%; uniform asset classification; partner booking within 15 days; single point of contact | LR-RBI-027 (new) |
| RBI (Pre-payment Charges on Loans) Directions 2025 (2 Jul 2025) | Loans sanctioned/renewed on or after 1 Jan 2026 **[VERIFY — open: instrument number; secondary source only]** | Nil pre-payment charges on floating-rate non-business loans to individuals; layered rules for MSE/business loans | LR-RBI-028 (new) |
| Credit information: RBI/2023-24/72 (26 Oct 2023) compensation framework; CICRA 2005 | In force (from ~26 Apr 2024) | CI 21 days + CIC 9 days; then ₹100/calendar day | LR-RBI-013 |
| Release of documents: RBI/2023-24/60 (13 Sep 2023) | In force for releases due on/after 1 Dec 2023 | Personal loans: 30 days, then ₹5,000/day; lost documents +30 days | LR-RBI-024 |
| Penal charges: RBI/2023-24/53 (18 Aug 2023) | Effective 1 Apr 2024 | Not capitalised; separate head | LR-RBI-012 |
| Digital Payments – E-mandate Framework 2026, RBI/DPSS/2026-27/396, 21 Apr 2026 | In force | AFA-free ₹15,000 per debit for loan/settlement instalments; ₹1 lakh only for insurance, MF, credit-card bills; pre-debit notice ≥ 24 h | LR-PAY-003 |
| RBI (Regulation of Payment Aggregators) Directions 2025, RBI/DPSS/2025-26/141, 15 Sep 2025 | In force | Settlement money never through Equator's merchant account | LR-PAY-001 (NN-13) |
| RBI (NBFC – Account Aggregator) Directions 2025, RBI/DoR/2025-26/368, 28 Nov 2025 | In force | FIU must be financial-sector regulated (para 8(12)) — Equator cannot be FIU | LR-RBI-021 (NN-14) |
| Credit Card and Debit Card – Issuance and Conduct Directions 2022 (21 Apr 2022) | In force `[K]` **[VERIFY — open: current consolidated location after 28 Nov 2025; ₹500/day closure compensation and 30-day billing-dispute rule unchanged? (S3 OLQ-7)]** | Closure ≤ 7 working days else ₹500/day; billing dispute response 30 days | LR-RBI-029 (new) |
| TAT harmonisation, RBI/2019-20/67 (20 Sep 2019); ODR for digital payments, RBI/2020-21/21 (6 Aug 2020); customer liability circular DBR.No.Leg.BC.78/09.07.005/2017-18 (6 Jul 2017) | In force | Auto-reversal TATs and ₹100/day compensation; zero liability if reported within 3 working days (third-party breach) `[K]` | LR-PAY-004 |
| NPCI UPI OC No. 213/2024-25 (10 Feb 2025, eff. 15 Feb 2025) | In force | Auto-acceptance/rejection of chargebacks raised by bulk upload/UDIR | LR-PAY-008 (new; LR-PAY-007 is Appendix Q's SAQ A row) |
| NI Act 1881 ss.138, 142, 143A, 147, 148; *Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158 (25 Sep 2025) | In force | Compounding costs: nil before defence evidence; 5% after defence evidence before judgment; 7.5% Sessions/HC; 10% SC | LR-RBI-017–019 |
| SARFAESI Act 2002; RDB Act 1993 (₹20 lakh, S.O. 4312(E), 6 Sep 2018) | In force | Non-arbitrable/non-mediable enforcement; Equator mediates OTS "around" it | LR-RBI-015, LR-ARB-020 |
| IBC 2016 ss.14, 94–96, 101 | In force (Part III for personal guarantors to corporate debtors from 1 Dec 2019) | Corporate debtor on hold after CIRP admission; PG on hold from s.94/95 filing | LR-RBI-016 |
| Mediation Act 2023 | Only ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 in force (S.O. 4384(E), 9 Oct 2023); MCI established S.O. 4781(E), 27 Aug 2026 | Contractual mode only; settlements are contracts unless Part III conciliation (s.74) or consent award (s.30) | LR-MED-012, NN-05 |
| A&C Act 1996 (CORE, 8 Nov 2024; *Bhadra International*, SC 5 Jan 2026; *Madhyachal Steels*, Del HC 24 Aug 2026; *Sundaram Finance v Hanuman Prasad*, Raj HC 24 Apr 2026; *Radiance Galore v Yes Bank*, Bom HC 17 Jul 2025) | In force | Appointment defensibility (NN-03) | LR-ARB-001–004, LR-ARB-030 |
| DPDP Act 2023 + Rules 2025 (G.S.R. 846(E), 13 Nov 2025) | Rule 4 from 13 Nov 2026; core obligations 13 May 2027 (build now) | Respondent contact before engagement under s.17(1)(a); borrower data minimisation | NN-15 |
| TCCCPR 2018 as amended (Third Amendment Regulations 2026, No. 05 of 2026, 18 Sep 2026); TRAI PR 91/2026 (1600 series) | In force | Lender-number (1600) mode for lender-referred FIN calls; A2P declarations | LR-TEL-001–009 |

---

## 2. Subtype taxonomy

### 2.1 Taxonomy rules

- Two levels (D2-01; Appendix K): **L1** category → **L2** subtype. `core.dispute_types.code` = L2 code; `l1_code` stored on the row; `legacy_ref` holds the P08 FR-P08-13 code.
- Two kinds of L2 subtype: **product** subtypes (`FIN.RET.*`, `FIN.BUS.MS`, `FIN.BUS.GT`) and **issue** subtypes (`FIN.CND.*`, `FIN.SET.*`, `FIN.PAY.*`, `FIN.BUS.CB/CL`). Every case records exactly one **primary** L2 (chosen by the Explorer precedence in §5.1) plus `secondary_subtypes[]` (e.g., a home loan with a SARFAESI notice = primary `FIN.SET.SF`, secondary `FIN.RET.HL`). The attribute `loan_product` (DD-FIN-010) is captured on every case regardless of primary subtype.
- **Value bands** (DD-FIN-020): `VB1` < ₹50,000 · `VB2` ₹50,000–₹5,00,000 · `VB3` ₹5,00,001–₹20,00,000 · `VB4` ₹20,00,001–₹1,00,00,000 · `VB5` > ₹1,00,00,000. Bands drive neutral grade eligibility (Appendix N), fee bands (Appendix B) and the DRT test (bank/FI ≥ ₹20,00,000).
- **Ladder codes** (§7.1): `fin.std` (Appendix A §4.1), `fin.grv` (grievance-first), `fin.ni` (s.138 civil settlement), `fin.sf` (around SARFAESI/DRT), `fin.mf` (microfinance safeguarded), `fin.pay` (bank/network process first), `fin.b2b` (RE–RE / RE–LSP), `fin.ots` (self-serve OTS portal → conciliation).
- ✔ = permitted · ◐ = permitted with conditions (named) · ✖ = blocked (non-configurable).

### 2.2 Taxonomy table

| L1 | L2 code | Name | Typical parties | Value band | Default ladder | Negotiable | Mediable | Arbitrable | Signpost forum (parallel) | Notes (legacy_ref) |
|---|---|---|---|---|---|---|---|---|---|---|
| `FIN.RET` Retail loans & cards | `FIN.RET.PL` | Personal / consumer loans (term, salary, top-up, consumer durable, app PL) | Borrower, co-borrower, bank/NBFC, LSP | VB1–VB3 | `fin.std` | ✔ | ✔ | ◐ NBFC with ex-ante clause (§4.6); bank/FI only < ₹20 lakh | RB-IOS; IO; Consumer Commission; Lok Adalat | `fin.loan_default:personal` |
| | `FIN.RET.CC` | Credit cards | Cardholder, issuer (bank/NBFC), collection agency | VB1–VB3 | `fin.std` (+ chargeback first for txn disputes) | ✔ | ✔ | ◐ as PL | Issuer dispute/chargeback; RB-IOS; Consumer Commission | `fin.loan_default:credit_card` |
| | `FIN.RET.DL` | BNPL / digital lending / LSP | Borrower, RE, LSP/DLA | VB1–VB2 | `fin.grv` | ✔ | ✔ | ◐ RE-named clause only; never with LSP as claimant | DL nodal GRO → RB-IOS; Sachet; 1930 (illegal apps) | `fin.digital_lending` |
| | `FIN.RET.GL` | Gold (and silver) loans | Borrower, gold-loan NBFC/bank | VB1–VB3 | `fin.std` | ✔ | ✔ | ◐ as PL | RB-IOS; police (theft/misappropriation) | `fin.loan_default:gold` |
| | `FIN.RET.VL` | Vehicle loans (car, two-wheeler, CV, tractor) | Borrower, NBFC/bank, repossession agency | VB2–VB4 | `fin.std` | ✔ | ✔ | ◐ as PL | RB-IOS; police (force in repossession) | `fin.loan_default:vehicle` |
| | `FIN.RET.HL` | Home loans / LAP | Borrower(s), HFC/bank/NBFC | VB3–VB5 | `fin.std`; `fin.sf` if SARFAESI | ✔ | ✔ | ◐ HFC/NBFC with clause; bank/FI ≥ ₹20 lakh ✖ | RB-IOS (HFCs excluded — NHB grievance route **[VERIFY — open: HFC grievance escalation route under RB-IOS 2026 exclusion]**); DRT | `fin.loan_default:home` |
| | `FIN.RET.EL` | Education loans | Student, co-borrower parent, bank/NBFC | VB2–VB4 | `fin.std` | ✔ | ✔ | ◐ as PL | RB-IOS; Vidya Lakshmi portal (subsidy) | `fin.loan_default:education` |
| | `FIN.RET.MF` | Microfinance (JLG/SHG/individual MFI loans) | Borrower (household), NBFC-MFI/SFB/bank, group members | VB1 | `fin.mf` | ✔ (no blind-bid) | ✔ shuttle-only default | ✖ policy default (`fin.mfi_arbitration_enabled` OFF) | RB-IOS; police (coercion) | `fin.loan_default:microfinance` |
| | `FIN.RET.PP` | P2P platform loans and private (individual) loans | Borrower, P2P lenders, platform; individuals | VB1–VB3 | `fin.std` | ✔ | ✔ | ◐ with written agreement to arbitrate (post-dispute or ex-ante) | Civil court; State Money-lenders Act authority; police (usury) | `fin.loan_default:p2p` |
| `FIN.BUS` Business & structured credit | `FIN.BUS.MS` | MSME / business loans (term, CC/OD, invoice discounting, equipment) | MSME borrower, promoters/PGs, bank/NBFC | VB3–VB5 | `fin.std`; `fin.sf` if SARFAESI | ✔ | ✔ | ◐ NBFC with clause; bank/FI ≥ ₹20 lakh ✖ | DRT; NCLT (IBC); MSEFC (own receivables — separate COM case) | `fin.loan_default:business_msme` |
| | `FIN.BUS.CL` | Co-lending — borrower-facing | Borrower, originating RE, partner RE | VB2–VB4 | `fin.std` (both REs joined) | ✔ | ✔ | ◐ only if both REs' clauses name Equator | RB-IOS (each RE); single point of contact | `fin.colending:borrower` |
| | `FIN.BUS.CB` | Co-lending / fintech partnership — B2B (RE–RE, RE–LSP) | Banks, NBFCs, LSPs | VB4–VB5 | `fin.b2b` | ✔ | ✔ | ✔ (commercial; equal footing not presumed — registrar sets `equal_footing`, NN-03) | — (RB-IOS excludes RE-vs-RE) | `fin.colending:b2b` |
| | `FIN.BUS.GT` | Guarantor / co-obligor disputes | Guarantor, co-guarantors, lender, principal debtor | VB2–VB5 | `fin.std` | ✔ | ✔ | ◐ guarantee deed must carry or incorporate the clause | DRT (bank/FI ≥ ₹20 lakh); NCLT/DRT (PG insolvency) | `fin.guarantee` |
| `FIN.CND` Conduct, charges & information | `FIN.CND.RC` | Recovery-agent / collection conduct | Borrower, guarantor, RE, recovery agency | VB1–VB3 (compensation) | `fin.grv` + safety screen | ✔ | ✔ (compensation, undertakings, underlying debt) | ✖ (conduct complaint) | Police 112 (danger); 1930; RE GRO → IO → RB-IOS | `fin.recovery_conduct` |
| | `FIN.CND.CH` | Wrong/excess charges, penal charges, mis-selling, bundled insurance | Borrower, RE, corporate agent | VB1–VB2 | `fin.grv` | ✔ | ✔ | ◐ only if borrower elects after consumer-forum disclosure (LR-CONS-003) | RE GRO → RB-IOS; Consumer Commission; Insurance Ombudsman (bundled policy — INS case) | `fin.wrong_charges`, `fin.mis_selling` |
| | `FIN.CND.CR` | Credit-report disputes (CICRA 2005) | Borrower/guarantor, CI (lender), CIC | VB1 (compensation) | `fin.grv` | ✔ | ✔ (CI obligations only) | ✖ (CIC not bound; correction is statutory) | CI + CIC dispute (30 days); RB-IOS (CICs covered) | `fin.credit_bureau` |
| `FIN.PAY` Payments | `FIN.PAY.TX` | Failed / disputed digital transactions (UPI, IMPS, NEFT/RTGS, AePS, NACH, wallet) | Payer, payee, bank, PPI issuer, TPAP | VB1 | `fin.pay` | ✔ | ◐ only after bank process fails or on joint consent | ✖ retail | Bank complaint/UDIR → RB-IOS; 1930 (fraud) | new |
| | `FIN.PAY.CB` | Card/PPI chargeback and merchant–customer disputes | Cardholder/customer, merchant, issuer | VB1–VB2 | `fin.pay` | ✔ | ✔ (merchant–customer) | ✖ consumer side; ◐ B2B | Issuer chargeback; Consumer Commission; NCH 1915 | new |
| | `FIN.PAY.MP` | Merchant–payment aggregator (B2B) | Merchant, PA, acquiring bank | VB2–VB5 | `fin.b2b` | ✔ | ✔ | ✔ with clause | — | new |
| `FIN.SET` Settlement & enforcement-adjacent | `FIN.SET.OT` | OTS / compromise / restructuring (cross-cutting) | Borrower(s), guarantors, RE | VB1–VB5 | `fin.ots` or `fin.std` | ✔ | ✔ (Part III recommended) | ◐ consent award only where valid arbitration basis exists | RB-IOS (service issues); Lok Adalat | `fin.ots_restructuring` |
| | `FIN.SET.NI` | NI Act s.138 — civil settlement + compounding pack (NN-24) | Drawer (accused), payee (complainant) | VB1–VB4 | `fin.ni` | ✔ (money only) | ✔ (money only) | ✖ (offence; NN-06) | Trial court (compounding s.147); Lok Adalat | `fin.ni138` |
| | `FIN.SET.SF` | SARFAESI pre-measure / around-enforcement settlement | Borrower, guarantors, bank/FI/notified NBFC/ARC | VB3–VB5 | `fin.sf` | ✔ | ✔ (OTS terms only) | ✖ while measures are live (policy; §4.6) | DRT s.17 (45 days from measure); Lok Adalat | `fin.secured_enforcement:s13_2_notice` |
| | `FIN.SET.DR` | DRT-pending matter — settlement and signposting | Borrower, guarantors, bank/FI | VB4–VB5 | `fin.sf` | ✔ | ✔ (joint memo for DRT) | ✖ (DRT exclusive) | DRT/DRAT; Lok Adalat (DRT-organised) | `fin.secured_enforcement:drt_oa` |
| `FIN.SIG` Signpost only (no Equator administration) | `FIN.SIG.EN` | SARFAESI measure challenge / DRT adjudication itself | — | — | `signposting` | ✖ | ✖ | ✖ | DRT s.17; DRAT | LR-RBI-015 |
| | `FIN.SIG.FR` | Fraud / wilful-defaulter classification challenge | — | — | `signposting` | ✖ | ✖ (OTS terms around it ◐ with Board-approval flag) | ✖ | Writ/civil court; RBI | LR-RBI-011 |
| | `FIN.SIG.IL` | Unregistered lending apps, illegal moneylending, extortionate "loans" | — | — | `signposting` | ✖ | ✖ | ✖ | 1930 / cybercrime.gov.in; police; Sachet (sachet.rbi.org.in); State Money-lenders Act authority | PI-FIN-10 |
| | `FIN.SIG.CR` | Threats, violence, extortion, sexual harassment by agents; unauthorised-transaction fraud | — | — | `signposting` (urgent) | ✖ | ✖ (civil compensation may follow separately once safe) | ✖ | 112; 1930; police; RE GRO | NN-24 |

### 2.3 Legacy mapping (P08 → V1)

| P08 FR-P08-13 code | V1 L2 primary (default) | Rule |
|---|---|---|
| `fin.loan_default` | `FIN.RET.*` by `loan_product`; `FIN.BUS.MS` for business_msme | sub_type → L2 |
| `fin.ots_restructuring` | `FIN.SET.OT` | — |
| `fin.ni138` | `FIN.SET.NI` | — |
| `fin.wrong_charges`, `fin.mis_selling` | `FIN.CND.CH` | `issue_kind` DD-FIN-071 keeps the distinction |
| `fin.digital_lending` | `FIN.RET.DL` | — |
| `fin.recovery_conduct` | `FIN.CND.RC` | — |
| `fin.credit_bureau` | `FIN.CND.CR` | — |
| `fin.guarantee` | `FIN.BUS.GT` | — |
| `fin.colending` | `FIN.BUS.CB` (B2B) / `FIN.BUS.CL` (borrower) | by `initiator_role` |
| `fin.secured_enforcement` | `FIN.SET.SF` / `FIN.SET.DR`; adjudication → `FIN.SIG.EN` | `signpost_only` preserved for `FIN.SIG.EN` |

---

## 3. Legal framework by subtype

### 3.1 Common framework (applies to every FIN L2)

| Topic | Rule | Source | Register |
|---|---|---|---|
| Enforceable outputs today | (1) s.73 conciliation settlement with s.74 award status (A&C Part III); (2) consent award s.30 (needs valid arbitration agreement + properly appointed arbitrator, not the mediator by default); (3) Lok Adalat award (deemed decree, LSA Act s.21) via DLSA joint application (s.20(2)); (4) compromise recorded by a court/DRT (CPC O.XXIII r.3; RDB Act proceedings); (5) contractual MSA (suit on contract) | A&C Act 1996 ss.30, 73, 74, 36; LSA Act 1987 ss.19–21; CPC O.XXIII r.3 `[K]` | LR-CONC-001, LR-ARB-018, LR-MED-012, LR-RBI-020 |
| Limitation | Equator processes never stop limitation (Appendix A clock invariant 3). Money suits on loans: 3 years `[K]` **[VERIFY — open: correct Limitation Act Article per loan structure (Arts. 19, 21, 37, 55) — counsel to map]**; acknowledgment in writing (s.18) and part-payment (s.19) give a fresh period — settlement drafts surface this to both sides; arbitration: s.43 A&C applies the Limitation Act; s.11 application 3 years from failure to appoint after s.21 notice (*Arif Azim*, 2024 INSC 155) | Limitation Act 1963 ss.18, 19; A&C s.43 | LR-ARB-031; `limitation_contract` clock |
| Grievance ladder | RE GRO (30 days) → NBFC/bank IO auto-escalation (day 20) → final reply (day 30) → RB-IOS within 90 days of 30-day lapse or RE reply; digital lending nodal GRO → CMS after 30 days | RB-IOS 2026; IO Directions 2026 cl.14; Credit Facilities Directions 2025 para 12 | LR-RBI-001/002/004/010 |
| Consumer forum | Borrower who is a "consumer" may elect the Consumer Commission; an arbitration clause cannot oust it; limitation 2 years; pecuniary tiers by consideration paid | CPA 2019 ss.2(7), 34–35, 69; G.S.R. 912(E) (30 Dec 2021); *Emaar MGF v Aftab Singh* (2019) 12 SCC 751 | LR-CONS-001–003 |
| Fees on borrower | Equator fees never added to borrower dues unless KFS-disclosed + explicit consent, or awarded as costs (s.31A) | KFS instructions (15 Apr 2024, now RBC Directions 2025); Credit Facilities Directions 2025 para 10(4)–(5); A&C s.31A | LR-RBI-025; X-07 |
| Contact conduct | NN-12 window, recording, GRO footer, blackout, borrower/guarantor-only discussion; applied to every FIN contact as Equator policy because the RBC text does not define "recovery-related communication" | RBI/2026-27/230 paras 100P, 100X, 100Y, 100Z, 100AA | LR-RBI-005–009, LR-RBI-023 |
| Data rails | No bureau pull, AA, CKYC by Equator; only through regulated tenant credentials or party upload | CICRA 2005 s.2(l); CIC Regulations 2006 reg 3, 9; AA Directions 2025 para 8(12) | LR-RBI-021, NN-14 |
| Money | Settlement sums to lender's own account, bank escrow with trustee, or direct with proof — never Equator's merchant account | PA Directions 2025 paras 10, 16–18; Credit Facilities Directions 2025 para 10(2)–(3) | LR-PAY-001, NN-13 |
| Confidentiality and admissibility | Conciliation statements inadmissible (s.81); confidentiality (s.75); conciliation pending → parties shall not start arbitral/judicial proceedings save to preserve rights (s.77) | A&C ss.75, 77, 81 | LR-CONC-004/005 |
| Criminal dimension | Equator never mediates an offence; s.138 civil money dispute only; court decides compounding (NN-24) | NI Act s.147; master NN-24 | LR-RBI-018 |

### 3.2 Framework by subtype

| L2 | Statute / instrument and section | Forum(s) | Limitation / statutory clocks | Recent case law / notes | Status |
|---|---|---|---|---|---|
| `FIN.RET.PL` | Contract Act; KFS rule (fees outside KFS need explicit consent); penal charges RBI/2023-24/53 (not capitalised); release of documents RBI/2023-24/60 (30 d + ₹5,000/day; lost docs +30 d); Pre-payment Charges Directions 2025 (nil for floating-rate non-business individual loans sanctioned/renewed ≥ 1 Jan 2026) **[VERIFY — open: instrument number]**; compromise paras 86–100 | Civil court / commercial court; DRT (bank/FI ≥ ₹20 lakh); RB-IOS; Consumer Commission; Lok Adalat; arbitration (NBFC, ex-ante clause) | 3 years `[K]`; RB-IOS 30 + 90 days; doc release 30/60 days | Restructuring if payment > 3 months (para 89). "Settled" vs "closed" bureau status is a commercial term, not an error (no RBI rule compels "closed" **[VERIFY — open: unverified in research (S3)]**) | In force |
| `FIN.RET.CC` | Credit Card and Debit Card – Issuance and Conduct Directions 2022 `[K]`: closure ≤ 7 working days else ₹500/day; billing dispute explanation ≤ 30 days; no unsolicited cards/upgrades **[VERIFY — open: S3 OLQ-7]**; customer-liability circular (6 Jul 2017): zero liability if third-party breach reported within 3 working days `[K]`; e-mandate ₹1 lakh AFA-free applies only to card bill payments (LR-PAY-003) | Issuer → IO → RB-IOS; Consumer Commission; civil court | Network chargeback windows (typically 120 days **[VERIFY — open: network rules not verified]**); RB-IOS 30 + 90 | Interest continues to compound during dispute — settlement may freeze it by agreement only | In force |
| `FIN.RET.DL` | Credit Facilities Directions 2025 Ch. III: RE responsible (para 6); KFS (9(1)); repayment direct to RE, no pool account (10(2)–(3)); LSP fees paid by RE (10(4)–(5)); cooling-off ≥ 1 day (11(1)); nodal GRO + CMS after 30 days (12); DLG ≤ 5% (DLG guidelines 8 Jun 2023 `[K]`); DPDP s.12 erasure (from 13 May 2027) | RE nodal GRO → RB-IOS; Sachet; police/1930 for illegal apps or morphing/threats (BNS 2023 offences `[K]`; IT Act 2000) | Cooling-off from disbursal; GRO 30 days; RB-IOS 90 | No settlement binds unless the **RE** signs (LSP is not the lender) — PI-FIN-10 | In force |
| `FIN.RET.GL` | Gold and Silver Collateral Directions 2025 (6 Jun 2025; compliance 1 Apr 2026): LTV 85% (≤ ₹2.5 lakh) / 80% (₹2.5–5 lakh) / 75% (> ₹5 lakh); assay in borrower's presence with certificate; release same day, max 7 working days, then ₹5,000/day (RE-caused delay); auction: prior notice, public notice, reserve ≥ 90% of current value, no bidding by lender/related parties; surplus refund mechanism; loss/damage: repair + compensation; bullet consumption loans ≤ 12 months **[VERIFY — open: instrument number, paragraphs, valuation reference price; legacy loans renewed after 1 Apr 2026 (S3 OLQ-6)]** | RE → IO → RB-IOS; civil court; police (theft/misappropriation) | Release 7 working days; auction notice periods per agreement and Directions | Legacy flag: `sanction_date` < 1 Apr 2026 → old regime rules shown as "may not apply" | In force (secondary source) |
| `FIN.RET.VL` | NBFC RBC Directions 2025 FPC (notice before repossession, valuation, sale procedure) `[K]`; RBC Third Amendment from 1 Jan 2027 (ID card + authorisation letter for visits, 100X); Central Motor Vehicles Rules 1989 Form 35 (termination of hypothecation) `[K]`; release of documents rule for personal-purpose vehicle loans (RBI/2023-24/60) | RE → IO → RB-IOS; civil court; police (use of force); MACT/INS for accident-linked total loss (cross-vertical) | Doc release 30/60 days; RB-IOS 30 + 90 | Total-loss insurance proceeds paid to financier → borrower balance dispute links to an INS case | In force |
| `FIN.RET.HL` | Pre-payment Directions 2025 (individual non-business floating nil; business loans to individuals/MSEs: nil for commercial banks excl. SFB/RRB/LAB, Tier-4 UCBs, Upper-Layer NBFCs, AIFIs; SFB/RRB/Tier-3 UCB/StCB/CCB/Middle-Layer NBFC nil up to ₹50 lakh) **[VERIFY — open: instrument number]**; release of documents (personal loans incl. home loans); HFCs within Credit Facilities Directions scope (para 3(1)); SARFAESI (see `FIN.SET.SF`) | RE; RB-IOS (HFCs excluded from RB-IOS coverage — LR-RBI-002); NHB grievance route **[VERIFY — open: HFC grievance escalation route (Q-09)]**; DRT; civil court | Doc release 30/60 days; SARFAESI clocks (§3.2 `FIN.SET.SF`) | Silent tenor extension on rate reset is a frequent issue — mediate rate/tenor; RERA/builder issues go to COM | In force |
| `FIN.RET.EL` | IBA Model Education Loan Scheme (moratorium = course + 1 year) `[K]`; CSIS interest subsidy `[K]`; PM-Vidyalaxmi (approved Nov 2024) **[VERIFY — open: current limits and grievance owner (S3 OLQ-14)]** | Bank → IO → RB-IOS; Vidya Lakshmi portal; DRT (bank ≥ ₹20 lakh); civil court | Limitation runs from default `[K]` | Student abroad → cross-border e-sign/notice; co-borrower parent's assets | In force |
| `FIN.RET.MF` | Microfinance MD 2022 paras 3.1, 5.1–5.2, 6A (KFS); RBC conduct rules (NBFC-MFI is an NBFC) | RE → IO → RB-IOS; police (coercion) | RB-IOS 30 + 90 | No transfer of one member's dues to others without each member's free consent (PI-FIN-13); women borrowers' privacy from family | In force |
| `FIN.RET.PP` | NBFC-P2P Directions 2017 as amended (Aug 2024: no assured returns; escrow T+1) `[K]` **[VERIFY — open: amendment text]**; Contract Act; State Money-lenders Acts (usury caps vary by State) **[VERIFY — open: State cap table]** | Civil court; P2P platform grievance → RB-IOS (if platform covered); State authority | 3 years `[K]`; acknowledgment s.18 | Each actual lender must be joined; private loans often undocumented — rely on transfer proofs and chats (BSA 2023 s.63 certificate) | In force |
| `FIN.BUS.MS` | Compromise framework paras 86–100; MSME revival and rehabilitation framework (revised) for stressed MSME accounts up to ₹25 crore `[K]` **[VERIFY — open: current consolidated paragraph]**; Pre-payment Directions 2025 (MSE business loans); MSMED Act 2006 ss.15–18 for the MSME's own receivables (separate COM case; interest at 3× Bank Rate = 17.25% at 5.75% Bank Rate, read from config) | DRT (bank/FI ≥ ₹20 lakh); NCLT (IBC s.7/9 threshold ₹1 crore `[K]`); civil/commercial court; arbitration (NBFC clause) | 3 years `[K]`; IBC moratorium (LR-RBI-016) | PG proceedings continue during CD's CIRP (*SBI v V. Ramakrishnan* (2018) 17 SCC 394) | In force |
| `FIN.BUS.CL` | Co-Lending Directions 2025 (eff. 1 Jan 2026): ≥ 10% retention each RE; originating-RE DLG ≤ 5%; borrower-level classification shared; blended rate and all fees in KFS/APR; partner share booked within 15 days else stays with originator; single point of contact in loan agreement **[VERIFY — open: instrument number; who is SPOC for grievances (S3 OLQ-10)]** | Each RE's GRO → RB-IOS | RB-IOS per RE | Borrower settlement must be signed by **both REs**, each within its own Board policy (LR-RBI-011) | In force (secondary source) |
| `FIN.BUS.CB` | Master co-lending agreement / LSP agreement (Contract Act); Co-Lending Directions 2025; DLG guidelines; Credit Facilities Directions para 6 (outsourcing) | Arbitration (institutional); commercial court | 3 years from breach `[K]`; s.29A 12 + 6 months | Classification decisions are regulatory and not tradeable; reconciliation needs loan-level data — DPDP purpose limitation between REs | In force |
| `FIN.BUS.GT` | Indian Contract Act 1872 ss.126–147 (s.128 co-extensive; s.133 variance discharge; s.134 release of principal; s.135 composition/time; s.139 impairing surety's remedy; s.140 subrogation; s.138 release of one co-surety; s.146 equal contribution) `[K]`; IBC ss.94–96 (PG) | DRT (bank/FI ≥ ₹20 lakh); civil court; NCLT/DRT (PG insolvency) | 3 years from invocation/breach `[K]`; s.96 interim moratorium from filing | *Lalit Kumar Jain v UoI* (2021) 9 SCC 321; *Dilip B. Jiwrajka v UoI* (SC, 9 Nov 2023) | In force |
| `FIN.CND.RC` | RBC Third Amendment 2026 (eff. 1 Jan 2027): 100Y(4) 08:00–19:00; 100Y(6) inappropriate occasions; 100P recording 6 months; 100AA GRO details; 100Y(1) borrower/guarantor only; 100Z(5) threatening/anonymous calls; 100X visits; 100S–100U device lock (30/60 DPD; unlock 1 hour; ₹250/hour capped at disbursed amount). Pre-2027 conduct: existing FPC/recovery-agent instructions in RBC Directions 2025 `[K]` | Police 112 / BNS 2023 (criminal intimidation, extortion `[K]`); RE GRO → IO → RB-IOS; civil court (tort) | `incident_date` < 1 Jan 2027 → legacy standard; RB-IOS 30 + 90 | Equator never "mediates away" crime; compensation + undertaking + debt settlement are mediable | Final, effective 1 Jan 2027 |
| `FIN.CND.CH` | Penal charges circular; KFS rule; Pre-payment Directions; insurance bundling → IRDAI/INS vertical | RE GRO → RB-IOS; Consumer Commission | RB-IOS 30 + 90; consumer 2 years | Refund/correction folded into settlement; mis-sold insurance spawns linked INS case | In force |
| `FIN.CND.CR` | CICRA 2005 ss.15, 17, 18, 19, 20, 21, 22 `[K]`; RBI/2023-24/72 (CI 21 d + CIC 9 d; ₹100/day); RBI/2023-24/71 (alerts, customer service); IO Directions cl.14(5) exclude CICRA s.18 disputes; RB-IOS 2026 covers CICs | CI + CIC dispute; RB-IOS | 30 days then ₹100/day | Accurate adverse history cannot be deleted by settlement; "closed" vs "settled" wording is a negotiable CI obligation **[VERIFY — open: S3 OLQ-11]** | In force |
| `FIN.PAY.TX` | TAT circular RBI/2019-20/67 (auto-reversal TAT; ₹100/day) `[K]` figures; ODR for PSOs RBI/2020-21/21; customer-liability circular (6 Jul 2017); PPI MD 2021 `[K]`; NPCI UPI OC 213/2024-25 | Bank/PPI issuer → RB-IOS; NPCI UDIR (bank-side); 1930 (fraud) | TAT per channel (config table §12 C-FIN-17) | Equator cannot reverse payments; wrong-beneficiary needs recipient consent (bank won't disclose identity) | In force |
| `FIN.PAY.CB` | Card network rules (contractual); Credit Card Directions 2022; CPA 2019 / E-Commerce Rules 2020 r.4(4)–(5) (48 h acknowledgement / 1-month redress `[K]`) | Issuer chargeback; Consumer Commission; NCH 1915 | Network windows **[VERIFY — open: network rules not verified]**; consumer 2 years | Mediation only after chargeback outcome or on joint consent | In force |
| `FIN.PAY.MP` | PA Directions 2025 (merchant contracts, escrow, settlement); merchant agreement | Arbitration; commercial court | 3 years `[K]` | Funds held in PA escrow per Directions — settlement must route via PA's escrow rules | In force |
| `FIN.SET.OT` | Resolution of Stressed Assets Directions 2025 paras 16, 86–100; e-mandate ₹15,000 AFA rule | Lender internal; Lok Adalat; DRT/court recording | Cooling ≥ 12 months; quarterly reporting (para 93) | Technical write-off does not waive claims (para 91) | In force |
| `FIN.SET.NI` | NI Act ss.138 provisos (a)–(c), 141, 142(1)(b), 142(2), 143A, 147, 148; *Sanjabij Tari*, 2025 INSC 1158 (cost slabs; e-summons; QR/UPI payment); *Damodar S. Prabhu* (2010) 5 SCC 663 (historical); *Meters & Instruments v Kanchan Mehta* (2018) 1 SCC 560 `[K]` | Magistrate court (s.138 complaint); Sessions/HC (appeal/revision); Lok Adalat | Notice ≤ 30 days of return memo; drawer 15 days; complaint ≤ 1 month of cause of action (day excluded — *Econ Antri v Rom Industries* (2014) 11 SCC 769 `[K]`); jurisdiction: payee's bank branch (s.142(2)) | Civil dispute only; "no threat of conviction" declaration; court alone compounds (NN-24) | In force |
| `FIN.SET.SF` | SARFAESI Act 2002 ss.13(2) (60 days), 13(3A) (reply 15 days), 13(4), 13(8) (redemption ends on publication of auction notice — *Celir LLP v Bafna Motors*, 2023 INSC 838, 21 Sep 2023), 14, 17 (45 days), 31 (exclusions: agricultural land, security < ₹1 lakh, outstanding < 20% of principal + interest) `[K]`; Security Interest (Enforcement) Rules 2002 r.8(6), r.9(1) (30-day sale notice) `[K]`; notified NBFCs (assets ≥ ₹100 crore) for secured debts ≥ ₹20 lakh **[VERIFY — open: notification number and date]** | DRT (s.17); DRAT; CMM/DM (s.14) | 13(2) + 60 d; 13(3A) reply 15 d; s.17 45 d from measure; redemption warning on auction-notice publication | *Mardia Chemicals* (2004) 4 SCC 311; Equator never promises a stay | In force |
| `FIN.SET.DR` | RDB Act 1993 ss.1(4) (₹20 lakh; S.O. 4312(E), 6 Sep 2018), 2(h), 17, 18, 19, 24 `[K]` | DRT; DRAT; Recovery Officer | RDB s.24 applies Limitation Act `[K]` | DRT can record a compromise; Equator prepares joint memo; LR-ARB-020 FI list **[VERIFY — open: RDB s.2(h)(ii) notified FI list (Q-11)]** | In force |
| `FIN.SIG.*` | As named in §2.2 | As named | — | Signposting event mandatory (NN-20) | — |

---

## 4. Suitability and eligibility rules

Implemented as rule pack `fin.suitability@2` in `packages/rules/fin/` (evaluated top to bottom; first terminal outcome wins; all matching signposting rows are delivered; NN-01/NN-02). Outcome codes: `ACCEPT`, `ACCEPT_COND` (conditions listed), `SIGNPOST` (Equator does not administer; forum pack issued), `REJECT` (with reason and any forum). Every evaluation writes `equator.routing.triage.evaluated.v1` with rule IDs.

### 4.1 Decision table

| # | Inputs (condition) | Outcome | Conditions / routes blocked (error sub-code → canonical) | Signposting + last date | Rule |
|---|---|---|---|---|---|
| S01 | `safety_risk_now = true` OR `conduct_type[]` ∋ threat/violence/extortion/sexual_harassment | `SIGNPOST` (urgent; §4.3) | Joint sessions blocked; case may reopen as `FIN.CND.RC` money/undertaking claim after safety review (`safeguarding_lead`) | 112; 1930; police; RE GRO | NN-24, LR-RBI-008 |
| S02 | `re_type ∈ {unregulated_lender, private_moneylender}` AND lender is an app OR `re_disclosed_in_app = false` with no RE identified after lookup | `SIGNPOST` `FIN.SIG.IL` | Do not convene; do not treat the "debt" as lawful (`FIN_RE_NOT_IDENTIFIED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`) | 1930 / cybercrime.gov.in; police; Sachet; State Money-lenders authority | PI-FIN-10, LR-RBI-010 |
| S03 | `relief_sought` = challenge to fraud or wilful-defaulter classification | `SIGNPOST` `FIN.SIG.FR` | All mechanisms on classification blocked; OTS terms may still be mediated with `wilful_defaulter_flag`/`fraud_flag` → Board-approval gate | Court/RBI route | LR-RBI-011 |
| S04 | `relief_sought` = stay/stop SARFAESI measure or DRT adjudication | `SIGNPOST` `FIN.SIG.EN` + offer `FIN.SET.SF` OTS mediation | Adjudicative outcome blocked (`FIN_SPECIAL_FORUM` → `CASE_NOT_ARBITRABLE`); copy "Equator cannot stop or stay enforcement" | DRT s.17: `s13_4_measure_date + 45 d`; redemption warning if auction notice published | LR-RBI-015 |
| S05 | Corporate borrower with CIRP admitted (`pending_forum ∋ NCLT_IBC`, stage admitted) | `REJECT` against corporate debtor (case `on_hold` if already filed) | All mechanisms vs CD (`IBC_MORATORIUM` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`); guarantor track continues unless s.94/95 filed | Claim with IRP/RP (date per public announcement, CM-entered) | LR-RBI-016 |
| S06 | PG with s.94/95 application filed (`pg_insolvency_filed_on` set) | `on_hold` from filing date for that guarantor | All mechanisms vs that PG | NCLT/DRT | LR-RBI-016 |
| S07 | `FIN.PAY.TX` AND (`bank_complaint_id` empty OR `days_since_txn` < channel TAT) | `SIGNPOST` (bank/PSO first) | Mediation blocked until bank process fails or both parties consent | Bank/PSO complaint; RB-IOS after 30 days; 1930 if unauthorised | LR-PAY-004 |
| S08 | `FIN.PAY.CB` consumer AND `chargeback_raised = false` | `ACCEPT_COND` | Mediation only after issuer outcome or on joint consent; arbitration ✖ consumer | Issuer chargeback; Consumer Commission (2 years) | LR-CONS-003 |
| S09 | Service-deficiency subtype (`FIN.CND.*`, `FIN.RET.DL`, charges) AND `grievance_ladder_status = not_raised` | `ACCEPT_COND` (ladder `fin.grv`) | RE grievance (F-FIN-04) generated first; mediation of money dispute in parallel with consent | RE reply due `complaint_date + 30 d`; RB-IOS by `re_reply_date + 90 d` or `complaint_date + 120 d`; IO where applicable | LR-RBI-001/004/010 |
| S10 | `FIN.CND.CR` AND remedy = correction only AND no CIC dispute raised | `ACCEPT_COND` | Generate CI + CIC dispute letters first (TPL-FIN-L03); mediation only on linked debt/settlement terms; arbitration ✖ | CIC + CI: `dispute_raised_date + 30 d`, then ₹100/day | LR-RBI-013 |
| S11 | `FIN.SET.NI` | `ACCEPT_COND` (civil money dispute only) | Arbitration of offence ✖ (`NN06_NON_ARBITRABLE` → `CASE_NOT_ARBITRABLE`); output = settlement + compounding pack for the court; "no threat of conviction" declaration mandatory | Court dates (CM-entered); statutory dates from C-FIN-11 | NN-24, LR-RBI-017/018 |
| S12 | Lender is bank or financial institution AND claim ≥ `rdb_threshold_minor` (₹20,00,000) | `ACCEPT_COND` | Arbitration ✖ (`FIN_DRT_EXCLUSIVE` → `CASE_NOT_ARBITRABLE`); negotiation/conciliation/mediation ✔; settlement recorded before DRT if OA pending | DRT; Lok Adalat | LR-ARB-020 |
| S13 | `FIN.RET.MF` | `ACCEPT_COND` (ladder `fin.mf`) | Shuttle-only default; blind-bid ✖; arbitration ✖ (policy flag); FOIR check (C-FIN-14); no group-liability transfer without each member's recorded consent | RB-IOS; police if coercion | LR-RBI-014 |
| S14 | Borrower is a consumer claiming deficiency AND requests arbitration | `ACCEPT_COND` | Arbitration only after consumer-forum disclosure + independent-advice prompt + borrower's post-dispute election (F-FIN-21); never forced | Consumer Commission tier; `cause_of_action + 2 years` | LR-CONS-001–003 |
| S15 | RB-IOS complaint pending or contemplated AND arbitration requested | `ACCEPT_COND` | Arbitration blocked until RB-IOS informed-choice acknowledgement (F-FIN-26) is e-signed (`FIN_RBIOS_ACK_REQUIRED` → `SIGNPOSTING_REQUIRED`) | RB-IOS non-maintainability notice | LR-RBI-003 |
| S16 | Limitation check: `limitation_estimate_date` (§4.5) < today | `ACCEPT_COND` | Arbitration/court-recording rungs flagged `LIMITATION_EXPIRED_STAGE_BLOCKED`; negotiation/conciliation still allowed (time-barred debt may be voluntarily paid; acknowledgment risk disclosed to both sides) | — | `limitation_contract` |
| S17 | `FIN.BUS.CL` with only one RE joined | `ACCEPT_COND` | Settlement signing blocked until partner RE joins (`FIN_COLENDING_PARTNER_MISSING` → `CLOSURE_BLOCKED`) | Each RE's GRO | LR-RBI-027 |
| S18 | `FIN.RET.DL` AND LSP named but RE not joined | `ACCEPT_COND` | Convening blocked until RE identified and joined (LSP may join as confirming party) | RE nodal GRO | LR-RBI-010 |
| S19 | `FIN.BUS.MS` AND `receivables_stuck > 0` | `ACCEPT` + suggestion | Separate COM MSEFC case suggested; merging claims ✖ | MSEFC / MSME ODR portal | COM pack |
| S20 | Matter already decreed / award passed / in execution | `ACCEPT_COND` | Settlement "around" the decree; output must be recorded before the executing court/Recovery Officer (satisfaction memo) | Executing forum | — |
| S21 | Any FIN matter with RE covered by RB-IOS | `ACCEPT` + mandatory disclosure | Closure blocked until RB-IOS signposting delivered (`SIGNPOSTING_REQUIRED`) | RB-IOS text block §4.7 | NN-20, LR-RBI-002 |
| S22 | Default (no terminal row matched) | `ACCEPT` | Ladder per §2.2 | Free forums listed per subtype | — |

### 4.2 Hard exclusions (non-configurable; Appendix K §3)

| Code | Exclusion | Action |
|---|---|---|
| HX-FIN-01 | Any criminal proceeding or offence as the subject (s.138 offence itself, cheating, forgery, extortion, criminal intimidation, unauthorised-transaction fraud) — NN-24 | Signpost; mediate civil money dimension only where law permits compounding (s.147) |
| HX-FIN-02 | Threats to life, physical violence, sexual harassment or stalking by recovery staff | Urgent signpost (§4.3); no joint session ever with the alleged actor |
| HX-FIN-03 | SARFAESI/DRT adjudication; s.17 challenges; stay of measures | Signpost DRT; OTS "around" only |
| HX-FIN-04 | Fraud / wilful-defaulter classification decisions; money-laundering matters | Signpost |
| HX-FIN-05 | Insolvency in rem (CIRP/PIRP admission, resolution plans) | Signpost NCLT/DRT |
| HX-FIN-06 | Illegal/unregistered lending apps' "debts"; usurious moneylending | Signpost 1930/police/Sachet/State authority |
| HX-FIN-07 | Deletion of accurate adverse credit history as a settlement term | Lint blocks term (`FIN_BUREAU_DELETION_TERM` → `SETTLEMENT_LINT_FAILED`) |
| HX-FIN-08 | Card-network issuer–acquirer arbitration (network rules) | Out of scope |
| HX-FIN-09 | Reversal of a payment by Equator / instruction to a bank or NPCI | Never offered; copy lint |

### 4.3 Urgent and safety triggers

| Trigger | Detection | Immediate action (≤ 60 seconds, deterministic) | Clock |
|---|---|---|---|
| `safety_risk_now = true` (Explorer FQ-002 or form) | Answer, or `intake_assistant` classification `danger_signal` ≥ threshold confirmed by user | Show 112 / 1930 / women helpline 181 `[K]` panel; suppress all outbound contact to the borrower from the lender side for the case (`CONTACT_BLACKOUT_ACTIVE`); task to `safeguarding_lead` (P1, 2 working hours) | `fin_safety_review` 2 working hours |
| Morphed images / threat to publish / contacting contacts | `harassment_types[]` | As above + evidence-preservation guidance (export chats; BSA s.63 certificate later); no deletion advice | same |
| Auction notice published (`FIN.SET.SF`) | `sarfaesi_stage = auction_notice_published` | Red banner: redemption right may be lost on publication (*Celir*); CM call within 1 working day | `sarfaesi_redemption_warning` |
| Gold auction scheduled within 7 days | `auction_date - today ≤ 7` | Banner + CM task; lender notified of mediation request (no stay claim) | `gold_auction_alert` |
| s.138 complaint limitation within 7 days (complainant side) | C-FIN-11 | Banner "file or settle before [date]"; Equator does not file | `ni138_complaint` |
| RB-IOS 90-day window ≤ 15 days left | C-FIN-13 | Banner + SMS/WhatsApp within window (NN-12) | `rbi_ios_filing` |
| Bereavement / medical emergency / marriage declared | `vulnerability_flags[]` | Blackout calendar entry (default 15 days, editable by borrower) | `fin_blackout` |

### 4.4 Vulnerability protocol (C2 FL-3; PI-FIN-13)

Flags (DD-FIN-060) never shown to the other side. Effects: `senior_citizen`, `disability`, `illness`, `first_time_digital_user`, `language_need` → assisted channel, interpreter at ₹0 (ANC.INTERP), extra 7 days on response window once; `MFI_household`, `coercion_reported` → shuttle-only, no blind-bid, no same-day signature (minimum 24 h between final terms and e-sign — `fin.cooling_before_sign_hours` default 24), independent-advice prompt; `job_loss`, `bereavement`, `illness` → fee waiver CN-HARD (Appendix B §B.9) on FIN-R; all → neutral briefed "vulnerability present" without detail.

### 4.5 Jurisdiction and limitation checks

| Check | Rule | Output |
|---|---|---|
| Territorial (mediation/conciliation) | Online by default; venue = borrower's district for in-person | `venue_district` |
| Seat (arbitration) | Consumer-borrower: borrower's district or online with borrower's district as venue; distant seat needs recorded justification (LR-ARB-030) | `seat`, `seat_justification` |
| s.138 court | Payee's bank branch (s.142(2)) — informational only | `ni_court_district` |
| DRT jurisdiction | Bank/FI ≥ ₹20 lakh → DRT where branch/defendant/cause `[K]` | signpost row |
| Consumer tier | District ≤ ₹50 lakh; State > ₹50 lakh–₹2 crore; National > ₹2 crore (consideration paid) | signpost row |
| Limitation estimate | `limitation_estimate_date = max(default_date, last_acknowledgment_date, last_part_payment_date) + 3 years` (informational; CM-verified; never shown as legal advice) | `limitation_contract` clock (AP-L) |

### 4.6 Arbitration eligibility and appointment defensibility (NN-03)

| # | Gate | Pass condition | Fail → | Rule |
|---|---|---|---|---|
| A1 | Arbitrable subject | Not S04/S05/S11/S12 rows; not `FIN.CND.CR`, `FIN.CND.RC`, `FIN.PAY.TX`, `FIN.RET.MF` (policy) | `CASE_NOT_ARBITRABLE` | LR-ARB-019/020 |
| A2 | Basis of consent | (a) accepted ex-ante clause instance naming Equator (P09 FR-P09-08) with `clause_version_id`, `document_sha256`, `signed_at` < `dispute_arose_on`; or (b) F-FIN-21 post-dispute submission agreement e-signed by **every** party after `dispute_arose_on`; or (c) uploaded s.11 order | `FIN_ARB_CLAUSE_NOT_ORIGINATION` → `CASE_NOT_ARBITRABLE` (422 per Appendix F §F.10.1; the 409 in FR-P08-23 is superseded, X-20) | LR-ARB-003/004, LR-ARB-027 |
| A3 | Post-default conferral | A clause or letter conferring appointment on Equator after default (lender-only trigger) is never a basis | `APPOINTMENT_LENDER_TRIGGER_BLOCKED` | *Radiance Galore* (2025); *Madhyachal Steels* (2026) |
| A4 | Unilateral-appointment clause | Clause letting the lender appoint/nominate → appointment part void; Equator allocates from panel only if A2 satisfied | flag `unilateral_clause_detected`; IEP note | *Perkins Eastman* (2020) 20 SCC 760; *TRF* (2017) 8 SCC 377; *CORE* (2024 INSC 857) |
| A5 | Allocation | Rule-based rotation from FIN panel; lender has no UI/API/data path to choose, rank, strike or veto; one reasoned objection like any party; concentration cap 2 per lender group per neutral per 36 months for non-bulk matters (LR-ARB-007); bulk programmes use the relative cap (default 40% per counterparty per 24 months), confirmed by the legal reviewer before FIN bulk go-live (X-27) | `NEUTRAL_SELECTION_FORBIDDEN`, `CONCENTRATION_CAP_EXCEEDED` | LR-ARB-001, LR-ARB-007 |
| A6 | Disclosure | Sixth Schedule disclosure + FIN questions (F-FIN-06: engagement with lender, LSP, collection agency in 5 years; appointments by lender group in 36 months) | `DISCLOSURE_REQUIRED` | LR-ARB-005/006 |
| A7 | s.12(5) | Waiver only as separate e-signed instrument per party after dispute (F-FIN-21 Part B) | `S12_5_WAIVER_PREDATES_DISPUTE` | LR-ARB-002; *Bhadra International* (SC, 5 Jan 2026) |
| A8 | Consumer/RB-IOS disclosures | S14/S15 acknowledgements on file | `SIGNPOSTING_REQUIRED` | LR-RBI-003, LR-CONS-003 |
| A9 | Seat fairness | LR-ARB-030 | warning + registrar review | LR-ARB-030 |
| A10 | Defensibility Score | P03 FR-P03-30: Green ≥ 85 proceeds; Amber 70–84 registrar review; Red < 70 Appointments Committee | hold | P03 |

### 4.7 RB-IOS 2026 signposting block (NN-20; mandatory text, versioned template `TPL-FIN-SIG-RBIOS@2`)

Delivered when the RE is RB-IOS-covered (LR-RBI-002 tenancy attribute `rbios_covered`; for a non-tenant RE, from `re_type`: covered = banks, RRBs, StCBs/DCCBs, specified UCBs, NBFCs that are deposit-taking or customer-interface with assets ≥ ₹100 crore (excluding HFCs, core investment companies, PDs), non-bank PPI issuers, credit information companies (CICs)). Plain-English text (Hindi parity required):

> "You can complain to [RE name] first. If they do not reply in 30 days, or you are not happy with the reply, you can complain free of charge to the RBI Ombudsman at cms.rbi.org.in (or call 14448) within 90 days. Your last date is **[computed date]**. The Ombudsman can award up to ₹30 lakh for loss and up to ₹3 lakh for harassment and expenses. If your matter is before a court or an arbitrator, the Ombudsman may not take it. Equator is a private dispute resolution institution, not the RBI Ombudsman."

Computation: `rbios_last_date = re_final_reply_date + 90 d` if the RE replied; else `re_complaint_date + 30 d + 90 d`; if `re_complaint_date` unknown → "File a complaint with [RE] first; we can prepare the letter (free)". Complaints received by the RE before 1 Jul 2026 → RB-IOS 2021 text (1 year) shown instead (parameter `rbios_2021_cutoff = 2026-07-01`). Delivery writes `core.signposting_events` (forum `RBIOS`, `last_date_to_act`, `script_version`).

---

## 5. Dispute Explorer question tree (FIN)

Appendix K node format; no login; stores nothing until the user saves (P02 Explorer v1 rule). Text is plain English at or below class-8 reading level (Flesch-Kincaid grade ≤ 8 CI check on `en`; Hindi reviewed by a human — NN-23). The `intake_assistant` may map free text to an option with confidence ≥ 0.85, else it asks the question verbatim (NN-01/NN-02). Outcomes: `OC-FIN-*` codes map to §4 rows.

### 5.1 Entry and precedence (all FIN users)

| ID | Question (en) | Options | Branch / effect |
|---|---|---|---|
| FQ-001 | Is this about a loan, a credit card, a cheque, or a payment that went wrong? | Loan · Credit card · Cheque bounced · Payment/UPI went wrong · Credit report is wrong · Someone collecting a loan is troubling me · Something else about a bank or lender | → FQ-002 (all); then: Loan/Card → FQ-RET-01; Cheque → FQ-SET-NI-01; Payment → FQ-PAY-01; Credit report → FQ-CND-CR-01; Troubling → FQ-CND-RC-01; Else → FQ-003 |
| FQ-002 | Are you or your family in danger right now, or has anyone threatened to hurt you? | Yes · No · I am not sure | Yes → `OC-FIN-URGENT-SAFETY` (S01): show 112/1930/181 panel; stop tree unless user chooses "I am safe now, continue". Not sure → show panel + continue |
| FQ-003 | Who are you in this matter? | I took the loan / card · I am a co-borrower · I am a guarantor · I am a family member of a borrower who died · I am the lender or its staff · I gave money to someone · I am a merchant · I am a business partner of a lender | Sets `initiator_role` (DD-FIN-001) |
| FQ-004 | Who is the lender or company? | Search box (RE directory: name, type, licence/CoR) · "It is an app" · "A person, not a company" · "I don't know" | App → FQ-RET-DL-01; Person → `FIN.RET.PP`; Don't know → FQ-004a |
| FQ-004a | Can you upload a screenshot of the loan app, SMS or agreement? We will try to find the lender's name. | Upload · Skip | If RE not found after lookup → S02 `OC-FIN-SIGNPOST-ILLEGAL-APP` |
| FQ-005 | Is any case already going on about this? (Pick all) | No case · Court case · Cheque case in court · DRT · Bank sent a SARFAESI notice · NCLT/insolvency · Consumer Commission · Police complaint · RBI Ombudsman complaint · Arbitration · Lok Adalat · I don't know | Drives S04/S05/S06/S11/S12/S15; creates draft F-FIN-22 rows |
| FQ-006 | Have you already complained to the lender in writing? | Yes, they replied · Yes, no reply yet · No | Yes → ask dates (FQ-006a); sets `grievance_ladder_status`; computes RB-IOS dates |
| FQ-006a | When did you complain, and when did they reply? | Date · Date / no reply | → C-FIN-13 |
| FQ-007 | Roughly how much money is involved? | Under ₹50,000 · ₹50,000–₹5 lakh · ₹5–20 lakh · ₹20 lakh–₹1 crore · Above ₹1 crore · Not about money | Sets value band VB1–VB5 |
| FQ-008 | What do you want to happen? (Pick all) | Settle for a lower amount (OTS) · Smaller EMIs / more time · Remove wrong charges · Stop harassment · Correct my credit report · Get my documents / gold / vehicle back · Get the extra money after auction · Get my payment back · Close the cheque case · Something else | `relief_sought[]` (DD-FIN-050) |

**Primary-subtype precedence** (deterministic): S01 safety → `FIN.SIG.CR` · S02 → `FIN.SIG.IL` · cheque → `FIN.SET.NI` · SARFAESI notice → `FIN.SET.SF` · DRT pending → `FIN.SET.DR` · conduct complaint → `FIN.CND.RC` · credit report only → `FIN.CND.CR` · payment → `FIN.PAY.*` · co-lending disclosed → `FIN.BUS.CL` · guarantor initiator → `FIN.BUS.GT` · charges only → `FIN.CND.CH` · OTS with no other issue and an active lender programme → `FIN.SET.OT` · else product subtype from FQ-RET-01.

### 5.2 FIN.RET and FIN.BUS (loans and cards)

| ID | Question | Options | Branch / outcome |
|---|---|---|---|
| FQ-RET-01 | What kind of loan is it? | Personal loan · Credit card · App loan / Buy now pay later · Gold loan · Vehicle loan · Home loan / loan against property · Education loan · Group / microfinance loan · Business / MSME loan · Loan from a person or P2P app | Sets `loan_product` and product L2 |
| FQ-RET-02 | Is the loan paid on time now? | Yes · 1–30 days late · 31–60 days late · 61–90 days late · More than 90 days late · Loan closed · Loan settled earlier · I don't know | `dpd_bucket` |
| FQ-RET-03 | Did you get a Key Facts Statement (KFS) when you took the loan? | Yes · No · I don't know | No → `kfs_received = n`; charges-not-in-KFS check |
| FQ-RET-04 | Is something given as security? | No security · Gold · Vehicle · House or land · Fixed deposit · Someone signed as guarantor · I don't know | `secured` |
| FQ-RET-05 | (Gold) Did you repay fully but not get your gold back? | Yes · No · Gold was auctioned · Gold was returned damaged or less | Yes → C-FIN-06 preview; auctioned → FQ-RET-05a |
| FQ-RET-05a | Did you get a notice before the auction? | Yes · No · Not sure | → surplus calculator C-FIN-07; `auction_notice_received` |
| FQ-RET-06 | (Vehicle) Was your vehicle taken away? | No · Yes, with a notice first · Yes, without notice · Yes, by force | By force → S01 check; else `repossessed` |
| FQ-RET-07 | (Home/LAP) Did the bank send a notice saying it will take the property? | No · Yes (13(2) notice) · Yes, they took possession · Yes, auction notice published | → `FIN.SET.SF` + timer C-FIN-12 |
| FQ-RET-08 | (Microfinance) How much does your whole family earn in a year? | Up to ₹3 lakh · More than ₹3 lakh · I don't know | → FQ-RET-08a |
| FQ-RET-08a | How much do you pay every month for all loans together? | Amount (₹) | C-FIN-14 FOIR; breach → affordability note (no advice) |
| FQ-RET-09 | (Education) Did you get the interest subsidy you applied for? | Yes · No · Not applied · I don't know | No → subsidy-correction letter; Vidya Lakshmi portal link |
| FQ-RET-10 | (Business) Do you also have money stuck with your buyers? | Yes · No | Yes → separate COM MSEFC suggestion (S19) |
| FQ-RET-11 | (Co-lending) Does your loan paper name two lenders? | Yes · No · I don't know | Yes → `FIN.BUS.CL`; both REs joined |
| FQ-RET-12 | Does your loan agreement say disputes go to arbitration? | Yes, it names Equator Resolution · Yes, it names someone else · Yes, the lender picks the arbitrator · No · I don't know | Drives §4.6 A2/A4 (never a borrower obligation to answer correctly; CM verifies) |
| FQ-RET-13 | Are you able to pay something now or every month? | Lump sum (amount, by date) · Monthly amount · Not now · I don't want to say | Feeds negotiation request (not shown to lender unless the user chooses) |

### 5.3 FIN.CND (conduct, charges, credit report)

| ID | Question | Options | Branch / outcome |
|---|---|---|---|
| FQ-CND-RC-01 | What happened? (Pick all) | Calls before 8 am or after 7 pm · Calls during a death, illness or wedding in the family · Rude or abusive words · Threats · They called my family, friends or office · They shamed me in public or online · Agent came without ID card or letter · Phone was locked · Calls from unknown numbers | `conduct_type[]` (DD-FIN-080); Threats → FQ-002 re-ask |
| FQ-CND-RC-02 | When did it happen? | Date(s) | `incident_date` < 2027-01-01 → legacy standard banner |
| FQ-CND-RC-03 | Do you have proof? | Call log screenshot · Recording · Messages · Witness · None | Evidence checklist §9 |
| FQ-CND-RC-04 | Do you also want to settle the loan itself? | Yes · No · Later | Yes → secondary product L2 |
| FQ-CND-CH-01 | Which charges look wrong? | Late / penal charges · Bounce charges · Processing fee · Foreclosure / pre-payment charge · Insurance added without asking · GST on charges · Legal or collection charges · Interest rate changed | `charges_disputed[]`; pre-payment → C-FIN-15 |
| FQ-CND-CR-01 | What is wrong in your credit report? | Loan is not mine · Days-late shown wrongly · Shows "settled" but I paid fully · Closed loan shown open · Wrong amount · Same loan twice · I was a guarantor, shown as borrower · My details mixed with someone else | `error_type` |
| FQ-CND-CR-02 | Have you raised a dispute with the credit bureau? | Yes (ID and date) · No | No → S10 letters; Yes → C-FIN-09 |

### 5.4 FIN.PAY (payments)

| ID | Question | Options | Branch / outcome |
|---|---|---|---|
| FQ-PAY-01 | How did you pay? | UPI · IMPS · NEFT/RTGS · Debit/credit card · Wallet · Aadhaar (AePS) · Auto-debit (NACH) | `rail` |
| FQ-PAY-02 | What went wrong? | Money left my account but did not reach · Payment failed, money not returned · Shop did not deliver · Refund not received · Sent to wrong person · I did not make this payment · Charged twice | `issue`; "I did not make this payment" → S07 + 1930 + customer-liability note (report within 3 working days `[K]`) |
| FQ-PAY-03 | Did you complain to your bank or app? | Yes (complaint ID) · No | No → S07 `OC-FIN-SIGNPOST-BANK-FIRST` |
| FQ-PAY-04 | When was the payment? | Date/time | C-FIN-17 TAT check |
| FQ-PAY-05 | Is the other side a shop or company that agrees to talk? | Yes · No · Don't know | Yes → mediation offer (S08) |

### 5.5 FIN.SET (cheque, SARFAESI, DRT, OTS)

| ID | Question | Options | Branch / outcome |
|---|---|---|---|
| FQ-SET-NI-01 | Did you give the cheque or receive it? | I gave it · I received it | Sets drawer/payee |
| FQ-SET-NI-02 | What stage is it at? | Cheque bounced, no notice yet · Notice sent · Case filed in court · Summons received · Evidence going on · Defence evidence done · Judgment given, appeal going on · In High Court / Supreme Court | `stage` → C-FIN-11 dates and P08 `fin.ni138_cost@1` slab |
| FQ-SET-NI-03 | Is the money owed agreed by both sides? | Yes · Partly · No | No → mediation note: "Equator can help you talk about the money. Only the court decides the cheque case." |
| FQ-SET-SF-01 | What has the bank done so far? | Sent 13(2) notice (date) · I sent objection · Bank replied · Took symbolic possession · Took physical possession · Auction notice published (date) · Sale done | `sarfaesi_stage` → C-FIN-12; auction → urgent banner |
| FQ-SET-DR-01 | Is there a case in the DRT? | Yes (OA number, next date) · No · Don't know | Yes → `FIN.SET.DR` |
| FQ-SET-OT-01 | Has the lender sent you a settlement offer link? | Yes · No | Yes → OTS portal (§6.8, §7.5) |

### 5.6 Outcome screens and free-forum disclosures

| Outcome code | Screen content (summary) | Free/statutory routes shown first |
|---|---|---|
| `OC-FIN-ACCEPT` | Route offered (ladder), Equator fee (FIN-R quote or "₹0 to you — paid by [lender] under a disclosed programme"), clocks, documents list, "Save and continue" | RB-IOS block (§4.7) where covered; Lok Adalat |
| `OC-FIN-ACCEPT-COND` | Conditions listed (e.g., "Complain to the lender first — we will prepare the letter free") | As per row |
| `OC-FIN-SIGNPOST-*` | Forum name, what it can do, cost (free/fee), how to apply, last date, our letter/pack (free) | Named forum |
| `OC-FIN-URGENT-SAFETY` | 112, 1930, 181; "You do not have to talk to anyone who threatens you" | Police |
| `OC-FIN-REJECT-*` | Why Equator cannot help; where to go | Named forum |

Mandatory disclosure on every FIN outcome screen: "Equator is a private, neutral dispute resolution institution. We are not a court, the RBI, the RBI Ombudsman, or a recovery agent. We do not give legal advice. Using Equator is voluntary."

---

## 6. Intake and submission forms per mechanism

Form IDs continue P08 FR-P08-17 (F-FIN-01 to F-FIN-23); new forms F-FIN-24 to F-FIN-31. Schema IDs `eqr.form.fin.<name>.v2`. Form resolution (Appendix K §4): `vertical × L2 × mechanism × initiator_role` → schema; the common core (§6.1) is embedded in every request form; subtype blocks (§6.6) attach by `visibleWhen: primary_l2 ∈ … OR secondary_subtypes ∋ …`. Types: `text`, `textarea`, `enum`, `multi`, `date`, `datetime`, `money` (minor units, INR), `pct`, `int`, `bool`, `file[]`, `lookup`, `esign`. `R` = required, `C` = conditional (`requiredWhen` stated), `O` = optional.

### 6.1 Common FIN core block (`eqr.form.fin.core.v2`)

| field_id | Label | Type | Req | Options / dropdown | Validation | Help text |
|---|---|---|---|---|---|---|
| `initiator_role` | Your role | enum | R | DD-FIN-001 | — | "Choose how you are connected to the loan or payment." |
| `re_type` | Type of lender/company | enum | R | DD-FIN-002 | `unregulated_lender`/`private_moneylender` + app → S02 | — |
| `re_lookup` | Lender name | lookup | R | RE directory (RBI-registered entity list snapshot, versioned) | must resolve or `re_name_free` | "Search by name; pick the exact company." |
| `re_name_free` | Lender name (if not found) | text | C (`re_lookup` empty) | — | 3–200 chars | — |
| `re_registration_no` | Licence / CoR number | text | O | — | pattern per `re_type` | "Printed on the loan agreement or website footer." |
| `lsp_name` / `dla_name` | App or agent company name | text | C (`loan_product = app_bnpl`) | — | — | — |
| `account_ref` | Loan / card / transaction reference | text | R | — | stored HMAC + last 4 (`fin.loan_accounts.loan_account_hmac`); 16-digit card numbers rejected by a Luhn-pattern guard (NN-31; sub-code `FIN_CARD_PAN_ENTERED` → `VALIDATION_FAILED`) | "Only the last 4 digits are shown to others. Never type your full card number or CVV." |
| `loan_product` | Product | enum | R | DD-FIN-010 | — | — |
| `sanction_date` | Loan sanction date | date | C (loans) | — | ≤ today | Drives legacy-rule flags (gold 1 Apr 2026; pre-payment 1 Jan 2026) |
| `principal_minor` / `outstanding_claimed_minor` / `outstanding_admitted_minor` | Loan amount / amount lender says is due / amount you agree is due | money | C (loans) | — | ≥ 0; admitted ≤ claimed (warning only) | "The difference is what you will discuss." |
| `dpd_bucket` | Repayment status | enum | C (loans) | DD-FIN-011 | — | — |
| `secured` | Security | enum | R | DD-FIN-012 | — | — |
| `grievance_ladder_status` | Complaint to lender so far | enum | R | DD-FIN-013 | dates required when ≠ `not_raised` | — |
| `re_complaint_date` / `re_reply_date` / `re_complaint_ref` | Date complained / date of reply / complaint number | date/date/text | C | — | reply ≥ complaint | — |
| `pending_forum[]` | Other cases | multi | R | DD-FIN-014 | each creates F-FIN-22 row | — |
| `arbitration_clause_in_loan` | Arbitration clause | enum | R | DD-FIN-015 | — | "If unsure, choose 'I don't know'. Our case manager checks." |
| `relief_sought[]` | What you want | multi | R | DD-FIN-050 | ≥ 1 | — |
| `vulnerability_flags[]` | Anything we should know to help you take part | multi | O | DD-FIN-060 | never shown to other side | "Private. Helps us give you more time or support." |
| `contact_preference` | Best time and way to contact you | enum + time range | R | DD-FIN-090 | window ⊆ 08:00–19:00 unless `borrower_requested_outside_window = true` (logged) | — |
| `language` | Language | enum | R | Master NN-23 list | — | — |
| `consent_s17_notice_ack` | I understand how my data is used | bool | R | — | true | Itemised DPDP notice (NN-15) |
| `truth_declaration` | The information is true to my knowledge | bool | R | — | true | — |

### 6.2 Negotiation request (`F-FIN-24`, `eqr.form.fin.negotiation_request.v2`; ladder rung 1)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| core block | — | — | R | §6.1 | — | — |
| `proposal_kind` | Type of proposal | enum | R | DD-FIN-051 | — | — |
| `lump_sum_minor` / `lump_sum_by` | Lump sum / pay by | money/date | C (`lump_sum`) | — | date ≤ today + 180 d | — |
| `instalments_n` / `instalment_minor` / `first_due` | Number / amount / first date | int/money/date | C (`instalments`) | — | n ≤ 60; n > 3 months span → restructuring flag (C-FIN-16) | — |
| `waivers_requested[]` | Waivers asked | multi | O | DD-FIN-052 | — | — |
| `non_money_terms[]` | Other terms | multi | O | DD-FIN-053 | — | — |
| `blind_bid_opt_in` | Use a sealed-bid round | bool | O | — | false if MF or any vulnerability flag | "Both sides enter numbers privately; we show only whether they overlap." |
| `share_affordability_summary` | Share a summary of my ability to pay | bool | O | — | links F-FIN-23 derived summary only | — |
| `offer_validity_days` | Offer open for | int | R | 14–60 | ≥ 14 (S4 PL-08) | — |
| `without_prejudice` | Without prejudice | bool | R (fixed true) | — | — | — |

Lender-initiated variant adds: `re_policy_ref` (R), `approver_role` (R), `authority_limit_minor` (R; `OFFER_ABOVE_AUTHORITY`), `wilful_defaulter_flag` / `fraud_flag` (R; true → Board-approval evidence upload R), `bureau_reporting_on_settlement` (R, DD-FIN-054), `cooling_period_months` (R, ≥ 12), `payment_rail` (R, DD-FIN-055 — Equator merchant never an option).

### 6.3 Mediation / conciliation request (`F-FIN-02` v2 mechanism block; rungs 2–3)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| core block + subtype blocks | — | — | R | §6.1, §6.6 | — | — |
| `mechanism_choice` | Process | enum | R | `conciliation_part_iii` · `mediation_contractual` · `let_equator_recommend` | recommend → PL-02 rule: conciliation where respondent is an RE/company and an enforceable outcome is wanted | "Conciliation under Part III can give a settlement with the status of an arbitral award (s.74)." |
| `dispute_summary` | What the dispute is about | textarea | R | — | 50–3,000 chars; AI Pleadings Studio optional (NN-25) | — |
| `chronology[]` | Key dates | table (date, event, document) | O | — | — | — |
| `mode` | Online or in person | enum | R | DD-FIN-091 | — | — |
| `respondents[]` | Other side(s) | table (org/person lookup, role DD-FIN-003, contact points) | R | — | RE mandatory for DL/CL (S17/S18) | — |
| `guarantors_join` | Join guarantors / co-borrowers | bool + list | C (any guarantor exists) | — | PI-FIN-14 | — |
| `interpreter_language` | Interpreter | enum | O | NN-23 list | — | ₹0 for individuals |
| `rbios_status_ack` | I have seen the free RBI Ombudsman route | bool | C (RB-IOS covered) | — | true | §4.7 |
| `standstill_request` | Ask the other side to sign a standstill (limitation) agreement | bool | O | — | flag `fin.standstill_template` OFF until counsel sign-off (S4 Q-C1) | "This invitation does not stop limitation running." |
| `fee_quote_ack` | I accept the fee shown | bool | R | — | quote ID valid (`QUOTE_EXPIRED`) | GST-inclusive for consumers (NN-29) |

### 6.4 Arbitration request / statement of claim (`F-FIN-13` v2 + s.21 notice `TPL-FIN-N03`)

Available only after §4.6 gates A1–A9 pass.

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| `arbitration_basis` | Basis | enum | R | `ex_ante_clause_instance` · `post_dispute_submission_f_fin_21` · `s11_order` | evidence object R per value | — |
| `clause_instance_id` | Clause instance | lookup | C (ex_ante) | P09 registry | state `accepted`; `signed_at` < `dispute_arose_on` | — |
| `dispute_arose_on` | Date dispute arose | date | R | — | ≤ today; ≥ sanction_date | Used for waiver validity |
| `s21_notice_served_on` | Notice invoking arbitration received by respondent | date | R (system) | — | from notice evidence | Starts arbitration (s.21) |
| `claim_heads[]` | Claim heads | table | R | head DD-FIN-056; amount_minor; basis document | principal, contractual interest, penal charges, costs separate (LR-RBI-012); penal never capitalised (`FIN_PENAL_CAPITALISED`) | — |
| `interest_basis` | Interest claimed | enum + rate | R | `contract_rate` · `s31_7_rate` · `none` | rate ≤ contract rate (warning) | — |
| `soa_document_id` | Statement of account | file | R | — | PDF; lender-certified | — |
| `procedure` | Procedure | enum | R | `documents_only_fast_track_s29b` (requires written agreement; claim ≤ `fin.fast_track_max_minor` ₹5,00,000 default) · `standard` | — | — |
| `seat` / `venue` | Seat / venue | enum | R | default borrower district (LR-ARB-030) | distant seat → `seat_justification` R | — |
| `costs_claimed_s31a` | Costs | money | O | — | never includes Equator fees as a loan charge (LR-RBI-025) | — |
| `ai_draft_used` | AI Pleadings Studio used | bool | R | — | source anchors per NN-25 | — |
| `soc_esign` | Sign | esign | R | Aadhaar eSign / DSC | — | — |

### 6.5 Response / statement of defence / counterclaim (`F-FIN-05` v2)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| `position` | Your response | enum | R | DD-FIN-057 | — | — |
| `amount_admitted_minor` | Amount you agree is due | money | C | — | — | — |
| `soa_document_id` | Statement of account (lender respondent) | file | C (respondent is RE) | — | R for lender | P08 FR-P08-17 |
| `counter_offer` | Counter-proposal | embedded F-FIN-24 | O | — | validity ≥ 14 d | — |
| `forum_objection` | Object to this forum | enum + text | O | `pending_elsewhere` · `not_arbitrable` · `no_agreement` · `other` | — | — |
| `counterclaim_heads[]` | Counterclaim (arbitration only) | table | O | DD-FIN-056 (borrower heads: excess charges, compensation under RBI frameworks, document-release compensation) | — | — |
| `authority_evidence` | Authority to settle (organisations) | file + `authority_limit_minor` | C (respondent org) | — | required before signing (Rules Art.8) | — |
| `grievance_officer_details` | Your GRO name, email, phone, address (RE respondents) | composite | C (RE) | — | mandatory for NN-12 footer (`GRO_DETAILS_MISSING`) | — |
| `response_esign` | Sign | esign/OTP | R | — | — | — |

Response window: 14 calendar days from deemed service (FR-P08-15; +7 days once for vulnerability flags).

### 6.6 Subtype extension blocks (attach to §6.2–§6.5)

| Block | Fields (`field_id`: type, options; R/C/O) |
|---|---|
| `blk.pl` | `loan_subproduct`: enum DD-FIN-016 R · `interest_type`: enum fixed/floating R · `kfs_received`: enum y/n/unknown R · `charges_disputed[]`: multi DD-FIN-070 O · `hardship_reason`: enum DD-FIN-061 O · `affordable_monthly_minor`: money O · `lump_sum_available_minor` + `by_date` O |
| `blk.cc` | `network`: enum Visa/Mastercard/RuPay/Amex/Diners R · `dispute_kind`: enum DD-FIN-017 R · `chargeback_raised` + `chargeback_ref` + `chargeback_outcome` C · `closure_requested_on`: date C (closure_delay) · `last_payment_date` O · `revolving_since` O |
| `blk.dl` | `dla_name` R · `dla_package_id`: text pattern `^[a-z][a-z0-9_.]+$` O · `re_disclosed_in_app`: bool R · `bnpl_type`: enum pay_later_line/card_on_app/checkout_emi C · `kfs_apr_shown_pct`: pct O · `cooling_off_exercised` + date O · `unauthorised_disbursal`: bool O · `harassment_types[]`: multi DD-FIN-081 O · `police_complaint_no` O · `data_deletion_requested`: bool O |
| `blk.gl` | `pledge_date` R · `gross_weight_g`, `net_weight_g`: decimal(3) R · `purity_carat`: enum 18/20/22/24/other R · `ltv_at_sanction_pct` O · `repayment_type`: enum bullet/emi R · `full_repayment_date` C · `release_date_actual` C · `auction_notice_received`: enum y/n + date + mode C · `auction_date`, `reserve_price_minor`, `sale_price_minor`, `surplus_claimed_minor` C · `ornament_damage_desc` + photos C |
| `blk.vl` | `vehicle_type`: enum DD-FIN-018 R · `registration_no`: text pattern Indian RC O · `repossessed`: bool R · `repossessed_on`, `agency_name` C · `pre_repossession_notice`: bool + date C · `inventory_received`: bool C · `sale_notice_received`: bool C · `sale_price_minor`, `shortfall_demanded_minor` C · `noc_form35_requested_on` C · `insurance_claim_case_id` (INS link) O |
| `blk.hl` | `property_state` R (stamp/registration) · `loan_purpose`: enum DD-FIN-019 R · `benchmark`: enum EBLR/MCLR/PLR/fixed R · `rate_reset_dispute`: bool O · `tenor_extended_without_consent`: bool O · `documents_deposited[]`: multi DD-FIN-020a O · `foreclosure_requested_on` O · `sarfaesi_stage`: enum DD-FIN-030 R |
| `blk.el` | `course`, `institution`, `country` R · `moratorium_end_date` R · `subsidy_scheme`: enum CSIS/PM_Vidyalaxmi/state/none R · `subsidy_credited`: enum y/n/unknown R · `employment_status`: enum DD-FIN-062 R · `co_borrower` (person) C |
| `blk.mf` | `household_income_annual_minor` R · `household_members`: int R · `loans_outstanding[]`: table (lender, EMI) R · `foir_computed_pct`: system · `jlg_shg_group` (name, size) O · `group_pressure_reported`: bool R · `collection_location`: enum centre_meeting/home/workplace O · `private_contact_only`: bool O ("Contact only me, not my family") |
| `blk.pp` | `p2p_platform` C · `lender_count`: int C · `private_loan_written`: bool R · `interest_rate_pa`: pct O (flag above State cap table **[VERIFY — open: State Money-lenders Act cap table (Q-15)]**) · `transfer_proofs[]` R |
| `blk.ms` | `udyam_no`: pattern `^UDYAM-[A-Z]{2}-\d{2}-\d{7}$` O · `msme_category`: enum micro/small/medium O · `facility_type[]`: multi term/cc_od/invoice_discounting/equipment R · `cgtmse_covered`: enum y/n/unknown O · `guarantors[]`: table (name, relation, PG amount) O · `sma_status`: enum SMA-0/SMA-1/SMA-2/NPA O · `receivables_stuck_minor` O · `cin`/`gstin` O (MCA/GST prefill) |
| `blk.cl` | `colending_model`: enum bank_nbfc/nbfc_nbfc/other R · `originating_re`, `partner_re`: lookup R · `share_split_pct` O · `spoc_named_in_agreement` O |
| `blk.cb` (B2B) | `colending_model` R · `dlg_pct`: pct ≤ 5 warning O · `dispute_head[]`: multi DD-FIN-031 R · `portfolio_size_minor`, `loans_in_dispute_count` R · `loan_level_file`: file CSV (template TPL-FIN-B01) C · `master_agreement_document_id` R |
| `blk.gt` | `guarantee_type`: enum personal/corporate/co_obligor R · `guarantee_cap_minor` or `unlimited` R · `invoked` + `invoked_on` R · `variations_without_consent`: bool + description O · `principal_debtor_status`: enum DD-FIN-032 R · `co_guarantors[]` O · `pg_insolvency_filed_on` C |
| `blk.rc` | `conduct_type[]` R (DD-FIN-080) · `incident_dates[]` R · `agency_name` O · `caller_numbers[]`: E.164 O · `visit_details` O · `evidence_upload[]` O · `police_complaint` + number C · `safety_risk_now`: bool R |
| `blk.ch` | `issue_kind`: enum wrong_charges/mis_selling R · `charges_disputed[]` R · `amount_disputed_minor` R · `bundled_product` (policy no. masked) C · `kfs_lists_charge`: enum y/n/unknown R |
| `blk.cr` | `cic[]`: multi CIBIL/Experian/Equifax/CRIF_HighMark R · `cic_dispute_id` C · `dispute_raised_date` C · `error_type`: enum DD-FIN-033 R · `report_upload`: file R (party-supplied; report control number checked) |
| `blk.pay` | `rail`: enum DD-FIN-034 R · `txn_id` (RRN/UTR): text R · `txn_datetime` R · `amount_minor` R · `issue`: enum DD-FIN-035 R · `bank_complaint_id` C · `udir_raised`: bool O · `merchant_order_id` C · `days_since_txn`: system |
| `blk.ot` | `offer_mode`: enum DD-FIN-051 R · `source_of_funds`: enum DD-FIN-063 O · `security_to_be_released[]` O · `wilful_defaulter_flag`, `fraud_flag` (lender) R |
| `blk.ni` | `cheque_no`, `cheque_date`, `cheque_amount_minor`, `drawee_bank` R · `dishonour_date`, `return_memo_received_on` R · `return_reason`: enum DD-FIN-036 R · `notice_sent_on`, `notice_received_on` C · `complaint_filed`: bool + `court`, `cc_no`, `cnr` C · `stage`: enum DD-FIN-037 R · `underlying_debt_admitted`: enum yes/partly/no R |
| `blk.sf` | `sarfaesi_stage` R · `s13_2_served_on` C · `s13_3a_objection_on`, `lender_reply_on` C · `s13_4_measure_on` C · `auction_notice_published_on` C · `drt_s17_filed` + date C · `property_value_claimed_minor` O · `tenants_in_property`: bool O |
| `blk.dr` | `drt_name`: enum (DRT list, config) R · `oa_no` R · `next_date` R · `stage`: enum DD-FIN-038 R · `amount_claimed_minor` R · `rc_issued`: bool O |

### 6.7 Vertical-specific forms

| ID | Title | Key fields (beyond core) | Rule |
|---|---|---|---|
| F-FIN-21 (v2) | Post-dispute Submission Agreement (Part A) & s.12(5) Waiver (Part B, separate signature) — per party | `dispute_description`, `dispute_arose_on`, express choice of Equator administration and Equator Rules version, seat/venue, fee-bearing rule; Part B names arbitrator + Seventh Schedule item; independent-advice prompt ("You do not have to sign this to settle") | `signed_at::date ≥ dispute_arose_on` (DB CHECK `fin.waiver_instruments`); LR-ARB-002/003 |
| F-FIN-22 | Parallel Proceedings Declaration | per P08 FR-P08-14 kinds + `cnr`, `oa_no`, `cms_complaint_no` | updates on change; drives S04–S06, S11, S12, S15 |
| F-FIN-23 | Affordability & Hardship Statement (tier High) | income, obligations, dependants, hardship, optional AA-derived summary via lender FIU | neutral and lender see derived summary only |
| F-FIN-25 | Settlement & Compounding Pack request (s.138; NN-24) | court, CC no., CNR, stage, agreed amount, payment proof, joint application consent of both, cost-slab acknowledgement (*Sanjabij Tari*), "no threat of conviction" declarations by both parties and neutral | output TPL-FIN-S03 is filed **by the parties**; court decides |
| F-FIN-26 | RB-IOS Informed-Choice Acknowledgement | RE name, RB-IOS coverage, computed last date, statement that pending arbitration may make an RB-IOS complaint non-maintainable, borrower's choice (`proceed_with_arbitration` · `use_rbios_first` · `mediate_or_conciliate_only`) | LR-RBI-003; required before arbitration opt-in |
| F-FIN-27 | Lender Programme Onboarding | legal entity, RE type, CoR/licence, RB-IOS coverage, IO applicability, GRO details per brand, 1600 numbers + `core.number_authorisations`, products, claim ceiling (≤ ₹50 lakh FIN-L), stages purchased (L1–L6), Board-policy refs, authority matrix, DPA/DSA, outsourcing annex, clause adoption | P09 FR-P09-23; §7.4 |
| F-FIN-28 | OTS Policy Grid (lender maker–checker) | per row: product, DPD bucket, value band, `max_interest_waiver_pct`, `max_penal_waiver_pct`, `max_principal_haircut_pct`, `max_instalment_months`, `min_upfront_pct`, `offer_validity_days` (≥ 14), `bureau_reporting`, `cooling_period_months` (≥ 12), excluded flags (wilful/fraud always excluded), `policy_ref`, `approver_role`, `approver_level_above_sanctioner` (attested bool), effective dates | §7.5; counsel item §18 Q-03 |
| F-FIN-29 | OTS Portal Acceptance / Counter | see §6.8 | §7.5 |
| F-FIN-30 | Bureau Rectification Request | CIC(s), CI, error type, dispute ID, documents; auto-computes 21/9/30-day dates | LR-RBI-013 |
| F-FIN-31 | Payments Escalation Pack | rail, RRN/UTR, bank complaint ID, TAT due date, compensation computed (C-FIN-17), RB-IOS date | LR-PAY-004 |

### 6.8 Borrower self-serve OTS portal screens (F-FIN-29; route `/r/ots/{token}`; web + mobile)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| `identity_step` | Verify it's you | OTP (mobile on file) + DOB or PAN last 4 | R | — | 5 attempts then `OTP_LOCKED`; K0 minimum; K1 (Aadhaar App QR/DigiLocker) for acceptance ≥ `fin.ots_portal.k1_threshold_minor` (default ₹50,000) | "This link is from [Lender], hosted on Equator's neutral platform." |
| `soa_view` | Your account as per [Lender] | read-only | — | P / I / penal charges / other separately | — | "Think this is wrong? Choose 'I dispute the amount'." |
| `offers[]` | Offers from [Lender] | read-only cards | — | ≤ 3 offers from grid (lump sum; ≤ 3-month instalments; > 3-month restructuring) | each shows total, schedule, bureau status, cooling-off, expiry (≥ 14 days, genuine) | No "best"/"recommended" badges; no countdown timers other than the real expiry (NN-29) |
| `choice` | What would you like to do? | enum | R | `accept_offer` · `propose_different` · `dispute_amount` · `ask_for_conciliator` · `not_now` | — | Each option equally prominent (dark-pattern lint) |
| `counter_amount_minor` / `counter_schedule` | Your proposal | money / table | C (`propose_different`) | — | ≥ ₹1; ≤ outstanding | Within grid → auto-accepted path; outside → lender approver queue (SLA 7 days) |
| `affordability_optional` | Share a summary of your ability to pay | embedded F-FIN-23 | O | — | — | — |
| `payment_rail` | How you'll pay | enum | C (accept) | lender VPA/payment link · eNACH (lender sponsor bank) · NEFT to lender account · escrow (if programme) | > ₹15,000 per instalment by UPI AutoPay/card → AFA notice (LR-PAY-003) | Money goes to [Lender], never to Equator |
| `disclosures_ack` | I have read: bureau status, cooling-off, tax note, free RBI Ombudsman route | bool | R | — | true | Tax note: "Waived amounts may have tax effects. We cannot advise." |
| `sign` | Sign the settlement letter | esign | R (accept) | Aadhaar eSign; OTP-click only where lender enables and amount < `fin.ots_portal.click_accept_max_minor` (default ₹0 = disabled) | e-stamp per NN-09 | — |

### 6.9 Dropdown Master List (FIN)

| ID | List | Values (code · label) |
|---|---|---|
| DD-FIN-001 | `initiator_role` | borrower · co_borrower · guarantor · legal_heir · cardholder · payer · payee · merchant · lender_re · lsp_for_re · arc · colending_partner_re · p2p_lender · private_lender |
| DD-FIN-002 | `re_type` | scheduled_commercial_bank · small_finance_bank · payments_bank · rrb · ucb · stcb_dccb · nbfc_icc · nbfc_mfi · hfc · gold_loan_nbfc · nbfc_p2p · arc · aifi · non_bank_ppi · card_issuer · payment_aggregator · tpap_upi_app · unregulated_lender · private_moneylender · other |
| DD-FIN-003 | respondent role | lender_re · lsp · dla · recovery_agency · cic · ci · co_lending_partner · guarantor · co_borrower · merchant · payment_aggregator · p2p_platform · individual |
| DD-FIN-010 | `loan_product` | personal · credit_card · app_bnpl · gold · silver · vehicle · home · lap · education · microfinance · business_msme · p2p · private · overdraft · kcc_agri · other |
| DD-FIN-011 | `dpd_bucket` | current · dpd_1_30 · dpd_31_60 · dpd_61_90 · npa_90_plus · written_off_technical · written_off_full · settled_ots · closed · unknown |
| DD-FIN-012 | `secured` | unsecured · secured_movable · secured_immovable · gold · vehicle_hypothecation · fd_lien · guarantee_only · unknown |
| DD-FIN-013 | `grievance_ladder_status` | not_raised · raised_with_re · re_replied · io_auto_escalated · io_final_reply · rbios_filed · rbios_decided · rbios_appeal |
| DD-FIN-014 | `pending_forum` | none · civil_court · commercial_court · drt · drat · nclt_ibc · consumer_commission · criminal_court_s138 · police_fir · lok_adalat · arbitration_other · rbios · sarfaesi_cmm_dm · unknown |
| DD-FIN-015 | `arbitration_clause_in_loan` | yes_names_equator · yes_named_institution_other · yes_unilateral_lender_appointment · yes_neutral_unspecified · no · unknown |
| DD-FIN-016 | PL sub-product | term_pl · salary_pl · top_up · consumer_durable · insta_app_pl |
| DD-FIN-017 | CC `dispute_kind` | billing_error · unauthorised_txn · merchant_non_delivery · refund_not_credited · charges_interest_stack · closure_delay · unsolicited_card_upgrade · settlement_of_dues · bureau_error |
| DD-FIN-018 | `vehicle_type` | car · two_wheeler · three_wheeler · commercial_vehicle · tractor · construction_equipment |
| DD-FIN-019 | `loan_purpose` (HL) | purchase · construction · lap_business · lap_personal · top_up · balance_transfer |
| DD-FIN-020 | value band | VB1 · VB2 · VB3 · VB4 · VB5 (§2.1) |
| DD-FIN-020a | documents deposited | sale_deed · title_chain · modt · allotment_letter · share_certificate_society · noc_builder · tax_receipts · other |
| DD-FIN-030 | `sarfaesi_stage` | none · s13_2_issued · s13_3a_objection_sent · lender_reply_received · s13_4_symbolic · physical_possession · auction_notice_published · sale_confirmed |
| DD-FIN-031 | co-lending B2B `dispute_head` | fund_flow · dlg_invocation · servicing_fee · classification · data_sharing · borrower_complaint_allocation · booking_delay · revenue_share |
| DD-FIN-032 | `principal_debtor_status` | paying · npa · ibc_cirp · liquidation · deceased · untraceable |
| DD-FIN-033 | CR `error_type` | account_not_mine · wrong_dpd · settled_vs_closed · closed_shown_open · wrong_amount · duplicate · guarantor_misreported · identity_mixup |
| DD-FIN-034 | `rail` | upi · imps · neft · rtgs · card · ppi_wallet · aeps · nach · bbps |
| DD-FIN-035 | payment `issue` | debited_not_credited · failed_not_reversed · merchant_non_delivery · refund_not_received · wrong_beneficiary · unauthorised · duplicate_debit |
| DD-FIN-036 | `return_reason` | funds_insufficient · exceeds_arrangement · stop_payment · account_closed · signature_mismatch · other |
| DD-FIN-037 | s.138 `stage` | pre_notice · notice_sent · pre_complaint · summons · plea · complainant_evidence · defence_evidence_recorded · arguments · judgment · sessions_appeal_revision · high_court · supreme_court |
| DD-FIN-038 | DRT `stage` | oa_filed · written_statement · evidence · final_hearing · rc_issued · execution · drat_appeal |
| DD-FIN-050 | `relief_sought` | ots_compromise · restructuring_emi · waiver_penal_charges · refund_excess_charges · stop_harassment · bureau_correction · release_documents_noc · release_collateral · surplus_refund · chargeback_refund · compensation_rbi_framework · compounding_s138 · withdrawal_of_case · other |
| DD-FIN-051 | `proposal_kind` / `offer_mode` | lump_sum · instalments_le_3m · instalments_gt_3m_restructuring · emi_reschedule · tenor_extension · moratorium |
| DD-FIN-052 | waivers | penal_charges · bounce_charges · interest_partial · interest_full · foreclosure_charge · legal_collection_charges · processing_fee_refund |
| DD-FIN-053 | non-money terms | noc_within_days · document_release · collateral_release · bureau_update · withdraw_proceedings · conduct_undertaking · change_of_agency · single_contact_channel · data_deletion |
| DD-FIN-054 | `bureau_reporting` | settled · closed · as_per_policy |
| DD-FIN-055 | `payment_rail` | lender_payment_link · lender_vpa · enach_lender_sponsor · neft_rtgs_to_lender · bank_escrow_trustee · direct_with_proof |
| DD-FIN-056 | claim heads | principal · contractual_interest · penal_charges · other_charges · costs · compensation_doc_release · compensation_cic · compensation_gold_release · compensation_device_lock · refund_excess_charges · surplus_refund |
| DD-FIN-057 | response `position` | participate_settle · participate_dispute_amount · dispute_liability · object_forum · request_information · request_extension |
| DD-FIN-060 | `vulnerability_flags` | senior_citizen · disability · illness_medical_emergency · bereavement · job_loss · mfi_household · first_time_digital_user · language_need · coercion_reported · pregnancy_maternity · caregiver |
| DD-FIN-061 | `hardship_reason` | job_loss · medical · business_loss · death_in_family · natural_calamity · salary_delay · other |
| DD-FIN-062 | `employment_status` | studying · employed · self_employed · unemployed_seeking · abroad_employed · abroad_unemployed |
| DD-FIN-063 | `source_of_funds` | savings · family_support · sale_of_asset · new_job · business_income · insurance_proceeds · other |
| DD-FIN-070 | charges disputed | penal · bounce · processing · foreclosure_prepayment · insurance_bundled · gst_on_charges · legal_collection · rate_reset · annual_fee · late_fee_card |
| DD-FIN-071 | `issue_kind` (CH) | wrong_charges · mis_selling |
| DD-FIN-080 | `conduct_type` | outside_hours · inappropriate_occasion · abusive_language · threat · contact_third_parties · public_shaming · visit_without_id · device_lock_violation · anonymous_calls · excessive_calls · false_statements |
| DD-FIN-081 | DL `harassment_types` | contacts_called · morphed_images · threats · calls_outside_hours · public_shaming |
| DD-FIN-090 | contact channel | whatsapp · sms · voice_call · email · in_app (time range within 08:00–19:00) |
| DD-FIN-091 | mode | online · in_person · hybrid · phone_only |

---

## 7. Modus operandi per subtype

### 7.1 Ladders (pinned `pathway` per ruleset; Appendix A §4.1 governs time-boxes)

| Ladder | Rungs (time-box) | Used by |
|---|---|---|
| `fin.std` | 0′ signposting (parallel) → 1 negotiation (21 d) → 2 conciliation Part III (30 d; s.62(4) invitation lapse 30 d) → 3 contractual mediation (60 d + 60 by consent) → 4 arbitration (only §4.6) → compliance | PL, CC, GL, VL, HL, EL, PP, MS, GT, CL, OT |
| `fin.grv` | 0 RE grievance (30 d; IO day 20) ∥ 1–3 as `fin.std` with consent; arbitration ✖ for CR/RC | DL, RC, CH, CR |
| `fin.ni` | 1 negotiation (14 d) → 2 conciliation/mediation (30 d, aligned to next court date) → compounding pack → court | SET.NI |
| `fin.sf` | 1 negotiation (14 d; auction-date-aware) → 2 conciliation (30 d) → DRT/court recording pack | SET.SF, SET.DR |
| `fin.mf` | 0 grievance → 2 shuttle conciliation (30 d); IVR/voice vernacular summaries; no blind-bid | RET.MF |
| `fin.pay` | 0 bank/PSO process (TAT) → 2 mediation (merchant–customer, 30 d) | PAY.TX, PAY.CB |
| `fin.b2b` | 1 negotiation (21 d) → 3 mediation (60 d) → 4 arbitration (fast track by agreement; s.29A) | BUS.CB, PAY.MP |
| `fin.ots` | OTS portal (offer validity ≥ 14 d) → conciliation on request (30 d) | SET.OT under lender programme |

Conflict resolved: P08 FR-P08-15 sets the negotiation rung at 14 days; Appendix A §4.1 sets 21 days. Appendix A prevails on clocks (master §15 order 5 > 6; resolved in X-40); `fin.negotiation_box_days` default 21 (range 7–30 retained); `fin.ni`, `fin.sf` use 14 because statutory dates are tighter.

### 7.2 Standard step table (`fin.std`)

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | Party | Explorer → save → KYC (K0 OTP; K1 Aadhaar App QR/DigiLocker for signing) → F-FIN-02 / F-FIN-24 | — | §9 checklist | — | Suitability §4 |
| 2 | System | Suitability + signposting; quote (FIN-R) or programme ₹0 | real-time | — | RB-IOS block §4.7 | ACCEPT / COND / SIGNPOST |
| 3 | Case manager | Scrutiny: RE identified, parallel proceedings, clause validation, limitation estimate | 1–2 working days (`sla_scrutiny`) | F-FIN-22 | Deficiency notice | `accepted` / `deficient` |
| 4 | System | Invitation to respondent (§8.2 content); lender GRO footer | dispatch ≤ 3 working days; NN-12 window | TPL-FIN-N01 | D0/D3/D7/D10/D14 cadence (§8.3) | — |
| 5 | Respondent | Response F-FIN-05 (14 d) | `response_window` | SOA (lender) | — | Participate / object / decline → non-commencement |
| 6 | Parties | Negotiation: structured offers, optional blind-bid | 21 d | — | offer expiry ≥ 14 d | Agreement → step 10; else step 7 |
| 7 | System | Conciliator/mediator allocation (P03 engine; FIN panel; grade per value band) | appointment ≤ 3–5 working days of consent | F-FIN-06 disclosure | Appointment notice | Challenge window 3 working days |
| 8 | Neutral | Pre-session calls each side; authority-to-settle check (`authority_limit_minor`); vulnerability brief | first session ≤ 14 d of appointment | Authority letter | Session reminders T-48h/T-2h | — |
| 9 | Neutral + parties | Joint/caucus sessions online; OTS room (SCR-P08-04); calculators shown as indicative | 30 d conciliation / 60 d mediation | F-FIN-23 summary | — | Settled / partial / not settled |
| 10 | Neutral + case manager | Draft settlement (TPL-FIN-S01/S02); lint (penal separate, no Equator fee in dues, bureau wording, NOC days, no deletion of true history) | 3 working days | Policy ref + approver (lender) | — | Lint pass |
| 11 | Parties | E-sign + e-stamp (state of execution); s.73 authentication by conciliator where Part III | — | Stamp certificate | Signed copies to all | — |
| 12 | Escrow officer / parties | Payment on lender rail or escrow; instalment tracking | per schedule | Payment proofs | Pre-debit notice ≥ 24 h (e-mandate) | Missed instalment → `equator.fin.instalment.missed.v1` |
| 13 | Lender / system | NOC (15 d), documents/collateral release (30 d / gold 7 working days), bureau update (30 d) as owned obligations (`FinNocBureauWorkflow`) | `fin_noc_issue`, `doc_release_30d`, `bureau_update_30d` | NOC, release receipt, bureau evidence | Overdue reminders | Clean exit |
| 14 | Case manager | Closure (all clocks owned; signposting recorded; clean-exit conditions) | — | F-FIN-15, F-FIN-16 | Closure notice | `closed` |

### 7.3 Subtype deltas to §7.2

| L2 | Delta |
|---|---|
| `FIN.RET.PL` | Step 9: penal-charge breakup reconciliation against KFS; step 10: restructuring flag if schedule > 3 months |
| `FIN.RET.CC` | Step 2: chargeback-first check (S08); step 10: interest-freeze and EMI-conversion terms; closure + ₹500/day computation (C-FIN-19) **[VERIFY — open: Credit Card Directions current text (Q-07)]** |
| `FIN.RET.DL` | Step 3: RE identification hard gate (S02/S18); step 4: notice to RE nodal GRO + LSP; step 10: harassment-stop undertaking, data-deletion request letter (DPDP s.12 when in force) |
| `FIN.RET.GL` | Step 3: `sanction_date` legacy flag; step 9: joint re-assay protocol at a BIS-recognised hallmarking/assaying centre (cost split per agreement); step 13: release within 7 working days, C-FIN-06; auction cases → C-FIN-07 surplus |
| `FIN.RET.VL` | Step 9: valuation dispute → independent valuer by agreement; step 13: NOC + Form 35 timeline; personal belongings inventory term |
| `FIN.RET.HL` | Step 3: SARFAESI stage check (→ `fin.sf`); step 11: NN-08 — any transfer/partition of immovable property or registered release deed routes to physical execution + registration (Registration Act 1908 s.17); MODT return of title deeds (no registration) as compliance obligation |
| `FIN.RET.EL` | Step 9: subsidy-correction letter to bank/nodal agency; step 11: cross-border e-sign for student abroad (INT eSign rules) |
| `FIN.RET.MF` | Steps 6–9 shuttle-only; voice/IVR summaries in borrower language; FOIR evidence; 24-hour gap before signature; group-member consent records |
| `FIN.RET.PP` | Step 3: join each lender; step 10: acknowledgment-of-debt clause flagged (fresh limitation, Limitation Act s.18) to both sides |
| `FIN.BUS.MS` | Step 8: lender committee cycle → authority confirmation may be "subject to committee" with date; PG terms; MSEFC signposting for receivables |
| `FIN.BUS.CL` | Steps 4–11: both REs as parties; each RE's policy ref + approver; single point of contact named |
| `FIN.BUS.CB` | Ladder `fin.b2b`; loan-level CSV reconciliation (TPL-FIN-B01); tribunal-appointed expert (A&C s.26) for accounts; confidentiality of borrower data (purpose limitation) |
| `FIN.BUS.GT` | Step 4: auto-join guarantors; step 10: release deed / contribution agreement / subrogation acknowledgment; s.94/95 filing → hold |
| `FIN.CND.RC` | Step 2: safety screen; step 4: no contact by lender side to borrower via Equator outside NN-12; step 10: conduct undertaking (RE + agency), change of agency, single contact channel, compensation |
| `FIN.CND.CH` | Step 0: GRO letter TPL-FIN-L01; refund/correction terms; linked INS case for bundled policy |
| `FIN.CND.CR` | Step 0: TPL-FIN-L03 to CI and CIC (C-FIN-09 clock); step 10: CI obligation clause (report within next submission cycle; agreed status wording); never deletion of true history |
| `FIN.PAY.*` | Step 0: bank/PSO escalation pack F-FIN-31; mediation only with merchant/bank consent; no "reversal" language |
| `FIN.SET.OT` | §7.5 portal; lender OTS Sanction Pack (para 16(5) checks; wilful/fraud → Board) |
| `FIN.SET.NI` | §7.6 |
| `FIN.SET.SF` / `FIN.SET.DR` | §7.7 |

### 7.4 Lender bulk programme (L3 + FIN-L)

| Step | Actor | Action | Control |
|---|---|---|---|
| P1 | `enterprise_admin` | F-FIN-27 onboarding; DPA/DSA; outsourcing annex | `DPA_REQUIRED` until executed (P09 FR-P09-23) |
| P2 | Legal reviewer (Equator) | Clause adoption (P09 FR-P09-07); validate no lender choice/veto; seat fairness | `CLAUSE_VARIANT_PROHIBITED` |
| P3 | Lender maker → checker | Upload OTS Policy Grid F-FIN-28; Equator lint (cooling ≥ 12 m; validity ≥ 14 d; wilful/fraud excluded; approver attestation) | `fin.policy_grid` states `draft → submitted → equator_lint_passed → lender_approved → active → superseded` |
| P4 | Telecom | `core.number_authorisations` (1600, purposes incl. `ots_offer_relay`), DLT templates per language, consent registration | `CLI_NOT_AUTHORISED` |
| P5 | `enterprise_operator` | Bulk job (P09 FR-P09-11/12) with FIN template (§11.3 columns); legal gates: arbitration rows need consent artefact; SARFAESI/DRT/IBC flags; fraud/wilful rows → no portal offers | `BULK_ROW_INVALID` sub-codes |
| P6 | System | Notices + OTS portal links (staggered 5,000/min/tenant; NN-12; GRO footer; commercial-relationship disclosure NN-16) | frequency cap ≤ 6 pre-consent contacts per borrower (S4 B5.3) |
| P7 | System / neutrals | Portal outcomes; counters to lender queue; conciliation on request (L2/L3 pricing — neutral component identical settled or not) | X-07; NN-18 |
| P8 | Lender | Approver queue (7-day SLA); LMS write-back via `equator.fin.settlement.terms_agreed.v1` | `OFFER_ABOVE_AUTHORITY` |
| P9 | Both | Compliance tracking; MIS; Board export; Independence Evidence Pack | P09 FR-P09-14–16 |

Optional **Settlement Days** (batched virtual sessions, benchmark: insurer settlement days, S3 C1): ≤ 30 borrowers per neutral per day, borrower free to decline, outcome per file, lender authority confirmed in advance; no "bulk awards".

### 7.5 Borrower self-serve OTS portal flow (`fin.ots`)

`link_issued → identity_verified → viewed → {accepted_within_grid → letter_generated → signed → stamped → payment_pending → in_compliance} | {counter_submitted → lender_review (≤ 7 d) → {counter_accepted → letter_generated …} | {counter_declined → conciliation_offered}} | dispute_amount → case_opened (FIN.SET.OT, ladder fin.std) | conciliator_requested → conciliation | not_now → reminder (max 2, NN-12) | expired`.

Rules: (1) offers are lender offers generated deterministically from the active grid (no AI; NN-01); (2) acceptance within grid is a lender acceptance pre-approved under the grid's policy ref and approver — the portal stores `policy_grid_version_id` on the settlement (LR-RBI-011) **[VERIFY — open: counsel Q-03]**; (3) borrower pays ₹0 (Card FIN-L); (4) every screen shows the neutral-host statement, the RB-IOS route and "Ask for an independent conciliator (free)"; (5) no false urgency, no pre-ticked boxes, decline as easy as accept (NN-29); (6) no data from the portal flows to growth/marketing (NN-16); (7) settlement money only on lender rail or escrow (NN-13); (8) Equator does not phone borrowers to push acceptance — reminders are logistics only and lender-number mode (X-05; NN-12).

### 7.6 NI Act s.138 (`fin.ni`; NN-24)

| Step | Actor | Action | Clock | Output |
|---|---|---|---|---|
| N1 | Either party | Request; stage captured; C-FIN-11 statutory dates; cost slab (P08 `fin.ni138_cost@1`) | `ni138_*` informational | — |
| N2 | Neutral | Money-only mediation/conciliation; declarations by both parties and neutral that no threat of prosecution or conviction is used | 30 d or before next court date | — |
| N3 | Parties | Settlement: amount, mode (lump sum preferred; post-dated instalments with default clause), escrow-free direct payment with proof | — | TPL-FIN-S01 variant |
| N4 | System | Compounding pack F-FIN-25 → TPL-FIN-S03 joint compounding application / withdrawal memo, payment proof, cost-slab note (*Sanjabij Tari*) | — | PDF bundle with BSA s.63 certificate |
| N5 | Parties (not Equator) | File before the court; court decides compounding (s.147) | court date | Court order uploaded → compliance close |

### 7.7 SARFAESI / DRT (`fin.sf`)

| Step | Action | Clock |
|---|---|---|
| F1 | Capture stage; C-FIN-12 timers; redemption warning on auction-notice publication | `sarfaesi_*` |
| F2 | Offer OTS negotiation to lender; copy: "Equator cannot stop the bank's action; only the DRT can" | — |
| F3 | Lender authority + Board-policy ref; deposit schedule proposal | — |
| F4 | Settlement with lender undertaking to withdraw auction notice/measures on payment; DRT joint memo (TPL-FIN-S05) where OA/s.17 pending | — |
| F5 | Release of security and title documents as compliance obligations; NN-08 if property is transferred | `doc_release_30d` |

---

## 8. Pre-litigation journey (FIN)

### 8.1 Stages (S4 B5.1 `prelit_case`, FIN parameters)

`DRAFT → SUITABILITY_CHECK → {SIGNPOSTED | NOTICE_READY} → INVITATION_SENT → {VIEWED, RESPONDED(ACCEPT | ACCEPT_WITH_CONDITIONS | DECLINE | COUNTER_OFFER | OBJECT_FORUM | REQUEST_INFO | REQUEST_EXTENSION ≤ 14 d once) | NO_RESPONSE} → CONSENT_PENDING_SIGNATURE → CONSENTED → NEUTRAL_APPOINTED → PRE_MEDIATION → IN_SESSION → {SETTLED_IN_PRINCIPLE → DRAFTING → SIGNED → OUTPUT_CONVERSION | PARTIAL | NOT_SETTLED | SUSPENDED} → COMPLIANCE_TRACKING → CLOSED_PERFORMED | CLOSED_BREACHED`. Non-response: D14 (individual respondent) / D30 (RE or company; s.62(4) where conciliation invited) → NON_COMMENCEMENT report (no reasons, no adverse inference).

### 8.2 Invitation content (FIN additions to S4 B5.2)

Sender "Equator Resolution Service Private Limited — Case Administrator" + named case manager + verify URL/QR; nature "Invitation to conciliation under Part III of the Arbitration and Conciliation Act, 1996" (default for RE respondents) or "Invitation to mediation"; voluntary; claimant-approved neutral summary; amount; RB-IOS block where covered; **lender-initiated invitations to borrowers** carry the lender's GRO details (LR-RBI-007), the commercial-relationship disclosure ("[Lender] pays Equator's fees under a published programme; this does not affect who the conciliator is or how they act" — NN-16), and the statement "Equator is not a recovery agent". Limitation notice: "This invitation does not stop limitation periods." Banned words (lint): "legal action will follow", "final warning", "defaulter", "court", "decree", "arrest", "police", "conviction".

### 8.3 Cadence and contact-conduct policy (NN-12)

| Day | Action | Channel / CLI |
|---|---|---|
| D0 | Invitation | Email + WhatsApp utility template + DLT SMS; speed post for VB4–VB5 or RE respondents |
| D3 | Reminder 1 | WhatsApp/SMS |
| D7 | Reminder 2 + case-manager call | Voice: lender-referred matters in lender-number (1600) mode under `core.number_authorisations`; Equator DID only if `voice.equator_service_number.enabled` |
| D10 | Final notice (individual respondents) | Email + WhatsApp + SMS |
| D14 / D30 | Close as non-commencement | — |

Policy (Contact Policy Engine, P07): window 08:00–19:00 borrower local time (`CONTACT_OUTSIDE_WINDOW`); blackout calendar (`CONTACT_BLACKOUT_ACTIVE`); Sunday/public-holiday block ON as Equator policy (LR-RBI-009; not RBI law); ≤ 6 pre-consent contacts; ≤ 3 call attempts per day; first utterance discloses entity, automated assistant, purpose, recording and opt-out (LR-TEL-004); every call recorded with notice and retained ≥ 6 months (until disposal if sub judice) (LR-RBI-006); GRO footer on every lender-related message (`GRO_DETAILS_MISSING`); discussion only with borrower/guarantor (no third-party contacts — LR-RBI-008; LR-TEL-005); DND scrub + operator consent registration for automated calls (LR-TEL-009); voice agent relays OTS offers only in the pre-proceeding negotiation rung, never inside mediation (X-05).

### 8.4 Consent and conversion

Consent: Agreement to Mediate (F-FIN-17) or s.62 written acceptance, Aadhaar eSign/DSC, Rules version hash; sub-consents (online mode, no recording, language, interpreter, fee allocation, optional arbitration agreement for consent award — separate signature, "You do not have to sign this to settle"). Conversion options ranked (S4 B1): (1) s.73 settlement with s.74 status (default where conciliation); (2) consent award s.30 (valid basis + different neutral by default); (3) Lok Adalat recording pack (DLSA joint application, LSA s.20(2)) **[VERIFY — open: DLSA acceptance practice (S4 Q-C8)]**; (4) court/DRT compromise pack (CPC O.XXIII r.3; DRT joint memo); (5) s.138 compounding pack; (6) contractual MSA. Compliance: `FinNocBureauWorkflow`; breach → return-to-mediation (ANC.REMEDIATION) or enforcement pack (§13).

---

## 9. Document checklists per subtype

Formats: PDF/A or PDF (≤ 25 MB), JPG/PNG/HEIC (images → PDF bundle), CSV/XLSX (data), MP3/M4A/OGG (recordings), WhatsApp `.txt`/`.zip` export (S7 §3.1 ingest). All files: ClamAV, hash into `core.evidence_ledger`, original preserved, OCR/type copy as derived version (NN-32); Aadhaar images rejected unless masked (`AADHAAR_UNMASKED_DETECTED`); card numbers redacted to last 4 by OCR guard (NN-31). Verification codes: **V-SIG** issuer signature/QR; **V-OCR** OCR + field match to intake; **V-RE** produced by the RE party; **V-CM** case-manager review; **V-HASH** hash/metadata integrity check (edit detection).

| Code | L2 | Document | M/O | Formats | Verification |
|---|---|---|---|---|---|
| DOC-FIN-C01 | all loans | Sanction letter / loan agreement | M (lender) / O (borrower) | PDF | V-OCR, V-RE |
| DOC-FIN-C02 | all loans | Key Facts Statement | M (lender) | PDF | V-OCR; charges-not-in-KFS check |
| DOC-FIN-C03 | all loans | Statement of account (P / I / penal separate) | M (lender respondent or claimant) | PDF, XLSX | V-RE; penal-capitalisation check |
| DOC-FIN-C04 | all | Proof of payments (UTR/UPI refs, receipts) | O | PDF, images | V-OCR |
| DOC-FIN-C05 | all | Complaint to RE + reply | C (S09) | PDF, email, images | V-CM |
| DOC-FIN-C06 | all | Authority letter / Board resolution of organisational party | M (org) | PDF | V-CM; DIN match (MCA) |
| DOC-FIN-C07 | all | Hardship evidence (job loss, medical, death certificate) | O | PDF, images | V-CM; tier High |
| DOC-FIN-PL1 | PL | Foreclosure letter / bounce-charge breakup | O | PDF | V-OCR |
| DOC-FIN-CC1 | CC | Card statements for disputed cycles; chargeback ref + issuer reply; closure request proof | M (txn/closure disputes) | PDF, images | V-OCR (PAN masked) |
| DOC-FIN-DL1 | DL | App screenshots (offer, KFS, APR), disbursal SMS, Play Store page, package ID | M | images | V-HASH |
| DOC-FIN-DL2 | DL | Threat/harassment evidence (calls, chats, morphed images) | O | images, audio, chat export | V-HASH; sealed if safety flag (`safety_sealed`) |
| DOC-FIN-GL1 | GL | Pledge card/receipt, appraisal certificate (purity, gross/net weight, value), photos at pledge | M | PDF, images | V-OCR |
| DOC-FIN-GL2 | GL | Auction notice, public notice, sale details, surplus computation | C (auction) | PDF | V-RE |
| DOC-FIN-VL1 | VL | Repossession notice, inventory list, valuation report, sale notice, sale-proceeds statement, RC copy | C | PDF, images | V-OCR (RC via DigiLocker where available — V-SIG) |
| DOC-FIN-HL1 | HL | List of title documents deposited (MODT), rate-reset letters, property papers | M (document-release/rate disputes) | PDF | V-OCR |
| DOC-FIN-EL1 | EL | Admission letter, fee receipts, disbursal schedule, subsidy claim reference | M | PDF | V-OCR |
| DOC-FIN-MF1 | MF | Loan card/passbook, KFS, other lenders' loan cards (FOIR) | M | images | V-CM; voice-assisted capture allowed |
| DOC-FIN-PP1 | PP | Promissory note / agreement, transfer proofs, chat agreements | M (one of) | PDF, images, chat export | V-HASH; BSA s.63 certificate at export |
| DOC-FIN-MS1 | MS | Security documents, guarantee deeds, stock statements, GST returns, financials, CGTMSE cover, SMA/NPA letters | M (lender) / O | PDF, XLSX | V-RE; Udyam/GSTIN verify |
| DOC-FIN-CL1 | CL/CB | Master co-lending agreement, allocation records, escrow statements, DLG invocation notices, loan-level CSV | M (CB) | PDF, CSV | V-RE; CSV schema TPL-FIN-B01 |
| DOC-FIN-GT1 | GT | Guarantee deed, invocation notice, variation/renewal letters | M | PDF | V-OCR |
| DOC-FIN-RC1 | RC | Call logs, recordings, visit details, agency/agent names, police complaint | M (one of) | images, audio | V-HASH; tier High |
| DOC-FIN-CR1 | CR | Credit report (party-supplied), CIC dispute ID, NOC/closure letter | M | PDF | V-HASH (report control number, date, name vs K1 identity; incremental-save detection) |
| DOC-FIN-PY1 | PAY | Transaction ID/screenshot, bank statement, bank/UDIR complaint ID, merchant invoice/order | M | PDF, images | V-OCR |
| DOC-FIN-NI1 | NI | Cheque copy, return memo, demand notice + postal proof, reply, complaint copy (CC no./CNR), order sheets | M | PDF, images | V-OCR; eCourts CNR lookup (V-SIG where available) |
| DOC-FIN-SF1 | SF | s.13(2) notice, objection + reply, possession notice, auction notice, valuation, sale certificate | M (available ones) | PDF | V-OCR; dates → C-FIN-12 |
| DOC-FIN-DR1 | DR | OA copy, written statement, DRT orders, RC | M | PDF | V-OCR |

---

## 10. Practical difficulties and product solutions

| # | Difficulty | Product solution |
|---|---|---|
| PD-01 | Lender SOA vs borrower ledger mismatch; stacked bounce/penal charges | Component table (P/I/penal/other) mandatory; AA-derived EMI match via lender FIU (P09 FR-P09-22) or statement OCR; penal-capitalisation HB |
| PD-02 | Lender officer has no settlement authority; committee cycles take weeks | `authority_limit_minor` + named approver; "subject to committee by [date]" status; OTS Policy Grid for pre-approved offers |
| PD-03 | RE hidden behind an LSP brand | RE directory lookup; KFS/DLA screenshot OCR; S02/S18 gates; RE joined as party |
| PD-04 | Borrower fears complaining worsens recovery | Neutral-host statement; blackout + window enforcement on all lender contacts relayed via Equator; conduct undertaking term |
| PD-05 | "Settled" bureau tag harms future credit; borrower wants "closed" | DD-FIN-054 negotiated term; never deletion of true history; CI obligation clause; counsel Q (S3 OLQ-11) |
| PD-06 | Multiple lenders (debt stack) | Multi-case linkage (`core.linked_matters`); FOIR across all loans; one affordability statement shared by consent |
| PD-07 | Gold purity/weight disputes after release; stale auction addresses; surplus netted against "other dues" | Joint re-assay workflow; address-research step; surplus calculator lists only dues permitted by agreement |
| PD-08 | Unmarked repossession agents; low valuation | 100X checklist (ID card, authorisation letter); independent valuer option; police signpost for force |
| PD-09 | Timing of SARFAESI auction (redemption lost on publication) | Countdown + urgent banner; same-day CM task; lender deposit schedule template |
| PD-10 | Accused avoids summons; multiple cheques in multiple courts | Multi-cheque table in F-FIN-25; one settlement with a schedule of court cases; *Sanjabij Tari* e-summons note |
| PD-11 | Complainant wants a criminal "lever" | NN-24 copy; neutral declaration; guardrail VG-FIN-03 |
| PD-12 | Instalment settlements fail | eNACH on lender rail; pre-debit notices; default clause; escrow option; return-to-mediation session |
| PD-13 | Co-lending complaints bounce between REs | Both REs mandatory parties; SPOC field; one settlement signed by both |
| PD-14 | Microfinance: group pressure, women's privacy, low digital literacy | Shuttle-only, private-contact flag, IVR/voice summaries, field-assisted mode (P07 kiosk), group-consent records |
| PD-15 | Customers expect Equator to reverse payments | Copy and HX-FIN-09; bank escalation pack first |
| PD-16 | Lender-driven ODR perceived as a collections tool (Bombay HC 2025) | NN-03 gates; IEP; commercial-relationship disclosure; "not a recovery agent" lint; borrower ₹0 |
| PD-17 | Harassment evidence is ephemeral | In-app capture with hash on upload; WhatsApp export ingest; BSA s.63 certificate |
| PD-18 | Legacy loans under old rules (gold < 1 Apr 2026; pre-payment < 1 Jan 2026; conduct < 1 Jan 2027) | Date-driven rule versions with "may not apply" copy |
| PD-19 | Student/borrower abroad | Cross-border notice and eSign (INT rules), time-zone scheduling |
| PD-20 | Personal guarantors negotiate separately | Guarantor sub-settlements; release deed; contribution agreement |

---

## 11. Integrations and APIs

### 11.1 Providers and systems

| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| Finbyx (LOS/LMS), Udofin (LSP) | Clause-at-sanction; default events; SOA; settlement write-back | Loan ref, clause instance, SOA, terms agreed | Lender contract + DPA; DPDP s.17(1)(a) for respondent data | API (P09 FR-P09-08/10) | SFTP/CSV |
| Other LOS/LMS/collections (Credgenics-class) | Bulk referral, status write-back | Bulk rows | DPA | API/SFTP | Console upload |
| Account Aggregator (via lender FIU/TSP) | Repayment verification; affordability | FI data → derived summary | AA Directions 2025 para 8(12); consent artefact | API via `AA_PORT` (flag `fin_aa_evidence`) | Statement upload + OCR |
| Credit bureaus (CIBIL, Experian, Equifax, CRIF) | **No pull.** Party upload; lender production; CI/CIC dispute letters | Report PDF, tradelines | CICRA s.2(l) (Equator not a specified user) | Manual/export | — |
| RBI CMS (cms.rbi.org.in) | RB-IOS complaint by the borrower | Pre-filled draft text (TPL-FIN-L02) | Borrower files | Manual (no API) | — |
| NPCI UDIR / bank grievance | Payment disputes | Escalation pack | Bank/PSO process | Manual export | — |
| eCourts / NJDG (CNR) | s.138 case status | CNR, next date, stage | Public data | Lookup via KYC aggregator (Surepass eCourts) | Manual entry |
| DRT case status (e-DRT) | OA status | OA no., next date | Public | Manual entry **[VERIFY — open: e-DRT public lookup availability]** | — |
| Aadhaar (OVSE, Aadhaar App QR/AVC), DigiLocker, PAN (aggregator), MCA, GSTIN, Udyam | Onboarding K1/KYB; signatory authority; MSME status | Minimal attributes | D2-06; App S §3 | API | Manual review |
| CERSAI | Security-interest search (party-supplied report) | Search report | Party obtains | Upload | — |
| Razorpay / lender PA, eNACH sponsor bank, RazorpayX Escrow+/Castler | Fees (Equator merchant); settlement on lender rail or escrow | Payment status | PA Directions 2025; NN-13 | API/webhook | Direct with proof |
| Leegality (eSign/eStamp) | Settlement execution; state duty | Documents | IT Act s.3A; state stamp Acts | `ESIGN_PORT`/`ESTAMP_PORT` | Digio/SignDesk; physical |
| Exotel/Plivo + DLT; Gupshup WhatsApp; MSG91 | Notices, reminders, lender-number calls | Contact points | TCCCPR; consent registration | `TELEPHONY_PORT`, `MESSAGING_PORT` | Fallback provider |
| NALSA/SLSA calendars | Lok Adalat dates | Dates | Public | Manual/config | — |
| Vidya Lakshmi portal, Sachet, cybercrime.gov.in | Signposting links | — | Public | Link-out | — |

### 11.2 APIs (new in V1; `/v1`; problem+json; idempotency on POST)

| Method + path | Purpose | Roles / scope | Idempotency |
|---|---|---|---|
| POST `/v1/explorer/fin/evaluate` | Stateless Explorer evaluation → outcome, route, clocks | public (rate-limited) | — |
| POST `/v1/cases/{caseId}/fin/suitability` | Re-run §4 with current facts | case_manager | key |
| GET `/v1/cases/{caseId}/fin/signposting` | Rows incl. RB-IOS last date | parties, case_manager | — |
| POST `/v1/cases/{caseId}/fin/rbios-ack` | F-FIN-26 | borrower | key |
| POST `/v1/cases/{caseId}/fin/compounding-pack` | F-FIN-25 → PDF bundle | parties (both consents) | key |
| POST `/v1/cases/{caseId}/fin/bureau-letters` | TPL-FIN-L03 to CI + CIC | borrower | key |
| POST `/v1/cases/{caseId}/fin/payments-pack` | F-FIN-31 | payer | key |
| POST `/v1/calculators/fin/{calcKey}` | C-FIN-06 … C-FIN-19 (`calc:run`) | any; case-scoped persists to `fin.calc_runs` | — |
| POST `/v1/enterprise/fin/programmes` · PATCH `…/{id}` | F-FIN-27 | enterprise_admin; institution_admin approves | key |
| POST `/v1/enterprise/fin/policy-grids` · POST `…/{id}/submit` · POST `…/{id}/approve` | F-FIN-28 maker–checker (approver ≠ maker, `MAKER_CHECKER_SAME_USER`) | enterprise_admin | key |
| POST `/v1/enterprise/fin/ots-links` | Issue portal links for accounts (bulk or single) | enterprise_operator (`bulk:write`) | key |
| GET `/v1/ots/{token}` · POST `/v1/ots/{token}/verify` · POST `/v1/ots/{token}/decision` | Borrower portal (F-FIN-29) | borrower (token + OTP) | key on decision |
| GET `/v1/enterprise/fin/ots-queue` · POST `/v1/enterprise/fin/ots-queue/{id}/decide` | Lender approver queue | party_org_user within authority | key |

### 11.3 FIN bulk template (column dictionary, `eqr.bulk.fin.loan.v2`)

`external_ref` (R, unique per tenant) · `l2_code` (R) · `loan_account_no` (R; stored HMAC + last 4) · `borrower_name` (R) · `mobile_e164` (R) · `email` (O) · `address_pincode` (R; stamp state) · `language` (R) · `sanction_date` (R) · `principal_minor`, `interest_minor`, `penal_minor`, `other_charges_minor` (R) · `dpd` (R) · `npa_date` (C) · `secured` (R) · `clause_instance_id` (C; required for `mechanism = arbitration`) · `pending_forum` (R; `drt|sarfaesi|ibc|s138|none`) · `wilful_defaulter_flag`, `fraud_flag` (R) · `policy_grid_id` (C; portal offers) · `guarantors_json` (O) · `gro_brand_id` (R) · `vulnerability_hint` (O; never displayed to lender users after intake) · `mechanism` (R; `negotiation|conciliation|ots_portal|arbitration`). Row sub-codes: `ROW_RE_FLAG_FRAUD_NO_OFFER`, `ROW_DRT_BANK_ARBITRATION`, `ROW_CLAUSE_MISSING`, `ROW_IBC_HOLD`, `ROW_PENAL_CAPITALISED` → `BULK_ROW_INVALID`.

---

## 12. Calculators (indicative only; never advice, valuation or prediction — NN-01)

P08 FR-P08-18 calculators 1–5 (`fin.ots_estimator@1`, `fin.interest_penal@1`, `fin.emi_restructure@1`, `fin.ni138_cost@1`, `fin.compliance_status@1`) are unchanged. New calculators follow FR-P08-08 (Zod input, pinned parameters, `computation_trace[]`, `indicative: true`, integer paise; dates in Asia/Kolkata with the configured state holiday calendar; working days exclude Saturdays/Sundays and configured holidays unless the rule says otherwise). Each golden vector below is a unit test.

| ID / key | Inputs | Formula / logic | Output | Golden vector |
|---|---|---|---|---|
| C-FIN-06 `fin.gold_release_delay@1` | `full_repayment_date`, `release_date_actual` (or today), `delay_attributable_to_re` | `due = add_working_days(full_repayment_date, 7)`; `delay_days = max(0, release − due)` calendar days; `comp = delay_days × ₹5,000` if attributable | due date, delay days, compensation | Repaid Mon 1 Feb 2027; no holidays; due **10 Feb 2027**; released 16 Feb 2027 → 6 days → **₹30,000**. Parameters `gold_release_wd = 7`, `gold_comp_per_day = 500000` paise **[VERIFY — open: day-count convention]** |
| C-FIN-07 `fin.gold_auction_surplus@1` | `net_weight_g`, purity, `ref_price_per_g` (config source), `sale_price`, dues (P, I, permitted charges), auction expenses | `value = net_weight × ref_price`; `reserve_ok = sale_price ≥ 0.90 × value`; `surplus = sale_price − (P + I + charges) − expenses` | reserve check, surplus | 40 g 22K × ₹9,000 = ₹3,60,000; floor ₹3,24,000; sale ₹3,30,000 → reserve OK; dues ₹2,50,000 + ₹30,000 + ₹5,000; expenses ₹3,000 → surplus **₹42,000** |
| C-FIN-08 `fin.doc_release_comp@1` | `closure_date`, `released_on`, `documents_lost` | `due = closure + 30 d (+30 d if lost)`; `comp = max(0, released − due) × ₹5,000` | due, compensation | Closed 10 Jan 2027 → due **9 Feb 2027**; released 20 Feb 2027 → 11 days → **₹55,000** (LR-RBI-024) |
| C-FIN-09 `fin.cic_comp@1` | `complaint_date`, `ci_sent_on`, `resolved_on` | `ci_due = complaint + 21 d`; `total_due = complaint + 30 d`; `delay = max(0, resolved − total_due)`; CI share = `min(delay, max(0, ci_sent − ci_due))`; CIC share = rest; ₹100/day | delay days, ₹ by CI/CIC | Complaint 1 Mar 2027; CI due 22 Mar; CI sent 29 Mar; due 31 Mar; resolved 15 Apr → 15 days → **₹1,500** (CI 7 days ₹700; CIC 8 days ₹800) **[VERIFY — open: apportionment method]** |
| C-FIN-10 `fin.device_lock_comp@1` | `unlock_trigger_at`, `unlocked_at`, `disbursed_minor`, `incident_date` | applies only if `incident_date ≥ 2027-01-01`; `due = trigger + 1 h`; `hours = ceil((unlocked − due)/1 h)`; `comp = min(hours × ₹250, disbursed)` | compensation | Trigger 10:00, unlocked 16:30 same day → 5.5 h → 6 h → **₹1,500** (rounding `ceil` config) |
| C-FIN-11 `fin.ni138_dates@1` | `return_memo_received_on`, `notice_received_on` | `notice_by = memo + 30 d`; `pay_by = notice_received + 15 d`; `coa = pay_by + 1 d`; `complaint_by = coa + 1 month` (day of cause of action excluded) | statutory dates (informational) | Memo 5 Jan 2027 → notice by **4 Feb 2027**; notice received 20 Jan → pay by **4 Feb 2027**; cause of action 5 Feb → complaint by **5 Mar 2027** |
| C-FIN-12 `fin.sarfaesi_timer@1` | `s13_2_served_on`, `objection_on`, `s13_4_measure_on`, `auction_notice_on` | `pay_window_end = served + 60 d`; `reply_due = objection + 15 d`; `s17_last = measure + 45 d`; `redemption_warning = auction_notice_on IS NOT NULL` | dates + warning | Served 1 Feb 2027 → **2 Apr 2027**; objection 1 Feb → reply by **16 Feb 2027**; measure 10 Apr → s.17 by **25 May 2027** |
| C-FIN-13 `fin.grievance_ladder@1` | `re_complaint_date`, `re_reply_date`, `io_applicable`, `rbios_covered` | `io_escalate_by = complaint + 20 d`; `re_final_by = complaint + 30 d`; `rbios_last = reply + 90 d` else `complaint + 120 d`; pre-1 Jul 2026 complaints → 2021 rule | dates | Complaint 3 Aug 2026 → IO by **23 Aug**; final by **2 Sep**; no reply → RB-IOS by **1 Dec 2026**; reply 25 Aug → by **23 Nov 2026** |
| C-FIN-14 `fin.mfi_foir@1` | annual household income, existing EMIs, proposed EMI | `eligible = income ≤ ₹3,00,000`; `cap = income/12 × 50%`; `breach = existing + proposed − cap` | eligibility, cap, breach | ₹2,40,000 → cap ₹10,000; ₹6,500 + ₹4,000 = ₹10,500 → **breach ₹500** (warning, not advice) |
| C-FIN-15 `fin.prepayment_check@1` | borrower type, purpose, rate type, RE layer, sanction/renewal date, amount | Decision table §3.2 `FIN.RET.HL` | `nil_charge_applies` y/n + reason | Individual, non-business, floating, sanctioned 15 Jan 2026 → **nil**; same sanctioned 15 Dec 2025 → "rule may not apply (legacy)" |
| C-FIN-16 `fin.ots_restructuring_flag@1` | schedule dates | `restructuring = last_payment − first_payment > 3 months`; cooling ≥ 12 m disclosure | flags | 3 instalments 1 Mar, 1 Apr, 1 May 2027 → **not** restructuring; 4th on 1 Jul 2027 → **restructuring** |
| C-FIN-17 `fin.payment_tat_comp@1` | rail, issue, `txn_datetime`, `reversed_on` | TAT table (config `rbi_tat_2019`, loaded verbatim from RBI/2019-20/67 annex **[VERIFY — open: load annex table]**); `comp = days_beyond_tat × ₹100` | due date, compensation | UPI P2P debited-not-credited 1 Mar 2027, TAT T+1 → due **2 Mar**; reversed 6 Mar → 4 days → **₹400** |
| C-FIN-18 `fin.colending_booking@1` | originator disbursal date, partner booking date | `ok = booking ≤ disbursal + 15 d` | ok / breach | Disbursal 1 Feb 2027, booking 20 Feb → **breach** (stays with originator per Directions) |
| C-FIN-19 `fin.card_closure_comp@1` | `closure_requested_on`, `closed_on` | `due = add_working_days(request, 7)`; `comp = max(0, closed − due) × ₹500` | compensation | Request Mon 1 Mar 2027 → due **10 Mar**; closed 15 Mar → **₹2,500** (flag `fin_card_closure_comp` OFF until OLQ-7 verified) |
| C-FIN-20 `fin.ots_portal_grid@1` | grid row, P, I, C, chosen plan | `floor_lump = P×(1−haircut) + I×(1−iw) + C×(1−pw)`; instalment floor per row; `within_grid = offer ≥ floor ∧ months ≤ max` | offers ≤ 3; within-grid flag | Grid PL DPD 91–180: haircut 10%, iw 100%, pw 100%; P ₹2,40,000, I ₹36,000, C ₹12,000 → lump floor **₹2,16,000**; borrower ₹2,20,000 → within grid; ₹2,00,000 → counter to lender queue |

---

## 13. Outputs, templates, enforcement and registration route

| Template | Label (copy-lint allowed) | Enforcement / route |
|---|---|---|
| TPL-FIN-S01 OTS / settlement terms | "Settlement Agreement under section 73 of the Arbitration and Conciliation Act, 1996, having the status of an arbitral award on agreed terms (section 74)" (Part III) or "Mediated Settlement Agreement (contract) under the Equator Mediation Rules" | s.74 → execution as a decree under s.36 (CPC O.XXI; where assets are — *Sundaram Finance v Abdul Samad* (2018) 3 SCC 622); MSA → suit on contract |
| TPL-FIN-S02 Consent award FIN clauses | "Arbitral award on agreed terms (section 30)" | s.36; s.34 window 3 months + 30 days (LR-ARB-016) |
| TPL-FIN-S03 Joint compounding application / withdrawal memo (s.138) | "Joint application for compounding under section 147 of the Negotiable Instruments Act, 1881 — prepared for filing by the parties" | Court decides (NN-24) |
| TPL-FIN-S04 Lok Adalat joint application + compromise memo | "Joint application for reference under section 20 of the Legal Services Authorities Act, 1987" | Lok Adalat award = deemed decree (s.21) |
| TPL-FIN-S05 DRT / court joint memo of compromise | "Joint memo of compromise for recording" | DRT/court order |
| TPL-FIN-S06 Guarantor release deed / contribution agreement | — | Contract; stamp per state |
| TPL-FIN-S07 Conduct undertaking (RE + agency) | — | Contract; breach → RB-IOS / civil remedy |
| TPL-FIN-L01–L07 Borrower letters (P08 FR-P08-19) + L08 gold release demand, L09 surplus refund demand, L10 document-release compensation claim, L11 CIC compensation claim, L12 card closure compensation claim | Self-help letters (free) — "Prepared by you using Equator's free template" | RE grievance ladder |
| TPL-FIN-R02 Non-commencement notice; R03 Closure report; R04 Record of pre-action steps | No reasons, no conduct comments | Costs/urgency arguments |
| TPL-FIN-SIG-RBIOS@2 | §4.7 | — |

Rules: GRO footer and "not a recovery agent" line on every lender-related output (LR-RBI-007); bureau clause library (PI-FIN-12) — CI to report within its next submission cycle, agreed status wording, ₹100/day framework reference, never deletion of accurate history; NOC within 15 days default; document release within 30 days (personal loans) / gold 7 working days; post-award interest clause in money awards (LR-ARB-015); severable operative paragraphs (LR-ARB-021). **Stamping (NN-09):** e-stamp by state of execution at signing via `ESTAMP_PORT`; payer per programme (lender default) or instrument rule. **Registration (NN-08):** any OTS involving transfer of immovable property (debt-asset swap), registered release/reconveyance deed or partition → physical execution + Sub-Registrar task (`core.registration_tasks`), never e-sign alone; return of deposited title deeds under an equitable mortgage is a compliance obligation, not a registration. **Publication (NN-26):** FIN settlements/awards published only with every party's consent, redacted (Appendix R §3). **Execution pack** (ANC.EXEC.PACK / FIN-L L6): award or s.74 settlement, BSA s.63(4) certificate, hash manifest, s.34-window status, asset-location court note.

---

## 14. Dashboards, KPIs and enterprise hooks

Extends P08 FR-P08-21/22 and P09 FR-P09-14–16. All KPIs are SQL views in `fin` over pinned data; no neutral win-rates or party-side tags (NN-16); "commenced" and "filed" denominators shown separately (S4 B5.7).

| KPI | Definition | Target (Y1) |
|---|---|---|
| Portal view rate | portal links viewed ÷ delivered | ≥ 50% |
| Portal resolution rate | signed settlements via portal ÷ viewed | report only (not targeted) |
| Counter turnaround | median lender decision time on counters | ≤ 7 days |
| Conciliation request rate from portal | conciliator requested ÷ viewed | report (fairness signal) |
| "Felt pressured" (post-case survey) | yes ÷ responses | ≤ 5% |
| Contact-conduct compliance | sends blocked by window/blackout ÷ attempted; zero sends outside window | 100% compliance |
| Clean-exit rate | settled cases with paid + NOC + documents/collateral + bureau evidenced | 100% of performed |
| Compensation-clock breaches | gold/doc/CIC/card clocks breached by RE after settlement | report per lender |
| Defensibility | FIN arbitrations with Score ≥ 85 | ≥ 95%; awards set aside on appointment grounds = 0 |
| Signposting accuracy | audited sample correct forum | ≥ 98% |
| RB-IOS signposting delivered before closure | covered-RE cases | 100% |

Events (new; register in Appendix F §F.9): `equator.fin.programme.activated.v1` · `equator.fin.policy_grid.approved.v1` · `equator.fin.ots_portal.link_issued.v1` · `equator.fin.ots_portal.viewed.v1` · `equator.fin.ots_portal.offer_accepted.v1` · `equator.fin.ots_portal.counter_submitted.v1` · `equator.fin.ots_portal.counter_decided.v1` · `equator.fin.compounding_pack.generated.v1` · `equator.fin.sarfaesi.redemption_warning.v1` · `equator.fin.gold.release_overdue.v1` · `equator.fin.bureau.rectification_overdue.v1` · `equator.fin.conduct.safety_signposted.v1` (no narrative in payload). Webhooks to lenders exclude vulnerability flags, affordability raw data and caucus content.

---

## 15. Competitor notes and Equator differentiation

| Competitor | FIN position (evidence) | Equator response |
|---|---|---|
| Jupitice | BFSI portfolios; ODR + e-stamp/e-sign (Jul 2026) + legal-notice management; 1.16 lakh cases resolved (advertorial); opaque take-rate (R1 §2.1) | Published FIN-R/FIN-L fee cards; D2 closed settlement loop; D1 defensibility |
| Presolv360 | Lender ODR; Series A USD 4.7 mn; named in Bombay HC notice (*Radiance Galore*, Jul 2025); mediation ₹4,500 + ₹5,000/session; arbitration from ₹5,000 (S3 C2) | §4.6 gates + IEP; borrower ₹0 under programmes |
| Sama | ICICI/Bajaj Markets; 2 crore+ cases (Lok Adalat-heavy); arbitration ≤ 180 days; unpaid settlement fee bars future matters (S3 C2) | Mid-market NBFC/co-lending focus; no punitive fee terms (NN-29) |
| CORD | Rules 2.0 (4 Sep 2026): AI-governance chapter, opt-in appeal, Appointments Council; banking/NBFC category | Match on rules (Equator Rules + AI Governance Rule + appeal tier); win on lender tooling (portal, bulk, NN-12 engine) |
| Webnyay | Grievance redressal SaaS for BFSI | D5 GRM `FIN_RBI` with RB-IOS 2026/IO 2026 clocks |
| DAC / MCCI / CNICA | Subsidised banking schedules; named-institution clauses upheld (*Sundaram Finance*, Raj HC 2026) | Clause-at-sanction naming Equator ex ante; verification seal page |
| AdresNow; Credgenics; Rezolv | Lender-triggered ODR / collections tech | Partner via API rail; never sell "bulk awards" |
| Sahamati ODR (AA network) | Empanelment closed (deadline 15 Apr 2025), no next round; name "Vikalp" unconfirmed | Build AA evidence (D6) now; request next-round slot |

Gap no competitor publishes: statutory-ladder-aware FIN intake (IO/RB-IOS clocks), free-route-first screens, and a borrower self-serve OTS portal with neutral hosting, real offer expiry and an equal-prominence "ask for a conciliator" option.

---

## 16. Data-model extensions (schema `fin`; tenant + case RLS per Appendix F §F.8)

Existing and kept: `fin.loan_accounts`, `fin.ots_proposals` (Appendix F); `fin.case_ext`, `fin.parallel_proceedings`, `fin.waiver_instruments`, `fin.affordability_statements`, `fin.calc_runs`, `fin.aa_fi_payloads` (P08/P09). Changes and new tables (ADR required; register in Appendix F):

```sql
-- Enum alignment (resolves P08 vs Appendix F drift): lender_type adds 'financial_institution','sfb','payments_bank','rrb','ucb','gold_loan_nbfc','non_bank_ppi','aifi'
CREATE TYPE fin.l2_code AS ENUM ('FIN.RET.PL','FIN.RET.CC','FIN.RET.DL','FIN.RET.GL','FIN.RET.VL','FIN.RET.HL','FIN.RET.EL','FIN.RET.MF','FIN.RET.PP',
 'FIN.BUS.MS','FIN.BUS.CL','FIN.BUS.CB','FIN.BUS.GT','FIN.CND.RC','FIN.CND.CH','FIN.CND.CR','FIN.PAY.TX','FIN.PAY.CB','FIN.PAY.MP',
 'FIN.SET.OT','FIN.SET.NI','FIN.SET.SF','FIN.SET.DR','FIN.SIG.EN','FIN.SIG.FR','FIN.SIG.IL','FIN.SIG.CR');
ALTER TABLE fin.case_ext ADD COLUMN primary_l2 fin.l2_code NOT NULL, ADD COLUMN secondary_l2 fin.l2_code[] NOT NULL DEFAULT '{}',
  ADD COLUMN rbios_covered boolean, ADD COLUMN io_applicable boolean, ADD COLUMN limitation_estimate_date date,
  ADD COLUMN unilateral_clause_detected boolean NOT NULL DEFAULT false, ADD COLUMN programme_id uuid;

CREATE TABLE fin.lender_programmes (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, lender_org_id uuid NOT NULL REFERENCES core.organisations(id),
  re_type text NOT NULL, rbios_covered boolean NOT NULL, io_applicable boolean NOT NULL, claim_ceiling_minor bigint NOT NULL CHECK (claim_ceiling_minor <= 500000000),   -- ₹50,00,000 FIN-L ceiling
  stages text[] NOT NULL CHECK (stages <@ ARRAY['L1','L2','L3','L4','L5','L6']), fee_schedule_id uuid NOT NULL, dpa_id uuid NOT NULL,
  number_authorisation_ids uuid[] NOT NULL, gro_profiles jsonb NOT NULL, status text NOT NULL CHECK (status IN ('draft','in_review','active','suspended','ended')),
  approved_by uuid, CHECK (status <> 'active' OR approved_by IS NOT NULL));
CREATE TABLE fin.ots_policy_grids (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, programme_id uuid NOT NULL REFERENCES fin.lender_programmes(id),
  version int NOT NULL, policy_ref text NOT NULL, approver_role text NOT NULL, approver_above_sanctioner_attested boolean NOT NULL CHECK (approver_above_sanctioner_attested),
  rows jsonb NOT NULL,              -- validated by JSON Schema eqr.fin.policy_grid_row.v1 (cooling_period_months >= 12; offer_validity_days >= 14; exclude wilful/fraud)
  effective_from date NOT NULL, effective_to date, maker_id uuid NOT NULL, checker_id uuid, state text NOT NULL
  CHECK (state IN ('draft','submitted','equator_lint_passed','lender_approved','active','superseded','withdrawn')),
  CHECK (checker_id IS NULL OR checker_id <> maker_id), UNIQUE (programme_id, version));
CREATE TABLE fin.ots_portal_links (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  loan_account_id uuid NOT NULL REFERENCES fin.loan_accounts(id), policy_grid_id uuid NOT NULL REFERENCES fin.ots_policy_grids(id),
  token_hash char(64) NOT NULL UNIQUE, offers jsonb NOT NULL, expires_at timestamptz NOT NULL, state text NOT NULL
  CHECK (state IN ('issued','identity_verified','viewed','accepted','counter_submitted','counter_accepted','counter_declined','disputed','conciliator_requested','not_now','expired','revoked')),
  CHECK (expires_at >= created_at + interval '14 days'), created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE fin.ots_counters (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, link_id uuid NOT NULL REFERENCES fin.ots_portal_links(id),
  amount_minor bigint NOT NULL CHECK (amount_minor > 0), schedule jsonb NOT NULL, within_grid boolean NOT NULL, decided_by uuid, decision text
  CHECK (decision IS NULL OR decision IN ('accepted','declined')), decided_at timestamptz, due_at timestamptz NOT NULL);
CREATE TABLE fin.cheques (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  cheque_no_masked text NOT NULL, cheque_date date NOT NULL, amount_minor bigint NOT NULL, return_reason text NOT NULL, return_memo_received_on date NOT NULL,
  notice_received_on date, complaint_cnr text, court text, stage text NOT NULL, compounding_slab_pct numeric(4,2));
CREATE TABLE fin.sarfaesi_events (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  stage text NOT NULL, event_date date NOT NULL, document_id uuid, UNIQUE (case_id, stage));
CREATE TABLE fin.gold_pledges (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  pledge_date date NOT NULL, gross_weight_mg int NOT NULL, net_weight_mg int NOT NULL CHECK (net_weight_mg <= gross_weight_mg), purity_carat smallint,
  full_repayment_date date, released_on date, auction_date date, reserve_price_minor bigint, sale_price_minor bigint, surplus_claimed_minor bigint,
  legacy_regime boolean GENERATED ALWAYS AS (pledge_date < DATE '2026-04-01') STORED);
CREATE TABLE fin.bureau_disputes (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  cic text NOT NULL CHECK (cic IN ('cibil','experian','equifax','crif_highmark')), dispute_id text, raised_on date NOT NULL, ci_sent_on date, resolved_on date,
  error_type text NOT NULL, agreed_status text CHECK (agreed_status IN ('settled','closed','as_per_policy')));
CREATE TABLE fin.payment_disputes (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  rail text NOT NULL, txn_ref_masked text NOT NULL, txn_at timestamptz NOT NULL, amount_minor bigint NOT NULL, issue text NOT NULL, bank_complaint_id text, tat_due_at timestamptz);
CREATE TABLE fin.conduct_incidents (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  incident_at timestamptz NOT NULL, conduct_type text NOT NULL, agency_name text, caller_hmac char(64), evidence_document_ids uuid[],
  regime text GENERATED ALWAYS AS (CASE WHEN incident_at >= TIMESTAMPTZ '2027-01-01 00:00+05:30' THEN 'rbc_2026' ELSE 'legacy' END) STORED);
  -- danger/safety narrative never stored here: safety_sealed via opaque case_token (NN-07)
CREATE TABLE fin.guarantees (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  guarantor_party_id uuid NOT NULL, guarantee_type text NOT NULL, cap_minor bigint, invoked_on date, pg_insolvency_filed_on date);
CREATE TABLE fin.rbios_acknowledgements (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  party_id uuid NOT NULL, rbios_last_date date, choice text NOT NULL CHECK (choice IN ('proceed_with_arbitration','use_rbios_first','mediate_or_conciliate_only')),
  esign_request_id uuid NOT NULL, signed_at timestamptz NOT NULL, script_version text NOT NULL);
-- Guard: core.proceedings insert with mechanism='arbitration' on FIN requires fin.rbios_acknowledgements row when fin.case_ext.rbios_covered
-- and pending_forum contains 'rbios' or the borrower ticked "considering RB-IOS" → else SIGNPOSTING_REQUIRED (rule FIN_RBIOS_ACK_REQUIRED).
-- Guard: core.settlements on a FIN case rejects terms with bureau action 'delete_accurate_history' → SETTLEMENT_LINT_FAILED (rule FIN_BUREAU_DELETION_TERM).
```

New error sub-codes (Appendix F §F.10.2 mapping): `FIN_RE_NOT_IDENTIFIED`, `IBC_MORATORIUM` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `FIN_COLENDING_PARTNER_MISSING` → `CLOSURE_BLOCKED`; `FIN_RBIOS_ACK_REQUIRED` → `SIGNPOSTING_REQUIRED`; `FIN_BUREAU_DELETION_TERM`, `FIN_PENAL_CAPITALISED` → `SETTLEMENT_LINT_FAILED`; `FIN_CARD_PAN_ENTERED` → `VALIDATION_FAILED`; `FIN_POLICY_GRID_INVALID` → `RULESET_GUARDRAIL_VIOLATION`; `FIN_OTS_LINK_EXPIRED` → `OFFER_EXPIRED`; `ROW_*` FIN codes → `BULK_ROW_INVALID`.

New clocks (Appendix A §6.3): `gold_release_7wd` (contractual-regulatory, AP-S, B-CRIT compliance), `doc_release_30d` (LR-RBI-024), `bureau_update_30d` (LR-RBI-013), `sarfaesi_pay_60d`, `sarfaesi_reply_15d`, `sarfaesi_s17_45d` (informational), `ots_offer_validity` (≥ 14 d), `ots_counter_decision_7d` (service), `fin_safety_review` (2 working hours).

---

## 17. Acceptance tests (Gherkin; `tests/acceptance/fin/`)

```gherkin
Feature: FIN vertical v2

Scenario: NN-24_fin_ni138_offence_never_arbitrated
  Given a FIN.SET.NI case at stage "summons"
  When the complainant requests arbitration of the cheque offence
  Then the API returns 422 CASE_NOT_ARBITRABLE with rule "NN06_NON_ARBITRABLE"
  And the compounding pack shows "prepared for filing by the parties; the court decides"

Scenario: NN-24_fin_ni138_no_conviction_threat
  Given a draft settlement message containing "you will be convicted"
  When the neutral submits it
  Then the qa lint blocks it and VG-FIN-03 is logged

Scenario: NN-03_fin_post_default_conferral_rejected
  Given a loan agreement without an Equator clause and a lender letter dated after default appointing Equator
  When the lender files for arbitration
  Then the API returns 403 APPOINTMENT_LENDER_TRIGGER_BLOCKED
  And mediation and conciliation remain offered

Scenario: NN-03_fin_waiver_predating_dispute_rejected
  Given dispute_arose_on 2027-02-01 and an s.12(5) waiver signed 2027-01-15
  When the tribunal tries to issue the award
  Then 422 S12_5_WAIVER_PREDATES_DISPUTE is returned

Scenario: LR-ARB-020_bank_25L_no_arbitration
  Given lender_type "scheduled_commercial_bank" and claim ₹25,00,000
  When arbitration is requested
  Then 422 CASE_NOT_ARBITRABLE with rule "FIN_DRT_EXCLUSIVE" and DRT and Lok Adalat are signposted

Scenario: NN-20_fin_rbios_last_date_shown
  Given an NBFC with rbios_covered = true and a complaint to the RE on 2026-08-03 with no reply
  When the Explorer outcome is shown
  Then the RB-IOS block shows last date "01 Dec 2026" before any fee
  And a signposting event with forum "RBIOS" is written

Scenario: LR-RBI-003_arbitration_needs_rbios_ack
  Given a borrower who ticked "considering RBI Ombudsman"
  When she opts into arbitration without F-FIN-26
  Then 409 SIGNPOSTING_REQUIRED with rule "FIN_RBIOS_ACK_REQUIRED"

Scenario: NN-12_fin_contact_window_and_blackout
  Given a borrower in Asia/Kolkata with a bereavement blackout until 2027-03-10
  When a reminder is scheduled at 19:05 on 2027-03-12 and another at 10:00 on 2027-03-05
  Then the first is rejected with CONTACT_OUTSIDE_WINDOW and the second with CONTACT_BLACKOUT_ACTIVE

Scenario: NN-12_fin_gro_footer_required
  Given a lender-initiated invitation template without GRO details
  When it is published
  Then 422 GRO_DETAILS_MISSING

Scenario: Safety_trigger_signposts_before_anything
  Given Explorer answer FQ-002 = "Yes"
  When the outcome is computed
  Then 112, 1930 and 181 are shown, lender-side contact is blacked out, and a safeguarding task due in 2 working hours exists

Scenario: Illegal_app_not_convened
  Given loan_product "app_bnpl" and no RE identified after lookup
  When the borrower submits
  Then outcome is OC-FIN-SIGNPOST-ILLEGAL-APP and no invitation is generated

Scenario: Sarfaesi_redemption_warning
  Given sarfaesi_stage "auction_notice_published" on 2027-04-20
  Then a red banner states that the right to redeem may be lost and copy never says Equator can stop the auction
  And event equator.fin.sarfaesi.redemption_warning.v1 is emitted

Scenario: IBC_moratorium_holds_corporate_debtor_only
  Given a corporate borrower in CIRP admitted and a personal guarantor with no s.94/95 filing
  Then the case against the corporate debtor is on_hold with IBC_MORATORIUM and the guarantor track proceeds

Scenario: MFI_shuttle_and_foir
  Given FIN.RET.MF with household income ₹2,40,000, existing EMIs ₹6,500 and proposed ₹4,000
  Then blind-bid is disabled, sessions are shuttle-only, and the FOIR warning shows breach ₹500

Scenario: NN-13_settlement_never_to_equator_merchant
  Given an accepted OTS of ₹2,20,000
  When payment_rail "equator_merchant" is posted
  Then 422 PAYMENTS_SETTLEMENT_ON_MERCHANT_FORBIDDEN

Scenario: NN-29_ots_portal_no_dark_patterns
  Given an OTS portal link
  Then accept and decline controls have equal prominence, no countdown other than expires_at is shown, and expires_at ≥ issued + 14 days

Scenario Outline: OTS_portal_within_grid_vs_counter
  Given an active policy grid with lump-sum floor ₹2,16,000 and flag fin.ots_portal.auto_accept ON
  When the borrower submits a lump-sum figure of <amount>
  Then the result is <result>

  Examples:
    | amount    | result                                                                 |
    | ₹2,20,000 | settlement letter generated carrying policy_grid_version_id            |
    | ₹2,00,000 | counter in the lender approver queue with due_at = submitted_at + 7 d  |

Scenario: Bureau_deletion_term_blocked
  Given a settlement term "delete all adverse history"
  Then 422 SETTLEMENT_LINT_FAILED with rule "FIN_BUREAU_DELETION_TERM"

Scenario: Penal_charges_never_capitalised
  Given a claim head adding penal charges into principal
  Then 422 SETTLEMENT_LINT_FAILED with rule "FIN_PENAL_CAPITALISED"

Scenario: Gold_release_delay_golden_vector
  Given full repayment on 2027-02-01 and release on 2027-02-16
  Then C-FIN-06 returns due 2027-02-10 and compensation ₹30,000 with indicative = true

Scenario: NN-01_no_valuation_by_ai
  Given a borrower asks the assistant "How much will the bank accept?"
  Then the assistant refuses with VG-FIN-02 and offers the deterministic OTS calculator labelled indicative

Scenario: NN-18_borrower_never_pays_success_fee
  Given a FIN-L programme case that settles
  Then the borrower invoice total is ₹0 and the neutral component equals the not-settled component
```

---

## 18. Open items and counsel questions

| # | Item | Owner | Effect until closed |
|---|---|---|---|
| Q-01 | Is an ODR institution's procedural or offer-relay call a "recovery-related communication" under RBI/2026-27/230? (LR-RBI-023; S3 OLQ-5) | Counsel | NN-12 applied as policy to all FIN contacts |
| Q-02 | Does hosting a lender's OTS portal make Equator an outsourced service provider for "recovery" (RBI outsourcing of financial services directions, current consolidated text)? Which annex clauses are needed? | Counsel | Outsourcing annex in F-FIN-27 mandatory |
| Q-03 | Does a pre-approved OTS Policy Grid, approved by an authority one level above the sanctioning authority, satisfy para 16(5) of the Resolution of Stressed Assets Directions 2025 for each account accepted through the portal? | Counsel | Flag `fin.ots_portal.auto_accept` OFF → every acceptance goes to lender approver queue |
| Q-04 | s.31A cost-shifting against borrowers in standard-form consumer loans (LR-RBI-025) | Counsel | Equator fees never shifted |
| Q-05 | Can a settlement require a CI to report "closed" instead of "settled" (CICRA accuracy duty)? (S3 OLQ-11) | Counsel | Term allowed only as "as agreed by the CI" with accuracy caveat |
| Q-06 | Gold & Silver Collateral, Co-Lending and Pre-payment Directions 2025: instrument numbers, paragraphs, gold reference price, legacy renewals (S3 OLQ-6, OLQ-10) | Legal research | LR-RBI-026/027/028 `UNVERIFIED`; calculators C-FIN-06/07/15/18 behind flags `fin_gold_rules`, `fin_colending_rules`, `fin_prepayment_rules` (warning-only ON) |
| Q-07 | Credit Card Directions 2022 current location; ₹500/day and 30-day rules (S3 OLQ-7) | Legal research | C-FIN-19 flag OFF |
| Q-08 | RBI/2019-20/67 TAT annex to load verbatim | Legal research | C-FIN-17 flag OFF |
| Q-09 | HFC borrowers: grievance escalation route given RB-IOS 2026 excludes HFCs | Legal research | Signpost text "NHB complaint route" hidden until verified |
| Q-10 | Limitation Article mapping per loan structure (Arts. 19, 21, 37, 55) | Counsel | `limitation_estimate_date` shown to CM only |
| Q-11 | SARFAESI NBFC notification (≥ ₹100 crore assets; ≥ ₹20 lakh debts) and RDB s.2(h)(ii) notified FI list (LR-ARB-020) | Legal research | NBFCs treated as arbitrable unless notified FI |
| Q-12 | Lok Adalat recording of Equator-negotiated terms: DLSA practice and stamp position (S4 Q-C8) | Counsel | Pack offered with "DLSA may require appearance" copy |
| Q-13 | Standstill/tolling agreement validity (S4 Q-C1) | Counsel | `fin.standstill_template` OFF |
| Q-14 | Does a pending Equator conciliation trigger RB-IOS non-maintainability ("pending before arbitrator")? (S4 Q-C9) | Counsel | Informed-choice text covers arbitration and mentions conciliation as "may" |
| Q-15 | PM-Vidyalaxmi/CSIS limits and grievance owners (S3 OLQ-14); State Money-lenders Act cap table | Legal research | Informational links only |

Conflicts recorded for ADR: **C-01** negotiation time-box P08 14 d vs Appendix A 21 d → Appendix A (21 d). **C-02** P08 FR-P08-13 offers `expert_determination` for co-lending; master §5.2 blocks it in FIN → blocked; A&C s.26 tribunal expert used instead. **C-03** `lender_type` enum differs between P08 (`financial_institution`) and Appendix F (absent) → Appendix F enum extended (§16). **C-04** P08 taxonomy (issue-based) replaced by L1/L2 with `legacy_ref` (§2.3). **C-05** RES_A2 cites RBI/2023-24/102 for both the IT-outsourcing Master Direction (10 Apr 2023) and the penal-charges deferral (29 Dec 2023); one number is wrong — cite instruments by title and date until verified.
