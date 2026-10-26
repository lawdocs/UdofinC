# Phase P11 — Return Studio, Data Preparation and Accounting Bridge

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, ledger, object storage with Object Lock, outbox, Temporal);
> - **P01** (roles, step-up MFA, external-access grants);
> - **P02** (settings, rule packs, holiday calendars, delegation matrix);
> - **P03** (instrument catalogue — every return definition cites an instrument version);
> - **P04** (obligations, calendar, tasks, notifications, evidence — every return due instance is also a compliance obligation instance);
> - **P07** (DMS: evidence vault, OCR, PDF extraction);
> - **P18** (integration gateway: Finbyx and Udofin connectors, Tally agent channel, SFTP drop, API keys).
>
> **Sequencing:** P11 starts with the **shared returns kernel** contract (D-05) agreed with the Finbyx team in sprint 1 (interface ADR, package `@infrabyx/returns-kernel` and data packs `infrabyx-returns-packs`). P11 then runs in parallel with P10 (shared snapshot and evidence services) and feeds P09 (ratios, capital, ALM), P06 (annual report and board-pack financials), P10 (PBC items, CARO, AUD checklists, tax-audit packs) and P19 (export).
>
> **Binding appendices:** I (returns, CIC and tax return catalogue), J (accounting, auditing and secretarial standards map), B (data model, events, errors), L (adapters and APIs incl. Tally, Finbyx, Udofin), M (export package — `11 Returns and Regulatory Reporting`, `11 Returns and Regulatory Reporting/Credit Information Companies`, `11 Returns and Regulatory Reporting/Accounts and Tax`), G (rules register — LR-RBI-SR, LR-RBI-CIR, LR-GST, LR-IT, LR-MCA). Ecosystem: Infrabyx Ecosystem Integration Specification v1.1 §§5.2 (entities 30–32), 6.18–6.20, 10.2, 12.1–12.3.
>
> **Requirements covered:** R-048 (RBI returns, CIMS/DAKSH/PRAVAAH, data definitions, supervisory-return directions), R-049 (CIC submissions), R-050 (Tally/Excel import and transformation), R-051 (Ind AS/AS applicability; exports follow standards), R-052 (draw from Finbyx/Udofin/other LMS; export return-ready data), R-053 (data for annual reports and minutes), R-061 (CFO ratios from accounts and loan data), R-077 (return-ready data for RBI, SEBI, IFSCA, GST and tax portals with agentic AI), R-078 (import balance sheets, prior annual reports, books, data dumps, Tally), R-079 (GST/tax exports), R-081 (download), R-013 (maker-checker).
>
> **Estimated effort:** 10 two-week sprints for a squad of 9 (kernel client and registry 2; ingestion and mapping 3; validation, reconciliation and packaging 2; accounting bridge 1; CIC and tax packs 1), plus a regulatory-reporting analyst (ex-bank/NBFC MIS) and a CA for accounting and tax packs.

---

## 1. Objective and business outcome

Indian regulated entities file dozens of periodic, event-based and ad hoc returns to RBI, NABARD, NHB, SEBI, IFSCA, IRDAI, FIU-IND, CERSAI, the GST Network, the income-tax department, the MCA and the four credit information companies (CICs). Compliance teams rarely own the source data; finance, credit and treasury do, often in Tally Prime, Excel and a loan system that may not be Finbyx. This phase gives every tenant a **Return Studio** that turns raw data — wherever it lives — into validated, reconciled, approved, upload-ready files, with the human filer in control and a complete evidence trail.

The design honours three fixed decisions:
1. **Shared kernel (D-05).** Return definitions, cell maps, validation rules and CIC layouts are maintained once, in the Infrabyx returns kernel, and used by both Finbyx and LawDocsComply. LawDocsComply never forks a definition.
2. **Prepare, never file (D-13, NN-08).** LDC generates, validates, reconciles, packages and evidences. An authorised user of the regulated entity uploads on the portal and records the acknowledgement. No portal credential, OTP, DSC PIN, cookie or token is stored, proxied or scripted; no RPA.
3. **Finbyx stays the book of record (NN-23).** For Finbyx tenants, LDC consumes Finbyx `return_run` packages, bureau-cycle records, `PeriodClosed` and `FinancialStatementsApproved` events and never recomputes those returns. LDC computes only for data that is not in Finbyx (non-Finbyx lenders, non-lending entities, group companies, co-operative societies, SEBI/IRDAI/IFSCA entities).

| Outcome | Exit-gate measure |
|---|---|
| A return calendar for every entity type | For an ML NBFC, a scheduled UCB, an ARC, a credit co-operative society, a listed company and an AIF manager, the registry resolves the applicable returns with citations, generates due instances 13 months ahead and shows them in the P04 calendar within 1 minute of profile approval |
| Any source, one pipeline | A non-Finbyx NBFC can load a loan tape (Excel/CSV), a TallyPrime trial balance and GL (via the local agent or XML/JSON export file), a borrowings and investments schedule, and produce DNBS02, DNBS04B and DNBS13 packages reconciled to the trial balance within the template rounding tolerance |
| Finbyx tenants get no duplication | For a Finbyx tenant, every RBI return and CIC cycle appears in LDC from Finbyx events with status, hashes and acknowledgement; "Generate in LDC" is disabled with the reason |
| Deterministic outputs | The same snapshot hash, cell-map version and template hash give a byte-identical file; validation errors cite rule ID and instrument paragraph |
| CIC files for non-Finbyx lenders | Consumer UCRF v3.74, Commercial UCRF v3.10 and MFI UCRF v3.3.1 files built from the loan tape pass the golden-file tests; four bureau outputs from one dataset; incremental W1–W3 and month-end cadence (CIR para 10(2) as substituted from 1 Jul 2026) |
| GST and TDS ready | GSTR-1, GSTR-1A, GSTR-3B, GSTR-9/9C data packages and Form 140/138/144/143 data files (Income-tax Act 2025; 1961-Act forms for earlier periods) are produced with reconciliations and human-filing workflows |
| Accounting bridge | A trial balance mapped once to Schedule III (Division I, II or III), BR Act Third Schedule or the co-operative format produces draft financial statements, notes skeletons and the ratio feed to P09; framework resolved per entity-year with citations (Appendix J) |
| AI that helps but never invents numbers | Vidhi suggests column and ledger mappings, extracts tables from PDF balance sheets and annual reports, explains variances and drafts commentary; every number in a return cell comes from a deterministic computation with lineage (NN-14, NN-22) |
| Evidence and export | Every filing has a sealed evidence pack exported under `11 Returns and Regulatory Reporting/<regulator>/<portal>/<return code>/<period>/` with manifest and acknowledgement (Appendix M) |

---

## 2. Scope (in / out)

**In scope**
- Kernel client: consume `@infrabyx/returns-kernel` (engine) and `infrabyx-returns-packs` (versioned data packs: return definitions, applicability rules, due rules, cell maps, validation rules, CIC format packs, GST/TDS schemas); pin versions per tenant; contract tests.
- Return registry view and applicability resolution for every entity family LDC serves; return due instances in the P04 calendar.
- Data Room: ingestion connectors (Finbyx packages, Udofin packs, TallyPrime agent and file import, Excel/CSV templates, third-party LMS/LOS dumps, ERP exports, SFTP drop, REST API push, PDF financial statements and annual reports via OCR/extraction).
- LDC Canonical Financial Data Model (CFDM) and staging; mapping studio (source → canonical; chart of accounts → element families and statement lines); transformation rules.
- Data-quality profiling and rules; reconciliation (loan tape ↔ TB; sub-ledger ↔ GL; return ↔ TB; cross-return; period-on-period).
- Return generation through the kernel; validation (kernel DSL), reconciliation, maker-checker-signatory approvals, signed package, guided human upload, acknowledgement capture, revisions, supervisory queries.
- CIC submission files for non-Finbyx lenders (consumer, commercial, MFI), rejection ingestion, data-quality index tracking, dispute-clock view (dispute handling itself is P14 + Finbyx).
- GST and TDS/TCS data packages, reconciliations and filing workflows for tenant entities (financial companies and non-financial companies); SFT data where applicable.
- MCA financial-statement filing data (AOC-4 / AOC-4 NBFC (Ind AS) / AOC-4 CFS payloads; XBRL mapping workbook for companies that must file XBRL; MGT-7/7A data from P06 registers).
- SEBI, IFSCA, IRDAI periodic report packs (data preparation and calendar; formats as published) — catalogued in Appendix I.
- Accounting bridge: framework resolver (Ind AS / AS / bank / co-operative / IFRS-IFSC / ICAI non-company), TB import, COA mapping, statement drafting (Schedule III Divisions I–III, Third Schedule Forms A/B, co-operative formats), notes skeletons, Schedule III additional disclosures datasets, ratio feed, CARO and AUD computation feeds to P10, tax-audit data feed.
- Agentic AI data-preparation assistant (P17) with deterministic validators.
- Dashboards for CFO, CCO, Head of Reporting; exports.

**Out of scope**
- Filing on any portal (always human; D-13).
- Bookkeeping or replacing the tenant's accounting system; LDC holds imported books for reporting only (it is not the book of record and does not claim Companies (Accounts) Rules r.3(1) compliance for the tenant's books).
- ECL modelling and IRACP provisioning computation as book-of-record (LDC re-performs classification checks as validations only; Finbyx or the tenant's system computes).
- CIC dispute resolution workflow (P14 grievances; Finbyx RR7 for Finbyx tenants).
- Borrower-facing tax certificates (owned by the RE through Finbyx; Udofin only displays RE-signed certificates — Udofin UB2). LDC does not build borrower tax features; R-079's "borrowers at Udofin" is satisfied by Finbyx/Udofin (master note).
- Payroll TDS computation (P13 computes salary TDS; P11 packages Form 138 data from P13 output).

---

## 3. Personas and permissions touched

| Role | P11 actions | Restrictions |
|---|---|---|
| `ten_maker` (reporting maker, by return family) | Load data, run mapping, generate, validate, reconcile, submit | Cannot approve own run (NN-05) |
| `ten_checker` (head of finance/treasury/risk per family) | Accept warnings, approve or reject | Cannot be maker or signatory of the same run |
| `ten_kmp` CFO / CRO / CCO / MD & CEO / CS (signatory per matrix) | Sign off with step-up MFA | CRO and CCO cannot be makers (GOV/CMP SoD) |
| Authorised filer (any tenant user flagged `portal_filer` in the portal-user alias register) | Download package, follow guided upload, record acknowledgement | Alias only; no credential fields exist |
| `ten_cco` | Owns calendar, overdue escalation, variance and revision decisions | — |
| CIC nodal officer (`ten_kmp` sub-type or flag `cic_nodal_officer`) | Approve each bureau cycle | — |
| `ten_external_auditor` (via grant) | Read packages, lineage, reconciliations; DNBS10 data pack | Read-only |
| `dlv_rm` / `dlv_professional` (retainer maker under D-03/R-072) | Act as maker for the client where the tenant grants the maker role | Cannot be checker or signatory for the client; every action shows "on behalf of LawDocs retainer" |
| `svc_vidhi` | Mapping suggestions, extraction, variance commentary drafts | No writes to cells, approvals or packages (NN-14) |
| `plt_content_maker` / `plt_content_checker` / `plt_content_publisher` | Publish kernel pack versions into LDC (after Infrabyx contracts release) and LDC-only data templates | Content maker-checker (NN-04) |

---

## 4. Functional requirements

### 4A. Shared returns kernel (D-05)

**FR-P11-01 Kernel packaging.** The kernel lives in the `infrabyx-contracts` organisation (Ecosystem Spec §3.3) as:
- `@infrabyx/returns-kernel` — TypeScript library: registry model, applicability evaluator (CEL), due-date engine with holiday calendars, cell-map engine, template filler (XLSX input cells only; never alters protected cells, formulas, hidden sheets), XML/CSV/fixed-width writers, validation DSL runtime (YAML + CEL), reconciliation primitives, package builder (`return_package_v1` manifest + detached JWS), CIC UCRF writers and parsers, GST and TDS schema writers.
- `infrabyx-returns-packs` — versioned, signed data packs per regulator and entity family: `return_definition`, `return_version`, `applicability_rule`, `due_rule`, `cell_map`, `validation_rule`, `format_pack` (UCRF consumer/commercial/MFI; GSTN offline-tool schemas; TDS file formats), each with citations, effective dates, source URL, fetch date, approver and SHA-256.
Finbyx and LDC pin a kernel version (`ret.kernel.version`, Governed tier) and a pack set per tenant; upgrades are opt-in per tenant with a preview of changed rows. A pack row with status `ACTIVE_UNVERIFIED` can be displayed and calendared but cannot reach `GENERATED` (Finbyx RR1.5 rule adopted).

**FR-P11-02 One source of truth for definitions.** LDC never edits a kernel row. Tenant-specific needs (e.g., an additional internal MIS, a State Registrar return for one co-operative) are created as **tenant return definitions** in an LDC overlay schema (`ret.tenant_return_definition`) that reuses kernel primitives and is clearly badged "Tenant-defined" (NN-03). A proposal to promote a tenant definition into the kernel goes to the Infrabyx contracts change process (Ecosystem Spec §14.2).

**FR-P11-03 Conflict rule.** The binding Direction prevails over the RBI web list or portal help (Finbyx RR1.4 adopted). A `registry_variance` (return, field, Direction text and citation, web text and URL, fetch date, decision, approver, review date) is required before activating any pack version that differs from the cached RBI list; variances show on the CCO dashboard and in every affected evidence pack.

**FR-P11-04 Contract tests.** CI runs the kernel's golden fixtures (byte-identical files for DNBS02, DNBS04B, DNBS13 NIL, UCRF consumer/commercial/MFI, GSTR-1 JSON, Form 140) in LDC's pipeline; a kernel upgrade that changes a golden output fails the build until the fixture change is approved.

### 4B. Return registry, applicability and calendar

**FR-P11-05 Registry chain.** `regulator → portal → return_definition → return_version → return_due_instance → return_run` (kernel model). Regulators seeded: RBI (DoS, DoR, FED, DCM, DSIM, FMRD), NABARD, NHB, SEBI, IFSCA, IRDAI, FIU-IND, CERSAI (CKYCR and Central Registry), CBDT (income-tax), GSTN, MCA, CRCS (multi-state co-operatives), State Registrars of Co-operative Societies, CICs, stock exchanges and depositories (for listed entities and intermediaries). Portals seeded with URL, channels and help-document references: CIMS Common Login (https://cims.rbi.org.in), CIMS DRM/Sankalan (https://sankalan.rbi.org.in), DAKSH (https://daksh.rbi.org.in), PRAVAAH (https://pravaah.rbi.org.in), FED/FIRMS/FLAIR/BoP-FETERS/SMS/Data Collector/CISBI (RBI reporting platforms page, updated 23 Oct 2026), NABARD ENSURE, FINGate 2.0, CKYCR, CERSAI CR, income-tax e-filing and reporting portal, GST portal, MCA V3, NSE NEAPS/Digital Exchange and BSE Listing Centre, SEBI Intermediary (SI) portal, IFSCA portal(s) [VERIFY current URLs], IRDAI portal(s) [VERIFY], CIC SFTP endpoints.

**FR-P11-06 Applicability inputs.** From the P15 entity profile: legal form; regulator class; NBFC layer and its effective date; NBFC category flags (MFI, ICC, core investment company, P2P, SPD, Factor, AA, MGC, NOFHC, HFC, IDF, IFC); deposit-taking; public funds; customer interface; standalone, last-audited and group asset size; bank type (SCB, SFB, PB, LAB, RRB); UCB tier and scheduled status; StCB/DCCB; ARC; IFSCA entity type (33-value list per D-08 IFSCA template); SEBI entity type (listed — main board/SME/debt-only; MF/AMC; AIF category I/II/III; REIT; InvIT; stock broker; DP; RTA; IA; RA; PMS); IRDAI entity type (life/general/health/reinsurer; broker; corporate agent; web aggregator; IMF; TPA; surveyor); co-operative type (credit/other; State/multi-state; State); FX flags (AD Cat II, FFMC, ODI/FDI investee, ECB borrower); `has_dla`, `has_overseas_investment`, `fraud_frm_applicable`, `cic_member[]`; GSTINs; TAN; listed exchanges.

**FR-P11-07 Applicability decisions.** Each rule is a CEL expression with citation (kernel). Re-evaluated at onboarding, FY start, profile change and pack change; writes `applicability_decision` (rule version, inputs hash, result, citation). Future instances close with `APPLICABILITY_CHANGED`; past instances remain (NN-29). The per-entity applicability matrix (returns × reasons) is a printable report for CCO and auditors.

**FR-P11-08 Due-date engine.** Kernel `due_rule` tokens (`+15D`, `+21D`, `+7D_FROM_15TH`, `WED_NEXT_WEEK`, `+5WD_FROM_AUDIT_REPORT_CAP_31DEC`, `+1M_FROM_SA_APPOINTMENT`, `+14D_FROM_CLASSIFICATION`, `IMMEDIATE`, `+6H_FROM_DETECTION`, `+4CD_FROM_REFDATE`, `5TH_NEXT_MONTH`, GST and TDS statutory dates with extension notifications as data). Holiday calendars: RBI Mumbai holidays + registered-office State calendar (default), tenant-overridable; a calendar-day limit ending on a holiday moves to the **preceding** working day unless the instrument says otherwise — never later than the Direction allows [REC; Finbyx RR5.1].

**FR-P11-09 Calendar and obligations.** Each `return_due_instance` creates or links a P04 compliance obligation instance (type `Returns & Reporting`, department from the maker matrix) so that the compliance register, calendar, notifications and Board reports show returns alongside other obligations. Alerts T−7, T−3, T−1 and on breach (tenants may add stages, never remove the breach alert); escalation to the CCO on breach and to the MD & CEO after 2 working days [REC].

**FR-P11-10 Event-driven instances.** FMR (+14 days of classification), FUA (immediate), cyber incident (+6 hours, DAKSH; CERT-In separately in P12), Form A appointment (+1 month), DNBS10 and audited returns (+5 working days of auditor's report signing; DNBS10 capped 31 Dec), CKYCR (+10 days of account opening; updates +7 days), CERSAI (+30 days of creation/modification/satisfaction), STR (+7 working days of suspicion), CTR/NTR/CBWTR (15th of next month) [VERIFY PML Rules r.8], DLA register changes, LODR event disclosures (Reg 30, within 24 hours or as specified) [VERIFY].

### 4C. Data Room — ingestion connectors

**FR-P11-11 Source types and adapters.**

| Source | Adapter | Mechanism | Notes |
|---|---|---|---|
| Finbyx (same tenant) | `FINBYX_RETURNS` | Consume `ReturnDue/Generated/Validated/Approved/Filed/Revised`, `BureauFile*`, `PeriodClosed`, `FinancialStatementsApproved`, `GstReturnPrepared`, `TdsStatementPrepared`; fetch packages by document reference (`GET /v1/return-instances/{id}`) | LDC does not generate these returns; shows status, hashes, acknowledgements; packages in LDC evidence by reference (option to copy into tenant's LDC evidence vault with hash match) |
| Udofin (LSP data for an RE) | `UDOFIN_RE_PACK` | `re_audit_pack_v1` P1 pack (DLA facts, LSP metrics, grievance counts) by document reference | For DLA register and CF-related returns; Udofin never files |
| TallyPrime (tenant's machine) | `TALLY_AGENT_READ` | LDC Connector Agent (signed Windows service; outbound-only mTLS; loopback `127.0.0.1:9000`); TallyPrime 7.0+ JSON ("JSONEx") export requests for Trial Balance, Ledger masters, Group masters, Day Book/vouchers by period, Stock summary, GST reports; earlier releases via XML ENVELOPE `TALLYREQUEST Export`; `svCurrentCompany` always set | **Read-only** (export from Tally); never writes vouchers into Tally from P11 (contrast Finbyx AC6 push); refuses non-loopback endpoint |
| Tally export files | `TALLY_FILE` | User uploads XML/JSON/XLSX exported from Tally (TB, Day Book, ledgers) | For tenants that do not want an agent |
| Excel/CSV templates | `LDC_DATA_TEMPLATE` | Downloadable LDC data templates (§4D.3) with validation sheets; upload with preview | Most non-Finbyx clients |
| Third-party LMS/LOS dumps | `GENERIC_TABULAR` | CSV/XLSX/fixed-width/JSON; saved mapping profiles per source system | Profiles for common Indian LMS exports shipped as starter mappings [REC]; never vendor-specific scraping |
| ERP | `ERP_EXPORT` | SAP S/4HANA (OData read), SAP B1 Service Layer (read), Zoho Books API (read), Microsoft Dynamics (read) [VERIFY APIs]; else file export | TB, GL, vendor, customer, fixed assets |
| Core banking extracts (UCB, co-operative banks) | `CBS_EXTRACT` | SFTP drop or upload of CBS report files (CSV/fixed width) | Mapping profile per CBS vendor |
| SFTP drop | `SFTP_INBOUND` | Tenant pushes files to a tenant-specific SFTP inbox (keys in tenant vault) | Scheduled pipelines |
| REST push | `INGEST_API` | `POST /v1/returns/datasets/{dataset}/batches` (JSON/CSV; schema per CFDM entity) with idempotency key | For tenants' own systems (D-02 ecosystem openness) |
| PDF/scan financial statements and annual reports | `DOC_EXTRACT` | P07 OCR + Claude PDF extraction (P17) → structured tables with confidence → human confirmation | Prior-year comparatives, opening balances, ratio history |
| Prior regulatory filings | `FILED_RETURN_IMPORT` | Upload previously filed RBI XLSX templates/acknowledgements | Seeds history for period-on-period checks |

**FR-P11-12 Batch lifecycle.** Every ingestion creates a `data_batch` (source, dataset, period, row count, control totals, file hash, uploader/agent, schema version) with states `RECEIVED → SCANNED (malware) → PARSED → PROFILED → MAPPED → VALIDATED → ACCEPTED | REJECTED | QUARANTINED`. Batches are immutable; corrections are new batches that supersede by period (`supersedes_batch_id`), never edits.

**FR-P11-13 Connection health.** Data Room dashboard: last successful batch per source, freshness vs period close, agent heartbeat, failed parses, unmapped columns, pending confirmations; alerts to the reporting maker and CFO.

### 4D. Canonical Financial Data Model (CFDM) and data templates

**FR-P11-14 CFDM entities (staging schema `ret_stg`, per tenant, per legal entity, per reference date).** Aligned to the Ecosystem canonical model (§5.2) and the kernel's element dictionary so that the kernel can run on LDC staging data exactly as it runs on Finbyx data:

| CFDM entity | Key fields (abridged) | Feeds |
|---|---|---|
| `cf_trial_balance_line` | ledger code, ledger name, group path, opening Dr/Cr, period Dr/Cr, closing Dr/Cr, currency, book (STAT/PRUD/TAX), cost centre | Statements, all TB reconciliations, DNBS01/02 BS/PL, Schedule III |
| `cf_gl_entry` (optional) | voucher no., date, type, ledger, amount, narration, user, created/altered timestamps | CAATs (P10), GST/TDS reconciliations |
| `cf_loan_account` | account id (pseudonymised key), borrower key, product, sanction date and amount, disbursement dates/amounts, outstanding principal, interest accrued, overdue principal/interest, DPD, asset class, SMA status, stage (Ind AS), ECL/provision, restructured flag, security/collateral type and value, rate, tenure, EMI, sector (BSR/RBI sector), MSME flag, priority-sector category (banks/UCBs), state/district/PIN, branch, co-lending share, DLA flag, LSP id, write-off/settlement amounts, closure date | DNBS, CRILC/LEF/RDB, ALM, CIC files, PSL returns, concentration |
| `cf_borrower` | key, type (individual/non-individual), constitution, PAN token (masked), CKYC no. (token), CIN/LLPIN/Udyam, name, DOB/incorporation, gender (where required by CIC format), address, phone, email, income/turnover, related-party flag, group id, wilful-defaulter flag | CIC files, exposure, related-party |
| `cf_guarantor_relationship` | borrower key, related party key, relationship code, share % | Commercial CIC RS/GS segments |
| `cf_exposure_snapshot` | borrower/group, fund-based, non-fund-based, investment exposure, limits, Tier 1 basis | CRILC, LEF, concentration, DNBS03 |
| `cf_borrowing` | lender type, instrument (TL, NCD, CP, ECB, sub-debt, PDI), outstanding, rate, maturity schedule, security, covenant | ALM, DNBS01/02, AUD checks |
| `cf_deposit` (deposit takers) | depositor key, scheme, amount, rate, maturity, nomination, unclaimed flag | NBFC-D returns, UCB Form IX/VIII, co-op returns |
| `cf_investment_holding` | ISIN/identifier, issuer, category (equity listed/unlisted, MF, AIF units, REIT/InvIT units, G-sec, T-bill, CP, NCD, SR), classification (AC/FVOCI/FVTPL; HTM/AFS/HFT for banks), quantity, cost, fair value, level, residency, group/related flag | DNBS13 (overseas), concentration, ICC investment limits, P09 market risk, Schedule III |
| `cf_liquidity_bucket` | bucket code, inflow/outflow category, amount (computed or supplied) | DNBS04A/04B, UCB ALM, bank SLS |
| `cf_capital_component` | component code (equity, reserves, intangibles, deferred tax asset, investments in group, sub-debt, PDI, general provisions), amount | NOF, CRAR, DNBS03, P09 |
| `cf_rwa_line` | exposure class, risk weight, CCF, EAD, RWA | DNBS03, P09 |
| `cf_fraud_case`, `cf_rbr_incident` | case id, classification date, amount, nature, status updates | FMR, FUA, FMR4-RBR |
| `cf_branch` | branch id, type, state/district, opening/closing date, fixed-point unit flag | Branch returns, UCB Form VI, branch coverage |
| `cf_dla` | DLA name, LSP, URL, store links, grievance officer | DLA register on CIMS |
| `cf_gst_document` | GSTIN, document type (invoice, credit/debit note), number, date, counterparty GSTIN, place of supply, HSN/SAC, taxable value, rates, tax amounts, exempt/nil/non-GST flags, RCM | GSTR-1/1A/3B/9 |
| `cf_gst_inward` | supplier GSTIN, invoice, ITC eligibility, IMS action, 2B status | ITC reconciliation, GSTR-3B Table 4 |
| `cf_tds_deduction` | TAN, section/table serial, deductee PAN token, amount paid/credited, TDS, date, challan ref | Form 140/144/143 data files |
| `cf_payroll_summary` (from P13) | employee key, salary components, TDS, PF/ESI, PT, LWF | Form 138; labour returns (P13) |
| `cf_fixed_asset` | asset id, class, cost, additions, disposals, depreciation, title deed holder | Schedule III, CARO 3(i) |
| `cf_related_party_txn` | party, relationship, nature, amount, approval ref | Notes, AUD/CARO, LODR Reg 23 disclosures |
| `cf_member` (co-operatives) | member no., class, shares, deposits, loans, voting status | Registrar returns (with P16) |
| `cf_scheme_nav` (MF/AIF) | scheme, NAV date, AUM, investor counts | SEBI/AMFI reports [VERIFY formats] |

**FR-P11-15 Masking and keys.** Personal identifiers (PAN, Aadhaar-derived refs, account numbers, phone, email) are stored as keyed tokens with masked display; clear values exist only where an output format requires them (CIC files, FIU reports, CKYCR uploads, TDS deductee PAN) and are resolved inside the file-builder service at build time from the tenant's encrypted vault, never written to logs or staging tables in clear (NN-12, NN-32). Aadhaar numbers are never accepted (rejected at parse with `LDC-RET-PII-001`).

**FR-P11-16 LDC data templates.** Downloadable XLSX templates (with a `README` sheet, field definitions linked to RBI harmonised definitions where they exist, dropdowns, sample rows clearly marked and ignored by the parser, a `_Template_Info` sheet with template code and version like the question templates in D-08): `LDC-DT-TB-v1.0` (trial balance), `LDC-DT-LOAN-v1.0` (loan tape), `LDC-DT-BORR-v1.0` (borrower master), `LDC-DT-EXPO-v1.0`, `LDC-DT-BORROWINGS-v1.0`, `LDC-DT-DEPOSITS-v1.0`, `LDC-DT-INVEST-v1.0`, `LDC-DT-ALM-v1.0`, `LDC-DT-CAPITAL-v1.0`, `LDC-DT-FRAUD-v1.0`, `LDC-DT-BRANCH-v1.0`, `LDC-DT-GST-OUT-v1.0`, `LDC-DT-GST-IN-v1.0`, `LDC-DT-TDS-v1.0`, `LDC-DT-FA-v1.0`, `LDC-DT-RPT-v1.0`, `LDC-DT-COOP-MEMBER-v1.0`. Each template is versioned; the parser identifies the template from `_Template_Info` and rejects unknown versions with an upgrade hint.

### 4E. Mapping studio

**FR-P11-17 Column mapping (tabular sources).** For each source profile: source column → CFDM field, with type coercion, unit and scale (₹, ₹ lakh, ₹ crore), date format, code-list translation (e.g., the source's product codes → CFDM product taxonomy; asset class labels → IRACP classes), derived fields (e.g., DPD from overdue since date), default values with reason. Profiles are versioned and approved (maker-checker); a batch uses the profile version current at upload unless the maker selects another.

**FR-P11-18 Chart-of-accounts mapping.** Ledger/group → (a) statement line (Schedule III Division I/II/III, BR Act Third Schedule schedule and line, co-operative format line) and (b) kernel element family (e.g., `ADV_GROSS`, `BORR_TL_BANKS`, `INV_EQ_LISTED`, `PL_INT_INCOME_LOANS`), with sign and book. One ledger maps to exactly one statement line per framework; element families may need splits by dimension (e.g., investments by category from `cf_investment_holding` rather than ledger). Unmapped ledgers with non-zero balances block statement and return generation and are listed by name and balance.

**FR-P11-19 Mapping intelligence (AI-assisted, P17).** Vidhi proposes mappings from ledger names, group paths, prior-period mappings, peer-anonymised patterns (platform library of Tally group names → Schedule III lines, never another tenant's data — NN-01, NN-15) and accounting knowledge; each proposal shows confidence and rationale; only an approved human mapping is used. Proposals for amounts never exist — AI maps structures, the engine computes numbers.

**FR-P11-20 Mapping change control.** A mapping change after a run is `SIGNED_OFF` creates a new mapping version and, if it affects a filed period, opens a revision assessment (§4H.6).

### 4F. Transformation, data quality and reconciliation

**FR-P11-21 Transformation rules.** Declarative (YAML + CEL, same runtime as the kernel DSL) per tenant: derive ALM buckets from cash-flow schedules (if the tenant supplies schedules rather than buckets) using the kernel's bucket definitions (NBFC ALM Annex layout; UCB ALM; bank SLS) [VERIFY bucket definitions per instrument]; aggregate loan tape to element families by dimension; compute exposures at borrower and group level; compute NIL flags; FX conversion with snapshot rates (source and timestamp) for IFSC USD reporting.

**FR-P11-22 Data-quality rules (per CFDM entity).** Completeness (mandatory fields by output need), validity (code lists, PAN pattern, PIN–State consistency, date ordering, DPD ≥ 0, sanctioned ≥ outstanding unless OD), uniqueness (account keys), consistency (asset class vs DPD under the tenant's IRACP rule pack; stage vs DPD under Ind AS policy flags; closed accounts with zero balance), timeliness (data as-of date vs reference date). Each rule has severity (ERROR blocks freeze; WARNING requires maker comment). DQ scores per element feed the data-governance view required by supervisory-returns directions (data quality as part of risk management; documented aggregation rules; reconciliation to accounting data; automation — e.g., RBI (Commercial Banks – Supervisory Returns) Directions 2026 paras 6–17; NBFC SR paras 7, 12–17 per Finbyx RR2 [VERIFY paragraph mapping per entity direction]).

**FR-P11-23 Reconciliations (blocking unless stated).**
1. Loan tape ↔ TB: gross advances, interest accrued, provisions, write-offs by product within tolerance (rounding unit of the target template; e.g., ₹ crore at 2 decimals → ₹1 lakh).
2. Sub-ledger ↔ GL for borrowings, investments, deposits, fixed assets.
3. Return ↔ TB after scaling for every balance-sheet and P&L element (kernel RR3.4 logic).
4. Cross-return: DNBS01/02 ↔ DNBS04B totals; DNBS03 CRAR ↔ capital computation (P09) ↔ notes to accounts; CRILC count ↔ exposures ≥ ₹5 crore; DNBS13 ↔ investment holdings with non-resident flag; GSTR-1 ↔ books; GSTR-3B ↔ GSTR-1; 2B ↔ purchase register; Form 140 ↔ TDS ledger and challans.
5. Period-on-period reasonableness (WARNING): configurable % thresholds per element; spikes produce variance tasks with AI-drafted commentary for the maker to confirm.
Any break beyond tolerance needs an `explained_variance` (reason code, amount, evidence, approver) before `RECONCILED`.

**FR-P11-24 Snapshot freeze.** `reporting_snapshot` per legal entity × reference date × book: the set of accepted batches and the mapping versions used, content hash. Generation always reads a frozen snapshot; later batches for the same period surface as post-snapshot items and, if material, revision assessments.

**FR-P11-25 Lineage.** Each output cell (or record, for CIC/GST/TDS files) stores element, aggregation, filter, snapshot id, row count, query hash and a masked drill-down to contributing staging rows and their source batch and file line numbers. "Explain this number" on any cell shows the chain: cell → element → staging rows → batch → source file (line) or Finbyx document reference.

### 4G. Generation, validation, approval, packaging, human filing

**FR-P11-26 Filing state machine (kernel, adopted unchanged).** `SCHEDULED → DATA_FROZEN → GENERATED → VALIDATED → RECONCILED → MAKER_SUBMITTED → CHECKER_APPROVED → SIGNED_OFF → PACKAGED → UPLOADED_BY_HUMAN → ACKNOWLEDGED → CLOSED`, with `REPAIR`, `PORTAL_REJECTED`, `CONTINGENCY_EMAIL`, `ONLINE_RESUBMISSION_PENDING`, `REVISION_REQUESTED`, `CANCELLED (APPLICABILITY_CHANGED)`, `NOT_APPLICABLE (CCO approval)`. Overdue is a flag, not a state. Table in §5.1. For Finbyx-sourced returns the LDC instance is a **mirror** whose state follows Finbyx events (`source_system = FINBYX`), shown read-only.

**FR-P11-27 Template handling.** The filer (or maker) uploads the period's RBI/portal template; LDC checks its hash against `format_version`; a changed hash opens a template-change task (new version, cell-map review by the kernel maintainers and, until approved, generation blocked for that return). Only unprotected input cells are filled. Where the channel is web-form (CIMS screen-based form has a 2,000-record cap per Finbyx RR4.1), the package also carries a web-form entry sheet; above the cap, file upload is forced.

**FR-P11-28 Validation.** Kernel validation packs per return (schema, intra-return arithmetic, cross-return, GL reconciliation, period-on-period reasonableness, portal's own validation rules as a separate pack). ERROR blocks sign-off; WARNING needs maker comment and checker acceptance; INFO logged. Each failure shows rule ID, message, instrument citation and an "open lineage" link.

**FR-P11-29 Approval matrix (defaults; tenant-configurable within SoD).** Kernel defaults (Finbyx RR3.5) for NBFC families, extended for other entity families in Appendix I §I.9 (e.g., UCB Form I/B: maker Accounts, checker GM Finance, sign-off CEO; co-operative Registrar returns: maker Accountant, checker Secretary, sign-off President/Chairman per by-laws; SEBI LODR reg 33 results: maker Finance, checker CFO, sign-off Board-authorised director and CFO certification under Reg 33(2)(a) [VERIFY]; IRDAI returns: maker Actuarial/Finance, checker CFO, sign-off Principal Officer/CEO [VERIFY]). Maker ≠ checker ≠ signatory; CRO/CCO cannot be makers; sign-off needs step-up MFA; absence covered only by time-boxed delegation (P02).

**FR-P11-30 Signed package.** Filled file(s) + `manifest.json` (entity, return, period, run, kernel/pack/template versions, snapshot hash, file SHA-256, validation and reconciliation hashes, approvals) + validation report + reconciliation sheet + lineage extract + NIL declaration (if applicable) + variance rows; detached JWS with the tenant signing key in the tenant KMS. Portal DSCs are applied by the signatory on the portal; LDC never holds a DSC or PIN.

**FR-P11-31 Guided human upload.** One screen, steps ticked in order and time-stamped: open portal in a separate tab (link only; never embedded or automated) → confirm entity/return/period/template version → upload file and compare SHA-256 shown by LDC → record portal validation result (errors pasted/attached → `PORTAL_REJECTED`) → portal checker submits → download acknowledgement → upload acknowledgement to LDC (LDC pre-reads reference and timestamp from the PDF for the filer to confirm). Portal-user alias register records portal role, employee and alias only — no credential field exists (D-04 default for RBI portals is client-only; NN-17).

**FR-P11-32 Contingency.** Email filing only on RBI-advised contingency (supervisory-returns directions: online only, email deemed filing only when portals are unavailable, followed by online resubmission — e.g., Commercial Banks SR 2026 para 18) with the advice attached; opens `ONLINE_RESUBMISSION_PENDING` until online acknowledgement.

**FR-P11-33 Revisions and revision assessments.** Triggers: RBI query, audit adjustment, back-dated posting into a filed period, DQ error, `FinancialStatementsApproved` figures differing from filed quarterly returns, mapping change affecting a filed period. Assessment lists every affected return and period with a draft cell diff from a fresh snapshot → owner proposes REVISE/NO_REVISION (prudential-ratio cells or above `ret.revision.materiality` default REVISE) → CCO decides → REVISE opens run n+1 at `DATA_FROZEN`; version n preserved byte-for-byte; `ReturnRevised` emitted on acknowledgement. NO_REVISION kept with diff in the evidence pack.

**FR-P11-34 Supervisory queries.** `supervisory_item` register (source DAKSH/email/letter/inspection/PRAVAAH; type return query/ad hoc request/RMP item/letter; linked returns; owner; due; drafts; approvals; response reference). Ad hoc requests run as ad hoc returns (`ad_hoc = true`) through the same path with the regulator's due date.

**FR-P11-35 Evidence vault.** Folder layout `11 Returns and Regulatory Reporting/<regulator>/<portal>/<return code>/<period>/run-<n>/` with byte-identical filed files, validation report, sign-offs, acknowledgement, revision history, variances; retention class `REG-RETURN` 10 years from filing [REC], never below statutory periods; legal hold supported.

### 4H. Return families (entity-specific logic; full catalogue in Appendix I)

**FR-P11-36 NBFCs (RBI (NBFC – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/466, 31 Jul 2026; HFCs excluded).** Twenty-one kernel definitions from SR para 21 (DNBS01, 02, 03, 04A, 04B, 08 CRILC, 09 RDB, 10 SAC, 11, 12, 13, 14, LEF, PDR-III, PDR-IV, STRESS, IRS, FMR, FUA, FMR4-RBR, FORM-A-SA) with applicability by layer and category, and returns kept alive by other Directions (DLA register on CIMS, RBR incident email, group-entity fraud email, cyber incident on DAKSH, NBFC-D nomination coverage, securitisation report, WD/LD files) — Appendix I §I.2. Known web-list variances (DNBS04A/04B ₹100 crore BL threshold; DNBS08/09 BL qualifier; ARC rows; Form A mode) are pre-loaded as `registry_variance` rows (Finbyx RR1.4).

**FR-P11-37 HFCs.** Returns to NHB [VERIFY current NHB list, portal and format]; CIC reporting applies (CIR para 3). Pack status `ACTIVE_UNVERIFIED` until verified.

**FR-P11-37A v1 generation scope (X-32; review R4).** In Wave 2 the Return Studio generates packages only for NBFC (RBI/DoS/2026-27/466), ARC (/469) and co-operative-society families whose State pack is verified (MSCS and Maharashtra first, P16), plus CIC, GST, TDS, FIU-IND and MCA data packages. Bank, SFB, PB, LAB, RRB, UCB, StCB/DCCB, HFC, IRDAI, SEBI and IFSCA rows load as `ACTIVE_UNVERIFIED`: calendar, applicability, data collection, reconciliation, secondary validation and evidence work; generation unlocks per return only after a pilot tenant and a named reviewer verify the cell map (Appendix I status → VP).

**FR-P11-38 Commercial banks (RBI (Commercial Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/415; 37 returns).** Timelines para 22 (weekly → Wednesday of following week; fortnightly → 7 days of 15th; monthly 15 days; quarterly/half-yearly/yearly 21 days; audited 5 working days of auditor's report) with para 23 exceptions (RFA 7 days; CPR provisional end-June/audited end-September; BLR 3 and 7 within 15 days; FINCON 45 days; investment portfolio review 15 June/15 December; branch allocation within a month of SBA appointment; GML 7 days; FMR 14 days; FUA immediate; FMR4 15 days); NIL for CRILC and RDB. Statutory returns under BR Act and RBI Act (Form A NDTL/CRR, Form VIII SLR, Form IX unclaimed, Form X, BSR-1/2, etc.) from the RBI list — Appendix I §I.3. Most bank tenants have a CBS and an ADF; LDC's role for banks is primarily calendar, evidence, governance, reconciliation and secondary validation; full generation for bank returns is `ACTIVE_UNVERIFIED` until a bank pilot verifies cell maps [REC].

**FR-P11-39 Small finance banks (RBI/DoS/2026-27/424; 33 returns)** and **payments banks, LABs, RRBs** [VERIFY direction numbers] — Appendix I §I.4.

**FR-P11-40 UCBs (RBI (Urban Co-operative Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/442; 21 returns).** Form B (fortnightly, scheduled UCBs, 5 days), Form I (CRR/SLR, monthly, 20 days), Form II, Form VI, Form VIII (31 Dec ref., 30 days), Form IX (monthly, 30 days), RAL, ROE, RAQ-UCB, RCL, RCP, PSA (excl. salary earners' UCBs), RBP, CRILC-UCBs (quarterly; total assets ≥ ₹500 crore; NIL), ALM returns (scheduled: ALM 1 monthly, ALM 3 fortnightly; non-scheduled quarterly), SFA-WD, SAI, FSI, FMR, FUA, FMR4 [VERIFY rows 8–11, 20, 21 frequencies]. UCB tier (Tier 1–4 under the revised regulatory framework) drives applicability flags [VERIFY].

**FR-P11-41 StCBs and DCCBs.** RBI list rows 64–69 (Form I SLR monthly; Form II monthly; Form VIII at 31 Dec; sectoral deposits half-yearly; Form B fortnightly for StCBs; Form IX monthly) on CIMS; NABARD ENSURE supervisory returns (indicative: OSC returns, cyber incident reporting) [VERIFY current list].

**FR-P11-42 ARCs (RBI (ARC – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/469).** DNBS07 (quarterly, 21 days), DNBS10 (yearly; 5 working days of auditor's report, ≤ 31 Dec), DNBS13 (quarterly); plus ARC Directions 2025 reporting (audited balance sheet to RO, website possession list, CERSAI/IU filings) [VERIFY paragraph numbers].

**FR-P11-43 AIFIs, credit information companies** — out of LDC's first-release target market; registry rows loaded `ACTIVE_UNVERIFIED` only on demand.

**FR-P11-44 Credit co-operative societies and other co-operatives.** No RBI returns. Registrar returns: MSCS Act 2002 s.120 annual return within 6 months of FY end and other CRCS returns for multi-state societies [VERIFY]; State Act returns (e.g., Maharashtra Co-operative Societies Act 1960 s.79 [VERIFY]); audit-related submissions; election-authority filings (P16). Pack per State `ACTIVE_UNVERIFIED` until verified; tenant-defined returns allowed (FR-P11-02).

**FR-P11-45 IFSCA entities.** Reporting in USD per entity regulations (e.g., IFSCA (Finance Company) Regulations 2021 reg 9 for FC/FU [VERIFY]); FIU-IND reporting; FEMA/ECB where lending into India [VERIFY]; IFSCA prudential and statistical returns per circulars — catalogued in Appendix I §I.11 with the D-08 IFSCA entity list driving applicability.

**FR-P11-46 SEBI entities.** Listed entities (LODR): Reg 33 financial results (45 days; 60 days for Q4/annual audited) with Reg 33(2)/(3) certifications; Reg 31 shareholding pattern (21 days of quarter end) [VERIFY]; Reg 27(2) corporate governance report (21 days) [VERIFY]; Reg 13(3) investor grievance statement (21 days) [VERIFY]; Reg 24A Annual Secretarial Compliance Report (60 days); Reg 23(9) RPT disclosure; Reg 34 annual report and BRSR; Reg 40(9)/(10) and Reg 7(3) certificates [VERIFY continuing applicability]; SEBI (Depositories and Participants) Regulations 2018 reg 76 reconciliation of share capital audit (quarterly, 30 days) [VERIFY]; SAST Reg 31(4) and PIT disclosures. MFs/AMCs, AIFs, REIT/InvIT and intermediaries: periodic reports to SEBI (SI portal), AMFI, exchanges and depositories per master circulars [VERIFY each] — Appendix I §I.12. LDC prepares XBRL/XML data where the exchange requires it (NSE/BSE XBRL utilities) as a mapping workbook plus generated instance when the taxonomy pack is verified [VERIFY].

**FR-P11-47 IRDAI entities.** Insurers' periodic returns, public disclosures (quarterly), solvency (IRDAI (Assets, Liabilities and Solvency Margin) Regulations), investment returns, and intermediaries' annual/half-yearly returns per IRDAI regulations and master circulars (2024 consolidation) [VERIFY each] — Appendix I §I.13.

**FR-P11-48 FIU-IND, CKYCR, CERSAI.** STR/CTR/NTR/CCR/CBWTR XML (FINnet 2.0 report generation and validation utilities [VERIFY version]) with Principal Officer approval and tipping-off protection (STR visible only to AML roles); CKYCR bulk upload files and response ingestion (10/7-day clocks); CERSAI Central Registry charge filing tasks (30 days) — for non-Finbyx lenders; Finbyx tenants mirrored.

**FR-P11-49 FEMA and RBI FED returns** (for any tenant with foreign investment or borrowings): FLA return on FLAIR (annual) [VERIFY due date], ECB-2 monthly (via AD bank), ODI annual performance report, FC-GPR/FC-TRS/DI on FIRMS (event-based) — calendar, data pack and evidence; filed by the tenant or its AD bank.

### 4I. Credit bureau (CIC) submissions for non-Finbyx lenders

**FR-P11-50 Applicability.** Lending tenants that are members of CICs (CIR para 6: membership of all four CICs; reporting needs no borrower consent — CIR para 11) and not on Finbyx; co-operative societies only where a CIC has admitted them as members [VERIFY]; LSPs never report (CF para 17); co-lenders report their own shares.

**FR-P11-51 Cadence (effective-dated; CIR para 10(2) as substituted by the amendment of 4 Dec 2025 (RBI/DOR/2025-26/117 [VERIFY reference]), in force 1 Jul 2026).** Incremental files for the 9th (W1), 16th (W2), 23rd (W3) reference dates within 4 calendar days; month-end (ME) full file by the 5th of next month; Annex VI rejection and correction timetable; rejected data rectified before or with the next reference-date file; daily (DL) by agreement (e.g., MFIN members). Pre-1 Jul 2026 cadence (15th and month-end, 7 days) kept for historical periods. **Do not implement the withdrawn draft cadence (7th/14th/21st/28th).**

**FR-P11-52 Population and routing.** ME = all active accounts + accounts ended since last reference date; W1–W3 = opened ∪ ended ∪ changed by borrower-initiated action or transaction ∪ any overdue (accounts whose only change is DPD must be reported). Individuals → Consumer; non-individuals and guarantors → Commercial (relationship segment for accounts opened on/after 1 Jul 2018); microfinance → MFI only (never also Consumer); co-borrowers each in their own format.

**FR-P11-53 Format packs.** UCRF Consumer v3.74 (4 Feb 2026, w.e.f. 1 Jul 2026; header tag `CONS`/`TUDF`; PN/ID/PT/EC/PA/TL/TH/ES segments; TLV encoding; DPD cap 900; ID type 09 CKYC), UCRF Commercial v3.10 (13 Apr 2026; pipe-delimited; HD/BS/AS/RS/CR/GS/SS/CD/TS; SFTP only; `~` and `^` forbidden; written-off and settled amounts enforced from 1 Apr 2027), UCRF MFI v3.3.1 (Apr 2026; pipe; separate SHG and JLG+individual files; DPD 000–999 mandatory; field 49 household income mandatory) — kernel format packs, data not code; each CIC's member specification obtained under the member agreement before go-live; spec inconsistencies logged as `format_issue` and resolved in writing with the CIC.

**FR-P11-54 Mapping rules.** Settled only when principal/interest waived for financial inability (CIR para 12(4)); disputed charges as disputes, never "settled"; IBC admission → suit-filed (consumer 01; commercial 05 NCLT/NCLAT) (CIR 12(7)); wilful defaulter (ML+) per WD directions; write-off and settlement amounts; sold/purchased/securitised flags; restructuring reason codes; CKYC number per CIR 12(10).

**FR-P11-55 Build, approve, transmit.** Freeze → extract → route → validate (format pack + CICs' uniform data-acceptance rules) → build four outputs from one dataset → CIC nodal officer approval (counts by segment, status, DPD bucket; held-back records; variance to last cycle) → transmit by SFTP **from a tenant-controlled host or the LDC Connector Agent on the tenant's premises/cloud**, keys in the tenant vault (BYOK; unreadable by LawDocs staff) → record hash, size, time, server acknowledgement → ingest rejection reports and file-level DQI (CICs return within 3 calendar days) → repair at source → resubmit as `RR` cycle by the Annex VI date. Missing the 4-day or 5th-of-month deadline raises `ComplianceIssueRaised` (CICs report laggards to RBI). Per-CIC cycles tracked separately.

**FR-P11-56 Data quality and governance.** File-level and CI-level DQI trending; half-yearly DQI review report to top management within two months of half-year end (CIR para 17) drafted for approval; nodal officer register with 5-day change notification task per bureau (CIR para 34(2)(ii)); borrower SMS/email alert on default/DPD data submission (CIR para 34(1)(i)) as a P04 control check (sending is the lender's system or LDC's notification service if enabled with DLT-registered templates [VERIFY tenant consent and TRAI rules]).

### 4J. GST

**FR-P11-57 Fee and supply master.** For each tenant GSTIN: supply categories with GST treatment (exempt interest on loans/advances/deposits — Notification 12/2017-CT(Rate) entry 27(a) [VERIFY wording]; taxable fees 18% with SAC [VERIFY per fee]; penal charges under the RBI penal-charges framework not subject to GST per CBIC Circular 245/02/2025-GST (28 Jan 2025) — a fee merely labelled penal stays taxable; pure-agent recoveries (CGST Rules r.33); co-lending spread treatment by tenant decision with written opinion, default taxable [REC]); non-financial tenants: HSN/SAC master from imported invoices.

**FR-P11-58 Returns.** GSTR-1 (B2B, B2C, exports, exempt/nil, credit/debit notes, HSN Table 12 with separate B2B and B2C tabs and digit rules), GSTR-1A (amendments), GSTR-3B (Table 3 auto-populated and locked from the July 2025 period; Table 4 ITC incl. 4B(1) reversals and the 50% option for banking companies/FIs/NBFCs under CGST Act s.17(4) with r.38 — election recorded annually and locked), GSTR-9, GSTR-9C (self-certified reconciliation where AATO > ₹5 crore [VERIFY]); IMS actions on inward invoices (accept/reject/pending with maker-checker; deemed acceptance warning before GSTR-2B cut-off [VERIFY]); 3-year time-bar flags; JSON per GSTN offline-tool schema; filing by authorised user with EVC/DSC on the GST portal or through the tenant's own GSP/ASP — LDC never stores GST portal credentials or OTPs.

**FR-P11-59 E-invoicing.** Not applicable to banking companies and financial institutions including NBFCs (CGST Rules r.48(4); Notification 13/2020-CT as amended) [LAW]; for other tenants above the AATO threshold (₹5 crore from 1 Aug 2023, Notification 10/2023-CT) LDC produces IRP-ready JSON from imported invoices for upload through the tenant's IRP/GSP [REC; LDC is not an IRP or GSP].

**FR-P11-60 Reconciliations.** Books ↔ GSTR-1 monthly; GSTR-3B ↔ GSTR-1; 2B ↔ purchase register; ITC reversal computation; RCM liability ↔ vendor invoices; annual books ↔ GSTR-9 ↔ GSTR-9C. Workflow per GSTIN × period × return: `DATA_FROZEN → GENERATED → SCHEMA_VALIDATED → RECONCILED → CHECKER_APPROVED → FILED_BY_HUMAN (ARN, date) → CLOSED`; post-filing differences via GSTR-1A or next-period adjustment, never by editing the filed package; late filing computes late fee and interest from the rule pack.

**FR-P11-61 Finbyx tenants.** Consume `GstReturnPrepared` packages; LDC shows calendar, reconciliation status, ARN and evidence; no recomputation.

### 4K. Income-tax: TDS/TCS, SFT, tax-audit data

**FR-P11-62 Regime selection.** FY 2025-26 and earlier obligations (including statements filed after 1 Apr 2026) use Income-tax Act 1961 forms (24Q, 26Q, 27Q, 27EQ; Forms 16/16A/27D; 61A/61B); tax year 2026-27 onwards uses the Income-tax Act 2025 (in force 1 Apr 2026) and Income-tax Rules 2026: Form 140 (non-salary, quarterly), Form 138 (salary), Form 144 (non-resident), Form 143 (TCS); certificates Form 130 (salary), 131, 133; declarations Form 121; lower-deduction Form 128; SFT s.508 Form 165; FATCA/CRS Form 166; tax audit s.63 Form 26 — every section, form and table number is configurable data with [VERIFY] until confirmed against the official text and CBDT transition guidance (Finbyx AC5.1 concordance adopted).

**FR-P11-63 TDS statements.** From `cf_tds_deduction` (vendor/professional/rent/commission/interest payments) and P13 payroll (Form 138): challan matching, interest on late deposit, validation through the official file validation utility [VERIFY utility name] run by the user or bundled where licence permits; due dates 31 Jul, 31 Oct, 31 Jan, 31 May; workflow `DATA_FROZEN → GENERATED → UTILITY_VALIDATED → CHECKER_APPROVED → FILED_BY_HUMAN → PROCESSED (import processing result) → CERTIFICATES_ISSUED → CLOSED`; corrections linked to the original statement.

**FR-P11-64 TDS receivable matching.** For lenders: TDS deducted by corporate borrowers on interest matched to Form 168 (formerly 26AS) [VERIFY] by TAN/period/amount; shortfalls create chase tasks; never closes the interest receivable automatically.

**FR-P11-65 SFT and FATCA/CRS** data files for reporting entities (designated director sign-off) [VERIFY reportable transaction list for NBFCs].

**FR-P11-66 Tax-audit data pack** (clause-wise; s.63 Form 26 / s.44AB Form 3CD) delivered to P10 `TAX_AUDIT_SUPPORT` engagements.

### 4L. MCA filing data

**FR-P11-67 Financial statements filing.** AOC-4 / AOC-4 CFS for non-Ind AS and non-NBFC companies; AOC-4 NBFC (Ind AS) and AOC-4 CFS NBFC (Ind AS) for Ind AS NBFCs (substituted by Companies (Accounts) Second Amendment Rules 2025, in force 14 Jul 2025 [VERIFY]); XBRL only where triggered (listed; paid-up ≥ ₹5 crore; turnover ≥ ₹100 crore; Ind AS companies) — **never XBRL for NBFCs** (exempt) or banking companies (exempt till further order); for XBRL filers LDC produces a taxonomy mapping workbook and, when the MCA taxonomy pack is verified, an instance document validated against the MCA validation tool [VERIFY tooling]. Board's report data (Rule 8 as amended 2025 — POSH complaint counts and maternity-benefit statement) handed to P06; Rule 3(6) cloud/backup statement data where LDC holds books for the tenant — **not applicable** since LDC is not the book of record (§2) unless the tenant designates it [REC].

**FR-P11-68 Annual return and other forms.** MGT-7/MGT-7A data from P06 registers; DPT-3 (deposits/exempted deposits) from `cf_borrowing`/`cf_deposit`; MSME-1 half-yearly from vendor ageing (MSME vendors > 45 days) [VERIFY current applicability]; CSR-2 from P06 CSR data; LLP Form 8 and Form 11 for LLP tenants. Filing on MCA V3 by the company's authorised signatory with DSC; LDC prepares data, attachments and checklist only.

### 4M. Accounting bridge

**FR-P11-69 Framework resolver.** Per legal entity per financial year, deterministic rules with citations (Appendix J §J.2; Finbyx AC1 matrix adopted): Ind AS (Companies (Ind AS) Rules 2015 r.4; NBFC Phase I/II; non-NBFC roadmap; sticky once adopted), AS (Companies (AS) Rules 2021), bank AS + RBI with Third Schedule (Ind AS deferred for SCBs; bank ECL from 1 Apr 2027 under RBI/DOR/2026-27/398 for banking companies other than SFB/PB/LAB), UCB AS + Third Schedule via BR Act s.56, co-operative society Act format, ICAI scheme for non-company entities (MSME vs Large, periods from 1 Apr 2024), IFRS for IBUs, IFSC FC/FU per profile [VERIFY], insurers per IRDAI accounting regulations (Ind AS for insurers deferred [VERIFY current status]), MF schemes per SEBI MF Regulations accounting provisions, REIT/InvIT Ind AS per SEBI [VERIFY]. Output: framework, currency, statement set, disclosure packs, CARO flag, AUD flag, MCA route. Decision log approved by the CFO.

**FR-P11-70 Statement drafting.** From the mapped TB (current and comparative periods; comparatives from prior-year mapped TB or from extracted prior annual report): Balance Sheet, Statement of Profit and Loss, Statement of Changes in Equity (Ind AS), Cash Flow Statement (indirect method from TB movements + supplied non-cash adjustments), notes skeletons with numeric tables filled and narrative placeholders, Schedule III general instructions (rounding by turnover band: < ₹100 crore — nearest hundreds, thousands, lakhs or millions or decimals; ≥ ₹100 crore — nearest lakhs, millions or crores or decimals; consistent units), Schedule III additional regulatory information datasets (2021 amendment: title deeds, promoter shareholding, ageing of receivables/payables/CWIP, loans to promoters/directors/KMP/related parties, benami, wilful defaulter, struck-off company transactions, charges not registered, layering, schemes, funds routed through intermediaries, undisclosed income, CSR, crypto) each with "nil with evidence" option; Division III NBFC-specific line items and ratios (CRAR, Tier I, Tier II, LCR) [LAW]; RBI FS Directions disclosures (FS RBI/DOR/2025-26/359 Annex/para 21 tables for C.1 all, C.2 ML/UL, C.3 UL) fed from P09 and imported data; bank Third Schedule Forms A and B with Schedules 1–16 and RBI notes-to-accounts disclosures [VERIFY 2025 bank FS Directions].

**FR-P11-71 Outputs.** DOCX (notes and narrative, ready for the auditor and the Board — Word track changes on regeneration show what changed), XLSX (statements and schedules with formulas live), PDF/A (approved version), AOC-4 payload (§4L). Each output records framework, mapping version, TB batch hashes and approvals. Statements are **drafts for the tenant's finance team and auditors**; LDC never presents them as audited.

**FR-P11-72 Validations (blocking unless stated).** Balance sheet balances; cash flow ties to cash movement; provisions not netted where FS requires separate disclosure; CRAR in notes = DNBS03 = P09 capital run (0.01 pp tolerance); NPA movement ties to the loan tape classification history; Schedule III datasets present or evidenced nil; comparatives present; warning at 60 days if statements not finalised within the FS-required period (3 months of 31 March for NBFCs — FS para 9 per Finbyx [VERIFY]).

**FR-P11-73 Principal Business Criteria and NOF computations.** Financial assets / total assets (net of intangibles) and financial income / gross income tests (bank FDs not financial assets) with lineage, quarterly and at 31 March — feeds P10 AUD para 6 checklist, CARO 3(xvi), P15 entity-logic monitoring (alert if the NBFC drifts below 50%) [VERIFY current RBI wording in the 2025 consolidated Directions].

**FR-P11-74 Ratio feed to P09.** Publishes `FinancialDataSetReady` (internal event) with element values by period for the P09 ratio library (capital, asset quality, liquidity, profitability, leverage, concentration, ALM gaps, NOF, PBC tests, co-operative ratios, insurer solvency inputs where supplied). P09 owns ratio definitions, thresholds and dashboards; P11 owns the data and lineage.

**FR-P11-75 Annual report and governance data.** Data packs for P06: financial highlights, ten-year summary (from history), segment data, related-party tables, CSR spend, MD&A data tables, Board's report numeric items, AGM notice financial items; for listed entities the Reg 33 results format; for co-operatives, the AGM financial statements and profit appropriation per Act and by-laws (reserve fund, education fund) [VERIFY per Act]. Data for minutes (e.g., "Board noted the financial results for the quarter: total income ₹X crore") is offered as merge fields to P06 templates — values with lineage, never AI-typed figures (NN-22).

### 4N. Vidhi Data-Prep agent (P17 delivers the agent; P11 delivers tools, validators and guardrails)

**FR-P11-76 Tools exposed to the agent (on behalf of a named maker).** `profile_batch`, `suggest_column_mapping`, `suggest_coa_mapping`, `extract_tables_from_pdf` (annual report, audited statements, bank statements, sanction letters), `explain_validation_failure`, `draft_variance_commentary`, `compare_periods`, `find_missing_data` (what is needed for return X for period Y), `prepare_data_request` (email/task to the data owner listing missing fields), `generate_lineage_explanation`. Every tool output is a **proposal** stored with model/provider/version, prompt hash, inputs hash and confidence; acceptance by the maker turns it into a mapping version, a comment or a task.

**FR-P11-77 Hard guardrails.** The agent cannot write staging values, cell values, approvals, packages or acknowledgements; cannot change mapping versions without human approval; cannot open a portal or send a file externally; cannot see clear PII (tokens only); extraction from documents produces staging candidates that must pass DQ rules and human confirmation before acceptance; every AI-touched artefact is badged (NN-04, NN-14, NN-15). A deterministic validator re-computes any figure the agent quotes in commentary and blocks the comment if the figure does not match lineage.

**FR-P11-78 Agentic run-book automation.** A tenant may schedule an agent "return preparation run" (e.g., on the 3rd working day after month end): pull latest batches → run profiles and DQ → generate drafts → run validations → prepare a maker brief (what passed, what failed, what is missing, suggested actions) → create tasks. The run stops before `MAKER_SUBMITTED`; humans do the rest.

### 4O. Dashboards

**FR-P11-79** CFO / Head of Reporting / CCO dashboards (widgets per Appendix C): returns due in 7/30 days by state; overdue and breach count; acknowledgements pending; revisions open; variances awaiting approval; Data Room freshness; DQ scores by element; CIC cycle status by bureau (on-time %, rejection rate, DQI trend); GST and TDS filing status and reconciliation breaks; framework decisions pending; statement drafting progress; registry variances; supervisory items due. Board/ACB summary widget: "Regulatory reporting health" (on-time rate, revisions, penalties exposure flags).

### 4P. Exports

**FR-P11-80** `11 Returns and Regulatory Reporting/<Regulator>/<Portal>/<Return code – name>/<Period>/run-<n>/` (filed file, manifest, validation, reconciliation, lineage extract, approvals, acknowledgement); `11 Returns and Regulatory Reporting/Credit Information Companies/<CIC>/<Consumer|Commercial|MFI>/<Reference date Cycle>/` (file, acknowledgement, rejections, DQI); `11 Returns and Regulatory Reporting/Accounts and Tax/<FY>/01 Trial balances and mappings`, `02 Financial statements (draft and approved)`, `03 GST/<GSTIN>/<Period>/`, `04 TDS/<TAN>/<Quarter>/<Form>/`, `05 MCA filings data/`, `06 Tax audit data/`; `23 Integrations and Data Exchanges/Data Room/<Source>/<Dataset>/<Period>/batch-<id>/` (original files and parse reports) — each with an index XLSX and manifest (Appendix M; NN-10).

---

## 5. Workflows and state machines

### 5.1 Return run (kernel; LDC-native and mirrored)

| State | Entry condition | Owner | Allowed actions | Timer | Exits |
|---|---|---|---|---|---|
| `SCHEDULED` | Due instance created | Return owner (maker) | Assign owner; mark `NOT_APPLICABLE` (CCO approval + reason) | Freeze target = reference date + `ret.freeze_lead_days` | Freeze → `DATA_FROZEN`; applicability change → `CANCELLED` |
| `DATA_FROZEN` | All required datasets accepted; DQ ERRORs nil; loan↔TB reconciliation clean; period soft-closed in source (Finbyx `PeriodClosed` or tenant attestation for Tally/Excel) | Maker | Generate; unfreeze (checker approval + reason; snapshot kept) | Alert if not generated by due − `ret.generate_lead_days` | → `GENERATED`; → `SCHEDULED` |
| `GENERATED` | Template hash matches; every cell mapped or `NOT_APPLICABLE_FOR_ENTITY` with reason | Maker | Validate; view lineage | — | No ERROR → `VALIDATED`; ERROR → `REPAIR` |
| `VALIDATED` | WARNINGs listed | Maker | Reconcile; comment WARNINGs | — | → `RECONCILED`; break → `REPAIR` |
| `RECONCILED` | Reconciliation hash stored | Maker | Attest and submit | — | → `MAKER_SUBMITTED` |
| `MAKER_SUBMITTED` | Maker attestation | Checker | Accept WARNINGs; approve; reject (reason code) | Checker SLA 1 working day | → `CHECKER_APPROVED`; → `REPAIR` |
| `CHECKER_APPROVED` | SoD check passed | Signatory | Sign off (step-up); reject | Signatory SLA 1 working day | → `SIGNED_OFF` (`ReturnApproved`); → `REPAIR` |
| `SIGNED_OFF` | Signature recorded | System | Build package | Immediate | → `PACKAGED`; any input change voids sign-off → new run |
| `PACKAGED` | Package hash stored | Authorised filer | Download; guided upload | Alert at due − 1 working day | → `UPLOADED_BY_HUMAN`; → `CONTINGENCY_EMAIL` |
| `UPLOADED_BY_HUMAN` | Alias, time, file hash confirmed | Filer | Record portal result; upload acknowledgement | Reminder after 4 working hours | → `ACKNOWLEDGED` (`ReturnFiled`); → `PORTAL_REJECTED` |
| `PORTAL_REJECTED` | Portal message recorded | Maker | Classify data vs portal error | — | Data → `REPAIR`; portal → `PACKAGED` (same file) |
| `REPAIR` | Rule failure, break, rejection | Data owner then maker | Fix at source (new batch or mapping version), regenerate | Escalate to CCO if due at risk | → `GENERATED` |
| `CONTINGENCY_EMAIL` | RBI advice attached | Filer | Record email sent | — | → `ONLINE_RESUBMISSION_PENDING` |
| `ONLINE_RESUBMISSION_PENDING` | Contingency recorded | Filer | Upload online later | Daily reminder | → `ACKNOWLEDGED` |
| `ACKNOWLEDGED` | Ack hash and reference | System | Evidence completeness | — | → `CLOSED` |
| `CLOSED` | Evidence pack sealed | CCO | Request revision | — | → `REVISION_REQUESTED` → run n+1 |

NIL returns pass every state with the same approvals. For mirrored runs (`source_system = FINBYX`), commands are disabled; state updates arrive by event; LDC raises its own `ComplianceIssueRaised` only if Finbyx has not (dedup by instance id).

### 5.2 Data batch

`RECEIVED → SCANNED → PARSED → PROFILED → MAPPED → VALIDATED → ACCEPTED | REJECTED | QUARANTINED (malware or PII violation)`; `SUPERSEDED` when a newer batch for the same dataset and period is accepted (the old batch stays readable and pinned in any snapshot that used it).

### 5.3 Mapping profile and COA mapping

`DRAFT → AI_PROPOSED (optional) → MAKER_CONFIRMED → CHECKER_APPROVED → ACTIVE → SUPERSEDED`. Approval of a mapping that affects a period with a `SIGNED_OFF` or filed run opens a revision assessment.

### 5.4 CIC cycle (per CIC × format × reference date)

`PLANNED → SNAPSHOT → EXTRACTED → VALIDATED → BUILT → APPROVED (nodal officer) → TRANSMITTED (tenant host/agent) → ACK_RECEIVED → REJECTIONS_INGESTED → (REPAIRED → RESUBMITTED)* → DQI_RECEIVED → CLOSED`; `FILE_REJECTED` path; per-CIC independence.

### 5.5 GST return and TDS statement

GST: `DATA_FROZEN → GENERATED → SCHEMA_VALIDATED → RECONCILED → CHECKER_APPROVED → FILED_BY_HUMAN → CLOSED`. TDS: `DATA_FROZEN → GENERATED → UTILITY_VALIDATED → CHECKER_APPROVED → FILED_BY_HUMAN → PROCESSED → CERTIFICATES_ISSUED → CLOSED`.

### 5.6 Framework decision and statements

Framework: `PROPOSED (engine) → CFO_APPROVED → LOCKED_FOR_FY`. Statements: `DRAFT → FINANCE_REVIEWED → AUDITOR_SHARED → ADJUSTED (n) → BOARD_APPROVED (P06 resolution ref) → FINAL`; `FinancialStatementsApproved` emitted on `FINAL` for non-Finbyx tenants (Ecosystem Spec §6.20 payload) and starts DNBS10/audited-return clocks.

### 5.7 Agentic preparation run (pseudo-code)

```text
on schedule(tenant, return_family, period):
  batches = latest_accepted(datasets_required(return_family), period)
  missing = required - batches
  if missing: create_task(data_owner, prepare_data_request(missing)); stop
  dq = run_dq(batches);   if dq.errors: create_task(maker, explain(dq.errors)); stop
  snap = freeze(batches, mapping_versions)            # deterministic
  for r in due_instances(return_family, period):
      run = generate(r, snap)                          # kernel
      v = validate(run); rc = reconcile(run)
  brief = draft_maker_brief(runs, v, rc)               # AI text; numbers re-verified by validator
  assert all(quoted_numbers(brief) ⊆ lineage_values(runs))
  notify(maker, brief)                                 # stops before MAKER_SUBMITTED
```

---

## 6. Screens and UX

Menu root: **Returns & Reporting** (tenant app). `i` help keys `help.ret.*`; glossary entries for every return code.

| Screen ID | Name | Menu path | Key elements | Roles |
|---|---|---|---|---|
| SCR-RET-01 | Reporting home | Returns › Home | Due in 7/30 days, overdue, acknowledgements pending, Data Room freshness, next-best actions | Makers, checkers, CFO, CCO |
| SCR-RET-02 | Return calendar | Returns › Calendar | Month/quarter view by regulator/portal/department; drag to assign owner; iCal subscribe (P04) | All reporting roles |
| SCR-RET-03 | Applicability matrix | Returns › Applicability | Returns × reasons with citations; variances; download PDF | CCO, auditors |
| SCR-RET-04 | Return instance | Returns › {code} › {period} | State bar, run history, lineage explorer, validation, reconciliation, approvals, package, guided upload, acknowledgement | Per matrix |
| SCR-RET-05 | Lineage explorer | … › Lineage | Cell → element → rows → batch → source line / Finbyx document | Makers, checkers, auditors |
| SCR-RET-06 | Guided upload | … › File | Ordered checklist, SHA-256 comparator, portal link (new tab), ack pre-read | Filer |
| SCR-RET-07 | Data Room | Returns › Data Room | Sources, batches by dataset/period, freshness, agent status, upload, template downloads | Makers, data owners |
| SCR-RET-08 | Batch detail | … › Batch {id} | Parse report, profile, DQ results, sample rows (masked), supersede history | Makers |
| SCR-RET-09 | Mapping studio | Returns › Mapping | Column mapping grid with AI suggestions and confidence; COA tree → statement lines and element families; unmapped list | Makers, checkers |
| SCR-RET-10 | Reconciliations | Returns › Reconciliations | Loan↔TB, sub-ledger↔GL, return↔TB, cross-return, period-on-period; explained-variance register | Makers, checkers, CFO |
| SCR-RET-11 | Revisions & queries | Returns › Revisions | Revision assessments, supervisory items, ad hoc requests | CCO, makers |
| SCR-RET-12 | Credit bureau | Returns › Credit bureau | Cycles per CIC/format, on-time status, rejections, DQI, nodal officer register | Bureau ops, nodal officer |
| SCR-RET-13 | GST | Returns › GST | GSTINs, periods, returns, IMS queue, reconciliations, ITC election, ARN log | Finance, tax |
| SCR-RET-14 | TDS/TCS | Returns › Income-tax | TANs, quarters, forms, challans, processing defaults, certificates, receivable matching | Finance, tax |
| SCR-RET-15 | MCA filings data | Returns › MCA | AOC-4 / MGT-7 / DPT-3 / MSME-1 / CSR-2 / LLP forms data packs and checklists | CS, CFO |
| SCR-RET-16 | Accounting bridge | Finance › Statements | Framework decision, TB versions, mapping, draft statements, notes, Schedule III datasets, validations, Board approval link | CFO office |
| SCR-RET-17 | Ratio data | Finance › Data for ratios | Element values by period with lineage (consumed by P09 dashboards) | CFO, CRO |
| SCR-RET-18 | Vidhi data-prep | Side panel on SCR-RET-07/09/10/04 | Proposals with accept/reject, maker brief, data requests | Makers |
| SCR-RET-19 | Registry (platform) | Console › Returns registry | Kernel versions, pack rows, verification status, variances, golden fixtures, rollout per tenant | plt_content_* |

**Fewer clicks.** Month-end "Prepare all" button runs the agentic run-book (§4N) for the period and opens a single maker brief; checker inbox shows all runs awaiting approval with bulk "approve" only when no WARNINGs remain unaccepted (each warning must be individually accepted); upload checklist remembers the last portal tab; the same package can be downloaded for all four CICs in one zip.

**Accessibility.** Lineage explorer and grids are keyboard-navigable; validation results have text severity labels; colour is never the only signal (NN-21).

---

## 7. Backend design

### 7.1 Modules

`ret` (Return Studio), `acc` (accounting bridge), `int` (connectors; Tally agent channel), `dms` (evidence), `wf` (calendar/tasks), `ai` (agent tools), kernel library linked in-process (no network dependency at generation time).

### 7.2 Tables (schemas `ret`, `ret_stg`, `acc`; tenant RLS; bitemporal where noted)

| Table | Key columns |
|---|---|
| `ret.kernel_pin` | tenant_id, kernel_version, pack_set_version, pinned_at, approved_by |
| `ret.registry_view` | materialised view of kernel rows + tenant overlay with status |
| `ret.tenant_return_definition` | tenant overlay definitions (badged), reuses kernel schema |
| `ret.applicability_decision` | entity_id, return_definition_id, rule_version, inputs_hash, result, citation, decided_at |
| `ret.return_due_instance` | definition, version, entity, period, reference_date, due_at, holiday_calendar, alert_stage, obligation_instance_id (P04), source_system |
| `ret.return_run` | instance_id, run_no, state, snapshot_id, cell_map_version, template_hash, file_hash, validation_hash, reconciliation_hash, package_hash, ack_ref, ack_hash, external_ref (Finbyx) |
| `ret.validation_result`, `ret.reconciliation_item`, `ret.explained_variance` | rule_id, severity, message, cell refs; element, return value, TB value, variance; reason, evidence, approver |
| `ret.registry_variance` | as FR-P11-03 |
| `ret.portal_user_alias` | portal, role, person_id, alias, valid_from/to (no credential columns — schema lint forbids `password`, `otp`, `secret`, `token` names) |
| `ret.supervisory_item`, `ret.revision_assessment` | as FR-P11-33/34 |
| `ret.data_source`, `ret.data_batch`, `ret.batch_file`, `ret.parse_report` | source config (no secrets; vault refs), batch metadata and states |
| `ret.mapping_profile`, `ret.mapping_rule`, `acc.coa_mapping` | versioned; approvals |
| `ret.reporting_snapshot` | entity, reference_date, book, batch_ids, mapping_versions, content_hash |
| `ret.cell_lineage` | run_id, cell_ref, element, aggregation, filter, row_count, query_hash, drilldown_ref |
| `ret_stg.cf_*` | CFDM entities (§4D), partitioned by tenant/entity/reference_date; token columns for PII |
| `ret.cic_cycle`, `ret.cic_file`, `ret.cic_rejection`, `ret.cic_dqi`, `ret.cic_nodal_officer` | per §4I |
| `ret.gst_return`, `ret.gst_ims_action`, `ret.itc_election` | per §4J |
| `ret.tds_statement`, `ret.tds_challan`, `ret.tds_receivable_match` | per §4K |
| `ret.mca_filing_pack` | form, FY, payload hash, attachments, checklist |
| `acc.framework_decision`, `acc.statement_run`, `acc.statement_line_value`, `acc.schedule3_dataset`, `acc.pbc_test_result` | per §4M |
| `ret.agent_proposal` | tool, inputs_hash, output, model/provider/version, confidence, accepted_by, accepted_at |

### 7.3 APIs (`/v1/returns/...`, `/v1/accounting/...`)

`GET /registry`, `GET /applicability?entity_id=`, `POST /applicability/commands/recompute`; `GET /due-instances?from&to&state`; `POST /due-instances/{id}/runs`; `POST /runs/{id}/commands/{freeze|generate|validate|reconcile|submit|approve|reject|sign-off|package|record-upload|record-portal-rejection|record-ack|contingency|close|request-revision}`; `GET /runs/{id}/lineage?cell=`; `GET /runs/{id}/package` (signed URL, logged); `POST /datasets/{dataset}/batches` (ingest API), `POST /uploads` (multipart), `GET /batches/{id}`; `POST /mapping-profiles`, `POST /coa-mappings/commands/approve`; `POST /reconciliations/run`; `POST /explained-variances`; `GET/POST /cic/cycles`, `POST /cic/cycles/{id}/commands/{build|approve|record-transmission|ingest-response}`; `GET/POST /gst/returns`, `POST /gst/ims-actions`; `GET/POST /tds/statements`; `POST /mca/packs`; `POST /accounting/framework/commands/resolve`; `POST /accounting/statements/runs`; `GET /accounting/elements?period=` (P09 consumer); agent tools under `/v1/ai/tools/ret.*` (P17 registry). Connector agent channel: `wss://agent.lawdocscomply.com/v1/agents/{id}` (mTLS; outbound from tenant).

### 7.4 Domain events

Published: `in.lawdocscomply.ret.ReturnDue.v1`, `ReturnGenerated.v1`, `ReturnValidated.v1`, `ReturnApproved.v1`, `ReturnFiled.v1`, `ReturnRevised.v1`, `ReturnStatusUpdated.v1` (Ecosystem names), `BureauFileGenerated.v1`, `BureauFileSubmitted.v1`, `BureauRejectionReceived.v1`, `GstReturnPrepared.v1`, `TdsStatementPrepared.v1`, `FinancialStatementsApproved.v1` (non-Finbyx tenants), `ComplianceIssueRaised.v1` (breach, overdue), internal `DataBatchAccepted.v1`, `MappingApproved.v1`, `FinancialDataSetReady.v1`, `RegistryVarianceRecorded.v1`. Consumed: Finbyx `Return*`, `Bureau*`, `PeriodClosed`, `FinancialStatementsApproved`, `GstReturnPrepared`, `TdsStatementPrepared`; Udofin `DLGDisclosurePublished`; P15 `EntityProfileChanged`; P03 `InstrumentVersionPublished`; P13 `PayrollRunApproved` (Form 138 data); P06 `ResolutionPassed` (statements Board approval).

**Event naming (X-01; review R4).** The `in.lawdocscomply.ret.*` names are internal. Cross-product events — `ReturnStatusUpdated`, `Return*` and `Bureau*` for non-Finbyx lenders, `FinancialStatementsApproved`, `ComplianceIssueRaised` — are published only by `int` under `in.infrabyx.reporting.*`, `in.infrabyx.bureau.*`, `in.infrabyx.finance.*` and `in.infrabyx.grc.*` (Ecosystem Spec §6.15, §6.18–§6.20); LDC as producer of `Return*`, `Bureau*` and `FinancialStatementsApproved` is an Ecosystem Spec v1.2 change request (master §19 item 6) and stays behind a flag until approved. For Finbyx tenants LDC consumes only and generates nothing (NN-39).

### 7.5 Jobs and Temporal workflows

`DueInstanceGenerator` (nightly; 13-month horizon); `ReturnRunWorkflow` (per run; timers and escalations); `ReturnPrepRunbook` (agentic scheduled run, §5.7); `CicCycleWorkflow` (per cycle; Annex VI timers); `GstPeriodWorkflow`; `TdsQuarterWorkflow`; `DataRoomFreshnessMonitor` (hourly); `TallyAgentHeartbeat` (5 min); `KernelUpgradePreview` (on new pack release: computes affected tenants and changed definitions); `GoldenFixtureCI` (build-time); `RevisionTriggerListener`; `RetentionAndLegalHold`.

---

## 8. Integrations (ports and adapters)

| Port | Adapters | Notes |
|---|---|---|
| `RETURNS_KERNEL` | `@infrabyx/returns-kernel` (in-process) | Pinned per tenant |
| `ECOSYSTEM_EVENTS` (P18) | Finbyx, Udofin | Mirrors and document references |
| `ACCOUNTING_SOURCE` | Tally agent (read), Tally file, Zoho Books API, SAP OData, SAP B1 Service Layer, Dynamics, generic file | Read-only; Finbyx `AccountingSink` push to Tally is Finbyx's, not LDC's |
| `LMS_SOURCE` | Generic tabular profiles, SFTP inbound, ingest API | Third-party LMS/LOS/CBS |
| `DOC_EXTRACT` (P07/P17) | OCR + Claude PDF | Annual reports, statements |
| `CIC_TRANSPORT` | LDC Connector Agent SFTP client on tenant host; or tenant's own SFTP host (LDC provides file + checksum) | Keys in tenant vault (BYOK) |
| `GST_SCHEMA` | GSTN offline-tool JSON schemas (kernel pack) | Human filing or tenant's GSP |
| `TDS_FORMAT` | File format per CBDT/TRACES (kernel pack) | Human filing |
| `MCA_PAYLOAD` | AOC-4 / XBRL mapping workbook / instance (when verified) | Human filing on MCA V3 |
| `STORAGE_PORT` (P19) | Tenant storage | Evidence export |
| `CALENDAR_PORT` (P04) | M365/Google/ICS | Due dates |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds / notes | Changed by |
|---|---|---|---|---|
| `ret.kernel.version` | G | latest verified | opt-in upgrade with preview | ten_admin + CCO |
| `ret.host.mode` | G | `LDC_NATIVE`; `FINBYX_MIRROR` for Finbyx families | per return family | CCO |
| `ret.freeze_lead_days` | T | 3 | 0–15 | Head of reporting |
| `ret.generate_lead_days` | T | 5 | 1–15 | Head of reporting |
| `ret.alert_stages` | T | T−7, T−3, T−1, breach | breach alert locked | CCO |
| `ret.escalation.ceo_after_wd` | T | 2 | 1–5 | CCO |
| `ret.holiday_calendar` | T | RBI Mumbai + registered-office State | add tenant calendars | ten_admin |
| `ret.tolerance.rounding_unit` | L | template unit | — | — |
| `ret.reasonableness.pct.<element>` | T | 25% | 1–200% | Head of reporting |
| `ret.revision.materiality` | T | any prudential-ratio cell or ≥ ₹1 crore | — | CCO |
| `ret.approval_matrix.<family>` | G | Appendix I §I.9 defaults | SoD floors | ten_admin + CCO |
| `ret.webform.record_cap` | L | 2,000 (CIMS) [VERIFY] | — | — |
| `ret.cic.enabled` | T | off (on when `cic_member[]` set) | — | CCO |
| `ret.cic.cycles` | L | W1, W2, W3, ME (+ DL by agreement) | from 1 Jul 2026 | — |
| `ret.cic.transport` | T | `TENANT_HOST` | `TENANT_HOST`, `LDC_AGENT` | CISO |
| `ret.gst.itc_option` | G (annual lock) | proportionate | proportionate / 50% (banks/FIs/NBFCs) | CFO |
| `ret.gst.einvoice.enabled` | T | off for financial institutions | on only if not exempt | CFO |
| `ret.tds.regime_cutover` | L | 1 Apr 2026 (ITA25) | — | — |
| `ret.mca.xbrl.enabled` | T | off; on when triggers met and not NBFC/bank | — | CS |
| `acc.framework.override` | G | engine decision | CFO + auditor note | CFO |
| `acc.rounding.unit` | T | by Schedule III turnover band | — | CFO |
| `ret.ai.mapping_suggestions` | T | on | — | ten_admin |
| `ret.ai.prep_runbook.schedule` | T | off | cron | Head of reporting |
| `ret.share_status_with_ops_hub` | T | off | metadata only if on (Ecosystem Spec) | ten_admin |
| `ret.tally.agent.allowed` | T | off | loopback enforced | CISO |

---

## 10. Security, privacy and audit

- No credential storage for any portal; schema lint and static scans forbid credential columns and HTTP clients configured for regulator domains (`*.rbi.org.in`, GST portal, income-tax portal, MCA, NSE/BSE upload endpoints, FINGate, CERSAI); build fails if added (NN-08, NN-17). CIC SFTP is a documented machine channel and runs only from tenant-controlled hosts or the tenant-installed agent with tenant-held keys.
- PII tokenisation in staging; clear values resolved only inside file builders; Aadhaar rejected; logs PII-free (NN-12, NN-32).
- Returns, CIC files and tax files are classed `CONFIDENTIAL-REG`; stored in India (NN-24), encrypted, access-logged, never emailed by the system.
- Every run, mapping, batch, approval and acknowledgement is ledger-backed (NN-02); corrections by revision runs or Correction Entries only (D-02).
- Tally agent: code-signed, signature-verified auto-update, outbound-only mTLS, refuses non-loopback Tally endpoints, device certificate revocable by the tenant, heartbeat and version inventory visible to IS auditors (P10).
- Retainer makers (LawDocs staff) see only the tenant scope granted; their actions are labelled and visible to the tenant (NN-30).

## 11. AI touchpoints and guardrails

| Touchpoint | Function | Guardrail |
|---|---|---|
| Column/COA mapping suggestion | Proposals with confidence | Human approval creates the mapping version |
| PDF/scan extraction | Tables from annual reports, audited statements | Staging candidates only; each value is confirmed by a maker against the highlighted source page, passes DQ and is recorded in lineage as a human-confirmed extraction (document hash, page, cell); unconfirmed values can never reach a return cell, statement or ratio (NN-37) |
| Validation explainer | Plain-language reason and fix suggestion | Cites rule ID and instrument paragraph |
| Variance commentary | Draft explanation | Figures re-verified against lineage; maker edits and owns |
| Missing-data finder and data requests | Lists missing fields and drafts the request | Request sent only by the maker |
| Maker brief (agentic run) | Summary of the run | Stops before `MAKER_SUBMITTED` |
| Prohibited | — | No cell writes, approvals, packages, uploads, external sends, credential use, or clear PII; no AI-generated figure in any return, statement or minute (NN-14, NN-22, NN-37) |

## 12. Acceptance criteria (`tests/acceptance/p11/*.feature`)

```gherkin
Feature: Finbyx tenants are mirrored, not recomputed
  Scenario: Generate is disabled for a Finbyx-sourced return
    Given a tenant with ret.host.mode = FINBYX_MIRROR for NBFC returns
    And a ReturnDue event from Finbyx for DNBS02 for quarter ending 30 Sep 2026
    When the maker opens the DNBS02 instance in LDC
    Then the "Generate" action is disabled with "Owned by Finbyx — package available by reference"
    And the instance shows state, hashes and acknowledgement as received from Finbyx

Feature: Non-Finbyx NBFC prepares DNBS02 from Tally and Excel
  Scenario: Return reconciles to the trial balance
    Given a BL NBFC that is not on Finbyx
    And an accepted TallyPrime trial-balance batch and an accepted LDC-DT-LOAN-v1.0 loan tape for 30 Sep 2026
    And an approved COA mapping with no unmapped non-zero ledgers
    When the maker freezes, generates and validates DNBS02
    Then the run reaches RECONCILED
    And every balance-sheet element differs from the TB by no more than the template rounding unit

Feature: Unmapped ledger blocks generation
  Scenario: A ledger with a balance is unmapped
    Given ledger "Suspense – Disbursement" with closing balance ₹12,40,000 is unmapped
    When the maker attempts to generate DNBS02
    Then generation fails with "LDC-RET-MAP-004 unmapped ledger" naming the ledger and balance

Feature: Deterministic package
  Scenario: Regenerating with unchanged inputs
    Given a SIGNED_OFF run with snapshot S, cell map C and template T
    When generate is called again with the same S, C and T
    Then the same file hash is returned and no new run is created

Feature: No credential storage
  Scenario: Static check for portal credentials
    When the build runs the regulatory-guard scan
    Then no table, column, secret reference or HTTP client is configured for rbi.org.in, gst.gov.in, incometax.gov.in or mca.gov.in domains

Feature: CIC incremental cadence from 1 July 2026
  Scenario: DPD-only change is reported in W2
    Given a consumer loan whose only change between the 9th and the 16th is DPD 31 → 38
    When the W2 cycle for the 16th is extracted
    Then the account is included
    And the W2 file is due within 4 calendar days of the 16th

Feature: Microfinance routing
  Scenario: MFI loans never appear in the consumer file
    Given a JLG microfinance loan
    When the consumer and MFI files are built for month-end
    Then the loan is present only in the MFI file

Feature: GST e-invoice exemption for NBFCs
  Scenario: No IRP JSON for an NBFC GSTIN
    Given an NBFC GSTIN with AATO ₹40 crore
    When GST documents are processed
    Then no e-invoice JSON is generated and the reason "CGST Rules r.48(4) exemption" is shown

Feature: Income-tax regime cut-over
  Scenario: Form selection by payment date
    Given a vendor payment dated 25 Mar 2026 and another dated 2 Apr 2026
    Then the first is reported in Form 26Q (ITA 1961) and the second in Form 140 (ITA 2025)

Feature: AI cannot write numbers
  Scenario: Agent commentary with a wrong figure is blocked
    Given Vidhi drafts variance commentary stating "advances grew to ₹512 crore"
    And lineage shows gross advances ₹498.6 crore
    Then the commentary is blocked with "LDC-RET-AI-002 figure not supported by lineage"

Feature: Revision assessment after audit adjustment
  Scenario: Audited CRAR differs from filed DNBS03
    Given a filed DNBS03 for 31 Mar 2026 with CRAR 19.42%
    And FinancialStatementsApproved with audited CRAR 19.10%
    Then a revision assessment opens listing DNBS03 with default decision REVISE

Feature: Framework resolution
  Scenario: Unlisted NBFC with net worth ₹320 crore on 31 Mar 2016
    When the framework resolver runs for FY 2026-27
    Then the result is Ind AS, Schedule III Division III, with citation "Companies (Ind AS) Rules 2015 r.4(1)(iv)"
```

NN tests: `NN-08_no_portal_credentials`, `NN-12_aadhaar_rejected_at_parse`, `NN-14_agent_no_cell_writes`, `NN-22_package_byte_identical`, `NN-23_finbyx_returns_not_recomputed`, `NN-24_return_files_india_region`, `NN-10_returns_export_complete`.

## 13. Deliverables and exit gate

1. Kernel interface ADR signed by Finbyx and LDC leads; kernel and packs consumed with pinned versions; golden-fixture CI.
2. `ret`, `ret_stg`, `acc` migrations; CFDM; LDC data templates (17 templates with `_Template_Info`); starter mapping profiles (Tally group names → Schedule III; three generic LMS exports).
3. Data Room with all §4C adapters (Tally agent read path behind flag); malware and PII scanning.
4. Return engine path for NBFC families (DNBS01–14, LEF, FMR family, Form A) on LDC-native data; mirror path for Finbyx; UCB, ARC, bank, SFB rows loaded `ACTIVE_UNVERIFIED` with calendar and evidence.
5. CIC builder (consumer, commercial, MFI) with golden files; GST and TDS packs; MCA AOC-4 payload; accounting bridge (framework resolver, statements, Schedule III datasets, ratio feed).
6. Vidhi data-prep tools and guardrails; agentic run-book behind flag.
7. Screens §6 with empty and error states and help content; dashboards §4O.
8. Exports per §4P with contract tests.
9. Documentation: `docs/modules/ret.md`, `docs/modules/acc.md`, data-template guide for clients, Tally agent installation guide, CIC onboarding checklist, filer's guide (guided upload).

Exit gate: (a) a non-Finbyx BL NBFC demo tenant produces reconciled, signed packages for DNBS02, DNBS04B and DNBS13 (NIL) for one quarter from Tally + Excel, records acknowledgements, and exports the evidence; (b) a Finbyx-linked demo tenant shows mirrored returns with no generate action; (c) a CIC month-end and one W-cycle build passes golden tests; (d) GSTR-1/3B and one Form 140 package pass schema/utility validation; (e) draft Division III statements tie to DNBS02 and the P09 CRAR; (f) all NN tests green.

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P11-01 | Owner's reference to supervisory-returns MDs of "28 Nov 2025" | 28 Nov 2025 is the DoR set (238 Directions); the SR directions are DoS of 31 Jul 2026 (NBFC /466, banks /415, SFB /424, UCB /442, ARC /469) | CCO / owner | Record in `docs/regulations/errata.md`; registry uses 31 Jul 2026 texts |
| OI-P11-02 | SR direction numbers for payments banks, LABs, RRBs, rural co-operative banks, AIFIs | Not fetched | Reporting analyst | Rows `ACTIVE_UNVERIFIED` |
| OI-P11-03 | UCB SR rows 8–11, 20, 21 frequency and timelines | Fetch truncated | Reporting analyst | `ACTIVE_UNVERIFIED` |
| OI-P11-04 | CIMS web-form record cap and S2S/ADF availability for NBFCs/UCBs | Finbyx [VERIFY: Sankalan help] | Reporting analyst | File upload default; S2S adapter flag OFF |
| OI-P11-05 | NHB returns for HFCs | Not in RBI SR | Reporting analyst | HFC pack OFF |
| OI-P11-06 | IFSCA, IRDAI, SEBI periodic report formats and portals | Many circulars; formats vary | Sector analysts | Calendar + evidence only (no generation) until verified |
| OI-P11-07 | Income-tax Act 2025 forms, sections, utility names | New Act; secondary concordances | Tax adviser | Rule-pack data with [VERIFY]; generation flagged |
| OI-P11-08 | AOC-4 NBFC (Ind AS) payload format (XBRL vs structured) | MCA V3 | CS | Data pack + checklist only |
| OI-P11-09 | MCA XBRL taxonomy tooling for instance generation | Licence and validation tool | CTO | Mapping workbook only |
| OI-P11-10 | CIC member specifications per bureau (encryption rules, validators) | Under member agreements | Bureau ops | Golden tests against public UCRF only |
| OI-P11-11 | Co-operative Registrar returns per State and MSCS s.120 details | 28 States + CRCS | Co-op analyst | Tenant-defined returns |
| OI-P11-12 | Principal Business Criteria wording in 2025 consolidated Directions | Consolidation may renumber | Reporting analyst | Computation as per 1999 press release; flagged |
| OI-P11-13 | Ind AS status for insurers, AIF/MF scheme accounting framework | IRDAI/SEBI | CA | Framework override by CFO with note |
| OI-P11-14 | Licensing of NSE/BSE XBRL utilities and taxonomy for automated instance generation | Exchange terms | CS | Mapping workbook only |
| OI-P11-15 | Whether LDC may send CIC borrower alerts (CIR 34(1)(i)) on the lender's behalf | TRAI DLT, consent, contract | Counsel | Lender's own system sends; LDC checks evidence |

## 15. Sources (accessed 25 Oct 2026 unless stated)

- RBI List of Returns — https://rbi.org.in/scripts/BS_Listofallreturns.aspx ; Reporting platforms (updated 23 Oct 2026) — https://rbi.org.in/scripts/ReportingPlaform.aspx ; Data Definitions (updated 17 Jun 2026) — https://rbi.org.in/scripts/DataDefinition.aspx ; Reporting FAQ archives — https://rbi.org.in/scripts/ReportingFAQ.aspx
- RBI (Commercial Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/415 — https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13638
- RBI (Small Finance Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/424 — https://taxguru.in/rbi/rbi-issues-small-finance-banks-supervisory-returns-directions-2026-effect.html
- RBI (Urban Co-operative Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/442 — https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13611
- RBI (ARC – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/469 — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13584
- RBI press release 2026-2027/787 (64 DoS Directions, 31 Jul 2026) — https://rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63265 ; RBI 238 consolidated DoR Directions (28 Nov 2025) — https://website.rbi.org.in/documents/d/rbi/pr1588rbiconsolidatedmasterdirections-1-
- Repealed predecessor: Master Direction – Filing of Supervisory Returns, RBI/DoS.DSG/2023-24/110, 27 Feb 2024 — https://website.rbi.org.in/documents/87730/39710850/Final+MD+on+Returns+filing+%28Governor+Approved%29+-+2024+%2827-2-2024%29.pdf
- Finbyx Master Prompt v1.5, Parts 7B (RR1–RR9) and 7C (AC1–AC7) (owner's corpus, 23 Oct 2026) — NBFC SR inventory, CIC cadence and UCRF formats, GST, ITA25 concordance, TallyPrime 7.0 JSON, Rule 11(g)
- Infrabyx Ecosystem Integration Specification v1.1 §§3.11, 5.2, 6.18–6.20, 9.1–9.3, 10.2, 12.1

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37, NN-39; X-09 (`LDC-DT-*` data templates), X-12, X-25, X-31, X-32 (return generation scope in v1), X-41 (Tally read-only)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

