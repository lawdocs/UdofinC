# v1.1 final review (V1) — 25 October 2026

| File | Location | Problem | Fix |
|---|---|---|---|
| appendices/Y | §Y.1 item 5, §Y.14 | G1 proposal numbering (R-103–R-110 with global meanings; X-G1-1…5; "proposed") conflicted with `02` R-103–R-111 | Rewritten as "adopted in master v1.1": NN/D/X cited by final numbers; global needs recorded as R-110.1–R-110.8 under R-110; Lawrbit study = R-111; X-G1 items stated as applied resolutions |
| phases/P25 | header "Requirements covered" | Cited R-103–R-110 with G1 meanings | Now R-110 (with sub-requirements) and R-111 |
| appendices/AB | header | Cited R-103 for the RBI instruction | Now R-108 |
| appendices/AB | AB-D6 | Content waves W1–W3 could be confused with product Waves 1–4 | Clarified |
| 01_MASTER_PROMPT | §2.5 | Lawrbit "reports more than 100 law and accounting firms" overstated the source | Softened to the public claim (legal experts at 100+ law firms across 80+ countries) with case-study description, citing Appendix Y §Y.2 |
| 00_README | §1 Global bullet | Same overstatement | Softened |
| 01_MASTER_PROMPT | §13.1 phase table | Efforts for P03, P04, P05, P06, P07, P10 did not reflect v1.1 phase headers | Updated to 8, 11, 9, 10, 9, 10 sprints |
| 01_MASTER_PROMPT, 00_README, build/condensed11.py | Wave 1 timing | S1–S25 no longer fits enlarged P03–P05 | Wave 1 now about S1–S27 (≈13 months) |
| 01_MASTER_PROMPT | §11 ports | `MCP_SERVER`/`A2A_GATEWAY` not named in Appendix L; `COURT_DATA_PORT` alias unstated | Master points to Appendix L §L.10; alias noted |
| appendices/L | port-name map | Missing master port names | Added `MCP_SERVER`, `A2A_GATEWAY` mapping to §L.10 |
| appendices/C §C.12, U §U.13, B §B.11 | compiled registers | P26/P27 screens, settings and events registered only as ranges | Explicit rows added (24 + 15 screens, 28 + 16 settings, 23 + 13 events) |

**Checks passed:** every NN-01–NN-55, X-01–X-60, D-01–D-48 and R-001–R-111 cited exists (only out-of-range hit was a test fixture id "R-991" in P26 Gherkin — not a requirement); roles in master §1.4 all present in Appendix D; export folders 25–29 match Appendix M §M.3; score names consistent with X-46; README file table matches disk (29 phases, 29 appendices, 29 Part-2 files, 27 templates); validator report 27/27 PASS; Appendix AC totals (938/77/12/42 of 1,069) match README; no broken tables, code fences or placeholders in reviewed files; P25–P28 have §1–§16.

**Catalogue spot-check (rbi.org.in, 25 Oct 2026):** all 35 NBFC DoR titles and "updated as on" dates (did=411) and all 9 NBFC DoS titles, dates and numbers 460–468 (did=427) match the workbook. Headers, dropdowns (status, priority, wave) and mandatory cells complete; Owner/Reviewer/Uploaded columns intentionally blank. Reference numbers other than the NBFC Governance /344 remain [VERIFY on document] as designed.
**Also:** `condensed/` Master Prompt and Phase Runbook regenerated after the master and README edits (wave timing).
