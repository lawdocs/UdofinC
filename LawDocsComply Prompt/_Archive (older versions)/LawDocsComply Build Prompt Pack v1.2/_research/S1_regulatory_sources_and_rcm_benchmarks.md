# S1 research notes — regulatory sources and regulatory-change benchmarks (as of 25 October 2026)

## A. Official sources verified

| Authority | Finding | Source (accessed 25-Oct-2026) |
|---|---|---|
| RBI | Main navigation: Notifications `https://www.rbi.org.in/Scripts/NotificationUser.aspx`; Master Directions `https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx`; Master Circulars `BS_ViewMasterCirculardetails.aspx`; Amendment Directions `Fs_AmendmentDirections.aspx`; Draft notifications `DraftNotificationsGuildelines.aspx`; Draft Directions (RE-wise) `BS_ViewREwiseDraftDirections.aspx`; Index to circulars `BS_CircularIndexDisplay.aspx`; Standalone circulars `BS_ViewListofstandalonecirculars.aspx`; Circulars withdrawn `NotificationUserWithdrawnCircular.aspx`; Press releases `BS_PressReleaseDisplay.aspx`; What's new `NewLinkDetails.aspx`; RSS `https://www.rbi.org.in/Scripts/rss.aspx`; Regulatory reporting: list of returns `BS_Listofallreturns.aspx`, data definitions `DataDefinition.aspx`, validation rules/taxonomy `ValidationRules.aspx`, portals `ReportingPlaform.aspx`, FAQs `ReportingFAQ.aspx` | rbi.org.in home page |
| RBI | Master Directions listed by RE category (Commercial Banks, SFBs, Payments Banks, LABs, RRBs, UCBs, Rural Co-op Banks, AIFIs, NBFCs, ARCs, CICs) under date headings; direction page `BS_ViewMasDirections.aspx?id=<n>`; PDFs `https://rbidocs.rbi.org.in/rdocs/notification/PDFs/<n><code>.PDF`; "Updated as on <date>" embedded in titles (e.g., UCB Governance Directions 2025 updated as on 25-May-2026) | BS_ViewMasterDirections.aspx |
| RBI | 28-Nov-2025: 238 function-wise consolidated Master Directions for 11 RE categories, consolidating > 9,000 circulars; naming "Reserve Bank of India (<RE category> – <Subject>) Directions, 2025"; savings clause preserves actions taken under repealed instructions; drafts issued 10-Oct-2025 | JSA KM Newsflash 29-Nov-2025; Taxscan 03-Dec-2025 |
| RBI | 2026 directions continue the pattern (e.g., Commercial Banks – Credit Valuation Adjustment Framework 07-Oct-2026; Minimum Capital Requirements for Market Risk 21-Sep-2026; Internal Ombudsman (NBFC) 14-Jan-2026) — confirms amendments arrive as Amendment Directions and "updated as on" consolidations | BS_ViewMasterDirections.aspx |
| RBI | A new website (`website.rbi.org.in`) existed with notification-preference subscription; URLs now 302-redirect to rbi.org.in [VERIFY at build: which site is canonical] | fetch 25-Oct-2026 |
| SEBI | RSS `https://www.sebi.gov.in/sebirss.xml` (Press Releases, Circulars, Orders/Rulings) | sebi.gov.in/rss.html |
| IFSCA | `https://ifsca.gov.in/Home/NewSection` table (Date, Type, Title); types: Regulation, Circular, Guidelines, Notification, FAQs, AML Compliance, Public Consultation, Public Comments, Press Release, Bulletin, Research, Committee Report, Informal Guidance, DRHP/RHP; URL patterns `/Legal/Index?MId=…`, `/ReportPublication/Index?MId=…`, `/PressRelease/Index?MId=…`; no RSS | ifsca.gov.in |
| IFSCA | Org egress allowlist previously blocked ifsca.gov.in from automation shells (owner memory, Sep 2026) — production egress must allow it | memory |
| IRDAI | Circulars listing on `policyholder.gov.in/web/guest/circulars` (IRDAI-owned site; reference format `IRDAI/PPGR/Cir/Misc/97/06/2024`); email-alert registration page exists; irdai.gov.in canonical structure [VERIFY] | policyholder.gov.in |
| CRCS | `https://crcs.gov.in/circulars` (S No, Subject, Issued Date; PDFs under `/public/uploads/circulars/`); newest listed item 23-Sep-2022 though footer updated 29-Sep-2026 → low-frequency source; monitor also Ministry of Cooperation | crcs.gov.in |
| MoLE | Four Labour Codes effective 21-Nov-2025; draft central rules published Dec-2025; state rules progressive | EY/KPMG/BDO alerts Nov–Dec 2025 |

## B. Benchmarks

| Product | Relevant capabilities | Source |
|---|---|---|
| Lawrbit GCMS | 2,000+ laws, 60,000+ obligations with 60+ parameters each; monitors 2,000+ websites; 5 layers (Performer, Approver, Group Owner, CXO, Auditor); approve/reject/reallocate; pre/post dependencies; event-trigger restrictions; FY calendar auto-populated; heat maps; Matrix report builder (10 filters, ~40 columns), scheduled email reports; compliance certificates HOD→CCO→Board; 70+ countries, 1,000+ authorities; tamper-proof documents; internal compliance module; licence tracking | lawrbit.com solution overview PDF (2024) |
| Komrisk (Lexplosion) | 70,000+ compliances; near-real-time updates; applicability at onboarding; escalation on missed deadline; mobile apps; AI: KAI assistant, Kompare (checks uploaded proof against requirement), RegIQ risk scoring | lexplosion.in |
| TeamLease RegTech (RegTrack) | 1,536 Acts, 69,233 obligations, 6,618 filings/registers, 3,756 sites monitored, ~12,000 changes/yr mapped in 24–48 h; performer/reviewer/approver/backup owner with auto-transfer on leave; tiered reminders (T-7 to T+3 escalation); sub-tasks must close first; time-boxed read-only auditor access; OCR auto-classification of challans; penalty exposure quantified; 7 role views; SOC 2 Type II, ISO 27001:2022 | teamleaseregtech.com |
| ServiceNow IRM Regulatory Change Management | Alert → triage → applicability → impact assessment → action tasks (policy/control/risk updates) → closure (docs portal fetch failed; pattern from public docs titles) | servicenow.com docs |
| Compliance.ai | AI obligation extraction; cross-jurisdiction comparison by topic | Compliance Week |
| CUBE RegPlatform | Acquired Thomson Reuters Regulatory Intelligence and Oden (2024) and Reg-Room; 250+ SMEs; AI regulatory intelligence; 4CRisk acquisition (mapping automation) | insurance-edge 09-Apr-2025; press |
| MetricStream RCM | Regulatory content partnerships (Kinetix) for automatic obligation identification; AI obligation management | metricstream.com |

## C. Design implications captured in P03–P05
1. Obligation metadata must exceed Lawrbit's 60 parameters → owner's 30 template columns + ~40 system fields.
2. Backup owner and auto-transfer on leave (TeamLease) → P04 delegation.
3. Proof checker AI (Komrisk Kompare) → Vidhi evidence-sufficiency check, advisory only (NN-14).
4. Penalty exposure quantification → feeds P20 savings ledger.
5. Change mapping SLA 24–48 h (TeamLease) → LDC target: triage ≤ 1 business day, publish ≤ 3 business days for High.
6. The owner's architecture Part 1 refers to a "31-column schema"; the actual Excel contract is 30 columns (A–AD). Treat the 30-column file as binding; the 31st is the system CompID/version field.
