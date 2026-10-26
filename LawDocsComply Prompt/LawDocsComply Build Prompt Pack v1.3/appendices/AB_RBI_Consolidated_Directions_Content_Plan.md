# Appendix AB — RBI Consolidated Directions: Content Plan and Catalogue *(v1.1)*

> **Binding for:** P03 (content library, template registry, importer, Regulation Catalogue), P05 (regulatory change management, concordance, AI Question Authoring Studio), P15 (entity-family applicability), P11 (Supervisory Returns directions as return definitions), Part-2 production (`part2_prompts/00` and `01`–`06`). **Companion workbook:** `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`. **Research date:** 25 October 2026. **Primary sources:** rbi.org.in Master Directions pages by department and RE category (`BS_ViewMasterDirections.aspx?did=403`–`413` for the Department of Regulation, `419`–`429` for the Department of Supervision, `338` for Consumer Education and Protection), RBI circular RBI/2025-26/100 of 28 November 2025 ("Consolidation of Regulations – Withdrawal of circulars").
>
> **Management instruction of 25 October 2026 (R-108):** "The 28 November 2025 set is the 238 consolidated directions on other topics, I know, but these directions only shall be ultimately uploaded on the compliance tool." (RBI's withdrawal circular counts the same set as 244 Master Directions — AB-D2.) This appendix turns that instruction into a content plan: what exactly is uploaded, in which order, by whom, in which file, and how the tool keeps it current.

---

## AB.1 Summary of decisions

| # | Decision *(v1.1)* | Effect |
|---|---|---|
| AB-D1 | **The RBI content base is the Department of Regulation consolidated Master Directions issued on 28 November 2025**, read as amended to date, plus the DoR directions issued since, the Department of Supervision directions of 31 July 2026, the CEPD Internal Ombudsman directions of 14 January 2026 and the Reserve Bank – Integrated Ombudsman Scheme, 2026. No question sheet is written against a repealed pre-consolidation Master Direction or circular. | All RBI-family checkpoints cite the consolidated instruments; the 9,445 withdrawn circulars exist in LDC only as historical sources for the concordance (AB.5). |
| AB-D2 | **238 and 244 are both RBI figures — use the serial range.** RBI's press release of 28 November 2025 (2025-2026/1588) speaks of 238 function-wise Master Directions for eleven RE categories; RBI's circular RBI/2025-26/100 of the same date counts **244 Master Directions** and withdraws 9,445 circulars. The RBI-page serials run continuously from RBI/DOR/2025-26/143 to /386 (244 numbers), which include four licensing/subsidiary guidelines and a "Forthcoming Instructions" direction [VERIFY how RBI arrives at 238]. LDC catalogues all 244 serials. | Files that say "238" add "(244 Master Directions per RBI/2025-26/100; serials /143–/386)" — see `_contrib/v11/G4_integration_notes.md`. |
| AB-D3 | **240 of the 244 are live today.** Four 2025 dividend directions (Commercial Banks /168, Small Finance Banks /199, Payments Banks /217, Local Area Banks /242) no longer appear on RBI's lists; they were replaced on 10 March 2026 by new dividend directions (/387–/391). | The four are catalogued as `Superseded` and never receive question sheets. |
| AB-D4 | **The catalogue is pre-seeded into the tool.** Every catalogue row becomes a `cnt.instruments` record (with its first `cnt.instrument_versions` row) before any question sheet exists, so the client admin's Regulation Catalogue (SCR-CNT-10) shows the full list from day one, with each direction's coverage state (`Checkpoints available`, `In preparation`, `Planned`). | R-087 is met even before Part 2 is complete; clients see what is coming and when. |
| AB-D5 | **One question sheet per direction per RE category.** Directions with the same subject in several categories (for example "Know Your Customer" exists for eleven categories) are written once for the lead category and then cloned and adapted, never merged into one cross-category sheet. | Applicability stays exact; cloning cuts effort (AB.7.4). |
| AB-D6 | **Production order is by wave and priority** (content-production waves W1–W3 are distinct from the product release Waves 1–4 of master §13.2; content W1 must be complete for product Wave 1 GA) *(v1.1, V1)* (Appendix AB.7; catalogue sheet `Waves`): W1 NBFC; W2 UCB, RCB, ARC, credit information companies; W3 commercial banks, SFBs, payments banks, LABs, RRBs, AIFIs, non-bank PPI issuers. Within a wave: P1 → P2 → P3. | Matches master §13 (RBI-NBFC is a Wave-1 family). |
| AB-D7 | **Reference numbers are recorded with their basis.** RBI's PDF file codes for these directions equal the RBI reference serial (checked against nine directions whose first page was read). A reference not yet read on the document is marked `Derived … [VERIFY on document]` and the importer will not publish a sheet until the reference basis is `Confirmed`. | NN-06 citation integrity; NN-38 (unverified rules advisory only). |

---

## AB.2 What exactly is uploaded

### AB.2.1 The four instrument sets

| Set | Issuer | Date | Numbers | Count | Status in LDC |
|---|---|---|---|---|---|
| **A. Consolidated Master Directions** | Department of Regulation (DoR) | 28 Nov 2025 | RBI/DOR/2025-26/143 – /386 | 244 issued; **240 live**, 4 superseded | Content base (AB-D1) |
| **B. DoR directions issued after the consolidation** | DoR | 10 Mar 2026 – 7 Oct 2026 (to date) | /387–/391 (dividends, Mar 2026); /397, /398 (commercial banks, 27 Apr 2026); /472 (market risk, 21 Sep 2026); /474 (CVA, 7 Oct 2026) [VERIFY FY prefix of the 2026-27 numbers] | 9 | Content base; new instruments |
| **C. Supervisory directions** | Department of Supervision (DoS) | 31 Jul 2026 | RBI/DoS/2026-27/408 – /471 | 64 | Content base; also drive P11 return definitions (Supervisory Returns directions) |
| **D. Consumer protection** | Consumer Education and Protection Department (CEPD) | 14 Jan 2026; scheme effective 1 Jul 2026 | Internal Ombudsman directions for six RE types (PDF codes 380–385 [VERIFY]); Reserve Bank – Integrated Ombudsman Scheme, 2026 [VERIFY reference] | 6 + 1 | Content base; drive P14 grievance clocks |

The companion workbook lists all **320** rows (240 + 9 + 64 + 6 + 1) with title, reference, date, department, subject area, applicability notes, consolidated-from summary, last-updated date shown by RBI, template, command file, priority, wave, size class, indicative effort, proposed file name, status, owner, reviewer, RBI page and verification status.

### AB.2.2 Counts by RE category

| RE category | Template | Wave | Set A (live) | Set B | Set C | Set D | Total |
|---|---|---|---|---|---|---|---|
| Non-Banking Financial Companies (incl. HFC, CIC, MGC, SPD, NOFHC, AA, P2P, MFI directions) | `LDC-TPL-RBI-NBFC` | W1 | 35 | 0 | 9 | 1 | 45 |
| All RBI REs within RB-IOS 2026 | each family template | W1 | — | — | — | 1 | 1 |
| Urban Co-operative Banks | `LDC-TPL-RBI-UCB` | W2 | 27 | 0 | 9 | 0 | 36 |
| Rural Co-operative Banks | `LDC-TPL-RBI-RCB` | W2 | 26 | 0 | 3 | 0 | 29 |
| Asset Reconstruction Companies | `LDC-TPL-RBI-ARC` | W2 | 4 | 0 | 1 | 0 | 5 |
| Credit Information Companies | `LDC-TPL-RBI-OTH` | W2 | 2 | 0 | 2 | 1 | 5 |
| Commercial Banks | `LDC-TPL-RBI-SCB` | W3 | 32 | 5 | 9 | 1 | 47 |
| Small Finance Banks | `LDC-TPL-RBI-SCB` | W3 | 30 | 1 | 9 | 1 | 41 |
| Payments Banks | `LDC-TPL-RBI-SCB` | W3 | 17 | 1 | 9 | 1 | 28 |
| Local Area Banks | `LDC-TPL-RBI-SCB` | W3 | 25 | 1 | 7 | 0 | 33 |
| Regional Rural Banks | `LDC-TPL-RBI-SCB` | W3 | 23 | 1 | 2 | 0 | 26 |
| All India Financial Institutions | `LDC-TPL-RBI-OTH` | W3 | 19 | 0 | 4 | 0 | 23 |
| Non-bank PPI issuers (Internal Ombudsman only) | `LDC-TPL-RBI-OTH` | W3 | 0 | 0 | 0 | 1 | 1 |
| **Total** | | | **240** | **9** | **64** | **7** | **320** |

Notes: (1) Set A for Commercial Banks includes two guidelines (Universal Banks – Licensing; Setting Up of Wholly Owned Subsidiaries by Foreign Banks) and a "Forthcoming Instructions" direction; SFB and UCB include one licensing guideline each. (2) HFCs, CICs, MGCs, SPDs and NOFHCs are RBI categories with their own principal directions inside the NBFC list on RBI's site; LDC treats them as NBFC types (P15 family `NBFC`) whose common NBFC directions also apply where the applicability paragraph says so. (3) Credit information companies (CICRA 2005 companies such as TransUnion CIBIL) are an RBI category distinct from Core Investment Companies; the catalogue abbreviation is `CIC-CI` to avoid the clash with the NBFC type `CIC`.

### AB.2.3 Subject structure common to every category

RBI used one subject skeleton for all eleven DoR categories. Knowing it lets the content team clone sheets safely:

| Subject group | Directions (DoR set A) | Present in |
|---|---|---|
| Entry and structure | Licensing/Registration (guidelines or SBR), Acquisition and Holding of Shares or Voting Rights / Acquisition of Shareholding or Control, Voluntary Amalgamation, Branch Authorisation, Digital Banking Channels Authorisation, Undertaking of Financial Services | Most categories |
| Governance | Governance | All except ARC, CIC-CI (covered in their principal directions) |
| Capital and distributions | Prudential Norms on Capital Adequacy; Prudential Norms on Declaration of Dividend(s) | Banks, co-op banks, AIFIs, NBFCs |
| Liquidity and reserves | Asset Liability Management; Cash Reserve Ratio and Statutory Liquidity Ratio; Interest Rate on Deposits; Resource Raising Norms; Acceptance of Public Deposits (NBFC) | Varies |
| Credit | Credit Facilities; Credit Risk Management; Concentration Risk Management; Interest Rates on Advances; Credit Cards and/or Debit Cards: Issuance and Conduct | Lenders |
| Credit quality | Income Recognition, Asset Classification and Provisioning; Resolution of Stressed Assets; Treatment of Wilful Defaulters and Large Defaulters | Lenders, ARCs (defaulters) |
| Markets and transfer | Classification, Valuation and Operation of Investment Portfolio; Securitisation Transactions; Transfer and Distribution of Credit Risk | Lenders |
| Reporting | Financial Statements: Presentation and Disclosures; Credit Information Reporting | All lenders; ARCs (CIR) |
| Conduct and customer | Know Your Customer; Responsible Business Conduct | All |
| Operations | Managing Risks in Outsourcing; Climate Finance and Management of Climate Change Risks; Miscellaneous | Most |
| Type-specific principal directions | HFC; CIC; MGC; SPD; NOFHC; AA; P2P; MFI; ARC; Credit Information Companies | NBFC types, ARC, CIC-CI |

The DoS set C adds, per category: Compliance Function; Cybersecurity, Technology: Risk, Resilience and Assurance Framework; Digital Payment Security Controls; Fraud Risk Management; Internal Audit Function; Concurrent Audit (banks); Statutory Audit; Supervisory Returns; Miscellaneous Supervisory Directions (incl. PCA for NBFCs); Auditor's Report (NBFC). Not every category received every DoS direction (RRBs received two; RCBs three) — the catalogue reflects exactly what RBI lists.

---

## AB.3 Why the consolidated directions are the right content base

1. **They are now the law in force.** RBI/2025-26/100 withdrew and repealed 9,445 circulars with immediate effect; actions under the repealed instructions are saved, but obligations from 28 November 2025 run from the new directions. A checkpoint citing a repealed paragraph is a defective checkpoint (NN-06).
2. **They are organised by regulated entity.** Each direction states its own applicability chapter, so P15's applicability engine can map rows to entity families, layers and tiers without inference from cross-referenced circulars.
3. **They are stable containers for amendment.** RBI now amends a direction "as on" a date (the RBI page shows "Updated as on …"); P05 tracks these as instrument versions instead of chasing stand-alone circulars.
4. **They match how supervisors test.** RBI's 31 July 2026 DoS directions (compliance function, internal audit, statutory audit, supervisory returns) refer to the consolidated regulatory directions; inspection teams will test against them.
5. **They make the product comparable across categories.** The common subject skeleton (AB.2.3) means a group with an NBFC, a UCB and an ARC sees one consistent compliance structure.
6. **They are a market driver.** RBI (NBFC – Compliance Function) Directions, 2026 (RBI/DoS/2026-27/460) expect Middle- and Upper-Layer NBFCs to run compliance through workflow-based tools with a unified dashboard [VERIFY paragraph before quoting externally]; a library built on the current directions is what those tools must hold.

---

## AB.4 How the instruments are modelled in LDC

### AB.4.1 Records created per catalogue row (P03 data model)

| LDC record | Populated from catalogue column | Notes |
|---|---|---|
| `cnt.instruments` | Direction title, RE category, department, subject area, RBI page id, source set | `instrument_code` = `RBI.<CAT>.<SUBJECT-SLUG>` (e.g. `RBI.NBFC.GOVERNANCE`); `authority` = RBI; `instrument_type` = MASTER_DIRECTION / GUIDELINE / SCHEME |
| `cnt.instrument_versions` | Reference number and basis, date of issue, last updated (RBI page) | Version 1 = as issued (28 Nov 2025 or later date); each "Updated as on" date becomes a new version when P05 confirms the amendment text |
| `cnt.content_packs` | Template code, wave, priority | One pack per RE category per set (e.g. `PACK.RBI.NBFC.DOR2025`, `PACK.RBI.NBFC.DOS2026`) so clients can adopt whole packs or single directions |
| `cnt.catalogue` (tenant-facing view) | All of the above + coverage state | Coverage state: `PLANNED` (no sheet), `IN_PREPARATION` (sheet Drafted/Reviewed), `AVAILABLE` (published), `SUPERSEDED` |
| `chg.concordance` | Supersedes / consolidated-from summary | Seeded per AB.5 |
| `ret.return_definitions` (P11) | Supervisory Returns directions (Set C) | Each return listed in a Supervisory Returns direction becomes a return definition with its citation (Appendix I) |

### AB.4.2 Identifiers and citations

- **Checkpoint `obligation_ref`:** `RBI/<instrument_code>/v<n>#<para>` — e.g. `RBI/RBI.NBFC.GOVERNANCE/v2#14(3)`. The human citation in the template's Clause / Para No. column (`clause_ref`; v1.0 column K) remains the paragraph as RBI prints it ("Para 14(3)", "Chapter IV, para 21", "Annex II").
- **CompID** *(v1.2; replaces the v1.1 column-E convention)*: issued by the platform when a sheet is imported, never typed by authors, as `RBI-<FAM>-<INST>-<NNNN>` (e.g. `RBI-NBFC-GOV25-0042`; master §6.7, Appendix B §B.12, Appendix E §A.8). `<INST>` is `<SUBJECT><YY>` (RBI-SCB adds a bank-category letter, e.g. `KYCC25`), proposed for every catalogue row in column AF and approved by the content lead before the first CompID is reserved. NBFC examples: `GOV25`, `KYC25`, `CAP25`, `IRACP25`, `ALM25`, `OUTS25`, `CRM25`, `RBC25`, `CIR25`, `HFC25`, `CICORE25`, `MFI25`, `P2P25`; DoS: `CF26`, `CYB26`, `DPS26`, `FRM26`, `IAF26`, `SA26`, `SR26`, `AR26`; CEPD: `IO26`, `RBIOS26`. v1.1 dotted IDs (`RBI-NBFC.GOV.0001`) are kept as aliases.
- **Reference basis:** a sheet is publishable only when its instrument's `reference_basis` = `CONFIRMED` (reference read on the document). The content checker confirms it in Content Studio while reviewing the first page of the PDF; this is a two-minute task and closes the `Derived` flag in the catalogue.

### AB.4.3 Common subjects across categories (shared checkpoints with family-specific applicability)

Some obligations are worded identically in several categories' directions (for example the Know Your Customer chapters, large parts of Responsible Business Conduct, Managing Risks in Outsourcing). LDC does **not** create one shared checkpoint for several categories, because:

- each category's direction is a separate legal instrument with its own paragraph numbering, amendment history and applicability; and
- a client who holds two licences (an NBFC and an ARC in the same group) must evidence compliance under each.

Instead, P03 holds a **`checkpoint_family_link`** ("sibling") relation: when a KYC checkpoint is written for NBFCs and then cloned for UCBs, the clone carries `sibling_of = <NBFC checkpoint id>`. Benefits: (a) the content team sees all siblings when one is amended, and P05 proposes the same change to siblings when RBI amends the common text across categories on the same date (a frequent pattern: many "Updated as on 1 October 2026" entries above); (b) a group tenant can choose **evidence reuse** — one evidence item satisfies sibling instances across its legal entities, still reviewed separately by each entity's checker (NN-05). *(v1.1)*

---

## AB.5 Concordance with the withdrawn circulars and the owner's earlier question banks

### AB.5.1 What a concordance is in LDC

A concordance row says: *old instrument, old paragraph* → *new instrument, new paragraph*, with a status: `SAME_SUBSTANCE`, `MODIFIED`, `MERGED`, `SPLIT`, `DROPPED`, `NEW` (P05 FR-P05-42). It answers the question every compliance officer asks after a consolidation: "Where did my old circular go, and did anything change?"

### AB.5.2 Sources for building it

1. **RBI/2025-26/100 Annex** — the list of 9,445 withdrawn circulars (loaded once as `cnt.instruments` of type `WITHDRAWN_CIRCULAR`, status `REPEALED`, with RBI's dates and numbers).
2. **Each consolidated direction's repeal paragraph** — e.g. NBFC Governance para 44 repeals "existing Directions, instructions, and guidelines relating to governance"; many directions also list the instruments consolidated in a footnote or annex [VERIFY per direction].
3. **RBI's draft directions (RE-wise)** published before 28 November 2025 (`BS_ViewREwiseDraftDirections.aspx`), which carried "List of Circulars to be Repealed/Withdrawn" pages.
4. **Secondary summaries** (for example professional-firm consolidation tables for NBFCs) — used only as hints for the analyst, never as authority; they are captured in the catalogue's "Supersedes / consolidated from" column with the tag "[secondary summary — VERIFY]".

### AB.5.3 Who builds it and how fast

| Step | Actor | Tool | Output |
|---|---|---|---|
| 1. Load the Annex and the repealed MDs as historical instruments | `plt_content_maker` | P05 bulk loader | Historical instrument records |
| 2. For each consolidated direction, list the old instruments it absorbed | Vidhi (AI proposal from the direction's repeal/consolidation text) → analyst confirms | SCR-CHG-03 concordance editor | Instrument-level map |
| 3. Paragraph mapping | Vidhi proposes old para → new para pairs with similarity scores; analyst confirms each (P05 FR-P05-42) | Concordance editor with side-by-side text | `chg.concordance` rows |
| 4. Re-citation of existing checkpoints | System: for each existing checkpoint citing an old para, create a draft new version citing the new para (`SAME_SUBSTANCE`) or raise a review flag (`MODIFIED`/`DROPPED`) | Content Studio | Draft checkpoint versions |
| 5. Checker review and release | `plt_content_checker` → `plt_content_publisher` | Release manager (SCR-CNT-04) | Published re-cited checkpoints; tenant Update "Where did my old circular go?" |

Indicative effort: instrument-level mapping 1–2 hours per direction; paragraph mapping 4–12 hours for an XL direction with AI proposals. The concordance is built **only for directions that have existing LDC checkpoints or tenant overlays** in Wave 1; for categories with no legacy content (most W3 bank categories) the new sheets are written directly against the consolidated directions and no paragraph concordance is needed — only the instrument-level map for the tenant-facing "Where did my old circular go?" table.

### AB.5.4 The owner's existing question banks

| Existing asset (per owner's records) | Treatment *(v1.1)* |
|---|---|
| RBI NBFC question banks written before 28 Nov 2025 for Base Layer, Middle Layer and CIC (live in the beta at lawdocscomply.com, MongoDB) | Migrated in P00 as **historical** checkpoints; P05 concordance (AB.5.3) re-cites them to the 35 NBFC directions. Rows whose substance survives become draft versions of the new sheets, cutting W1 drafting effort; rows mapped `DROPPED` are archived with their history (NN-29). |
| Nine NBFC DoS sheets built in September 2026 (RBI/DoS/2026-27/460–468) | Catalogue status `Drafted`. Before upload: check each against the RBI page's "Updated as on" date (several DoS directions show 1 October 2026 updates for banks; confirm NBFC versions), confirm paragraph references, run the Part-2 QA checklist and the importer validation. |
| IFSCA sheets (43 finished) | Not affected (IFSCA family). |
| Tenant overlays on old checkpoints (beta clients, e.g. the Branch International pilot) | P03 overlay rebase: the overlay is re-pointed to the re-cited checkpoint; where the base checkpoint is `MODIFIED`, the tenant sees a rebase conflict in SCR-CNT-13 with the old base, new base and their overlay side by side; never auto-merged (NN-03). |

---

## AB.6 Pre-seeding the catalogue so client admins can tick directions (R-087)

### AB.6.1 What the client admin sees on day one

SCR-CNT-10 Regulation Catalogue, filtered automatically by the tenant's entity profile (P15). For an NBFC-ML ICC the default view shows the 35 NBFC directions, the 9 NBFC DoS directions, the NBFC Internal Ombudsman directions and RB-IOS 2026, each with:

| Column | Source |
|---|---|
| ☐ Adopt (checkbox) | Tenant action (default: pre-ticked for directions whose applicability rules match the profile; un-ticked for type-specific directions that do not match, e.g. HFC for an ICC) |
| Direction | Catalogue title |
| Reference and date | Catalogue (with "Confirmed"/"Being verified" badge) |
| Last updated | RBI "Updated as on" date and LDC's current version date |
| Applies to you because… | P15 explanation ("Middle Layer: Chapters II–IV apply") |
| Coverage | `Checkpoints available (124)` / `In preparation — expected <month>` / `Planned (Wave 3)` |
| What changed recently | Link to the last P05 Update for this instrument |
| Dependencies | e.g. "Credit Cards direction applies only if you issue credit cards — confirm" |

**Fewer clicks *(v1.1)*:** "Adopt all recommended" (one click, with a preview of how many compliance instances will be created and for which departments); "Adopt pack" per set; "Explain" opens the applicability reasoning; bulk un-tick with a mandatory reason (stored, audited, and shown to the auditor role).

### AB.6.2 Directions without checkpoints yet

A ticked direction in state `PLANNED` or `IN_PREPARATION` creates **one placeholder compliance instance** ("Maintain compliance with <direction> — detailed checkpoints in preparation") owned by the CCO, so the obligation is visible on the register and the board report; it auto-converts to detailed checkpoints when the sheet is published, preserving the placeholder's history. The client may also author tenant-only checkpoints for it with the AI Question Authoring Studio (P05) in the meantime; at publication, P03 offers to map their tenant checkpoints onto the platform ones (keep, replace, or keep as overlay).

### AB.6.3 Profile changes

When a tenant crosses a threshold (e.g. Base → Middle Layer) P15 recalculates applicability; the catalogue shows newly applicable directions and chapters with an effective date; adoption happens in one action with a dated impact preview; historical instances stay as they were (NN-07, NN-29).

---

## AB.7 Part-2 production plan

### AB.7.1 Roles

| Role | Who | Responsibility |
|---|---|---|
| Content lead | Company Secretary (owner) | Approves the wave plan, signs off each family's first sheet, decides disputes |
| Writer | Claude Cowork chat run by a content analyst using `part2_prompts/00` + family command; or P05 AI Question Authoring Studio once live | Drafts sheets per the master command |
| Domain reviewer | CS / CA / ex-banker per subject (governance and secretarial: CS; capital, IRACP, ALM, financial statements: CA; KYC, RBC, fraud, cyber: compliance specialist) | Checks substance, splits, applicability, citations |
| QA reviewer | Content checker (`plt_content_checker`) | Runs `99_QA_Checklist_for_Question_Sheets.md`, the template validator and the importer preview |
| Publisher | `plt_content_publisher` | Publishes the release; triggers tenant Updates |

Maker ≠ checker throughout (NN-05). AI-drafted sheets never auto-publish (NN-04).

### AB.7.2 Order of work

**Wave 1 — NBFC (45 rows):**

1. P1 DoR: Registration, Exemptions and Framework for SBR → Governance → Know Your Customer → Responsible Business Conduct → IRACP → Capital Adequacy → ALM → Credit Facilities → Credit Risk Management → Concentration Risk Management → Credit Information Reporting → Managing Risks in Outsourcing → Financial Statements.
2. P1 DoS: re-verify and upload the nine owner-built sheets (460–468); then NBFC Internal Ombudsman (CEPD 2026); then RB-IOS 2026 (NBFC version).
3. P2 DoR: Undertaking of Financial Services; Investment Portfolio; Securitisation; Transfer and Distribution of Credit Risk; Resolution of Stressed Assets; Wilful Defaulters; Dividends; Acceptance of Public Deposits; Credit Cards; Climate; Miscellaneous; Acquisition of Shareholding or Control; Branch Authorisation; then the type-specific directions in order of market size: HFC, MFI, CIC, P2P, AA, MGC, NOFHC, SPD.
4. P3: Voluntary Amalgamation.

**Wave 2 — UCB, RCB, ARC, credit information companies (75 rows):** clone-and-adapt from the NBFC sheets where the subject exists (KYC, RBC, IRACP, Outsourcing, Credit Information Reporting, Credit Risk/Concentration, Investment Portfolio, Financial Statements, Wilful Defaulters, Stressed Assets, Governance), write fresh where the subject is bank-specific (CRR/SLR, Interest Rate on Deposits, Interest Rates on Advances, Debit Cards, Digital Banking Channels, Licensing/Scheduling/Regulatory Classification for UCBs), then the DoS sets (UCB 9, RCB 3, ARC 1, CIC-CI 2) and the ARC and CIC-CI principal directions.

**Wave 3 — banks and AIFIs (199 rows):** write the Commercial Banks set first as the "bank master", then clone to SFB, PB, LAB, RRB and adapt; AIFI from the bank master plus its Resource Raising Norms; DoS bank sets (CB 9, SFB 9, PB 9, LAB 7, RRB 2, AIFI 4); post-consolidation DoR directions (dividends 2026, commercial-bank 2026 credit-risk standardised approach and asset classification, market risk, CVA).

### AB.7.3 Size classes and effort (planning only)

| Class | Indicative checkpoints | Draft + review hours | Typical directions |
|---|---|---|---|
| S | 15–40 | 4–8 | Dividends, Voluntary Amalgamation, Branch Authorisation, Interest Rates on Advances, Digital Banking Channels, licensing guidelines, Forthcoming Instructions |
| M | 40–90 | 8–16 | Credit Information Reporting, Wilful Defaulters, Undertaking of Financial Services, Credit Cards, MGC, NOFHC, SPD, Auditor's Report, Internal Ombudsman |
| L | 90–180 | 16–32 | ALM, Outsourcing, Investment Portfolio, Financial Statements, Concentration, Credit Risk Management, Securitisation, Transfer and Distribution, Registration/SBR, Deposits, CIC, MFI, P2P, AA, most DoS directions |
| XL | 180–400 | 32–60 | KYC, Responsible Business Conduct, IRACP, Capital Adequacy, Governance, Credit Facilities, Resolution of Stressed Assets, HFC, ARC principal direction, Cybersecurity framework, Miscellaneous Supervisory |

Sum of indicative effort across all 320 rows without cloning savings: about 5,400–10,500 hours (workbook sheet `By_Category_Summary`). Cloning across sibling categories is expected to reduce W2 and W3 effort by 40–60% for cloned subjects [REC; measure on the first three clones and re-plan]. With the P05 AI Question Authoring Studio, the drafting portion is expected to fall further; review hours do not fall below the domain-review floor (NN-04).

**Capacity example:** two writers and two reviewers at 30 productive hours per week each produce roughly 4–6 L-class sheets per week; Wave 1 (45 rows, about 760–1,490 hours) then takes 7–12 weeks, which fits inside the P03–P05 build window (master §13: S10–S23).

### AB.7.4 Clone-and-adapt protocol

1. Copy the reviewed lead-category sheet into the target family template (the General Applicability Layer/Type vocabularies and extension columns differ: e.g. UCB tiers instead of NBFC layers).
2. Open the target category's direction side by side; for every row: confirm the paragraph exists, re-cite Clause / Para No. and Name of Master Direction to the target direction, adjust wording to the target's text, reset the applicability columns, clear CompID (the target family gets its own CompIDs), and delete rows with no counterpart; add rows for paragraphs unique to the target.
3. Record `sibling_of` in the run log (Related Document / Policy / Committee gets "Sibling: <lead file name>, row <n>" — P03 converts it into the sibling link at import).
4. Domain review focuses on the differences list the run log produces ("rows added", "rows deleted", "rows with changed substance").

### AB.7.5 File naming and storage

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx` (v1.2: " v2" is the template contract version), where `<CAT>` ∈ {NBFC, UCB, RCB, ARC, CIC-CI, SCB (commercial banks), SFB, PB, LAB, RRB, AIFI, PPI, ALL}. The proposed name for every row is pre-filled in catalogue column V and the proposed instrument short code in column AF. Revisions: append ` (rev 2)`, ` (rev 3)` (Part-2 master command §3A.9). Store finished sheets in the owner's folder `Compliance Tool Questions/RBI/<CAT>/` mirroring the catalogue, and record the upload date in catalogue column Z.

### AB.7.6 Acceptance checks before upload

| # | Check | Tool |
|---|---|---|
| 1 | Template unchanged (contract v2.0: rows 1–2, machine keys, `Lists` named ranges; CompID left blank) | `templates/_validate_templates_v2.py`; importer header/key hash check |
| 2 | Every paragraph of the direction appears in the para map; sub-clauses split into rows | Part-2 run log, QA checklist §B |
| 3 | Clause / Para No. and Name of Master Direction cite the consolidated direction (never a repealed circular) and the reference basis is Confirmed | QA checklist; catalogue column I |
| 4 | General Applicability (Layer/Type), extension columns and Conditional Applicability match the direction's applicability chapter | Domain reviewer |
| 5 | Due Date & Frequency and Due Date Rule computable by P04; Actionable Last Updated On within the date rule (D-58) | Importer preview (LDC-TPL errors) |
| 6 | Evidence / Proof to Upload, Control Activity (Maker Guidance), Checker Review Points and Auditor Test Procedure present on every row | Importer |
| 7 | No `[VERIFY]` left in any cell | Importer blocks |
| 8 | Risk calibration reasonable (warning above 70% High) | Importer LDC-TPL-030 |
| 9 | Diff against previous version (for re-cited sheets) reviewed | SCR-TPL-04 |

---

## AB.8 Keeping the library current (P05 flow for these directions)

### AB.8.1 Monitoring

P05 watches, for each of the 22 RBI category pages (did 403–413, 419–429) and did 338: new rows, changed titles and changed "Updated as on" dates — at 20:00 IST daily and intraday from RBI's notification and press-release feeds (Appendix F). Because RBI updates the consolidated directions in place, **the "Updated as on" date change is the primary change signal**; the matching amendment notification (where issued) is linked as the amending instrument.

### AB.8.2 From amendment to tenant action

1. **Detect:** "NBFC – Concentration Risk Management Directions, 2025 — Updated as on 25 August 2026" (example from the RBI page).
2. **Fetch and hash** the new consolidated PDF; store as `instrument_version` v(n+1) with `valid_from` = the amendment's effective date (not the fetch date; NN-07).
3. **Diff:** clause-level diff v(n) → v(n+1); Vidhi drafts a plain-language summary with citations (labelled "unreviewed" until checked; NN-34).
4. **Impact:** affected checkpoints (by clause link), sibling checkpoints in other categories (AB.4.3), affected tenants (by adoption and profile), affected overlays.
5. **Draft release:** new checkpoint versions (modified wording, new rows, retired rows marked `[RETIRED]`), with old vs new actionable side by side (P05 FR-P05-62).
6. **Review and publish:** content checker → publisher; catalogue column K updated; Part-2 sheet re-exported as `v2` for the owner's folder.
7. **Tenant Update:** the three-part note — what changed / why it matters to you / what to do — with the old vs new actionable table, effective date, the instances that will change, and one-click actions (assess impact, update policy, add Board agenda item). Completed instances keep their old version (NN-03).

### AB.8.3 New directions

A new direction (for example the commercial-bank Market Risk directions of 21 September 2026) creates a catalogue row and instrument automatically (state `PLANNED`), notifies the content lead, appears in affected tenants' catalogues with the badge "New — checkpoints in preparation", and enters the production queue with priority set by the content lead (default P2; P1 if it has a compliance date within 90 days).

### AB.8.4 Repeal and supersession

When RBI supersedes a direction (the March 2026 dividend directions are the pattern), the old instrument becomes `SUPERSEDED` with `valid_to`; its checkpoints are re-cited through a concordance or retired; tenant instances due after `valid_to` are cancelled with an explanation, and completed instances remain (NN-29).

---

## AB.9 Integration with other modules

| Module | Use of the catalogue *(v1.1)* |
|---|---|
| P11 Return Studio | Each Supervisory Returns direction (Set C) is parsed into return definitions (code, frequency, due date, portal: CIMS/DAKSH) in `ret.return_definitions` with citations; Appendix I is aligned to these directions |
| P14 Grievance | CEPD Internal Ombudsman directions and RB-IOS 2026 drive escalation ladders and clocks (NN-31, NN-40) |
| P06 Governance | Governance directions seed committee requirements (RMC, Audit, NRC, CRO, CCO) per layer/tier (P15 §4F) |
| P08/P09 Risk | Capital Adequacy, ALM, Concentration, IRACP directions seed ratio thresholds and PCA (Miscellaneous Supervisory Directions) in the risk kernel (NN-38) |
| P10 Audit | Internal Audit Function, Concurrent Audit, Statutory Audit and Auditor's Report directions seed audit programmes and report templates |
| P12 Cyber | Cybersecurity, Technology: Risk, Resilience and Assurance Framework and Digital Payment Security Controls directions seed the control library |
| P17 Vidhi notebooks | The RBI notebook per category is built from exactly these instrument versions, so Vidhi's answers cite the current consolidated paragraphs |
| P23 Website | Public "RBI Directions Tracker" page (titles, dates, last updated, LDC coverage) — a lead magnet that shows clients the coverage before they buy [REC] |

---

## AB.10 KPIs

| KPI | Target |
|---|---|
| Catalogue completeness (RBI-listed directions present in LDC) | 100% within 1 business day of RBI listing |
| Reference basis confirmed | 100% of published instruments |
| W1 coverage (NBFC sheets published) | All P1 by Wave-1 GA; all 45 by GA + 8 weeks |
| Amendment latency (RBI "Updated as on" change → tenant Update published) | ≤ 5 business days for P1 directions; ≤ 10 for others |
| Checkpoints citing repealed instruments | 0 |
| Re-citation completion for migrated legacy NBFC checkpoints | 100% mapped or retired before Wave-1 GA |
| Importer first-pass acceptance (sheets with zero blocking errors) | ≥ 90% after the third sheet of each family |
| Sibling drift (siblings with different substance after a common amendment) | 0 unexplained |

---

## AB.11 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-AB-01 | Confirm on the documents the 2026-27 reference prefix for the April–October 2026 DoR directions (/397, /398, /472, /474) | Content checker | Show "Derived" badge; do not publish their sheets until confirmed |
| OI-AB-02 | CEPD Internal Ombudsman reference numbers: the RBI page's PDF codes indicate NBFC = 383 and non-bank PPI = 384, while v1.0 cited RBI/CEPD/2025-26/384 for NBFCs | Content checker | Use the title and date as the citation until confirmed |
| OI-AB-03 | RB-IOS 2026 reference number and whether UCBs/RCBs are covered | Content checker | Mark coverage advisory for co-op banks |
| OI-AB-04 | Paragraph-level applicability for every NBFC direction (the catalogue's NBFC applicability notes come from a secondary summary) | Domain reviewer | Writers read the applicability paragraph (master command §3) |
| OI-AB-05 | Whether RBI publishes formal concordance tables for each direction | Content lead | Build concordances per AB.5.3 |
| OI-AB-06 | Non-DoR RBI instruments for RBI-OTH payment-system entities (PA, PPI, card networks) and FEMA entities (AD Cat-II, FFMC) are outside the 28 Nov 2025 set | Content lead | Catalogue them in v1.2 from the DPSS and FED Master Direction pages (did 344 and 335) |

---

## AB.12 Wave-1 writing guide: the NBFC directions one by one *(v1.1)*

This guide tells the writer and reviewer what to look for in each NBFC instrument. It names subjects, not paragraph numbers: the writer takes every paragraph number from the attached text (master command §8). "Split hot-spots" are places where a single paragraph usually becomes many rows.

| # | Direction (RBI/DOR/2025-26/…) | Applies to (read the applicability paragraph) | What the sheet must capture | Split hot-spots | Reviewer |
|---|---|---|---|---|---|
| 1 | Registration, Exemptions and Framework for Scale Based Regulation (/339) | All NBFCs incl. HFCs | Registration and NOF, principal-business criteria, exemptions, layer classification and transition, Upper Layer identification and consequences, types | NOF glide paths; layer-transition timelines; each exemption condition | CS + CA |
| 2 | Governance (/344, confirmed) | All NBFCs except HFCs; BL Ch III, ML Ch II–IV, UL Ch II–V | Board-approved policies, board experience, RMC, prior approval for change of management/control, KMP, independent directors, Audit Committee and NRC functions, CRO and CCO, compensation, whistle-blower, UL board competence and listing | Lists of Board-approved policies; each committee function; each fit-and-proper element in the annexes | CS |
| 3 | Know Your Customer (/361) | All NBFCs | CDD, risk categorisation, periodic updation, V-CIP, CKYC, reporting to FIU-IND, record keeping, sanctions screening | Each document list, each high-risk trigger, each reporting deadline | Compliance |
| 4 | Responsible Business Conduct (/362) | All NBFCs except HFCs | Fair practices, KFS, penal charges, recovery and agent conduct, grievance redressal, digital lending, gold/silver collateral conduct, microfinance conduct | KFS contents; each prohibited recovery practice; each digital lending requirement | Compliance |
| 5 | Income Recognition, Asset Classification and Provisioning (/356) | All NBFCs incl. HFCs | NPA recognition, upgrade, provisioning by category, SMA, standard asset provisioning, divergence | Each asset category; each provisioning rate (with layer differences) | CA |
| 6 | Prudential Norms on Capital Adequacy (/345) | ICC, Factor, deposit-taking, IFC, IDF and as specified | CRAR, Tier 1, CET1 for UL, risk weights, leverage for ML/UL, reporting | Each risk-weight category; each capital component and deduction | CA |
| 7 | Asset Liability Management (/355) | All NBFCs incl. HFCs | ALCO, structural liquidity, interest-rate sensitivity, LRM framework and LCR where applicable, tolerance limits, reporting | Each liquidity metric and bucket rule; LCR phase-in | CA / treasury |
| 8 | Credit Facilities (/347) | All NBFCs incl. HFCs | Loan policy, digital lending, gold/silver collateral, project finance, non-fund-based facilities, restrictions | Each restricted loan type; each digital-lending requirement; each LTV rule | Credit |
| 9 | Credit Risk Management (/350) | All NBFCs incl. HFCs | Credit risk policy, LEI, CERSAI, valuation, sanction controls | Each policy element | Risk |
| 10 | Concentration Risk Management (/351, updated 25 Aug 2026) | All NBFCs | Single/group exposure limits, large exposures framework for UL, sensitive sectors, capital market exposure | Each limit by layer and type | Risk / CA |
| 11 | Credit Information Reporting (/349) | All NBFCs incl. HFCs | Membership of all CICs, data submission frequency and formats, rectification, customer notification, grievance | Each reporting timeline; each data-quality obligation | Compliance |
| 12 | Managing Risks in Outsourcing (/363) | All NBFCs; BL exempt from Ch IV and IT parts of Ch II | Outsourcing policy, materiality, due diligence, contracts, IT outsourcing, group outsourcing, exit, incident reporting | Each mandatory contract clause; each prohibited outsourced function; IT outsourcing timeline for existing contracts | Compliance / IT |
| 13 | Financial Statements: Presentation and Disclosures (/359) | All NBFCs | Schedule disclosures, notes to accounts, specific disclosure formats | Each disclosure table | CA |
| 14 | Compliance Function (DoS /460) | NBFC-ML and NBFC-UL [VERIFY para] | CCO appointment and independence, compliance policy, compliance risk assessment, testing, reporting, tools | Each CCO condition; each element of the compliance policy; tooling requirements | Compliance |
| 15 | Cybersecurity, Technology: Risk, Resilience and Assurance Framework (DoS /461) | Layer-wise chapters | IT governance, cyber security, incident reporting (DAKSH within 6 hours), BCP/DR, VAPT, audit | Each control; each reporting timeline | IT / CISO |
| 16 | Digital Payment Security Controls (DoS /462) | NBFCs offering digital payment products | Payment security controls | Each control | IT |
| 17 | Fraud Risk Management (DoS /463) | All NBFCs | Fraud policy, early-warning signals, classification and reporting, staff accountability | Each EWS; each reporting deadline | Risk / Compliance |
| 18 | Internal Audit Function (DoS /464) | Per thresholds (RBIA scope) | RBIA, head of internal audit, independence, outsourcing limits, reporting | Each RBIA element; outsourcing bar for large NBFCs | Internal audit |
| 19 | Statutory Audit (DoS /465) | Per thresholds | Auditor appointment, eligibility, tenure, rotation, independence | Each eligibility condition | CA |
| 20 | Supervisory Returns (DoS /466) | All NBFCs per return | Return list, frequencies, portals, timelines, accuracy, sign-off | One row per return obligation (feeds P11) | Compliance / finance |
| 21 | Miscellaneous Supervisory Directions (DoS /467) | Per chapter | PCA framework, supervisory reporting items, other supervisory instructions | PCA thresholds and mandatory actions per Risk Threshold | Risk / CS |
| 22 | Auditor's Report (DoS /468) | All NBFCs | Matters to be reported by statutory auditors | One row per reportable matter | CA |
| 23 | Internal Ombudsman (CEPD 2026) | NBFCs within thresholds | IO appointment, tenure, escalation of partly-resolved or rejected complaints, reporting | Each IO function | Compliance |
| 24 | RB-IOS 2026 (NBFC version) | NBFCs covered by the scheme | Principal Nodal Officer, response timelines to the RBI Ombudsman, display requirements, compensation | Each RE obligation under the scheme | Compliance |
| 25 | Undertaking of Financial Services (/343) | NBFC-D, ICC, MFI, Factor, IDF, IFC, HFC (paras 7–12 from 1 Jan 2026) | Permitted business, investment in AIFs, insurance/agency business, other activities | Each permission condition | CS / Compliance |
| 26 | Classification, Valuation and Operation of Investment Portfolio (/354) | All NBFCs incl. HFCs | Investment policy, classification, valuation, transfers, AIF investment limits (with /343) | Each classification rule | CA / treasury |
| 27 | Securitisation Transactions (/353) | All NBFCs incl. HFCs | MRR, MHP, true sale, disclosures | Each originator condition | CA |
| 28 | Transfer and Distribution of Credit Risk (/352) | All NBFCs; Part B from 1 Jan 2026 | Transfer of loan exposures, co-lending | Each transferor/transferee condition; each co-lending requirement | Credit |
| 29 | Resolution of Stressed Assets (/357) | All NBFCs (HFCs specified paras) | Review period, ICA, RP implementation, compromise settlements, technical write-offs | Each timeline; each disincentive | Credit / legal |
| 30 | Treatment of Wilful Defaulters and Large Defaulters (/358) | All NBFCs incl. HFCs | Identification committee, review, reporting to CICs, consequences | Each procedural step | Legal |
| 31 | Prudential Norms on Declaration of Dividends (/360) | All NBFCs | Eligibility criteria, ceiling, reporting | Each criterion | CA |
| 32 | Acceptance of Public Deposits (/346) | Deposit-taking NBFCs | Ceilings, rating, interest, maturity, liquid assets, deposit insurance-like disclosures, returns | Each ceiling and return | CA / compliance |
| 33 | Credit Cards: Issuance and Conduct (/348) | NBFCs permitted to issue cards | Issuance, billing, closure, conduct | Each customer right | Compliance |
| 34 | Climate Finance and Management of Climate Change Risks (/364) | All NBFCs | Green deposits framework, climate risk management | Each framework element | Risk |
| 35 | Miscellaneous (/373, updated 26 Feb 2026) | As specified per chapter | Residual instructions | Each chapter | Compliance |
| 36 | Acquisition of Shareholding or Control (/340) | All NBFCs incl. HFCs | Prior approval triggers, application, public notice | Each trigger | CS |
| 37 | Branch Authorisation (/342) | All NBFCs incl. HFCs | Branch opening and closure intimations | Each intimation | CS |
| 38 | Voluntary Amalgamation (/341) | All NBFCs | Approval process | Each step | CS |
| 39–46 | Type-specific: HFC (/365), MFI (/371), CIC (/367), P2P (/370), AA (/368), MGC (/369), NOFHC (/372), SPD (/366) | The type only | Everything in the type direction; cross-check which common NBFC directions also apply (the type direction usually says) | Type-specific prudential ratios and business limits | CA / Compliance |

---

## AB.13 Worked example: an amendment reaches a tenant *(v1.1)*

1. **20:00 IST scan.** P05 sees that the RBI NBFC page now shows "Reserve Bank of India (Non-Banking Financial Companies – Concentration Risk Management) Directions, 2025 (Updated as on August 25, 2026)", where the previous scan showed no update date.
2. **Fetch and version.** The updated PDF is fetched, hashed and stored as `RBI.NBFC.CONC` version 2, `valid_from` = the effective date stated in the amending instrument (the analyst confirms it); the amending notification is linked.
3. **Diff and summary.** Clause diff shows two paragraphs substituted and one inserted. Vidhi drafts a three-line summary with paragraph citations, labelled "Unreviewed".
4. **Impact.** Seven NBFC checkpoints link to the changed paragraphs; three are modified, one new checkpoint is needed, none retired. Siblings: the UCB and RCB concentration directions were not updated on that date, so no sibling proposals. 212 tenants hold the instrument; 31 have overlays on the modified checkpoints.
5. **Release.** The content maker edits the three checkpoints and adds the new one; the checker approves; the publisher releases on the next business day; catalogue row updated (column K "25 Aug 2026"; Part-2 file `RBI-NBFC - Concentration Risk Management - Compliance Questions v2.xlsx`).
6. **Tenant Update (20:30 IST digest and immediate e-mail for P1 directions).** "What changed: limits on … now … (para …). Why it matters to you: you are an NBFC-ML ICC with exposures to … What to do: (1) review the exposure policy (owner: CRO), (2) re-test the limit monitoring report (owner: Risk), (3) note for the next Risk Management Committee." Old vs new actionable table; 3 overlay conflicts sent to the tenant's content owner; future compliance instances move to v2 from the effective date; completed instances stay on v1.
7. **Audit trail.** Every step is in the ledger: detection, version, diff, review, release, tenant acknowledgement and each tenant action (NN-02).

---

## AB.14 Clone map: which subjects exist in which category *(v1.1)*

Generated from the RBI category pages on 25 October 2026. A tick means RBI issued a direction on that subject for that category; for the licensing/type-specific row the number is the count of such instruments. Use this map to plan clone-and-adapt (AB.7.4): a subject with ticks in many columns is written once for the lead category of its wave and cloned.

| Subject (DoR set A) | NBFC | UCB | RCB | CB | SFB | PB | LAB | RRB | AIFI | ARC | CIC-CI |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Know Your Customer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Miscellaneous | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Managing Risks in Outsourcing | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ |
| Responsible Business Conduct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Financial Statements: Presentation and Disclosures | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Treatment of Wilful Defaulters and Large Defaulters | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — |
| Asset Liability Management | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Classification, Valuation and Operation of Investment Portfolio | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Credit Information Reporting | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — |
| Prudential Norms on Capital Adequacy | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Resolution of Stressed Assets | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Income Recognition, Asset Classification and Provisioning | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Transfer and Distribution of Credit Risk | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Concentration Risk Management | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Credit Risk Management | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Cards: Issuance and Conduct | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Credit Facilities | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — |
| Governance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Undertaking of Financial Services | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — |
| Branch Authorisation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Voluntary Amalgamation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Interest Rate on Deposits | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Cash Reserve Ratio and Statutory Liquidity Ratio | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Digital Banking Channels Authorisation | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Licensing / principal / type-specific direction(s) | 8 | 1 | — | 2 | 1 | — | — | — | — | 1 | 1 |
| Interest Rates on Advances | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — |
| Acquisition of Shares / Control | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Securitisation Transactions | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | — | — |
| Climate Finance and Management of Climate Change Risks | ✓ | — | — | ✓ | ✓ | — | — | — | — | — | — |
| Prudential Norms on Declaration of Dividend(s) | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — |
| Resource Raising Norms | — | — | — | ✓ | ✓ | — | — | — | ✓ | — | — |
| Acceptance of Public Deposits | ✓ | — | — | — | — | — | — | — | — | — | — |
| Registration, Exemptions and Framework for Scale Based Regulation | ✓ | — | — | — | — | — | — | — | — | — | — |
| Forthcoming Instructions | — | — | — | ✓ | — | — | — | — | — | — | — |

| Subject (DoS set C, 31 Jul 2026) | NBFC | UCB | RCB | CB | SFB | PB | LAB | RRB | AIFI | ARC | CIC-CI |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Miscellaneous Supervisory | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Fraud Risk Management | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Supervisory Returns | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — |
| Cybersecurity, Technology: Risk, Resilience and Assurance Framework | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ |
| Statutory Audit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Compliance Function | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Internal Audit Function | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Digital Payment Security Controls | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | — |
| Concurrent Audit | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — |
| Auditor's Report | ✓ | — | — | — | — | — | — | — | — | — | — |

Note: the dividend row shows only the 2025 directions still live; commercial banks, SFBs, payments banks, LABs and RRBs have 2026 dividend directions (set B), and AIFIs, ARCs and credit information companies have none.

Reading the map: (1) KYC, Responsible Business Conduct, IRACP, Investment Portfolio, Credit Information Reporting, Wilful Defaulters and Resolution of Stressed Assets exist almost everywhere — highest clone value. (2) CRR/SLR, Interest Rate on Deposits, Interest Rates on Advances and Digital Banking Channels Authorisation are bank and co-op-bank subjects with no NBFC lead — write them first for UCBs in Wave 2 and clone to banks in Wave 3. (3) Securitisation exists for NBFCs, AIFIs, commercial banks and SFBs only. (4) DoS directions are thinner for RRBs (2) and RCBs (3), whose supervision sits largely with NABARD.

---

## AB.15 Sources (accessed 25 October 2026)

- RBI, Master Directions by department and RE category: https://rbi.org.in/Scripts/BS_ViewMasterDirections.aspx (category pages `?did=403`–`413`, `419`–`429`, `338`).
- RBI, Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025, RBI/DOR/2025-26/344 (page id 12960): https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12960
- RBI circular RBI/2025-26/100, DOR.RRC.REC.302/33-01-010/2025-26, "Consolidation of Regulations – Withdrawal of circulars", 28 November 2025: https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13170
- RBI, Draft Directions (RE-wise) and lists of circulars to be repealed: https://rbi.org.in/Scripts/BS_ViewREwiseDraftDirections.aspx?id=197
- RBI press release, Reserve Bank – Integrated Ombudsman Scheme, 2026: https://website.rbi.org.in/web/rbi/-/press-releases/rbi-issues-reserve-bank-integrated-ombudsman-scheme-2026
- Secondary (hints only): Vinod Kothari Consultants, "RBI Master Directions 2025 — Comprehensive Regulatory Consolidation" (Dec 2025): https://vinodkothari.com/wp-content/uploads/2025/12/RBI-Master-Directions-2025_-Comprehensive-Regulatory-Consolidation-1.pdf ; A2I Legal, RBI Master Directions for NBFCs 2025: https://resource.a2ilegal.com/rbi-master-directions-for-nbfcs-2025/ ; Business Today (28 Nov 2025) reporting 244 directions: https://www.businesstoday.in/amp/latest/economy/story/rbi-consolidates-9000-circulars-into-244-master-directions-for-enhanced-ease-of-doing-business-details-here-504215-2025-11-28 ; TaxScan reporting 238: https://www.taxscan.in/top-stories/rbi-issues-238-consolidated-master-directions-9000-circulars-guidelines-reorganised-1439158
