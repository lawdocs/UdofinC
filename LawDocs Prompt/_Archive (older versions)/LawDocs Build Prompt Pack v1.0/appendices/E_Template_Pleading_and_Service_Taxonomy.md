# Appendix E — Template, Pleading and Service Taxonomy

**Status:** Binding (content load list and codes). Values marked [VERIFY], [OWNER] or [COUNSEL] are seeds that the named owner confirms before the item is published.
**Used by:** P06 (template library load, lanes, reviewer of record, formalities metadata), P07 (agreement types), P08 (eligibility and formalities seeds for Appendix F), P10 (pleadings library, notices), P14 (service catalogue), P16 (review and service SKUs), P21 (page inventory, slugs, redirects, noindex rules), P23 (content QA gate).

**How to use.** This appendix is the single list of every document, pleading and service page that LawDocs publishes from the owner's four manuals (`src/Manual_Documents.md`, `Manual_Pleadings.md`, `Manual_Compliance.md`, `Manual_Start_a_Business.md`), compiled from R5 (§8 and `R5_Document_Page_Inventory.csv`). Load it as seed data into `tpl.category`, `tpl.subcategory`, `tpl.template` (status `DRAFT`), `pld` and `bsv` catalogues; never hard-code it. Every row keeps its R5 ID as `canonical_doc_id`; slugs are the P21 URL leaf; aliases become 301 redirects. Changes to this list after load are content changes (NN-30) made in Template Studio with maker-checker — this appendix is then regenerated from the database, not edited by hand.

---

## 1. Codes and legend

| Column | Codes |
|---|---|
| **eSign** (eligibility seed for Appendix F; P08 gate decides — NN-07) | **V** = eSign valid (Aadhaar eSign/DSC) per R5 · **C** = check: interest in immovable property or stamping/registration route; eSign may be valid but stamp/registration rules govern · **X** = excluded by IT Act 2000 s.1(4) and First Schedule (wills and testamentary dispositions, trusts, powers of attorney other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity, negotiable instruments other than cheques — R3 LG-003) → wet-ink pack · **R** = R5 marked "not valid", but R3 LG-003 (V-WEB) shows Entry 5 (contracts for sale or conveyance of immovable property) was **omitted** by S.O. 4720(E) of 26 Sep 2022; eSign is therefore not barred by the IT Act, but compulsory registration (Registration Act 1908 s.17) and State e-registration acceptance decide the route → default **wet-ink + registration pack** until Appendix F records the State position [COUNSEL; VERIFY per State] |
| **Upcoming** | `(U)` after the ID = the sub-category is "(upcoming)" in the manual; sub-category tables show **L** (live) / **U** (upcoming). Upcoming items stay `noindex` until content exists (R5 §2). |
| **Type** (drafting lane — P06 FR-P06-03) | **TA** = template automation, free on the public page; AI-custom drafting available on top under the review gate (NN-14, CH-30) · **AI** = no vetted template is practical (bespoke by nature); AI-custom only, always behind the review gate · **PRO** = professional-only (no self-serve output; sold as a P16 service) · **PLD** = court/forum document drafted in the P10 Pleadings Studio (advocate review gate rules of P10 apply) · **RET** = retire (law repealed/replaced) |
| **Reviewer** (profession of the reviewer of record for the template and of the paid reviewer) | **ADV** advocate · **CS** company secretary · **CA** chartered accountant · **PA** registered patent agent · **TMA** trademark agent · **ED** editorial (non-legal document; `PLT_CONTENT_EDITOR` + editorial checker) · combinations mean either |
| **Formalities** (seed for template metadata — P06 FR-P06-05; rates and State rules live in P03/P08 rule packs) | **S** = stamp duty chargeable or potentially chargeable — check the State Stamp Act article (Indian Stamp Act 1899 s.3, s.17 stamp before or at execution, s.35 inadmissible if unstamped — R3 LG-096/097) · **R** = compulsory registration (Registration Act 1908 s.17(1); presentation within 4 months, s.23 — R3 LG-104) · **R\*** = compulsory if the instrument creates, declares, assigns, limits or extinguishes an interest in immovable property of ₹100 or more (s.17(1)(b)) · **R?** = conditional or optional (e.g., leases from year to year or above one year — s.17(1)(d); part-performance agreements — s.17(1A); wills — optional, s.18; adoption deeds — HAMA 1956 s.16 presumption) · **W2** = two attesting witnesses required by statute (wills — Indian Succession Act 1925 s.63; gifts of immovable property — TPA 1882 s.123; mortgages ≥ ₹100 — TPA s.59) · **W2\*** = W2 if immovable property · **N** = notary/oath commissioner (affidavits, declarations — Notaries Act 1952, Oaths Act 1969 — R3 LG-106); POAs are customarily notarised/authenticated · **F** = filing or recordal with an authority (MCA/ROC, Registrar of Firms or Societies, IP office, labour authority, marriage registrar) · **F\*** = filing only in specified cases (e.g., resolutions requiring MGT-14) · **CF** = court/forum fee on filing · **—** = none known. All [LAW] items are verified by `PLT_LEGAL_REVIEWER` before a template is published; State variations are [VERIFY]. |
| **Wave** (content/launch priority) | **1** = launch set (high-demand, live sub-categories with template lists) · **2** = second load (other live sub-categories) · **3** = upcoming categories, specialist or professional-only items · **P10** = loaded with the Pleadings Studio (Wave 2 build) · **—** = not published (alias/retire) |
| **Content status** (sub-category level, inherited by its documents) | **HC** = manual has usable copy (rewrite in brand voice and plagiarism-check before use — R5 §4 policy applies to every row) · **RW** = needs rewrite: thin (< 500 words) or stub (< 150 words) · **CP** = copied third-party text or borrowed line detected; rewrite from scratch (`?` = suspected, scan pending) · **OL** = outdated law reference; fix listed (seed backlog §7) |
| **Slug** | Leaf under `/documents/{category}/{sub-category}/`. `†` = corrected from the R5 proposal (typo/grammar); the R5 form becomes a 301. |
| **≈** | Near-duplicate of the named canonical; merge as a variant toggle unless `PLT_LEGAL_REVIEWER` records why it differs [OWNER] (P06 FR-P06-02). |

**Reconciliation note (raise to P08/Appendix F owner).** R5 flags 35 documents "not valid"; this appendix keeps **21 as X** (wills, POAs, trusts and testamentary items, promissory notes) and marks **14 as R** (agreements for sale and conveyance of immovable property, mortgage/reconveyance, release of mortgaged property, gifts of immovable property, sale deed to members) following R3 LG-003. Affidavits are **V** for signature but always **N** — an eSigned affidavit is never presented as sworn (NN-07; R3 LG-106).

---

## 2. Documents (18 categories → 134 sub-categories → 347 entries / 327 canonical documents)

R5 counted 330 unique documents; this appendix finds three further duplicates (D3.12.3 → D12.6.2; D11.9.4 → D11.5.4; D11.9.5 → D3.5.1) and five near-duplicates (≈), leaving **327 canonical document templates** to load.

### 2.1 Category summary

| Code | Category | Hub slug | Sub-categories | Live / upcoming | Document entries (R5) | Canonical documents | Dominant wave |
|---|---|---|---|---|---|---|---|
| D1 | Deals & Agreements | `deals-and-agreements` | 10 | 9 / 1 | 40 | 27 | 2 |
| D2 | Family Matters | `family-matters` | 7 | 6 / 1 | 19 | 19 | 2 |
| D3 | Financial Transactions | `financial-transactions` | 13 | 13 / 0 | 56 | 52 | 2 |
| D4 | Operations & Management | `operations-and-management` | 8 | 7 / 1 | 43 | 43 | 2 |
| D5 | Planning & Execution | `planning-and-execution` | 8 | 1 / 7 | 8 | 8 | 3 |
| D6 | Marketing & Sales | `marketing-and-sales` | 9 | 1 / 8 | 2 | 2 | 3 |
| D7 | Industries (upcoming) | `industries` | 9 | 0 / 9 | 5 | 5 | 3 |
| D8 | Intellectual Property Rights | `intellectual-property-rights` | 3 | 3 / 0 | 11 | 11 | 1 |
| D9 | IT and Websites | `it-and-websites` | 8 | 6 / 2 | 4 | 4 | 2 |
| D10 | HR and Service | `hr-and-service` | 11 | 7 / 4 | 24 | 24 | 3 |
| D11 | Legal | `legal` | 12 | 12 / 0 | 39 | 37 | 2 |
| D12 | Property Transactions | `property-transactions` | 8 | 7 / 1 | 43 | 43 | 1 |
| D13 | RERA | `rera` | 3 | 3 / 0 | 1 | 1 | 2 |
| D14 | SEBI (upcoming) | `sebi` | 3 | 0 / 3 | 0 | 0 | 3 |
| D15 | Secretarial (upcoming) | `secretarial` | 9 | 0 / 9 | 0 | 0 | 3 |
| D16 | Students | `students` | 3 | 3 / 0 | 17 | 16 | 1 |
| D17 | Succession and Inheritance | `succession-and-inheritance` | 6 | 6 / 0 | 35 | 35 | 2 |
| D18 | Accounting & Tax (upcoming) | `accounting-and-tax` | 4 | 0 / 4 | 0 | 0 | 3 |
| **Total** | | | **134** | | **347** | **327** | |

### 2.2 Sub-categories and documents by category

#### D1. Deals & Agreements — `/documents/deals-and-agreements`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D1.1 | Collaboration and Joint Venture | `collaboration-and-joint-venture` | L | 5 | 2 | HC · CP? (scan FAQs) |
| D1.2 | Contracts and Agreements | `contracts-and-agreements` | L | 7 | 1 | HC · OL: IPC→BNS; SRA 2018 |
| D1.3 | Distributorship & Agencies | `distributorship-and-agencies` | L | 10 | 1 | HC |
| D1.4 | Franchise and License | `franchise-and-license` | L | 10 | 1 | HC |
| D1.5 | Mergers and Acquisitions | `mergers-and-acquisitions` | L | 3 | 2 | HC · OL: IT Act 1961→2025 |
| D1.6 | Formal Proposals | `formal-proposals` | L | 0 — to define (§3) | 2 | RW (thin) |
| D1.7 | Quotes | `quotes` | L | 1 | 2 | RW (thin) |
| D1.8 | Statement of Work | `statement-of-work` | L | 4 | 1 | RW (thin) |
| D1.9 | Shipping agreements | `shipping-agreements` | U | 0 — to define (§3) | 3 | RW (thin) |
| D1.10 | Sign off | `sign-off` | L | 0 — to define (§3) | 2 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D1.1.1 | Collaboration agreement with foreign company | `collaboration-agreement-with-foreign-company` | V | TA | ADV | S | 2 |
| D1.1.2 | Joint venture agreement | `joint-venture-agreement` | V | TA | ADV | S | 2 |
| D1.1.3 | Technical collaboration | `technical-collaboration` | V | TA | ADV | S | 2 |
| D1.1.4 | Transfer of shares | `transfer-of-shares` | V | TA | CS | S | 2 |
| D1.1.5 | Allotment of shares | `allotment-of-shares` | V | TA | CS | S, F | 2 |
| D1.2.1 | Amendment agreement | `amendment-agreement` | V | TA | ADV | S | 1 |
| D1.2.2 | Business agreement | `business-agreement` | V | TA | ADV | S | 1 |
| D1.2.3 | Confidentiality and non disclosure agreement | `confidentiality-and-non-disclosure-agreement` | V | TA | ADV | S | 1 |
| D1.2.4 | Consultancy agreement | `consultancy-agreement` | V | TA | ADV | S | 1 |
| D1.2.5 | Notice for termination of contract | `notice-for-termination-of-contract` | V | TA | ADV | — | 1 |
| D1.2.6 | Revocation of agreement | `revocation-of-agreement` | V | TA | ADV | S | 1 |
| D1.2.7 | Settlement agreement | `settlement-agreement` | C | TA | ADV | S | 1 |
| D1.3.1 | Agreement with commission agent | `agreement-with-commission-agent` | V | TA | ADV | S | 1 |
| D1.3.2 | Dealership agreement | `dealership-agreement` | V | TA | ADV | S | 1 |
| D1.3.3 | Distributorship agreement | `distributorship-agreement` | V | TA | ADV | S | 1 |
| D1.3.6 | Revocation of distributorship or franchise | `revocation-of-distributorship-or-franchise` | V | TA | ADV | S | 1 |
| D1.4.4 | Franchise agreement | `franchise-agreement` | V | TA | ADV | S | 1 |
| D1.4.5 | Notice to franchise | `notice-to-franchise` | V | TA | ADV | — | 1 |
| D1.4.7 | Leave and license agreement | `leave-and-license-agreement` | C | TA | ADV | S, R? | 1 |
| D1.4.8 | License to use immovable property | `license-to-use-immovable-property` | C | TA | ADV | S, R? | 1 |
| D1.4.9 | Notice to licensee | `notice-to-licensee` | V | TA | ADV | — | 1 |
| D1.4.10 | Revocation of licensee | `revocation-of-licensee` | V | TA | ADV | S | 1 |
| D1.7.1 | Quotation | `quotation` † | V | TA | ED | — | 2 |
| D1.8.1 | Interior design | `interior-design` | V | TA | ADV | S | 1 |
| D1.8.2 | IT system installation | `it-system-installation` | V | TA | ADV | S | 1 |
| D1.8.3 | Software development | `software-development` | V | TA | ADV | S | 1 |
| D1.8.4 | Websites | `websites` | V | TA | ADV | S | 1 |

Aliases (no own page; 301 to canonical): D1.3.4 Franchise agreement → `franchise-and-license`; D1.3.5 Notice to franchise → `franchise-and-license`; D1.3.7 Leave and license agreement → `franchise-and-license`; D1.3.8 License to use immovable property → `franchise-and-license`; D1.3.9 Notice to licensee → `franchise-and-license`; D1.3.10 Revocation of licensee → `franchise-and-license`; D1.4.1 Agreement with commission agent → `distributorship-and-agencies`; D1.4.2 Dealership agreement → `distributorship-and-agencies`; D1.4.3 Distributorship agreement → `distributorship-and-agencies`; D1.4.6 Revocation of distributorship or franchise → `distributorship-and-agencies`; D1.5.1 Business Plan → `investment-support-and-business-funding`; D1.5.2 Founders Agreement → `investment-support-and-business-funding`; D1.5.3 Fund raising → `investment-support-and-business-funding`.

#### D2. Family Matters — `/documents/family-matters`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D2.1 | Child Custody | `child-custody` | L | 2 | 2 | HC |
| D2.2 | Divorce | `divorce` | L | 7 | 2 | HC · OL: CrPC→BNSS; s.13B waiver |
| D2.3 | Domestic Violence | `domestic-violence` | L | 3 | 2 | HC · OL: IPC 498A→BNS 85/86 |
| D2.4 | Maintenance | `maintenance` | L | 6 | 2 | HC · OL: CrPC 125→BNSS 144 |
| D2.5 | Marriage | `marriage` | L | 1 | 1 | HC · OL: CrPC→BNSS |
| D2.6 | Mutual Divorce | `mutual-divorce` | U | 0 — to define (§3) | 3 | RW (stub) |
| D2.7 | Senior Citizens Protection | `senior-citizens-protection` | L | 0 — to define (§3) | 2 | HC · OL: CrPC→BNSS |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D2.1.1 | Child custody application before court | `child-custody-application-before-court` | V | PLD | ADV | CF, N | P10 |
| D2.1.2 | Deed of settlement for the benefit of minor children | `deed-of-settlement-for-the-benefit-of-minor-children` | C | TA | ADV | S, R* | 2 |
| D2.2.1 | Application for Release of Property to the Police | `application-for-release-of-property-to-the-police` | C | PLD | ADV | CF, N | P10 |
| D2.2.2 | Application to Provide extract of Marriage Register | `application-to-provide-extract-of-marriage-register` | V | TA | ADV | F | 2 |
| D2.2.3 | Divorce Petition by Hindu Wife | `divorce-petition-by-hindu-wife` | V | PLD | ADV | CF, N | P10 |
| D2.2.4 | Petition for Judicial Separation | `petition-for-judicial-separation` | V | PLD | ADV | CF, N | P10 |
| D2.2.5 | Petition for Nullity of Marriage | `petition-for-nullity-of-marriage` | V | PLD | ADV | CF, N | P10 |
| D2.2.6 | Restitution of Conjugal Rights under Muslim Law | `restitution-of-conjugal-rights-under-muslim-law` | V | PLD | ADV | CF, N | P10 |
| D2.2.7 | Separation Agreement | `separation-agreement` | V | TA | ADV | S | 2 |
| D2.3.1 | Application for Domestic Violence | `application-for-domestic-violence` | V | PLD | ADV | N | P10 |
| D2.3.2 | Domestic incident report | `domestic-violence-incident-report` | V | PLD | ADV | — | P10 |
| D2.3.3 | Information for Domestic Violence | `information-for-domestic-violence` | V | PLD | ADV | — | P10 |
| D2.4.1 | Application for Staying Recovery Amount | `application-for-staying-recovery-amount` | V | PLD | ADV | CF, N | P10 |
| D2.4.2 | Compromise Agreement regarding Maintenance | `compromise-agreement-regarding-maintenance` | V | TA | ADV | S | 2 |
| D2.4.3 | Petition for Maintenance by Wife | `petition-for-maintenance-by-wife` | V | PLD | ADV | CF, N | P10 |
| D2.4.4 | Petition of the Husband for Maintenance | `petition-of-the-husband-for-maintenance` | V | PLD | ADV | CF, N | P10 |
| D2.4.5 | Reply of the Husband for Maintenance | `reply-of-the-husband-for-maintenance` | V | PLD | ADV | CF, N | P10 |
| D2.4.6 | Reply of the Wife for Maintenance | `reply-of-the-wife-for-maintenance` | V | PLD | ADV | CF, N | P10 |
| D2.5.1 | Application for filing Memorandum of Marriage | `application-for-filing-memorandum-of-marriage` | V | TA | ADV | F | 1 |

#### D3. Financial Transactions — `/documents/financial-transactions`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D3.1 | Acknowledgement | `acknowledgement` | L | 6 | 1 | RW (thin) |
| D3.2 | Banking and Finance | `banking-and-finance` | L | 3 | 2 | HC · OL: CPA 1986; CA 1956 |
| D3.3 | Bonds | `bonds` | L | 6 | 2 | HC · OL: CrPC→BNSS |
| D3.4 | Compromise | `compromise` | L | 3 | 2 | RW (thin) |
| D3.5 | Dishonour of Cheques | `dishonour-of-cheques` | L | 1 | 1 | HC · OL: IPC→BNS |
| D3.6 | Hire-Purchase | `hire-purchase` | L | 6 | 2 | HC |
| D3.7 | Hypothecation and Pledge | `hypothecation-and-pledge` | L | 5 | 2 | HC |
| D3.8 | Indemnity and Guarantee | `indemnity-and-guarantee` | L | 7 | 1 | HC |
| D3.9 | Insurance | `insurance` | L | 2 | 2 | HC |
| D3.10 | Promissory Note | `promissory-note` | L | 4 | 2 | HC · OL: eSign claim |
| D3.11 | Receipts | `receipts` | L | 4 | 1 | HC |
| D3.12 | Release Deeds | `release-deeds` | L | 4 | 2 | HC |
| D3.13 | Sale of Goods | `sale-of-goods` | L | 5 | 1 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D3.1.1 | Acceptance of offer or terms and conditions | `acceptance-of-offer-or-terms-and-conditions` | V | TA | ADV | — | 1 |
| D3.1.2 | Acknowledgment of consignment | `acknowledgment-of-consignment` | V | TA | ADV | — | 1 |
| D3.1.3 | Acknowledgement of payment | `acknowledgement-of-payment` | V | TA | ADV | S | 1 |
| D3.1.4 | Acknowledgement through letter | `acknowledgement-through-letter` | V | TA | ADV | — | 1 |
| D3.1.5 | Simple acknowledgement | `simple-acknowledgement` | V | TA | ADV | — | 1 |
| D3.1.6 | Short form of acknowledgement | `short-form-of-acknowledgement` | V | TA | ADV | — | 1 |
| D3.2.1 | Indemnity to bank | `indemnity-to-bank` | V | TA | ADV | S | 2 |
| D3.3.1 | Administration bond | `administration-bond` | V | TA | ADV | S | 2 |
| D3.3.2 | Bond by debtor | `bond-by-debtor` | V | TA | ADV | S | 2 |
| D3.3.3 | Installment bond | `installment-bond` | V | TA | ADV | S | 2 |
| D3.3.4 | Loan bond | `loan-bond` | V | TA | ADV | S | 2 |
| D3.3.5 | Security bonds | `security-bonds` | V | TA | ADV | S | 2 |
| D3.3.6 | Simple bonds | `simple-bonds` | V | TA | ADV | S | 2 |
| D3.4.1 | Settlement agreement between debtor and creditor (≈ D1.2.7) | `settlement-agreement-between-debtor-and-creditor` | C | TA | ADV | S | 2 |
| D3.4.2 | Compromise during a court case | `compromise-during-a-court-case` † | V | TA | ADV | S, CF | 2 |
| D3.4.3 | Simple compromise | `simple-compromise` | V | TA | ADV | S | 2 |
| D3.5.1 | Notice for dishonour of cheque (s.138 NI Act) | `notice-for-dishonour-of-cheque` † | V | TA | ADV | — | 1 |
| D3.6.1 | Assignment of benefit of hire purchase agreement | `assignment-of-benefit-of-hire-purchase-agreement` | V | TA | ADV | S | 2 |
| D3.6.2 | Guarantee of performance of hire purchase | `guarantee-of-performance-of-hire-purchase` | V | TA | ADV | S | 2 |
| D3.6.3 | Hire purchase agreement | `hire-purchase-agreement` | V | TA | ADV | S | 2 |
| D3.6.4 | Hire purchase of goods | `hire-purchase-of-goods` | V | TA | ADV | S | 2 |
| D3.6.5 | Notice for termination of hire purchase agreement | `notice-for-termination-of-hire-purchase-agreement` | V | TA | ADV | — | 2 |
| D3.6.6 | Revocation of hire purchase agreement | `revocation-of-hire-purchase-agreement` | V | TA | ADV | S | 2 |
| D3.7.1 | Deed of pledge | `deed-of-pledge` | V | TA | ADV | S | 2 |
| D3.7.2 | Cash credit facility agreement (bank) | `granting-cash-credit-facilities-by-bank` | V | TA | ADV | S | 2 |
| D3.7.3 | Hypothecation of movables | `hypothecation-of-movables` | V | TA | ADV | S | 2 |
| D3.7.4 | Letter of credit and bank guarantee facilities | `letter-of-credit-and-bank-guarantee-facilities` | V | TA | ADV | S | 2 |
| D3.7.5 | Pledges | `pledges` | V | TA | ADV | S | 2 |
| D3.8.1 | Deed of counter guarantee | `deed-of-counter-guarantee` | V | TA | ADV | S | 1 |
| D3.8.2 | Deed of indemnity bond | `deed-of-indemnity-bond` | V | TA | ADV | S | 1 |
| D3.8.3 | Guarantee agreement | `guarantee-agreement` | V | TA | ADV | S | 1 |
| D3.8.4 | Indemnity by debtor to the guarantor | `indemnity-by-debtor-to-the-guarantor` | V | TA | ADV | S | 1 |
| D3.8.5 | Indemnity by land owner | `indemnity-by-land-owner` | V | TA | ADV | S | 1 |
| D3.8.6 | Indemnity for loss | `indemnity-for-loss` | V | TA | ADV | S | 1 |
| D3.8.7 | Letter of guarantee | `letter-of-guarantee` | V | TA | ADV | S | 1 |
| D3.9.1 | Application for compensation (insurance claim) | `application-for-compensation` | V | TA | ADV | — | 2 |
| D3.9.2 | Notice for providing compensation | `notice-for-providing-compensation` | V | TA | ADV | — | 2 |
| D3.10.1 | Joint promissory notes | `joint-promissory-notes` | X | TA | ADV | S | 2 |
| D3.10.2 | Promissory note by representative | `promissory-note-by-representative` | X | TA | ADV | S | 2 |
| D3.10.3 | Promissory note for payment | `promissory-note-for-payment` | X | TA | ADV | S | 2 |
| D3.10.4 | Promissory note with surety | `promissory-note-with-surety` | X | TA | ADV | S | 2 |
| D3.11.1 | Receipt for papers | `receipt-for-papers` | V | TA | ADV | — | 1 |
| D3.11.2 | Receipt for payment | `receipt-for-payment` | V | TA | ADV | S | 1 |
| D3.11.3 | Receipt for sale consideration | `receipt-for-sale-consideration` | V | TA | ADV | S | 1 |
| D3.11.4 | Rent receipt | `rent-receipt` | V | TA | ADV | S | 1 |
| D3.12.1 | Release bond | `release-bond` | C | TA | ADV | S | 2 |
| D3.12.2 | Release deed by debtor to a creditor | `release-deed-by-debtor-to-a-creditor` | C | TA | ADV | S | 2 |
| D3.13.1 | Agreement for sale of Car | `agreement-for-sale-of-car` | V | TA | ADV | S | 1 |
| D3.13.2 | Sale of future goods | `sale-of-future-goods` | V | TA | ADV | S | 1 |
| D3.13.3 | Sale of Goods under Buyer's Trademark | `sale-of-goods-under-buyers-trademark` | V | TA | ADV | S | 1 |
| D3.13.4 | Sale of goods | `sale-of-goods` | V | TA | ADV | S | 1 |
| D3.13.5 | Sale of Ready Goods | `sale-of-ready-goods` | V | TA | ADV | S | 1 |

Aliases (no own page; 301 to canonical): D3.2.2 Installment bond → `bonds`; D3.2.3 Loan bond → `bonds`; D3.12.3 Release of an interest in immovable property → D12.6.2 (new); D3.12.4 Release of right of way → `release-and-nocs`.

#### D4. Operations & Management — `/documents/operations-and-management`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D4.1 | Clubs and Societies | `clubs-and-societies` | L | 6 | 2 | HC · OL: CA 1956 |
| D4.2 | Companies | `companies` | L | 13 | 2 | HC · OL: CA 1956; Listing Agmt→LODR |
| D4.3 | Limited Liability Partnership | `limited-liability-partnership` | L | 4 | 2 | RW (thin) |
| D4.4 | MSME | `msme` | L | 0 — to define (§3) | 2 | RW (thin) · OL: Udyog Aadhaar→Udyam |
| D4.5 | Office Management | `office-management` | U | 0 — to define (§3) | 3 | RW (stub) |
| D4.6 | Partnership Firm | `partnership-firm` | L | 11 | 1 | HC · OL: IT Act 1961→2025 |
| D4.7 | Proprietorship | `proprietorship` | L | 3 | 1 | RW (thin) |
| D4.8 | Trusts and Wakfs | `trusts-and-wakfs` | L | 6 | 2 | HC · OL: eSign claim |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D4.1.1 | Affidavit of declaration | `affidavit-of-declaration` | V | TA | ADV | S, N | 2 |
| D4.1.2 | By laws of society | `by-laws-of-society` | V | TA | ADV | F | 2 |
| D4.1.3 | Calling for general meeting | `calling-for-general-meeting` | V | TA | ADV | — | 2 |
| D4.1.4 | Formation of club | `formation-of-club` | V | TA | ADV | F | 2 |
| D4.1.5 | Letters to members (club/society) | `letters-to-members` † | V | AI | ADV | — | 2 |
| D4.1.6 | Sale deed to members | `sale-deed-to-members` | R | TA | ADV | S, R | 2 |
| D4.2.1 | Agreement for promoting a company | `agreement-for-promoting-a-company` | V | TA | CS | S | 2 |
| D4.2.2 | Agreement for underwriting shares of a company | `agreement-for-underwriting-shares-of-a-company` † | V | TA | CS | S | 2 |
| D4.2.3 | Articles of Association | `articles-of-association` † | V | TA | CS | S, F | 2 |
| D4.2.4 | Brokerage agreement | `brokerage-agreement` | V | TA | CS | S | 2 |
| D4.2.5 | Listing agreement BSE | `listing-agreement-bse` | V | RET | CS | S | — |
| D4.2.6 | Listing agreement NSE | `listing-agreement-nse` | V | RET | CS | S | — |
| D4.2.7 | Shareholders agreements | `shareholders-agreements` | V | TA | CS | S | 2 |
| D4.2.8 | Appointment of a general manager | `appointment-of-a-general-manager` | V | TA | CS | — | 2 |
| D4.2.9 | Company affidavits | `company-affidavits` | V | TA | CS | S, N | 2 |
| D4.2.10 | Company resolution | `company-resolution` | V | TA | CS | F* | 2 |
| D4.2.11 | Declaration of solvency by company | `declaration-of-solvency-by-company` | V | PRO | CS | N, F | 3 |
| D4.2.12 | Indemnity for the registration of shares | `indemnity-for-the-registration-of-shares` | V | TA | CS | S | 2 |
| D4.2.13 | Complaint of professional misconduct against a Chartered Accountant | `professional-misconduct-by-chartered-accountant` | V | TA | CA/ADV | F | 2 |
| D4.3.1 | Limited Liability Partnership agreement | `limited-liability-partnership-agreement` | V | TA | CS | S, F | 2 |
| D4.3.2 | Consent Letter | `consent-letter` | V | TA | CS | F | 2 |
| D4.3.3 | Resolution authorising body corporate as partner | `resolution-authorising-body-corporate-as-partner` | V | TA | CS | F | 2 |
| D4.3.4 | Statement by professional regarding compliances of incorporation | `statement-by-professional-regarding-compliances-of-incorporation` | V | PRO | CS | F | 3 |
| D4.6.1 | Partnership Agreement | `partnership-agreement` | V | TA | ADV | S, F | 1 |
| D4.6.2 | Partnership agreement with managing and sleeping Partners | `partnership-agreement-with-managing-and-sleeping-partners` | V | TA | ADV | S, F | 1 |
| D4.6.3 | Partnership agreement between two partnership firms | `partnership-agreement-between-two-partnership-firms` | V | TA | ADV | S, F | 1 |
| D4.6.4 | Partnership agreement between Partnership firm and HUF | `partnership-agreement-between-partnership-firm-and-huf` | V | TA | ADV | S, F | 1 |
| D4.6.5 | Agreement admitting new partner | `agreement-admitting-new-partner` | V | TA | ADV | S, F | 1 |
| D4.6.6 | Agreement admitting minor to the benefits of Partnership | `agreement-admitting-minor-to-the-benefits-of-partnership` | V | TA | ADV | S, F | 1 |
| D4.6.7 | Deed of Retirement from Partnership | `deed-of-retirement-from-partnership` | V | TA | ADV | S, F | 1 |
| D4.6.8 | Deed of Retirement of one Partner and Admission of a new Partner | `deed-of-retirement-of-one-partner-and-admission-of-a-new-partner` | V | TA | ADV | S, F | 1 |
| D4.6.9 | Agreement for Dissolution of partnership | `agreement-for-dissolution-of-partnership` | V | TA | ADV | S, F | 1 |
| D4.6.10 | Agreement for Dissolution of partnership through an attorney | `agreement-for-dissolution-of-partnership-through-an-attorney` | V | TA | ADV | S, F | 1 |
| D4.6.11 | Deed of sub partnership | `deed-of-sub-partnership` | V | TA | ADV | S, F | 1 |
| D4.7.1 | Self declaration of Proprietorship | `self-declaration-of-proprietorship` | V | TA | ADV | N | 1 |
| D4.7.2 | Rent Agreement or Lease Agreement | `rent-agreement-or-lease-agreement` | C | TA | ADV | S, R? | 1 |
| D4.7.3 | No objection certificates | `no-objection-certificates` | V | TA | ADV | — | 1 |
| D4.8.1 | Codicil substituting a trustee in a trust | `codicil-substituting-a-trustee-in-a-trust` | X | TA | ADV | W2 | 2 |
| D4.8.2 | Donation to trust | `donation-to-trust` | X | TA | ADV | S, R* | 2 |
| D4.8.3 | Endowment to a deity | `endowment-to-a-deity` | X | TA | ADV | S, R* | 2 |
| D4.8.4 | Family trust deed | `family-trust-deed` | X | TA | ADV | S, R* | 2 |
| D4.8.5 | Private trust | `private-trust` | X | TA | ADV | S, R* | 2 |
| D4.8.6 | Public trust | `public-trust` | X | TA | ADV | S, R* | 2 |

#### D5. Planning & Execution — `/documents/planning-and-execution`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D5.1 | Start-up | `start-up` | U | 0 — to define (§3) | 3 | RW (stub) |
| D5.2 | Budgeting | `budgeting` | U | 0 — to define (§3) | 3 | RW (stub) |
| D5.3 | Partnership and Founders | `partnership-and-founders` | L | 5 | 1 | HC · OL: IT Act 1961→2025 |
| D5.4 | Investment Support and Business Funding | `investment-support-and-business-funding` | U | 3 | 3 | HC |
| D5.5 | Business Plan | `business-plan` | U | 0 — to define (§3) | 3 | RW (stub) |
| D5.6 | Business Process | `business-process` | U | 0 — to define (§3) | 3 | RW (stub) |
| D5.7 | Business Analysis | `business-analysis` | U | 0 — to define (§3) | 3 | RW (stub) |
| D5.8 | Strategy | `strategy` | U | 0 — to define (§3) | 3 | RW (stub) |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D5.3.1 | Agreement modifying partnership deed | `agreement-modifying-partnership-deed` | V | TA | ADV | S, F | 1 |
| D5.3.2 | Deed of retirement (≈ D4.6.7) | `deed-of-retirement` | V | TA | ADV | S, F | 1 |
| D5.3.3 | Dissolution of partnership (≈ D4.6.9) | `dissolution-of-partnership` | V | TA | ADV | S, F | 1 |
| D5.3.4 | Notice to partner | `notice-to-partner` | V | TA | ADV | — | 1 |
| D5.3.5 | Partnership deed (≈ D4.6.1) | `partnership-deed` | V | TA | ADV | S, F | 1 |
| D5.4.1 (U) | Business Plan | `business-plan` | V | AI | CA/CS | — | 3 |
| D5.4.2 (U) | Founders Agreement | `founders-agreement` | V | TA | CS | S | 3 |
| D5.4.3 (U) | Fund raising | `fund-raising` | V | AI | CS | — | 3 |

#### D6. Marketing & Sales — `/documents/marketing-and-sales`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D6.1 | Advertisements and Media | `advertisements-and-media` | L | 2 | 2 | HC · OL: IPC; CPA 1986 |
| D6.2 | Marketing | `marketing` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.3 | Email and Newsletters | `email-and-newsletters` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.4 | Sales | `sales` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.5 | Invoice | `invoice` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.6 | Business Letters | `business-letters` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.7 | Tracker Sheets | `tracker-sheets` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.8 | Feedback Forms | `feedback-forms` | U | 0 — to define (§3) | 3 | RW (stub) |
| D6.9 | Questionnaire | `questionnaire` | U | 0 — to define (§3) | 3 | RW (stub) |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D6.1.1 | Advertisement of petition | `advertisement-of-petition` | V | TA | ADV | — | 2 |
| D6.1.2 | Advertising agreement | `advertising-agreement` | V | TA | ADV | S | 2 |

#### D7. Industries (upcoming) — `/documents/industries`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D7.1 | Construction | `construction` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.2 | Education | `education` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.3 | Electricity and Power Sector | `electricity-and-power-sector` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.4 | Food Processing | `food-processing` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.5 | Healthcare and Pharma | `healthcare-and-pharma` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.6 | Hotel and Tourism | `hotel-and-tourism` | U | 5 | 3 | HC · OL: Labour Codes |
| D7.7 | Import-Export and Customs | `import-export-and-customs` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.8 | Media and Entertainment | `media-and-entertainment` | U | 0 — to define (§3) | 3 | RW (stub) |
| D7.9 | Oil and Gas | `oil-and-gas` | U | 0 — to define (§3) | 3 | RW (stub) |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D7.6.1 (U) | Accommodation Services Agreement with Company | `accommodation-services-agreement-with-company` | V | TA | ADV | S | 3 |
| D7.6.2 (U) | Hotel and Travel Agency Agreement | `hotel-and-travel-agency-agreement` | V | TA | ADV | S | 3 |
| D7.6.3 (U) | MOU with Consultant | `mou-with-consultant` | V | TA | ADV | S | 3 |
| D7.6.4 (U) | MOU for Revenue Sharing | `mou-for-revenue-sharing` | V | TA | ADV | S | 3 |
| D7.6.5 (U) | Hotel Management Agreement | `hotel-management-agreement` | V | TA | ADV | S | 3 |

#### D8. Intellectual Property Rights — `/documents/intellectual-property-rights`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D8.1 | Copyright | `copyright` | L | 5 | 1 | HC |
| D8.2 | Patents | `patents` | L | 3 | 2 | HC |
| D8.3 | Trademark | `trademark` | L | 3 | 1 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D8.1.1 | Agreement to write content or book and sell copyright | `agreement-to-write-content-or-book-and-sell-copyright` | V | TA | ADV | S | 1 |
| D8.1.2 | Assignment of copyright | `assignment-of-copyright` | V | TA | ADV | S | 1 |
| D8.1.3 | License to use copyright | `license-to-use-copyright` | V | TA | ADV | S | 1 |
| D8.1.4 | Notice for not using copyright material | `notice-for-not-using-copyright-material` | V | TA | ADV | — | 1 |
| D8.1.5 | Revocation of copyright | `revocation-of-copyright` | V | TA | ADV | S | 1 |
| D8.2.1 | Assignment of patent | `assignment-of-patent` | V | TA | ADV/PA | S, F | 2 |
| D8.2.2 | License to use patent | `license-to-use-patent` | V | TA | ADV/PA | S, F | 2 |
| D8.2.3 | Revocation of patent licence | `revocation-of-patent-license` † | V | TA | ADV/PA | — | 2 |
| D8.3.1 | Assignment of trademark | `assignment-of-trademark` | V | TA | ADV/TMA | S, F | 1 |
| D8.3.2 | Licence to use trademark | `license-to-use-trademark` | V | TA | ADV/TMA | S, F | 1 |
| D8.3.3 | Revocation of trademark licence | `revocation-of-trademark-license` † | V | TA | ADV/TMA | — | 1 |

#### D9. IT and Websites — `/documents/it-and-websites`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D9.1 | IT and Net related Contracts | `it-and-net-related-contracts` | L | 4 | 1 | HC |
| D9.2 | Software Contracts | `software-contracts` | L | 0 — to define (§3) | 2 | HC |
| D9.3 | Hardware Contracts | `hardware-contracts` | L | 0 — to define (§3) | 2 | RW (thin) |
| D9.4 | Maintenance Agreements | `maintenance-agreements` | L | 0 — to define (§3) | 2 | RW (thin) |
| D9.5 | Website Policies & Documents | `website-policies-and-documents` | L | 0 — to define (§3) | 2 | HC · OL: DPDP 2023 |
| D9.6 | Cyber Security & Data Protection | `cyber-security-and-data-protection` | U | 0 — to define (§3) | 3 | RW (stub) · OL: DPDP 2023 |
| D9.7 | Mobile App | `mobile-app` | U | 0 — to define (§3) | 3 | RW (stub) |
| D9.8 | Privacy & Cookie Policy | `privacy-and-cookie-policy` | L | 0 — to define (§3) | 3 | RW (stub) · OL: DPDP 2023 |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D9.1.1 | Hardware agreements | `hardware-agreements` | V | TA | ADV | S | 1 |
| D9.1.2 | Agreement for development of portal | `agreement-for-development-of-portal` | V | TA | ADV | S | 1 |
| D9.1.3 | Agreement for development of website | `agreement-for-development-of-website` | V | TA | ADV | S | 1 |
| D9.1.4 | Supply technical know how | `supply-technical-know-how` | V | TA | ADV | S | 1 |

#### D10. HR and Service — `/documents/hr-and-service`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D10.1 | Agents and Broker | `agents-and-broker` | L | 4 | 2 | HC |
| D10.2 | Apprenticeship | `apprenticeship` | L | 3 | 2 | HC |
| D10.3 | Consultants | `consultants` | U | 0 — to define (§3) | 3 | RW (stub) |
| D10.4 | Employer-Employee Communication | `employer-employee-communication` | L | 6 | 1 | HC · OL: IR Code [INTERP] |
| D10.5 | ESOP Schemes | `esop-schemes` | U | 0 — to define (§3) | 3 | RW (stub) · CP (borrowed one-liner) |
| D10.6 | HR Operations | `hr-operations` | U | 0 — to define (§3) | 3 | RW (stub) |
| D10.7 | HR Policies | `hr-policies` | U | 0 — to define (§3) | 3 | HC |
| D10.8 | Job Agreements | `job-agreements` | L | 4 | 1 | HC |
| D10.9 | Work from Home | `work-from-home` | L | 0 — to define (§3) | 3 | RW (stub) |
| D10.10 | Job Application and Offers | `job-application-and-offers` | L | 3 | 1 | RW (thin) |
| D10.11 | Labour Agreements | `labour-agreements` | L | 4 | 2 | HC · OL: Labour Codes |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D10.1.1 | Agreement between Company and Agent | `agreement-between-company-and-agent` | V | TA | ADV | S | 2 |
| D10.1.2 | Agreement between Manufacturer and Agent | `agreement-between-manufacturer-and-agent` | V | TA | ADV | S | 2 |
| D10.1.3 | Agreement with Service Provider and Agent | `agreement-with-service-provider-and-agent` | V | TA | ADV | S | 2 |
| D10.1.4 | Cancellation Agreement with Broker or Agent | `cancellation-agreement-with-broker-or-agent` | V | TA | ADV | S | 2 |
| D10.2.1 | Apprenticeship Agreement by Guardian | `apprenticeship-agreement-by-guardian` | V | TA | ADV | S, F | 2 |
| D10.2.2 | Apprenticeship Agreement for Training | `apprenticeship-agreement-for-training` | V | TA | ADV | S, F | 2 |
| D10.2.3 | Cancellation of Apprenticeship Agreement | `cancellation-of-apprenticeship-agreement` | V | TA | ADV | — | 2 |
| D10.4.1 | Chargesheet to Employee | `chargesheet-to-employee` | V | TA | ADV | — | 1 |
| D10.4.2 | Notice of Retrenchment | `notice-of-retrenchment` | V | TA | ADV | — | 1 |
| D10.4.3 | Notice to Employee | `notice-to-employee` | V | TA | ADV | — | 1 |
| D10.4.4 | Resignation Letter | `resignation-letter` | V | TA | ADV | — | 1 |
| D10.4.5 | Revocation of Contract with Employee | `revocation-of-contract-with-employee` | V | TA | ADV | — | 1 |
| D10.4.6 | Warning to Employee | `warning-to-employee` | V | TA | ADV | — | 1 |
| D10.8.1 | Contractual Employment Agreement | `contractual-employment-agreement` | V | TA | ADV | S | 1 |
| D10.8.2 | Employment Agreement | `employment-agreement` | V | TA | ADV | S | 1 |
| D10.8.3 | Job Agreement | `job-agreement` | V | TA | ADV | S | 1 |
| D10.8.4 | ESOP plan and grant letter | `esop-plan-and-grant-letter` † | V | TA | CS | F | 1 |
| D10.10.1 | Application for Job | `application-for-job` | V | TA | ADV | — | 1 |
| D10.10.2 | Appointment letter | `appointment-letter` | V | TA | ADV | — | 1 |
| D10.10.3 | Offer Letter | `offer-letter` | V | TA | ADV | — | 1 |
| D10.11.1 | Agreement between Master and Labour | `agreement-between-master-and-labour` | V | TA | ADV | S | 2 |
| D10.11.2 | Agreement for Providing Compensation for injury | `agreement-for-providing-compensation-for-injury` | V | TA | ADV | S | 2 |
| D10.11.3 | Agreement for Supply of Labour | `agreement-for-supply-of-labour` | V | TA | ADV | S | 2 |
| D10.11.4 | Memorandum of Settlement for Industrial Dispute | `memorandum-of-settlement-for-industrial-dispute` | C | TA | ADV | F | 2 |

#### D11. Legal — `/documents/legal`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D11.1 | Affidavits | `affidavits` | L | 0 — to define (§3) | 2 | HC · OL: Evidence Act→BSA |
| D11.2 | Arbitration | `arbitration` | L | 6 | 2 | HC · CP (borrowed one-liner) |
| D11.3 | Mediation | `mediation` | L | 0 — to define (§3) | 3 | RW (stub) · CP (borrowed one-liner) |
| D11.4 | Negotiation | `negotiation` | L | 0 — to define (§3) | 3 | RW (stub) |
| D11.5 | Consumer | `consumer` | L | 5 | 1 | HC · OL: CPA 1986→2019 |
| D11.6 | Motor Vehicles | `motor-vehicles` | L | 1 | 2 | HC |
| D11.7 | Notices | `notices` | L | 0 — to define (§3) | 2 | HC |
| D11.8 | RTI | `rti` | L | 2 | 1 | HC |
| D11.9 | Legal Notices | `legal-notices` | L | 8 | 1 | HC · OL: IPC; Evidence Act |
| D11.10 | Reply to Legal Notices | `reply-to-legal-notices` | L | 1 | 1 | RW (thin) |
| D11.11 | Service Agreement with Lawyer | `service-agreement-with-lawyer` | L | 2 | 2 | HC |
| D11.12 | Vakalatnama | `vakalatnama` | L | 14 | 1 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D11.2.1 | Arbitration Agreement among Members of HUF | `arbitration-agreement-among-members-of-huf` | V | TA | ADV | S | 2 |
| D11.2.2 | Arbitration Agreement for Reference to the Arbitrator | `arbitration-agreement-for-reference-to-the-arbitrator` | V | TA | ADV | S | 2 |
| D11.2.3 | Directions by the Arbitrator | `directions-by-the-arbitrator` | V | PRO | ADV | — | 3 |
| D11.2.4 | Notice by the Arbitrator | `notice-by-the-arbitrator` | V | PRO | ADV | — | 3 |
| D11.2.5 | Notice for revocation of Arbitration Agreement | `notice-for-revocation-of-arbitration-agreement` | V | TA | ADV | — | 2 |
| D11.2.6 | Notice to the Arbitrator | `notice-to-the-arbitrator` | V | TA | ADV | — | 2 |
| D11.5.1 | Advocate Notice for Consumer Complaint | `advocate-notice-for-consumer-complaint` | V | TA | ADV | — | 1 |
| D11.5.2 | Consumer Appeal | `consumer-appeal` | V | PLD | ADV | CF, N | P10 |
| D11.5.3 | Consumer complaint (CPA 2019) | `consumer-complaint` | V | PLD | ADV | CF, N | P10 |
| D11.5.4 | Notice for Initiating Consumer Proceedings | `notice-for-initiating-consumer-proceedings` | V | TA | ADV | — | 1 |
| D11.5.5 | Written reply to the consumer Complaint | `written-reply-to-the-consumer-complaint` | V | PLD | ADV | CF, N | P10 |
| D11.6.1 | Motor accident compensation claim (MACT) | `motor-accident-compensation-claim` † | V | PLD | ADV | CF, N | P10 |
| D11.8.1 | Appeal under RTI | `appeal-under-rti` | V | TA | ADV | CF | 1 |
| D11.8.2 | RTI Application | `rti-application` | V | TA | ADV | CF | 1 |
| D11.9.1 | Legal notice by counsel — arrears of rent and ejectment | `arrears-of-rent-and-ejectment-suit-by-counsel` | V | TA | ADV | — | 1 |
| D11.9.2 | Notice to bank | `bank-notice` | V | TA | ADV | — | 1 |
| D11.9.3 | Claiming damages for breach of contract | `claiming-damages-for-breach-of-contract` | V | TA | ADV | — | 1 |
| D11.9.6 | Notice of eviction (≈ D12.7.4) | `notice-of-eviction` | V | TA | ADV | — | 1 |
| D11.9.7 | Notice for making payment | `notice-for-making-payment` | V | TA | ADV | — | 1 |
| D11.9.8 | Repayment of loan | `repayment-of-loan` | V | TA | ADV | — | 1 |
| D11.10.1 | Reply to the legal notice | `reply-to-the-legal-notice` | V | TA | ADV | — | 1 |
| D11.11.1 | Between a company and advocate | `between-a-company-and-advocate` | V | TA | ADV | S | 2 |
| D11.11.2 | Between a company and firm of advocates | `between-a-company-and-firm-of-advocates` | V | TA | ADV | S | 2 |
| D11.12.1 | Vakalatnama in Hindi | `vakalatnama-in-hindi` | V | TA | ADV | CF | 1 |
| D11.12.2 | Vakalatnama in English | `vakalatnama-in-english` | V | TA | ADV | CF | 1 |
| D11.12.3 | Blank vakalatnama (PDF) — Hindi | `blank-vakalatnama-in-pdf-format-hindi` | V | TA | ADV | CF | 1 |
| D11.12.4 | Blank vakalatnama (PDF) — English | `blank-vakalatnama-in-pdf-format-english` | V | TA | ADV | CF | 1 |
| D11.12.5 | Blank vakalatnama (PDF) — Malayalam | `blank-vakalatnama-in-pdf-format-malayalam` | V | TA | ADV | CF | 1 |
| D11.12.6 | Blank vakalatnama (PDF) — Telugu | `blank-vakalatnama-in-pdf-format-telugu` | V | TA | ADV | CF | 1 |
| D11.12.7 | Blank vakalatnama (PDF) — Tamil | `blank-vakalatnama-in-pdf-format-tamil` | V | TA | ADV | CF | 1 |
| D11.12.8 | Blank vakalatnama (PDF) — Gujarati | `blank-vakalatnama-in-pdf-format-gujarati` | V | TA | ADV | CF | 1 |
| D11.12.9 | Blank vakalatnama (PDF) — Kannada | `blank-vakalatnama-in-pdf-format-kannada` | V | TA | ADV | CF | 1 |
| D11.12.10 | Blank vakalatnama (PDF) — Marathi | `blank-vakalatnama-in-pdf-format-marathi` | V | TA | ADV | CF | 1 |
| D11.12.11 | Blank vakalatnama (PDF) — Punjabi | `blank-vakalatnama-in-pdf-format-punjabi` | V | TA | ADV | CF | 1 |
| D11.12.12 | Blank vakalatnama (PDF) — Bengali | `blank-vakalatnama-in-pdf-format-bengali` | V | TA | ADV | CF | 1 |
| D11.12.13 | Blank vakalatnama (PDF) — Oriya | `blank-vakalatnama-in-pdf-format-oriya` | V | TA | ADV | CF | 1 |
| D11.12.14 | Blank vakalatnama (PDF) — Assamese | `blank-vakalatnama-in-pdf-format-assamese` | V | TA | ADV | CF | 1 |

Aliases (no own page; 301 to canonical): D11.9.4 Legal notice — consumer protection → D11.5.4 (new); D11.9.5 Dishonour of cheque — legal notice → D3.5.1 (new).

#### D12. Property Transactions — `/documents/property-transactions`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D12.1 | Building Contracts | `building-contracts` | L | 9 | 2 | HC |
| D12.2 | Exchange Deeds and Settlement | `exchange-deeds-and-settlement` | L | 2 | 2 | HC |
| D12.3 | Lease | `lease` | L | 7 | 1 | HC |
| D12.4 | Mortgage | `mortgage` | U | 2 | 3 | HC · OL: CA 1956 |
| D12.5 | Notices regarding Property Transactions | `notices-regarding-property-transactions` | L | 5 | 1 | HC |
| D12.6 | Release and NOCs | `release-and-nocs` | L | 4 | 2 | HC |
| D12.7 | Rent | `rent` | L | 7 | 1 | HC |
| D12.8 | Sale and Purchase | `sale-and-purchase` | L | 7 | 1 | HC · OL: eSign claim |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D12.1.1 | Agreement between Developer and existing Tenant | `agreement-between-developer-and-existing-tenant` | C | TA | ADV | S, R? | 2 |
| D12.1.2 | Conveyance Agreement | `conveyance-agreement` | R | TA | ADV | S, R | 2 |
| D12.1.3 | Agreement for Building Construction | `agreement-for-building-construction` | C | TA | ADV | S | 2 |
| D12.1.4 | Application to the Municipality | `application-to-the-municipality` | C | TA | ADV | F | 2 |
| D12.1.5 | Developer Agreement to Sell Flat | `developer-agreement-to-sell-flat` | C | TA | ADV | S, R? | 2 |
| D12.1.6 | Agreement between owner and Architect | `agreement-between-owner-and-architect` | C | TA | ADV | S | 2 |
| D12.1.7 | Agreement between owner and Builder | `agreement-between-owner-and-builder` | C | TA | ADV | S | 2 |
| D12.1.8 | Agreement between owner and Contractor | `agreement-between-owner-and-contractor` | C | TA | ADV | S | 2 |
| D12.1.9 | Agreement between owner and Labour Contractor | `agreement-between-owner-and-labour-contractor` | C | TA | ADV | S | 2 |
| D12.2.1 | Compromise Agreement for Partition | `compromise-agreement-for-partition` | C | TA | ADV | S, R* | 2 |
| D12.2.2 | Exchange Deeds | `exchange-deeds` | C | TA | ADV | S, R | 2 |
| D12.3.1 | Lease Deed for Land | `lease-deed-for-land` | C | TA | ADV | S, R? | 1 |
| D12.3.2 | Lease Deed of a building of Office | `lease-deed-of-a-building-of-office` | C | TA | ADV | S, R? | 1 |
| D12.3.3 | Lease Deed of Commercial Property | `lease-deed-of-commercial-property` | C | TA | ADV | S, R? | 1 |
| D12.3.4 | Lease Deed of Residential Property | `lease-deed-of-residential-property` | C | TA | ADV | S, R? | 1 |
| D12.3.5 | Modification of Lease Deed | `modification-of-lease-deed` | C | TA | ADV | S, R? | 1 |
| D12.3.6 | Renewal of Lease Deed | `renewal-of-lease-deed` | C | TA | ADV | S, R? | 1 |
| D12.3.7 | Surrender of Lease | `surrender-of-lease` | C | TA | ADV | S, R* | 1 |
| D12.4.1 (U) | Mortgage Deed | `mortgage-deed` | R | TA | ADV | S, R, W2 | 3 |
| D12.4.2 (U) | Revocation of Mortgage Deed | `revocation-of-mortgage-deed` | R | TA | ADV | S, R | 3 |
| D12.5.1 | Notice claiming damages for breach of Contract | `notice-claiming-damages-for-breach-of-contract` | C | TA | ADV | — | 1 |
| D12.5.2 | Notice terminating Agency | `notice-terminating-agency` | C | TA | ADV | — | 1 |
| D12.5.3 | Notice to the Agent | `notice-to-the-agent` | C | TA | ADV | — | 1 |
| D12.5.4 | Notice to the Trespasser to hand over Possession | `notice-to-the-trespasser-to-hand-over-possession` | C | TA | ADV | — | 1 |
| D12.5.5 | Reply to the Notice | `reply-to-the-notice` | C | TA | ADV | — | 1 |
| D12.6.1 | Release Deed for Mortgage Property | `release-deed-for-mortgage-property` | R | TA | ADV | S, R | 2 |
| D12.6.2 | Release of an Interest in Immovable Property | `release-of-an-interest-in-immovable-property` | C | TA | ADV | S, R* | 2 |
| D12.6.3 | Release of Property under Maintenance | `release-of-property-under-maintenance` | C | TA | ADV | S, R* | 2 |
| D12.6.4 | Release of Right of Way | `release-of-right-of-way` | C | TA | ADV | S, R* | 2 |
| D12.7.1 | Agreement for Paying Guest | `agreement-for-paying-guest` | C | TA | ADV | S | 1 |
| D12.7.2 | Compromise between Landlord and Tenant | `compromise-between-landlord-and-tenant` | C | TA | ADV | S | 1 |
| D12.7.3 | Notice by Tenant | `notice-by-tenant` | C | TA | ADV | — | 1 |
| D12.7.4 | Notice to the Tenant | `notice-to-the-tenant` | C | TA | ADV | — | 1 |
| D12.7.5 | Rent Agreement Commercial | `rent-agreement-commercial` | C | TA | ADV | S, R? | 1 |
| D12.7.6 | Rent Agreement Flat | `rent-agreement-flat` | C | TA | ADV | S, R? | 1 |
| D12.7.7 | Rent Agreement Residential | `rent-agreement-residential` | C | TA | ADV | S, R? | 1 |
| D12.8.1 | Agreement for Sale of Commercial Property | `agreement-for-sale-of-commercial-property` | R | TA | ADV | S, R? | 1 |
| D12.8.2 | Agreement for Sale of Flat | `agreement-for-sale-of-flat` | R | TA | ADV | S, R? | 1 |
| D12.8.3 | Agreement for Sale of Freehold Property | `agreement-for-sale-of-freehold-property` | R | TA | ADV | S, R? | 1 |
| D12.8.4 | Agreement for Sale of Land | `agreement-for-sale-of-land` | R | TA | ADV | S, R? | 1 |
| D12.8.5 | Agreement for Sale of Residential House | `agreement-for-sale-of-residential-house` | R | TA | ADV | S, R? | 1 |
| D12.8.6 | Deed of Cancellation of Sale Deed | `deed-of-cancellation-of-sale-deed` | R | TA | ADV | S, R | 1 |
| D12.8.7 | Deed of Conveyance | `deed-of-conveyance` | R | TA | ADV | S, R | 1 |

#### D13. RERA — `/documents/rera`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D13.1 | For Builders and Developers | `for-builders-and-developers` | L | 0 — to define (§3) | 2 | HC |
| D13.2 | For Consumers | `for-consumers` | L | 1 | 2 | HC |
| D13.3 | For Agents | `for-agents` | L | 0 — to define (§3) | 2 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D13.2.1 | RERA Complaint | `rera-complaint` | V | PLD | ADV | CF, N | P10 |

#### D14. SEBI (upcoming) — `/documents/sebi`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D14.1 | Insider Trading | `insider-trading` | U | 0 — to define (§3) | 3 | RW (stub) |
| D14.2 | Listing Regulation | `listing-regulation` | U | 0 — to define (§3) | 3 | RW (stub) |
| D14.3 | Takeover | `takeover` | U | 0 — to define (§3) | 3 | RW (stub) |

#### D15. Secretarial (upcoming) — `/documents/secretarial`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D15.1 | Secretarial Compliances | `secretarial-compliances` | U | 0 — to define (§3) | 3 | HC · OL: Listing Agmt→LODR |
| D15.2 | Board Meeting | `board-meeting` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.3 | Company Meetings | `company-meetings` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.4 | Directors or KMP | `directors-or-kmp` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.5 | General Meeting | `general-meeting` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.6 | Misc. Drafts | `misc-drafts` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.7 | NBFCs | `nbfcs` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.8 | Policies and Codes | `policies-and-codes` | U | 0 — to define (§3) | 3 | RW (stub) |
| D15.9 | Resolutions | `resolutions` | U | 0 — to define (§3) | 3 | RW (stub) |

#### D16. Students — `/documents/students`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D16.1 | Affidavits for Students | `affidavits-for-students` | L | 7 | 1 | HC · OL: Evidence Act→BSA |
| D16.2 | Application | `application` | L | 4 | 1 | RW (thin) |
| D16.3 | CV | `cv` | L | 6 | 2 | HC |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D16.1.1 | Affidavit for students — admission | `admission` | V | TA | ADV | S, N | 1 |
| D16.1.2 | Affidavit for students — anti ragging | `anti-ragging` | V | TA | ADV | S, N | 1 |
| D16.1.3 | Affidavit for students — fee waiver | `fee-waiver` | V | TA | ADV | S, N | 1 |
| D16.1.4 | Affidavit for students — for issuing duplicate certificate | `for-issuing-duplicate-certificate` | V | TA | ADV | S, N | 1 |
| D16.1.5 | Affidavit for students — loss of marksheet or certificate | `loss-of-marksheet-or-certificate` | V | TA | ADV | S, N | 1 |
| D16.1.6 | Affidavit for students — provisional admission | `provisional-admission` | V | TA | ADV | S, N | 1 |
| D16.1.7 | Affidavit for students — study gap | `study-gap` | V | TA | ADV | S, N | 1 |
| D16.2.2 | Application for Leave | `application-for-leave` | V | TA | ED | — | 1 |
| D16.2.3 | For providing Marksheet or Degree | `for-providing-marksheet-or-degree` | V | TA | ED | — | 1 |
| D16.2.4 | Internship Application | `internship-application` | V | TA | ED | — | 1 |
| D16.3.1 | CV — Accountancy/ CA/CS | `accountancy-ca-cs` | V | TA | ED | — | 2 |
| D16.3.2 | CV — Common CV | `common-cv` | V | TA | ED | — | 2 |
| D16.3.3 | CV — Engineering | `engineering` | V | TA | ED | — | 2 |
| D16.3.4 | CV — Law | `law` | V | TA | ED | — | 2 |
| D16.3.5 | CV — Management | `management` | V | TA | ED | — | 2 |
| D16.3.6 | CV — Medical | `medical` | V | TA | ED | — | 2 |

Aliases (no own page; 301 to canonical): D16.2.1 Application for Job → `job-application-and-offers`.

#### D17. Succession and Inheritance — `/documents/succession-and-inheritance`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D17.1 | Adoption | `adoption` | L | 4 | 2 | HC · OL: JJ Act 2021/CARA |
| D17.2 | Family Agreement and Settlement | `family-agreement-and-settlement` | L | 5 | 2 | HC |
| D17.3 | Gift Deed | `gift-deed` | L | 8 | 1 | HC · OL: eSign claim |
| D17.4 | Partition | `partition` | L | 7 | 2 | HC · OL: IT Act 1961→2025 |
| D17.5 | Power of Attorney | `power-of-attorney` | L | 6 | 1 | HC · OL: Evidence Act; eSign claim |
| D17.6 | Will | `will` | L | 5 | 1 | HC · OL: eSign claim |

| ID | Document | Slug | eSign | Type | Reviewer | Formalities | Wave |
|---|---|---|---|---|---|---|---|
| D17.1.1 | Adoption by Hindu male | `adoption-by-hindu-male` | V | TA | ADV | S, R? | 2 |
| D17.1.2 | Adoption by Woman | `adoption-by-woman` | V | TA | ADV | S, R? | 2 |
| D17.1.3 | Adoption Deed | `adoption-deed` | V | TA | ADV | S, R? | 2 |
| D17.1.4 | Consent for Adoption | `consent-for-adoption` | V | TA | ADV | N | 2 |
| D17.2.1 | Deed of Family Arrangement | `deed-of-family-arrangement` | C | TA | ADV | S, R* | 2 |
| D17.2.2 | Deed of Settlement | `deed-of-settlement` | C | TA | ADV | S, R* | 2 |
| D17.2.3 | Division of the Property of the Deceased | `division-of-the-property-of-the-deceased` | V | TA | ADV | S, R* | 2 |
| D17.2.4 | Division of Property | `division-of-property` | V | TA | ADV | S, R* | 2 |
| D17.2.5 | Memorandum recording Family Settlement | `memorandum-recording-family-settlement` | C | TA | ADV | S, R? | 2 |
| D17.3.1 | Creating Life Estate for Maintenance | `creating-life-estate-for-maintenance` | R | TA | ADV | S, R, W2 | 1 |
| D17.3.2 | Gift Deed of Business | `gift-deed-of-business` | C | TA | ADV | S, R*, W2* | 1 |
| D17.3.3 | Gift for Charity | `gift-for-charity` | C | TA | ADV | S, R*, W2* | 1 |
| D17.3.4 | Gift in Consideration of Marriage | `gift-in-consideration-of-marriage` | C | TA | ADV | S, R*, W2* | 1 |
| D17.3.5 | Gift of Immovable Property | `gift-of-immovable-property` | R | TA | ADV | S, R, W2 | 1 |
| D17.3.6 | Gift to Grand Children | `gift-to-grand-children` | C | TA | ADV | S, R*, W2* | 1 |
| D17.3.7 | Revocation of Gift Deed | `revocation-of-gift-deed` | C | TA | ADV | S, R*, W2* | 1 |
| D17.3.8 | Simple Gift Deed | `simple-gift-deed` | C | TA | ADV | S, R*, W2* | 1 |
| D17.4.1 | Deed evidencing Partition | `deed-evidencing-partition` | C | TA | ADV | S, R* | 2 |
| D17.4.2 | Partial Partition in Joint Family Business | `partial-partition-in-joint-family-business` | C | TA | ADV | S, R* | 2 |
| D17.4.3 | Partition deed between co-owners | `partition-deed-between-co-owners` † | C | TA | ADV | S, R* | 2 |
| D17.4.4 | Partition of Family Business | `partition-of-family-business` | C | TA | ADV | S, R* | 2 |
| D17.4.5 | Partition of Land | `partition-of-land` | C | TA | ADV | S, R* | 2 |
| D17.4.6 | Partition of Property among Members of HUF | `partition-of-property-among-members-of-huf` | C | TA | ADV | S, R* | 2 |
| D17.4.7 | Simple Partition Deed | `simple-partition-deed` | C | TA | ADV | S, R* | 2 |
| D17.5.1 | Detailed General Power of Attorney | `detailed-general-power-of-attorney` | X | TA | ADV | S, N, R? | 1 |
| D17.5.2 | General Power of Attorney | `general-power-of-attorney` | X | TA | ADV | S, N, R? | 1 |
| D17.5.3 | Power of Attorney for executing Sale Deed | `power-of-attorney-for-executing-sale-deed` | X | TA | ADV | S, N, R? | 1 |
| D17.5.4 | Power of Attorney for representing before Registrar | `power-of-attorney-for-representing-before-registrar` | X | TA | ADV | S, N, R? | 1 |
| D17.5.5 | Power of Attorney of Court Case | `power-of-attorney-of-court-case` | X | TA | ADV | S, N, R? | 1 |
| D17.5.6 | Revocation of Power of Attorney | `revocation-of-power-of-attorney` | X | TA | ADV | S, N | 1 |
| D17.6.1 | Revocation of Will | `revocation-of-will` | X | TA | ADV | W2 | 1 |
| D17.6.2 | Simple Will | `simple-will` | X | TA | ADV | W2, R? | 1 |
| D17.6.3 | Will by Husband | `will-by-husband` | X | TA | ADV | W2, R? | 1 |
| D17.6.4 | Will creating Life Estate | `will-creating-life-estate` | X | TA | ADV | W2, R? | 1 |
| D17.6.5 | Will regarding a Partnership Business | `will-regarding-a-partnership-business` | X | TA | ADV | W2, R? | 1 |

#### D18. Accounting & Tax (upcoming) — `/documents/accounting-and-tax`

| Sub-cat | Name | Slug | L/U | Docs | Wave | Content status |
|---|---|---|---|---|---|---|
| D18.1 | GST | `gst` | U | 0 — to define (§3) | 3 | RW (stub) · OL: GST 2.0 |
| D18.2 | Income Tax | `income-tax` | U | 0 — to define (§3) | 3 | RW (stub) · OL: IT Act 1961→2025 |
| D18.3 | Finance | `finance` | U | 0 — to define (§3) | 3 | RW (stub) |
| D18.4 | Accounting | `accounting` | U | 0 — to define (§3) | 3 | RW (stub) |

---

## 3. Sub-categories with no document list — proposed starter documents [OWNER to approve]

63 sub-categories have copy but no template list, and 48 are stubs (R5 §0). Do not publish an empty hub. Seed the following candidates as `DRAFT` templates (not in the manuals; written fresh, reviewed, neutral). Remaining "to define" hubs stay `noindex`.

| Sub-cat | Proposed starter documents (type · reviewer · formalities) | Wave |
|---|---|---|
| D1.5 Mergers and Acquisitions | Term sheet; share purchase agreement; business transfer agreement (slump sale); due-diligence request list; disclosure letter (TA · ADV/CS · S) | 2 |
| D1.6 Formal Proposals / D1.10 Sign off | Proposal letter; letter of intent (non-binding); project sign-off / acceptance certificate (TA · ED/ADV · —) | 2 |
| D2.6 Mutual Divorce | Cross-link to PL-FAM-05; settlement terms for mutual consent (TA · ADV · S) | P10 |
| D2.7 Senior Citizens Protection | Application to Maintenance Tribunal (Maintenance and Welfare of Parents and Senior Citizens Act 2007 s.5) (PLD · ADV · —); gift with maintenance condition (s.23 — cross-link D17.3) | 2 |
| D4.4 MSME | Udyam-ready declaration pack; MSME supplier payment reminder (MSMED Act 2006 s.15–16 interest) (TA · CA/ADV · —) | 2 |
| D5.1 Start-up / D5.5 Business Plan | Founders' agreement (cross-link D5.4.2); advisor agreement; business plan outline (AI · CA/CS) | 3 |
| D6.2–D6.9 Marketing & Sales set | Influencer agreement (with ASCI disclosure clause [VERIFY guideline]); newsletter consent text; sales agency agreement; GST invoice format (cross-link P14); business letter set; feedback form with DPDP notice (TA · ADV/ED) | 3 |
| D7.x Industries | Construction: sub-contract; Food: co-packing/manufacturing agreement; Healthcare: clinical-establishment consultant agreement; Import-export: sale contract with Incoterms reference (TA · ADV) | 3 |
| D9.2 Software Contracts | SaaS subscription agreement; software licence (EULA); source-code escrow (TA · ADV · S) | 2 |
| D9.3 Hardware / D9.4 Maintenance | Annual maintenance contract (AMC); hardware supply and warranty (TA · ADV · S) | 2 |
| D9.5 Website Policies & Documents / D9.8 Privacy & Cookie | **DPDP Act 2023 / Rules 2025 privacy notice**; consent notice per purpose; cookie notice; terms of use; grievance officer page (IT Rules 2021 r.3(2)); refund and cancellation policy (Consumer Protection (E-Commerce) Rules 2020) (TA · ADV · —) | 1 |
| D9.6 Cyber Security & Data Protection | Data processing agreement (processor terms under DPDP s.8(2)); breach notification letter template; information-security policy for SMEs (TA · ADV) | 2 |
| D9.7 Mobile App | App development agreement; app privacy notice (cross-link D9.5) (TA · ADV · S) | 3 |
| D10.3 Consultants | Independent consultant agreement (cross-link D1.2.4) | 2 |
| D10.5 ESOP Schemes | Cross-link D10.8.4 and service C6.4 | 2 |
| D10.6 HR Operations / D10.7 HR Policies | POSH policy and internal committee constitution order (POSH Act 2013 s.4); leave policy; code of conduct; full-and-final settlement letter; experience letter (TA · ADV · —) — align with LDC HRMS kernel where tenant uses LDC (NN-47) | 2 |
| D10.9 Work from Home | Work-from-home policy and addendum to employment terms (TA · ADV · —) | 1 |
| D11.1 Affidavits | General affidavit; name-change affidavit; address affidavit; income affidavit; affidavit of identity (TA · ADV · S, N) | 1 |
| D11.3 Mediation / D11.4 Negotiation | Mediation agreement and settlement agreement under the Mediation Act 2023 [VERIFY commencement of relevant sections]; neutral ODR-provider cross-link (`ODR_PORT`; Equator one option, disclosed, never default); negotiation term sheet (TA · ADV · S) | 2 |
| D11.7 Notices | Hub merges into D11.9 Legal Notices (no separate list) | — |
| D13.1 RERA — builders | RERA-compliant agreement for sale (State model form [VERIFY per State]); allotment letter (TA · ADV · S, R?) | 2 |
| D13.3 RERA — agents | Agent registration declaration; agent–promoter agreement (TA · ADV · S) | 3 |
| D14.x SEBI | Insider-trading code of conduct (SEBI PIT Regulations 2015); LODR policy packs — RPT (Reg 23), materiality (Reg 30), website disclosures (Reg 46) (TA · CS · —) — replaces retired listing agreements | 3 |
| D15.x Secretarial | Board meeting notice and agenda; minutes (SS-1); general meeting notice (SS-2); director appointment consent (DIR-2) and resignation; resolutions library; NBFC policy pack links to LDC (D-10) (TA · CS · F*) | 2 |
| D18.x Accounting & Tax | Cross-link P14 services; GST invoice and credit note formats; rent receipt for HRA (TA · CA · —) | 3 |

---

## 4. Pleadings (13 areas → 89 manual drafts → 64 canonical pages + 6 imported from Documents + commissioned gaps)

### 4.1 Consolidated pleadings list

R5 estimated about 68 canonical pages. This list applies four further merges (divorce petitions P2.5 + P2.12; four cheque-bounce complaints into one; the trespass pair P8.1 + P8.3; the three corporate-law consumer complaints into the canonical CPA 2019 complaint) and moves the arbitral award out of pleadings, giving **64 canonical pages** from the manual. Slugs are shortened and corrected (all †; R5-proposed URLs 301 to them). **Limitation** shows the advisory seed reference from P10 FR-P10-15 — every row [VERIFY] before activation. **Type** is PLD for all rows; **PLD\*** = advocate review mandatory for every user (criminal area, P10 FR-P10-25). **Reviewer** is ADV for all rows. **Content:** OL = outdated law (fix in brackets), TY = heading typo, HC/RW as §1.

**P1 Civil Pleadings** — `/pleadings/civil-pleadings`

| ID | Canonical page (current law) | Slug | Merges | Forum profile | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-CIV-01 | Affidavit in civil proceedings (CPC O.XIX) | `affidavit-civil-proceedings` | P1.1 | DIST_CIVIL | — | 1 | RW |
| PL-CIV-02 | Suit for permanent injunction (Specific Relief Act 1963 ss.37–38; CPC O.VII r.1) | `suit-for-permanent-injunction` | P1.2 | DIST_CIVIL / DIST_COMMERCIAL | Art. 113 | 1 | HC |
| PL-CIV-03 | Application for temporary injunction (CPC O.XXXIX rr.1–2) | `temporary-injunction-application` | P1.3 | DIST_CIVIL | — | 1 | HC |
| PL-CIV-04 | Application for disobedience of injunction (CPC O.XXXIX r.2A) | `order-39-rule-2a-application` | P1.4 | DIST_CIVIL | — | 2 | HC |
| PL-CIV-05 | Application to sue as an indigent person (CPC O.XXXIII) | `suit-as-indigent-person` | P1.5 | DIST_CIVIL | per suit | 2 | RW |
| PL-CIV-06 | Suit for ejectment and damages (TPA s.106; State rent law) | `suit-for-ejectment-and-damages` | P1.6 | DIST_CIVIL | Art. 67 (reviewer) | 2 | HC |
| PL-CIV-07 | Suit for specific performance (SRA s.10 as amended 2018) | `suit-for-specific-performance` | P1.7, P1.17 | DIST_CIVIL / DIST_COMMERCIAL | Art. 54 | 1 | OL (SRA 2018) |
| PL-CIV-08 | Written statement (CPC O.VIII; commercial: O.VIII r.1 proviso — 120-day outer limit) | `written-statement` | P1.8, P1.13 | DIST_CIVIL / DIST_COMMERCIAL | 30/90/120 days (CPC) | 1 | OL (CCA timelines) |
| PL-CIV-09 | Caveat (CPC s.148A; valid 90 days) | `caveat-section-148a-cpc` | P1.9 | DIST_CIVIL / HC_GENERIC | — | 1 | RW |
| PL-CIV-10 | Transfer petition (CPC s.25 Supreme Court / s.24 High Court–District) | `transfer-petition-cpc` | P1.10 | SC_2020_PRINT / HC_GENERIC | — | 2 | HC |
| PL-CIV-11 | Plaint for compensation for defamation | `plaint-compensation-for-defamation` | P1.11 | DIST_CIVIL | Arts. 75/76 | 2 | TY; OL (IPC 499/500 → BNS s.356 if cited) |
| PL-CIV-12 | Plaint by a minor or person of unsound mind (CPC O.XXXII) | `plaint-by-minor-or-person-of-unsound-mind` | P1.12 | DIST_CIVIL | Limitation Act s.6 (disability) | 2 | RW |
| PL-CIV-13 | Application to set aside an ex parte decree (CPC O.IX r.13) | `set-aside-ex-parte-decree` | P1.14 | DIST_CIVIL | Art. 123 | 1 | HC |
| PL-CIV-14 | First appeal against a decree (CPC s.96, O.XLI) | `first-appeal-against-decree` | P1.15, P1.16 | DIST_CIVIL / HC_GENERIC | Art. 116 | 2 | HC |

**P2 Family Law Pleadings** — `/pleadings/family-law-pleadings`

| ID | Canonical page (current law) | Slug | Merges | Forum profile | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-FAM-01 | Petition for restitution of conjugal rights (HMA 1955 s.9; toggles SMA 1954 s.22, Muslim law suit) | `restitution-of-conjugal-rights` | P2.1, P2.3, P2.17 (+ D2.2.6) | FAMILY_COURT | — | 2 | HC; TY (Title Case) |
| PL-FAM-02 | Suit for divorce by Muslim wife (talaq-e-tafweez; Dissolution of Muslim Marriages Act 1939 [VERIFY grounds]) | `divorce-by-muslim-wife-talaq-e-tafweez` | P2.2 | FAMILY_COURT | — | 2 | HC |
| PL-FAM-03 | Petition for judicial separation (HMA s.10; ground toggles) | `judicial-separation-petition` | P2.4, P2.9, P2.15 (+ D2.2.4) | FAMILY_COURT | — | 2 | TY ("Adultry") |
| PL-FAM-04 | Petition for divorce (HMA s.13; petitioner toggle incl. wife's grounds s.13(2)) | `divorce-petition` | P2.5, P2.12 (+ D2.2.3) | FAMILY_COURT | — | 1 | HC |
| PL-FAM-05 | Divorce by mutual consent (HMA s.13B) + application to waive the s.13B(2) period (*Amardeep Singh v Harveen Kaur*, 2017) | `mutual-consent-divorce` | P2.6, P2.7, P2.16 (+ D2.6) | FAMILY_COURT | — | 1 | OL (cooling-off waiver) |
| PL-FAM-06 | Affidavit in matrimonial proceedings (incl. assets-and-liabilities disclosure format per *Rajnesh v Neha*, 2020 [VERIFY]) | `matrimonial-affidavit` | P2.8 | FAMILY_COURT | — | 1 | RW |
| PL-FAM-07 | Petition for nullity of a void marriage (HMA s.11) | `nullity-void-marriage` | P2.13, P2.18 (+ D2.2.5) | FAMILY_COURT | — | 2 | HC |
| PL-FAM-08 | Petition for annulment of a voidable marriage (HMA s.12; toggle: Prohibition of Child Marriage Act 2006 s.3 [VERIFY]) | `annulment-voidable-marriage` | P2.10, P2.19 | FAMILY_COURT | HMA s.12(2) limits | 2 | Rename ("Girl" → "minor at marriage") |
| PL-FAM-09 | Suit for contribution by a member of a joint Hindu family | `suit-for-contribution-joint-hindu-family` | P2.11 | DIST_CIVIL | Art. 113 (reviewer) | 3 | HC |
| PL-FAM-10 | Maintenance pendente lite and permanent alimony (HMA ss.24–25; either spouse) | `alimony-pendente-lite` | P2.14 (+ D2.4.4) | FAMILY_COURT | — | 1 | HC |
| PL-FAM-11 | Petition for removal of guardian (Guardians and Wards Act 1890 s.39) | `removal-of-guardian` | P2.20 | DIST_CIVIL / FAMILY_COURT | — | 3 | HC |
| PL-FAM-12 | Permission to sell a minor's property (HMGA 1956 s.8; GWA s.29) | `permission-to-sell-minors-property` | P2.21 | DIST_CIVIL | — | 2 | HC |
| PL-FAM-13 | Application for child custody (GWA s.25; HMA s.26) | `child-custody-application` | P2.22 (+ D2.1.1) | FAMILY_COURT | — | 1 | TY (trailing hyphen) |
| PL-FAM-14 | Application for maintenance under BNSS s.144 (formerly CrPC s.125) | `maintenance-section-144-bnss` | P2.23 (+ D2.4.3, D2.4.1 variant) | FAMILY_COURT / MAGISTRATE | — | 1 | OL (CrPC 125 → BNSS 144) |
| PL-FAM-15 | Application under the Protection of Women from Domestic Violence Act 2005 s.12 (+ Form I DIR) | `domestic-violence-act-application` | P6.3 re-filed (+ D2.3.1–3) | MAGISTRATE | — | 1 | TY ("Under of"); OL (IPC 498A → BNS 85/86 cross-refs) |

**P3 Succession and Inheritance** — `/pleadings/succession-and-inheritance`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-SUC-01 | Petition for probate (Indian Succession Act 1925 s.276) | `probate-petition` | P3.1 | DIST_CIVIL / HC_GENERIC | Art. 137 | 1 | HC |
| PL-SUC-02 | Petition for letters of administration (ISA s.278) | `letters-of-administration` | P3.2 | DIST_CIVIL / HC_GENERIC | Art. 137 | 2 | HC (differentiate from probate) |
| PL-SUC-03 | Petition for succession certificate (ISA s.372) | `succession-certificate` | P3.3 | DIST_CIVIL | Art. 137 | 1 | HC |

**P4 Criminal Law Pleadings** — `/pleadings/criminal-law-pleadings` (all PLD\*)

| ID | Canonical page (BNSS 2023) | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-CRM-01 | Regular bail application — BNSS s.480 (Magistrate) / s.483 (Sessions/High Court) (formerly CrPC ss.437/439) | `regular-bail-application` | P4.1, P4.4, P4.5 | MAGISTRATE / HC_GENERIC | — | 1 | OL |
| PL-CRM-02 | Anticipatory bail — BNSS s.482 (formerly CrPC s.438) | `anticipatory-bail-section-482-bnss` | P4.2, P4.6 | HC_GENERIC / Sessions | — | 1 | OL |
| PL-CRM-03 | Default bail — BNSS s.187 (formerly CrPC s.167(2)) | `default-bail-section-187-bnss` | P4.7 | MAGISTRATE | — | 2 | OL |
| PL-CRM-04 | Exemption from personal appearance — BNSS ss.228/355 (formerly CrPC ss.205/317) | `exemption-from-personal-appearance` | P4.3 | MAGISTRATE | — | 2 | OL; TY ("apperance") |
| PL-CRM-05 | Compounding of offence — BNSS s.359 (formerly CrPC s.320; BNS offence table) | `compounding-section-359-bnss` | P4.8 | MAGISTRATE | — | 2 | OL |
| PL-CRM-06 | Affidavit of surety for bail bond | `surety-affidavit-bail-bond` | P4.9 | MAGISTRATE | — | 1 | RW |
| PL-CRM-07 | Recall/re-examination of witness — BNSS s.348 (formerly CrPC s.311) | `recall-witness-section-348-bnss` | P4.10 | MAGISTRATE / Sessions | — | 3 | OL; TY |
| PL-CRM-08 | Application on non-appearance of complainant — BNSS s.279 (formerly CrPC s.256) [VERIFY subject of manual draft] | `non-appearance-of-complainant` | P4.11 | MAGISTRATE | — | 3 | OL |
| PL-CRM-09 | Complaint before Magistrate — BNSS s.223 (pre-cognizance hearing of accused; BNS offences) | `criminal-complaint-section-223-bnss` | P4.12 | MAGISTRATE | — | 2 | OL |

**P5 Rent & Property** — `/pleadings/rent-and-property`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-PRP-01 | Suit for eviction of licensee | `eviction-of-licensee` | P5.1 | DIST_CIVIL | Reviewer | 2 | HC |
| PL-PRP-02 | Suit for contribution against joint owner for repairs | `contribution-against-joint-owner` | P5.2 | DIST_CIVIL | Art. 113 | 3 | HC |
| PL-PRP-03 | Suit for cancellation of sale deed for fraud (SRA s.31) | `cancellation-of-sale-deed-fraud` | P5.3 | DIST_CIVIL | Art. 59 | 2 | HC |
| PL-PRP-04 | Suit for partition (Hindu family) | `partition-suit-hindu-family` | P5.4 | DIST_CIVIL | Reviewer | 2 | HC |

**P6 Consumer Law** — `/pleadings/consumer-law`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-CON-01 | Consumer complaint under CPA 2019 (s.35 District; s.47 State; s.58 National; goods / services / deficiency toggles; e-filing) | `consumer-complaint-cpa-2019` | P6.1, P6.2, P12.1, P12.2, P12.3 (+ D11.5.3) | CONSUMER_COMMISSION | CPA s.69 (2 years) | 1 | OL (CPA 1986, "District Forum"); TY ("Consumet") |

**P7 Cheque Bounce Matters** — `/pleadings/cheque-bounce-matters`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-CHQ-01 | Complaint under NI Act 1881 ss.138 and 142 (jurisdiction s.142(2); BNSS s.223 note) | `cheque-bounce-complaint-section-138` | P7.1, P7.2, P7.3, P7.4 | MAGISTRATE | s.142(1)(b) (1 month) | 1 | OL (BNSS cognizance note); TY ("Instrument") |
| PL-CHQ-02 | Evidence affidavit of complainant (NI Act s.145) | `cheque-bounce-evidence-affidavit` | P7.5 | MAGISTRATE | — | 1 | RW (vague title) |

**P8 Suit for Damages** — `/pleadings/suit-for-damages`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-DMG-01 | Suit for damages for trespass (toggle: illegal attachment) | `damages-for-trespass` | P8.1, P8.3 | DIST_CIVIL | Reviewer | 2 | HC |
| PL-DMG-02 | Suit by bailor against bailee | `damages-bailor-against-bailee` | P8.2 | DIST_CIVIL | Reviewer | 3 | TY ("Bailer") |
| PL-DMG-03 | Suit against public servant/police officer for wrongful acts (CPC s.80 notice prerequisite) | `damages-against-public-servant` | P8.4 | DIST_CIVIL | Reviewer | 3 | HC |
| PL-DMG-04 | Suit for damages for medical negligence (toggle: consumer route PL-CON-01) | `damages-medical-negligence` | P8.5 | DIST_CIVIL | Reviewer | 2 | HC |
| PL-DMG-05 | Suit by landlord against tenant for injury to premises | `damages-landlord-against-tenant` | P8.6 | DIST_CIVIL | Reviewer | 3 | HC |
| PL-DMG-06 | Suit for wrongful sale of plaintiff's house | `damages-wrongful-sale-of-house` | P8.7 | DIST_CIVIL | Reviewer | 3 | HC |
| PL-DMG-07 | Suit for breach of contract of service | `damages-breach-of-contract-of-service` | P8.8 | DIST_CIVIL | Art. 55 | 3 | HC |
| PL-DMG-08 | Suit for malicious prosecution | `damages-malicious-prosecution` | P8.9 | DIST_CIVIL | Art. 74 | 2 | OL (IPC → BNS) |

(P8.1 and P8.3 merged as one page with an "illegal attachment" toggle; the area therefore has 8 pages from 9 drafts.)

**P9 Money Recovery & Financial Matters** — `/pleadings/money-recovery-and-financial-matters`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-MNY-01 | Suit for recovery of money (toggles: CPC O.XXXVII summary suit; commercial suit with Commercial Courts Act s.12A pre-institution mediation statement) | `money-recovery-suit` | P9.1 | DIST_CIVIL / DIST_COMMERCIAL | Art. 113 / specific article | 1 | OL (s.12A; O.XXXVII) |
| PL-MNY-02 | Suit for refund of money advanced for performance of contract | `refund-of-advance-suit` | P9.2 | DIST_CIVIL | Reviewer | 2 | HC |
| PL-MNY-03 | Suit for price of goods sold and delivered | `recovery-for-goods-sold` | P9.3 | DIST_CIVIL / DIST_COMMERCIAL | Art. 14 | 2 | HC |
| PL-MNY-04 | Suit on a promissory note (toggle: O.XXXVII) | `suit-on-promissory-note` | P9.4 | DIST_CIVIL | Arts. 34–38 (reviewer) | 2 | HC |
| PL-MNY-05 | Suit on a foreign bill of exchange | `suit-on-foreign-bill-of-exchange` | P9.5, P9.6 | DIST_COMMERCIAL | Reviewer | 3 | Exact duplicate removed |

**P10 Alternative Dispute Resolution** — hub kept for commissioned drafts (§4.3) and a neutral ODR-provider cross-link (P19 §4I: Equator is one provider behind `ODR_PORT`, disclosed as a group company, never default); "Award by an Arbitral Tribunal" (P10.1) moves to Documents D11.2 as a professional-only arbitrator document (PRO, ADV); awards themselves are made by the institution the parties chose.

**P11 Intellectual Property Rights** — `/pleadings/intellectual-property-rights`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-IPR-01 | Suit for injunction — copyright infringement (Copyright Act 1957 s.55; IP disputes are commercial disputes — CCA s.2(1)(c)(xvii) [VERIFY]) | `copyright-injunction-suit` | P11.1 | DIST_COMMERCIAL / HC_GENERIC | Reviewer | 2 | HC |
| PL-IPR-02 | Suit for damages — copyright infringement | `copyright-damages-suit` | P11.2 | DIST_COMMERCIAL | Reviewer | 3 | HC |

**P12 Corporate Law** — the three manual drafts are consumer complaints (merged into PL-CON-01). The hub is rebuilt with the commissioned NCLT set (§4.3).

**P13 MACT & Insurance** — `/pleadings/mact-and-insurance`

| ID | Canonical page | Slug | Merges | Forum | Limitation | Wave | Content |
|---|---|---|---|---|---|---|---|
| PL-INS-01 | Suit against insurance company (with Insurance Ombudsman route note — P15) | `suit-against-insurance-company` | P13.1 | DIST_CIVIL / DIST_COMMERCIAL | Reviewer | 2 | HC; add Ombudsman Rules 2017 route |

**Count:** Civil 14 · Family 15 (incl. DV re-filed) · Succession 3 · Criminal 9 · Rent & Property 4 · Consumer 1 · Cheque 2 · Damages 8 · Money 5 · ADR 0 · IPR 2 · Corporate 0 · MACT 1 = **64 canonical pages** from 89 drafts (+ the award moved to Documents). (R5's ≈68 estimate did not merge the cheque complaints, the divorce pair, the trespass pair or the corporate consumer complaints.)

### 4.2 Court documents imported from the Documents manual

Documents flagged **PLD** in §2 are built in the Studio. Most map onto §4.1 pages; six become new pages.

| Document ID | Maps to | New page (if any) | Wave |
|---|---|---|---|
| D2.1.1 | PL-FAM-13 | — | 1 |
| D2.2.1 Application for release of property (police custody) | — | **PL-CRM-10** Application for release of property — BNSS ss.497/503 (formerly CrPC ss.451/457) [VERIFY] `release-of-seized-property` (PLD\*) | 2 |
| D2.2.3 / D2.2.4 / D2.2.5 / D2.2.6 | PL-FAM-04 / -03 / -07 or -08 / -01 | — | — |
| D2.3.1–D2.3.3 | PL-FAM-15 | — | 1 |
| D2.4.1, D2.4.3 | PL-FAM-14 | — | 1 |
| D2.4.4 | PL-FAM-10 (a husband claims under HMA ss.24–25, not BNSS s.144) | — | 1 |
| D2.4.5 / D2.4.6 | — | **PL-FAM-16** Reply to maintenance application `reply-to-maintenance-application` | 1 |
| D11.5.2 | — | **PL-CON-02** Consumer appeal (CPA 2019 s.41 / s.51) `consumer-appeal` | 2 |
| D11.5.3 | PL-CON-01 | — | 1 |
| D11.5.5 | — | **PL-CON-03** Written version/reply of opposite party `consumer-written-version` | 2 |
| D11.6.1 | — | **PL-INS-02** Motor accident claim petition (MV Act 1988 s.166; s.166(3) six months [VERIFY]) `mact-claim-petition` | 1 |
| D13.2.1 | — | **PL-PRP-05** Complaint to RERA authority / adjudicating officer (RERA Act 2016 s.31; State rules form [VERIFY]) `rera-complaint` | 2 |

Studio total at load: **64 + 6 = 70 pleading pages.**

### 4.3 Commissioned content gaps (promised by the manual intro, not drafted) [OWNER to approve]

| ID | Draft | Area | Type · reviewer | Wave |
|---|---|---|---|---|
| PL-CRP-01 | Petition for oppression and mismanagement (Companies Act 2013 ss.241–242) | Corporate (NCLT) | PLD\* · ADV/CS | 3 |
| PL-CRP-02 | Application by financial creditor (IBC 2016 s.7) | Corporate (NCLT) | PLD\* · ADV | 3 |
| PL-CRP-03 | Demand notice (IBC s.8) and application by operational creditor (s.9) | Corporate (NCLT) | PLD\* · ADV | 3 |
| PL-CRP-04 | Appeal for restoration of struck-off company (Companies Act s.252) | Corporate (NCLT) | PLD\* · ADV/CS | 3 |
| PL-ADR-01 | Petition for interim measures (A&C Act 1996 s.9) | ADR | PRO · ADV | 3 |
| PL-ADR-02 | Petition for appointment of arbitrator (A&C Act s.11) | ADR | PRO · ADV | 3 |
| PL-ADR-03 | Application for pre-institution mediation (Commercial Courts Act s.12A; PIMS Rules 2018 [VERIFY]) | ADR | PLD · ADV | 2 |
| PL-CIV-15 | Application for condonation of delay (Limitation Act s.5) | Civil | PLD · ADV | 2 |
| PL-CON-04 | Writ petition skeleton (Constitution Art. 226) — advocate-only | Constitutional | PRO · ADV | 3 |
| PL-ENG-01 | Electricity consumer grievance to CGRF and Ombudsman (Electricity Act 2003 s.42(5)–(6)) | Energy | PLD · ADV | 3 |

Until published, hubs make no promise of these drafts (NN-20).

---

## 5. Compliance services (7 groups → 22 services) — owning phase P14; storefront in P16/P21

**Type:** all are **PRO** (delivered by LawDocs-employed professionals for non-reserved work, or by independent practitioners engaged directly for attest functions — NN-41, D-05); the "Self-serve docs" column lists templates the user can draft free (TA). **Reviewer** = profession that delivers and reviews the page. **Formalities** = filings/registrations involved (F) and stamp (S). **Content** codes as §1; CP items name the copied source (R5 §4).

| ID | Service | Slug (`/compliance/{group}/…`) | Self-serve docs | Reviewer | Formalities | Wave | Content |
|---|---|---|---|---|---|---|---|
| C1.1 | Corporate compliances | `roc-compliances/corporate-compliances` | Board resolutions (D4.2.10) | CS | F | 1 | HC; verify DIR-3 KYC periodicity, ADT-1, MGT-7A |
| C1.2 | Company and OPC annual filings | `roc-compliances/companies-and-opc-annual-filings` | — | CS | F | 1 | HC; MCA V3 forms check |
| C1.3 | LLP annual filing | `roc-compliances/llp-annual-filing` | — | CS | F | 1 | HC |
| C2.1 | Closing a company | `closure-of-business/closing-of-company` | — | CS | F | 2 | HC; add C-PACE (STK-2) |
| C2.2 | Closing an LLP | `closure-of-business/closure-of-llp` | — | CS | F | 2 | CP (LegalWiz FAQ) |
| C2.3 | Closing an OPC | `closure-of-business/closing-an-opc` | — | CS | F | 2 | HC |
| C3.1 | GST registration | `gst/gst-registration` | — | CA | F | 1 | OL (GST 2.0 rates from 22 Sep 2025; biometric authentication) |
| C3.2 | GST return filing | `gst/gst-return-filing` | — | CA | F | 1 | OL (GSTR-2/3 → GSTR-1/1A, 3B, 2B, IMS) |
| C4.1 | Income-tax return filing | `taxation/income-tax-return-filing` | — | CA | F | 1 | CP (Vakilsearch); OL (Income-tax Act 2025 from 1 Apr 2026; dual-cite) |
| C4.2 | TDS return filing | `taxation/tds-return-filing` | — | CA | F | 1 | CP (Corpbiz, Vakilsearch); OL (2025 Act section numbers [VERIFY]) |
| C4.3 | Professional tax registration | `taxation/professional-tax-registration` | — | CA | F | 2 | CP (corpbiz.io FAQs) |
| C5.1 | Accounting and book-keeping | `accounting/accounting-and-book-keeping` | — | CA | — | 2 | CP (provenience.in FAQs) |
| C5.2 | Payroll maintenance | `accounting/payroll-maintenance` | Offer/appointment letters (D10.10) | CA | — | 2 | CP (Vakilsearch); OL (Code on Wages 2019; SS Code 2020) |
| C6.1 | Provident fund registration | `labour-law-compliances/provident-fund-registration` | — | CA/ADV | F | 1 | CP (Vakilsearch); OL (SS Code 2020; schemes continue) |
| C6.2 | ESI registration | `labour-law-compliances/esi-registration` | — | CA/ADV | F | 1 | OL (SS Code 2020) |
| C6.3 | Shops and establishments licence | `labour-law-compliances/shops-and-establishments-licence` † | — | ADV | F | 1 | CP (Vakilsearch ×3); State Acts continue |
| C6.4 | Employee stock option plan (ESOP) | `labour-law-compliances/employee-stock-option-plan` † | ESOP plan and grant letter (D10.8.4) | CS | F (special resolution, MGT-14) | 2 | HC; TY (escaped "[ESOP]") |
| C7.1 | Secretarial audit | `audit/secretarial-audit` | — | CS (attest: independent PCS engaged directly) | F | 2 | OL (SEBI LODR Reg 24A amendments Dec 2024) |
| C7.2 | Tax audit | `audit/tax-audit` | — | CA (attest: independent CA engaged directly) | F | 2 | OL (threshold ₹10 crore where cash ≤ 5%; 2025 Act numbering) |
| C7.3 | GST annual return and reconciliation (GSTR-9/9C) | `audit/gst-annual-return-and-reconciliation` † | — | CA | F | 2 | OL (s.35(5) omitted w.e.f. 1 Aug 2021; 9C self-certified) — re-scope |
| C7.4 | Company (statutory) audit | `audit/company-audit` | — | CA (attest: independent CA) | F | 3 | CP (Registrationwala, hub) |
| C7.5 | Internal audit | `audit/internal-audit` | — | CA | — | 3 | HC; verify s.138 Companies Act thresholds |

Hub items: C0 landing "Customer experiences" testimonials are **fabricated/adapted** — remove (NN-49); C2 hub Wikipedia definition (CP); C5 hub Provenience (CP); C7 hub Registrationwala (CP).

---

## 6. Start-a-business services (6 groups → 26 services) — owning phase P14

All **PRO** with self-serve document packs (TA). Replace every "Call now. 9468776000" CTA with the unified contact number and the Vidhi/"Hire a professional" blocks (R5 §8.4). Government fees shown separately from professional fees (NN-22).

| ID | Service | Slug (`/start-a-business/{group}/…`) | Self-serve docs | Reviewer | Formalities | Wave | Content |
|---|---|---|---|---|---|---|---|
| S1.1 | Private limited company registration | `incorporate-your-business/private-limited-company` † | AoA (D4.2.3), SHA (D4.2.7), founders' agreement (D5.4.2) | CS | F, S (MoA/AoA duty via SPICe+ [VERIFY per State]) | 1 | HC; TY ("PLC" → Pvt Ltd) |
| S1.2 | One person company | `incorporate-your-business/one-person-company` | — | CS | F, S | 1 | OL (2021 OPC liberalisation) |
| S1.3 | Sole proprietorship | `incorporate-your-business/sole-proprietorship` | Self-declaration (D4.7.1), NOC | CA | F (GST/Udyam/S&E as needed) | 1 | HC |
| S1.4 | Partnership firm | `incorporate-your-business/partnership-firm` | Partnership deed (D4.6.1) | ADV/CA | S, F (Registrar of Firms) | 1 | HC |
| S1.5 | Limited liability partnership | `incorporate-your-business/limited-liability-partnership` | LLP agreement (D4.3.1) | CS | F, S | 1 | CP (toppr links) |
| S1.6 | Nidhi company | `incorporate-your-business/nidhi-company` | — | CS | F (NDH-4) | 3 | CP (enterslice link); OL (Nidhi Amendment Rules 2022) |
| S2.1 | Patent filing | `protect-your-intellectual-property/patent` | Patent assignment/licence (D8.2) | PA | F | 2 | CP (LegalRaasta; upcounsel); update Patents (Amendment) Rules 2024 |
| S2.2 | Copyright registration | `protect-your-intellectual-property/copyright` † | Copyright assignment/licence (D8.1) | ADV | F | 2 | TY ("Copy Right") |
| S2.3 | Trademark registration | `protect-your-intellectual-property/trademark` | TM assignment/licence (D8.3) | ADV/TMA | F | 1 | CP (Wikipedia; ebizfiling) |
| S2.4 | Geographical indication registration | `protect-your-intellectual-property/geographical-indications` | — | ADV | F | 3 | RW |
| S2.5 | Logo design and branding | `protect-your-intellectual-property/logo-designing-and-branding` | Copyright assignment from designer (D8.1.2) | ED (+ ADV for assignment) | — | 3 | RW (no procedure/docs) |
| S3.1 | FSSAI registration/licence | `get-a-license/fssai` | — | CA/ADV | F | 1 | CP (legaldocs.co.in FAQ) |
| S3.2 | Import export code (IEC) | `get-a-license/import-export-code` † | — | CA | F (annual update Apr–Jun) | 1 | CP (eximguru link) |
| S4.1 | MSME (Udyam) registration | `registrations-for-business/msme-registration` | — | CA | F | 1 | OL (Udyog Aadhaar → Udyam; limits from 1 Apr 2025) |
| S4.2 | Industrial design registration | `registrations-for-business/industrial-design-registration` | — | PA/ADV | F | 3 | HC |
| S4.3 | APEDA registration | `registrations-for-business/apeda-registration` | — | CA | F | 3 | HC |
| S4.4 | Pollution consent (CTE/CTO) | `registrations-for-business/pollution-registration` | — | ADV | F | 3 | RW |
| S4.5 | Spices Board registration | `registrations-for-business/spices-board-registration` | — | CA | F | 3 | CP (Wikipedia); one-liner fix |
| S4.6 | Barcode (GS1) registration | `registrations-for-business/barcode-registration` | — | ED | F | 3 | HC |
| S5.1 | Agmark certification | `quality-certification/agmark-certification` | — | ED | F | 3 | Rewrite (dmi.gov.in text) |
| S5.2 | Hallmark registration | `quality-certification/hallmark-certification` | — | ED | F | 3 | CP (Wikipedia, Business Standard); OL (mandatory from 16 Jun 2021; HUID from 1 Apr 2023) |
| S5.3 | ISI certification | `quality-certification/isi-certification` | — | ED | F | 3 | HC |
| S5.4 | ISO certification support | `quality-certification/iso-certification` | — | ED | — (certification body, not a registry) | 3 | HC |
| S6.1 | Section 8 company registration | `ngo-and-society-registration/section-8-company-registration` | AoA (D4.2.3) | CS | F, S | 1 | OL (s.25 CA 1956 context only; 12A/80G → 2025 Act [VERIFY]) |
| S6.2 | Trust registration | `ngo-and-society-registration/trust-registration` | Public/private trust deed (D4.8.5–6) | ADV | S, R* | 2 | OL (12A/80G → 2025 Act) |
| S6.3 | Society registration | `ngo-and-society-registration/society-registration` | By-laws (D4.1.2) | ADV | F | 2 | HC |

---

## 7. Content legal-review backlog — seed items (load into `tpl.backlog_item`, P06 FR-P06-54)

| ID | Type | Old reference → current law | Scope (this appendix) | Fix instruction | SLA |
|---|---|---|---|---|---|
| BL-001 | OUTDATED_LAW | CrPC 1973 → BNSS 2023 (1 Jul 2024; savings BNSS s.531) | D2.2, D2.4, D2.5, D2.7, D3.3; PL-FAM-14; PL-CRM-* | Map sections (125→144, 167(2)→187, 200→223, 205→228, 256→279, 311→348, 317→355, 320→359, 437→480, 438→482, 439→483); add "(formerly CrPC s.x)" | 30 days |
| BL-002 | OUTDATED_LAW | IPC 1860 → BNS 2023 | D1.2, D2.3, D3.5, D6.1, D11.9; PL-CIV-11, PL-DMG-08, PL-FAM-15 | 498A→85/86; 406→316; 420→318; 499/500→356; 506→351; pre-1 Jul 2024 offences under IPC | 30 days |
| BL-003 | OUTDATED_LAW | Indian Evidence Act 1872 s.65B → BSA 2023 s.63 (Schedule certificate) | D11.1, D11.9, D16.1, D17.5 | Replace certificate language; link P10 s.63(4) generator | 30 days |
| BL-004 | OUTDATED_LAW | Consumer Protection Act 1986 / "District Forum" → CPA 2019, Commissions, s.69 limitation, 2021 pecuniary limits | D3.2, D6.1, D11.5; PL-CON-* | Rewrite forum, limitation, filing route | 30 days |
| BL-005 | OUTDATED_LAW | Companies Act 1956 (s.25, s.292) → Companies Act 2013 (s.8, ss.179/180) | D3.2, D4.1, D4.2, D12.4; S6.1 | Replace citations; "formerly s.25" context only | 30 days |
| BL-006 | OUTDATED_LAW | Listing Agreement / Clause 49 → SEBI (LODR) Regulations 2015 | D4.2.5, D4.2.6 (RET); D15.1 | Retire templates; build LODR policy packs (D14) | 30 days |
| BL-007 | OUTDATED_LAW | Udyog Aadhaar → Udyam Registration; MSME limits revised from 1 Apr 2025 | D4.4; S4.1 | Rewrite; remove udyogaadhaar link | 30 days |
| BL-008 | OUTDATED_LAW | GSTR-2/3 matching; s.35(5) GST audit → GSTR-1/1A/3B/2B, IMS; self-certified 9C; GST 2.0 rates | C3.1, C3.2, C7.3; D18.1 | Rewrite procedure; re-scope C7.3 | 30 days |
| BL-009 | OUTDATED_LAW | Income-tax Act 1961 → Income-tax Act 2025 (1 Apr 2026; "tax year") | D1.5, D4.6, D5.3, D17.4; C4.*, C7.2; S6.1–S6.2 | Dual-cite during transition; verify new section numbers [VERIFY] | 30 days |
| BL-010 | OUTDATED_LAW | Pre-Code labour statutes → Code on Wages 2019, IR Code 2020, SS Code 2020, OSH Code 2020 (21 Nov 2025) | D7.6, D10.4, D10.11; C5.2, C6.* | Cite Codes; State S&E Acts continue; transitional rules | 30 days |
| BL-011 | OUTDATED_LAW | IT Act s.43A/SPDI Rules → DPDP Act 2023 and Rules 2025 | D9.5, D9.6, D9.8 | Build DPDP notice/DPA templates (§3) | 30 days |
| BL-012 | OUTDATED_LAW | "eSign on every document" → IT Act s.1(4) First Schedule as amended 2022 | D3.10, D4.8, D12.8, D17.3, D17.5, D17.6 | Show eligibility box; wet-ink/registration route; reconcile R rows | 14 days |
| BL-013 | OUTDATED_LAW | Pre-2018 Specific Relief Act; money suits without s.12A; mutual-consent wait fixed | D1.2; PL-CIV-07, PL-MNY-01, PL-FAM-05 | Update grounds/prayers; add s.12A paragraph; waiver application | 30 days |
| BL-014 | OUTDATED_LAW | Court-ordered adoption → JJ (Amendment) Act 2021 / Adoption Regulations 2022 (District Magistrate); HAMA deeds remain | D17.1 | Distinguish HAMA deed vs JJ route | 30 days |
| BL-015 | OUTDATED_LAW | Hallmarking dates; Nidhi pre-2022; OPC pre-2021 | S5.2, S1.6, S1.2 | Rewrite | 30 days |
| BL-016 | COPIED_THIRD_PARTY | 21 sections with competitor brands, scraped FAQs, Wikipedia text (R5 §4) | §5–§6 CP rows; C0, C2, C5, C7 hubs | Rewrite from scratch; plagiarism scan result recorded | 14 days |
| BL-017 | COPIED_THIRD_PARTY | Fabricated/adapted testimonials (C0 and 6 repeats) | Compliance hubs | Delete; only verified, consented reviews (NN-49) | 7 days |
| BL-018 | COPIED_THIRD_PARTY | Borrowed one-liners ("Conflict is inevitable…", "Competition makes us faster…", "Win the workplace…", Yoda line) | D1.1, D10.5, D11.2, D11.3 | Replace with original lines (R5 §6.2) | 14 days |
| BL-019 | DUPLICATE | 17 R5 aliases + 3 new + 5 near-duplicates (≈) | §2 | 301 aliases; variant model decision [OWNER] | 14 days |
| BL-020 | TYPO_HEADING | Heading/slug typos (R5 §3.2) | §2 †, §4 TY | Correct H1/slug; redirect | 7 days |
| BL-021 | THIN_OR_STUB | 48 stubs and "Educate on what is ?" placeholder FAQs | §2 RW (stub) | Keep `noindex`; write or merge | per wave |

---

## 8. Roll-up and load order

| Section | Raw (manual) | Canonical to load | TA | AI | PRO | PLD | RET | Wave 1 | Wave 2 | Wave 3 |
|---|---|---|---|---|---|---|---|---|---|---|
| Documents | 347 entries | 327 | 299 | 3 | 4 | 19 (→ P10) | 2 | 169 | 123 | 14 |
| Pleadings | 89 drafts | 64 + 6 imported = 70 pages (+ 10 commissioned) | — | — | 3 (commissioned) | 70 (+7) | — | 25 | 33 | 12 (+ commissioned) |
| Compliance services | 22 | 22 | docs only | — | 22 | — | — | 10 | 10 | 2 |
| Start-a-business services | 26 | 26 | docs only | — | 26 | — | — | 10 | 4 | 12 |

eSign seed across the 327 canonical documents: **V 234 · C 58 · R 14 · X 21**.

**Load order.** (1) Taxonomy and aliases (all 18 categories, 134 sub-categories; `noindex` where empty or upcoming). (2) Wave-1 documents with open backlog items fixed first (BL-001–BL-012 scope). (3) Wave-1 pleadings with P10. (4) Service pages with storefront (orders handled through P18 delivery until P14 workflows ship). (5) Wave 2, then Wave 3 and commissioned items. Each item publishes only through P06 maker-checker with a reviewer of record (NN-18, NN-30).

**Maintenance.** This appendix is regenerated from the database at each content release (`tpl`, `pld`, `bsv` exports) so that slugs, waves and statuses never drift from what is live; the regeneration script lives in `tools/content/export_appendix_e.ts`.
