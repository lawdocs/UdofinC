# Appendix F — Regulatory Source Register and Monitoring Catalogue

> Binding for P05 (source monitor) and P03 (authority registry). Seed data for `chg.sources` and `cnt.authorities`. Prepared 25 October 2026. URLs marked **[VERIFY]** were not opened during preparation or were observed to redirect; the build team test-fetches every source in P05 sprint 1 and records the result in `chg.fetch_runs`. Changing this register in production is a Governed change (P02).

## F.1 How to read this register

| Field | Meaning |
|---|---|
| Source ID | `SRC-<AUTH>-<NN>`; stable; used in `chg.sources.source_id` |
| Method | RSS · LIST (HTML listing with parser profile) · PAGE (single page change detection) · PDF (follow links to PDFs) · GAZ (e-Gazette search) · MAIL (regulator e-mail alert to monitored mailbox) · NEWS (licensed feed, flag OFF) |
| Priority | P1 core regulators (affect most tenants, frequent) · P2 ministries and standard-setters · P3 state departments, low-frequency or redundant sources |
| Schedule | INTRA (every 30 min 09:00–21:00 IST, hourly otherwise) · EVE (daily 20:00 IST reconciliation — every source is included in EVE regardless of class) · WEEK (Sunday 03:00 IST deep crawl) |
| SLA | Maximum time between successful scans before a P2 alert |
| Families | Appendix E template families most affected |

## F.2 Reserve Bank of India (RBI)

RBI's main site navigation (verified 25-Oct-2026) groups regulatory content under Notifications, Press Releases and Regulatory Reporting. On 28-Nov-2025 RBI issued 238 function-wise consolidated Master Directions for 11 RE categories (commercial banks, small finance banks, payments banks, local area banks, regional rural banks, UCBs, rural co-operative banks, AIFIs, NBFCs, ARCs, CICs), repealing over 9,000 circulars; later changes arrive as Amendment Directions and "updated as on" consolidations. The Master Directions page groups by RE category under date headings; direction pages follow `BS_ViewMasDirections.aspx?id=<n>`; PDFs follow `https://rbidocs.rbi.org.in/rdocs/notification/PDFs/<n><code>.PDF`. A newer site (`website.rbi.org.in`) offered notification preferences but its URLs redirected (302) to `rbi.org.in` on 25-Oct-2026 [VERIFY canonical site at build].

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
| SRC-RBI-21 | Integrated Ombudsman / CEPD | https://cms.rbi.org.in/ [VERIFY] | PAGE | P2 / WEEK / 7 d | Scheme changes → P14 | RBI-* |
| SRC-RBI-22 | RBI e-mail notification preferences | (subscription) | MAIL | P3 / — | Redundancy | all RBI |

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

## F.12 International packs (flag OFF until pack readiness = LIVE, D-19)

| Source ID | Authority | URL | Method | Notes |
|---|---|---|---|---|
| SRC-EU-01 | EUR-Lex (GDPR, NIS2, DORA, AI Act consolidated texts) | https://eur-lex.europa.eu/ | LIST/RSS [VERIFY feeds] | Consolidated versions with dates |
| SRC-EU-02 | EDPB guidelines and opinions | https://www.edpb.europa.eu/ | LIST | |
| SRC-US-CA-01 | California Privacy Protection Agency (CCPA/CPRA regulations) | https://cppa.ca.gov/ | LIST | |
| SRC-US-CA-02 | California Attorney General (CCPA enforcement) | https://oag.ca.gov/privacy/ccpa | PAGE | |
| SRC-UK-01 | ICO | https://ico.org.uk/ | LIST | |
| SRC-SG-01 | PDPC Singapore | https://www.pdpc.gov.sg/ | LIST | |
| SRC-AE-01 | UAE (federal PDPL; DIFC/ADGM regulators) | [VERIFY] | LIST | |

## F.13 News and secondary sources (P3 signals; `chg.news.enabled` = OFF)

Licensed business and legal news feeds; law-firm alert pages (e.g., JSA, Cyril Amarchand, Trilegal, Vinod Kothari, Taxguru, Taxscan) may be used by analysts as **secondary context** only, never as the source of an obligation (NN-06). Secondary items create WATCH entries that close when the official instrument is detected.

## F.14 Fetch, parse and failure handling

1. **Fetch:** via the production egress proxy; HTTPS; per-host rate limit ≤ 1 request / 3 s; conditional GET; timeout 30 s; max body 50 MB (PDF), 5 MB (HTML); retries 3 with exponential backoff (1, 4, 16 min).
2. **Parse:** parser profile per source (selectors, date formats e.g. `MMM dd, yyyy`, `dd/MM/yyyy`, `YYYYMMDD`, reference regexes); a structural fingerprint (DOM path hash of the list container) stored per run; a fingerprint change with zero parsed items → `PARSER_BROKEN`.
3. **Change detection:** new GUID/URL; same URL with new hash → `version_of`; title change on same URL → flagged; disappearance of a previously listed item → `possibly withdrawn` flag for analyst review (no automatic repeal).
4. **Language:** prefer English documents; store Hindi/regional versions as alternates; regional-only documents → OCR (if scanned) + machine translation labelled as translation (P07), analyst reviews against the original.
5. **Failure handling:** DEGRADED after one failure; FAILING after three consecutive failures or SLA breach → P2 alert to content lead (e-mail + Console banner); P1 sources failing for > 6 hours → P1 alert to on-duty analyst; daily Radar lists all non-healthy sources; manual "mark checked" by an analyst (with evidence screenshot) can satisfy the SLA for a day when a site is down.
6. **Evidence of monitoring:** `chg.fetch_runs` retained for 7 years; monthly monitoring report (coverage, failures, mean detection lag vs official publication date) available to tenants on request as assurance evidence for their own regulatory-change process.
7. **Legal/terms:** public government publications are fetched for the purpose of informing regulated entities of their obligations; LawDocs copies the official text for reference with attribution and link; no login-only content is scraped (CIC member portals, regulator filing portals) — those changes reach LDC only through tenant-forwarded notices or partner agreements.


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
