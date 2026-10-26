# A7_INS — research summary (22 Oct 2026)

41 items: 7 verified, 6 corrected, 7 watch, 13 provisional, 4 counsel sign-off, 3 product decision, 1 vendor confirmation. There are 56 proposed edits, and each `old` string is unique in its file.

**Research limit.** The search budget ran out mid-pass, and IRDAI, India Code and eGazette block automated fetches. So the Health Master Circular paragraphs, the s.64UM threshold, the CPA proviso ordinals, the e-Jagriti date and the *Mahakali Sujatha* and *Harsolia* citations stay provisional. No numbers were invented; these are cited by title and date only.

## Key findings
- **Policy suit-bar clauses: verified (J-002, J-004, J2-195).** For policies issued on or after 8 Jan 1997, Contract Act s.28(b) voids such a clause to that extent. Authorities: *IndusInd Bank* (2016) 9 SCC 720 (the amendment is prospective); *Oriental Insurance v Sanjesh* (SC, 2022); *H P Spinning Mills* (Delhi HC Division Bench, 13 Oct 2025). Pre-1997 policies follow *Sujir Ganesh Nayak*. Label the clock "contestable".
- **MV Act s.166(3): verified (J-060, J2-182/184/189).** In force from 1 Apr 2022 (MoRTH notification of 25 Feb 2022, S.O. 859(E)). On 4 Nov 2025 the SC ordered that no claim be dismissed as time-barred while the challenge is pending (*ICICI Lombard v Ayiti Navaneetha*, SLP(C) 8412-8413/2023; *Bhagirathi Dash*, W.P.(C) 166/2024). It was still pending in Sep 2026. `mact_6m` must stay informational.
- **Insurance Ombudsman.**
  - G.S.R. 864(E) and the Internal Insurance Ombudsman guidelines are still drafts; the CIO lists amendments only to 9 Nov 2023.
  - **Correction (J2-193):** under r.14(1) the complainant may file where they live *or* where the insurer's or broker's branch is.
  - PMJJBY/PMSBY claims are probably covered as group insurance under r.3.
  - **Above ₹50 lakh:** the Rules cap only the award, but the CIO FAQ limits complaints to ₹50 lakh. Show "ombudsman_capped" and list the Consumer Commission or civil court first.
- **SEBI.** The 23 Jul 2026 consultation is confirmed on sebi.gov.in. There is no final circular up to 15 Oct 2026.

## Pack errors found
- **Who pays SEBI arbitration fees (J-132, J-139).** Appendix B (lines 772 and 860) and LR-SEBI-006 say only the initiator pays, and treat "both sides pay" as the 2026 draft. Wrong: Master Circular /195 para 28(c) already requires the initiator **and** the respondent to pay within 7 days. The initiator may pay the respondent's share and recover it.
- **SEBI citations.** The fees are in para 28(b)–(c), not "Annexure A" or "para 8". The circular is dated 31 Jul 2023, as updated on 28 Dec 2023.
- **INS database code (J2-295) refers to columns that do not exist.** `core.proceedings` has no `vertical`, and `core.quote_lines` has no `vertical` or `basis`. A CHECK constraint also cannot read another table. Corrected trigger code on `core.tariff_items` is supplied (`outcome_linked`, or `PCT_OF_AMOUNT` on settlement amounts), and `emergency_arbitration` is added to the retail block.
- **Competitor data (J2-298).** Insurance Samadhan (Fastsurance Consultants Pvt Ltd) now charges ₹999 + 20% + GST (22% at legal level), not ₹500 + 9%. Its domain is `.com`, not `.in` as Appendix T says. ClaimBuddy's site cannot be fetched, so it stays [U].
- **e-Jagriti.** "Launched 7 Sep 2020" is e-Daakhil's date, not e-Jagriti's.

## Launch blockers
- **J2-295:** do not migrate until the corrected triggers pass the NN-18 and INS_R1 tests.
- **Health Master Circular citations (J-096/098, J2-181/185/186/188):** the template lint must block unconfirmed serial and paragraph numbers in party letters.
- **J2-187/196:** the transition rule for pre-2024 health policies needs counsel. Meanwhile compute both regimes; the policyholder-favourable result is an argued position only.
- **SEC payer rule:** fix before `sec_smart_odr_connector` is turned ON. It is OFF now, so this does not block launch.

## "Also check" claims
None falls within A7_INS; not assessed. Rechecks: SEBI, CIO and IRDAI monthly (next 20 Nov 2026); the SC s.166(3) judgment.
