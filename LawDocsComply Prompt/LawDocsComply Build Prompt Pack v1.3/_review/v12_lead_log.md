# v1.2 lead integration log (25 October 2026)

Instruction: rework the Excel templates and the related workflow. The 30-column sheet was a reference only. The rework covers more columns, the instrument name, a per-question update date, family-specific columns and dropdowns, an 8–9-column list view with a CompID pop-up, PDF/Excel export, system-generated CompIDs, stars, conversations, accountability, filter, sort and grouped export, RAG urgency, API onboarding, a Health Check Studio by CompID, the audit trail by CompID, and RiskIDs and GovIDs.

## Streams

| Stream | Scope | Result |
|---|---|---|
| Lead spec | D-49–D-57, NN-56–NN-60, ID formats, 62-column contract, family extension columns, RISK/GOV templates, tool behaviour | `_contrib/v12/LEAD_v12_spec.md` |
| T1 | 29 v2.0 workbooks, builder, validator v2, synthetic list exports, Appendix E Part A | 29/29 PASS (15 tests) |
| T2 | Part-2 commands: 00 rewritten, 01–27 updated, 00A migration, 28 RISK-LIB, 29 GOV-LIB, 99 QA | Done |
| T3 | P04 §4R (FR-P04-200–270), Appendix A §A.46–A.51, Appendix C §C.2A, §C.8.1A, §C.11.12 | Done |
| T4 | P03 CompID generation (FR-P03-100–114) and importer, P05 §4M, P23 §4U Health Check Studio, Appendix P §P.11 | Done |
| T5 | P01 onboarding APIs, Appendix B §B.12 ID registry, P00 FR-P00-70–78, P06 GovID, P08/P09 RiskID, P18 and Appendix L ports, Appendix D §D.19 | Done |

## Lead integration

| Item | Action |
|---|---|
| Master | v1.2 header and change box; NN-35 amended; NN-56–NN-60; §6.7 IDs, list view, drawer and RAG; X-61–X-66; X-08, X-10, X-11, X-29 and X-51 restated for contract v2.0; effort table and Wave 1 sprint plan (S1–S30) |
| `02` | D-49–D-58 (§2.5), NN additions (§3.6), corrections (§3.7), pending owner decisions 20–27, R-112–R-127, review log |
| README | v1.2 change box, template list, validator commands, decisions, coverage, effort |
| Date-order error | P03 V-30 and LDC-TPL-075 corrected to issue ≤ Actionable Last Updated On ≤ Instrument Last Amended On ≤ today; never-amended instruments repeat the issue date (D-58), aligned with Appendix E, Part-2 00 and the validator |
| Screen-ID collision | P03 SCR-TPL-06–08 renumbered SCR-TPL-20–22 |
| Stale v1.0 references | Template paths, validator paths, `30-column` statements and column letters across phases and appendices updated or annotated with v2.0 machine keys (about 90 lines); FR-P04-03 instance reference and FR-P04-100 register export rewritten for v2.0 |
| Catalogue | `LDC_RBI_Directions_Catalogue_v1.2.xlsx`: file names end " v2"; new column AF with 319 proposed instrument short codes (RBI-SCB adds a bank-category letter); instructions updated |
| Cross-file requests | P04 settings `cmp.conversation.guidance_route` and SLA; P13 FR-P13-X03 reporting lines; P28 FR-P28-X02 heat map and exports; P17 FR-P17-70 list skills; Appendix B family short forms; Appendix C §C.3.10 menu additions |
| Compiled registers | B §B.13, C §C.13, U §U.14, V §V.7 (with NN-56–NN-60 index and UAT-V12-01–07), W §W.6 (with the integration resolutions) |
| Phase §16 | v1.2 integration notes in P00, P01, P02, P03, P04, P05, P06, P08, P09, P18, P23, P28 |
| Condensed | Master Prompt and Phase Runbook regenerated as v1.2 |

## Checks

- Validator v2: 29/29 PASS.
- No unbalanced code fences in the pack.
- Every referenced FR ID is defined (2,297 FR IDs).
- Appendix section references resolve, except paragraph-level anchors (A.0.5).
- No reference to the v1.1 catalogue, v1.0 template paths or `_validation_report.md` outside legacy context.
