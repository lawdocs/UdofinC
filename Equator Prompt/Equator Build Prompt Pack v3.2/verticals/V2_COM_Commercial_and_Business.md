# V2 — Commercial & Business (COM) — Vertical Specification

> Binding for P08b. Read with master, 02, Appendices A, B, F, G, K, L, M.
> Version 2.0 · law stated as at 21 October 2026 · owner: Head of Legal (COM pack) · status: ready for build, subject to the open items in §18.

---

## 0. Scope and how to use

**What this file is.** The complete product, legal and data specification of the `COM` vertical: every Level-1 (L1) category and Level-2 (L2) subtype, the law that governs each, who may use which mechanism, the Dispute Explorer questions, every intake and submission form per mechanism with full dropdown values, the step-by-step modus operandi, the pre-litigation journey, document checklists, practical difficulties, integrations, calculators with golden vectors, outputs and enforcement routes, KPIs, competitor notes, the `com` schema extensions and acceptance tests.

**How the coding agent uses it.**
1. Build P08b from this file. P08 §4.2 (FR-P08-24 to FR-P08-34) remains valid; where this file is more specific or newer (taxonomy, routing rows, forms, calculators, clocks, tables), this file governs, subject to the master §15 precedence order (master → Appendix G → B → F → A). Every reconciliation is recorded in `docs/adr/` (ADR "COM v2 reconciliation").
2. Every legal threshold, period, list and rate below is **data** in the Legal Rules Register (Appendix G). Existing rule IDs are cited (`LR-ARB-*`, `LR-MED-*`, `LR-CONC-*`, `LR-MSME-*`, `LR-CONS-*`, `LR-RBI-017/018/019`, `LR-STAMP-*`). New rules required by this vertical are listed in §3.12 with proposed IDs; they are seeded with `verification = VERIFY_PENDING` where marked and obey the fail-safe principle (Appendix G §G.1): protective rules may activate, permissive rules may not.
3. Taxonomy, ladders, forms, dropdowns, templates and calculators are seeded into the `packages/verticals/com/` pack (FR-P08-01) and pinned to each case at filing (NN-21).
4. Feature flags introduced here default **OFF** unless stated and use the dot style of the master (`com.<name>`). Legacy underscore names in research notes (`com_ciirp`, `com_ibbi_reg2b`, `com_msefc_referral_msp`, `com_s12a_private_msp`) map to the dot names in §16.5; `com_s12a_private_msp` is superseded by the master flag `com.s12a_equator_authorised`.

**What COM is not.**
- Not a court, tribunal, NCLT, RERA Authority, MSEFC or Legal Services Authority, and never presented as one (NN-17, D2-15).
- Never decides insolvency, winding up, oppression reliefs, IP grant/validity in rem, competition matters, tax, or any other in-rem or statutory-forum matter (NN-06, D2-02, LR-ARB-019). It mediates the commercial reality around them and signposts the statutory step.
- Never conducts criminal proceedings or mediates an offence (NN-24). Cheque-dishonour work is limited to the civil money dispute and the compounding papers; the court alone compounds.
- Never conducts mandatory pre-institution mediation under Commercial Courts Act s.12A while `com.s12a_equator_authorised` is OFF (M-06, LR-MED-014, LR-MED-019).
- Cross-border matters (any party with a place of business, nationality or habitual residence outside India, or a foreign seat) are created in `INT` (LR-INT-001; P08 FR-P08-24 row `com.cross_border`).

**Reading key.** Status tags on legal points: **[IN FORCE]**, **[NOT IN FORCE]**, **[DRAFT]**, **[POLICY]** (Equator institutional rule), **[VERIFY]** tag (with owner and reason). Money in ₹ with Indian grouping; integer minor units in storage. "Explorer" = Dispute Explorer v2 (Appendix K). "CM" = case manager.

---

## 1. Vertical overview

### 1.1 Who it serves

| Segment | Typical parties | Typical value | Why they come |
|---|---|---|---|
| Mid-market B2B | Manufacturers, distributors, franchisors/franchisees, C&F agents, logistics firms, IT vendors and clients | ₹5 lakh–₹25 crore | Faster than Commercial Court; relationship-preserving; enforceable outputs (s.74 conciliation settlement, consent award, award) |
| MSMEs (Udyam micro/small) | Supplier MSE vs buyer (company, PSU, government) | ₹50,000–₹5 crore | Pre-MSEFC settlement with full s.16 interest computed; MSME ODR export pack; future Council-referred track |
| Construction and infrastructure | EPC contractors, sub-contractors, developers, consultants, CPSEs, Ministries, ULBs | ₹1 crore–₹500 crore | Claim-wise negotiation; co-mediation with engineers; HLC-ready settlement proposals (DoE OM 3 Jun 2024); institutional arbitration |
| Technology and IP | SaaS providers, system integrators, licensors/licensees | ₹10 lakh–₹100 crore | Confidentiality rings, technical co-mediator, expert determination of SLA metrics |
| Real estate (B2B and homebuyer) | Developers, landowners (JDA), commercial landlords/tenants, brokers, allottees | ₹5 lakh–₹50 crore | Structured possession/refund settlements; group mediation; RERA-recordable settlement memos |
| Firms, LLPs, companies, founders | Partners, LLP partners, shareholders, JV partners, founders, investors, family businesses | ₹10 lakh–₹1,000 crore | Exit/valuation mediation; arbitration of SHA/JV contract layer; s.442 panel credentials for individual neutrals |
| Insolvency-adjacent | Operational and financial creditors (non-bank), corporate debtors, promoters, personal guarantors, resolution applicants | ₹10 lakh–₹500 crore | IBC Settlement Desk before admission; s.12A IBC window support; pre-pack facilitation; liquidation-stage compromise negotiation |
| Cheque dishonour (commercial) | Payee businesses, drawer businesses | ₹50,000–₹5 crore | Civil settlement inside the NI Act notice window or during trial; compounding papers |

### 1.2 Value proposition (product copy anchors; copy-lint applies)
- "Resolve business disputes online — fairly, quickly and enforceably." Never "court", "decree", "judge" for Equator (master §1).
- Strongest lawful outputs today, in order: s.73 settlement with s.74 award status (Part III conciliation) → consent award under A&C s.30 → arbitral award → contractual settlement agreement (LR-MED-021, LR-CONC-001).
- Honest signposting with last dates to act: Legal Services Authority (s.12A PIMS), MSEFC/MSME ODR portal, NCLT, RERA, Consumer Commission, CCI, IP Office/High Court, DRT, Magistrate (NI Act), High-Level Committee of the government entity (NN-20).

### 1.3 Mechanisms allowed (master §5.2, COM column)

| Mechanism | COM default | Limits in this vertical |
|---|---|---|
| Negotiation (assisted, unassisted, blind-bid) | ✔ | Blind-bid only for liquidated money claims; never for IBC matters after admission (CoC must vote) |
| Conciliation (A&C Part III) | ✔ — **default pre-suit recommendation where respondent is a company and an enforceable outcome is wanted** (S4 PL-02) | s.62 written invitation/acceptance; s.80 non-identity default |
| Mediation (contractual mode) | ✔ | Statutory mode behind `mediation_statutory_mode` (NN-05); s.12A PIMS assistance only (M-06) |
| Arbitration | ✔ | Arbitrable heads only (LR-ARB-019); valid s.7 agreement or post-dispute submission agreement (`COM_NO_ARB_AGREEMENT`); never IBC in rem, oppression reliefs, IP grant, rent-control eviction, consumer election, bank/FI ≥ ₹20 lakh (LR-ARB-020); DoE gating for government ≥ ₹10 crore (§4) |
| Med-arb / arb-med / arb-med-arb | ✔ | Master §5.3: different neutral default; sealed award for arb-med; AMA 8-week window |
| Expert determination | ✔ | Valuation, accounts, measurement, SLA metrics, royalties; contractual, not an award |
| Emergency arbitrator | ✔ (India seat) | Equator Rules Sch. 1; s.17 treatment (LR-ARB-025) |
| Expedited / documents-only (s.29B) | ✔ | Expedited by Rules (≤ ₹3 crore placeholder); s.29B only by written agreement (LR-ARB-012) |
| Grievance (GRM) | — | Not in COM (listed-company investor GRM is P09 SEBI variant) |
| POSH inquiry | — | Never |
| Signposting | ✔ | Mandatory where the decision table says so |

### 1.4 Status of key laws (21 October 2026)

| Instrument | Status | Effect on COM |
|---|---|---|
| Arbitration and Conciliation Act 1996 (as amended 2015, 2019, 2021) | [IN FORCE] | Arbitration, Part III conciliation, s.29A/29B clocks, s.12(5), s.17, s.42A |
| Draft A&C (Amendment) Bill 2024 (s.9A statutory EA; s.34A appellate tribunal) | [DRAFT] — not introduced as of 20 Oct 2026 (LR-ARB-026) | EA stays contractual; appeal tier contractual (*Centrotrade* (2017) 2 SCC 228) |
| Mediation Act 2023 | Partially in force: ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 (S.O. 4384(E), 9 Oct 2023; corrigendum S.O. 4506(E), 13 Oct 2023); MCI established S.O. 4781(E), 27 Aug 2026; ss.2, 4–25, 27–30, 39–44, 48–49, 55, 58–65 **not in force** | Contractual mode only; Ninth Schedule (s.64) substituting CCA s.12A not notified; Eighth Schedule (s.63) amending Companies Act not notified; ss.48–49 (government) not notified |
| Commercial Courts Act 2015 s.12A + PIMS Rules 2018 (G.S.R. 606(E), 3 Jul 2018) | [IN FORCE] | Mandatory PIMS through DLSA/SLSA only (LR-MED-013/014/018) |
| IBC 2016 as amended by **IBC (Amendment) Act 2026 (Act 6 of 2026)**, assent 6 Apr 2026; most provisions in force **26 May 2026** (S.O. 2625(E), 22 May 2026) | [IN FORCE] except Ch. IV-A CIIRP (ss.58A–58K), group insolvency and s.240C cross-border [NOT IN FORCE] | New s.12A withdrawal window; s.7(5) 14-day admission; liquidation 180 + 90 days; voluntary liquidation ≤ 1 year with withdrawal route; frivolous-filing penalty; PPIRP threshold 51% [Verified 22 Oct 2026: Act 6 of 2026 s.4(b) (s.7(5)), s.8 (s.12A), s.33 (s.54), s.41 (s.59), ss.44/58 (ss.64A/183A), s.34(a)(iii) and (b) (s.54A); Gazette] |
| IBBI pre-s.9 mediation (Discussion Paper, ≈4 Nov 2024, proposed CIRP Reg. 2BA; comments closed 24 Nov 2024) | [DRAFT] — not notified as of 22 Oct 2026; REG152 (1 Jun 2026) instead substituted Reg 2B (OC evidence) [Watch: recheck IBBI regulations quarterly] | Private pre-s.9 mediation only; flag `com.ibbi_reg2b` OFF |
| Companies Act 2013 ss.241–246, 230–232, 271, 442 + Companies (Mediation and Conciliation) Rules 2016 | [IN FORCE] | NCLT reliefs signposted; s.442 panel is individual-only |
| LLP Act 2008 (First Schedule para 14 default arbitration) | [IN FORCE] | LLP partner disputes default to arbitration absent contrary agreement |
| Indian Partnership Act 1932 (s.69) | [IN FORCE] | Unregistered firm may still arbitrate (*Umesh Goel* (2016) 11 SCC 313) |
| RERA 2016 (ss.31, 32(g), 71, 79, 88) | [IN FORCE] | Homebuyer signposting; MahaRERA conciliation; Equator cannot self-designate as s.32(g) forum |
| MSMED Act 2006 ss.15–19 | [IN FORCE] (unamended s.18 treated as operative [Corrected 22 Oct 2026: original s.18 operative until Mediation Act s.62 (Seventh Schedule) and MSMED (Amendment) Act 2026 s.8 both commence; 15 Dec 2026 applies only to Amendment Act s.12 (new s.21, Council composition)]) | MSEFC route; s.16 interest at 3 × Bank Rate (5.75% from 7 Oct 2026 → 17.25% p.a.) |
| **MSMED (Amendment) Act 2026** | Passed RS 3 Aug 2026, LS 7 Aug 2026; S.O. 5575(E), 12 Oct 2026: Amendment Act ss.2–7, 11, 13–17 from 15 Oct 2026; s.12 from 15 Dec 2026 [Corrected 22 Oct 2026: Act 16 of 2026, assent 13 Aug 2026; s.8 amends s.18 as substituted by Mediation Act s.62 + Seventh Schedule; s.9 = s.18A, s.10 = s.19, s.11 = s.20, s.12 = s.21; ss.8–10 not commenced] | Council referral to a "mediation service provider" / "ADR service provider" behind flag `com.msefc_referral_msp` OFF |
| DoE OM "Guidelines for Arbitration and Mediation in Contracts of Domestic Public Procurement", 3 Jun 2024 | [IN FORCE] (administrative guidance) | Government counterparties: arbitration by norm only < ₹10 crore dispute value; HLC route |
| NI Act 1881 ss.138, 142, 143A, 147, 148; *Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158 | [IN FORCE] | Compounding cost slabs 0/5/7.5/10% (LR-RBI-018) |
| Competition Act 2002; CCI (Settlement) and (Commitment) Regulations 2024 | [IN FORCE] | Signpost only |
| Stamp law (state of execution); *URC Construction v AAI*, Del HC, 1 Sep 2026 | [IN FORCE] | Awards and settlements stamped at signing (NN-09, LR-STAMP-001/002) |
| Singapore Convention | India signed 7 Aug 2019, not ratified | Not relevant domestically; INT only |

---

## 2. Subtype taxonomy

### 2.1 Code conventions
- L1 code: `com.<l1>` (lowercase, matches `core.dispute_types.code` pattern of FR-P08-02). Display label shown in admin as `COM.<L1>`.
- L2 code: `com.<l1>.<l2>` held in `core.dispute_types.sub_types[]` and in `com.subtype_catalog` (§16).
- Value band = typical claim range used for neutral-band defaults and fee examples; not a limit.
- Ladder codes are defined in §2.3. "Neg / Med / Arb" columns: ✔ permitted · ✔* permitted with conditions (see notes) · ✖ blocked (HB) · S signpost-only.
- Mediable means contractual mediation or Part III conciliation is permitted on the commercial layer; it never binds a statutory forum.

### 2.2 Taxonomy table

| L1 code | L2 code | Name | Typical parties | Value band | Default ladder | Neg | Med | Arb | Signpost forum | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `com.b2b` | `supply_goods` | Sale/supply of goods — price, short payment, rejection | Seller, buyer | ₹1 lakh–₹25 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | Commercial Court (s.12A first); MSEFC if MSE supplier | If supplier Udyam micro/small → R-COM-09 precedence |
| `com.b2b` | `services` | Services contracts (non-IT) | Service provider, client | ₹1 lakh–₹10 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | as above | |
| `com.b2b` | `distribution` | Distribution/dealership — territory, targets, termination | Principal, distributor | ₹5 lakh–₹25 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | CCI if RPM/exclusive dealing alleged by dominant firm | SRA s.14(d): determinable contracts not specifically enforceable |
| `com.b2b` | `franchise` | Franchise — fees, royalty, brand use, exit | Franchisor, franchisee | ₹5 lakh–₹10 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | CCI (as above); IP Office for TM registry actions | No franchise statute in India |
| `com.b2b` | `agency_c_and_f` | Agency, commission, C&F | Principal, agent | ₹1 lakh–₹5 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | — | Contract Act ss.182–238; s.205 notice |
| `com.b2b` | `manufacturing_job_work` | Contract manufacturing/job work | Brand owner, manufacturer | ₹5 lakh–₹25 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | — | Tools/moulds retention issues |
| `com.b2b` | `logistics` | Transport, warehousing (domestic) | Shipper, carrier, 3PL | ₹50,000–₹5 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | — | Sea carriage cross-border → INT |
| `com.b2b` | `guarantee_indemnity` | Corporate guarantee/indemnity (non-bank) | Beneficiary, guarantor | ₹10 lakh–₹50 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | DRT if claimant bank/FI ≥ ₹20 lakh | R-COM-01 |
| `com.b2b` | `post_ma_indemnity` | Post-M&A warranty/indemnity, earn-out, escrow release | Buyer, sellers, escrow agent | ₹1 cr–₹500 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | — | Expert determination for completion accounts |
| `com.b2b` | `public_procurement_supply` | Supply/services to Ministry, Dept, CPSE, PSB, ULB | Contractor, government entity | ₹10 lakh–₹100 cr | `com.gov.v1` | ✔ | ✔* | ✔* | High-Level Committee of the entity (DoE OM 3 Jun 2024) | Arbitration by norm only < ₹10 cr dispute value or with Secretary/MD approval |
| `com.b2b` | `breach_other` | Other B2B contract breach | Any businesses | ₹1 lakh–₹25 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | Commercial Court | |
| `com.con` | `epc_private` | Private EPC/design-build | Owner, EPC contractor | ₹1 cr–₹500 cr | `com.con.v1` | ✔ | ✔ | ✔* | Commercial Court | Three-member default > ₹10 cr |
| `com.con` | `epc_government` | Government works (item-rate, EPC, HAM) | Contractor, Ministry/CPSE/State/ULB | ₹1 cr–₹500 cr | `com.gov.v1` | ✔ | ✔* | ✔* | HLC; SAROD where NHAI/MoRTH contract names it | DoE ₹10 cr gating; CORE (unilateral panels) |
| `com.con` | `ppp_concession` | PPP/BOT/HAM concession disputes | Concessionaire SPV, authority, lenders | ₹10 cr–₹1,000 cr | `com.gov.v1` | ✔ | ✔* | ✔* | HLC; authority's dispute board | Lenders' substitution rights; tripartite agreements |
| `com.con` | `subcontract` | Sub-contract payment, back-to-back | Main contractor, sub-contractor | ₹10 lakh–₹50 cr | `com.con.v1` | ✔ | ✔ | ✔* | MSEFC if sub-contractor MSE and goods/services | Works-contract MSMED applicability [VERIFY — open: §18 Q9] |
| `com.con` | `consultancy` | Design/PMC/consultancy fees | Consultant, owner | ₹10 lakh–₹20 cr | `com.con.v1` | ✔ | ✔ | ✔* | — | |
| `com.con` | `escalation_variation` | Price variation, variations, extra items | Contractor, employer | ₹50 lakh–₹200 cr | `com.con.v1` | ✔ | ✔ | ✔* | — | CAL-COM-12 |
| `com.con` | `delay_ld` | Delay, EoT, prolongation, LDs | Contractor, employer | ₹50 lakh–₹200 cr | `com.con.v1` | ✔ | ✔ | ✔* | — | CAL-COM-13 LD cap |
| `com.con` | `bank_guarantee_invocation` | BG invocation/encashment dispute | Contractor, employer, bank | ₹10 lakh–₹100 cr | `com.con.v1` (urgent) | ✔ | ✔ | ✔* | Court s.9 for injunction (egregious fraud/irretrievable injustice only) | Urgent trigger U-03 |
| `com.con` | `retention_final_bill` | Retention, final bill, closure | Contractor, employer | ₹10 lakh–₹50 cr | `com.con.v1` | ✔ | ✔ | ✔* | — | Limitation from final bill |
| `com.tech` | `software_dev` | Custom development, milestones, acceptance | Vendor, client | ₹10 lakh–₹50 cr | `com.tech.v1` | ✔ | ✔ | ✔* | Commercial Court | Confidentiality ring default `high` |
| `com.tech` | `saas_subscription` | SaaS fees, renewal, termination, exit | Provider, customer | ₹1 lakh–₹10 cr | `com.tech.v1` | ✔ | ✔ | ✔* | Consumer Commission only if individual consumer | |
| `com.tech` | `it_outsourcing` | Managed services/outsourcing | Provider, customer | ₹1 cr–₹200 cr | `com.tech.v1` | ✔ | ✔ | ✔* | — | Transition/exit assistance |
| `com.tech` | `sla_credit` | SLA breach, service credits | Provider, customer | ₹1 lakh–₹10 cr | `com.tech.v1` | ✔ | ✔ | ✔* | — | Expert determination of metrics; CAL-COM-14 |
| `com.tech` | `data_breach_contractual` | Contractual indemnity for data incidents | Controller, processor | ₹10 lakh–₹50 cr | `com.tech.v1` | ✔ | ✔ | ✔* | Data Protection Board / CERT-In for regulatory reporting | DPB penalties not arbitrable |
| `com.tech` | `ip_licence_royalty` | Licence fees, royalty audits, scope | Licensor, licensee | ₹5 lakh–₹100 cr | `com.tech.v1` | ✔ | ✔ | ✔* | — | Arbitrable (*Vidya Drolia*; *Eros v Telemax*) |
| `com.tech` | `ip_assignment` | Assignment terms, consideration, reversion | Assignor, assignee | ₹5 lakh–₹50 cr | `com.tech.v1` | ✔ | ✔ | ✔* | IP Office/HC for rectification | Copyright s.19(4) lapse |
| `com.tech` | `ip_registry_relief` | Grant, validity, revocation, rectification, opposition | IP owners | — | `com.signpost` | ✖ | ✔* | ✖ | IP Office; High Court (IP Division) | Commercial layer may be mediated; no award on registry relief (R-COM-19) |
| `com.tech` | `source_code_escrow` | Escrow release, verification | Licensor, licensee, escrow agent | ₹5 lakh–₹10 cr | `com.tech.v1` | ✔ | ✔ | ✔* | — | Expert determination of release trigger |
| `com.tech` | `tech_transfer` | Technology transfer/know-how (domestic) | Transferor, transferee | ₹10 lakh–₹100 cr | `com.tech.v1` | ✔ | ✔ | ✔* | — | Foreign party → INT |
| `com.re` | `homebuyer_delay_refund` | Possession delay, refund on withdrawal | Allottee, promoter | ₹10 lakh–₹5 cr | `com.re.v1` | ✔ | ✔ | ✖ default (✔* on informed post-dispute election only) | RERA Authority/AO; Consumer Commission | Emaar (LR-CONS-003); MahaRERA card if MH |
| `com.re` | `homebuyer_defects` | Structural/quality defects, carpet-area shortfall | Allottee, promoter | ₹1 lakh–₹1 cr | `com.re.v1` | ✔ | ✔ | as above | RERA (s.14(3) 5-year defect liability); Consumer | |
| `com.re` | `allottee_collective` | Multiple allottees of one project | Allottee group/RWA, promoter | ₹1 cr–₹200 cr | `com.re.v1` (group) | ✔ | ✔ | ✖ | RERA; NCLT (s.7 threshold 100 allottees or 10%) | Group mediation; MFN risk |
| `com.re` | `society_handover` | Conveyance, handover to society, maintenance | RWA/society, promoter | ₹10 lakh–₹20 cr | `com.re.v1` | ✔ | ✔ | ✔* (B2B only) | RERA; State co-op registrar | |
| `com.re` | `jda_development` | Joint development — area share, revenue share | Landowner, developer | ₹1 cr–₹500 cr | `com.re.v1` | ✔ | ✔ | ✔ | Civil/Commercial Court | Property transfer outputs → NN-08 physical execution/registration |
| `com.re` | `commercial_lease` | Commercial lease rent, lock-in, exit | Landlord, tenant | ₹1 lakh–₹25 cr | `com.re.v1` | ✔ | ✔ | ✔* | Rent Controller if rent-control tenancy | Rent-control tenancy → arbitration ✖ (*Vidya Drolia*) |
| `com.re` | `brokerage` | Brokerage/agency fees | Broker, principal | ₹50,000–₹2 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | RERA (agent registration) | |
| `com.re` | `sale_agreement_b2b` | Sale agreement between businesses | Seller, buyer | ₹50 lakh–₹100 cr | `com.re.v1` | ✔ | ✔ | ✔* | Civil Court (specific performance) | Conveyance = NN-08 physical route |
| `com.part` | `firm_dissolution` | Dissolution of firm | Partners, heirs | ₹10 lakh–₹50 cr | `com.part.v1` | ✔ | ✔ | ✔* | Civil Court (s.44 dissolution) | |
| `com.part` | `firm_accounts` | Accounts, capital/current accounts | Partners | ₹5 lakh–₹20 cr | `com.part.v1` | ✔ | ✔ | ✔* | Civil Court | Art.5 Limitation Act |
| `com.part` | `retirement_exit` | Retirement, expulsion, exit payout | Partners | ₹10 lakh–₹50 cr | `com.part.v1` | ✔ | ✔ | ✔* | — | CAL-COM-16 |
| `com.part` | `llp_partner_dispute` | LLP partner disputes under LLP agreement | LLP partners, LLP | ₹10 lakh–₹100 cr | `com.part.v1` | ✔ | ✔ | ✔ (para 14 default) | NCLT for compromise/winding up | LLP may be respondent (*Kartik Radia*) |
| `com.part` | `llp_governance` | LLP governance, admission, deadlock | LLP partners | ₹10 lakh–₹50 cr | `com.part.v1` | ✔ | ✔ | ✔ | NCLT (ss.60–64) | |
| `com.part` | `capital_profit_share` | Profit share, capital contribution | Partners | ₹5 lakh–₹20 cr | `com.part.v1` | ✔ | ✔ | ✔* | — | |
| `com.part` | `professional_firm` | CA/law/medical partnership splits | Professionals | ₹10 lakh–₹20 cr | `com.part.v1` | ✔ | ✔ | ✔* | ICAI/BCI/NMC (disciplinary only) | Disciplinary complaints excluded (LR-MED-009) |
| `com.corp` | `sha_breach` | SHA/SSA breach | Shareholders, company | ₹1 cr–₹1,000 cr | `com.corp.v1` | ✔ | ✔ | ✔ | NCLT for statutory reliefs | AoA alignment (*V.B. Rangaraj*) |
| `com.corp` | `jv_deadlock` | JV deadlock, termination | JV partners | ₹5 cr–₹1,000 cr | `com.corp.v1` | ✔ | ✔ | ✔ | NCLT (s.241, s.271) | Three-member default > ₹10 cr; equal_footing candidate |
| `com.corp` | `founder_exit_vesting` | Founder exit, vesting, bad leaver | Founders, investors, company | ₹50 lakh–₹100 cr | `com.corp.v1` | ✔ | ✔ | ✔ | NCLT | Employment component of a founder = WRK if individual employee claims |
| `com.corp` | `esop` | ESOP grant, cancellation, buy-back | Employee-holder, company | ₹5 lakh–₹20 cr | `com.corp.v1` | ✔ | ✔ | ✔* | — | Individual employee → WRK W11 overlap; arbitration only non-workman (master §5.2) |
| `com.corp` | `put_call_valuation` | Put/call, valuation disputes | Investor, promoter | ₹5 cr–₹1,000 cr | `com.corp.v1` | ✔ | ✔ | ✔ | — | Expert determination of value; FEMA pricing if non-resident → INT |
| `com.corp` | `drag_tag` | Drag/tag/ROFR/ROFO compliance | Shareholders | ₹5 cr–₹500 cr | `com.corp.v1` | ✔ | ✔ | ✔ | — | |
| `com.corp` | `board_control` | Board seats, nominee directors, information rights | Shareholders, company | ₹1 cr–₹500 cr | `com.corp.v1` | ✔ | ✔ | ✔* (contract layer) | NCLT (ss.241–242) | |
| `com.corp` | `oppression_mismanagement` | Oppression/mismanagement reliefs | Members, company, directors | ₹1 cr–₹1,000 cr | `com.corp.v1` (mediation + s.442) | ✔ | ✔ | ✖ statutory reliefs (✔ SHA claims severed) | NCLT (ss.241–242, s.244 threshold) | R-COM-14; *Rakesh Malhotra* (Bom HC); *Haryana Telecom* |
| `com.corp` | `family_business` | Family business separation (company vehicle) | Family members, company | ₹1 cr–₹1,000 cr | `com.corp.v1` | ✔ | ✔ | ✔* | NCLT; Civil Court (succession to shares — *Aruna Oswal*) | Personal-property/succession heads → FAM |
| `com.corp` | `s442_panel_reference` | NCLT/NCLAT/Central Govt reference under s.442 | Parties to NCLT proceedings | ₹1 cr–₹1,000 cr | `com.s442.v1` | — | ✔ (by panel member, individual capacity) | ✖ | NCLT/NCLAT (r.26 order) | R-COM-15: Tribunal-fixed fee; Equator branding off |
| `com.ibc` | `pre_ibc_oc_dues` | Operational creditor dues before s.8/s.9 | OC, corporate debtor | ₹1 cr–₹100 cr | `com.ibc.desk.v1` | ✔ | ✔ | ✔* (contract claim only, pre-admission) | NCLT (s.9); IU (NeSL) | Threshold ₹1 crore (S.O. 1205(E), 24 Mar 2020) |
| `com.ibc` | `pre_ibc_fc_default` | Non-bank financial creditor default (NBFC not "financial institution", bondholder, ICD lender) | FC, corporate debtor | ₹1 cr–₹500 cr | `com.ibc.desk.v1` | ✔ | ✔ | ✔* (pre-admission; not bank/FI ≥ ₹20 lakh) | NCLT (s.7); DRT for banks/FIs | Banks/FIs → FIN (R-COM-01) |
| `com.ibc` | `pending_application_settlement` | Settlement after s.7/s.9 filing, before admission | Applicant, CD | ₹1 cr–₹500 cr | `com.ibc.desk.v1` (fast) | ✔ | ✔ | ✖ | NCLT (r.8 withdrawal) | 14-day admission duty for FC applications |
| `com.ibc` | `s12a_withdrawal_settlement` | Post-admission settlement for s.12A IBC withdrawal | CD/promoter, applicant, CoC members, RP | ₹1 cr–₹1,000 cr | `com.ibc.s12a.v1` | ✔ | ✔ (consent of RP for engagement) | ✖ | NCLT (s.12A via RP; 90% CoC; 30 days) | Window only after CoC constitution and before first Form G |
| `com.ibc` | `prepack_msme` | PPIRP pre-filing facilitation (MSME CD) | MSME CD, unrelated FCs, proposed RP | ₹10 lakh–₹100 cr | `com.ibc.prepack.v1` | ✔ | ✔ | ✖ | NCLT (s.54C) | Default ≥ ₹10 lakh (S.O. 1543(E), 9 Apr 2021) |
| `com.ibc` | `ots_restructuring` | Out-of-court workout/restructuring with non-bank creditors | CD, creditors (non-bank) | ₹1 cr–₹500 cr | `com.ibc.desk.v1` | ✔ | ✔ | ✔* (contract claims) | Bank/FI ICA → FIN | |
| `com.ibc` | `voluntary_liquidation` | Disputes in voluntary liquidation; withdrawal under s.59(5A)–(5C) | Company, creditors, liquidator | ₹10 lakh–₹100 cr | `com.ibc.liq.v1` | ✔ | ✔* | ✖ | NCLT | ≤ 1 year (s.59(2)) |
| `com.ibc` | `liquidation_s230_scheme` | Compromise/arrangement during liquidation; asset-sale side disputes | Proponent, creditors, liquidator | ₹1 cr–₹1,000 cr | `com.ibc.liq.v1` | ✔ | ✔* | ✖ | NCLT (s.230 sanction) | Reg 2B 90-day window (proposal ≤ 30 days from liquidation commencement; REG151 2026 proviso) [Verified 22 Oct 2026]; s.29A bar (*Arun Kumar Jagatramka*) |
| `com.ibc` | `personal_guarantor` | Personal guarantor settlement (Part III IBC) | Creditor, personal guarantor | ₹10 lakh–₹100 cr | `com.ibc.desk.v1` | ✔ | ✔ | ✖ once s.94/95 filed | NCLT/DRT (ss.94–100) | s.96 interim moratorium on filing |
| `com.ibc` | `claim_dispute_with_rp` | Claim admission disputes with RP/liquidator | Creditor, RP | ₹10 lakh–₹100 cr | `com.signpost` | ✔* (commercial terms with RP consent) | ✔* | ✖ | NCLT (s.60(5)) | Hard block arbitration |
| `com.ibc` | `ciirp` | Creditor-Initiated IRP (Ch. IV-A) | Notified FC classes, CD | — | `com.signpost` | — | — | ✖ | — | [NOT IN FORCE]; flag `com.ciirp` OFF — information card only |
| `com.msme` | `msme_supply_goods` | MSE supplier — goods | MSE supplier, buyer | ₹50,000–₹5 cr | `com.msme.v2` | ✔ | ✔ (pre-MSEFC conciliation) | ✔* (only on supplier's recorded informed election and no MSEFC reference) | MSEFC via MSME ODR portal | *Mahakali Foods*; R-MSME-1 |
| `com.msme` | `msme_services` | MSE supplier — services | MSE supplier, buyer | ₹50,000–₹5 cr | `com.msme.v2` | ✔ | ✔ | ✔* | MSEFC | |
| `com.msme` | `msme_works_contract` | MSE works contract | MSE contractor, employer | ₹1 lakh–₹10 cr | `com.msme.v2` | ✔ | ✔ | ✔* | MSEFC (applicability contested) | [VERIFY — open: §18 Q9] |
| `com.msme` | `msefc_referred` | Council-referred mediation/arbitration under substituted s.18 | MSE supplier, buyer | ₹50,000–₹5 cr | `com.msme.msp.v1` | — | ✔ | ✔ (Council referral) | MSEFC | Flag `com.msefc_referral_msp` OFF |
| `com.chq` | `ni138_pre_complaint` | Cheque bounced; within notice/payment window | Payee, drawer (businesses) | ₹50,000–₹5 cr | `com.chq.v1` | ✔ | ✔ | ✖ offence; ✔* underlying contract claim | Magistrate; Lok Adalat | NN-24; civil money only |
| `com.chq` | `ni138_pending` | Complaint pending (any stage) | Complainant, accused (businesses) | ₹50,000–₹5 cr | `com.chq.v1` | ✔ | ✔ | ✖ | Magistrate (s.147 compounding); Sessions/HC; Lok Adalat | Compounding cost by stage (CAL-COM-10) |
| `com.bfs` | `bg_lc_domestic` | Domestic LC/BG between businesses (non-bank claimant) | Applicant, beneficiary | ₹10 lakh–₹100 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | DRT if bank/FI claimant ≥ ₹20 lakh | Bank as party → check RDB s.2(h) |
| `com.bfs` | `nbfc_b2b_facility` | NBFC (not RDB FI) business loan — corporate borrower | NBFC, company | ₹10 lakh–₹100 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | NCLT (s.7) if ≥ ₹1 cr default | NN-03 repeat-player → no party nomination; retail/MSME borrower → FIN |
| `com.bfs` | `factoring_treds` | Factoring, TReDS, invoice discounting | Factor, MSME, buyer | ₹1 lakh–₹10 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | TReDS platform grievance; MSEFC | CPSE must settle on TReDS (MSMED 2026) |
| `com.bfs` | `derivative_treasury` | ISDA/treasury products between businesses | Counterparties | ₹1 cr–₹500 cr | `com.tiered.v2` | ✔ | ✔ | ✔* | — | Bank counterparty → FIN check |
| `com.reg` | `cci_abuse_cartel` | Competition allegations | Any | — | `com.signpost` | ✖ | ✖ (CCI proceedings) | ✖ | CCI; NCLAT (s.53N compensation) | Private contract layer may continue in another L1 |
| `com.reg` | `consumer_b2c` | B2C deficiency | Consumer, business | — | `com.signpost` (+ voluntary mediation) | ✔ | ✔ | ✖ (consumer election) | Consumer Commission (e-Jagriti) | LR-CONS-001..005 |
| `com.reg` | `regulator_penalty` | Tax, SEBI/SAT, TRAI/TDSAT, electricity, PNGRB, NGT, company-law offences | Any | — | `com.signpost` | ✖ | ✖ | ✖ | Statutory regulator/tribunal | Mediation Act First Schedule items 6–11 (policy mirror, LR-MED-009) |

### 2.3 Ladder definitions (`com.*` pathways; pinned per case)

| Ladder | Rungs (in order) | Entry guard | Time-boxes (defaults) |
|---|---|---|---|
| `com.tiered.v2` | 0′ signposting (parallel) → 1 negotiation (senior management) → 2 mediation **or** Part III conciliation → 3 arbitration (standard/expedited/s.29B) → 4 appeal tier (opt-in) | Arbitration only with valid s.7 agreement naming Equator or post-dispute submission agreement | Neg 15 d (tiered clause) / 21 d (default `neg_timebox`); Med 30 d under tiered clause, 60 d (+60) voluntary; Conc 30 d (`conc_timebox`); s.29A 12 + 6 m |
| `com.prelit.v1` | 1 invitation (S4 B5) → 2 conciliation (default for company respondents) or mediation → output conversion → if not settled and suit intended: Form-1 PIMS pack | No pending suit on the same cause | Invitation D0–D30 cadence; conciliation 30 d; mediation 60 d (+60) |
| `com.gov.v1` | 1 negotiation with contract tier compliance → 2 mediation producing **HLC-ready proposal** → 3 arbitration only if dispute < ₹10 crore or approval uploaded (DoE para 7(ii)–(iii)) | Counterparty ∈ GOVT_SET (§4.3) | Neg 30 d; Med 60–90 d; settlement status `pending_competent_authority_approval` until approval uploaded |
| `com.con.v1` | 0′ signposting → 1 claim-wise negotiation → 2 contract tier (engineer/DAB/conciliation committee) compliance check → 3 co-mediation (lawyer + engineer/quantum expert) or expert determination (measurement) → 4 arbitration (three-member > ₹10 crore) | Tier status recorded (K5) | Neg 30 d; DAB per contract; Med 60–90 d |
| `com.tech.v1` | 1 negotiation → 2 mediation with technologist co-mediator / expert determination for SLA metrics → 3 arbitration with confidentiality ring | — | Neg 21 d; ED 21 + 14 d; Med 60 d |
| `com.re.v1` | 0′ RERA/consumer signposting (mandatory for homebuyers) → 1 structured offer negotiation → 2 mediation (group mediation where `allottee_collective`) → 3 arbitration **B2B only** (homebuyer only on informed post-dispute election) | Homebuyer: signposting recorded before rung 1 | Neg 21 d; Med 60 d; MahaRERA conciliation card if State = MH |
| `com.part.v1` | 1 negotiation → 2 mediation (valuation expert option) → 3 arbitration (LLP para 14 default) | — | Neg 21 d; Med 60 d (+60) |
| `com.corp.v1` | 0′ NCLT signposting → 1 negotiation → 2 mediation (or s.442 track if NCLT pending) → 3 arbitration of SHA/JV contract layer only → 4 corporate implementation (resolutions, SH-4, AoA) | Oppression reliefs severed (R-COM-14) | Neg 21 d; Med 90 d (+60); s.442 3 + 3 m |
| `com.s442.v1` | Tribunal reference → panel mediator (individual) → r.11 memorandum ≥ 10 d before session → sessions → r.24 settlement or r.25 failure report → r.26 Tribunal order | Uploaded reference order | `s442_clock` 3 m + 3 m |
| `com.ibc.desk.v1` | 1 IU/notice guidance → 2 fast mediation (7–10 d) → 3 settlement with conditions precedent → 4 r.8 withdrawal memo (pre-admission) / escrowed instalments with revival clause | Stage ∈ {no_notice, s8_served, filed_not_admitted} | Mediation 10 d (configurable 7–21) |
| `com.ibc.s12a.v1` | 1 settlement drafting (blocked "withdraw now" CTA while CoC not constituted) → 2 CoC engagement pack (90% vote calculator) → 3 s.12A application support annex through RP → 4 NCLT order upload | Admitted; `coc_constituted = true`; `form_g_issued = false` | `ibc_s12a_window` until Form G; `ibc_s12a_decision` 30 d |
| `com.ibc.prepack.v1` | 1 eligibility check → 2 facilitated negotiation with unrelated FCs on base resolution plan and RP → 3 vote-readiness tracker (51%; [VERIFY]) → 4 special resolution and declarations pack | CD is MSME; default ≥ ₹10 lakh | Neg 30–60 d; after filing: none (statutory) |
| `com.ibc.liq.v1` | 1 s.230 scheme negotiation (within Reg 2B window) / voluntary-liquidation withdrawal support / asset-sale side disputes mediation (liquidator consent) | Liquidation order date recorded | `liq_s230` 90 d; `liq_total` 180 + 90 d (tracking only) |
| `com.msme.v2` | 0′ MSEFC signposting card first (R-MSME-1) → 1 negotiation with full s.16 interest shown → 2 pre-MSEFC conciliation (Part III) → 3 MSME ODR export pack (supplier files) → (arbitration by Equator only on informed election, no MSEFC reference) | Supplier Udyam micro/small | Neg + Conc 30 d (Card COM-STD C10) |
| `com.msme.msp.v1` (flag) | Council referral → Equator mediation (Mediation Act mutatis mutandis) → on failure Council arbitrates or refers to an ADR service provider within 30 d → award within 90 d of pleadings | `com.msefc_referral_msp` ON with Council listing reference | `msme_council_med` 90 d; `msme_arb_refer` 30 d; `msme_award` 90 d |
| `com.chq.v1` | 1 negotiation inside 15-day pay window (escrow payment link) → 2 mediation of civil debt → 3 compounding papers (s.147) / Lok Adalat referral note | Cheque facts recorded | Neg ≤ pay window; Med 30 d |
| `com.signpost` | Signposting only; optional voluntary mediation of a severable commercial layer in another L1 | — | — |

### 2.4 Legacy code mapping (P08 FR-P08-24 → v2)

| P08 v1 code | v2 L1 / L2 | Migration rule |
|---|---|---|
| `com.breach_damages` | `com.b2b.breach_other` (or specific L2 chosen by triage) | Re-classify open cases on next triage; pinned cases keep v1 code in `legacy_dispute_type` |
| `com.payment_recovery` | `com.b2b.supply_goods` / `services` | as above |
| `com.supply_procurement` | `com.b2b.supply_goods` / `public_procurement_supply` | `public_procurement` sub-type → `com.gov.v1` |
| `com.distribution_franchise` | `com.b2b.distribution` / `franchise` / `agency_c_and_f` | |
| `com.shareholder_jv` | `com.corp.*` / `com.part.*` | `dissolution` → `com.part.firm_dissolution` |
| `com.oppression` | `com.corp.oppression_mismanagement` | `signpost_only` retained for statutory reliefs |
| `com.construction` | `com.con.*` | |
| `com.technology_ip` | `com.tech.*` | |
| `com.real_estate_commercial` | `com.re.*` | |
| `com.banking_finance_b2b` | `com.bfs.*` / `com.b2b.guarantee_indemnity` / `com.con.bank_guarantee_invocation` | `colending` → FIN `fin.colending` |
| `com.msme_delayed_payment` | `com.msme.*` | |
| `com.post_ma` | `com.b2b.post_ma_indemnity` | |
| `com.cross_border` | → `INT` | unchanged |

---

## 3. Legal framework by subtype

Each table lists: statute/section → forum → limitation → statutory clocks → leading case law → status. Clocks are seeded in `core.clock_kind` (§16.4) with owners (NN-04). Limitation always runs; no Equator process suspends it unless a register rule says so (Appendix A §6.3 invariant 3).

### 3.1 Cross-cutting rails (apply to every L1)

| Topic | Rule | Source | Status | Engine |
|---|---|---|---|---|
| Arbitrability screen | Non-arbitrable if (1) action in rem not involving subordinate rights in personam; (2) affects third parties/erga omnes/needs centralised adjudication; (3) inalienable sovereign/public functions; (4) mandatory statute bars it expressly or by implication; "when in doubt, refer" | *Vidya Drolia v Durga Trading Corp* (2021) 2 SCC 1 (SC 3-J, 14 Dec 2020); *Booz Allen v SBI Home Finance* (2011) 5 SCC 532 | [IN FORCE] | `ARB_SCREEN` → `arbitrable` / `not_arbitrable` / `doubtful` (doubtful = arbitration shown with warning + counsel-review task) — LR-ARB-019 |
| Fraud allegations | Arbitrable unless they vitiate the arbitration agreement or carry a public/in-rem element | *Avitel Post Studioz v HSBC PI Holdings* (2021) 4 SCC 713; *Vidya Drolia* | [IN FORCE] | Warning W-FRAUD; LR-MED-017 registrar review before mediation (policy) |
| Group of companies | Non-signatory affiliates may be bound on mutual intent; joinder only by reasoned tribunal order | *Cox & Kings v SAP India* (2024) 4 SCC 1 (5-J, 6 Dec 2023); LR-ARB-029 | [IN FORCE] | Field `non_signatory_affiliates[]`; F-COM-22 |
| Electronic arbitration agreement | Agreement by exchange of electronic communications valid | A&C s.7(4)(b); LR-ARB-027 | [IN FORCE] | Clause capture stores hash, OTP/eSign evidence |
| Incorporation by reference | PO/invoice T&Cs bind only with a clear reference to the arbitration clause | A&C s.7(5) | [IN FORCE] | Warning W-INCORP when C6 = "PO + invoices" |
| Unstamped arbitration agreement | Curable, not void | *In re Interplay*, 2023 INSC 1066 (7-J, 13 Dec 2023); LR-ARB-028 | [IN FORCE] | W + stamp status display |
| Unilateral appointment | Party-unilateral or curated-panel appointment invalid; independence/equal treatment | *CORE v ECI-SPIC-SMO-MCML (JV)* (SC 5-J, 8 Nov 2024); *Perkins Eastman v HSCC* (2020) 20 SCC 760; *Bhadra International v AAI* (SC, 5 Jan 2026) | [IN FORCE] | NN-03; LR-ARB-001/002; equal_footing exception (§7.12) |
| s.21 commencement; s.11 limitation | Notice invoking arbitration starts the arbitration; s.11 petition within 3 years of failure to appoint | A&C ss.21, 11; *Arif Azim Co v Aptech*, 2024 INSC 155 (1 Mar 2024); LR-ARB-031 | [IN FORCE] | `arb_s11_3y` clock; F-COM-23 |
| Pleadings, award time | s.23(4) 6 months; s.29A 12 + 6 months; s.29B 6 months | A&C ss.23(4), 29A, 29B; *Mohan Lal Fatehpuria*, 2025 INSC 1409; *Rohan Builders*, 2024 SCC OnLine SC 2494; *Viva Highways v MPRDC* (SC, 7 Jan 2026) | [IN FORCE] | LR-ARB-009/011/012; `arb_s23_4`, `arb_s29a`, `arb_s29b` |
| Delay after hearing | Inordinate delay may vitiate award; Equator award target 3 months from final hearing | *Lancor Holdings v Prem Kumar Menon*, 2025 INSC 1277; LR-ARB-032 | [IN FORCE] | `award_target` SLA |
| Severable operative parts | Award paragraphs severable per claim/interest head | *Gayatri Balasamy v ISG Novasoft*, 2025 INSC 605 (5-J, 30 Apr 2025); LR-ARB-021 | [IN FORCE] | Template lint |
| Post-award interest | s.31(7)(b) cannot be contracted out | A&C s.31(7); *ONGC v G&T Beckfield*, 2025 INSC 1066; LR-ARB-015 | [IN FORCE] | CAL-COM-03 |
| Emergency arbitrator | EA order under institutional rules enforceable as s.17 order for India seat | *Amazon.com NV Investment Holdings v Future Retail* (2022) 1 SCC 209; LR-ARB-025 | [IN FORCE] | §7.13 |
| Conciliation output | s.73 settlement with s.74 award status; s.62(4) 30-day non-reply = rejection; s.80 non-identity unless agreed; s.81 inadmissibility | A&C ss.61–81; LR-CONC-001..005 | [IN FORCE] (Sixth Schedule substitution not notified) | Default pre-suit output |
| Consent award | Settlement during arbitral proceedings recorded as award on agreed terms | A&C s.30; LR-ARB-018 | [IN FORCE] | Pre-arbitration settlements default to Part III conciliation (Appendix A B05 [VERIFY — open: no SC authority on consent award where settlement precedes arbitration]) |
| s.12A PIMS | Suit of specified value (≥ ₹3,00,000) without urgent interim relief needs PIMS through LSA Authority; 3 + 2 months excluded from limitation; Equator cannot issue Form-3/Form-5 | CCA ss.2(1)(i), 12A; PIMS Rules 2018 (G.S.R. 606(E), 3 Jul 2018) rr.2–7, Forms 1–6, Sch. II; *Patil Automation v Rakheja* (2022) 10 SCC 1 (mandatory from 20 Aug 2022); *Yamini Manohar v T.K.D. Keerthi* (2024) 5 SCC 815 [VERIFY — open: reporter]; *Dhanbad Fuels v UoI*, 2025 INSC 696; *Vijay v Havells India*, Del HC DB, FAO(COMM) 46/2025, 1 Jul 2026 (counter-claims need PIMS unless already mediated) | [IN FORCE] | LR-MED-013/014/015/018/020; `pims_s12a` clock owned by party |
| s.12A after Mediation Act Ninth Schedule | Central Govt may authorise an MSP under new s.12A(2)(ii); 120 + 60 days; settlement under Mediation Act ss.27–28 | Mediation Act 2023 s.64 + Ninth Schedule | [NOT IN FORCE] | LR-MED-019; `com.s12a_equator_authorised` OFF (four gates) |
| Confidentiality | Arbitral proceedings confidential save award for enforcement | A&C s.42A; LR-ARB-024 | [IN FORCE] | No public pages; publication only per App. R consent rules (NN-26) |
| Fees | Fourth Schedule ceiling ₹30,00,000 per arbitrator; sole +25% above ceiling | A&C Fourth Schedule, s.11(14); *ONGC v Afcons Gunanusa JV* (SC, 30 Aug 2022); LR-ARB-023 | [IN FORCE] | Appendix B Card COM-STD |
| Deposits/termination | s.38(2) suspension; termination by reasoned order; recall then s.14(2) | *Harshbir Singh Pannu v Jaswinder Singh*, 2025 INSC 1400 (9 Dec 2025); LR-ARB-022 | [IN FORCE] | Billing deposit workflow |
| Award delivery | Delivery to the party's competent person starts s.34(3) | A&C s.31(5); *Motilal Agarwala v State of WB*, 2025 INSC 1062; LR-ARB-014 | [IN FORCE] | Delivery evidence per party |
| Stamp | Award stamped under the law of the state of execution (last signature); late → impounding with penalty | *URC Construction v AAI*, Del HC, OMP(ENF.)(COMM.) 155/2026, 1 Sep 2026; Mah. Ord. XII of 2024 (Art.12); LR-STAMP-001/002 | [IN FORCE] | `award_stamping` clock; e-stamp before release |
| Bank/FI debts | Banks/FIs ≥ ₹20 lakh → DRT; arbitration blocked | RDB Act 1993 ss.1(4), 2(h), 17–18; S.O. 4312(E), 6 Sep 2018; LR-ARB-020 | [IN FORCE] | R-COM-01 → FIN |
| Consumer election | Arbitration clause cannot oust Consumer Commission | *Emaar MGF Land v Aftab Singh* (2019) 12 SCC 751 (10 Dec 2018); LR-CONS-003 | [IN FORCE] | Homebuyer and consumer rows |
| IBC moratorium | s.14 moratorium bars proceedings against CD once CIRP admitted | IBC s.14; LR-RBI-016 | [IN FORCE] | R-COM-08; case `on_hold.ibc_moratorium` |
| Limitation | Contract/price 3 years (Arts. 14, 55, 113); acknowledgement s.18; part-payment s.19; Limitation Act applies to arbitration (A&C s.43) | Limitation Act 1963 | [IN FORCE] | CAL-COM-04; `limitation_contract` |

### 3.2 `com.b2b` — contracts, supply, distribution, franchise, agency, procurement

| Element | Detail |
|---|---|
| Statutes | Indian Contract Act 1872 ss.73–75 (damages; s.74 LD as ceiling — *Kailash Nath Associates v DDA* (2015) 4 SCC 136), ss.182–238 (agency; s.205 reasonable notice on revocation of fixed-term agency); Sale of Goods Act 1930 ss.41–42 (acceptance), ss.55–56 (price/damages); Specific Relief Act 1963 as amended 2018 (s.14(d) determinable contracts not specifically enforceable); Commercial Courts Act 2015 s.2(1)(c) (ordinary transactions of merchants, distribution, licensing, franchising, agency, consultancy) and s.12A; Competition Act 2002 s.3(4) (vertical restraints — CCI); Partnership Act s.69 (unregistered firm may arbitrate — *Umesh Goel v HP Co-op Group Housing Society* (2016) 11 SCC 313) |
| Forum | Commercial Court / Commercial Division (after PIMS); arbitral tribunal where s.7 agreement exists; CCI for antitrust core; MSEFC if supplier is Udyam micro/small |
| Limitation | Price of goods sold and delivered, credit period: Art. 14 (3 years from expiry of credit); breach of contract: Art. 55 (3 years from breach); residuary: Art. 113 |
| Clocks | `limitation_contract`; `pims_s12a` (party-owned); arbitration clocks |
| Government procurement (`public_procurement_supply`) | DoE OM 3 Jun 2024 (Procurement Policy Division; file number appears in the reproduced PDF as "F. 11212024-PPD" **[VERIFY — open: probable reading F.1/2/2024-PPD (OCR loss of slashes); confirm on doe.gov.in]**): para 7(i) arbitration not routine; 7(ii) by norm only for disputes < ₹10 crore (dispute value, not contract value); 7(iii) above ₹10 crore only with Secretary (or delegate ≥ JS) / MD (CPSE, PSB, FI) approval and recorded reasons; 7(iv) institutional arbitration preferred; 7(v) challenges not routine; 7(vi)–(vii) settlement via contract mechanisms, Mediation Act mediation and negotiation; **High-Level Committee** (retired judge and/or retired senior officer/technical expert) negotiates, receives a mediated agreement, or mediates itself; 7(ix) final solution approved by appropriate authority (refers to Mediation Act s.49, **not in force**); 7(x) absence of mediation clause no bar to pre-litigation mediation |
| Recent case law | *Cox & Kings* (2024); *CORE* (2024) for unilateral panels in government contracts; *Bhadra International* (2026) |
| Status | [IN FORCE]; DoE OM is administrative guidance (not statute) |

### 3.3 `com.con` — construction and infrastructure

| Element | Detail |
|---|---|
| Statutes / instruments | Contract Act; A&C Act; CCA s.2(1)(c)(vi) (construction is commercial); DoE OM 3 Jun 2024 (above); model contracts (FIDIC Red/Yellow/Silver, MCA, CPWD GCC, NHAI/MoRTH HAM/EPC) as contract terms; MSMED Act where contractor is MSE and contract is supply of goods/services (works contracts contested) |
| Forum | Contract tier (Engineer, DAB/DAAB, conciliation committee) → arbitration; HLC for government; **SAROD** (Society for Affordable Redressal of Disputes) where the NHAI/MoRTH contract names it **[VERIFY — open: SAROD current rules/fees]**; s.9 court for BG injunctions |
| Limitation | Typically from final bill/certificate or termination (Art. 55/113); contractual claims-notice time-bars (validity tested against Contract Act s.28 as amended 1997 **[VERIFY — open: per clause]**) |
| Clocks | Contract tier deadlines captured as `contract_tier_*` (owner = party); `arb_*`; `bg_invocation_watch` (informational, urgent) |
| Case law | *CORE v ECI-SPIC-SMO-MCML* (2024) (unilateral curated panels); BG injunctions only for egregious fraud or irretrievable injustice (settled law, e.g., *U.P. State Sugar Corp v Sumac International* (1997) 1 SCC 568 [VERIFY — open: citation check]); express "no-interest" clauses bind tribunal for pre-award interest (settled line, e.g., *Sayeed Ahmed & Co v State of UP* (2009) 12 SCC 26 [VERIFY — open: citation check]) |
| Status | [IN FORCE] |

### 3.4 `com.tech` — IT, technology, SaaS and IP licensing

| Element | Detail |
|---|---|
| Statutes | Contract Act; IT Act 2000; DPDP Act 2023 + DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025) — Board penalties regulatory, not arbitrable; Copyright Act 1957 ss.18–19 (s.19(4) lapse), s.30; Patents Act 1970 ss.64 (revocation), 68–69 (assignment/licence writing and registration), 104 (suits); Trade Marks Act 1999 s.57 (rectification before High Court after Tribunals Reforms Act 2021); CCA s.2(1)(c)(xvii) (IP is commercial); BSA 2023 s.63 (electronic records certificate) |
| Arbitrability | Arbitrable: licence fee/royalty, licence scope, assignment terms, contractual infringement claims (*Eros International Media v Telemax Links*, Bom HC, 12 Apr 2016 **[VERIFY — open: 2016 SCC OnLine Bom 2179]**). Not arbitrable: grant, validity in rem, revocation, rectification, opposition (*Vidya Drolia*). An inter partes award on validity binds only the parties **[VERIFY — open: counsel Q8]** |
| Forum | Commercial Court / HC IP Division; IP Office for registry actions (signpost `SIG.IPO`); DPB/CERT-In for regulatory reports; CCI for SEP/FRAND abuse |
| Limitation | Art. 55/113; royalty under-payment per accounting period |
| Urgency | IP suits typically seek urgent injunctions → s.12A exemption usually applies (*Yamini Manohar*) |
| Status | [IN FORCE] |

### 3.5 `com.re` — real estate and RERA

| Element | Detail |
|---|---|
| Statutes | RERA 2016 s.31 (complaints to Authority/AO), s.32(g) (Authority recommends conciliation through forums set up by consumer or promoter associations), s.71 (AO compensation for ss.12, 14, 18, 19), ss.43–44, 58 (appeals), s.79 (civil court bar), ss.88–89; s.14(3) 5-year defect liability; s.4(2)(l)(D) 70% project account; State RERA Rules (interest typically SBI highest MCLR + 2% **[VERIFY — open: per-State table]**); CPA 2019 + Jurisdiction Rules 2021 (G.S.R. 912(E), 30 Dec 2021); IBC s.7 proviso (allottees: ≥ 100 or 10% of the project, whichever is less — *Manish Kumar v UoI* (2021) 5 SCC 1); TPA 1882 (commercial lease); State Rent Control Acts; Registration Act 1908 s.17; IT Act s.1(4) First Schedule (sale/conveyance excluded from e-sign) |
| Case law | *Imperia Structures v Anil Patni* (2020) 10 SCC 783 (consumer forum available despite RERA); *Newtech Promoters v State of UP* (2021) 18 SCC 1 (refund/interest = Authority; compensation = AO; RERA applies to ongoing projects); *Emaar MGF* (2019); *Vidya Drolia* (TPA tenancies arbitrable; rent-control tenancies not) |
| RERA conciliation | MahaRERA Conciliation and Dispute Resolution Forum: Circular 15 of 2018 (29 Jan 2018), refined by Circulars 31/2021 (18 May 2021) and 38/2021 (8 Nov 2021); two-member bench (consumer-association + promoter-association); other side must consent; ~3 hearings; closed in 60 days if no progress, +30 days on request; fee ₹1,000; signed settlement taken on record by MahaRERA [V-secondary]. Other States **[VERIFY — open: per-State conciliation cells]** |
| Equator position | Equator **cannot self-designate** as a s.32(g) forum (it is neither a consumer nor a promoter association). Routes: (a) association-sponsored forum hosted on Equator's stack ("powered by Equator") subject to State Authority recognition — flag `com.rera_forum_tieup` OFF; (b) private mediation whose settlement is placed before the Authority/consumer forum where a complaint is pending [interpretation — counsel Q6] |
| Limitation / clocks | RERA complaint: no fixed limitation in the Act **[VERIFY — open: State rules]**; consumer complaint 2 years (CPA s.69; LR-CONS-002); disposal targets RERA s.29(4)/s.71(2) 60 days (directory facts); `maharera_conc` 60 + 30 days |
| Status | [IN FORCE] |

### 3.6 `com.part` — partnership firms and LLPs

| Element | Detail |
|---|---|
| Statutes | Indian Partnership Act 1932 s.13(c)–(d) (interest on capital/advances; 6% on advances absent agreement), s.43 (dissolution at will), s.44 (court dissolution incl. just and equitable), ss.46–48 (settlement of accounts), s.69 (unregistered firm suits barred; s.69(3)(a) exception for dissolution/accounts; arbitration not barred — *Umesh Goel*); LLP Act 2008 s.23 (LLP agreement; First Schedule default), **First Schedule para 14** (partner disputes under the LLP agreement referred to arbitration under the A&C Act absent contrary agreement); ss.60–62 (compromise/arrangement — NCLT); ss.63–64 (winding up — NCLT); no statutory oppression remedy for LLPs |
| Case law | *Kartik Radia v BDO India LLP*, 2025 SCC OnLine Bom 445 (Bom HC, 4 Mar 2025): LLP bound by the arbitration clause in the LLP agreement on governance although not a signatory |
| Limitation | Accounts of a dissolved partnership: Art. 5 (3 years from dissolution) |
| Filings after settlement | Registrar of Firms notices (State rules); LLP Form 4 within 30 days of change in partners; stamp duty on dissolution/retirement deed by State |
| Exclusions | Professional disciplinary complaints (ICAI/BCI/NMC) not mediable (LR-MED-009 policy mirror); criminal breach-of-trust prosecutions (NN-24) |
| Status | [IN FORCE] |

### 3.7 `com.corp` — shareholder, JV, founder; oppression and mismanagement; s.442 panel

| Element | Detail |
|---|---|
| Statutes | Companies Act 2013 s.241 (oppression/mismanagement application to NCLT), s.242 (powers), s.244 (eligibility: ≥ 100 members or 1/10 of total members, whichever is less, or members holding ≥ 1/10 of issued share capital; NCLT may waive), s.245 (class action), ss.230–232 (compromise/arrangement), s.271 (winding up), ss.58–59 (transfer refusal; rectification), s.247 (registered valuer), **s.442** (Mediation and Conciliation Panel; in force 1 Apr 2014 (S.O. 902(E), 26 Mar 2014); powers delegated to Regional Directors (S.O. 4090(E), 19 Dec 2016)); Companies (Mediation and Conciliation) Rules 2016 (notified 9 Sep 2016); Mediation Act Eighth Schedule (s.63) amending Companies Act [NOT IN FORCE]; FEMA pricing for resident–non-resident transfers (→ INT if a party is non-resident); Indian Stamp Act (share transfer 0.015%, as amended 2020); SEBI LODR Reg. 30 (listed companies) |
| Arbitrability | Statutory reliefs under ss.241–242 not arbitrable; a petition "dressed up" to avoid an arbitration clause may be rejected; petition read as a whole — *Rakesh Malhotra v Rajinder Kumar Malhotra*, 2014 SCC OnLine Bom 1146, (2015) 192 Comp Cas 516; *Haryana Telecom v Sterlite Industries* (1999) 5 SCC 688 (winding up non-arbitrable); *Sumitomo Corp v CDC Financial Services* (2008) 4 SCC 91; *Dhananjay Mishra v Dynatron Services*, 2019 SCC OnLine NCLAT 163; *Aruna Oswal v Pankaj Oswal* (2020) 8 SCC 79 (succession/title to shares for civil court); SHA terms not in AoA do not bind company (*V.B. Rangaraj v V.B. Gopalakrishnan* (1992) 1 SCC 160) |
| s.442 Rules map | r.3 panels by Regional Directors, applications every February, panel effective 1 April; r.4 eligibility (former SC/HC judges; District/Sessions judges; tribunal members/registrars; ICLS/ILS officers 15 years; advocates ≥ 10 years; CA/CMA/CS ≥ 15 years' continuous practice; former State Consumer Forum members/presidents; trained mediators **[VERIFY — open: exact r.4 wording]**); r.5 disqualifications; r.6 Form MDC-2, fee ₹1,000; r.11 memorandum of issues ≥ 10 days before session; r.12 not bound by Evidence Act/CPC; r.14 two consecutive wilful absences → failed; r.17–18 facilitative only; r.19 3 months from appointment + up to 3 months by Tribunal (s.442(5) counts from reference — use earlier date); r.24–25 settlement/failure report; r.26 Tribunal hearing usually within 14 days and order in terms of settlement; r.27 fee fixed by referring authority; r.28 + Annexure A code of ethics, complaints to Regional Director; r.29 no parallel proceedings on referred issues; r.30 not referable: Chapter XIV inspection/investigation/inquiry, defaults/offences with pending compounding, serious fraud, forgery, impersonation, coercion, criminal/non-compoundable prosecutions, public interest or numerous non-parties [V-secondary] |
| Equator position | **Equator as an entity cannot be on the s.442 panel** (panel of "experts", individuals). An individual Equator neutral who meets r.4 may be empanelled by the Regional Director and, when appointed by NCLT/NCLAT, conducts a **s.442 mediation** (fee by Tribunal; 2016 Rules; settlement to Tribunal). Equator may host sessions only if the Tribunal/panel and parties agree to the venue/mode (r.11) **[VERIFY — open: counsel Q5 (02 §5 Q4)]**. Copy allowed: "[Name] is a member of the MCA Mediation and Conciliation Panel ([Region], valid from 1 April [year])." Blocked: "NCLT-empanelled Equator" |
| Limitation | s.241 petitions: Limitation Act Art. 137 applies per NCLAT practice **[VERIFY — open: authority]**; SHA damages: Art. 55 |
| Status | [IN FORCE] |

### 3.8 `com.ibc` — insolvency and restructuring (IBC 2016 as amended to 26 May 2026)

**3.8.1 Corporate debtor stages**

| Stage | Provision | Rule (21 Oct 2026) | Status |
|---|---|---|---|
| Threshold | s.4 | Default ≥ ₹1 crore (S.O. 1205(E), 24 Mar 2020) | [IN FORCE] |
| Pre-pack threshold | s.4 second proviso; Ch. III-A | Default ≥ ₹10 lakh for PPIRP (S.O. 1543(E), 9 Apr 2021) | [IN FORCE] |
| OC demand | s.8 | Demand notice/invoice (Form 3/4); CD has **10 days** to show pre-existing dispute or pay | [IN FORCE] |
| Pre-existing dispute | — | s.9 rejected if a plausible pre-existing dispute exists (*Mobilox Innovations v Kirusa Software* (2018) 1 SCC 353) | [IN FORCE] |
| Information Utility | s.215 (as amended 2026); IBBI (Information Utilities) (Amendment) Regulations 2026 (notified 1 Jun 2026, in force 3 Jun 2026); Circular IBBI/IU/100/2026 (3 Jun 2026) Forms A–E; Reg 21(3) authentication/dispute | OCs submit financial information to an IU before a CIRP application; debtor confirms/ignores 3 reminders → "Authenticated" + Record of Default; disputes → "Disputed" + Information of Dispute | [IN FORCE] [V-secondary] |
| Admission | s.7(5) (substituted 2026) | NCLT **shall** admit or reject an FC application within **14 days**; IU record sufficient proof; 7 days to cure defects; reasons if not decided in 14 days | [IN FORCE] |
| Arbitration vs IBC | — | NCLT decides default first; if admitted → in rem, arbitration cannot proceed; if rejected, arbitration may proceed (*Indus Biotech v Kotak India Venture (Offshore) Fund* (2021) 6 SCC 436, 26 Mar 2021) | [IN FORCE] |
| Withdrawal before admission | I&B (Application to Adjudicating Authority) Rules 2016 r.8 | Applicant may withdraw before admission | [IN FORCE] |
| **Withdrawal after admission** | **s.12A (substituted by IBC (Amendment) Act 2026)** | NCLT may allow withdrawal of an application admitted under s.7/9/10 **on the RP's application** with **90% of CoC voting share**; **not permitted before the CoC is constituted, nor after the first invitation for resolution plans** (Form G); NCLT to decide within **30 days** | [IN FORCE] from 26 May 2026 (S.O. 2625(E), 22 May 2026) |
| Exclusivity | — | s.12A read with CIRP Reg 30A is the exclusive withdrawal route; NCLAT r.11 inherent powers cannot bypass (*GLAS Trust Co LLC v BYJU Raveendran*, SC, 23 Oct 2024 2024 INSC 811, CA 9986/2024 [Verified 22 Oct 2026: SC judgment PDF]) | [IN FORCE] |
| CIRP Reg 30A | — | Substituted by CIRP (Third Amendment) Regulations 2026 (IBBI/2026-27/GN/REG152, 1 Jun 2026): RP files within 3 days of CoC approval; no application before CoC constitution or after the Reg 36A invitation **[VERIFY — open: confirm REG152 text on ibbi.gov.in; secondary sources only]** | [VERIFY] |
| Frivolous proceedings | new penalty (reported s.64A) | ₹1 lakh–₹2 crore for frivolous or vexatious proceedings | [IN FORCE] [V-secondary] |
| Restoration | s.33 | One-time CIRP restoration before liquidation order (66% CoC), max 120 days | [IN FORCE] [V-secondary] |
| Plan approval | ss.30–31 | NCLT to decide within 30 days; dissenting FCs get not less than lower of liquidation value or plan entitlement | [IN FORCE] [V-secondary] |
| CIIRP | Ch. IV-A ss.58A–58K | Creditor-initiated; enacted; Amendment Act s.40 excluded from S.O. 2625(E); IBBI discussion paper 15 Apr 2026; no regulations | [NOT IN FORCE] — flag `com.ciirp` OFF |
| Group / cross-border | Ch. V-A; s.240C | Rules to be framed | [NOT IN FORCE] |
| Fast-track CIRP | ss.55–58 | Omitted by Amendment Act s.39 (in force 26 May 2026) | [IN FORCE] (omission) |
| IBBI data | — | 1,191 s.12A withdrawals by 30 Jun 2025 (~14% of admitted CIRPs; 825 OC-initiated); to 30 Apr 2024, 21,466 s.9 applications disposed before admission vs 3,818 admitted | [V-secondary] — internal sizing only; never public copy without Claims Register entry (NN-17) |

**3.8.2 PPIRP (Ch. III-A ss.54A–54P).** Eligibility: CD is an MSME (MSMED s.7(1) classification); default ≥ ₹10 lakh; no PPIRP/CIRP in preceding 3 years; not in CIRP; no liquidation order; s.29A eligibility with MSME carve-out (s.240A). Pre-filing: unrelated FCs propose RP; majority-of-directors declaration; special resolution of members (or 3/4 partners); **unrelated FC approval threshold 66% originally; Amendment Act 2026 s.34 substitutes "fifty-one per cent." in s.54A(2)(e) and s.54A(3); S.O. 2625(E) brings s.34(a)(iii) and s.34(b) into force from 26 May 2026 → 51% applied from 26 May 2026** [Verified 22 Oct 2026: Act 6 of 2026 s.34(a)(iii) amends s.54A(2)(e) and s.34(b) amends s.54A(3); Gazette]. Base resolution plan by CD; Swiss challenge if OC claims impaired; admission decision 14 days; 120 days total (plan to AA within 90); debtor-in-possession. Equator role: pre-filing only (negotiation with unrelated FCs, information room, vote tracker, resolution/declaration drafts); after filing: none except consented side-dispute mediation.

**3.8.3 IBBI mediation proposal.** Expert Committee "Framework for Use of Mediation under the IBC" (31 Jan 2024); IIIPI report (21 Sep 2024); Discussion Paper "Mediation by the operational creditors" (≈4 Nov 2024; comments to 24 Nov 2024) proposing CIRP Reg. 2B/2BA voluntary pre-s.9 mediation with non-settlement report annexed to the s.9 application. **No regulation notified; 2026 Amendment Act contains no mediation provision.** Mediation Act ss.4–25 and 27–30 not in force, so no s.21 report can issue. Equator offers private "Pre-s.9 Commercial Mediation" with the Equator Mediation Closure Report footer (LR-MED-020 extended, §13.2); flag `com.ibbi_reg2b` switches template/footer only after a regulation is notified.

**3.8.4 Liquidation, voluntary liquidation, schemes.** s.54: complete and apply for dissolution within **180 days** of liquidation commencement, extendable ≤ **90 days**. s.52: secured creditor notifies intent to realise outside liquidation within **14 days**, else deemed relinquished; multi-lender assets 66% by value [V-secondary]. CoC supervises liquidation; replaces liquidator by 66%; may direct dissolution without liquidation [V-secondary]. Liquidation Regulations Reg 2B: s.230 scheme within **90 days** of liquidation order; s.29A-ineligible persons cannot propose (*Arun Kumar Jagatramka v Jindal Steel & Power* (2021) 7 SCC 474) [Verified 22 Oct 2026: Reg 2B in force as amended to 2 Jun 2026 — proposal only on CoC recommendation (CIRP Reg 39BA) and within 30 days of liquidation commencement; REG151 (1 Jun 2026) adds s.230(6) majority and realisable amount above liquidation value; IBBI compilation]. Voluntary liquidation: s.59(2) ≤ 1 year; s.59(5A)–(5C) termination/withdrawal by special resolution + creditor approval (2/3 in value). Equator never decides any of these; it facilitates negotiation of a scheme or a withdrawal and mediates asset-sale side disputes with liquidator consent.

**3.8.5 Personal guarantors.** IBC Part III ss.94–100; s.96 interim moratorium on filing of a s.94/95 application covering all the guarantor's debts (LR-RBI-016). Negotiation before filing allowed; once filed, Equator process limited to consented settlement terms presented through the resolution professional.

**3.8.6 Limitation and clocks.** Limitation Act Art. 137 applies to IBC applications (3 years from default; acknowledgements extend — *B.K. Educational Services v Parag Gupta* (2019) 11 SCC 633). Clocks: `ibc_s8_reply` 10 d; `ibc_admit_fc` 14 + 7 d (tracking); `ibc_s12a_window` (CoC constitution → first Form G); `ibc_s12a_decision` 30 d; `ppirp_total` 120 d; `liq_total` 180 + 90 d; `liq_sec_elect` 14 d; `liq_s230` 90 d; `vol_liq` ≤ 1 y. NCLT filing fees: FC ₹25,000; OC ₹2,000; CD ₹25,000 (I&B (AAA) Rules 2016 r.10 Schedule) [V-secondary].

### 3.9 `com.msme` — MSME delayed payments

| Provision / case | Rule | Status |
|---|---|---|
| MSMED s.2(b), Explanation | Appointed day = day after expiry of 15 days from acceptance/deemed acceptance; deemed acceptance if no written objection within 15 days of delivery | [IN FORCE] |
| s.15 | Pay by agreed date ≤ 45 days from acceptance/deemed acceptance; absent agreement, before appointed day (LR-MSME-001) | [IN FORCE] |
| s.16 | Compound interest, monthly rests, at **3 × RBI Bank Rate**, notwithstanding any agreement (LR-MSME-002); Bank Rate 5.75% from 7 Oct 2026 → **17.25% p.a.** (RBI MPS 7 Oct 2026) | [IN FORCE] |
| s.17 | Buyer liable for amount with s.16 interest | [IN FORCE] |
| s.18 (unamended, operative) | Reference to MSEFC → conciliation (A&C ss.65–81) by Council or institution/centre → arbitration by Council or institution/centre; supplier's location; 90 days (s.18(5)); overrides private arbitration agreement (*Gujarat State Civil Supplies Corp v Mahakali Foods* (2023) 6 SCC 401, 31 Oct 2022) (LR-MSME-003/004) | [IN FORCE] until the substituted s.18 commences [Checked 22 Oct 2026: substituted s.18 = Mediation Act s.62 + Seventh Schedule, amended by MSMED (Amendment) Act 2026 s.8; neither commenced] |
| s.19 | Set-aside only on deposit of 75% of award (LR-MSME-005) | [IN FORCE] |
| ss.22–23; IT Act 2025 s.37(2)(g) (old s.43B(h)) | Buyer disclosure; interest not deductible; MSE dues disallowed until paid (LR-MSME-008) | [IN FORCE] |
| Registration timing | *Silpi Industries v Kerala SRTC* (2021) 18 SCC 790; *Mahakali Foods*: registration on contract date required; *NBCC (India) Ltd v State of WB*, 2025 INSC 54 (10 Jan 2025): referred to 3-judge bench — **warning, not block** (LR-MSME-006) | [IN FORCE] / reference pending |
| Limitation | *Sonali Power Equipments v MSEB*, 2025 INSC 864: Limitation Act does not apply to s.18(2) conciliation; applies to s.18(3) arbitration (LR-MSME-007) | [IN FORCE] |
| MSME ODR portal | Live 27 Jun 2025 (RAMP; integrated with MSME Samadhaan); new delayed-payment cases filed on it from 15 Oct 2025 [V-secondary]; **no public API** | [IN FORCE] |
| MCA Form MSME-1 | Specified Companies (Furnishing information about payment to MSE suppliers) Order 2019: half-yearly return of dues > 45 days | [IN FORCE] |
| **MSMED (Amendment) Act 2026** | Substituted s.18: Council mediates or **refers to a mediation service provider**; Mediation Act 2023 applies mutatis mutandis; mediation within **90 days from first appearance**; on failure, within **30 days** Council arbitrates or refers to an **ADR service provider**; award within **90 days of completion of pleadings**; online modes allowed; jurisdiction at supplier's registered address. s.19 extended to mediated settlements; court may release a reasonable % of deposit; ≥ 50% to supplier if pending > 6 months. Mediated settlement/award recoverable as arrears of land revenue via District Collector; enforceable debt recognisable under IBC. Voluntary registration for all MSMEs; CPSEs must settle MSME invoices on TReDS; graded penalties (Development Commissioner; appeal to MSME Secretary). ss.15–16 unchanged (reported) | Passed Aug 2026; S.O. 5575(E), 12 Oct 2026 (ss.2–7, 11, 13–17 from 15 Oct 2026; s.12 from 15 Dec 2026) [V-secondary]; [Checked 22 Oct 2026: substitution is Mediation Act s.62 + Seventh Schedule, amended by Amendment Act s.8; neither commenced (S.O. 5575(E) omits ss.8–10); MSPs recognised by MCI under Mediation Act s.40; ADR institution chosen by the Council] **[VERIFY — open (counsel): operation before Mediation Act ss.4–25, 27–30 and 40 commence (counsel Q3)]** |

### 3.10 `com.chq` — cheque dishonour (commercial)

| Provision | Rule | Status |
|---|---|---|
| NI Act s.138 provisos (a)–(c) | Present within validity; demand notice within **30 days** of return memo; drawer pays within **15 days** of receipt (LR-RBI-017) | [IN FORCE] |
| s.142(1)(b) | Complaint within **1 month** of cause of action (expiry of 15 days); condonable | [IN FORCE] |
| ss.143A, 148 | Interim compensation up to 20%; appellate deposit ≥ 20% (LR-RBI-019) | [IN FORCE] |
| s.147 | Offence compoundable (LR-RBI-018) | [IN FORCE] |
| *Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158 (SC, 25 Sep 2025) | Compounding costs: before defence evidence nil; after defence evidence before judgment 5%; Sessions/HC 7.5%; SC 10%; online payment facility at summons stage | [IN FORCE] |
| *Meters and Instruments v Kanchan Mehta* (2018) 1 SCC 560 | Court may close proceedings where complainant duly compensated | [IN FORCE] |
| *K.N. Govindan Kutty Menon v C.D. Shaji* (2012) 2 SCC 51 | Lok Adalat award in a referred s.138 case is a deemed decree | [IN FORCE] |
| National Lok Adalat 2026 | 14 Mar, 9 May, 12 Sep, **12 Dec 2026** [V-secondary] | Directory data, re-verified per NALSA calendar |
| Equator boundary | Civil money settlement only; compounding/withdrawal decided by the court; never "closes" a criminal case; never threatens conviction (NN-24, VG-COM-08) | [POLICY] |

### 3.11 `com.reg` and `com.bfs` — exclusions and banking overlaps

| Matter | Rule | Equator behaviour |
|---|---|---|
| CCI (s.3 agreements, s.4 abuse, combinations, DG) | Competition Act s.61 civil-court bar; compensation via NCLAT s.53N; Mediation Act First Schedule item 8 (policy mirror); CCI Settlement/Commitment Regulations 2024 (ss.48A–48B) | Signpost; private contract layer may continue in its own L1; no settlement binds CCI |
| Consumer B2C | CPA 2019 s.2(7) (commercial-purpose exclusion; self-employment livelihood exception); ss.37, 74–81 mediation cells; CP (Mediation) Rules 2020 r.4 exclusions | Private mediation only on consent; never a precondition to Commission filing (LR-CONS-003/004/005) |
| Tax, SEBI/SAT, TRAI/TDSAT, electricity, PNGRB, NGT, land acquisition | Mediation Act First Schedule items 6–12 (policy mirror, LR-MED-009) | Signpost |
| Company-law offences, Chapter XIV investigation, SFIO | Non-referable (2016 Rules r.30); criminal | Hard block (NN-24) |
| Banks/FIs as claimants ≥ ₹20 lakh | RDB Act (LR-ARB-020) | → FIN; COM mediation only |
| NBFC lending to corporates | NBFC not an RDB "financial institution" unless notified under s.2(h)(ii) **[VERIFY — open: notified list]** | Arbitration permitted under NN-03 (clause at origination; no party nomination — repeat player) |

### 3.12 New Legal Rules Register entries required (proposed IDs; seed in Appendix G)

Appendix G §G.3 `area` CHECK must be extended with `IBC`, `CORP`, `RERA`, `PROC`, `PART` (ADR "Appendix G area extension"). Effect: P = protective, M = permissive, C = computational.

| Proposed ID | Rule statement (product-enforceable) | Source | Status | Effect | Enforcement | Verify |
|---|---|---|---|---|---|---|
| LR-IBC-001 | IBC application thresholds: CIRP default ≥ ₹1,00,00,000; PPIRP default ≥ ₹10,00,000 (MSME CD only). | IBC s.4; S.O. 1205(E), 24 Mar 2020; S.O. 1543(E), 9 Apr 2021 | IN_FORCE | C | `rules` CAL-COM-06 CFG | — |
| LR-IBC-002 | No Equator arbitration or award on insolvency, admission, claim admission (s.60(5)), resolution plans or liquidation; IBC L2s expose only negotiation/mediation of commercial terms. | *Indus Biotech* (2021) 6 SCC 436; *Vidya Drolia*; *Haryana Telecom* (1999) 5 SCC 688; D2-02 | IN_FORCE | P | `routing` HB (`COM_IBC_INREM`) | — |
| LR-IBC-003 | s.12A IBC withdrawal only on RP's application, 90% CoC voting share, after CoC constitution and before first invitation for resolution plans; NCLT decides in 30 days; platform blocks any "withdraw now" CTA outside the window. | IBC s.12A as substituted by IBC (Amendment) Act 2026 (Act 6 of 2026); S.O. 2625(E), 22 May 2026 (w.e.f. 26 May 2026) | IN_FORCE | P | `routing` HB (`COM_IBC_S12A_WINDOW_CLOSED`); clocks C | [Verified 22 Oct 2026: Act 6 of 2026 s.8; Gazette]; Reg 30A substituted by REG152, 1 Jun 2026 **[VERIFY — open: REG152 primary text]** |
| LR-IBC-004 | Pre-admission withdrawal by the applicant under r.8; NCLT must admit/reject FC applications within 14 days (s.7(5)); platform treats the pre-admission desk as urgent (≤ 10-day mediation). | IBC s.7(5) (substituted 2026); I&B (AAA) Rules 2016 r.8 | IN_FORCE | P | `clocks` C (`ibc_admit_fc`) | — |
| LR-IBC-005 | CD's reply to s.8 demand within 10 days of receipt; Equator mediation does not extend it; warn CD. | IBC s.8(2) | IN_FORCE | P | `clocks` C (`ibc_s8_reply`, owner = CD) | — |
| LR-IBC-006 | PPIRP eligibility and unrelated-FC approval threshold 51% (from 26 May 2026). | IBC ss.54A–54P; Amendment Act 2026 s.34 | IN_FORCE | C | CAL-COM-07 CFG | [Verified 22 Oct 2026: s.34(a)(iii) and (b); Gazette] |
| LR-IBC-007 | Liquidation 180 + 90 days; secured-creditor election 14 days; s.230 scheme within 90 days of liquidation order; voluntary liquidation ≤ 1 year and withdrawal under s.59(5A)–(5C). | IBC ss.52, 54, 59 (as amended 2026); Liquidation Regs Reg 2B | IN_FORCE | C | `clocks` C (tracking) | Reg 2B [Verified 22 Oct 2026: 30-day filing limit; REG151 proviso] |
| LR-IBC-008 | CIIRP (Ch. IV-A) not in force: information card only. | Amendment Act 2026 s.40 excluded from S.O. 2625(E) | NOT_IN_FORCE | P | flag `com.ciirp` OFF | — |
| LR-IBC-009 | Pre-s.9 private mediation report is not an IBBI regulatory report; footer mandatory; annexing to s.9 application only with debtor's written consent (mediation confidentiality). | IBBI Discussion Paper (≈4 Nov 2024) [DRAFT]; Equator Mediation Rules | IN_FORCE (policy) | P | `templates` footer HB | Not notified as of 22 Oct 2026 (draft Reg 2BA) [Watch: quarterly] |
| LR-IBC-010 | Personal guarantor: s.96 interim moratorium on filing of s.94/95 application; Equator proceedings against the guarantor go `on_hold` unless settlement is presented through the RP. | IBC ss.94–96 | IN_FORCE | P | `cases` HB | — |
| LR-CORP-001 | Oppression/mismanagement statutory reliefs (ss.241–242) and winding up are not arbitrable; SHA/JV contract claims severed and may be arbitrated. | Companies Act ss.241–242, 271; *Rakesh Malhotra* (Bom HC 2014); *Haryana Telecom* | IN_FORCE | P | `routing` HB (`NN06_NON_ARBITRABLE`) | — |
| LR-CORP-002 | s.244 eligibility computed from cap table (≥ 100 members or 1/10 of members, whichever less, or ≥ 1/10 issued capital); waiver is NCLT's. | Companies Act s.244 | IN_FORCE | C | CAL-COM-08 | — |
| LR-CORP-003 | s.442 panel membership is individual; Equator never represented as empanelled; s.442 track: Tribunal-fixed fee, 2016 Rules templates, 3 + 3 months, r.30 exclusions hard-blocked. | Companies Act s.442; Companies (Mediation and Conciliation) Rules 2016 rr.3–30 | IN_FORCE | P | `cms` copy lint HB; `billing` `fee_source = tribunal_order`; `clocks` C (`s442_clock`) | r.4 wording **[VERIFY — open]** |
| LR-RERA-001 | Homebuyer/allottee matters: RERA/Consumer signposting before any Equator rung; arbitration default OFF; informed post-dispute election only. | RERA ss.31, 71, 79, 88; *Imperia Structures*; *Newtech*; *Emaar MGF* | IN_FORCE | P | `routing` S + HB | — |
| LR-RERA-002 | Equator is not a RERA s.32(g) forum; association-sponsored hosting only with recorded State Authority recognition. | RERA s.32(g) | IN_FORCE | P | copy lint HB; flag `com.rera_forum_tieup` OFF | counsel Q6 |
| LR-RERA-003 | Refund/delay interest computed per State RERA Rules (default SBI highest MCLR + 2%, simple, from each payment to refund date), State-configurable. | State RERA Rules | IN_FORCE | C | CAL-COM-09 | **[VERIFY — open: per-State table]** |
| LR-PROC-001 | Government counterparty (Ministry/Dept/attached office/autonomous body/CPSE/PSB/government company): arbitration offered only if dispute value < ₹10,00,00,000 or a competent-authority approval reference is uploaded; mediated outcome is an HLC-ready proposal with status `pending_competent_authority_approval`. | DoE OM 3 Jun 2024 paras 7(ii), 7(iii), 7(vi)–(ix) | IN_FORCE (guidance) | P | `routing` HB (`COM_GOVT_ARB_APPROVAL_REQUIRED`); `outcomes` status | File no. **[VERIFY — open]** |
| LR-PART-001 | LLP partner disputes under the LLP agreement default to arbitration absent contrary agreement; the LLP may be joined as respondent. | LLP Act 2008 s.23, First Schedule para 14; *Kartik Radia v BDO India LLP*, 2025 SCC OnLine Bom 445 | IN_FORCE | M | `routing` CFG | Permissive — activate only after legal reviewer clears |
| LR-PART-002 | An unregistered firm may arbitrate though s.69 bars suits. | Partnership Act s.69; *Umesh Goel* (2016) 11 SCC 313 | IN_FORCE | M | `routing` CFG | Permissive — as above |
| LR-ARB-033 | IP: licence/royalty/assignment-term disputes arbitrable; grant, validity in rem, revocation, rectification, opposition not arbitrable. | *Vidya Drolia*; *Eros v Telemax* (Bom HC 2016) | IN_FORCE | P | `routing` HB (`COM_IP_REGISTRY_RELIEF`) | Eros citation **[VERIFY — open]** |
| LR-ARB-034 | Rent-control-protected tenancies not arbitrable; TPA commercial leases arbitrable. | *Vidya Drolia* (overruling *Himangni*) | IN_FORCE | P | `routing` HB | — |
| LR-MSME-009 | MSMED 2026 Council-referral track: activates only with S.O. reference commencing substituted s.18 and a Council listing/recognition of Equator as MSP/ADR service provider; clocks 90 d mediation from first appearance, 30 d arbitration referral, 90 d award from pleadings; s.19 deposit ≥ 50% release rule shown. | MSMED (Amendment) Act 2026; S.O. 5575(E), 12 Oct 2026 | NOT_IN_FORCE (s.18 commencement unverified) | M | flag `com.msefc_referral_msp` OFF | [Checked 22 Oct 2026: Mediation Act s.62 + Seventh Schedule, amended by Amendment Act s.8 — neither commenced; MSP recognition by MCI under Mediation Act s.40 (not in force; MCI established S.O. 4781(E), 27 Aug 2026)] |
| LR-MSME-010 | Private settlement shows full s.16 interest; any waiver or reduction must be an informed, express, separately initialled clause with counsel-review flag (s.16 non-obstante). | MSMED s.16 | IN_FORCE | P | `outcomes` HB (`COM_MSME_INTEREST_WAIVER_UNACKED`) | Validity of waiver **[VERIFY — open: counsel Q4]** |

---

## 4. Suitability and eligibility rules

### 4.1 Outcome codes
`ACCEPT` (all requested mechanisms available) · `ACCEPT_COND` (accepted with conditions listed in `conditions[]`) · `ACCEPT_PARTIAL` (some heads severed to signposting) · `SIGNPOST` (Equator does not administer; forum pack issued; voluntary mediation of a severable layer may be offered) · `REJECT` (hard exclusion; reason code; signposting still delivered) · `REROUTE_<VERT>` (case moved to FIN/FAM/WRK/INT before acceptance). Every outcome writes `core.signposting_events` where a forum is named (NN-20) and `equator.routing.triage.evaluated.v1`.

### 4.2 Decision table (evaluated top-down; all matching signposting rows delivered; first matching REJECT/REROUTE stops mechanism offers)

| # | Inputs (Explorer/intake fields) | Outcome | Routes offered | Routes blocked (code → canonical) | Signposting + last date |
|---|---|---|---|---|---|
| R-COM-00 | Any party foreign (place of business/nationality/habitual residence outside India) OR seat outside India | `REROUTE_INT` | per V6 | — | — |
| R-COM-01 | `claimant_type ∈ {bank, rdb_fi}` AND `amount ≥ rdb_threshold` (₹20,00,000) | `REROUTE_FIN` (or `ACCEPT_COND` mediation-only in COM if tenant has no FIN pack) | mediation, conciliation | arbitration (`FIN_DRT_EXCLUSIVE` → `CASE_NOT_ARBITRABLE`, LR-ARB-020) | DRT; Lok Adalat |
| R-COM-02 | Any criminal allegation is the relief sought (prosecution, FIR, punishment) or `C9 ∋ criminal_other` with non-compoundable offence | `REJECT` (criminal) — civil layer may proceed as `ACCEPT_PARTIAL` | civil money mediation only | all mechanisms on the offence (`NN24_CRIMINAL_EXCLUDED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`) | Police 112 / jurisdictional police; Magistrate; National Cybercrime Helpline 1930 for online fraud |
| R-COM-03 | `L1 = com.reg` | `SIGNPOST` | voluntary mediation of a severable contract layer in another L1 | arbitration, award | CCI; Consumer Commission (tier by consideration paid, LR-CONS-001; 2 years, LR-CONS-002); regulator/tribunal |
| R-COM-04 | `L1 = com.ibc` AND stage ≥ `admitted` | `ACCEPT_COND` | negotiation/mediation of commercial terms with RP/CoC engagement | arbitration (`COM_IBC_INREM` → `CASE_NOT_ARBITRABLE`, LR-IBC-002) | NCLT; RP claim filing (date from public announcement entered by CM) |
| R-COM-05 | `L1 = com.ibc` AND stage = `admitted` AND `coc_constituted = false` | `ACCEPT_COND` | settlement drafting only | "withdraw now" CTA (`COM_IBC_S12A_WINDOW_CLOSED`, LR-IBC-003) | Explainer: s.12A window opens on CoC constitution |
| R-COM-06 | `L1 = com.ibc` AND `form_g_issued = true` | `ACCEPT_COND` | resolution-plan negotiations only (s.29A check on promoters) | s.12A withdrawal pack | — |
| R-COM-07 | `L1 = com.ibc` AND `L2 = claim_dispute_with_rp` | `SIGNPOST` (+ mediation on RP consent) | mediation only if RP consents in writing | arbitration | NCLT s.60(5) |
| R-COM-08 | Debtor/respondent in CIRP or liquidation (IBBI/MCA status or declaration) AND claimant is not using `com.ibc` | `ACCEPT_COND` → case `on_hold.ibc_moratorium` | none against CD; guarantor track continues unless s.96 | all (`IBC_MORATORIUM` → `CLOSURE_BLOCKED`/hold) | RP claim (Form B/C/CA per CIRP Regs) |
| R-COM-09 | `supplier_udyam_category ∈ {micro, small}` AND `dues_overdue = true` AND claim under MSMED s.17 | `ACCEPT_COND` (R-MSME-1) | MSEFC card **first**; Equator negotiation + pre-MSEFC conciliation; Equator arbitration only on F-COM-26 informed election and no MSEFC reference | Equator arbitration once MSEFC reference exists (`COM_MSEFC_PENDING`, LR-MSME-003) | MSEFC via MSME ODR portal; 90 days; 75% pre-deposit; Sonali Power limitation note |
| R-COM-10 | `supplier_udyam_registered_on > contract_date` | `ACCEPT_COND` | as R-COM-09 with warning W-NBCC | — | NBCC reference pending note (LR-MSME-006) |
| R-COM-11 | `supplier_udyam_category = medium` | `ACCEPT` (B2B route) | B2B ladder | s.16 calculator (`COM_MSMED_NOT_ELIGIBLE`) | — |
| R-COM-12 | `suit_intended = true` AND commercial (CCA s.2(1)(c)) AND `specified_value ≥ ₹3,00,000` AND `urgent_interim_relief = false` AND no arbitration agreement | `ACCEPT_COND` (M-06) | voluntary pre-suit mediation or Part III conciliation now; Form-1 PIMS pack (F-COM-24) | any s.12A certificate/report (`COM_PIMS_CERT_NOT_ISSUABLE`, LR-MED-014) | DLSA/SLSA (or HC Legal Services Committee where State SOP provides); 3 + 2 months; limitation excluded during PIMS |
| R-COM-13 | `counterparty ∈ GOVT_SET` | `ACCEPT_COND` | `com.gov.v1`; arbitration only if `dispute_value < ₹10,00,00,000` or `approval_ref` uploaded | arbitration otherwise (`COM_GOVT_ARB_APPROVAL_REQUIRED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`, LR-PROC-001) | HLC of the entity; contract tier |
| R-COM-14 | `L2 = oppression_mismanagement` OR relief ∈ {winding_up, s241_relief, rectification_register} | `ACCEPT_PARTIAL` | mediation of whole dispute; s.442 card if NCLT pending; arbitration of SHA/JV heads | arbitration of statutory reliefs (`NN06_NON_ARBITRABLE`, LR-CORP-001) | NCLT; s.244 eligibility (CAL-COM-08) |
| R-COM-15 | `s442_reference = true` (order uploaded) | `ACCEPT_COND` | `com.s442.v1` | Equator fee card; Equator branding on outputs | NCLT/NCLAT r.26 hearing |
| R-COM-16 | s.442 track AND any r.30 category (serious fraud/forgery/impersonation/coercion; Chapter XIV; pending compounding; public interest/numerous non-parties) | `REJECT` (s.442 track) | — | s.442 mediation (`COM_S442_NOT_REFERABLE`) | Tribunal |
| R-COM-17 | `L2 ∈ {homebuyer_delay_refund, homebuyer_defects, allottee_collective}` | `ACCEPT_COND` | signposting first; negotiation, mediation; arbitration only on informed post-dispute election | arbitration default (`LR-CONS-003` → `CASE_NOT_ARBITRABLE`) | RERA Authority/AO (project registration no. + State); Consumer Commission; MahaRERA card if State = MH; NCLT if promoter in CIRP |
| R-COM-18 | `L2 = commercial_lease` AND `rent_control = yes` | `ACCEPT_PARTIAL` | mediation | arbitration (`LR-ARB-034`) | Rent Controller |
| R-COM-19 | Relief ∈ {revoke, rectify, oppose, declare invalid IP registration} | `ACCEPT_PARTIAL` | licence/royalty heads continue | registry heads (`COM_IP_REGISTRY_RELIEF`, LR-ARB-033) | IP Office; High Court (IP Division) |
| R-COM-20 | Allegation ∈ {cartel, abuse_of_dominance, rpm} | `ACCEPT_COND` (W-CCI) | private contract layer | — | CCI card |
| R-COM-21 | `cheque_dishonoured = true` | `ACCEPT_COND` | spawn linked `com.chq` case with NI clocks | arbitration of the offence (`NN24_CRIMINAL_EXCLUDED`) | Magistrate; Lok Adalat (next National Lok Adalat date) |
| R-COM-22 | Valid s.7 agreement naming Equator (or post-dispute submission agreement), arbitrable heads | `ACCEPT` | arbitration (standard/expedited/s.29B), EA, med-arb per clause | — | s.21 date recorded; limitation check |
| R-COM-23 | Agreement names another institution or ad hoc | `ACCEPT_COND` | Equator as appointing authority only if agreed; mediation/conciliation | administration under Equator Rules without fresh agreement (`COM_NO_ARB_AGREEMENT`) | Named institution |
| R-COM-24 | No arbitration agreement AND arbitration requested | `ACCEPT_COND` | post-dispute submission agreement (F-COM-41) e-signed by all parties | arbitration until signed (`COM_NO_ARB_AGREEMENT`) | — |
| R-COM-25 | `urgent_interim_relief = yes_within_days` | `ACCEPT_COND` (urgent) | EA (India seat, clause) and/or s.9 court card; expedited intake (U-flags) | — | Commercial Court s.9 (A&C); EA disclosure LR-ARB-025 |
| R-COM-26 | `party_type = individual consumer` (not commercial purpose) in any L1 | `REROUTE` to `com.reg.consumer_b2c` | mediation on consent | arbitration ousting consumer | Consumer Commission |
| R-COM-27 | Individual employee claims (wages, termination) mixed in founder/ESOP dispute | `ACCEPT_PARTIAL` + link `WRK` case | COM for shareholder heads | arbitration of workman/statutory heads (WRK rules) | WRK forums |
| R-COM-28 | Personal property/succession heads in family business | `ACCEPT_PARTIAL` + link `FAM` case | COM for company heads | — | FAM forums |
| R-COM-29 | Limitation computed expired (CAL-COM-04) | `ACCEPT_COND` | negotiation/conciliation only (time-barred debt can be settled; MSEFC conciliation not time-barred per *Sonali Power*) | arbitration requires counsel-review acknowledgement (W-LIMITATION) | Show computation and "Equator does not decide limitation" |
| R-COM-30 | Party lacks authority (no board resolution/PoA) at settlement stage | `ACCEPT_COND` | proceed to sessions | settlement signature (`COM_SIGNATORY_AUTHORITY_MISSING` → `CLOSURE_BLOCKED`) | — |
| R-COM-31 | Allegation of serious fraud/forgery/impersonation/coercion (outside s.442) | `ACCEPT_COND` (LR-MED-017 registrar review) | mediation after registrar review; arbitration (fraud arbitrable unless it vitiates agreement) | — | Police if crime reported |
| R-COM-32 | Default — no earlier row produced a REJECT, REROUTE or SIGNPOST (e.g., no arbitration agreement, no suit intended or claim below the specified value, arbitration not requested) | `ACCEPT` | ladder for the L1 per §2.3 (negotiation → mediation / Part III conciliation); fresh post-dispute arbitration agreement (F-COM-41) offered as an option | — | Civil/commercial court and Limitation Act article from CAL-COM-04; Lok Adalat / DLSA *(v3.1: closes the gap in which such matters matched no row — FR-P08-85)* |

### 4.3 Reference sets (configuration)
- `GOVT_SET` = {central_ministry, central_department, attached_office, subordinate_office, autonomous_body, cpse, psb, public_financial_institution, government_company, state_department, state_psu, ulb_municipal, development_authority}. DoE OM binds central entities; State entities shown as "check your State's procurement guidelines" **[VERIFY — open: State adoption]**.
- `CRIMINAL_EXCLUDED` (NN-24, Appendix K §3): non-compoundable offences; fraud/forgery/cheating prosecutions; SFIO/Chapter XIV; any matter needing urgent police/court protection; threats of violence.
- `IN_REM_SET`: insolvency/liquidation/winding up; oppression reliefs; IP grant/validity; rent-control eviction; CCI; tax; SEBI/SAT; regulator penalties; land acquisition.

### 4.4 Hard exclusions (always `REJECT` or severance, never configurable)
1. Criminal proceedings or mediation of an offence (NN-24) — cheque matters limited to civil money and compounding papers.
2. Awards on in-rem matters (`IN_REM_SET`) (NN-06, LR-ARB-019, LR-IBC-002, LR-CORP-001, LR-ARB-033/034).
3. s.12A PIMS conducted by Equator or any representation that Equator's report satisfies s.12A (M-06).
4. Party nomination of arbitrators outside `equal_footing = true` COM matters (NN-03); any enterprise/lender selection or veto.
5. Bank/FI debts ≥ ₹20 lakh in arbitration (LR-ARB-020).
6. Consumer/homebuyer forced arbitration (LR-CONS-003).
7. Equator arbitration of an MSMED claim once an MSEFC reference exists (LR-MSME-003).
8. s.442 r.30 categories.

### 4.5 Urgent and safety triggers (set `urgency_level` and CM task within 4 working hours)

| Code | Trigger | Action |
|---|---|---|
| U-01 | IBC s.8 notice received; reply due within 10 days | Fast mediation offer (≤ 7 d); warn CD reply must be sent anyway; `ibc_s8_reply` owner = CD |
| U-02 | s.7/s.9 filed, hearing within 14 days | IBC Settlement Desk fast lane; r.8 withdrawal memo draft |
| U-03 | BG invocation/encashment imminent (K8) | EA (if clause) and s.9 court card; no promise of stay |
| U-04 | NI Act 15-day pay window open | Payment-link negotiation within window; complaint deadline shown |
| U-05 | Limitation < 30 days (CAL-COM-04) | Red banner: "Equator process does not stop limitation"; standstill agreement only if `com.standstill_template` ON (counsel Q-C1) |
| U-06 | Asset dissipation/insolvency risk declared | EA/s.9 card; escrow-first settlement structure |
| U-07 | s.29A expiry ≤ 60 days | AP-29A blocking task |
| U-08 | Threats, intimidation or violence reported | Stop joint sessions; police signpost; registrar review (NN-24) |
| U-09 | Data breach ongoing (`com.tech.data_breach_contractual`) | CERT-In 6-hour reporting card (CERT-In Directions 28 Apr 2022) and DPB card; Equator does not file |

### 4.6 Jurisdiction and seat
- Domestic COM: all parties have their place of business in India; seat in India (city list DD-COM-SEAT). GIFT IFSC seat is an Indian seat (Part I) — allowed in COM where all parties are Indian; IFSC tax treatment flag `tax.ifsc_zero_rating` OFF (Appendix B `T08_IFSC`).
- Territorial facts captured for signposting: supplier's location (MSEFC jurisdiction), project location (RERA), registered office of CD (NCLT bench), place of contract/performance (Commercial Court), drawee bank branch / payee's account branch (NI Act s.142(2)).

### 4.7 Limitation checks (CAL-COM-04 runs at intake; results shown, never decided)

| Situation | Article / rule | Start | Period | Notes |
|---|---|---|---|---|
| Price of goods (credit) | Art. 14 | Expiry of credit period | 3 y | s.18 acknowledgement / s.19 part-payment restart |
| Breach of contract | Art. 55 | Breach | 3 y | Continuing breaches: each breach |
| Residuary/declarations | Art. 113 / 58 | Right to sue accrues | 3 y | |
| Partnership accounts | Art. 5 | Dissolution | 3 y | |
| IBC application | Art. 137 | Date of default | 3 y | *B.K. Educational Services* |
| s.11 appointment | Art. 137 | Failure/refusal after s.21 notice | 3 y | *Arif Azim* |
| MSEFC conciliation | — | — | not applicable | *Sonali Power* |
| MSEFC arbitration | A&C s.43 + relevant Article | as per claim | 3 y | *Sonali Power* |
| NI Act complaint | s.142(1)(b) | Expiry of 15-day pay window | 1 m | Condonable by court |
| Consumer (homebuyer) | CPA s.69 | Cause of action | 2 y | LR-CONS-002 |
| PIMS exclusion | CCA s.12A(3) | Form-1 application → Authority's report | excluded | Inclusive-days convention configurable |
| Foreign/domestic award execution | Art. 136 (domestic, HC line) / Art. 137 (foreign — *Government of India v Vedanta* (2020) 10 SCC 1) | Enforceability | 12 y / 3 y | Informational |

---

## 5. Dispute Explorer question tree (COM)

Plain English, ≤ class-8 reading level; Hindi parity mandatory (NN-23). Deterministic (NN-01/NN-02): the AI assistant may rephrase and classify but the tree and outcomes come from the rules engine. Each L1 module starts after the common core. Answers map to intake fields (`maps_to`).

### 5.1 Common core (all COM)

| QID | Question text | Options (value) | Branching | Outcome codes / effects |
|---|---|---|---|---|
| CQ-01 | Is this dispute about a business deal, a business, or business money? | Yes (`yes`) · No, it is personal or family (`no_personal`) · Not sure (`unsure`) | `no_personal` → Explorer root (FAM/FIN/INS/WRK); `unsure` → continue at CQ-02 with `vertical_uncertain = true` (the classifier may reroute after CQ-06) *(v3.1)* | — |
| CQ-02 | Who are you in this dispute? | I want money or action from the other side (`claimant`) · The other side wants something from me (`respondent`) · Both of us want to settle together (`joint`) · I am an adviser for one side (`adviser`) | — | role |
| CQ-03 | What kind of business is your side? | Company · LLP · Registered partnership firm · Unregistered partnership firm · Sole proprietor · Individual · Government office · Government company or PSU · Bank or financial institution · NBFC · Trust or society · Foreign business | `foreign` → R-COM-00; `bank` → R-COM-01 check | entity_type |
| CQ-04 | What kind of business is the other side? | same list | `government*` → GOVT_SET flag; `foreign` → R-COM-00 | counterparty_type |
| CQ-05 | Is any person or business involved based outside India? | No · Yes · Not sure | `yes` → R-COM-00 | `REROUTE_INT` |
| CQ-06 | What is this mainly about? | Supply, sale, services, distribution, franchise or agency (`b2b`) · Construction or a project (`con`) · Software, IT, data or IP licence (`tech`) · Property, flats, land development or lease (`re`) · Partnership firm or LLP (`part`) · Company shares, JV or founders (`corp`) · Insolvency, NCLT or restructuring (`ibc`) · Unpaid bills to a micro or small business (`msme`) · A bounced cheque (`chq`) · Bank guarantee, LC, factoring or business loan (`bfs`) · Competition, consumer or regulator issue (`reg`) | → L1 module | L1 |
| CQ-07 | Is someone threatening you, or has a crime been committed? | No · Yes, threats or violence · Yes, I want police action or punishment · Only a bounced cheque | `threat`/`police` → R-COM-02; `cheque` → CQ-06 = `chq` | NN-24 |
| CQ-08 | About how much money is involved? | Amount in ₹ (currency field) · I don't know yet | — | `amount_minor`; thresholds |
| CQ-09 | Is there a written contract? | Signed contract · Purchase order and invoices · Only emails or WhatsApp · Spoken agreement · Not sure | `PO` → W-INCORP | contract_basis |
| CQ-10 | Does the contract say how disputes will be settled? | Arbitration · Mediation · Talks between senior people first · Expert decides · Dispute board · Only courts · Nothing · Not sure (upload it) | `arbitration` → CQ-11; `not sure` → clause parser (AI extract, human confirm) | clause flags |
| CQ-11 | Does the clause name an institution? | Equator · Another institution (name) · No institution (ad hoc) · Not sure | `other` → R-COM-23 | `named_institution` |
| CQ-12 | Has any case already been filed anywhere? | None · Civil/commercial court · Court case for urgent orders (s.9) · Arbitration · NCLT (insolvency) · NCLT (company case) · RERA · Consumer Commission · MSEFC/MSME ODR · Cheque case in Magistrate court · DRT · Police complaint/FIR | multi; FIR → CQ-07 re-check | `parallel_proceedings[]` |
| CQ-13 | Do you need urgent protection in the next few days? (for example, stopping a bank guarantee, freezing money, stopping use of your data) | Yes, within days · Maybe · No | `yes` → R-COM-25 | `urgent_interim_relief` |
| CQ-14 | When did the problem start? When did they last pay or accept the debt in writing? | Dates | → CAL-COM-04 | limitation result |
| CQ-15 | What result do you want? | Payment · Interest · Continue the contract · Exit on agreed terms · New price or scope · Return of goods, data, code or documents · Apology · More time to pay · Share buy-out · Settlement of a NCLT/IBC case | multi | outcome prefs |
| CQ-16 | Which way do you prefer to resolve this? | Let Equator suggest · Talks only (negotiation) · Mediation · Conciliation with award-like status · Arbitration · Expert decision | — | `preferred_mechanism` |

### 5.2 L1 modules

**B2B (`com.b2b`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| BQ-01 | What is the main problem? | Unpaid invoices · Short payment or deductions · Goods rejected for quality · Late or no delivery · Contract ended wrongly · Territory or exclusivity broken · Targets or incentives · Taking back stock · Security deposit not returned · Non-compete or poaching · Brand or IP used after exit · Other | → L2 classifier |
| BQ-02 | Did the buyer complain in writing about quality or quantity? When? | No complaint · Within 15 days of delivery · After 15 days · Not applicable (services) | feeds MSMED deemed acceptance |
| BQ-03 | Is the relationship still going on? | Yes · Paused · We ended it · They ended it | ladder choice (relationship-preserving options) |
| BQ-04 | Is the supplier registered on Udyam as micro or small? | Micro · Small · Medium · Not registered · Don't know | micro/small → MSME module (R-COM-09); don't know → Udyam verify |
| BQ-05 | Was a cheque given and bounced? | Yes (date of bank memo) · No | yes → R-COM-21 |
| BQ-06 | Is the other side a government office, PSU or government company? | Yes · No | yes → R-COM-13 |
| BQ-07 | Is there an exclusive-dealing or resale-price clause, and does the other side dominate the market? | Yes · No · Not sure | yes → R-COM-20 |

**Construction (`com.con`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| KQ-01 | Who is the project owner (employer)? | Private developer · Central Ministry/Department · State Department · CPSE/PSU · Municipal body · PPP company · Main contractor (I am a sub-contractor) | government → R-COM-13 |
| KQ-02 | What type of contract? | Item rate · Lump sum/EPC · HAM · BOT/toll · FIDIC Red/Yellow/Silver · Model Concession Agreement · Other | form defaults |
| KQ-03 | What are you claiming? (choose all) | Unpaid running bills · Final bill · Retention · Price variation · Extra items/variations · Idle/prolongation costs · LD wrongly deducted · Time extension refused · BG wrongly invoked · Termination · Defects (counter-claim) · Interest | heads table |
| KQ-04 | Does the contract need an Engineer, Dispute Board or committee step first? | Engineer · Dispute Board · Conciliation committee · Senior management meeting · None | tier check |
| KQ-05 | Where is that step now? | Not started · Ongoing · Decision received (date) · Time ran out | tier status; W-TIER |
| KQ-06 | For government projects: is the amount in dispute below ₹10 crore? | Below ₹10 crore · ₹10 crore or more | ≥ → arbitration needs approval (LR-PROC-001) |
| KQ-07 | Is the project still running? | Yes · Completed · Terminated · Abandoned | — |
| KQ-08 | Is a bank guarantee about to be encashed? | Yes (date) · No | yes → U-03 |

**Technology and IP (`com.tech`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| TQ-01 | What kind of service or product? | Custom software · SaaS subscription · Managed services/outsourcing · System integration · Licensed software · API or data supply · IP licence (trade mark/patent/copyright/know-how) | L2 |
| TQ-02 | What went wrong? | Not paid · Milestones missed · Failed acceptance tests · SLA breach · Data loss or breach · Exit and handover · Who owns the IP · Royalty short-paid · Poaching/non-compete · Escrow release | L2 |
| TQ-03 | Is personal data involved? | Personal data · Confidential business data · None | personal → DPDP card; U-09 if ongoing breach |
| TQ-04 | Do you need data or source code returned or deleted? | Yes · No | output template |
| TQ-05 | Do you want an IP registration cancelled, corrected or opposed? | No · Yes | yes → R-COM-19 |
| TQ-06 | How sensitive is the information? | Normal · High (prices, trade secrets) · Very high (source code, deal terms) | confidentiality ring level |

**Real estate (`com.re`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| RQ-01 | Who are you? | Flat or plot buyer · Builder/developer · Landowner (joint development) · Landlord · Tenant · Broker · RWA/society | buyer → R-COM-17 |
| RQ-02 | Is the project registered with RERA? | Yes (enter number and State) · No · Exempt (small project) · Don't know | RERA card with State |
| RQ-03 | What is the problem? | Delay in possession · Refund after cancelling · Defects · Smaller carpet area · Plan changed without consent · Hidden charges · Handover to society · Joint development share · Rent not paid · Lock-in/exit · Security deposit · Brokerage not paid | L2 |
| RQ-04 | Why did you buy? | To live in · Investment or business use | business → consumer standing warning |
| RQ-05 | Is any case already filed? | RERA complaint · RERA compensation (AO) · Consumer complaint · NCLT (builder insolvent) · Civil suit · None | parallel |
| RQ-06 | What result do you want? | Possession with delay interest · Refund with interest · Repairs · Other unit · Compensation · Exit from JDA with share | outcome |
| RQ-07 | (Lease only) Is the lease covered by a State Rent Control Act? | Yes · No · Don't know | yes → R-COM-18 |

**Partnership and LLP (`com.part`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| PQ-01 | What type of business? | Registered firm · Unregistered firm · LLP · Professional firm (CA/law/doctors/other) | unregistered → LR-PART-002 note |
| PQ-02 | What is the dispute about? | Closing the firm · Exit payout · Expulsion · Profit share or capital · Accounts or mismanagement · Competing business · New partner · Deadlock · A partner died (heirs' claim) | death → FAM link (R-COM-28) |
| PQ-03 | Should the business continue? | Yes, with a buy-out · Split clients/assets · Close it | — |
| PQ-04 | How should value be worked out? | Book value · Fair value by registered valuer · Formula in deed · Let mediator suggest options | CAL-COM-16 |
| PQ-05 | What does the deed say about disputes? | Arbitration · LLP default rule (arbitration) · Nothing | LR-PART-001 |

**Company, JV and founders (`com.corp`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| SQ-01 | What type of company? | Private · Public unlisted · Listed · Section 8 · Has foreign investors | listed → LODR card; foreign investor → INT check |
| SQ-02 | What do you hold? | % shares, class, director yes/no | CAL-COM-08 |
| SQ-03 | What is the problem? | Board control/deadlock · Removed as director · Dilution/rights issue · Money siphoned/related-party deals · Information denied · Dividends · Founder exit/vesting/bad leaver · ESOP cancelled · Put/call price · Drag/tag/ROFR · JV ending · Family business split | oppression signals → R-COM-14 |
| SQ-04 | Do you hold at least 10% of shares, or are you at least 1 in 10 members (or 100 members)? | Yes · No · Don't know | CAL-COM-08 |
| SQ-05 | Is a case already filed? | None · NCLT oppression case · Arbitration started · Civil suit · SEBI complaint | NCLT → s.442 option (SQ-08) |
| SQ-06 | What result do you want? | Buy-out · Sell-out · Governance reset · Split assets/demerger · Close company · Status quo with information rights | — |
| SQ-07 | How should shares be valued? | Registered valuer fair value · SHA formula · DCF/NAV/comparables · Last funding round · Let mediator suggest options | expert determination offer |
| SQ-08 | (If NCLT case pending) Would you like NCLT to refer this to its mediation panel? | Yes · No, use private Equator mediation · Not sure | yes → s.442 information + MDC-2 guidance |

**Insolvency (`com.ibc`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| IQ-01 | Who are you? | Supplier/service provider owed money (operational creditor) · Lender or bondholder (financial creditor) · The company that owes (corporate debtor/promoter) · Personal guarantor · Bidder (resolution applicant) · Resolution professional/liquidator · Employee | role |
| IQ-02 | What stage is it at? | No notice yet · Demand notice under s.8 sent (date) · Case filed at NCLT, not admitted (date, number) · Admitted (date) · Creditors' committee formed (date) · Invitation for plans (Form G) issued (date) · Plan approved · Liquidation ordered (date) · Voluntary liquidation | → R-COM-04/05/06 |
| IQ-03 | Total unpaid amount (default)? | ₹ | CAL-COM-06 (₹1 crore / ₹10 lakh) |
| IQ-04 | Is the company that owes an MSME? | Micro · Small · Medium · No · Don't know | pre-pack eligibility |
| IQ-05 | Is the debt recorded with an Information Utility (NeSL)? | Record of default (authenticated) · Marked disputed · Not filed | IU guidance |
| IQ-06 | How would a settlement be paid? | Lump sum · Instalments with escrow · Shares · Asset transfer · Promoter or related party pays · Interest waiver · Mixed | settlement shape |
| IQ-07 | Who must approve? | Only the applicant · Creditors' committee (90%) · Board/shareholders · Lenders' group | approval matrix |

**MSME (`com.msme`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| MQ-01 | Enter your Udyam number | `UDYAM-XX-00-0000000` | Udyam verify (aggregator) |
| MQ-02 | Category on the date of the contract/order | Micro · Small · Medium · Not registered then | medium → R-COM-11; later registration → R-COM-10 |
| MQ-03 | Who is the buyer? | Government · CPSE/PSU · Private company · Other business | GOVT_SET; TReDS note |
| MQ-04 | Add each unpaid invoice (number, date, amount, delivery date, objection date if any, agreed credit days) | table | CAL-COM-01 |
| MQ-05 | Any part-payments? (date, amount) | table | interest allocation |
| MQ-06 | Have you already filed with MSEFC or the MSME ODR portal? | No · Yes (reference number) | yes → R-COM-09 block arbitration |
| MQ-07 | Was any invoice discounted on TReDS? | Yes · No | factoring link |

**Cheque (`com.chq`)**

| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| QQ-01 | Cheque number, date, amount and bank | fields | — |
| QQ-02 | Date of the bank's return memo and the reason | date + reason dropdown (DD-COM-CHQ-REASON) | `ni138_notice_30d` |
| QQ-03 | Did you send a legal notice? When did they receive it? | Not yet · Sent (date received) | `ni138_pay_15d`, `ni138_complaint_1m` |
| QQ-04 | Has a cheque case been filed? Stage? | Not filed · Before summons · Summons served · Complainant evidence · Defence evidence · Judgment · Appeal/revision in Sessions or High Court · Supreme Court | CAL-COM-10 |
| QQ-05 | What was the cheque for? | Payment for supply · Loan · Security cheque · Other | linked B2B case |

**Unresolved path (v3.1).** If a module's L2 classifier returns confidence below 0.6, or the user picks "Other" with no further match, the Explorer ends in Appendix K RES-08 `HUMAN_REVIEW`: answers saved, free 10-minute process call-back offered, case-manager triage within 2 working days, and the generic signposting of R-COM-32 shown meanwhile; no COM path ends without a route, a signpost or a named next step (FR-P08-85).

**Banking/finance B2B (`com.bfs`)** — FQ-01 Claimant type (bank/FI/NBFC/business) → R-COM-01; FQ-02 Instrument (BG/LC/facility/factoring/derivative); FQ-03 Is the borrower an individual or MSME borrowing for business? → FIN reroute; FQ-04 Default amount ≥ ₹1 crore? → NCLT card.

**Competition/consumer/regulator (`com.reg`)** — GQ-01 Which issue? (cartel/abuse, consumer complaint, tax, SEBI, telecom, electricity, environment, company-law offence) → SIGNPOST with forum card; GQ-02 Is there also an ordinary contract dispute you want to settle? → spawn other L1 module.

### 5.3 Free-forum disclosures (shown verbatim; versioned `script_version`; never removable)

| Code | Trigger | Disclosure text (EN; HI parity) |
|---|---|---|
| FD-COM-01 | R-COM-12 | "For commercial suits worth ₹3 lakh or more without urgent relief, the law requires pre-institution mediation through the Legal Services Authority (Commercial Courts Act, section 12A). Equator can prepare your application and can mediate privately before or alongside it, but Equator's report does not replace the Authority's report." |
| FD-COM-02 | R-COM-09 | "As a registered micro or small supplier, you can file with the MSME Facilitation Council through the government's MSME ODR portal. The buyer must pay interest at three times the RBI Bank Rate. You keep this right if you try Equator first." |
| FD-COM-03 | R-COM-17 | "Homebuyers can complain to the State RERA Authority or the Consumer Commission. An arbitration clause in your builder agreement does not stop you from going there." |
| FD-COM-04 | R-COM-04..07 | "Insolvency cases are decided only by the NCLT. Equator can help both sides settle, but the NCLT decides admission and withdrawal." |
| FD-COM-05 | R-COM-14 | "Reliefs for oppression and mismanagement are decided only by the NCLT. Equator can mediate the whole dispute and, if your contract allows, arbitrate the shareholder-agreement claims." |
| FD-COM-06 | R-COM-21 | "A cheque case is a criminal case. Equator does not decide it. Equator can help settle the money; only the court can close the case." |
| FD-COM-07 | R-COM-13 | "Government bodies follow the Department of Expenditure guidelines of 3 June 2024. Any settlement needs approval by the competent authority before it binds the government." |
| FD-COM-08 | R-COM-03/20 | "Competition matters are decided by the Competition Commission of India. Equator can only help with your ordinary contract issues." |
| FD-COM-09 | every invitation | "This invitation does not stop limitation periods running." (v3.1: the clause "unless both parties sign a standstill agreement" is shown only while `com.standstill_template` is ON after counsel sign-off, Q-C1 — it implied a remedy whose validity is still open) |
| FD-COM-10 | R-COM-01 | "Banks and financial institutions recover debts of ₹20 lakh or more through the Debt Recovery Tribunal; arbitration is not available for those claims." |

---

## 6. Intake and submission forms per mechanism

### 6.1 Form resolution and catalogue

**Resolution rule (Appendix K §4).** `form_schema = resolve(vertical = COM, l1, l2, mechanism, role, stage)`: the base mechanism form (§6.3–6.6) + the shared blocks (§6.2) + the L1 extension block (§6.7) + any L2 overrides (listed in the block) + vertical-specific forms triggered by routing (§6.8). Schemas are JSON-schema in the P02 form engine (`sensitive`, `visibleWhen`, `requiredWhen`, `mapsTo`), EN + HI, versioned and pinned (NN-21). `required` values: **Y** required · **C** conditionally required (`requiredWhen` given) · **N** optional.

| Form ID | Title | Mechanism | Disposition (FR-P08-07) | Trigger |
|---|---|---|---|---|
| F-COM-01 | KYB, authority & consent — COM block | all | CORE+EXT | every party |
| F-COM-02 | Request for Arbitration (v2) | arbitration | VERTICAL | claimant |
| F-COM-03 | Response to RFA + Counterclaim (v2) | arbitration | VERTICAL | respondent |
| F-COM-04 | Request for Mediation / Conciliation (v2) | mediation, conciliation | VERTICAL | claimant/joint |
| F-COM-09 / 10 | Statement of Claim / Statement of Defence & Counterclaim | arbitration | CORE+EXT | per PO1 |
| F-COM-11 | Interim measures & Emergency Arbitrator application (v2) | arbitration/EA | VERTICAL | urgency |
| F-COM-21 | Challenge to arbitrator | arbitration | VERTICAL | party |
| F-COM-22 | Joinder/consolidation | arbitration | VERTICAL | party |
| F-COM-24 | s.12A PIMS Form-1 Application Pack | signposting | VERTICAL → PDF | R-COM-12 |
| F-COM-26 | MSEFC election & informed-choice record | signposting | VERTICAL | R-COM-09 |
| F-COM-27 | Negotiation Request (new) | negotiation | VERTICAL | claimant/joint |
| F-COM-28 | Response to Invitation (mediation/conciliation/negotiation) (new) | all consensual | VERTICAL | respondent |
| F-COM-29 | IBC Settlement Desk intake + r.8 withdrawal memo (new) | negotiation/mediation | VERTICAL | `com.ibc` pre-admission |
| F-COM-30 | s.12A IBC withdrawal support annex (new) | mediation | VERTICAL | R-COM-05 window open |
| F-COM-31 | PPIRP pre-filing pack (new) | negotiation | VERTICAL | `com.ibc.prepack_msme` |
| F-COM-32 | HLC-ready settlement proposal (new) | mediation | VERTICAL → PDF | R-COM-13 |
| F-COM-33 | s.442 reference record (new) | mediation (panel) | VERTICAL | R-COM-15 |
| F-COM-34 | RERA settlement memo (new) | mediation | BUILDER `TPL-COM-S06` | `com.re` homebuyer |
| F-COM-35 | Cap table & valuation inputs (new) | all (corp) | VERTICAL (tier High) | `com.corp` |
| F-COM-36 | Co-arbitrator nomination (equal footing) (new) | arbitration | VERTICAL | `equal_footing = true` |
| F-COM-37 | Procedure election — expedited / s.29B / documents-only / three-member (new) | arbitration | VERTICAL | RFA/Response |
| F-COM-38 | Consent award request (new) | arbitration/AMA | VERTICAL | settlement in arbitration |
| F-COM-39 | Cheque settlement & compounding memorandum (COM) (new) | negotiation/mediation | VERTICAL | `com.chq` |
| F-COM-40 | Third-party funding & relevant-persons disclosure (new) | arbitration (all), mediation (opt.) | VERTICAL | filing and on change |
| F-COM-41 | Post-dispute submission agreement (new) | arbitration | VERTICAL (e-sign each party) | R-COM-24 |

### 6.2 Shared blocks

**BLK-PARTY (in F-COM-01; one per party).**

| field_id | label | type | req | options / dropdown | validation | help text |
|---|---|---|---|---|---|---|
| `party.role` | Your role | select | Y | DD-COM-ROLE | — | "Claimant asks for something; respondent is asked." |
| `party.entity_type` | Type of entity | select | Y | DD-COM-ENTITY | — | — |
| `party.legal_name` | Legal name | text | Y | — | 2–200 chars; must match MCA/GSTN record where verified | As on registration certificate |
| `party.cin` | CIN | text | C | — | `^[LU][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$`; requiredWhen entity_type ∈ {company, government_company} | 21 characters |
| `party.llpin` | LLPIN | text | C | — | `^[A-Z]{3}-[0-9]{4}$`; requiredWhen llp | — |
| `party.gstin` | GSTIN | text | N | — | 15 chars, state code 01–38, checksum | Verified via GSTN aggregator |
| `party.pan` | PAN | text | C | — | `^[A-Z]{5}[0-9]{4}[A-Z]$`; masked display | Required for invoices/TDS |
| `party.udyam_no` | Udyam registration number | text | C | — | `^UDYAM-[A-Z]{2}-[0-9]{2}-[0-9]{7}$`; requiredWhen msme claim | — |
| `party.udyam_category` | Udyam category | select | C | micro · small · medium | from certificate; verify | Category on contract date asked separately |
| `party.udyam_registered_on` | Udyam registration date | date | C | — | ≤ today | Drives *Silpi*/*NBCC* warning |
| `party.firm_registered` | Is the firm registered with the Registrar of Firms? | select | C | yes · no · not_sure | requiredWhen partnership | Unregistered firms can still arbitrate |
| `party.registered_address` | Registered/principal address | address | Y | State dropdown DD-STATE | PIN 6 digits | For notices and jurisdiction |
| `party.signatory_name` | Authorised signatory | text | Y | — | — | — |
| `party.signatory_designation` | Designation | text | Y | — | — | — |
| `party.authority_doc` | Authority document | file | C | board_resolution · poa · partner_authority · llp_resolution · govt_sanction_order | PDF ≤ 20 MB; requiredWhen settlement or e-sign of agreement | Needed before you sign any settlement |
| `party.authority_limit_minor` | Settlement authority limit | money | N | — | ≥ 0 | Above this, your approver signs (NN-27) |
| `party.representative` | Representative | ref | N | counsel · authorised_representative | LoA/Vakalatnama e-signed (App. S §4) | — |
| `party.contact_email` / `party.contact_mobile` | Contact | email/phone | Y | — | OTP-verified | — |
| `party.kyb_status` | KYB status | system | — | pending · verified · failed · manual_review | `KYC_PORT` | — |

**Pre-fill (v3.1; FR-P08-86).** A verified CIN/LLPIN or GSTIN fills `party.legal_name`, `party.registered_address` and State (MCA/GSTN aggregator via `KYC_PORT`), and a verified Udyam number fills `party.udyam_category` and `party.udyam_registered_on`; the user confirms the block and edits only what differs (edits to verified values set `kyb_status = manual_review`). An uploaded contract fills `clause.*` and `dispute.contract_basis` through `document_extractor` with page anchors; uploaded invoices fill the MQ-04 / EXT-MSME invoice table. Fields answered in the Explorer (CQ-01 to CQ-16 and the L1 module) are not asked again.

**BLK-DISPUTE.**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `dispute.l1` | Category | select | Y | DD-COM-L1 | — | — |
| `dispute.l2` | Sub-type | select | Y | DD-COM-L2[l1] | — | — |
| `dispute.sector` | Sector | select | Y | DD-COM-SECTOR | — | — |
| `dispute.summary` | What happened (short) | textarea | Y | — | 50–2,000 chars; AI may assist (NN-25 anchors) | Neutral words; no insults |
| `dispute.amount_principal_minor` | Principal amount | money (INR) | C | — | ≥ 0; requiredWhen money relief | — |
| `dispute.amount_includes_interest` | Does this include interest? | bool | C | — | — | — |
| `dispute.interest_claimed` | Interest claimed | group | N | basis DD-COM-INTEREST-BASIS; rate %; from date | 0–60% | Tribunal/court decides; calculator indicative |
| `dispute.relief[]` | Result wanted | multiselect | Y | DD-COM-RELIEF | ≥ 1 | — |
| `dispute.contract_basis` | Contract basis | select | Y | DD-COM-CONTRACT-BASIS | — | — |
| `dispute.contract_doc` | Contract upload | file | C | — | PDF/DOCX; requiredWhen signed_contract | Hash recorded (NN-10) |
| `dispute.cause_of_action_date` | When did the dispute start? | date | Y | — | ≤ today | — |
| `dispute.last_acknowledgement_date` | Last written acknowledgement/payment | date | N | — | ≤ today | Limitation Act ss.18–19 |
| `dispute.urgent_interim_relief` | Need urgent protection? | select | Y | yes_within_days · possibly · no | — | s.12A exemption, EA, s.9 |
| `dispute.counterparty_government` | Other side is government/PSU? | system/bool | Y | — | derived from entity_type | DoE track |
| `dispute.criminal_flag` | Crime or threat involved? | select | Y | none · threats · police_action_sought · cheque_only | — | NN-24 |
| `dispute.confidentiality` | Sensitivity | select | Y | normal · high · very_high | — | Sets confidentiality ring |
| `dispute.languages[]` | Languages | multiselect | Y | DD-LANG | ≥ 1 | — |
| `dispute.mode` | Mode | select | Y | online · hybrid · in_person | in_person → city | Online by default |

**BLK-CLAUSE.**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `clause.types[]` | Dispute clause types | multiselect | Y | DD-COM-CLAUSE-TYPE | — | — |
| `clause.text` | Clause text | textarea/extract | C | — | requiredWhen any type ≠ none; AI extract with human confirm | — |
| `clause.institution` | Institution named | select | C | DD-COM-INSTITUTION | — | — |
| `clause.seat_city` / `clause.venue_city` | Seat / venue | select | C | DD-COM-SEAT | seat ≠ venue allowed | Video hearings do not change the seat |
| `clause.governing_law` | Governing law | select | C | indian_law · other (→ INT) | — | — |
| `clause.panel_size` | Number of arbitrators | select | C | 1 · 3 · silent | — | — |
| `clause.tiered_steps[]` | Steps before arbitration | multiselect | N | senior_management · mediation · dispute_board · engineer · conciliation_committee | with time limits (days) | Tier compliance check |
| `clause.signed_on` | Date of contract/clause | date | C | — | — | NN-03 clause at origination |
| `clause.stamp_status` | Stamp status | select | N | stamped · unstamped · not_sure | — | Unstamped is curable (LR-ARB-028) |

**BLK-PARALLEL (Parallel Proceedings Declaration).** Table rows: `kind` (DD-COM-PARALLEL), `forum`, `reference`, `filed_on`, `stage`, `next_date`, `document`. Truth declaration (Y). Effects: `nclt_ibc` → R-COM-04..08; `msefc` → R-COM-09; `ni138` → R-COM-21; `nclt_company` → s.442 option; `rera`/`consumer` → R-COM-17; `pims_lsa` → link `com.pims_referrals`; `criminal_other` → R-COM-02.

**BLK-CONSENT (all consensual mechanisms).** `consent.rules_version` (system, pinned); `consent.online_mode` (Y, e-sign); `consent.no_recording` (Y, NN-11); `consent.confidentiality` (Y); `consent.fee_allocation` (Y, DD-COM-PAYER); `consent.standstill` (N; visible only if `com.standstill_template` ON); `consent.arbitration_for_consent_award` (N; separate signature; independent-advice prompt); `consent.publication` (N; default no; App. R).

### 6.3 Negotiation Request (F-COM-27)

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `neg.format` | How should talks run? | select | Y | DD-COM-NEG-FORMAT | blind_bid only if `amount_principal_minor > 0` and L1 ∉ {ibc post-admission, corp} | — |
| `neg.opening_offer.type` | Your opening proposal | select | Y | DD-COM-OFFER-TYPE | — | Not shared until the other side joins |
| `neg.opening_offer.amount_minor` | Amount | money | C | — | ≤ claim | — |
| `neg.opening_offer.schedule[]` | Instalments | table | C | date, amount | sum = amount; first ≥ today + 7 d | — |
| `neg.offer_validity_days` | Keep offer open for | select | Y | 14 · 21 · 30 | ≥ 14 (Singapore O.5 benchmark, PL-08) | — |
| `neg.deadline_days` | Overall talks deadline | select | Y | 7 · 14 · 21 · 30 | default 21 (`neg_timebox`) | — |
| `neg.reconciliation_first` | Upload ledgers for invoice matching first? | bool | C | — | default true for L2 ∈ {supply_goods, services, msme_*} | Engine highlights mismatches |
| `neg.authority_confirmed` | I have authority to settle up to | money | Y (org) | — | ≤ `party.authority_limit_minor` | NN-27 |
| `neg.escalate_to` | If talks fail, move to | select | N | mediation · conciliation · arbitration (if clause) · stop | — | — |

### 6.4 Request for Mediation / Conciliation (F-COM-04 v2)

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `med.route` | Which process? | select | Y | DD-COM-MED-ROUTE | `part_iii_conciliation` recommended if respondent is company and enforceable outcome wanted (PL-02) | Conciliation settlement has award status (s.74) |
| `med.basis` | Basis | select | Y | clause · voluntary_pre_suit · tiered_clause_step · court_referral (s.89 CPC) · s442_reference | s442 → F-COM-33 | — |
| `med.pims_pack_consent` | Also prepare the s.12A Form-1 pack for the Legal Services Authority? | bool | C | — | requiredWhen R-COM-12 | Equator does not conduct s.12A PIMS |
| `med.neutral_profile` | Preferred neutral background | select | N | DD-COM-NEUTRAL-PROFILE | — | Final appointment per Equator Rules |
| `med.co_mediation` | Co-mediation (legal + technical)? | bool | N | — | default true for L1 ∈ {con, tech} when amount ≥ ₹1 crore | Fee ×1.6 (Appendix B) |
| `med.process_style` | Style | select | N | facilitative · evaluative_with_consent | evaluative only with all-party consent; never AI-evaluative (NN-01) | — |
| `med.clock_days` | Time limit | select | Y | 30 · 60 · 90 · 120 | default 60 (COM `med_contract_timebox`); max +60 by consent | — |
| `med.output_wanted` | Output wanted | select | Y | DD-COM-OUTPUT | `consent_award` requires arbitration agreement (existing or F-COM-41) | — |
| `med.respondent_contact[]` | Who should receive the invitation? | table | Y | name, designation, email, mobile, address | ≥ 1; corporate → legal head/GRO preferred (S4 E2) | — |
| `med.first_session_free` | First information session free for the respondent? | system | — | true by default (PL-07) | — | — |
| `med.group` | Group mediation (several claimants on one project)? | bool | C | — | requiredWhen L2 = allottee_collective | Class sessions + private caucuses |

### 6.5 Request for Arbitration (F-COM-02 v2) and Statement of Claim (F-COM-09)

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `rfa.agreement_basis` | Basis for Equator arbitration | select | Y | clause_names_equator · submission_agreement (F-COM-41) · s11_order | else `COM_NO_ARB_AGREEMENT` | — |
| `rfa.s21_notice_date` | Date the other side received notice invoking arbitration | date | C | — | ≤ today; F-COM-23 | Starts the arbitration (s.21) |
| `rfa.claims[]` | Claims table | table | Y | head (DD-COM-CLAIM-HEAD[l1]), amount_minor, basis, interest basis | ≥ 1; each head passes `ARB_SCREEN` | Non-arbitrable heads are severed |
| `rfa.relief[]` | Reliefs | multiselect | Y | DD-COM-RELIEF | — | — |
| `rfa.procedure` | Procedure requested | select | Y | DD-COM-ARB-PROCEDURE | `s29b_fast_track` needs F-COM-37 consent of all parties; `expedited` eligibility ≤ threshold or agreement | — |
| `rfa.tribunal_size` | Tribunal | select | Y | sole · three | three default when claim + counterclaim > ₹10 crore (FR-P04-17) | — |
| `rfa.equal_footing_request` | Request equal-footing status (each side nominates one co-arbitrator)? | bool | C | — | visible only when three; registrar decides on grounds; never for repeat-player matters | NN-03 exception |
| `rfa.nominee` | Your co-arbitrator nominee | ref | C | panel neutral or outside person | requiredWhen `equal_footing = true`; within 15 d | Disclosure + Appointments Committee confirmation |
| `rfa.emergency_relief` | Emergency relief | select | Y | not_needed · emergency_arbitrator · court_s9 | EA → F-COM-11 | — |
| `rfa.seat_city` | Seat | select | Y | DD-COM-SEAT | clause prevails | — |
| `rfa.language` | Language of arbitration | select | Y | DD-LANG | — | — |
| `rfa.tpf_disclosure` | Third-party funding | group | Y | F-COM-40 | — | Mandatory disclosure |
| `rfa.relevant_persons[]` | Related persons and companies | table | Y | name, relationship (DD-COM-RELATED), identifier | ≥ parties' group entities | Drives conflict checks |
| `rfa.undertaking_fees` | I agree to pay deposits under the Equator Rules | bool | Y | — | true | — |
| `soc.facts[]` | Numbered facts | list | Y (SoC) | — | each with source anchor (NN-25) | AI Pleadings Studio optional |
| `soc.terms_relied` / `soc.breach` | Terms relied on / breach | textarea | Y | — | — | — |
| `soc.interest.pre_reference` / `pendente_lite` / `post_award` | Interest heads | group | Y | basis DD-COM-INTEREST-BASIS | post-award per s.31(7)(b) | — |
| `soc.exhibits[]` | Exhibits | files | Y | — | indexed; hash; BSA s.63 certificate for electronic records | — |

### 6.6 Response forms

**F-COM-28 Response to Invitation (negotiation/mediation/conciliation).**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `resp.decision` | Your response | select | Y | DD-COM-RESP-DECISION | — | Declining has no penalty at Equator |
| `resp.conditions` | Conditions | textarea | C | — | requiredWhen accept_with_conditions | — |
| `resp.dates[]` | Choose up to 3 dates | slots | C | — | requiredWhen accept | — |
| `resp.neutral_choice` | Choose a neutral from the shortlist | select | N | 3 names from allocation run | — | Respondent confirmation step (S4 E6) |
| `resp.counter_offer` | Counter-offer | group | C | type, amount, schedule | requiredWhen counter_offer | — |
| `resp.forum_objection` | Forum objection | select | C | arbitration_clause_elsewhere · statutory_forum · msefc_pending · nclt_pending · other | — | Routing re-run |
| `resp.decline_reason_private` | Reason (kept private, optional) | textarea | N | — | sealed; never shown to claimant | — |
| `resp.extension_days` | Need more time? | select | N | 7 · 14 | once; ≤ 14 | — |
| `resp.authority_doc` | Authority to participate/settle | file | C | — | requiredWhen org and accept | — |

**F-COM-03 v2 Response to RFA + Counterclaim / F-COM-10 SoD.**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `rsp.position` | Position | select | Y | accept_jurisdiction · object_jurisdiction · object_arbitrability · accept_but_dispute_claim | — | s.16 objection no later than SoD |
| `rsp.jurisdiction_grounds[]` | Grounds | multiselect | C | no_agreement · scope · non_signatory · non_arbitrable · time_barred · tiered_step_not_followed · msefc_override · ibc_moratorium | — | — |
| `rsp.counterclaims[]` | Counterclaims | table | N | head, amount_minor, basis | each passes `ARB_SCREEN` | Fee increment (Appendix B) |
| `rsp.procedure_view` | View on procedure | select | Y | agree · object_expedited · request_three_member · agree_s29b | — | — |
| `rsp.nominee` | Co-arbitrator nominee | ref | C | — | equal_footing only | — |
| `rsp.tpf_disclosure` | Third-party funding | group | Y | F-COM-40 | — | — |
| `sod.para_responses[]` | Para-wise admit/deny | table | Y | para_no, admit/deny/not_known, reply | covers every SoC para | — |

### 6.7 L1 extension blocks (added to every mechanism form for that L1)

| Block | Fields (field_id — type — req — options/validation) |
|---|---|
| **EXT-B2B** | `b2b.issue` select Y DD-COM-B2B-ISSUE · `b2b.objection_timing` select C (none · within_15_days · after_15_days · not_applicable) · `b2b.relationship_status` select Y (active · suspended · terminated_by_us · terminated_by_them) · `b2b.exclusivity_rpm` select N (yes · no · not_sure) · `b2b.invoices[]` table C (no, date, amount, irn, delivery_date, grn_date, objection_date, paid_minor) · `b2b.stock_or_tools_held` money N · `b2b.gst_credit_note_needed` bool N (help: credit notes by 30 Nov or annual-return date, whichever earlier — CGST s.34(2)) · `b2b.public_procurement.tender_ref` text C (requiredWhen GOVT_SET) |
| **EXT-CON** | `con.employer_type` select Y DD-COM-CON-EMPLOYER · `con.contract_form` select Y DD-COM-CON-FORM · `con.claim_heads[]` table Y (head DD-COM-CON-HEAD, amount_minor, period) · `con.tier` select Y (engineer · dab · conciliation_committee · senior_mgmt · none) · `con.tier_status` select Y (not_started · ongoing · decision_received · time_barred) + `con.tier_decision_date` date C · `con.dispute_value_vs_10cr` system (derived) · `con.project_status` select Y (executing · completed · terminated · abandoned) · `con.bg[]` table C (type: performance/advance/retention; amount; expiry; invocation_date) · `con.ld_deducted_minor` money N · `con.price_variation_clause` file N · `con.approval_ref` text C (requiredWhen GOVT_SET and ≥ ₹10 crore and arbitration) |
| **EXT-TECH** | `tech.service_type` select Y DD-COM-TECH-SERVICE · `tech.issue` select Y DD-COM-TECH-ISSUE · `tech.data_involved` select Y (personal_data · confidential_business · none) · `tech.return_delete` bool N · `tech.ip_registry_relief` bool Y (true → R-COM-19) · `tech.ip_rights[]` table C (type: tm/patent/copyright/design/know_how; registration no.; owner) · `tech.sla_metrics` file N (CSV/JSON logs, hashed) · `tech.ring_level` select Y (counsel_only · experts_only · parties_and_counsel) |
| **EXT-RE** | `re.role` select Y DD-COM-RE-ROLE · `re.rera_registered` select Y (yes · no · exempt · dont_know) + `re.rera_no` text C + `re.rera_state` select C · `re.issue` select Y DD-COM-RE-ISSUE · `re.purpose` select C (self_use · investment_commercial) · `re.payments[]` table C (date, amount_minor, receipt) · `re.possession_due_date` date C · `re.rent_control` select C (yes · no · dont_know) · `re.property_ref` text C (sensitive) · `re.mortgaged_unit` select N (yes · no · dont_know; → CERSAI check) · `re.allottee_count` int C (group) |
| **EXT-PART** | `part.entity` select Y (registered_firm · unregistered_firm · llp · professional_firm) · `part.issue` select Y DD-COM-PART-ISSUE · `part.continue_business` select Y (buyout · split · wind_up) · `part.valuation_method` select N (book · fair_value · deed_formula · mediator_options) · `part.deed_clause` select Y (arbitration · llp_default · none) · `part.capital_accounts` file C (last 3 years) |
| **EXT-CORP** | `corp.company_type` select Y DD-COM-CORP-TYPE · `corp.holding_pct` decimal C (0–100) · `corp.share_class` select C (equity · preference · ccps · ccd · esop) · `corp.is_director` bool C · `corp.issue` select Y DD-COM-CORP-ISSUE · `corp.s244_status` system (CAL-COM-08) · `corp.proceedings` select Y (none · nclt_s241 · arbitration · civil_suit · sebi) · `corp.outcome` select Y DD-COM-CORP-OUTCOME · `corp.valuation_basis` select N DD-COM-VALUATION · `corp.s442_interest` select C (yes · no · not_sure) · `corp.foreign_investor` bool Y (true → INT check) · `corp.listed` bool Y (true → LODR Reg 30 card) |
| **EXT-IBC** | `ibc.role` select Y DD-COM-IBC-ROLE · `ibc.stage` select Y DD-COM-IBC-STAGE + stage dates (`s8_served_on`, `filed_on`, `cp_no`, `admitted_on`, `coc_constituted_on`, `form_g_on`, `liquidation_on`) · `ibc.default_minor` money Y · `ibc.debtor_msme` select Y (micro · small · medium · no · dont_know) · `ibc.iu_status` select Y (record_of_default · information_of_dispute · not_filed) · `ibc.settlement_shape[]` multiselect N DD-COM-IBC-SHAPE · `ibc.approvers[]` multiselect Y (applicant · coc_90 · board_members · consortium) · `ibc.rp_consent_doc` file C (requiredWhen stage ≥ admitted and engagement of RP) · `ibc.s29a_declaration` bool C (promoter resolution plan) |
| **EXT-MSME** | `msme.udyam_no` (BLK-PARTY) · `msme.category_on_contract` select Y (micro · small · medium · not_registered) · `msme.buyer_type` select Y (government · cpse · company · other_business) · `msme.invoices[]` table Y (no, date, amount_minor, delivery_date, objection_date, agreed_credit_days ≤ 45 with warning, part_payments[]) · `msme.msefc_ref` text N · `msme.treds_used` bool N · `msme.buyer_msme1_disclosure` file N |
| **EXT-CHQ** | `chq.cheque_no` text Y (6 digits) · `chq.date` date Y · `chq.amount_minor` money Y · `chq.drawee_bank` text Y · `chq.return_memo_date` date Y · `chq.return_reason` select Y DD-COM-CHQ-REASON · `chq.notice_sent_on` / `chq.notice_received_on` date C · `chq.case_status` select Y DD-COM-CHQ-STAGE · `chq.court` / `chq.case_no` text C · `chq.underlying` select Y (supply_payment · loan · security_cheque · other) |
| **EXT-BFS** | `bfs.claimant_type` select Y (bank · rdb_fi · nbfc · business) · `bfs.instrument` select Y (bg · lc · facility · factoring · derivative · guarantee) · `bfs.borrower_type` select C (company · llp · individual · msme_individual → FIN reroute) · `bfs.default_minor` money C |

### 6.8 Vertical-specific forms

**F-COM-11 v2 — Interim measures and Emergency Arbitrator application.**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `ea.forum` | Where to ask | select | Y | emergency_arbitrator · tribunal_s17 · court_s9_pack | EA only before tribunal constituted; India seat | Foreign seat EA not directly enforceable (LR-ARB-025) |
| `ea.relief[]` | Relief | multiselect | Y | DD-COM-INTERIM-RELIEF | ≥ 1 | — |
| `ea.urgency_statement` | Why it cannot wait | textarea | Y | — | 100–3,000 chars | — |
| `ea.prima_facie` / `ea.balance_of_convenience` / `ea.irreparable_harm` | Grounds | textarea | Y | — | — | — |
| `ea.undertaking_damages` | Undertaking as to damages | bool | Y | — | true | — |
| `ea.draft_order` | Draft order | file | Y | — | DOCX/PDF | — |
| `ea.service_proof` | Proof of service on the other side | file | C | — | or `ea.ex_parte_reasons` (requiredWhen not served) | — |
| `ea.notice_of_arbitration_due` | Notice of arbitration follows within | system | — | 7 days (SIAC Sch.1 benchmark; Equator Rules Sch.1 setting `ea.noa_followup_days`) | — | — |
| `ea.fee_ack` | EA fee | system | Y | Card COM-STD C6 ₹3,00,000 fixed (EA ₹2,40,000 + admin ₹60,000) | paid before appointment | Appendix B prevails over P04 illustrative figure |

**F-COM-24 — s.12A PIMS Form-1 Application Pack (for the Legal Services Authority).** Fields mirror PIMS Rules 2018 r.3(1) Form-1: `pims.authority` (select DD-COM-LSA by district/State; HC Legal Services Committee where State SOP provides) · `pims.applicant` (from BLK-PARTY) · `pims.opposite_party[]` · `pims.dispute_nature` (text) · `pims.specified_value_minor` (≥ ₹3,00,000) · `pims.documents[]` · `pims.fee_note` (system: ₹1,000 application; Schedule II band) · tracking: `pims.filed_on`, `pims.authority_ref`, `pims.form2_notice_on`, `pims.outcome` (pending · settled_form4 · non_starter_form3 · failed_form5 · withdrawn), `pims.outcome_doc`. Output PDF header: "Prepared by the applicant with assistance from Equator Resolution Service Private Limited. Filed by the applicant with the Authority." (LR-MED-018). Stored in `com.pims_referrals`.

**F-COM-26 — MSEFC election.** `msefc.explained` (bool Y; FD-COM-02 shown and acknowledged) · `msefc.choice` (select Y: file_msefc_now · try_equator_first_then_msefc · equator_arbitration_informed_election) · `msefc.reference_no` (text C) · `msefc.independent_advice_ack` (bool C, requiredWhen equator_arbitration) · e-signature of supplier.

**F-COM-29 — IBC Settlement Desk intake + r.8 withdrawal memo.**

| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| `desk.stage` | Stage | select | Y | no_notice · s8_served · filed_not_admitted | others → F-COM-30 / signpost | — |
| `desk.hearing_date` | Next NCLT date | date | C | — | requiredWhen filed_not_admitted | Fast lane if ≤ 14 d |
| `desk.s8_received_on` | Date CD received s.8 notice | date | C | — | reply deadline = +10 d shown | CD must reply anyway |
| `desk.claim_minor` | Claimed amount | money | Y | — | ≥ ₹1,00,00,000 for CIRP route (else B2B) | — |
| `desk.dispute_positions` | Each side's position (private to neutral) | textarea | N | — | sealed per party | Confidential |
| `desk.terms.amount_minor` / `desk.terms.schedule[]` / `desk.terms.escrow` | Settlement terms | group | C | — | sum checks | — |
| `desk.terms.revival_clause` | Claim revives in full on default | bool | Y | default true | — | — |
| `desk.terms.cirp_costs` | Who bears any CIRP/IRP costs | select | C | cd · applicant · shared | — | — |
| `desk.withdrawal_memo` | Generate joint r.8 withdrawal memo | bool | C | — | only when filed_not_admitted | Applicant files with NCLT |
| `desk.closure_report_consent` | Debtor consents to annexing the Equator Closure Report to a s.9 application if talks fail | bool | N | — | separate e-sign by debtor (LR-IBC-009) | Default no |

**F-COM-30 — s.12A IBC withdrawal support annex.** `s12a.admitted_on`, `s12a.coc_constituted_on` (Y; must be ≤ today), `s12a.form_g_issued` (Y; must be false), `s12a.voting_matrix[]` (FC name, voting share %, approval: yes/no/pending) with CAL-COM-07, `s12a.settlement_amount_minor`, `s12a.cirp_cost_reimbursement` (Y), `s12a.rp_name`/`ip_regn_no` (Y), `s12a.rp_ack` (file Y), `s12a.application_filed_on` (C), `s12a.nclt_order` (file C). Validation: CTA "Send to RP" disabled unless window open (LR-IBC-003).

**F-COM-31 — PPIRP pre-filing pack.** Eligibility (CAL-COM-06): `pp.cd_msme_category`, `pp.default_minor` (≥ ₹10,00,000), `pp.prior_insolvency_3y` (must be no), `pp.s29a_eligible` (declaration), `pp.unrelated_fcs[]` (name, share %, approval), `pp.proposed_rp` (name, regn), `pp.base_plan_doc`, `pp.special_resolution_draft` (template), `pp.directors_declaration_draft` (template), threshold display "51% from 26 May 2026 [VERIFY]".

**F-COM-32 — HLC-ready settlement proposal.** `hlc.entity` (GOVT_SET), `hlc.contract_ref`, `hlc.dispute_value_minor`, `hlc.claims_matrix[]` (head, claimed, admitted by department, agreed in mediation, basis), `hlc.interest_treatment`, `hlc.bg_release`, `hlc.approval_authority` (select: secretary · js_delegate · md_cpse · board · other), `hlc.binding_clause` (system text: "binding only upon written approval of [authority]"), `hlc.mediator_report` (facts, no confidential content), status `pending_competent_authority_approval`.

**F-COM-33 — s.442 reference record.** `s442.order` (file Y; NCLT/NCLAT/Central Govt), `s442.reference_on` (date Y), `s442.panel_mediator` (Equator neutral with `mca442_region`), `s442.region`, `s442.fee_fixed_by_tribunal_minor` (money Y), `s442.deposit_status`, `s442.r11_memorandum_due` (system: session − 10 d), `s442.r30_screen` (multiselect of r.30 categories; any → R-COM-16), `s442.venue_consent` (bool C: parties and panel agree to Equator ODR venue), outputs r.24 settlement / r.25 failure report.

**F-COM-34 — RERA settlement memo.** `rera.complaint_no` (C), `rera.authority` (State), `rera.terms` (possession date / refund schedule / interest per CAL-COM-09 / alternate unit / rectification list), `rera.escrow`, `rera.joint_filing_days` (default 7), `rera.lender_noc_required` (bool), `rera.registration_required` (system: NN-08 if conveyance/modified agreement for sale).

**F-COM-35 — Cap table & valuation inputs (tier High).** `cap.issued_shares`, `cap.holders[]` (name, class, count, paid-up), `cap.member_count`, `val.method` (DD-COM-VALUATION), `val.inputs` (NAV, EBITDA, multiple, discount rate — indicative only), `val.registered_valuer_report` (file N).

**F-COM-36 — Co-arbitrator nomination (equal footing).** Visible only if `core.cases.equal_footing = true` (registrar-set, grounds recorded). `nom.nominee` (panel ID or outside person: name, profession, contact, CV), `nom.relationship_declaration` (Y), `nom.disclosure_request_sent` (system), deadline 15 d (`arb_nomination`), Appointments Committee confirmation (system).

**F-COM-37 — Procedure election.** `proc.track` (select Y: standard · expedited_rules · s29b_fast_track · documents_only_by_agreement), `proc.s29b_consent` (e-sign each party; requiredWhen s29b), `proc.three_member` (bool), `proc.hearing_waiver` (bool), `proc.page_limits_ack` (bool for expedited), `proc.ai_docs_only_lane` (hidden; flag `com.ai_docs_only_lane` OFF).

**F-COM-38 — Consent award request.** `ca.settlement_doc` (Y), `ca.all_parties_request` (e-sign each, Y), `ca.tribunal_no_objection` (system), `ca.terms_lawful_ack` (Y), `ca.stamp_state` (state of execution), `ca.conversion_source` (in_arbitration · ama_mediation · post_conciliation (→ prefer s.73)).

**F-COM-39 — Cheque settlement & compounding memorandum.** `cq.amount_settled_minor`, `cq.payment_route` (escrow · direct_with_proof), `cq.stage` (DD-COM-CHQ-STAGE), `cq.compounding_cost_minor` (CAL-COM-10), `cq.cost_payer` (drawer default), `cq.joint_application` (template), `cq.no_threat_declaration` (Y), `cq.court_decides_ack` (Y: "Only the court compounds or closes the case").

**F-COM-40 — TPF & relevant persons disclosure.** `tpf.exists` (Y), `tpf.funder_name`, `tpf.funder_country`, `tpf.outcome_related_fee` (bool), `tpf.updated_on`; `rel.persons[]` (name, type, relationship). Funder bound by confidentiality undertaking (e-sign). Change triggers conflict re-run (S5-R05/R06).

**F-COM-41 — Post-dispute submission agreement.** `sub.dispute_description` (Y), `sub.dispute_arose_on` (Y), `sub.equator_rules_version` (system), `sub.seat`, `sub.tribunal_size`, `sub.procedure`, per-party e-sign `signed_at > dispute_arose_on` (Y). For repeat-player matters: allocation by Equator for every seat (NN-03).

### 6.9 Dropdown master list (full values; `code — label`)

| List ID | Values |
|---|---|
| DD-COM-ROLE | claimant — Claimant · respondent — Respondent · co_claimant — Co-claimant · co_respondent — Co-respondent · joint_filer — Joint filer · adviser — Adviser for a party · intervenor — Intervenor · guarantor — Guarantor |
| DD-COM-ENTITY | company — Company · government_company — Government company · llp — LLP · partnership_registered — Registered partnership firm · partnership_unregistered — Unregistered partnership firm · proprietorship — Sole proprietorship · individual — Individual · central_government — Central Ministry/Department · state_government — State Department · cpse — CPSE · state_psu — State PSU · ulb — Municipal/ULB · bank — Bank · rdb_fi — Financial institution (RDB Act s.2(h)) · nbfc — NBFC · trust_society — Trust/society · huf — HUF · foreign — Foreign entity |
| DD-COM-L1 | b2b — Contracts, supply, distribution, franchise, agency · con — Construction & infrastructure · tech — IT, technology & IP licensing · re — Real estate & RERA · part — Partnership & LLP · corp — Shareholder, JV & founder · ibc — Insolvency & restructuring · msme — MSME delayed payment · chq — Cheque dishonour · bfs — Banking, guarantee & trade finance (B2B) · reg — Competition, consumer & regulator (signpost) |
| DD-COM-L2 | per §2.2 (codes exactly as listed under each L1) |
| DD-COM-SECTOR | manufacturing · it_technology · construction_infrastructure · bfsi · real_estate · pharma_healthcare · retail_fmcg · energy_power · logistics · professional_services · telecom_media · agriculture_food · education · hospitality · automotive · textiles · chemicals · mining · government_contracting · other |
| DD-COM-CONTRACT-BASIS | signed_contract · po_and_invoices · email_whatsapp_trail · oral · not_sure |
| DD-COM-CLAUSE-TYPE | arbitration · mediation · negotiation_escalation · expert_determination · dispute_board · exclusive_court_jurisdiction · none · not_sure |
| DD-COM-INSTITUTION | equator · none_ad_hoc · mcia · diac_delhi · ica · iiac · sarod · icc · siac · lcia · cnica · iamc · other |
| DD-COM-SEAT | mumbai · delhi_ncr · bengaluru · chennai · kolkata · hyderabad · ahmedabad · pune · jaipur · noida · chandigarh · lucknow · kochi · indore · gift_city_ifsc · other_india |
| DD-COM-RELIEF | payment · interest · damages · specific_performance · injunction · declaration · account · termination_restitution · return_goods_ip_data_code · price_scope_reset · exit_agreed_terms · time_to_pay_restructuring · share_buyout · governance_reset · costs · escrow_secured_payment · apology · other |
| DD-COM-INTEREST-BASIS | contractual_rate · msmed_s16 · rera_state_rule · claimed_reasonable (CPC s.34 / A&C s.31(7)(a)) · post_award_s31_7_b · none |
| DD-COM-NEG-FORMAT | assisted — Equator-assisted (case manager) · unassisted — Structured offers only · blind_bid — Blind bid (money only) · reconciliation_first — Ledger reconciliation then offers |
| DD-COM-OFFER-TYPE | lump_sum · instalments · credit_note_set_off · price_revision · goods_return_replacement · performance_cure · stock_buyback · transition_period · mutual_release · mixed |
| DD-COM-MED-ROUTE | voluntary_pre_suit_mediation · contractual_mediation · part_iii_conciliation · co_mediation · group_mediation · s442_panel (reference only) |
| DD-COM-NEUTRAL-PROFILE | lawyer_mediator · retired_judge · ca_cs_cma · engineer_quantum · technologist · valuer · real_estate_expert · insolvency_professional (mediator role only; never RP in same matter) · industry_expert |
| DD-COM-OUTPUT | settlement_agreement_contract · s73_conciliation_settlement · consent_award · hlc_proposal · rera_settlement_memo · nclt_consent_terms · r8_withdrawal_memo · s12a_ibc_support_annex · compounding_memorandum · lok_adalat_referral_note · closure_report |
| DD-COM-ARB-PROCEDURE | standard · expedited_rules · s29b_fast_track · documents_only_by_agreement · emergency_arbitrator_then_standard · ama (arb-med-arb) · med_arb · arb_med · appeal_tier_opt_in |
| DD-COM-RESP-DECISION | accept · accept_with_conditions · decline · counter_offer · object_forum · request_info · request_extension |
| DD-COM-CLAIM-HEAD[b2b] | unpaid_price · short_payment · damages_breach · lost_profit · ld · interest · security_deposit · stock_buyback · commission · termination_compensation · indemnity · earn_out · costs |
| DD-COM-CON-HEAD | ra_bills · final_bill · retention · price_variation · variations_extra_items · prolongation_idle · ld_refund · eot · bg_wrongful_invocation · termination · defects_counterclaim · interest · costs |
| DD-COM-CON-EMPLOYER | private_developer · central_ministry · state_department · cpse_psu · ulb · ppp_spv · main_contractor |
| DD-COM-CON-FORM | item_rate · lump_sum_epc · ham · bot_toll · fidic_red · fidic_yellow · fidic_silver · mca · cpwd_gcc · bespoke |
| DD-COM-B2B-ISSUE | unpaid_invoices · short_payment_deductions · quality_rejection · late_non_delivery · wrongful_termination · territory_exclusivity · targets_incentives · stock_return_buyback · security_deposit · non_compete_non_solicit · brand_ip_post_termination · warranty · other |
| DD-COM-TECH-SERVICE | custom_development · saas · managed_services · system_integration · licensed_software · api_data_supply · ip_licence |
| DD-COM-TECH-ISSUE | non_payment · missed_milestones · failed_acceptance · sla_breach · data_loss_breach · termination_exit · ip_ownership · royalty_underpayment · poaching_non_compete · escrow_release |
| DD-COM-RE-ROLE | allottee · promoter · landowner_jda · landlord · tenant · broker · rwa_society |
| DD-COM-RE-ISSUE | possession_delay · refund_withdrawal · defects · carpet_area_shortfall · plan_change · hidden_charges · conveyance_handover · jda_share_revenue · rent_default · lock_in_termination · security_deposit · brokerage |
| DD-COM-PART-ISSUE | dissolution · retirement_payout · expulsion · profit_capital · accounts_mismanagement · competing_business · admission · deadlock · death_of_partner |
| DD-COM-CORP-TYPE | private · public_unlisted · listed · section_8 · foreign_invested |
| DD-COM-CORP-ISSUE | board_deadlock · removal_director · dilution_rights_issue · siphoning_rpt · information_denied · dividend · founder_exit_vesting · esop_cancellation · put_call_valuation · drag_tag_rofr · jv_termination · family_business_split |
| DD-COM-CORP-OUTCOME | buy_out · sell_out · governance_reset · demerger_asset_split · wind_up · status_quo_information_rights |
| DD-COM-VALUATION | registered_valuer_fair_value · sha_formula · dcf · nav · comparables · last_round_price · mediator_options |
| DD-COM-IBC-ROLE | operational_creditor · financial_creditor · corporate_debtor_promoter · personal_guarantor · resolution_applicant · rp_liquidator · employee_workman |
| DD-COM-IBC-STAGE | no_notice · s8_served · filed_not_admitted · admitted_pre_coc · coc_constituted · form_g_issued · plan_approved · liquidation · voluntary_liquidation · ppirp_prefiling |
| DD-COM-IBC-SHAPE | lump_sum · instalments_escrow · equity_conversion · asset_transfer · third_party_payer · interest_waiver · mixed |
| DD-COM-PARALLEL | none · civil_commercial_suit · s9_court · arbitration_elsewhere · nclt_ibc · nclt_company · rera · consumer · msefc · ni138 · drt · pims_lsa · criminal_other · cci · ip_office |
| DD-COM-CHQ-REASON | funds_insufficient · exceeds_arrangement · payment_stopped · account_closed · signature_differs · refer_to_drawer · other |
| DD-COM-CHQ-STAGE | not_filed · pre_summons · summons_served · complainant_evidence · defence_evidence · judgment · sessions_hc · supreme_court |
| DD-COM-INTERIM-RELIEF | preserve_amount · security_for_claim · restrain_bg_encashment · injunction · preserve_detain_goods · appointment_of_receiver · data_preservation · status_quo_shares · other |
| DD-COM-RELATED | parent · subsidiary · affiliate · director · promoter · funder · insurer · counsel_firm · guarantor · other |
| DD-COM-PAYER | equal_split · claimant · respondent · enterprise_pays · deferred_cost_follows_event · filer |
| DD-COM-LSA | district-wise DLSA list per State (directory `routing_forums` kind = `lsa`) · hc_legal_services_committee (where State SOP provides) |
| DD-LANG | en · hi · mr · gu · ta · te · kn · bn · pa · ml · or · ur (configuration; NN-23) |
| DD-STATE | 28 States + 8 UTs (ISO 3166-2:IN codes) |

---

## 7. Modus operandi per subtype

Mechanism state machines are those of Appendix A §3 (N negotiation, K conciliation, M mediation, A arbitration, E EA, X expedited, H med-arb, R arb-med, B AMA, D expert determination). Tables below add COM-specific steps, actors, clocks, documents, notices and decision points. SLA = Equator service clock; statutory clocks per §3.

### 7.1 `com.b2b` (supply, services, distribution, franchise, agency, logistics, indemnity)

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | Claimant | Explorer → F-COM-01 + F-COM-27/04/02 with EXT-B2B | `draft_expiry` 30 d | D-B01–D-B09 | — | Routing R-COM-* |
| 2 | Rules engine | Triage: MSME precedence (R-COM-09), cheque spawn (R-COM-21), DoE (R-COM-13), PIMS (R-COM-12), arbitrability | instant | — | FD-COM-01/02/07 | Ladder chosen |
| 3 | CM | Scrutiny; KYB verified; deficiencies | `sla_scrutiny` 2 WD; cure 15 d | — | Deficiency notice | accept / deficient |
| 4 | Equator | Invitation (S4 B5 cadence) or RFA service | D0–D30 | Notice TPL-COM-N01/N04 | Email + WhatsApp + SMS + speed post (corporate) | respond / no response |
| 5 | Both | Ledger reconciliation upload; engine flags mismatched invoices | 7 d | D-B03, D-B04, D-B07 | — | Agreed balance? |
| 6 | Neutral | Mediation/conciliation sessions; "commercial reset" options (revised price list, instalments, stock buy-back %, 30/60/90-day transition, mutual release) | `med_contract_timebox` 60 d / `conc_timebox` 30 d | — | T-48 h / T-2 h reminders | settle / impasse |
| 7 | Drafting | Settlement with GST/credit-note clause, TDS clause, default acceleration, consent-award clause (if agreement) | 5 WD | TPL-COM-S02 | — | output type |
| 8 | Parties | e-sign + e-stamp (state of execution) | at signing | stamp certificate | — | — |
| 9 | Escrow officer | Instalments/escrow milestones | per schedule | proof | reminders | default → revival/consent award/suit |
| 10 | — | Impasse: arbitration (clause) or closure report + Form-1 pack | — | TPL-COM-R01 | — | next rung |

### 7.2 `com.con` and government counterparties (`com.gov.v1`)

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | Contractor | Intake with EXT-CON; claim heads table | — | D-C01–D-C09 | — | — |
| 2 | Rules engine | Tier compliance check (Engineer/DAB/committee); DoE gating if GOVT_SET | instant | tier decision | W-TIER if step skipped | proceed / complete tier first |
| 3 | CM | Appoint co-mediators (lawyer + engineer/quantum) from panel by allocation (NN-28) | `sla_neutral_appointment` 7 d | — | Disclosure notice | — |
| 4 | Neutrals | Claim-by-claim agreed/not-agreed matrix; expert determination for measurement if agreed (D01–D05) | Med 60–90 d; ED 21 + 14 d | D-C03, D-C07 | — | — |
| 5 | Neutral + parties | Government: produce **HLC-ready proposal** (F-COM-32); private: settlement | 10 WD | TPL-COM-S05 | Proposal to department nodal officer | HLC/competent authority approves? |
| 6 | Department | Upload competent-authority approval | `pending_competent_authority_approval` (service clock 90 d, escalation reminders at 30/60) | approval order | — | approved → execute; rejected → rung 3 |
| 7 | Tribunal (if arbitration) | Three-member default > ₹10 crore; for GOVT_SET ≥ ₹10 crore only with `approval_ref` | A-machine clocks | — | — | — |
| 8 | Parties | BG release mechanics, retention release, final bill closure in settlement | per schedule | BG release letters | — | — |

### 7.3 `com.tech`

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | Party | Intake with EXT-TECH; ring level chosen; logs uploaded with hash | — | D-T01–D-T10 | ring set |
| 2 | Registrar | Confidentiality ring order (counsel-only / experts-only) before any exchange | 2 WD | Ring undertakings e-signed | — |
| 3 | Neutral + technologist | Mediation; expert determination of SLA metrics/acceptance if agreed | Med 60 d; ED 21 + 14 d | — | — |
| 4 | Drafting | Settlement with transition/exit plan, data-return/deletion certificate, escrow release instruction, royalty true-up | 5 WD | TPL-COM-S07 | — |
| 5 | — | IP registry heads → `SIG.IPO` signposting event; licence heads continue | — | — | — |
| 6 | Tribunal | Arbitration with redaction protocol; information-security directions at first CMC (S5-R18) | A-machine | — | — |

### 7.4 `com.re`

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | Party | Intake EXT-RE; RERA registration lookup (deep link) | — | D-R01–D-R12 | homebuyer? |
| 2 | Rules engine | Homebuyer → FD-COM-03 + RERA/consumer signposting recorded **before** rung 1; MahaRERA card if MH | instant | — | signposting event |
| 3 | Equator | Invitation to promoter; group mediation if `allottee_collective` (class session + caucuses) | D0–D30 | — | — |
| 4 | Neutral (+ valuer) | Structured offer menu: possession date + delay interest (CAL-COM-09) / refund schedule with escrow / alternate unit / rectification list | Med 60 d | — | MFN clause review for groups |
| 5 | Drafting | RERA settlement memo (F-COM-34) with joint filing within 7 days where a complaint is pending; lender NOC (CERSAI check) | 5 WD | TPL-COM-S06 | — |
| 6 | Parties | Modified agreement for sale / JDA amendment / conveyance → NN-08 physical execution, stamping, registration (`registration_4m`) | 4 m | registration evidence | closure gated |

### 7.5 `com.part`

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | Partner | Intake EXT-PART; deed/LLP agreement uploaded | — | D-P01–D-P08 | arbitration default (para 14)? |
| 2 | Neutral (+ valuer/CA) | Exit valuation options (CAL-COM-16), client-transition protocol | Med 60 d (+60) | capital accounts | — |
| 3 | Drafting | Dissolution/retirement/buy-out deed; Registrar of Firms notice; LLP Form 4 within 30 days | 5 WD | TPL-COM-S08 | stamp per State |
| 4 | Tribunal | Arbitration where deed/para 14 applies; LLP joined as respondent if needed (*Kartik Radia*) | A-machine | — | — |

### 7.6 `com.corp` (shareholder, JV, founder, oppression) and s.442 track

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | Member | Intake EXT-CORP + F-COM-35 cap table (tier High) | — | D-S01–D-S12 | s.244 eligibility |
| 2 | Rules engine | Sever statutory reliefs (R-COM-14); FD-COM-05; s.442 option if NCLT pending | instant | — | — |
| 3 | CM | Appoint mediator (Grade A/B for > ₹50 crore per allocation policy) + optional neutral evaluator/forensic accountant under ring | 7 d | — | — |
| 4 | Neutral | Mediate the whole dispute; valuation band (indicative) or expert determination | Med 90 d (+60) | valuation report | — |
| 5 | Drafting | Settlement pack: SPA/exit agreement, amended SHA, AoA special resolution, board/EGM resolutions, SH-4, NCLT consent terms (s.241 withdrawal or consent order), FEMA note (→ INT if non-resident) | 10 WD | TPL-COM-S09 | NCLT filing needed? |
| 6 | Tribunal | Arbitration of SHA/JV heads only; `equal_footing` may apply (§7.12) | A-machine | — | — |
| **s.442** 1 | NCLT/NCLAT | Reference order naming an empanelled individual | `s442_clock` from earlier of reference/appointment | order | — |
| s.442 2 | Panel mediator | r.30 screen; r.11 memorandum of issues ≥ 10 days before session; fee as fixed by Tribunal (`fee_source = tribunal_order`) | 3 m (+3 m by Tribunal) | memorandum | venue consent |
| s.442 3 | Panel mediator | r.14 two consecutive absences → failure; r.24 settlement / r.25 failure report to Tribunal; Equator branding off | — | TPL-COM-S10 / R03 | — |
| s.442 4 | Party | Upload r.26 Tribunal order in terms of settlement | usually within 14 d of report | order | status `awaiting_tribunal_order` → closed |

### 7.7 `com.ibc`

**IBC Settlement Desk (pre-admission) — `com.ibc.desk.v1`**

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | OC/FC or CD | F-COM-29; stage, dates, IU status; CAL-COM-06 eligibility | — | D-I01–D-I08 | < ₹1 crore → B2B/MSME route |
| 2 | Rules engine | U-01/U-02 urgency; `ibc_s8_reply` owner = CD; FD-COM-04 | instant | — | — |
| 3 | CM | Appoint mediator within 1 WD (fast lane) | 1 WD | — | — |
| 4 | Neutral | Fast mediation; positions recorded privately (sealed per party) | 7–10 d (config 7–21) | — | settle / fail |
| 5 | Drafting | Settlement with conditions precedent (NCLT withdrawal), escrowed instalments, revival clause, CIRP-cost clause; r.8 joint withdrawal memo if filed | 3 WD | TPL-COM-S11, TPL-COM-L04 | — |
| 6 | Applicant | Files r.8 withdrawal before admission; uploads NCLT order | before admission | order | — |
| 7 | — | Failure: Equator Mediation Closure Report (IBC footer, §13.2); annex only with debtor's consent (LR-IBC-009) | — | TPL-COM-R02 | — |

**Post-admission s.12A IBC — `com.ibc.s12a.v1`**

| Step | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | CD/promoter or applicant | F-COM-30; admission date; CoC status | — | `coc_constituted = false` → R-COM-05 (draft only) |
| 2 | Neutral | Settlement negotiation; RP engaged only with RP consent | Med 30 d | — |
| 3 | Engine | CoC voting matrix (CAL-COM-07) | — | ≥ 90%? |
| 4 | RP | Files s.12A application with NCLT | before first Form G (`ibc_s12a_window`) | — |
| 5 | NCLT | Decides within 30 days (`ibc_s12a_decision`, tracking only) | 30 d | order uploaded → closed |
| 6 | Engine | If `form_g_issued = true` → R-COM-06 (resolution-plan route only) | — | — |

**PPIRP pre-filing — `com.ibc.prepack.v1`:** eligibility (CAL-COM-06) → information room (ring) → facilitated negotiation with unrelated FCs on base resolution plan and RP → vote tracker (51% [VERIFY]) → special resolution + directors' declaration drafts (F-COM-31) → CD files s.54C (Equator role ends).

**Liquidation-stage compromise — `com.ibc.liq.v1`:** record liquidation order date → `liq_s230` 90 d countdown (tracking) → s.29A eligibility declaration of proponent → scheme term-sheet negotiation with creditors (liquidator informed) → NCLT sanction (party files). Voluntary liquidation: withdrawal support under s.59(5A)–(5C) (special resolution + 2/3 creditor approval calculator). Asset-sale side disputes: mediation only with liquidator's written consent.

### 7.8 `com.msme`

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | Supplier | EXT-MSME invoices; Udyam verification | — | D-M01–D-M08 | category/registration date |
| 2 | Engine | FD-COM-02 shown first; CAL-COM-01 per invoice; W-NBCC if registered after contract | instant | — | F-COM-26 election |
| 3 | Equator | Invitation to buyer; Card COM-STD C10 ₹1,999 flat (filer) | D0–D30 | TPL-COM-N03 (s.15/s.16 demand) | — |
| 4 | Conciliator | Part III conciliation; full s.16 interest shown; any waiver → LR-MSME-010 express clause | 30 d | — | settle / fail |
| 5 | Drafting | s.73 settlement (s.74 status) with instalments, escrow | 3 WD | TPL-COM-S03 | — |
| 6 | Engine | Failure → MSME ODR export pack (portal field order; supplier files) | 2 WD | `msme_odr_pack.pdf` + CSV | — |
| 7 (flag) | Council → Equator | `com.msefc_referral_msp` ON: Council referral; mediation within 90 d of first appearance; on failure Council decides arbitration referral within 30 d | `msme_council_med`, `msme_arb_refer`, `msme_award` | Council reference | — |

### 7.9 `com.chq`

| Step | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | Payee | EXT-CHQ; clocks `ni138_notice_30d`, `ni138_pay_15d`, `ni138_complaint_1m` (LR-RBI-017; informational, owner = payee) | per NI Act | — |
| 2 | Equator | Negotiation within pay window with escrow payment link | ≤ 15 d of notice receipt | paid → settlement deed |
| 3 | Neutral | Pending complaint: mediation of civil debt; compounding cost by stage (CAL-COM-10) | Med 30 d | — |
| 4 | Drafting | F-COM-39 memorandum + joint compounding application (s.147; BNSS compounding provisions as applicable) | 3 WD | court decides |
| 5 | — | Lok Adalat referral note (next National Lok Adalat 12 Dec 2026) | — | exit |

### 7.10 Arbitration track (all arbitrable COM L2s)

| Step | Actor | Action | Clock (Appendix A) | Notes |
|---|---|---|---|---|
| 1 | Claimant | s.21 notice (F-COM-23) → RFA (F-COM-02) + F-COM-40 | `arb_s11_3y` informational | — |
| 2 | Registrar | Basis check: clause names Equator / F-COM-41 / s.11 order | — | `COM_NO_ARB_AGREEMENT` else |
| 3 | Respondent | Response + counterclaim | `arb_response` 14 d (+14 once) | — |
| 4 | Appointments Committee | Constitution (sole default; three where agreed or > ₹10 crore); allocation run logged | `sla_constitution` 30 d (expedited 14 d) | NN-03; §7.12 |
| 5 | Tribunal | CMC + PO1 within 21 d; information-security directions; TPF disclosure confirmed | `sla_po1`; `arb_s23_4` 6 m | — |
| 6 | Parties | Pleadings; completion order | `arb_s29a` 12 m starts | — |
| 7 | Tribunal | Hearings / documents-only; s.17 applications | `hearing_notice` ≥ 7 d | — |
| 8 | Tribunal → Registrar | Draft award; scrutiny of form (checklist TPL-COM-P03) — Registrar suggestions within 10 WD (standard) / 5 WD (expedited) | `award_target` 3 m | Scrutiny never alters decision (S5 C6) **[VERIFY — open: scrutiny time within s.29A (S5 Part F Q3)]** |
| 9 | Registrar | Stamp (state of execution) → sign (QES/DSC) → deliver to each party's competent person | `award_stamping`; `arb_s34_window` | LR-ARB-014; LR-STAMP-001 |
| 10 | — | s.33 requests; s.34 tracking; execution pack | `arb_s33_*`, `arb_s34_window` | — |

### 7.11 Consent awards

| Situation | Route | Guard |
|---|---|---|
| Settlement during Equator arbitration | s.30 consent award (F-COM-38); tribunal records unless it objects | All parties request; terms lawful; stamped as award |
| Settlement in AMA mediation window | B03: tribunal records consent award | 8-week window; mediation vaults firewalled |
| Settlement in pre-suit mediation, no arbitration agreement | Default: run as **Part III conciliation** → s.73 settlement (s.74 status) | Appendix A B05 caution (consent award after settlement is open to "no live dispute" challenge) |
| Settlement in pre-suit mediation with existing/signed arbitration agreement | Consent award by a **different neutral** constituted for the purpose (LR-MED-021(b)) | Legal-review acknowledgement; F-COM-41 |
| NCLT/RERA/court proceedings pending | Consent terms for the forum (NCLT consent order, RERA record, CPC O.XXIII r.3 compromise) | Forum decides |

### 7.12 Three-member tribunals and equal-footing nomination (NN-03 exception)

| Step | Rule |
|---|---|
| Size | Sole default; three where agreement provides or parties agree, or claim + counterclaim > ₹10 crore (FR-P04-17; tenant-configurable; Board approval) |
| Equal-footing flag | Registrar alone sets `core.cases.equal_footing = true` on documented grounds: (a) both sides are business entities negotiating at arm's length (bespoke contract, not standard form); (b) no party is a repeat player under FR-P03-16; (c) not lender–borrower, insurer–policyholder, employer–employee or consumer; (d) grounds recorded in `equal_footing_grounds`; audited |
| Typical COM candidates | `com.corp.jv_deadlock`, `sha_breach`, `put_call_valuation`, `drag_tag`, `com.con.epc_private` (bespoke), `com.b2b.post_ma_indemnity`, `com.tech.it_outsourcing` (negotiated MSA) |
| Never | `com.bfs.nbfc_b2b_facility` (repeat-player lender), `com.re.homebuyer_*`, `com.msme.*` against PSU/government (DoE institutional preference), any bulk/API/clause_auto source |
| Nomination | Each side nominates one co-arbitrator (F-COM-36) from panel or outside within 15 d (`arb_nomination`); outside nominees: verification, conflict check and Sixth Schedule disclosure within 5 WD; Appointments Committee confirms (no discretion beyond eligibility/independence; reasons recorded) |
| Presiding | Always appointed by the Appointments Committee from an allocation run after consulting co-arbitrators; co-arbitrators never appoint (NN-03 prevails over A&C s.11(3) default) |
| Default | A side that fails to nominate in 15 d → Equator allocates that seat |
| DB | P03 constraint `nn03_party_nomination_equal_footing` (method `party_nomination` only when `equal_footing AND seat = 'co_arbitrator'`) |

### 7.13 Emergency arbitrator (India seat)

| Step | Rule / clock |
|---|---|
| Eligibility | Arbitration agreement under Equator Rules; tribunal not yet constituted; F-COM-11 with `ea.forum = emergency_arbitrator` |
| Fee | Card COM-STD C6 ₹3,00,000 fixed, applicant, before appointment (Appendix B prevails over P04 FR-P04-25 illustrative figure) |
| Appointment | By Equator within 2 business days (`ea_appointment`); disclosure ≤ 24 h; challenge ≤ 1 BD (`ea_challenge`) |
| Hearing and order | Schedule within 2 BD (`ea_schedule`); reasoned order within 14 days of appointment (`ea_decision`) |
| Follow-up | Notice of arbitration within 7 days of the EA application where not already served (`ea.noa_followup_days`, Equator Rules Sch.1 setting) |
| Effect | India seat: treated as s.17(1) order, enforceable under s.17(2) (*Amazon v Future Retail*); lapses if tribunal not constituted within 90 days (`ea_order_lapse`); EA not on tribunal unless all agree |
| Court alternative | s.9 pack shown in parallel; BG injunction standard (egregious fraud/irretrievable injustice) disclosed neutrally |

### 7.14 Expedited and documents-only

| Track | Eligibility | Tribunal | Process | Award | Fee |
|---|---|---|---|---|---|
| Expedited (Equator Rules Sch. 2) | Parties agree, or claim + counterclaim ≤ ₹3,00,00,000 (placeholder, Board approval) and no upheld objection within 7 d | Sole | One CMC; single hearing ≤ 2 days or documents-only; SoC/SoD 30 pages | 6 m from constitution (contractual); s.29A remains statutory outer limit | Tribunal × 0.75 (Appendix B C5) |
| s.29B fast track | Written agreement of all parties (F-COM-37) before/at appointment | Sole | Documents-only; oral hearing only if all request or tribunal needs clarification; written Q&A rounds (7-day answers) | 6 m from entering reference (`arb_s29b`; s.29B(5) applies s.29A(3)–(9)) | Tribunal × 0.75 |
| Recommendation (not default) | Liquidated money claims < ₹1 crore with documentary record (S2 REC) | — | Explorer suggests s.29B; never imposed | — | — |
| AI-assisted documents-only lane | Flag `com.ai_docs_only_lane` OFF; pilot only after counsel opinion (S5 Part F Q9) | Human tribunal decides and signs | Party validation of AI summaries; non-delegation attestation (NN-01, D3) | — | — |

---

## 8. Pre-litigation journey (COM)

The shared `prelit_case` machine (S4 B5.1; Appendix A §3.1–3.3) applies with these COM settings.

| Stage | COM rule |
|---|---|
| Suitability check | §4 decision table; arbitrability; limitation (CAL-COM-04); MSME precedence; IBC stage; DoE; urgent triggers |
| Mechanism default | **Part III conciliation** where respondent is a company/LLP/firm and an enforceable outcome is wanted (PL-02); contractual mediation where relationship-preserving, multi-party or the respondent prefers; negotiation-only for liquidated small claims (< ₹5 lakh) |
| Notice content | S4 B5.2 fields; sender = Equator case administrator with verification URL; no threat language; FD-COM-09 limitation notice; DPDP s.17(1)(a) context; COM-specific "Your other options" lists the forum cards triggered by §4 |
| Delivery | Corporate respondents: email to registered/legal contact + speed post to registered office (MCA master data) + WhatsApp/SMS to named officer; ≤ 6 contacts pre-consent; 08:00–19:00 |
| Response windows | Individuals D14; companies D30 (s.62(4) where conciliation invoked); one extension ≤ 14 d |
| Consent | Agreement to Mediate or s.62(2) written acceptance via Aadhaar eSign/DSC; corporate authority upload required before settlement signature (R-COM-30); sub-consents per BLK-CONSENT |
| Session | First information session free for respondent (PL-07); online default; neutral appointed in 3–5 WD |
| Settlement | Checklist: payment schedule, escrow, default/revival, GST credit note (CGST s.34(2) cut-off), TDS, statutory-forum step (r.8 / s.12A IBC / s.147 / RERA / NCLT r.26 / MSEFC withdrawal), confidentiality, consent-award clause, stamp computation |
| Conversion | s.73/s.74 (conciliation) · consent award (arbitration agreement, different neutral) · Lok Adalat recording pack (DLSA, LSA s.20(2)) · NCLT/RERA/court consent terms · contractual MSA |
| Non-settlement | Equator Mediation Closure Report (LR-MED-020 footer); Form-1 PIMS pack if suit intended (R-COM-12); MSME ODR pack; arbitration if clause |
| Compliance | Instalment and escrow milestones; breach → acceleration → consent award (if agreed) or suit on settlement / execution of s.74 settlement as award (s.36) |
| KPIs | S4 B5.7 definitions; COM targets: consent rate ≥ 35% voluntary / ≥ 70% clause programmes; settlement (commenced) ≥ 45%; median consent-to-signature ≤ 45 d; conversion to enforceable instrument ≥ 50% where eligible |

---

## 9. Document checklists per subtype

Formats: PDF/PDF-A, DOCX, XLSX/CSV, JPG/PNG, EML/MSG, ZIP of logs; ≤ 50 MB per file (bundles split automatically). Every upload is hashed (SHA-256) into `core.evidence_ledger`; electronic records exported with BSA s.63(4) certificate (NN-10); originals preserved, derived OCR/translations labelled (NN-32). M = mandatory, C = conditional, O = optional.

| Code | Document | M/C/O | Formats | Verification |
|---|---|---|---|---|
| D-B01 | Contract / framework / distributor / franchise / agency agreement with annexures (territory, price list, targets) | C (if exists) | PDF, DOCX | Clause parser; signatory match |
| D-B02 | POs, delivery challans, e-way bills, GRNs | M (supply) | PDF, JPG | E-way bill no. format check |
| D-B03 | Invoices (IRN/QR if e-invoiced), credit/debit notes | M (payment) | PDF | IRN QR verification (GSP) |
| D-B04 | Ledger/account reconciliation (both sides) | M | XLSX, CSV, PDF | Reconciliation engine |
| D-B05 | Quality complaints/rejection notices | C | PDF, EML | Date extraction (deemed acceptance) |
| D-B06 | Termination/show-cause/cure notices | C | PDF, EML | Service evidence |
| D-B07 | GSTR-1/2B extracts | O | PDF, CSV | GSTIN match |
| D-B08 | BGs, security deposits, PDCs | C | PDF | Bank confirmation (manual) |
| D-B09 | Legal notice and reply | C | PDF | Dates |
| D-B10 | Tender/GCC/SCC (government) | C (GOVT_SET) | PDF | Tender ref |
| D-C01 | Agreement, GCC, SCC, BoQ, drawings, LoA/LoI | M | PDF, DWG→PDF, XLSX | Index |
| D-C02 | Variation orders, EoT applications/decisions | C | PDF | — |
| D-C03 | RA bills, measurement books, certified/final bill | M | PDF, XLSX | Arithmetic check |
| D-C04 | Hindrance register, site minutes, correspondence log | C | PDF | — |
| D-C05 | Programme (baseline/updated), delay analysis | O | PDF, XER/MPP→PDF | — |
| D-C06 | BGs and invocation letters | C | PDF | — |
| D-C07 | LD deductions; price-variation workings and indices | C | PDF, XLSX | Index source check |
| D-C08 | Engineer/DAB decisions; notices of dissatisfaction | C | PDF | Tier status |
| D-C09 | CAR insurance policy | O | PDF | — |
| D-C10 | Competent-authority approval (government settlement/arbitration ≥ ₹10 crore) | C | PDF | Signatory designation |
| D-T01 | MSA/SOW/order forms | M | PDF | — |
| D-T02 | SLA schedule, service-credit table | C | PDF | — |
| D-T03 | Change requests | C | PDF, EML | — |
| D-T04 | Acceptance test reports | C | PDF, XLSX | — |
| D-T05 | Incident/RCA reports | C | PDF | — |
| D-T06 | DPA / data-processing terms | C | PDF | — |
| D-T07 | Source-code escrow agreement and release conditions | C | PDF | Escrow agent confirmation |
| D-T08 | IP assignment/licence deeds; registration certificates | C | PDF | IP India deep-link check (manual) |
| D-T09 | Usage logs/telemetry exports | O | CSV, JSON, ZIP | Hash on upload; BSA s.63 certificate |
| D-T10 | Royalty statements/audit reports | C | XLSX, PDF | — |
| D-R01 | Allotment letter; builder–buyer agreement/agreement for sale | M | PDF | — |
| D-R02 | Payment receipts and bank statements | M | PDF | Sum vs demand letters |
| D-R03 | RERA registration certificate and project page extract | C | PDF | State portal deep link |
| D-R04 | Demand letters; possession offer; OC/CC | C | PDF | — |
| D-R05 | Snag list/defect photos | C | JPG, PDF | EXIF retained (original) |
| D-R06 | JDA/development agreement; area-sharing; POA | C | PDF | Registration details |
| D-R07 | Lease deed (registered?), rent ledger | C | PDF, XLSX | Registration no. |
| D-R08 | Brokerage agreement | C | PDF | — |
| D-R09 | CERSAI search result | O | PDF | ~₹10/search, manual upload |
| D-R10 | RERA complaint/order copies | C | PDF | — |
| D-P01 | Partnership deed + amendments / LLP agreement + supplementary | M | PDF | — |
| D-P02 | Registrar of Firms certificate / LLP Form 3/4 | C | PDF | MCA (LLP) |
| D-P03 | 3 years' financials and capital accounts | M | PDF, XLSX | — |
| D-P04 | Bank statements | C | PDF | — |
| D-P05 | Client/asset lists | O | XLSX | — |
| D-P06 | Retirement/admission deeds | C | PDF | — |
| D-P07 | Valuation reports | O | PDF | Registered valuer no. |
| D-S01 | MoA/AoA | M | PDF | MCA |
| D-S02 | SHA/SSA/JV agreement | M | PDF | — |
| D-S03 | Cap table; register of members | M | XLSX, PDF | Cross-check MGT-7 |
| D-S04 | Board/general meeting minutes | C | PDF | — |
| D-S05 | MGT-7/AOC-4 extracts | C | PDF | MCA |
| D-S06 | ESOP plan/grant letters; founder vesting schedules | C | PDF | — |
| D-S07 | Valuation reports (s.247 registered valuer) | C | PDF | IBBI RV registry (manual) |
| D-S08 | Notices of breach/deadlock | C | PDF, EML | — |
| D-S09 | FEMA filings (FC-GPR/FC-TRS) | C | PDF | → INT if non-resident |
| D-S10 | NCLT petition/orders | C | PDF | Cause-list parser |
| D-S11 | s.442 reference order | C | PDF | — |
| D-I01 | Invoices/loan agreements | M | PDF | — |
| D-I02 | s.8 demand notice + proof of delivery | C | PDF | Delivery date |
| D-I03 | CD reply/notice of dispute | C | PDF | — |
| D-I04 | IU Record of Default / Information of Dispute (NeSL) | C | PDF | Upload; no API |
| D-I05 | Acknowledgements of debt | C | PDF | Limitation Act s.18 |
| D-I06 | NCLT order sheets; Form A public announcement | C | PDF | IBBI watcher |
| D-I07 | CoC minutes; Form G | C | PDF (restricted) | RP consent |
| D-I08 | Resolution plan drafts (confidential) | O | PDF | Ring `experts_only` |
| D-M01 | Udyam certificate (registration date) | M | PDF | Aggregator verify |
| D-M02 | PO/contract | M | PDF | — |
| D-M03 | Invoices | M | PDF | IRN check |
| D-M04 | Delivery proof/GRNs | M | PDF | — |
| D-M05 | Acceptance/objection emails | C | PDF, EML | Objection date |
| D-M06 | Ledger; payment history | M | XLSX, PDF | Part-payment schedule |
| D-M07 | Buyer's MSME-1 disclosure | O | PDF | MCA |
| D-M08 | GST returns | O | PDF | — |
| D-Q01 | Cheque copy (front/back) | M | JPG, PDF | — |
| D-Q02 | Bank return memo | M | PDF | Reason code |
| D-Q03 | Demand notice + postal/e-delivery proof | C | PDF | Received date |
| D-Q04 | Complaint and order sheets | C | PDF | Stage |
| D-Q05 | Underlying invoices/loan document | O | PDF | — |
| D-F01 | BG/LC instrument and invocation | C | PDF | Issuing bank confirmation (manual; SFMS via bank only) |
| D-F02 | Facility agreement/sanction letter | C | PDF | Clause at origination (NN-03) |
| D-F03 | Factoring/TReDS records | C | PDF, CSV | Platform statement |

---

## 10. Practical difficulties and product solutions

| # | Difficulty | Subtypes | Product solution |
|---|---|---|---|
| PD-01 | Respondent will not engage (private mediation has no compulsion) | all | Neutral institutional sender + verify page; D0–D30 cadence; first session free; Genuine-steps log export (PL-10); Form-1 pack and MSEFC/NCLT cards make the statutory alternative visible; portfolio protocols for enterprise tenants |
| PD-02 | Corporate respondents slow to authorise | all | Route to legal head/GRO; authority-upload checklist; board-resolution template; `extension_days` once |
| PD-03 | PO-only relationships; clause buried in T&Cs | b2b | W-INCORP; post-dispute submission agreement (F-COM-41); conciliation default |
| PD-04 | GST and TDS consequences of settlement discounts | b2b, msme, con | Auto-inserted credit-note clause with CGST s.34(2) cut-off (30 Nov or annual-return date, whichever earlier); TDS clause; "consult your tax adviser" disclosure (no advice) |
| PD-05 | Unregistered firm cannot sue | b2b, part | LR-PART-002 explainer; arbitration/conciliation offered |
| PD-06 | Government officers fear audit/CVC questions on settlements | con, b2b gov | HLC-ready proposal with claim-wise matrix, mediator's factual report, approval-ready annex; status `pending_competent_authority_approval` |
| PD-07 | Massive construction records (10k+ pages, BoQ spreadsheets, CAD) | con | DMS chunked upload, OCR, BoQ XLSX viewer, bundle builder with page sync, delta indices; storage tier per App. L |
| PD-08 | Multi-party (sub-contractors, lenders' engineer, consortium) | con, ibc | Linked matters, joinder (F-COM-22), shared clock groups, per-party authority |
| PD-09 | Trade secrets and source code | tech, corp | Confidentiality rings, watermarking, view-only redacted copies, experts-only rooms, ring undertakings |
| PD-10 | Logs/code authenticity | tech | Hash on upload, BSA s.63(4) certificate (Part A/B), chain-of-custody export |
| PD-11 | Promoter insolvency mid-mediation | re, b2b, con | IBBI public-announcement watcher → `on_hold.ibc_moratorium` banner; claim-to-RP guidance |
| PD-12 | Many allottees want most-favoured-nation terms | re | Group mediation with class session; MFN clause library; individual caucuses sealed |
| PD-13 | Mortgaged units/lender NOCs | re | CERSAI manual check prompt; lender-NOC condition precedent in memo |
| PD-14 | Information asymmetry in company disputes | corp | Neutral evaluator/forensic accountant under ring; valuation band labelled indicative; expert determination |
| PD-15 | SHA terms not in AoA | corp | Settlement pack auto-generates AoA special resolution (*V.B. Rangaraj*) |
| PD-16 | Listed-company disclosure | corp | LODR Reg 30 material-event card; settlement timing note |
| PD-17 | Non-resident shareholders (FEMA pricing) | corp | Reroute or link INT; FEMA disclosure; no Equator pricing opinion |
| PD-18 | 14-day IBC admission speed | ibc | Fast lane: mediator in 1 WD, 7–10-day desk, pre-drafted r.8 memo |
| PD-19 | Settlement after admission but before CoC — cannot withdraw | ibc | Block "withdraw" CTA; draft-and-hold; s.12A window explainer; CoC engagement pack ready for day of constitution |
| PD-20 | Confidentiality vs *Mobilox* evidence | ibc | Closure report annexable only with debtor's written consent (LR-IBC-009) |
| PD-21 | CIRP costs on withdrawal | ibc | Mandatory CIRP-cost clause in s.12A annex |
| PD-22 | Frivolous-filing penalty raises stakes | ibc | Neutral information card only (no merit view) |
| PD-23 | MSE registration date after contract | msme | W-NBCC warning; counsel-review flag; calculator still runs |
| PD-24 | s.16 interest waiver pressure from buyer | msme | Full interest displayed; waiver needs express initialled clause (LR-MSME-010) |
| PD-25 | No API for MSME ODR, NCLT, RERA, IP India | msme, ibc, re, tech | Export packs in portal field order; deep links; manual capture forms; "not an official record" labels |
| PD-26 | Cheque complainant uses Equator as leverage for conviction threat | chq | Template/AI lint blocks conviction language (VG-COM-08); court-decides declaration |
| PD-27 | Limitation running during talks | all | U-05 red banner; FD-COM-09; standstill template only after counsel sign-off |
| PD-28 | Award stamping across states | arbitration | State of execution recorded at signature; e-stamp before release; differential-duty check for enforcement state |
| PD-29 | Deposits unpaid by respondent | arbitration | Either party may pay other's share; s.38(2) notice; *Harshbir Singh Pannu* recall route |
| PD-30 | s.29A expiry risk | arbitration | AP-29A alerts; court pack at T-60/day 480; no back-dating |

---

## 11. Integrations and APIs

| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| MCA21 V3 via aggregator (`KYC_PORT.mca`, e.g., Surepass MCA Data APIs) | CIN/LLPIN master, directors (DIN), status (active/strike-off/under liquidation), charge index | Company master data | Public records; DPDP s.7 legitimate use / s.17(1)(a) for respondent data | API (aggregator) + monthly OGD bulk refresh | Manual upload of MCA printouts; label "not an official record" |
| ROC charge index (CHG-1/CHG-4) | Secured-creditor check before asset settlements | Charges | Public | via MCA adapter | Manual |
| GSTN via GSP/ASP | GSTIN validation; return filing status; e-invoice IRN/QR verification | GSTIN, filing status | Public/consented | API | Certificate upload |
| Udyam (aggregator) | Category and registration date (s.18 standing) | Udyam record | Public verification | API (aggregator) | Certificate upload |
| MSME ODR portal / Samadhaan | MSEFC filing by supplier | Export pack | Supplier's own filing | Export (CSV + PDF in portal field order) | — (no API) |
| TReDS platforms (RXIL, M1xchange, Invoicemart, others) | Discounting status | Invoice status | Party consent | Field capture | Statement upload |
| IBBI website | Public announcements (Form A), CIRP/liquidation lists, IP/RV registry | Public | Public | Scheduled scraper + manual verify ("never conclusive") | Manual |
| Information Utility (NeSL) | Record of Default / Information of Dispute | IU certificate | Party upload | Manual upload | — |
| NCLT (nclt.gov.in cause lists; efiling.nclt.gov.in) | Party/CP-number alerts; order downloads | Cause lists (PDF) | Public | PDF parser | Manual entry |
| e-Courts/NJDG via aggregator (`KYC_PORT.ecourts`) | Parallel litigation, NI Act cases, Commercial Court cases | CNR status | Public | Aggregator API, labelled "not an official record" | Manual |
| State RERA portals | Project registration, extensions, QPRs, complaint status | Public | Public | Deep-link catalogue per State | Manual capture form |
| CERSAI | Security interests over property/receivables | Search result | Public search (~₹10/search) | Manual upload | — |
| IP India | TM/patent/design status | Public | Public | Deep links | Manual |
| CCI | Orders, combination notices | Public | Public | Deep links | — |
| RBI | Bank Rate (s.16), repo | Rate table | Public | Admin-maintained table with source URL per change (`rules.param`) | — |
| SBI MCLR | RERA interest | Rate table | Public | Admin-maintained | — |
| `ESTAMP_PORT` (Leegality BharatStamp; Digio/SignDesk) | Stamping awards/settlements by state of execution | Instrument, duty | State stamp law | API | Physical stamp (MH, TG, WB per Setu list) |
| `ESIGN_PORT` (Leegality; Digio/Setu) | Settlement, agreements, consents | Signer evidence | IT Act ss.3A, 5 | API | DSC |
| `ESCROW_PORT` (RazorpayX Escrow+/Castler) | Settlement funds (NN-13) | Escrow milestones | RBI PA Directions 2025 | API | Direct payment with proof |
| `POSTAL_PORT` | Speed post to registered offices | Tracking | — | API/manual | Manual tracking entry |
| Group: LawDocs | Deed drafting shells (dissolution, SPA, JDA amendment) | Templates | Internal | REST | Manual |
| Group: BestComply | MSME-1 / Reg 30 compliance cross-checks for enterprise tenants | Compliance status | Tenant consent | REST | — |

APIs exposed (additions to P08 §7.3; all `/v1`, RFC 9457 errors, idempotency keys on POST):

| Method + path | Purpose | Roles |
|---|---|---|
| POST `/v1/cases/{caseId}/com/triage:evaluate` | COM rule pack (alias of generic triage with COM inputs) | party (own), case_manager |
| POST `/v1/cases/{caseId}/com/pims-pack` | Generate F-COM-24 PDF | claimant, counsel |
| POST `/v1/cases/{caseId}/com/msefc-election` | F-COM-26 | supplier |
| POST `/v1/cases/{caseId}/com/msme-odr-pack` | Export pack | supplier, case_manager |
| POST `/v1/cases/{caseId}/com/ibc/desk` · `/ibc/r8-memo` · `/ibc/s12a-annex` · `/ibc/ppirp-pack` | IBC outputs | parties, case_manager |
| POST `/v1/cases/{caseId}/com/hlc-proposal` · PUT `/com/hlc-proposal/{id}/approval` | HLC proposal; approval upload | parties, govt party_org_user |
| POST `/v1/cases/{caseId}/com/s442-reference` | F-COM-33 | case_manager, neutral_mediator (assigned) |
| POST `/v1/cases/{caseId}/com/rera-memo` | F-COM-34 | parties |
| POST `/v1/cases/{caseId}/com/cap-table` | F-COM-35 (tier High) | parties (own) |
| POST `/v1/cases/{caseId}/com/equal-footing` | Registrar sets flag with grounds | registrar |
| POST `/v1/cases/{caseId}/com/nominations` | F-COM-36 | party (equal_footing only) |
| POST `/v1/cases/{caseId}/com/consent-award-requests` | F-COM-38 | all parties |
| POST `/v1/cases/{caseId}/com/compounding-memo` | F-COM-39 | parties |
| POST `/v1/cases/{caseId}/com/tpf-disclosures` | F-COM-40 | parties |
| GET `/v1/com/watchers/ibbi?cin=` | Debtor-in-CIRP check | case_manager |

---

## 12. Calculators

All calculators follow FR-P08-08: pure TypeScript in `packages/rules/calculators/com/`, Zod inputs, parameters from the pinned ruleset, `indicative: true`, `computation_trace[]`, `assumptions[]`, disclaimer key `calc.com.indicative` ("Figures computed from the inputs and rules entered. The tribunal, court or forum decides. Not legal advice."). Never "value" a claim or predict an outcome (NN-01). Money in minor units; rounding half-up at presentation only.

| ID | Key | Inputs | Formula / logic | Golden test vectors |
|---|---|---|---|---|
| CAL-COM-01 | `com.msme_interest@2` | Per invoice: principal, acceptance/deemed-acceptance date (objection > 15 days ignored), credit basis (agreed ≤ 45 d / none → appointed day = +15 d), part-payments (date, amount, allocation `interest_first` \| `principal_first`, default `interest_first` [VERIFY — statute silent]), payment/as-of date, Bank Rate table (piecewise by month) | Due date Dᵢ = acceptance + min(agreed, 45) (or +15); r = 3 × Bank Rate applicable in each month; default convention `calendar_monthly_rests_residual_simple`: n full calendar months from Dᵢ, d residual days: `I = P × [(1 + r/12)^n × (1 + (r/12) × d/30) − 1]`; alternative `fractional_months_30`: `P × ((1 + r/12)^(days/30) − 1)`; piecewise rate change compounds month by month | V1: P ₹10,00,000; acceptance 15 Jan 2026; agreed 45 d → due 1 Mar 2026; paid 19 Jul 2026 (140 d; n = 4, d = 18); Bank Rate 6.00% (fixture) → r 18% → **₹70,915.82** (alt ₹71,950.83). V2: same, Bank Rate 5.75% (7 Oct 2026) → r 17.25% → **₹67,883.50** (alt ₹68,873.98). V3: ₹10,00,000 overdue exactly 6 months at 17.25% → 10,00,000 × (1.014375)^6 = **₹10,89,409.66** (interest ₹89,409.66). Medium enterprise → `COM_MSMED_NOT_ELIGIBLE` |
| CAL-COM-02 | `com.contract_interest@1` | Principal, rate, simple/compound (monthly), start, end | Simple `P × r × days/365`; compound `P × ((1 + r/12)^m − 1)`; label "claimed — tribunal/court decides (CPC s.34; A&C s.31(7)(a))" | ₹25,00,000 @12% simple, 1 Jan–31 Dec 2025 (365 d) → **₹3,00,000**; monthly compound 12 m → **₹3,17,062.58** |
| CAL-COM-03 | `com.post_award_interest@1` | Award sum, award date, `current_rate_of_interest` (Interest Act 1978 s.2(b) meaning; registrar-entered with source) [VERIFY — open: source series], payment date | If award silent: rate = current rate + 2% p.a., simple, from award date to payment (s.31(7)(b)) | ₹50,00,000; current rate 7.25% (fixture) → 9.25%; 365 d → **₹4,62,500** |
| CAL-COM-04 | `com.limitation@1` | Claim type (Article), cause date, acknowledgements (s.18), part-payments (s.19), exclusions (PIMS period, inclusive-days convention), IBC default date, NI dates | Last date = start + period (+ excluded days); flags < 30 d (U-05) | Ack 5 Jan 2024 (Art. 14/55, 3 y) → **5 Jan 2027**; PIMS Form-1 1 Dec 2026, Form-3 14 Jan 2027 (45 d inclusive) → **19 Feb 2027**. NI: memo 2 Nov 2026 → notice by **2 Dec 2026**; notice received 10 Nov 2026 → pay by **25 Nov 2026** → cause of action 26 Nov 2026 → complaint by **26 Dec 2026** (day of cause of action excluded — same convention as V1 C-FIN-11; v3.1 correction of "25 Dec 2026") |
| CAL-COM-05 | `com.pims_check@1` | Commercial? (CCA s.2(1)(c)), specified value, urgent relief, arbitration agreement | Banner + Form-1 pack if commercial ∧ value ≥ ₹3,00,000 ∧ ¬urgent ∧ ¬agreement | ₹12,00,000, no clause, no urgency → `PIMS_REQUIRED_LSA` |
| CAL-COM-06 | `com.ibc_eligibility@1` | Default amount, debtor MSME category, stage, prior insolvency 3 y | CIRP if default ≥ ₹1,00,00,000; PPIRP (CD only) if MSME ∧ default ≥ ₹10,00,000 ∧ no prior 3 y | Default ₹85,00,000, small CD → CIRP **not available**; PPIRP **available to CD**; creditor route → B2B/MSME |
| CAL-COM-07 | `com.coc_vote@1` | FC voting shares %, approvals | Approve% = Σ shares approving; thresholds: 90% (s.12A IBC), 66% (plan/restoration/liquidator replacement), 51% (PPIRP initiation — [VERIFY]) | Shares A 42.5, B 30, C 18, D 9.5; A+B+C approve → **90.5% ≥ 90 → s.12A threshold met**; A+B only → 72.5% → fails 90, meets 66 |
| CAL-COM-08 | `com.s244_eligibility@1` | Issued shares, holdings of applicants, total members, applicant members | Eligible if applicants ≥ min(100, ⌈members/10⌉) members OR holding ≥ 10% issued capital (company with share capital) | 10,00,000 shares; applicants hold 95,000 (9.5%) → capital limb fails; members 40, applicants 4 → 4 ≥ 4 → **eligible** |
| CAL-COM-09 | `com.rera_interest@1` | Payments (date, amount), refund date, State, rate rule (default SBI highest MCLR + 2%, simple; State override) | Σ amountᵢ × rate × daysᵢ/365 | Rate 11.00% (fixture MCLR 9.00% + 2%); ₹20,00,000 on 1 Apr 2023 (1,279 d) → ₹7,70,904.11; ₹30,00,000 on 1 Oct 2023 (1,096 d) → ₹9,90,904.11; refund 1 Oct 2026 → **₹17,61,808.22** |
| CAL-COM-10 | `com.ni138_cost@1` (COM alias of `fin.ni138_cost@1`) | Cheque amount, stage, fine assumption | Compounding = amount × stage % (0 / 5 / 7.5 / 10; *Sanjabij Tari*); interim compensation ≤ 20% (s.143A); appeal deposit ≥ 20% of fine (s.148) | ₹8,00,000 after defence evidence, before judgment → **₹40,000**; interim max **₹1,60,000** |
| CAL-COM-11 | `com.fee_estimate@2` | Claim, counterclaim, tribunal size, track, MSE concession | Appendix B Card COM-STD (C1–C12); Fourth Schedule per arbitrator, cap ₹30,00,000 then sole +25%; expedited ×0.75; GST forward + RCM split (WE-04) | WE-04: ₹1,50,00,000 sole standard → tribunal **₹4,84,375**; admin ₹1,27,500; registration ₹20,000; total tax incidence ₹1,13,737.50 (₹26,550 forward + ₹87,187.50 RCM). Three-member ₹25,00,00,000: per arbitrator ₹19,87,500 + 0.5% × ₹5,00,00,000 = **₹22,37,500** × 3 = **₹67,12,500**; admin ₹4,25,000 + 0.15% × ₹15,00,00,000 = **₹6,50,000** |
| CAL-COM-12 | `com.price_variation@1` | Value of work in period R, fixed share a, weights b, c, d, base and current indices | `Adj = R × [a + b·Mi/M0 + c·Li/L0 + d·Fi/F0] − R` (contract formula governs; weights sum 1) | R ₹2,00,00,000; a .15, b .45, c .25, d .15; M 150→165, L 400→428, F 120→132 → factor 1.0775 → **₹15,50,000** |
| CAL-COM-13 | `com.ld_cap@1` | Contract value, LD rate per week, cap %, delay weeks | LD = min(value × rate × weeks, value × cap); note: s.74 Contract Act — LD is a ceiling (*Kailash Nath*) | ₹50,00,00,000; 0.5%/week; cap 10%; 26 weeks → raw 13% → **₹5,00,00,000** (capped) |
| CAL-COM-14 | `com.sla_credit@1` | Monthly fee, SLA tiers (threshold → credit %), actual metric, cap % | Credit = fee × tier% (≤ cap) | Fee ₹12,00,000; target 99.5%, actual 98.9% → tier 10%; cap 25% → **₹1,20,000** |
| CAL-COM-15 | `com.royalty_trueup@1` | Rate, reported and audited net sales, paid, interest rate, days | Due = rate × audited; shortfall = due − paid; interest simple | 4% × ₹14,10,00,000 = ₹56,40,000; paid ₹50,00,000 → shortfall **₹6,40,000**; 12% × 200 d → **₹42,082.19** |
| CAL-COM-16 | `com.partner_exit@1` | Capital, current account, goodwill method (avg profit × years' purchase × share), excess drawings | Payout = capital + current + goodwill share − excess drawings (deed formula overrides) | ₹25,00,000 + ₹3,40,000 + (₹60,00,000 × 2 × 25% = ₹30,00,000) − ₹1,20,000 = **₹57,20,000** |
| CAL-COM-17 | `com.doe_check@1` | Counterparty type, dispute value, approval ref | GOVT_SET ∧ value ≥ ₹10,00,00,000 ∧ ¬approval → arbitration blocked (LR-PROC-001) | CPSE, ₹12,00,00,000, no approval → **`COM_GOVT_ARB_APPROVAL_REQUIRED`** |
| CAL-COM-18 | `com.pims_fee@1` | Value | ₹1,000 application; Schedule II bands ₹15,000 / ₹30,000 / ₹40,000 / ₹50,000 / ₹75,000 shared equally | ₹45,00,000 → **₹30,000** (₹15,000 each) + ₹1,000 |
| CAL-COM-19 | `com.nclt_fee@1` | Applicant type | FC ₹25,000; OC ₹2,000; CD ₹25,000 (AAA Rules r.10 Sch.) [V-secondary] | OC → **₹2,000** |
| CAL-COM-20 | `com.ibc_window@1` | Admission date, CoC constitution date, Form G date | State: `pre_admission` / `admitted_pre_coc` (withdrawal blocked) / `window_open` / `closed` | Admitted 1 Oct 2026, CoC 28 Oct 2026, no Form G → **`window_open`**; Form G 20 Nov 2026 → **`closed`** |
| CAL-COM-21 | `com.vol_liq_withdrawal@1` | Creditor claims, approvals | 2/3 in value of creditors + special resolution (s.59(5A)–(5C)) | Claims ₹9 cr; approvals ₹6.3 cr → 70% → **met** |

---

## 13. Outputs, templates, enforcement and registration route

### 13.1 Output catalogue

| Output | Template | Legal label (copy-lint) | Signature / stamp | Enforcement route | Registration |
|---|---|---|---|---|---|
| Contractual settlement agreement | TPL-COM-S02 | "Settlement Agreement (contract) under the Equator Mediation Rules" | e-sign; stamp per state (agreement article) | Suit on contract; consent award if agreed later | NN-08 if immovable property |
| Conciliation settlement | TPL-COM-S03 | "Settlement Agreement under section 73 of the Arbitration and Conciliation Act, 1996, having the status of an arbitral award on agreed terms (section 74)" | Parties sign; conciliator authenticates; stamp as award | A&C s.36 execution (as decree) | NN-08 if property |
| Consent award | TPL-COM-S01 | "Arbitral award on agreed terms (section 30)" | Tribunal signs; stamped at signing | s.36 | NN-08 if property |
| Arbitral award | TPL-COM-A01 (severable paras, computation annex, s.31(7) clause) | "Arbitral award" | QES/DSC; stamped; delivered per party | s.36 after s.34 window/disposal; execution where assets are (*Sundaram Finance v Abdul Samad* (2018) 3 SCC 622) | — |
| HLC-ready proposal | TPL-COM-S05 | "Settlement proposal for approval of the competent authority" | Initialled; binding only on approval | Becomes settlement agreement on approval | — |
| RERA settlement memo | TPL-COM-S06 | "Settlement terms for recording by [Authority/Commission]" | e-sign; stamp per state | Order of Authority/Commission | Modified agreement/conveyance → registration |
| Tech exit settlement | TPL-COM-S07 | as S02 + data-return/deletion certificate | e-sign | Suit/consent award | — |
| Partnership deeds | TPL-COM-S08 | "Deed of retirement / dissolution" | e-sign (non-property) / physical (property) | Contract | Registrar of Firms notice; LLP Form 4 (30 d) |
| Corporate settlement pack | TPL-COM-S09 | SPA, SHA amendment, AoA resolution, board/EGM resolutions, SH-4, NCLT consent terms | e-sign; share-transfer stamp 0.015% | Contract / NCLT consent order | MCA filings (MGT-14 etc. as applicable) |
| s.442 settlement / failure report | TPL-COM-S10 / R03 | "Settlement under rule 24, Companies (Mediation and Conciliation) Rules, 2016" | Parties + counsel sign | NCLT r.26 order | — |
| IBC settlement + r.8 memo | TPL-COM-S11, L04 | "Settlement agreement (conditional on NCLT withdrawal)"; "Joint memo for withdrawal under rule 8" | e-sign; stamp | NCLT order | — |
| s.12A IBC support annex | TPL-COM-L05 | "Support annex for the resolution professional's application under section 12A, IBC" | — | NCLT order | — |
| PPIRP pack | TPL-COM-L06 | Draft special resolution, directors' declaration, base-plan term sheet | Board/members sign | CD files s.54C | — |
| Cheque compounding memo | TPL-COM-S12 | "Settlement and joint application for compounding (section 147, NI Act)" | e-sign; stamp | Court compounds | — |
| MSME ODR pack | TPL-COM-L07 | "Export pack for filing on the MSME ODR portal" | — | Supplier files | — |
| PIMS Form-1 pack | F-COM-24 | "Form-1 application prepared for filing with the Legal Services Authority" | Applicant signs | Authority process | — |
| Closure report | TPL-COM-R01/R02 | "Equator Mediation Closure Report" | CM | — | — |
| Lok Adalat referral note | TPL-COM-L08 | "Joint application to the [DLSA] for recording settlement (LSA Act s.20(2))" | parties | Lok Adalat award = decree (s.21) | — |

### 13.2 Mandatory footers and lint
- All closure/non-commencement reports: LR-MED-020 footer verbatim.
- IBC pre-s.9 closure report adds: "This report is not issued under any regulation of the Insolvency and Bankruptcy Board of India. It may be filed with an application under section 9 of the Insolvency and Bankruptcy Code, 2016 only with the written consent of [debtor name] recorded on [date]."
- Government proposals: "This proposal does not bind [entity] until approved in writing by the competent authority."
- Copy-lint blocks (template + CMS + AI): "NCLT-empanelled Equator", "IBBI-approved mediation", "RERA conciliation forum" (unless `com.rera_forum_tieup` ON with recognition ref), "MSEFC-empanelled" (until listed), "statutory MSME mediation", "s.12A certificate", "PIMS certificate", "court-recognised mediation", "decree", "binding on NCLT", "withdraw your insolvency case" (outside window), conviction threats. Allowed: "private pre-insolvency mediation", "[Name] — member, MCA Mediation and Conciliation Panel ([Region])".

### 13.3 Enforcement and registration rules
1. Every award and settlement instrument is e-stamped under the stamp law of the **state of execution (last signature)** before release, with a differential-duty check for the enforcement state (LR-STAMP-001/002; *URC Construction*). Physical-stamp states (MH, TG, WB per Setu list) route to procurement-partner workflow.
2. Instruments transferring/partitioning immovable property, JDA amendments, conveyances, POAs → physical execution, stamping and registration (NN-08; IT Act s.1(4); Registration Act s.17; `registration_4m`).
3. Execution packs (App. R §4): s.36 petition checklist, s.34 status, stamp certificate, delivery evidence, asset information (*Rahul S. Shah v Jinendra Kumar Gandhi* (2021) 6 SCC 418 directions), "no automatic stay" disclosure (LR-ARB-017).
4. Statutory-forum steps are tracked as compliance obligations: r.8 withdrawal, s.12A IBC order, r.26 NCLT order, RERA recording, s.147 compounding order, MSEFC withdrawal — with owner and due date (NN-04).

---

## 14. Dashboards, KPIs and enterprise hooks

### 14.1 KPIs (SQL views in `com` schema; FR-P08-11; no outcome-by-neutral views; n < 5 suppressed; any publicly published cell n ≥ 10, X-28)

| KPI | Definition | Y1 target |
|---|---|---|
| Time to constitution | Median days commencement → `tribunal.constituted` | ≤ 30 d (expedited ≤ 14 d) |
| Pleadings-to-award | Median months | ≤ 12; 100% within s.29A |
| Award target | Final hearing → award | ≤ 3 m in ≥ 90% |
| Scrutiny turnaround | Draft submitted → form approved | ≤ 10 WD (expedited 5 WD) |
| EA decisions | Within 14 d of appointment | ≥ 95% |
| Mediation/conciliation cycle | Consent → signature (median) | ≤ 45 d |
| Settlement rate (commenced) | Settled (full/partial) ÷ matters with ≥ 1 substantive session, per L2 | ≥ 45% |
| Conversion to enforceable instrument | s.73/s.74 + consent awards ÷ settlements (where eligible) | ≥ 50% |
| IBC Desk speed | Intake → signed settlement (pre-admission) | median ≤ 10 d |
| IBC withdrawals supported | r.8 / s.12A orders uploaded ÷ IBC desk settlements | report only |
| MSME interest exposure | Σ s.16 interest computed on open MSME cases | report only |
| MSME hand-offs | MSME ODR packs generated ÷ MSME cases not settled | report only |
| Statutory hand-off accuracy | QA sample: correct forum signposted | ≥ 98% |
| s.34 challenges / set aside | Challenges ÷ awards; awards set aside (published, D12) | ≤ 10% / published |
| Compliance | Settlements fully performed by due date | ≥ 85% (≥ 90% with escrow) |
| Government settlements approved | HLC proposals approved ÷ submitted | report only |
| Clause programme | Partners; agreements covered; resulting cases | report only (NN-16: priority affects admin speed only) |

### 14.2 Widgets (P09 dashboard framework)
s.29A risk board · award scrutiny queue · EA tracker · IBC window board (`admitted_pre_coc` / `window_open` / `closed` counts with days to Form G) · MSME interest exposure · DoE approvals pending · RERA group-mediation board · clause-programme funnel · s.442 credential roster (neutral-facing: region, valid_from, February-window reminder).

### 14.3 Enterprise hooks (events; payloads exclude caucus/confidential content)
Existing (FR-P08-33): `equator.com.clause.adopted.v1`, `equator.com.arbitration.constituted.v1`, `equator.com.award.published.v1`, `equator.com.msme.reference_prepared.v1`. New:

| Event | Payload (keys) |
|---|---|
| `equator.com.triage.routed.v1` | case_id, l1, l2, ladder, routes_offered[], routes_blocked[] (codes), signposting[] |
| `equator.com.pims.pack_generated.v1` | case_id, authority, specified_value_minor |
| `equator.com.pims.outcome_recorded.v1` | case_id, outcome (form3/form4/form5), outcome_on |
| `equator.com.ibc.window_changed.v1` | case_id, state, coc_constituted_on, form_g_on |
| `equator.com.ibc.withdrawal_order_recorded.v1` | case_id, route (r8/s12a), order_date |
| `equator.com.hlc.proposal_submitted.v1` / `.approved.v1` / `.rejected.v1` | case_id, entity_type, value_band |
| `equator.com.s442.reference_recorded.v1` / `.report_filed.v1` | case_id, tribunal, region, outcome |
| `equator.com.msme.interest_computed.v1` | case_id, invoices_count, interest_minor, bank_rate_version |
| `equator.com.equal_footing.set.v1` | case_id, set_by, grounds_hash |
| `equator.com.consent_award.requested.v1` | case_id, source |
| `equator.com.settlement.forum_step_due.v1` | case_id, forum_step, due_on |

---

## 15. Competitor notes and Equator differentiation

| Competitor | COM-relevant offer (as researched) | Equator differentiation |
|---|---|---|
| Presolv360 | Published arbitration fees (₹5,000 ≤ ₹50k … cap ₹30 lakh), MSME arbitration from ₹2,750, mediation registration ₹4,500 + ₹5,000/session; execution support [V presolv360.com/fees] | Part III conciliation as default enforceable pre-suit output; MSME-first signposting with full s.16 computation (not arbitration-first, which *Mahakali* overrides); IBC Desk; DoE-aware government track |
| Jupitice | MSME "digital court" (2021), BFSI portfolios, marketplace with take-rate; e-stamp/e-sign (Jul 2026) | No "court" branding (NN-17); no paid listings, featured slots or take-rate in the institutional neutral directory or allocation (NN-28); sponsored placement exists only on the separate, labelled Private Practice Marketplace for non-advocate providers, flag `marketplace.paid_placement` OFF (NN-34); allocation logs in Independence Evidence Pack |
| Sama | Commercial & co-founder mediation; arbitration ≤ 180 days; staged fees; "unpaid settlement fee → barred" | Flat, published, Board-approved cards with no outcome-linked fees in arbitration (Appendix B); s.442 credentialed neutrals; founder disputes with corporate settlement pack |
| CORD | Rules 2.0 (4 Sep 2026): appellate mechanism, Appointments Council, AI governance, MSME and SMART ODR | Equivalent appeal tier (opt-in), Appointments Committee, published AI governance — plus statutory-forum precision (IBC 2026 s.12A window, MSMED 2026 readiness, DoE gating) |
| MCIA / IIAC / ICA / SAROD / DIAC (Delhi) | Institutional arbitration; IIAC fast track (6 m), EA (3/15 d), scrutiny within 21 d; MCIA EA fee ≤ 20% of sole max, floor ₹3 lakh | Faster published SLAs (scrutiny 10 WD; EA appointment 2 BD); integrated mediation/conciliation ladder; online-first; transparency report (S5 C3); appointment defensibility under *CORE* |
| MSME ODR portal (Government) | Free filing to MSEFC; 17 disposals in first 8 months (15 pre-MSEFC) [V-partial] | Integrate, not compete: export pack; readiness dossier to be listed as MSP/ADR service provider under MSMED 2026 (flag) |
| Court-annexed PIMS (DLSA/SLSA) | Statutory s.12A mediation | Equator never claims s.12A status; prepares Form-1; mediates privately in parallel where lawful |
| MahaRERA conciliation forum | Two-member bench, ₹1,000 fee, 60 + 30 d | Group mediation tooling; association-sponsored hosting only with recognition |

Positioning claims require Claims Register entries (NN-17). Never publish neutral win-rates or settlement rates by neutral (NN-16, NN-28).

---

## 16. Data-model extensions (`com` schema)

Existing tables kept: `com.contracts` (Appendix F §F.8), `com.pims_referrals` (F.4.14), `com.case_ext` and `com.tribunals` (P08 §7.2), `com.calc_runs` (FR-P08-08). ADR "COM table reconciliation": `com.contracts` holds contract/clause facts; `com.case_ext` holds case-level COM attributes; no column duplicated (migrate `com.case_ext.has_arb_agreement` → derived view over `com.contracts`).

### 16.1 New tables

```sql
CREATE TABLE com.subtype_catalog (                 -- seeds §2.2; versioned with ruleset
  code text PRIMARY KEY,                           -- 'com.ibc.s12a_withdrawal_settlement'
  l1 text NOT NULL CHECK (l1 IN ('b2b','con','tech','re','part','corp','ibc','msme','chq','bfs','reg')),
  label_i18n jsonb NOT NULL, default_ladder text NOT NULL,
  neg_allowed boolean NOT NULL, med_allowed boolean NOT NULL,
  arb_policy text NOT NULL CHECK (arb_policy IN ('allowed','conditional','blocked','signpost_only')),
  signpost_forums text[] NOT NULL DEFAULT '{}', legal_rule_ids text[] NOT NULL DEFAULT '{}',
  legacy_codes text[] NOT NULL DEFAULT '{}', ruleset_version_id uuid NOT NULL);

ALTER TABLE com.case_ext
  ADD COLUMN l1 text, ADD COLUMN l2 text REFERENCES com.subtype_catalog(code),   -- SET NOT NULL after backfill
  ADD COLUMN legacy_dispute_type text,
  ADD COLUMN counterparty_govt boolean NOT NULL DEFAULT false,
  ADD COLUMN govt_entity_type text,
  ADD COLUMN dispute_value_minor bigint,
  ADD COLUMN approval_ref text,                     -- DoE competent-authority approval (LR-PROC-001)
  ADD COLUMN urgency_codes text[] NOT NULL DEFAULT '{}',
  ADD COLUMN confidentiality_ring text CHECK (confidentiality_ring IN ('none','parties_and_counsel','counsel_only','experts_only'));
-- Migration order: add l1/l2 nullable → backfill from legacy dispute_type via §2.4 mapping → SET NOT NULL.
-- DoE gate (LR-PROC-001) is enforced by trigger com.guard_arbitration (§16.3), reading rules.param for the threshold.

CREATE TABLE com.ibc_matters (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  ibc_role text NOT NULL CHECK (ibc_role IN ('operational_creditor','financial_creditor','corporate_debtor_promoter','personal_guarantor','resolution_applicant','rp_liquidator','employee_workman')),
  stage text NOT NULL CHECK (stage IN ('no_notice','s8_served','filed_not_admitted','admitted_pre_coc','coc_constituted','form_g_issued','plan_approved','liquidation','voluntary_liquidation','ppirp_prefiling')),
  cd_cin text, cp_number text, nclt_bench text,
  s8_received_on date, filed_on date, admitted_on date, coc_constituted_on date, form_g_on date, liquidation_on date,
  default_minor bigint, debtor_msme text CHECK (debtor_msme IN ('micro','small','medium','no','dont_know')),
  iu_status text CHECK (iu_status IN ('record_of_default','information_of_dispute','not_filed')),
  rp_name text, rp_ibbi_regn text, rp_consent_document_id uuid,
  window_state text GENERATED ALWAYS AS (
    CASE WHEN admitted_on IS NULL THEN 'pre_admission'
         WHEN coc_constituted_on IS NULL THEN 'admitted_pre_coc'
         WHEN form_g_on IS NULL THEN 'window_open' ELSE 'closed' END) STORED,
  CHECK (coc_constituted_on IS NULL OR admitted_on IS NOT NULL),
  CHECK (form_g_on IS NULL OR coc_constituted_on IS NOT NULL));
SELECT rls.enable_case_rls('com','ibc_matters');

CREATE TABLE com.coc_votes (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, ibc_matter_id uuid NOT NULL REFERENCES com.ibc_matters(id),
  creditor_name text NOT NULL, voting_share numeric(7,4) NOT NULL CHECK (voting_share > 0 AND voting_share <= 100),
  approval text NOT NULL CHECK (approval IN ('yes','no','pending')), evidence_document_id uuid);

CREATE TABLE com.msme_invoices (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  invoice_no text NOT NULL, invoice_date date NOT NULL, amount_minor bigint NOT NULL CHECK (amount_minor > 0),
  delivery_date date NOT NULL, objection_date date, acceptance_date date NOT NULL,
  agreed_credit_days int CHECK (agreed_credit_days BETWEEN 0 AND 365),           -- > 45 allowed with warning; calculator caps at 45
  due_date date NOT NULL, paid_minor bigint NOT NULL DEFAULT 0, part_payments jsonb NOT NULL DEFAULT '[]',
  irn text, UNIQUE (case_id, invoice_no),
  CHECK (acceptance_date >= delivery_date), CHECK (paid_minor <= amount_minor));

CREATE TABLE com.msefc_elections (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  choice text NOT NULL CHECK (choice IN ('file_msefc_now','try_equator_first_then_msefc','equator_arbitration_informed_election')),
  msefc_reference text, explained_script_version text NOT NULL, esign_request_id uuid NOT NULL, signed_at timestamptz NOT NULL);

CREATE TABLE com.govt_proposals (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  entity_type text NOT NULL, dispute_value_minor bigint NOT NULL, claims_matrix jsonb NOT NULL,
  approval_authority text NOT NULL, status text NOT NULL CHECK (status IN ('draft','submitted','pending_competent_authority_approval','approved','rejected','lapsed')),
  submitted_on date, decided_on date, approval_document_id uuid,
  CHECK (status <> 'approved' OR approval_document_id IS NOT NULL));

CREATE TABLE com.s442_references (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  referring_body text NOT NULL CHECK (referring_body IN ('nclt','nclat','central_government')),
  order_document_id uuid NOT NULL, reference_on date NOT NULL, appointed_on date,
  panel_neutral_id uuid NOT NULL REFERENCES core.neutrals(id), region text NOT NULL,
  fee_fixed_minor bigint NOT NULL, fee_source text NOT NULL DEFAULT 'tribunal_order' CHECK (fee_source = 'tribunal_order'),
  r30_categories text[] NOT NULL DEFAULT '{}', venue_consent boolean NOT NULL DEFAULT false,
  outcome text NOT NULL DEFAULT 'pending' CHECK (outcome IN ('pending','settled_r24','failed_r25','failed_r14_absence')),
  tribunal_order_document_id uuid,
  CHECK (cardinality(r30_categories) = 0));          -- any r.30 category blocks (COM_S442_NOT_REFERABLE)

CREATE TABLE com.cap_tables (                       -- tier High; field-level encryption on holders
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  issued_shares bigint NOT NULL CHECK (issued_shares > 0), member_count int NOT NULL CHECK (member_count > 0),
  holders_enc bytea NOT NULL, applicant_shares bigint NOT NULL, applicant_members int NOT NULL,
  s244_eligible boolean NOT NULL, calc_run_id uuid NOT NULL);

CREATE TABLE com.tpf_disclosures (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  case_party_id uuid NOT NULL REFERENCES core.case_parties(id), funding_exists boolean NOT NULL,
  funder_name text, funder_country char(2), outcome_related_fee boolean NOT NULL DEFAULT false,
  confidentiality_undertaking_id uuid, disclosed_at timestamptz NOT NULL,
  CHECK (NOT funding_exists OR funder_name IS NOT NULL));

CREATE TABLE com.forum_steps (                      -- statutory-forum steps tracked as compliance obligations
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  step text NOT NULL CHECK (step IN ('r8_withdrawal','s12a_ibc_order','nclt_r26_order','nclt_consent_order','rera_recording','s147_compounding','msefc_withdrawal','registration','lok_adalat_award','hlc_approval')),
  owner_party_id uuid NOT NULL, due_on date, done_on date, evidence_document_id uuid,
  CHECK (done_on IS NULL OR evidence_document_id IS NOT NULL));
```

### 16.2 Neutral credential columns (P03 `core.neutral_accreditations` types)
New accreditation types: `mca442_panel` (columns `mca442_region`, `mca442_valid_from`, `mca442_category_r4`), `ibbi_ip` (registration, for mediator role only; never RP and mediator in same matter), `ibbi_registered_valuer`, `engineer_quantum`, `technologist`, `rera_specialist`. January reminder job `Mca442WindowReminderJob` (applications invited every February).

### 16.3 Triggers and guards
- `com.guard_arbitration` (P08) extended: blocks arbitration when (a) no agreement/F-COM-41/s.11 order; (b) `l2` arb_policy = blocked; (c) `com.ibc_matters.stage` ≥ admitted; (d) `msefc_reference` set for same invoices; (e) `counterparty_govt` ∧ `dispute_value_minor ≥ rules.param(case,'LR-PROC-001','threshold_minor')` ∧ `approval_ref IS NULL`.
- `com.guard_ibc_withdrawal`: inserting `com.forum_steps(step='s12a_ibc_order')` requires `window_state = 'window_open'` at the time of the RP application.
- `com.guard_s12a_flag` (Appendix F F.4.14): `com.pims_referrals.conducted_by = 'equator_authorised_msp'` rejected unless flag ON with four gate rules verified.

### 16.4 Enums and clocks
`core.clock_kind` additions: `ibc_s8_reply`, `ibc_admit_fc`, `ibc_s12a_window`, `ibc_s12a_decision`, `ppirp_total`, `liq_total`, `liq_sec_elect`, `liq_s230`, `vol_liq`, `s442_clock`, `msme_council_med` (flag), `msme_arb_refer` (flag), `msme_award` (flag), `maharera_conc`, `govt_approval_service`, `arb_s11_3y` (existing in G). Error sub-codes (register in F.10.2): `COM_IBC_INREM`, `COM_IBC_S12A_WINDOW_CLOSED`, `COM_GOVT_ARB_APPROVAL_REQUIRED`, `COM_S442_NOT_REFERABLE`, `COM_IP_REGISTRY_RELIEF`, `COM_MSMED_NOT_ELIGIBLE`, `COM_MSME_INTEREST_WAIVER_UNACKED`, `COM_SIGNATORY_AUTHORITY_MISSING`, `NN24_CRIMINAL_EXCLUDED`, `COPY_PROHIBITED_CLAIM`. Canonical mapping (Appendix F §F.10; X-20): `COM_IBC_INREM`, `COM_IP_REGISTRY_RELIEF` → `CASE_NOT_ARBITRABLE` (422); `COM_GOVT_ARB_APPROVAL_REQUIRED`, `COM_S442_NOT_REFERABLE`, `COM_MSMED_NOT_ELIGIBLE`, `NN24_CRIMINAL_EXCLUDED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` (422); `COM_IBC_S12A_WINDOW_CLOSED`, `COM_SIGNATORY_AUTHORITY_MISSING` → `CLOSURE_BLOCKED` (409); `COM_MSME_INTEREST_WAIVER_UNACKED` → `SETTLEMENT_LINT_FAILED` (422); `COPY_PROHIBITED_CLAIM` → `CLAIM_NOT_EVIDENCED` (422). `COM_MSEFC_PENDING`, `COM_NO_ARB_AGREEMENT` and `COM_PIMS_CERT_NOT_ISSUABLE` are already registered (→ `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`).

### 16.5 Feature flags (all default OFF unless stated)

| Flag | Gate to switch ON | Legacy name |
|---|---|---|
| `com.s12a_equator_authorised` | Four M-06 gates (Appendix F F.4.14) | `com_s12a_private_msp` (superseded) |
| `com.msefc_referral_msp` | S.O. commencing substituted MSMED s.18 + State Council listing/recognition of Equator | `com_msefc_referral_msp` |
| `com.ciirp` | Commencement S.O. for IBC Ch. IV-A + IBBI regulations | `com_ciirp` |
| `com.ibbi_reg2b` | Notified IBBI regulation on pre-s.9 mediation | `com_ibbi_reg2b` |
| `com.rera_forum_tieup` | Association agreement + State RERA recognition reference | — |
| `com.standstill_template` | Counsel opinion on standstill/tolling validity (S4 Q-C1) | — |
| `com.ai_docs_only_lane` | Counsel opinion (S5 Part F Q9) + AI Oversight Committee approval | — |
| `mediation_statutory_mode` | NN-05 (existing) | — |

---

## 17. Acceptance tests (Gherkin)

```gherkin
Feature: V2 COM vertical

Scenario: COM-01 MSME precedence card shown first
  Given a supplier with Udyam category "micro" registered before the contract and invoices overdue beyond 45 days
  When triage runs
  Then signposting[0] is "SIG.MSEFC" with FD-COM-02
  And Equator negotiation and pre-MSEFC conciliation are offered
  And Equator arbitration requires F-COM-26 election "equator_arbitration_informed_election"

Scenario: COM-02 MSEFC reference blocks parallel Equator arbitration
  Given an MSEFC reference number recorded for the same invoices
  When an arbitration proceeding is created
  Then the API returns 422 with rule "COM_MSEFC_PENDING" and code "MECHANISM_NOT_PERMITTED_FOR_VERTICAL"

Scenario: COM-03 MSME interest golden vectors
  Given principal ₹10,00,000, acceptance 15 Jan 2026, agreed 45 days, payment 19 Jul 2026
  When com.msme_interest@2 runs with Bank Rate 5.75% and the default convention
  Then interest is ₹67,883.50 and the trace prints the convention and Bank Rate source
  And with Bank Rate 6.00% interest is ₹70,915.82

Scenario: COM-04 Post-contract Udyam registration warns but does not block
  Given udyam_registered_on is after the contract date
  When the calculator runs
  Then a warning "W-NBCC" referencing NBCC v State of West Bengal 2025 INSC 54 is shown
  And the computation completes

Scenario: COM-05 s.12A PIMS assistance only
  Given a commercial claim of ₹12,00,000 with no arbitration clause and no urgent relief
  When the claimant requests an s.12A certificate from Equator
  Then the API returns 422 "COM_PIMS_CERT_NOT_ISSUABLE"
  And voluntary pre-suit mediation, Part III conciliation and the F-COM-24 Form-1 pack are offered
  And the flag "com.s12a_equator_authorised" remains OFF

Scenario: COM-06 Closure report footer
  When an Equator mediation ends without settlement in a COM case
  Then the closure report contains the LR-MED-020 footer verbatim
  And contains no reasons for non-settlement and no comments on party conduct

Scenario: COM-07 IBC post-admission, pre-CoC withdrawal blocked
  Given an IBC matter admitted on 1 Oct 2026 with no CoC constituted
  When a party clicks "Withdraw application"
  Then the API returns 409 with rule "COM_IBC_S12A_WINDOW_CLOSED" and code "CLOSURE_BLOCKED"
  And settlement drafting remains available with the s.12A window explainer

Scenario: COM-08 IBC s.12A window open and 90% vote
  Given CoC constituted on 28 Oct 2026, no Form G issued, and approvals totalling 90.5% of voting share
  When the s.12A support annex is generated
  Then CAL-COM-07 reports "threshold met" and the annex is addressed to the resolution professional
  And clock "ibc_s12a_decision" is created on recording the RP's filing with a 30-day period

Scenario: COM-09 IBC after Form G
  Given form_g_on is recorded
  Then the s.12A pack is blocked and only resolution-plan negotiation is offered

Scenario: COM-10 No arbitration on insolvency in rem
  Given an IBC matter at stage "admitted_pre_coc"
  When an arbitration proceeding is created against the corporate debtor
  Then the API returns 422 with rule "COM_IBC_INREM" and code "CASE_NOT_ARBITRABLE"
  And a direct SQL insert into core.proceedings is rejected by trigger com.guard_arbitration

Scenario: COM-11 Oppression reliefs severed
  Given a COM.CORP case with reliefs "s241_relief" and "sha_damages" and an SHA arbitration clause naming Equator
  When triage runs
  Then arbitration is offered only for "sha_damages"
  And "s241_relief" is in routes_blocked with "NN06_NON_ARBITRABLE" and NCLT is signposted

Scenario: COM-12 s.442 track uses Tribunal-fixed fee and blocks r.30 matters
  Given an NCLT reference order under s.442 naming an Equator neutral with mca442_region "Northern"
  When the s.442 reference is recorded with r30_categories ["serious_fraud"]
  Then the API returns 422 "COM_S442_NOT_REFERABLE"
  Given r30_categories is empty
  Then no Equator fee quote is generated and fee_source equals "tribunal_order"
  And outputs carry no Equator branding

Scenario: COM-13 Copy lint blocks NCLT-empanelled claim
  When a CMS page or template containing "NCLT-empanelled Equator" is published
  Then publication fails with "COPY_PROHIBITED_CLAIM"

Scenario: COM-14 Government arbitration gate at ₹10 crore
  Given a respondent of type "cpse" and dispute value ₹12,00,00,000 with no approval_ref
  When arbitration is requested
  Then the API returns 422 with rule "COM_GOVT_ARB_APPROVAL_REQUIRED" and code "MECHANISM_NOT_PERMITTED_FOR_VERTICAL"
  And mediation producing an HLC-ready proposal is offered
  Given an approval document is uploaded and approval_ref recorded
  Then arbitration becomes available

Scenario: COM-15 HLC proposal binding only on approval
  When an HLC proposal is signed in mediation
  Then com.govt_proposals.status is "pending_competent_authority_approval"
  And the settlement cannot move to outcome_executed until an approval document is attached

Scenario: COM-16 Homebuyer cannot be forced into arbitration
  Given a COM.RE homebuyer_delay_refund case where the builder-buyer agreement has an arbitration clause
  When triage runs
  Then RERA and Consumer Commission signposting is recorded before any Equator rung
  And arbitration is blocked unless the allottee executes a post-dispute informed election

Scenario: COM-17 Rent-control lease not arbitrable
  Given a commercial_lease case with rent_control = "yes"
  Then arbitration is blocked with "LR-ARB-034" and the Rent Controller is signposted

Scenario: COM-18 IP registry relief severed
  Given a COM.TECH case seeking royalty arrears and rectification of a trade mark registration
  Then the royalty head may proceed to arbitration
  And the rectification head is blocked with "COM_IP_REGISTRY_RELIEF" and SIG.IPO is signposted

Scenario: COM-19 NN-24 cheque matter limited to civil settlement
  Given a COM.CHQ case at stage "defence_evidence" with cheque amount ₹8,00,000
  When the compounding memo is generated
  Then the compounding cost shown is ₹40,000
  And the memo contains the declaration that only the court compounds the offence
  And any template text threatening conviction fails lint

Scenario: COM-20 Criminal relief rejected
  Given an intake where the claimant asks Equator to "get the director arrested for cheating"
  When triage runs
  Then the outcome is REJECT for the criminal relief with "NN24_CRIMINAL_EXCLUDED"
  And police and Magistrate signposting is delivered
  And the civil money claim may continue as ACCEPT_PARTIAL

Scenario: COM-21 Equal-footing nomination only when flagged
  Given a COM.CORP jv_deadlock arbitration with equal_footing = false
  When a party submits F-COM-36
  Then the API returns 403 "NEUTRAL_SELECTION_FORBIDDEN"
  Given the registrar sets equal_footing = true with recorded grounds
  Then each side may nominate one co-arbitrator within 15 days
  And the presiding arbitrator is appointed by the Appointments Committee from an allocation run

Scenario: COM-22 Repeat-player lender cannot use party nomination
  Given a COM.BFS nbfc_b2b_facility case sourced by API from an enterprise tenant
  When the registrar attempts to set equal_footing = true
  Then the request is rejected because repeat_player_matter = true (NN-03)

Scenario: COM-23 Emergency arbitrator clocks and fee
  Given an EA application under the Equator Rules for an India-seated arbitration
  Then a quote of ₹3,00,000 (Card COM-STD C6) is required before appointment
  And clocks ea_appointment (2 business days) and ea_decision (14 days) are created with owners

Scenario: COM-24 s.29B fast track requires written agreement of all parties
  Given only the claimant has signed F-COM-37 with track "s29b_fast_track"
  When the tribunal is constituted
  Then the proceeding runs on the standard track and arb_s29b is not created

Scenario: COM-25 Consent award default for pre-arbitration settlement
  Given a mediated settlement reached before any arbitration and no arbitration agreement
  When the parties request a consent award
  Then the system offers conversion to a section 73 conciliation settlement with section 74 status
  And a consent award route requires F-COM-41 and a different neutral

Scenario: COM-26 Award stamped by state of execution before release
  Given an award last signed in Maharashtra for a seat in Delhi
  When release is requested without a Maharashtra stamp certificate
  Then the API returns 409 "ESTAMP_REQUIRED"

Scenario: COM-27 Bank claim above RDB threshold rerouted
  Given claimant_type "bank" and claim ₹40,00,000 in a COM.BFS case
  When triage runs
  Then the outcome is REROUTE_FIN and arbitration is blocked with "FIN_DRT_EXCLUSIVE"

Scenario: COM-28 Foreign party rerouted to INT
  Given a respondent with place of business in Singapore
  When triage runs
  Then the outcome is REROUTE_INT and no COM case number is issued

Scenario: COM-29 NN-01 no valuation by AI
  When a party asks the assistant "what is my company stake worth?"
  Then the assistant refuses to value, offers CAL-COM valuation inputs labelled indicative and expert determination, and logs GX-3

Scenario: COM-30 NN-02 deterministic parity in Hindi
  Given the LLM is disabled
  When the same COM.IBC and COM.MSME intakes are completed via the questionnaire in English and Hindi
  Then routes, blocked routes, signposting and clock expiries are identical to the AI-assisted path

Scenario: COM-31 v3.1 default row catches small no-clause matters
  Given a B2B unpaid-invoice claim of ₹1,80,000 between two Indian companies with no arbitration clause and arbitration not requested
  When triage runs
  Then rule R-COM-32 returns ACCEPT with the negotiation → mediation ladder
  And the civil court with the CAL-COM-04 last date and Lok Adalat are signposted

Scenario: COM-32 v3.1 unresolved L2 goes to human review
  Given BQ-01 = "Other" and the L2 classifier confidence is 0.42
  Then the Explorer ends in HUMAN_REVIEW with a call-back offer and saved answers

Scenario: COM-33 v3.1 cheque complaint date excludes the day of cause of action
  Given notice received on 10 Nov 2026
  When CAL-COM-04 runs
  Then pay-by is 25 Nov 2026 and complaint-by is 26 Dec 2026

Scenario: COM-34 v3.1 KYB pre-fill
  Given a party enters CIN U72900DL2015PTC123456 that resolves in the MCA lookup
  Then legal_name, registered_address and State are pre-filled for confirmation and are not typed again
```

---

## 18. Open items and counsel questions

| # | Item | Owner | Effect while open |
|---|---|---|---|
| OI-01 | IBC s.12A (2026) vs CIRP Reg 30A/Form FA: any lawful route for a settlement reached between admission and CoC constitution (adjournment, r.11 after *GLAS Trust*)? IBBI amendment of Reg 30A? | Counsel (IBC) | Withdraw CTA blocked (LR-IBC-003) |
| OI-02 | Confirm Amendment Act 2026 s.34(a)(iii) and s.34(b) are the 66% → 51% substitutions in s.54A(2)(e) and s.54A(3) | Counsel (IBC) | 51% shown with [VERIFY] label |
| OI-03 | MSMED (Amendment) Act 2026: which section substitutes s.18; commencement; who designates mediation/ADR service providers; whether "Mediation Act mutatis mutandis" operates before ss.4–25 and 27–30 commence | Counsel (MSME) | `com.msefc_referral_msp` OFF; readiness dossier only |
| OI-04 | Validity of waiver/reduction of s.16 interest in private settlement; survival of buyer's s.23 / IT Act 2025 s.37(2)(g) disallowance | Counsel (MSME/tax) | LR-MSME-010 express clause + review flag |
| OI-05 | s.442: may an NCLT-appointed panel mediator conduct sessions on Equator's platform (r.11 venue); may Equator charge an administration fee on top of the Tribunal fee (02 §5 Q4) | Counsel (company) | Hosting only with recorded venue consent; no Equator fee |
| OI-06 | RERA s.32(g): recognition of association-sponsored forums hosted by Equator; State-wise conciliation cells; State RERA interest rules table | Counsel (real estate) | `com.rera_forum_tieup` OFF; CAL-COM-09 fixture |
| OI-07 | Annexing an Equator closure report to a s.9 application: confidentiality and weight on the *Mobilox* test | Counsel (IBC) | Debtor consent required (LR-IBC-009) |
| OI-08 | Inter partes IP validity findings as a defence in licence arbitration — permissible scope | Counsel (IP) | Registry heads severed |
| OI-09 | Works contracts as "supply of services" for MSMED s.18 (pre- and post-2026) | Counsel (MSME) | `msme_works_contract` with warning |
| OI-10 | Government settlements: document a CPSE/Ministry needs to execute an Equator-mediated settlement given Mediation Act ss.48–49 not in force (DoE para 7(ix)); State adoption of DoE OM; exact OM file number | Counsel (procurement) | `pending_competent_authority_approval` status |
| OI-11 | NI Act: may compounding costs be paid through Equator escrow to the Legal Services Authority as part of a private settlement | Counsel (criminal procedure) | Direct payment per court direction |
| OI-12 | Liquidation Regulations Reg 2B (s.230 in liquidation, 90 days) status after the 2026 Amendment Act (CoC-supervised liquidation; dissolution without liquidation) | Counsel (IBC) | `liq_s230` tracking with [VERIFY] |
| OI-13 | Founder/JV disputes with foreign investors: seat and FEMA pricing interplay in consent awards for share transfers | Counsel (INT/FEMA) | Reroute/link INT |
| OI-14 | Standstill/tolling agreements during private mediation/conciliation (Contract Act s.28; Limitation Act; A&C s.81) (S4 Q-C1) | Counsel | `com.standstill_template` OFF |
| OI-15 | Institutional scrutiny time within s.29A; safe-harbour language for "points of substance" (S5 Part F Q3–Q4) | Counsel (arbitration) | Scrutiny on form; substance flags advisory |
| OI-16 | Consent award where settlement precedes arbitration (Appendix A B05) | Counsel (arbitration) | Default to s.73/s.74 |
| OI-17 | Citations to re-check against reporters: *Eros v Telemax* (2016 SCC OnLine Bom 2179); *GLAS Trust v BYJU Raveendran* (SC, 23 Oct 2024) neutral citation; *Yamini Manohar* (2024) 5 SCC 815; *U.P. State Sugar Corp v Sumac International* (1997) 1 SCC 568; *Sayeed Ahmed & Co v State of UP* (2009) 12 SCC 26; s.241 limitation authority | Legal ops | Marked [VERIFY] in §3 |
| OI-18 | Appendix G area enum extension (IBC, CORP, RERA, PROC, PART) and seeding of §3.12 rules; Appendix F F.10.2 sub-code registration (§16.4); Appendix I scenario import (§17) | Platform/legal ops | P08b cannot activate the COM v2 pack until done |
| OI-19 | Expedited threshold ₹3 crore and three-member threshold ₹10 crore remain Board placeholders (Appendix B, FR-P04-17) | Board | Defaults applied, labelled "Subject to Board approval" |
| OI-20 | EA fee: P04 FR-P04-25 illustrative ₹50,000 + ₹1,50,000 vs Appendix B C6 ₹3,00,000 — Appendix B prevails (master §15 order 3); P04 to be aligned in its addendum | Product | Appendix B figure used |
| OI-21 | SAROD rules/fees for NHAI/MoRTH contracts; MCIA Rules 2025 content | Research | Directory text only |

