# G1 — second independent error review (P01, P04, P05, P08, P10, P11, P12)

Reviewer: G1 (Indian advocate / legal-tech architect). Date: 25 October 2026. Files read in full: `phases/P01_*`, `P04_*`, `P05_*`, `P08_*`, `P10_*`, `P11_*`, `P12_*`. Governing files read: master §4, §7, §18; `02` §3; Appendices G (LG-001–LG-034, LG-090–LG-099), A §A.8, B §B.1, W §W.9 (LA-01…LA-36 not redone). First-party checks: ipindia.gov.in Trade Marks Rules 2017 page (rr.33, 42, 44–47, 57, 59, 60); services.ecourts.gov.in app help (CNR = 16 alphanumeric characters). The eCourts CIS 3.0 manual was robots-blocked and was not fetched. Scripted checks: every `FR-Pxx-nn` reference in the seven files resolves; appendix `§X.n` references resolve; table column counts are consistent; no doubled words were found.

| ID | File | Location | Error | Fix |
|---|---|---|---|---|
| G1-01 | P01 | §1 | Stated as fact that LawDocs "cannot be" an Aadhaar requesting entity. This ignores the good-governance route (LG-027, 2025 amendment). | Reworded: LawDocs is not one and does not plan to become one; s.57 omitted by the 2019 Amendment Act; the LG-027 route is a long path, never a dependency |
| G1-02 | P01 | FR-P01-20 (logo) | "Regs 251A–253" is an implausible regulation number taken from a secondary source | Converted to `[VERIFY: regulation numbers …]` |
| G1-03 | P01 | FR-P01-34 (POA row) | "a POA itself is never eSigned on LawDocs" contradicts the NN-07 / First Schedule entry 2 carve-out | Limited to signatory POAs; the regulated-entity carve-out is named; Appendix F governs |
| G1-04 | P01 | @P01-AT-03 | Test always stores the last four digits, but FR-P01-20 allows them only where display is required (NN-04) | Last four digits only where the purpose requires display |
| G1-05 | P01 | @P01-AT-04 | Verification row "VL-P01-AVC" does not exist | Now cites W.3 backlog item `V-012` |
| G1-06 | P01 | @P01-AT-07 | Synthetic GSTIN "07ABCDE1234F1Z5": the embedded PAN has fourth character D (not a valid holder type) and the check character is wrong, so it fails FR-P01-26's own validation | Replaced with `07AAACA1234A1ZM` (company PAN, computed check character) |
| G1-07 | P01 | @P01-AT-17 | Non-canonical state "CANCELLED" | `CANCELLED_BY_OWNER` with `LD-KYC-060` (A.8) |
| G1-08 | P01 | FR-P01-50 | Release triggers omit the INACTIVITY trigger that A.8, P01 §5.7 and P04 FR-P04-60 use | INACTIVITY added (no evidence review, per A.8) |
| G1-09 | P04 | FR-P04-60 | "Nominees are notified of designation only if the owner chooses" contradicts A.8 `DESIGNATED → ACCEPTED (nominee OTP)` and FR-P01-49 | Nominee is notified and accepts by OTP; only the personal message can be held back |
| G1-10 | P04 | FR-P04-62 `HC-ESIGN-EXCLUDED` | "ordinary POAs, most NIs" is the pre-LA-22 wording | Aligned with NN-07 carve-out language |
| G1-11 | P04 | FR-P04-58 | "accounts are 18+" cited LG-032 (the Aadhaar s.3A row) | LG-066 cited first |
| G1-12 | P04 | §10 data classes | Claim evidence "visible only to the grievance queue" contradicts FR-P04-61 / A.8 reviewers (F1 corrected the FR, not §10) | Reviewers per A.8; grievance officer only on escalation |
| G1-13 | P05 | FR-P05-01 | DIX job prefix given as `run_`, which is reserved for `ai.runs` (B §B.1; P05 §7.2 uses `dxj_`) | `dxj_` |
| G1-14 | P08 | §1 | S.O. 4720(E) "26 Sep 2022" stated without the unresolved-date caveat (LA-01) | `[VERIFY: Gazette text; dated 26 Sep 2022, published 4 Oct 2022]` |
| G1-15 | P08 | FR-P08-08 | "omitted on 26 Sep 2022" — same issue | Cites S.O. 4720(E) with `[VERIFY/COUNSEL … LA-01]` |
| G1-16 | P08 | FR-P08-10 | User message "A power of attorney can't be signed electronically" is overbroad because of the carve-out (FR-P08-11, @P08-AT-02) | "This power of attorney …", carve-out named |
| G1-17 | P08 | §5.2 DRAFT row | "Created by maker or agent" contradicts §3 and §7.3 (agents get 403 `LD-AGT-007` on `sgn.*` writes; NN-43) | Human maker only; agent drafts arrive as `agt` proposals |
| G1-18 | P10 | §1 | "about 68 consolidated pages" conflicts with FR-P10-01 and X-23 (70) | 70 pages; X-23 cited |
| G1-19 | P10 | FR-P10-11 consumer row | Pecuniary bands with no basis, read as claim value (the LA-02 error) | Value of consideration paid (CPA ss.34(1), 47(1)(a)(i), 58(1)(a)(i); LG-215); Rules title `[VERIFY]` |
| G1-20 | P10 | FR-P10-11 NI row | s.142(2) paraphrased as "court where the payee's bank branch is" | (a) branch where the payee maintains the account through which the cheque was presented; (b) drawer's branch (LA-09) |
| G1-21 | P10 | FR-P10-15 | "Arts. 28–38" for promissory notes and bills of exchange is unconfirmed (Art. 28 is not a negotiable-instrument article) | "Arts. 34–38" plus `[VERIFY article range]` |
| G1-22 | P10 | FR-P10-26 | Type copy "VERIFIED by the user's declaration" conflicts with P05 FR-P05-19 (handwriting for filing needs independent verification, or self-attestation plus zero LOW lines) | Status per FR-P05-19 |
| G1-23 | P10 | FR-P10-26 | Translation annexure label `P-3(E)` conflicts with the P05 FR-P05-22 contract `P-n(Tr)` | `P-3(Tr)` |
| G1-24 | P10 | FR-P10-27 | Header "TYPED COPY …" breaks P05 fixed labels (FR-P05-13/-15/-20; lint `LBL-TC-01`) | P05 fixed "TYPE COPY" header and status labels |
| G1-25 | P10 | FR-P10-28 | "empanelled IT Act s.79A examiner": s.79A examiners are notified, and "LawDocs-engaged" conflicts with the marketplace route | Marketplace expert via P16, preferably a notified s.79A Examiner |
| G1-26 | P10 | @P10-AT-06 | `P-3(E)` | `P-3(Tr)` |
| G1-27 | P11 | FR-P11-08 CNR | Format left open, so a coding agent could build the wrong validator | 16 alphanumeric, no separators (eCourts app help, checked); candidate regex marked `[VERIFY]`, non-blocking until verified |
| G1-28 | P11 | FR-P11-30 SLP-SC | Cited only SC Rules 2013 Order XXII r.2, which covers criminal SLPs | Order XXI (civil) / Order XXII (criminal) `[VERIFY]`; Limitation Act Art. 133 |
| G1-29 | P11 | FR-P11-48 | "Schedule III Part B on litigation" — Part B is not the litigation list | Schedule III Part A (2023 restructuring), `[VERIFY para/item]` |
| G1-30 | P11 | §10 | Counsel "session 30 minutes" contradicts P01 FR-P01-13 (15-minute idle, 8-hour absolute) | Points to P01 values |
| G1-31 | P11 | FR-P11-08 consumer row | e-Jagriti replacement date stated as fact while P10 OI-P10-07 treats it as open | `[VERIFY]` + cross-reference |
| G1-32 | P12 | FR-P12-07 TM-EXAM-REPLY | "30 days" (from LA-04), but the first-party rule says **"within one month from the date of receipt"** (r.33(4)) | One month, computed as a calendar month; r.33(4), (6), r.115 cited |
| G1-33 | P12 | FR-P12-07 opposition rows | Act s.21(1) alone gives 3 months + 1 month extension; the flat 4 months comes from the Rules | s.21(1) read with r.42(1) (checked) |
| G1-34 | P12 | FR-P12-07 counter-statement / evidence / renewal | Rule numbers marked `[VERIFY]`; evidence start events missing | r.44(1), rr.45–47 (with start events and deemed abandonment) and r.57(1) confirmed |
| G1-35 | P12 | FR-P12-07 surcharge / restoration | Rule references missing | r.59 (6 months), r.60 (1 year) confirmed; `[VERIFY]` removed |
| G1-36 | P12 | §1 | "30-day reply window" | "one-month reply window (r.33(4))" |
| G1-37 | P12 | FR-P12-29 | Rectification forum given as High Court only; s.57 allows the Registrar or the High Court | "Registrar or High Court (s.57)"; appeals s.91; IPAB abolished |

## Reported for files not owned by G1

| File | Exact text | Fix |
|---|---|---|
| Appendix G LG-382; Appendix W §W.9 LA-04; `_review/F3_legal_review_log.md` R-8; content deck FP-13 | "30 days from receipt (Trade Marks Rules 2017, r.33)" / "Reply to examination report within 30 days" | "within one month from the date of receipt (Trade Marks Rules 2017 r.33(4); ipindia.gov.in checked 25 Oct 2026)". LA-04 reversed a correct "one month" |
| `01_MASTER_PROMPT.md` §11 port table; `02` CH-29 | "`WORKSPACE_PORT`" | Appendix I, P11, P13 and P19 use `WORKPLACE_PORT`. Choose one name (Appendix I governs ports) and align master/`02`/P16/P18/R/J |
| `phases/P06_*` FR-P06-43 | "(wills, trusts, ordinary POAs, …" | "POAs other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity" (NN-07 / LA-22 wording) |
