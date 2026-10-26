# Appendix F — Regulatory Source Register and Monitoring Catalogue

> Binding for P05 (source monitor) and P03 (authority registry). Seed data for `chg.sources` and `cnt.authorities`. Prepared 25 October 2026. URLs marked **[VERIFY]** were not opened during preparation or were observed to redirect; the build team test-fetches every source in P05 sprint 1 and records the result in `chg.fetch_runs`. Changing this register in production is a Governed change (P02).

**v1.1 changes (25 October 2026)**

- §F.2 wording corrected: 238 directions (press release) / 244 serials /143–/386 (RBI/2025-26/100) / 240 live on the category pages; credit information companies abbreviated CIC-CI.
- New §F.2A: the 22 RBI Master Direction category pages (DoR did=403–413, DoS did=419–429) and CEPD (did=338) as sources SRC-RBI-30 to SRC-RBI-52, plus RBI/2025-26/100 as SRC-RBI-53, with the "Updated as on" parser rule and catalogue join (D-39, Appendix AB §AB.8.1).
- New §F.2B: withdrawn and historic references kept for concordance only (NN-55; G5 E-08).
- New §F.7A: AI-governance sources for the AI-GOV family (D-36).
- §F.12 rewritten: foreign regulator sources for the priority jurisdictions (UAE mainland, DIFC, ADGM; Singapore; UK; EU; US federal and states), lifecycle gate PUBLISHED (D-45) replacing "LIVE", local-time schedules, official-language rule (NN-54).
- New §F.12B: licensed feeds through `REG_INTEL_PORT` (signals only; LDC-CHG-121).
- §F.1 adds API and LICENSED methods and local-time schedules; §F.14 adds row-set hashing (faster sweeps), back-fill and official-language handling; §F.16 adds parser profiles; §F.17 adds catalogue-drift and foreign-lag KPIs; §F.18 adds sources.

## F.1 How to read this register

| Field | Meaning |
|---|---|
| Source ID | `SRC-<AUTH>-<NN>`; stable; used in `chg.sources.source_id` |
| Method | RSS · LIST (HTML listing with parser profile) · PAGE (single page change detection) · PDF (follow links to PDFs) · GAZ (e-Gazette search) · MAIL (regulator e-mail alert to monitored mailbox) · NEWS (licensed feed, flag OFF) · *(v1.1)* API (official JSON/XML API, e.g., US Federal Register) · LICENSED (`REG_INTEL_PORT` provider, flag OFF, signals only) |
| Priority | P1 core regulators (affect most tenants, frequent) · P2 ministries and standard-setters · P3 state departments, low-frequency or redundant sources |
| Schedule | INTRA (every 30 min 09:00–21:00 IST, hourly otherwise) · EVE (daily 20:00 IST reconciliation — every source is included in EVE regardless of class) · WEEK (Sunday 03:00 IST deep crawl) |
| SLA | Maximum time between successful scans before a P2 alert |
| Local schedules *(v1.1)* | INTRA-L, EVE-L, WEEK-L: the same cadences anchored to the authority's own time zone (EVE-L = 20:00 local). Used for foreign sources; results reach the content Radar at the next IST working window |
| Lifecycle *(v1.1)* | Foreign sources run only while their jurisdiction pack is PILOT or PUBLISHED (D-45); DRAFT packs are scanned weekly for build purposes only |
| Families | Appendix E template families most affected |

## F.2 Reserve Bank of India (RBI)

RBI's main site navigation (verified 25-Oct-2026) groups regulatory content under Notifications, Press Releases and Regulatory Reporting. On 28-Nov-2025 RBI issued function-wise consolidated Master Directions for 11 RE categories (commercial banks, small finance banks, payments banks, local area banks, regional rural banks, UCBs, rural co-operative banks, AIFIs, NBFCs, ARCs, credit information companies (CIC-CI)). *(v1.1 corrected)* The press release speaks of 238 directions; circular RBI/2025-26/100 lists 244 serials (/143 to /386); 240 are live on the category pages; together they withdrew about 9,445 circulars [VERIFY count]. The LawDocsComply catalogue holds 320 rows: these directions plus later DoR directions (9), the DoS set of 31 Jul 2026 (64) and CEPD (6+1) (D-39; Appendix AB); later changes arrive as Amendment Directions and "updated as on" consolidations. The Master Directions page groups by RE category under date headings; direction pages follow `BS_ViewMasDirections.aspx?id=<n>`; PDFs follow `https://rbidocs.rbi.org.in/rdocs/notification/PDFs/<n><code>.PDF`. A newer site (`website.rbi.org.in`) offered notification preferences but its URLs redirected (302) to `rbi.org.in` on 25-Oct-2026 [VERIFY canonical site at build].

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-RBI-01 | RSS | https://www.rbi.org.in/Scripts/rss.aspx | RSS | P1 / INTRA / 2 h | Confirm feed scope (notifications, press releases) [VERIFY]; GUID de-dup | all RBI |
| SRC-RBI-02 | Notifications | https://www.rbi.org.in/Scripts/NotificationUser.aspx | LIST + PDF | P1 / INTRA / 2 h | Date headings; title; reference no. (`RBI/YYYY-YY/NNN`, department ref); addressee line in PDF | all RBI |
| SRC-RBI-03 | Master Directions | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx | LIST + PDF | P1 / INTRA / 2 h | Group by RE category; "Updated as on" parsed from title → new instrument version | RBI-SCB, RBI-UCB, RBI-RCB, RBI-NBFC, RBI-ARC, RBI-OTH |
| SRC-RBI-04 | Amendment Directions | https://www.rbi.org.in/Scripts/Fs_AmendmentDirections.aspx | LIST + PDF | P1 / INTRA / 2 h | Amendment instructions parsed (P05 FR-P05-41) | all RBI |
| SRC-RBI-05 | Master Circulars | https://www.rbi.org.in/Scripts/BS_ViewMasterCirculardetails.aspx | LIST | P2 / EVE / 24 h | Residual master circulars (non-DoR departments) | all RBI |
| SRC-RBI-06 | Draft Directions (RE-wise) | https://www.rbi.org.in/Scripts/BS_ViewREwiseDraftDirections.aspx | LIST | P1 / INTRA / 6 h | Class CONSULTATION_DRAFT; comment deadline | all RBI |
| SRC-RBI-07 | Draft Notifications/Guidelines | https://www.rbi.org.in/Scripts/DraftNotificationsGuildelines.aspx | LIST | P1 / EVE / 24 h | Consultation horizon | all RBI |
| SRC-RBI-08 | Circulars Withdrawn | https://www.rbi.org.in/Scripts/NotificationUserWithdrawnCircular.aspx | LIST | P1 / EVE / 24 h | REPEAL_WITHDRAWAL; link to instruments | all RBI |
| SRC-RBI-09 | Standalone circulars | https://www.rbi.org.in/Scripts/BS_ViewListofstandalonecirculars.aspx | LIST | P2 / EVE / 24 h | Post-consolidation standalone instructions | all RBI |
| SRC-RBI-10 | Index to RBI Circulars | https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx | LIST | P3 / WEEK / 7 d | Reconciliation only | all RBI |
| SRC-RBI-11 | Press Releases | https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx | LIST | P1 / INTRA / 2 h | Classes: ENFORCEMENT_PENALTY (monetary penalties on REs), REGISTRATION_CANCELLATION (NBFC CoR cancellations), PRESS_RELEASE_INFO | all RBI |
| SRC-RBI-12 | What's New | https://www.rbi.org.in/scripts/NewLinkDetails.aspx | LIST | P1 / INTRA / 2 h | Catch-all redundancy | all RBI |
| SRC-RBI-13 | List of Returns | https://www.rbi.org.in/scripts/BS_Listofallreturns.aspx | PAGE | P1 / EVE / 24 h | Change detection on return list → P11 return definitions | RBI-* (returns) |
| SRC-RBI-14 | Data Definition | https://www.rbi.org.in/scripts/DataDefinition.aspx | PAGE | P2 / EVE / 24 h | → P11 | RBI-* |
| SRC-RBI-15 | Validation rules / Taxonomy | https://www.rbi.org.in/scripts/ValidationRules.aspx | PAGE + files | P1 / EVE / 24 h | XBRL taxonomy versions → P11 | RBI-* |
| SRC-RBI-16 | Reporting portals | https://www.rbi.org.in/scripts/ReportingPlaform.aspx | PAGE | P2 / WEEK / 7 d | CIMS, DAKSH, PRAVAAH details → P11 | RBI-* |
| SRC-RBI-17 | Reporting FAQs | https://www.rbi.org.in/scripts/ReportingFAQ.aspx | PAGE | P2 / WEEK / 7 d | FAQ_CLARIFICATION | RBI-* |
| SRC-RBI-18 | FAQs | https://www.rbi.org.in/Scripts/FAQDisplay.aspx | LIST | P2 / EVE / 24 h | FAQ_CLARIFICATION | all RBI |
| SRC-RBI-19 | Holiday matrix (NI Act holidays by state) | https://www.rbi.org.in/Scripts/HolidayMatrixDisplay.aspx [VERIFY] | PAGE | P2 / WEEK / 7 d | → `cnt.holiday_calendars` IN-RBI-<state> | — |
| SRC-RBI-20 | New website notifications | https://website.rbi.org.in/ [VERIFY] | LIST | P2 / EVE / 24 h | Monitor while canonical status unclear | all RBI |
| SRC-RBI-21 | Integrated Ombudsman / CEPD | https://cms.rbi.org.in/ [VERIFY] | PAGE | P2 / WEEK / 7 d | Scheme changes → P14. *(v1.1)* CEPD directions themselves are monitored by SRC-RBI-52 | RBI-* |
| SRC-RBI-22 | RBI e-mail notification preferences | (subscription) | MAIL | P3 / — | Redundancy | all RBI |

## F.2A RBI Master Directions category pages *(v1.1)*

RBI updates consolidated directions **in place**, so the category pages are the primary change signal (Appendix AB §AB.8.1; P05 FR-P05-04). One source per page; the base URL is `https://rbi.org.in/Scripts/BS_ViewMasterDirections.aspx?did=<id>`. Every source: method LIST + PDF; priority P1; schedule EVE (20:00 IST) plus a light intraday check every 2 h from 09:00 to 21:00 IST; SLA 24 h.

| Source ID | Department | Category | did | Catalogue `source_set` | Families |
|---|---|---|---|---|---|
| SRC-RBI-30 | DoR | Commercial Banks | 403 | A (and B for later DoR directions) | RBI-SCB |
| SRC-RBI-31 | DoR | Small Finance Banks | 404 | A (and B for later DoR directions) | RBI-SCB |
| SRC-RBI-32 | DoR | Payments Banks | 405 | A (and B for later DoR directions) | RBI-SCB |
| SRC-RBI-33 | DoR | Local Area Banks | 406 | A (and B for later DoR directions) | RBI-SCB |
| SRC-RBI-34 | DoR | Regional Rural Banks | 407 | A (and B for later DoR directions) | RBI-SCB |
| SRC-RBI-35 | DoR | Urban Co-operative Banks | 408 | A (and B for later DoR directions) | RBI-UCB |
| SRC-RBI-36 | DoR | Rural Co-operative Banks | 409 | A (and B for later DoR directions) | RBI-RCB |
| SRC-RBI-37 | DoR | All India Financial Institutions | 410 | A (and B for later DoR directions) | RBI-OTH |
| SRC-RBI-38 | DoR | NBFCs | 411 | A (and B for later DoR directions) | RBI-NBFC |
| SRC-RBI-39 | DoR | Asset Reconstruction Companies | 412 | A (and B for later DoR directions) | RBI-ARC |
| SRC-RBI-40 | DoR | Credit Information Companies (CIC-CI) | 413 | A (and B for later DoR directions) | RBI-OTH |
| SRC-RBI-41 | DoS | Commercial Banks | 419 | C | RBI-SCB |
| SRC-RBI-42 | DoS | Small Finance Banks | 420 | C | RBI-SCB |
| SRC-RBI-43 | DoS | Payments Banks | 421 | C | RBI-SCB |
| SRC-RBI-44 | DoS | Local Area Banks | 422 | C | RBI-SCB |
| SRC-RBI-45 | DoS | Regional Rural Banks | 423 | C | RBI-SCB |
| SRC-RBI-46 | DoS | Urban Co-operative Banks | 424 | C | RBI-UCB |
| SRC-RBI-47 | DoS | Rural Co-operative Banks | 425 | C | RBI-RCB |
| SRC-RBI-48 | DoS | All India Financial Institutions | 426 | C | RBI-OTH |
| SRC-RBI-49 | DoS | NBFCs | 427 | C | RBI-NBFC |
| SRC-RBI-50 | DoS | Asset Reconstruction Companies | 428 | C | RBI-ARC |
| SRC-RBI-51 | DoS | Credit Information Companies (CIC-CI) | 429 | C | RBI-OTH |
| SRC-RBI-52 | CEPD | Consumer Education and Protection (Integrated Ombudsman and related directions) | 338 | D | all RBI |
| SRC-RBI-53 | DoR | Circular RBI/2025-26/100 of 28 Nov 2025 (consolidation; annex of withdrawn circulars) [VERIFY URL] | — (PAGE + PDF; P2 / WEEK / 7 d) | concordance seed | all RBI |

**Parser rule (all SRC-RBI-30 to 52).** For each row capture: title, item id (`BS_ViewMasDirections.aspx?id=<n>`), reference (`RBI/<dept>/<yyyy-yy>/<nnn>`), date of issue and the "Updated as on" date. Then:

1. **Join** the row to the catalogue (`catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`) on item id, falling back to reference and normalised title. The same direction appearing on several category pages is one instrument with several category links (siblings, D-40).
2. **Changed "Updated as on" date** → CONSOLIDATION_UPDATE change item; fetch and hash the consolidated PDF; new instrument version with `valid_from` = the amendment's effective date (NN-07); link the amendment notification found by SRC-RBI-02/04.
3. **New row** → NEW_INSTRUMENT change item, catalogue row and instrument created automatically (coverage `PLANNED`; Appendix AB §AB.8.3).
4. **Missing row** → "possibly superseded" flag for analyst review; never an automatic repeal (P05 FR-P05-48).
5. **Speed.** The page's row set is hashed; when the hash is unchanged nothing else is parsed. Only new or changed rows trigger a PDF fetch. Target: all 23 pages swept in ≤ 2 minutes at EVE.
6. **Reconciliation.** Weekly, the catalogue is compared with the pages; any difference (count, title, date) is a catalogue-drift exception on the content Radar (§F.17).

## F.2B Withdrawn and historic references *(v1.1)*

Circulars withdrawn by RBI/2025-26/100 (SRC-RBI-53) and by later withdrawal notices (SRC-RBI-08) are loaded as instruments of type WITHDRAWN_CIRCULAR with `valid_to` = the withdrawal date. They exist only for the concordance (old circular → new paragraph; P05 FR-P05-42) and for history; no checkpoint may cite them as current authority (NN-55; LDC-TPL-043). Example: the UCB categorisation circular RBI/2022-23/144 relied on by the v1.0 baseline is marked **historic**; UCB content is seeded from the 2025 consolidated UCB directions mapped in Appendix AB (G5 E-08).

## F.3 Securities and Exchange Board of India (SEBI)

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-SEBI-01 | RSS (press releases, circulars, orders) | https://www.sebi.gov.in/sebirss.xml | RSS | P1 / INTRA / 2 h | Verified via https://www.sebi.gov.in/rss.html | SEBI-* |
| SRC-SEBI-02 | Circulars | https://www.sebi.gov.in/legal/circulars | LIST | P1 / INTRA / 2 h | Page URL pattern `/legal/circulars/<mon-yyyy>/<slug>_<id>.html` (observed); ref `SEBI/HO/…/P/CIR/YYYY/NNN` | SEBI-* |
| SRC-SEBI-03 | Master circulars | https://www.sebi.gov.in/legal/master-circulars | LIST | P1 / INTRA / 6 h | e.g., LODR master circular (Jan-2026, id 99432) supersedes earlier ones → new instrument version | SEBI-* |
| SRC-SEBI-04 | Regulations | https://www.sebi.gov.in/legal/regulations [VERIFY] | LIST | P1 / EVE / 24 h | Amendment regulations; consolidated "last amended on" | SEBI-* |
| SRC-SEBI-05 | Rules / Acts / Gazette notifications | https://www.sebi.gov.in/legal/rules · /acts · /gazette-notification [VERIFY] | LIST | P2 / EVE / 24 h | | SEBI-* |
| SRC-SEBI-06 | Consultation papers | https://www.sebi.gov.in/reports-and-statistics/reports [VERIFY consultation listing] | LIST | P1 / EVE / 24 h | CONSULTATION_DRAFT; comment deadline | SEBI-* |
| SRC-SEBI-07 | Orders (adjudication, settlement) | via RSS + https://www.sebi.gov.in/enforcement/orders [VERIFY] | LIST | P2 / EVE / 24 h | ENFORCEMENT_PENALTY | SEBI-* |
| SRC-SEBI-08 | FAQs | https://www.sebi.gov.in/sebiweb/home/... [VERIFY] | PAGE | P3 / WEEK / 7 d | | SEBI-* |
| SRC-SEBI-09 | Stock exchange circulars affecting listed entities (NSE, BSE compliance circulars) | NSE/BSE circular pages [VERIFY] | LIST | P2 / EVE / 24 h | Listed-company operational requirements (e.g., XBRL filing formats) | SEBI-LISTED |
| SRC-SEBI-10 | Trading holidays (NSE/BSE) | NSE/BSE holiday pages [VERIFY] | PAGE | P2 / WEEK / 7 d | → `IN-NSE` calendar | SEBI-* |

## F.4 International Financial Services Centres Authority (IFSCA)

IFSCA publishes a consolidated "New Section" table (Date, Type, Title) with types Regulation, Circular, Guidelines, Notification, FAQs, AML Compliance, Public Consultation, Public Comments, Press Release, Bulletin, Research, Committee Report, Informal Guidance, DRHP/RHP; URL patterns `/Legal/Index?MId=…`, `/ReportPublication/Index?MId=…`, `/PressRelease/Index?MId=…`; some `MId` tokens contain stray spaces (encode carefully); **no RSS** observed. The owner's automation environment previously found `ifsca.gov.in` blocked by an egress allowlist (Sep-2026) — production egress must allow it.

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-IFSCA-01 | New Section | https://ifsca.gov.in/Home/NewSection | LIST | P1 / INTRA / 2 h | Type column → class map (Regulation/Circular/Guidelines/Notification → NEW or AMENDMENT; FAQs → FAQ; Public Consultation → CONSULTATION_DRAFT; Informal Guidance → FAQ_CLARIFICATION; DRHP/RHP, Career, Tender → NON_ACTIONABLE) | IFSCA-* |
| SRC-IFSCA-02 | Legal framework (Acts, Regulations, Circulars, Guidelines, Notifications, Directions, Handbooks) | https://ifsca.gov.in/Legal/Index/… (category tokens) [VERIFY each] | LIST | P1 / EVE / 24 h | Consolidated regulations "as amended up to <date>" (e.g., Fund Management Regulations 2025 as amended up to 10-Sep-2026) → instrument versions | IFSCA-* |
| SRC-IFSCA-03 | AML Compliance | IFSCA AML section [VERIFY] | LIST | P1 / EVE / 24 h | Master Guidelines "as on" dates (e.g., AML/CFT/KYC Master Guidelines as on 03-Aug-2026) | IFSCA-* (cross-cutting) |
| SRC-IFSCA-04 | Press releases | https://ifsca.gov.in/PressRelease/Index | LIST | P2 / EVE / 24 h | Enforcement, registrations | IFSCA-* |
| SRC-IFSCA-05 | Consultation papers | https://ifsca.gov.in/ReportPublication/Index | LIST | P1 / EVE / 24 h | CONSULTATION_DRAFT | IFSCA-* |
| SRC-IFSCA-06 | IFSC holidays | IFSCA / GIFT City notices [VERIFY] | PAGE | P3 / WEEK / 7 d | → `IN-IFSC` calendar | — |

## F.5 Insurance Regulatory and Development Authority of India (IRDAI)

Circular listings with IRDAI reference numbers (e.g., `IRDAI/PPGR/Cir/Misc/97/06/2024`) were observed on `policyholder.gov.in` (an IRDAI-owned site), which also offers e-mail alert registration; `irdai.gov.in` remains the expected primary domain [VERIFY canonical document pages for Regulations, Circulars, Master Circulars, Guidelines, Notifications, Exposure Drafts]. IRDAI has warned of fraudulent look-alike portals — the fetcher pins exact hostnames and TLS certificates' issuer expectations.

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-IRDAI-01 | Regulations | https://irdai.gov.in/ (Regulations listing) [VERIFY] | LIST | P1 / INTRA / 6 h | "IRDAI (…) Regulations, 2024" style consolidations and master circulars | IRDAI-INS, IRDAI-INT |
| SRC-IRDAI-02 | Circulars / Master circulars | https://policyholder.gov.in/web/guest/circulars ; irdai.gov.in circulars [VERIFY] | LIST | P1 / INTRA / 6 h | Department filter not available; parse reference code for department (e.g., PPGR, Life, Non-Life, Health, F&A, Actuarial, Intermediaries) | IRDAI-* |
| SRC-IRDAI-03 | Notifications / Gazette | irdai.gov.in [VERIFY] + e-Gazette | LIST/GAZ | P1 / EVE / 24 h | | IRDAI-* |
| SRC-IRDAI-04 | Exposure drafts | irdai.gov.in [VERIFY] | LIST | P1 / EVE / 24 h | CONSULTATION_DRAFT | IRDAI-* |
| SRC-IRDAI-05 | What's new | https://policyholder.gov.in/web/guest/whats-new1 | LIST | P2 / EVE / 24 h | Redundancy | IRDAI-* |
| SRC-IRDAI-06 | E-mail alerts | https://policyholder.gov.in/web/guest/register-for-email-alerts | MAIL | P3 / — | Redundancy | IRDAI-* |

## F.6 Ministry of Corporate Affairs (MCA) and Registrar of Companies

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-MCA-01 | Notifications (Acts & Rules) | https://www.mca.gov.in/ (Acts & Rules › Notifications) [VERIFY V3 path] | LIST + PDF | P1 / INTRA / 6 h | G.S.R./S.O. numbers; rules amendments (e.g., Companies (Accounts) Rules) | MCA-CO, MCA-LLP, all |
| SRC-MCA-02 | General Circulars | MCA circulars listing [VERIFY] | LIST | P1 / INTRA / 6 h | DUE_DATE_EXTENSION (fee relaxations, filing extensions) frequent | MCA-* |
| SRC-MCA-03 | Comments invited / draft rules | https://www.mca.gov.in/MinistryV2/commentsinvitedarchive.html (legacy) [VERIFY current] | LIST | P2 / EVE / 24 h | CONSULTATION_DRAFT | MCA-* |
| SRC-MCA-04 | MCA21 V3 e-form changes / form versions | MCA V3 "What's new" [VERIFY] | PAGE | P1 / EVE / 24 h | Form revisions → P06 filing catalogue | MCA-* |
| SRC-MCA-05 | e-Gazette (Ministry of Corporate Affairs) | https://egazette.gov.in/ | GAZ | P2 / EVE / 24 h | Search by ministry and date | MCA-* |
| SRC-MCA-06 | IEPF Authority notices | iepf.gov.in [VERIFY] | LIST | P3 / WEEK / 7 d | Unclaimed dividend/share transfer obligations | MCA-CO, SEBI-LISTED |

## F.7 Ministry of Electronics and IT (MeitY), CERT-In, Data Protection Board

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-MEITY-01 | DPDP Act/Rules and notifications (DPDP Rules 2025 notified 13/14-Nov-2025, phased commencement) | https://www.meity.gov.in/ (Data Protection framework) [VERIFY path] | LIST + PDF | P1 / INTRA / 6 h | Commencement notifications per phase → instrument status PARTIALLY_IN_FORCE | DATA-PRIV, all |
| SRC-MEITY-02 | IT Act rules, intermediary rules, SPDI rules amendments | meity.gov.in content [VERIFY] | LIST | P1 / EVE / 24 h | | DATA-PRIV, CYBER |
| SRC-MEITY-03 | Data Protection Board of India (notices, procedures, consent manager registrations) | DPB site [VERIFY URL once live] | LIST | P1 / EVE / 24 h | | DATA-PRIV |
| SRC-CERTIN-01 | Directions and advisories (e.g., Directions No. 20(3)/2022-CERT-In of 28-Apr-2022) | https://www.cert-in.org.in/ (Directions, Advisories, Vulnerability Notes) [VERIFY paths] | LIST | P1 / INTRA / 6 h | Advisories: class INFO_ONLY unless directions; incident-reporting changes → ACTIONABLE | CYBER, all |
| SRC-MEITY-04 | e-Gazette (MeitY) | https://egazette.gov.in/ | GAZ | P2 / EVE / 24 h | | DATA-PRIV, CYBER |

## F.7A AI governance sources (family AI-GOV) *(v1.1)*

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-AI-01 | RBI FREE-AI Committee Report (13 Aug 2025) and follow-up directions | https://rbi.org.in (report page) [VERIFY] | PAGE + PDF | P2 / WEEK / 7 d | Recommendations are suggestive until directions issue; a direction is detected by SRC-RBI-02/06 | AI-GOV |
| SRC-AI-02 | RBI draft Model Risk Management guidance (2026) | via SRC-RBI-06 / SRC-RBI-07 | LIST | P1 / EVE / 24 h | Class CONSULTATION_DRAFT until final | AI-GOV, RBI-* |
| SRC-AI-03 | MeitY India AI Governance Guidelines and IndiaAI notices | https://www.meity.gov.in ; https://indiaai.gov.in [VERIFY paths] | LIST | P2 / EVE / 24 h | Guidelines = INFO / suggestive | AI-GOV |
| SRC-AI-04 | SEBI AI/ML guidance (consultation 20 Jun 2025 and any circular) | via SRC-SEBI sources | LIST | P1 / INTRA / 6 h | Keyword rule: "artificial intelligence", "AI/ML" | AI-GOV, SEBI-* |
| SRC-AI-05 | EU AI Office (guidelines, codes of practice, Digital Omnibus on AI) | https://digital-strategy.ec.europa.eu/en/policies/ai-office [VERIFY] | LIST | P2 / EVE-L / 24 h | Legal acts themselves come from SRC-EU-01 / SRC-EU-07 | AI-GOV, INTL-GEN |
| SRC-AI-06 | ISO/IEC JTC 1/SC 42 standards catalogue (42001, 23894, 42005) | https://www.iso.org/committee/6794475.html [VERIFY] | PAGE | P3 / WEEK / 7 d | Catalogue metadata only; standard text is licensed and never copied | AI-GOV |
| SRC-AI-07 | NIST AI RMF and profiles | https://www.nist.gov/itl/ai-risk-management-framework | PAGE | P3 / WEEK / 7 d | | AI-GOV |
| SRC-AI-08 | IMDA Singapore Model AI Governance Frameworks (incl. Agentic AI, Jan 2026) | https://www.imda.gov.sg [VERIFY path] | PAGE | P3 / WEEK-L / 7 d | | AI-GOV |

## F.8 Ministry of Labour and Employment (MoLE) and State Labour Departments

The four Labour Codes (Code on Wages 2019, Industrial Relations Code 2020, Code on Social Security 2020, Occupational Safety, Health and Working Conditions Code 2020) were brought into force with effect from 21-Nov-2025; draft central rules followed in Dec-2025 and final central rules and appropriate authorities were notified around May-2026 (L&E Global, 28-May-2026; KPMG flash news) [VERIFY exact notification numbers in Appendix T]. States notify their own rules progressively.

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-MOLE-01 | Labour Codes, rules, notifications, FAQs | https://labour.gov.in/ (Labour Codes section) [VERIFY path] | LIST + PDF | P1 / INTRA / 6 h | Section-wise commencement; rules; forms/registers → Appendix T | LAB |
| SRC-MOLE-02 | EPFO circulars | https://www.epfindia.gov.in/ (circulars) [VERIFY] | LIST | P1 / EVE / 24 h | Contribution rates, due dates, ECR changes | LAB, TAX |
| SRC-MOLE-03 | ESIC circulars | https://www.esic.gov.in/ (circulars) [VERIFY] | LIST | P1 / EVE / 24 h | | LAB |
| SRC-MOLE-04 | Shram Suvidha / unified returns portal notices | [VERIFY] | PAGE | P2 / WEEK / 7 d | Unified returns under codes | LAB |
| SRC-STLAB-xx | State labour departments (priority: Delhi, Uttar Pradesh, Rajasthan, Maharashtra, Karnataka, Gujarat, Tamil Nadu, Telangana, Haryana, West Bengal) | per state [VERIFY each] | LIST | P2 / EVE / 24 h for priority states; P3 / WEEK for others | State rules under the codes, Shops & Establishments Acts, Professional Tax, Labour Welfare Fund, holidays; many in regional language → OCR + translation (P07) | LAB, TAX |
| SRC-MOLE-05 | Ministry of Women & Child Development (POSH Act; SHe-Box) | https://wcd.gov.in/ [VERIFY] | LIST | P2 / WEEK / 7 d | POSH changes | LAB |

## F.9 Co-operative societies

The Central Registrar of Co-operative Societies (CRCS) lists circulars at `https://crcs.gov.in/circulars` (S No, Subject, Issued Date; PDFs at `/public/uploads/circulars/Cir_<category>_<id>_<name>.pdf`); on 25-Oct-2026 the newest listed circular was dated 23-Sep-2022 although the page footer showed an update on 29-Sep-2026 — treat as low-frequency and monitor the Ministry of Cooperation in parallel. The CRCS "State Registrar" page lists every state/UT registrar with postal address and e-mail (no URLs); state websites below are seeded from the build team's verification in P05 sprint 1.

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-COOP-01 | CRCS circulars / orders / notifications | https://crcs.gov.in/circulars | LIST + PDF | P2 / EVE / 24 h | MSCS Act 2002 (as amended 2023) and MSCS Rules | COOP-CCS, COOP-GEN |
| SRC-COOP-02 | CRCS model bye-laws / templates | https://crcs.gov.in/tempale_bye_law | PAGE | P3 / WEEK / 7 d | Bye-law templates → P16 | COOP-* |
| SRC-COOP-03 | Ministry of Cooperation | https://www.cooperation.gov.in/ [VERIFY] | LIST | P2 / EVE / 24 h | Schemes, model bye-laws for PACS, national database | COOP-* |
| SRC-COOP-04 | Co-operative Election Authority (multi-state) | [VERIFY] | PAGE | P3 / WEEK / 7 d | Election rules for MSCS | COOP-* |
| SRC-COOP-05 | CRCS state registrar directory | https://crcs.gov.in/state_registrar | PAGE | P3 / WEEK / 7 d | Contact directory; seeds state sources | — |
| SRC-STCOOP-MH | Maharashtra — Commissioner for Co-operation & Registrar | state site [VERIFY] | LIST | P2 / EVE / 24 h | Marathi + English; Maharashtra Co-operative Societies Act 1960 | COOP-* |
| SRC-STCOOP-GJ | Gujarat Registrar | state site [VERIFY] | LIST | P2 / EVE / 24 h | | COOP-* |
| SRC-STCOOP-KA | Karnataka Registrar | state site [VERIFY] | LIST | P2 / EVE / 24 h | Kannada | COOP-* |
| SRC-STCOOP-UP | Uttar Pradesh Commissioner & Registrar | state site [VERIFY] | LIST | P2 / EVE / 24 h | Hindi | COOP-* |
| SRC-STCOOP-RJ | Rajasthan Registrar (RajSahakar portal launched Dec-2022) | state site [VERIFY] | LIST | P2 / EVE / 24 h | Hindi | COOP-* |
| SRC-STCOOP-DL | Delhi Registrar | state site [VERIFY] | LIST | P2 / EVE / 24 h | | COOP-* |
| SRC-STCOOP-TN, -KL, -MP, -WB, -TS, -AP, -PB, -HR, -OD, -BR | Other priority states | state sites [VERIFY] | LIST | P3 / WEEK / 7 d | Regional languages → OCR + translation | COOP-* |
| SRC-RBI-UCB | RBI directions for UCBs and RCBs | (SRC-RBI-03) | — | — | Banking co-operatives are monitored under RBI | RBI-UCB, RBI-RCB |
| SRC-NABARD-01 | NABARD circulars for RCBs (StCB/DCCB) | https://www.nabard.org/ [VERIFY] | LIST | P2 / EVE / 24 h | Supervision of rural co-operative banks | RBI-RCB |

## F.10 Tax, AML and other cross-cutting authorities

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-GST-01 | CBIC Central Tax notifications | https://cbic-gst.gov.in/central-tax-notifications.html (Hindi path observed: `/hindi/central-tax-notifications.html`) | LIST + PDF | P1 / INTRA / 6 h | Due-date extensions, return changes | TAX |
| SRC-GST-02 | Central Tax (Rate) notifications | https://cbic-gst.gov.in/central-tax-rate.html | LIST | P2 / EVE / 24 h | | TAX |
| SRC-GST-03 | CBIC circulars, IGST, UTGST, compensation | cbic-gst.gov.in [VERIFY] | LIST | P2 / EVE / 24 h | | TAX |
| SRC-GST-04 | GST Council | https://gstcouncil.gov.in/ | LIST | P2 / EVE / 24 h | Meeting recommendations (horizon) | TAX |
| SRC-GST-05 | GSTN advisories (portal changes, e-invoicing thresholds) | https://www.gst.gov.in/newsandupdates [VERIFY] | LIST | P1 / EVE / 24 h | Portal/format changes → P11 | TAX |
| SRC-CBDT-01 | CBDT notifications and circulars (Income-tax Act 2025 in force from 1-Apr-2026 [VERIFY]) | https://incometaxindia.gov.in/ (communications) [VERIFY] | LIST | P1 / INTRA / 6 h | TDS/TCS, forms renumbering under the 2025 Act | TAX |
| SRC-CBDT-02 | Income-tax e-filing portal updates | https://www.incometax.gov.in/ [VERIFY] | LIST | P2 / EVE / 24 h | Utility/schema changes → P11 | TAX |
| SRC-FIU-01 | FIU-IND notices, reporting formats (FINnet) | https://fiuindia.gov.in/ [VERIFY] | LIST | P1 / EVE / 24 h | PMLA reporting entities | RBI-*, SEBI-*, IRDAI-*, IFSCA-* |
| SRC-PFRDA-01 | PFRDA regulations/circulars (inactive by default) | https://www.pfrda.org.in/ [VERIFY] | LIST | P3 / WEEK / 7 d | Activated only if a PFRDA family is enabled | — |
| SRC-CERSAI-01 | CERSAI notices | https://www.cersai.org.in/ [VERIFY] | LIST | P2 / WEEK / 7 d | Registration of security interests | RBI-NBFC, RBI-SCB, RBI-ARC |
| SRC-CIC-01 | Credit information companies (TransUnion CIBIL, CRIF High Mark, Experian, Equifax) — member notices and format changes | member portals [VERIFY; often login-only] | MAIL | P2 / — | Format/cycle changes → P11 via tenant-forwarded notices | RBI-* |
| SRC-EGAZ-01 | e-Gazette of India | https://egazette.gov.in/ | GAZ | P1 / EVE / 24 h | Searches per ministry: Finance (DEA/DFS/Revenue), MCA, MeitY, MoLE, Cooperation | all |

## F.11 Standard-setters and professional bodies

| Source ID | Section | URL | Method | Priority / Schedule / SLA | Parser notes | Families |
|---|---|---|---|---|---|---|
| SRC-ICAI-01 | ICAI announcements | https://www.icai.org/category/announcements | LIST | P2 / EVE / 24 h | Ind AS/AS amendments, guidance notes, auditing standards → Appendix J | all |
| SRC-ICAI-02 | ICAI new circulars/announcements | https://www.icai.org/post/new-circulars-announcements | LIST | P2 / EVE / 24 h | | all |
| SRC-ICAI-03 | ICAI resources (guidance notes, technical guides) | https://www.icai.org/resources.shtml?mod=6 | PAGE | P2 / WEEK / 7 d | Some downloads require registration — manual fetch | all |
| SRC-NFRA-01 | NFRA (auditing/accounting standards notifications, orders) | https://nfra.gov.in/ [VERIFY] | LIST | P2 / EVE / 24 h | | MCA-CO, SEBI-LISTED |
| SRC-ICSI-01 | ICSI announcements, Secretarial Standards, guidance notes | https://www.icsi.edu/ [VERIFY sections] | LIST | P2 / EVE / 24 h | SS-1/SS-2 revisions → P06 | MCA-CO, SEBI-LISTED, all companies |
| SRC-ICMAI-01 | ICMAI (cost audit) | https://icmai.in/ [VERIFY] | LIST | P3 / WEEK / 7 d | | MCA-CO |
| SRC-BCI-01 | Bar Council of India (rules affecting marketplace) | https://www.barcouncilofindia.org/ [VERIFY] | PAGE | P3 / WEEK / 7 d | → P21 rules | — |
| SRC-BIS-01 | BCBS / BIS publications (Basel framework updates) | https://www.bis.org/bcbs/publications.htm [VERIFY] | LIST | P3 / WEEK / 7 d | Horizon for P08/P09 | RBI-SCB |

## F.12 International and foreign-regulator sources (flag OFF per jurisdiction until its pack is PILOT or PUBLISHED, D-45) *(v1.1)*

*(v1.1)* The heading's earlier "pack readiness = LIVE" is replaced by the pack lifecycle DRAFT → PILOT → PUBLISHED → DEPRECATED (D-45). A foreign source feeds Updates only for a PUBLISHED pack with a reviewer of record (NN-53); official-language text is kept and translations are labelled (NN-54). The original v1.0 rows are kept below; §F.12A adds the priority jurisdictions.

| Source ID | Authority | URL | Method | Notes |
|---|---|---|---|---|
| SRC-EU-01 | EUR-Lex (GDPR, NIS2, DORA, AI Act consolidated texts) | https://eur-lex.europa.eu/ | LIST/RSS [VERIFY feeds] | Consolidated versions with dates |
| SRC-EU-02 | EDPB guidelines and opinions | https://www.edpb.europa.eu/ | LIST | |
| SRC-US-CA-01 | California Privacy Protection Agency (CCPA/CPRA regulations) | https://cppa.ca.gov/ | LIST | |
| SRC-US-CA-02 | California Attorney General (CCPA enforcement) | https://oag.ca.gov/privacy/ccpa | PAGE | |
| SRC-UK-01 | ICO | https://ico.org.uk/ | LIST | |
| SRC-SG-01 | PDPC Singapore | https://www.pdpc.gov.sg/ | LIST | |
| SRC-AE-01 | UAE (federal PDPL; DIFC/ADGM regulators) | [VERIFY] | LIST | *(v1.1)* Split into SRC-AE-02 to AE-13 below; kept as an umbrella ID |

### F.12A Priority jurisdictions *(v1.1)*

Order follows the corridor rollout (D-43): UAE (mainland, DIFC, ADGM) and Singapore first, then UK, EU and US. Company-registry **data** (Companies House API, ACRA BizFile, DIFC/ADGM registers) is not a regulatory source: it is fetched through `COMPANY_DATA_PORT` adapters for the group entity register (P25 `gem`, P18) and is listed here only for completeness.

| Source ID | Authority / section | URL | Method | Schedule (local TZ) | Notes | Families |
|---|---|---|---|---|---|---|
| SRC-AE-02 | Central Bank of the UAE — Rulebook | https://rulebook.centralbank.ae/ | LIST + PAGE | EVE-L (Asia/Dubai) | Rulebook shows amendment dates per section | INTL-GEN |
| SRC-AE-03 | CBUAE notices and regulations | https://www.centralbank.ae/ [VERIFY path] | LIST | EVE-L | | INTL-GEN |
| SRC-AE-04 | Securities and Commodities Authority (SCA) | https://www.sca.gov.ae/ [VERIFY path] | LIST | EVE-L | Arabic official; English labelled translation | INTL-GEN |
| SRC-AE-05 | DFSA (DIFC) — rulebook and notices | https://www.dfsa.ae/ [VERIFY rulebook host] | LIST + PAGE | EVE-L | | INTL-GEN |
| SRC-AE-06 | DIFC Authority — laws, regulations, Registrar of Companies, Commissioner of Data Protection | https://www.difc.ae/ [VERIFY paths] | LIST | EVE-L | DIFC DP Law No. 5 of 2020 (as amended) | INTL-GEN, DATA-PRIV |
| SRC-AE-07 | ADGM FSRA — rulebook and notices | https://www.adgm.com/ [VERIFY rulebook host] | LIST + PAGE | EVE-L | | INTL-GEN |
| SRC-AE-08 | ADGM Registration Authority and Office of Data Protection | https://www.adgm.com/ [VERIFY paths] | LIST | WEEK-L | | INTL-GEN, DATA-PRIV |
| SRC-AE-09 | UAE federal legislation portal | https://uaelegislation.gov.ae/ | LIST + PDF | EVE-L | Arabic is the official text (NN-54) | INTL-GEN |
| SRC-AE-10 | Ministry of Human Resources and Emiratisation (MoHRE) | https://www.mohre.gov.ae/ [VERIFY] | LIST | WEEK-L | Emiratisation, WPS | INTL-GEN |
| SRC-AE-11 | Federal Tax Authority (corporate tax, VAT) | https://tax.gov.ae/ [VERIFY] | LIST | EVE-L | | INTL-GEN |
| SRC-AE-12 | UAE Financial Intelligence Unit (goAML) | https://www.uaefiu.gov.ae/ [VERIFY] | LIST | WEEK-L | | INTL-GEN |
| SRC-AE-13 | UAE Data Office (federal PDPL executive regulations) | [VERIFY URL once operational] | PAGE | WEEK-L | | INTL-GEN, DATA-PRIV |
| SRC-SG-02 | Monetary Authority of Singapore — regulations, notices, guidelines | https://www.mas.gov.sg/regulation [VERIFY RSS] | LIST / RSS | INTRA-L (Asia/Singapore) | | INTL-GEN, AI-GOV |
| SRC-SG-03 | MAS consultations | https://www.mas.gov.sg/publications/consultations | LIST | EVE-L | Class CONSULTATION_DRAFT | INTL-GEN |
| SRC-SG-04 | ACRA — news and legislative changes | https://www.acra.gov.sg/ [VERIFY path] | LIST | EVE-L | Annual return, RORC changes | INTL-GEN |
| SRC-SG-05 | Singapore Statutes Online — new Acts and subsidiary legislation | https://sso.agc.gov.sg/ [VERIFY "What's New" path] | LIST | EVE-L | Point-in-time versions | INTL-GEN |
| SRC-SG-06 | IRAS | https://www.iras.gov.sg/ | LIST | WEEK-L | | INTL-GEN |
| SRC-SG-07 | Ministry of Manpower | https://www.mom.gov.sg/ | LIST | WEEK-L | | INTL-GEN |
| SRC-UK-02 | FCA — news, policy statements, Handbook notices | https://www.fca.org.uk/news [VERIFY RSS] ; https://www.handbook.fca.org.uk/ | RSS + LIST | INTRA-L (Europe/London) | Handbook instruments carry commencement dates | INTL-GEN |
| SRC-UK-03 | PRA (Bank of England) — policy and supervisory statements | https://www.bankofengland.co.uk/prudential-regulation [VERIFY feed] | LIST | EVE-L | | INTL-GEN |
| SRC-UK-04 | Companies House — guidance and changes (GOV.UK organisation feed) | https://www.gov.uk/government/organisations/companies-house (Atom feed) | RSS | EVE-L | ECCTA 2023 identity-verification stages [VERIFY dates]; entity data via the Companies House API (`COMPANY_DATA_PORT`) | INTL-GEN |
| SRC-UK-05 | legislation.gov.uk — new UK legislation | https://www.legislation.gov.uk/new [VERIFY feed] | RSS / API | EVE-L | Point-in-time revised versions | INTL-GEN |
| SRC-UK-06 | HMRC (GOV.UK organisation feed) | https://www.gov.uk/government/organisations/hm-revenue-customs | RSS | WEEK-L | | INTL-GEN |
| SRC-EU-03 | European Banking Authority | https://www.eba.europa.eu/ | LIST / RSS [VERIFY] | EVE-L (Europe/Brussels) | RTS/ITS, guidelines | INTL-GEN |
| SRC-EU-04 | ESMA | https://www.esma.europa.eu/ | LIST | EVE-L | | INTL-GEN |
| SRC-EU-05 | EIOPA | https://www.eiopa.europa.eu/ | LIST | WEEK-L | | INTL-GEN |
| SRC-EU-06 | EU AI Office | see SRC-AI-05 | — | — | Cross-reference | AI-GOV |
| SRC-EU-07 | Official Journal of the EU (L series, daily) | https://eur-lex.europa.eu/oj/direct-access.html | LIST | EVE-L | New regulations and directives; national transposition handled by member-state packs later | INTL-GEN, DATA-PRIV, CYBER |
| SRC-US-01 | SEC — press releases and rulemaking | https://www.sec.gov/news/pressreleases.rss ; https://www.sec.gov/rules-regulations [VERIFY paths] | RSS + LIST | INTRA-L (America/New_York) | Final rules → instruments; proposed → CONSULTATION_DRAFT | INTL-GEN |
| SRC-US-02 | Federal Register API (agencies: SEC, FinCEN, CFPB, FTC, OCC, FRB, FDIC) | https://www.federalregister.gov/api/v1/documents.json | API | INTRA-L | Filter by agency and document type; effective dates parsed | INTL-GEN |
| SRC-US-03 | eCFR (point-in-time CFR) | https://www.ecfr.gov/ (versioner API) | API | WEEK-L | Used for consolidated text and diffs | INTL-GEN |
| SRC-US-04 | FinCEN — news, guidance, BOI reporting | https://www.fincen.gov/ | LIST | EVE-L | CTA BOI scope after the 2025 interim final rule [VERIFY] | INTL-GEN |
| SRC-US-05 | CFPB — rules and policy | https://www.consumerfinance.gov/rules-policy/ | LIST | WEEK-L | | INTL-GEN |
| SRC-US-DE-01 | Delaware Division of Corporations (franchise tax, annual report) | https://corp.delaware.gov/ | PAGE | WEEK-L | Annual 1 March deadline for corporations [VERIFY] | INTL-GEN |
| SRC-US-NY-01 | New York DFS (23 NYCRR 500 cybersecurity and notices) | https://www.dfs.ny.gov/ [VERIFY path] | LIST | EVE-L | | INTL-GEN, CYBER |
| SRC-US-TX-01 | Texas Comptroller (franchise tax) | https://comptroller.texas.gov/ | PAGE | WEEK-L | P3 | INTL-GEN |

Later packs (not seeded): Saudi Arabia (SAMA rulebook; personal-data limits under D-46), Qatar (QFCRA, QCB), Bahrain (CBB rulebook), Hong Kong (HKMA, SFC, Companies Registry), Mauritius (FSC), Australia (ASIC, APRA), Canada and Mexico. Each pack adds its rows to this register when it enters DRAFT.

### F.12B Licensed regulatory-intelligence feeds (`REG_INTEL_PORT`) *(v1.1)*

- **Purpose.** Breadth for jurisdictions where LawDocsComply has no pack yet, and early warning for packs being built. Flag OFF per provider until contracted (OI-P05-11). Candidate providers are listed in P25 (Thomson Reuters Regulatory Intelligence, LexisNexis, Wolters Kluwer, CUBE, Regology, Corlytics, OneTrust DataGuidance).
- **Signals only.** Each provider item becomes a `LICENSED_SIGNAL` WATCH entry on the Radar, labelled with the provider. It cannot become an Update or change a checkpoint until an analyst links the official primary source (LDC-CHG-121; NN-06, NN-53).
- **Licence limits.** Display and retention follow the provider licence (some items visible to the content team only); provider text is never copied into checkpoints.
- **De-duplication.** A signal is matched to official items detected by §F.12A sources (same authority, reference or title within 7 days) and closes automatically when the official item is published.
- **Metering.** Calls and items per provider are metered for cost (P20) and reported in §F.17.

### F.12C Scheduling and residency *(v1.1)*

Foreign scans run on local-time schedules (§F.1) from the regional cell that hosts the pack (P25). Public legislation and regulator publications are not personal data, so the parsed results are published to the global content library and replicated to every cell; tenant data never leaves its home cell (NN-24).

## F.13 News and secondary sources (P3 signals; `chg.news.enabled` = OFF)

Licensed business and legal news feeds; law-firm alert pages (e.g., JSA, Cyril Amarchand, Trilegal, Vinod Kothari, Taxguru, Taxscan) may be used by analysts as **secondary context** only, never as the source of an obligation (NN-06). Secondary items create WATCH entries that close when the official instrument is detected. *(v1.1)* Licensed foreign feeds follow §F.12B.

## F.14 Fetch, parse and failure handling

1. **Fetch:** via the production egress proxy; HTTPS; per-host rate limit ≤ 1 request / 3 s; conditional GET; timeout 30 s; max body 50 MB (PDF), 5 MB (HTML); retries 3 with exponential backoff (1, 4, 16 min).
2. **Parse:** parser profile per source (selectors, date formats e.g. `MMM dd, yyyy`, `dd/MM/yyyy`, `YYYYMMDD`, reference regexes); a structural fingerprint (DOM path hash of the list container) stored per run; a fingerprint change with zero parsed items → `PARSER_BROKEN`.
3. **Change detection:** new GUID/URL; same URL with new hash → `version_of`; title change on same URL → flagged; disappearance of a previously listed item → `possibly withdrawn` flag for analyst review (no automatic repeal).
4. **Language:** prefer English documents; store Hindi/regional versions as alternates; regional-only documents → OCR (if scanned) + machine translation labelled as translation (P07), analyst reviews against the original. *(v1.1)* For foreign sources the official-language text is always stored as the authoritative version; translations carry `translation_state` (`OFFICIAL`, `REVIEWED`, `MACHINE_UNREVIEWED`, `NONE`; P03 FR-P03-02) and a `MACHINE_UNREVIEWED` translation blocks publication (NN-54; LDC-PACK-102).
5. **Failure handling:** DEGRADED after one failure; FAILING after three consecutive failures or SLA breach → P2 alert to content lead (e-mail + Console banner); P1 sources failing for > 6 hours → P1 alert to on-duty analyst; daily Radar lists all non-healthy sources; manual "mark checked" by an analyst (with evidence screenshot) can satisfy the SLA for a day when a site is down.
6. **Evidence of monitoring:** `chg.fetch_runs` retained for 7 years; monthly monitoring report (coverage, failures, mean detection lag vs official publication date) available to tenants on request as assurance evidence for their own regulatory-change process.
7. **Legal/terms:** public government publications are fetched for the purpose of informing regulated entities of their obligations; LawDocs copies the official text for reference with attribution and link; no login-only content is scraped (CIC member portals, regulator filing portals) — those changes reach LDC only through tenant-forwarded notices or partner agreements.
8. *(v1.1)* **Faster sweeps:** listing pages are hashed by row set and only new or changed rows are parsed; PDFs are fetched only for those rows; sources are sharded by host so a slow site does not delay others. Target: all P1 Indian sources complete an EVE sweep in ≤ 10 minutes.
9. *(v1.1)* **Back-fill:** after a source outage, the next successful run re-reads the listing for the missed window (date filter or pagination) and marks back-filled items so detection-lag KPIs are not distorted (P05 FR-P05-12).


## F.15 Addressee dictionary (classification seed for P05 FR-P05-22)

Regulators state the addressees at the head of each instrument. The dictionary maps addressee phrases (case-insensitive, punctuation-normalised, with Hindi equivalents where published) to template families and entity types. Analysts extend it in the Console; each entry is versioned.

| Addressee phrase (examples) | Family | Entity types / layers |
|---|---|---|
| "All Commercial Banks (excluding Regional Rural Banks)", "All Scheduled Commercial Banks" | RBI-SCB | Public sector, private sector, foreign banks (as listed in Appendix E) |
| "All Small Finance Banks" | RBI-SCB | SFB |
| "All Payments Banks" | RBI-SCB | PB |
| "All Local Area Banks" | RBI-SCB | LAB |
| "All Regional Rural Banks" | RBI-SCB (or RBI-RCB per Appendix E decision) | RRB |
| "All Primary (Urban) Co-operative Banks", "All UCBs" | RBI-UCB | Tier 1–4 |
| "All State Co-operative Banks / District Central Co-operative Banks" | RBI-RCB | StCB, DCCB |
| "All All-India Financial Institutions (EXIM Bank, NABARD, NHB, SIDBI, NaBFID)" | RBI-OTH | AIFI |
| "All Non-Banking Financial Companies", "All NBFCs including HFCs" | RBI-NBFC | all layers; type list |
| "All NBFCs in the Upper Layer", "NBFC-UL" | RBI-NBFC | Upper Layer |
| "All NBFCs in the Middle Layer and Upper Layer" | RBI-NBFC | Middle, Upper |
| "All Housing Finance Companies" | RBI-NBFC | HFC |
| "All NBFC-MFIs", "NBFC-Micro Finance Institutions" | RBI-NBFC | MFI |
| "Core Investment Companies" | RBI-NBFC | CIC |
| "NBFC – Peer to Peer Lending Platforms" | RBI-NBFC | P2P |
| "NBFC – Account Aggregators" | RBI-NBFC | AA |
| "Asset Reconstruction Companies" | RBI-ARC | ARC |
| "Credit Information Companies" | RBI-OTH | CIC (credit information) — distinct from Core Investment Company |
| "Payment System Operators / Payment Aggregators / PPI issuers" | RBI-OTH | PSO, PA, PPI |
| "Authorised Dealers Category-I/II", "Full-Fledged Money Changers" | RBI-OTH | AD-I, AD-II, FFMC |
| "All recognised Stock Exchanges / Clearing Corporations / Depositories" | SEBI-INT | MII |
| "All listed entities", "All entities having listed specified securities / NCDs" | SEBI-LISTED | equity-listed, debt-listed |
| "All Mutual Funds / Asset Management Companies / Trustee Companies" | SEBI-MF | AMC, Trustee |
| "All Alternative Investment Funds and their Managers" | SEBI-AIF | Cat I/II/III, manager |
| "All REITs / InvITs and their Managers / Investment Managers" | SEBI-REIT-INVIT | REIT, InvIT |
| "All Stock Brokers / Depository Participants / Investment Advisers / Research Analysts / Portfolio Managers / RTAs / Merchant Bankers / Debenture Trustees / CRAs / KRAs" | SEBI-INT | per type |
| "All IFSC Banking Units", "IBUs" | IFSCA-GEN | IBU |
| "Finance Companies / Finance Units in IFSC" | IFSCA-FCFU | FC, FU |
| "Fund Management Entities", "FMEs" | IFSCA-FME | FME (registered/authorised/retail) |
| "IFSC Insurance Offices / Insurance Intermediary Offices" | IFSCA-GEN | IIO, IIIO |
| "All Regulated Entities in IFSC" | IFSCA-GEN (+ all IFSCA families) | all |
| "All Insurers", "Life / General / Health insurers, Reinsurers, FRBs" | IRDAI-INS | per type |
| "All Insurance Intermediaries", "Brokers / Corporate Agents / Web Aggregators / IMFs / TPAs / Surveyors" | IRDAI-INT | per type |
| "All companies", "Companies (other than …)" | MCA-CO | private, public, OPC, small, Section 8, listed (cross-tag) |
| "Limited Liability Partnerships" | MCA-LLP | LLP, small LLP |
| "Data Fiduciaries", "Significant Data Fiduciaries", "Consent Managers" | DATA-PRIV | DF, SDF, CM |
| "Service providers, intermediaries, data centres, body corporate and Government organisations" (CERT-In) | CYBER | all |
| "Establishments", "Employers", "Factories", "Contractors" (Labour Codes) | LAB | by headcount/establishment type |
| "Registered persons", "Taxpayers" (GST) | TAX | by turnover/registration type |
| "Multi-State Co-operative Societies" | COOP-CCS / COOP-GEN | MSCS by type |
| "Co-operative societies registered under the <State> Co-operative Societies Act" | COOP-CCS / COOP-GEN | state, type |
| "Reporting entities" (PMLA / FIU-IND) | cross-cutting (RBI-*, SEBI-*, IRDAI-*, IFSCA-*, COOP-CCS where applicable) | — |

Ambiguities are resolved by the analyst: e.g., "CIC" must be disambiguated between Core Investment Company (RBI-NBFC) and Credit Information Company (RBI-OTH) from the instrument's subject; "Regional Rural Banks" may appear with commercial banks or separately.

## F.16 Parser profile examples (illustrative; final profiles are data in `chg.sources.parser_profile`)

```yaml
SRC-RBI-03:   # Master Directions listing
  container: "table.tablebg"            # [VERIFY selector at build]
  group_heading: "td.tableheader"        # RE category headings
  date_heading: "tr > td > b"            # e.g. "Nov 28, 2025"
  date_format: "MMM dd, yyyy"
  item: "a.link2"                        # title link to BS_ViewMasDirections.aspx?id=<n>
  pdf_link: "a[href*='rbidocs.rbi.org.in']"
  version_marker_regex: "\(Updated as on ([A-Za-z]{3,9} \d{1,2}, \d{4})\)"
  ref_regex: "RBI/\d{4}-\d{2}/\d+"
  fingerprint: dom_path_hash(container)
  expected_min_items_per_30d: 3          # drift detection
SRC-RBI-30:   # (v1.1) category page, DoR Commercial Banks (same profile for SRC-RBI-31..52 with did changed)
  url: "https://rbi.org.in/Scripts/BS_ViewMasterDirections.aspx?did=403"
  container: "table.tablebg"            # [VERIFY selector at build]
  item: "a[href*='BS_ViewMasDirections.aspx?id=']"
  item_id_regex: "id=(\d+)"
  updated_as_on_regex: "Updated as on ([A-Za-z]{3,9} \d{1,2}, \d{4})"
  ref_regex: "RBI/[A-Za-z]+/\d{4}-\d{2}/\d+"
  rowset_hash: true                      # skip parse when unchanged
  catalogue_join: [item_id, ref, normalised_title]
  on_date_change: CONSOLIDATION_UPDATE
  on_new_row: NEW_INSTRUMENT
  on_missing_row: POSSIBLY_SUPERSEDED
  expected_rows: from_catalogue           # drift when page count differs
SRC-US-02:    # (v1.1) Federal Register API
  type: api
  endpoint: "https://www.federalregister.gov/api/v1/documents.json"
  params: { "conditions[agencies][]": [securities-and-exchange-commission, financial-crimes-enforcement-network], "conditions[type][]": [RULE, PRORULE] }
  date_field: publication_date
  effective_field: effective_on
  class_map: { RULE: INSTRUMENT, PRORULE: CONSULTATION_DRAFT }
  timezone: America/New_York
SRC-SEBI-01:  # RSS
  type: rss
  guid: link
  category_map: { "Circulars": CIRCULAR, "Press Releases": PRESS_RELEASE, "Orders": ORDER }
  ref_regex: "SEBI/HO/[A-Z0-9/-]+/P/CIR/\d{4}/\d+"
SRC-IFSCA-01: # New Section table
  container: "table"                     # columns Date | Type | Title
  date_columns: ["YYYYMMDD", "dd/MM/yyyy"]
  type_column_index: 1
  title_link: "td:nth-child(3) a"
  url_normalise: "trim_spaces_in_MId"    # some MId tokens contain stray spaces
  class_map: { Regulation: INSTRUMENT, Circular: INSTRUMENT, Guidelines: INSTRUMENT, Notification: INSTRUMENT,
               FAQs: FAQ_CLARIFICATION, "AML Compliance": INSTRUMENT, "Public Consultation": CONSULTATION_DRAFT,
               "Informal Guidance": FAQ_CLARIFICATION, "Press Release": PRESS_RELEASE_INFO,
               Career: NON_ACTIONABLE, Tender: NON_ACTIONABLE, DRHP: NON_ACTIONABLE, RHP: NON_ACTIONABLE }
SRC-COOP-01:  # CRCS circulars
  container: "table"
  columns: [s_no, subject, issued_date]
  pdf_pattern: "/public/uploads/circulars/Cir_.*\.pdf"
  expected_min_items_per_365d: 1         # low-frequency source
```

## F.17 Monitoring KPIs reported monthly

| KPI | Definition | Target |
|---|---|---|
| Source availability | Successful scans / scheduled scans per source | ≥ 99 % for P1 |
| Detection lag | Detected_at − official publication time (where the source shows time) or date | P1 ≤ 2 h median during 09:00–21:00 IST; all ≤ 24 h |
| Triage lag | Triaged_at − detected_at | ≤ 1 business day (IMMEDIATE ≤ 4 h) |
| Publication lag | Published_at − detected_at for ACTIONABLE | IMMEDIATE ≤ 1, HIGH ≤ 3, NORMAL ≤ 10 business days (P95) |
| Missed items | Official items found later by manual check or by tenants that the monitor did not detect | 0 for P1 sources |
| Parser incidents | PARSER_BROKEN events per month | Trend down; each closed ≤ 1 business day |
| Tenant reach | Updates delivered within 1 hour of publication | ≥ 99 % |
| Catalogue drift *(v1.1)* | RBI catalogue rows whose "Updated as on" date or presence differs from the category page for more than 24 h | 0 |
| Foreign detection lag *(v1.1)* | Detected_at − official publication (authority local time) for PUBLISHED packs | ≤ 24 h median; ≤ 48 h P95 |
| Licensed-signal confirmation *(v1.1)* | Share of `LICENSED_SIGNAL` items linked to a primary source or closed within 5 business days | ≥ 95 % |

## F.18 Sources for this appendix (accessed 25 October 2026)

1. https://www.rbi.org.in/ (navigation and RSS link); https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx
2. JSA KM Newsflash on RBI function-wise Master Directions (29-Nov-2025): https://www.jsalaw.com/wp-content/uploads/2025/11/KM-Newsflash-RBI-Master-Directions.pdf
3. https://www.sebi.gov.in/rss.html; SEBI master circular URL patterns, e.g., https://www.sebi.gov.in/legal/master-circulars/jan-2026/master-circular-for-compliance-with-the-provisions-of-the-securities-and-exchange-board-of-india-listing-obligations-and-disclosure-requirements-regulations-2015-by-listed-entities_99432.html
4. https://ifsca.gov.in/Home/NewSection
5. https://policyholder.gov.in/web/guest/circulars ; https://policyholder.gov.in/web/guest/register-for-email-alerts
6. https://crcs.gov.in/circulars ; https://crcs.gov.in/state_registrar ; https://crcs.gov.in/tempale_bye_law
7. CBIC GST notification pages: https://cbic-gst.gov.in/hindi/central-tax-notifications.html ; https://cbic-gst.gov.in/hindi/central-tax-rate.html
8. ICAI announcements: https://www.icai.org/post/new-circulars-announcements
9. EY alert on Labour Codes effective 21-Nov-2025: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/alerts-hub/2025/11/new-labour-codes-implemented-across-the-country-effective-21-november-2025.pdf ; L&E Global, 28-May-2026: https://leglobal.law/2026/05/28/india-indian-ministry-of-labour-and-employment-notifies-central-rules-and-appropriate-authorities-under-the-labour-codes/
10. SCC Online, "MeitY notified Digital Personal Data Protection Rules, 2025" (14-Nov-2025): https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/
11. *(v1.1)* RBI Master Directions category pages: https://rbi.org.in/Scripts/BS_ViewMasterDirections.aspx?did=403 (and did=404–413, 419–429, 338); Appendix AB and `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`
12. *(v1.1)* Federal Register API documentation: https://www.federalregister.gov/developers/documentation/api/v1
13. *(v1.1)* Companies House public data API: https://developer.company-information.service.gov.uk/
14. *(v1.1)* MAS regulations: https://www.mas.gov.sg/regulation ; CBUAE Rulebook: https://rulebook.centralbank.ae/ ; EUR-Lex Official Journal: https://eur-lex.europa.eu/oj/direct-access.html
15. *(v1.1)* Foreign URLs in §F.12A marked [VERIFY] were not opened during preparation; P05 sprint 1 test-fetches them with the Indian sources.
