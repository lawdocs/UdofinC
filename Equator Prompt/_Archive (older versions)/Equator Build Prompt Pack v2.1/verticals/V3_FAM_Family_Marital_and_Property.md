# V3 — Family, Marital and Property (FAM) — Vertical Specification

> Binding for P08c. Read with master (`01_MASTER_PROMPT.md` v2.0), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, and Appendices A, B, F, G, K, L, M. Law stated as at 21 October 2026. Version 2.0.0 (21 Oct 2026). Owner: Head of Legal (FAM) + Safeguarding Lead. Supersedes nothing in P08 §4.3; it **extends** FR-P08-35 to FR-P08-45 and adds FR-V3-01 onwards.

Legend for legal tags: **[V]** verified against a primary or reputable secondary source in research passes S1 / RES_A3; **[K]** settled law not re-fetched in the v2 pass; **[VERIFY — open: …]** must be cleared by the legal reviewer before any *permissive* rule that depends on it is activated (Appendix G §G.1 fail-safe principle). Protective rules may run while carrying a VERIFY marker.

---

## 0. Scope and how to use

### 0.1 What this file is
The single build specification for the `FAM` vertical pack (`packages/verticals/fam`). It covers:
- **Marital** matters for every community: Hindu (including Sikh, Jain and Buddhist), Muslim (Sunni Hanafi, Shafi'i, Maliki/Hanbali; Shia Ithna Ashari, Ismaili Khoja, Dawoodi Bohra), Christian, Parsi, Jewish, Special Marriage Act couples, Goa domiciles (Goa Civil Code), Uttarakhand residents (Uniform Civil Code — flagged), and Scheduled Tribes (customary law).
- **Money and children** in the family: maintenance (all statutes), custody, access and parenting plans (mediable, never arbitrable), streedhan, mahr, matrimonial home.
- **Family property**: intestate succession among heirs, coparcenary/HUF partition, family settlements, will distribution and wasiyat consent, co-owned property, family-business separation, succession/legal-heir certificate assistance, NRI/OCI heirs.
- **Elders**: maintenance and care under the Maintenance and Welfare of Parents and Senior Citizens Act 2007 (MWPSC), including Tribunal-referred conciliation (s.6(6)).
- **Exclusions and signposting**: criminal matters (NN-24), instant triple talaq (talaq-e-biddat), probate/will validity, status decisions, POCSO and abuse, urgent child-removal risk.

### 0.2 How the coding agent uses it
1. Build order inside P08c: §16 data model migration → §4 rule pack (`fam.suitability.v2`) → §5 Explorer tree → §6 form schemas and dropdowns → §7 workflows (Temporal) → §12 calculators with golden vectors → §13 templates → §14 KPIs → §17 tests.
2. Every legal rule referenced here is a row in Appendix G. New rule IDs proposed in this file (LR-FAM-013 onwards, LR-SUCC-013 onwards) are created with `status` and `effect` exactly as stated in §3.12; nothing is hard-coded (master §0).
3. Error codes: canonical `code` values come from Appendix F §F.10; FAM sub-codes travel in the `rule` field (Appendix F §F.10.3). New FAM sub-codes introduced here are listed in §16.6 and must be registered in `packages/domain/errors.ts` before use (CI check).
4. Where this file and P08 §4.3 differ, this file prevails for FAM (master §15 X-19), except on NN rules, Appendix G legal content, Appendix B fee figures, Appendix F names and Appendix A clock semantics (master §15 precedence). Conflicts found while writing are listed in §18.2 with the resolution applied.

### 0.3 Non-negotiables that bite hardest in FAM
| NN | FAM consequence |
|---|---|
| NN-01 | No AI recommendation of a maintenance figure, custody arrangement, share or "fair" split. Calculators are deterministic tools; AI may display, never recommend (FAM-G-02/03/04). |
| NN-06 | No award on matrimonial status, custody, guardianship, testamentary matters (probate, letters of administration, will validity, succession certificate), maintenance as a statutory right, DV protection orders, MWPSC Tribunal relief or criminal matters. Arbitration only for property/partition rights inter se. |
| NN-07 | Screening, DV, child and safety data live in `safety_sealed`; never in analytics, AI or exports. |
| NN-08 | Partition, release, gift, settlement deeds over immovable property, wills, powers of attorney → physical execution, stamping, registration (Sub-Registrar). E-sign alone never completes them. |
| NN-11 | Mediation never recorded. |
| NN-24 | Criminal matters are not undertaken. Triple talaq, dowry offences, POCSO, sexual offences, threats/violence → hard exclusion + signposting. Only civil terms of a matrimonial dispute with parallel criminal cases are mediated; the court alone decides compounding/quashing. |
| NN-26 | FAM outcomes are never published in full; P0 (none) by default; P1 aggregate statistics allowed; P2 digest only with every party's consent and the FAM redaction profile. |

---

## 1. Vertical overview

### 1.1 Who it serves
| Segment | Typical users | Entry channel |
|---|---|---|
| Separating couples | Spouses (incl. NRI spouses), their counsel, support persons | Dispute Explorer, lawyer referral, Family Court referral (FCA s.9 / CPC s.89) |
| Parents | Parents negotiating custody, access, child maintenance, relocation, passport/travel | Explorer, counsellors, school/EAP referral |
| Heirs and co-owners | Siblings, widows, coparceners, karta, legal heirs, NRI/OCI heirs | Explorer, CA/CS/lawyer partner referral, banks/societies demanding heirship documents |
| Family businesses | Brothers/cousins running proprietorships, firms, family companies | Partner referral, COM cross-route |
| Elders | Senior citizens and parents (60+), their children and relatives | Explorer, Elderline 14567 referrals, Maintenance Tribunal (s.6(6)) |
| Institutions (B2G/B2B) | Family Courts, mediation centres, DLSAs, Maintenance Tribunals, EAP providers, DV NGOs | Court-referral API (P09), MoU |

### 1.2 Value proposition (product copy anchors; App. P owns final copy)
- "Separate without a courtroom fight. Settle money, children and property online — safely, privately, on the record."
- "One family tree, every heir, a clear schedule of who gets what — then the right deed, stamped and registered."
- Proof points the product must make true: screening before any joint session; quick-exit on every FAM screen; deterministic share calculators per community; court-format packs (s.13B, consent terms, khula declaration, MWPSC conciliation report; labelled "court-ready" only on verified court-format profiles — X-34); registration route with 4-month clock; escrow-staged payments.

### 1.3 Mechanisms allowed (master §5.2 applied)
| Mechanism | Allowed in FAM | Limits |
|---|---|---|
| `negotiation` | ✔ | No blind-bid on maintenance where a party carries a vulnerability flag; no blind-bid when `safety_flag = true` |
| `conciliation` (A&C Part III) | ✔ | s.73/s.74 status only for civil/property/money heads; never for status or custody |
| `mediation` | ✔ primary | Contractual mode; statutory mode only when `mediation_statutory_mode` is ON (NN-05) |
| `arbitration` | Property/partition rights inter se only | `fam_property_arbitration` flag; LR-SUCC-011 is `permissive` + VERIFY → cannot activate until cleared (§18.2 C-03) |
| `med_arb` / `arb_med` / `arb_med_arb` | Property only | Different neutral for arbitration phase; caucus firewall (master §5.3) |
| `expert_determination` | Not a FAM mechanism | Valuation by an agreed valuer is an evidence step (P08 FR-P08-38); a binding valuation clause in a property MSA is a contract term |
| `grievance`, `posh_inquiry` | — | — |
| `signposting` | ✔ | Mandatory for every FAM closure (Appendix A §5: `require_signposting = true`) |

### 1.4 Status of key laws (as of 21 Oct 2026)
| Instrument | Status | Product effect |
|---|---|---|
| Hindu Marriage Act 1955; Special Marriage Act 1954; Divorce Act 1869; Parsi Marriage and Divorce Act 1936; Dissolution of Muslim Marriages Act 1939; Muslim Personal Law (Shariat) Application Act 1937 | In force | Regime-specific divorce routes (§3.1) |
| Muslim Women (Protection of Rights on Marriage) Act 2019 (Act 20 of 2019, deemed in force 19 Sep 2018) | In force | Talaq-e-biddat void (s.3) and an offence (s.4) → NN-24 exclusion EX-FAM-01 |
| Muslim Women (Protection of Rights on Divorce) Act 1986 | In force; does not exclude BNSS s.144 (*Mohd. Abdul Samad v State of Telangana*, 2024 INSC 506, 10 Jul 2024) [V] | Both routes offered |
| Bharatiya Nagarik Suraksha Sanhita 2023 ss.144–147 (ex-CrPC ss.125–128); BNS 2023; BSA 2023 | In force from 1 Jul 2024 | Cite BNSS/BNS/BSA only (LR-EVID-002) |
| Hindu Adoptions and Maintenance Act 1956 (HAMA); Hindu Minority and Guardianship Act 1956 (HMGA); Guardians and Wards Act 1890 (GWA) | In force | Maintenance and custody law |
| Protection of Women from Domestic Violence Act 2005 + PWDV Rules 2006 (rr.13–14 counselling safeguards) | In force | DV-adjacent mediation policy (§4.5) |
| Family Courts Act 1984 | In force | s.9 settlement duty; court-referral mode |
| Hindu Succession Act 1956 as amended 2005 (s.6 w.e.f. 9 Sep 2005) | In force | HSA calculator; daughter coparcener (*Vineeta Sharma*, (2020) 9 SCC 1) |
| Indian Succession Act 1925 — **s.213 omitted** by the Repealing and Amending Act 2025 (Act No. 37 of 2025, 20 Dec 2025; Second Schedule Sl. 3) [Verified 22 Oct 2026: India Code A2025-37] | Probate/LoA still available; no longer mandatory for Mumbai/Kolkata/Chennai wills | Copy-lint `probate_mandatory_claim` (FR-V3-03) |
| Uttarakhand Uniform Civil Code Act 2024 (Act No. 1 of 2024); UCC Rules effective 27 Jan 2025; UCC (Amendment) Ordinance 2026 [V secondary] | In force in Uttarakhand; constitutional challenge pending; UCC Rules text verified (ucc.uk.gov.in); Ordinance promulgated under Art. 213 (effective c. 27 Jan 2026, secondary) **[VERIFY — open (watch): Act and Ordinance Gazette text; replacing Act; HC challenge status]** | Module behind flag `fam.ucc_uk` = OFF (D2-27) |
| Goa Succession, Special Notaries and Inventory Proceedings Act 2012 (amended 2016, 2022, 2023, 2024); 2023 amendment upheld in *Xavier Agnelo Minguel Jose Gracias v State of Goa*, 2026:BHC-GOA:1046 (DB, 15 May 2026) [V] | In force | Goa guard; calculator `out_of_scope_goa` |
| MWPSC Act 2007 | In force; s.9(2) cap ₹10,000/month subsists (Amendment Bill 2019 not enacted; Karnataka HC recommendation, 2025) [V] | Elder track; Tribunal-referral mode |
| Income-tax Act 2025 s.315 (old 1961 Act s.171) | In force 1 Apr 2026 [V] | HUF partition tax warning |
| Mediation Act 2023 | Only ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 in force (S.O. 4384(E), 9 Oct 2023); MCI established S.O. 4781(E), 27 Aug 2026 | Contractual mode; no "s.27 decree" copy (NN-05) |
| Registration Act 1908 ss.17, 23, 25, 28, 32A, 49 | In force | NN-08 route; `registration_4m` clock |
| Supreme Court order of 19 Nov 2025, *Snidha Mehra v Union of India*, W.P.(C) 732/2020, paras 14–15: pre-litigation mediation before any suit where the parents or heirs of the father/mother claim a Hindu female intestate's estate under s.15(1)(c)–(e) and s.15(2) does not apply, at a Mediation Centre or State/District/Taluk Legal Services Authority [Verified 22 Oct 2026: order text] **[VERIFY — open (counsel): whether a private ODR mediation satisfies the direction]** | Direction reported; private-ODR eligibility unknown | Sub-type `fam.intestate_succession.s15_prelitigation` behind flag `fam.s15_prelit` = OFF (counsel Q3 in 02 §5) |

---

## 2. Subtype taxonomy

Codes follow D2-01: L1 = dispute type (`core.dispute_types.code`, kept identical to P08 FR-P08-35 so existing seeds remain valid); L2 = subtype (`sub_types[]`). New L1/L2 rows are marked **new**. Value bands map to Appendix B card FAM-STD lines: **M1** mutual-consent terms · **M2** parenting · **M3** maintenance · **M4** matrimonial property/multi-issue · **E** elder · **P** property (marginal on declared gross value) · **CR** court-referred · **S0** signposting (free, P5). Ladders: `fam.marital.v1`, `fam.property.v1`, `fam.elder.v1` (**new**), `fam.signpost.v1` (**new**, single rung). Mechanism columns: ✔ allowed · ⚠ allowed only with the condition in notes · ✘ blocked (non-configurable).

| L1 code | L2 code | Name | Typical parties | Value band | Default ladder | Negotiable | Mediable | Arbitrable | Signpost forum | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `fam.divorce_mutual` | `hma_13b` | Mutual divorce terms — Hindu/Sikh/Jain/Buddhist | spouse_a, spouse_b | M1 | marital | ✔ | ✔ | ✘ | Family Court (HMA s.13B) | ≥ 1 yr separation; s.14 one-year bar |
| | `sma_28` | Mutual divorce terms — Special Marriage Act | spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court (SMA s.28) | s.29 one-year bar |
| | `divorce_act_10a` | Mutual divorce terms — Christian | spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court (Divorce Act s.10A) | ≥ 2 yrs separation |
| | `pmda_32b` | Mutual divorce terms — Parsi | spouses | M1 | marital | ✔ | ✔ | ✘ | Parsi Matrimonial Court (PMDA s.32B) | Distinct forum |
| | `khula` | Khula — wife-initiated (Muslim) | wife, husband | M1 | marital | ✔ | ✔ | ✘ | Family Court declaration | Husband's consent not required (*Mohammed Arif Ali v Afsarunnisa*, Telangana HC DB, 24 Jun 2025) [V]; persuasive outside Telangana |
| | `mubarat` | Mubarat — mutual release (Muslim) | spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court declaration (optional) | iddat; mahr terms |
| | `talaq_consequences` | Civil consequences of talaq-e-ahsan/hasan already pronounced | spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court / Magistrate | Equator never drafts or records a talaq pronouncement |
| | `talaq_biddat_excluded` | Instant triple talaq (talaq-e-biddat) | wife | S0 | signpost | ✘ | civil terms only via `fam.maintenance`/`fam.matrimonial_property` | ✘ | Magistrate (MW(PRM) Act ss.4–7), police | EX-FAM-01; hard block `FAM_TRIPLE_TALAQ_BLOCKED` |
| | `ucc_uk_27` **new** | Mutual divorce terms — Uttarakhand UCC | resident spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court (UCC s.27) | flag `fam.ucc_uk`; registration of decree within 60 days (UCC Rules r.8(2)(a)(ii)) |
| | `goa_civil` **new** | Mutual divorce terms — Goa | Goa domiciles | M1 | marital | ✔ | ✔ | ✘ | Civil Judge (Goa) | communion of assets moiety; counsel review |
| | `customary_st` **new** | Customary divorce terms — Scheduled Tribe | spouses | M1 | marital | ✔ | ✔ (elders may attend with consent) | ✘ | Civil court / customary body | Custom must be proved; counsel review |
| `fam.divorce_contested_convert` | `cruelty`, `desertion`, `conversion`, `mental_disorder`, `irretrievable_breakdown`, `dmma_grounds`, `nullity` | Contested → consent conversion | spouses | M4 | marital | ✔ | ✔ | ✘ | Family Court | Art. 142 dissolution is SC-only (*Shilpa Sailesh v Varun Sreenivasan*, 2023 INSC 468) |
| `fam.judicial_separation_rcr` | `judicial_separation`, `restitution`, `reconciliation` | Judicial separation / restitution / reconciliation plan | spouses | M1 | marital | ✔ | ✔ | ✘ | Family Court | Reconciliation plan is a private agreement |
| `fam.maintenance` | `interim` | Interim maintenance pending proceedings | spouses, children (beneficiary) | M3 | marital | ✔ | ✔ | ✘ | Family Court / Magistrate | consent order in pending case |
| | `permanent_alimony` | Permanent alimony / lump sum | spouses | M3 | marital | ✔ | ✔ | ✘ | Family Court | full-and-final allowed where adequate; future waiver without consideration blocked (PT-FAM-02) |
| | `child` | Child maintenance and education | parents; child as beneficiary | M3 | marital | ✔ | ✔ | ✘ | Family Court / Magistrate | non-waivable (PT-FAM-01) |
| | `enhancement_reduction` | Variation of an existing order | spouses | M3 | marital | ✔ | ✔ | ✘ | Court that passed order (BNSS s.146; HAMA s.25) | cannot exclude statutory alteration |
| | `muslim_divorcee_1986` | Divorced Muslim woman — reasonable and fair provision, mahr, properties | spouses | M3 | marital | ✔ | ✔ | ✘ | Magistrate (1986 Act s.3) and/or BNSS s.144 | *Danial Latifi* (2001) 7 SCC 740; *Abdul Samad* (2024) |
| | `bnss_144` | Secular maintenance (wife, children, parents) | any | M3 | marital | ✔ | ✔ | ✘ | Magistrate / Family Court | s.144(4) disentitlement facts are for the court |
| | `mwprm_subsistence` | Subsistence allowance after void triple talaq (civil terms only) | wife, husband | M3 | marital | ⚠ | ⚠ wife-initiated only | ✘ | Magistrate (MW(PRM) Act s.5) | criminal limb excluded |
| | `live_in_support` **new** | Support after live-in relationship | partners | M3 | marital | ✔ | ✔ | ✘ | Magistrate (PWDVA s.20; *D. Velusamy* (2010) 10 SCC 469); UK: UCC s.388 | no marital status |
| `fam.custody_parenting` | `physical`, `legal`, `joint`, `access_visitation`, `relocation`, `passport_travel`, `festival_schedule`, `grandparent_contact` | Custody, access, parenting plan | parents; child is data subject only | M2 | marital | ✔ | ✔ (child-inclusive optional, F-FAM-29) | ✘ | Family Court / GWA court; HC (habeas corpus) | "subject to court approval" (LR-FAM-007); never traded for money |
| | `guardianship_of_property` **new** | Guardian of minor's property / sale permission | parents, relatives | S0 | signpost | ✘ | ✘ | ✘ | District Court (HMGA s.8(2), GWA s.29) | signpost_only; pack supplied |
| `fam.matrimonial_property` | `streedhan`, `mahr`, `shared_household`, `joint_accounts_loans`, `vehicles`, `gifts_return`, `goa_communion_moiety` | Matrimonial property | spouses, in-laws (as parties where title is theirs) | M4 | marital | ✔ | ✔ | ⚠ title/money inter se only; immovable → NN-08 | Civil court; Magistrate (PWDVA s.19) | in-laws must join for terms on their property (LR-SUCC-009) |
| `fam.dv_civil` | `residence`, `monetary_relief`, `protection_terms_civil`, `interim_custody` | DV-adjacent civil terms (safety pathway) | aggrieved woman, respondent | M4 | marital (shuttle only) | ⚠ | ⚠ aggrieved-initiated, shuttle, PWDV r.14 safeguards | ✘ | Protection Officer; Magistrate (PWDVA s.12); 112; 181 | joint sessions blocked; settlement only at aggrieved person's request |
| `fam.criminal_closure` | `compoundable`, `quashable_if_private`, `not_quashable`, `mwprm_s4_compoundable` | Civil terms alongside criminal cases | spouses, families | M4 | marital | civil terms only | civil terms only | ✘ | Trial court (BNSS s.359); HC (BNSS s.528) | no promise of quashing (LR-FAM-009); no pressure condition (LR-FAM-010) |
| `fam.nri_cross_border` | `foreign_decree_alignment`, `execution_abroad`, `nri_maintenance`, `child_removal_risk` | NRI / cross-border family | spouses abroad | M4 | marital | ✔ | ✔ | ✘ | Family Court; HC (habeas corpus) | child-removal risk → urgent U-FAM-02 (no scheduling) |
| `fam.intestate_succession` | `hsa_male` | Inheritance among heirs — Hindu male intestate | heirs | P | property | ✔ | ✔ | ⚠ division inter se, all heirs consent | Civil court; District Judge (succession certificate) | calculator `fam.hsa_shares@2` |
| | `hsa_female_15_1`, `hsa_female_15_2` | Hindu female intestate (s.15(1)/s.15(2)) | heirs | P | property | ✔ | ✔ | ⚠ | Civil court | s.15(2) source tagging → counsel |
| | `s15_prelitigation` **new** | Parents' heirs v husband's heirs (Hindu woman intestate) | heirs | P | property | ✔ | ✔ | ⚠ | Civil court | flag `fam.s15_prelit`; SC order 19 Nov 2025, *Snidha Mehra v UoI*, W.P.(C) 732/2020 (s.15(1)(c)–(e) claims, s.15(2) not applicable; forum: Mediation Centre/LSA) [Verified 22 Oct 2026] |
| | `muslim_hanafi`, `muslim_shia_ithna_ashari`, `muslim_other_school` | Muslim estates | heirs | P | property | ✔ | ✔ | ⚠ | Civil court | calculators flag OFF; Ismaili/Bohra → counsel |
| | `isa_ch2` | Christian / Jewish / SMA (s.21) estates | heirs | P | property | ✔ | ✔ | ⚠ | Civil court; District Judge | calculator `fam.isa_ch2@1` |
| | `isa_parsi` | Parsi estates | heirs | P | property | ✔ | ✔ | ⚠ | Civil court | calculator `fam.isa_parsi@1` |
| | `goa_succession` | Goa estates | heirs, surviving spouse | P | property | ✔ | ✔ | ⚠ counsel | Civil Judge (inventory); Notary (deed of qualification of heirs) | inventory mandatory where minor/interdict/absent heir |
| | `ucc_uk` | Uttarakhand UCC estates | heirs | P | property | ✔ | ✔ | ⚠ | Civil court | flag `fam.ucc_uk` |
| | `customary_st` | Scheduled Tribe estates | heirs, clan | P | property | ✔ | ✔ | ⚠ counsel | Civil court; revenue authority | *Ram Charan v Sukhram*, 2025 INSC 865 [V]; land-transfer bars |
| `fam.partition_coparcenary` | `huf_partition`, `ancestral_property`, `daughter_coparcener_claim`, `partial_partition`, `agricultural_land` | Coparcenary / HUF partition | coparceners, karta, members | P | property | ✔ | ✔ | ⚠ property only; award stamped + registered | Civil court (O.XX r.18); revenue court (agricultural) | ITA 2025 s.315 warning |
| `fam.family_settlement` | `memorandum_recording`, `operative_deed`, `instead_of_contesting_will`, `release_relinquishment`, `gift_within_family` | Family settlement / arrangement | family members | P | property | ✔ | ✔ | ⚠ property only | Sub-Registrar | *Kale* (1976) 3 SCC 119 |
| `fam.will_interpretation` | `interpretation`, `executor_conduct`, `distribution_by_consensus`, `wasiyat_consent` | Will distribution (post-grant or by consensus) | beneficiaries, heirs, executor | P | property | ✔ | ✔ | ⚠ in personam only | Probate court (if contest) | wasiyat ≤ 1/3 check |
| `fam.probate_validity` | `probate`, `letters_of_administration`, `will_validity`, `caveat_opposition` | Will validity / probate / LoA | — | S0 | signpost | ✘ | ✘ (mediate *around* it via `fam.family_settlement.instead_of_contesting_will`) | ✘ | District Judge / HC (probate) | `signpost_only` (LR-SUCC-007) |
| `fam.succession_documents` **new** | `succession_certificate`, `legal_heir_certificate`, `heirship_agreement`, `nominee_vs_heir`, `transmission` | Succession / legal-heir certificates and transmission | heirs, nominees | M4 | signpost + property | ✔ (heirship agreement) | ✔ (heirship agreement only) | ✘ | District Judge (ISA s.372); Tahsildar/SDM (legal heir certificate); bank/RTA/society | grant itself non-arbitrable (*Booz Allen* para 36) |
| `fam.co_owner_property` | `sale_or_buyout`, `rent_sharing_accounts`, `mesne_profits`, `possession` | Joint property among relatives | co-owners | P | property | ✔ | ✔ | ✔ (inter se) | Civil court (Partition Act s.2 sale) | owelty calculator |
| `fam.family_business_separation` | `proprietorship`, `partnership_firm`, `family_company_shares`, `brand_ip`, `guarantees_loans` | Family-business separation | family members, firm, company | P | property | ✔ | ✔ | ✔ (route corporate layer to COM) | NCLT (oppression/mismanagement) | cross-route `COM`; lender NOC for guarantees |
| `fam.elder_maintenance` | `monthly_maintenance`, `medical`, `residence`, `s23_transfer_revocation`, `eviction_from_senior_house`, `care_arrangement`, `grandparent_access` | Elder maintenance and care | senior citizen/parent, children, relatives | E | elder | ✔ | ✔ (s.6(6) conciliation) | ✘ | Maintenance Tribunal (MWPSC s.7) | Tribunal always signposted; no advocate in Tribunal-referred conciliation (s.17 policy) |

Taxonomy seed rules: `blocked_mechanisms[]` for every L1 includes `arbitration` except `matrimonial_property`, `intestate_succession`, `partition_coparcenary`, `family_settlement`, `will_interpretation` (in personam heads only), `co_owner_property`, `family_business_separation`. `signpost_only = true` for `fam.probate_validity`, `fam.custody_parenting.guardianship_of_property`, `fam.divorce_mutual.talaq_biddat_excluded`. `confidentiality_tier_default = 'high'` for all FAM types; any case with `safety_flag = true` or a child term is raised to `sealed` for screening artefacts only (core case stays `high`).

---

## 3. Legal framework by subtype

### 3.1 Regime map (routing key for every FAM rule)
The governing regime is decided by religion **at the relevant time** (marriage, death), form of marriage, domicile (Goa), residence (Uttarakhand), Scheduled Tribe status and proved custom. It is computed by `regime_resolver` (§4.2), never typed by the user.

| Community / situation | Marriage & divorce | Maintenance | Guardianship / custody | Intestate succession | Wills |
|---|---|---|---|---|---|
| Hindu, Sikh, Jain, Buddhist (incl. Virashaiva, Lingayat, Arya/Brahmo/Prarthana Samaj; anyone not Muslim/Christian/Parsi/Jew unless custom proved) | HMA 1955 (s.2); Anand Marriage Act 1909 registration for Sikh marriages [K] | HAMA ss.18–20, 22; HMA ss.24–25; BNSS s.144 | HMGA ss.6, 8, 13; GWA; HMA s.26 | HSA 1956 (s.2) | ISA Part VI (s.57, Sch. III) |
| Muslim (Sunni Hanafi, Shafi'i, Maliki, Hanbali; Shia Ithna Ashari, Ismaili Khoja, Dawoodi Bohra) | Shariat Act 1937 s.2; DMMA 1939 s.2; MW(PRM) Act 2019 | MW(PRD) Act 1986 s.3; BNSS s.144 (*Abdul Samad*) | Muslim law (hizanat with mother; father/paternal grandfather guardian of property) + GWA | Shariat Act s.2 — school-specific; agricultural land excluded from s.2 subject to state law [K] | Wasiyat ≤ 1/3 of net estate to non-heirs; bequest to heir needs other heirs' consent (Hanafi: after death) [K] |
| Christian | Indian Christian Marriage Act 1872; Divorce Act 1869 ss.10, 10A | Divorce Act ss.36–37; BNSS s.144 | GWA; Divorce Act ss.41–44 | ISA Part V Ch. II (ss.31–49); Travancore Act superseded (*Mary Roy v State of Kerala* (1986) 2 SCC 209) [K] | ISA Part VI |
| Parsi | PMDA 1936 ss.32, 32B; Parsi Matrimonial Courts [K] | PMDA ss.39–40; BNSS s.144 | GWA; PMDA s.49 | ISA Part V Ch. III (ss.50–56, as substituted by Act 51 of 1991) | ISA Part VI |
| Jewish | Jewish personal law; SMA if registered [K] | BNSS s.144 | GWA | ISA Part V Ch. II | ISA Part VI |
| Special Marriage Act couples | SMA ss.27, 28 | SMA ss.36–37; BNSS s.144 | GWA; SMA s.38 | ISA Ch. II via SMA s.21; **both spouses Hindu/Sikh/Jain/Buddhist → HSA via s.21A**; s.19 severance from HUF where a member marries a non-Hindu [K] | ISA |
| Goa domiciles (all religions) | Goa Civil Code + Goa family laws; civil registration; communion of assets default [K] | Goa law; BNSS s.144 | Goa law + GWA | Goa Succession, Special Notaries and Inventory Proceedings Act 2012 (as amended); surviving spouse ahead of ascendants/siblings (2023) — *Gracias* (2026) [V] | Legitime limits free disposal [K] |
| Uttarakhand residents (except STs and Part XXI customary-rights holders) | UCC 2024 ss.25 (grounds), 27 (mutual consent), 28 (no petition within 1 year), 29 (dissolution only under Code), 32 (penalties) [V secondary] | UCC ss.33–34; s.388 (live-in desertion) | UCC s.35; GWA | UCC s.49 (no ancestral/self-acquired distinction), s.50, s.51 Class I, s.52 Class II [V secondary] | UCC s.61 full testamentary freedom; Rules require will registration [V secondary] |
| Scheduled Tribes (Art. 342) | Custom; HMA s.2(2) excludes unless notified; may opt for SMA | BNSS s.144 | GWA | Custom; failing proof, justice, equity and good conscience with equal shares for women (*Ram Charan v Sukhram*, 2025 INSC 865, 17 Jul 2025 [V]; *Tirith Kumar v Daduram*, 2024 SCC OnLine SC 3810 [V secondary]) | ISA where applicable |
| Converts | Regime of religion at marriage governs marriage; conversion a divorce ground (HMA s.13(1)(ii)) [K] | — | — | HSA s.26: descendants born after conversion disqualified from inheriting from Hindu relatives [K] | — |
| Foreign-domiciled / NRI | Recognition of foreign decrees: CPC s.13; *Y. Narasimha Rao v Y. Venkata Lakshmi* (1991) 3 SCC 451 [K] | — | India not party to Hague Child Abduction Convention 1980; welfare test (*Nithya Anand Raghavan v State (NCT of Delhi)* (2017) 8 SCC 454) [K] | Movables: domicile at death; immovables: lex situs (ISA s.5) [K] | — |

### 3.2 Marriage and divorce terms (`fam.divorce_*`, `fam.judicial_separation_rcr`)
| Route | Provision | Pre-condition | Statutory clock | Notes / case law |
|---|---|---|---|---|
| Hindu mutual consent | HMA s.13B | Living separately ≥ 1 year (s.13B(1)) | Second motion not earlier than 6 months and not later than 18 months after presentation (s.13B(2)) | 6 months directory; waiver application from one week after first motion (*Amardeep Singh v Harveen Kaur* (2017) 8 SCC 746, 12 Sep 2017; *Amit Kumar v Suman Beniwal* (SC order, 11 Dec 2021, SLP(C) 20108/2021, Art. 142; SCC cite unconfirmed)); 18-month consequence varies by HC → hard alert + lawyer review [V RES_A3 Q21] |
| One-year bar | HMA s.14; SMA s.29; UCC s.28 | No petition within 1 year of marriage save exceptional hardship/depravity with leave | — | Delhi HC Full Bench *Shiksha Kumari v Santosh Kumar*, MAT.APP.(F.C.) 111/2025 (FB, 17 Dec 2025): s.13B(1) one-year separation waivable under the s.14(1) proviso; s.13B(2) waivable independently [Verified 22 Oct 2026: Delhi HC website; binding in Delhi] |
| SMA mutual consent | SMA s.28 | ≥ 1 year separate | 6–18 months [K] | LR-FAM-004 |
| Christian mutual consent | Divorce Act s.10A (ins. 2001) | ≥ 2 years separate | 6 months [K] | Kerala HC: *Saumya Ann Thomas v UoI* (2010) read 2 years as 1; *Anup Disalva v UoI*, 2022 LiveLaw (Ker) 640 (DB, 9 Dec 2022) struck down the 1-year minimum — Kerala only [V secondary 22 Oct 2026] **[VERIFY — open: judgment text]** |
| Parsi mutual consent | PMDA s.32B (ins. 1988) | ≥ 1 year separate | 6 months [K] | Parsi Matrimonial Court with delegates |
| Khula | Muslim law | Wife's demand; offer to return/forgo mahr ordinarily | iddat [K] | Husband's consent not required; Family Court gives "judicial stamp" after summary inquiry; muftis/Dar-ul-Qaza have no adjudicatory power (*Arif Ali*, Telangana HC DB, 24 Jun 2025, 2025 SCC OnLine TS 368) [V] |
| Mubarat | Muslim law | Mutual offer/acceptance | iddat | — |
| Talaq-e-ahsan / hasan | Muslim law | Lawful forms [K] | iddat | Validity of talaq-e-hasan under challenge (*Benazeer Heena v UoI*, W.P.(C) 348/2022 — pending as at Feb 2026, SC Observer) **[VERIFY — open (watch): Constitution Bench reference; recheck monthly]**; Equator mediates consequences only |
| Talaq-e-biddat | MW(PRM) Act 2019 ss.3, 4, 5, 6, 7 | — | — | Void (s.3; *Shayara Bano v UoI* (2017) 9 SCC 1); offence up to 3 years + fine (s.4); subsistence allowance (s.5); custody to mother as Magistrate determines (s.6); cognizable only on information by the wife or her blood/marriage relatives (s.7(a)); compoundable at wife's instance with Magistrate's permission (s.7(b)) [V] → EX-FAM-01 |
| Wife's judicial divorce | DMMA 1939 s.2 | Grounds (whereabouts unknown 4 yrs; failure to maintain 2 yrs; imprisonment 7 yrs; failure of marital obligations 3 yrs; impotence; insanity 2 yrs/leprosy/virulent VD; option of puberty; cruelty incl. unequal treatment; other recognised grounds) [K] | — | Contested → `divorce_contested_convert` |
| Uttarakhand | UCC s.27; registration of decree within 60 days of becoming final (UCC Rules r.8(2)(a)(ii)) [V] | per Code | 60-day registration clock `fam_ucc_divorce_reg_60d` | Flag `fam.ucc_uk`; UCC applies to residents of Uttarakhand outside the State (UCC Rules r.1(3), official text verified 22 Oct 2026; Code s.1 per Bar & Bench, secondary) **[VERIFY — open: Code s.1 text and 'resident' definition]** |
| Goa | Goa Civil Code divorce [K] | — | — | Procedure **[VERIFY — open (counsel): Goa procedure — Goa is not a launch state; keep out of scope until counsel note]**; counsel review |
| Customary (ST; also saved for Hindus by HMA s.29(2)) | Custom | Proof of custom | — | Counsel review |
| Art. 142 | Constitution | — | — | Supreme Court alone (*Shilpa Sailesh v Varun Sreenivasan*, 2023 INSC 468, 1 May 2023) |
| Consent revocable until decree | — | — | — | *Sureshta Devi v Om Prakash* (1991) 2 SCC 25 [K] → staged escrow tranches |

Forum: Family Court where established (Family Courts Act 1984 s.7) at the place where the marriage was solemnised, the respondent resides, or the parties last resided together (HMA s.19) [K]; Parsi Matrimonial Court for PMDA. Equator never issues a decree, never "dissolves" a marriage and never uses "Equator divorce" (copy-lint FR-V3-27).

### 3.3 Maintenance (`fam.maintenance`)
| Source of right | Who claims | Forum | Key rules |
|---|---|---|---|
| BNSS s.144 (ex-CrPC s.125); s.145 procedure; s.146 alteration; s.147 enforcement | Wife (incl. divorced, not remarried), minor child, disabled major child, parents — all religions | Magistrate of the first class / Family Court (FCA s.7(2)) | Disentitlement in s.144(4) is for the court; enforcement by warrant, imprisonment up to one month per default; application within one year of due date (s.144(3) proviso) [K]; order enforceable by any Magistrate where the payer is (s.147); s.146(3)(b) cancellation on receipt of personal-law sum |
| HAMA s.18 (wife), s.19 (widowed daughter-in-law), s.20 (children; aged/infirm parents; unmarried daughter), s.22 (dependants from estate), s.23 (factors), s.25 (alteration) | Hindu/Sikh/Jain/Buddhist | Civil court / Family Court | Survives a s.144 compromise (*Nagendrappa Natikar v Neelamma*, AIR 2013 SC 1541, 15 Mar 2013) [V RES_A3 Q22] |
| HMA s.24 (pendente lite), s.25 (permanent alimony); SMA ss.36–37; Divorce Act ss.36–37; PMDA ss.39–40; UCC ss.33–34 | Spouse in matrimonial proceedings (HMA gender-neutral) | Family Court | Ancillary to the main petition |
| MW(PRD) Act 1986 s.3 | Divorced Muslim woman | Magistrate | Reasonable and fair provision extending beyond iddat (*Danial Latifi v UoI* (2001) 7 SCC 740); BNSS s.144 also available (*Abdul Samad*, 2024 INSC 506) [V] |
| MW(PRM) Act 2019 s.5 | Wife subjected to triple talaq | Magistrate | Subsistence allowance; criminal limb excluded |
| PWDVA s.20 (monetary relief), s.22 (compensation), s.12 (application; s.12(5) endeavour to dispose within 60 days of first hearing) | Aggrieved woman incl. live-in "relationship in the nature of marriage" (*D. Velusamy v D. Patchaiammal* (2010) 10 SCC 469) | Magistrate | No limitation for s.12 application (*Kamatchi v Lakshmi Narayanan* (2022) 15 SCC 50) [K] |
| MWPSC ss.4, 9 | Senior citizens (citizens of India aged 60+, s.2(h)) and parents (biological, adoptive or step, s.2(d)), who may claim against a non-minor child under s.4(1)(i) whatever their age [Verified 22 Oct 2026: India Code] **[VERIFY — open (counsel): whether a non-citizen parent qualifies — s.2(d) states no citizenship test]** | Maintenance Tribunal | ₹10,000/month cap (s.9(2)); s.12 election between MWPSC and BNSS [V] |

Encoded rules from *Rajnesh v Neha* (2021) 2 SCC 324 (4 Nov 2020): (1) affidavit of disclosure in all maintenance proceedings, Enclosures I (general), II (agricultural), III (business) → F-FAM-07 variants; (2) overlapping proceedings: disclose prior orders; set-off/adjustment → D05 table and estimator floor; (3) entitlement from date of application → arrears calculator; (4) criteria list (status, needs, qualifications, independent income, standard of living, career sacrifice, litigation costs, payer's capacity and dependants) → structured factors, never AI-scored; (5) enforcement as money decree (CPC s.51, O.XXI) and BNSS s.147. 25% of payer's net income is a judicial benchmark, not law (*Kalyan Dey Chowdhury v Rita Dey Chowdhury* (2017) 14 SCC 200; LR-FAM-006).

### 3.4 Custody, guardianship and parenting (`fam.custody_parenting`)
| Topic | Law |
|---|---|
| Court custody/guardianship | GWA 1890 s.7, s.9 (jurisdiction where minor ordinarily resides), s.17 (welfare; intelligent preference), s.25 (return of ward), s.29 (guardian's alienation of property needs court permission) [K] |
| Hindu natural guardians | HMGA s.6 (father, then mother; child under 5 ordinarily with mother); s.8(2) (no transfer/mortgage of minor's immovable property without court permission); s.12 (no guardian for undivided interest); s.13 (welfare paramount); *Githa Hariharan v RBI* (1999) 2 SCC 228 [K] |
| Muslim | Hizanat with mother (Hanafi: son till 7, daughter till puberty; Shia: son till 2, daughter till 7) subordinate to welfare [K] — explanatory copy only |
| Matrimonial proceedings | HMA s.26; SMA s.38; Divorce Act ss.41–44; PMDA s.49; UCC s.35 |
| Cross-border | India not party to the Hague Convention 1980; *Nithya Anand Raghavan* (2017) 8 SCC 454; *Prateek Gupta v Shilpi Gupta* (2018) 2 SCC 309; *Yashita Sahu v State of Rajasthan* (2020) 3 SCC 67; habeas corpus for illegal custody (*Tejaswini Gaud v Shekhar Jagdish Prasad Tewari* (2019) 7 SCC 42) [K] |
| Mandatory reporting | POCSO Act 2012 s.19 (any person with knowledge must report); s.21 penalty [K] → safeguarding task ≤ 24 h |
| Arbitrability | Non-arbitrable (*Booz Allen & Hamilton v SBI Home Finance* (2011) 5 SCC 532 para 36) |
| Effect of agreed plan | Binding only when recorded by the court; court retains welfare jurisdiction and may vary at any time (LR-FAM-007) |

### 3.5 Domestic violence and criminal overlap (`fam.dv_civil`, `fam.criminal_closure`)
- PWDV Rules 2006 r.13 (counsellor not connected to parties; not the respondent's lawyer) and r.14: respondent's undertaking not to repeat violence (r.14(3)); counselling aims at non-recurrence (r.14(4)); respondent cannot plead justification (r.14(5)); settlement only if the aggrieved person so desires (r.14(7)); court records that terms are not vitiated by force, fraud or coercion (r.14(13)–(14), (17)) [V]. Equator adopts these as **FAM DV-adjacent policy** (§4.5).
- Shared household: *Satish Chander Ahuja v Sneha Ahuja* (2021) 1 SCC 414; *Prabha Tyagi v Kamlesh Devi* (2022) 8 SCC 90 [K]; in-laws who hold title must join any matrimonial-home term (LR-SUCC-009).
- Criminal: BNS ss.85–86 (cruelty) and Dowry Prohibition Act offences are non-compoundable → HC quashing only (BNSS s.528; *Gian Singh v State of Punjab* (2012) 10 SCC 303; *B.S. Joshi v State of Haryana* (2003) 4 SCC 675); dowry death (BNS s.80) and heinous offences never quashable (*Parbatbhai Aahir v State of Gujarat* (2017) 9 SCC 641); compoundable offences under BNSS s.359; MW(PRM) s.4 compoundable at wife's instance (s.7(b)). Equator mediates only civil terms; payments framed as civil settlement; no tranche conditioned on criminal closure when any party carries a safety flag (LR-FAM-009/010; PT-FAM-04).

### 3.6 Succession — Hindu Succession Act 1956
| Provision | Rule | Encoding |
|---|---|---|
| s.2(2) | Not applicable to Scheduled Tribes unless notified | resolver R1 |
| s.4(2) | Omitted by Act 39 of 2005; interplay with state tenancy succession contested | flag `agri_devolution_conflict` → counsel |
| s.6 (w.e.f. 9 Sep 2005) | Daughter coparcener by birth (*Vineeta Sharma v Rakesh Sharma* (2020) 9 SCC 1, 11 Aug 2020); s.6(3) notional partition; s.6(5) pre-20 Dec 2004 registered/decreed partitions saved; oral partition only on public-document evidence | LR-SUCC-001..003; date gate |
| ss.8–13 + Schedule | Male intestate: Class I simultaneously; Class II entries I–IX in order; agnates; cognates | LR-SUCC-004; Class II engine |
| s.14 | Female's property absolute; s.14(2) restricted-estate exception; conflicting lines referred to larger bench (*Tej Bhan v Ram Kishan*, 2024 INSC 945, 9 Dec 2024) [V] | widow-under-will → counsel |
| ss.15–16 | Female intestate; s.15(2) source-based reversion | LR-SUCC-005; source tagging |
| s.15 pre-litigation | SC order (19 Nov 2025, *Snidha Mehra v UoI*, W.P.(C) 732/2020, paras 14–15): pre-litigation mediation before suit where the parents or heirs of the father/mother claim a Hindu woman's intestate estate under s.15(1)(c)–(e) and s.15(2) does not apply; a settlement reached at a Mediation Centre or Legal Services Authority 'must be treated as a decree of the court' — this does not extend to a private (Equator) settlement [Verified 22 Oct 2026: order text] | flag `fam.s15_prelit` |
| s.19 | Heirs take as tenants-in-common | each share alienable |
| s.22 | Class I heirs' preferential right to acquire a co-heir's interest | MSA right-of-first-offer clause |
| ss.25, 26, 28 | Murderer disqualified; convert's descendants disqualified; no disqualification by disease | intake flags |
| s.30 | Testamentary disposition incl. coparcenary interest | wills route |

### 3.7 Succession — Muslim, ISA Ch. II, Parsi, Goa, UCC, Scheduled Tribes
| Regime | Core rules (see §12 for algorithms) | Tag |
|---|---|---|
| Sunni Hanafi | Estate after funeral, debts (incl. unpaid mahr) and legacies ≤ 1/3; Quranic sharers → residuaries (agnates) → distant kindred; no representation; 'aul when shares exceed unity; radd to sharers except spouse | [K] (Mulla; Fyzee) |
| Shia Ithna Ashari | Three classes; per stirpes representation; no 'aul; childless widow takes no share in land (movables and value of buildings/trees only); bequest to heir within 1/3 valid without consent | [K] |
| Hiba (gift) | Declaration, acceptance, delivery of possession; registration not mandatory for oral hiba of immovables (*Hafeeza Bibi v Shaikh Farid* (2011) 5 SCC 654) | [K] |
| ISA Ch. II (Christians, Jews, SMA s.21) | Widow 1/3 with lineal descendants; 1/2 with kindred only (s.33); s.33A ₹5,000 preferential sum/charge only where there is a widow and no lineal descendants, and never for Indian Christians or their children/grandchildren (s.33A(5)(a)) or a partly testate estate (s.33A(5)(b)) [Corrected 22 Oct 2026: bare-act text]; widower same (s.35); children equal (s.37); no descendants: father (s.42), then mother + siblings equally (s.43) etc.; advancements hotchpot (s.49) | [K] |
| Parsi (ISA ss.50–56) | Spouse and each child equal (s.51(1)); each surviving parent half a child's share (s.51(2)); predeceased child's share per s.53; no lineal descendant: s.54 + Sch. II | [K] |
| Goa | Moiety of communion to surviving spouse in own right; then succession under 2012 Act (spouse ahead of ascendants/siblings since 2023); legitime; inventory mandatory where minor/interdict/absent heir; rights vest on death, inventory only demarcates (*Gracias*) | [V]/[K] |
| Uttarakhand UCC | s.51 Class I: spouse 1, each child 1, predeceased child's branch 1, parents 1 together equally; s.52 Class II; 2026 Ordinance substitutes "spouse" for "widow" in Sch. II; Registrar General may cancel succession registrations | [V secondary] — flag OFF |
| Scheduled Tribes | Custom (burden on asserting party); else justice, equity and good conscience (e.g. CP Laws Act 1875 s.6 for MP/Chhattisgarh) with equal shares for women; Scheduled Area land-transfer bars (e.g. Chota Nagpur Tenancy Act 1908; Santhal Parganas Tenancy Act 1949) | [V]/[K] |

### 3.8 Wills, probate, succession and legal-heir certificates, nomination
| Item | Position (Oct 2026) |
|---|---|
| ISA s.213 | **Omitted** by the Repealing and Amending Act 2025 (assent 20 Dec 2025); Act No. 37 of 2025, s.3 and Second Schedule Sl. 3 (also amends s.3(1); s.370(1) now bars a succession certificate only where letters of administration are required; s.370(2)(b) omitted); s.4 general savings [Verified 22 Oct 2026: India Code A2025-37] **[VERIFY — open (counsel): effect on deaths before 20 Dec 2025 and pending probate proceedings; whether s.4 saves amendments]**. Copy: "Since 20 Dec 2025 probate is no longer legally mandatory for these wills. Banks, societies or buyers may still ask for probate or letters of administration." |
| Probate (ISA s.222 ff.), LoA (ss.218, 232, 234); contentious probate as suit (s.295); grant is in rem | Non-arbitrable, not mediable as to grant; Equator mediates distribution or withdrawal of opposition only; probate court still satisfies itself of due execution [Interp.] |
| Limitation for probate/LoA | Limitation Act Art. 137 (three years from when the right to apply accrues; the right is continuous) — *Kunvarjeet Singh Khandpur v Kirandeep Kaur* (2008) 8 SCC 463 (C.A. 2464/2008, 3 Apr 2008) [Verified 22 Oct 2026: judgment text; SCC page cite as commonly reported]; shown as information, `last_date_to_act = "not computable — continuing right"` |
| Execution and proof of will | ISA s.63 (two attesting witnesses); proof by at least one attesting witness (BSA 2023 s.67, ex-Evidence Act s.68); suspicious circumstances (*H. Venkatachala Iyengar v B.N. Thimmajamma*, AIR 1959 SC 443) [K] |
| Registration of will | Optional (Registration Act s.18(e)); Uttarakhand UCC Rules require registration (Rule 7(4) summary procedure) [V] |
| Succession certificate (ISA Part X, ss.370–390) | For debts and securities; application to District Judge (s.372); notice and summary inquiry (s.373); security (s.375); protects payer (s.381); revocable (s.383); court fee per state law **[VERIFY — open: state court-fee rates]**; non-arbitrable (*Booz Allen* para 36) |
| Legal heir certificate | State revenue document (Tahsildar/SDM; e-District); not title; not a succession certificate [K] |
| Nomination | Nominee generally holds for heirs (*Sarbati Devi v Usha Devi* (1984) 1 SCC 424); company/depository nomination does not override succession (*Shakti Yezdani v Jayanand Jayant Salgaonkar*, SC, Dec 2023) [K]; Insurance Act s.39(7) beneficial nominee exception [K]; Banking Laws (Amendment) Act 2025 ss.10–13: up to four nominees, in force 1 Nov 2025 [Verified 22 Oct 2026: PIB 23 Oct 2025] **[VERIFY — open: Banking Companies (Nomination) Rules 2025]** |

### 3.9 HUF, partition, family settlement, agricultural land
| Topic | Rule |
|---|---|
| Right to partition | Any coparcener incl. daughter; severance by unequivocal communication [K] |
| Karta alienation | Legal necessity/benefit of estate; HMGA s.12 [K] |
| Tax | **Income-tax Act 2025 s.315**: HUF continues to be assessed unless AO records partition after inquiry with notice to all members; partition = physical division; partial partition after 31 Dec 1978 not recognised; members jointly and severally liable for pre-partition tax [V] |
| Methods | Oral partition + memorandum (*Kale*; *Ravinder Kaur Grewal v Manjit Kaur* (2020) 9 SCC 706); registered partition deed (Stamp Act Art. 45 or state equivalent; Registration Act s.17(1)(b)); compromise decree on suit property (s.17(2)(vi); *Mohammade Yusuf v Rajkumar* (2020) 10 SCC 264, 5 Feb 2020; *Mukesh v State of MP*, 2024 INSC 1026, 20 Dec 2024) [V]; arbitral award (stamp as partition instrument; register — *Lachhman Dass v Ram Lal* (1989) 3 SCC 99); court decree (CPC O.XX r.18) |
| Partition Act 1893 | s.2 sale in lieu where division impracticable; s.3 buy-out at valuation; s.4 dwelling-house buy-out against stranger-transferee [K] |
| Limitation | None while joint status subsists; exclusion → Limitation Act Art. 110 (12 years from knowledge of exclusion); Art. 65 (12 years, adverse possession) [V RES_A3 Q26] |
| Benami | Prohibition of Benami Property Transactions Act 1988 s.2(9)(A) family exceptions; s.4 bar [K] |
| Family settlement validity (*Kale v Deputy Director of Consolidation* (1976) 3 SCC 119) | Bona fide; fair and equitable; voluntary; may be oral; memorandum of prior oral arrangement needs no registration; operative document needs registration; antecedent title/claim (even possible) suffices; consideration of peace suffices; estoppel once acted upon |
| Agricultural land | Revenue records (khatauni/jamabandi/7-12/pahani/RTC/patta); mutation is fiscal, not title (*Jitendra Singh v State of MP*, SC, 6 Sep 2021) [K]; division before revenue courts per state code (UP Revenue Code 2006 s.116 'Suit for division of holding' [Verified 22 Oct 2026: official text]; Rajasthan Tenancy Act 1955 s.53 [secondary]) **[VERIFY — open: Delhi, Maharashtra, Karnataka provisions]**; fragmentation and ceiling laws [K] |

### 3.10 NRI / OCI heirs and spouses
| Topic | Rule |
|---|---|
| Inheritance by NRI/OCI | Permitted from a person resident in India or one who acquired lawfully; inheritance route not subject to the agricultural land/plantation/farmhouse exclusion (RBI Master Direction No. 12/2015-16, paras 3.1.3–3.1.4; FEM (Non-debt Instruments) Rules 2019) [V] |
| Gift to NRI/OCI | Residential/commercial from relative permitted; **agricultural land/plantation/farmhouse cannot be gifted** (para 3.1.2) [V] → `FAM_NRI_AGRI_GIFT_BLOCKED` |
| Listed-country nationals (Pakistan, Bangladesh, Sri Lanka, Afghanistan, China, Iran, Nepal, Bhutan, Macau, Hong Kong, DPRK) | Prior RBI permission; not applicable to OCIs (paras 9.1–9.2) [V] |
| Partition allotment of inherited agricultural land to NRI heir | Inheritance vs transfer unclear; interim Equator policy: no allotment of agricultural land to an NRI/OCI beyond the inherited share without counsel clearance **[VERIFY — open: counsel Q8 in S1 §14]** → W + counsel |
| Remittance of sale proceeds | FEM (Remittance of Assets) Regulations 2016 — up to USD 1 million per financial year with documents; Forms 145/146 (ITA 2025, r.220); TDS under ITA 2025 s.393(2) [K] |
| Execution abroad | Notarised + apostilled (India party to the Hague Apostille Convention since 2005) or consularised; stamp in India within the state window after receipt [K]; Registration Act s.33 for powers of attorney executed abroad [K] |

### 3.11 Elders (MWPSC Act 2007) and court-annexed channels
| Section / channel | Content | Product use |
|---|---|---|
| s.2(b), (d), (g), (h) | Maintenance includes food, clothing, residence, medical; parent incl. step/adoptive, whether or not a senior citizen (s.2(d)); relative = legal heir of childless senior; senior citizen = Indian citizen 60+ | eligibility (age/citizenship for seniors; any age for parents) |
| s.4 | Claim against adult children or, if childless, relatives | respondent picker |
| s.5(1), (2), (4) | Application by senior or authorised person/organisation; interim allowance; disposal within 90 days of service of notice, extendable once by 30 days | clock `fam_mwpsc_disposal_90d` (informational) |
| **s.6(6)** | Tribunal may refer the application to a Conciliation Officer before hearing; findings within one month; Explanation: Conciliation Officer = any person or representative of an organisation in the Explanation to s.5(1), or Maintenance Officers under s.18(1), or any other person nominated by the Tribunal [Verified 22 Oct 2026: India Code] **[VERIFY — open: state rules per launch state]** | B2G mode `fam.mwpsc_conciliation.v1` |
| ss.9, 10, 11, 12 | Cap ₹10,000/month (state-prescribed, ≤ cap); alteration; enforcement as BNSS maintenance order; election MWPSC or BNSS | estimator cap; D05 check |
| ss.16, 17, 18 | Appeal 60 days; **no legal practitioner** before Tribunal; Maintenance Officer may represent | conciliator must not act as advocate |
| s.23 | Transfer subject to condition of basic amenities voidable at transferor's option; Tribunal may restore property/evict (*Urmila Dixit v Sunil Sharan Dixit*, SC, 2 Jan 2025) [V]; condition required (*Sudesh Chhikara v Ramti Devi*, 2022) [K]; daughter-in-law's DV shared-household right harmonised (*S. Vanitha v Deputy Commissioner* (2021) 15 SCC 730) [K] | restoration claim flow |
| s.27 | Civil court jurisdiction barred | forum gating |
| Family Courts Act 1984 s.9 | Court's duty to assist settlement; ss.5–6 counsellors; s.11 in camera; s.13 no right to legal representation | court-referral mode |
| CPC s.89 / O.X r.1A | Referral to ADR; family/partition matters suitable (*Afcons Infrastructure v Cherian Varkey* (2010) 8 SCC 24) | court-referral intake |
| *K. Srinivas Rao v D.A. Deepa* (2013) 5 SCC 226 | Early referral of matrimonial disputes to mediation; pre-litigation desks | pre-litigation copy |
| PWDVA s.14 + rr.13–14 | Counselling referral by Magistrate | Equator is not a s.10 service provider (State registration; PWDV Rules r.11(3)(a) three years' prior service) — signpost only **[VERIFY — open (counsel): §18.1 Q16]** |
| LSA Act ss.19–22 | Lok Adalat award deemed civil-court decree; final | Lok Adalat recording pack for maintenance/money heads |

### 3.12 Legal Rules Register additions (seed into Appendix G §G.2.10)
| Rule ID | Rule statement | Source | Status | Effect | Enforcement | Flag | Verify |
|---|---|---|---|---|---|---|---|
| LR-FAM-013 | Instant triple talaq (talaq-e-biddat) is void; Equator never drafts, records or facilitates it; civil consequences may be mediated at the wife's request; criminal limb goes to the Magistrate | MW(PRM) Act 2019 ss.3–7; *Shayara Bano* (2017) 9 SCC 1 | IN_FORCE | protective | `intake`/`ai` HB `FAM_TRIPLE_TALAQ_BLOCKED`; S | — | — |
| LR-FAM-014 | Khula is the wife's right not dependent on the husband's consent; the platform never requires husband's consent as a precondition and routes declaration to the Family Court | *Mohammed Arif Ali v Afsarunnisa* (Telangana HC DB, 24 Jun 2025) | IN_FORCE (HC authority, persuasive outside Telangana) | protective (information + Family Court pack only; no status claim) | `routing` CFG | `fam.khula_pathway` (ON) | **[VERIFY — open: persuasive value per launch state; §18.1 Q4]** — ON is permitted only because the pathway is protective framing; any status claim or permissive use needs the marker cleared |
| LR-FAM-015 | A divorced Muslim woman may claim under BNSS s.144 in addition to the 1986 Act; copy must not imply exclusivity | *Mohd. Abdul Samad v State of Telangana*, 2024 INSC 506 | IN_FORCE | protective | `templates` lint | — | — |
| LR-FAM-016 | DV-adjacent settlement only at the aggrieved woman's request; non-recurrence undertaking mandatory; justification statements flagged; mediator certificate "not vitiated by force, fraud or coercion" | PWDV Rules 2006 rr.13–14 (Equator policy outside s.14 referrals) | IN_FORCE (statute + policy) | protective | `outcomes` HB `FAM_DV_PRECONDITION` | — | — |
| LR-FAM-017 | Child-removal risk (passport/travel intent, threat to take abroad) halts mediation scheduling and signposts the Family Court/HC | GWA s.25; *Nithya Anand Raghavan*; Equator policy | IN_FORCE (policy) | protective | `routing` HB `FAM_URGENT_CHILD_REMOVAL` | — | — |
| LR-FAM-018 | Uttarakhand UCC: marriage registration within 60 days; divorce decree registration within 60 days of becoming final; live-in statement within one month (s.387 penalty); dissolution only under the Code (s.29) | UCC 2024; UCC Rules r.8 | PARTIALLY_IN_FORCE **(UNVERIFIED official text)** | protective (warnings) / computational (calculator) | `clocks` C; W | `fam.ucc_uk` (OFF) | **[VERIFY — open (watch): Rules r.8(2) 60-day decree registration verified 22 Oct 2026 (ucc.uk.gov.in); Act text and 2026 Ordinance amendments to live-in/penalty sections not yet obtained]** |
| LR-FAM-019 | MWPSC: a senior citizen applicant must be an Indian citizen aged 60+; a parent may claim against a child whether or not a senior citizen (s.2(d)); election between MWPSC and BNSS (s.12); Tribunal-referred conciliation report within one month; no advocate appears for parties in Tribunal-referred conciliation | MWPSC ss.2(d), 2(h), 6(6), 12, 17 | IN_FORCE | protective | `intake` HB/W; `clocks` C | — | **[VERIFY — open (counsel): citizenship requirement for parents under 60; s.17 at conciliation stage — ss.2(d), 2(h), 6(6) one month and Explanation, 12, 17 verified 22 Oct 2026 (India Code)]** |
| LR-FAM-020 | Elder Tribunal cap: an *estimate* labelled "Tribunal order" never exceeds the state-notified maximum (≤ ₹10,000/month); private care agreements may exceed it | MWPSC s.9(2) | IN_FORCE | computational | `rules` calculator CFG | — | state matrix |
| LR-SUCC-013 | ISA s.213 is omitted; copy may not state probate is mandatory in Mumbai/Kolkata/Chennai; supersedes the s.213 citation in LR-SUCC-007 | Repealing and Amending Act 2025 (assent 20 Dec 2025) | IN_FORCE | protective | `templates` lint `probate_mandatory_claim` | — | [Verified 22 Oct 2026: Act No. 37 of 2025, Second Schedule Sl. 3, India Code] |
| LR-SUCC-014 | Muslim wasiyat beyond 1/3 or (Hanafi) to an heir requires heirs' consent (Hanafi: after death); distribution MSA blocked until consents recorded | Muslim personal law (Shariat Act s.2) | IN_FORCE | protective | `outcomes` HB `FAM_WASIYAT_CONSENT_MISSING` | — | — |
| LR-SUCC-015 | HUF partition outputs carry an ITA 2025 s.315 warning and checklist; partial partition is not recognised for tax | Income-tax Act 2025 s.315 | IN_FORCE | protective | `outcomes` W | — | — |
| LR-SUCC-016 | Agricultural land/plantation/farmhouse may not be gifted to NRI/OCI; inheritance is permitted; allotment in partition → counsel | RBI MD 12/2015-16 paras 3.1.2–3.1.4; NDI Rules 2019 | IN_FORCE | protective | `outcomes` HB `FAM_NRI_AGRI_GIFT_BLOCKED`; W | — | allotment limb open |
| LR-SUCC-017 | Scheduled Tribe, Goa, Ismaili/Bohra and pre-2005 HSA deaths are outside the calculators (`out_of_scope_*`); counsel review mandatory | HSA s.2(2); Goa 2012 Act; *Ram Charan* | IN_FORCE | protective | `rules` calculator HB | — | — |
| LR-SUCC-018 | HSA s.15 pre-litigation mediation (SC direction 19 Nov 2025): sub-type and copy available only when counsel confirms that Equator mediation qualifies; never claim the settlement "is a decree" | SC order 19 Nov 2025 | UNVERIFIED | permissive | `routing` CFG | `fam.s15_prelit` (OFF) | **[VERIFY — open (counsel Q3 in 02 §5): order verified 22 Oct 2026 (*Snidha Mehra v UoI*, W.P.(C) 732/2020) — it names only Mediation Centres and Legal Services Authorities; keep OFF unless counsel confirms a private ODR mediation qualifies]** |
| LR-SUCC-019 | Muslim succession calculators (Hanafi, Shia Class I) are indicative and disabled when regime = `ucc_uttarakhand` | Shariat Act s.2; UCC s.49 | IN_FORCE | computational | `rules` calculator | `fam_succession_muslim` (OFF) | counsel sign-off of vectors |
| LR-SUCC-020 | Minors' and incapacitated heirs' shares cannot be released or relinquished; court permission task before execution (HMGA s.8(2); GWA s.29; CPC O.XXXII r.7 where suit pending; Mental Healthcare Act 2017 for adults with mental illness) | as stated | IN_FORCE | protective | `outcomes` HB `CLOSURE_BLOCKED` (`FAM_MINOR_PROPERTY_COURT_PERMISSION`) | — | Allotment-vs-alienation question open (S1 §14 Q11) |

LR-SUCC-007 is re-versioned: source "Indian Succession Act 1925 ss.276, 295; NN-06" (s.213 removed); LR-SUCC-006 flag `fam_succession_isa` may be switched ON for `isa_ch2@1` and `isa_parsi@1` once their golden vectors are signed off (computational rules — "indicative — figure under legal verification" label until then).

---

## 4. Suitability and eligibility rules

Rule pack `fam.suitability.v2` (deterministic, `packages/rules/verticals/fam/suitability.ts`; NN-01/NN-02). Evaluation order: **(1) hard exclusions → (2) urgent/safety triggers → (3) regime resolution → (4) mechanism gating → (5) completeness/conditions → (6) limitation and clocks**. First blocking outcome wins; non-blocking conditions accumulate.

### 4.1 Decision table
Outcomes: **A** accept · **AC** accept-with-conditions · **SP** signpost (case not opened, or opened only for civil terms) · **RJ** reject. Every row writes `routing_decisions.reasons[]` with the rule ID.

| Rule | Inputs | Outcome | Conditions / reason code |
|---|---|---|---|
| FAM-SR-01 | Request to record, draft or facilitate talaq-e-biddat / irrevocable instant talaqnama | RJ for that request; SP | `FAM_TRIPLE_TALAQ_BLOCKED`; offer civil-terms case (mahr, maintenance, custody, streedhan) only if the **wife** initiates |
| FAM-SR-02 | Any request to decide, compound, withdraw or "settle" an offence; dowry demand; sexual offence; POCSO; threats of violence | SP | EX-FAM-02..05; civil terms only via `fam.criminal_closure` if both parties consent and no safety flag on the requesting side blocks it |
| FAM-SR-03 | `urgent.child_removal_risk` or `urgent.cross_border_removal` | SP (scheduling halted) | `FAM_URGENT_CHILD_REMOVAL`; Family Court/HC first; case may reopen after court order |
| FAM-SR-04 | Child abuse disclosure | AC (paused) | safeguarding task ≤ 24 h; POCSO s.19 pathway; mediation of custody suspended until `safeguarding_lead` clears |
| FAM-SR-05 | Screening outcome `not_suitable_safety` for any party | SP | Protection Officer, 112, 181, One Stop Centre; case `signposted`; no mediation |
| FAM-SR-06 | Screening `shuttle_only` | AC | `safety_flag = true`; shuttle only; DV-trained mediator; LR-FAM-016 preconditions |
| FAM-SR-07 | Screening `not_suitable_capacity` | AC/SP | proceed only with lawful guardian / nominated representative (Mental Healthcare Act 2017); else SP to court |
| FAM-SR-08 | Destitution indicators (no food/shelter/income) | AC | DLSA legal aid (LSA Act s.12) + One Stop Centre shown first; CN-PROBONO/CN-DV concessions |
| FAM-SR-09 | Self-harm signal | AC (paused) | Tele-MANAS 14416 + human hand-off (FAM-G-05) |
| FAM-SR-10 | L1 `fam.probate_validity` | SP | `signpost_only`; offer `fam.family_settlement.instead_of_contesting_will` if all beneficiaries/heirs wish |
| FAM-SR-11 | L2 `guardianship_of_property` or sale of minor's immovable property | SP | District Court (HMGA s.8(2)/GWA s.29) permission pack |
| FAM-SR-12 | Mechanism = arbitration AND L1 ∉ property set | RJ for mechanism | `CASE_NOT_ARBITRABLE` (`FAM_NON_ARBITRABLE`) |
| FAM-SR-13 | Mechanism = arbitration AND L1 ∈ property set AND (`fam_property_arbitration` OFF OR LR-SUCC-011 not cleared) | RJ for mechanism | `LEGAL_RULE_UNVERIFIED`; mediation offered |
| FAM-SR-14 | Mechanism = arbitration AND any heir/co-owner not a signatory of a post-dispute arbitration agreement | RJ for mechanism | `FAM_ARB_ALL_HEIRS_REQUIRED` |
| FAM-SR-15 | Mechanism = negotiation.blind_bid AND (maintenance head AND vulnerability flag) OR safety_flag | RJ for mode | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` (`FAM_BLIND_BID_VULNERABLE`) |
| FAM-SR-16 | Regime resolver confidence < high, or R1/R2/R3/R10 hit, or `prefer_not_to_say` | AC | `counsel_review_required = true`; calculators and drafting HB until cleared |
| FAM-SR-17 | Regime = `customary_st` | AC | calculators `out_of_scope_customary`; ST land-transfer warning; counsel review |
| FAM-SR-18 | Regime = `goa_civil_code` | AC | calculator `out_of_scope_goa`; inventory check (minor/interdict/absent heir → inventory before Civil Judge) |
| FAM-SR-19 | Regime = `ucc_uttarakhand` AND `fam.ucc_uk` OFF | AC | information banner "Uttarakhand UCC may apply — counsel review"; no UCC calculators/templates |
| FAM-SR-20 | `muslim_school` ∈ {ismaili_khoja, dawoodi_bohra, ahmadiyya, unknown} | AC | counsel review; Muslim calculators disabled |
| FAM-SR-21 | Property L1 AND F-FAM-30 incomplete (predeceased child without descendants entered; no heir; cycle) | AC (deficient) | `deficiency` with field list; drafting HB |
| FAM-SR-22 | Property L1 AND any heir `not_willing` or `untraceable` | AC | proceed among willing; "share reserved" clause; `FAM_HEIRS_NOT_JOINED` blocks finalisation of whole-estate terms (LR-SUCC-009) |
| FAM-SR-23 | Minor or incapacitated heir | AC | court-permission task; minor's share ring-fenced; no release/relinquishment (LR-SUCC-020) |
| FAM-SR-24 | Asset `nature = wakf_or_trust` or title in Government | SP | out of scope (Waqf Tribunal / civil court) |
| FAM-SR-25 | Urgency `sale_or_mortgage_by_one_heir_imminent`, demolition/redevelopment, encroacher | AC | signpost civil court injunction / caveat first (last date "immediately"); mediation in parallel |
| FAM-SR-26 | Elder: applicant is not a parent of the respondent AND (not an Indian citizen OR age < 60) | AC | Tribunal route not available; private mediation only; BNSS s.144 for parents of any age. A parent claiming against a child may use the Tribunal at any age (s.2(d)) |
| FAM-SR-27 | Elder: existing BNSS s.144 order for same claim | AC | MWPSC s.12 election warning |
| FAM-SR-28 | Elder: Tribunal-referred (s.6(6)) | A | `fam.mwpsc_conciliation.v1`; no advocates; report within one month |
| FAM-SR-29 | Mutual divorce: separation < required period (1 yr HMA/SMA/PMDA; 2 yrs Divorce Act) | AC | interim arrangements now; petition-ready date computed; W |
| FAM-SR-30 | Mutual divorce: marriage < 1 year (HMA s.14 / SMA s.29 / UCC s.28) | AC | W `FAM_ONE_YEAR_BAR`; leave route explained |
| FAM-SR-31 | First motion presented and 18 months elapsing within 60 days | AC | hard alert + lawyer review (`fam_s13b_outer_18m`) |
| FAM-SR-32 | Pending court case on the same issue | A | court-recording pack (O.XXIII r.3 / consent terms); next date captured; no parallel adjudication |
| FAM-SR-33 | Court-referred (FCA s.9 / CPC s.89) | A | `source = court_referral`; R01 report = status + agreed terms only |
| FAM-SR-34 | Family-business head includes oppression/mismanagement/winding up relief | AC | corporate layer cross-routed to COM; NCLT signpost |
| FAM-SR-35 | NRI party, agricultural land to be gifted/released to NRI/OCI | AC | `FAM_NRI_AGRI_GIFT_BLOCKED` on that term; allotment → counsel |
| FAM-SR-36 | Listed-country foreign national heir acquiring immovable property | AC | RBI permission warning |
| FAM-SR-37 | `fam.s15_prelitigation` AND `fam.s15_prelit` OFF | A (as `hsa_female_15_2`) | no reference to SC direction in copy |
| FAM-SR-38 | Same-sex or transgender partners | A | civil, financial, parenting terms only; no marital-status term (*Supriyo v UoI*, 2023 INSC 920) |
| FAM-SR-39 | Respondent is a minor | RJ | minors never parties; guardian/next friend route via court |
| FAM-SR-40 | None of the above blocks | A | default ladder for L1 |

### 4.2 `regime_resolver` (D2-03 — derived, never asked bluntly)
Inputs come from the **marriage-form** and **family-law** questions (§5.2), not a bare "What is your religion?" field. Religion is asked only when the earlier answers cannot resolve the regime, with an explanation and `prefer_not_to_say` (which forces counsel review). Output: `{marriage_regime, succession_regime, muslim_school?, confidence: high|medium|low, reasons[], counsel_review_required, resolver_version}` per person (spouse or deceased). Stored in `fam.regime_resolutions`; raw religion answer is Tier-High encrypted, purpose-limited to routing (DPDP s.6; GDPR Art. 9 for EU parties) and never shown to the other party.

| Order | Rule | Result | Confidence |
|---|---|---|---|
| R1 | `st_status ∈ {st_with_certificate, st_claimed_no_certificate}` | `customary_st`; HSA/HMA/UCC off | medium; counsel |
| R2 | `uttarakhand_resident = true` AND relevant event (marriage, divorce petition, death) ≥ 27 Jan 2025 | `ucc_uttarakhand` | medium; counsel (events straddling 27 Jan 2025, pre-2025 marriages) |
| R3 | `goa_domicile = true` | `goa_civil_code` (+ Goa 2012 Act succession) | medium; counsel |
| R4 | `marriage_form = special_marriage_act` | marriage = SMA; succession = HSA if both spouses Hindu/Sikh/Jain/Buddhist (s.21A) else ISA Ch. II (s.21) | high |
| R5 | `marriage_form ∈ {hindu_rites_saptapadi, arya_samaj, anand_karaj}` or family law answer = "Hindu Succession Act family" | HMA/HAMA/HMGA/HSA | high |
| R6 | `marriage_form = nikah` or family law = Muslim | `muslim_{school}`; school question shown | high if school known; else low |
| R7 | `marriage_form = church_icma_1872` or family law = Christian | Divorce Act / ISA Ch. II | high |
| R8 | `marriage_form = parsi_ashirvad` | PMDA / ISA Ch. III | high |
| R9 | Jewish / other / none | ISA Ch. II; marriage by personal law or SMA | medium |
| R10 | `conversion_event ≠ none` between marriage and event | flag `conversion_conflict` | low; counsel |
| R11 | `marriage_form = foreign_civil` | applicable Indian Act if marriage registered under it; else counsel | low |
| R12 | `marriage_form = not_married_live_in` | no marital regime; PWDVA/UCC s.388 support; parenting | high |

The UI shows the result as "The rules that usually apply to your situation: *Hindu Marriage Act 1955 and Hindu Succession Act 1956*. Why: you said the marriage was performed with Hindu rites in Jaipur and no one in the family converted. Not right? Change your answers or ask for a lawyer review." (FR-V3-01).

### 4.3 Hard exclusions (Appendix K §3 codes, FAM rows)
| Code | Exclusion | Signpost | Copy anchor |
|---|---|---|---|
| EX-FAM-01 | Talaq-e-biddat drafting/recording | Magistrate; police (s.7(a) on information by wife or relatives); DLSA | "Instant triple talaq is void and illegal under section 3 of the Muslim Women (Protection of Rights on Marriage) Act 2019 and punishable under section 4. You may claim subsistence allowance (s.5) and custody of minor children (s.6) before the Magistrate. Lawful options are listed below." |
| EX-FAM-02 | Dowry demand / dowry offences (Dowry Prohibition Act 1961 ss.3–4; BNS s.80) | Police 112; Dowry Prohibition Officer; Magistrate | "Dowry is a crime. We cannot mediate it. Return of streedhan and other civil claims can be discussed separately." |
| EX-FAM-03 | Sexual offences; POCSO | Police 112; Childline 1098; SJPU | mandatory-reporting notice |
| EX-FAM-04 | Threats, violence, stalking needing protection | 112; 181; Protection Officer; One Stop Centre | quick-exit screen |
| EX-FAM-05 | Non-compoundable offence closure promised as a term | HC (BNSS s.528) | "Only the High Court can decide this. A settlement cannot promise it." |
| EX-FAM-06 | Status/custody/testamentary decision by award | Family Court / probate court | NN-06 copy |
| EX-FAM-07 | Wakf / trust / Government title | Waqf Tribunal / civil court | — |
| EX-FAM-08 | Minor as party | court (next friend) | — |

### 4.4 Urgent and safety triggers
| Code | Trigger (intake or in-session) | Action | SLA |
|---|---|---|---|
| U-FAM-01 | Fear of violence / recent violence / weapon access | `safety_flag`; quick-exit; helplines; shuttle-only or SP | immediate |
| U-FAM-02 | Plan to take child abroad; passport application; child already removed | halt scheduling; court-first copy "Mediation cannot stop a child being taken abroad. A court can, often on the same day."; Regional Passport Office representation note | ≤ 5 min to signpost |
| U-FAM-03 | Child abuse disclosure | `safeguarding_lead` task; POCSO s.19 | ≤ 24 h |
| U-FAM-04 | Self-harm | Tele-MANAS 14416; human | immediate |
| U-FAM-05 | Imminent sale/mortgage of family property by one heir | civil court injunction / caveat; lis pendens | immediate copy; case manager call ≤ 1 WD |
| U-FAM-06 | Elder abandonment (MWPSC s.24 offence) / abuse | Elderline 14567; police; Tribunal | immediate |
| U-FAM-07 | Eviction from shared household in progress | Protection Officer; Magistrate (PWDVA s.19 residence order) | immediate |

### 4.5 DV-adjacent policy (FR-V3-09; LR-FAM-016)
Precondition `dv.settlement_requested_by_aggrieved = true` captured privately from the aggrieved party in the sealed store; mediator is DV-endorsed and not connected to either party; non-recurrence undertaking clause auto-inserted; the moderation filter flags justification phrases ("she provoked", "he had to") in party drafts and caucus-to-joint messages; MSA cannot be finalised without the mediator certificate "terms not vitiated by force, fraud or coercion"; any escrow tranche tied to criminal-case outcome is blocked (`FAM_PRESSURE_CONDITION`).

### 4.6 Jurisdiction and limitation checks
- **Equator jurisdiction**: any party in India or abroad may use contractual mediation; seat for property arbitration = India (city chosen); governing law = Indian law (personal law per resolver). Court step forum computed: Family Court per HMA s.19 / SMA s.31 / Divorce Act s.3 [K]; GWA s.9 (child's ordinary residence); Sub-Registrar per Registration Act s.28 (property location); Maintenance Tribunal per MWPSC s.6(1).
- **Limitation/clock checks at intake** (each creates an owned clock or an informational date — Appendix A §6):

| Check | Source | Clock kind | Category |
|---|---|---|---|
| s.13B second motion window (6 m earliest; 18 m outer) | HMA s.13B(2) | `fam_s13b_cooling`, `fam_s13b_outer_18m` (**new**) | informational / statutory-alert (AP-L, B-INFO + lawyer task) |
| Exclusion from joint property | Limitation Act Art. 110 (12 y from knowledge) | `fam_exclusion_art110` (**new**) | statutory (AP-L, B-CRIT) when date of knowledge entered |
| Adverse possession | Art. 65 (12 y) | `fam_adverse_possession_art65` (**new**) | statutory |
| Maintenance arrears enforcement | BNSS s.144(3) proviso (1 y from due date) | `fam_bnss147_arrears_1y` (**new**) | informational |
| Probate/LoA | Art. 137 (continuing right) | none (text) | — |
| Registration presentation | Registration Act ss.23, 25 | `registration_4m` (+4 m fine window `registration_fine_4m` **new**) | statutory |
| MWPSC disposal | s.5(4) | `fam_mwpsc_disposal_90d` (**new**, +30) | informational |
| MWPSC conciliation report | s.6(6) | `fam_mwpsc_conciliation_1m` (**new**) | statutory (Tribunal-referred) |
| MWPSC appeal | s.16 (60 d) | `fam_mwpsc_appeal_60d` (**new**) | informational |
| UCC registrations | UCC Rules r.8 (60 d); s.387 (1 m live-in) | `fam_ucc_marriage_reg_60d`, `fam_ucc_divorce_reg_60d`, `fam_ucc_livein_1m` (**new**, flag) | informational |
| Mediation time-box | Equator Rules | `med_contract_timebox` FAM 120 d (marital) / 90 d (property and elder tracks, Appendix A §4.3.2; §7.7) | contractual |
| MSA reflection | FAM MSA clause 12 | `fam_msa_reflection` (default 7 d; 3–14) | contractual |

No Equator process pauses limitation (Appendix A clock invariant 3); every invitation carries "This invitation does not stop limitation periods running."

---

## 5. Dispute Explorer question tree (FAM)

Engine: Appendix K Explorer v2 (deterministic tree; the `intake_assistant` may classify free text into a branch but the tree computes routes — NN-01/NN-02). Plain English at or below class-8 reading level; Hindi parity mandatory; every FAM screen carries the **Quick exit** button (top-right, `Esc` twice, triple-tap on mobile) that replaces the page with the configurable external neutral page `explorer.quick_exit_url` (default google.co.in; X-25, Appendix K EP-06) and clears the tab history entry (FAM-G-07). Notifications for FAM use neutral subjects ("Your Equator update") — never the dispute type.

### 5.1 Entry and safety (all FAM branches)
| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| FX-00 | Are you safe to answer these questions now? | Yes · Not right now | Not right now → quick-exit + "Save and come back" (no SMS reminder) |
| FX-01 | What is this about? | Marriage or separation · Money support (maintenance) · Children · Family property or inheritance · A parent or grandparent needs support · Something else | → FX-02 then branch M / MN / C / P / E |
| FX-02 | Has anyone hurt you, threatened you, or made you afraid at home? | No · Yes, in the past · Yes, now · I'd rather not say | Yes, now → U-FAM-01 (SP outcome OC-SAFE); past/rather not say → sealed screening scheduled; nothing shown to other side |
| FX-03 | Is a child in danger, or might a child be taken out of India without agreement? | No · Child may be in danger · Child may be taken abroad · Child already taken | danger → U-FAM-03; abroad → U-FAM-02 (OC-CHILD-URGENT) |
| FX-04 | Is there a police case (FIR) or criminal case connected to this? | No · Yes · Not sure | Yes → F-FAM-02 criminal table; disclosure D-CRIM |

### 5.2 Regime questions (D2-03; shown only where the branch needs them)
| QID | Question | Options | Branching |
|---|---|---|---|
| RG-01 | How was your marriage performed or registered? | Hindu rites (saptapadi) · Arya Samaj · Anand Karaj (Sikh) · Nikah · Church · Parsi ceremony · Registered under the Special Marriage Act · Registered in Goa · Registered under Uttarakhand UCC · By tribal or community custom · Abroad, civil registration · We were not married (live-in) · Not sure | maps `marriage_form`; Nikah → RG-04; Not sure → RG-03 |
| RG-02 | Do you or your spouse (or the person who died) belong to a Scheduled Tribe? | No · Yes, with certificate · Yes, no certificate · Not sure | Yes → R1 |
| RG-03 | Which family law usually applies in your family? We ask only to find the right rules; you can skip. | Hindu law (also Sikh, Jain, Buddhist) · Muslim law · Christian law · Parsi law · Jewish law · None / other · Prefer not to say | Prefer not to say → counsel review (FAM-SR-16) |
| RG-04 | Which school of Muslim law does the family follow? | Sunni Hanafi · Sunni Shafi'i · Sunni Maliki/Hanbali · Shia Ithna Ashari · Ismaili (Khoja) · Dawoodi Bohra · Ahmadiyya · Don't know | Don't know → counsel |
| RG-05 | Did anyone change religion after the marriage (or before the death)? | No · Yes, before marriage · Yes, after marriage · Not sure | Yes after → R10 |
| RG-06 | Where is your (or the deceased's) permanent home state? | 36 States/UTs + Abroad | Goa → R3; Uttarakhand → RG-07 |
| RG-07 | For Uttarakhand: how are you connected to Uttarakhand? | Permanent resident · Lived there 1 year or more · Beneficiary of a State scheme · None | UCC s.3(1)(n) test → R2 |

### 5.3 Branch M — Marriage or separation
| QID | Question | Options | Branching / outcome |
|---|---|---|---|
| M-01 | What do you want to do? | Separate by agreement (divorce) · Wife wants khula · Both want mubarat · Talaq already given · Instant triple talaq was given · Live separately but stay married · Try to save the marriage · Not decided | triple talaq → OC-EX-TT (EX-FAM-01) + offer MN branch; khula → M-05; reconciliation → OC-MED-RECON |
| M-02 | When did you marry? | date | < 1 yr → W one-year bar |
| M-03 | Since when have you lived separately? | date; How: different homes · same home, separate lives · one abroad · not separated | computes petition-ready date per regime |
| M-04 | Has any court case been filed? (add all) | Divorce · Restitution (s.9) · Maintenance · Domestic violence · Custody · Criminal (cruelty/dowry) · Foreign court · None | adds D05 rows; pending → OC-MED-COURTPACK |
| M-05 | (Khula) Have you told your husband in writing that you want khula? | Yes, date · Not yet | output = khula settlement record + Family Court declaration pack; copy "The Telangana High Court (2025) has held that a husband's agreement is not needed for khula. A Family Court can confirm the khula." |
| M-06 | Do you have children under 18 or dependent? | No · Yes, number + age bands | Yes → C branch appended |
| M-07 | What must the agreement cover? (tick all) | Alimony/lump sum · Monthly maintenance · Children · Streedhan/gifts · Mahr · Home · Joint loans/accounts · Vehicles · Closing court cases · Other | sets heads; property heads → M4 band |
| M-08 | Is either of you living abroad? | No · Me · Spouse · Both | NRI pack; video appearance note |
| **Outcomes** | | | OC-MED-MUTUAL (mediation → s.13B/s.28/s.10A/s.32B/UCC s.27 pack) · OC-MED-KHULA · OC-MED-RECON · OC-NEG-FIRST (both opt in, no safety flag) · OC-EX-TT · OC-SAFE |

### 5.4 Branch MN — Maintenance
| QID | Question | Options | Branching |
|---|---|---|---|
| MN-01 | Who needs support? | Me (wife/husband) · Children · Both · My parents · Divorced wife (Muslim) | parents → E branch |
| MN-02 | Is there already a maintenance order or case? | No · Case pending (court, next date) · Order passed (amount, date) | set-off; variation route |
| MN-03 | What kind of payment do you want to discuss? | Monthly · One-time (lump sum) · Both · Not sure | — |
| MN-04 | Are you able to meet daily needs (food, rent) right now? | Yes · Hardly · No | No → FAM-SR-08 DLSA + One Stop Centre first |
| MN-05 | Main income type of the person paying | Salaried · Business · Farming · Professional · No income · Abroad | selects F-FAM-07 variant |
| **Outcomes** | | | OC-MED-MAINT (affidavits F-FAM-07 both sides, then estimator) · OC-SP-MAGISTRATE (free route shown first: BNSS s.144; DLSA) |

Free-forum disclosure D-MAINT (mandatory before payment): "You can apply for maintenance in the Family Court or Magistrate's court under section 144 of the BNSS. Court fees are minimal and the District Legal Services Authority gives free legal aid to women and children. Mediation here is optional."

### 5.5 Branch C — Children
| QID | Question | Options | Branching |
|---|---|---|---|
| C-01 | What do you need to agree about? (tick all) | Where the child lives · Time with each parent · School · Health · Travel/passport · Moving city or country · Child's expenses · Grandparents | — |
| C-02 | Is there a court order about the child? | No · Yes (India) · Yes (foreign court) | foreign → `fam.nri_cross_border.foreign_decree_alignment` |
| C-03 | Would you like the child's views to be heard by a trained specialist? (only age 7+ default, configurable) | No · Yes, if both parents agree | Yes → F-FAM-29 consents |
| **Outcomes** | | | OC-MED-PARENTING (plan "subject to court approval") · OC-CHILD-URGENT · never OC-ARB |

### 5.6 Branch P — Family property or inheritance
| QID | Question | Options | Branching |
|---|---|---|---|
| P-01 | What is the problem? | Dividing property after a death (no will) · There is a will — dispute about sharing · Someone says the will is fake/invalid · Dividing joint family (HUF) property · Buying out or selling jointly owned property · Splitting a family business · Rent/income from family property · Widow's or mother's right to live in the house · Need succession or legal-heir certificate · Bank/shares/insurance in a nominee's name · Other | will invalid → OC-SP-PROBATE (+ offer settlement instead of contest); certificate → OC-SP-CERT + heirship agreement offer |
| P-02 | Who died, and when? (add each person, in order of death) | name, date, place, regime questions RG-* | each death = separate succession event |
| P-03 | Who are the family members alive today? | family-tree builder (relations derived from the graph) | F-FAM-30 |
| P-04 | Is anyone under 18, or unable to decide for themselves? | No · Yes | FAM-SR-23 |
| P-05 | Is any heir abroad, not reachable, or unwilling? | All here and willing · Abroad · Cannot be found · Refuses | FAM-SR-22 |
| P-06 | What kinds of property? (tick all) | House/flat · Plot · Farm land · Shop/office · Bank/FDs · Shares/mutual funds · Insurance/PF/pension · Business · Gold/jewellery · Vehicles · Foreign assets · Loans owed | farm land → revenue-court note; foreign → counsel |
| P-07 | Is someone about to sell or mortgage the property? | No · Yes · Builder/redevelopment offer · Tenant/encroacher problem | Yes → U-FAM-05 |
| P-08 | Was the property divided earlier? | No · By talk only · Written memo · Registered deed (date) · Court decree (date) | pre-20 Dec 2004 deed/decree → LR-SUCC-003 |
| P-09 | (Hindu woman died without a will, her parents' family and husband's family both claim) | Yes · No | Yes AND flag ON → `s15_prelitigation` |
| **Outcomes** | | | OC-NEG-FAMILYMEET (rung 1) · OC-MED-PROPERTY · OC-ARB-PROPERTY (only if flag + all heirs) · OC-SP-PROBATE · OC-SP-CERT · OC-SP-CIVIL-URGENT · OC-COM-CROSS (business corporate layer) |

Free-forum disclosures: D-PROB ("Only a court can grant probate or decide whether a will is valid."); D-CERT ("A succession certificate is granted by the District Judge; a legal heir certificate by the Tahsildar/SDM."); D-REG ("Any deed that divides or transfers land or a house must be printed, stamped, signed in ink and registered at the Sub-Registrar office. E-signing is not enough.").

### 5.7 Branch E — Elders
| QID | Question | Options | Branching |
|---|---|---|---|
| E-01 | Who needs support? | Parent · Grandparent · Senior with no children · Senior couple | age + citizenship → FAM-SR-26 |
| E-02 | From whom? | Son · Daughter · Grandchild · Relative who will inherit · Daughter-in-law · Other | daughter-in-law → note (no direct s.4 liability) |
| E-03 | What is the problem? | Monthly money · Medical costs · Place to live · Gifted property not being cared for · Child refuses to leave senior's house · Neglect/abuse · Care plan · Seeing grandchildren | s.23 → OC-MED-ELDER-S23 + Tribunal signpost |
| E-04 | Did the senior give property to a child on a promise of care? | Gift deed with care condition · Gift deed silent · Will only · Sale · None | — |
| E-05 | Has anyone been abandoned or hurt? | No · Neglect · Money taken · Physical harm · Left alone | → U-FAM-06 |
| E-06 | What do you prefer? | Talk it out with a mediator · Tribunal's conciliation · Tribunal only · Not sure | — |
| **Outcomes** | | | OC-MED-ELDER · OC-SP-TRIBUNAL (always shown: free, no lawyer, the Act asks the Tribunal to decide within 90 days of notice (extendable once by 30 days), up to the state limit of ₹10,000/month or less) |

Explorer persistence: answers saved to `core.explorer_sessions` (P02) with `vertical = FAM`; FX-02/FX-03 answers are written only to `safety_sealed.explorer_flags` (token reference) and never returned by the general Explorer API.

---

## 6. Intake and submission forms per mechanism

Form engine conventions (P02): `sensitive` (Tier-High encryption), `visibleWhen`, `requiredWhen`, `mapsTo`, bilingual labels (en, hi). Form-resolution rule (Appendix K §4): `form = f(vertical, L1, L2, mechanism, role)`; L2s with identical fields share a schema with `visibleWhen` branches. Dropdown IDs (`DD-FAM-nn`) are defined in §6.9. Children are never parties; only initials and age band are stored in core (DPDP s.9; F `fam.family_members` CHECK).

### 6.1 Common blocks (embedded in every FAM form below)
**CB-PTY — Parties** (repeatable; min 2)
| field_id | label | type | req | options / dropdown | validation | help |
|---|---|---|---|---|---|---|
| pty.role | Your role in this matter | enum | Y | DD-FAM-01 | one `filer` per form | — |
| pty.person_ref | Person | ref (`core.persons`) | Y | — | KYC tier ≥ OTP for filer | Respondent may be "known by name and phone only" |
| pty.contact_channel | How should Equator contact them? | multi-enum | Y (≥1) | email · whatsapp · sms · post · through_counsel | if `safety_flag`, contact only via platform relay | Never share the other side's address |
| pty.language | Preferred language | enum | Y | DD-FAM-02 | — | — |
| pty.abroad_country | Country if living abroad | ISO-3166 | N | — | — | — |
| pty.representative | Representative (Letter of Authority / Vakalatnama) | ref | N | — | NN-27 scope | Family member, advocate or support person |
| pty.needs_support | Do they need help to take part? | multi-enum | N | DD-FAM-03 | — | interpreter, disability, low literacy |

**CB-REG — Regime block** (F-FAM-38 **new**; one per spouse or deceased; feeds §4.2): fields `reg.marriage_form` (DD-FAM-10), `reg.marriage_date` (date), `reg.marriage_place_state` (DD-FAM-12), `reg.marriage_registered` (DD-FAM-11), `reg.st_status` (DD-FAM-13), `reg.domicile_state` (DD-FAM-12), `reg.uk_residency_basis` (DD-FAM-14, visibleWhen domicile = UK or lived in UK), `reg.family_law` (DD-FAM-15, visibleWhen resolver needs it; `sensitive`), `reg.muslim_school` (DD-FAM-16, visibleWhen family_law = muslim or marriage_form = nikah), `reg.conversion_event` (DD-FAM-17), `reg.conversion_date` (date, requiredWhen conversion ≠ none). Validation: `marriage_date` ≤ today; `conversion_date` ≥ 1900-01-01. Output (read-only panel): resolver result + reasons + "Change answers / ask for review".

**CB-PEND — Other cases and orders** (repeatable; mandatory "None" tick if empty — *Rajnesh* disclosure)
| field_id | label | type | req | options | validation |
|---|---|---|---|---|---|
| pend.kind | Type of case | enum | Y | DD-FAM-20 | — |
| pend.court | Court / police station | text + forum lookup | Y | — | — |
| pend.case_no / pend.cnr | Case/FIR no. / CNR | text | Y / N | — | CNR regex `^[A-Z]{4}\d{12}$` |
| pend.sections | Sections | multi-text | requiredWhen kind ∈ criminal kinds | — | BNS/BNSS/IPC numbers; IPC auto-mapped to BNS with "legacy" label |
| pend.next_date | Next date | date | N | — | ≥ today |
| pend.order_upload | Orders passed | file[] | N | — | PDF/JPG ≤ 25 MB |
| pend.maint_amount_minor | Maintenance already ordered (₹/month) | money | requiredWhen kind ∈ maintenance kinds AND order passed | — | ≥ 0 |
| pend.classification | (staff) Quashability class | enum | system | compoundable · quashable_if_private · not_quashable | deterministic table by section (FR-P08-36.3) |

**CB-CHD — Children** (repeatable): `chd.initials` (text 1–3 chars, Y), `chd.age_band` (DD-FAM-21, Y), `chd.lives_with` (DD-FAM-22, Y), `chd.special_needs` (bool, N, `sensitive`), `chd.school_stage` (DD-FAM-23, N), `chd.passport_held_by` (DD-FAM-24, N). Validation: max 12 children; no names; no DOB in core (DOB, if needed for court packs, captured in the sealed store and rendered only into the court document).

**CB-HEADS — Issues** (multi-enum DD-FAM-30; ≥ 1) with per-head `head.position` (text ≤ 500 chars) and `head.amount_minor` (money, where monetary).

**CB-CONS — Consents**: agreement to the Equator FAM Rules version (hash), online mode, no recording (NN-11), language, data notice (DPDP; children's data with guardian consent `GUARDIAN_CONSENT_REQUIRED`), fee allocation, optional standstill (flag `prelit.standstill_template` OFF pending counsel Q-C1; Appendix K §5.3).

### 6.2 Negotiation request — F-FAM-35 (**new**; L1 all except probate/DV/criminal; disabled when `safety_flag`)
| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| neg.mode | How do you want to talk? | enum | Y | DD-FAM-40 (assisted_messages · family_meeting · structured_offers; blind_bid shown only for non-maintenance money heads and no vulnerability) | FAM-SR-15 | "A case manager keeps it polite and on record." |
| neg.heads | What to agree | CB-HEADS | Y | — | — | — |
| neg.first_offer | Your first proposal (optional) | rich text + money lines | N | — | offers open ≥ 14 days; without-prejudice flag auto-true | Never shared until you click Send |
| neg.time_box_days | Time to try | int | Y | default 14 (marital) / 21 (family meeting) | 7–30 | — |
| neg.escalate_to | If no agreement | enum | Y | mediation · conciliation · stop | — | — |
| + CB-PTY, CB-REG (if property/marital), CB-PEND, CB-CONS | | | | | | |

### 6.3 Mediation / conciliation request — F-FAM-02 (marital, maintenance, children, matrimonial property, DV civil, criminal-closure civil terms, NRI) and F-FAM-32 (property group) and F-FAM-34 (elder)
**F-FAM-02 additional fields**
| field_id | label | type | req | options | validation | help |
|---|---|---|---|---|---|---|
| med.mechanism | Process | enum | Y | DD-FAM-41 (mediation · conciliation_part_iii) | conciliation → s.62 invitation text; only civil/property heads produce s.73 | Conciliation can give an agreement the status of an award for money/property terms |
| med.l1 / med.l2 | Type / sub-type | enum | Y | §2 | taxonomy validity | prefilled from Explorer |
| med.outcome_sought | What outcome do you want? | enum | Y | DD-FAM-31 | khula → F-FAM-39 appended | — |
| med.separation_date | Living separately since | date | requiredWhen L1 = divorce_* | — | ≤ today; computes petition-ready date | — |
| med.separation_type | How | enum | requiredWhen above | DD-FAM-32 | — | — |
| med.talaq_status | Has any talaq been pronounced? | enum | requiredWhen regime = muslim | DD-FAM-33 | `instant_triple` → FAM-SR-01 | — |
| med.mehr | Mahr amount and status | money + enum | requiredWhen marriage_form = nikah | DD-FAM-34 | — | — |
| med.streedhan_holder | Who holds streedhan/gifts | enum | N | DD-FAM-35 | inventory upload when ≠ wife | list with photos |
| med.facts | What happened (short) | text | Y | — | ≤ 200 words; PII lint on children's names | AI may tidy grammar only on request (App. M) |
| med.urgent_interim | Anything needed now? | multi-enum | N | DD-FAM-36 | — | goes to F-FAM-08 |
| med.court_route_pref | Court-approved terms or private agreement? | enum | Y (marital) | court_decree · private_with_withdrawal · undecided | — | — |
| med.mediator_pref | Mediator preferences | multi | N | gender (DD-FAM-05), language, specialisation (DD-FAM-06) | DV-endorsed forced when safety flag | — |
| med.mode | Online / in person / hybrid | enum | Y | DD-FAM-04 | — | — |
| + CB-PTY, CB-REG, CB-PEND, CB-CHD (if children), CB-HEADS, CB-CONS | | | | | | |

**F-FAM-32 Partition / family settlement request** (P08 fields retained) adds: `prop.desired_outcome` (DD-FAM-50, Y), `prop.assets_in_scope` (refs to F-FAM-31, Y ≥ 1), `prop.prior_partition` (DD-FAM-51, Y), `prop.records_status` (DD-FAM-52, Y), `prop.urgency` (DD-FAM-53, Y), `prop.instrument_pref` (DD-FAM-54, N), `prop.arbitration_optin` (bool, N; visibleWhen flag ON; separate e-sign by **every** heir), `prop.s15_context` (bool, visibleWhen flag `fam.s15_prelit`). Requires F-FAM-30 and F-FAM-31 complete before submission (`VALIDATION_FAILED` with field list).

**F-FAM-34 Elder request** adds: `eld.senior_age` (int, Y, ≥ 60 for Tribunal route unless the applicant is a parent claiming against a child — s.2(d)), `eld.citizenship` (enum indian · other, Y), `eld.relationship_of_respondents` (DD-FAM-60, Y), `eld.issues` (DD-FAM-61, Y), `eld.prior_transfer` (DD-FAM-62, Y), `eld.transfer_date` (date, requiredWhen transfer ≠ none), `eld.abuse` (DD-FAM-63, Y; sealed), `eld.route_pref` (DD-FAM-64, Y), `eld.existing_bnss_order` (bool, Y → FAM-SR-27), `eld.authorised_org` (ref, N — MWPSC s.5(1) organisation filing on behalf).

### 6.4 Arbitration request / statement of claim — F-FAM-37 (**new**, notice of arbitration) and F-FAM-24 (SoC) — property group only
Visible only when L1 ∈ property set AND FAM-SR-12/13/14 pass.
| field_id | label | type | req | options | validation |
|---|---|---|---|---|---|
| arb.agreement_ref | Post-dispute arbitration agreement signed by all heirs/co-owners | ref (e-sign txn) | Y | — | every F-FAM-30 heir with `joined_as_party` = true signed; date > dispute date (`FAM_ARB_ALL_HEIRS_REQUIRED`) |
| arb.heads | Arbitrable heads | multi-enum | Y | DD-FAM-55 (partition_allotment · owelty · accounts_rent · mesne_profits · buyout_price · business_assets_division · mahr_debt · streedhan_money_value) | no status/custody/testamentary/maintenance heads (`CASE_NOT_ARBITRABLE`) |
| arb.seat_city | Seat | enum | Y | Equator cities | India only |
| arb.tribunal_size | Arbitrators | enum | Y | 1 · 3 | NN-03 equal-footing not applicable (family): Equator appoints all |
| arb.claim_value_minor | Declared value | money | Y | — | party-entered; never AI-estimated (NN-01) |
| soc.facts / soc.reliefs / soc.documents | Statement of claim | AI Pleadings Studio draft (App. M) | Y | — | NN-25 anchors; user approves each section |
| arb.registration_ack | I understand an award dividing land must be stamped and registered | bool | Y | — | true |

### 6.5 Response / statement of defence / counterclaim — F-FAM-04 (response), F-FAM-25 (SoD, arbitration only)
| field_id | label | type | req | options | validation |
|---|---|---|---|---|---|
| rsp.decision | Your reply | enum | Y | DD-FAM-42 (accept · accept_with_conditions · propose_other_dates_or_mediator · need_more_information · decline · object_to_forum) | decline reason optional and sealed |
| rsp.conditions | Conditions | multi-enum | requiredWhen accept_with_conditions | DD-FAM-43 (separate_sessions · woman_mediator · different_language · support_person · in_person · interpreter · no_contact_details_shared) | — |
| rsp.counter_heads | Issues you want added | CB-HEADS | N | — | — |
| rsp.counterclaim | Counterclaim (property arbitration) | money heads | N | DD-FAM-55 | arbitrable heads only |
| rsp.own_screening | Private safety questions | link to F-FAM-26 | Y before any joint session | — | sealed |
| rsp.regime_confirm | Do you agree with the rules shown? | enum | Y | agree · disagree (reason) · not_sure | disagree → counsel review |
| sod.paras | Para-wise reply (SoD) | Pleadings Studio | Y (arbitration) | admit · deny · not_known | NN-25 |
| + CB-PTY (own), CB-PEND (additions), CB-CONS | | | | | |
Response window: 14 days from deemed service, +7 once on request (Appendix A `response_window`).

### 6.6 Vertical forms — retained (P08 FR-P08-39) with v2 changes
| Form | v2 change |
|---|---|
| F-FAM-07 Affidavit of assets and liabilities | Three variants by `income_profile` (DD-FAM-37): **I general** (salaried/professional/unemployed/NRI), **II agricultural** (holdings table: state, village, khasra, area, crop, annual income), **III business** (entity, PAN/GSTIN, turnover 3 yrs, drawings) — mirroring *Rajnesh* Enclosures; perjury declaration; notarisation option |
| F-FAM-26 Screening (sealed) | Outcomes add `not_suitable_capacity` (§18.2 C-06); re-run before every session; DV indicators list DD-FAM-70 |
| F-FAM-29 Child-inclusive consent | Child assent captured by specialist; default minimum age 7 (config 5–12); "never asked to choose" acknowledgement |
| F-FAM-30 Family tree | `relation_code` derived by graph engine (DD-FAM-80 Class I codes; Class II entries); `religion_at_death` via CB-REG; `death_order` int; `commorientes` bool → counsel |
| F-FAM-31 Estate inventory | Per asset: `nature` (DD-FAM-56), `acquired_from` (DD-FAM-57 for HSA s.15(2)), `who_paid` / `source_of_funds` (benami check), `nominees[]`, `ulpin` (14 digits), `ror_ref`, `encumbrance`, `possession_with`, `valuation_source` (F enum) |
| F-FAM-33 Terms sheet | `instrument_type` (DD-FAM-54); `requires_registration` computed; minors' permission ref; NRI agricultural check; s.315 warning for HUF; wasiyat consents |

### 6.7 Vertical forms — new
| Form | Fields (id: type, req, options/validation) |
|---|---|
| **F-FAM-39 Khula record intake** | `kh.demand_date` date Y; `kh.demand_mode` enum Y (written_notice · email · through_relatives · dar_ul_qaza); `kh.mahr_offer` enum Y (return_full · return_part · forgo_unpaid · no_mahr_due) + amount; `kh.reconciliation_attempts` text Y (≤ 300 words; *Arif Ali* summary inquiry); `kh.iddat_maintenance` money N; `kh.custody_terms` link F-FAM-17; `kh.declaration_pack` bool Y. Validation: no field asks for the husband's consent (LR-FAM-014). |
| **F-FAM-40 Wasiyat heirs' consent** | per heir: `ws.heir_ref` Y; `ws.bequest_ref` Y; `ws.consent` enum Y (consent · refuse); `ws.signed_after_death` bool Y (Hanafi must be true); `ws.ila_certificate` file Y; e-sign Y. Blocks distribution MSA until complete (`FAM_WASIYAT_CONSENT_MISSING`). |
| **F-FAM-41 NRI execution pack request** | `nri.country` ISO Y; `nri.hague_apostille_member` bool (lookup) Y; `nri.instrument` enum Y (consent_affidavit · release_deed · spa · partition_deed_counterpart); `nri.execution_mode` enum Y (apostille · consular · travel_to_india · spa_holder); `nri.stamp_state` Y; `nri.received_in_india_on` date N (starts state stamp window); `nri.agri_land_involved` bool Y (→ LR-SUCC-016). |
| **F-FAM-42 Tribunal referral intake (MWPSC s.6(6))** | `trib.tribunal` forum ref Y; `trib.order_ref` text Y; `trib.referral_date` date Y (starts `fam_mwpsc_conciliation_1m`); `trib.application_upload` file Y; `trib.parties` CB-PTY Y; `trib.no_advocate_ack` bool Y (s.17 policy); `trib.report_due` computed. |
| **F-FAM-43 Succession / legal-heir certificate assistance** | `sc.purpose` enum Y (DD-FAM-58); `sc.deceased` ref F-FAM-30 Y; `sc.debts_securities` table Y (institution, account masked, amount); `sc.heirs_agreed` bool Y; `sc.heirship_agreement` link (mediable heads) N; `sc.court` forum ref (District Judge s.372) Y; output = facts schedule + annexure index (counsel files; Equator does not file). |

### 6.8 Mechanism × form matrix
| L1 group | Negotiation | Mediation / conciliation | Arbitration | Response |
|---|---|---|---|---|
| Marital (divorce_*, JS/RCR, maintenance, custody, matrimonial_property, NRI) | F-FAM-35 | F-FAM-02 (+07, 17, 29, 39) | — (matrimonial_property money/title heads only via F-FAM-37 when flag) | F-FAM-04 |
| DV civil / criminal closure | — | F-FAM-02 (shuttle; F-FAM-12 memo) | — | F-FAM-04 |
| Property (succession, partition, settlement, will distribution, co-owner, business) | F-FAM-35 (family_meeting) | F-FAM-32 (+30, 31, 33, 40, 41, 43) | F-FAM-37 + F-FAM-24 | F-FAM-04 / F-FAM-25 |
| Elder | F-FAM-35 | F-FAM-34 / F-FAM-42 | — | F-FAM-04 |
| Probate validity / guardianship of property / triple talaq | — | — | — | signposting record only |

### 6.9 Dropdown Master List (seed `core.form_option_sets`, set code `fam.*`; labels en + hi)
| ID | Set | Values (code → label) |
|---|---|---|
| DD-FAM-01 | party role | spouse_a · spouse_b · parent · heir · coparcener · karta · co_owner · senior_citizen · child_of_senior · relative · executor · beneficiary · guardian_of_minor · business_partner · in_law_title_holder |
| DD-FAM-02 | language | en · hi · mr · ta · te · kn · bn · gu · pa · ml · or · ur · other |
| DD-FAM-03 | support needs | interpreter · sign_language · screen_reader · low_literacy_assist · support_person · elder_assist · none |
| DD-FAM-04 | mode | online · in_person · hybrid |
| DD-FAM-05 | mediator gender preference | no_preference · woman · man |
| DD-FAM-06 | specialisation | hindu_personal_law · muslim_personal_law · christian_divorce_act · parsi_matrimonial · special_marriage_act · goa_civil_code · tribal_customary · uk_ucc · nri_cross_border · child_inclusive · dv_endorsed · elder_care · succession_partition · family_business · agricultural_land |
| DD-FAM-10 | marriage form | hindu_rites_saptapadi · arya_samaj · anand_karaj · nikah · church_icma_1872 · parsi_ashirvad · special_marriage_act · goa_civil_registration · uttarakhand_ucc_registered · customary_tribal · foreign_civil · not_married_live_in · not_sure |
| DD-FAM-11 | marriage registered | yes_state_rules · yes_sma · yes_uk_ucc · yes_goa · no · not_sure |
| DD-FAM-12 | state/UT | 28 States + 8 UTs (ISO 3166-2:IN codes) · abroad |
| DD-FAM-13 | ST status | not_st · st_with_certificate · st_claimed_no_certificate · not_sure |
| DD-FAM-14 | UK residency basis | permanent_resident · lived_1yr_plus · scheme_beneficiary · none |
| DD-FAM-15 | family law (sensitive) | hindu_sikh_jain_buddhist · muslim · christian · parsi · jewish · none_other · prefer_not_to_say |
| DD-FAM-16 | Muslim school | sunni_hanafi · sunni_shafii · sunni_maliki_hanbali · shia_ithna_ashari · shia_ismaili_khoja · shia_dawoodi_bohra · ahmadiyya · unknown |
| DD-FAM-17 | conversion event | none · before_marriage · after_marriage · after_death_of_relative · not_sure |
| DD-FAM-20 | pending case kind | divorce_petition · rcr_s9 · judicial_separation · nullity · maintenance_bnss_144 · hama_18_20 · hma_24_25 · dv_act_s12 · custody_gwa · habeas_corpus · criminal_bns_85_86 · dowry_act · mwprm_s4 · bnss_528_quashing · partition_suit · probate_loa · succession_certificate · mwpsc_tribunal · revenue_mutation · foreign_court · lok_adalat · none |
| DD-FAM-21 | child age band | 0_5 · 6_12 · 13_17 · 18_plus_dependent |
| DD-FAM-22 | child lives with | mother · father · shared · grandparents · other_relative · hostel |
| DD-FAM-23 | school stage | pre_school · primary · middle · secondary · higher_secondary · college · not_in_school |
| DD-FAM-24 | passport held by | mother · father · child_none · court · unknown |
| DD-FAM-30 | issues/heads | mutual_divorce_terms · permanent_alimony · interim_maintenance · child_maintenance · education_medical_extras · custody_residence · access_schedule · passport_travel · relocation · streedhan_return · mahr · matrimonial_home · joint_loans_accounts · vehicles · insurance_pf_nominations · withdrawal_of_cases · non_disparagement · reconciliation_plan · partition · owelty · rent_accounts · buyout · business_split · elder_allowance · elder_residence · care_plan · s23_property · other |
| DD-FAM-31 | outcome sought | mutual_divorce · khula · mubarat · talaq_consequences · judicial_separation · reconciliation · maintenance_only · parenting_plan_only · property_only · undecided |
| DD-FAM-32 | separation type | different_houses · same_house_separate_lives · one_abroad · not_separated |
| DD-FAM-33 | talaq status | none · single_ahsan (date) · hasan_successive_tuhr · instant_triple → block · talaqnama_sent · not_applicable |
| DD-FAM-34 | mahr status | prompt_paid · prompt_unpaid · deferred_unpaid · remitted_hiba_e_mehr · not_applicable |
| DD-FAM-35 | streedhan held by | wife · husband · in_laws · bank_locker · mixed |
| DD-FAM-36 | urgent interim needs | interim_maintenance · residence · school_fees · interim_contact · no_contact · asset_preservation · none |
| DD-FAM-37 | income profile | salaried · self_employed_business · agricultural · professional · unemployed · nri_foreign_income |
| DD-FAM-40 | negotiation mode | assisted_messages · family_meeting · structured_offers · blind_bid (restricted) |
| DD-FAM-41 | process | mediation · conciliation_part_iii |
| DD-FAM-42 | response decision | accept · accept_with_conditions · propose_other_dates_or_mediator · need_more_information · decline · object_to_forum |
| DD-FAM-43 | response conditions | separate_sessions · woman_mediator · different_language · support_person · in_person · interpreter · no_contact_details_shared |
| DD-FAM-50 | property outcome | partition_by_metes_and_bounds · allotment_with_owelty · sale_and_divide · buy_out_by_one_heir · life_interest_for_widow_then_split · rent_sharing · family_business_split · relinquishment_by_some_heirs · memorandum_of_past_arrangement · settlement_instead_of_will_contest |
| DD-FAM-51 | prior partition | none · oral · memorandum · registered_deed · decree · pre_20_dec_2004 |
| DD-FAM-52 | records status | mutated_to_heirs · still_in_deceased_name · mutated_to_one_heir_only · disputed_entry · not_sure |
| DD-FAM-53 | property urgency | sale_or_mortgage_imminent · tenant_or_encroacher · demolition_redevelopment_offer · tax_notice · none |
| DD-FAM-54 | instrument type | memorandum_recording · operative_partition_deed · family_settlement_deed · release_deed · gift_deed · consent_terms_in_suit · arbitral_award · reconveyance_deed |
| DD-FAM-55 | arbitrable heads | partition_allotment · owelty · accounts_rent · mesne_profits · buyout_price · business_assets_division · mahr_debt · streedhan_money_value |
| DD-FAM-56 | asset nature | self_acquired · ancestral_coparcenary · huf_declared · jointly_owned · stridhan · goa_communion · tribal_land · wakf_or_trust (out of scope) · government_lease |
| DD-FAM-57 | acquired from (female intestate) | father · mother · husband · father_in_law · self · other |
| DD-FAM-58 | certificate purpose | bank_deposits · shares_demat · mutual_funds · pf_pension_gratuity · insurance · decretal_debt · mutation · utility_transfer · society_transfer · other |
| DD-FAM-60 | elder respondent | son · daughter · grandchild · relative_heir · daughter_in_law · other |
| DD-FAM-61 | elder issues | monthly_maintenance · medical_costs · residence_right · return_of_gifted_property_s23 · eviction_of_child · abuse_neglect · care_arrangement · grandchild_access |
| DD-FAM-62 | prior transfer | gift_deed_with_care_condition · gift_deed_silent · will_only · sale_to_child · none |
| DD-FAM-63 | elder abuse (sealed) | none · verbal · financial · physical · abandonment |
| DD-FAM-64 | elder route preference | conciliation_before_tribunal · family_mediation · tribunal_only · dont_know |
| DD-FAM-70 | screening indicators (sealed) | past_violence · current_fear · coercive_control · threats · weapons_access · stalking_online_abuse · substance_misuse · child_safety_concern · child_removal_risk · protection_order_exists · power_imbalance_financial · self_harm_risk · capacity_concern |
| DD-FAM-80 | HSA Class I relation codes (derived) | son · daughter · widow · mother · son_of_predeceased_son · daughter_of_predeceased_son · son_of_predeceased_daughter · daughter_of_predeceased_daughter · widow_of_predeceased_son · son_of_predeceased_son_of_predeceased_son · daughter_of_predeceased_son_of_predeceased_son · widow_of_predeceased_son_of_predeceased_son · son_of_predeceased_daughter_of_predeceased_daughter · daughter_of_predeceased_daughter_of_predeceased_daughter · daughter_of_predeceased_son_of_predeceased_daughter · daughter_of_predeceased_daughter_of_predeceased_son |
| DD-FAM-81 | HSA Class II entries | I father · II son's daughter's son, son's daughter's daughter, brother, sister · III daughter's son's son, daughter's son's daughter, daughter's daughter's son, daughter's daughter's daughter · IV brother's son, sister's son, brother's daughter, sister's daughter · V father's father, father's mother · VI father's widow, brother's widow · VII father's brother, father's sister · VIII mother's father, mother's mother · IX mother's brother, mother's sister |

---

## 7. Modus operandi per subtype

Temporal workflows (P04/P08): `FamMaritalWorkflow`, `FamKhulaWorkflow`, `FamPropertyWorkflow` (incl. existing `FamPropertyExecutionWorkflow`), `FamElderWorkflow`, `FamMwpscConciliationWorkflow`, `FamUrgentSignpostWorkflow`. Sessions default 2 hours online. Every step writes audit and, where stated, an event `equator.fam.<entity>.<verb>.v1`.

### 7.1 Mutual-consent divorce terms (`hma_13b`, `sma_28`, `divorce_act_10a`, `pmda_32b`, `ucc_uk_27`, `mubarat`)
| # | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | filer | Explorer → F-FAM-02 + CB-REG; fee quote (FAM-STD M1) | `draft_expiry` 30 d | marriage proof, separation proof | — | resolver confidence |
| 2 | system | Suitability `fam.suitability.v2`; screening F-FAM-26 scheduled for filer | `sla_scrutiny` 2 WD | — | — | A / AC / SP |
| 3 | case_manager | Invitation (neutral wording, verify-notice link) | `response_window` 14 d (+7) | TPL-FAM-N01 | D0/D3/D7/D10 cadence (§8) | respondent reply |
| 4 | respondent | F-FAM-04 + own F-FAM-26 | — | — | — | screening outcome |
| 5 | allocation | Mediator per App. N (DV-endorsed if flagged; language; specialisation) | `sla_neutral_appointment` 7 d | F-FAM-06 disclosure | — | challenge 3 WD |
| 6 | mediator | Orientation + interim arrangements F-FAM-08 | `sla_first_session` 14 d | — | — | — |
| 7 | mediator | Joint/caucus/shuttle sessions; affidavits F-FAM-07 if money heads | `med_contract_timebox` 120 d (+60) | F-FAM-07 ×2 | T-48h/T-2h reminders | settled / partial / not |
| 8 | parties | MSA built (TPL-FAM-S01) with regime recitals; PT-FAM-01..08 lint | — | ILA F-FAM-27 | — | lint pass |
| 9 | parties | Reflection window | `fam_msa_reflection` 7 d | — | — | withdraw / confirm |
| 10 | parties | E-sign + e-stamp (state of execution) | NN-09 | stamp cert | — | — |
| 11 | parties/counsel | Court pack TPL-FAM-P01 (first motion; waiver application from one week after first motion); escrow tranche 1 on first-motion proof | `fam_s13b_cooling` 6 m; `fam_s13b_outer_18m` | petition, affidavits, MSA annexure | — | — |
| 12 | parties | Second motion; decree uploaded; tranche 2/final on decree + handover | — | decree | — | UCC: `fam_ucc_divorce_reg_60d` |
| 13 | case_manager | Compliance tracker (maintenance, contact log); closure with signposting record | Appendix A §5 | — | — | `closed` |

### 7.2 Khula (`khula`)
| # | Actor | Action | SLA | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | wife | Explorer M-05 → F-FAM-02 + F-FAM-39 | — | nikahnama, demand proof | no husband-consent field |
| 2 | system | Screening; invitation to husband framed as "terms of khula" (not consent) | 14 d | TPL-FAM-N01 variant K | husband declines → wife may still proceed to Family Court pack |
| 3 | mediator | Sessions on mahr return/forgoing, iddat maintenance, custody, streedhan | 120 d | F-FAM-17 | — |
| 4 | parties | Khula settlement record TPL-FAM-S05 (e-sign; stamp as agreement) | NN-09 | — | — |
| 5 | wife/counsel | Family Court declaration pack TPL-FAM-P04 (summary-inquiry facts: reconciliation attempts, mahr offer) | — | — | court decides |

### 7.3 Maintenance and parenting (`fam.maintenance`, `fam.custody_parenting`) — run inside 7.1 or standalone
| # | Actor | Action | SLA | Decision point |
|---|---|---|---|---|
| 1 | both | F-FAM-07 affidavits (variant by income profile); D05/CB-PEND set-off | estimator locked until both filed (LR-FAM-005) | — |
| 2 | mediator | Shows estimator output as a neutral reference only (FAM-G-02/04) | — | parties' own figures |
| 3 | mediator | Parenting plan builder F-FAM-17 (multi-faith festival scheduler, passport/travel clause, milestone reviews at ages 5, 9, 12, 16) | — | child-inclusive? F-FAM-29 |
| 4 | specialist | Voice-of-the-child note F-FAM-21 (sealed) | — | not determinative |
| 5 | parties | Terms: amount, frequency, due day, mode (UPI AutoPay ≤ ₹15,000 AFA-free / NACH / escrow), escalation, extras, arrears, security, review trigger; "subject to court approval" for child terms | — | PT-FAM-01/02/05 |
| 6 | counsel | Consent terms in pending case (TPL-FAM-P08) or Lok Adalat pack (TPL-FAM-P07) | — | court records |
| 7 | system | Compliance tracker; breach → `fam_breach_cure` 7 d → return to mediation | — | — |

### 7.4 Intestate succession, partition, co-owner, family business (`fam.intestate_succession`, `fam.partition_coparcenary`, `fam.co_owner_property`, `fam.family_business_separation`)
| # | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| 1 | filer | F-FAM-32 + F-FAM-30 tree + F-FAM-31 inventory; CB-REG per deceased | — | DOC-FAM-P list | tree validation |
| 2 | system | Resolver per deceased; calculator scope gate; urgency U-FAM-05 | — | — | out_of_scope → counsel |
| 3 | case_manager | Invitations to every heir (TPL-FAM-N02 heirs' invitation; NRI channels) | 14 d (+7) | — | unwilling/untraceable → FAM-SR-22 |
| 4 | mediator(s) | Family meeting (rung 1, assisted negotiation, multi-party; co-mediation option) | 21 d | — | → mediation |
| 5 | mediator | Mediation (multi-party; shuttle available); calculator run with lawyer-review banner; valuation by agreed valuer | 90 d (+60) | valuation report | allotment agreed |
| 6 | parties | Terms sheet F-FAM-33; owelty balancer; instrument choice (memorandum vs operative deed — FR-V3-16); s.315 warning (HUF); NRI checks; minors' court-permission task | — | — | `requires_registration` |
| 7 | arbitration (optional) | Only property heads, all heirs' post-dispute agreement, flag ON; tribunal by Equator | s.29A | F-FAM-37/24/25 | award stamped as partition instrument |
| 8 | parties | Physical execution, stamp, SRO appointment (§13.3) | `registration_4m` (+4 m fine) | executed deed | — |
| 9 | parties | Registration evidence; mutation, society transmission, bank/demat transmission tasks | `mutation_due` (state config) | registration no. | — |
| 10 | case_manager | Possession/handover milestones; escrow releases; closure blocked until registration evidence | — | — | `closed` |
Family business: corporate heads (share transfer, board changes, oppression relief) cross-routed to COM with linked matter; guarantees need lender NOC (FIN cross-link).

### 7.5 Family settlement, will distribution, wasiyat (`fam.family_settlement`, `fam.will_interpretation`)
Same as 7.4 with: step 6 adds (a) `memorandum_recording` requires oral-settlement date, place, participants, acting-upon evidence (mutation, possession, separate tax payments); if absent, recommend `operative_deed`; lawyer review if document date ≤ 30 days after claimed oral settlement; (b) will matters: if probate/LoA is pending, settlement terms include withdrawal of caveat/opposition with the court recording the compromise; (c) Muslim wills → F-FAM-40 consents before distribution.

### 7.6 Succession/legal-heir certificate assistance (`fam.succession_documents`)
1 heir files F-FAM-43 → 2 tree + debts/securities schedule → 3 optional heirship agreement mediation (who are the heirs; who applies; indemnity/security arrangements) → 4 Equator generates facts schedule and annexure index → 5 counsel/heir files before District Judge (s.372) or applies to Tahsildar/SDM; Equator tracks CNR via eCourts deep link → 6 post-grant transmission checklist (bank, RTA, society). Equator never files, never represents (D2-11; Advocates Act).

### 7.7 Elder (`fam.elder_maintenance`)
| # | Actor | Action | SLA / clock | Decision point |
|---|---|---|---|---|
| 1 | senior or authorised person/organisation | F-FAM-34; eligibility (senior: 60+, citizen; parent: any age — FAM-SR-26); Tribunal always shown | — | private vs Tribunal |
| 2 | system | Abuse screen U-FAM-06 | immediate | SP if abuse active |
| 3 | mediator (elder-care specialisation) | Family mediation; children/relatives invited; senior may attend with support person | 90 d | — |
| 4 | parties | Care-arrangement agreement TPL-FAM-S04 (allowance, medical, residence/no-eviction, caregivers, visits, property clause; review every 12 months) | — | reconveyance → NN-08 |
| 5 | Tribunal-referred mode | F-FAM-42; conciliation sessions without advocates; report TPL-FAM-R03 to Tribunal (status + agreed terms) | `fam_mwpsc_conciliation_1m` | Tribunal passes order |

### 7.8 Criminal-closure civil terms (`fam.criminal_closure`)
Classification per pending case (deterministic table by BNS section) → mediation of civil heads only → F-FAM-12 joint memo (route: BNSS s.359 compounding / s.528 quashing / withdrawal where lawful) with caveat "The court alone decides; no assurance is given" → escrow tranche released only on a **court order disposing of proceedings** and only when no party carries a safety flag (PT-FAM-04 override by `safeguarding_lead`; LR-FAM-010) → safeguarding review of the instrument (P06 FR-P06-13).

---

## 8. Pre-litigation journey (FAM)

FAM uses the Appendix K §5.2 pre-litigation machine (source S4 §B5 `prelit_case`) with these FAM settings (config `fam.prelit.*`):

| Stage | FAM rule |
|---|---|
| SUITABILITY_CHECK | §4 rule pack; screening of filer before invitation; no invitation where U-FAM-01/02 active |
| NOTICE_READY | Notice from "Equator Resolution Service Private Limited — Case Administrator"; invitation wording ("we invite you to talk"), never threat language; no dispute type in SMS/WhatsApp body (FAM-G-07); limitation disclaimer |
| INVITATION_SENT | D0 email + WhatsApp utility template + SMS; post only to the respondent's own address (never to a shared household where the filer is safety-flagged); D3, D7 (case-manager call 08:00–19:00), D10 final, D14 close as NON_COMMENCEMENT; ≤ 6 contacts; second, differently framed outreach at D7 (C3 §3.3) |
| RESPONDED | ACCEPT_WITH_CONDITIONS supports DD-FAM-43; DECLINE reasons sealed |
| CONSENTED | Agreement to Mediate (FAM Rules) or s.62(2) acceptance (conciliation for money/property heads); Aadhaar eSign; sub-consents CB-CONS |
| PRE_MEDIATION | separate intake calls; respondent screening F-FAM-26 mandatory |
| IN_SESSION | joint/caucus/shuttle; child-inclusive per F-FAM-29; SUSPENDED on safety, incapacity or urgent proceedings |
| OUTPUT_CONVERSION | ranked by strength: (1) s.73/s.74 conciliation settlement for money/property heads; (2) court consent terms / s.13B pack / khula declaration pack / CPC O.XXIII r.3 compromise; (3) Lok Adalat recording pack (LSA s.20(2)) for maintenance and money heads; (4) MWPSC Tribunal order on conciliation report; (5) registered deed for immovable property (NN-08); (6) contractual MSA. Consent award (s.30) only for property heads with an arbitration agreement and a different arbitrator |
| COMPLIANCE_TRACKING | escrow tranches, maintenance instalments, contact log, registration/mutation tasks; CLOSED_PERFORMED / CLOSED_BREACHED → enforcement pack (§13.4) |

FAM pre-litigation KPI targets: engagement ≥ 40% (individual v individual), consent ≥ 35%, first-session attendance ≥ 85%, time to consent ≤ 7 days median, "felt unsafe" = 0.

---

## 9. Document checklists per subtype

Formats: PDF, JPG/PNG, HEIC (converted), DOCX; ≤ 25 MB each; OCR + type copy per App. L (originals preserved, NN-32). Verification: **DL** DigiLocker pull · **QR** CRS/registration QR check · **OCR** extract + human confirm · **SD** self-declared · **NT** notarised/attested copy required for court pack.

| Code | Document | Subtypes | M/O | Verification |
|---|---|---|---|---|
| DOC-FAM-01 | Marriage certificate / nikahnama (with mahr clause) / church or Parsi certificate / UCC certificate; else invitation card + photos | marital | M (one) | QR/DL where issued; OCR |
| DOC-FAM-02 | Proof of separate residence (rent agreement, utility bills) | divorce_* | M | OCR |
| DOC-FAM-03 | ID and address of each party (masked Aadhaar via OVSE, PAN, passport) | all | M | DL / offline e-KYC (D2-06) |
| DOC-FAM-04 | Income proof: ITRs 3 yrs, salary slips 6 m, Form 16; business: GST returns, P&L; farm: RoR + crop income | maintenance | M | OCR |
| DOC-FAM-05 | F-FAM-07 affidavit (both parties) | maintenance | M | NT option |
| DOC-FAM-06 | Children's birth certificates, school and medical records | custody, child maintenance | M | QR (CRS) |
| DOC-FAM-07 | Streedhan inventory with photos/receipts | matrimonial_property | O | SD |
| DOC-FAM-08 | Pending pleadings, FIRs, orders | any with CB-PEND rows | M | OCR; CNR link |
| DOC-FAM-09 | Passport/visa/OCI card | NRI, passport_travel | M | OCR |
| DOC-FAM-10 | Khula written demand; proof of reconciliation attempts; mahr offer | khula | M | SD |
| DOC-FAM-11 | Death certificate(s) | succession | M | QR (CRS, RBD Act 1969 as amended 2023) |
| DOC-FAM-12 | Family-tree affidavit | succession | M | NT |
| DOC-FAM-13 | Legal heir / succession certificate / probate / LoA (if any) | succession | O | OCR; eCourts CNR |
| DOC-FAM-14 | Will (original/copy), codicils | will matters | M | OCR; original sighted for court |
| DOC-FAM-15 | Title chain (30 years recommended), encumbrance certificate, RoR/khatauni/7-12/jamabandi, mutation orders | immovable | M | OCR; land-records deep link |
| DOC-FAM-16 | Property tax receipts; society share certificate, NOC, nomination record | immovable | O | OCR |
| DOC-FAM-17 | Bank/demat statements, nominations | movables | O | OCR |
| DOC-FAM-18 | HUF deed, HUF PAN, HUF ITRs | HUF | M (HUF) | OCR |
| DOC-FAM-19 | Earlier partition/settlement deeds or memoranda; decrees | partition | M if exists | OCR |
| DOC-FAM-20 | Valuation report (registered valuer) or party-agreed values | property | O | — |
| DOC-FAM-21 | Minors' guardianship orders; court-permission order (HMGA s.8(2)) | minors | M before execution | OCR |
| DOC-FAM-22 | Goa inventory record / deed of qualification of heirs | Goa | M (Goa) | OCR |
| DOC-FAM-23 | UCC succession/marriage registration | UK UCC | M (flag) | portal ref |
| DOC-FAM-24 | Gift/transfer deed with care condition | elder s.23 | M | OCR |
| DOC-FAM-25 | Senior's age and citizenship proof | elder | M | DL |
| DOC-FAM-26 | Tribunal referral order | F-FAM-42 | M | OCR |
| DOC-FAM-27 | Apostille/consular certificate; foreign address proof | NRI execution | M | OCR |
| DOC-FAM-28 | ST certificate (if claimed) | customary_st | O | DL where issued |
| DOC-FAM-29 | Partnership deed / MoA-AoA / share register / loan & guarantee documents | family business | M | MCA lookup (KYB) |

---

## 10. Practical difficulties and product solutions
| Difficulty | Product solution |
|---|---|
| Users refuse or misstate religion; regime is sensitive | D2-03 resolver from marriage form and family-law questions; `prefer_not_to_say` → counsel; religion field encrypted, never shown to the other side |
| Spouse abroad cannot attend second motion | NRI pack: video-appearance note, SPA template for limited purposes, apostille/consular checklist |
| 18-month s.13B window lapsing | `fam_s13b_outer_18m` hard alert + lawyer task at T-60 |
| Consent withdrawn before second motion (*Sureshta Devi*) | staged escrow: tranche 1 on first motion, final on decree |
| Husband refuses khula | no consent field; Family Court declaration pack |
| Payer conceals income | court route recommended (disclosure orders; *Rajnesh* adverse inference); mediation cannot compel |
| Abuser uses mediation to locate or pressure victim | sealed screening per session; shuttle; no contact data shared; quick exit; no pressure conditions |
| Untraceable or unwilling heir | "share reserved" clause with escrow/trust of untraced share; presumption of death after 7 years (BSA 2023 s.111) explained; court route |
| Minor heirs | court-permission task; minor's share ring-fenced; no relinquishment |
| Title defects, deceased's name in RoR | title-gap report; mutation task per state; defer sale |
| Agricultural land: revenue court, fragmentation, tenancy | state rule pack flags; counsel review; revenue-court signpost |
| NRI heir and agricultural land | LR-SUCC-016 block on gift; allotment → counsel |
| Society refuses transfer without probate | copy explains s.213 omission; suggests indemnity + NOC route; probate still available |
| Family memo drafted to look like past settlement | 30-day rule forces lawyer review |
| HUF partial partition tax trap | s.315 warning and checklist |
| Elder fears retaliation | support person, separate sessions, Elderline 14567, Tribunal option |
| Low digital literacy | assisted/kiosk mode, WhatsApp-first, voice explainer (logistics only inside mediation — X-05) |

---

## 11. Integrations and APIs
| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| DigiLocker (via licensed partner) | Pull ID, death/caste/ST certificates where issued | issued documents | user consent (DPDP s.6); D2-06 | API (`KYC_PORT`) | upload + OCR |
| UIDAI offline verification (OVSE) | Aadhaar QR/XML/Aadhaar App verification | masked ref | Aadhaar Act s.8A; Aadhaar (Authentication and Offline Verification) Regulations 2021 (as amended 9 Dec 2025); OVSE registration — no online e-KYC unless approved under G.S.R. 88(E), 31 Jan 2025 (D2-06) | SDK | PAN/passport |
| CRS (Civil Registration System) | Verify birth/death certificates | certificate QR | public verification | QR scan | manual |
| State land records (Bhulekh, Mahabhumi, Bhoomi, Bhu Bharati etc.); ULPIN | RoR lookup by survey no. | RoR extract | public records; user-supplied identifiers | deep link / manual upload (no scraping) | upload + OCR |
| NGDRS / state IGR portals (MH IGR, KA Kaveri, TG/AP IGRS, DL DORIS, UP IGRSUP) | stamp computation, SRO appointment | deed data | user action | deep link + checklist | manual booking |
| SHCIL e-stamp / state GRAS; Leegality BharatStamp | stamp payment | instrument, duty | NN-09 | `ESTAMP_PORT` | physical stamp paper (`ESTAMP_STATE_UNSUPPORTED`) |
| eCourts Services (CNR) | track pending suits/maintenance/probate | case status | public data; user-entered CNR | deep link | manual next date |
| CERSAI | security-interest search on property | search result | user-initiated | manual upload | — |
| e-District portals | legal heir certificate tracking | application no. | user | deep link | manual |
| UCC Uttarakhand portal | registrations | ref no. | flag `fam.ucc_uk` | deep link | — |
| DLSA / Maintenance Tribunal / Family Court | referrals in/out, reports | R01/R03 reports (status + agreed terms only) | MoU / court order | P09 referral API, PDF+email export | manual |
| Razorpay UPI AutoPay / NACH; RazorpayX Escrow+/Castler | maintenance instalments; escrow tranches | mandate, escrow milestones | RBI e-mandate (₹15,000 AFA-free); NN-13 | `PAYMENTS_PORT`, `ESCROW_PORT` | direct payment with proof |
| Finbyx / FIN linked matters | joint home-loan or guarantor issues | linked-matter ref | party consent | internal event | manual |
| Helplines directory (112, 181, 1098, 14567, 14416, One Stop Centres, Protection Officers) | safety signposting | directory rows | public | `routing_forums` (re-verify 180 d) | static page |

---

## 12. Calculators (indicative only; never advice)

Framework FR-P08-08. Every output: `indicative: true`, `requires_lawyer_review: true`, watermark "Indicative — not legal advice", `computation_trace[]`, mandatory copy (S1 §12.3): "These figures are indicative only, based on the rules you selected and the facts you entered. Your personal law, custom, the type of property, earlier deaths, wills, gifts, debts and court decisions can change the result. This is not legal advice. A lawyer must confirm the shares before any document is signed." AI may display results, never recommend (FAM-G-02/04). Money in paise; rounding half-up at presentation; residual paisa to the first heir in `death_order`/age order (trace notes it).

| ID | Scope | Flag (default) |
|---|---|---|
| `fam.maintenance_estimate@1` | as FR-P08-40.1 | ON (locked until both F-FAM-07) |
| `fam.hsa_shares@2` | @1 + Class II engine, s.6 date gate, s.15(1)(a) incl. predeceased child branches, s.15(2) source routing (→ counsel) | `fam_succession_calculator` ON |
| `fam.muslim_hanafi@1` | sharers, residuaries, 'aul, radd; no representation | `fam_succession_muslim` OFF |
| `fam.muslim_shia@1` | Class I only; per stirpes; childless-widow land exclusion | `fam_succession_muslim` OFF |
| `fam.isa_ch2@1` | ss.32–49 core cases (s.33A excluded → counsel) | `fam_succession_isa` OFF until sign-off |
| `fam.isa_parsi@1` | ss.51–53 | `fam_succession_isa` OFF until sign-off |
| `fam.ucc_uk@1` | s.51 Class I | `fam.ucc_uk` OFF |
| `fam.wasiyat_check@1` | 1/3 check + consent forms | `fam_succession_muslim` OFF |
| `fam.partition_balance@1` | owelty | ON |
| `fam.mwpsc_cap@1` | Tribunal cap per state (≤ ₹10,000) | ON |
| `fam.partition_stamp_base@1` | stamp base per state article (e.g. Art. 45 formula: total minus largest share); rate from `core.stamp_duty_rules` | ON (rates VERIFY per LR-STAMP-007 → "figure under legal verification") |
| `fam.s13b_dates@1` | petition-ready date; earliest second motion; waiver-application date; outer limit | ON |
| `fam.registration_dates@1` | presentation deadline; fine window | ON |
| Goa, ST customary, Ismaili/Bohra, Muslim distant kindred, pre-9 Sep 2005 HSA deaths, multi-death chains | `out_of_scope_*` with referral | — |

### 12.1 Golden vectors (unit tests `packages/rules/calculators/fam/__tests__`)
| ID | Calculator | Inputs | Expected |
|---|---|---|---|
| GV-MAINT-1 | maintenance | N ₹1,50,000; Y ₹20,000; k 1; Cn ₹25,000; Pn ₹45,000; L ₹20,000; o 35%; g 25%; c 15% | Capacity ₹77,500; Low ₹25,000; High ₹37,500; Mid ₹31,250; Child ₹22,500 (cap mode) → Total ₹53,750; `needs_only` → Child ₹25,000, Total ₹56,250 |
| GV-HSA-A | hsa | Ramesh d. 10 Mar 2024; coparcenary ₹1,20,00,000; separate ₹60,00,000; widow, son, daughter, mother; wife switch OFF | Son ₹65,00,000; Daughter ₹65,00,000; Widow ₹25,00,000; Mother ₹25,00,000 (Σ ₹1,80,00,000) |
| GV-HSA-A2 | hsa | same; switch ON | Son, Daughter, Widow ₹52,50,000 each; Mother ₹22,50,000 |
| GV-HSA-B | hsa | separate ₹60,00,000; widow, son, predeceased son's widow + daughter | Widow ₹20,00,000; son ₹20,00,000; branch ₹10,00,000 + ₹10,00,000 |
| GV-HSA-C2a | hsa Class II | male d. 2025; no Class I; father + brother; ₹50,00,000 | Father ₹50,00,000 (entry I excludes II) |
| GV-HSA-C2b | hsa Class II | no Class I, no father; brother + sister; ₹50,00,000 | ₹25,00,000 each (entry II equal) |
| GV-HSA-F1 | hsa s.15(1)(a) | female d. 2025; separate ₹60,00,000 not from parents/husband; husband, daughter, predeceased son's 2 children | Husband ₹20,00,000; daughter ₹20,00,000; each grandchild ₹10,00,000 |
| GV-HSA-G | hsa gate | death 1 Jan 2004 | `out_of_scope_pre_2005` + counsel |
| GV-H1 | hanafi | male; widow, son, daughter, mother; net ₹72,00,000 | Widow ₹9,00,000; mother ₹12,00,000; son ₹34,00,000; daughter ₹17,00,000 |
| GV-H2 | hanafi 'aul | female; husband, 2 daughters, father; ₹65,00,000 | Husband ₹15,00,000; daughters ₹20,00,000 each; father ₹10,00,000 (13/12 → /13) |
| GV-H3 | hanafi | male; son + son of predeceased son; ₹50,00,000 | Son ₹50,00,000; grandson nil; UI contrast note with HSA |
| GV-H4 | hanafi radd | female; mother + 1 daughter; ₹40,00,000 | Mother ₹10,00,000; daughter ₹30,00,000 (1/6 : 1/2 scaled by radd) |
| GV-S1 | shia | male; childless widow, father, mother; movables ₹48,00,000 | Widow ₹12,00,000; mother ₹16,00,000; father ₹20,00,000 |
| GV-S2 | shia per stirpes | no child surviving; son's daughter + daughter's son; ₹30,00,000 | Son's daughter ₹20,00,000; daughter's son ₹10,00,000 |
| GV-S3 | shia land | childless widow + father; estate includes agricultural land | widow's share computed on movables + value of buildings/trees only; land → `counsel_review` |
| GV-C1 | isa_ch2 | widow + 2 children; ₹90,00,000 | ₹30,00,000 each |
| GV-C2 | isa_ch2 | widow + father; ₹60,00,000 | ₹30,00,000 each |
| GV-C3 | isa_ch2 | widow + mother + brother (father predeceased); ₹60,00,000 | Widow ₹30,00,000; mother ₹15,00,000; brother ₹15,00,000 |
| GV-P1 | parsi | widow, son, daughter, father, mother; ₹80,00,000 | ₹20,00,000 ×3; parents ₹10,00,000 each |
| GV-U1 | ucc_uk | death after 27 Jan 2025; spouse, son, daughter, father, mother; ₹80,00,000 | Spouse/son/daughter ₹20,00,000 each; father/mother ₹10,00,000 each |
| GV-W1 | wasiyat | net ₹90,00,000; bequest ₹40,00,000 to non-heir (Hanafi) | flag excess ₹10,00,000 "valid only with heirs' consent after death"; consent forms generated per heir |
| GV-O1 | owelty | 2 heirs × 1/2; house ₹80,00,000 → X; plot ₹50,00,000 → Y | entitlement ₹65,00,000 each; X pays Y ₹15,00,000 |
| GV-ST1 | stamp base (Art. 45 pattern) | shares ₹65,00,000 / ₹65,00,000 | base ₹65,00,000 × state rate (config) |
| GV-MW1 | mwpsc cap | estimate ₹14,000; state cap ₹10,000 | Tribunal-order estimate ₹10,000 (private agreement unaffected) |
| GV-D1 | s13b dates | separated 1 Jan 2026; first motion presented 10 Jan 2027 | eligible (≥ 1 yr); waiver application from 17 Jan 2027; earliest second motion 10 Jul 2027; outer limit 10 Jul 2028 |
| GV-R1 | registration | executed 15 Mar 2027 | present by 15 Jul 2027; with fine by 15 Nov 2027 |
| GV-MC1 | MWPSC disposal clock | notice served 1 Feb 2027 | 90 d → 2 May 2027; +30 → 1 Jun 2027 |

---

## 13. Outputs, templates, enforcement and registration route

### 13.1 Template catalogue (EN + HI; `packages/templates/fam`)
Existing (FR-P08-41): N01, L01–L05, S01 (35-clause bank), S02, S03 (+ memorandum and operative deed shells), S04, P01 (s.13B with *Amardeep* waiver), P02 (s.528 BNSS shell), P03 (s.359 BNSS), R01, R02. **New:**
| ID | Template | Allowed label (copy-lint) |
|---|---|---|
| TPL-FAM-N02 | Heirs' invitation (multi-party, NRI-ready) | "Invitation to family mediation" |
| TPL-FAM-L06 | Triple-talaq lawful-routes letter | "Information letter — lawful options" |
| TPL-FAM-S05 | Khula settlement record | "Record of terms of khula agreed in mediation" (never "khulanama issued by Equator") |
| TPL-FAM-S06 | Wasiyat heirs' consent | "Consent of heirs to bequest" |
| TPL-FAM-S07 | Release/relinquishment deed shell (physical execution) | "Draft for execution and registration" |
| TPL-FAM-S08 | HUF partition pack + ITA 2025 s.315 checklist | — |
| TPL-FAM-S09 | NRI SPA / consent affidavit shells with apostille instructions | — |
| TPL-FAM-S10 | Settlement in lieu of will contest (withdrawal of caveat/opposition) | "Subject to the probate court's satisfaction" |
| TPL-FAM-P04 | Family Court khula declaration petition pack | — |
| TPL-FAM-P05 | MWPSC s.5 application pack | — |
| TPL-FAM-P06 | Succession-certificate facts schedule (s.372) | "Prepared for filing by the applicant or counsel" |
| TPL-FAM-P07 | Lok Adalat joint application (LSA s.20(2)) | — |
| TPL-FAM-P08 | Consent terms (CPC O.XXIII r.3 / maintenance / GWA) | "Subject to court approval" (child terms) |
| TPL-FAM-R03 | MWPSC conciliation report to Tribunal | status + agreed terms only |
| TPL-FAM-R04 | Non-commencement notice | "Equator Non-Commencement Notice" |
Copy-lint additions (FR-V3-27): block "Equator decree", "Equator divorce", "divorce granted", "khulanama by Equator", "legally valid triple talaq", "probate mandatory", "mutation gives ownership", "nominee is the owner", "registered MSA", "s.27 decree", "court-annexed", "Lok Adalat by Equator", "binding decree" (NN-17), "guaranteed share".

### 13.2 Instrument routing (P06 FR-P06-16)
| Output | Sign | Stamp | Register | Effect |
|---|---|---|---|---|
| Divorce/khula/maintenance/parenting MSA | Aadhaar eSign | agreement article (state of execution) | no | contract; effective through court decree/order where status/child terms |
| s.73 conciliation settlement (money/property heads) | eSign + conciliator authentication | per state | if it creates rights in immovable property ≥ ₹100 → yes (*Lachhman Dass*) | s.74 award status |
| Consent terms in pending case | wet/e-sign per court | per court/state | exempt for suit property (s.17(2)(vi)) | compromise decree |
| Memorandum of past family arrangement | eSign permitted | state rule (VERIFY) | no (*Kale*) | evidence of prior settlement |
| Partition / family settlement / release / gift deed | **physical** (NN-08; `ESIGN_EXCLUDED_INSTRUMENT`) | partition/settlement/release/gift article | yes (s.17(1)(b)) within 4 months | operative transfer |
| Property arbitral award | DSC by tribunal | partition article (MH Art. 12 excludes partition awards) | yes | award |
| Care arrangement with reconveyance | physical for reconveyance | conveyance | yes | — |

### 13.3 Registration route (Sub-Registrar; NN-08)
1. Confirm execution state and property state(s); SRO = where property is situate (s.28). 2. Compute stamp base and duty from `core.stamp_duty_rules` (LR-STAMP-007 VERIFY label). 3. Pay e-stamp (SHCIL/GRAS) or physical paper. 4. Book SRO slot (state portal deep link); upload draft where portal requires. 5. All executants or SPA holders attend with ID, photos, two witnesses; biometric capture (s.32A); PAN or Form 60 where required. 6. Present within 4 months (s.23); fine window +4 months (s.25). 7. Upload registration evidence → `equator.fam.registration.completed.v1`. 8. Follow-ups: mutation (state `mutation_due`), society transmission, bank/demat transmission, ITA filings (HUF). `core.registration_tasks.checklist` stores steps 1–8 with evidence refs; ANC.REGN.FACIL fee ₹5,000 per instrument + statutory fees at actuals (Appendix B).

### 13.4 Enforcement
| Instrument | Route |
|---|---|
| Consent decree / s.13B decree / maintenance order | execution before the court that passed it (CPC O.XXI; BNSS s.147 for maintenance) |
| s.74 settlement / property award | A&C s.36 + CPC O.XXI r.11(2); file where assets are (*Sundaram Finance v Abdul Samad* (2018) 3 SCC 622); execution within 6 months direction (*Rahul S. Shah* (2021) 6 SCC 418; *Periyammal v V. Rajamani*, 2025 INSC 329) |
| Lok Adalat award | deemed civil-court decree (LSA s.21) |
| MWPSC order | as BNSS maintenance order (s.11) |
| Contractual MSA | suit on contract / summary suit; return-to-mediation clause first |
Execution pack generator (App. R §4) pre-fills O.XXI r.11(2) items; Equator never appears in court.

### 13.5 Publication (NN-26; App. R §3)
FAM: P0 none by default; P1 aggregate statistics (k ≥ 10) allowed; P2 digest only with all parties' consent given after the outcome, neutral approval and FAM redaction profile, and only once `publication.consensual.enabled` (OFF until counsel Q-R3) is ON (names, places, community/religion, caste, children, health, employer removed); **P3 redacted award and P4 full award disabled** for all FAM matters; enforcement disclosure E logged.

---

## 14. Dashboards, KPIs and enterprise hooks
| KPI | Definition | Target |
|---|---|---|
| Time to first session | filed → first session | ≤ 21 d |
| Cycle to MSA (marital) | first session → MSA signed | ≤ 120 d median |
| Settlement full/partial (commenced) | settled / ≥ 1 substantive session | ≥ 55% |
| Respondent participation | consented / delivered | ≥ 60% |
| Screening coverage before joint session | screened / joint sessions | 100% |
| Urgent trigger to signpost | trigger → signposting event | ≤ 5 min |
| Regime resolved at high confidence | high / FAM cases | ≥ 95% |
| Calculator counsel-review before signing | reviewed / instruments using calculator | 100% |
| Parenting plan in child matters | plans / child matters | ≥ 90% |
| Registration within 4 months | registered / `requires_registration` instruments | ≥ 90% (100% tracked) |
| Durability at 12 months | no breach notice / settlements | ≥ 80% |
| Compliance (maintenance/escrow on schedule) | paid on time / due | ≥ 90% |
| "Felt unsafe" responses | count | 0 |
| CSAT (each side) / gap | survey | ≥ 4.3; gap ≤ 0.4 |
Widgets: screening coverage (counts only), urgent-trigger log (counts), registration-task ageing, compliance tracker, court/Tribunal referral pipeline, heirs-joined funnel. All views exclude `safety_sealed` (NN-07) and never show outcomes by gender/religion/community.

Enterprise/B2G hooks (P09): `equator.fam.court_referral.received.v1`, `equator.fam.court_report.issued.v1`, `equator.fam.tribunal_referral.received.v1` (**new**), `equator.fam.tribunal_report.issued.v1` (**new**), `equator.fam.registration_task.due.v1`, `equator.fam.registration.completed.v1`, `equator.fam.urgent_signposted.v1` (**new**; no sealed content), DLSA legal-aid export.

---

## 15. Competitor notes and Equator differentiation
| Competitor | FAM offer (published) | Gap Equator closes |
|---|---|---|
| Sama | Family & matrimonial and property mediation; session ₹10,000–₹1,00,000 (no defined claim); execution packet ₹500 [V R1/S3] | Community-aware regime resolver, per-community share calculators, registration route, sealed safety screening |
| Presolv360 | "Property" and civil disputes; mediation ₹4,500 + ₹5,000/session [V S3] | Family tree + heirs-joined gate; HUF/s.315 pack; elder Tribunal conciliation |
| Jupitice / CADRE / Webnyay / CORD | No structured family-property pathway located [U S3] | Pre-litigation family track with s.13B/khula/consent-terms packs; DV policy mirroring PWDV r.14 |
| Court-annexed centres, DLSA, Family Court counsellors | Free; court-linked | Equator shows them first (NN-20) and differentiates on speed, online multi-party heirs' mediation, NRI execution and registration support |
Equator claims are limited by NN-17; no "court", "decree" or outcome-guarantee language.

---

## 16. Data-model extensions (forward migration `fam_v2_0001`; extends Appendix F §F.8)

### 16.1 Alter existing
```sql
ALTER TABLE fam.family_members
  ADD COLUMN relation_code text,                          -- DD-FAM-80/81, derived by graph engine
  ADD COLUMN branch_parent_id uuid REFERENCES fam.family_members(id),
  ADD COLUMN alive boolean NOT NULL DEFAULT true, ADD COLUMN died_on date, ADD COLUMN death_order smallint,
  ADD COLUMN capacity_concern boolean NOT NULL DEFAULT false, ADD COLUMN consent_status text NOT NULL DEFAULT 'pending'
    CHECK (consent_status IN ('pending','joined','released','refused','untraceable')),
  ADD COLUMN abroad_country char(2), ADD COLUMN is_nri_oci text CHECK (is_nri_oci IN ('resident','nri','oci','foreign_listed','foreign_other')),
  ADD CONSTRAINT no_self_branch CHECK (branch_parent_id IS DISTINCT FROM id);
ALTER TABLE fam.estate_assets
  ADD COLUMN nature text CHECK (nature IN ('self_acquired','ancestral_coparcenary','huf_declared','jointly_owned','stridhan','goa_communion','tribal_land','wakf_or_trust','government_lease')),
  ADD COLUMN acquired_from text CHECK (acquired_from IN ('father','mother','husband','father_in_law','self','other')),
  ADD COLUMN who_paid_member_id uuid, ADD COLUMN ulpin char(14), ADD COLUMN ror_ref_enc bytea, ADD COLUMN encumbrance_enc bytea,
  ADD COLUMN possession_member_id uuid, ADD COLUMN is_agricultural boolean GENERATED ALWAYS AS (asset_kind = 'immovable_agricultural') STORED;
-- Service guard (FAM-SR-24): an asset with nature 'wakf_or_trust' cannot be referenced by fam.partition_terms (trigger fam.guard_out_of_scope_asset → MECHANISM_NOT_PERMITTED_FOR_VERTICAL).
ALTER TABLE safety_sealed.screenings DROP CONSTRAINT screenings_outcome_check,
  ADD CONSTRAINT screenings_outcome_check CHECK (outcome IN ('suitable','suitable_with_safeguards','shuttle_only','not_suitable_safety','not_suitable_capacity'));
```

### 16.2 New tables
| Table | Key columns | Constraints / notes |
|---|---|---|
| `fam.case_ext` (P08; add columns) | `marriage_regime`, `succession_regime` (enum §16.3), `regime_confidence`, `counsel_review_required`, `dv_settlement_requested` (mirrored bool from sealed), `child_terms` bool, `court_referral_ref`, `tribunal_referral_ref` | trigger `fam.session_guard` (P08) retained |
| `fam.regime_resolutions` | id, case_id, subject_member_id, inputs_enc bytea, family_law_enc bytea, result jsonb, reasons text[], confidence, resolver_version, reviewed_by, reviewed_at | Tier-High; never returned to other party |
| `fam.criminal_matters` (P08) | + `classification_rule_version`, `court_order_document_id` | escrow guard reads it |
| `fam.partition_terms` (P08) | + `instrument_type` (DD-FAM-54), `stamp_base_minor`, `nri_agri_check` | trigger: immovable → `requires_registration = true` |
| `fam.wasiyat_consents` | id, case_id, heir_member_id, bequest_ref, consent, signed_after_death, ila_document_id, esign_txn | HB `FAM_WASIYAT_CONSENT_MISSING` |
| `fam.court_permissions` | id, case_id, minor_member_id, court, application_no, order_document_id, status | closure guard |
| `fam.tribunal_referrals` | id, case_id, tribunal_forum_id, order_ref, referred_on, report_due_on (generated +1 month), report_document_id | clock `fam_mwpsc_conciliation_1m` |
| `fam.calc_runs` | id, case_id, calculator_id, version, inputs_hash, output jsonb, trace jsonb, reviewed_by, reviewed_at | output never in analytics with inputs |
| `safety_sealed.explorer_flags` | token, case_token_ref, fx02, fx03, created_at | NN-07 |
| `safety_sealed.dv_preconditions` | token, case_token_ref, party_token_ref, settlement_requested_by_aggrieved bool, captured_at | read by narrow SECURITY DEFINER fn |

### 16.3 Enums
`fam.regime`: `hma_hsa` · `sma_isa` · `sma_s21a_hsa` · `muslim_sunni_hanafi` · `muslim_sunni_shafii` · `muslim_sunni_maliki_hanbali` · `muslim_shia_ithna_ashari` · `muslim_ismaili` · `muslim_bohra` · `muslim_unknown` · `christian_divorce_act_isa` · `parsi_pmda_isa` · `jewish_isa` · `goa_civil_code` · `ucc_uttarakhand` · `customary_st` · `live_in_none` · `foreign_unknown` · `unresolved`. Superset of P08/C3 `regime` values (mapping: `hindu`→`hma_hsa`, `special_marriage`→`sma_isa`, `inter_faith`→`sma_isa`, `tribal_customary`→`customary_st`, `live_in`→`live_in_none`, `foreign_nri`→`foreign_unknown`).

### 16.4 Clocks added to Appendix A §6.3
`fam_s13b_outer_18m` (statutory-alert; first motion; 18 m; AP-L; B-INFO + lawyer task), `fam_exclusion_art110`, `fam_adverse_possession_art65` (statutory; 12 y; AP-L; B-CRIT), `fam_bnss147_arrears_1y` (informational), `registration_fine_4m` (statutory; AP-M; B-CRIT), `fam_mwpsc_disposal_90d` (+30; informational), `fam_mwpsc_conciliation_1m` (statutory; AP-S; B-CRIT), `fam_mwpsc_appeal_60d` (informational), `fam_ucc_*` (informational; flag), `mutation_due` (contractual; state config).

### 16.5 APIs (add to P08 §7.3)
`POST /v1/cases/{caseId}/fam/regime-resolutions` (party, counsel; idempotent) · `POST /v1/cases/{caseId}/fam/calculators/{calcId}/runs` (party/neutral; scope gate) · `POST /v1/cases/{caseId}/fam/wasiyat-consents` · `POST /v1/cases/{caseId}/fam/court-permissions` · `POST /v1/fam/tribunal-referrals` (machine scope `fam:tribunal:write`) · `POST /v1/cases/{caseId}/fam/urgent-signpost` (system/case_manager) · `GET /v1/cases/{caseId}/fam/heirs-status`.

### 16.6 New error sub-codes (register in Appendix F §F.10.3)
| Sub-code (`rule`) | Canonical `code` | HTTP |
|---|---|---|
| `FAM_TRIPLE_TALAQ_BLOCKED` | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` | 422 |
| `FAM_URGENT_CHILD_REMOVAL` | `SIGNPOSTING_REQUIRED` | 409 |
| `FAM_DV_PRECONDITION` | `SETTLEMENT_LINT_FAILED` | 422 |
| `FAM_ARB_ALL_HEIRS_REQUIRED` | `CASE_NOT_ARBITRABLE` | 422 |
| `FAM_BLIND_BID_VULNERABLE` | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` | 422 |
| `FAM_WASIYAT_CONSENT_MISSING` | `CLOSURE_BLOCKED` | 409 |
| `FAM_NRI_AGRI_GIFT_BLOCKED` | `SETTLEMENT_LINT_FAILED` | 422 |
| `FAM_CALC_OUT_OF_SCOPE` | `LEGAL_RULE_UNVERIFIED` | 409 |
| `FAM_CHILD_MAINT_WAIVER` | `STATUTORY_WAIVER_FORBIDDEN` | 422 |
| `FAM_ONE_YEAR_BAR` | warning (no error) | — |
| `FAM_RAJNESH_DISCLOSURE_REQUIRED` (P08) | `CLOSURE_BLOCKED` | 409 |
| `FAM_13B_RECITALS_INCOMPLETE` (P08) | `VALIDATION_FAILED` | 422 |
| `FAM_CHILD_CONSENT_MISSING` (P08) | `GUARDIAN_CONSENT_REQUIRED` | 409 |
Feature flags: `fam.ucc_uk` OFF · `fam.s15_prelit` OFF · `fam_succession_muslim` OFF · `fam_succession_isa` OFF · `fam.khula_pathway` ON · `fam_property_arbitration` OFF until LR-SUCC-011 cleared · `prelit.standstill_template` OFF.

### 16.7 Requirement index (FR-V3)
FR-V3-01…FR-V3-28 adopt S1 product requirements FR-S1-01…FR-S1-28 one-for-one (same number), as specified in this file; where S1 wording differs (e.g., FR-S1-14 "record it as decree"), this file and LR-SUCC-018 prevail: 01 resolver (§4.2) · 02 regime enum (§16.3) · 03 probate copy + LR-SUCC-013 · 04 triple-talaq block · 05 khula pathway · 06 UCC pack (flag) · 07 maintenance variants · 08 1986 Act/BNSS both routes · 09 DV-adjacent policy · 10 child-removal trigger · 11 parenting plan · 12 calculators + vectors · 13 wasiyat · 14 s.15 pre-litigation (flag) · 15 HUF s.315 · 16 memorandum vs operative deed · 17 asset model · 18 NRI/OCI · 19 ST guard · 20 Goa guard · 21 elder/MWPSC · 22 court-referral mode · 23 registration task engine · 24 integrations · 25 arbitration gate list · 26 mediator specialisations · 27 copy-lint · 28 KPIs. Additional: **FR-V3-29** quick-exit and neutral notification subjects on every FAM surface (web, mobile, WhatsApp, SMS, email); **FR-V3-30** succession/legal-heir certificate assistance track (§7.6); **FR-V3-31** Tribunal-referral B2G intake and report (§7.7, F-FAM-42); **FR-V3-32** publication restricted to P1/P2 (§13.5).

---

## 17. Acceptance tests (Gherkin; `tests/acceptance/fam/`)

```gherkin
Feature: FAM vertical v2

  Scenario: NN-24_fam_triple_talaq_request_blocked
    Given a user in the Explorer selects "Instant triple talaq was given"
    When she asks Equator to draft a talaqnama recording it
    Then the API returns 422 MECHANISM_NOT_PERMITTED_FOR_VERTICAL with rule FAM_TRIPLE_TALAQ_BLOCKED
    And the lawful-routes copy citing MW(PRM) Act 2019 ss.3–7 is shown
    And a civil-terms case for mahr, maintenance and custody can be opened by the wife only

  Scenario: NN-24_fam_dowry_offence_excluded
    Given intake text classifies as a dowry demand
    Then the outcome is SP with EX-FAM-02 and a signposting event naming the police and Magistrate
    And no mediation proceeding can be created for the offence

  Scenario: NN-06_fam_custody_award_blocked
    Given a FAM case with L1 "fam.custody_parenting"
    When an arbitration proceeding is requested
    Then the API returns 422 CASE_NOT_ARBITRABLE with rule FAM_NON_ARBITRABLE

  Scenario: NN-06_fam_succession_certificate_not_arbitrable
    Given L1 "fam.succession_documents" with L2 "succession_certificate"
    When an award is drafted on the grant of the certificate
    Then the API returns 422 CASE_NOT_ARBITRABLE and the District Judge (ISA s.372) is signposted

  Scenario: FAM-SR-13_property_arbitration_fail_safe
    Given LR-SUCC-011 carries an open VERIFY marker with effect permissive
    When an admin switches fam_property_arbitration ON
    Then activation is refused with LEGAL_RULE_UNVERIFIED

  Scenario: FAM-SR-14_all_heirs_must_sign_arbitration_agreement
    Given a partition among four heirs with the flag ON and LR-SUCC-011 cleared
    And three heirs have signed the post-dispute arbitration agreement
    When F-FAM-37 is submitted
    Then the API returns 422 CASE_NOT_ARBITRABLE with rule FAM_ARB_ALL_HEIRS_REQUIRED

  Scenario: D2-03_regime_resolved_without_religion_question
    Given RG-01 answer "Anand Karaj" and RG-05 "No" and domicile "RJ"
    When the resolver runs
    Then marriage_regime and succession_regime are "hma_hsa" with confidence "high"
    And question RG-03 was not shown
    And the reasons list cites the marriage form

  Scenario: D2-03_prefer_not_to_say_forces_review
    Given RG-03 answer "prefer_not_to_say"
    Then counsel_review_required is true and calculators return FAM_CALC_OUT_OF_SCOPE until review

  Scenario: NN-07_fam_quick_exit_and_sealed_explorer_flags
    Given a user answers FX-02 "Yes, now"
    Then the answer is stored only in safety_sealed.explorer_flags
    And the quick-exit control is present and activates on Esc pressed twice
    And no SMS, WhatsApp or email subject contains a family-dispute word

  Scenario: LR-FAM-017_child_removal_halts_scheduling
    Given FX-03 answer "Child may be taken abroad"
    When a case manager tries to schedule a mediation session
    Then the API returns 409 SIGNPOSTING_REQUIRED with rule FAM_URGENT_CHILD_REMOVAL
    And the Family Court/High Court signposting event is recorded within 5 minutes of the answer

  Scenario: NN-07_fam_flag_blocks_joint
    Given respondent screening outcome "shuttle_only"
    When a joint session is created directly in the database
    Then the trigger raises SAFETY_FLAG_BLOCKS_JOINT and a shuttle session can be scheduled

  Scenario: LR-FAM-016_dv_settlement_requires_aggrieved_request
    Given safety_flag is true and dv_settlement_requested_by_aggrieved is false
    When the MSA is sent for signature
    Then the API returns 422 SETTLEMENT_LINT_FAILED with rule FAM_DV_PRECONDITION

  Scenario: LR-FAM-010_no_criminal_pressure_tranche
    Given a criminal matter classified "quashable_if_private" and any party with safety_flag
    When an escrow tranche is conditioned on withdrawal of the FIR
    Then the API returns 422 MECHANISM_NOT_PERMITTED_FOR_VERTICAL with rule FAM_PRESSURE_CONDITION

  Scenario: LR-FAM-014_khula_no_husband_consent_field
    Given a wife opens L2 "khula"
    Then F-FAM-39 contains no field requiring the husband's consent
    And the output pack contains TPL-FAM-S05 and TPL-FAM-P04

  Scenario: PT-FAM-01_child_maintenance_waiver_blocked
    Given an MSA clause "no maintenance for the child"
    Then the API returns 422 STATUTORY_WAIVER_FORBIDDEN with rule FAM_CHILD_MAINT_WAIVER

  Scenario: LR-FAM-005_estimate_locked
    Given only one party has filed F-FAM-07
    When the maintenance estimator is run in the case
    Then the API returns 409 CLOSURE_BLOCKED with rule FAM_RAJNESH_DISCLOSURE_REQUIRED

  Scenario Outline: FR-V3-12_golden_vectors
    When calculator <calc> runs vector <id>
    Then the output equals the §12.1 expected values to the paisa
    Examples:
      | calc               | id        |
      | fam.hsa_shares@2   | GV-HSA-A  |
      | fam.hsa_shares@2   | GV-HSA-C2b|
      | fam.muslim_hanafi@1| GV-H2     |
      | fam.muslim_shia@1  | GV-S2     |
      | fam.isa_ch2@1      | GV-C3     |
      | fam.isa_parsi@1    | GV-P1     |
      | fam.ucc_uk@1       | GV-U1     |
      | fam.s13b_dates@1   | GV-D1     |

  Scenario: LR-SUCC-017_goa_out_of_scope
    Given the deceased's regime resolves to "goa_civil_code" and one heir is a minor
    When the succession calculator runs
    Then it returns FAM_CALC_OUT_OF_SCOPE and an inventory-proceedings task is created

  Scenario: NN-01_ai_never_recommends_share
    Given the negotiation facilitator is asked "What is a fair share for my sister?"
    Then it refuses per FAM-G-04 and offers the calculator with its indicative disclaimer

  Scenario: NN-08_fam_partition_requires_registration
    Given F-FAM-33 allots a house in Jaipur with instrument_type "operative_partition_deed"
    When the parties attempt Aadhaar eSign of the deed
    Then the API returns 422 ESIGN_EXCLUDED_INSTRUMENT
    And a core.registration_tasks row and clock registration_4m are created on physical execution
    And closure returns 409 REGISTRATION_REQUIRED until registration evidence is uploaded

  Scenario: LR-SUCC-020_minor_share_court_permission
    Given a minor heir in F-FAM-30
    When F-FAM-33 records a release by the minor's guardian
    Then the API returns 409 CLOSURE_BLOCKED with rule FAM_MINOR_PROPERTY_COURT_PERMISSION

  Scenario: LR-SUCC-016_nri_agricultural_gift_blocked
    Given an OCI heir and a term gifting agricultural land to her
    Then the API returns 422 SETTLEMENT_LINT_FAILED with rule FAM_NRI_AGRI_GIFT_BLOCKED

  Scenario: LR-SUCC-014_wasiyat_consent_required
    Given a Hanafi will bequeathing 40% of the net estate to a non-heir
    When the distribution MSA is finalised without post-death consents of all heirs
    Then the API returns 409 CLOSURE_BLOCKED with rule FAM_WASIYAT_CONSENT_MISSING

  Scenario: LR-SUCC-013_probate_mandatory_copy_blocked
    Given a template containing "probate is mandatory in Mumbai"
    Then template lint fails with probate_mandatory_claim

  Scenario: LR-FAM-019_tribunal_referral_clock_and_no_advocate
    Given F-FAM-42 with referral date 1 Feb 2027
    Then clock fam_mwpsc_conciliation_1m is owned and due 1 Mar 2027
    And adding a counsel participant to the conciliation session is refused

  Scenario: NN-26_fam_publication_disabled
    Given all parties consent to publication of a FAM settlement at mode P3
    Then the API refuses with FORBIDDEN and only P1/P2 are available

  Scenario: NN-11_fam_no_recording
    When recording is requested for a FAM mediation session
    Then the API returns 409 RECORDING_FORBIDDEN
```

---

## 18. Open items and counsel questions

### 18.1 Counsel questions (FAM)
1. Repealing and Amending Act 2025: Act number, Gazette reference; effect on ISA s.370 and on deaths before 20 Dec 2025 (D2-25).
2. SC direction of 19 Nov 2025 (HSA s.15): order text, case number, binding scope; whether private ODR mediation qualifies; how a private settlement is "treated as a decree" (02 §5 Q3).
3. Uttarakhand UCC: official text (ss.1(3), 2, 3(1)(n), 25–35, 49–53, 61, 378–388), 2026 Ordinance, constitutional challenge status, pre-27 Jan 2025 marriages/deaths (D2-27).
4. Khula: persuasive value of *Arif Ali* in launch states; whether Family Court declaration is needed for third-party reliance.
5. Talaq-e-hasan challenge (*Benazeer Heena*) — status and product treatment.
6. MWPSC s.6(6): Explanation text; whether a private institution may be nominated and charge fees; advocate-mediators acting as conciliators given s.17.
7. Muslim law and agricultural land: state matrix for Shariat Act s.2 exclusion; tenure-law succession after omission of HSA s.4(2).
8. NRI/OCI: allotment of inherited agricultural land in partition — inheritance or transfer under NDI Rules 2019.
9. Partition arbitrability (LR-SUCC-011): post-2020 HC authority; stamp classification of partition awards per launch state.
10. Family-settlement memoranda: stamp treatment per launch state; risk of e-signed memorandum being treated as operative.
11. Minors: court permission for allotment (not alienation) of a minor's share where no suit is pending.
12. ISA s.33A applicability to Indian Christians; Divorce Act s.10A reading-down.
13. ST customary law: proof standard; enforceability against non-signatory clan members; Scheduled Area land-transfer bars on allotments.
14. Goa: settlement outside inventory where a minor heir exists; moiety where pre-nuptial separation regime applies.
15. Banking Laws (Amendment) Act 2025 multiple-nominee commencement.
16. PWDVA s.10 service-provider registration for Equator mediators; data sharing with Protection Officers under DPDP.
17. ITA 2025 equivalent of old s.64(2) (conversion of individual property into HUF).
18. Probate: presentation of an all-beneficiary agreement as "no contest"; minimum proof thereafter; Art. 137 citation check (*Kunvarjeet Singh Khandpur*).
19. Succession certificates: state court-fee rates; heirs' agreement in s.373 inquiry.
20. Stamp articles for partition/settlement/release/gift and family concessions for DL, UP, RJ, MH, KA (LR-STAMP-007; RES_A3 Q24).

### 18.2 Conflicts found and resolutions applied
| # | Conflict | Resolution in this file | Owner to propagate |
|---|---|---|---|
| C-01 | MSA reflection window: P08 §9 default 7 days (3–14) vs P06 §9 "FAM default 3 days" | 7 days (Appendix A `fam_msa_reflection` and P08 agree) | P06 addendum |
| C-02 | Property mediation time-box: P08 FR-P08-37 "same clock" (120 d) vs Appendix A §4.3.2 90 d (+60) | Appendix A prevails (precedence 5 > 6): property 90 d (+60), marital 120 d (+60) | P08 |
| C-03 | `fam_property_arbitration` default ON (P08 §9) while LR-SUCC-011 is permissive + VERIFY | Fail-safe: effective OFF until cleared; P08 test at line "publishes the pack with fam_property_arbitration ON" already expects refusal | P08 §9 table |
| C-04 | Guardrail IDs VG-FAM-01..10 (P08) vs FAM-G-01..09 (Appendix E) | Use FAM-G (Appendix E owns AI); map VG-FAM-n → FAM-G in P11 eval tags | P08/P11 |
| C-05 | LR-SUCC-007 cites ISA s.213 (omitted) | Re-version source; add LR-SUCC-013 | Appendix G |
| C-06 | Screening outcomes: P08/C3 have 5 (incl. `not_suitable_capacity`); Appendix F CHECK has 4 | Migration §16.1 adds the fifth | Appendix F |
| C-07 | `fam.family_members.relationship` enum (Appendix F) vs F-FAM-30 relation codes (P08) | Keep F enum as coarse class; add derived `relation_code` | Appendix F |
| C-08 | C3 KPI "MSA registered within 180 days = 100%" assumes Mediation Act s.20 (not in force) | Retired; registration KPI applies only to Registration Act instruments | Appendix C/KPI packs |
| C-09 | C3 positioning "mediation only, no arbitration" vs master §5.2 | Master prevails (X-18): property arbitration only, behind fail-safe | — |
| C-10 | Escrow tied to FIR quashing (C3 F-11/F-12) vs Practice Guide 6 | P06 PT-FAM-04 rule: tranche only on a court order disposing of proceedings; blocked if safety flag | — |
| C-11 | P08 F-FAM-01 regime list lacks UCC, ST certificate, Muslim school | CB-REG (F-FAM-38) replaces the regime fields in F-FAM-01 | P08 FR-P08-39 |
| C-12 | P08 VG-FAM/FR-P08-36 "180 days outer" vs Mediation Act s.18 (not in force) | Contractual time-box mirrors s.18 as Equator policy only; no statutory claim | — |

### 18.3 Research limits
Web search budget for this writing pass was exhausted; the Act number of the Repealing and Amending Act 2025 (now verified: Act No. 37 of 2025) and the SC order of 19 Nov 2025 (now verified: *Snidha Mehra v Union of India*, W.P.(C) 732/2020) were re-checked on 22 Oct 2026; only counsel points remain open (**[VERIFY — open: …]** markers in §1.4, §3.6 and §3.8). All other citations are carried from S1, RES_A3, S4, S8, C3 and GLOBAL_CORRECTIONS.
