# 28 — RISK-LIB Command: Platform Risk Library (RiskIDs) *(v1.2 — new)*

**Template:** `templates/LDC-TPL-RISK-v2.0 - Risk Register.xlsx` · **Template code:** `LDC-TPL-RISK-v2.0` · **Owner:** LawDocsComply content team (platform library) · **Use with:** `00_Part2_Master_Command.md` §2, §3, §6A, §8, §12–§15 (paste first), then this file, then one line naming the scope (family and taxonomy codes) and the instruments you are drawing from. As of 25 October 2026.

**v1.2 changes** *(v1.2)* — New command (decision D-57). It writes the **platform risk library**: reusable risk statements, each with a library RiskID assigned by the system, mapped to the Appendix H taxonomy and the Basel / regulatory framework, and linked to the compliance questions (CompIDs) whose controls mitigate them. Tenants copy library risks into their own register, where they get tenant RiskIDs (`RSK-<TENANT4>-<NNNNN>`).

---

## 1. What a library risk row is

One row = **one risk event or condition** that an entity in the scope could face, written so that a Chief Risk Officer can adopt it, rate it and assign it. It is not a compliance obligation (that is a CompID) and not a governance action (that is a GovID). A good risk statement has cause → event → consequence: "Because <cause>, <event> may occur, leading to <consequence>."

Example: "Because collection agents are not trained on the fair-practices code, abusive recovery calls may occur, leading to customer complaints, regulatory penalty and reputational harm."

## 2. Template and groups

The `Risk Register` sheet follows the v2.0 design (row 1 group bands, row 2 headers, data from row 3, `Lists`, `_Template_Info`, `Read Me`, collapsed groups, freeze panes, AutoFilter). Use the exact row-2 headers in T1's template; the groups are:

| Group | Columns (summary) | Who fills in the library |
|---|---|---|
| LIST VIEW | S. No. · RiskID · Risk Title · Risk Category · Department · Risk Owner · Inherent Rating · Residual Rating · Status | Author: S. No., Risk Title, Risk Category, Department, default Inherent Rating. **RiskID blank** (system). Risk Owner, Residual Rating, Status: blank (tenant) |
| SOURCE / TAXONOMY | Taxonomy L1 / L2 code, Basel / regulatory mapping, library RiskID, source instruments | Author (library RiskID column blank — system) |
| ASSESSMENT | Description, causes, consequences, likelihood, impact, scales, appetite / tolerance, KRIs (KRI IDs), controls (Control IDs), linked CompIDs, linked GovIDs | Author: description, causes, consequences, suggested KRIs and controls as text, linked CompIDs and GovIDs where known. Likelihood, impact, appetite: blank (tenant) |
| TREATMENT | Response, action plans, due dates, owners | Blank (tenant), except a suggested default response |
| REVIEW | Last review, next review, trend, comments | Blank (tenant) |
| SYSTEM | Version, RAG | Blank (system) |

## 3. Column rules

| Field | Rule |
|---|---|
| RiskID | **Leave blank.** The system assigns `RSKL-<TAXO>-<NNNN>` on import (e.g. `RSKL-OPR-0107`); never type, copy or reuse one (NN-56). On a re-export it is filled — never edit it. |
| Risk Title | ≤ 120 characters, noun phrase naming the event: "Abusive recovery practices by collection agents". |
| Risk Category | High-level category from the `Lists` sheet (maps to the Appendix H Level 1). |
| Taxonomy code | Appendix H §H.2.1 Level-1 code and Level-2 code, e.g. `CND` / `CND.03 Recovery conduct`. The TAXO segment of the RiskID is the Level-1 code. Use only codes in Appendix H (CRD, CON, CCR, MKT, IRB, LIQ, CAP, OPR, CYB, TPR, MOD, CMP, CND, FRD, STR, REP, GRP, PPL, DPR, RES, ESG, GOV, INS, ARC, FND). |
| Basel / regulatory mapping | From Appendix H §H.3 and §H.5: Pillar 1 / Pillar 2 treatment, the Basel operational-risk event type for OPR / CND / FRD / CYB risks (e.g. "OPR.04 Clients, products and business practices"), and the regulatory hook (e.g. "RBI NBFC Governance Directions 2025 – risk management committee [VERIFY para]"; "ICAAP Part [x]"). |
| Department | The department that owns the risk day to day (same family list as compliance sheets). |
| Description, causes, consequences | Description in 1–3 sentences (cause → event → consequence); causes and consequences as "; "-separated lists. |
| Inherent Rating (default) | High / Medium / Low suggested for a typical entity in the scope, using Appendix H §H.11 scales; tenants re-rate. |
| KRIs | Suggested KRIs by Appendix H §H.8 ID where one exists (e.g. `KRI-CRD-001 GNPA %`), else a description; never invent a KRI ID. |
| Controls | Suggested controls as short imperative phrases; Control IDs are tenant-side (`CTL-…`) and stay blank. |
| Linked CompIDs | CompIDs of published compliance questions whose controls mitigate this risk, "; " separated. Only IDs that exist in the published library; otherwise leave blank and list the intended questions (instrument + para) in the run log so a content curator links them in Content Studio. |
| Linked GovIDs | Library GovIDs (`GOVL-…`) that address the risk (e.g. a Risk Management Committee meeting requirement), same rules. |
| Source instruments | The instruments or standards that make the risk relevant (directions, BCBS principles, ISO 31000), with official links. |

## 4. Linking risks and compliance questions

- Link in both directions: a CompID's **Linked RiskID** column and a risk's **Linked CompIDs** column must agree after import (the system builds the reverse link; author one side and list the other in the run log).
- Link a CompID to a risk only when the obligation's control actually reduces the likelihood or impact of that risk. Reporting rows usually link to `CMP.02` (reporting accuracy); conduct rows to `CND.*`; KYC rows to `FRD.05`; outsourcing rows to `TPR.*`.
- Do not link every compliance row to "regulatory breach". `CMP.01` is the default only for pure filing or registration obligations.

## 5. Coverage and quality bar

- Write per family pack (Appendix H §H.2.2): every core (●) Level-2 code for the family has at least one library risk; optional (○) codes only where relevant.
- 1–3 risks per Level-2 code is typical; avoid near-duplicates (one risk, several causes).
- Every row: taxonomy code, Basel / regulatory mapping, description, causes, consequences, default inherent rating, at least one KRI or control suggestion.
- [VERIFY] markers follow the master command rules.

## 6. Example row (illustrative)

| Field | Example |
|---|---|
| S. No. | 1 |
| RiskID | (blank — system assigns, e.g. `RSKL-CND-0003`) |
| Risk Title | Abusive or coercive recovery practices by collection agents |
| Risk Category | Conduct risk |
| Department | Collections & Recovery |
| Risk Owner / Residual Rating / Status | (blank — tenant) |
| Inherent Rating (default) | High |
| Taxonomy code | CND / CND.03 Recovery conduct |
| Basel / regulatory mapping | Op-risk event type OPR.04 Clients, products and business practices; Pillar 2 scenario; RBI fair-practices and recovery-agent provisions in the 2025 consolidated directions [VERIFY direction and para] |
| Description | Because recovery agents are not trained or monitored, they may harass or threaten borrowers, leading to complaints, RBI penalty and reputational harm. |
| Causes | Incentives tied only to collections; no call recording review; weak agent due diligence |
| Consequences | Customer harm; RBI penalty and directions; media coverage; Ombudsman awards |
| KRIs | Complaints against recovery agents per 10,000 accounts (no seed KRI ID — describe); share of calls reviewed |
| Controls | Agent training and certification; call recording and sample review; time-of-call restrictions; agent empanelment due diligence |
| Linked CompIDs | (CompIDs of the recovery-agent and fair-practices questions once published) |
| Linked GovIDs | (blank) |
| Treatment / Review / System | (blank) |

## 7. File naming

`RISK-LIB - <Family or pack> - <Taxonomy scope> - Risk Library v2.xlsx` (e.g. `RISK-LIB - RBI-NBFC - Conduct and Fraud - Risk Library v2.xlsx`); revisions add ` (rev N)`. Keep `_Template_Info`, `Lists` and `Read Me`.
