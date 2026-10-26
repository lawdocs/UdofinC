# Appendix Y — Ecosystem Spec v1.2 Change Request (LawDocs)

**Status:** Binding as a proposal. LawDocs code may implement the contracts below only behind `int.eco.v12_contracts.enabled` (OFF) until the pull request carrying this proposal is merged into `infrabyx-contracts` and every affected owner has approved (Ecosystem Spec v1.1, "How to use", change-control rule; Part 14.2). **Used by:** P19 (owner), P01, P04, P07, P08, P11, P12, P13, P14, P15, P16, P17, P18, P20, P21, P23.

**How to use.** This appendix is the text of the proposal file `infrabyx-contracts/proposals/2026-10-25-add-lawdocs-ld.md`. Copy §Y.1 to §Y.17 into that file unchanged, open the pull request, and attach the impact note (§Y.14). Do not invent or rename any event, field, scope or entity beyond what is listed here; if implementation shows a gap, amend this proposal (new revision) and stop for approval (Spec "How to use", Claude Code item 2). Until approval, LawDocs runs only v1.1 contracts and the logged manual interim channel (P19 FR-P19-27).

---

## Y.1 Proposal header

| Field | Value |
|---|---|
| Proposal id | `2026-10-25-add-lawdocs-ld` |
| Title | Register LawDocs (owner code `LD`) as an ecosystem product; add legal-work entities, the `legal`, `esign`, `ip` and `engagement` event domains, LawDocs scopes and archive profiles; add service-order, marketplace-transfer and Operations Hub delivery, customer-success, content and grievance contracts; add cross-product customer sign-in by token exchange; amend routing rules for same-organisation legal systems of record; add the Consumer Help wall and the eSign non-sharing principle |
| Proposer | LawDocs product owner (Company Secretary, Infrabyx Group) |
| Target version | Specification **v1.2** — **minor** (Part 14.1): new owner code, product value, entities, events, APIs, optional fields, code-table values, layouts, scopes and principles; no published schema changes meaning, ownership or a mandatory field |
| Affected owners (approval required) | Finbyx, Udofin, Operations Hub, Equator Resolution, LawDocsComply, Recovery Suite/Udolex (consumer additions only) |
| Not affected | Field-investigation app; third-party connectors (except one new certification test, §Y.13) |
| Related LawDocs pack files | P19, Appendix I (§I.8 event mapping), Appendix K (`LD-EXPORT-1.0`), Appendix X (Operations Hub and LawDocsComply addenda), master §18–§19 (X-05, X-08, X-13); conventions §5 and §14 (research record only) |
| Rollout | §Y.15 |
| Rollback | §Y.15 |

**Approval record (to be completed in the pull request).**

| Owner | Decision | Date | Conditions |
|---|---|---|---|
| Finbyx | | | |
| Udofin | | | |
| Operations Hub | | | |
| Equator Resolution | | | |
| LawDocsComply | | | |
| Recovery Suite / Udolex | | | |

---

## Y.2 Motivation and regulatory basis

**Motivation.** Specification v1.1 lists Finbyx, Udofin, the Operations Hub, Equator, LawDocsComply, the Recovery Suite and third parties, but not LawDocs. LawDocs appears only as a template supplier and the public face of the professional directory (Part 4.6, "Other group products") and as a legal-tech data source (Part 10.2). The owner's brief requires LawDocs to connect "with Finbyx, Udofin, Equator, LawDocsComply and third-party systems" with "proper APIs and gateways" (LawDocs R-002, R-003) and to share data "across ecosystem apps both ways" (R-023). Owner decision D-10 (25 October 2026) makes LawDocs the system of record for legal work — contract lifecycle, eSign and eStamp, Legal Vault, litigation and IP tracking, notices and pleadings, legal engagements — and LawDocsComply the system of record for compliance, governance and client HRMS. Without an owner code, entities and events, every LawDocs exchange would be improvised, which the Specification forbids (principle 1; "How to use").

**Regulatory basis for the design choices in this proposal.**

| Choice | Basis |
|---|---|
| eSign capability is never shared between products (principle 15) | IT Act 2000 s.3A and Second Schedule; CCA eSign FAQ — an ASP may integrate eSign "only for applications owned or operated by them", and signer consent and logs stay with the ASP (LawDocs R3 LG-001, LG-004, LG-007) [LAW] |
| Instrument eligibility before signing | IT Act First Schedule as amended by S.O. 4720(E), 26 Sep 2022 (R3 LG-003) [LAW]; Registration Act 1908 s.17 (R3 LG-104) |
| Stamp before sign; authorised channels | Indian Stamp Act 1899 s.17, s.35 and State Acts; SHCIL as CRA (R3 LG-096–LG-100) [LAW] |
| Evidence by reference with hashes | Bharatiya Sakshya Adhiniyam 2023 s.63(4) and Schedule; *Pune Bar Assn. v. UoI* (SC, 22 May 2026) (R3 LG-091) [VERIFY: citation] |
| Purpose-bound, consented sharing | DPDP Act 2023 ss.5–8 and Rules 2025 (R3 LG-061–LG-065) [LAW]; Spec principle 5 |
| Party-initiated ADR referrals need a basis | Arbitration and Conciliation Act 1996 s.7, s.7(4)(b), s.12; *Perkins Eastman v HSCC* (2020) 20 SCC 760; *CORE v ECI-SPIC-SMO-MCML (JV)* (SC, 8 Nov 2024) (Spec §8.2) [LAW] |
| Directory limited to Rule 36 fields; no paid ranking | BCI Rules Part VI Ch II Rule 36; Madras HC, 3 Jul 2024 (R3 LG-111, LG-113) [LAW] |
| DigiLocker access not extended to sister products | DigiLocker Requester Terms of Use (2 Jun 2025) cl.17 (R3 LG-038) |
| Consumer Help wall | Conflict of interest between a consumer-grievance service and the group's lender and insurer clients; LawDocs NN-23, D-06 [INTERP] [COUNSEL] |
| Marketplace transfers instructed by LawDocs but held and executed only by OH8 through Razorpay Route | RBI Master Directions on Regulation of Payment Aggregators (15 Sep 2025) (R3 LG-145) [LAW] [VERIFY: paragraph references]; LawDocs never pools third-party money (LawDocs NN-22) |
| B2C billing identity to the Hub | GST invoicing obligations for supplies to individuals (CGST Rules r.46) handled by OH8 under D-11 [INTERP] [TAX MEMO] |

---

## Y.3 Registrations in Parts 1, 3, 4 and 5

**Y.3.1 Part 1 product table — add row.**

| Product or party | Role | Regulatory position | System of record for |
|---|---|---|---|
| **LawDocs** (`lawdocs.in`; web and iOS/Android apps) | Legal-documents and legal-operations platform for individuals and companies: drafting and templates, contract lifecycle, eSign and eStamp execution, Legal Vault, litigation and IP tracking, notices and pleadings, legal department tools, marketplace of legal and compliance services; operates a separately branded Consumer Help service behind an ethical wall | Technology platform and intermediary for user content [INTERP]; eSign only through a licensed ESP, via a contracted aggregator acting as Application Service Provider or LawDocs' own ASP arrangement (`asp_mode` per vendor), never sublet; DigiLocker Requester; e-commerce entity for its marketplace [INTERP]; does not practise law (Advocates Act 1961 ss.29, 33) — reserved services are delivered by practitioners under direct engagement | Agreements and their versions; signing requests and eSign evidence (as ASP); stamp instruments it procured or attached; Legal Vault documents; legal matters and the court cases it tracks; IP assets; contract obligations; engagements and retainers (operational records — commercial records stay with OH) |

**Y.3.2 Part 3.2 envelope.** Add `lawdocs` to the `source` product list: `urn:infrabyx:lawdocs:[tenantid]`. Consumer Help uses the same product and never publishes a cross-product event (principle 14); its brand and legal-entity profile are LawDocs-internal.

**Y.3.3 Part 4.1 links — add four link types.**

| Link | Parties | Fields | Purpose |
|---|---|---|---|
| `legal_sor_link` | One organisation's tenants in LD and LDC (same `org_id`) | org_id, LD tenant, LDC tenant, kernel choices (`GOVERNANCE` → LD or LDC; `HRMS` → LD or LDC; `LEGAL` → LD, or LDC P26 only where no LD tenant exists), effective dates, migration state, approvals (both tenants' admins, maker-checker) | Decides which product is system of record per kernel and authorises the projections in §Y.7.1 and §Y.7.6 |
| `signing_handoff_link` | An organisation's tenant in a requesting product (e.g., Finbyx) and the same organisation's LD tenant | org_id, requesting tenant, LD tenant, OAuth client id, document classes, valid_from, valid_to, approver (LD tenant admin) | Lets the requesting product create LawDocs-hosted signing requests in the organisation's own LD tenant (principle 15) |
| `deposit_link` | One individual's accounts in a depositing product (e.g., Udofin) and LD | pairwise link ref, depositor client id, LD folder, valid_from, revoked_at | Opt-in deposit of the individual's own documents into their Legal Vault (§Y.8) |
| `finbyx_legal_link` | An RE's Finbyx tenant and the same RE's LD tenant | reid, org_id, both tenants, permitted contracts (template packs, `DocumentShared` to recovery cases, litigation projection), approvals | Lets the RE's legal department see recovery litigation and share drafted documents |

**Y.3.4 Part 4.2 and 4.6 identity.** LawDocs keeps realm `ld` (customers, counterparties, professionals) and staff realm `ld-staff`, provisioned by SCIM from OH10 with `group_grant` memberships (Spec §4.6). Add to the Equator wall (Part 4.6, "Equator neutrality wall"): no `group_grant` combines an Equator case-level role with a LawDocs delivery role (`OPS_RM`, `OPS_PROFESSIONAL`, `OPS_DELIVERY_LEAD`, `OPS_CONSUMER_CASE_MANAGER`) for the same party.

**Y.3.5 Part 5.1 owners.** Add owner code **`LD` — LawDocs**. Add `LAWDOCS` to the `product` enumeration of `TenantProvisioned` (Part 6.29) and to `module.yaml` `product` values (Part 11.1).

**Y.3.6 Part 4.4 cross-product customer sign-in by token exchange (N12+; LawDocs OI-P01-12).** Register LawDocs as both a launch source and a launch target of the Part 4.4 launch pattern for **customers of the same organisation** (realm `ld`), in addition to the organisation's own enterprise IdP federated into both products (preferred). Rules:

| Rule | Detail |
|---|---|
| Mechanism | OAuth 2.0 Token Exchange (RFC 8693) at the **target** product's identity provider; the source presents a short-lived subject token (≤ 60 s, audience = target product, single use, `jti` logged); the target issues its own session — no session, cookie or refresh token is shared |
| Subject | Pairwise subject identifier per product pair; the target resolves it to an existing account of the same person in the same organisation (`org_id` match) or offers sign-up; never creates a membership or role by itself |
| Assurance | Target applies its own step-up (OTP or passkey) before any legal-effect action; Aadhaar is never a login method on either side (LawDocs NN-03) |
| Scope of launch | Deep link to a named screen (e.g., "open this signing request", "open this agreement projection"); no data travels in the token beyond `org_id`, pairwise subject, `acr` and the deep-link target |
| Excluded | Consumer Help (principle 14) is never a source or target; staff realms (`ld-staff`) use `group_grant` and SCIM (Part 4.6), not this flow; Equator case-level roles follow Part 4.6 neutrality |
| Evidence | Both products log launch id, time, subject pair, target and outcome; sharing-ledger entry with `legalbasis = CONTRACT_PERFORMANCE_CUSTOMER` or the customer's `consentref` |

---

## Y.4 Principles (Part 2) — add two

14. **Consumer Help data is walled.** LawDocs' Consumer Help service (loan, lending and insurance grievances, credit-report disputes, challans, vehicle matters) keeps its case data in class `CONSUMER_HELP` (§Y.6.3). No cross-product schema may declare it; gateways reject any message carrying it; it never reaches Finbyx, Udofin, Equator, LawDocsComply, the Operations Hub (except anonymous counts) or any RE archive; no product may refer, route or advertise to it.
15. **eSign capability is never shared.** No product calls another product's ESP or ASP route, receives its ESP credentials, or frames its ceremony. A user of one product signs through another product only as that product's own customer, in its own tenant and under its consent screen; signer consent and eSign logs stay with the hosting ASP; the requesting product receives status and evidence by document reference (§Y.7.2).

---

## Y.5 Canonical data model (Part 5.2)

**Y.5.1 New entities.** All carry Part 5.1 fields (`id`, `reid` or `none`, `tenantid`, `owner_system`, `version`, timestamps, `source_refs[]`) and `x-dataclass` per field.

| # | Entity | Owner | Key fields (beyond 5.1) | Copies |
|---|---|---|---|---|
| 46 | `agreement` | LD | business ref (`LD-AGR-…`), type, title, party_refs with roles, governing law, value (money), term, status (DRAFT, NEGOTIATION, APPROVED, EXECUTED, AMENDED, TERMINATED, EXPIRED), executed_at, formalities record (stamp, witnesses, registration, board approval), dispute clause (institution, seat, rules ref), document version refs (#28), stamp refs (#48) | LDC (projection under `legal_sor_link`), FX (when linked to a recovery case), EQ (only inside a referral pack) |
| 47 | `signing_request` | LD (hosting platform; ASP of record per route `asp_mode`) | document_id and sha256 (final, stamped), eligibility result and rule version, signers (pseudonymous refs, order, `signing_method`), ESP route, status, ESP transaction ids, evidence-pack ref, requesting product and link ref | Requesting product (status and evidence by reference) |
| 48 | `stamp_instrument` | LD (procurer or attacher) | State, article, consideration, duty (money), `stamp_channel`, certificate number/UIN, first party, purchase date, verification status and method, lock status, linked document sha256 | Requesting product; EQ (inside a referral pack) |
| 49 | `legal_matter` | The organisation's legal system of record: LD; LDC P26 only for organisations without an LD tenant (recorded in `legal_sor_link`) | business ref (`LD-MAT-…`), `legal_matter_type`, status, risk rating, claim amount and contingent-liability band (FINANCIAL), counsel refs (#42), linked agreements (#46), court cases (#50), ADR cases (#23), privileged flag | LDC (projection) |
| 50 | `court_case` | LD | business ref (`LD-CAS-…`), forum, court, State, case type, number, year, CNR, party role, stage, next date, `court_case_source`, as_of, linked `litigation_case` ref (#24) where the same proceeding is a recovery proceeding in RS; child records hearings and orders | LDC (projection) |
| 51 | `ip_asset` | LD | business ref (`LD-TMK-…`), `ip_asset_type`, office, application number, mark or title, classes, `ip_status`, filing, advertisement, registration and renewal dates, source, as_of | LDC (opt-in projection) |
| 52 | `engagement` | LD (operational); OH (order, invoice, payment) | business ref (`LD-ENG-…`), service id, `supplier_type`, professional ref (#42) or LawDocs, client org/tenant, SLA tier, status, dates; scope description and deliverables stay LD-internal (`CONFIDENTIAL`) | OH (commercial fields only) |
| 53 | `retainer` | LD (operational); OH (contract, invoices) | engagement refs, hour bank, SLA (eSigned document ref), term, renewal, delivery-grant refs | OH (commercial fields only) |
| 54 | `contract_obligation` | LD | agreement ref, obligation type (PAYMENT, DELIVERY, REPORTING, INSURANCE, NOTICE, RENEWAL, CONFIDENTIALITY, OTHER), owner position, due rule, next due date, status, evidence ref | LDC (projection) |

**Y.5.2 Amendments to existing entities (additive).**

| # | Entity | Change |
|---|---|---|
| 20 | `notice` | Add LD as producer **for non-recovery instruments only**; add instrument codes `GENERAL_LEGAL_NOTICE`, `CONTRACT_NOTICE`, `REPLY_NOTICE`, `CONSUMER_NOTICE`. Recovery instruments (LRN, S13_2, S13_4, S138 by an RE, ARB_S21 for loans, etc.) remain RS only |
| 23 | `adr_case` | Owner column "EQ docket; RS referral" becomes "EQ docket; RS or LD referral"; Copies add LD (party view) |
| 24 | `litigation_case` | Owner unchanged (RS). Copies add LD (read-only projection for the RE's own legal department under `finbyx_legal_link`) |
| 25 | `hearing`, `order` | Unchanged. LawDocs hearings and orders are child records of #50 |
| 28 | `document` | Add optional fields: `origin` (`document_origin`), `vault_scope` (PERSONAL, COMPANY), `rendition_of` (source document id for derived renditions — OCR, type copy, translation), `evidence_pack_ref`, `privileged` (bool), `bsa63_certificate_ref`. This **reconciles the proposed `vault_document`**: no new entity; a vault document is a `document` with `vault_scope` set |
| 29 | `consent_artefact` | Capturer adds LD; `method` adds `IN_APP_AUTHORISATION` (OAuth consent screen) and `CONSENT_MANAGER` (DPDP consent-manager artefact); purpose codes add `DOCUMENT_COPY_TO_PERSONAL_VAULT`, `ADR_REFERRAL_PACK`, `LEGAL_SOR_SYNC`, `SIGNING_HANDOFF`, `PARTNER_ONBOARDING_PREFILL` |
| 38 | `plan`, `entitlement`, `invoice`, `subscription_payment` | Copies add LD |
| 39 | `usage_aggregate` | Producers add LD |
| 40, 41 | `export_job`, `archive`, `storage_target` | LD as producing product; folder profiles in §Y.11 |
| 42 | `professional`, `matter_allocation` | `professional` copies add LD (Rule 36 fields only, for directory display that is OFF by default). `matter_allocation` producers add LD for engagements of advocates by organisations through the LawDocs marketplace; optional `org_id` where the client has no `reid`; allocation basis adds `CLIENT_CHOICE` |
| 44 | `group_grant` | LD staff realm added as a consumer (SCIM) |

**Y.5.3 Why `court_case` is a new entity and not an extension of #24.** Principle 2 allows one owner per entity per tenant. An RE tenant using both the Recovery Suite and LawDocs would otherwise have two owners of `litigation_case` in one tenant. Keeping #24 for RS recovery proceedings and #50 for all other proceedings, linked by reference when both describe the same case, preserves single ownership; RS wins for recovery fields, LD shows its projection.

---

## Y.6 Code tables, legal bases and data classes

**Y.6.1 New code tables (Part 5.3).**

| Code table | Values |
|---|---|
| `instrument_eligibility_result` | ELIGIBLE_ESIGN, ELIGIBLE_DSC_ONLY, WET_INK_REQUIRED (IT Act First Schedule), REGISTRATION_REQUIRED (Registration Act s.17), NOTARISATION_REQUIRED |
| `signing_method` | AADHAAR_OTP_ESIGN, AADHAAR_BIO_ESIGN, ACCOUNT_ESIGN (eSign API 3.x), DSC, E_ACCEPTANCE_OTP (IT Act s.10A; not an electronic signature), WET_INK |
| `stamp_channel` | SHCIL, STATE_PORTAL, GRAS, FRANKING, PHYSICAL, NESL_DDE |
| `stamp_verification_method` | VENDOR_API, CRA_PUBLIC_CHECK_HUMAN, SUB_REGISTRAR_LOCK |
| `legal_matter_type` | ADVISORY, CONTRACT_DISPUTE, LITIGATION, NOTICE, REGULATORY, IP, EMPLOYMENT, PROPERTY, CONSUMER, FAMILY, CRIMINAL_COMPLAINT, OTHER |
| `court_case_source` | LICENSED_AGGREGATOR, USER_ENTERED, OFFICIAL_API_CLIENT_CREDENTIALS |
| `ip_asset_type` | TRADEMARK, PATENT, DESIGN, COPYRIGHT, GEOGRAPHICAL_INDICATION |
| `ip_status` | FILED, FORMALITIES_DEFECT, UNDER_EXAMINATION, OBJECTED, HEARING_SCHEDULED, ACCEPTED_ADVERTISED, OPPOSED, REGISTERED, RENEWAL_DUE, REFUSED, ABANDONED, WITHDRAWN, REMOVED (mapped from IP India status labels; LawDocs R1 §7.2) |
| `supplier_type` | LAWDOCS, ADVOCATE, CHARTERED_ACCOUNTANT, COMPANY_SECRETARY, COST_ACCOUNTANT, TRADEMARK_AGENT, NON_REGULATED_PROVIDER, GOVERNMENT_FEE, STAMP_DUTY_PURE_AGENT |
| `dispute_origin` | LOAN (RS path only), CONTRACT, CONSUMER, EMPLOYMENT, PROPERTY, COMMERCIAL_OTHER, FAMILY_PROPERTY |
| `document_origin` | USER_UPLOAD, DIGILOCKER_URI, PRODUCED, SIGNED, RECEIVED_FROM_PRODUCT, DEPOSITED |

**Y.6.2 Legal basis (Part 3.2).** Add `CONTRACT_PERFORMANCE_CUSTOMER`: the billing identity of an individual customer buying from an Infrabyx company, sent only to OH8 billing subjects for quotes, orders, tax invoices, credit notes and refunds. **Permitted fields (closed list; LawDocs X-13):** name, email, phone (mobile), GSTIN (optional), billing address and billing State (place of supply; address optional where the invoice rules allow), amounts and tax lines, SKU and quantity. Never vault, matter, case, document, consumer-case, respondent-institution, grievance-narrative or credential data. **Consumer Help purchases** use the same basis and the same closed list, invoiced by the Consumer Help selling entity (OH1 entity scope, LawDocs Appendix X §X.1): SKUs are generic service codes (e.g., `CH-LETTER-DRAFT`, `CH-CASE-MANAGED`) that name neither the respondent institution nor the vertical detail; any field outside the list in a Consumer Help billing payload is rejected with `dataclass-not-permitted` (principle 14). [OWNER] [TAX MEMO] [COUNSEL] — DPO sign-off required before the first B2C invoice.

**Y.6.3 Data classes (Part 13.2).**

| Change | Rule |
|---|---|
| New class `CONSUMER_HELP` | LawDocs Consumer Help case data. LawDocs' separate store only; no cross-product schema may declare it; gateways reject any message carrying it (`dataclass-not-permitted`); never in any RE archive; counts only to OH (principle 14) |
| Field annotation `x-privileged: true` on `LEGAL` fields | Privileged advice and litigation strategy. Leaves the producing product only with the holder's explicit per-record approval (RS: counsel; LD: the tenant's `ORG_CLO` or the individual) — extends the existing `LEGAL` rule |
| Operations Hub ceiling exception | OH subjects keep the `INTERNAL` ceiling from product sources, **except** named billing fields of `POST /v1/billing/quotes` and `POST /v1/billing/orders` (`buyer_billing_identity.*`) which may carry `PII` when `legalbasis = CONTRACT_PERFORMANCE_CUSTOMER` (§Y.6.2). Certification adds a test that any other PII field to OH is rejected (§Y.13) |

---

## Y.7 Event catalogue additions (Part 6)

Columns as Part 6.1. Tag **(N12)** = new canonical name in v1.2; **(N12+)** = API or field added in v1.2. All new events carry `productfamily = na` and `reid = none` unless an RE tenant's own record is concerned.

### Y.7.1 Legal work (`legal`)

**Routing rule.** `legal` events are **organisation-internal**: they reach only the same organisation's tenants in other products under `legal_sor_link` or `finbyx_legal_link`; never the Operations Hub, never another organisation, never Equator except as documents inside a referral pack, never Consumer Help. Gateways refuse other subscriptions at registration.

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `AgreementExecuted` (N12) signed | LD → LDC; FX (if linked to a recovery case) | Formalities gate passed | agreement id, business ref, type, parties (pseudonymous refs and roles), executed_at, document ref and sha256, stamp refs, dispute clause | LD | (agreement_id, version) | std |
| `AgreementAmended` (N12) | LD → same | Amendment executed | agreement id, amendment ref, effective date, document ref | LD | (agreement_id, version) | std |
| `AgreementTerminated` (N12) | LD → same | Termination or expiry recorded | agreement id, reason class, effective date | LD | (agreement_id, version) | std |
| `ContractObligationRegistered` (N12) | LD → LDC | Obligation created or extracted and confirmed | obligation id, agreement id, type, owner position, due rule, next due | LD | (obligation_id, version) | std |
| `ContractObligationStatusChanged` (N12) | LD → LDC | Status change (DUE, MET, BREACHED, WAIVED) | obligation id, status, evidence ref | LD | (obligation_id, seq) | std |
| `LegalMatterOpened` (N12) | LD → LDC | Matter created | matter id, business ref, type, risk rating, claim amount band | LD | matter_id | ≤ 1 working day |
| `LegalMatterUpdated` (N12) | LD → LDC | Material change (risk, amount, counsel, status) | matter id, changed fields, contingent-liability band | LD | (matter_id, seq) | ≤ 1 working day |
| `LegalMatterClosed` (N12) | LD → LDC | Closure | matter id, outcome class, amount | LD | matter_id | ≤ 1 working day |
| `CourtCaseRegistered` (N12) | LD → LDC | Case added (CNR, number, aggregator match) | case id, forum, court, case type, number, CNR, role, source, as_of, linked litigation_case ref | LD | court_case_id | ≤ 1 working day |
| `CourtCaseUpdated` (N12) | LD → LDC | Stage, status or next date change | case id, stage, next date, source, as_of | LD | (court_case_id, seq) | ≤ 1 working day |
| `CourtHearingScheduled` (N12) | LD → LDC | Next date recorded | case id, date, purpose, source | LD | (court_case_id, date) | Same day |
| `CourtOrderRecorded` (N12) signed | LD → LDC | Order added and verified by the user | case id, order type (`order` code table, Part 5.2 #25), directions with due dates, document ref and sha256 | LD | (court_case_id, order_id) | ≤ 1 working day |
| API `GET /v1/legal-matters?updated_since=` (N12+) | LDC → LD | Reconciliation and pull | matters with projections by scope | LD | n/a | p95 ≤ 800 ms |
| API `GET /v1/court-cases?updated_since=` (N12+) | LDC → LD | Same | cases | LD | n/a | p95 ≤ 800 ms |
| API `GET /v1/contract-obligations?updated_since=` (N12+) | LDC → LD | Same | obligations | LD | n/a | p95 ≤ 800 ms |
| API `GET /v1/agreements/{id}` (N12+) | LDC, FX (linked) → LD | Display | projection by scope; documents by reference | LD | n/a | p95 ≤ 800 ms |

### Y.7.2 Signing and stamping (`esign`)

**Relationship to existing events.** `ESignCompleted` and `EStampCompleted` (Part 6.2, UD → FX) are unchanged and remain the loan-journey evidence events; LD never produces them. The `esign` domain is used only when an organisation uses LawDocs, as its own customer, to execute a document requested from another of its products under `signing_handoff_link` (principle 15).

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| API `POST /v1/signing-requests` (N12+) | Requesting product (e.g., FX) → LD | Create a LawDocs-hosted signing request in the organisation's own LD tenant | document ref and sha256, signer refs and methods, order, deadline, link ref; returns signing_request_id and status (no signing URLs to the caller) | LD | Idempotency-Key | ≤ 2 s; eligibility result ≤ 5 s |
| API `GET /v1/signing-requests/{id}` (N12+) | Requester → LD | Status | status, signer statuses, evidence-pack ref when complete | LD | n/a | p95 ≤ 800 ms |
| API `POST /v1/signing-requests/{id}/withdrawal` (N12+) | Requester → LD | Withdraw before completion | reason | LD | Idempotency-Key | ≤ 2 s |
| `SigningRequestCreated` (N12) | LD → requester | Eligibility passed and invitations sent; or WET_INK_REQUIRED returned | signing_request_id, `instrument_eligibility_result`, rule version | LD | signing_request_id | std |
| `SigningRequestCompleted` (N12) signed | LD → requester | All signatures applied and validated | signing_request_id, document ref and signed sha256, ESP transaction ids, certificate summary, `signing_method` per signer, evidence-pack ref; never consent logs or ESP request XML | LD | (signing_request_id, version) | std |
| `SigningRequestDeclined` (N12) | LD → requester | A signer declined | signing_request_id, signer ref | LD | (signing_request_id, signer_ref) | std |
| `SigningRequestExpired` (N12) | LD → requester | Deadline passed | signing_request_id | LD | signing_request_id | std |
| `SigningRequestWithdrawn` (N12) | LD → requester | Withdrawn by requester or tenant | signing_request_id, actor class | LD | signing_request_id | std |
| `StampInstrumentVerified` (N12) signed | LD → requester | Stamp certificate attached and UIN verified | stamp id, State, article, duty, certificate no, `stamp_verification_method`, linked document sha256 | LD | (stamp_id, version) | std |

### Y.7.3 IP assets and engagements (`ip`, `engagement`)

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `IpAssetRegistered` (N12) | LD → LDC (opt-in, organisation-internal) | Asset added | asset id, type, office, application number, classes, status, source | LD | ip_asset_id | std |
| `IpAssetStatusChanged` (N12) | LD → LDC | Status change | asset id, status, next deadline type and date, source, as_of | LD | (ip_asset_id, seq) | std |
| `EngagementCreated` (N12) | LD → OH | Engagement confirmed | engagement id, org_id or tenant, service SKU, `supplier_type`, SLA tier, value (money), start; never scope text, matter or party data | LD | engagement_id | std |
| `EngagementStatusChanged` (N12) | LD → OH | Status change (ACTIVE, ON_HOLD, COMPLETED, CANCELLED) | engagement id, status, effective_at | LD | (engagement_id, seq) | std |
| `RetainerActivated` (N12) | LD → OH | Retainer SLA executed | retainer id, engagement refs, term, hour bank, SLA document ref (hash only) | LD | retainer_id | std |
| `RetainerEnded` (N12) | LD → OH | Term end, termination or non-renewal | retainer id, reason class, effective_at | LD | retainer_id | std |

Engagement events are commercial-adjacent records under `INTERNAL`; OH8 continues to own orders, invoices and payments (Part 6.27).

### Y.7.4 ADR (`adr`) — changes for party-initiated referrals

| Change | Detail |
|---|---|
| `ADRReferralCreated` producer | Add LD for **non-loan disputes** where the LawDocs user (individual or organisation) is a party. LD can never refer an RE's loan dispute (`regulatory-guard`); Part 8.1 "only the RE refers" remains the rule for loan disputes |
| New optional fields (N12+) | `dispute_origin` (§Y.6.1), `referring_party_role` (CLAIMANT, RESPONDENT, JOINT), `referrer_product` (RS, LD) |
| New scope | `adr.referral:create.party` — issued only to LD (§Y.9); existing `adr.referral:create` unchanged (RE systems only) |
| LD gates before referral (logged) | Arbitration only with a clause naming an institution or written post-dispute consent (A&C Act s.7, s.7(4)(b)); no unilateral appointment (*Perkins Eastman*; *CORE*); non-arbitrable categories blocked (matrimonial status, custody, testamentary validity, criminal matters, insolvency in rem, *Vidya Drolia* tests); a pending consumer complaint cannot be compelled to arbitration (*Emaar MGF v Aftab Singh*); IBC moratorium where known; commercial suits route through Commercial Courts Act s.12A pre-institution mediation (statutory authorities, not Equator) where the user intends to sue without urgent relief |
| Consumers | Add LD (party view, projection subject `[EventName].party`) for `ADRCaseStatusChanged`, `ADRHearingScheduled`, `ADRNeutralAppointed` (name only), `ADROutcomeRecorded` (summary and document reference); LD never receives hearing content, selection logs, mandates or other parties' documents (Parts 4.4, 8.4) |
| Disclosure | Every LD screen presenting Equator states "Equator Resolution is an Infrabyx group company" and shows other configured providers (Part 8.1) |
| Provider neutrality | In LawDocs, Equator is **one ODR provider** behind LawDocs' provider-neutral `ODR_PORT` (adapters for other institutions run as API, webhook, file or portal-manual routes). Equator is never pre-selected, default or mandatory; the user (or both parties under the clause) chooses the institution; ordering of providers is neutral; a model clause naming Equator is offered only alongside clauses naming other institutions |
| eSign | Equator signs awards and settlement agreements through its own ESP route; where a LawDocs user executes a settlement in LawDocs, it is a LawDocs-hosted ceremony in the user's own tenant and Equator receives the evidence by document reference only (principle 15) |

### Y.7.5 Litigation (`litigation`) — consumer additions

Add LD as a consumer of `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled`, `OrderRecorded` and `LitigationCaseClosed` through a new projection subject `[EventName].legal`, delivered only to the RE's own LD tenant under `finbyx_legal_link` with scope `litigation.case:read.legal` and `legalbasis = LEGAL_CLAIM`. RS remains owner; LD shows a read-only projection. No producer or schema change.

### Y.7.6 Governance (`governance`) — routing amendment

Amend Part 6.23 tenant-internal routing **rule 1** by adding: "…except to the **same organisation's legal system of record** (LawDocs) under an active `legal_sor_link`, limited to `BoardMeetingScheduled`, `ResolutionPassed` and `KmpChanged`, for checking execution formalities and signing authority." Add producers: LDC for the same three events where LDC is the organisation's governance system of record (today only FX produces them). Add APIs:

| API | Caller → server | Purpose | Scope | SLA |
|---|---|---|---|---|
| `GET /v1/governance/resolutions?updated_since=` (N12+) | LD → LDC or FX | Resolutions by subject code and date for the formalities gate | `governance.resolution:read` | p95 ≤ 800 ms |
| `GET /v1/governance/kmp` (N12+) | LD → LDC or FX | Current directors, KMP and authorised signatories (role, DIN for directors, effective dates; never PAN or date of birth) | `governance.kmp:read` | p95 ≤ 800 ms |

Workforce events are unchanged; LD reads only a minimal people projection through the HRMS system of record's API (`hr.employee:read.minimal`), never salary, leave, attendance or identity documents (rule 3).

### Y.7.7 Platform, operations, documents and billing

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `TenantRegistered` (N12) signed | LD → OH | A Company or practitioner tenant created by self-service or partner onboarding (not by `TenantProvisioned`) | tenantid, org identifiers (legal name, constitution, CIN/LLPIN, masked PAN, GSTIN), plan, partner_ref, first-admin work email (`legalbasis = CONTRACT_PERFORMANCE_VENDOR`), activated_at | LD (tenant); OH creates the commercial record | tenantid | ≤ 1 working day |
| `SystemOfRecordSwitched` (N12) signed | LD ↔ LDC | Kernel cutover completed under `legal_sor_link` | org_id, kernel, from product, to product, effective_at, reconciliation report hash | Outgoing product | (org_id, kernel, effective_at) | Same day |
| API `POST /v1/document-deposits` (N12+) | UD (or another approved app, on a delegated user token) → LD | Individual saves own document to their vault | document_id at source, sha256, JWS, document type, consentref; LD fetches bytes from the source `GET /v1/documents/{id}` (Part 6.13) | LD (stored copy); source (original) | Idempotency-Key | Ack ≤ 2 s |
| `DocumentDeposited` (N12) | LD → depositor | Deposit verified and stored | deposit id, source document_id, sha256, status (STORED, REJECTED + reason); never LD folder or account data | LD | (source, document_id) | ≤ 5 min |
| `MarketplacePayoutSettled` (N12) signed | OH → LD | Razorpay Route transfer to a professional's linked account settled for a marketplace order | order ref, line ref, `supplier_type`, transfer id, amount, settled_at; never bank details | OH | transfer_id | ≤ 15 min |
| Fields on `POST /v1/billing/quotes` and `/orders` (N12+) | LD → OH | Marketplace and service orders | `line_items[].supplier_type`, `line_items[].supplier_ref`, `line_items[].pure_agent` (bool), `route_transfers[]` (linked-account ref, amount, on_hold), `buyer_billing_identity` (§Y.6.2) | OH | Idempotency-Key | As Part 6.27 |
| `MarketplaceTransferInstructed` (N12) signed | LD → OH8 | After the order exists, an instruction on an on-hold Route transfer created from `route_transfers[]`: `RELEASE` on deliverable acceptance, deemed acceptance, consult window closed or dispute outcome; `REVERSE` (full or partial) on refund or dispute outcome; `EXTEND_HOLD` while a dispute is open | order ref, line ref, transfer ref, action, amount, reason code, engagement ref (`eng_` id only), milestone seq; never deliverable content, party names or bank details | LD (instruction); OH8 executes and owns the transfer | (eng_id, milestone_seq, attempt) | ≤ 15 min to OH8 acknowledgement; settlement per Razorpay |
| `UsageRecorded` (existing, Part 6.27) — **producer LD added** | LD → OH8 | Usage statement closed for a billing period or credit lot | `usage_aggregate_v1`: tenantid, period, meter code (`ESIGN_AADHAAR`, `ESIGN_OTP`, `ESTAMP_FACILITATION`, `AI_CREDITS`, `AGENT_SEATS`, `COURT_DATA_REFRESH`, `TM_WATCH_MARKS`, `STORAGE_GB_MONTH`, `API_CALLS`, `EXTRA_SEATS_PEAK`, `DATA_ROOMS`), quantity, unit, statement id; counts only, never document or matter identifiers | LD (meter readings); OH8 (rating and invoice) | (tenantid, meter, period, statement_id) | ≤ 1 working day after period close |

LD also implements the existing `PUT /v1/provisioning-requests/{id}`, `GET /v1/tenants/{tenantid}/provisioning-status` and `GET /v1/entitlements?tenant=` contracts (Part 6.27, 6.29) and produces `UsageRecorded`, `ModuleAttached`, `ModuleDetached`, `ReleasePublished`, `ControlEvidenceCollected`, `AccessReviewCompleted` (PLATFORM) and portability events on the same terms as Finbyx and Udofin.

### Y.7.8 Directory (`directory`)

| Change | Detail |
|---|---|
| `MatterAllocated` producer | Add LD for advocates engaged by an organisation through the LawDocs marketplace; optional field `org_id` when no `reid`; basis value `CLIENT_CHOICE`; same prohibitions (no party names, matter or case numbers, amounts) |
| `ProfessionalEmpanelled`, `ProfessionalSuspended` consumers | Add LD |
| API `POST /v1/directory/professionals/applications` (N12+) | LD → OH9: a professional applies through LawDocs; Rule 36 fields, credential documents by reference, consentref; OH9 verifies and empanels |
| API `POST /v1/client-conflicts/check` (N12+) | LD (Consumer Help conflict service only) → OH: input respondent organisation identifiers (legal name, CIN or GSTIN); output `is_group_client` flag and category (LENDER_RE, INSURER, OTHER) and as_of; never contract, value or pipeline data; every call logged |

### Y.7.9 Service orders across products (`ops`)

**Domain choice.** Both events use the existing `ops` domain (Operations Hub order context) so that one name exists across LawDocs, LawDocsComply and the Hub (LawDocs Appendix X §X.15, §X.22). Earlier LawDocs drafts used `compliance.ServiceOrderStatusChanged` and `services.ServiceOrderRouted`; both are superseded (§Y.16). A LawDocs service order is an engagement (`eng_`, `LD-ENG-…`); the OH8 order is the commercial record.

| Event or API | Producer → consumer(s) | Trigger | Key payload fields | Owner | Idempotency key | SLA |
|---|---|---|---|---|---|---|
| `ServiceOrderRouted` (N12) | LD → LDC (via `int`; order context from OH8) | A buyer on the group storefront (lawdocs.in/marketplace) ordered a SKU whose fulfilment product is LDC and payment is confirmed | OH8 order ref, line ref, SKU, fulfilment product (`LDC`), buyer org_id or pairwise customer ref, buyer tenant ref in LDC (if any), required-inputs checklist id, consentref (buyer's consent to pass order context); never LawDocs tenant documents or answers | OH8 (order); LDC (fulfilment) | (order_ref, line_ref) | ≤ 15 min |
| `ServiceOrderStatusChanged` (N12) | LDC → LD (and LD → LDC for LawDocs-fulfilled lines bought in LDC) | Fulfilment status change of a routed line | order ref, line ref, status (ACCEPTED, INPUTS_PENDING, IN_PROGRESS, ON_HOLD, DELIVERED, CLOSED, CANCELLED), status_at, deliverable available (bool; documents stay in the fulfilling product and are opened by the buyer there) | Fulfilling product | (order_ref, line_ref, seq) | ≤ 1 working day |

Both carry `dataclass = INTERNAL`; no Consumer Help order is ever routed (principle 14).

### Y.7.10 Operations Hub delivery, customer-success, content and grievance contracts (`ops`, `billing`)

These events implement LawDocs Appendix X (OH addendum) and reuse the LawDocsComply-proposed contracts where named. All are aggregates or commercial/operational metadata under the `INTERNAL` ceiling; schemas are **closed** (unknown fields rejected) so that no tenant document, matter, case, consumer-case or credential data can be added (LawDocs NN-19).

| Event | Producer → consumer | Trigger | Key payload fields (closed list) | Idempotency key | SLA |
|---|---|---|---|---|---|
| `TenantSelfServeCreated` (N12; reuse LDC proposal) | LD → OH4/OH3 | Self-serve tenant created (not via `TenantProvisioned`) | tenantid, product `LD`, origin (FREE_DRAFT, PRICING, MARKETPLACE, HEALTH_CHECK, RM_INVITE, MOBILE_APP), plan, segment, created_at | tenantid | ≤ 15 min |
| `ClientHealthSignal` (N12; reuse LDC proposal) | LD → OH5 | Daily per Company tenant | tenantid, date, active_users, entitled_seats, documents_created_30d, signatures_completed_30d, matters_tracked, tm_marks_tracked, vault_storage_gb, sla_breaches_30d, open_change_requests, retainer_hours_used_pct, last_meeting_at, renewal_risk_flag (fixed reason codes) | (tenantid, date) | Daily |
| `SurveyResponseRecorded` (N12) | LD → OH5 | CSAT/NPS response submitted | tenantid or pairwise customer ref, survey type, score, sentiment class, engagement ref (id only); free text only when the respondent opts to share it | response id | ≤ 1 h |
| `TimesheetAggregated` (N12) | LD → OH10/OH11 | Daily per staff member | staff id, date, client org id, tenantid, category, engagement id, hours, billable (bool); never task titles or content | (staff_id, date, tenantid, engagement_id) | Daily |
| `DeliveryMetricsMonthly` (N12) | LD → OH10/OH11 | Month close per staff member | staff id, month, tasks completed, SLA attainment %, deliverables accepted first time, rework rate, CSAT, hours vs plan; for appraisal input only — no automated people decisions (LawDocs NN-33) | (staff_id, month) | ≤ 3 working days after month end |
| `ServiceCreditIssued` (N12; reuse LDC proposal) signed | LD → OH8 | Retainer or marketplace SLA breach confirmed for credit | credit ref, order_context (MARKETPLACE_ENGAGEMENT, CONSUMER_HELP_CASE), `eng_` or `grv_` id only, amount, reason code, approver ref (maker-checker) | credit ref | ≤ 1 working day |
| `ContentPublished` (N12) | LD → OH7 | A CMS page, post, video or clip linked to an OH7 calendar item is published (internal source `web.PageVersionPublished`, `hlp.TutorialPublished`, `hlp.ClipExported`) | calendar item id, content kind, public URL, published_at, locale, claims-gate check id | (calendar_item_id, version) | ≤ 15 min |
| `GrievanceStatusChanged` (N12) | LD → OH6 (metadata mirror for MIS) | A grievance in a LawDocs grievance desk (platform, e-commerce, DPDP) changes state | grievance ref, category, channel, received_at, acknowledged_at, status, statutory clock code and due time, closed_at; never complaint text, user content or identity beyond a pairwise ref. Consumer Help grievances mirror only into the Consumer Help entity's own OH scope | (grievance_ref, seq) | ≤ 15 min |
| `EmployeeOffboarded` (existing Part 6.23) — **consumer LD added** | OH10 → LD | Staff leaver | staff id, effective_at | (staff_id, effective_at) | Delivered ≤ 5 min; LawDocs sweep per LawDocs P18 |

---

## Y.8 API summary (LawDocs-served and LawDocs-called)

| API | Server | Caller | Section |
|---|---|---|---|
| `POST /v1/signing-requests`, `GET /v1/signing-requests/{id}`, `POST /v1/signing-requests/{id}/withdrawal` | LD | Requesting product of the same organisation | §Y.7.2 |
| `POST /v1/document-deposits` | LD | Udofin and other approved apps (delegated user token) | §Y.7.7 |
| `GET /v1/legal-matters`, `GET /v1/court-cases`, `GET /v1/contract-obligations`, `GET /v1/agreements/{id}` | LD | LDC; FX (linked agreements) | §Y.7.1 |
| `GET /v1/template-packs/{pack}/versions/{v}` (N12+; signed pack with reviewer of record and effective dates) | LD | FX, LDC, OH (for Infrabyx's own contracts) | — |
| `GET /v1/events?after=&types=` | LD | Any consumer of LD events | Part 3.1 |
| `PUT /v1/provisioning-requests/{id}` | OH | LD | Part 6.29 |
| `GET /v1/tenants/{tenantid}/provisioning-status`, `GET /v1/entitlements?tenant=` | LD | OH | Parts 6.27, 6.29 |
| `POST /v1/adr/referrals` | EQ | LD (scope `adr.referral:create.party`) | §Y.7.4 |
| `GET /v1/governance/resolutions`, `GET /v1/governance/kmp` | LDC or FX | LD | §Y.7.6 |
| `POST /v1/client-conflicts/check`, `POST /v1/directory/professionals/applications` | OH | LD | §Y.7.8 |
| Catalogue, quotes, orders, invoices, usage disputes, support tickets, CRM requests, claims gate | OH | LD | Parts 6.27, 6.29 |
| **LawDocs as caller of OH CRM, ticket and asset-library APIs (N12+ caller registration):** `POST /v1/crm/requests` (talk to sales, enterprise and marketplace quotes), `POST /v1/crm/leads` (lead with consent objects), `POST /v1/crm/activities` (RM activity; reuse LDC proposal; commercial-only classifier + LawDocs matter-term block list), `POST /v1/support/tickets` (redacted ticket text), OH7 asset-library bundle upload for social calendar items [path to be fixed by the OH owner; OI-Y-10] | OH | LD (`int` only) | LawDocs Appendix X §X.2, §X.3, §X.6 |
| `POST /v1/delivery/assignments` (N12+) | LD | OH4 (signed machine client) | LawDocs Appendix X §X.4 |
| `POST /v1/conflicts/check` (extended: LD as client; categories `CONSUMER_HELP_ADVERSE`, `LENDER_CLIENT`) | OH | LD | LawDocs Appendix X §X.10 |
| Token-exchange launch (RFC 8693) at each product's token endpoint | LD and peer product | Peer product and LD | §Y.3.6 |

Ecosystem paths are not module-prefixed. Where LawDocs also offers the same operation to tenant clients under a module path (e.g., `/v1/sgn/signing-requests`), the gateway serves one implementation under both paths (LawDocs ADR); the registry records the ecosystem path as canonical.

---

## Y.9 Scopes (Part 4.5) — rows to add

| Scope | Granted to |
|---|---|
| `ops.provisioning:ack`, `ops.ticket:write`, `crm.request:write`, `billing.quote:write`, `billing.order:write`, `billing.dispute:write`, `billing.catalogue:read`, `ops.claims:check`, `billing.usage:write` | LawDocs product services calling the Hub (the same set Finbyx and Udofin hold; LawDocs runs B2C and B2B checkout on OH8 under D-11) |
| `ops.tenant:provision`, `platform.entitlement:read` | Operations Hub calling LawDocs (existing grantee; LD added as a server) |
| `templates.pack:read` | Finbyx, LawDocsComply, Operations Hub |
| `legal.agreement:read`, `legal.matter:read`, `legal.obligation:read` | LawDocsComply tenant of the same organisation under `legal_sor_link`; Finbyx for linked agreements under `finbyx_legal_link` (`legal.agreement:read` only) |
| `esign.request:create`, `esign.request:read` | A product acting for an organisation in that organisation's own LawDocs tenant under `signing_handoff_link`, approved by the organisation's LawDocs admin with step-up |
| `documents.deposit:write` | Delegated user tokens issued by LawDocs to approved apps (Udofin first) for one individual's chosen folder |
| `litigation.case:read.legal` | The RE's own LawDocs tenant under `finbyx_legal_link` |
| `adr.referral:create.party` | LawDocs only |
| `adr.case:read.party` | Existing scope; LawDocs added |
| `governance.resolution:read`, `governance.kmp:read` | LawDocs under `legal_sor_link` (same organisation) |
| `ops.client_conflict:check` | LawDocs Consumer Help conflict service only |
| `directory.professional:read` | Existing; LawDocs added |
| `directory.allocation:write` | Existing (FX RS, Udolex); LawDocs added for marketplace engagements |
| `directory.application:write` | LawDocs → OH9 |
| `crm.lead:write`, `crm.activity:write`, `ops.asset:write` | LawDocs product services calling OH3 and OH7 (`int` only) |
| `ops.delivery_assignment:write` | Operations Hub OH4 calling LawDocs |
| `ops.conflict:check` | Existing (EQ); LawDocs added for marketplace and delivery conflict checks |

---

## Y.10 Regulated messages (Part 3.6) — add

`AgreementExecuted`, `CourtOrderRecorded`, `SigningRequestCompleted`, `StampInstrumentVerified`, `SystemOfRecordSwitched`, `TenantRegistered`, `MarketplacePayoutSettled`, `MarketplaceTransferInstructed`, `ServiceCreditIssued`. Each carries RFC 9421 in transit and a detached JWS over the CloudEvent, stored with it (Part 3.6).

---

## Y.11 Archive standard (Part 12.1) — register LawDocs profiles and layouts

**Y.11.1 Folder profiles.** Register four profiles — `ld_company_v1`, `ld_individual_v1`, `ld_professional_v1` and `ld_consumer_help_v1` (LawDocs X-08) — implementing `LD-EXPORT-1.0` (LawDocs Appendix K §K.0, §K.3) under `archive_standard_version` 1.0. LawDocs Appendix K is the detailed source; on any difference in folder names, Appendix K governs and this table is corrected in the same revision.

| Profile | Top-level folders after the mandatory `00 Start Here/` |
|---|---|
| `ld_company_v1` | `01 Company Profile`, `02 Agreements and Contracts/<FY>/<Department>/<Agreement folder>/{01 Drafts, 02 Negotiation and Redlines, 03 Signed and Stamped, 04 Evidence and Certificates, 05 Amendments and Renewals, 06 Correspondence}`, `03 Litigation and Disputes/<Year>/<Forum>/<Case folder>`, `04 Trademarks and IP`, `05 Board and Governance/<FY>` (only while LD is governance SoR), `06 Policies and Registers`, `07 People and HR` (restricted archive), `08 Notices and Correspondence`, `09 Services and Engagements`, `10 Billing and Invoices/<FY>`, `11 AI Work Products (labelled)`, `99 System Data (CSV and JSON)` |
| `ld_individual_v1` | `01 My Profile and IDs (masked)`, `02 Property`, `03 Family and Succession`, `04 Employment`, `05 Finance, Loans and Insurance`, `06 Vehicles`, `07 Disputes and Court Cases`, `08 Agreements`, `09 Tax/Tax Year <YYYY-YY>` (legacy alias `AY <YYYY-YY>` for years before 2026-27; LawDocs X-12), `10 Receipts and Invoices`, `99 System Data` |
| `ld_professional_v1` | `01 Practice Profile and Registrations`, `02 Clients and Matters/<Client>/<Matter or engagement> (LD-MAT-… or LD-ENG-…)/{01 Engagement and Terms, 02 Client Documents (only copies the client permitted), 03 Work Product, 04 Court Filings and Orders, 05 Correspondence, 06 Invoices and Payouts}`, `03 Calendar and Hearings`, `04 Templates and Precedents`, `05 Marketplace Engagements and Retainers/<FY>`, `06 Invoices and Payouts/<FY>`, `07 Correspondence`, `11 AI Work Products (labelled)`, `99 System Data (CSV and JSON)`. Person-naming default `masked_name`; client-owned material otherwise appears as reference rows only |
| `ld_consumer_help_v1` | `01 My Profile (masked)`, `02 Loan and Lending Complaints/<Year>/<case folder> (LD-GRV-…)`, `03 Insurance Complaints/<Year>`, `04 Credit Report Disputes/<Year>`, `05 Challans/<Year>`, `06 Vehicles`, `07 Fees and Receipts/<Year>` (Consumer Help fees only; never fines or dues), `99 System Data`. Naming LOCKED to `ids_only` for natural persons (institutions named); produced only for the data principal's own destination; never part of an RE archive, a cross-product share or an OH dataset (principle 14) |

**Y.11.2 Conflicts between `LD-EXPORT-1.0` (as summarised in LawDocs conventions §14) and Part 12.1, with the proposed resolution.**

| Point | Part 12.1 | `LD-EXPORT-1.0` | Proposed resolution |
|---|---|---|---|
| Start folder | `00 Start Here/` mandatory and identical in every profile (README.pdf/.docx/.txt, export-manifest.csv, manifest.json, manifest.json.jws, data dictionary, relationships, code tables, schemas, verifier) | `00 READ ME FIRST.pdf`, `00 Index.xlsx`, `manifest.json`, `checksums.sha256` at the root | LawDocs adds the full `00 Start Here/` folder; keeps `00 READ ME FIRST.pdf` and `00 Index.xlsx` at the root as convenience copies and `checksums.sha256` (same hashes as `export-manifest.csv`) for `sha256sum -c` users. LawDocs Appendix K is aligned (LawDocs X-07) |
| Root name | `[Owner legal name] - [Product] Archive - [scope] - as of [YYYY-MM-DD]/` | `LawDocs Export – <Name> – <YYYY-MM-DD>/` | Adopt the Part 12.1 pattern: `[Owner name] - LawDocs Archive - [scope] - as of [YYYY-MM-DD]/` |
| Names in folders | No personal data in folder or file names (default `ids_only`; `id_and_masked_name` for internal archives) | Counterparty and agreement titles in folder names (e.g., `<Counterparty> – <Agreement title> (LD-AGR-…)`) so the archive is self-explanatory without the tool (LawDocs R-021) | Add naming mode **`owner_readable`** to Part 12.1: allowed only when the recipient is the data owner itself (the tenant or the individual) and the archive is delivered to the owner's own destination; permits counterparty names, titles and business references; never Aadhaar, PAN, account numbers, health data or another person's identifiers. Every archive for a third party (auditor, court, successor, ecosystem product) uses `ids_only` or `id_and_masked_name` |
| Year convention | Not specified | Indian FY for companies, calendar year for individuals | Recorded in the profile's `folder_policy`; canonical dataset paths stay in the manifest (Part 12.1) |

**Y.11.3 Registered layouts (Part 12) — add.**

| Layout | Producer → consumer | Content |
|---|---|---|
| `agreement_register_v1` | LD → archive, LDC, successor | Agreement id, business ref, type, title, parties (refs; names in `owner_readable` only), status, dates, value, governing law, dispute clause, stamp refs, signed document sha256 |
| `signing_evidence_index_v1` | LD → archive, courts, requester | Signing request id, document sha256 before and after signing, signers (refs), method, ESP transaction ids, timestamps, certificate summary, evidence-pack file refs, s.63(4) certificate ref |
| `stamp_register_v1` | LD → archive | Stamp id, State, article, consideration, duty, channel, certificate no/UIN, first party ref, verification method and date, lock status, document sha256 |
| `legal_matter_register_v1` | LD → archive, LDC | Matter id, type, status, risk, claim amount, contingent-liability band, counsel refs, linked agreements, cases, ADR cases |
| `court_case_register_v1` | LD → archive, LDC | Case id, forum, court, number, CNR, role, stage, next date, source, as_of, hearings and orders (refs and hashes) |
| `ip_register_v1` | LD → archive | Asset id, type, office, application number, mark/title, classes, status, dates, source |
| `contract_obligation_register_v1` | LD → archive, LDC | Obligation id, agreement id, type, owner position, due rule, next due, status, evidence ref |
| `engagement_register_v1` | LD → archive, OH (commercial columns only) | Engagement id, service, supplier type, professional ref, SLA tier, status, dates, value |
| `vault_index_v1` | LD → archive | Document id, folder path (canonical and profile), origin, sha256, version, renditions (ids, labels, confidence), legal hold, retention class |
| `sharing_ledger_v1` | LD → archive, auditors | Entry id, time, direction, counterparty product and tenant, link, contract, purpose, consentref or legalbasis, record ids, payload sha256, data class, outcome, previous hash |
| `governance_kernel_export_v1`, `hrms_kernel_export_v1` | LD ↔ LDC (system-of-record switch) | Kernel records as defined by `@infrabyx/governance-kernel` and `@infrabyx/hrms-kernel` [VERIFY: kernel schema versions], with hash-chain heads and control totals |

---

## Y.12 Security, privacy and retention (Part 13) — add

- **Retention (Part 13.3):** eSign evidence (consent version, request and response, ESP transaction ids, certificates, audit trail) ≥ 7 years after the later of signing and account closure (eSign API v3.3 log archiving; Limitation Act 1963 — LawDocs R3 LG-008, LG-092) [REC]; stamp certificates for the life of the instrument plus limitation; court-case records until disposal plus 12 years where a decree may be executed (Limitation Act Art. 136) [REC]; sharing-ledger entries 8 years [REC].
- **Incidents:** a LawDocs incident involving DigiLocker-pulled data starts a 24-hour NeGD notice clock in addition to CERT-In (6 hours) and DPDP duties (R3 LG-038, LG-065, LG-079).
- **Logging:** Part 13.3 logging rule applies; in addition no document content, signer consent payloads or stamp certificate images in logs, traces or DLQ metadata.
- **Keys:** LawDocs' JWKS per environment; detached JWS for documents by reference (Part 3.6).

---

## Y.13 Certification suite (Part 14.3) — new group "Legal-tech boundaries (v1.2)"

| Test | Pass condition |
|---|---|
| eSign non-sharing | No product client can obtain ESP credentials, ASP keys, raw eSign transactions or signing URLs from LD; ceremony pages refuse framing (`frame-ancestors 'none'`); attempts return `regulatory-guard` |
| Eligibility before signing | A `POST /v1/signing-requests` for a will, trust deed, ordinary power of attorney or a promissory note not in favour of a listed regulated entity returns `WET_INK_REQUIRED` and no ESP call is made |
| Stamp before sign | A chargeable instrument without a verified `stamp_instrument` cannot reach READY |
| No loan referrals from LD | `ADRReferralCreated` from LD with `dispute_origin = LOAN` is rejected with `regulatory-guard` |
| Party view only | LD receives no hearing content, selection log, mandate or other parties' documents in any `adr` projection |
| Consumer Help wall | Any message declaring `CONSUMER_HELP` is rejected by every gateway; no subscription to a Consumer Help subject can be registered; a seeded group client returns `is_group_client = true` and nothing else |
| Organisation-internal legal routing | An OH or other-organisation subscription to a `legal` subject is refused at registration and at the gateway |
| Governance exception scope | Governance events reach LD only with an active `legal_sor_link` of the same `org_id`; no other governance event type is delivered |
| OH ceiling exception | Only `buyer_billing_identity.*` fields with `legalbasis = CONTRACT_PERFORMANCE_CUSTOMER` pass to OH as PII; a seeded vault, matter or document id in any OH payload is rejected with `dataclass-not-permitted` |
| Deposits | A deposit whose fetched bytes do not match `sha256` or whose JWS fails is rejected; `WELLNESS` is rejected; LD returns no account or folder data to the depositor |
| Archive profiles | All four LawDocs profiles contain `00 Start Here/`; `owner_readable` names appear only in archives addressed to the owner; an `ld_consumer_help_v1` archive addressed to anyone other than the data principal is refused; the verifier passes and fails on one changed byte |
| Closed OH schemas | A `ClientHealthSignal`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `SurveyResponseRecorded` or `GrievanceStatusChanged` carrying an unknown field (e.g., `document_titles`, `complaint_text`) is rejected by schema |
| Service-order routing | `ServiceOrderRouted` without a buyer `consentref` is rejected; no `ServiceOrderRouted` or `ServiceOrderStatusChanged` exists for a Consumer Help order |
| Transfer instructions | A `MarketplaceTransferInstructed` `RELEASE` replayed with the same idempotency key produces one release; a `RELEASE` for a line under an open dispute is refused |
| Token-exchange launch | A subject token older than 60 s, reused, or with an audience other than the target is refused; the launch creates no role or membership; Consumer Help is never a source or target |

---

## Y.14 Impact note per product

| Product | What changes for it | Mandatory? | Effort (indicative) | Tests to add |
|---|---|---|---|---|
| **Finbyx** | Optional: pull LD template packs; send recovery-litigation projections to the RE's LD tenant (subscription only); receive `DocumentShared` from LD against a recovery case; create LawDocs-hosted signing requests in the RE's LD tenant and consume `SigningRequestCompleted`; serve `GET /v1/governance/resolutions` and `/kmp` to LD where Finbyx GV is the RE's governance SoR. No change to any published Finbyx schema | No (opt-in features) | 1–2 sprints across 16b/16d | Pact with LD; Legal-tech boundaries group (eSign non-sharing, eligibility) |
| **Udofin** | Optional "Save to LawDocs" button using `POST /v1/document-deposits` with a delegated token and its own consent; no grievance, referral or advertising path to Consumer Help (principle 14); wellness store unaffected | No (opt-in) | ≤ 1 sprint | Deposit and Consumer Help wall tests |
| **Operations Hub** | Add `LAWDOCS` product value; LD scope rows (§Y.9); consume `TenantRegistered`, engagement and retainer events; `CONTRACT_PERFORMANCE_CUSTOMER` basis and billing-identity ceiling exception; order line-item and Route transfer fields; produce `MarketplacePayoutSettled`; execute `MarketplaceTransferInstructed`; consume LD `UsageRecorded`, `ServiceCreditIssued`, `TenantSelfServeCreated`, `ClientHealthSignal`, `SurveyResponseRecorded`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `ContentPublished` and `GrievanceStatusChanged` (§Y.7.10); deliver `EmployeeOffboarded` to LD; register LD as caller of the CRM, ticket and asset-library APIs and serve OH4 `POST /v1/delivery/assignments` calls to LD (§Y.8); route `ServiceOrderRouted`/`ServiceOrderStatusChanged` order context (§Y.7.9); serve `POST /v1/client-conflicts/check` and `POST /v1/directory/professionals/applications`; accept `MatterAllocated` from LD with `CLIENT_CHOICE`. **Correction to the OH Master Prompt v1.0 adapter table:** "`ESignProvider`: LawDocs eSign (group) [VERIFY API]" is replaced by principle 15 — Infrabyx group companies sign MSAs, DPAs and HR letters as LawDocs customers in their own LD tenants (hosted ceremony), with document and evidence references returned to OH | Yes (D-11 depends on it) | 2–3 sprints across O3–O9 | Aggregates-only group updated; ceiling-exception test; client-conflict API returns flags only |
| **Equator Resolution** | Accept party-initiated referrals from LD (`adr.referral:create.party`), apply its own screening; publish party-view projections to LD; disclose common ownership; add LD delivery roles to its separation-of-duties checks. **Correction to EQ Appendix AC:** the optional `lawdocs_esign` route on Equator's `ESIGN_PORT` is withdrawn under principle 15 — Equator signs awards and settlements through its own ESP | Yes for referrals from LD | 1–2 sprints (EQ P09) | No-loan-referral test; party-view test |
| **LawDocsComply** | Implement `legal_sor_link` and the kernel system-of-record switch; consume `legal` and `ip` projections; serve governance read APIs; pull template packs; consume `ServiceOrderRouted` and produce `ServiceOrderStatusChanged` for LDC SKUs sold on the group storefront (§Y.7.9); support the token-exchange launch for same-organisation customers (§Y.3.6). **Reconciliation:** LDC Pack v1.2 P26 builds a legal-matter register and CLM; where an organisation has an LD tenant, P26 consumes LD projections and does not hold a second register (D-10 of the LawDocs pack); P26 stays SoR only for organisations without LD. **Corrections:** LDC P18 FR-P18-40 lists "LawDocs eSign (group)" as an `ESignProvider` adapter and FR-P18-22 describes LawDocs eSign envelopes — both become hosted signing hand-offs under principle 15 | Yes for joint customers | 2–3 sprints (LDC P18, P26) | Routing and SoR-switch tests |
| **Recovery Suite / Udolex** | Add LD as a consumer of the `.legal` litigation projection; no ownership change | Yes if the RE enables it | < 1 sprint | Projection carries no forbidden fields |
| **Field-investigation app, third-party connectors** | None, except the Consumer Help rejection test | — | — | `CONSUMER_HELP` rejection |

---

## Y.15 Versioning, parallel run, rollout and rollback

- **Classification:** minor (Part 14.1). All new fields are optional; every new subject is new; no existing scope is widened (party referrals use a new scope rather than changing `adr.referral:create`); the two policy amendments (governance rule 1 and the OH ceiling exception) narrow-scope additions that need explicit owner approvals but break no published schema. **No parallel run** is required because no published major changes.
- **Rollout order:** (1) registry entries, schemas, code tables and SDK release; (2) Operations Hub additions and LawDocs core (provisioning, billing, usage) — unblocks D-11; (3) LawDocsComply links, projections and system-of-record switch; (4) Finbyx and Udofin opt-in features; (5) Equator party referrals. Each pair runs sandbox certification (§Y.13 plus existing groups) before production; propagation to every repository within 10 working days of merge (Spec change-control rule).
- **Interim:** until a pair is certified, LawDocs uses the logged manual interim channel (signed packs; sharing-ledger entries with `channel = MANUAL_INTERIM`).
- **Rollback:** disable the relevant subscriptions and links (LawDocs `int.eco.v12_contracts.enabled` OFF and per-link pause); LawDocs records remain intact; consumers mark projections stale with the last `as_of`; no data is deleted; kernel switches in progress roll back with the outgoing product remaining SoR.

---

## Y.16 Superseded and reconciled names

| Name used elsewhere | Canonical in v1.2 |
|---|---|
| "LawDocs eSign (group)" as an `ESignProvider` adapter (OH Master Prompt v1.0; LDC P18 FR-P18-40) | Hosted signing hand-off: `POST /v1/signing-requests` under `signing_handoff_link`; `SigningRequestCompleted` |
| `lawdocs_esign` on Equator `ESIGN_PORT` (EQ Appendix AC) | Withdrawn (principle 15) |
| `vault_document` (draft entity name) | `document` (#28) with `vault_scope` and `origin` |
| LawDocs-internal `in.lawdocs.*` names | Mapped to ecosystem names in LawDocs Appendix I §I.8; internal names are never published to the ecosystem |
| LDC P26 `lit.matters` for organisations with an LD tenant | Projection of `legal_matter` (#49) and `court_case` (#50) |
| `matter_allocation` basis for marketplace choice | `CLIENT_CHOICE` |
| `in.infrabyx.compliance.ServiceOrderStatusChanged` (LawDocs P14 draft) | `in.infrabyx.ops.ServiceOrderStatusChanged.v1` (§Y.7.9) |
| `in.infrabyx.services.ServiceOrderRouted` (LawDocs P16 draft) | `in.infrabyx.ops.ServiceOrderRouted.v1` (§Y.7.9) |
| Internal `in.lawdocs.web.ContentPublished` (LawDocs Appendix X draft) | Internal sources `web.PageVersionPublished`, `hlp.TutorialPublished`, `hlp.ClipExported` → `in.infrabyx.ops.ContentPublished.v1` |
| "Equator as default ADR route" (any draft wording) | Equator is one provider behind `ODR_PORT`; never default or mandatory (§Y.7.4) |

---

## Y.17 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-Y-01 | Approval by all six affected owners (§Y.1) | [OWNER] | Manual interim channel |
| OI-Y-02 | ESP/aggregator confirmation that LawDocs-hosted ceremonies created through a customer's own systems are within ASP terms | [COUNSEL] + procurement | Disable API-initiated signing; UI-only signing |
| OI-Y-03 | `CONTRACT_PERFORMANCE_CUSTOMER` basis and B2C invoicing on OH8 | [OWNER], DPO, [TAX MEMO] | LawDocs issues B2C invoices itself (deviation from D-11) |
| OI-Y-04 | Consumer Help conflict policy when the respondent is a group client | [COUNSEL] | Decline intake; signpost free official routes |
| OI-Y-05 | LDC P26 overlap — agreement between LDC and LawDocs pack leads | Pack leads | Per-organisation choice in `legal_sor_link` |
| OI-Y-06 | Kernel export schema versions for the system-of-record switch | Kernel maintainers | Archive-standard export + import tools |
| OI-Y-07 | `owner_readable` naming mode acceptance by every archive-producing product | Archive-standard owners | LawDocs uses `owner_readable` only for its own customer exports and `ids_only` everywhere else |
| OI-Y-08 | BSA s.63(4) citation and Schedule text in the evidence layout | [VERIFY] | Label certificate drafts "for review by an advocate" |
| OI-Y-09 | Token-exchange launch (§Y.3.6) acceptance by LDC, Finbyx and Udofin identity owners; Part 4.4 parameters (token lifetime, pairwise subject algorithm) | Spec owner + identity owners | Customer's own enterprise IdP federated into both products; otherwise separate sign-in |
| OI-Y-10 | OH7 asset-library upload path and OH3 `crm/leads` field set for LawDocs as caller | OH owner | Manual download and upload by `OPS_CONTENT_PUBLISHER`; `POST /v1/crm/requests` only |
| OI-Y-11 | `ops` as the domain for `ServiceOrderRouted` / `ServiceOrderStatusChanged` (vs a new `engagement`-domain event) | Spec owner + LDC and OH owners | Manual interim order-status updates by the delivery lead |
