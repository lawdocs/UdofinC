# Lead integration log — LawDocs Build Prompt Pack v1.0 (25 Oct 2026)

1. Plan mode: four rounds of owner questions → D-01…D-13 (02 §2.1).
2. Research R1–R6 (live web; first-party first) → `_research/`.
3. Conventions (`_research/00_Authoring_Conventions.md`) issued before authoring: stack, module codes, IDs, NN-01…NN-50, D-01…D-17, CH-01…CH-32, R-001…R-092, phase template.
4. Authoring: 11 authoring streams (A1–A11) + content deck (C1) + policies (C2); then cross-cutting appendices A, B, C, V, G, W, Z (X1–X4).
5. Cross-file resolutions X-01…X-30 (master §18.1).
6. Mechanical fixes by lead: OVSE keys (`kyc.ovse.*`), `hlp.gen.*`, AI-crawler keys (`web.crawl.ai_*`), `hlp.video.captions_default_on`.
7. Review F1 (P00–P11, A, B, D, K, R), F2 (P12–P23, C, E, H, I, J, L, N, P, Q, T, U, V, X, Y), F3 (legal accuracy: F, G, M, O, S, W, content; 36 findings LA-01…LA-36 in W §W.9).
8. Lead fixes after F3: master §7 Aadhaar s.57 wording and First Schedule exclusions (S.O. 4720(E) [VERIFY]); NN-07 wording; 02 CH-01; P15 pecuniary jurisdiction by consideration paid (FR-P15-35, @P15-AT-14), MV Act s.50 seller/buyer periods (FR-P15-59); P12 30-day examination reply; Appendix L "verified advocates" and consult allowance wording; P13 tests use `int.eco.ldc.sor_mode.governance`; Appendix B §B.4.5 resolved; Appendix R SoR keys tier ENT.
9. Scripted checks: every phase has §1–§13; NN ≤ 50, CH ≤ 32, X ≤ 30; D-xx references outside D-01…D-17 are qualified (`R6 D-xx` data sources, `LDC D-xx`); P26/AA/AC references are to LDC/EQ documents; 0 duplicate settings rows in Appendix R (F1); every referenced error code defined in Appendix B (F1); all 26 appendix letters present.
10. Word editions built with pandoc + house reference document (navy headings, A4, full-width tables): consolidated pack (≈ 1,670 pages), condensed master, runbook, content deck; rendered to PDF and spot-checked.

Known residuals (by design): ≈ 1,600 `[VERIFY]` markers (130 de-duplicated items, Appendix W §W.3); 338 open items (W §W.4); TOC fields in the Word files update on opening (Word: right-click → Update field).
