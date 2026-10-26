# F3 — Legal-accuracy review log (25 Oct 2026)

**Reviewer role:** senior Indian legal-tech reviewer (advocate's eye), independent of the authors.
**Scope read:** `_research/00_Agent_Brief_Common.md`; `01_MASTER_PROMPT.md` §4 (NN-01…NN-50) and §7; `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` §3 (CH-01…CH-32); Appendices F, G, M, O, S, W; `content/LawDocs_Website_Content_v1.0.md`. Spot checks in R2, R3, R5, P12, P15 and Appendix L.
**Files edited (owned):** `appendices/F_*.md`, `appendices/G_*.md`, `appendices/M_*.md`, `appendices/O_*.md`, `appendices/S_*.md`, `appendices/W_*.md` (new §W.9 and a W.8 change-log row), `content/LawDocs_Website_Content_v1.0.md`.
**Findings register:** Appendix W §W.9, LA-01…LA-36.

## 1. Method and limits

- The base was R2 and R3 together with the reviewer's knowledge of the statutes. Every edit kept or added `[VERIFY]` where first-party text was not seen.
- **Web budget.** The shared WebSearch limit was exhausted when the review began: the first search returned "budget used up". No further searches were attempted. Three WebFetch calls were made on URLs already cited in R3 or returned by a fetch:
  1. `leegality.com/blog/first-schedule` (retrieved). It says the October 2022 amendment removed demand promissory notes (DPNs) and bills of exchange in favour of regulated entities, POAs empowering regulated entities, and contracts for the sale or conveyance of immovable property from the exclusions.
  2. `vinodkothari.com/tag/power-of-attorney/`, which leads to "Expanding the ambit of IT Act…", 12 Oct 2022 (retrieved). It confirms that entry 5 was omitted, that entry 2 carves out POAs empowering RBI/NHB/SEBI/IRDAI/PFRDA-regulated entities, and that entry 1 extends to DPNs/BoEs in favour of such entities. No notification number or date is given in the text. It links e-Gazette PDF 239378.
  3. `egazette.nic.in/WriteReadData/2022/239378.pdf` (blocked by robots; not retrieved).
- **Result on the First Schedule.** The substance in R3 LG-003 and App F L1 is corroborated by two independent secondary sources. The S.O. date (26 Sep 2022) against the Gazette publication date (4 Oct 2022) is unresolved, and the Gazette text stays `[VERIFY]`. Master §7 is right to keep `[VERIFY]` on "property-sale contracts no longer excluded".

## 2. Corrections applied (owned files)

| File | Change | W.9 ID |
|---|---|---|
| F §1 L1 | S.O. date vs Gazette date flagged; source note records the two secondary sources | LA-01 |
| F §1 L18 | MV Act s.50 transferor 14/45 days, transferee 30 days, s.50(2) with CMVR r.56 | LA-03 |
| F IF-42, IF-49 | *Suraj Lamp* (2012) 1 SCC 656; *In re: Interplay* 2023 INSC 1066 [VERIFY] | LA-27 |
| G LG-003 | Status note: Gazette text pending | LA-01 |
| G LG-023 | *Puttaswamy* citation; "omitted", not "struck" | LA-21 |
| G LG-071 | DPDP penalty heads completed (₹150 crore SDF; ₹10,000 Data Principal) | LA-28 |
| G LG-215 | Pecuniary jurisdiction by consideration paid; Rules title | LA-02 |
| G LG-261, LG-265 | Citations | LA-27 |
| G LG-316 | LLP Act s.11(1)(c) | LA-20 |
| G LG-382 | TM examination reply 30 days | LA-04 |
| G LG-400 | MV Act s.50 transferor/transferee clocks; basis s.50 + rr.55–56 | LA-03 |
| G G.24.2 | Change-log row v1.0.1 | — |
| M MP-LD-03, M.19 | "verified professionals/advocate" removed | LA-19 |
| M M.4, M.15.3 | RCM/exemption wording for advocates' services | LA-18 |
| O POL-LD-01 §5.3 | Last-four retention tagged [INTERP; COUNSEL] | LA-29 |
| O POL-LD-03 §6.1 | Amendment cited by S.O. number, date [VERIFY] | LA-01 |
| O POL-LD-03 §6.2 | s.49 effect of non-registration; s.17(1A)/s.53A; yearly-rent leases | LA-12 |
| O POL-LD-03 §6.4 | Attestation examples (TPA ss.59, 123; ISA s.63) | LA-08 |
| O POL-LD-05 §1 | E-Commerce Rules r.4(10) | LA-31 |
| O POL-LD-13 | Hosting claim gated; CERT-In scope | LA-32 |
| S CHR-CC-01, CHR-B-05, F-09 | Consideration-paid test; F-09 re-routed to District Commission | LA-02 |
| S CHR-D-02, F-11, F-12 | Seller and buyer clocks under s.50 | LA-03 |
| Content (multiple) | LA-05…LA-11, LA-13…LA-17, LA-23…LA-26, LA-30, LA-33 (see W.9) | — |
| W §W.9, W.8 | Findings register; change-log row | — |

## 3. Corrections needed in files not owned (exact quote → fix)

| # | File | Quote | Fix |
|---|---|---|---|
| R-1 | `01_MASTER_PROMPT.md` §7 Aadhaar row | "(Aadhaar Act s.4(4), s.57 struck)" | "(Aadhaar Act s.4(4); s.57 omitted by the Aadhaar and Other Laws (Amendment) Act 2019 after *Puttaswamy* (2018))" |
| R-2 | `01_MASTER_PROMPT.md` §7 eSign row | "First Schedule exclusions as amended 26 Sep 2022 (property-sale contracts no longer excluded [VERIFY]; wills, trusts, ordinary POAs, most negotiable instruments excluded)" | "First Schedule as amended by S.O. 4720(E) (dated 26 Sep 2022; Gazette 4 Oct 2022 [VERIFY]): entry 5 omitted (two secondary sources; Gazette text pending); excluded — wills, trusts, POAs other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity, NIs other than cheques and DPNs/BoEs in favour of such entities" |
| R-3 | `01_MASTER_PROMPT.md` NN-07 | "(wills, trusts, ordinary powers of attorney, negotiable instruments other than cheques, and any other excluded entry as amended)" | "(wills, trusts, powers of attorney other than those empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity, negotiable instruments other than cheques and demand promissory notes/bills of exchange in favour of or endorsed by such an entity, and any other excluded entry as amended)" |
| R-4 | `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` CH-01 | "s.57 struck down" | "s.57 omitted (2019) after *Puttaswamy* struck down its contract-based limb" |
| R-5 | `phases/P15_*.md` FR-P15-35 | "District ≤ ₹50 lakh; State > ₹50 lakh to ₹2 crore; National > ₹2 crore" | Prefix "By value of goods or services paid as consideration (CPA 2019 s.34(1), s.47(1)(a)(i), s.58(1)(a)(i)) — not the compensation claimed:"; input `consideration_paid_inr` |
| R-6 | `phases/P15_*.md` @P15-AT-14 | "Scenario: Insurance claim above ₹50 lakh routes to the State Commission … Given a rejected health claim of ₹72 lakh / Then … shows the State Commission via e-Jagriti" | "Scenario: Insurance claim above ₹50 lakh skips the Ombudsman and routes by premium paid. Given a rejected health claim of ₹72 lakh and a premium paid of ₹48,000. Then the ladder skips the Insurance Ombudsman and shows the District Commission via e-Jagriti" |
| R-7 | `phases/P15_*.md` FR-P15-59 | "Deadlines: apply within 14 days (same State) or 45 days (other State)" | "Deadlines: seller reports within 14 days (same State) or 45 days (other State) — MV Act s.50(1)(a)–(b); buyer reports within 30 days — s.50(1); legal-heir and auction-buyer variants under s.50(2) and CMVR r.56 [VERIFY]" |
| R-8 | `phases/P12_*.md` §1 narrative and TM-EXAM-REPLY row | "the one-month reply window"; "1 month from receipt" | "the 30-day reply window"; "30 days from receipt" (Trade Marks Rules 2017 r.33 [VERIFY sub-rule]) |
| R-9 | `appendices/L_*.md` FAQ-18 | "verified advocates and other professionals" | "advocates enrolled with a State Bar Council and other professionals whose registration we check" |
| R-10 | `appendices/L_*.md` l.51 and F-131 | "Professional consult allowance … 1 × 15-min / year …" | "LawDocs documentation-team guided session allowance (not legal advice)"; advocate consultations sold separately at a fixed fee paid to the advocate, never inside a plan price (CH-08, NN-21) [COUNSEL] |

## 4. Content and policy checks (summary)

- **NN-20 unevidenced claims.** These were removed or gated: "binding", "forever", "for life", "legal officer", "RBI-ready", "one legal head … department", "verified advocate", the hosting statement, and the CERT-In blanket claim. The §2.4 proof-point table is sound.
- **Outcome promises (NN-23).** Fixed in the Consumer Help eyebrow. The banned-phrase list in S §S.11.3 is adequate.
- **Rule 36 advertising.** Directory and display rules are compliant. The PR-02 description of the Madras HC judgment was overstated and is corrected. Bundled advocate consultations (LA-16) are the main residual risk.
- **Dark patterns (NN-50).** Cancellation parity and no fake urgency were already in place. Ex-GST plan cards, the auto-renewal default and trial conversion were aligned to POL-LD-05.
- **Testimonials.** All formats are marked PLACEHOLDER, the block is OFF and the CMS blocks publication. Compliant.
- **AI-draft labels (NN-14).** Present in GB-10, POL-LD-04 §3 and the FAQ. Compliant.
- **Fee transparency (NN-22).** The four-line price card is compliant. The stamp-duty "we collect" wording is corrected.

## 5. Open (could not be verified in this pass)

The items are listed in W.9 LA-36. Of those, the RB-IOS 2026 clause numbers and the IT Rules 2026 timelines carry the most risk, because Locked settings rely on them (LG-173, LG-077). Both are conservative-direction locks, so NN-38 allows them, but neither may be cited as verified in public copy until it is logged.
