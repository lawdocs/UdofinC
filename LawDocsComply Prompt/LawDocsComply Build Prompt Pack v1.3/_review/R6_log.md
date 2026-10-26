# R6 review log — P17–P23, Appendices C, K, L, M, N, O, P, R, X (25 Oct 2026)

| File | Fix |
|---|---|
| P20, U, W, _contrib/S9_* | Setting key `bil.billing_port.adapter` (OH8/LOCAL/MOCK) renamed to master's `bil.billing_port.mode` (OH8/LOCAL_INTERIM/MOCK) everywhere (X-02, master §9). |
| P20 | `Billing/<FY>/` DMS filing path → Appendix M folder `20 Billing, Subscription and Invoices/<FY>/`. Billing ownership text checked: consistent with X-02 (OH8 issues invoices, holds Razorpay; LDC presents/submits). |
| P21 | FR-P21-13: added RBIA outsourcing bar (≥ ₹5,000 cr etc.) and `ia_contributor` co-sourcing (X-30). M1/M2/M3 money and invoice rules checked against X-02, D-06, D-32. |
| P23 | §7.4: added cross-product publication note — Hub-bound events use `in.infrabyx.ops.*` via `int` (X-01) with interim `POST /v1/crm/requests`. |
| P19 | Added FR-P19-10A never-block rule for exports/backups/exit (NN-42). Folder list verified identical to Appendix M. |
| Appendix X | Cross-product event types changed from `in.lawdocscomply.*` to `in.infrabyx.ops.*` (X-01); OI-X-03/X.8.4 rewritten to master D-28 (owner never approves own draft); OH9 citation corrected ("free to professionals" is OH9, not OH9.2); added `POST /v1/trials/extensions` row (master §19); event-namespace note on the register. OH section references (OH1.6, OH2.3, OH3.x, OH4.x, OH6.x, OH8.1–8.10, OH9.x, OH11.6, OH12.x, OH14.6) verified against OH v1.0. |
| Appendix L | New §L.1A path reconciliation: phase §7.3 module-prefixed paths canonical; §L.3 representative/alias; per-phase prefix table (≈ 488 phase-declared operations); precedence sentence amended; MBP-1 removed from register list (X-37); unescaped pipes in table code spans escaped (3 rows). |
| Appendix M | §11 "GST and Tax/" replaced by "Accounts and Tax/<FY>/01–06" sub-tree (to host P11/J financial statements, GST, TDS, MCA data); §23 gained `Data Room/` (P11 raw intake). |
| Other-stream files (folder names, X-27) | P06 `03 Governance` → `05 Governance - …` / `06 Company Secretarial - …`; P08 `07 Risk Management` → `08 …`; P09 `08 Risk Assessment Lab` → `09 Risk Assessments - ICAAP, Stress Tests and Ratios`; P11 `05 Regulatory Returns`/`06 Credit Bureau Reporting`/`07 Accounts and Tax`/`00 Data Room` → folders under `11 Returns and Regulatory Reporting` and `23 …/Data Room`; P16 co-op export list → sub-folders of `15 Co-operative Society Records`; Appendix J `07 Accounts and Tax` → `11 …/Accounts and Tax`. (P10 `08 Audit` was already fixed by another reviewer.) |
| Appendix C | Duplicate screen IDs resolved: P00 keeps SCR-CORE-01–09; shell screens renumbered SCR-CORE-20 (palette), -21 (global search), -22 (context switcher); Work Inbox SCR-WF-00 (Calendar keeps SCR-WF-01); SCR-TPL-01–04 declared one screen each (P03 labels, App E content). Tokens verified by computation (#8A6D2B 4.88:1, #B45309 5.02:1, #64748B 4.76:1). |
| Appendix N | ADD-REG pack codes aligned to Appendix E template families (X-09); "e-voting of resolutions by circulation" → circular resolutions under s.175. |
| Appendix O | §O.8: added rows for RBIA-bound full IA outsourcing bar and LODR Reg 24A secretarial-audit conflict (X-30). |
| Appendix P | §P.3.1: added column mapping the 12 health-check families to the 24 template families + note. |
| Facts spot-checked (web) | E-Commerce (Amendment) Rules 2026 exist (Sep 2026); Google FAQ rich results ended 2026; ICAI 2019 aggregator bar; Bedrock India route; s.52 TCS 0.5%; WCAG 2.2 SC numbers. Web search budget exhausted before TallyPrime 7.0 JSON claim could be re-checked (it carries a Tally help-site source in P18). |

## For the lead (outside R6 files)

1. Master X-26 and P04 §16 still name SCR-WF-01 / SCR-CORE-02 as Work Inbox / global search — should read **SCR-WF-00** and **SCR-CORE-21** (Appendix C §C.9).
2. Master §12 says folder `99` is "for system files"; Appendix M §M.3 names it **99 Restricted** (encrypted sealed classes). Master §12 summary list also differs in wording from M (authoritative per X-27).
3. Master §9 billing bullet: key name now matches (`bil.billing_port.mode`); P20 uses value `LOCAL_INTERIM`.
4. Appendix U and W were edited by search-replace only (setting key rename); if another reviewer rewrote those files concurrently, re-apply the rename.
