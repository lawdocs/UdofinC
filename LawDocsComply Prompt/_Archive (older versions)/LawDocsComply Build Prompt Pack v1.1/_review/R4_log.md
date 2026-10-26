# Review R4 — P08, P09, P11, Appendix H, Appendix I (25 Oct 2026)

Scope: consistency with master NN-01–NN-46, X-01–X-41 and D-01–D-33; cross-file IDs; regulatory and arithmetic accuracy; Markdown. Web search budget for the session ran out midway; later corrections rely on knowledge already gathered and are marked [VERIFY] where not confirmed.

## Checks that passed (no change needed)
- Every `§H.x` and `§I.x` reference across the pack resolves to an existing heading.
- Metric IDs used in P08/P09 (R1, R50–R53, R57, R58), scenario IDs (SCN-*) and KRI IDs (KRI-*) exist in Appendix H (125 metrics, 46 scenarios, 172 KRIs).
- NBFC PCA thresholds, boundary tests, mandatory actions and exit rule (H.7.1, P09 FR-P09-49/50) match the PCA framework; transitions into or out of PCA need a recorded RBI letter (NN-38).
- Capital minima (NBFC CRAR 15%/Tier 1 10%/UL CET1 9%; bank 5.5/7/9 + CCB 2.5; UCB 9%/12%; ARC 15% and NOF ₹300 crore; CIC 30% and 2.5×; insurer 150%), SLS limits 10/10/20%, LCR haircuts and caps, gold/share/HFC LTVs, DLG 5%, non-MFI microfinance cap 25%, IPO financing ₹1 crore — consistent with the regulatory text as known.
- X-16 host switches (`ral.icaap.host`, `ral.stress.fx_mode`), X-31 (borrower certificates), X-41 (Tally read-only) and NN-39 (mirror Finbyx outputs) already present.
- No broken tables or placeholders in the five files.

## Fixes made
| File | Fix |
|---|---|
| P09 | Data templates duplicated P11's: renamed `LDC-DT-RAL-TB/-LOAN/-EXPOSURE/-FUNDING/-INVEST/-CAP` to P11's `LDC-DT-TB/-LOAN/-EXPO/-BORROWINGS + -DEPOSITS/-INVEST/-CAPITAL`; added a shared-intake note (one upload feeds Return Studio and Lab; aliases `LDC-DT-RAL-TB`, `LDC-DT-INVESTMENTS`) |
| P09 | X-01 event-naming paragraph (cross-product events re-published by `int` as `in.infrabyx.*`) |
| P09 | D-22 now recorded as adopted (FR-P09-07, OI-P09-14); kernel name aligned to `@infrabyx/returns-kernel` + `infrabyx-returns-packs` |
| P09 | §11: ICAAP tracked changes written by the P07 deterministic redline engine, figures bound/lineage-checked (NN-37); closing guardrail cites NN-37/NN-38 |
| P08 | X-01 event-naming paragraph for outbound `erm` events consumed by Finbyx/Udofin/RE GRC destinations |
| P11 | Data-template versions normalised to `-v1.0` |
| P11 | X-01 event-naming paragraph; LDC as producer of `Return*`/`Bureau*`/`FinancialStatementsApproved` flagged as Spec v1.2 change request behind a flag |
| P11 | New FR-P11-37A stating the v1 generation scope (X-32) |
| P11 | §11 AI table: PDF-extracted figures are staging candidates confirmed by a maker against the source page and recorded as human-confirmed extraction (NN-37) |
| P11 | Setting key `returns.kernel.version` → `ret.kernel.version` (module-code rule) |
| P11, I | CIC amendment reference numbers RBI/DOR/2025-26/117 and /119 marked [VERIFY] (numbering inconsistent with the 28 Nov 2025 series) |
| H | SEBI MF Regulations 1996 → SEBI (Mutual Funds) Regulations, 2026 (H.1.2, R87) |
| H | R43 PSL: SFB target 60% of ANBC from FY 2025-26 (75% earlier), [VERIFY] retained |
| H | R47 MFI qualifying assets: 60% recorded as the June 2025 reduction from 75%; OI-H-01 kept open for the paragraph citation |
| H | R24 SICR backstop restated (Ind AS 109 30-DPD presumption; cap [VERIFY]) |
| H | Shared-intake note under H.8.3 data templates |
| I | New §I.14A: FIU-IND (CTR, STR, CCR, NTR, CBWTR, registration), CKYCR, CERSAI, FLA, FC-GPR/FC-TRS/DI, ECB-2, ODI APR — supports FR-P11-48/49 |
| I | DIR-3 KYC periodicity aligned with master §7 (triennial from 31 Mar 2026) |
| I | 31 Jul 2026 repeal reference marked [VERIFY] and linked to press release 2026-2027/787 |

## Unresolved / for other owners
- Appendix U §U.9 and `_contrib/S5_settings.md` still list `returns.kernel.version` (should be `ret.kernel.version`).
- Master X-09 cites `LDC-DT-RAL-TB` and P15 FR-P15-34 cites `LDC-DT-INVESTMENTS` as examples; both are now aliases of `LDC-DT-TB` / `LDC-DT-INVEST`.
- Appendix I: payments bank, LAB, RRB, rural co-operative bank, AIFI and CIC supervisory-returns direction numbers; all SEBI, IRDAI and IFSCA rows remain AU.
- OI-H-01 (MFI qualifying-asset paragraph), PSL targets, R31 related-party thresholds and R24 SICR cap need primary-text confirmation.
