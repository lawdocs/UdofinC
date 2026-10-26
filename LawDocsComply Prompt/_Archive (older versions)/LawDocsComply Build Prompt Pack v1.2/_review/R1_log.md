# Review R1 — log (25 October 2026)

Scope: `01_MASTER_PROMPT.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, P00, P01, P02, P24, Appendices A, B, D, Q, U.

| File | Location | Problem | Fix |
|---|---|---|---|
| 01 | §0 working agreement | "Twelve such challenges" — 02 §3.1 lists C-01–C-15 | "Fifteen … `02` §3.1" |
| 01 | §14 performance | Write budget < 800 ms conflicted with P00 FR-P00-50 (≤ 600 ms) | Aligned to P00 (≤ 300/≤ 600 ms at 200 concurrent users per tenant) |
| 01 | §6.6 | Emergency single-approver correction path (P02 FR-P02-67, App A §A.5) not stated; trial-extension mechanism ambiguous | Emergency path (24 h auto-revert unless ratified) and `ENTITLEMENT` correction for trial extensions stated |
| 01 | NN-02 | "Dual-approved" absolute while emergency path exists | Cross-reference to §6.6 emergency path added |
| 01 | §1.4 | `eng_*` staff roles used in P24 missing from role list | Engineering staff roles added |
| 01 | §12 | Export folder list did not match Appendix M §M.3; "99" described as system files (it is "Restricted") | Folder names copied from Appendix M; 99 = Restricted |
| 02 | §9 review log | "Fourteen stream NN proposals" — 27 proposals merged into 14 rules | Corrected |
| P00 | FR-P00-34 table (`requested_by` row) | Unescaped pipe in `PRIOR` \| `POST` broke the table | Replaced with "or" |
| P00 | FR-P00-47 and §9 settings | Upload limit 200 MB, T tier — conflicted with Appendix U core row (G lower-only, 100 MB) | Aligned to `dms.upload.max_mb` G lower-only, default 100 MB |
| P01 | FR-P01-28 | `bil.quote` implied LDC computes price and GST | States OH8 returns prices and tax (X-02) |
| P01 | FR-P01-29 | Trial extension "Correction Entry not needed" contradicted NN-02 and App A §A.17 | Extension via `ENTITLEMENT` Correction Entry with second approver or approved promo rule |
| P01 | §9 settings | Key `bil.trial.days` duplicated P20's `bil.trial.default_days` | Renamed to `bil.trial.default_days` (owned by P20) |
| P02 | §12 tests | `NN-28_statutory_clock_never_pauses` — rule is now NN-33 | Renamed `NN-33_…` (also in App V and `_contrib/S12_tests.md`) |
| P02 | §12 Gherkin, §9 | `LDC-CFG-031` collided with App T's "unsigned rule pack" code | P02 code renumbered `LDC-CFG-080` (also B and `_contrib/S12_errors.md`) |
| A | §A.5 correctable targets | Invoices via credit note without owner | "via OH8 credit note" (X-02) |
| A | §A.17 | Trial extension, checkout (Razorpay webhook to LDC), GST invoice by LDC; trial retention T-tier; exit window default 90 days conflicted with P20 (`bil.exit.read_only_days` default 30) | OH8 payment confirmation and invoice; `ENTITLEMENT` correction; retention per `bil.trial.retention_days`; exit window per P20 key |
| A | §A.18 | Quote tax, payment verification, invoice, payout, credit note attributed to LDC | Attributed to OH8 (X-02) |
| B | B.8 / B.9.3 | `LDC-CMP-013` message allowed bulk approval of Low-risk items (contradicts NN-46) | Message: bulk only for bulk-approvable item types; use Review next |
| B | B.9 intro | Listed B.9.1 ID prefixes and B.9.4 ownership map that do not exist | Intro corrected; pointers to phase §7.2 and `db/ownership.yaml` |
| B | B.9.2/B.9.3 headings | Stream sub-headings at same level as B.9.x | Demoted to `####` (24 headings) |
| B | B.9.3 S1 table | `LDC-TPL-001–011` collided with Appendix E's authoritative `LDC-TPL-001–040`; `LDC-AI-001–004` collided with P17 | Renumbered `LDC-TPL-101–111` and `LDC-CHG-101–104` with a note (also `_contrib/S1_errors.md`; codes are not used inline in P03/P05) |
| B | B.9.3 S3 table | `LDC-DMS-002` defined twice with different wording | Unified as the core code (malware/quarantine) |
| D | D.2.1–D.2.3 | Roles of X-19 (`ten_integration_admin`, `ia_contributor`, `ext_developer`, `plt_web_editor`, `plt_web_publisher`), `anon`, `lead` and `eng_*` missing | Rows added |
| D | D.2.3 `plt_finance` | Described as invoice issuer | Re-described per X-02 / D-28 |
| D | D.10 | `dlv_lead` could add makers without client approval (contradicts NN-43, master §9) | "Propose"; effective only after `ten_admin` approval |
| D | D.10 | Invoices in delivery console unattributed | "issued by OH8, read-only" |
| Q | Q.9 sub-processors | Anthropic API listed for tenant content; Bedrock "if available" (contradicts X-03) | Split rows: Bedrock India default for regulated data, Anthropic API non-personal only |
| Q | Q.9 Jio row | JioBrain/Jio AI as AI provider (contradicts master §7, C-10) | JioCX channels/SIP/Haptik only |
| Q | Q.9 Razorpay row | Merchant agreement implied LDC's own | Through OH8 group merchant account |
| Q | OI-Q-05 | Outdated (Bedrock India now available) | Updated |
| U | §U.9 settings | `ten_cro` (non-existent role) | `ten_kmp` (CRO) |
| U | §U.9 settings | Conflicting duplicates: `dms.upload.max_mb` (T 200 vs G 100), `tpl.import.max_rows` (G 5,000 vs L 2,000 per App E), `ai.enabled` (G vs T), three names for trial days | Aligned to G lower-only 100; L 2,000; T; canonical `bil.trial.default_days` (also `_contrib/S1_settings.md`, `S11_settings.md`) |
| U | §U.0 key rule | Example key `bil.platform.trial_default_days` conflicted with P20 key | Rule reworded without an invented key |
| U | §U.9.1 headings | Stream sub-headings at wrong level | Demoted to `####` (12) |

Verified by web: RBI NBFC Governance Directions reference format "RBI/DOR/2025-26/344 … 28 November 2025" (rbi.org.in, BS_ViewMasDirections id=12960) — master §7 citation style confirmed.

## Issues outside R1 scope for the lead

1. **P04 vs NN-46:** P04 lines on bulk approve (§6 "multi-select submit/approve (Low risk)", SCR-CMP-05 "bulk approve Low-risk", setting `cmp.review.bulk_approve_max_risk`) contradict NN-46 / D-33 unless Low-risk compliance checks are added to `wf.bulk_approvable_sources` (Appendix U default list excludes them). Owner/lead decision; App B message now follows NN-46.
2. **P03 `tpl.import.max_rows` (G 5,000)** conflicts with Appendix E (2,000 rows, LDC-TPL-009); U now says L 2,000.
3. **App T uses `LDC-CFG-031`** (unsigned rule pack) — kept; P02's code moved to 080.
4. **Export folder numbering:** S4 notes asked for `07 Risk Management`/`08 Risk Assessment Lab`; Appendix M uses 08/09 — P08/P09 text should be checked against Appendix M (X-27).
5. **Appendix C §C.9** compiled screen headings likely have the same heading-level issue fixed here in B and U.
