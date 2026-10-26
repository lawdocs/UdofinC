# Phase P15 — Sector Packs and Entity Logic

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, feature flags, bitemporal conventions);
> - **P01** (onboarding wizard, PAN/CIN/GSTIN auto-fetch, legal-entity and group model, users and roles);
> - **P02** (settings registry, three-tier configurability L/G/T, rule-pack engine, terminology/vocabulary packs, menus);
> - **P03** (regulatory content library `cnt`, template registry `tpl`, Excel importer — columns C, D and S feed this phase);
> - **P04** (compliance instances and calendar consume applicability results).
>
> **Sequencing:** P15 sprint 1 freezes the entity taxonomy, the `pack.entity_profile` schema and the applicability-rule DSL, because P04–P14 and P16 read them. P15 runs in parallel with P05–P10; per-family default packs (§4F) are completed family by family as the corresponding content (Part 2 Excel sheets) arrives. P16 (co-operative suite) starts after P15 sprint 2.
>
> **Binding appendices:** E (Excel template contract and entity-family vocabularies — the dropdown values for columns C/D are the taxonomy codes defined here), G (legal and regulatory rules register — every threshold below is an `LR-*` row), H (risk taxonomy and ratio library), I (returns catalogue), S (co-operative law), U (settings catalogue).
>
> **Requirements covered:** R-005, R-007, R-009, R-010, R-012, R-024, R-039, R-056, R-058, R-059, R-060, R-062 (with P16), R-064, R-065, R-066, R-084 (taxonomy side), R-086, R-087, R-093.
>
> **Estimated effort:** 7 two-week sprints for a squad of 8 (taxonomy and rule engine 3; family packs and defaults 3; investment/ARC/listed extensions and UX 2) plus a regulatory content analyst pair (CS + CA) for the family packs.

---

## 1. Objective and business outcome

LawDocsComply is sold to very different organisations: a ₹200 crore NBFC-ICC in the Base Layer, a Tier 3 UCB, a listed HFC, an AIF manager, a GIFT City finance unit, a composite insurance broker, a private limited company with 40 employees, an LLP, or a Maharashtra credit co-operative society with 12 branches. Each has a different regulator (often several), vocabulary, governance organs, mandatory committees, KMP set, returns, calendars and risk profile. This phase delivers the **entity logic layer**: a single, versioned taxonomy and profile, an explainable applicability engine, and **sector packs** that pre-configure each tenant so that a new client sees only what applies to it, with reasons, from the first login — and so that the profile moves automatically and audibly when the entity crosses a threshold or changes category.

| Outcome | Exit-gate measure |
|---|---|
| Right obligations, explained | For the 12 golden entity profiles (§12), the applicability engine selects exactly the expected obligations from the seeded content (precision and recall = 100% against the golden set); every selected or excluded obligation shows a human-readable "why" (rule, attribute, threshold, citation) |
| Separate logic per entity type (R-007) | Departments, committees, KMP roles, vocabulary, dashboards, return calendars, risk taxonomy and Excel template family are seeded from the sector pack in ≤ 60 seconds after profile activation; no NBFC term appears in a co-operative or insurance tenant |
| Thresholds and transitions handled as data | A simulated crossing of ₹1,000 crore assets moves an NBFC-ICC from Base to Middle Layer with an impact report (added/removed obligations, new committees, new returns) and an effective date equal to the date of crossing (SBR para 22), without a code release |
| Multi-regulator entities | A listed NBFC, a UCB (RBI + State Registrar), an IFSC banking unit of an Indian bank, and an NBFC that is also an IRDAI corporate agent each resolve the union of applicable packs with conflicts resolved by the strictest-wins rule |
| Investment, ARC and listed-company extensions | NBFC-ICC/CIC investment-limit monitors, the ARC pack and the listed-company pack (LODR, PIT, SAST, ICDR events) are active for their families and consume Finbyx aggregates where connected |
| Global readiness (D-19) | The jurisdiction-pack framework accepts a non-India pack (EU GDPR overlay used as the pilot) without schema change; no non-India pack is enabled for a tenant unless it is in state `PUBLISHED` with a named reviewer |
| Customisable without super admin (R-024, R-039, R-086) | A client admin can rename departments and committees, add a voluntary obligation ("Suggestive Compliance"), narrow scope with a reason, and adjust KMP sets within the floors; Locked legal floors cannot be loosened by any tenant role (test `NN-28_*`) |

---

## 2. Scope (in / out)

**In scope**
- Entity taxonomy: families, types, sub-types, layers/tiers/categories/size classes, and attributes (§4A–§4B).
- Entity profile per legal entity, bitemporal, evidence-backed, with auto-fetch (P01) and Finbyx/Udofin-fed metrics (§4B).
- Multi-family and group structures (§4C, §4K).
- Applicability rule DSL and engine, explanations, what-if simulator, exemptions and conditional applicability (Excel column S), tenant narrowing/broadening with reasons (§4D).
- Profile-change detection and re-applicability with impact analysis (§4E).
- Sector packs: per-family defaults (departments, committees, KMP sets, calendars, returns, dashboards, risk taxonomy, templates, vocabulary, glossary) (§4F).
- Investment-entity extension (NBFC-ICC investments, NBFC-CIC tests, AIF exposures, IPO and capital-market exposure, REIT/InvIT and SR holdings) consuming Finbyx aggregates (§4G).
- ARC pack and NBFC stressed-asset compliance view (§4H).
- Listed-company pack (LODR, PIT, SAST, ICDR, HVDLE) (§4I).
- Global jurisdiction-pack framework (§4J).
- Pack lifecycle and dependency management with `cnt`, `tpl`, `cfg` (§4L).

**Out of scope (owned elsewhere)**
- Writing the compliance questions themselves (Part 2, Excel sheets; importer in P03).
- Co-operative society day-to-day operations — P16 (this phase supplies the co-operative families and applicability; P16 builds members, elections, AGMs).
- Loan, deposit, trade and valuation processing — Finbyx (NN-23). LDC consumes aggregates and limit-breach events only.
- Board and committee mechanics (P06), risk register and ICAAP calculations (P08–P09), returns preparation (P11), labour and HRMS (P13).
- Licence/registration applications to regulators (CoR, PRAVAAH filings) — LDC prepares checklists and evidence (P04/P11), never submits (NN-08, D-13).

---

## 3. Personas and permissions touched

| Role | What they do in P15 |
|---|---|
| `plt_content_maker` | Authors families, types, attributes, applicability rules, family default packs and jurisdiction packs |
| `plt_content_checker` | Reviews and approves rule and pack versions (maker ≠ checker, NN-05) |
| `plt_content_publisher` | Publishes approved pack versions and schedules effective dates; triggers tenant impact runs |
| `plt_super_admin` | May correct a tenant's profile only by Correction Entry (D-02); cannot bypass Locked floors |
| `ten_admin` | Activates the profile in onboarding, confirms auto-fetched facts, uploads evidence, approves tenant overlays (rename, narrow, broaden) |
| `ten_cco` | Owns applicability decisions, exemption claims, profile-change approvals; signs the applicability statement |
| `ten_kmp` (CFO) | Confirms financial attributes (assets, NOF, deposits, turnover, net worth) each quarter |
| `ten_kmp` (CS) | Confirms corporate attributes (listing status, company class, paid-up capital, group links) |
| `ten_dept_head` | Views applicability for their department; requests narrowing with reasons |
| `ten_internal_auditor`, `ten_external_auditor` | Read-only access to profile history, applicability explanations and exemption evidence |
| `ten_supervisor_view` | Read-only applicability statement and profile as at a chosen date (D-12) |
| `dlv_rm` | Under a tenant grant, prepares profile updates as maker; tenant user is checker (R-072) |
| `svc_vidhi` | Proposes structured conditions from column S text and profile facts from uploaded documents; never activates (NN-04, NN-14) |

---

## 4. Functional requirements

### 4A. Entity taxonomy (family → type → sub-type → layer/tier/category → attributes)

**FR-P15-01 Taxonomy as versioned data.** The taxonomy is held in `pack.entity_family`, `pack.entity_type`, `pack.entity_subtype` and `pack.classification_scheme` (layers, tiers, size classes, categories), each versioned and effective-dated (NN-07). No family, type or layer is hard-coded in application logic; code reads codes from the registry. Adding a new type (for example the SBR Amendment 2026 "Unregistered Type I NBFC") is a Governed content change, not a release.

**FR-P15-02 Seed family catalogue.** Seed the following families. Family codes are binding and are the values used by Appendix E for the `_Template_Info` family field and by column C/D dropdown sets.

| Family code | Regulator(s) | Types (seed) | Classification scheme | Template family (App. E) |
|---|---|---|---|---|
| `BANK` | RBI (DoR, DoS); for RRBs also NABARD | `SCB_PSB`, `SCB_PVT`, `SCB_FOREIGN` (branch / WOS), `SFB`, `PB`, `LAB`, `RRB` | D-SIB flag; listed flag; scheduled flag | `LDC-TPL-RBI-SCB` |
| `UCB` | RBI (BR Act s.56 AACS) + State Registrar or CRCS | `UCB_STATE`, `UCB_MSCS`, `UCB_SALARY_EARNERS`, `UCB_UNIT` | Tier 1–4 (deposits ≤ ₹100 cr; ₹100–1,000 cr; ₹1,000–10,000 cr; > ₹10,000 cr; unit and salary-earner UCBs always Tier 1) [LR-RBI-110] | `LDC-TPL-RBI-UCB` |
| `RCB` | RBI (regulation) + NABARD (supervision, BR Act s.35(6)) + State Registrar | `STCB`, `DCCB` | CAMELSC rating band (NABARD) | `LDC-TPL-RBI-RCB` |
| `NBFC` | RBI (DoR, DoS); HFCs also NHB | `ICC`, `MFI`, `FACTOR`, `IFC`, `IDF`, `HFC`, `CIC_CORE` (Core Investment Company), `P2P`, `AA`, `MGC`, `NOFHC`, `SPD`, `TYPE_I_UNREG`, `S8_MFI_EXEMPT` | Layer BL / ML / UL / TL (SBR paras 8–16) | `LDC-TPL-RBI-NBFC` |
| `ARC` | RBI (DoR, DoS) under SARFAESI s.3 | `ARC` | NOF band (≥ ₹300 cr; ≥ ₹1,000 cr IBC-eligible) | `LDC-TPL-RBI-ARC` |
| `AIFI` | RBI | `NABARD`, `SIDBI`, `EXIM`, `NHB`, `NABFID` | — | `LDC-TPL-RBI-OTH` (AIFI types) |
| `PAY` | RBI (DPSS) | `PA` (online / cross-border / physical), `PPI_BANK`, `PPI_NONBANK`, `PSO_CARD_NETWORK`, `WLAO`, `BBPOU`, `TReDS` | — | `LDC-TPL-RBI-OTH` (payment types) |
| `CIC_INFO` | RBI under CICRA 2005 | `CREDIT_INFORMATION_COMPANY` | — | stub |
| `CCS` (credit co-operative society) | State Registrar (State Act) or CRCS (MSCS Act) | `CCS_STATE`, `CCS_MSCS`, `SALARY_EARNERS_CS`, `URBAN_CREDIT_SOCIETY`, `SOUHARDA_KA`, `MULTIPURPOSE_CREDIT` | MSCS size class Micro/Small/Medium/Large (deposits ≤ ₹10 cr / ≤ ₹100 cr / ≤ ₹500 cr / > ₹500 cr); State audit class A–D | `LDC-TPL-COOP-CCS` |
| `COOP` (other co-operatives) | State Registrar or CRCS; sector departments | `PACS`, `HOUSING`, `DAIRY`, `CONSUMER`, `MARKETING`, `FISHERIES`, `PRODUCER_COOP`, `LABOUR_CONTRACT`, `MULTIPURPOSE`, `FEDERAL` (district/State federations), `MSCS_OTHER` | State/MSCS; audit class | `LDC-TPL-COOP-GEN` |
| `IFSC` | IFSCA | the 33 entity types of the owner's IFSCA list (IBU, IBC, FCFU, ACL, SHL, FME, PENF, MII, BDCM, CUDP, IAPM, INVB, DIST, DTEE, CRA, RESE, ERDP, KRA, ISSU, IIO, IIIO, MGA, BMII, VM, BTCM, PSP, FE, TFIN, ASP, BATF, GIC, EDU, ITFS) grouped by the owner's 13 sectors | sector (owner's column C list) | `LDC-TPL-IFSCA-GEN`, `LDC-TPL-IFSCA-FCFU`, `LDC-TPL-IFSCA-FME` |
| `MF` | SEBI (MF Regulations 2026) | `AMC`, `TRUSTEE_CO`, `MF_LITE_AMC`, `SIF_PLATFORM` | — | `LDC-TPL-SEBI-MF` |
| `AIF` | SEBI (AIF Regulations 2012) | `AIF_CAT_I` (incl. VCF, SVF, infra, social, angel), `AIF_CAT_II`, `AIF_CAT_III`, `AIF_MANAGER`, `AIF_ACCREDITED_ONLY` (LVF / accredited-investor schemes) | Category; large-value fund flag | `LDC-TPL-SEBI-AIF` |
| `LISTED` | SEBI + stock exchanges + MCA | `LISTED_EQUITY_MAIN`, `LISTED_EQUITY_SME`, `LISTED_DEBT_ONLY`, `HVDLE` (listed NCDs ≥ ₹5,000 cr under LODR Reg 15(1A) as amended 2026), `LISTED_CP`, `LISTED_SDI` | Top-1,000 / top-2,000 by market cap (for LODR thresholds), HVDLE flag | `LDC-TPL-SEBI-LISTED` |
| `REIT_INVIT` | SEBI | `REIT`, `SM_REIT`, `INVIT_PUBLIC`, `INVIT_PRIVATE_LISTED`, `INVIT_PRIVATE_UNLISTED`, `REIT_MANAGER`, `INVIT_INVESTMENT_MANAGER`, `TRUSTEE` | — | `LDC-TPL-SEBI-REIT-INVIT` |
| `SEBI_INT` | SEBI | `STOCK_BROKER`, `CLEARING_MEMBER`, `DP`, `AUTHORISED_PERSON`, `IA`, `RA`, `PMS`, `MERCHANT_BANKER`, `RTA`, `CRA`, `DEBENTURE_TRUSTEE`, `CUSTODIAN`, `KRA`, `PROXY_ADVISER`, `BANKER_TO_ISSUE`, `ESG_RATING_PROVIDER`, `OBPP` (online bond platform), `MII` | Qualified Stock Broker flag; size bands per CSCRF (MII, Qualified, Mid-size, Small-size, Self-certification) | `LDC-TPL-SEBI-INT` |
| `INSURER` | IRDAI | `LIFE`, `GENERAL`, `HEALTH_SAHI`, `REINSURER`, `FRB` (foreign reinsurer branch), `LLOYDS_INDIA` | — | `LDC-TPL-IRDAI-INS` |
| `INS_INT` | IRDAI | `BROKER_DIRECT`, `BROKER_REINSURANCE`, `BROKER_COMPOSITE`, `CORPORATE_AGENT` (incl. banks/NBFCs as CA), `IMF`, `WEB_AGGREGATOR`, `TPA`, `SURVEYOR_LOSS_ASSESSOR`, `INSURANCE_REPOSITORY`, `IIB_CONNECTED`, `POSP_ENTITY` | — | `LDC-TPL-IRDAI-INT` |
| `COMPANY` | MCA / ROC under Companies Act 2013 | `PVT`, `PUBLIC_UNLISTED`, `OPC`, `SECTION_8`, `NIDHI`, `PRODUCER_CO`, `GOVT_CO`, `FOREIGN_CO`, `SUBSIDIARY_OF_FOREIGN`, `DORMANT` | Small company (paid-up ≤ ₹10 cr and turnover ≤ ₹100 cr, as raised in Dec 2025 [VERIFY G.S.R.]); thresholds for CSR (s.135), IA (s.138), secretarial audit (s.204), independent directors (Rule 4 Appointment Rules), CFO/CS (s.203), cost audit | `LDC-TPL-MCA-CO` |
| `LLP` | MCA under LLP Act 2008 | `LLP`, `SMALL_LLP`, `FOREIGN_LLP` | Small LLP thresholds [VERIFY current values] | `LDC-TPL-MCA-LLP` |
| `SOCIETY` | State Registrar of Societies | `SRA_1860`, `STATE_SRA` (State amendments, e.g. Karnataka Societies Registration Act 1960), `TRUST_PUBLIC`, `TRUST_PRIVATE` | — | `LDC-TPL-SOC-NPO` (future template; v1.0 uses MCA-CO structure) |
| `PFRDA` | PFRDA | `POP`, `CRA`, `PENSION_FUND`, `RETIREMENT_ADVISER` | — | stub (no content pack in v1.0) |

**Cross-cutting overlays** (attach to any family; each has its own template family and content pack): `OV_DATA` (DPDP Act 2023 and Rules 2025, IT Act 2000 s.43A and SPDI Rules 2011, GDPR, CCPA/CPRA), `OV_CYBER` (CERT-In Directions 2022, sector cyber frameworks — RBI CYB 461 / bank IT governance directions, SEBI CSCRF, IRDAI IS&CS guidelines, IFSCA cyber circulars, ISO/IEC 27001:2022), `OV_LABOUR` (four Labour Codes in force 21 Nov 2025, Central Rules 8 May 2026, State rules; POSH Act 2013), `OV_TAX` (CGST/IGST, Income-tax Act 2025 from 1 Apr 2026), `OV_AML` (PMLA 2002 reporting entities, FIU-IND), `OV_FEMA` (FDI/ODI/ECB reporting where foreign investment or borrowing exists), `OV_ESG` (CSR s.135; BRSR for top-1,000 listed), `OV_CONSUMER` (Consumer Protection Act 2019, e-commerce rules), `OV_MSME` (MSMED Act payment obligations, s.43B(h)-equivalent tax disallowance [VERIFY 2025 Act section]). Overlay applicability is computed from attributes (for example `OV_AML` for every RBI/SEBI/IRDAI/IFSCA regulated entity and for any reporting entity under PMLA s.2(1)(wa)).

**FR-P15-03 Vocabulary and terminology per family.** Each family carries a vocabulary pack registered in `cfg` (P02): for example `customer` = Customer (NBFC), Member (CCS/COOP), Policyholder (INSURER), Unitholder (MF, REIT_INVIT), Investor (AIF), Client (SEBI_INT, IFSC); `governing_body` = Board of Directors / Managing Committee or Board of Directors (co-operatives under State Acts) / Governing Body (SOCIETY) / Designated Partners (LLP) / Trustee (REIT_INVIT, AIF trust); `owners_meeting` = General Meeting / General Body Meeting (AGM, SGM) / Unitholders' Meeting / Partners' Meeting; `constitution` = Articles of Association / Bye-laws / Memorandum and Rules / LLP Agreement / Trust Deed / Investment Management Agreement; `supervisor` = RBI / Registrar of Co-operative Societies / Central Registrar / SEBI / IRDAI / IFSCA / ROC. Labels only; statutory documents and returns keep statutory field names.

**FR-P15-04 Codes and dropdown alignment.** The `pack` registry is the single source for Excel dropdowns in columns C (General Applicability (Layer)) and D (General Applicability (Type)) per template family (Appendix E). When the registry adds a type, the template family's `Rough` list and `_Template_Info` column-contract hash are regenerated by P03 and a new template minor version is published; old templates remain importable under their version (NN-11).

### 4B. Entity profile

**FR-P15-05 Profile record.** One `pack.entity_profile` per legal entity (`core.legal_entity`), bitemporal (`valid_from`, `valid_to`, `recorded_at`, `recorded_by`; NN-07). Attributes are typed rows in `pack.profile_attribute` with `value`, `unit`, `as_of`, `source` (`AUTO_FETCH_MCA`, `AUTO_FETCH_GST`, `FINBYX_FEED`, `UDOFIN_FEED`, `TALLY_IMPORT`, `AUDITED_FS`, `USER_DECLARED`, `REGULATOR_ADVICE`, `AUDITOR_CERTIFICATE`), `evidence_doc_id` (DMS), `confidence`, and `confirmed_by`.

**FR-P15-06 Attribute dictionary (seed; extensible).** Common: legal name, constitution, CIN/LLPIN/registration number, PAN (masked + token, NN-12), GSTIN(s), LEI, date of incorporation/registration, registered office State, operating States, listing status and exchanges, ISINs (count), group id and parent, ultimate holding company, foreign-investment flag and percentage, employee count by State (feeds `OV_LABOUR`), turnover, paid-up capital, net worth, total assets, financial year end, Ind AS/AS framework, auditors.
Family-specific:
- **NBFC:** NBFC type; CoR number/date; deposit-taking flag; public-funds flag (definition SBR para 6(18): excludes instruments compulsorily convertible into equity within 5 years) and evidence; customer-interface flag (para 6(4)); standalone total assets (monthly), last audited assets; group consolidated assets and annual auditor certificate (para 20); date ₹1,000 crore first crossed; layer and source (computed for BL/ML; RBI advice reference and date for UL/TL); UL transition milestones and 5-year floor date (paras 27–28); NOF and glide-path milestone (paras 39–44); PBC test result (para 38); FATF-jurisdiction voting share (para 47); gold-primary flag; FRA registration (Factor); IFC infrastructure-asset share (≥ 75%, para 6(13)); MFI qualifying-asset share (≥ 60%); credit-card issuer flag (drives DPS 462); fixed-point service delivery unit count (MSD 467 Ch II applies at ≥ 10 for ML/UL); credit rating; CRILC reporting status.
- **BANK/UCB/RCB:** licence type, scheduled status, D-SIB, deposits, UCB tier and glide-path end date, PSL achievement, SAF/PCA status, CAMELSC rating (RCBs), area of operation, number of branches.
- **ARC:** NOF, CRAR, number of trusts/schemes, SR outstanding, sponsor list.
- **CCS/COOP:** governing Act and State, registration number and date, area of operation, member count by class, deposits (MSCS size class), audit class by year, managing committee term end date, election authority, financing bank, multi-State flag.
- **SEBI families:** registration number(s) and category, AUM (MF/PMS/AIF), number of schemes, Qualified Stock Broker flag, CSCRF category, top-1,000/2,000 rank (LISTED), HVDLE outstanding listed NCDs.
- **INSURER/INS_INT:** registration code, lines of business, number of tie-ups (corporate agents: up to 9 insurers per line under the 2026 amendment [VERIFY]), premium income.
- **IFSC:** IFSCA registration, activity class, base currency (USD), parent entity and home regulator.
- **COMPANY/LLP:** class flags (small company, OPC, Section 8, Nidhi), CSR applicability inputs (net worth ≥ ₹500 cr or turnover ≥ ₹1,000 cr or net profit ≥ ₹5 cr), borrowings and deposits (for internal-audit and secretarial-audit thresholds) [VERIFY current values in Appendix G].

**FR-P15-07 Auto-fetch and confirmation.** In onboarding (P01) the profile is pre-filled from MCA master data (via licensed provider, P18), GST, regulator registers (RBI NBFC list, SEBI intermediary lists, IRDAI lists, IFSCA register, CRCS MSCS list — by scraping only where terms permit, else user upload), and Finbyx/Udofin for connected tenants. The user confirms or edits each fact; every edit records a reason; facts that drive a Locked classification (layer, tier, size class) need evidence before activation.

**FR-P15-08 Quarterly attestation.** CFO and CS attest the financial and corporate attributes each quarter (default; tenant may shorten). An unattested profile older than 120 days raises a High-priority notification to the CCO and shows a stale banner on the applicability statement.

**FR-P15-09 Finbyx/Udofin-fed metrics.** For connected tenants, `risk_metric_value`, `PositionValued`, balance-sheet aggregates and deposit snapshots (Integration Spec §6.22, §6.24–6.25) update the relevant attributes (total assets, deposits, NOF where computed, investment aggregates) automatically; LDC never receives loan- or member-level personal data for this purpose (NN-23). A Finbyx-fed value that would change a classification is held as `PENDING_CONFIRMATION` until the CFO confirms (§4E).

### 4C. Multi-family entities

**FR-P15-10** A legal entity may hold several family memberships at once (`pack.profile_membership`): for example a listed NBFC (`NBFC` + `LISTED`), a UCB (`UCB` + State co-operative Act), a bank with an IFSC banking unit (`BANK` + `IFSC:IBU` on a separate legal-entity scope), an NBFC that is an IRDAI corporate agent (`NBFC` + `INS_INT:CORPORATE_AGENT`), an HFC with listed NCDs ≥ ₹5,000 crore (`NBFC:HFC` + `LISTED:HVDLE`), a company that is a SEBI-registered IA (`COMPANY` + `SEBI_INT:IA`).

**FR-P15-11 Conflict resolution.** Where two packs impose different values for the same control (for example board-meeting frequency, independent-director share, retention period), the engine applies **strictest-wins** for thresholds and limits and **union** for obligations; it records the binding source per control so that the explanation names both. Where two rules genuinely conflict (cannot both be satisfied), the engine raises a `PACK_CONFLICT` content issue to `plt_content_checker` and shows both obligations to the tenant with a conflict banner until content resolves it.

**FR-P15-12 Primary regulator.** Each entity has one primary regulator for dashboards and calendars; secondary regulators appear as filters and tabs. The CCO may change the primary regulator (Tenant tier).

### 4D. Applicability rule engine

**FR-P15-13 Rule model.** Every obligation in `cnt` (P03) carries an applicability expression in a restricted, side-effect-free DSL (CEL with a whitelisted function set; JSON-logic export) over profile attributes, plus a citation (NN-06). Example:

```
// RBI NBFC Compliance Function Directions 2026 (RBI/DoS/2026-27/460), para 3 — ML and UL only
family == "NBFC" && layer in ["ML","UL"] && !(type in ["TYPE_I_UNREG","NOFHC"])
```

```
// RBI NBFC Fraud Risk Management Directions 2026 (463) — UL, ML, and BL with assets ≥ ₹500 crore (audited 31 March)
family == "NBFC" && (layer in ["ML","UL","TL"] || (layer == "BL" && audited_total_assets_inr >= 500e7))
```

```
// Companies Act 2013 s.135 CSR — any of three thresholds in the immediately preceding FY
family in ["COMPANY","NBFC","BANK","INSURER","LISTED", ...] && is_company &&
  (net_worth_prev_fy_inr >= 500e7 || turnover_prev_fy_inr >= 1000e7 || net_profit_prev_fy_inr >= 5e7)
```

**FR-P15-14 Excel column mapping.** The importer (P03) maps columns C and D to `layer_scope[]` and `type_scope[]` and generates a base expression `family == F && layer in C && type in D`. Column S (Conditional Applicability/Exemptions) is free text written by the content author; Vidhi proposes a structured condition (thresholds, exemptions, dates) from it and the content maker accepts, edits or rejects the proposal (NN-04); until accepted, column S is shown as "conditions to check" on the compliance item and the item applies on the base expression with a `CONDITION_UNSTRUCTURED` flag visible to the CCO, who can confirm "applies / does not apply" with a reason (tenant overlay, NN-03).

**FR-P15-15 Thresholds and dates.** Expressions may reference: attribute values as at a date (`as_of(attr, date)`), audited values (`audited(attr, fy)`), rolling windows, counts (branches, employees per State), date of first crossing (`first_crossed(attr, value)`), RBI-advised flags, and calendar functions (financial year, quarter). Threshold constants are not literals in rules: they are named parameters in `pack.parameter` (for example `NBFC.ML_ASSET_THRESHOLD = 1000e7`, `NBFC.FRM_BL_ASSET_THRESHOLD = 500e7`, `COMPANY.CSR_NET_WORTH = 500e7`) — effective-dated, cited and Locked (L) so that an amendment is a parameter version, not a rule rewrite.

**FR-P15-16 Effective-date semantics.** The engine distinguishes (a) the obligation's own effective period (from the instrument), (b) the entity's classification effective date (for example ML rules apply from the date assets reach ₹1,000 crore, SBR para 22; UL compliance within 24 months of RBI advice, para 27; MSCS size-class change from the approved effective date), and (c) transitional/glide paths (NBFC NOF glide to ₹10 crore by 31 Mar 2027, para 42; UCB 3-year glide on moving up; CRCS CRAR glide to 2028-29). Each compliance instance (P04) stores the classification version that generated it.

**FR-P15-17 Explanations.** For every obligation × entity the engine returns `APPLIES`, `DOES_NOT_APPLY`, `APPLIES_WITH_CONDITIONS`, `EXEMPT` (claimed and evidenced), `NOT_YET_EFFECTIVE`, `TRANSITIONING` with a structured explanation: rule id and version, attributes and values used (with `as_of` and source), parameter versions, citation, and the human sentence ("Applies because your NBFC is in the Middle Layer since 14 Aug 2026, when total assets first reached ₹1,000 crore (SBR para 22)."). The explanation is shown behind the "i" button (P23) and in the applicability statement export.

**FR-P15-18 What-if simulator.** CCO and admins can simulate attribute changes (assets ₹950 → ₹1,050 crore; listing on SME platform; opening a branch in Karnataka; crossing 20 employees in Delhi) and see added/removed obligations, committees, KMP roles, returns and calendar entries before they happen. Simulations never change live data; results can be exported (XLSX/PDF) for board notes.

**FR-P15-19 Exemptions.** An exemption is a structured claim: obligation(s), basis (rule/para), evidence (document, certificate, regulator letter), validity period, approver (CCO; board for material exemptions per tenant setting), and review date. Exempt obligations remain visible with an "Exempt until" badge; on expiry they revert to `APPLIES` and create a task. Platform-defined exemptions (for example CON para 16 single/group limits not applied where the NBFC has no public funds and has issued no guarantees) are evaluated automatically from attributes and re-tested monthly.

**FR-P15-20 Tenant overlays on applicability (R-017, R-086).** Within tier rules (P02): (a) **narrow** — mark an applicable obligation "Not applicable to us" with reason and approver; Locked obligations (statutory, regulator-mandated) can be narrowed only with a documented legal basis and CCO + one other approver, and are flagged in board reports as "narrowed"; (b) **broaden** — adopt an obligation outside scope voluntarily (best practice, group policy, lender covenant) as `Suggestive Compliance`; (c) **re-scope** to departments, branches or legal entities. Every overlay is audit-ledgered (NN-02) and survives platform content updates (NN-03).

**FR-P15-21 Applicability statement.** A versioned, signable document (DOCX/PDF/XLSX) listing every instrument and obligation with status and reason, generated on activation, on every profile change and on demand; signed by the CCO (eSign, D-20) and optionally noted by the board or audit committee. It is part of the export package (NN-10).

### 4E. Profile-change detection and re-applicability

**FR-P15-22 Detectors.** A detector job (`pack.ProfileChangeDetector`, daily 02:00 IST and on every attribute write) evaluates classification rules: NBFC layer (BL ↔ ML on ₹1,000 crore, group consolidation; UL/TL only on recorded RBI advice), NBFC type change (only on recorded RBI CoR change), Type I eligibility (SBR Amendment 2026), UCB tier, MSCS size class, LODR top-1,000/2,000 rank (on exchange list publication), HVDLE status (₹5,000 crore listed NCD outstanding; exit after three consecutive FYs below, with the 2026 one-time proviso for entities that fall out only because of the higher threshold), small-company status, CSR thresholds, employee-count thresholds per State (labour overlay), CSCRF category (SEBI), and any parameterised threshold in `pack.parameter`.

**FR-P15-23 Change workflow.** `DETECTED → IMPACT_ASSESSED → APPROVED → SCHEDULED → ACTIVE`, with `REJECTED` (reason; re-detected at the next run) and `ROLLED_BACK` (only before the first compliance instance under the new version is completed). The impact report lists: obligations added/removed/changed, committees to constitute, KMP roles to appoint, returns added/removed, calendar entries, dashboards, risk taxonomy additions, glide-path milestones and the effective date per rule. Approval: CCO + one KMP (CFO for financial thresholds, CS for corporate thresholds); board noting for layer/tier changes (tenant setting `pack.change.board_noting_required`, default ON for layer/tier). Impact report due within 15 days of detection [REC], escalated to the CCO, then MD/CEO.

**FR-P15-24 No retroactive mutation.** Historic compliance instances, returns and reports stay bound to the classification version of their period (NN-07, NN-29). A back-dated classification correction (for example an auditor certificate shows the ₹1,000 crore crossing two months earlier) creates a Correction Entry (D-02), produces a "gap report" of obligations that applied in the window and were not tracked, and opens remediation tasks — it never rewrites closed items.

**FR-P15-25 Downgrade semantics.** Moving to a lower layer or tier is never automatic where the instrument requires a dispensation (SBR para 23: an NBFC that dips below ₹1,000 crore stays ML until its next audited balance sheet and a specific RBI dispensation; UL floor of 5 years, para 28). The detector flags "eligible to request downgrade" and the obligations stay active until the evidence is recorded.

### 4F. Sector packs: per-family defaults

**FR-P15-26 Pack contents.** A sector pack (`pack.sector_pack`, versioned) bundles for one family (and optionally type/layer): (1) default departments and functions; (2) default committees with terms of reference template, composition rules and meeting frequency; (3) KMP and designated-officer roles with appointment rules; (4) compliance calendar seeds (by reference to `cnt` obligations); (5) returns catalogue subset (Appendix I) and portal map; (6) dashboards and widgets per role (Appendix C); (7) risk taxonomy subset and KRI library (Appendix H); (8) policy register seed (required policies with owner and review frequency; P07); (9) Excel template family (Appendix E); (10) vocabulary pack; (11) glossary entries ("i" help); (12) Vidhi knowledge notebook scope (P17). Applying a pack creates tenant records as **defaults** the tenant may rename, merge, add to or (where Tenant tier) remove; Locked items (for example a statutory committee) can be renamed but not deleted while the obligation applies (NN-28).

**FR-P15-27 Default departments (seed; renameable, R-086).** Owner's IFSCA department list is the base vocabulary: Governance & Administration; Finance, Treasury and Accounts; Legal & Litigation; IT; Operations & Management; HR; Compliance; Returns & Reporting; Risk Management. Family additions:

| Family | Additional default departments / functions |
|---|---|
| NBFC | Credit (Sanction and Underwriting), Collections & Recovery, Internal Audit, Information Security (CISO office), Customer Service & Grievance Redressal, Business/Sourcing, Co-lending & Partnerships, Treasury & ALM, Fraud Risk Management (ML+), Data Protection Office |
| BANK / UCB / RCB | Branch Banking, Credit, Treasury (front/mid/back office), Internal Audit and Inspection, Concurrent Audit, Vigilance, IT & Cyber Security, Customer Service, Priority Sector & Financial Inclusion, Recovery & NPA Management, Deposits and Clearing, Board Secretariat |
| ARC | Acquisitions, Resolution, Trust Accounting & SR Administration, Valuation, Legal (SARFAESI/IBC), Investor Relations (QBs) |
| CCS / COOP | Managing Committee Secretariat, Membership & Share Register, Loans & Recovery, Deposits (where held), Accounts & Audit Compliance, Elections & General Body, Member Services & Complaints |
| MF | Investments (Equity/Fixed Income), Dealing, Risk Management, Operations & Fund Accounting, Investor Services, Sales & Distribution (distributor oversight), Trustee Secretariat |
| AIF | Investment Team, Investor Relations & Drawdowns, Fund Accounting & Valuation, Compliance & Reporting |
| LISTED | Secretarial & Investor Relations, Insider Trading Compliance (PIT designated persons), Stock Exchange Disclosures |
| REIT_INVIT | Investment Management, Asset Management (SPVs/HoldCos), Valuation Liaison, Unitholder Relations, Trustee Liaison |
| SEBI_INT | Operations & Client Onboarding (KYC/KRA), Surveillance, Investor Grievances (SCORES), Cyber Security (CSCRF), Client Funds & Securities Segregation |
| INSURER | Underwriting, Claims, Actuarial (Appointed Actuary), Investments, Distribution/Channel Management, Reinsurance, Policyholder Servicing, Fraud Monitoring |
| INS_INT | Placement/Advisory, Claims Assistance, Principal Officer Office, Training & Certification of persons (Specified Persons), Grievance Redressal |
| IFSC | per owner's IFSCA department list (unchanged) plus Home-Regulator Liaison |
| COMPANY / LLP | Secretarial, Accounts & Taxation, Legal & Contracts, HR & Labour Compliance, Administration |

**FR-P15-28 Default committees (seed; P06 builds the mechanics).** Each committee carries `basis` (rule ids), `mandatory_if` (DSL), composition rules (minimum members, independent/non-executive share, chair rules, quorum), minimum meeting frequency, ToR template id and reporting line. Seed (each row is an `LR-*` in Appendix G; [VERIFY] items are resolved there):

| Family / condition | Committees |
|---|---|
| Companies Act — listed or public company meeting Rule 6 Meetings of Board Rules thresholds (paid-up ≥ ₹10 cr, or turnover ≥ ₹100 cr, or loans/borrowings/deposits > ₹50 cr) | Audit Committee (s.177), Nomination and Remuneration Committee (s.178(1)); Stakeholders Relationship Committee where > 1,000 security holders (s.178(5)); CSR Committee where s.135(1) applies and CSR obligation > ₹50 lakh (s.135(9)) |
| LISTED (LODR) | Audit (Reg 18), NRC (Reg 19), SRC (Reg 20), Risk Management Committee (Reg 21: top 1,000 by market capitalisation and HVDLEs), meeting of independent directors (Reg 25(3)); for HVDLE the Chapter VA set (Regs 62A–62Q) with the ₹5,000 crore threshold from 2026 |
| NBFC — ML/UL (GOV 344 Ch II–IV; CYB 461 Ch V; FRM 463; WD 358) | Audit Committee, NRC, Risk Management Committee, IT Strategy Committee, IT Steering Committee (management), ALCO (management), Special Committee of the Board for monitoring and follow-up of frauds (FRM), Review Committee for wilful-defaulter identification (WD), Customer Service / Grievance committee [REC]; UL adds board-level policy on succession and independent chair rules [VERIFY GOV paras] |
| NBFC — BL | Board-approved policies; Audit Committee and NRC where Companies Act thresholds apply; ALCO for assets ≥ ₹100 crore (ALM Ch II) [VERIFY] |
| BANK | Audit Committee of the Board, Risk Management Committee of the Board, NRC, Customer Service Committee, IT Strategy Committee, Special Committee for Monitoring Large Value Frauds, Review Committee (wilful defaulters), CSR Committee, Stakeholders Relationship Committee (if listed), ALCO and Credit committees (management) |
| UCB | Board of Directors; Board of Management where the UCB's deposits meet the RBI threshold [VERIFY under UCB Governance Directions 2025]; Audit Committee of the Board; Loans Committee; Recovery Committee; IT Steering Committee |
| ARC | Independent Advisory Committee (settlements > ₹1 crore, fraud/wilful-default cases, management changes — ARC paras 45–47, 64–66), Audit Committee, NRC, Risk Management Committee, IT Strategy Committee [VERIFY ARC paras] |
| MF | AMC Board and Trustee Board; Audit Committee (AMC and trustee), Risk Management Committee (AMC and trustee; relaxed for MF Lite), Investment Committee, Valuation Committee, Unitholder Protection Committee [VERIFY under MF Regulations 2026] |
| AIF | Investment Committee (manager); Compliance Officer; trustee oversight where trust form |
| REIT_INVIT (manager) | Audit Committee, NRC, SRC, Risk Management Committee; Investment Committee [VERIFY REIT/InvIT governance regulations] |
| INSURER (IRDAI CG Regs 2024 and Master Circular) | Audit, Investment, Risk Management, Policyholder Protection, Grievance Redressal and Claims Monitoring, NRC, CSR, With-Profits (life), ALM (life) [VERIFY list in the 2024 Master Circular] |
| CCS / COOP (MSCS and State Acts) | Board / Managing Committee; Audit and Ethics Committee (MSCS 2023 amendment) [VERIFY section]; Loans and Recovery Committee; Staff Committee; Election-related committees as required |
| `OV_LABOUR` (any employer) | Internal Committee under POSH s.4 (≥ 10 employees at an office/branch), Grievance Redressal Committee (IR Code s.4; ≥ 20 workers), Works Committee (IR Code s.3; ≥ 100 workers, where ordered), Safety Committee (OSH Code s.22 where notified), Canteen/Welfare committees as notified — built in P13 |

**FR-P15-29 Default KMP and designated-officer roles.** Each role carries `basis`, `mandatory_if`, eligibility checklist (fit-and-proper template for P06), appointment intimation (form/portal and timeline) and conflicts (incompatible roles).

| Family / condition | Roles (seed) |
|---|---|
| COMPANY — Companies Act s.203 and Rule 8 / 8A (listed; public paid-up ≥ ₹10 cr; private paid-up ≥ ₹10 cr for whole-time CS) | MD/CEO/Manager or WTD; Company Secretary; CFO; Independent Directors (s.149(4) listed: one-third; Rule 4 classes: at least two); Woman Director (s.149(1) second proviso, Rule 3) |
| NBFC | Principal Officer and Designated Director (PMLA/KYC 361), Grievance Redressal Officer and Nodal Officer (RBC 362), Internal Ombudsman (IO Directions 2026, where applicable [VERIFY scope]), Chief Risk Officer (ML/UL, GOV), Chief Compliance Officer (ML/UL, CMP 460), Head of Internal Audit (IAF 464 scope), CISO and Head of IT (CYB 461), DPO where SDF or by choice (DPDP) |
| BANK | MD & CEO, WTDs, CRO, CCO, CFO, CISO, CTO/CIO, Head of Internal Audit, Chief of Internal Vigilance, Principal Officer, Designated Director, Internal Ombudsman, Chief Customer Service Officer [VERIFY bank governance directions] |
| UCB | CEO (RBI approval for appointment where required [VERIFY]), Chairman, CCO, CRO (by tier), Principal Officer, Internal Ombudsman (larger UCBs) [VERIFY] |
| ARC | MD/CEO, CRO, CCO, CFO, Chief Valuation Officer [REC], Principal Officer |
| MF | AMC CEO, CIO, CRO, CCO, Fund Managers, Chief Investor Relations Officer; Trustee directors (independent share) |
| AIF | Manager's Key Investment Team, Compliance Officer, Principal Officer (PMLA) |
| LISTED | Compliance Officer (LODR Reg 6, the CS), CFO and CEO certifications (Reg 17(8)), Designated Persons and the Compliance Officer for PIT (Reg 9 code), Investor Relations Officer [REC] |
| INSURER | CEO, CFO, CIO, CRO, CCO, Appointed Actuary, Chief of Internal Audit, CS, Principal Officer, Chief Grievance Officer [VERIFY KMP list] |
| INS_INT | Principal Officer (broker/CA/IMF/WA), Specified Persons, Compliance Officer |
| SEBI_INT | Compliance Officer, Designated Director and Principal Officer (PMLA), CISO (CSCRF), Designated Officer for investor grievances |
| CCS / COOP | Chairperson/President, Vice-Chairperson, Secretary, Treasurer, CEO/Manager, Compliance Officer and Information Officer (MSCS 2023 amendment) [VERIFY sections], Returning Officer (event-based, appointed by CEA/State Election Authority) |
| IFSC | Principal Officer, Compliance Officer, MLRO, Home-Regulator Liaison, as per each IFSCA framework |

**FR-P15-30 Calendars and returns seed.** The pack binds the return subset from Appendix I by family and attributes, for example: NBFC (except HFC) — RBI NBFC Supervisory Returns Directions 2026 (RBI/DoS/2026-27/466) return-wise applicability (para 21), CIC submissions (CIR as amended; incremental files on the 9th, 16th and 23rd and month-end full file from 1 Jul 2026), FIU-IND (CTR/STR/NTR/CBWTR), CKYCR, CERSAI, Form A (statutory auditor certificate) where applicable; HFC — NHB returns; BANK — CB-SR 2026 (37 returns), CRILC; UCB — UCB SR Directions 2026; RCB — NABARD ENSURE plus statutory forms on CIMS; ARC — ARC SR 2026 set; CCS/COOP — Registrar or CRCS returns (annual return within 6 months under MSCS s.120), audit report and rectification (Form O in Maharashtra); LISTED — LODR periodic filings (Reg 13(3), 27(2), 31, 33, 24A, 34), PIT disclosures, SAST Reg 29/30/31; MF — SEBI/AMFI periodic reports; INSURER — IRDAI returns; IFSC — IFSCA returns (USD); COMPANY/LLP — MCA annual filings (AOC-4, MGT-7/7A, DIR-3 KYC, DPT-3, MSME-1, LLP Form 8 and 11). Returns preparation is in P11 (D-05, D-13).

**FR-P15-31 Dashboards seed (per family).** Examples: NBFC — layer status and glide-path milestones, CRAR and Tier 1 (CAP), NOF vs requirement, leverage, CME, ALM buckets and LCR (where applicable), GNPA/NNPA, concentration, compliance heat-map by MD; UCB — tier, CRAR, PSL achievement, SAF/PCA triggers, CRR/SLR; CCS — deposits-eligibility exceptions, CRAR (MSCS), leverage (10×), unsecured ≤ 15%, audit class trend, AGM/election countdowns, director disqualification countdown; LISTED — disclosure clock (Reg 30 within 24 hours / 30 minutes for board outcomes), trading-window status, RPT approvals; MF — scheme limits breaches, TER, stress-test results (liquidity), unitholder complaints; INSURER — solvency ratio, claims ratio, grievance TAT; ARC — NOF, CRAR, trust ageing, planning-period clocks, SR NAV cycle. Ratio definitions live in Appendix H; widgets in Appendix C.

**FR-P15-32 Risk taxonomy seed.** Each family selects a subset of the master taxonomy (Appendix H): banks — full Basel Pillar 1/2 set (credit, market, operational, IRRBB, liquidity, concentration, reputational, strategic, compliance, model, climate); NBFC — credit, concentration, liquidity/ALM, IRR, operational (incl. outsourcing, fraud, IT/cyber), compliance, conduct, reputational, model, group; MF — liquidity, credit, market, operational, conduct, unitholder risk (risk-o-meter); insurer — underwriting, reserving, ALM, investment, reinsurance, operational; CCS — member concentration, liquidity, governance/related-party, fraud, deposit-eligibility, recovery; company/LLP — strategic, operational, legal, people, IT, financial. The CRO can add risks and rename categories (Tenant tier).

**FR-P15-33 Policy register seed.** Each pack seeds the mandatory policy list (owner department, approver, review frequency, citation) for P07; for example NBFC ML: KYC/AML, Fair Practices Code, Grievance Redressal, Credit, Interest Rate Model, Recovery (incl. recovery agents), Outsourcing, IT and Cyber Security, Business Continuity, Fraud Risk Management, Compliance Policy (CMP), Internal Audit (IAF/RBIA), ALM/Liquidity, Investment, Concentration and Large Exposure, Related-party lending, Wilful-defaulter, Resolution of Stressed Assets, Co-lending, Securitisation/Transfer, Dividend, Fit-and-Proper, Board Diversity, Compensation, Succession, Whistle-blower, Data Protection (DPDP), Climate (NBFC-D), Gold Loan (where applicable). Lists for other families are in Appendix G (rule type `POLICY_REQUIRED`).

### 4G. Investment-entity extension (NBFC-ICC, NBFC-CIC, AIF holdings) — R-064

**FR-P15-34 Positioning.** LDC is the **compliance, risk and governance view** of investments; Finbyx (Part 7H IV1–IV7) is the system of record for instrument master, trades, positions, valuation and accounting (NN-23). LDC consumes `PositionValued` (aggregates), `InvestmentLimitBreached`, `LimitBreached`, `risk_metric_value` and the AIF look-through results (Integration Spec §6.22, §6.25). For tenants without Finbyx, LDC accepts a periodic **investment register import** (XLSX/CSV; template `LDC-DT-INVEST-v1.0`: ISIN/identifier, instrument class, issuer PAN/CIN, group flag, quantity, cost, carrying value, fair value and level, classification (AC/FVOCI/FVTPL or AS 13 current/long-term), AIF scheme and corpus, commitment, drawdown, SR scheme and NAV) and computes the same monitors read-only.

**FR-P15-35 Monitors (each an `LR-RBI-*` rule; values are parameters).**

| Monitor | Rule | Basis |
|---|---|---|
| AIF individual exposure | commitment ÷ scheme corpus ≤ 10% | RBI (Investment in AIF) Directions 2025 (RBI/DOR/2025-26/138) para 6(a), from 1 Jan 2026 |
| AIF collective RE exposure | manager attestation that all REs together ≤ 20% of corpus | para 6(b) |
| AIF look-through provision | holding > 5% of corpus and downstream non-equity exposure to a debtor (12-month look-back) → 100% provision on proportionate exposure, capped at direct exposure | para 6(c) [VERIFY final consolidated paragraph numbers] |
| AIF regime tag | `LEGACY_2023` or `AIF_DIR_2025`, irrevocable | paras 2, 8 |
| Capital market exposure | aggregate CME ≤ Board-approved limit; FS para 21(8)(ii) disclosure lines | CON paras 12, 24 |
| IPO financing | ≤ ₹1 crore per borrower | CON paras 11, 24(2); CF para 104 |
| Single / group exposure (ML) | ≤ 25% / 40% of Tier 1 (+5/+10 infrastructure) | CON paras 13, 14(3) |
| UL large exposures | 20% (+5% with Board approval) single; 25% group of eligible capital | CON paras 33–39 |
| NOF deduction | exposures to group, subsidiaries, other NBFCs > 10% of owned funds deducted; AIF look-through for group investments where ≥ 50% of AIF funds from the NBFC | SBR paras 45–46 |
| Investment classification and transfers | inter-class transfers only on 1 April / 1 October with board resolution | INV para 10 |
| CIC tests | group investment ≥ 90% of net assets; group equity (incl. sponsor InvIT units) ≥ 60%; non-group non-financial ≤ 10%; ANW/RWA ≥ 30%; outside liabilities ≤ 2.5 × ANW; ≤ 2 CIC layers; registration if assets ≥ ₹100 cr and public funds | CICD (RBI/DOR/2025-26/367) paras 3, 11, 15–17, 19, 20, 23 |
| CIC governance | Group Risk Management Committee (≥ 5 members, ≥ 2 independent, independent chair, quarterly) | CICD paras 69–71 |
| Derivatives | hedging-only instruments permitted per INV paras 28–34; equity F&O/arbitrage OFF unless board policy + legal opinion recorded | INV; Finbyx IV5.5 |
| SR holdings | QB basis; valuation per TDCR paras 82–86; unredeemed at end of resolution period → loss asset | SARFAESI s.2(1)(u); TDCR |
| REIT/InvIT units held | default non-CME investment exposure; Board flag to treat as CME | Finbyx IV4.4 [VERIFY] |

**FR-P15-36 Investment compliance workspace.** Screens show limit utilisation, breach episodes (OPEN/CURED, passive vs active), regime tags, CIC test trend, board-limit register and evidence (board resolutions, manager attestations, AIF PPMs). Breaches open `ComplianceIssueRaised` (P04) with owner (CFO/Treasury) and due date, and feed ERM (P08) and the CFO dashboard (P09). LDC never places or advises on trades (no investment advice; SEBI IA Regulations).

**FR-P15-37 AIF and other investment vehicles as tenants.** For `AIF`, `MF`, `PMS`, `IFSC:FME` tenants, the pack seeds investment-restriction monitors from their own regulations (e.g., AIF Cat I/II single investee concentration limits, Cat III leverage limits; MF scheme investment limits under the MF Regulations 2026 schedules [VERIFY numbering]) fed by the tenant's fund-accounting system or Finbyx IV6, and SEBI periodic-report calendars.

### 4H. ARC pack and NBFC stressed-asset compliance view — R-065

**FR-P15-38 ARC pack.** Seeds obligations, parameters and monitors from the RBI (Asset Reconstruction Companies) Directions 2025 (DoR.FIN.REC.No.293/26.03.001/2025-26, 28 Nov 2025, updated 10 Mar 2026) and SARFAESI Act 2002 ss.3, 5, 7, 9, 10: NOF ≥ ₹300 crore (paras 14–16), IBC resolution-applicant eligibility at NOF ≥ ₹1,000 crore (para 18), CRAR ≥ 15% (para 93), deposit prohibition (para 23), surplus funds ≤ 10% of NOF (para 21), own-use property ≤ 10% of owned funds and sale of acquired property within 5 years (para 22), board acquisition policy within 90 days of CoR (para 24), due diligence ≥ 2 weeks (para 27), auction-only acquisition from sponsor/related sellers (para 34), one trust per scheme (para 76), SR self-investment ≥ max(15% of transferors' SRs, 2.5% of total) (para 81), planning period ≤ 6 months (para 12), realisation 5 years extendable to 8 by board (paras 35–36), rating within 6 months (paras 82–84), NAV as on 30 June and 31 December (para 90), management-fee rules and reversal after 180 days (paras 142–144), settlement policy and IAC routing (> ₹1 crore, fraud, wilful default) (paras 60–67), FATF < 20% (para 126), disclosures (paras 150, 154), CERSAI/IU filings (paras 158–162). All paragraph numbers are `[VERIFY]` against the signed PDF (Finbyx IP5.1). Consumes `AssetAcquired`, `SecurityReceiptIssued`, `SrNavPublished` from the ARC's Finbyx tenant where connected.

**FR-P15-39 ARC clocks.** Planning-period, rating, NAV-cycle and realisation-period clocks per trust/scheme are compliance instances with owners and escalation at T-30/T-15/T-7 days (tenant may tighten).

**FR-P15-40 NBFC stressed-asset view.** For NBFCs that acquire stressed loans or hold SRs (permitted without issuing SRs), the NBFC pack adds: 6-month minimum holding (TDCR para 74), no re-acquisition from an ARC of loans it transferred (para 87), recoveries first reducing cost and 100% risk weight while standard (paras 76–77), SR valuation (paras 82–86), QB declaration per purchase, board policy on stressed-asset acquisition, and the explicit block that an NBFC may not form trusts, issue SRs or describe itself as an ARC (SARFAESI ss.3, 7, 9). These are shown as guard-rail obligations; enforcement of transactions is in Finbyx (GR-7G-08 to -10).

### 4I. Listed-company pack — R-066

**FR-P15-41 Scope.** Applies to `LISTED` memberships (equity main board, SME platform, debt-only, HVDLE, CP, SDI) and adds: LODR (2015, as amended including the 2025 Fifth Amendment on RPT materiality and the 2026 Amendment notified 20 Jan 2026 — HVDLE threshold ₹5,000 crore under Reg 15(1A), RPT carve-outs, demat-only investor services, director > 75 years needs shareholder approval, HVDLE secretarial audit from FY 2026-27), PIT 2015 (structured digital database, trading window, designated persons, code of conduct, UPSI sharing log, pre-clearance), SAST 2011 (Reg 29, 30, 31 disclosures; open-offer triggers awareness for promoters), ICDR 2018 (post-issue monitoring, monitoring-agency reports, lock-in tracker), Companies Act listed-company provisions, BRSR (top-1,000) and BRSR Core assurance, SEBI SCORES/ODR for investor grievances, Reg 24A secretarial compliance report (signed only by the secretarial auditor or a qualifying peer-reviewed CS from 1 Apr 2025).

**FR-P15-42 Event-driven disclosures.** The pack seeds an **event register** mapping corporate events to disclosures: board meeting outcomes (Reg 30 within 30 minutes of conclusion), material events (Reg 30 within 24 hours; Schedule III Part A deemed-material vs Part B materiality policy), financial results (Reg 33: 45 days of quarter end; 60 days for annual), shareholding pattern (Reg 31), corporate-governance report (Reg 27(2)), RPT disclosures (Reg 23(9)), credit-rating changes, fraud/default disclosures, and record-date intimation [VERIFY each timeline against the consolidated LODR as amended 22 Jan 2026]. Each event creates a clock-owned task (P04) with the disclosure draft generated by Vidhi from the board minutes (P06) for human approval (NN-04, NN-14).

**FR-P15-43 Market-cap rank.** On publication of the exchanges' market-capitalisation lists (as at 31 December, per LODR Reg 3(2)) the rank attribute updates and the detector re-evaluates top-500/1,000/2,000 obligations (RMC, BRSR, dividend distribution policy, D&O insurance for IDs, etc.) with the instrument's own effective-date rule (e.g., "from the following financial year") [VERIFY per regulation].

### 4J. Global jurisdiction-pack framework (D-19)

**FR-P15-44 Model.** `pack.jurisdiction` (ISO 3166 country / sub-national code), `pack.authority` (regulator or legislature), `pack.jurisdiction_pack` (versioned bundle of instruments, families/types mapped to local entity types, vocabulary, calendars, currency, time zone, languages, holidays, reviewer). India is jurisdiction `IN` with authorities RBI, SEBI, IFSCA, IRDAI, PFRDA, MCA, MeitY, CERT-In, MoLE, MoCoop, State Registrars, CBIC, CBDT, FIU-IND.

**FR-P15-45 Enablement gate.** A non-India pack may be enabled for a tenant only when state `PUBLISHED`, with a named qualified reviewer (in-jurisdiction counsel or accredited professional), source register complete (Appendix F), and a "coverage statement" shown to the tenant (what is and is not covered). Until then the pack appears in the catalogue as "Coming soon" and cannot generate obligations (NN-19: no global-coverage claim without evidence).

**FR-P15-46 Pilot overlays.** First non-India packs (content, not code): EU GDPR overlay (for Indian entities offering goods/services to EU data subjects), US CCPA/CPRA overlay, UAE (ADGM/DIFC data protection) and Singapore PDPA as candidates; country entity-type mapping tables allow a foreign subsidiary to be onboarded as a legal entity under a group (§4K) with its own jurisdiction.

**FR-P15-47 Multi-currency, time zone, holidays.** Calendars compute due dates using the jurisdiction's holiday calendar and time zone (IFSC uses IST but USD base currency); amounts carry currency; dashboards show both functional and reporting currency.

### 4K. Group and holding structures

**FR-P15-48** A tenant may contain several legal entities in a group (`core.legal_entity.group_id`), each with its own profile. Group consolidation rules (for example SBR paras 17–21: consolidated assets of all CoR-holding NBFCs in a group, including always-BL entities and certain unregistered CICs, determine ML for ICC/MFI/Factor/MGC members; not used for UL) are computed across the group's profiles with the annual auditor certificate as evidence. Group dashboards aggregate compliance status; data stays scoped by legal entity (NN-01, ABAC in P01). Cross-tenant groups (where group companies are separate tenants) use the Integration Spec `LDC_GROUP` mode (§9.1 there) only with each tenant's recorded consent.

### 4L. Pack lifecycle and dependencies

**FR-P15-49 Lifecycle.** `DRAFT → IN_REVIEW → APPROVED → SCHEDULED → PUBLISHED → SUPERSEDED | WITHDRAWN`, maker ≠ checker ≠ publisher for L-tier content (NN-05). A `STUB` pack (structure without verified content, e.g. most State co-operative Acts) is visible but cannot drive live obligations; activation of a profile that depends on a stub shows "limited coverage" and requires CCO acknowledgement.

**FR-P15-50 Tenant impact runs.** Publishing a pack version runs applicability for every subscribed tenant in a sandbox first, produces per-tenant impact reports, notifies via the **Updates** inbox (NN-27; P05) with "what changed / why it matters / what to do", and applies after the effective date or tenant acceptance (tenant setting: auto-accept non-material changes). Tenant overlays are preserved and re-validated; an overlay that no longer matches (obligation removed/split) is flagged for review, never silently dropped (NN-03).

**FR-P15-51 Dependency graph.** Packs declare dependencies (family pack → overlays → templates → policies → returns). Withdrawing an instrument shows dependent tenant records and requires a migration plan; completed history is retained (NN-29).

---

## 5. Workflows and state machines

### 5.1 Profile activation (onboarding step 3, P01)

`NOT_STARTED → FACTS_PREFILLED (auto-fetch) → FACTS_CONFIRMED (user) → EVIDENCE_ATTACHED (for classification facts) → CLASSIFIED (engine) → APPLICABILITY_PREVIEWED → APPROVED (ten_admin + ten_cco; one person may hold both during a 7-day trial, flagged) → PACK_APPLIED → ACTIVE`

- Guards: classification facts (layer, tier, size class, listing, HVDLE) need evidence or an explicit "declared, evidence to follow within 30 days" acknowledgement that creates a task.
- Timers: save-and-resume for 30 days; reminder at day 3 and day 7 of trial.
- Output: applicability statement v1, seeded departments/committees/roles/calendar/dashboards, Updates entry "Your compliance universe is ready".

### 5.2 Classification change (§4E)

```
on attribute_written(entity, attr):
  for rule in classification_rules.depending_on(attr):
     new = rule.evaluate(profile.as_of(today))
     if new != current_classification(rule.scheme):
        if rule.requires_regulator_advice and not evidence.has(rule.advice_type):
            raise_flag("ELIGIBLE_FOR_CHANGE_ON_ADVICE")   # e.g., UL, downgrade
            continue
        change = ProfileChange(DETECTED, scheme, old, new,
                               effective_at = rule.effective_date(profile))  # e.g. first_crossed date
        impact = applicability.diff(profile, change)       # sandbox run
        change.attach(impact); change.state = IMPACT_ASSESSED
        notify(cco, cfo_or_cs, due = today + 15d)
```

- `APPROVED` requires CCO + CFO (financial) or CS (corporate); board noting for layer/tier when configured.
- `SCHEDULED` applies at 00:00 IST of the effective date; if the effective date is in the past (back-dated crossing), the gap report and remediation tasks are produced (FR-P15-24).

### 5.3 Exemption claim

`DRAFT → SUBMITTED (maker) → REVIEWED (checker ≠ maker) → APPROVED (CCO; board if material) → ACTIVE → EXPIRING (T-30) → EXPIRED | RENEWED | REVOKED`. Expired → obligation reverts to `APPLIES`, task created, Notification to owner.

### 5.4 Tenant overlay on applicability

`REQUESTED (dept head or CCO) → JUSTIFIED (reason, legal basis for Locked items) → APPROVED (CCO; plus second approver for Locked) → ACTIVE → REVALIDATE (on base content change) → CONFIRMED | WITHDRAWN`.

### 5.5 Column-S structuring (content side)

`IMPORTED (text) → AI_PROPOSED (Vidhi, with spans highlighted) → MAKER_ACCEPTED | MAKER_EDITED | MAKER_REJECTED → CHECKER_APPROVED → PUBLISHED_WITH_RULE`. Rejected or unstructured conditions remain as `CONDITION_UNSTRUCTURED` text shown to tenants.

### 5.6 Jurisdiction pack

`PROPOSED → SOURCE_REGISTER_BUILT → CONTENT_AUTHORED → IN_COUNTRY_REVIEW → APPROVED → PUBLISHED → MAINTAINED (monitoring active) → SUSPENDED (monitoring stale > 30 days) → WITHDRAWN`. `SUSPENDED` shows a coverage-warning banner to tenants using it.

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-PACK-01 | Entity profile | Settings › Organisation › Entity profile | Card layout: identity, classification (with "why" chips), regulators, family memberships, attributes with as-of and source icons, attestation status; edit opens a side panel with reason and evidence upload; history tab (bitemporal timeline slider "as at") |
| SCR-PACK-02 | Profile activation wizard | Onboarding › Step 3 Regulatory profile | Auto-fetched facts pre-filled; one question per screen for undetermined attributes (e.g. "Do you accept public funds?" with "i" definition from SBR para 6(18)); live preview of obligation count by regulator |
| SCR-PACK-03 | Applicability explorer | Compliance › Applicability | Table of instruments → obligations with status chips (Applies / Conditions / Exempt / Not yet effective / Narrowed / Suggestive); filters by regulator, department, status, reason type; "Why?" drawer; bulk "request narrowing"; export statement |
| SCR-PACK-04 | What-if simulator | Compliance › Applicability › Simulate | Attribute sliders/inputs; diff view (added in green, removed in grey with history retained); export to board note |
| SCR-PACK-05 | Profile change queue | Compliance › Profile changes | Detected changes with impact summary, due date, approvers, effective date; approve/reject with reason; glide-path chart |
| SCR-PACK-06 | Exemptions register | Compliance › Exemptions | List with basis, evidence, expiry; renew/revoke |
| SCR-PACK-07 | Sector pack overview | Settings › Sector pack | What the pack seeded (departments, committees, roles, returns, dashboards, policies), with tenant changes highlighted; "reset item to pack default"; pack version and pending updates |
| SCR-PACK-08 | Investment compliance | Risk › Investments | Limit utilisation gauges, breach episodes, AIF regime tags and look-through results, CIC tests, board-limit register; source badge (Finbyx / import) |
| SCR-PACK-09 | ARC trusts and clocks | Compliance › ARC › Trusts | Per scheme: planning, rating, NAV, realisation clocks; IAC routing; SR self-investment check |
| SCR-PACK-10 | Listed-company event register | Governance › Listed company › Events | Event → disclosure clock; drafts from minutes; trading-window status; PIT SDD log link |
| SCR-PACK-11 | Group structure | Settings › Organisation › Group | Legal entities tree with classifications; consolidated metrics for group rules; auditor certificate upload |
| SCR-CNT-PK-01 | Taxonomy studio (platform) | Console › Content › Taxonomy | Families/types/schemes/attributes/parameters; versioning; dependency graph |
| SCR-CNT-PK-02 | Rule editor (platform) | Console › Content › Applicability rules | DSL editor with autocomplete on attribute dictionary, test cases (golden profiles), coverage report, column-S proposals queue |
| SCR-CNT-PK-03 | Jurisdiction packs (platform) | Console › Content › Jurisdictions | Pack state, reviewer, source register completeness, coverage statement editor |

UX rules: every classification and status chip has an "i" key (`help.pack.<code>`); fewer clicks — the applicability explorer opens pre-filtered to "Applies — owner missing"; keyboard: `/` search, `w` why-drawer, `s` simulate; empty state for a stub pack: "Limited coverage for <State> co-operative law — we will notify you when the full pack is published"; all screens WCAG 2.2 AA (NN-21); vocabulary pack labels applied everywhere.

---

## 7. Backend design

### 7.1 Modules touched
`pack` (owner), `cnt`, `tpl`, `cfg`, `cmp`, `wf`, `gov`, `erm`, `ral`, `ret`, `int`, `ai`, `rpt`, `core`.

### 7.2 Tables (key columns)

| Table | Key columns |
|---|---|
| `pack.entity_family` | code, name, regulators[], version, valid_from/to, status |
| `pack.entity_type` | family_code, code, name, attributes_required[], version |
| `pack.classification_scheme` | code (NBFC_LAYER, UCB_TIER, MSCS_SIZE, AUDIT_CLASS, LODR_RANK, HVDLE, SMALL_CO, CSCRF_CAT), values[], rule_ids[] |
| `pack.attribute_def` | code, data_type, unit, family_scope[], sensitivity, sources_allowed[], evidence_required |
| `pack.parameter` | code, value, unit, citation_lr_id, tier (L/G/T), valid_from/to, recorded_at |
| `pack.entity_profile` | tenant_id, legal_entity_id, primary_regulator, status, version, valid_from/to, recorded_at |
| `pack.profile_membership` | profile_id, family_code, type_code, subtype_code, registration_no, valid_from/to |
| `pack.profile_attribute` | profile_id, attr_code, value_json, as_of, source, evidence_doc_id, confidence, confirmed_by, valid_from/to, recorded_at |
| `pack.classification` | profile_id, scheme_code, value, source (COMPUTED/ADVICE/DECLARED), effective_from, advice_ref, evidence_doc_id |
| `pack.applicability_rule` | obligation_id (cnt), expr_cel, expr_jsonlogic, rule_version, citation_lr_id, structured_from_column_s (bool) |
| `pack.applicability_result` | tenant_id, legal_entity_id, obligation_id, status, explanation_json, rule_version, profile_version, param_versions[], computed_at |
| `pack.exemption` | tenant_id, obligation_ids[], basis_lr_id, evidence_doc_ids[], valid_from/to, approver_ids[], state |
| `pack.applicability_overlay` | tenant_id, obligation_id, kind (NARROW/BROADEN/RESCOPE), reason, legal_basis, approvers[], state |
| `pack.profile_change` | tenant_id, scheme_code, old, new, effective_at, impact_json, state, approvers[] |
| `pack.sector_pack` | family_code, type_scope[], version, contents_manifest_json, status |
| `pack.pack_seed_record` | tenant_id, pack_version, seeded_object_type, seeded_object_id, tenant_modified (bool) |
| `pack.jurisdiction`, `pack.authority`, `pack.jurisdiction_pack` | iso_code; authority code, type; pack version, reviewer, coverage_statement, state |
| `pack.investment_monitor_result` | tenant_id, monitor_code, value, limit, status, episode_id, source (FINBYX/IMPORT), as_of |
| `pack.arc_scheme_clock` | tenant_id, scheme_id, clock_type, start, due, state |
| `pack.listed_event` | tenant_id, event_type, occurred_at, disclosure_due_at, disclosure_doc_id, state |

All tenant tables carry `tenant_id` with RLS (NN-01); history tables are append-only with Correction Entries (NN-02).

### 7.3 APIs (REST, versioned `/v1`)

- `GET/PATCH /v1/entity-profiles/{legalEntityId}` (PATCH creates a new attribute version with reason)
- `POST /v1/entity-profiles/{id}/activate`, `POST /v1/entity-profiles/{id}/attest`
- `GET /v1/applicability?legalEntityId=&status=&regulator=` ; `GET /v1/applicability/{obligationId}/explain`
- `POST /v1/applicability/simulate` (body: attribute overrides) → diff
- `GET/POST /v1/exemptions`, `POST /v1/exemptions/{id}/approve`
- `GET/POST /v1/applicability-overlays`
- `GET /v1/profile-changes`, `POST /v1/profile-changes/{id}/approve|reject|rollback`
- `GET /v1/sector-pack`, `POST /v1/sector-pack/items/{id}/reset`
- `GET /v1/investment-monitors`, `POST /v1/investment-register/imports`
- Console: `POST /v1/console/taxonomy/*`, `POST /v1/console/applicability-rules/{id}/test`, `POST /v1/console/sector-packs/{id}/publish`, `POST /v1/console/jurisdiction-packs/{id}/publish`

### 7.4 Domain events (CloudEvents `in.lawdocscomply.pack.*.v1`)

`EntityProfileActivated`, `EntityProfileAttributeChanged`, `EntityClassificationChanged` (scheme, old, new, effective_at), `ProfileChangeDetected`, `ProfileChangeApproved`, `ApplicabilityRecomputed` (counts added/removed), `ExemptionApproved`, `ExemptionExpired`, `ApplicabilityOverlayApproved`, `SectorPackApplied`, `SectorPackVersionPublished`, `JurisdictionPackPublished`, `InvestmentMonitorBreached` (mirrors Finbyx `InvestmentLimitBreached` for imported registers), `ListedEventDisclosureDue`. Consumed: Finbyx `PositionValued`, `InvestmentLimitBreached`, `LimitBreached`, `risk_metric_value` updates, `AssetAcquired`, `SecurityReceiptIssued`, `SrNavPublished`; Udofin/Finbyx `MemberAdmitted` (counts only, for co-ops).

### 7.5 Jobs and Temporal workflows

`ProfileChangeDetector` (daily 02:00 IST + on write); `ApplicabilityRecompute` (on pack publish, profile change, overlay change; idempotent per tenant+version); `QuarterlyAttestationReminder`; `ExemptionExpiryWatcher` (daily); `MarketCapRankRefresh` (on list publication); `InvestmentMonitorRun` (on Finbyx event or import; daily for imports); `ArcClockWatcher` (daily); `PackImpactSandbox` (Temporal: per tenant fan-out with progress, retries, compensation).

---

## 8. Integrations (ports and adapters)

- `COMPANY_REGISTRY_PORT` (MCA data via licensed provider; P18) and `GST_PORT` for auto-fetch.
- `REGULATOR_REGISTER_PORT` (RBI NBFC/ARC lists, SEBI intermediary search, IRDAI lists, IFSCA register, CRCS MSCS list): download/upload adapters, never credentialed scraping where terms forbid; results are evidence, user-confirmed.
- `ECOSYSTEM_PORT` (Integration Spec v1.1): Finbyx risk, investments, members aggregates; Udofin LSP-side metrics (D-05, NN-23).
- `MARKET_LIST_PORT`: exchange market-cap lists (public files) for rank.
- `CONTENT_PORT` internal to `cnt`/`tpl` for obligations and template families.

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `pack.profile.attestation_interval_days` | T | 90 | 30–90 | ten_cco |
| `pack.profile.stale_after_days` | G | 120 | 90–180 | plt_content_checker |
| `pack.change.impact_due_days` | T | 15 | 5–30 | ten_cco |
| `pack.change.board_noting_required` | T | true for layer/tier; false otherwise | — | ten_admin |
| `pack.change.approvers` | T | CCO + CFO/CS | ≥ 2 distinct persons | ten_admin |
| `pack.overlay.narrow_locked_second_approver` | L | required | — | — |
| `pack.overlay.broaden_allowed` | T | true | — | ten_cco |
| `pack.exemption.board_approval_material` | T | true | — | ten_admin |
| `pack.exemption.expiry_warning_days` | T | 30 | 7–90 | ten_cco |
| `pack.primary_regulator` | T | from family | any membership | ten_cco |
| `pack.vocabulary_pack` | T | from family | catalogue | ten_admin |
| `pack.updates.auto_accept_non_material` | T | false | — | ten_cco |
| `pack.investment.arbitrage_monitor_enabled` | G | false | requires board policy + legal opinion evidence | ten_cco with CFO |
| `pack.arc.clock_warning_days` | T | [30,15,7] | tighten only | ten_cco |
| `pack.listed.disclosure_warning_minutes` | T | 15 before statutory clock | tighten only | ten_kmp (CS) |
| `pack.jurisdiction.enabled[]` | G | ["IN"] | only PUBLISHED packs | plt_content_publisher + ten_admin |
| `pack.parameter.*` | L | per instrument | — | content team via versioning only |

---

## 10. Security, privacy and audit

- All profile, classification, overlay and exemption writes are audit-ledgered with before/after values (NN-02); super-admin changes only by Correction Entry with dual approval (D-02).
- Financial attributes are `CONFIDENTIAL`; PAN masked (NN-12); evidence documents inherit DMS classification.
- Regulator view (D-12) can show the applicability statement and profile "as at" a date, read-only.
- Explanations must never expose another tenant's data; rule tests use synthetic golden profiles only.
- Applicability results are reproducible: storing rule, parameter and profile versions guarantees the same answer on replay (NN-22).

---

## 11. AI touchpoints and guardrails

- **Column-S structuring:** Vidhi proposes structured conditions with source spans; content maker decides (NN-04).
- **Profile fact extraction:** from uploaded CoR, audited financial statements, auditor certificates, bye-laws or registration certificates, Vidhi proposes attribute values with page citations; user confirms (NN-14).
- **Applicability Q&A:** "Why does the Fraud Risk Management Direction apply to us?" answered only from the stored explanation and cited instrument text (NN-06); if no rule exists, Vidhi says so and offers to raise a content query.
- **Impact narrative:** Vidhi drafts the board note for a layer change from the impact report; human approval required.
- Vidhi never changes a classification, approves an exemption or publishes a pack.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p15/*.feature`)

Golden profiles (synthetic): G1 NBFC-ICC BL ₹420 cr non-deposit with customer interface; G2 NBFC-ICC ML ₹1,250 cr; G3 HFC ML listed NCDs ₹6,000 cr (HVDLE); G4 NBFC-CIC ML; G5 Tier 3 UCB (Maharashtra, State-registered); G6 MSCS credit society Medium (₹320 cr deposits); G7 Maharashtra credit society, audit class B; G8 equity-listed main-board company (rank 820); G9 Category II AIF manager; G10 composite insurance broker; G11 private company small (paid-up ₹2 cr, turnover ₹40 cr, 35 employees in Delhi); G12 IFSC FCFU (branch of an Indian NBFC).

```gherkin
Feature: Applicability engine
  Scenario: ML rules apply from the date of crossing
    Given golden profile G1 with monthly assets reaching 1,000 crore on 14 Aug 2026
    When the profile change detector runs
    Then a profile change BL->ML is detected with effective_at 2026-08-14
    And the impact report lists the Compliance Function Directions 2026 (460) obligations as added
    And no ML obligation is shown as overdue for any date before 2026-08-14

  Scenario: Downgrade requires dispensation
    Given golden profile G2 whose assets fall to 950 crore
    When the detector runs
    Then the classification stays ML
    And the flag "eligible to request downgrade on RBI dispensation" is shown

  Scenario: UL only on RBI advice
    Given golden profile G2 with assets of 40,000 crore
    When the detector runs
    Then no UL classification is created
    Until an RBI advice reference and date are recorded

  Scenario: Strictest-wins across packs
    Given golden profile G3 (NBFC HFC + LISTED HVDLE)
    When applicability is computed for board composition controls
    Then the binding source for each control lists both instruments
    And the stricter independent-director requirement is applied

  Scenario: Column S unstructured condition
    Given an imported obligation with column S "Not applicable to NBFCs without public funds"
    And Vidhi proposed the condition public_funds == true
    When the content maker has not yet accepted the proposal
    Then tenants see the item as "Applies — conditions to check" with the column S text

  Scenario: Tenant narrowing of a Locked obligation needs two approvers
    Given golden profile G11 and a Locked statutory obligation
    When the CCO requests "Not applicable to us" without a legal basis
    Then the request is rejected with LDC-PACK-004
    And with a legal basis it requires a second approver distinct from the CCO

  Scenario: Back-dated classification correction
    Given an auditor certificate shows ML crossing two months earlier than recorded
    When the CCO records the correction
    Then a Correction Entry is written and the original classification history remains visible
    And a gap report and remediation tasks are created
    And no closed compliance instance is modified

  Scenario: Co-operative vocabulary
    Given golden profile G7
    When the user opens the compliance dashboard
    Then labels read "Member", "Managing Committee" and "General Body"
    And no screen shows "Customer" or "Board of Directors" as a label

  Scenario: AIF individual exposure monitor on imported register
    Given golden profile G2 without Finbyx and an imported register with a 55 crore commitment to a 500 crore AIF scheme
    When the investment monitor runs
    Then the AIF individual exposure monitor shows 11% against a 10% limit and opens a compliance issue

  Scenario: Jurisdiction pack gate
    Given the EU GDPR overlay pack is in IN_COUNTRY_REVIEW
    When a tenant admin tries to enable it
    Then the action is refused with LDC-PACK-010 and the pack shows "Coming soon"

  Scenario: What-if does not change live data
    Given golden profile G11
    When the admin simulates 120 employees in Delhi
    Then the diff shows a Works Committee obligation and labour registers added
    And the live applicability is unchanged

  Scenario: Pack update preserves tenant overlays
    Given golden profile G8 with a renamed "Risk & Audit Committee" and a narrowed item
    When a new LISTED pack version is published
    Then the rename and the narrowing persist and the narrowed item is flagged "revalidate"
```

NN tests: `NN-03_pack_update_preserves_overlay`, `NN-07_classification_bitemporal_replay`, `NN-22_applicability_reproducible`, `NN-28_locked_floor_not_loosened`, `NN-29_instrument_removal_keeps_history`, `NN-19_jurisdiction_pack_claim_gate`.

---

## 13. Deliverables and exit gate

1. `pack` schema, migrations (expand-contract), RLS policies and seed taxonomy (all families, types, schemes, attribute dictionary, parameters with `LR-*` citations).
2. Applicability DSL, engine, explanation renderer, simulator; golden-profile test suite G1–G12 green with 100% precision/recall on seeded content.
3. Profile-change detector and workflows; exemption and overlay workflows.
4. Sector packs v1.0 for BANK, UCB, RCB, NBFC, ARC, CCS, COOP, IFSC (GEN, FCFU, FME), MF, AIF, LISTED, REIT_INVIT, SEBI_INT, INSURER, INS_INT, COMPANY, LLP, plus overlays (DATA, CYBER, LABOUR, TAX, AML, FEMA, ESG); stubs for AIFI, PAY, CIC_INFO, SOCIETY, PFRDA.
5. Investment, ARC and listed-company extensions with Finbyx event consumers and the investment-register importer.
6. Jurisdiction-pack framework with EU GDPR overlay as a pilot in `IN_COUNTRY_REVIEW` (not enabled).
7. Screens SCR-PACK-01–11 and console screens; "i" help keys registered (P23); settings registered (P02).
8. Applicability statement export (DOCX/PDF/XLSX) included in LDC-EXPORT-1.0 (P19).
9. Documentation: `docs/packs/taxonomy.md`, `docs/packs/rule-dsl.md`, `docs/packs/<family>.md` per family, `docs/regulations/errata.md` entries.

**Exit gate:** §12 scenarios and NN tests pass; content team signs the seeded parameters against Appendix G; three pilot tenants (one NBFC, one credit society, one private company) activated end-to-end in staging within 60 minutes each.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag | Phase |
|---|---|---|---|---|---|
| OI-P15-01 | UCB Board of Management threshold and status under the UCB Governance Directions 2025 | 2019 BoM guidelines consolidated; current text not read | Content (CS) | Committee seeded as "recommended" until verified | P15 |
| OI-P15-02 | IRDAI CG Regulations 2024 committee and KMP lists | Master Circular text not read in full | Content (insurance) | Seed as `[VERIFY]`; pack stays STUB for INSURER committees | P15 |
| OI-P15-03 | SEBI MF Regulations 2026 regulation numbers (UPC, RMC, investment limits) | New regulations from 1 Apr 2026 | Content (SEBI) | MF pack published with instrument-level citations only | P15 |
| OI-P15-04 | Small LLP thresholds (current) and small-company G.S.R. number (Dec 2025) | Not verified from MCA gazette | Content (CS) | Parameters marked `[VERIFY]`; detector disabled for these two | P15 |
| OI-P15-05 | ARC Directions paragraph numbers | Read from RBI web text, not signed PDF (Finbyx IP5.1) | Content (RBI) | Citations shown at instrument level | P15 |
| OI-P15-06 | Final paragraph numbers of the RBI Investment in AIF Directions as consolidated into Undertaking of Financial Services Directions 2025 | Consolidated text updated 5 Oct 2026 | Content (RBI) | Use July 2025 numbering with note | P15 |
| OI-P15-07 | LODR timelines as amended 22 Jan 2026 (Reg 30, 33, 23(9)) | Consolidated text not fetched | Content (CS) | Event register flagged `[VERIFY]` | P15 |
| OI-P15-08 | REIT/InvIT governance (committees) and SM REIT obligations | Not researched to regulation level | Content (SEBI) | REIT_INVIT pack STUB for governance | P15 |
| OI-P15-09 | CSCRF entity categorisation for SEBI_INT | Category thresholds per CSCRF and clarifications | S6 / content | Category as declared attribute | P12/P15 |
| OI-P15-10 | Regulator register scraping terms (RBI, SEBI, IRDAI, IFSCA, CRCS) | Terms of use | Legal | Upload-only mode | P15/P18 |
| OI-P15-11 | PFRDA intermediary content | Out of v1.0 scope | Product | Family stub only | Later |
| OI-P15-12 | NBFC Internal Ombudsman Directions 2026 scope (which NBFCs) | Instrument not supplied | Content (RBI) | Role seeded as conditional on declared attribute | P14/P15 |

---

## 15. Sources (accessed 25 October 2026 unless stated)

Primary and verified corpus:
1. RBI (NBFC – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025, RBI/DOR/2025-26/339, 28 Nov 2025 — paras 6, 8–48, 49–67 (as read from the official PDF in Finbyx v1.5 Part 8A.25). https://www.rbi.org.in
2. RBI SBR Amendment Directions 2026, RBI/2026-27/43, 29 Apr 2026 (Unregistered Type I NBFC) — Finbyx v1.5 IV5.7.
3. RBI NBFC DoS Directions of 31 Jul 2026: Compliance Function (RBI/DoS/2026-27/460), Cybersecurity (461), Digital Payment Security (462), Fraud Risk Management (463), Internal Audit (464), Statutory Audit (465), Supervisory Returns (466), Miscellaneous Supervisory (467), Auditor's Report (468).
4. RBI NBFC DoR Directions of 28 Nov 2025: Credit Facilities (347), CIR (349 as amended by 117), CRM (350), Concentration (351), TDCR (352), Securitisation (353), Investment Portfolio (354), ALM (355), IRACP (356), RSA (357), WD (358), FS (359), DIV (360), KYC (361), RBC (362), OUT (363), CLM (364), HFC (365), CICD (367), AA (368), MFI (371), MISC (373), GOV (344), CAP (345), BR (342).
5. RBI (Investment in AIF) Directions 2025, RBI/DOR/2025-26/138, 29 Jul 2025.
6. RBI (Asset Reconstruction Companies) Directions 2025, DoR.FIN.REC.No.293/26.03.001/2025-26, 28 Nov 2025 (updated 10 Mar 2026).
7. RBI press release 2025-2026/1588, 28 Nov 2025 — 238 function-wise Master Directions for 11 categories of REs; ~9,445 circulars withdrawn. Secondary: https://teamleaseregtech.com/updates/article/49882/ ; https://www.taxscan.in/top-stories/rbi-issues-238-consolidated-master-directions-9000-circulars-guidelines-reorganised-1439158
8. Commercial Banks — Internal Audit Function Directions 2026 (RBI/DoS/2026-27/413); Supervisory Returns Directions 2026 (RBI/DoS/2026-27/415); Capital Adequacy Directions 2025; ECL Directions (RBI/DOR/2026-27/398) — Finbyx v1.5 Part 8A.37.
9. Multi-State Co-operative Societies Act 2002 (as amended 2023), MSCS Rules 2023; CRCS order L-11012/01/2023-Reg (22 Jan 2024). https://crcs.gov.in
10. SEBI (LODR) Regulations 2015 as amended; LODR (Amendment) Regulations 2026, SEBI/NRO-GN/2026/295, 20 Jan 2026. Secondary: https://blog.ipleaders.in/sebi-lodr-amendment-regulations-2026/
11. SEBI (Mutual Funds) Regulations 2026 (notified 14 Jan 2026; in force 1 Apr 2026). Secondary: https://blog.ipleaders.in/sebi-mutual-funds-regulations-2026/ ; ELP alert 10 Mar 2026.
12. SEBI REIT and InvIT Regulations 2014 as amended; SEBI circular Nov 2025 (REITs as equity-related for MFs from 1 Jan 2026); consultation paper 5 Feb 2026. Secondary: https://vinodkothari.com/2026/02/invits-and-reits-regulatory-actions-for-more-enabling-environment/
13. SEBI (AIF) Regulations 2012; SEBI (PIT) Regulations 2015; SEBI (SAST) Regulations 2011; SEBI (ICDR) Regulations 2018.
14. IRDAI consolidated regulations 2024 (Corporate Governance for Insurers Regulations 2024 and Master Circular). https://policyholder.gov.in/web/guest/regulations2 ; https://www.jsalaw.com/?p=50709
15. IRDAI (Insurance Intermediaries) (Amendment) Regulations 2026, F. No. IRDAI/Reg/8/222/2026, 30 Jul 2026 (Finbyx 8A.37).
16. Companies Act 2013 ss.135, 138, 149, 177, 178, 203, 204; Companies (Meetings of Board and its Powers) Rules 2014 r.6; Companies (Appointment and Qualification of Directors) Rules 2014 r.3–4; Companies (Specification of Definitions Details) Amendment Rules (Dec 2025; small company ₹10 cr / ₹100 cr). Secondary: https://www.taxmann.com/post/blog/mca-raises-small-company-thresholds-to-rs-10-cr-capital-and-rs-100-cr-turnover
17. Infrabyx Ecosystem Integration Specification v1.1 §§6.22, 6.24, 6.25, 9.1 (owner's corpus).
18. Finbyx Master Prompt v1.5 Parts 7G (IP1–IP6) and 7H (IV1–IV7) (owner's corpus).
19. Owner's LawDocs Comply Architecture Part 1 (Primary Regulated Segments; Entity Taxonomy, Table 3-1).

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-38; X-09 (family → template code map, master §1.2), X-10, X-12; D-19 jurisdiction packs**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

