# A5_FAM_TAX — research summary (22 Oct 2026)

55 items: 11 verified, 2 corrected, 9 provisional, 27 counsel/tax-memo sign-off, 3 watch, 3 product decision. Proposed `edits` are in the JSONL. Every `old` string was checked as unique, and column counts are unchanged.

**Limit:** the shared web-search budget ran out partway through. The family and succession items were checked against primary sources. Most tax and App. O items were not re-checked online. They carry conservative interim defaults, and their `residual` field says so.

## Key findings
- **Repealing and Amending Act, 2025:** Act No. 37 of 2025, 20 Dec 2025 (India Code). Second Schedule Sl. 3 omits ISA s.213 and the ", 213" in s.3(1). It also narrows s.370(1) to cases needing letters of administration and omits s.370(2)(b). Section 4 is a general savings clause. The effect on earlier deaths stays with counsel.
- **SC order of 19 Nov 2025:** *Snidha Mehra v UoI*, W.P.(C) 732/2020. It covers s.15(1)(c)–(e) claims where s.15(2) does not apply. Mediation must be at a Mediation Centre or a Legal Services Authority. "Treated as a decree" applies only there. **Correction:** a private Equator settlement does not become a decree. Keep `fam.s15_prelit` OFF.
- **MWPSC (India Code):** s.2(h) requires a senior citizen to be a citizen of India aged 60+. The s.2(d) definition of parent has no age or citizenship test. The s.6(6) one-month period and its Explanation are verified. Whether a non-citizen parent qualifies is for counsel.
- **Uttarakhand UCC:** the official Rules r.1(3) and r.8(2) are verified. The 2026 Ordinance under Art. 213 is confirmed only by secondary sources, as are the Act number and the HC challenge. Keep the module OFF.
- **Case law:**
  - *Shiksha Kumari* is verified (Delhi HC Full Bench, MAT.APP.(F.C.) 111/2025). The holding is about s.13B waiver, not s.14 alone.
  - *Kunvarjeet Singh Khandpur* is verified (C.A. 2464/2008).
  - *Amit Kumar v Suman Beniwal* is an SC order of 11 Dec 2021 (SLP(C) 20108/2021). The "(2023) 17 SCC 648" citation is unconfirmed.
- **Banking Laws (Amendment) Act 2025, ss.10–13:** in force 1 Nov 2025 (PIB).
- **ISA s.33A (corrected):** excludes Indian Christians (s.33A(5)(a)); applies only where there are no lineal descendants.
- **Kerala HC:** *Anup Disalva* (2022) struck down the one-year minimum in s.10A(1). Applies in Kerala only.
- **Partition awards:** MH Art. 12, as substituted by Mah. Ord. XII of 2024, still excludes partition awards. The same Ordinance raised Art. 52(a) release duty to ₹500. Post-2020 SC: *K. Arumuga Velaiah* (2022), where a future-division document is exempt from registration under s.17(2)(v). No post-2020 HC authority.
- **Stamp duty by state:** UP set a ₹5,000 cap on partition deeds (Cabinet, Sep 2025; notification not found). Karnataka set per-share rates in 2023 (secondary source). Delhi and Rajasthan are open.

## Pack errors beyond the item list
- Appendix G line 525 (LR-SUCC-013) needs the same Act No. 37 of 2025 citation.
- V3 line 193 credits s.2(d) with words it does not contain.
- The "One-year bar" row misplaces *Shiksha Kumari*, which concerns s.13B(1).
- `notional_partition_include_wife` should have no default. *Gurupad* gave the widow a notional share.

## Launch blockers
1. **Tax memo:** e-commerce operator TDS and GST-TCS under split-settlement; wallet as deposit or advance; `equator_principal`; platform fee notes. Interim: flags OFF with shadow ledgers, top-ups taxed on receipt, `neutral_direct` billing.
2. **MCA21 master data (J-170):** the CS must pull it before the footer goes live.
3. **Stamp matrix:** Delhi and Rajasthan.
4. **Income-tax Rules 2026:** form and rule numbers unconfirmed. Use generic labels.

## "Also check" claims
None of the eight claims is in this group's scope. Not assessed.
