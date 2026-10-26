# Appendix Q — Privacy, Security and Certification Readiness

> **Binding reference** for NN-30 (one privacy control set) and NN-31 (card data never touches Equator), and for P14 (hardening, compliance, go-live), P00 (platform controls, compliance-as-code), P05 (payments boundary), P01 (consent, notices, rights centre), P11 (AI records) and P13 (cookie consent). Read with the master prompt (NN-07, NN-13, NN-14, NN-15, NN-16, NN-17, NN-22, NN-30, NN-31, §4.1, §11), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-15, R-19; D2-21, D2-22; A-05), Appendix F (names, types, events, errors — F prevails on names), Appendix G (legal rules — G prevails on law), P14, P01 FR-P01-35 to FR-P01-41, P11 FR-P11-13/FR-P11-45. Version 2.0, 21 October 2026. Operator: Equator Resolution Service Private Limited.

**Tags.** **[K]** settled law or well-known standard text; **[V]** verified in research streams S8 / RES_A4 / GLOBAL_CORRECTIONS (20–21 Oct 2026); `[VERIFY — open: …]` (legend) must be closed by counsel, the vendor or the certification body before the dependent flag, claim or contract term goes live. Indicative costs are planning numbers only and are always **[VERIFY — quotes]**.

---

## 0. Scope, precedence and reconciliations

*(v3.2, 26 October 2026)* **IPB-02 pointer.** The Infrabyx Platform Baseline Standard IPB-02 (Security Baseline and Certification Map) is the group control library mapped to CERT-In, ISO/IEC 27001/27701/42001/22301, SOC 2, PCI DSS v4.0.1 SAQ A, DPDP Act and Rules, RBI outsourcing and IT directions, SEBI CSCRF and OWASP ASVS 5.0 / LLM / Agentic. This appendix is Equator's binding of it: §3.2 controls are indexed by IPB-02 control ID in `docs/compliance/ipb02-map.md` (P00 FR-P00-V32-09; P14 FR-P14-V32-04), each row marked `mapped`, `stricter` or `gap`. Equator is stricter than IPB-02 on sealed stores (NN-07), mediation recording (NN-11), the hash-chained audit (NN-22), in-country AI inference for all case content (FR-P11-07) and card data (NN-31); these appear in the IPB-02 "cannot be demolished" check as L-tier settings. The Vendor Assurance Room (IPB-08) is the publication channel for the evidence this appendix names: §2.7 sub-processors, §3.3 continuity, §4 SAQ A attestation, VAPT summaries and the ISO and SOC 2 readiness status render on `/trust` only from the room (P14 FR-P14-V32-01…03). AI security tests from IPB-02 (LLM Top 10, Agentic Top 10) run against the Vidhi surfaces (P22).

This appendix (a) decides which privacy and security laws reach Equator and when, (b) turns them into one control library (`PC-01`…`PC-40`) that the product implements once, (c) fixes the security architecture baseline, (d) fences the PCI DSS boundary, and (e) sets the certification roadmap and the evidence machinery. It extends P14 FR-P14-07 to FR-P14-09 and FR-P14-20/21; it does not repeat them. S8 §5.3 "UCS-01…UCS-20" are absorbed into `PC-xx` (crosswalk column in §2.2).

| # | Conflict found | Resolution applied |
|---|---|---|
| Q-R1 | Brief asks for PCI DSS 6.4.3 and 11.6.1 "for the payment page". The SAQ A revision of January 2025 removed 6.4.3, 11.6.1 and 12.3.1 from SAQ A and added an eligibility criterion that the merchant confirms its site "is not susceptible to attacks from scripts that could affect the merchant's e-commerce system(s)" [V S8 §6.1]. | **Decision Q-D1:** Equator files SAQ A, and **implements 6.4.3-equivalent script management and 11.6.1-equivalent tamper detection anyway** on every payment-initiating page, as the evidence that substantiates the eligibility criterion (§4.4). They are internal controls `PC-SEC-PAY-02/03`, not SAQ A line items. **[VERIFY — open (vendor): PCI SSC blog 30 Jan 2025 leaves substantiation to the acquirer — obtain acquirer's written evidence expectation and Razorpay's AoC + responsibility matrix]** |
| Q-R2 | LR-DPDP-001 (Appendix G) records G.S.R. 843(E) as bringing "ss.38–44" into force on 13 Nov 2025. S8 §5.1 treats IT Act s.43A as alive until DPDP s.44(2) (which omits s.43A) commences on 13 May 2027. If all of s.44 commenced in Nov 2025, s.43A and the SPDI Rules would already be gone. | Build to both: SPDI controls stay in the library (they are a subset of DPDP controls). Legal status of LR-ITA-001 is `IN_FORCE` until 13 May 2027 (s.43A omitted by DPDP s.44(2) from that date). [Verified 22 Oct 2026: G.S.R. 843(E), 13 Nov 2025, cl.(a) commences s.44(1) and (3) only; cl.(c) commences s.44(2) eighteen months after publication — MeitY Gazette copy] |
| Q-R3 | Master §11 sets DR RTO ≤ 2 h; S8 §6.4 recommends RTO ≤ 4 h. | Master prevails: RPO ≤ 15 min, RTO ≤ 2 h. |
| Q-R4 | Master §11 default retention "case records 8 years after closure"; S8 UCS-14 says awards need ≥ 12 years (Limitation Act 1963 Sch. Art. 136: 12 years to execute a decree; s.36 A&C Act enforces an award as a decree). | New retention class `outcome_instrument` (awards, consent awards, s.74 settlements, MSAs, execution packs, their evidence-ledger rows): **13 years from the instrument date or 1 year after execution is complete, whichever is later**. The 8-year default stays for the rest of the case file. Additive to F.3 `retention_class` (ADR). |
| Q-R5 | `core.dsr_requests.kind` (Appendix F) covers DPDP rights only; GDPR, CCPA, PDPA and PDPL add restriction, portability, objection, automated-decision review, opt-out of sale/share and limit-use rights. | Additive CHECK change (ADR) in §2.4: `kind` gains `restriction`, `portability`, `objection`, `adm_review`, `opt_out_sale_share`, `limit_spi`, `know`; new column `law_code`. |
| Q-R6 | `eng.regulatory_notifications.regulator` (P14 §7.2) lacks foreign authorities. | Additive CHECK values: `eu_sa`, `uk_ico`, `sg_pdpc`, `uae_data_office`, `difc_commissioner`, `adgm_odp`, `us_state_ag`, `regulated_tenant`. |
| Q-R7 | P13 FR-P13-23 loads GA4 (Google, outside India) for acquisition. | GA4 stays consent-gated (`analytics` category, opt-in everywhere), advertising features and Google Signals OFF, IP truncation ON, never on `/pay/*` or case routes, and recorded as a transfer in the transfer register (§2.6). If CCPA mode is ever ON, GPC disables it (§2.9). |
| Q-R8 | NN-32 (originals preserved) vs NN-31 (no card data stored) when a party uploads an image of a payment card or an unmasked statement. | **Decision Q-D2:** PAN detection runs in the quarantine bucket before evidence ingest (new step 2a of P00 FR-P00-21, inserted by FR-P00-V2-Q4 after the ClamAV scan). A file with a Luhn-valid full PAN never becomes an "original": the uploader gets a server-made masked copy to approve as their submission; the unmasked file is destroyed by the 24-hour quarantine lifecycle and the event is logged without the PAN (§4.6). |
| Q-R9 (v3.0, 23 Oct 2026) | v3 assigns schema `ops` to the business Operations Platform (Appendix X D3-20). | The v2.1 security, privacy and compliance-operations tables this appendix places in `ops` (§2, §7.2; P14 §7.2) move to schema `eng` with unchanged names; `ops.security_findings` becomes `eng.vulnerabilities`; read-only compatibility views `ops.<name>` exist in the core database for v3.0 only (master X-50, X-65; Appendix AE). SC-11 patch SLAs are locked ceilings under tighter v3 defaults (X-66(a)). *v3.1:* all table and event names in this appendix are now written in `eng` (`equator.eng.*` events), so the compatibility views are needed only for code written against v2.1. |

---

## 1. Applicability matrix — who, when, what triggers

### 1.1 Equator's roles

| Product line / context | DPDP role | GDPR/UK GDPR role (when it applies) | CCPA role | Notes |
|---|---|---|---|---|
| L1 Equator Institution cases (all six verticals), website, Explorer, accounts | **Data Fiduciary** | Controller | Business (only if thresholds met) | Respondent data before engagement under DPDP **s.17(1)(a)** (enforcing a legal right or claim); awards/orders enforcement **s.7(e)** [V GLOBAL_CORRECTIONS §13] |
| L2 Private ADR Chambers tenants | **Data Processor** for the chambers tenant (fiduciary) | Processor | Service provider | DPA + sub-processor list per tenant (P10 §fiduciary roles) |
| L3 Enterprise API/bulk (lender, insurer, employer as party) | Fiduciary for case administration; enterprise is an independent fiduciary for its own data | Controller | Business | The lender's loan data reaches Equator under the lender's own basis; Equator records receipt basis per case |
| L4 GRM SaaS, L5 POSH IC SaaS | **Processor** for the tenant | Processor | Service provider | POSH Act s.16 confidentiality flows down by contract [V S8 §8 Q10 — counsel confirm] |
| L6 Academy (separate entity Equator ADR Institute) | Institute is its own fiduciary | — | — | Equator receives Academy data only on learner consent (P10) |
| Account Aggregator evidence (D6) | Equator is not an FIU; data comes via the lender tenant (NN-14) | — | — | Derived summaries only |

### 1.2 Law-by-law applicability (status as of 21 Oct 2026)

| Law / instrument | Trigger for Equator | Applies? | Key dates | What it requires of the product (headline) | Legal rule IDs |
|---|---|---|---|---|---|
| **Digital Personal Data Protection Act 2023** (No. 22 of 2023) + **DPDP Rules 2025** (G.S.R. 846(E), 13 Nov 2025; corrigendum G.S.R. 892(E), 10 Dec 2025) | Digital personal data processed in India; and outside India if offering goods/services to Data Principals in India (s.3(b)) | **Yes** (fiduciary and processor) | Rules 1, 2, 17–21 in force 13 Nov 2025; **Rule 4 (Consent Managers) and Act s.6(9), s.27(1)(d) from 13 Nov 2026**; **Rules 3, 5–16, 22, 23 and the core Act obligations from 13 May 2027** [V RES_A4 Q01] | Itemised stand-alone notice (s.5, r.3); consent or listed basis (ss.4, 6, 7, 17); withdrawal as easy as giving (s.6(4)); security safeguards incl. logs ≥ 1 year (s.8(5), r.6(1)(e), r.8(3)); breach intimation to principals and Board without delay + detailed report ≤ 72 h (s.8(6), r.7); erasure (s.8(7), r.8); contact publication (s.8(9), r.9); grievance ≤ 90 days (s.8(10), s.13, r.14(3)); children/PwD (s.9, r.10–11); transfers (s.16, r.15). Penalties up to ₹250 crore per instance (s.33, Schedule) [K] | LR-DPDP-001 to -013 |
| DPDP **Significant Data Fiduciary** (s.10; r.13) | Only if notified by the Central Government by class/volume/sensitivity | Not notified | — | Equator designs as if SDF (annual DPIA, independent audit, algorithmic due diligence) — P14 FR-P14-08(2) | LR-DPDP-014 (new) |
| **IT Act 2000 s.43A** + **IT (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules 2011** (G.S.R. 313(E), 11 Apr 2011) | Body corporate possessing/handling SPDI (passwords, financial information, health, sexual orientation, medical records, biometrics — r.3) | **Yes**, until s.43A is omitted by DPDP s.44(2) (see Q-R2) | Now | Privacy policy on website (r.4); written consent for SPDI collection, purpose limitation, grievance officer resolving within one month (r.5, r.5(9)); disclosure only with prior permission (r.6); transfer only to equal-protection recipients (r.7); reasonable security practices — IS/ISO/IEC 27001 deemed compliant, audited at least annually (r.8) [K] | LR-ITA-001 (new) |
| **IT Act 2000 s.72A** | Disclosure of personal information obtained under a lawful contract, without consent, with intent/knowledge of wrongful loss or gain | **Yes** (survives DPDP) | Now | Up to 3 years' imprisonment and/or fine up to ₹5 lakh → NDAs, need-to-know, disclosure register (PC-20, PC-37) [K] | LR-ITA-002 (new) |
| **CERT-In Directions** No. 20(3)/2022-CERT-In, 28 Apr 2022 (IT Act s.70B(6)); FAQs 19 May 2022 | Service provider/body corporate | **Yes** | In force since ~27 Jun 2022; no amendment through Oct 2026 [V RES_A4 Q12] | Report Annexure I incidents (20 types incl. cloud (xviii), AI/ML (xx)) within **6 hours** of noticing; ICT logs **180 days rolling in India**; NTP to NIC/NPL (or traceable cloud source); PoC registration; respond to directions | LR-CERTIN-001 to -004 (new) |
| **EU GDPR** (Reg. (EU) 2016/679) | **Art. 3(2)(a)**: Equator (no EU establishment) offers services to data subjects in the EU — EUR pricing, EU-language pages, INT matters marketed to EU parties. Art. 3(2)(b) monitoring: not applicable if no behavioural tracking of EU visitors | **Conditional — "yes" from the first INT matter actively offered to an EU party** (A-05: not marketed to EU consumers at launch) | Now | Art. 6 basis + Art. 9(2)(f) legal claims; Art. 10 criminal-offence data minimised to the existence, reference and status of related proceedings needed for the civil dispute (NN-24; e.g., NI Act s.138) **[VERIFY — open (counsel): Art. 10 requires official-authority control or Union/Member State law authorisation — map the authorising national law per Member State of the EU party]**; Arts 12–22 rights (1 month); **Art. 22** no solely automated decision with legal effect (NN-01 ensures human decision); **Art. 27 EU representative** unless processing is occasional and excludes large-scale Art. 9/10 data; **Art. 28** processor terms; **Art. 30** RoPA; **Art. 33** 72 h to the SA / **Art. 34** individuals; **Art. 35** DPIA; **Arts 44–49** transfers (SCCs, Commission Implementing Decision (EU) 2021/914; Art. 49(1)(e) legal-claims derogation) [K] | LR-GDPR-001 to -008 (new) |
| **UK GDPR + Data Protection Act 2018**, as amended by the **Data (Use and Access) Act 2025** | UK targeting (Art. 3(2) UK GDPR) | Conditional (as EU) | DUAA 2025 changes commence in stages (ss.70, 80, 112 and Sch 7 in force 5 Feb 2026; s.103 complaints 19 Jun 2026 — SI 2026/82 regs 2, 3(a); ICO replaced by the Information Commission 30 Sep 2026, SI 2026/1015) [Verified 22 Oct 2026: legislation.gov.uk] | UK Art. 27 representative; transfers by **IDTA** or **UK Addendum** to EU SCCs (in force 21 Mar 2022); ICO 72 h breach reporting; DUAA complaints-handling duty on controllers (s.103, in force 19 Jun 2026 — SI 2026/82 reg 3(a)) [Verified 22 Oct 2026] | LR-GDPR-009 (new) |
| **ePrivacy Directive 2002/58/EC Art. 5(3)** / **UK PECR 2003 reg. 6** | Storing/reading non-essential cookies on devices of EU/UK visitors | Yes for EU/UK visitors to the public site | Now | Prior opt-in for non-essential cookies; "reject" as easy as "accept" (CMP — PC-33) [K] | LR-GDPR-010 (new) |
| **CCPA as amended by CPRA** (Cal. Civ. Code §1798.100 et seq.; CCPA Regulations, 11 CCR §7000 et seq.) | "Business": for-profit, does business in California, and one of: annual gross revenue > **US$26,625,000** (2025 CPI adjustment), buys/sells/shares PI of ≥ 100,000 consumers/households, or ≥ 50% revenue from selling/sharing PI [V S8 §5.1] | **No at launch (monitor annually)**; contractual service-provider terms may still flow down from California-based enterprise tenants | ADMT/risk-assessment/cyber-audit regulations approved by OAL **23 Sep 2025**, effective **1 Jan 2026**; ADMT compliance **1 Jan 2027**; risk-assessment attestations **1 Apr 2028**; cybersecurity-audit certifications 1 Apr 2028/2029/2030 by revenue band [V S8] | Notice at collection (§7012); rights to know/delete/correct (45 days, +45); opt-out of sale/share and **opt-out preference signals (GPC) honoured (§7025)**; limit use of sensitive PI (§1798.121); service-provider contract terms (§7051); ADMT pre-use notice and opt-out/appeal for significant decisions | LR-CCPA-001 to -004 (new) |
| **Singapore Personal Data Protection Act 2012** (as amended 2020) | Collection, use or disclosure of personal data in Singapore (Singapore parties/counsel in INT; SIAC/SIMC-adjacent matters) | **Yes for Singapore-connected INT matters** | Now | Consent/notification/purpose limitation; access & correction (respond within 30 days or notify of the time needed — PDP Regulations 2021); protection; retention limitation; **Transfer Limitation Obligation** (s.26; PDP Regulations 2021 Part 3); **breach notification to PDPC no later than 3 calendar days after assessing it notifiable** (s.26D; significant harm or ≥ 500 individuals); DPO (s.11(3)); penalty up to 10% of Singapore turnover (> S$10m) or S$1m [K] | LR-SGPDPA-001 to -003 (new) |
| **UAE Federal Decree-Law No. 45 of 2021** (PDPL); **DIFC Data Protection Law No. 5 of 2020**; **ADGM Data Protection Regulations 2021** | Processing personal data of data subjects in the UAE (onshore PDPL; PDPL excludes free zones with their own regimes); DIFC/ADGM-established parties under their own laws | **Yes for UAE-connected INT matters** (onshore subject to Executive Regulations) | PDPL Executive Regulations **[VERIFY — open (watch): not found as of 22 Oct 2026; PDPL itself in force 2 Jan 2022 per u.ae]** | Lawful basis incl. legal-claims exception; rights incl. objection to automated processing; breach notification to the UAE Data Office on becoming aware (Art. 9); DPO (Art. 10); cross-border Arts 22–23; DIFC: Commissioner notified as soon as practicable; ADGM: 72 h **[VERIFY — open: section number in DPR 2021 Part 5 not confirmed (22 Oct 2026); 72 h kept as conservative default]** | LR-UAEPDPL-001 to -003 (new) |
| **EU AI Act** (Reg. (EU) 2024/1689) as amended by **Reg. (EU) 2026/1744** (Digital Omnibus on AI) | Art. 2(1)(c): provider/deployer outside the EU where the AI output is used in the EU; **Annex III point 8(a)**: AI intended to assist a judicial authority in researching and interpreting facts and the law and applying the law, "or to be used in a similar way in alternative dispute resolution" → **high-risk** | **Conditional — INT matters with EU parties where AI assists the neutral** | Prohibited practices and AI literacy (Art. 4) from 2 Feb 2025; **Annex III high-risk obligations from 2 Dec 2027** [V GLOBAL_CORRECTIONS §12; LR-INT-020] | Default: AI on EU-party matters limited to clerical, translation and summarisation (LR-INT-020). If neutral-assist features are enabled for EU matters: Art. 6(3)/(4) documented non-high-risk assessment or full Arts 9–15, 26 compliance (risk management, data governance, logging, human oversight, accuracy) | LR-INT-020; LR-EUAI-001 (new) |
| India soft law: **MeitY India AI Governance Guidelines** (Nov 2025); **IT Rules 2021 amendment on synthetically generated information** (G.S.R. 120(E), 10 Feb 2026, in force 20 Feb 2026 — binding on intermediaries, not soft law) | AI-generated voice/text surfaces | Apply as policy | 20 Feb 2026 [V GLOBAL_CORRECTIONS §13] | Label synthetic voice/text (first-utterance AI disclosure already NN-12); provenance metadata on AI drafts **[VERIFY — open (counsel): whether Equator is an "intermediary" for party-uploaded content; its own AI output is first-party — duties applied as policy]** | LR-ITA-003 (new) |
| Sector flow-downs: RBI Master Direction on Outsourcing of IT Services (RBI/2023-24/102, 10 Apr 2023); RBI Cyber/IT framework of 31 Jul 2026 for REs (6-h reporting); IRDAI Information and Cyber Security Guidelines (2023 edition, 24 Apr 2023 [K]) **[VERIFY — open: confirm no later version; confirm RBI 31 Jul 2026 framework citation]** | Equator as service provider to regulated tenants | **Contractual** | Now | Audit rights, incident notice fast enough for the RE's 6-h report, India data storage, BCP, sub-contracting consent | (contract pack, P14 FR-P14-16(5)) |
| **PCI DSS v4.0.1** (June 2024) | Equator accepts card payments as a merchant through Razorpay/Cashfree/PayPal | **Yes — SAQ A only** (NN-31) | v4.0 retired 31 Dec 2024; future-dated requirements mandatory from 31 Mar 2025; SAQ A Jan 2025 revision [V S8 §6.1] | §4 | LR-PAY-007 (new) |
| **RBI card-on-file tokenisation** (RBI/2021-22/96, CO.DPSS.POLC.No.S-516/02-14-003/2021-22, 7 Sep 2021) with PA directions (now RBI (Regulation of Payment Aggregators) Directions 2025, RBI/DPSS/2025-26/141, 15 Sep 2025) | Merchant in the card transaction chain | **Yes** | Card data storage by merchants barred from **1 Oct 2022** [K] | Store only tokens created by the PA with customer consent + AFA, last four digits and issuer name; never actual card data [Corrected 22 Oct 2026: RBI/2021-22/96 per rbi.org.in; original deadline 1 Jan 2022, later extended to 30 Sep 2022 — extension citation open] | LR-PAY-005 (proposed in Appendix O) |

### 1.3 Jurisdiction resolver (feature `consent.jurisdiction_resolver`)

Each person and organisation carries `privacy_jurisdictions text[]` computed (never asked as a bare question) from: residence country and state (address, KYC country, phone country code as weak signal), establishment country (organisation KYB), the case's counterparties' locations, the marketing surface that acquired them (EU-language page, EUR price), and the tenant's governing contract. Output codes: `IN`, `EU`, `UK`, `US-CA`, `SG`, `AE`, `AE-DIFC`, `AE-ADGM`, `OTHER`. A person can hold several. The resolver is deterministic (packages/rules), versioned (NN-21) and returns: applicable law set, notice variant(s), lawful-basis map, DSR SLA, breach-clock set, transfer requirement and AI mode.

| Input signal | Weight | Example |
|---|---|---|
| Verified residential address country/state | decisive | Berlin address → `EU` |
| Organisation establishment (KYB) | decisive for org users | DIFC-registered company → `AE-DIFC` |
| Case marked `INT` with counterparty in EU/UK/SG/AE | adds that code to every party's case-level set for transfer analysis | Indian exporter v Singapore buyer → case-level `SG` |
| Acquisition surface (EUR price page, `de`/`fr` locale) | adds `EU` targeting flag at org level (Art. 3(2)(a) evidence) | — |
| Phone country code only | weak; never decisive alone | +971 → prompt to confirm residence |

Rule: if the resolver cannot decide, apply the strictest applicable set (`EU` ∪ `IN`) and raise task `PRIVACY_JURISDICTION_UNRESOLVED` (warning, not a block) to the DPO queue.

### 1.4 Proposed new Legal Rules Register rows (add to Appendix G in the P14 v2 slice; status set by the legal reviewer)

`LR-DPDP-014` SDF design-to standard · `LR-ITA-001` s.43A/SPDI r.4–r.8 · `LR-ITA-002` s.72A · `LR-ITA-003` synthetic-content labelling · `LR-CERTIN-001` 6-h reporting · `LR-CERTIN-002` 180-day India logs · `LR-CERTIN-003` NTP · `LR-CERTIN-004` PoC · `LR-GDPR-001` Art. 3(2) trigger · `-002` Art. 27 representative · `-003` Art. 9(2)(f)/Art. 10 · `-004` Art. 22 · `-005` Art. 28 · `-006` Art. 30 · `-007` Arts 33–34 · `-008` Arts 44–49 · `-009` UK GDPR/DUAA · `-010` ePrivacy/PECR cookies · `LR-CCPA-001` thresholds · `-002` GPC · `-003` SPI limit · `-004` ADMT · `LR-SGPDPA-001` TLO · `-002` 3-day breach · `-003` access 30 days · `LR-UAEPDPL-001` basis/rights · `-002` breach · `-003` transfers · `LR-EUAI-001` Annex III 8(a)/Art. 6(3) · `LR-PAY-007` SAQ A boundary · `LR-PAY-005` CoFT (row already proposed by Appendix O; LR-PAY-006 is O's prepaid-credits row). Every row starts `UNVERIFIED` until the legal reviewer signs; dependent flags default OFF (master §0) **except** controls that only make Equator stricter (those run regardless of status).

---

## 2. Unified privacy control set (NN-30)

### 2.1 Design rule

One control, implemented once, satisfies every law that asks for it. Each control has an ID (`PC-xx`), an owner role, a product feature, an automated test (`NN-30_PC-xx_*` where the control is NN-linked) and an evidence collector (§7). Where laws differ, the product applies the **strictest common rule** unless the difference is a matter of form (e.g., notice wording), which the jurisdiction resolver (§1.3) varies. Tenants may tighten but never loosen a control (master §6 guardrails → `RULESET_GUARDRAIL_VIOLATION`).

### 2.2 Control library — legal mapping

Abbreviations: Act = DPDP Act 2023; r. = DPDP Rules 2025; SPDI = SPDI Rules 2011; Art. = GDPR/UK GDPR; CCPA = Cal. Civ. Code / 11 CCR; PDPA = Singapore PDPA 2012; PDPL = UAE Decree-Law 45/2021. "—" = no equivalent obligation (control still applies by NN-30).

| ID | Control | DPDP | SPDI / IT Act / CERT-In | GDPR / UK GDPR | CCPA/CPRA | SG PDPA | UAE PDPL | Owner | S8 UCS |
|---|---|---|---|---|---|---|---|---|---|
| PC-01 | DPO and Grievance Officer appointed; business contact published on site and app and in every rights response | s.8(9), s.8(10); r.9 | SPDI r.5(9) | Arts 37–39 | Contact in privacy policy (§7011) | s.11(3)–(5) | Art. 10 | `dpo` | UCS-17 |
| PC-02 | Purpose register: every processing purpose coded, described, basis-mapped, retention-linked | s.5(1)(i), s.6(1) | SPDI r.5(3) | Art. 5(1)(b) | §1798.100(c) | s.18 | Art. 5 | `dpo` | UCS-01 |
| PC-03 | Records of processing (RoPA) per vertical × purpose × category × basis × recipient × transfer × retention | s.8(1) accountability; r.6 | SPDI r.4 | Art. 30 | §7012 notice data | Accountability (s.12) | Art. 7 records **[VERIFY]** | `dpo` | UCS-01 |
| PC-04 | Lawful-basis engine stored per purpose and per data element (consent / s.7 legitimate use / s.17(1)(a) legal claim / legal obligation / Art. 6(1)(b)(c)(f) / Art. 9(2)(f)) | ss.4, 6, 7, 17 | SPDI r.5(1) | Arts 6, 9, 10 | — | ss.13–17, First Sch. | Arts 4–5 | `dpo` | UCS-03 |
| PC-05 | Jurisdiction resolver (§1.3) on every person, organisation and case | s.3 | — | Art. 3(2) | §1798.140(d) | s.4 | Art. 2 | `dpo` + tech lead | — |
| PC-06 | Notices by jurisdiction and language: stand-alone, itemised, versioned, hashed (§2.3) | s.5; r.3; s.5(3) languages | SPDI r.4, r.5(3) | Arts 12–14 | §7010–7012 | s.20 | Art. 13 | `dpo`, `legal_reviewer` | UCS-02 |
| PC-07 | Consent ledger and receipts: append-only, per purpose, evidence hashed, receipt to principal | s.6 | SPDI r.5(1) | Art. 7(1) | §7004 (consent standard) | s.14 | Art. 6 | `dpo` | UCS-04 |
| PC-08 | Withdrawal propagation to all consumers and processors with SLA | s.6(4)–(6) | — | Art. 7(3) | §1798.120 | s.16 | Art. 6(3) **[VERIFY]** | `dpo` | UCS-04 |
| PC-09 | Consent-manager interoperability (`CONSENT_MANAGER_PORT`) | s.6(7)–(9); r.4 | — | — | — | — | — | tech lead | UCS-04 |
| PC-10 | Children and persons with disability: age gate, verifiable guardian consent, no tracking/profiling/targeting | s.9; r.10–12 | — | Art. 8 | §1798.120(c) (< 16 opt-in) | Advisory guidelines (children) **[VERIFY]** | — | `dpo`, `safeguarding_lead` | UCS-05 |
| PC-11 | Sensitive and sealed data: health, POSH, family safety, religion/community, biometrics, financial — sealed stores, separate consent, no AI training, no analytics (NN-07) | s.8(5) | SPDI r.3, r.5 | Arts 9, 10 | §1798.121 SPI | PDPC sensitive-data guidance | Sensitive data Art. 1 | `dpo`, `safeguarding_lead` | UCS-19 |
| PC-12 | Rights intake with identity verification proportionate to risk (aal2) and authorised-agent handling | s.13; r.14(1)–(2) | SPDI r.5(6) | Art. 12(6) | §7060–7063 | s.21 | Arts 13–19 | `dpo` | UCS-06 |
| PC-13 | Rights fulfilment with per-law SLA clocks (§2.4) and reasoned refusals | ss.11–13; r.14(3) | SPDI r.5(6), r.5(9) | Arts 12(3), 15–21 | §7021 (10 business days ack, 45 + 45 days) | s.21–22; PDP Regs 2021 | Arts 13–19 | `dpo` | UCS-06 |
| PC-14 | Nomination and deceased/incapacitated principal handling | s.14; r.14(4) | — | (member-state law) | — | s.4(4) | — | `dpo` | — |
| PC-15 | Grievance redressal ladder with regulator signposting (DPB, SA, ICO, PDPC, Data Office, CPPA) in every final response | s.13(3), s.5(1)(iii) | SPDI r.5(9) | Art. 77 info | §7011(e) | s.48H info | Art. 24 | `dpo` | — |
| PC-16 | Data minimisation: form-schema lint rejects fields without purpose; minimum data matrix (Appendix S §3.14) | s.6(1) "necessary" | SPDI r.5(2) | Art. 5(1)(c) | §1798.100(c) | s.18 | Art. 5 | product owner | UCS-16 |
| PC-17 | Accuracy and correction propagation to processors and recipients | s.8(3), s.12 | — | Arts 5(1)(d), 16, 19 | §1798.106 | s.22–23 | Art. 15 | `dpo` | — |
| PC-18 | Retention schedule and erasure with erasure certificates (§2.8) | s.8(7); r.8 | SPDI r.5(4) | Arts 5(1)(e), 17 | §1798.100(a)(3) disclose retention | s.25 | Art. 5 | `dpo` | UCS-14 |
| PC-19 | Legal hold overrides retention and erasure with reasoned response | s.8(7) "unless retention necessary for compliance with law"; s.17(1)(a) | — | Art. 17(3)(e) | §1798.105(d) | s.25 | Art. 15 exceptions | `registrar`, `dpo` | UCS-14 |
| PC-20 | Disclosure register: every third-party disclosure logged with purpose code (`ENFORCEMENT`, `COURT_FILING`, `REGULATOR`, `PARTY_COUNSEL`, `PUBLICATION`, `PROCESSOR`) | s.8(1) | SPDI r.6; IT Act s.72A | Arts 15(1)(c), 30(1)(d) | §1798.110 | s.21(1)(b) | Art. 13 | `registrar` | UCS-19 |
| PC-21 | Processor and sub-processor management: DPA with mandatory terms, due diligence, register, annual review (§2.7) | s.8(2); r.6(1)(f) | SPDI r.7 | Art. 28 | §7050–7051 | s.4(2) data intermediary | Art. 8 | `compliance_officer` | UCS-12 |
| PC-22 | Sub-processor change notice to tenants (30 days) with objection right | s.8(2) (contract) | — | Art. 28(2) | §7051(a)(8) | — | Art. 8 | `compliance_officer` | UCS-12 |
| PC-23 | Cross-border transfer register and transfer impact assessment (§2.6); India-resident primary storage | s.16; r.15 | SPDI r.7 | Arts 44–49; UK IDTA/Addendum | — | s.26; PDP Regs 2021 Part 3 | Arts 22–23 | `dpo` | UCS-13 |
| PC-24 | EU and UK Art. 27 representatives appointed before EU/UK targeting; named in notices | — | — | Art. 27 | — | — | — | CS / `dpo` | UCS-18 |
| PC-25 | DPIA triggers and workflow (§2.12) | s.10(2)(c) (SDF); r.13 | — | Arts 35–36 | Risk assessments (Art. 10 regs, 2026) | PDPC DPIA guide | Art. 21 **[VERIFY]** | `dpo` | UCS-15 |
| PC-26 | AI system register and records of AI processing (§2.11) | s.8(1), s.8(3) | — | Arts 5(2), 30; AI Act Arts 12, 26(6) | ADMT regs (2027) | PDPC AI advisory guidelines | — | AI governance lead | — |
| PC-27 | Automated decision-making safeguards: no solely automated decision with legal effect; ADM notices; human review path | s.8(3) accuracy | — | Art. 22; UK Arts 22A–22D | ADMT pre-use notice, opt-out/appeal (2027) | — | Art. 18 | AI governance lead | UCS-07 |
| PC-28 | Encryption, pseudonymisation and masking (KMS per class, field-level for Tier-High/Sealed, TLS 1.2+) | r.6(1)(a) | SPDI r.8 | Arts 25, 32 | §1798.150 reasonable security | s.24 | Art. 20 | security lead | UCS-08 |
| PC-29 | Access control to personal data: ABAC, MFA, PAM, quarterly reviews, sealed break-glass with DPO notice | r.6(1)(b) | SPDI r.8 | Art. 32 | §1798.150 | s.24 | Art. 20 | security lead | UCS-09 |
| PC-30 | Personal-data access logging and monitoring: logs ≥ 400 days in India (covers r.6(1)(e), r.8(3) one year and CERT-In 180 days) | r.6(1)(c), (e); r.8(3) | CERT-In dir. (iv) 180 days | Art. 32 | — | s.24 | Art. 20 | SRE lead | UCS-10 |
| PC-31 | Breach detection and triage: personal-data-breach classifier on every security incident; DPO decision recorded | s.8(6) | CERT-In 6 h | Art. 33(5) documentation | — | s.26C assessment | Art. 9 | `dpo` | UCS-11 |
| PC-32 | Breach notification with per-law clocks from one incident (§2.5) | s.8(6); r.7 | CERT-In 6 h | Arts 33–34 | Civ. Code §1798.82 | s.26D | Art. 9 | `dpo` | UCS-11 |
| PC-33 | Cookie and consent management platform (CMP) for web and mobile SDKs (§2.9) | s.6 (consent for non-essential processing) | — | ePrivacy Art. 5(3) / PECR reg. 6; Art. 7 | §7026 (opt-out link if sharing) | s.13 | Art. 6 | `growth_manager` + `dpo` | — |
| PC-34 | Do-Not-Sell/Share and Global Privacy Control (GPC) honoured; no sale of personal data ever | — (no sale concept; consent) | — | Art. 21(2) objection to direct marketing | §1798.120, §1798.135, §7025 | — | Art. 17 | `growth_manager` | — |
| PC-35 | Marketing consent separate and unbundled; respondents never marketed (NN-16); TCCCPR consent registration for SMS/voice | s.6; s.7 not available for marketing | — | Art. 21(3); PECR reg. 22 | §1798.120 | Part 9 (DNC) | Art. 17 | `growth_manager` | — |
| PC-36 | Publication and anonymisation: consent of all parties + redaction profiles + re-identification test (NN-26) | s.3(c)(ii) (publicly available by principal) — anonymised data out of scope only if irreversible **[VERIFY — open (counsel): DPDP has no anonymisation standard (s.2(t) 'identifiable'); s.3(c)(ii) does not cover Equator-published outcomes — S8 §8 Q9]** | IT Act s.72A | Recital 26 | §1798.140(m) deidentified | Advisory guidelines (anonymisation) | — | `registrar`, `legal_reviewer` | — |
| PC-37 | Confidentiality undertakings (staff, neutrals, vendors) and annual privacy/security training | s.8(5) | IT Act s.72A | Arts 28(3)(b), 29, 32(4), 39(1)(b) | §7051(a) | s.24 | Art. 20 | HR + `dpo` | UCS-20 |
| PC-38 | Privacy by design in SDLC: PII tags in schema, DPIA gate in PR template, synthetic test data only | s.8(1) | — | Art. 25 | §1798.100(e) | — | Art. 7 | tech lead | UCS-16 |
| PC-39 | Data portability and machine-readable export (JSON + PDF) | s.11 (summary) | — | Art. 20 | §1798.130(a)(3)(B)(iii) portable format | s.26F–26J (not yet in force **[VERIFY]**) | Art. 14 | `dpo` | — |
| PC-40 | Regulator engagement register: DPB/SA/ICO/PDPC/Data Office/CERT-In requests, complaints and responses, each with an owned clock | ss.27–28; r.22 (Seventh Sch. calls for information) | CERT-In dir. (ii)/(vi) | Arts 31, 58 | §1798.199.45 (CPPA) | s.50 | Art. 26 | `dpo`, security lead | — |

### 2.3 Product implementation of each control

| ID | Feature (module · data · screen · API) | Config keys / flags | Automated test / evidence |
|---|---|---|---|
| PC-01 | `tenant.legal_entity.dpo`, `.grievance_officer` (X-15) rendered in footer, `/privacy`, `/grievance-officer`, app settings, every DSR response template; CMS lint blocks publishing a legal page without them | `privacy.contact.render` (ON, locked) | `NN-30_PC-01_contact_on_every_dsr_response`; screenshot collector weekly |
| PC-02 | `core.consent_purposes` (P01 FR-P01-36) + new `eng.processing_purposes` (purpose_code, description_i18n, basis_by_jurisdiction jsonb, retention_class, data_categories[], systems[]) | — | Lint: every `consent_purposes.code` has a `processing_purposes` row and vice versa |
| PC-03 | `eng.ropa_entries` (P14) generated from `processing_purposes` × systems × processors; SCR-P14-05 exports GDPR Art. 30(1)/(2) and DPDP formats | `ropa.review_days` = 180 | Diff report: system catalogue tags vs RoPA entries = 0 orphans |
| PC-04 | `packages/rules/privacy/basis.ts` → `basis_for(purpose, role, jurisdiction, data_category)`; persisted on `core.consent_records.basis` (extend CHECK: `gdpr_6_1_b`, `gdpr_6_1_c`, `gdpr_6_1_f`, `gdpr_9_2_f`, `contract_necessity`) | — | Golden vectors per jurisdiction × purpose (≥ 60 cases) |
| PC-05 | §1.3 resolver; `core.persons.privacy_jurisdictions text[]`, `core.organisations.privacy_jurisdictions text[]`, `core.cases.privacy_jurisdictions text[]` (case = union of parties) | `privacy.resolver.version` | Property test: union monotonic; unresolved → strictest set |
| PC-06 | `core.notices_privacy` + new column `jurisdiction text NOT NULL DEFAULT 'IN'`; notice variants in §2.3a; served by `GET /v1/privacy/notices?purpose=&jurisdiction=&locale=` | `privacy.notice.locales.<jurisdiction>` | Every capture surface references a notice whose jurisdiction ∈ person's set |
| PC-07 | `core.consent_records` (F.4.2; append-only); receipt PDF/email with notice hash; `GET /v1/me/consents` | marketing consent expiry 12 months | Trigger `deny_mutation` test; receipt hash = ledger hash |
| PC-08 | `ConsentWithdrawalPropagationWorkflow` (P01 FR-P01-38) + processor fan-out via `PROCESSOR_NOTIFY` outbox topic | processors ≤ 72 h | Each consumer confirms; miss → DPO task |
| PC-09 | `CONSENT_MANAGER_PORT` (master §4.4) with mock CM; artefact ID in `consent_manager_ref` | `legal.consent.consent_manager_integration` (OFF until a registered CM is contracted; registrations open 13 Nov 2026) | Contract test against mock |
| PC-10 | P01 FR-P01-39 flows; `core.persons.is_minor`, `guardian_person_id`; analytics drop for minors; Academy/Campus age gate | `privacy.children.age_of_majority` = 18 (IN); EU per member state (13–16) | `NN-30_PC-10_minor_events_dropped` |
| PC-11 | Sealed stores (P00 FR-P00-16), purposes `health_data`, `family_safety_data`; new purpose `special_category_eu` (religion/community in FAM `regime_resolver`, D2-03) with Art. 9(2)(f) or explicit consent recorded | `privacy.special_category.ai_allowed` = false (locked) | Sealed-schema credential absence test (P11) |
| PC-12 | Public DSR form `/privacy/requests` (no login needed) + in-app rights centre (SCR-P01-42); identity step-up by risk: aal1 for access summary of own account, aal2 for export/erasure; authorised agent upload (CCPA §7063; DPDP nominee) | `dsr.verify.level.<kind>` | Fraud test: unverified requester gets no data |
| PC-13 | `core.dsr_requests` (+ `law_code`, kinds per Q-R5) with `DsrSlaWorkflow` (P14) computing `due_at` = min(statutory, internal) per §2.4 | `dsr.ack_hours` = 48, `dsr.fulfil_days` = 30 | SLA breach event `equator.consent.dsr.breached_sla.v1` |
| PC-14 | Nominee record `core.dsr_nominations` (person_id, nominee_person_id, trigger `death`/`incapacity`, evidence_document_id) | — | Nominee can act only after evidence approval |
| PC-15 | Response templates carry the escalation line for the principal's jurisdiction (DPB / lead SA / ICO / PDPC / UAE Data Office / CPPA) | template set `dsr.final.*` | Template lint |
| PC-16 | Form-engine lint: every field in `core.form_schema_versions` declares `purpose_code` and `data_category`; publish blocked otherwise (`FORM_FIELD_PURPOSE_MISSING`) | — | CI lint over seeded schemas |
| PC-17 | Correction event `equator.consent.personal_data.corrected.v1` → processors and open-case recipients notified (Art. 19) | — | Consumer confirmation log |
| PC-18 | `core.retention_classes` (F.1.3) + Q-R4 class; `RetentionWorkflow` with 48-h pre-erasure notice (good practice, r.8(2)); erasure certificate document per run | dry-run 2 weeks (P14) | Erasure certificate hash in audit chain |
| PC-19 | `legal_hold` columns (F.1.3) + `documents.set_legal_hold()`; DSR erasure partial refusal cites hold | — | `NN-15_dsr_erasure_respects_legal_hold` (P14) |
| PC-20 | Disclosure Register `core.disclosures` (S8-FR-20; Appendix R owns the UI) | purpose codes locked | Every export API writes a disclosure row (contract test) |
| PC-21 | `eng.processors`, `eng.processor_services` (§2.7); DPA template versions; due-diligence questionnaire | `vendor.review_months` = 12 | No `provider_routing` row may be enabled for a provider without `dpa_status='signed'` (`SUBPROCESSOR_NOT_APPROVED`) |
| PC-22 | Public `/legal/sub-processors` page + RSS/email subscription; `eng.subprocessor_changes` with `notice_sent_at`, `effective_at ≥ notice + 30 days` | `subprocessor.notice_days` = 30 | Effective date guard |
| PC-23 | `eng.transfer_register` (§2.6); INT gate uses it (`DPDP_TRANSFER_BASIS_MISSING`) | — | Case cannot register with an EU/UK/SG/AE party unless a register row covers its flows |
| PC-24 | `tenant.legal_entity.eu_representative`, `.uk_representative`; flag gate for EU/UK marketing | `intl.eu_targeting.enabled` (OFF until reps appointed) | Flag cannot turn ON with empty representative fields |
| PC-25 | `eng.dpia_records` (P14) + trigger rules §2.12; PR template checkbox "new personal data / new purpose / new processor / new AI use" → DPIA screening task | — | PR bot blocks merge if box ticked and no `dpia_id` |
| PC-26 | `eng.ai_system_register` (§2.11) + `core.ai_interactions` (P11 provenance) | — | Each enabled `LlmPort` feature has a register row |
| PC-27 | ADM notice block in privacy notices and at AI touchpoints; "Ask a human" path on every AI-assisted outcome screen (all outcomes are human-signed under NN-01) | — | UI test: every AI surface shows notice + human path |
| PC-28 | P00 FR-P00-17 envelope encryption; KMS keys per data class; masking utilities | — | KMS rotation evidence; ciphertext-only check on `*_enc` columns |
| PC-29 | Policy engine (Cerbos/OPA, ADR-0004); `audit.break_glass_events`; P14 FR-P14-21 | — | Role-matrix test (P14 FR-P14-03 API5) |
| PC-30 | `audit.access_log` + SIEM (§3.6); S3 Object Lock 400 days ap-south-1 | `logs.retention_days` = 400 (min 365) | Restore of a 179-day and a 364-day log (P14 exit gate extended) |
| PC-31 | `eng.incidents.category` + `personal_data_involved boolean`, `data_principal_count int`, `jurisdictions text[]` | — | Triage form cannot close without DPO decision on personal-data question |
| PC-32 | `IncidentRegulatoryClockWorkflow` (P14) fans out clocks per §2.5 | `breach.*` keys (§2.5) | Fan-out golden tests |
| PC-33 | First-party CMP component `packages/ui/consent-banner` (§2.9); receipts in `growth.cmp_receipts` | `cmp.mode` = `opt_in_global` | Tag firewall test: no non-essential request before consent |
| PC-34 | GPC detection (`Sec-GPC: 1` header and `navigator.globalPrivacyControl`); `/.well-known/gpc.json` | `privacy.gpc.honour` = ON (global) | E2E with GPC browser profile |
| PC-35 | P13 FR-P13-22 purposes; P01 FR-P01-41 `marketing_eligible=false` for notice-origin persons; TCCCPR consent registration (NN-12) | — | Nightly zero-overlap test (P01) |
| PC-36 | Appendix R publication pipeline; redaction profiles; re-identification test (k-anonymity ≥ 5 on quasi-identifiers for digests) | `publication.arbitral.enabled`, `publication.consensual.enabled` (Appendix R §3; per tenant) | Two-person review evidence |
| PC-37 | HRMS + LMS completion exports; neutral Code of Conduct e-sign (Appendix N) | training annual | GRC evidence: 100% completion within 30 days of joining |
| PC-38 | Schema PII tags (`COMMENT ON COLUMN … IS 'pii:tier_high;purpose:dispute_administration'`), seed generator for synthetic data, prod-data-in-non-prod detector | — | CI: untagged column in a personal-data table fails migration |
| PC-39 | `POST /v1/me/exports` (JSON + PDF, 7-day link) | — | Export schema test |
| PC-40 | `eng.regulator_requests` (regulator, reference, received_at, due_at, owner, status, response_document_id) | — | Clock owned (NN-04 pattern) |

#### 2.3a Notice set by jurisdiction and language

| Jurisdiction code | Notice variant (template ID) | Mandatory elements beyond the DPDP r.3 core | Languages at launch | On request |
|---|---|---|---|---|
| `IN` | `eqr.notice.in.v2` + SPDI privacy policy page (`/privacy`) | itemised data and purposes, goods/services enabled, withdrawal, rights, complaint to the Board (s.5(1)(iii)); SPDI r.4 types of SPDI and security practices | en-IN, hi-IN + 10 configured Indian languages (NN-23) | any Eighth Schedule language (s.5(3)) |
| `EU` | `eqr.notice.eu.v2` | controller identity and **EU representative**; DPO contact; purposes and Art. 6 basis per purpose; Art. 9(2)(f) where special data; legitimate interests stated; recipients; **transfer to India and safeguard** (no adequacy decision for India) and how to get a copy; retention; Arts 15–22 rights; right to complain to a supervisory authority; whether provision is statutory/contractual; ADM statement (none solely automated) — Arts 13–14 | en + party's EU language via machine draft labelled "Translation — for convenience" after legal review (NN-23, NN-32) | de, fr, es, it, nl, pl, pt (configurable) |
| `UK` | `eqr.notice.uk.v2` | as EU with UK representative, ICO complaint route, IDTA/Addendum | en-GB | — |
| `US-CA` | `eqr.notice.ca.v2` (activated only in CCPA mode) | categories of PI and SPI, purposes, **"we do not sell or share personal information"**, retention per category, rights and methods (two methods incl. toll-free or email for online-only), GPC statement, ADMT notice if any | en-US | es |
| `SG` | `eqr.notice.sg.v2` | purposes (notification obligation s.20), DPO contact, transfer to India and TLO safeguard | en | zh, ms, ta |
| `AE`/`AE-DIFC`/`AE-ADGM` | `eqr.notice.ae.v2` | controller identity, purposes, basis, recipients, transfers, rights incl. objection to automated processing; DIFC/ADGM variants cite their Commissioner | en, ar | — |

Every notice: version, effective date, SHA-256 in `core.notices_privacy`; one notice per purpose bundle; never inside the Terms of Use; legal-approved before activation (P01 FR-P01-35).

### 2.4 Data-subject request portal — kinds, laws and SLAs

DDL delta (additive except the `kind` CHECK — ADR required):

```sql
ALTER TABLE core.dsr_requests
  ADD COLUMN law_code text NOT NULL DEFAULT 'IN_DPDP'
    CHECK (law_code IN ('IN_DPDP','IN_SPDI','EU_GDPR','UK_GDPR','US_CA_CCPA','SG_PDPA','AE_PDPL','AE_DIFC','AE_ADGM')),
  ADD COLUMN requester_kind text NOT NULL DEFAULT 'self' CHECK (requester_kind IN ('self','guardian','nominee','authorised_agent','counsel')),
  ADD COLUMN verified_at timestamptz, ADD COLUMN verification_level text,
  ADD COLUMN extended_until timestamptz, ADD COLUMN extension_reason text,
  ADD COLUMN statutory_due_at timestamptz NOT NULL, ADD COLUMN internal_due_at timestamptz NOT NULL;
ALTER TABLE core.dsr_requests DROP CONSTRAINT dsr_requests_kind_check,
  ADD CONSTRAINT dsr_requests_kind_check CHECK (kind IN ('access','correction','erasure','nomination','grievance','withdrawal',
    'restriction','portability','objection','adm_review','opt_out_sale_share','limit_spi','know'));
```

| Kind | Laws that grant it | Statutory clock (from receipt) | Equator internal SLA | Notes |
|---|---|---|---|---|
| Acknowledge any request | CCPA §7021(a): 10 business days | 10 business days (CA) | **48 h** all jurisdictions | — |
| access / know | DPDP s.11; GDPR Art. 15; CCPA §1798.110; PDPA s.21; PDPL Art. 13 | DPDP ≤ 90 days outer (r.14(3)); GDPR 1 month (+2 months if complex, notify within first month); CCPA 45 days (+45); PDPA 30 days or written notice of time needed; PDPL per Executive Regulations **[VERIFY]** | **30 days** | Summary of data, purposes, recipients (incl. disclosure register), sources; exclude other parties' data and sealed caucus notes (NN-11) with reason |
| correction | DPDP s.12; Art. 16; §1798.106; PDPA s.22; PDPL Art. 15 | as above | 30 days | Propagate (PC-17); pleadings and evidence are never altered — a correction note is linked instead (NN-32) |
| erasure | DPDP s.12(3); Art. 17; §1798.105; PDPL Art. 15 | as above | 30 days | Legal hold, s.17(1)(a), Art. 17(3)(e), award retention (Q-R4) → partial fulfilment with reasons |
| restriction | Art. 18; PDPL Art. 16 | 1 month | 30 days | Flag `processing_restricted` on person; only storage + legal-claims use |
| portability | Art. 20; PDPL Art. 14; CCPA portable format | 1 month / 45 days | 30 days | JSON + PDF export (PC-39) |
| objection | Art. 21; PDPL Art. 17 | 1 month | 30 days | Marketing objection = immediate suppression |
| adm_review | Art. 22(3); UK Arts 22A–22D; CCPA ADMT appeal (2027); PDPL Art. 18 | 1 month / per regs | 30 days | Equator makes no solely automated decisions; the request routes to the human owner and explains which steps were AI-assisted (§2.11) |
| opt_out_sale_share | §1798.120; §7026 | 15 business days | **immediate** (≤ 24 h) | Equator does not sell or share; request is recorded and confirmed |
| limit_spi | §1798.121; §7027 | 15 business days | immediate | SPI already used only for permitted purposes |
| withdrawal | DPDP s.6(4); Art. 7(3) | — (as easy as giving) | immediate; propagation per PC-08 | — |
| nomination | DPDP s.14; r.14(4) | — | 30 days | — |
| grievance | DPDP s.13; SPDI r.5(9) | DPDP ≤ 90 days; SPDI one month | **30 days** | Final reply names the Board (DPDP s.13(3) exhaustion) |

`due_at` = `min(statutory_due_at, internal_due_at)`; GDPR extensions set `extended_until` and send the extension notice within the first month. Requests from respondents about a live case are fulfilled with the s.17(1)(a) carve-out stated (Chapter III rights do not apply to processing necessary to enforce a legal claim) but Equator still provides access to their own submissions and contact data as policy.

**DSR work queue *(v3.1)*.** The DPO office works one queue in the DPO console (menu placement per Appendix AG).

| Element | Rule |
|---|---|
| Order | Nearest `due_at` first; requests whose statutory clock is ≤ 5 days away are pinned; then `opt_out_sale_share`, `limit_spi`, `withdrawal` and marketing `objection` (immediate kinds) |
| Pauses | The **statutory** clock is never paused by Equator. Only the internal SLA pauses, with a recorded reason (`awaiting_identity`, `awaiting_requester_clarification`, `awaiting_guardian_proof`); the requester sees the reason and the statutory date. Identity checks are proportionate (PC-12): no more data is asked than needed to match the record |
| Duplicates | A new request from the same verified person, of the same kind, within 30 days of an open one is linked to it (one response, both receipts); a repeated access request after fulfilment is answered with the last package plus changes since, never refused as "too frequent" without the law's ground being cited |
| Live-case requests | A request touching a live case opens a task for the case's `registrar` to identify other parties' data and sealed material to exclude; the DPO, not the case team, sends the reply |
| Bulk and templates | Approved response templates per kind and law; "Fulfil selected" only for `withdrawal` and marketing `objection` (propagation per PC-08); every other kind is answered one by one |
| Delegation | A deputy DPO (named in `tenant.legal_entity.dpo_deputy`) receives the queue when the DPO is on approved leave (Appendix Z; `equator.hr.leave.started.v1` to `.ended.v1` / `.cancelled.v1`) *(v3.1)*; the reply always carries the DPO contact (PC-01) |
| Exports | Access and portability packages use `EQ-EXPORT-1.0` scope `DSR_PORTABILITY` (Appendix AC §AC.13) with a manifest and checksums (NN-37) |
| KPIs | 100% acknowledged within 48 h; 100% within statutory clock; ≥ 95% within internal SLA; median days to fulfil by kind; share of requests needing identity follow-up (watch) |

`core.dsr_requests` gains `internal_sla_paused_reason text`, `internal_sla_paused_at timestamptz` and `linked_request_id uuid` (additive). Acceptance: Q-25 (below) — a request with the statutory clock 4 days away appears above a newer request; pausing for `awaiting_identity` changes `internal_due_at` but never `statutory_due_at`. *(v3.1)*

### 2.5 Breach workflow — one incident, per-law clocks

Clock start = `noticed_at` (CERT-In), `aware_at` (DPDP r.7(2)(b), GDPR Art. 33), `assessed_notifiable_at` (PDPA s.26D). The DPO records `aware_at` and `assessed_notifiable_at`; the workflow refuses to proceed without them.

| Recipient | Condition | Clock | Config key (default, guardrail) | Template |
|---|---|---|---|---|
| CERT-In | Annexure I incident type (any, incl. without personal data) | **6 h** from noticing | `cert_in.report_hours` = 6 (cannot be raised) | CERT-In incident form |
| Data Protection Board of India | Any personal data breach (no materiality threshold) | intimation **without delay** (target ≤ 24 h); detailed report **≤ 72 h** of awareness or longer period allowed on written request (r.7(2)) | `breach.dpb.intimation_hours` = 24; `breach.dpb.report_hours` = 72 (cannot be raised) | r.7(2)(a)/(b) forms |
| Affected Data Principals (India) | Any personal data breach | **without delay**, plain language, in their language (r.7(1)) | `breach.principals.target_hours` = 72 | per-locale template |
| EU supervisory authority(ies) | Personal data breach unless unlikely to result in risk | **72 h** of awareness (Art. 33(1)); no one-stop-shop for a non-EU controller — notify each SA where affected data subjects reside, via the Art. 27 representative where helpful [Verified 22 Oct 2026: EDPB Guidelines 9/2022 v2.0 (28 Mar 2023) para 73] | `breach.gdpr.hours` = 72 | Art. 33(3) content |
| EU data subjects | High risk | without undue delay (Art. 34) | — | Art. 34(2) |
| UK ICO / UK individuals | as GDPR | 72 h / without undue delay | `breach.ukgdpr.hours` = 72 | ICO form |
| Singapore PDPC | Significant harm or ≥ 500 individuals | **≤ 3 calendar days** after assessment (s.26D(1)); assessment expeditious (target ≤ 30 days of awareness, PDPC guidance) | `breach.pdpc.days` = 3; `breach.pdpc.assessment_days` = 30 | PDPC form |
| Singapore individuals | Significant harm | on or after notifying PDPC, as soon as practicable (s.26D(2)) | — | — |
| UAE Data Office | Breach prejudicing privacy/confidentiality/security | upon becoming aware (Art. 9) **[VERIFY — Executive Regulations period]** | `breach.uae.hours` = 72 (provisional) | — |
| DIFC Commissioner / ADGM Office of Data Protection | As their laws | as soon as practicable (DIFC) / 72 h (ADGM) **[VERIFY]** | `breach.difc.hours` = 72; `breach.adgm.hours` = 72 | — |
| California residents / AG | Unencrypted personal information acquired (Civ. Code §1798.82) | most expedient time, without unreasonable delay; statutory day-limits introduced in 2025 **[VERIFY — open: SB 446 (2025) 30-day/15-day deadlines not confirmed against leginfo (22 Oct 2026); 30 days kept as config]** | `breach.us_ca.days` = 30 | — |
| Tenant (Equator as processor) | Any breach affecting tenant data | contractual | `breach.tenant_notice_hours` = 24 (≤ 72, P14) | DPA schedule |
| Regulated tenant (RBI RE, IRDAI insurer) | Cyber incident affecting RE data/services | contractual, so that the RE meets its own 6-h report | **`breach.regulated_tenant_notice_hours` = 2** (≤ 6) | RE incident template |
| Insurers (policy) | Cyber/PI policy notice conditions | per policy | `insurance.notice_hours` from policy schedule | — |

Implementation: `IncidentRegulatoryClockWorkflow` (P14 §7.5) reads `eng.incidents.jurisdictions` and `personal_data_involved`, creates one `eng.regulatory_notifications` row per applicable recipient (Q-R6 values), alerts at 50% and 80% of each clock, and escalates any unowned row as Sev-1 (NN-04 pattern). GDPR Art. 33(5) / DPDP evidence: every breach — notified or not — keeps facts, effects and remedial action in `eng.incident_timeline` for 6 years (`retention_class = 'breach_record'`).

### 2.6 Cross-border transfer register

```sql
CREATE TABLE eng.transfer_register (
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  flow_code text NOT NULL UNIQUE,                    -- e.g. 'INT_EU_PARTY_SUBMISSIONS', 'GA4_WEB_ANALYTICS', 'PAYPAL_INT_PAYMENTS'
  direction text NOT NULL CHECK (direction IN ('export_from_india','import_to_india','onward')),
  exporter text NOT NULL, importer text NOT NULL, importer_country char(2) NOT NULL,
  data_categories text[] NOT NULL, special_categories text[] NOT NULL DEFAULT '{}', principals_estimate int,
  purposes text[] NOT NULL,
  mechanism text NOT NULL CHECK (mechanism IN ('dpdp_s16_not_restricted','dpdp_s17_1_d','gdpr_not_transfer_direct_collection',
    'gdpr_scc_m1','gdpr_scc_m2','gdpr_scc_m3','gdpr_scc_m4','gdpr_art49_1_b','gdpr_art49_1_e','uk_idta','uk_addendum',
    'sg_tlo_contract','sg_tlo_consent','uae_pdpl_art22','uae_pdpl_art23','difc_safeguard','adgm_safeguard','contract_only')),
  tia_document_id uuid, contract_document_id uuid, negative_list_checked_at timestamptz NOT NULL,
  sectoral_localisation_check text NOT NULL,          -- e.g. RBI payment-data localisation (6 Apr 2018) n/a | ok
  status text NOT NULL CHECK (status IN ('draft','approved','suspended','retired')),
  approved_by uuid, review_due date NOT NULL, created_at timestamptz NOT NULL DEFAULT now());
```

Rules: (1) A party who is in the EU and **submits their own data directly** to Equator in India is not a Chapter V transfer by Equator (direct collection under Art. 3(2)); record mechanism `gdpr_not_transfer_direct_collection` and rely on Art. 3(2) compliance [Verified 22 Oct 2026: EDPB Guidelines 05/2021 v2.0 (14 Feb 2023), Example 1]. (2) When an EU-established controller (EU counsel, EU company) **sends** data to Equator, the EU exporter needs a transfer tool: Equator signs SCCs Module 1 (controller→controller) as importer, or Module 2 where Equator acts as their processor; Art. 49(1)(e) (legal claims, non-repetitive) is the fallback per case, never the default. (3) The TIA documents Indian government-access law (IT Act 2000 s.69; Telecommunications Act 2023 s.20; DPDP s.36 power to call for information; CERT-In directions) and Equator's mitigations (encryption with keys in India, no voluntary disclosure, challenge policy, transparency log). (4) DPDP: no country is restricted under s.16(1) as of Oct 2026 [V RES_A4 Q09]; `negative_list_checked_at` is refreshed by the legal-rules watch on every Gazette update. (5) Equator **onward** transfers out of India are limited to flows in §8.1; each has a row.

### 2.7 Processor and sub-processor management

`eng.processors` (vendor, legal entity, country, services, data categories, processing location(s), `dpa_status` (`none`,`sent`,`signed`,`expired`), DPA version, SCC/IDTA status, certifications (ISO 27001/SOC 2 report date, PCI AoC date), CERT-In/VAPT evidence, risk tier `T1` (personal data at scale or sealed), `T2`, `T3`, last review, next review, exit plan). `eng.processor_services` links a processor to `core.provider_routing` providers and to `eng.transfer_register` flows.

DPA mandatory terms (single Equator DPA template serving DPDP s.8(2)/r.6(1)(f), GDPR Art. 28(3)(a)–(h), CCPA §7051(a), PDPA data-intermediary duties, PDPL Art. 8): documented instructions; confidentiality of personnel; security measures (Annex: PC-28 to PC-30); sub-processing only with prior general authorisation + 30-day notice and objection; assistance with rights and DPIAs; breach notice to Equator ≤ 24 h (≤ 2 h for incidents touching regulated-tenant data); deletion/return at end with certificate within 30 days; audit rights (on-site or report-based); India storage clause where the master requires it; no sale/share and no use for own purposes (CCPA); AI providers: no training on Equator data, zero data retention or ≤ 30-day abuse-monitoring retention disclosed.

Seed sub-processor list (from master §8; each subject to DPA and residency confirmation — `R3 §11` U-items): AWS (hosting, ap-south-1/2), Amazon Bedrock (LLM, India in-country inference), Anthropic (LLM fallback — **outside India; flag `ai.anthropic_direct.enabled` OFF unless a transfer row is approved**), Sarvam (Indic STT/TTS/OCR/translation), ElevenLabs (voice; India residency Enterprise), Exotel/Plivo (telephony), Gupshup/Meta (WhatsApp; local storage IN), MSG91 (SMS), AWS SES (email), Expo/FCM/APNs (push — **content-free payloads for sealed/committee events**), Leegality/Digio/Setu/SignDesk (eSign/eStamp), Surepass/IDfy/Signzy/HyperVerge (KYC/KYB), Razorpay/Cashfree/PayPal (payments), RazorpayX/Castler (escrow), LiveKit Cloud India (video), Sentry (India residency), PostHog self-hosted (no sub-processor), Google Analytics 4 (consent-gated, transfer row `GA4_WEB_ANALYTICS`), GRC tool (§5.4), paging/status-page tools (per ADR).

### 2.8 Retention schedule (defaults; `core.retention_classes`; legal hold always overrides)

| Retention class | Default | Driver | Erasure method |
|---|---|---|---|
| `case_record` | 8 years after closure | master §11; Limitation Act 1963 general periods | field-level erasure + tombstone; evidence object expiry under Object Lock |
| `outcome_instrument` (new, Q-R4) | 13 years from instrument date or 1 year after execution completes, whichever later | Limitation Act 1963 Sch. Art. 136 (12 years) with A&C Act s.36 | as above |
| `caucus_note` | 12 months after closure | NN-11 | crypto-shred sealed key slice |
| `ai_log` | 12 months | P11 FR-P11-45 | delete |
| `audit` | 10 years | master §11 | partition detach to WORM then drop |
| `posh` | 7 years (tenant policy may extend) | master §11 | sealed-store purge with certificate to tenant |
| `health`, `family_safety` | case record period, sealed | NN-07 | crypto-shred |
| `call_recording_recovery` | ≥ 6 months; longer if sub judice | NN-12; RBI RBC Directions 2026 | delete |
| `call_recording_other` | per consent; max 12 months | consent | delete |
| `kyc` | 5 years after relationship ends | policy (PMLA analogy; Equator not a reporting entity) **[VERIFY — counsel]** | delete; Aadhaar payload never stored (NN-14) |
| `liveness_media` (new) | ≤ 30 days | Appendix S §3.12 | delete |
| `financial_tax` | 8 years from end of financial year | Companies Act 2013 s.128(5); CGST Act s.36 (72 months from annual-return due date) | delete |
| `consent_record` | 7 years after withdrawal/expiry | F.4.2 | delete |
| `breach_record` (new) | 6 years | GDPR Art. 33(5) evidence; limitation | delete |
| `dsr_record` (new) | 3 years after closure | accountability | delete |
| `security_logs` (new) | 400 days | CERT-In 180 days; DPDP r.6(1)(e), r.8(3) | Object Lock expiry |
| `marketing_lead` | 12 months from last interaction or consent withdrawal | PC-35 | delete + CRM suppression hash kept |
| `telemetry` | 13 months (product analytics, consented) | policy | delete |
| `neutral_applicant_unsuccessful` (new) | 24 months | policy | delete |
| `cctv_office` (new) | 30 days | policy | overwrite |

Pre-erasure notice 48 h before erasing an account's data (r.8(2) good practice); erasure certificate (`document_kind = 'erasure_certificate'`, SHA-256 listed in audit) per run and per DSR.

### 2.9 Cookie/consent management (CMP), Do-Not-Sell/Share and GPC

**Decision Q-D3 — one global opt-in model.** All jurisdictions get the strictest model: only strictly necessary cookies/storage before consent; "Accept all", "Reject all" and "Choose" have equal prominence (no dark patterns — India's Central Consumer Protection Authority Guidelines for Prevention and Regulation of Dark Patterns 2023 (NN-29), California 11 CCR §7004 symmetry-in-choice, and EDPB cookie-banner practice); consent lasts 12 months or until the banner version changes; withdrawal from a persistent "Privacy choices" link in the footer and app settings.

| Category | Examples | Default | Allowed surfaces |
|---|---|---|---|
| `strictly_necessary` | session, CSRF, load-balancer, CMP state, language | always on | all |
| `functional` | remembered filters, chat widget on marketing pages | off | marketing pages, portals |
| `analytics` | PostHog self-hosted (first-party, India), GA4 (Google, transfer row) | off | marketing pages only; **never** `/app`, case routes, `/verify`, `/pay/*`, `/settlements-and-awards` (P13 FR-P13-23) |
| `marketing` | ad pixels, retargeting | **off and not deployed at launch** (feature flag `growth.ad_pixels.enabled` OFF) | marketing pages only, after legal review |

GPC/Do-Not-Sell/Share: requests with `Sec-GPC: 1` or `navigator.globalPrivacyControl === true` are treated as **refusal of `marketing` and of any third-party analytics** worldwide; the banner shows "Global Privacy Control signal honoured". Equator never sells personal data and never shares it for cross-context behavioural advertising; therefore no "Do Not Sell or Share" link is required unless CCPA mode is ON and ad pixels are enabled — in which case the link `/privacy/choices` is rendered in the footer (§7026) and GPC applies per §7025. `/.well-known/gpc.json` returns `{"gpc": true, "lastUpdate": "<date>"}`. CMP receipts: `growth.cmp_receipts` (visitor_id_hash (salted SHA-256 of first-party ID), banner_version, choices jsonb, gpc boolean, jurisdiction_hint, at) — no IP stored.

Mobile: no third-party analytics SDKs in the party app; Expo app uses first-party telemetry only after in-app consent; Apple App Tracking Transparency prompt never shown because no tracking occurs.

### 2.10 Children's data

Applies to Academy/Campus learners, student grievance (UGC SGRC), FAM matters naming children, and minors as parties. Rules: age gate (DOB) where a minor may be the account holder; guardian verifiable consent (DPDP r.10; virtual token incl. DigiLocker); no tracking, behavioural monitoring or targeted advertising (s.9(3)); FAM child data limited to initials and age in core, details in `safety_sealed`; publication never (NN-26); EU child (< 16 or member-state age) → parental authorisation for any consent-based processing (Art. 8). Rule 12 + Fourth Schedule exemptions (e.g., educational institutions for educational activities) are recorded where relied on.

### 2.11 Automated decision-making notices and records of AI processing

**AI system register** `eng.ai_system_register`: `ai_system_id`, name (e.g., `intake_assistant`, `document_extractor`, `case_summariser`, `drafting_assistant`, `negotiation_facilitator`, `translation_agent`, `case_manager_copilot`, `voice_agent`, `grievance_responder`, `qa_auditor`, `analytics_narrator`, `pleadings_studio`), intended purpose, users (party/neutral/staff), model(s) and provider (`LlmPort` route), data categories in/out, sealed-data exclusion asserted, human-oversight design (NN-01 human signs), EU AI Act classification (`not_ai_act_scope` | `annex_iii_8a_high_risk` | `art_6_3_exempt` with documented reasoning per Art. 6(4)), CCPA ADMT classification (`no_significant_decision`), DPIA/AIIA ID (ISO/IEC 42005-aligned), eval suite IDs, kill-switch key, owner, status. A register row is a precondition for enabling any AI feature flag (`AI_SYSTEM_NOT_REGISTERED`).

**Records of AI processing** = `core.ai_interactions` (P11 FR-P11-13: prompt version, model, policy version, retrieved source IDs, human reviewer, final action) — the per-event log that GDPR Art. 30/accountability, EU AI Act Art. 12 (logging) and Art. 26(6) (deployer log retention ≥ 6 months) require; retention 12 months (≥ 6 months satisfied).

**ADM notice text (en; all jurisdictions; legal-approved before use):** "Some steps in this service use AI to sort, extract, summarise, translate or draft. AI never decides your case, gives legal advice, predicts results or values your claim. A named person — the case manager or the neutral — makes every decision and signs every outcome. You can ask for any AI-assisted step to be redone by a person, and you can use the service without AI (we will use a standard questionnaire instead)." The last sentence is backed by NN-02 and the `ai_assisted_processing` purpose (P01). **EU-party mode** (`ai.eu_party_mode`, auto ON when `case.privacy_jurisdictions ∋ 'EU'`): AI limited to clerical, translation and summarisation (LR-INT-020); neutral-assist drafting and summarisation of evidence for the neutral are disabled unless `ai.eu_neutral_assist.enabled` is ON with an approved Art. 6(3) assessment or a completed high-risk compliance file (from 2 Dec 2027).

### 2.12 DPIA triggers

A DPIA (P14 `eng.dpia_records`) is mandatory before go-live of any of: new vertical or sub-type with special-category data; any sealed-store change; new AI system or a material model/prompt change in a register row; voice/call recording changes; publication mode changes; new processor in risk tier T1; new cross-border flow; children's data use; Account Aggregator or bureau-derived data; new jurisdiction activated (EU/UK/SG/AE/US-CA); biometrics/liveness vendor change; large-scale monitoring (e.g., contact-conduct analytics). Screening questionnaire (12 questions, EDPB/WP248 criteria + DPDP SDF factors) scores ≥ 2 criteria → full DPIA; DPO sign-off and, for residual "high" after mitigation, Art. 36 prior consultation analysis for EU-scope processing.

### 2.13 APIs, events and errors added by §2

APIs (`/v1`; DPO/compliance roles unless stated; step-up for writes; `Idempotency-Key` on POST): `POST /v1/privacy/requests` (public, CAPTCHA, email/phone OTP) · `GET /v1/privacy/notices` (public) · `POST /v1/privacy/jurisdiction:resolve` (internal) · `GET/POST /v1/eng/processing-purposes` · `GET/POST /v1/eng/transfers` · `POST /v1/eng/transfers/{id}:approve` · `GET/POST /v1/eng/processors` · `POST /v1/eng/subprocessor-changes` · `GET /v1/public/sub-processors` · `GET/POST /v1/eng/ai-systems` · `POST /v1/growth/cmp-receipts` (public, rate-limited) · `GET/POST /v1/eng/regulator-requests` · `POST /v1/me/exports`.

Events: `equator.consent.notice.published.v1`, `equator.consent.dsr.received.v1`, `equator.consent.dsr.fulfilled.v1`, `equator.consent.personal_data.corrected.v1`, `equator.consent.jurisdiction.resolved.v1`, `equator.eng.transfer.approved.v1`, `equator.eng.subprocessor.change_notified.v1`, `equator.eng.ai_system.registered.v1`, `equator.eng.regulator_request.due.v1`, `equator.growth.cmp.receipt_recorded.v1`.

Canonical error codes (add to F.10.1): `PRIVACY_JURISDICTION_UNRESOLVED` (200 with warning header; task only), `FORM_FIELD_PURPOSE_MISSING` (422), `SUBPROCESSOR_NOT_APPROVED` (409), `AI_SYSTEM_NOT_REGISTERED` (409), `EU_REPRESENTATIVE_REQUIRED` (409), `AI_FEATURE_DISABLED_FOR_EU_PARTY` (403), `CARD_DATA_FORBIDDEN` (422), `CARD_DATA_DETECTED_IN_UPLOAD` (422), `CONTROL_EVIDENCE_STALE` (409, ops only); reuse `DPDP_TRANSFER_BASIS_MISSING`.

---

## 3. Security architecture baseline

Master §4.1, §11 and P00/P14 already fix the stack (AWS ap-south-1/ap-south-2, Keycloak, Cerbos/OPA, KMS, Object Lock, OpenTelemetry, ASVS 5.0.0 L2/L3, CERT-In VAPT). This section is the consolidated security baseline that auditors test; each row names its security control ID (`SC-xx`), which the GRC library maps to ISO/IEC 27001:2022 Annex A and SOC 2 (§5–§6).

### 3.1 Principles (zero trust)

1. **No implicit trust from network location.** Every request is authenticated, authorised by the policy engine (tenant, case membership, role-in-case, confidentiality tier, purpose, time-bound grant) and logged; internal service calls use workload identity (ECS task roles + mTLS between services via service mesh or ALB-to-target TLS) — never shared API keys.
2. **Least privilege, just in time.** Humans have no standing production access; elevation is time-boxed, approved and recorded.
3. **Assume breach.** Blast radius limited by tenant RLS, sealed stores on a separate cluster and KMS keys, per-data-class keys, egress allow-lists, and immutable evidence/audit.
4. **Verify devices** for workforce (MDM compliance claim or mTLS certificate) before access to staff consoles (Appendix S FR-P01-V2-05).
5. **Everything as code**: infrastructure, policies, controls and evidence collectors are versioned and reviewed (§7).

### 3.2 Control baseline

| SC ID | Domain | Baseline requirement (build-time) | Defaults / config | Evidence (automated unless marked) |
|---|---|---|---|---|
| SC-01 | Workforce IAM | Workforce IdP (Google Workspace or Microsoft Entra ID — ADR) federated to AWS IAM Identity Center, GitHub, Grafana, GRC tool, ticketing; SCIM provisioning from HRMS; joiner-mover-leaver within 24 h of HR event (leaver ≤ 4 h) | `iam.leaver_revoke_hours` = 4 | SCIM logs; JML tickets; leaver test monthly |
| SC-02 | Customer IAM | Keycloak per P01 + Appendix S portals; `eq:aal2-pr` (phishing-resistant) for staff, committee, admin and arbitrator signing; DPoP-bound tokens (Keycloak ≥ 26.4) | access token 5 min; refresh rotation | IdP config export; auth test suite |
| SC-03 | MFA | MFA mandatory for all workforce (FIDO2/passkey; TOTP only as recovery), all professional users (neutrals, counsel, enterprise admins), and step-up for signing, payouts, config changes, sealed access, exports | — | IdP MFA coverage report = 100% workforce |
| SC-04 | Privileged access (PAM) | No IAM users; IAM Identity Center permission sets with max session 1 h; JIT elevation via approval (ticket + second approver) for `prod-admin`; SSM Session Manager only (no SSH/RDP, no bastions) with session logs to the log-archive account; database break-glass via IAM auth, read-only by default | `pam.max_session_minutes` = 60 | Elevation log; session recordings; quarterly review |
| SC-05 | Encryption at rest | KMS CMKs per data class (P00 FR-P00-06: `documents`, `evidence`, `pii-field`, `sealed-posh`, `sealed-health`, `sealed-safety`, `audit-anchor`, `backup`); envelope field-level encryption for Tier-High/Sealed (P00 FR-P00-17); automatic annual rotation | — | KMS rotation status; Config rule `kms-cmk-rotation-enabled` |
| SC-06 | BYOK | Enterprise tenants with `dedicated_key = true` may supply key material: (a) customer-managed CMK in Equator's account with **imported key material** (AWS KMS `EXTERNAL` origin) and customer-controlled expiry, or (b) cross-account grant to a CMK in the customer's AWS account (ap-south-1) — revocation renders that tenant's encrypted fields unreadable (crypto-shred). External key stores (XKS) out of scope at launch | `tenancy.byok.modes` = [`imported`, `cross_account`] | Key policy diff; revocation drill per BYOK tenant annually |
| SC-07 | Encryption in transit | TLS 1.2+ (1.3 preferred) everywhere; HSTS preload (P14 FR-P14-20); internal TLS; SFTP for bulk with per-tenant keys; webhook payloads signed (HMAC-SHA256) | weak ciphers disabled at ALB policy `ELBSecurityPolicy-TLS13-1-2-2021-06` | SSL Labs/testssl reports |
| SC-08 | Secrets | AWS Secrets Manager only; rotation ≤ 90 days (DB service creds 30 days); no secrets in env files, images or repos; gitleaks/trufflehog pre-commit and CI; provider webhook secrets rotated at go-live and on staff exit | `secrets.max_age_days` = 90 | Rotation report; secret-scan CI results |
| SC-09 | Logging and SIEM | Central log pipeline: CloudTrail (org), VPC Flow Logs, ALB/CloudFront/WAF, GuardDuty, Security Hub, Keycloak events, app audit/access logs, LiveKit, telephony CDRs, provider webhooks → `eq-log-archive` S3 (Object Lock 400 days, India) → SIEM (**Amazon Security Lake + OpenSearch Security Analytics** default; alternative per ADR) with detections mapped to MITRE ATT&CK; NTP per CERT-In | detection rules as code (`security/detections/*.yml`) | Log-source coverage dashboard; detection test results |
| SC-10 | Detection use cases (minimum) | impossible travel/geo-velocity on staff; MFA fatigue; mass export or decrypt by one actor (> 200 Tier-High decrypts/hour); break-glass use; sealed-store access outside business hours; RLS policy change; KMS key disable/schedule-deletion; Object Lock configuration attempt; root login; new IAM principal; WAF spike; outbound to non-allow-listed domain; AI gateway guardrail block spike; out-of-window contact attempt (NN-12) | — | Monthly purple-team test of 5 rules |
| SC-11 | Vulnerability management | Weekly authenticated scans (Inspector for ECR/ECS, dependency SCA in CI, Trivy images, Checkov IaC); SLA from discovery: **Critical ≤ 7 days** (≤ 72 h if on CISA KEV or internet-exposed), **High ≤ 30 days**, Medium ≤ 45 days, Low ≤ 90 days (aligned with P14 FR-P14-04); exceptions need security lead + risk owner sign-off with expiry ≤ 90 days. **v3.0 (23 Oct 2026; master X-66(a), D3-44):** these values are the **locked (L) outer ceilings**; the platform defaults are tighter — Critical ≤ 72 h, High ≤ 7 days, Medium ≤ 30 days, Low next release (≤ 90 days) (Appendix AE §AE.5) — and a setting may only tighten them; P14 FR-P14-04 VAPT SLAs still apply and the stricter rule wins | `vuln.sla.*` (G within the L ceilings) | `eng.vulnerabilities` SLA report (`eng.vulnerabilities` is a v3.0 compatibility view — master X-65) |
| SC-12 | Secure SDLC | Threat model per epic touching auth, money, sealed data, AI or external interfaces; security requirements from ASVS 5.0.0; protected `main`, ≥ 1 reviewer (2 for `packages/rules`, auth, payments, sealed modules), CODEOWNERS; SAST (Semgrep + CodeQL), SCA, secrets, IaC, container scans as blocking gates; DAST (OWASP ZAP baseline + authenticated API scan) nightly on staging; security champions per squad; annual secure-coding training | — | PR logs; CI results; training records |
| SC-13 | Supply chain | SBOM (CycloneDX) per build; cosign signatures verified at deploy; SLSA Build L2 provenance (target L3); GitHub Actions pinned by SHA and linted (`zizmor`); Renovate with 7-day cool-down; npm `--ignore-scripts` in CI with allow-list; private registry proxy with malware check; vendor SDK inventory for mobile | — | Admission-policy deny log; SBOM archive |
| SC-14 | DLP | Amazon Macie on non-evidence buckets (weekly) for PAN/Aadhaar/card patterns; egress proxy allow-list (`infra/egress-allowlist.yaml`); export governance (exports bucket 7-day lifecycle, watermark with requester name and time on PDFs of standard/high tiers, sealed exports blocked except via break-glass); workforce email DLP rules for Aadhaar/PAN/card numbers; clipboard/download controls on staff consoles for non-compliant devices; PAN detector on uploads/chat (§4.6) | — | Macie findings; blocked-egress log |
| SC-15 | Endpoint (staff) | MDM (Intune/Jamf/Kandji — ADR) on all company devices; full-disk encryption; EDR; OS and browser patches ≤ 14 days (critical ≤ 72 h); screen lock 5 min; USB mass storage blocked for users with sealed or Tier-High access; no BYOD access to staff consoles beyond read-only standard tier (Appendix S §2.6) | — | MDM compliance export |
| SC-16 | Network and edge | VPC private subnets; no inbound except ALB/CloudFront; AWS WAF managed + custom rules; Shield Standard (Advanced if enterprise SLAs require); security groups least privilege; VPC endpoints; IMDSv2; DNSSEC on public zones; CAA records | — | Config rules; WAF logs |
| SC-17 | Backup and DR | Aurora PITR 35 days + Global Database to ap-south-2; AWS Backup vault lock; S3 CRR incl. Object Lock; **RPO ≤ 15 min, RTO ≤ 2 h** (master §11; Q-R3); monthly restore test; quarterly DR drill (P14 FR-P14-11) | — | `eng.dr_drills` |
| SC-18 | Incident response | P14 §5.1 lifecycle; severity matrix; on-call 24×7; RB-04/RB-06/RB-07/RB-10/RB-12; tabletop twice a year (one privacy breach with multi-jurisdiction fan-out per §2.5); forensic readiness (snapshot automation, chain-of-custody per ISO/IEC 27037) | — | IR tickets; tabletop minutes |
| SC-19 | BCP | ISO 22301-aligned business impact analysis (§3.3); alternate operations across Delhi, Noida and Jaipur offices plus remote; manual fallbacks; crisis communications; annual BCP exercise | — | BIA, exercise report |
| SC-20 | Physical (offices) | Badge access, visitor log, CCTV (30-day retention), clear-desk, locked storage for any paper originals pending scan, secure disposal (certificate) — data-centre controls inherited from AWS (SOC 2/ISO reports reviewed annually) | — | Access logs; AWS Artifact report review record |
| SC-21 | HR security | Background verification before access (identity, education, employment, address, criminal record check where lawful and consented); NDA and acceptable-use e-sign at onboarding; disciplinary process; exit checklist | — | HRMS export |
| SC-22 | Capacity and resilience | Autoscaling policies; load-test gates (P14 FR-P14-10); capacity review monthly; dependency circuit breakers (`provider_routing`) | — | Grafana capacity report |

### 3.3 Business continuity — critical processes

| Process | Max tolerable disruption | RTO / RPO | Manual fallback |
|---|---|---|---|
| Statutory clock alerts (NN-04) | 4 h | 1 h / 15 min | Daily encrypted export (06:00 IST) of all clocks due in next 30 days to registrar and deputy registrar (offline-readable, password via separate channel); manual phone/e-mail alerts |
| Scheduled hearings | duration of session | 30 min (failover to secondary video provider per `VIDEO_PORT`) | Tribunal-approved audio bridge; adjournment order template without loss of clocks |
| Filing and response deadlines for parties | 24 h | 2 h / 15 min | Registrar accepts e-mail filing to a monitored address with hash acknowledgement; later ingest via evidence pipeline |
| Notices and service | 24 h | 4 h / 15 min | Speed post via `POSTAL_PORT` manual booking |
| Payments and payouts | 48 h | 4 h / 0 (provider is system of record) | Payment links on fallback provider; payouts deferred |
| Award/settlement signing | 48 h | 4 h | Wet-ink counterpart with later upload (except where e-sign is mandatory by rule) |

---

## 4. PCI DSS v4.0.1 readiness — SAQ A boundary (NN-31)

### 4.1 Boundary

```mermaid
flowchart LR
  subgraph EQ["Equator systems (out of CDE)"]
    W["/pay/{intentId} page (Next.js, minimal scripts, CSP)"]
    API["payments module (Orders API, webhooks)"]
    DB[("core.payments: payment_id, order_id, method, last4, network, issuer, token_ref")]
  end
  subgraph RZP["Razorpay (PCI DSS Level 1 TPSP) — CDE"]
    CJS["checkout.js + hosted checkout iframe/redirect"]
    PG["Card processing, tokenisation (CoFT), 3DS/AFA"]
  end
  Payer((Payer browser / app)) -->|loads| W
  W -->|loads script| CJS
  Payer -->|card data typed only into| CJS
  CJS --> PG
  API -->|create order (amount, receipt) - no card data| PG
  PG -->|signed webhook: payment.captured| API
  API --> DB
```

| In scope of Equator's SAQ A | Out of scope (never present) |
|---|---|
| Web pages that launch the payment (`/pay/*`, fee screens that open checkout), their hosting (CloudFront/ALB/ECS `web`), and the scripts they load | PAN, CVV/CVC, expiry, track data, PIN — never entered, stored, logged or transmitted by Equator |
| Mobile app screens that invoke the Razorpay Standard Checkout SDK | Custom card forms, S2S card APIs, card-saving on Equator side |
| Payment links and e-mails/WhatsApp messages that carry Razorpay-hosted payment-link URLs | Any phone/IVR/voice-agent capture of card details (voice agents are prohibited from asking for card data — script policy + transcript PAN scrubbing) |
| Admin users who can change payment-page code or checkout configuration | UPI, netbanking, wallets (not card data; outside PCI DSS) |
| Third-party service provider management (Razorpay, Cashfree, PayPal AoCs) | Escrow and payout rails (RazorpayX/Castler — no card data) |

**Guardrail:** feature flag `payments.custom_checkout.enabled` is **permanently OFF** and listed in `core.feature_flags` as `locked=true`; enabling it requires a Board-level decision and moving to SAQ A-EP or SAQ D (ADR). Any API payload, form schema or log line matching a PAN pattern is rejected (`CARD_DATA_FORBIDDEN`).

### 4.2 Integration rules (P05 FR-P05-14 extended)

1. Web: Razorpay **Standard Checkout** (checkout.js opening the Razorpay-hosted iframe/modal) or Razorpay-hosted Payment Pages/Links. Mobile: Razorpay React Native/Expo Standard Checkout SDK (renders Razorpay's UI) **[VERIFY — open (vendor): no public Razorpay statement found (22 Oct 2026); until written confirmation, mobile uses hosted Payment Links in the system browser]**. Fallback Cashfree hosted checkout; international: Razorpay International hosted checkout or PayPal hosted buttons.
2. Store only: `provider`, `order_id`, `payment_id`, `method`, `card_network`, `card_last4`, `card_issuer` (for display/reconciliation as permitted by RBI CoFT), `token_id` where Razorpay creates a token on the customer's explicit consent with AFA (saved-card UX is Razorpay-hosted), `amount_minor`, `currency`, status, timestamps. Column CHECK: `card_last4 ~ '^[0-9]{4}$'`.
3. Recurring: UPI AutoPay / e-mandates via provider-hosted authorisation (RBI e-mandate framework; AFA above ₹15,000 per debit; pre-debit notice — NN-29, LR-PAY-003).
4. Webhooks: signature verification (`X-Razorpay-Signature`), idempotent inbox (P00 FR-P00-24); amounts computed server-side (P14 threat model).
5. Refunds and chargebacks via provider APIs by `payment_id` — no card data needed.

### 4.3 SAQ A requirement checklist and Equator evidence

Requirement list as applicable to SAQ A for PCI DSS v4.0.1 (January 2025 revision) (SAQ A Jan 2025 revision effective 31 Mar 2025 — PCI SSC blog 30 Jan 2025) **[VERIFY — open (vendor): line items against the SAQ A version in force on the assessment date]**:

| Req. | Requirement (summary) | Equator implementation | Evidence |
|---|---|---|---|
| 2.2.2 | Vendor default accounts managed | No vendor defaults on web tier; IaC baselines | Config scan |
| 3.1.1 / 3.2.1 | Data-retention policies; no storage of account data after authorisation | No-card-data policy; PAN detectors (§4.6) | Policy; Macie/DLP reports |
| 6.3.1 | Vulnerabilities identified and ranked | SC-11 | Scan reports |
| 6.3.3 | Critical/high security patches within one month | SC-11 SLAs | Patch reports |
| 8.2.1, 8.2.2, 8.2.5 | Unique IDs; shared IDs only by exception; terminated users revoked | SC-01, SC-04 | JML evidence |
| 8.3.1, 8.3.5–8.3.7, 8.3.9, 8.3.10.1 | Authentication factors, password rules, history, change on compromise | SC-02/03 (passkeys, MFA) for admins of payment pages | IdP policy export |
| 9.4.x | Paper media with account data protected/destroyed | No paper card data accepted; clear-desk | Policy |
| 11.3.2, 11.3.2.1 | Quarterly external vulnerability scans by a PCI SSC Approved Scanning Vendor (ASV) and after significant change | ASV scans of payment-initiating hosts | ASV passing reports |
| 12.8.1–12.8.5 | TPSP list, written agreements, due diligence, annual PCI status monitoring, responsibility matrix | `eng.processors` with AoC dates; Razorpay/Cashfree/PayPal AoCs; responsibility matrix (Razorpay 12.9 statement) | Annual vendor review |
| 12.10.1 | Incident response plan | SC-18 with card-data-specific playbook (suspected skimming → disable checkout route, switch to payment links) | IR plan |
| Eligibility | Site not susceptible to script attacks affecting the e-commerce system | §4.4 controls | Script inventory, tamper-detection logs |

### 4.4 Script integrity on payment-initiating pages (Decision Q-D1)

| Control | Implementation | Frequency / alert |
|---|---|---|
| PC-SEC-PAY-01 Page isolation | `/pay/[intentId]` route renders only first-party bundle + Razorpay checkout.js; **no** analytics, tag manager, chat widget, A/B testing, ad pixels, third-party fonts; same rule for fee-payment modals in portals (they navigate to `/pay`) | CI test fails if any non-allow-listed `<script src>` appears on `/pay/*` |
| PC-SEC-PAY-02 Script authorisation and inventory (6.4.3-equivalent) | `security/payment-scripts.yaml`: every script (first-party chunk hash, `https://checkout.razorpay.com/v1/checkout.js` and its loaded frames) with owner and business justification; CSP `script-src 'self' 'nonce-…' https://checkout.razorpay.com; frame-src https://api.razorpay.com https://checkout.razorpay.com; connect-src 'self' https://api.razorpay.com` **[VERIFY — open (vendor): no public Razorpay CSP list (22 Oct 2026) — derive from report-only CSP on staging and confirm with Razorpay support]**; **SRI** on first-party scripts; checkout.js cannot carry SRI (provider updates it in place) → allowed by origin with documented justification | Inventory reviewed monthly and on every change; CSP violation reports (`report-to`) alert security on-call |
| PC-SEC-PAY-03 Change and tamper detection (11.6.1-equivalent) | Synthetic monitor (Playwright in ap-south-1) loads `/pay/test-intent` every 15 minutes, records the HTTP security headers and the full list of executed scripts/frames with hashes (first-party) and origins (third-party); diff against the approved baseline | Alert to security on-call on any unapproved change; weekly report to GRC (meets "at least weekly") |
| PC-SEC-PAY-04 Admin change control | Only `release_manager` pipeline deploys `web`; payment-route files under CODEOWNERS (security + payments lead); no runtime tag injection | PR evidence |

### 4.5 RBI card-on-file and payment-data rules

- From 1 Oct 2022 no entity in the card transaction chain other than issuers and networks may store actual card data; merchants keep only tokens created with explicit consent and AFA, last four digits and issuer name (RBI CoFT circular RBI/2021-22/96, CO.DPSS.POLC.No.S-516/02-14-003/2021-22, 7 Sep 2021; read with the PA Directions 2025) [Verified 22 Oct 2026: rbi.org.in]. Equator never builds saved-card storage; Razorpay's tokenisation flow is used if saved cards are offered.
- RBI "Storage of Payment System Data" (RBI/2017-18/153, 6 Apr 2018): payment system data stored only in India — obligation on payment system operators (Razorpay); Equator's payment metadata is in ap-south-1 regardless.
- Settlement sums between parties never touch Equator's merchant account (NN-13; LR-PAY-001).

### 4.6 PAN-in-content handling (Decision Q-D2)

Detector: regex for 13–19 digit sequences (with spaces/dashes) + Luhn check + IIN range table; runs on (a) uploads in quarantine (OCR text layer and embedded text), (b) chat/messages, (c) form free-text, (d) voice transcripts, (e) AI gateway inputs. Outcomes: (a) upload → `CARD_DATA_DETECTED_IN_UPLOAD`; user is shown a masked copy (first 6/last 4 retained only if needed for a card-dispute narrative, else last 4 only) to approve as their submission; unmasked file destroyed by quarantine lifecycle (≤ 24 h) — never hashed into the evidence ledger; (b)–(e) masked before persistence; event `equator.documents.card_data.blocked.v1` with no PAN. FIN credit-card disputes ask for the card's last four digits only (V1 forms).

### 4.7 Annual cycle

Q1: ASV scan, SAQ A self-assessment with Attestation of Compliance signed by an officer, collection of TPSP AoCs (Razorpay, Cashfree, PayPal); Q2–Q4: quarterly ASV scans, monthly script-inventory review. If the acquirer/PA requests a different SAQ or an onsite assessment, Equator responds through the PA. Indicative cost: ASV ₹50,000–₹2,00,000 a year; internal effort 10–15 person-days **[VERIFY — quotes]**.

---

## 5. SOC 2 — Type I → Type II plan

### 5.1 Framework and scope

- **Criteria:** AICPA Trust Services Criteria (TSC) 2017 with revised points of focus (2022); description criteria DC 200; report under AICPA attestation standards (AT-C sections 105 and 205) issued by a **licensed CPA firm** [K]. A report issued by a firm that is not a licensed CPA firm is not a SOC 2 report and is not accepted as evidence (NN-17 Claims Register check).
- **Categories in scope (R-19 brief):** Security (CC1–CC9, mandatory) + Availability (A1) + Confidentiality (C1) + Processing Integrity (PI1 — fee computation, clocks, case-state transitions, award/settlement generation) + Privacy (P1–P8 — mapped to PC-xx). **Decision Q-D4:** all five categories from Type I, so that Type II needs no re-scoping; Privacy testing reuses DPDP/GDPR evidence.
- **System boundary:** Equator ODR platform (web, mobile, APIs, workers), its AWS accounts (ap-south-1/2), Keycloak, sealed stores, supporting processes (HR, change, incident, vendor) in Delhi, Noida and Jaipur. Carved-out subservice organisations: AWS, Razorpay, Leegality/Digio, LiveKit, Exotel, Gupshup/Meta, Sarvam, Amazon Bedrock — with complementary subservice organisation controls (CSOCs) listed and their SOC/ISO reports reviewed annually. Complementary user entity controls (CUECs) for tenants: SSO/MFA on their IdP, timely user deprovisioning, lawful basis for data they upload, safe handling of exports.
- **Excluded:** Equator ADR Institute (separate entity), marketing CMS content quality.

### 5.2 Timeline (L = production go-live; aligned with P14 FR-P14-09)

| Window | Activity | Exit evidence |
|---|---|---|
| L − 90 d → L | Readiness: GRC tool live with integrations; policies approved (§6.6); control owners assigned; gap assessment by the chosen auditor or an independent readiness firm (not the auditor if it would impair independence) | Gap report; remediation plan |
| L → L + 120 d | Remediate; Type I fieldwork at a point in time ≈ L + 100 d; report ≤ L + 120 d | SOC 2 Type I report (all five categories) |
| L + 120 d → L + 300 d | **Type II observation period 6 months** (first period); continuous evidence via GRC; monthly control-health review | — |
| L + 300 d → L + 345 d | Type II fieldwork and report | SOC 2 Type II report |
| thereafter | 12-month periods, contiguous; bridge letter issued by Equator management for gaps between period end and report date | Annual Type II; SOC 3 (general-use) report for the website |

Public claims only after issuance and registration in `growth.claims_register` with expiry = period end + 12 months (NN-17); interim copy "Controls designed to the AICPA Trust Services Criteria; SOC 2 examination in progress" only after the engagement letter is signed.

### 5.3 Control list mapped to platform features

| TSC | Criteria (summary) | Equator controls | Platform feature / evidence source |
|---|---|---|---|
| CC1.1–CC1.5 | Integrity and ethics; board oversight; structure; competence; accountability | Code of Conduct (staff, neutrals — Appendix N); Board/Institutional Committee charters (D2-15); org chart; SC-21; PC-37 | HRMS, LMS exports; Board minutes (CS) |
| CC2.1–CC2.3 | Information quality; internal and external communication | Policies portal; status page (SCR-P14-10); security.txt/VDP; tenant notices; sub-processor page (PC-22) | CMS versions; status page history |
| CC3.1–CC3.4 | Objectives; risk identification incl. fraud; change-driven risk | Risk register `eng.risks` (§7.2); STRIDE threat models (P14 FR-P14-01); DPIA (PC-25); fraud risks (fee manipulation, award back-dating, allocation tampering) | Risk register exports; threat models |
| CC4.1–CC4.2 | Monitoring; deficiency communication | Control-health dashboard (§7); internal audit (ISO 27001 cl. 9.2); management review | GRC test results; IA reports |
| CC5.1–CC5.3 | Control activities; technology general controls; policies | Policy set (§6.6); maker–checker (NN-21); SC baseline | Ruleset Studio approvals; policy acknowledgements |
| CC6.1 | Logical access security software, infrastructure, architecture | RLS + ABAC, KMS (SC-05/06), sealed stores | RLS lint (P00 FR-P00-15); KMS config |
| CC6.2–CC6.3 | User registration, authorisation, modification, removal | SC-01, P01 memberships, quarterly reviews (P14 FR-P14-21) | `eng.access_reviews` |
| CC6.4 | Physical access | SC-20; AWS carve-out | Office access logs |
| CC6.5 | Disposal of assets/data | PC-18 erasure certificates; SC-20 device disposal | Erasure certificates |
| CC6.6 | Boundary protection | SC-16 WAF, egress allow-list | WAF/Config exports |
| CC6.7 | Data transmission and movement | SC-07; Disclosure Register (PC-20); transfer register (PC-23) | TLS reports; disclosures |
| CC6.8 | Malicious software prevention | ClamAV on uploads (P00 FR-P00-21); EDR (SC-15); signed images (SC-13) | Scan logs; MDM report |
| CC7.1 | Configuration and vulnerability detection | SC-11, AWS Config, drift detection (P00 FR-P00-06) | `eng.vulnerabilities` |
| CC7.2 | Anomaly monitoring | SC-09/SC-10 SIEM detections; SLO alerts | Detection test log |
| CC7.3–CC7.5 | Incident evaluation, response, recovery | SC-18; P14 §5.1; RB-04; PC-31/32 | `eng.incidents`, PIRs |
| CC8.1 | Change management | §7.3 change management; CI gates; CAB for high-risk | PR + deploy logs |
| CC9.1 | Business disruption risk mitigation | SC-17, SC-19; insurance (P14 FR-P14-16(8)) | DR drills; BIA |
| CC9.2 | Vendor and business-partner risk | PC-21/22; `eng.processors` | Vendor reviews |
| A1.1 | Capacity planning | SC-22; k6 (P14 FR-P14-10) | `eng.perf_runs` |
| A1.2 | Environmental protections, backups, recovery infrastructure | SC-17; multi-AZ; Aurora Global DB | Backup job logs |
| A1.3 | Recovery plan testing | Quarterly DR drill; monthly restore | `eng.dr_drills` |
| C1.1 | Identify and maintain confidential information | Classification `standard`/`high`/`sealed` + `SEALED_ADR` information class (S8-FR-20); NN-11 caucus sealing | Data catalogue tags |
| C1.2 | Dispose of confidential information | PC-18; crypto-shred for sealed | Erasure certificates |
| PI1.1 | Specifications of processing (inputs, outputs) | Published fee schedules (Appendix B), rules of procedure, clock definitions (Appendix A/G) — versioned, pinned (NN-21) | Ruleset versions |
| PI1.2 | Input completeness/accuracy | Form-engine validation, idempotency keys, bulk row reconciliation (RB-03) | Validation reports |
| PI1.3 | Processing integrity | Deterministic rules engine (`packages/rules`, 100% branch coverage), clock engine (NN-04), fee golden vectors, audit chain | CI coverage; NN tests |
| PI1.4 | Output completeness/accuracy and timeliness | Award/settlement maker–checker, e-sign/e-stamp verification, hash manifests (NN-10), notice delivery evidence | Evidence ledger |
| PI1.5 | Storage of inputs/outputs | Evidence ledger + Object Lock (NN-22) | Ledger verification job |
| P1.1 | Notice | PC-06 | Notice registry |
| P2.1 | Choice and consent | PC-07/08/33/34 | Consent ledger |
| P3.1–P3.2 | Collection limited; explicit consent for sensitive data | PC-16, PC-11 | Form lint; sealed consents |
| P4.1–P4.3 | Use, retention, disposal | PC-02, PC-18, PC-19 | Retention runs |
| P5.1–P5.2 | Access and correction | PC-12/13/17 | DSR metrics |
| P6.1–P6.7 | Disclosure to third parties, authorised disclosures, breach notifications, processor commitments, accounting of disclosures | PC-20, PC-21, PC-31/32 | Disclosure register; DPA register |
| P7.1 | Data quality | PC-17 | Correction logs |
| P8.1 | Inquiries, complaints, disputes monitoring | PC-15, PC-40 | Grievance metrics |

### 5.4 Evidence automation (GRC tool) and auditor selection

**GRC tool (Vanta-, Drata- or Sprinto-class) — selection criteria:** (1) evidence store residency in India or an acceptable DPA + transfer row (§2.6); (2) native integrations: AWS (all accounts), GitHub, Microsoft Entra ID (Microsoft 365, D3-04, D3-40; Google Workspace stays OFF), Keycloak (API or custom collector), Jira/Linear, Equator's own HRMS (`hr`, Appendix Z; D3-03) via API, or an external HRMS (Keka/Darwinbox/greytHR via API or CSV) only where a group company still uses one *(v3.1)*, MDM, LMS, Slack/Teams; (3) pre-built frameworks: SOC 2, ISO 27001:2022, 27701, 42001, PCI DSS (SAQ A), GDPR; (4) **custom frameworks** for DPDP Act + Rules 2025, CERT-In Directions 2022, RBI IT-outsourcing flow-downs, and Equator's NN rules; (5) API to push evidence from Equator's own collectors (§7) and pull control status into the Compliance Cockpit; (6) auditor portal accepted by shortlisted auditors; (7) trust-centre page that respects NN-17 (no unevidenced badges). Vendor feature claims are unverified **[VERIFY — open: RFP with demo against these 7 criteria]**. Indicative: ₹8–30 lakh a year depending on frameworks and headcount **[VERIFY — quotes]**.

**Auditor selection criteria:** licensed CPA firm with AICPA peer review and SOC practice; India delivery team with fintech/ODR or regulated-SaaS references; independence (no implementation or readiness consulting by the same firm that would impair independence); acceptance of GRC-tool evidence and sampling via the auditor portal; experience with carve-out reporting for AWS/Razorpay; ability to issue SOC 3; fees fixed per period; report delivery ≤ 6 weeks after period end. Shortlist three; decision recorded by ADR and Board note. Indicative fees: Type I ₹8–20 lakh; Type II ₹15–40 lakh per period **[VERIFY — quotes]**.

---

## 6. ISO certification roadmap

### 6.1 Standards, purpose and sequencing

| Standard | Edition | What it certifies | Equator need | Target (L-relative) | Indicative external cost / internal effort **[VERIFY — quotes]** |
|---|---|---|---|---|---|
| ISO/IEC **27001** | 2022 (+ Amd 1:2024 climate clauses 4.1/4.2) | ISMS; 93 Annex A controls (37 organisational, 8 people, 14 physical, 34 technological) | **Must** — enterprise RFPs, SPDI r.8 deemed reasonable security, RBI IT-outsourcing due diligence | Stage 1 ≤ L + 60 d; Stage 2 ≤ L + 150 d (P14) | Certification body ₹4–10 lakh (cycle year 1), surveillance ₹2–5 lakh/yr; 1.5 FTE for 6 months |
| ISO/IEC **27017** | 2015 | Cloud-specific controls (provider and customer) | Should — SaaS tenants | With 27001 surveillance 1 (≈ L + 12 m) as an extension/attestation | + ₹1.5–4 lakh |
| ISO/IEC **27018** | 2019 (revision status **[VERIFY]**) | PII protection for public-cloud PII processors | Should — Equator as processor for GRM/POSH/Chambers tenants | With 27017 | + ₹1.5–4 lakh |
| ISO/IEC **27701** | **2025** (standalone PIMS; transition from 2019 **[VERIFY — open (vendor): not relevant to a first certification — certify directly to 2025 edition; confirm CB accreditation scope]**) | Privacy information management (controller and processor) | Should — evidence for DPDP, GDPR Art. 24/28, enterprise DPAs | ≈ L + 12 m (with 27001 surveillance 1) | + ₹2–5 lakh; 0.5 FTE (DPO office) |
| ISO/IEC **42001** | 2023 | AI management system; Annex A 38 controls (A.2–A.10); AI impact assessment per ISO/IEC 42005:2025; CBs per ISO/IEC 42006:2025 | Should — AI agents, voice agents, Pleadings Studio; supports EU AI Act readiness | Certificate **before 2 Dec 2027** if any AI neutral-assist feature is to be used on EU-party matters; otherwise ≈ L + 15 m | ₹5–12 lakh; AI governance lead 0.5 FTE |
| ISO **22301** | 2019 (+ Amd 1:2024) | Business continuity management | Could — enterprise BCP clauses; hearings and clocks | ≈ L + 24 m | ₹3–7 lakh |
| ISO **9001** | 2015 (+ Amd 1:2024; revision expected 2026 **[VERIFY]**) | Quality management — case administration consistency | Could — institutional credibility, future MCI service-provider grading | ≈ L + 24 m | ₹1.5–4 lakh |
| ISO **37301** | 2021 | Compliance management system (certifiable) | Could — Legal Rules Register discipline; Infrabyx BestComply synergy | ≈ L + 30 m | ₹3–7 lakh |

Rules: (1) certification bodies accredited by NABCB or an IAF MLA signatory for the specific scheme (for 42001, accreditation to ISO/IEC 42006 where available); (2) **integrated management system** — one policy set, one risk method, one internal audit programme and one management review covering all standards (Annex SL harmonised structure); (3) no certification claim until the certificate is issued and registered in the Claims Register (NN-17); (4) the scope statement must match the SOC 2 system boundary to reuse evidence.

### 6.2 ISO/IEC 27001:2022 Annex A — owners and evidence

Owner codes: **CISO** (security lead), **SRE**, **TL** (tech lead/engineering), **DPO**, **CS** (Company Secretary/legal), **HR**, **FAC** (facilities/admin), **PM** (product), **RM** (release manager), **PRC** (procurement/compliance officer). "Auto" = collected by the GRC tool or Equator collectors (§7); "Man" = manual upload.

| Control | Title | Owner | Equator implementation | Evidence |
|---|---|---|---|---|
| 5.1 | Policies for information security | CISO | Policy set §6.6, Board-approved | Man: approved policies, acknowledgements (Auto) |
| 5.2 | Information security roles and responsibilities | CISO | RACI; role codes (master §1.5) | Man: RACI |
| 5.3 | Segregation of duties | CISO | Maker–checker (NN-21); no self-approval | Auto: config-change approvals |
| 5.4 | Management responsibilities | CS | Management review; Board risk visibility | Man: minutes |
| 5.5 | Contact with authorities | CS | CERT-In PoC, DPB, regulators register (PC-40) | Man: PoC record |
| 5.6 | Contact with special interest groups | CISO | CERT-In advisories, OWASP, DSCI membership | Man |
| 5.7 | Threat intelligence | CISO | CERT-In/CISA KEV feeds into SIEM | Auto: feed status |
| 5.8 | Information security in project management | PM | Threat-model and DPIA gates in epics | Auto: PR template checks |
| 5.9 | Inventory of information and associated assets | SRE | IaC tags, data catalogue, SBOM | Auto: AWS Config, SBOM |
| 5.10 | Acceptable use | HR | AUP e-signed | Auto: HRMS |
| 5.11 | Return of assets | HR | Exit checklist, MDM wipe | Auto: MDM |
| 5.12 | Classification of information | DPO | `standard`/`high`/`sealed`, `SEALED_ADR` | Auto: schema tags |
| 5.13 | Labelling of information | DPO | Watermarks, document banners, PDF metadata | Auto: render tests |
| 5.14 | Information transfer | DPO | Disclosure register; transfer register; SFTP/TLS | Auto |
| 5.15 | Access control | CISO | ABAC policy engine | Auto: policy tests |
| 5.16 | Identity management | CISO | Keycloak + workforce IdP; SCIM | Auto |
| 5.17 | Authentication information | CISO | Passkeys, MFA, secret rules | Auto: IdP config |
| 5.18 | Access rights | CISO | Quarterly reviews | Auto: `eng.access_reviews` |
| 5.19 | Information security in supplier relationships | PRC | `eng.processors` risk tiers | Auto |
| 5.20 | Addressing security within supplier agreements | CS | DPA + security schedule | Man: signed DPAs |
| 5.21 | Managing security in the ICT supply chain | TL | SC-13 | Auto: SBOM/signatures |
| 5.22 | Monitoring, review and change of supplier services | PRC | Annual review; sub-processor changes | Auto: review tickets |
| 5.23 | Information security for use of cloud services | SRE | AWS shared-responsibility matrix; SCPs | Auto: Security Hub |
| 5.24 | Incident management planning and preparation | CISO | IR plan, runbooks RB-04…RB-14 | Man: plan; Auto: rehearsal log |
| 5.25 | Assessment and decision on events | CISO | Triage with severity matrix | Auto: `eng.incidents` |
| 5.26 | Response to incidents | CISO | P14 §5.1 | Auto |
| 5.27 | Learning from incidents | CISO | PIR ≤ 5 working days | Auto: PIR records |
| 5.28 | Collection of evidence | CISO | Forensic snapshots, hash chain (ISO/IEC 27037) | Auto |
| 5.29 | Information security during disruption | SRE | DR runbook keeps controls on in ap-south-2 | Auto: DR drill |
| 5.30 | ICT readiness for business continuity | SRE | SC-17/19 | Auto |
| 5.31 | Legal, statutory, regulatory and contractual requirements | CS | Legal Rules Register (Appendix G); obligations register | Auto: register status |
| 5.32 | Intellectual property rights | CS | Licence inventory (SBOM licences), content rights | Auto: licence scan |
| 5.33 | Protection of records | CS | Retention schedule, Object Lock | Auto |
| 5.34 | Privacy and protection of PII | DPO | PC-01…PC-40 | Auto/Man |
| 5.35 | Independent review of information security | CS | Internal audit; VAPT; SOC 2 | Man: reports |
| 5.36 | Compliance with policies and standards | CISO | Control-health dashboard | Auto |
| 5.37 | Documented operating procedures | SRE | Runbooks in `docs/runbooks/` | Auto: repo |
| 6.1 | Screening | HR | Background verification (SC-21) | Auto: HRMS |
| 6.2 | Terms and conditions of employment | HR | Security clauses in contracts | Man |
| 6.3 | Awareness, education and training | HR | Annual training + phishing simulation | Auto: LMS |
| 6.4 | Disciplinary process | HR | Policy | Man |
| 6.5 | Responsibilities after termination | HR | Exit NDA reminders; access removal ≤ 4 h | Auto |
| 6.6 | Confidentiality or non-disclosure agreements | CS | NDAs (staff, neutrals, vendors, auditors) | Auto: e-sign records |
| 6.7 | Remote working | CISO | MDM, device posture, VPN-less zero trust | Auto: MDM |
| 6.8 | Information security event reporting | CISO | Report button, security@ mailbox | Auto: tickets |
| 7.1 | Physical security perimeters | FAC | Office perimeters (Delhi, Noida, Jaipur) | Man |
| 7.2 | Physical entry | FAC | Badge system, visitor log | Man/Auto |
| 7.3 | Securing offices, rooms and facilities | FAC | Restricted room for paper originals | Man |
| 7.4 | Physical security monitoring | FAC | CCTV 30 days | Man |
| 7.5 | Protecting against physical and environmental threats | FAC | Fire/flood controls; AWS inherited | Man |
| 7.6 | Working in secure areas | FAC | Rules for records room | Man |
| 7.7 | Clear desk and clear screen | HR | Policy + 5-min lock (MDM) | Auto: MDM |
| 7.8 | Equipment siting and protection | FAC | Office network gear secured | Man |
| 7.9 | Security of assets off-premises | CISO | Encrypted laptops, MDM | Auto |
| 7.10 | Storage media | CISO | USB blocked for sealed-access users | Auto: MDM |
| 7.11 | Supporting utilities | FAC | UPS for office; AWS inherited | Man |
| 7.12 | Cabling security | FAC | Office cabling | Man |
| 7.13 | Equipment maintenance | FAC | Asset maintenance log | Man |
| 7.14 | Secure disposal or re-use of equipment | FAC | Wipe certificate | Man |
| 8.1 | User endpoint devices | CISO | SC-15 | Auto |
| 8.2 | Privileged access rights | CISO | SC-04 | Auto |
| 8.3 | Information access restriction | TL | RLS, ABAC, sealed stores | Auto: RLS lint |
| 8.4 | Access to source code | TL | GitHub org SSO, branch protection | Auto |
| 8.5 | Secure authentication | CISO | SC-02/03 | Auto |
| 8.6 | Capacity management | SRE | SC-22 | Auto |
| 8.7 | Protection against malware | CISO | ClamAV, EDR | Auto |
| 8.8 | Management of technical vulnerabilities | CISO | SC-11, VAPT | Auto |
| 8.9 | Configuration management | SRE | Terraform, drift detection | Auto |
| 8.10 | Information deletion | DPO | PC-18 | Auto |
| 8.11 | Data masking | TL | Masked display; synthetic test data | Auto |
| 8.12 | Data leakage prevention | CISO | SC-14 | Auto |
| 8.13 | Information backup | SRE | AWS Backup, PITR | Auto |
| 8.14 | Redundancy of information processing facilities | SRE | Multi-AZ, ap-south-2 | Auto |
| 8.15 | Logging | SRE | SC-09 | Auto |
| 8.16 | Monitoring activities | CISO | SC-10 | Auto |
| 8.17 | Clock synchronisation | SRE | NIC/NPL NTP, drift alert | Auto |
| 8.18 | Use of privileged utility programs | SRE | SSM only; no shells in images | Auto |
| 8.19 | Installation of software on operational systems | RM | Immutable images, admission policy | Auto |
| 8.20 | Networks security | SRE | SC-16 | Auto |
| 8.21 | Security of network services | SRE | WAF, CloudFront, TLS policies | Auto |
| 8.22 | Segregation of networks | SRE | Account/VPC separation; sealed subnet | Auto |
| 8.23 | Web filtering | CISO | Workforce DNS filtering; egress allow-list | Auto |
| 8.24 | Use of cryptography | CISO | SC-05/06/07 | Auto |
| 8.25 | Secure development life cycle | TL | SC-12 | Auto |
| 8.26 | Application security requirements | TL | ASVS 5.0.0 matrix | Auto |
| 8.27 | Secure system architecture and engineering principles | TL | ADRs; zero-trust principles §3.1 | Man/Auto |
| 8.28 | Secure coding | TL | Semgrep rules, reviews | Auto |
| 8.29 | Security testing in development and acceptance | TL | SAST/DAST/API Top 10 suite | Auto |
| 8.30 | Outsourced development | PRC | Contract clauses, code review of vendor code | Man |
| 8.31 | Separation of development, test and production | SRE | Separate AWS accounts; no prod data in non-prod | Auto |
| 8.32 | Change management | RM | §7.3 | Auto |
| 8.33 | Test information | TL | Synthetic data generator; prod-data detector | Auto |
| 8.34 | Protection of information systems during audit testing | CISO | VAPT in staging; time-bound `auditor` grants | Auto |

Statement of Applicability: all 93 controls applicable (none excluded; physical controls apply to offices, data-centre aspects inherited from AWS and documented).

### 6.3 ISO/IEC 27701 (PIMS) — additions

Controller and processor control sets map one-to-one onto PC-01…PC-40 (DPO owns). Deliverables: PIMS scope (controller for L1, processor for L2/L4/L5), PII-specific risk assessment, records of processing (PC-03), DPIA procedure (PC-25), processor contracts (PC-21), transfer procedure (PC-23), DSR procedure (PC-12/13).

### 6.4 ISO/IEC 42001 (AIMS) — AI governance and impact assessments

| Clause / Annex A area | Equator implementation |
|---|---|
| AI policy (A.2) | Published AI Governance Rule (P11 FR-P11-36) + internal AI Management Policy |
| Internal organisation (A.3) | AI Oversight sub-committee (D2-15); AI governance lead; roles for prompt owners and evaluators |
| Resources for AI systems (A.4) | AI system register (§2.11) incl. models, data, tooling, compute (Bedrock India) |
| Assessing impacts (A.5) | AI impact assessment per register row (ISO/IEC 42005-aligned): affected persons (parties, neutrals), fairness across languages and verticals, NN-01 boundary tests, misuse scenarios |
| AI system life cycle (A.6) | Prompt registry, eval gates (P11 FR-P11-39/40), red-team (FR-P11-41), change control for prompts/models |
| Data for AI systems (A.7) | No training on case data (FR-P11-17); corpus provenance (FR-P11-14); sealed exclusion |
| Information for interested parties (A.8) | ADM notice (§2.11), party disclosures (FR-P11-37), neutral guidance (FR-P11-38) |
| Use of AI systems (A.9) | Human-review invariant (FR-P11-12), kill switches (FR-P11-05), deterministic fallback (NN-02) |
| Third-party relationships (A.10) | LLM/voice vendor DPAs, no-training and retention terms (§2.7) |

### 6.5 ISO 22301, 9001, 37301 — scope notes

ISO 22301: BIA (§3.3), BC strategy, exercises, crisis communications. ISO 9001: quality objectives tied to P14 KPIs (scrutiny turnaround, clock compliance, notice delivery), customer complaints (Appendix N complaints), nonconformity and corrective action using `eng.incidents`/PIRs. ISO 37301: compliance obligations register = Appendix G Legal Rules Register + contractual obligations (`core.compliance_obligations`), compliance risk assessment, speak-up channel, compliance function independence (CS reporting to the Board).

### 6.6 Policy documents to be drafted by management (names only)

1. Information Security Policy · 2. Acceptable Use Policy · 3. Access Control Policy · 4. Authentication and Password Standard · 5. Cryptography and Key Management Policy · 6. Information Classification and Handling Policy · 7. Personal Data Protection Policy (internal) · 8. External Privacy Notices (set per §2.3a) · 9. Cookie Policy · 10. Data Retention and Disposal Schedule · 11. Records of Processing Procedure · 12. Data Protection Impact Assessment Procedure · 13. Data Subject Rights Procedure · 14. Personal Data Breach Response Procedure · 15. Cross-Border Transfer and Transfer Impact Assessment Procedure · 16. Processor and Sub-processor Management Procedure · 17. Children's and Guardians' Data Procedure · 18. Sealed Data Access and Break-Glass Procedure · 19. Confidentiality of Proceedings (Sealed-ADR) Policy · 20. Disclosure Register and Information Sharing Procedure · 21. Legal Hold Policy · 22. Incident Response Plan · 23. Business Continuity Policy and Plan · 24. Disaster Recovery Plan · 25. Backup Policy · 26. Change Management Policy · 27. Secure Development Policy · 28. Vulnerability and Patch Management Policy · 29. Logging and Monitoring Standard · 30. Asset Management Policy · 31. Cloud Security Standard · 32. Network Security Standard · 33. Secrets Management Standard · 34. Endpoint and Mobile Device Management Standard · 35. Remote Working Policy · 36. Clear Desk and Clear Screen Policy · 37. Physical and Environmental Security Policy · 38. Human Resources Security Policy (screening, onboarding, exit) · 39. Security and Privacy Awareness Training Policy · 40. Supplier Security and Privacy Policy · 41. Payment Card Data Policy (no-card-data) · 42. Penetration Testing and Vulnerability Disclosure Policy · 43. Test Data and Data Masking Standard · 44. Capacity Management Procedure · 45. Threat Intelligence Procedure · 46. Risk Management Policy and Methodology · 47. Internal Audit Charter and Programme · 48. Management Review Procedure · 49. Document and Record Control Procedure · 50. AI Management Policy · 51. AI Impact Assessment Procedure · 52. Model and Prompt Change Control Procedure · 53. Compliance Obligations Management Procedure · 54. Speak-Up (Whistle-blower) Policy · 55. Staff Code of Conduct and Disciplinary Policy · 56. Quality Manual and Case Administration Quality Procedure · 57. Customer Complaints Handling Procedure.

---

## 7. Compliance-as-code and evidence trail

### 7.1 Control IDs in code

- **Control library file** `compliance/controls.yaml` (source of truth, versioned): `id` (`PC-xx`, `SC-xx`, `PC-SEC-PAY-xx`, `NN-xx`), title, owner role, frameworks (`iso27001: [A.8.15]`, `soc2: [CC7.2]`, `dpdp: [r.6(1)(e)]`, `gdpr: [Art.32]`, `pci_saq_a: [12.10.1]`, `iso42001: [A.6]`), test refs, evidence collectors, frequency. Loaded into `eng.controls` by migration; GRC tool synced through its API.
- **Code annotations**: TypeScript decorator `@Control('PC-13','A.5.34','P5.1')` on service methods that implement a control; Terraform modules carry `# control: SC-05 A.8.24 CC6.1` comments and resource tags `eq:control=SC-05`; Semgrep rule fails CI when a file under `apps/api/src/{consent,payments,audit}` changes without an existing annotation; `pnpm controls:report` builds `docs/compliance/controls-coverage.md` (control → code locations → tests).
- **Policy as code**: Checkov custom policies and OPA/Conftest rules for Terraform (`policies/terraform/*.rego`) — e.g., S3 buckets must block public access (SC-16), Object Lock compliance mode on evidence (NN-22), KMS rotation (SC-05), region allow-list (§8); Kyverno/admission policies for signed images (SC-13); Cerbos/OPA authorisation policies under test (PC-29).
- **NN tests are controls**: every `NN-xx_*` test is linked to the control that it proves; a red NN test marks the control `failing` (release blocker, master §3).

### 7.2 Tables (additive; `eng` schema in the core database — X-50, X-65; RLS assurance roles only; never case content)

```sql
CREATE TABLE eng.controls (
  id text PRIMARY KEY,                                  -- 'PC-13', 'SC-05', 'PC-SEC-PAY-03'
  title text NOT NULL, owner_role text NOT NULL, frameworks jsonb NOT NULL,
  frequency text NOT NULL CHECK (frequency IN ('continuous','daily','weekly','monthly','quarterly','annual','event')),
  automated boolean NOT NULL, status text NOT NULL DEFAULT 'designed'
    CHECK (status IN ('designed','implemented','operating','failing','retired')),
  last_evaluated_at timestamptz, version int NOT NULL DEFAULT 1);
CREATE TABLE eng.control_tests (
  id uuid PRIMARY KEY DEFAULT uuidv7(), control_id text NOT NULL REFERENCES eng.controls(id),
  test_ref text NOT NULL,                               -- CI test name, collector ID or manual procedure ID
  kind text NOT NULL CHECK (kind IN ('ci_test','collector','manual')), UNIQUE (control_id, test_ref));
CREATE TABLE eng.control_evidence (
  id uuid PRIMARY KEY DEFAULT uuidv7(), control_id text NOT NULL REFERENCES eng.controls(id),
  period_start date NOT NULL, period_end date NOT NULL, collected_at timestamptz NOT NULL DEFAULT now(),
  collected_by text NOT NULL CHECK (collected_by IN ('collector','grc_tool','human')), collector_id text,
  result text NOT NULL CHECK (result IN ('pass','fail','exception','not_applicable')),
  artefact_uri text NOT NULL, artefact_sha256 char(64) NOT NULL, exception_ref uuid,
  CHECK (artefact_uri LIKE 's3://eq-%-evidence/compliance/%'));
CREATE TABLE eng.risks (
  id uuid PRIMARY KEY DEFAULT uuidv7(), title text NOT NULL, source text NOT NULL,   -- threat_model | dpia | audit | incident | vendor
  likelihood int NOT NULL CHECK (likelihood BETWEEN 1 AND 5), impact int NOT NULL CHECK (impact BETWEEN 1 AND 5),
  owner_role text NOT NULL, treatment text NOT NULL CHECK (treatment IN ('mitigate','accept','transfer','avoid')),
  control_ids text[] NOT NULL DEFAULT '{}', residual int, board_visible boolean GENERATED ALWAYS AS (residual >= 12) STORED,
  review_due date NOT NULL, status text NOT NULL);
CREATE TABLE eng.policy_documents (
  id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL, title text NOT NULL, version text NOT NULL,
  owner_role text NOT NULL, approved_by text NOT NULL, approved_on date NOT NULL, next_review date NOT NULL,
  document_id uuid NOT NULL, UNIQUE (code, version));
```

Evidence artefacts are written to `s3://eq-prod-evidence/compliance/{control_id}/{yyyy-mm}/…` under Object Lock (governance mode, 7 years) and hashed into the platform audit chain (`equator.eng.control.evidence_collected.v1`).

### 7.3 Automated evidence capture, change management and access reviews

| Collector (Temporal `ControlEvidenceWorkflow`, cron per frequency) | Control(s) | Output |
|---|---|---|
| `aws_config_snapshot` | SC-05, SC-16, SC-17, §8 region guard | Config compliance JSON |
| `idp_mfa_coverage` | SC-03 | CSV of users × MFA factors |
| `access_review_campaign` (quarterly; P14 `AccessReviewCampaign`) | SC-01/04, PC-29 | Reviewer decisions, revocations ≤ 5 working days |
| `ci_gate_summary` (per release) | SC-12, SC-13, CC8.1 | SAST/SCA/IaC/secret results + SBOM digest + cosign verification |
| `change_record_export` | CC8.1, A.8.32 | PR ↔ ticket ↔ deploy linkage; emergency changes with retro-approval ≤ 2 working days |
| `log_retention_probe` (monthly) | PC-30, CERT-In | Restore of oldest log object (≥ 179 days and ≥ 364 days) |
| `ntp_drift_report` (daily) | LR-CERTIN-003, A.8.17 | Max drift per node |
| `dsr_sla_report` (weekly) | PC-13 | SLA attainment by law |
| `retention_run_report` | PC-18 | Erasure certificate hashes |
| `processor_review_due` (monthly) | PC-21 | Overdue reviews |
| `payment_page_monitor` (15 min; weekly roll-up) | PC-SEC-PAY-03 | Script/header baseline diffs |
| `audit_chain_verify` (P00 FR-P00-19) | NN-22, PI1.5 | Verification result |
| `dr_drill_report` | A1.3, A.5.30 | RPO/RTO measured |
| `training_completion` | PC-37, A.6.3 | LMS export |

**Change management:** every production change has a PR, linked ticket, risk class (`standard`, `normal`, `high`, `emergency`); `high` (auth, payments, sealed, rules engine, RLS, KMS, AI policy) needs a second approver from security or the module owner plus a CAB note; emergency changes deploy with one approver and are retro-reviewed within 2 working days; configuration changes go through Ruleset Studio maker–checker (NN-21). **Access reviews:** quarterly for workforce, neutrals, enterprise admins and machine identities; monthly for privileged roles and sealed-data roles; reviewer cannot review own access; un-actioned items auto-revoke after 10 working days. **Audit logs:** NN-22 hash chain + `audit.access_log`; auditors get time-bound `auditor` grants (`eq_readonly_audit`) to evidence and audit views — never to case content.

**Control health:** a control is `failing` when its latest evidence is `fail` or older than 1.5× its frequency (`CONTROL_EVIDENCE_STALE`); failing NN-linked or PCI controls page security on-call; others open a ticket. The Compliance Cockpit (SCR-P14-01) gains a "Controls" tab (by framework, owner, status).

---

## 8. Data residency and multi-region

### 8.1 Default: India

All production personal data is stored and processed in AWS **ap-south-1** (Mumbai) with DR in **ap-south-2** (Hyderabad) (NN-15; P00 FR-P00-04 SCP region deny). Exceptions are allowed only through a transfer-register row (§2.6) and are minimised:

| Flow | Location of processing | Data | Control |
|---|---|---|---|
| LLM (Claude via Bedrock) | India in-country inference (ap-south-1/2) | prompts minimised and PII-redacted (P11 FR-P11-04) | `ai.anthropic_direct.enabled` OFF (would be a foreign transfer) |
| WhatsApp (Meta Cloud API) | Local storage IN for data at rest; transient processing abroad (≤ 60 min) [V RES_A4] | message content | transfer row `META_WHATSAPP`; minimal content in templates |
| Push (Expo/FCM/APNs) | Outside India | device token + content-free or minimal payloads | sealed/committee events content-free (Appendix S FR-P12-V2-07) |
| Voice (ElevenLabs) | India residency (Enterprise) | call audio/transcripts | contract must name India residency |
| GA4 | Outside India | pseudonymous web analytics (consented) | §2.9; Q-R7 |
| PayPal / Razorpay International | Outside India for foreign card schemes | payer details for INT payments | TPSP AoC; transfer row |
| Email to foreign parties | Recipient's provider | notice content | transmission at party's request (contract necessity) |
| GRC tool, paging, status page | Per vendor | staff identities, evidence metadata (no case content) | vendor selection criterion (§5.4) |

### 8.2 EU/UK (and SG/AE) party data in INT matters

1. **Storage stays in India** at launch; `intl.eu_data_region.enabled` (OFF) reserves an EU region (eu-central-1) for a future enterprise demand — enabling it requires an ADR, SCP change, separate KMS keys, a data-residency attribute on `core.tenants` (`data_region`) and a DPIA; it is not a GDPR requirement.
2. **Before the first EU/UK-targeted marketing or EUR price page goes live:** EU and UK representatives appointed (PC-24); EU/UK notices active (§2.3a); EU SCC Module 1/2 and UK IDTA/Addendum templates approved for counterparties that export to Equator; TIA approved; `intl.eu_targeting.enabled` ON only when all four are recorded (`EU_REPRESENTATIVE_REQUIRED`).
3. **Per case** (INT gate G3 extended, Appendix G LR-INT-012/013 sequence): resolver adds `EU`/`UK`/`SG`/`AE` to `core.cases.privacy_jurisdictions`; the case cannot move to `accepted` until (a) a transfer-register row covers each inbound flow, (b) the GDPR Art. 6/9 bases are recorded for each EU party's data categories (`intl.cases.gdpr_basis`, Appendix F F.8), (c) the EU-party AI mode is set (§2.11), (d) the parties have received the EU/UK notice.
4. **Special categories**: FAM `regime_resolver` religion/community data for EU-resident parties is Art. 9 data → Art. 9(2)(f) (legal claims) or explicit consent recorded; minimised to the derived regime (D2-03). Criminal-offence data (Art. 10) is limited to the existence, reference and status of related proceedings where NN-24 permits the civil dimension (e.g., NI Act s.138 compounding papers); any other criminal-offence material is quarantined for registrar review.
5. **Rights and breaches** run under §2.4/§2.5 with the GDPR clocks; correspondence with EU SAs goes through the representative where useful.
6. **Singapore**: TLO satisfied by contractual clauses in the submission agreement and Equator's DPA (PDP Regulations 2021); **UAE**: onshore PDPL transfer conditions (Arts 22–23) assessed per case **[VERIFY — Executive Regulations]**; DIFC/ADGM parties → their transfer safeguards (adequacy lists of those regimes may not include India — use their standard clauses).
7. **Sanctions/KYC data** for INT (NN-19) stays in India; screening provider calls carry minimal identifiers.

---

## 9. Acceptance tests

```gherkin
Feature: Privacy, security and certification readiness (Appendix Q)

  Scenario: Q-01 NN-30_jurisdiction_resolver_applies_strictest_when_unresolved
    Given a party with an Indian mobile number and no verified address
    And the party's case counterparty is established in Germany
    When the jurisdiction resolver runs
    Then the case privacy_jurisdictions contain "IN" and "EU"
    And the party receives notice "eqr.notice.in.v2" and the case transfer check requires an EU transfer-register row

  Scenario: Q-02 NN-30_eu_notice_required_before_capture
    Given a person whose privacy_jurisdictions contain "EU"
    When a consent capture surface references a notice with jurisdiction "IN" only
    Then the capture is rejected with code "VALIDATION_FAILED" and rule "PRIVACY_NOTICE_JURISDICTION_MISMATCH"

  Scenario: Q-03 NN-30_dsr_due_date_is_strictest_of_law_and_internal
    Given an EU resident files an access request on 1 March 2027
    Then statutory_due_at is 1 April 2027 and internal_due_at is 31 March 2027
    And due_at is 31 March 2027
    And an acknowledgement is sent within 48 hours

  Scenario: Q-04 NN-30_ccpa_opt_out_immediate
    Given CCPA mode is ON
    When a California consumer submits "opt_out_sale_share"
    Then the request is confirmed within 24 hours
    And the response states that Equator does not sell or share personal information

  Scenario: Q-05 NN-30_gpc_signal_blocks_third_party_analytics
    Given a browser sends "Sec-GPC: 1" to a marketing page
    When the page loads
    Then no request is made to any Google Analytics or advertising domain
    And the banner shows "Global Privacy Control signal honoured"

  Scenario: Q-06 NN-30_no_non_essential_cookie_before_consent
    Given a first-time visitor from any country
    When the home page loads and the visitor takes no action
    Then only cookies in category "strictly_necessary" are set
    And "Reject all" is displayed with equal prominence to "Accept all"

  Scenario: Q-07 NN-30_breach_fan_out_multi_jurisdiction
    Given an incident affecting 800 principals in India, 40 in Germany and 600 in Singapore is declared with aware_at 10:00 IST on day 1
    And CERT-In noticed_at is 09:30 IST on day 1
    Then regulatory notifications exist for "cert_in" due 15:30 IST day 1, "dpb" intimation due 10:00 IST day 2 and report due 10:00 IST day 4, "eu_sa" due 10:00 IST day 4
    And the "sg_pdpc" notification is due 3 calendar days after assessed_notifiable_at

  Scenario: Q-08 NN-30_regulated_tenant_notified_within_2_hours
    Given an incident affecting data of an NBFC tenant is declared
    Then a "regulated_tenant" notification is due within 2 hours of declaration

  Scenario: Q-09 NN-30_transfer_register_gate_for_int_case
    Given an INT case with a Singapore respondent and no transfer-register row covering "INT_SG_PARTY_SUBMISSIONS"
    When the registrar attempts to accept the case
    Then the transition fails with code "DPDP_TRANSFER_BASIS_MISSING"

  Scenario: Q-10 NN-30_subprocessor_requires_signed_dpa
    Given processor "NewVendor" has dpa_status "sent"
    When an admin enables a provider_routing row for "NewVendor"
    Then the change is rejected with code "SUBPROCESSOR_NOT_APPROVED"

  Scenario: Q-11 NN-30_subprocessor_change_notice_30_days
    Given a new sub-processor change is recorded on 1 June 2027
    Then its effective_at cannot be earlier than 1 July 2027
    And every tenant admin and subscriber receives the notice on 1 June 2027

  Scenario: Q-12 NN-30_ai_feature_requires_register_row
    Given AI feature flag "ai.case_summariser" has no eng.ai_system_register row
    When an admin turns the flag ON
    Then the change is rejected with code "AI_SYSTEM_NOT_REGISTERED"

  Scenario: Q-13 NN-01_eu_party_mode_limits_ai
    Given an INT case whose privacy_jurisdictions contain "EU"
    And "ai.eu_neutral_assist.enabled" is OFF
    When the neutral requests an AI summary of the evidence bundle
    Then the request is refused with code "AI_FEATURE_DISABLED_FOR_EU_PARTY"
    And translation of a party document remains available

  Scenario: Q-14 NN-31_no_card_fields_on_equator_pages
    When the payment page /pay/{intentId} is rendered
    Then the DOM contains no input of type text, tel or number whose name or autocomplete matches card number, expiry or CVV
    And the only third-party script origin is "https://checkout.razorpay.com"

  Scenario: Q-15 NN-31_card_number_in_api_payload_rejected
    Given a request body to any /v1 endpoint contains a Luhn-valid 16-digit number in a free-text field
    Then the response is 422 with code "CARD_DATA_FORBIDDEN"
    And the logged request body contains the number masked to its last 4 digits

  Scenario: Q-16 NN-31_card_image_upload_never_becomes_evidence
    Given a party uploads a photo of a debit card showing the full card number
    When the quarantine scan runs
    Then the upload is held with code "CARD_DATA_DETECTED_IN_UPLOAD"
    And the party is offered a masked copy to approve
    And no evidence_ledger row references the unmasked file
    And the unmasked object is deleted within 24 hours

  Scenario: Q-17 PCI_payment_page_tamper_detected
    Given the approved baseline for /pay/test-intent lists two scripts
    When a deployment adds a third-party script to the page
    Then the synthetic monitor raises an alert within 15 minutes
    And CI had already failed the build for an unapproved script on /pay/*

  Scenario: Q-18 NN-30_logs_retained_400_days_in_india
    When the log_retention_probe runs
    Then it restores a 364-day-old CloudTrail object from the ap-south-1 log archive
    And Object Lock retention on that object is at least 400 days from creation

  Scenario: Q-19 compliance_control_stale_evidence_fails_control
    Given control "SC-03" has frequency "weekly" and its latest evidence is 11 days old
    Then eng.controls status for "SC-03" is "failing" with reason "CONTROL_EVIDENCE_STALE"

  Scenario: Q-20 NN-17_no_soc2_claim_before_report
    Given no SOC 2 report is registered in growth.claims_register
    When a CMS editor publishes text containing "SOC 2 Type II"
    Then publishing is blocked with code "CLAIM_NOT_EVIDENCED"

  Scenario: Q-21 NN-30_eu_targeting_blocked_without_representative
    Given tenant.legal_entity.eu_representative is empty
    When an admin turns ON "intl.eu_targeting.enabled"
    Then the change is rejected with code "EU_REPRESENTATIVE_REQUIRED"

  Scenario: Q-22 NN-30_minor_analytics_dropped_and_guardian_required
    Given a learner aged 16 registers for an Academy course
    Then the account remains "pending_guardian" until a verified adult guardian consents
    And no product analytics event is stored for the learner

  Scenario: Q-23 NN-30_form_field_without_purpose_cannot_publish
    Given a form schema draft adds field "spouse_religion" without purpose_code
    When the schema is submitted for approval
    Then publication is blocked with code "FORM_FIELD_PURPOSE_MISSING"

  Scenario: Q-24 NN-30_erasure_certificate_written
    When the retention workflow erases 1,200 expired marketing leads
    Then an erasure certificate document is generated
    And its SHA-256 appears in an audit event of action "retention.erasure_completed"

  Scenario: Q-25 DSR queue order and pauses never move the statutory date (v3.1)
    Given an access request A received 26 days ago under DPDP with internal SLA 30 days and a request B received today
    Then A appears above B in the DPO queue
    When A is paused for "awaiting_identity"
    Then internal_due_at changes and statutory_due_at does not
```

---

## 10. Open items and counsel questions

1. Resolved (22 Oct 2026): G.S.R. 843(E) commenced s.44(1) and (3) on 13 Nov 2025; s.44(2) (omission of IT Act s.43A) commences 13 May 2027, so s.43A and the SPDI Rules apply until then; LR-DPDP-001 corrected.
2. **[VERIFY — open (counsel; short exposure — s.43A omitted 13 May 2027 per G.S.R. 843(E))]** SPDI r.8: acceptance of ISO/IEC 27001:2022 certification as the "IS/ISO/IEC 27001" deemed standard until s.43A is omitted (S8 §8 Q16).
3. **[VERIFY — open]** GDPR Art. 3(2) trigger point for INT marketing (EUR pricing, EU-language pages) and whether Equator's processing is "occasional" for the Art. 27(2)(a) exemption; whether FAM religion data of EU-resident diaspora parties is large-scale Art. 9 processing (S8 §8 Q11).
4. **[VERIFY — open]** EU AI Act: whether neutral-assist features used on EU-party matters make Equator a provider of an Annex III 8(a) system or fall within Art. 6(3); whether Art. 27 FRIA applies to a private ADR body (S8 §8 Q12).
5. **[VERIFY — open (watch; Executive Regulations not found 22 Oct 2026)]** UAE PDPL Executive Regulations status; DIFC/ADGM breach periods and transfer safeguards to India (S8 §8 Q13).
6. **[VERIFY — open]** CCPA: confirm Equator is not a "business"; service-provider terms for California-headquartered enterprise tenants; 2027 CPI adjustment of the revenue threshold; California breach-notification day limits (SB 446, 2025) (S8 §8 Q14).
7. Resolved (22 Oct 2026; SI 2026/82: ss.70, 80, 112 from 5 Feb 2026, s.103 from 19 Jun 2026): UK DUAA 2025 commencement of Arts 22A–22D, complaints-handling duty and cookie exemptions.
8. **[VERIFY — open (vendor: Razorpay/acquirer written evidence)]** PCI: SAQ A form version and line items on the assessment date; Razorpay responsibility matrix; SAQ A eligibility of the mobile SDK integration; PCI SSC guidance on substantiating the script-attack eligibility criterion; Razorpay CSP domain list.
9. Corrected (22 Oct 2026): CoFT = RBI/2021-22/96, 7 Sep 2021. **[VERIFY — open]** RBI CoFT circular number/date against the RBI website; PA Directions 2025 paragraphs on merchant card-data storage.
10. **[VERIFY — open (vendor, CB RFQ)]** ISO/IEC 27701:2025 transition deadline; ISO/IEC 27018 current edition; ISO 9001 revision timing; accreditation availability for ISO/IEC 42001 certification bodies in India (NABCB).
11. **[VERIFY — open (counsel): no DPDP standard; policy default all-party consent + re-identification test]** Anonymisation threshold for publication to fall outside DPDP (S8 §8 Q9) — drives PC-36.
12. **[VERIFY — open (counsel): recommended — tie KYC evidence to the case file retention class (Q-R4) rather than a free-standing 5 years]** KYC retention default (5 years) — Equator is not a PMLA reporting entity; counsel to confirm a defensible period.
13. All indicative costs and timelines in §4.7, §5.4 and §6.1 — obtain three quotes each before Board budget approval.

---

## Phase addendum (paste into P14)

**FR-P14-V2-01 — Control library live.** Load `compliance/controls.yaml` (PC-01…PC-40, SC-01…SC-22, PC-SEC-PAY-01…04, NN-01…NN-40 — NN-33 to NN-40 added in v3.0) into `eng.controls`/`eng.control_tests`; sync to the GRC tool; Compliance Cockpit "Controls" tab. *Acceptance:* every control has an owner, ≥ 1 test or collector and a framework mapping; Q-19 passes; coverage report `docs/compliance/controls-coverage.md` generated in CI.

**FR-P14-V2-02 — Evidence collectors.** Implement the 14 collectors in §7.3 as `ControlEvidenceWorkflow` schedules writing `eng.control_evidence` with Object Lock artefacts. *Acceptance:* each collector produced evidence at least once in staging and prod-like UAT; stale evidence flips the control to `failing`.

**FR-P14-V2-03 — Multi-law breach fan-out.** Extend `IncidentRegulatoryClockWorkflow` and `eng.regulatory_notifications` (Q-R6 values) to create one clock per recipient in §2.5 from `eng.incidents.jurisdictions` and `personal_data_involved`; record `aware_at` and `assessed_notifiable_at`. *Acceptance:* Q-07 and Q-08 pass; RB-04 tabletop includes an India + EU + Singapore scenario with timings recorded.

**FR-P14-V2-04 — DSR per-law SLAs.** Apply the §2.4 DDL delta (ADR for the CHECK change) and per-law due-date computation in `DsrSlaWorkflow`; public request form `/privacy/requests`. *Acceptance:* Q-03 and Q-04 pass; DSR KPI split by `law_code` on SCR-P14-04.

**FR-P14-V2-05 — Transfer register and INT gate.** `eng.transfer_register` with the seed rows of §8.1; INT case acceptance guard (§8.2 step 3). *Acceptance:* Q-09 passes; every non-India flow in §8.1 has an `approved` row before go-live or its feature is OFF.

**FR-P14-V2-06 — Processor and sub-processor programme.** `eng.processors`, `eng.processor_services`, `eng.subprocessor_changes`, public `/legal/sub-processors`; DPA template (§2.7). *Acceptance:* Q-10 and Q-11 pass; every enabled `provider_routing` provider has `dpa_status = 'signed'` and a review date.

**FR-P14-V2-07 — Retention schedule v2.** Add classes `outcome_instrument`, `liveness_media`, `breach_record`, `dsr_record`, `security_logs`, `neutral_applicant_unsuccessful`, `cctv_office` (Q-R4); erasure certificates. *Acceptance:* Q-24 passes; dry-run report shows no `outcome_instrument` row scheduled before 13 years.

**FR-P14-V2-08 — ISO 27001 Statement of Applicability v2.** SoA for all 93 Annex A controls with owners and evidence per §6.2; integrated management-system manual covering 27001 now and 27701/42001 later. *Acceptance:* internal audit 1 samples ≥ 30 Annex A controls with evidence links resolving; zero controls without owner.

**FR-P14-V2-09 — SOC 2 readiness.** System description draft (DC 200), CSOC/CUEC lists, TSC mapping table §5.3 in the GRC tool, auditor selection by ADR. *Acceptance:* readiness gap report with remediation dates; engagement letter signed before L; Type I fieldwork scheduled ≤ L + 100 d.

**FR-P14-V2-10 — PCI SAQ A pack.** SAQ A self-assessment draft, ASV onboarding and first passing scan of payment-initiating hosts, TPSP AoCs on file, script inventory and tamper monitor live (§4.3–§4.4). *Acceptance:* Q-14, Q-15, Q-17 pass; AoC signed by an officer before the first live card payment.

**FR-P14-V2-11 — Policy set.** The 57 policies in §6.6 drafted by management, approved (Board or delegated committee), registered in `eng.policy_documents`, acknowledged by staff. *Acceptance:* 100% of workforce acknowledgements for policies 1–3, 7, 22, 41 before go-live.

**FR-P14-V2-12 — Legal Rules Register additions.** Add the rows in §1.4 with status, source and reviewer; flags that depend on `UNVERIFIED` rows stay OFF. *Acceptance:* go/no-go check (P14 FR-P14-17) lists zero enabled features depending on an `UNVERIFIED` §1.4 row, except stricter-only controls.

**FR-P14-V2-13 — Certification roadmap and claims.** Roadmap §6.1 approved by the Board with budget; Claims Register entries prepared (inactive) for each certificate/report. *Acceptance:* Q-20 passes; no public page mentions ISO 27701, 42001, 22301, 9001, 37301 or SOC 2 status beyond the approved interim wording.

**FR-P14-V2-14 — EU/UK readiness gate.** Representatives, notices, SCC/IDTA templates and TIA recorded before `intl.eu_targeting.enabled` (§8.2). *Acceptance:* Q-21 passes.

## Phase addendum (paste into P00)

**FR-P00-V2-Q1 — Compliance-as-code scaffolding.** `compliance/controls.yaml`, `@Control()` decorator in `packages/domain`, Semgrep rule for annotated modules, Terraform `eq:control` tags, OPA/Conftest policies for SC-05/SC-16/region guard/Object Lock. *Acceptance:* CI fails when an un-annotated change touches `consent`, `payments` or `audit`; Conftest blocks a public S3 bucket in a test plan.

**FR-P00-V2-Q2 — Assurance tables (`eng`).** Migrations for `eng.controls`, `eng.control_tests`, `eng.control_evidence`, `eng.risks`, `eng.policy_documents`, `eng.transfer_register`, `eng.processors`, `eng.processor_services`, `eng.subprocessor_changes`, `eng.ai_system_register`, `eng.processing_purposes`, `eng.regulator_requests` with RLS (ops roles only) and RLS-lint coverage. *Acceptance:* `TEN-01` cross-tenant test and RLS lint pass; no case-content columns in `ops`.

**FR-P00-V2-Q3 — PII tagging and test-data guard.** Column comments `pii:<tier>;purpose:<code>` required on personal-data tables; migration fails on untagged columns; detector blocks prod-like identifiers in non-prod seeds. *Acceptance:* PC-38 CI check green on all migrations.

**FR-P00-V2-Q4 — PAN detector and card-data guard.** Shared Luhn + IIN detector in `packages/domain/security/pan.ts` used by the API body filter, log redaction middleware (P00 FR-P00-29) and the quarantine step (inserted into FR-P00-21 as new step 2a, after the ClamAV scan and before hashing). *Acceptance:* Q-15 and Q-16 pass; logging test shows masked PAN.

**FR-P00-V2-Q5 — Security baseline SC-01…SC-22.** Workforce IdP federation, IAM Identity Center JIT elevation, SSM-only access, SIEM pipeline with the §3.2 SC-10 detections, KMS key classes and BYOK modes, secrets rotation. *Acceptance:* evidence collectors for SC-03, SC-04, SC-05, SC-08, SC-09 return `pass` in staging.

**FR-P00-V2-Q6 — Jurisdiction columns.** `privacy_jurisdictions text[]` on `core.persons`, `core.organisations`, `core.cases`; resolver package `packages/rules/privacy/` with golden vectors. *Acceptance:* Q-01 passes.

## Phase addendum (paste into P05)

**FR-P05-V2-Q1 — SAQ A boundary.** Payment-initiating UI only through Razorpay Standard Checkout / hosted pages / payment links (web) and the Standard Checkout SDK (mobile); `/pay/[intentId]` isolated route; `payments.custom_checkout.enabled` locked OFF. *Acceptance:* Q-14 passes; a PR adding a card input anywhere fails the `no-card-fields` lint.

**FR-P05-V2-Q2 — Payment metadata only.** `core.payments` stores only the fields in §4.2(2) with `card_last4` CHECK; no column can hold a PAN (schema lint over column names and the PAN detector over sample data). *Acceptance:* Q-15 passes on payments endpoints and webhooks.

**FR-P05-V2-Q3 — Script integrity on payment pages.** CSP with nonces and the Razorpay origin allow-list, SRI on first-party scripts, `security/payment-scripts.yaml` inventory, synthetic tamper monitor (PC-SEC-PAY-01…04). *Acceptance:* Q-17 passes; weekly monitor report reaches the GRC tool.

**FR-P05-V2-Q4 — TPSP management.** Razorpay, Cashfree and PayPal recorded in `eng.processors` with AoC dates and responsibility matrices; annual review task. *Acceptance:* checkout cannot be enabled for a provider whose AoC is older than 13 months (`SUBPROCESSOR_NOT_APPROVED`).

**FR-P05-V2-Q5 — Voice and chat never take card data.** Voice-agent scripts and WhatsApp flows send payment links only; transcripts and messages pass the PAN detector before storage. *Acceptance:* red-team prompt "read me your card number" yields refusal + payment link; stored transcript contains no PAN.

## Phase addendum (paste into P01)

**FR-P01-V2-Q1 — Notices by jurisdiction.** `core.notices_privacy.jurisdiction` and the six variants of §2.3a; capture surfaces select by resolver output. *Acceptance:* Q-02 passes.

**FR-P01-V2-Q2 — Rights centre v2.** New DSR kinds (restriction, portability, objection, adm_review, opt_out_sale_share, limit_spi, know), requester kinds (guardian, nominee, authorised agent), export `POST /v1/me/exports`. *Acceptance:* Q-03 and Q-04 pass.

## Phase addendum (paste into P11)

**FR-P11-V2-Q1 — AI system register and EU-party mode.** `eng.ai_system_register` rows for every agent in master §9 and the Pleadings Studio; flags cannot turn ON without a row; `ai.eu_party_mode` auto-applies LR-INT-020 limits. *Acceptance:* Q-12 and Q-13 pass; ADM notice (§2.11) shown on every AI surface in en and hi.

## Phase addendum (paste into P13)

**FR-P13-V2-Q1 — First-party CMP and GPC.** Consent banner (global opt-in model, equal-prominence reject), `growth.cmp_receipts`, GPC handling and `/.well-known/gpc.json`, `/legal/sub-processors` page, GA4 gated per Q-R7. *Acceptance:* Q-05 and Q-06 pass; no analytics script on `/pay/*`, `/app`, `/verify` or case routes.
