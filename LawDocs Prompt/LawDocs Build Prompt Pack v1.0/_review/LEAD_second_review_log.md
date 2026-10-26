# Lead log — second error review (25 Oct 2026, owner instruction "review, look for the errors and fix them")

**Method.** Scripted checks (tables, code fences, FR/section/error/settings references, ID duplicates, counts) + four independent reviewers with disjoint file ownership: G1 (legal accuracy: P01, P04, P05, P08, P10, P11, P12 — 37 fixes), G2 (legal/commercial: P13–P18 — 29 fixes), G3 (architecture and logic: P00, P02, P03, P06, P07, P09, P19–P23 — 91 fixes), G4 (registries: A, B, C, D, K, R, V, W, Z — 24 fixes). Lead applied the cross-file fixes below.

| # | File | Fix |
|---|---|---|
| L-01 | G LG-382, W §W.9 LA-04, content FP-13 | Trade-mark examination reply restored to "within one month from the date of receipt" — Trade Marks Rules 2017 r.33(4) (IP India text, G1-32); LA-04 reversed; LG-382 marked VERIFIED |
| L-02 | P06 FR-P06-43 | "ordinary POAs" → POAs other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity (First Schedule as amended) |
| L-03 | Appendix L | "Free forever vault" and "safe for life" removed ([OWNER] storage commitment); plan "consults" re-labelled as documentation-team sessions, advocate consultations billed by the advocate (NN-21) |
| L-04 | Appendix R | Removed duplicate P18 `chp.enabled` / `chp.conflict.salt_rotation_days` rows; retired duplicate keys (`drf.free_plan.clean_downloads_per_month`, `mob.min_supported_version`, `eng.logs.retention_days`, `xpt.export.small_company_cooling_minutes`); API deprecation notice ≥ 12 months; added `web.kill.lead_capture`, `.video_embeds`, `.landing_pages` |
| L-05 | W, X | `chp.enabled` → `chp.brand.enabled` |
| L-06 | All files | `WORKPLACE_PORT` unified to `WORKSPACE_PORT` |
| L-07 | Master §6.2 | Status summaries aligned to Appendix A (A.18 documents, A.30 agreements, A.31 signing requests, A.15 items); Appendix A wins |
| L-08 | Master §20 / 02 §2.1 | D-01 → master §5.1; D-09 → master §13 |
| L-09 | Master §11 | `COMPANY_REGISTRY_PORT` → `COMPANY_DATA_PORT` |
| L-10 | Master §13, README | P21 dependency split (P00 shell for cut-over; P06 for Draft-free blocks); P09 workforce L0–L2 slice added to Wave 2 |
| L-11 | Master §0, README §3 | Conventions file committed as `docs/reference/authoring-conventions.md` (cited as "conventions §n"); master wins on conflict |
| L-12 | P04, P05, P08, P10 | API paths `/api/v1/…` → `/v1/…` (P00 FR-P00-19) |
| L-13 | P07, B | Table name unified to `clm.agreements` |
| L-14 | Appendix K | `Drafts not yet negotiated/` path added; individual profile uses `99 System Data (CSV and JSON)/` |
| L-15 | README, 02 | Counts refreshed: 582 phase scenarios, 515 screens, ~1,900 `[VERIFY]`, Appendix Z owner-brief 340 covered / 57 changed / 1 partial / 0 missing |

**Post-fix checks:** every FR ID cited resolves; every `Pxx §n` / `§nX` reference resolves; every settings key in a phase §9 table is in Appendix R; every error code referenced is enumerated in Appendix B §B.5.3 (G4); no unbalanced code fences or table column mismatches; Word editions rebuilt.
