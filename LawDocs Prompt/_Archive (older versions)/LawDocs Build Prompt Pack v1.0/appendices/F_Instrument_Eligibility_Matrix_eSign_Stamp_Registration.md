# Appendix F — Instrument Eligibility Matrix: eSign, Stamp and Registration

**Status:** Binding (row schema, decision codes, evaluation algorithm, locked rows). Matrix content is legal content under NN-30: each row is published, versioned and effective-dated through the P03 rule lifecycle with a reviewer of record; the rows in this appendix are the **seed set** and carry the verification status shown.
**Used by:** P03 (runs `IN.sgn.eligibility` and `IN.sgn.formalities`), P04 (health checks), P05 (classification tightening), P06 (template eligibility link and wet-ink pack), P07 (pre-sign gates), P08 (gate, stamp, formalities — owner), P10 (pleadings, affidavits, vakalatnama), P13 (governance documents), P14 (business-service filings), P15 (consumer claims), P16 (notary and registration-assistance services), P21 (public "Can I eSign this?" and stamp-duty tools).

**How to use.** Every executable document in LawDocs belongs to one **eligibility family** (`IF-xx`). A template carries its family in `tpl.template_version.eligibility_row_id` (P06); an uploaded document gets it from its P04 document type, confirmed by the user and tightened by P05 classification. Before any signing request, P08 evaluates the family's rows with the instrument's facts and the State; the decision fixes the permitted signing methods and the formalities that NN-40 tracks. A coding agent implements §3 (schema) and §8 (algorithm) exactly; content editors maintain §4–§7 as data. Nothing here is legal advice to users: user-facing explanations quote the row's plain-language text and citation. Where this appendix and R5's eSign flags disagree, this appendix governs (§9 lists the corrections). Where the law is unverified, the row says `[VERIFY]` and the P03 verification status decides what the row may do (NN-38).

---

## 1. Legal framework (summary for row authors)

| # | Instrument / provision | Effect on rows | Tag | Source |
|---|---|---|---|---|
| L1 | **IT Act 2000 s.1(4) read with the First Schedule**, as amended by **S.O. 4720(E) dated 26 Sep 2022** (Gazette publication 4 Oct 2022 [VERIFY: Gazette text and date — e-Gazette PDF not retrievable on 25 Oct 2026; LA-01]): entry 1 — negotiable instruments other than a cheque, or a demand promissory note/bill of exchange issued in favour of or endorsed by an entity regulated by RBI, NHB, SEBI, IRDAI or PFRDA; entry 2 — powers of attorney, except those empowering such a regulated entity to act for the executant; entry 3 — trusts as defined in s.3 of the Indian Trusts Act 1882; entry 4 — wills and other testamentary dispositions (s.2(h) Indian Succession Act 1925); entry 5 (contracts for sale or conveyance of immovable property) — **omitted** | Entries 1–4 → `WET_INK_ONLY` locked rows (with carve-outs); property contracts are no longer excluded by the IT Act — they are governed by stamp and registration law | [LAW] V-WEB (R3) and two independent secondary sources re-checked 25 Oct 2026 (Vinod Kothari, 12 Oct 2022; Leegality explainer); Gazette text pending (Appendix W §W.9 LA-01) | R3 LG-003 |
| L2 | **IT Act s.3A and Second Schedule** — eSign using Aadhaar e-KYC (G.S.R. 61(E), 27 Jan 2015) and other e-KYC services (S.O. 1119(E), 1 Mar 2019); **s.3** digital signatures (CA-issued DSC); **s.5** electronic signature satisfies a signature requirement; **s.10A** contracts formed electronically are not unenforceable for that reason alone | Methods `AADHAAR_OTP`, `AADHAAR_BIO`, `ACCOUNT_ESIGN`, `DSC` are signatures; `E_ACCEPTANCE` is contract formation evidence under s.10A, never labelled "eSign" | [LAW] V-WEB (titles) / [VERIFY wording] | LG-001, LG-002, LG-004 |
| L3 | **Bharatiya Sakshya Adhiniyam 2023** ss.61–63 (electronic records; s.63(4) certificate with hash, Part A and Part B per the Schedule); s.86 presumption for secure electronic records and signatures; ss.85, 87 [VERIFY wording] | Evidence notes per row; prefer s.3A methods for anything a user may need to prove | [LAW] V-SEC | LG-014, LG-090, LG-091 |
| L4 | **Indian Stamp Act 1899** s.3 (chargeability), **s.17** (stamp before or at execution), s.29 (who pays, subject to agreement), s.33 (impounding), **s.35** (inadmissible unless duty and penalty paid), s.2(14) "instrument" includes electronic records [VERIFY Finance Act 2019 amendment text]; **State Stamp Acts** and State amendments set articles and rates (e.g., Maharashtra Stamp Act 1958, Karnataka Stamp Act 1957, Rajasthan Stamp Act 1998; Indian Stamp Act as applied in UP and Delhi) | `STAMP_REQUIRED`; stamp-before-sign lock (NN-08); State variance through duty tables (§6) | [LAW] [VERIFY text] | LG-096, LG-097 |
| L5 | **e-Stamping**: SHCIL is the Central Record Keeping Agency in 23 States/UTs (Gujarat 2007 first; Meghalaya Nov 2021 latest per StockHolding 2022); ACCs (banks, FIs, licensed vendors, CSCs, co-operatives); State-specific routes (Kerala treasury e-stamp; Maharashtra SHCIL + GRAS + franking; Haryana SHCIL + Haryana Stamp (Payment of Duties by Means of Online E-Stamping) Rules 2017; Karnataka SHCIL with Kaveri); physical paper in some north-eastern States; platforms procure as the user's agent, not as sellers | State coverage registry (§5); agent-procurement route only (CH-13) | [LAW]/[INTERP] V-WEB/V-SEC; [VERIFY current list] | LG-098–LG-100 |
| L6 | **Registration Act 1908** s.17(1)(a)–(e) (compulsory: gifts of immovable property; non-testamentary instruments creating, declaring, assigning, limiting or extinguishing rights in immovable property of value ₹100 or more; leases from year to year, > 1 year or reserving yearly rent; etc.), **s.17(1A)** (contracts for transfer for consideration of immovable property for the purposes of TPA s.53A), s.17(3) (authorities to adopt not conferred by will), **s.18** (optional registration, incl. wills), **s.23** (presentation within four months of execution), ss.32–33 (presentation in person or by agent under a POA), ss.42–46 (deposit of wills) [VERIFY], **s.49** (effect of non-registration) | `REGISTRATION_REQUIRED` with conditions; four-month clock | [LAW] [VERIFY wording] | LG-104 |
| L7 | **Registration Bill 2025** (draft): electronic presentation, consent-based e-verification, adds agreements to sell, developer agreements, POAs for transfer, sale certificates, mortgage-by-deposit terms as compulsorily registrable | Pre-built `DRAFT` rows, never active until enacted | [INTERP] V-SEC [VERIFY status] | LG-105 |
| L8 | **Transfer of Property Act 1882**: s.3 ("attested" — two or more witnesses each of whom has seen the executant sign or received a personal acknowledgement); **s.54** (sale of tangible immovable property of value ₹100 or more only by registered instrument); s.53A (part performance); **s.58–59** (mortgage other than by deposit of title deeds securing ₹100 or more — registered instrument signed by the mortgagor and attested by at least two witnesses); **s.105–107** (lease; year-to-year or > 1 year or reserving yearly rent only by registered instrument); s.118 (exchange); **s.123** (gift of immovable property by registered instrument signed by the donor and attested by at least two witnesses) | Attestation counts and registration conditions; electronic attestation adequacy [COUNSEL] | [LAW] [VERIFY wording] | R3 §8; [VERIFY] |
| L9 | **Indian Succession Act 1925** s.2(h) (will), **s.63** (execution of unprivileged wills: signature by testator, attestation by two or more witnesses), s.70 (revocation) | Will rows: wet ink, two attesting witnesses | [LAW] [VERIFY wording] | LG-003 |
| L10 | **Indian Trusts Act 1882** s.3 (trust), **s.5** (trust of immovable property — non-testamentary instrument in writing, signed and registered; movable property — by such instrument or by transfer of ownership), s.1 (public or private religious or charitable endowments excluded) | Private trust deeds locked wet-ink; public/religious trusts conservative wet-ink under State trust law | [LAW] [VERIFY wording] / [INTERP] | — |
| L11 | **Powers-of-Attorney Act 1882** s.1A (definition), s.2 (execution by donee in own name); notarial authentication for use before courts/registrars (Notaries Act 1952 s.8 [VERIFY]); Registration Act s.33 | POA rows locked wet-ink except regulated-entity carve-out | [LAW] [VERIFY] | LG-003 |
| L12 | **Notaries Act 1952; Oaths Act 1969**; CPC Order XIX (affidavits); no operational e-notarisation located | Affidavits `DRAFT_APPROVAL_ONLY` + `NOTARY_REQUIRED` | [LAW] [VERIFY e-notarisation] | LG-106 |
| L13 | **CPC Order VI rr.14–15** (pleadings signed and verified by the party; affidavit in support where required) [VERIFY current text]; court e-filing rules on digital signatures (forum-specific) [VERIFY]; Court Fees Act 1870 and State Acts (court fee is not stamp duty) | Pleadings `FORUM_RULES` | [LAW] [VERIFY] | LG-093–LG-095 |
| L14 | **RERA 2016 s.13(1)** — promoter shall not accept more than ten per cent of the cost as advance without first entering into a written agreement for sale and registering it [VERIFY wording] | Agreement-for-sale rows in RERA projects: `REGISTRATION_REQUIRED` | [LAW] [VERIFY] | — |
| L15 | **Arbitration and Conciliation Act 1996 s.7** — arbitration agreement in writing, including an exchange of communications by electronic means (s.7(4)(b)) | Arbitration agreements `ESIGN_OK`/`E_ACCEPTANCE_OK`; stamping per State; consequences of non-stamping per the Supreme Court's 2023 seven-judge decision [VERIFY citation] | [LAW] / [VERIFY] | — |
| L16 | IP: **Copyright Act 1957 s.19** (assignment in writing signed by the assignor) and s.30 (licence in writing); **Patents Act 1970 s.68** (assignment/licence in writing, duly executed) and s.69 (registration of title); **Trade Marks Act 1999 s.45** (registration of assignment) | `ESIGN_OK` + `SPECIAL_LAW_STEP` (recordal) | [LAW] [VERIFY forms] | LG-170 |
| L17 | **Companies Act 2013** s.7 and SPICe+ (e-MoA/e-AoA with DSC) [VERIFY], **s.56** (transfer of securities — instrument of transfer in the prescribed form, stamped, executed by or on behalf of transferor and transferee) [VERIFY SH-4 practice], s.62(1)(b) (ESOP by special resolution), s.77 (registration of charges), s.118 (minutes; SS-1/SS-2 signature) [VERIFY electronic signature of minutes]; **LLP Act 2008** (LLP agreement filing) [VERIFY section]; **Indian Partnership Act 1932** s.58–59 (registration of firms), s.69 (effect of non-registration) | Corporate rows; governance minutes via `gov` (LDC SoR when present, NN-47) | [LAW] [VERIFY] | R3 §13 |
| L18 | **Motor Vehicles Act 1988 s.50** (transfer of ownership through the registering authority; Vahan Forms 29/30): s.50(1)(a) transferor reports within 14 days (same State); s.50(1)(b) within 45 days (registered in another State); transferee reports within 30 days; s.50(2) succession and public-auction cases within the prescribed period (CMVR r.56) [VERIFY current text; LA-03]; s.51 (hire-purchase endorsement) [VERIFY] | Vehicle sale: agreement ≠ transfer (CH-23) | [LAW] [VERIFY] | LG-107 |
| L19 | **Indian Contract Act 1872** s.10–11 (competence: minors cannot contract); **Hindu Adoptions and Maintenance Act 1956** s.16 (presumption for registered adoption deeds); **Juvenile Justice (Care and Protection of Children) Act 2015** and Adoption Regulations 2022 (orders by District Magistrate on the JJ route) [VERIFY] | Signer age rule; adoption rows | [LAW] [VERIFY] | R5 §5 |
| L20 | **Limitation Act 1963** s.18 (acknowledgement in writing signed by the party) and Schedule | Evidence notes; retention | [LAW] | LG-092 |

---

## 2. How to read the matrix

| Column | Meaning |
|---|---|
| **Code** | Eligibility family `IF-xx` (stable; never reused; superseded rows keep their code with a new version) |
| **Family (R5 / Appendix E IDs)** | Instruments in the family by canonical document ID from `R5_Document_Page_Inventory.csv` (D-codes) and the Pleadings inventory (P-codes); new templates are mapped when created |
| **eSign decision and methods** | Decision code (§3.2) and permitted methods (§3.3), with conditions in CEL (§3.4) where the decision depends on facts |
| **Stamp** | `STAMP_REQUIRED` (chargeable in every State), `STATE_VARIES` (chargeable in most States; article and rate per State table), `CHECK` (depends on facts, e.g., receipts above a threshold), `NOT_CHARGEABLE`; plus the canonical article code (§6.2) |
| **Registration** | `COMPULSORY`, `CONDITIONAL` (with condition), `OPTIONAL`, `NOT_REQUIRED`, `SPECIAL_RECORDAL` (non-Registration Act registry, e.g., Trade Marks Registry) |
| **Witness / notary** | Legal attestation requirement (count and source) vs customary witnesses; notarisation/oath requirement |
| **Special law and evidence notes** | Statutes beyond the IT/Stamp/Registration Acts; practical evidence notes |
| **Status** | P03 verification status of the row's operative facts: `VERIFIED`, `SECONDARY_ONLY`, `NOT_CONFIRMED` (P03 FR-P03-57); `LOCKED` marks protective rows that run regardless (R3 §17) |

---

## 3. Row schema and codes (binding for P03/P08)

### 3.1 Row fields (`rul` content kind `eligibility_row`, rule set `IN.sgn.eligibility`)

| Field | Type | Rule |
|---|---|---|
| `row_id` | string `IEM-<IF>-<nnn>` | Immutable; one family may have several rows (base row + conditional rows + State overrides) |
| `family` | `IF-xx` | Required |
| `instrument_ids[]` | D-/P- codes, `tpl_` IDs | Mapping maintained by P06; uploads map through P04 document types |
| `jurisdiction` | `IN` or `IN-<ST>` (ISO 3166-2:IN) | State rows override or add to `IN` rows (§8) |
| `condition` | CEL expression over facts (§3.4) | Empty = always applies |
| `esign_decision` | enum §3.2 | Required |
| `methods_permitted[]` | enum §3.3 | Must be consistent with the decision (validator) |
| `alt_route` | enum `WET_INK_PACK`, `NOTARY_PACK`, `REGISTRATION_PACK`, `FORUM_FILING`, `NONE` | Required when decision ≠ `ESIGN_OK`/`E_ACCEPTANCE_OK` |
| `flags[]` | enum §3.5 with parameters | E.g., `WITNESS_REQUIRED(2, LEGAL)` |
| `stamp` | `{ class, article_code, payer_default }` | `article_code` from §6.2 |
| `registration` | `{ class, condition, deadline_rule }` | `deadline_rule` e.g. `EXECUTION_PLUS_4_MONTHS` (Registration Act s.23) |
| `attestation` | `{ min_witnesses, mandatory_by_law, electronic_attestation_allowed }` | `electronic_attestation_allowed` defaults false where `mandatory_by_law` |
| `notary` | `REQUIRED`, `OPTIONAL`, `NOT_APPLICABLE` | — |
| `special_law[]` | `{ statute, provision, step_code }` | Creates `SPECIAL_LAW_STEP` formality items |
| `user_text` | i18n string ids | Plain-language explanation ("Why can't I eSign this?") and next steps; ≤ 60 words; reviewed |
| `citations[]` | `{ instrument, provision, url_ref, lg_id }` | ≥ 1; `LG-xxx` where available |
| `effect_class` | `protective` / `computational` / `permissive` | P03 FR-P03-56 |
| `verification_status` | `VERIFIED` / `SECONDARY_ONLY` / `NOT_CONFIRMED` | P03 FR-P03-57 |
| `locked` | bool | `true` for First Schedule rows and stamp-before-sign; tenants cannot overlay a relaxation |
| `effective_from`, `effective_to` | date | Gazette/notification dates; `effective_to` null while current |
| `version`, `supersedes_row_version` | semver | Lifecycle per P03 FR-P03-55 |
| `reviewer_of_record` | `prs_` of a `PLT_LEGAL_REVIEWER` (advocate/CS/CA with enrolment/membership number) | Not the maker (NN-30) |
| `counsel_ref` | doc reference | Required when the row carries `[COUNSEL]` in notes |
| `golden_cases[]` | fixture IDs | ≥ 1 positive and ≥ 1 negative (P03 FR-P03-58) |
| `next_review_due` | date | Default 180 days; 90 for `SECONDARY_ONLY`; 30 for volatile State tables |

### 3.2 Decision codes

| Code | Meaning | P08 behaviour |
|---|---|---|
| `ESIGN_OK` | Electronic signature lawful; no registration needed | All `methods_permitted` offered |
| `ESIGN_OK_REGISTRATION_ROUTE` | Electronic signature not excluded by the IT Act, but the instrument must be registered | Offered only if the State's registration route for eSigned instruments is `VERIFIED` (`IN-<ST>.registration.accepts_esigned = true`); otherwise P08 presents the registration pack and the decision behaves as `WET_INK_ONLY` with the explanation "Registration offices in <State> are not yet confirmed to accept electronically signed documents" |
| `DSC_OK` | Only DSC is appropriate (statutory e-forms, e-MoA/e-AoA) | DSC only |
| `E_ACCEPTANCE_OK` | Electronic acceptance (s.10A) sufficient; eSign optional | E-acceptance and eSign methods |
| `WET_INK_ONLY` | Excluded by the First Schedule, or execution must happen before a registering officer, or attestation by physically present witnesses is legally required | No electronic method; `alt_route` pack |
| `DRAFT_APPROVAL_ONLY` | Electronic approval of the draft only; the operative act is an oath, attestation or court act | E-acceptance "Approved for swearing/filing"; `NOTARY_PACK` or `FORUM_FILING` |
| `FORUM_RULES` | The forum's rules decide (pleadings, vakalatnama, statutory applications) | Methods from the P10 forum render profile; default wet ink |
| `NEEDS_CLASSIFICATION` | Family unknown or `eligibility_suspect` | No signing until a human classifies |

The P03 seed list (`ESIGN_OK`, `DSC_OK`, `WET_INK_ONLY`, `REGISTRATION_REQUIRED`, `NOTARY_REQUIRED`, `STAMP_REQUIRED`) and the P06 cached outcomes (`ESIGN_OK`, `ESIGN_OK_REGISTRATION_ROUTE`, `WET_INK_ONLY`) are subsets: the requirement-type values become flags (§3.5).

### 3.3 Methods

`AADHAAR_OTP`, `AADHAAR_BIO` (assisted counters only), `AADHAAR_FACE` (inactive until verified), `ACCOUNT_ESIGN` (eSign API 3.x), `DSC`, `E_ACCEPTANCE`, `WET_INK`. Tenants may remove methods from a row, never add (P08 FR-P08-19).

### 3.4 Facts available to conditions (CEL)

`instrument.immovable_property_interest` (bool), `instrument.creates_or_transfers_interest` (bool), `instrument.value_inr` (decimal), `instrument.market_value_inr`, `instrument.term_months` (int), `instrument.year_to_year` (bool), `instrument.reserves_yearly_rent` (bool), `instrument.possession_given` (bool), `instrument.rera_project` (bool), `instrument.movable_only` (bool), `instrument.records_past_arrangement` (bool), `instrument.court_proceeding` (bool), `party.counterparty_regulated_entity` (enum `RBI`, `NHB`, `SEBI`, `IRDAI`, `PFRDA`, `NONE`, verified by P01 KYB), `party.any_minor` (bool), `party.guardian_signing` (bool), `party.org_signatory` (bool), `state.execution`, `state.property`, `forum.profile_id`, `tenant.stricter_overlays[]`. Facts come from template answers (P06), document metadata (P04), extraction confirmed by a human (P05) or a short decision helper shown to the sender (P08 FR-P08-12). Unknown facts evaluate to the conservative branch (a condition that cannot be evaluated returns the stricter decision).

### 3.5 Flags

`STAMP_REQUIRED`, `REGISTRATION_REQUIRED(deadline)`, `NOTARY_REQUIRED`, `OATH_REQUIRED`, `WITNESS_REQUIRED(n, LEGAL|CUSTOMARY)`, `BOARD_APPROVAL_REQUIRED` (from tenant DoA rows, not from this appendix), `GUARDIAN_REQUIRED`, `SPECIAL_LAW_STEP(step_code)`, `RECORDAL_REQUIRED(registry)`, `COURT_FEE_SEPARATE`, `WELFARE_STAMP` (advocates' welfare fund stamp on vakalatnama [VERIFY]), `DELIVERY_PROOF_RECOMMENDED` (notices), `RETIRED_TEMPLATE`.

---

## 4. The matrix (seed rows)

Abbreviations: **eS** = Aadhaar OTP eSign + account-based eSign; **D** = DSC; **eA** = electronic acceptance; **W** = wet ink. "Cust." = customary (not legally required). Status column: L = `LOCKED`; V = `VERIFIED`; S = `SECONDARY_ONLY`; N = `NOT_CONFIRMED`.

### 4A. Commercial and corporate contracts

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-01 | General commercial agreements — business agreement D1.2.2, NDA D1.2.3, consultancy D1.2.4, statements of work D1.8.1–4, IT contracts D9.1.1–4, advertising D6.1.2, hotel and tourism D7.6.1–5, agency and broker D10.1.1–3, commission agent D1.3.1, dealership/distributorship D1.3.2–3, franchise D1.4.4, lawyer engagement D11.11.1–2 | `ESIGN_OK`; eS, D, eA (eA only if tenant enables for value ≤ `sgn.e_acceptance.max_value_inr`) | `STATE_VARIES` — `ART-AGREEMENT` | `NOT_REQUIRED` (unless a clause grants an interest in immovable property → IF-33/IF-36 rows apply to that instrument) | Cust. 2 witnesses; no notary | IT Act s.10A for formation; s.3A signature attracts BSA s.86 presumption; franchise/distribution with foreign party: FEMA reporting by parties [VERIFY]; lawyer engagement subject to BCI Rules (no fee-sharing) | S |
| IF-02 | Amendments, supplementary agreements, revocations and terminations — D1.2.1, D1.2.6, D1.3.6, D1.4.10, D3.6.6, D8.1.5, D8.2.3, D8.3.3, D10.1.4, D10.2.3, D10.4.5 | **Inherits** the base instrument's row (`inherits_base = true`): an amendment to a registered lease follows IF-33; an amendment to an NDA follows IF-01 | Inherits; supplementary instruments usually chargeable as agreement or per base article [VERIFY per State] | Inherits (amendment of a registered instrument affecting immovable property → registration) | Inherits | Link `AMENDS`/`TERMINATES` in P04; termination letters without new obligations may be `E_ACCEPTANCE_OK` | S |
| IF-03 | Joint ventures, collaborations, shareholders', founders', promoters', underwriting and brokerage agreements — D1.1.1–3, D4.2.1, D4.2.2, D4.2.4, D4.2.7, D5.4.2, D5.4.3 | `ESIGN_OK`; eS, D (company signatories usually D) | `STATE_VARIES` — `ART-AGREEMENT` | `NOT_REQUIRED`; `CONDITIONAL` if immovable property is contributed (condition `instrument.immovable_property_interest`) | Cust. | Articles of association may need amendment to give SHA rights effect (Companies Act) [INTERP]; foreign investment reporting by the company [VERIFY] | S |
| IF-04 | Share transfer — D1.1.4 (share purchase/transfer), D4.2.12 (indemnity for registration of shares) | SPA/indemnity: `ESIGN_OK` (eS, D). Instrument of transfer for physical shares (SH-4): `FORUM_RULES` — company/RTA practice; default W [VERIFY] | SPA: `STATE_VARIES`. Instrument of transfer: `STAMP_REQUIRED` — `ART-SHARE_TRANSFER` (duty on transfer of securities under the Indian Stamp Act as amended by Finance Act 2019 [VERIFY rate and collection mechanism]) | `NOT_REQUIRED` | SH-4: witness per form [VERIFY] | Companies Act s.56 [LAW] [VERIFY]; dematerialised transfers happen in the depository system, not by instrument | N |
| IF-05 | Allotment and ESOP documents — D1.1.5, D10.8.4 | Letters and grant agreements: `ESIGN_OK` (eS, D, eA for acceptance) | Grant/acceptance letters `CHECK` [VERIFY]; share certificates stamped per State [VERIFY] | `NOT_REQUIRED` | — | ESOP scheme needs special resolution (Companies Act s.62(1)(b)) → `BOARD_APPROVAL_REQUIRED` via `gov` | S |
| IF-06 | Memorandum and articles of association — D4.2.3 | `DSC_OK` (SPICe+ e-MoA/e-AoA signed by subscribers with DSC [VERIFY current MCA practice]) | `STATE_VARIES` — `ART-MEMORANDUM_ARTICLES`; paid through MCA for integrated States [VERIFY] | `SPECIAL_RECORDAL` (ROC incorporation) | Subscribers' witness per MCA form [VERIFY] | Companies Act s.7 [LAW]; LawDocs prepares, the authorised person files (NN-05, Ecosystem principle 11) | N |
| IF-07 | LLP agreement and LLP documents — D4.3.1, D4.3.2, D4.3.3, D4.3.4 | `ESIGN_OK` (eS, D); filing forms `DSC_OK` | `STATE_VARIES` — `ART-PARTNERSHIP` [VERIFY LLP article per State] | `SPECIAL_RECORDAL` (filing of LLP agreement with the Registrar within the prescribed time [VERIFY LLP Act section and period]) | Cust. | `SPECIAL_LAW_STEP(LLP_FORM_FILING)` | N |
| IF-08 | Partnership deeds and changes — D4.6.1–11, D5.3.1–3, D5.3.5 | `ESIGN_OK` (eS, D); `CONDITIONAL → REGISTRATION_ROUTE` where immovable property is brought in or relinquished (`instrument.immovable_property_interest`) [COUNSEL] | `STATE_VARIES` — `ART-PARTNERSHIP` (dissolution/retirement articles per State) | Deed: `NOT_REQUIRED` except condition; firm registration with the Registrar of Firms is separate and optional but affects suits (Partnership Act ss.58–59, 69) [LAW] | Cust. | Minor admitted to the benefits of partnership (D4.6.6): `GUARDIAN_REQUIRED` (Partnership Act s.30) [LAW]; partnership with HUF through karta | S |
| IF-09 | Corporate resolutions, consents, appointment letters, NOCs, declarations — D4.2.8, D4.2.10, D4.3.2, D4.7.1, D4.7.3, D4.1.3, D4.1.5 | `ESIGN_OK` / `E_ACCEPTANCE_OK` (letters); certified true copies of resolutions by director/CS with eS or D | `NOT_CHARGEABLE` (most); self-declarations used as affidavits → IF-46 | `NOT_REQUIRED` | — | Minutes and registers belong to `gov` (Companies Act s.118, SS-1/SS-2 signature rules [VERIFY electronic signing]); LDC is SoR when present (NN-47) | S |
| IF-10 | Society and club constitution — D4.1.2, D4.1.4 | `FORUM_RULES` (Registrar of Societies practice under the Societies Registration Act 1860 and State Acts) [VERIFY] | `STATE_VARIES` [VERIFY] | `SPECIAL_RECORDAL` (Registrar of Societies) | Signatures of subscribing members (≥ 7 under the 1860 Act [VERIFY State variants]) | Sale deed to members (D4.1.6) → IF-30 | N |
| IF-11 | Declaration of solvency — D4.2.11 | `DRAFT_APPROVAL_ONLY` (declaration verified by an affidavit for voluntary liquidation — IBC s.59(3)(a) [VERIFY]) | Affidavit article per State | `SPECIAL_RECORDAL` (filing with ROC/IBBI as applicable) [VERIFY] | `NOTARY_REQUIRED` | — | N |
| IF-12 | Listing agreements BSE/NSE — D4.2.5–6 | `RETIRED_TEMPLATE` — replaced by SEBI (LODR) Regulations 2015 (R5 §5); no new signing requests | — | — | — | Replace with LODR policy packs (P06) | V |

### 4B. Employment and HR

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-13 | Employment documents — offer D10.10.3, appointment D10.10.2, employment/contractual/job agreements D10.8.1–3, job application D10.10.1, resignation D10.4.4 | `ESIGN_OK`; eS, D (company side), eA (employee acceptance); bulk permitted (P08 §4G) | Offer/appointment letters `CHECK`; employment agreements `STATE_VARIES` — `ART-AGREEMENT` [VERIFY] | `NOT_REQUIRED` | — | Four Labour Codes in force 21 Nov 2025 (R5 §5); fixed-term employment terms per Code on Social Security/IR Code [VERIFY] | S |
| IF-14 | Disciplinary and separation communications — chargesheet D10.4.1, retrenchment notice D10.4.2, notice/warning D10.4.3, D10.4.6 | `ESIGN_OK` / `E_ACCEPTANCE_OK` (employer signs; employee acknowledges receipt, never "accepts" charges) | `NOT_CHARGEABLE` | `NOT_REQUIRED` | — | Retrenchment conditions and notices to appropriate Government under the IR Code 2020 [VERIFY sections]; `DELIVERY_PROOF_RECOMMENDED` | N |
| IF-15 | Apprenticeship — D10.2.1 (by guardian), D10.2.2 | `ESIGN_OK`; `GUARDIAN_REQUIRED` where apprentice is a minor (guardian signs) | `STATE_VARIES` [VERIFY] | `SPECIAL_RECORDAL` (registration of the contract of apprenticeship with the apprenticeship adviser/portal under the Apprentices Act 1961 [VERIFY]) | — | Indian Contract Act s.11 — minor cannot contract; guardian contracts as the Act permits [VERIFY] | N |
| IF-16 | Labour agreements — D10.11.1–3 | `ESIGN_OK` | `STATE_VARIES` | `NOT_REQUIRED` | — | Contract labour obligations under the OSH Code [VERIFY] | S |
| IF-17 | Memorandum of settlement in an industrial dispute — D10.11.4 | `FORUM_RULES` (settlement in the prescribed form signed by parties, copies to the conciliation officer/Government under the IR Code 2020 [VERIFY section and form]); default W | [VERIFY] | `SPECIAL_RECORDAL` (submission to authority) | Per prescribed form | — | N |

### 4C. Financial transactions

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-18 | Acknowledgements and receipts — D3.1.1–6, D3.11.1–4 | `E_ACCEPTANCE_OK` / `ESIGN_OK` | `CHECK` — receipts for money above the Schedule threshold attract a receipt stamp (`ART-RECEIPT`) [VERIFY threshold, State variants and treatment of electronic receipts]; acknowledgement of debt `STATE_VARIES` — `ART-ACKNOWLEDGEMENT` [VERIFY] | `NOT_REQUIRED` | — | Limitation Act s.18: written acknowledgement signed by the party extends limitation — prefer eS over eA for debt acknowledgements [INTERP] | N |
| IF-19 | Bonds, indemnities, guarantees — D3.2.1, D3.3.2–6, D3.8.1–7 | `ESIGN_OK`; eS, D | `STAMP_REQUIRED` — `ART-BOND` / `ART-INDEMNITY_BOND` / guarantee as `ART-AGREEMENT` per State [VERIFY] | `NOT_REQUIRED` | Cust. | Bank-format guarantees: issuing bank's own process | S |
| IF-20 | Administration bond — D3.3.1 | `FORUM_RULES` (bond required by the court granting letters of administration — Indian Succession Act [VERIFY section]) | Per court/State | `NOT_REQUIRED` | Sureties per court | Court format (P10) | N |
| IF-21 | Security over movables and credit facilities — pledge D3.7.1, D3.7.5, hypothecation D3.7.3, cash credit D3.7.2, LC/BG facilities D3.7.4 | `ESIGN_OK`; eS, D; NeSL digital document execution optional for lenders (R6 D-26) | `STAMP_REQUIRED` — `ART-PLEDGE_HYPOTHECATION` per State [VERIFY] | `NOT_REQUIRED` under the Registration Act; `SPECIAL_RECORDAL`: charge registration with ROC for company borrowers (Companies Act s.77) and CERSAI filing by the secured creditor where applicable [VERIFY] | Cust. | Lender-side filings are the lender's (Ecosystem principle 11) | S |
| IF-22 | Hire purchase — D3.6.1–4 | `ESIGN_OK` | `STATE_VARIES` — `ART-HIRE_PURCHASE` [VERIFY] | `NOT_REQUIRED`; vehicles: hire-purchase endorsement on the registration certificate through Vahan (MV Act s.51) [VERIFY] | Cust. | — | N |
| IF-23 | Promissory notes and bills of exchange — D3.10.1–4 | **`WET_INK_ONLY`** (First Schedule entry 1); **carve-out row**: `ESIGN_OK` where `party.counterparty_regulated_entity != NONE` (demand promissory note/bill in favour of or endorsed by an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity) | `STAMP_REQUIRED` — `ART-PROMISSORY_NOTE` (rates for bills of exchange, cheques and promissory notes are fixed by Parliament under the Indian Stamp Act [VERIFY]) | `NOT_REQUIRED` | — | Negotiable Instruments Act 1881; physical note must be produced in a suit | L |
| IF-24 | Cheque dishonour and legal notices — D3.5.1, D11.9.1–8, D11.10.1, D11.5.1, D11.5.4, D3.9.2, D1.2.5, D1.4.5, D1.4.9, D3.6.5, D8.1.4 | `ESIGN_OK` / `E_ACCEPTANCE_OK`; notices signed by the party or by an advocate in their own name (P10) | `NOT_CHARGEABLE` | `NOT_REQUIRED` | — | NI Act s.138(b): written demand within 30 days of receiving information of dishonour [LAW]; `DELIVERY_PROOF_RECOMMENDED` (speed post/RPAD; email/WhatsApp service accepted by courts in some contexts [VERIFY]) | S |
| IF-25 | Compromise and settlement — D1.2.7, D3.4.1, D3.4.3, D2.4.2 | `ESIGN_OK`; `CONDITIONAL → ESIGN_OK_REGISTRATION_ROUTE` if `instrument.immovable_property_interest && instrument.creates_or_transfers_interest && instrument.value_inr >= 100` (Registration Act s.17(1)(b)) | `STATE_VARIES` — `ART-SETTLEMENT` / `ART-AGREEMENT` [VERIFY] | `CONDITIONAL` | Cust. | Commercial disputes: pre-institution mediation settlements under Commercial Courts Act s.12A [VERIFY effect]; Equator handles mediated settlements (ecosystem boundary) | S |
| IF-26 | Compromise during a court case — D3.4.2 | `FORUM_RULES` (compromise in writing and signed by the parties, recorded by the court — CPC Order XXIII r.3 [VERIFY]); court may need physical or e-filed signatures | Per State / court | Decree-related registration questions [COUNSEL] | — | P10/P11 | N |
| IF-27 | Sale of goods and vehicles — D3.13.1–5 | `ESIGN_OK` | `STATE_VARIES` — `ART-AGREEMENT` | `NOT_REQUIRED`; vehicles: ownership transfer only through the registering authority (MV Act s.50; Forms 29/30) [VERIFY] → `SPECIAL_LAW_STEP(VAHAN_TRANSFER)` | Cust. | Agreement ≠ transfer (CH-23); Sale of Goods Act 1930 | S |
| IF-28 | Insurance and accident compensation applications — D3.9.1, D11.6.1 | `FORUM_RULES` (insurer process; MACT claim petition under MV Act s.166 [VERIFY] → pleadings rules) | `NOT_CHARGEABLE` (court fee rules separate) | — | Verification/affidavit per forum | P15 claim packs | N |

### 4D. Property

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-29 | Agreements for sale of immovable property — D12.8.1–5; developer agreement to sell flat D12.1.5 | **Not excluded by the IT Act** since entry 5 was omitted (S.O. 4720(E)) [LAW, V-WEB]. Base: `ESIGN_OK` (eS, D) when no registration condition applies; `ESIGN_OK_REGISTRATION_ROUTE` when any of: `instrument.rera_project` (RERA s.13(1)), `instrument.possession_given` or part-performance intended (Registration Act s.17(1A) with TPA s.53A), or a State row makes agreements for sale compulsorily registrable [VERIFY per State] | `STAMP_REQUIRED` — `ART-AGREEMENT_FOR_SALE`; several States charge conveyance-level duty where possession is given [VERIFY per State] | `CONDITIONAL` (as left); deadline `EXECUTION_PLUS_4_MONTHS` | Cust. 2 witnesses (registration offices require identifying witnesses [VERIFY]) | Registration Bill 2025 would make all agreements to sell registrable (L7, draft row only). R5 flagged these "not valid" on the pre-2022 basis — corrected (§9) | S |
| IF-30 | Conveyance, sale deed, deed of cancellation, sale deed to members — D12.1.2, D12.8.6, D12.8.7, D4.1.6 | `WET_INK_ONLY` (execution and presentation before the registering officer; TPA s.54 requires a registered instrument for sale of tangible immovable property of value ₹100 or more) [LAW]; becomes `ESIGN_OK_REGISTRATION_ROUTE` only through a State row with `accepts_esigned = true` `VERIFIED` | `STAMP_REQUIRED` — `ART-CONVEYANCE` (on market value or consideration, whichever is higher in most States [VERIFY]); cancellation `ART-CANCELLATION` | `COMPULSORY` (s.17(1)(b)) | Identifying witnesses at registration [VERIFY] | Cancellation of a registered sale deed by a registered cancellation deed or court decree [COUNSEL] | S |
| IF-31 | Gift deeds — D17.3.1–8 | Immovable property (D17.3.1, D17.3.5, and others where `!instrument.movable_only`): `WET_INK_ONLY` (TPA s.123: registered instrument signed by the donor and attested by at least two witnesses) [LAW]. Movable only: `ESIGN_OK` | `STAMP_REQUIRED` — `ART-GIFT` (State concessions for family gifts [VERIFY]) | Immovable: `COMPULSORY` (s.17(1)(a)); movable: `OPTIONAL` | Immovable: `WITNESS_REQUIRED(2, LEGAL)`; electronic attestation not allowed | Revocation of gift (D17.3.7) limited to TPA s.126 grounds [LAW]; registered revocation where the gift was registered [INTERP] | S |
| IF-32 | Mortgage and release of mortgage — D12.4.1–2, D12.6.1 | `WET_INK_ONLY` (TPA s.59: registered instrument signed by the mortgagor and attested by at least two witnesses, for mortgages other than by deposit of title deeds securing ₹100 or more) [LAW]. Memorandum recording a deposit of title deeds: `ESIGN_OK` if a mere record; `WET_INK_ONLY` + registration if it embodies the bargain [INTERP; COUNSEL] | `STAMP_REQUIRED` — `ART-MORTGAGE`; release `ART-RELEASE` | `COMPULSORY` (mortgage, release extinguishing an interest of ₹100 or more) | `WITNESS_REQUIRED(2, LEGAL)` | Registration Bill 2025 adds mortgage-by-deposit terms (draft row); lenders file CERSAI/ROC charges | S |
| IF-33 | Leases and rent agreements — D12.3.1–7, D12.7.5–7, D4.7.2 | `ESIGN_OK` when `instrument.term_months <= 12 && !instrument.year_to_year && !instrument.reserves_yearly_rent` (and no State override); otherwise `ESIGN_OK_REGISTRATION_ROUTE` (TPA s.107; Registration Act s.17(1)(d)) [LAW] | `STAMP_REQUIRED` — `ART-LEASE` (rent-and-deposit formula per State [VERIFY]) | `CONDITIONAL` (term > 1 year, year-to-year or yearly rent); **State override** `IN-MH`: leave and licence and lease agreements registrable regardless of term with online registration (Maharashtra Rent Control Act 1999 s.55 [VERIFY]) | Cust. 2 witnesses; registration identifying witnesses [VERIFY] | Eleven-month agreements avoid compulsory registration but remain stampable [INTERP]; renewal = new lease linked `RENEWS`; surrender of a registered lease by registered instrument [VERIFY] | S |
| IF-34 | Leave and licence, paying guest, licence to use immovable property — D1.4.7, D1.4.8, D12.7.1 | `ESIGN_OK` (a licence under the Indian Easements Act 1882 s.52 creates no interest in property) [LAW]; State override `IN-MH` as IF-33 | `STAMP_REQUIRED` — `ART-LEAVE_LICENCE` (or `ART-LEASE` where the State treats it so [VERIFY]) | `NOT_REQUIRED` except State overrides | Cust. | Substance over label: a "licence" with exclusive possession may be a lease [INTERP] — health check prompts review | S |
| IF-35 | Property notices and tenant correspondence — D12.5.1–5, D12.7.3–4, D11.9.6, D12.7.2 (landlord–tenant compromise: see IF-25) | `ESIGN_OK` / `E_ACCEPTANCE_OK` | `NOT_CHARGEABLE` | `NOT_REQUIRED` | — | Notice to quit under TPA s.106 [VERIFY amended text]; `DELIVERY_PROOF_RECOMMENDED`; R5's "Check" flag removed (§9) | S |
| IF-36 | Construction, architect, contractor and development agreements — D12.1.1, D12.1.3, D12.1.6–9; application to municipality D12.1.4 | Works contracts: `ESIGN_OK`. Development/joint development agreements granting development rights or possession: `ESIGN_OK_REGISTRATION_ROUTE` where the State requires registration [VERIFY per State]. Application to municipality: `FORUM_RULES` | Works contracts `STATE_VARIES` — `ART-AGREEMENT`; development agreements `ART-DEVELOPMENT_AGREEMENT` (conveyance-like duty in some States [VERIFY]) | `CONDITIONAL` | Cust. | Agreement with existing tenant (D12.1.1) may surrender tenancy rights → registration condition [COUNSEL]; Registration Bill 2025 adds developer agreements (draft row) | N |
| IF-37 | Partition, exchange, family settlement, release of immovable interest — D12.2.1–2, D17.4.1–7, D17.2.1–5, D3.12.1–3, D12.6.2–4, D2.1.2 | `ESIGN_OK` where `instrument.records_past_arrangement` (memorandum recording a family settlement already made) [INTERP; COUNSEL] or the instrument concerns only movables/money (e.g., release by creditor D3.12.2); otherwise `WET_INK_ONLY` with registration (partition and release creating/extinguishing rights in immovable property ≥ ₹100 — s.17(1)(b); exchange — TPA s.118) | `STAMP_REQUIRED` — `ART-PARTITION` / `ART-EXCHANGE` / `ART-RELEASE` / `ART-SETTLEMENT` | `CONDITIONAL` | Registration witnesses [VERIFY] | Division of a deceased's property (D17.2.3–4) follows the same condition; settlement for minor children (D2.1.2) → `GUARDIAN_REQUIRED` | S |

### 4E. Succession, trusts, powers of attorney and adoption

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-38 | Wills, codicils and revocation of wills — D17.6.1–5, D4.8.1 (codicil substituting a trustee) | **`WET_INK_ONLY`** (First Schedule entry 4) | `NOT_CHARGEABLE` (wills are not chargeable under the Indian Stamp Act Schedule [VERIFY State variants]) | `OPTIONAL` (Registration Act s.18(e)); deposit in sealed cover with the Registrar (ss.42–46) [VERIFY] | `WITNESS_REQUIRED(2, LEGAL)` — Indian Succession Act s.63 (each witness has seen the testator sign or received acknowledgement); electronic attestation not allowed | Revocation by another will/codicil or a writing executed like a will (s.70) [LAW]; wills under Muslim personal law need not be in writing [INTERP] — still wet-ink pack; vault stores the scan, the original must be kept safely | L |
| IF-39 | Private and family trusts — D4.8.4, D4.8.5 | **`WET_INK_ONLY`** (First Schedule entry 3) | `STAMP_REQUIRED` — `ART-TRUST` | Immovable property: `COMPULSORY` (Indian Trusts Act s.5) [LAW]; movables: `OPTIONAL` | Cust. 2 witnesses | — | L |
| IF-40 | Public, charitable and religious trusts; endowments to a deity; wakf — D4.8.6, D4.8.3 | `WET_INK_ONLY` [INTERP: the Indian Trusts Act excludes public/religious endowments (s.1) so entry 3 may not apply literally, but State public trust laws and dedication of immovable property require registration and physical execution; conservative block — COUNSEL] | `STAMP_REQUIRED` — `ART-TRUST` / `ART-SETTLEMENT` [VERIFY] | `COMPULSORY` where immovable property is dedicated; `SPECIAL_RECORDAL` with the Charity Commissioner/Waqf Board under State/Central law [VERIFY] | Cust. | Waqf Act 1995 as amended [VERIFY 2025 amendment status] | N |
| IF-41 | Donation to a trust — D4.8.2 | Movables/money: `ESIGN_OK` (a donation is a gift to the trust, not a trust instrument) [INTERP]; immovable property → IF-31 | `CHECK` — `ART-GIFT` for movables per State [VERIFY]; donation receipts (80G etc.) are the trust's documents | `CONDITIONAL` | — | R5 flagged "not valid" — corrected (§9) | S |
| IF-42 | Powers of attorney — D17.5.1–5 | **`WET_INK_ONLY`** (First Schedule entry 2); **carve-out row**: `ESIGN_OK` where the POA empowers an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity to act for the executant and the counterparty is verified as such | `STAMP_REQUIRED` — `ART-POA` (high duty in many States where the POA authorises sale for consideration or is irrevocable [VERIFY]) | `CONDITIONAL`: compulsory in some States for POAs to sell immovable property [VERIFY per State]; used for presentation of documents → authentication under Registration Act s.33 [VERIFY] | `NOTARY_REQUIRED` for use before courts and most authorities (Notaries Act; Powers-of-Attorney Act s.1A) [VERIFY] | A GPA sale is not a transfer of title (Supreme Court, *Suraj Lamp & Industries (P) Ltd v State of Haryana*, decided 11 Oct 2011, reported (2012) 1 SCC 656 [VERIFY citation]) — user text warns | L |
| IF-43 | Revocation of power of attorney — D17.5.6 | `WET_INK_ONLY` [INTERP: conservative — revocation should mirror the original's formality; notice to the agent and third parties may be sent electronically as IF-24] | `CHECK` per State [VERIFY] | `CONDITIONAL` (register revocation where the POA was registered) [INTERP] | Notarisation recommended | Pair with notice to agent (IF-24) | N |
| IF-44 | Adoption — D17.1.1–4 | `WET_INK_ONLY` [INTERP: HAMA s.16 presumption needs a registered document signed by the giver and taker; JJ Act route is by order of the District Magistrate, not a deed] | `STAMP_REQUIRED` — `ART-ADOPTION` [VERIFY] | `OPTIONAL` for the deed but needed for the s.16 presumption; authorities to adopt not conferred by will: `COMPULSORY` (Registration Act s.17(3)) [LAW] | `WITNESS_REQUIRED(2, CUSTOMARY)` | Hindu Adoptions and Maintenance Act 1956 ss.7–11 conditions; JJ Act 2015 and Adoption Regulations 2022 [VERIFY]; R5 flagged "valid" — corrected (§9) | N |

### 4F. Family, litigation, ADR, IP and students

| Code | Family (IDs) | eSign decision and methods | Stamp | Registration | Witness / notary | Special law and evidence notes | Status |
|---|---|---|---|---|---|---|---|
| IF-45 | Pleadings, petitions, applications, appeals, complaints and replies — Pleadings P1–P13; D2.1.1, D2.2.2–6, D2.3.1–3, D2.4.1, D2.4.3–6, D2.5.1, D11.5.2–3, D11.5.5, D13.2.1, D6.1.1 | `FORUM_RULES`: party (and advocate) signature and verification (CPC Order VI rr.14–15) [VERIFY]; e-filing with DSC/Aadhaar eSign where the forum's e-filing rules accept it (P10 render profile `esign_accepted`) [VERIFY per forum]; otherwise W | Court fees separate (`COURT_FEE_SEPARATE`) — not stamp duty | `NOT_REQUIRED` | Supporting affidavits → IF-46 | Filing by an advocate or party-in-person (NN-41); domestic incident reports are made by the Protection Officer in the prescribed form, not by the party (PWDVA 2005) [VERIFY]; marriage memoranda follow State registration rules with physical appearance [VERIFY] | N |
| IF-46 | Affidavits — D4.1.1, D4.2.9, D16.1.1–7, P1.1, P2.8, P4.9, P7.5 | **`DRAFT_APPROVAL_ONLY`** — e-acceptance "Approved for swearing"; the affidavit is sworn before a notary, oath commissioner or magistrate (Oaths Act 1969; Notaries Act 1952; CPC Order XIX) [LAW]; video-oath/e-affidavit only where a forum's rules provide [VERIFY] | `STATE_VARIES` — `ART-AFFIDAVIT` (court affidavits often exempt [VERIFY]) | `NOT_REQUIRED` | `NOTARY_REQUIRED` / `OATH_REQUIRED` | Never presented as sworn until the sworn scan is uploaded (P08 FR-P08-42); R5 flagged these "valid" — corrected (§9) | L |
| IF-47 | Vakalatnama — D11.12.1–14 | `FORUM_RULES`: signed by the client and accepted by the advocate; electronic only where the forum's e-filing system provides an e-vakalatnama [VERIFY]; default W [INTERP; whether a vakalatnama is a "power of attorney" for First Schedule entry 2 is a counsel question — COUNSEL] | `WELFARE_STAMP` — advocates' welfare fund stamp under the Advocates' Welfare Fund Act 2001 and State Acts [VERIFY] | `NOT_REQUIRED` | Advocate's acceptance; identification per court rules | Language versions (Hindi, regional) are templates; the court's prescribed form prevails | N |
| IF-48 | RTI applications and appeals — D11.8.1–2 | `FORUM_RULES` — online through the RTI portal (no signature) or physical application with fee (RTI Act 2005 s.6) [LAW]; eA for LawDocs records | `NOT_CHARGEABLE` (application fee separate) | — | — | User files; LawDocs drafts | S |
| IF-49 | Arbitration agreements, references and arbitral communications — D11.2.1–6 | `ESIGN_OK` / `E_ACCEPTANCE_OK` (A&C Act s.7(4)(b) electronic communications) [LAW]; arbitrators' directions and notices: eS, D (D preferred) | `STATE_VARIES` — `ART-ARBITRATION_AGREEMENT` (where chargeable as agreement); awards `ART-AWARD` [VERIFY] | `NOT_REQUIRED` (awards affecting immovable property: registration questions [COUNSEL]) | — | Non-stamping is curable, not fatal, per the Supreme Court's seven-judge bench in *In re: Interplay between Arbitration Agreements under the A&C Act 1996 and the Indian Stamp Act 1899* (13 Dec 2023; 2023 INSC 1066 [VERIFY citation]); Equator administers ADR (ecosystem boundary) | S |
| IF-50 | IP assignments and licences — D8.1.1–3, D8.2.1–2, D8.3.1–2 | `ESIGN_OK`; eS, D | `STATE_VARIES` — `ART-ASSIGNMENT` [VERIFY per State] | `SPECIAL_RECORDAL`: Copyright — none mandatory (s.19 writing and signature) [LAW]; Patents — registration of title with the Controller (s.69) [LAW]; Trade marks — request to register assignment (s.45) [LAW] [VERIFY forms] | — | `SPECIAL_LAW_STEP(PATENT_TITLE_REGISTRATION | TM_ASSIGNMENT_RECORDAL)` feeds P12 | S |
| IF-51 | Student applications, CVs and letters — D16.2.2–4, D16.3.1–6 | `E_ACCEPTANCE_OK` / `ESIGN_OK` | `NOT_CHARGEABLE` | — | — | Institutional rules decide format | V |
| IF-52 | Statutory e-forms and returns (MCA, GST, income-tax, labour, RBI/SEBI portals) | `FORUM_RULES` — signed by the authorised person with DSC/EVC on the portal; LawDocs prepares, a human files (Ecosystem principle 11; NN-05) | — | — | — | P13/P14 | V |
| IF-99 | Unclassified upload | `NEEDS_CLASSIFICATION` | — | — | — | Decision helper (P08 FR-P08-12) | L |

**Cross-cutting rules applied to every row (encoded as `IN` rows, not repeated above):**

1. **Minors.** If `party.any_minor` and not `party.guardian_signing` with a row that permits guardians → `WET_INK_ONLY` with message "A minor cannot sign this; a guardian may sign where the law allows" (Indian Contract Act s.11) [LAW]. Accounts are 18+ (R3 LG-032).
2. **Organisation signatories.** If `party.org_signatory`, the signer's authority must exist in the tenant's DoA (P02) for the family and amount → `BOARD_APPROVAL_REQUIRED` or internal approval flag from tenant rows; the row itself never relaxes.
3. **Aadhaar in the instrument.** Any instrument body containing a full Aadhaar number cannot be frozen (P08 FR-P08-15; NN-04).
4. **Stamp before sign.** Any row with `stamp ∈ {STAMP_REQUIRED, STATE_VARIES, CHECK}` sets `STAMP_REQUIRED` on the electronic route unless the State duty table resolves the article to nil or a cited exemption is declared (P08 FR-P08-35); locked (R3 LG-096).
5. **Electronic attestation.** Where `attestation.mandatory_by_law = true`, electronic witnessing is not offered; the row's decision is `WET_INK_ONLY` unless counsel-approved `electronic_attestation_allowed = true` is published (OI-F-03).

---

## 5. eStamp State coverage registry (`IN-<ST>.estamp.channels`)

### 5.1 Schema

| Field | Type | Rule |
|---|---|---|
| `state_code` | ISO 3166-2:IN | e.g., `IN-MH` |
| `stamp_law` | citation | State Stamp Act or Indian Stamp Act as applied, with amendment references |
| `channels[]` | enum `SHCIL_ESTAMP`, `STATE_ESTAMP_PORTAL`, `GRAS_CHALLAN`, `E_SBTR`, `FRANKING`, `PHYSICAL_PAPER`, `TREASURY_ESTAMP`, `OTHER` | Each with `authorised_by` citation and `verification_method` (`VENDOR_API`, `PUBLIC_PORTAL_MANUAL`, `NONE`) |
| `electronic_instrument_supported` | bool per channel | Whether the proof can be linked to an electronically signed instrument [VERIFY per channel] |
| `vendors[]` | provider IDs from `sgn.providers` | Which LawDocs vendor can procure in the State, as **agent** (R3 LG-100) |
| `purchase_enabled` | bool | `sgn.estamp.state.<code>.enabled`; permissive → requires `VERIFIED` (P03 FR-P03-56) |
| `attach_enabled` | bool | Protective: always true (users may attach authorised proof; verification may be manual) |
| `cancellation_procedure` | text ref + time limit | Spoiled/unused stamp refund rules [VERIFY] |
| `merge_rule` | enum `CERT_FIRST_PAGE`, `CERT_LAST_PAGE`, `ANNEX` | How the certificate is bound to the instrument [VERIFY per State] |
| `registration.accepts_esigned` | bool | Whether the State's registering offices accept electronically signed instruments for registration [VERIFY] |
| `verification_status`, `reviewer_of_record`, `effective_from`, `next_review_due` | — | As §3.1 |

### 5.2 Seed registry (status as of 25 Oct 2026)

Facts marked V-WEB/V-SEC come from R3 LG-098/LG-099; every other entry is an **analyst expectation to be verified** and is `NOT_CONFIRMED`. No State has `purchase_enabled = true` until its row is `VERIFIED` with the vendor's coverage confirmed in writing (P08 OI-P08-11). The attach route is open in every State.

| Code | State / UT | Stamp law | Channels (verified facts / expectation) | Status |
|---|---|---|---|---|
| IN-AP | Andhra Pradesh | Indian Stamp Act 1899 as amended for AP [VERIFY] | Expectation: SHCIL e-stamp; franking; physical [VERIFY] | N |
| IN-AR | Arunachal Pradesh | [VERIFY] | Expectation: physical paper [VERIFY] | N |
| IN-AS | Assam | Indian Stamp Act as amended for Assam [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-BR | Bihar | Indian Stamp Act as amended for Bihar [VERIFY] | Expectation: State/SHCIL e-stamp [VERIFY] | N |
| IN-CT | Chhattisgarh | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-GA | Goa | [VERIFY] | Expectation: franking; SHCIL e-stamp [VERIFY] | N |
| IN-GJ | Gujarat | Gujarat Stamp Act 1958 [VERIFY] | **SHCIL e-stamp — first State (2007)** (V-WEB, LG-098); franking [VERIFY] | S |
| IN-HR | Haryana | Indian Stamp Act as amended for Haryana; **Haryana Stamp (Payment of Duties by Means of Online E-Stamping) Rules 2017** (V-SEC, LG-099) | **SHCIL + State online e-stamping** (V-SEC) | S |
| IN-HP | Himachal Pradesh | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-JH | Jharkhand | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-KA | Karnataka | **Karnataka Stamp Act 1957** (LG-097) | **SHCIL integrated with Kaveri** (V-SEC, LG-099); franking [VERIFY] | S |
| IN-KL | Kerala | Kerala Stamp Act 1959 [VERIFY] | **Treasury e-stamp portal** (V-SEC, LG-099); physical [VERIFY] | S |
| IN-MP | Madhya Pradesh | Indian Stamp Act as amended for MP [VERIFY] | Expectation: State e-stamp through the State registration system [VERIFY] | N |
| IN-MH | Maharashtra | **Maharashtra Stamp Act 1958** (LG-097) | **SHCIL + GRAS (e-challan/e-SBTR) + franking** (V-SEC, LG-099) | S |
| IN-MN | Manipur | [VERIFY] | Expectation: physical [VERIFY] | N |
| IN-ML | Meghalaya | [VERIFY] | **SHCIL e-stamp — latest State (Nov 2021)** (V-WEB, LG-098) | S |
| IN-MZ | Mizoram | [VERIFY] | Expectation: physical [VERIFY] | N |
| IN-NL | Nagaland | [VERIFY] | Expectation: physical [VERIFY] | N |
| IN-OR | Odisha | Indian Stamp Act as amended for Odisha [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-PB | Punjab | Indian Stamp Act as amended for Punjab [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-RJ | Rajasthan | **Rajasthan Stamp Act 1998** (LG-097) | Expectation: SHCIL e-stamp; State e-GRAS; surcharge per vendor note (R1) [VERIFY] | N |
| IN-SK | Sikkim | [VERIFY] | Expectation: physical [VERIFY] | N |
| IN-TN | Tamil Nadu | Indian Stamp Act as amended for TN [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-TG | Telangana | Indian Stamp Act as amended for Telangana [VERIFY] | Expectation: [VERIFY] | N |
| IN-TR | Tripura | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-UP | Uttar Pradesh | Indian Stamp Act as applied in UP (LG-097) | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-UT | Uttarakhand | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-WB | West Bengal | Indian Stamp Act as amended for WB [VERIFY] | Expectation: State online payment (GRIPS) / franking [VERIFY] | N |
| IN-AN | Andaman and Nicobar Islands | Indian Stamp Act [VERIFY] | Expectation: [VERIFY] | N |
| IN-CH | Chandigarh | Indian Stamp Act as applicable [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-DH | Dadra and Nagar Haveli and Daman and Diu | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-DL | Delhi | Indian Stamp Act as applied in Delhi (LG-097) | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-JK | Jammu and Kashmir | [VERIFY post-2019 applicable law] | Expectation: SHCIL e-stamp [VERIFY] | N |
| IN-LA | Ladakh | [VERIFY] | Expectation: [VERIFY] | N |
| IN-LD | Lakshadweep | [VERIFY] | Expectation: physical [VERIFY] | N |
| IN-PY | Puducherry | [VERIFY] | Expectation: SHCIL e-stamp [VERIFY] | N |

SHCIL reports e-stamping in 23 States/UTs (LG-098) and vendors claim 16–31 States/UTs through their channels (R1 §6.1; R6 D-25) — vendor claims are self-published and are verified per State, per article, before activation (NN-20).

### 5.3 Verification procedure (per State)

1. `PLT_LEGAL_REVIEWER` confirms the stamp law, the authorised channels and the agent-procurement rules from the State's official notification or portal, and records the source with SHA-256 in `docs/compliance/verification-log.md`.
2. The vendor confirms in writing the States and articles it can procure, the issuing route (SHCIL ACC, State portal), verification API availability and turnaround.
3. A test purchase (lowest-value article) is completed and verified end to end in staging/production sandbox where available.
4. `registration.accepts_esigned` is set only on the State registration department's written or published position.
5. A checker publishes the row (`permissive` effect class) and the State flag is switched on; the help page lists the State as supported with the date of verification.

---

## 6. Stamp duty tables (`IN-<ST>.stamp.duty_table`)

### 6.1 Row schema

| Field | Rule |
|---|---|
| `state_code`, `article_code` (canonical, §6.2), `state_article_ref` (Schedule article number and description in the State law) | Required |
| `formula` | `FIXED(amount)`, `PERCENT(base, rate)`, `RENT_FORMULA(term_bands, rent_basis, deposit_treatment, premium_rate)`, `SLAB(table)`, `MAX_OF(a, b)`, `MIN_MAX(min, max)`, `COMPOSITE(...)` |
| `base` | `CONSIDERATION`, `MARKET_VALUE` (user-entered from the State guidance value; LawDocs never scrapes it — NN-05), `HIGHER_OF(CONSIDERATION, MARKET_VALUE)`, `SECURED_AMOUNT`, `RENT_AND_DEPOSIT`, `NONE` |
| `surcharges[]` | Cess, surcharge, metro/municipal levies with their own citations [VERIFY] |
| `concessions[]` | Eligibility question + effect (e.g., family gift concession, women purchaser concession) [VERIFY] |
| `rounding` | e.g., next ₹1, ₹10 or ₹100 [VERIFY] |
| `exemptions[]` | Coded list for P08 FR-P08-35 declarations |
| `citations[]`, `effective_from/to`, `verification_status`, `reviewer_of_record`, `golden_cases[]` | As §3.1; `computational` effect class |

**No rate is seeded in this appendix.** Rates change by State Finance Acts and notifications and must be entered from primary sources at verification time **[VERIFY — every row]**. A `NOT_CONFIRMED` row produces an "Indicative — under verification" estimate only (P03 FR-P03-57); the vendor's quote is shown alongside; purchase uses the vendor's computed duty.

### 6.2 Canonical article codes (cross-walk to each State Schedule)

`ART-ACKNOWLEDGEMENT`, `ART-ADOPTION`, `ART-AFFIDAVIT`, `ART-AGREEMENT` (agreement or memorandum not otherwise provided for), `ART-AGREEMENT_FOR_SALE`, `ART-ARBITRATION_AGREEMENT`, `ART-ASSIGNMENT`, `ART-AWARD`, `ART-BOND`, `ART-CANCELLATION`, `ART-CONVEYANCE`, `ART-DEVELOPMENT_AGREEMENT`, `ART-EXCHANGE`, `ART-GIFT`, `ART-HIRE_PURCHASE`, `ART-INDEMNITY_BOND`, `ART-LEASE`, `ART-LEAVE_LICENCE`, `ART-MEMORANDUM_ARTICLES`, `ART-MORTGAGE`, `ART-NOTARIAL_ACT`, `ART-PARTITION`, `ART-PARTNERSHIP`, `ART-PLEDGE_HYPOTHECATION`, `ART-POA`, `ART-PROMISSORY_NOTE`, `ART-RECEIPT`, `ART-RELEASE`, `ART-SETTLEMENT`, `ART-SHARE_TRANSFER`, `ART-SURRENDER_OF_LEASE`, `ART-TRUST`. A State that has no matching article maps to `ART-AGREEMENT` only with a reviewer note; otherwise the cross-walk row is `NOT_CONFIRMED`.

### 6.3 Inputs, who pays and inter-State instruments

- Inputs come from template answers (P06) — consideration, rent, deposit, term, market value, property State — never inferred by AI (NN-14).
- Who pays: Indian Stamp Act s.29 sets defaults subject to agreement [VERIFY State variants]; the template clause `stamp_duty_payer` drives the order's payer (P08 FR-P08-31).
- Instruments executed in one State and received or relating to property in another may attract duty differences on receipt [VERIFY inter-State provisions per State]; the calculator flags `INTER_STATE_CHECK` when `state.execution != state.property` and shows both States' estimates.

---

## 7. Registration and formalities rule sets

### 7.1 `IN-<ST>.registration.*`

| Key | Content |
|---|---|
| `required_instruments` | State additions to Registration Act s.17 (e.g., leave and licence in `IN-MH` [VERIFY]); each with citation |
| `accepts_esigned` | bool + source (§5.3 step 4) |
| `e_registration` | Portal name and public URL for deep links only; appointment booking is user-performed (NN-05) |
| `documents_checklist` | Identity proof, photographs, PAN/Form 60 requirement [VERIFY], property documents, witness IDs |
| `fees_ref` | Registration fee schedule reference (shown separately from duty and LawDocs fees, NN-22) [VERIFY] |
| `presentation_deadline` | `EXECUTION_PLUS_4_MONTHS` (s.23) unless State/Central law differs [VERIFY] |

### 7.2 `IN.sgn.formalities` row schema

| Field | Rule |
|---|---|
| `formality_kind` | `STAMP`, `SIGNATURES`, `WITNESSES`, `NOTARISATION`, `OATH`, `REGISTRATION`, `BOARD_APPROVAL`, `COUNTERPARTY_SIGNATURE`, `SPECIAL_LAW`, `INTERNAL_APPROVAL`, `RECORDAL` |
| `condition` | CEL over the same facts as §3.4 plus the eligibility decision |
| `evidence_types[]` | e.g., `ESTAMP_CERTIFICATE`, `FRANKING_SCAN`, `REGISTRATION_RECEIPT`, `SWORN_SCAN`, `RESOLUTION_REF`, `RECORDAL_ACK` |
| `waivable` | bool; `STAMP` (electronic route) and eligibility are never waivable; legal attestation is not waivable on an electronic route |
| `waiver_reason_codes[]` | Locked list (e.g., `HANDLED_OFFLINE_EVIDENCE_TO_FOLLOW`, `NOT_APPLICABLE_FACTS_CHANGED`, `COUNSEL_ADVISED`) |
| `deadline_rule` | e.g., `EXECUTION_PLUS_4_MONTHS`, `BEFORE_SIGNING`, `WITHIN_30_DAYS_OF_EXECUTION` [VERIFY per special law] |
| `external_label` | Text shown to counterparties for shared items (P03 FR-P03-78) |

---

## 8. How the rules engine consumes the matrix

### 8.1 Evaluation algorithm (deterministic; implemented once in `packages/rules`, called by P08)

```text
evaluate(doc, facts, tenant):
  family := doc.family ?? template.family
  if family is null or doc.eligibility_suspect: return NEEDS_CLASSIFICATION or WET_INK_ONLY (suspect)
  candidate_rows := active rows of IN.sgn.eligibility
       where row.family = family
       and row.jurisdiction in {IN, state.execution, state.property}
       and row.effective_from <= today < coalesce(row.effective_to, ∞)
  applicable := [r in candidate_rows where eval(r.condition, facts) = TRUE]
                 -- a condition that cannot be evaluated (missing fact) is treated as TRUE for
                 -- protective rows and FALSE for permissive rows (conservative)
  carve_outs := [r in applicable where r.is_carve_out and r.verification_status = VERIFIED]
  base_locked := [r in applicable where r.locked and not r.is_carve_out]
  if carve_outs non-empty: replace the base locked row it names (r.carves_out_row_id)
  -- permissive rows that are not VERIFIED are ignored; their declared fallback applies
  applicable := [r where r.effect_class != permissive or r.verification_status = VERIFIED]
  decision := strictest(applicable.esign_decision)
       order: NEEDS_CLASSIFICATION > WET_INK_ONLY > DRAFT_APPROVAL_ONLY > FORUM_RULES
              > ESIGN_OK_REGISTRATION_ROUTE > DSC_OK > ESIGN_OK > E_ACCEPTANCE_OK
  if decision = ESIGN_OK_REGISTRATION_ROUTE and not registry(state.property).accepts_esigned VERIFIED:
       effective := WET_INK_ONLY with reason REG_OFFICE_ESIGN_UNCONFIRMED
  methods := ∩(applicable.methods_permitted) ∩ tenant.allowed_methods ∩ provider_available
  flags := ∪(applicable.flags) ∪ cross_cutting_flags(facts)
  apply tenant stricter-only overlays (P03 FR-P03-61): may remove methods, add flags, raise decision
  record evaluation: decision, effective decision, flags, methods, row ids + versions,
         rule-set version, facts hash, explanation ids  → pinned on the signing request
```

**Strictest wins** because the cost of a wrongly blocked eSign is a printed document, while the cost of a wrongly allowed eSign is an unenforceable or inadmissible instrument.

### 8.2 Explanations

Each decision returns `user_text` ids rendered in the user's language with the citation, e.g.:

- `WET_INK_ONLY` (IF-38): "A will can't be signed electronically in India (IT Act 2000, First Schedule, entry 4). Print it, sign it in front of two witnesses who also sign, and keep the original safe. Registering it is optional."
- `ESIGN_OK_REGISTRATION_ROUTE` → effective `WET_INK_ONLY` (IF-33, 3-year lease): "Leases longer than one year must be registered (Registration Act 1908, s.17). Registration offices in <State> are not yet confirmed to accept electronically signed leases, so sign on paper and register within four months."
- `DRAFT_APPROVAL_ONLY` (IF-46): "An affidavit must be sworn before a notary or oath commissioner. Approve the draft here, then take it for swearing."

### 8.3 Golden cases (minimum seed; one positive and one negative per row in `packages/rules/fixtures/IN.sgn.eligibility/`)

| # | Family | Facts | Expected |
|---|---|---|---|
| G-01 | IF-38 will | any | `WET_INK_ONLY`, `WITNESS_REQUIRED(2, LEGAL)` |
| G-02 | IF-42 POA | counterparty `NONE` | `WET_INK_ONLY`, `STAMP_REQUIRED`, `NOTARY_REQUIRED` |
| G-03 | IF-42 POA | counterparty `RBI` verified, carve-out row `VERIFIED` | `ESIGN_OK` |
| G-04 | IF-23 promissory note | counterparty `NONE` | `WET_INK_ONLY` |
| G-05 | IF-23 promissory note | counterparty `SEBI` verified | `ESIGN_OK`, `STAMP_REQUIRED` |
| G-06 | IF-33 rent, `IN-KA` | term 11 months | `ESIGN_OK`, `STAMP_REQUIRED` |
| G-07 | IF-33 lease, `IN-KA` | term 36 months, `accepts_esigned` not verified | effective `WET_INK_ONLY`, `REGISTRATION_REQUIRED(EXECUTION_PLUS_4_MONTHS)` |
| G-08 | IF-33 leave and licence, `IN-MH` | term 11 months | `ESIGN_OK_REGISTRATION_ROUTE` (State override) → effective per `accepts_esigned` |
| G-09 | IF-29 agreement for sale | RERA project | `ESIGN_OK_REGISTRATION_ROUTE` |
| G-10 | IF-29 agreement for sale | not RERA, no possession, State without override | `ESIGN_OK`, `STAMP_REQUIRED` |
| G-11 | IF-31 gift | immovable | `WET_INK_ONLY`, `REGISTRATION_REQUIRED`, `WITNESS_REQUIRED(2, LEGAL)` |
| G-12 | IF-31 gift | movable only | `ESIGN_OK`, `STAMP_REQUIRED` |
| G-13 | IF-46 affidavit | any | `DRAFT_APPROVAL_ONLY`, `NOTARY_REQUIRED` |
| G-14 | IF-01 NDA | missing `state.execution` | `ESIGN_OK`, `STAMP_REQUIRED` with `STATE_UNKNOWN` prompt (cannot freeze until State given) |
| G-15 | IF-37 partition | `records_past_arrangement = unknown` | conservative `WET_INK_ONLY` |
| G-16 | Any | `party.any_minor`, no guardian row | `WET_INK_ONLY` (cross-cutting rule 1) |
| G-17 | IF-01 uploaded, P05 `eligibility_suspect` (POA detected) | — | `WET_INK_ONLY` until reclassified |
| G-18 | IF-45 plaint, forum profile `esign_accepted = false` | — | `FORUM_RULES` → wet ink |

### 8.4 Versioning, effective dating and in-flight objects

- Rows follow the P03 lifecycle (`DRAFT → IN_REVIEW → APPROVED → SCHEDULED → ACTIVE → SUPERSEDED → RETIRED`); a row's `effective_from` is the legal commencement date, not the publish date; a gazette change published late uses `open_items_with_notice` propagation to list in-flight requests decided under the old row (P03 FR-P03-59).
- Signing requests pin the rule-set version at creation; a stricter new row (e.g., a State making agreements for sale registrable) applies to requests not yet sent; requests already sent continue unless the change is an `emergency_block` (e.g., an ESP licence lapse or a court ruling invalidating a method), in which case unsent signatures pause and the sender is notified.
- `RETIRED` rows keep resolving historical evaluations for audit.

### 8.5 Reviewer of record and change triggers

| Trigger | Owner | SLA to a reviewed draft row |
|---|---|---|
| Gazette notification amending the IT Act Schedules, eSign rules or CCA guidelines | `PLT_LEGAL_REVIEWER` | 5 working days (emergency block same day if protective) |
| State Finance Act / stamp notification (often around 1 April) | `PLT_LEGAL_REVIEWER` + State reviewer | 10 working days; `next_review_due` 30 days in budget months |
| Registration Bill 2025 enactment or State registration notifications | `PLT_LEGAL_REVIEWER` | 10 working days; activate pre-built draft rows |
| Supreme Court / High Court judgment affecting execution or admissibility | `PLT_LEGAL_REVIEWER` with counsel | 10 working days |
| Rule challenge from a tenant (P03 FR-P03-61) | `PLT_LEGAL_REVIEWER` | Response within 10 working days |

Every published row shows "Source and review" (reviewer name, qualification, date) on the "Why?" panel; tenants receive a change notice listing affected templates (P06) and open requests (P08).

### 8.6 Consumers

| Consumer | Use |
|---|---|
| P06 | Template → `eligibility_row_id`; cached decision displayed on the template page and the public "Key facts" box ("eSign valid? Yes / No") |
| P07 | Pre-sign gates (FR-P07-42) |
| P08 | Gate, methods, stamp lock, formalities items, packs |
| P04 | Health checks `HC-STAMP-MISSING`, `HC-REGISTRATION-DUE`, `HC-WITNESS-MISSING`, `HC-NOTARY-MISSING`, `HC-ESIGN-EXCLUDED` |
| P05 | `eligibility_suspect` classification tightening |
| P10 | Forum render profiles supply `esign_accepted` for `FORUM_RULES` rows |
| P21 | Public "Can I eSign this?" and stamp-duty tools read the same published rows (no separate copy, NN-30) |
| Vidhi (P09) | Explains decisions by quoting `user_text` and citations; never computes eligibility (NN-14) |

---

## 9. Corrections to the R5 eSign flags (`R5_Document_Page_Inventory.csv`)

R5 classified 250 entries "Valid (Aadhaar eSign)", 62 "Check" and 35 "Not valid (IT Act s.1(4), Sch. I)". R5's rule list still includes "contracts for sale/conveyance of immovable property", which the 2022 amendment omitted (R3 LG-003, V-WEB). The matrix above supersedes the flags as follows:

| R5 flag | Entries | Matrix outcome | Reason |
|---|---|---|---|
| Not valid | Wills D17.6.1–5; codicil D4.8.1; POAs D17.5.1–6; private/family trusts D4.8.4–5; promissory notes D3.10.1–4 | `WET_INK_ONLY` (locked) | First Schedule entries 1–4 — confirmed |
| Not valid | Public trust D4.8.6; endowment to deity D4.8.3 | `WET_INK_ONLY` (conservative) | State trust laws and dedication of immovable property, not entry 3 literally [INTERP; COUNSEL] |
| Not valid | Donation to trust D4.8.2 | `ESIGN_OK` for movables; IF-31 for immovable | A donation is a gift, not a trust instrument |
| Not valid | Agreements for sale D12.8.1–5 | `ESIGN_OK` or `ESIGN_OK_REGISTRATION_ROUTE` (IF-29) | Entry 5 omitted in 2022; registration/stamp govern |
| Not valid | Conveyance D12.1.2, sale deed cancellation D12.8.6, deed of conveyance D12.8.7, sale deed to members D4.1.6 | `WET_INK_ONLY` (IF-30) — reason changed | Execution and registration before the registering officer (TPA s.54; Registration Act s.17), not the First Schedule |
| Not valid | Mortgage D12.4.1–2; release of mortgaged property D12.6.1 | `WET_INK_ONLY` (IF-32) — reason changed | TPA s.59 attestation + registration |
| Not valid | Gift of immovable property D17.3.5; life estate D17.3.1 | `WET_INK_ONLY` (IF-31) — reason changed | TPA s.123 attestation + registration |
| Valid | Affidavits D4.1.1, D4.2.9, D16.1.1–7 | `DRAFT_APPROVAL_ONLY` (IF-46) | Oath before a notary/oath commissioner; an eSign is not a jurat |
| Valid | Vakalatnama D11.12.1–14 | `FORUM_RULES` (IF-47) | Court rules and welfare stamp; POA question [COUNSEL] |
| Valid | Petitions, complaints, applications and replies D2.1.1, D2.2.2–6, D2.3.1–3, D2.4.1, D2.4.3–6, D2.5.1, D11.5.2–3, D11.5.5, D11.8.1–2, D13.2.1, D6.1.1 | `FORUM_RULES` (IF-45/IF-48) | Signature/verification and filing per forum |
| Valid | Adoption D17.1.1–4 | `WET_INK_ONLY` (IF-44) | Registered deed for HAMA s.16 presumption; s.17(3) authorities to adopt |
| Valid | Declaration of solvency D4.2.11 | `DRAFT_APPROVAL_ONLY` (IF-11) | Verified by affidavit [VERIFY] |
| Valid | MoA/AoA D4.2.3 | `DSC_OK` (IF-06) | SPICe+ DSC filing [VERIFY] |
| Valid | Listing agreements D4.2.5–6 | `RETIRED_TEMPLATE` (IF-12) | Replaced by SEBI LODR 2015 |
| Valid | Administration bond D3.3.1 | `FORUM_RULES` (IF-20) | Court-required bond |
| Valid | Share transfer D1.1.4 | SPA `ESIGN_OK`; SH-4 `FORUM_RULES` (IF-04) | Companies Act s.56 practice [VERIFY] |
| Valid | Division of property D17.2.3–4 | Conditional (IF-37) | Immovable property → registration |
| Valid | Apprenticeship by guardian D10.2.1 | `ESIGN_OK` + `GUARDIAN_REQUIRED` (IF-15) | Minor's contract through guardian |
| Check | Property notices D12.5.1–5; tenant notices D12.7.3–4 | `ESIGN_OK` (IF-35) | Notices create no interest in property |
| Check | Leases D12.3.1–7; rent agreements D12.7.5–7, D4.7.2 | Conditional on term (IF-33) + State overrides | TPA s.107; Registration Act s.17(1)(d) |
| Check | Leave and licence D1.4.7–8; paying guest D12.7.1 | `ESIGN_OK` + stamp; `IN-MH` override (IF-34) | Easements Act s.52 |
| Check | Building contracts D12.1.1, D12.1.3, D12.1.6–9 | `ESIGN_OK` unless development rights (IF-36) | — |
| Check | Settlements D1.2.7, D3.4.1, D12.7.2; family arrangements D17.2.1–2, D17.2.5; partitions D17.4.1–7; release deeds D3.12.1–3, D12.6.2–4; exchange D12.2.2; compromise for partition D12.2.1; settlement for minors D2.1.2; application for release of property to police D2.2.1 | Conditional (IF-25, IF-37) or `FORUM_RULES` (D2.2.1) | Registration only where rights in immovable property are created or extinguished |
| Check | Gift deeds D17.3.2–4, D17.3.6–8 | Conditional on movable/immovable (IF-31) | TPA s.123 |
| Check | Memorandum of settlement (industrial) D10.11.4 | `FORUM_RULES` (IF-17) | IR Code form [VERIFY] |
| Check | Application to municipality D12.1.4 | `FORUM_RULES` (IF-36) | Authority's process |

P06 OI-P06-04 (reconcile R5 flags with LG-003) is closed by this section once `PLT_LEGAL_REVIEWER` signs the seed rows. The public document pages' "eSign valid?" key fact (R5 §7.2 block 5) reads from the published row, not from R5.

---

## 10. Implementation checklist (P08 sprint 1 and content load)

- [ ] `rul` content kinds `eligibility_row`, `formalities_row`, `estamp_state_row`, `duty_table_row`, `registration_row` registered (P03 FR-P03-63) with the schemas in §3, §5.1, §6.1, §7.
- [ ] Validators: decision–methods consistency; locked rows cannot be overlaid; carve-out rows must name the row they carve out and be `VERIFIED`; every row ≥ 1 citation; golden cases present.
- [ ] Seed rows IF-01…IF-52 and IF-99 loaded as `DRAFT`; locked rows (IF-23 base, IF-38, IF-39, IF-42 base, IF-46, IF-99) published first after review.
- [ ] Mapping of every canonical R5 D-code and launch P-code to a family (CSV in `packages/rules/fixtures/IN.sgn.eligibility/mapping.csv`), with a CI test that no canonical template lacks a family.
- [ ] State registry rows loaded `NOT_CONFIRMED`; launch States verified per §5.3.
- [ ] Explanation strings in the 10 launch UI languages, reviewed.
- [ ] `NN-07_excluded_instrument_never_reaches_esp.spec.ts` and `NN-08_stamp_before_sign.spec.ts` run the golden cases end to end.

---

## 11. Open items

| ID | Item | Owner |
|---|---|---|
| OI-F-01 | Verify every `[VERIFY]` statute wording cited in §1 (TPA ss.3, 54, 59, 107, 123; Registration Act ss.17, 18, 23, 33, 42–46; ISA s.63, s.70; ITA s.5; RERA s.13(1); A&C s.7; IP sections) against official texts | `PLT_LEGAL_REVIEWER` |
| OI-F-02 | State registry (§5.2) and duty tables (§6) for launch States; vendor coverage letters | `PLT_LEGAL_REVIEWER` / P08 |
| OI-F-03 | Adequacy of remote electronic attestation where attestation is legally required | [COUNSEL] |
| OI-F-04 | Vakalatnama as "power of attorney" under First Schedule entry 2; e-vakalatnama acceptance per forum | [COUNSEL] / P10 |
| OI-F-05 | Public/religious trusts and wakf execution formalities; donation-to-trust treatment | [COUNSEL] |
| OI-F-06 | State e-registration acceptance of eSigned instruments (`accepts_esigned`) for launch States | `PLT_LEGAL_REVIEWER` |
| OI-F-07 | Share-transfer instrument (SH-4) electronic execution practice; stamp duty collection on securities transfers | [COUNSEL] / `PLT_LEGAL_REVIEWER` |
| OI-F-08 | Receipt stamp threshold and treatment of electronic receipts; acknowledgement-of-debt article | `PLT_LEGAL_REVIEWER` |
| OI-F-09 | Family settlement memoranda — registration test and citation | [COUNSEL] |
| OI-F-10 | Registration Bill 2025 status; pre-built draft rows | `PLT_LEGAL_REVIEWER` |
| OI-F-11 | Seven-judge Supreme Court decision (2023) on unstamped arbitration agreements — citation and effect for IF-49 | `PLT_LEGAL_REVIEWER` |
| OI-F-12 | Maharashtra leave-and-licence compulsory registration and online registration acceptance of eSigned agreements | `PLT_LEGAL_REVIEWER` |
