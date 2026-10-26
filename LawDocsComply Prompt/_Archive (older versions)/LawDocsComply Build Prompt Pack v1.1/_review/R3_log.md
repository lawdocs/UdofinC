# Review log R3 — P06, P07, P10, Appendix J (25 October 2026)

## Fixes applied

| File | Fix |
|---|---|
| P06 | X-04: ESIGN_PORT row rewritten (CCA-empanelled ESPs via ASP adapters incl. Protean); signatures bullet aligned |
| P06 | X-27: export folders `03 Governance/…` replaced with Appendix M names (`05 Governance - Board, Committees and Meetings/`, `06 Company Secretarial - Registers, Filings and Resolutions/`) in §1 outcome table, exit gate item 6, LODR disclosures path and annual report path |
| P06 | X-37: deposit row renamed "Register of deposits" (Rule 14) and separated from the DPT-3 return |
| P06 | PAS-3 due date corrected: 30 days (s.39(4)); 15 days for private placement (s.42(8)) [VERIFY] |
| P06 | NN-36: sealed minutes and attendance registers given DB-level REVOKE UPDATE/DELETE and sealed-row trigger |
| P06 | NN-37: annual-report narrative may not carry AI-supplied figures |
| P06 | NN-43/X-17: delivery-role row (retainer CS) restricted to maker via client-approved grant |
| P06 | X-30: Reg 24A conflict check added to the secretarial auditor workspace (FR-P06-52) |
| P06 | X-01: §7.4 states ecosystem re-publication as `in.infrabyx.governance.*` |
| P06, P07, P10 | OP-1/X-26: §7.1 now states use of shared packages (workflow, notify, calendar, config, docgen, redline, ai, export) |
| P07 | X-27: canonical path example rewritten to Appendix M structure |
| P07 | X-03/NN-41: translation/OCR engine routing via Bedrock India; low-confidence threshold linked to P17 `ai.typecopy.low_confidence_threshold` |
| P07 | NN-43: `dlv_professional` never reviewer/approver/checker of policies |
| P07 | `packages/docx-redline` renamed `packages/redline` (master §5.2) |
| P07 | X-01: §7.4 states `PolicyAttested` and `EvidenceSubmitted` re-published as `in.infrabyx.grc.*` |
| P10 | X-27: FR-P10-88 and §1 portability row rebuilt on Appendix M `10 Audits and Inspections/` structure |
| P10 | X-01: ecosystem audit events typed `in.infrabyx.audit.*` (and `in.infrabyx.grc.*` for ComplianceIssueRaised); internal events `in.lawdocscomply.aud.*` |
| P10 | X-04: ESIGN_PORT row corrected |
| P10 | Income-tax Act 2025 "s.63 / Form 26" marked [VERIFY] in FR-P10-76 |
| J | SEBI MF Regulations 1996 → 2026 (two rows) |
| J | Tax-audit row and ICAI Guidance Note row: ITA 2025 section/form marked unverified |
| J | Added §J.4.0 Ind AS phased applicability table (companies, NBFC phases, banks, insurers, non-company entities) |
| J | Added §J.4.0A ICDS / tax-computation layer |
| J | Added §J.9A co-operative audit and accounting standards |
| J | LLP audit threshold corrected (audit only where both ₹40 lakh turnover and ₹25 lakh contribution exceeded; r.24(8)) |
| J | Open items J-OI-11, J-OI-12 added |

## Checked, no change needed

Companies Act Rule 13 IA thresholds and Rule 9 secretarial-audit thresholds; MCA V3 form timelines (ADT-1, ADT-3, MGT-7, MGT-14, MGT-15, DIR-12, MR-1, DPT-3, MSME-1); SS-1 minutes 15/7/30-day clocks and Rule 25 citation; LODR Reg 17A/26(1) limits; Reg 24A (substituted 12 Dec 2024; ASCR within 60 days); CARO 2020 exclusions; NBFC IAF para 39 no-outsourcing and `ia_contributor` handling; `aud.host.mode` and `owner_system` (NN-39); deterministic redline (NN-37); WOPI/CSPP limitation (X-06); no bulk approval of legal-effect items in these files (NN-46); Markdown tables and headings (no column mismatches, placeholders or duplicate sections).

## Unresolved / for other owners

- Web search budget was exhausted mid-review; RBI bank IA/concurrent direction numbers (413, 409) rely on S5 research notes and remain as researched.
- Appendix M §M.3 should add `06 Company Secretarial - Registers, Filings and Resolutions/Annual Reports/<FY>/` (referenced by P06 FR-P06-54), and its "Register of Directors Interest - MBP-1 disclosures" file name under "Statutory Registers" should be re-labelled as a disclosure index (X-37) — Appendix M owner.
- Many paragraph-level SS-1/SS-2, Director KYC 2025 Rules and ICSI CSAS 2026 citations remain [VERIFY] by design.
