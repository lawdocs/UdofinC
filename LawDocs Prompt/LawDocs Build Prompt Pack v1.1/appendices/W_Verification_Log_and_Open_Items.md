# Appendix W — Verification Log and Open Items

> **Binding for every phase and appendix.** Compiled by the pack integrator (X3) on 25 October 2026 from the files in `/home/claude/ldpack/pack/` (phases P00–P23, Appendices A–Z except this one, and `content/LawDocs_Website_Content_v1.0.md`). Every `[VERIFY]` marker and every open item below is a **build flag**: the dependent feature ships OFF or advisory-only until the item is closed with evidence in `docs/compliance/verification-log.md` (NN-38; FR-P00-50, FR-P00-52; FR-P03-57). Legal rows referred to as `LG-*` are in Appendix G; Consumer Help rows `CHR-*` in Appendix S; settings in Appendix R.
> **Snapshot rule.** The census (W.2) and backlog (W.3) are a snapshot of the pack at compilation. P00 regenerates them from source on every content release with the census script (W.1 step 7); the generated `verification-log.yaml` is the system of record and this appendix is its human-readable mirror.

---

## W.1 Verification protocol

1. **Primary source first.** Re-check the fact on the legislature's, regulator's, court's or vendor's own site or signed document; record URL, retrieval date, SHA-256 of the document and the exact provision. Secondary commentary never closes a `P1` item.
2. **Log entry.** Each `V-*` item becomes one row in `docs/compliance/verification-log.yaml`: `id`, `statement`, `source_to_check`, `files[]`, `lg_rows[]`, `flags_gated[]`, `owner_role`, `priority`, `status`, `outcome`, `evidence[]`, `verified_by`, `verified_on`, `recheck_trigger`.
3. **Status and outcome (reconciles P00 and P03).** `status` follows FR-P00-52: `OPEN` → `VERIFIED` or `REJECTED`. `outcome` records the result class and drives the `rul` `verification_status` (FR-P03-57):

| `status` | `outcome` | Meaning | `rul` `verification_status` | Flag effect |
|---|---|---|---|---|
| `OPEN` | — | Not yet checked | `NOT_CONFIRMED` | Flag OFF or advisory (NN-38) |
| `VERIFIED` | `CONFIRMED` | Primary text matches the pack | `VERIFIED` | Flag may be requested ON (maker-checker) |
| `VERIFIED` | `SECONDARY_ONLY` | Only reputable secondary source found | `SECONDARY_ONLY` | Protective use only; computational outputs labelled "Indicative" |
| `VERIFIED` | `CHANGED` | Fact differs from the pack | per corrected row | Raise a Governed content/rule change (Appendix G §G.23); correct phase text |
| `REJECTED` | `NOT_CONFIRMED` | Cannot be confirmed | `NOT_CONFIRMED` | Declared fallback stays; feature remains OFF |

4. **Close by data, not code.** Most items close with a Governed rule-pack, setting or content release (NN-29, NN-30); only items that change behaviour need a story.
5. **Flags carry the link.** Every flag that depends on an item stores `requires_verification_id` = the `V-*` (or `OI-*`) ID; the flag service refuses ON while the item is `OPEN` (FR-P00-50).
6. **Launch gates.** `P1` items gate the wave named in "Blocking phase / flag"; P23's go-live checklist fails while any `P1` item for that wave is `OPEN` (P23 §13). `P2` items gate their feature only. `P3` items are content accuracy and are cleared in the normal content cycle.
7. **Census script.** `tools/compliance/verify-census.ts` extracts every `\[VERIFY[^\]]*\]` marker with 110 characters of preceding context, classifies it to a `V-*` item by ordered rules (P00 builds `tools/compliance/verify-rules.json` from W.3: one ordered rule per item, keyed on its `LG-*` rows and topic terms; markers inside Appendix G rows resolve through their `LG-*` ID), reports unassigned markers as a CI warning, and regenerates W.2 and W.3. A marker added without a matching rule fails `verify-lint` until a `V-*` item is assigned.
8. **Recheck triggers.** Each closed item records what reopens it: amendment or new circular, vendor contract change, annual review (October), court decision, or a tenant rule challenge.

---

## W.2 `[VERIFY]` census

**Method.** All bracketed markers beginning `[VERIFY` were extracted with `grep -o "\[VERIFY[^]]*\]"` (with context) from every phase file, every appendix except this one, the website content deck, `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`; "Bare" counts markers with no qualifier (`[VERIFY]`); "V-items" is the number of distinct backlog items (W.3) the file's markers resolve to. This appendix is excluded because it restates the markers.

**Totals (refreshed at registry review G4, 25 Oct 2026, by script over the current files).** **1,854 markers** in 52 files: phases 578, appendices, website content, master `01` and decision log `02` 1,276; 906 bare and 948 qualified. At compilation the census covered 50 files and found 1,792 markers; the difference of 62 comes from later phase and appendix edits and from adding `01` (26) and `02` (4) to the scope. The markers de-duplicate to **130 backlog items** (34 `P1`, 65 `P2`, 31 `P3`), of which 59 markers at compilation were umbrella or legend markers (V-130) that close with their underlying topic. The "V-items" column and the domain table below reflect the W.3 mapping made at compilation; markers added since compilation, and those in `01`/`02` (which restate phase and appendix facts), are assigned to existing V-items by the P00 census script at its next run, and a new V-item is opened only if a marker states a fact no W.3 item covers.

| Phase file | Markers | Bare | V-items | Appendix / content file | Markers | Bare | V-items |
|---|---|---|---|---|---|---|---|
| P00 | 16 | 7 | 6 | App A | 6 | 3 | 5 |
| P01 | 29 | 14 | 18 | App B | 13 | 10 | 7 |
| P02 | 0 | 0 | 0 | App C | 1 | 1 | 1 |
| P03 | 10 | 5 | 7 | App D | 4 | 0 | 2 |
| P04 | 16 | 7 | 13 | App E | 19 | 13 | 12 |
| P05 | 15 | 3 | 7 | App F | 204 | 153 | 42 |
| P06 | 9 | 5 | 6 | App G | 277 | 91 | 102 |
| P07 | 6 | 4 | 1 | App H | 5 | 1 | 3 |
| P08 | 32 | 7 | 16 | App I | 64 | 44 | 32 |
| P09 | 12 | 6 | 6 | App J | 27 | 14 | 5 |
| P10 | 34 | 16 | 15 | App K | 8 | 1 | 5 |
| P11 | 27 | 7 | 12 | App L | 29 | 19 | 19 |
| P12 | 51 | 29 | 11 | App M | 36 | 24 | 17 |
| P13 | 37 | 13 | 10 | App N | 22 | 11 | 15 |
| P14 | 103 | 59 | 19 | App O | 73 | 26 | 36 |
| P15 | 35 | 16 | 19 | App P | 40 | 18 | 25 |
| P16 | 27 | 15 | 12 | App Q | 17 | 9 | 14 |
| P17 | 12 | 7 | 5 | App R | 43 | 20 | 21 |
| P18 | 7 | 4 | 4 | App S | 68 | 30 | 24 |
| P19 | 15 | 3 | 12 | App T | 89 | 57 | 13 |
| P20 | 11 | 2 | 6 | App U | 18 | 7 | 4 |
| P21 | 26 | 9 | 14 | App V | 4 | 3 | 2 |
| P22 | 25 | 9 | 4 | App X | 11 | 4 | 7 |
| P23 | 23 | 8 | 11 | App Y | 5 | 1 | 2 |
|  | | |  | App Z | 6 | 5 | 4 |
|  | | |  | Website content v1.0 | 157 | 69 | 45 |
|  | | |  | Master prompt `01` | 26 | 14 | — |
|  | | |  | Decision log `02` | 4 | 3 | — |
| **Phases total** | **578** | **255** | | **Appendices + content + `01`/`02` total** | **1,276** | **651** | |

**By domain (W.3 mapping at compilation; 1,792 markers).**

| Domain | Items | Markers |
|---|---|---|
| eSign | 8 | 59 |
| Evidence | 3 | 24 |
| Aadhaar/identity | 3 | 17 |
| DigiLocker | 3 | 26 |
| Data protection | 9 | 87 |
| Foreign privacy | 1 | 14 |
| AI provider | 2 | 34 |
| Courts and procedure | 13 | 133 |
| Stamp and registration | 10 | 202 |
| Contracts and property | 11 | 93 |
| Companies and governance | 7 | 194 |
| Business registrations | 1 | 48 |
| RBI consumer rules | 9 | 78 |
| Payments | 4 | 22 |
| Insurance | 3 | 30 |
| Consumer protection | 3 | 47 |
| Professional conduct | 6 | 58 |
| Tax | 5 | 131 |
| Labour | 2 | 28 |
| IP | 7 | 102 |
| Motor vehicles | 3 | 45 |
| Telecom | 2 | 45 |
| Accessibility | 2 | 33 |
| Retention | 1 | 9 |
| Ecosystem contracts | 1 | 9 |
| Technology and vendors | 6 | 145 |
| Academy | 1 | 6 |
| Website facts | 2 | 9 |
| Market data | 1 | 5 |
| Umbrella markers | 1 | 59 |
| **Total** | **130** | **1792** |

---

## W.3 Verification backlog (`V-001`…`V-130`)

**Priority.** `P1` — gates Wave 1, drives a Locked/protective rule or a public legal statement; `P2` — gates a Wave 2/3 feature or computational rule; `P3` — content accuracy, no feature gate. **Owner role** — the role that closes the item (reviewer-of-record roles per Appendix G §G.0.1). **Files affected** — file codes (`Pxx` phase; letter = appendix; `Web` = website content) with marker counts.

| V-ID | Domain | Fact to verify | Source to check | Markers | Files affected (count) | Blocking phase / flag | Owner role | Pri | LG rows |
|---|---|---|---|---|---|---|---|---|---|
| V-001 | eSign | IT Act First Schedule entries as amended 26 Sep 2022; s.3A/s.10A wording; Entry 5 omission reading (X-02) | India Code; S.O. 4720(E) gazette | 11 | P21, F, G(3), Web(6) | NN-07 gate rows; website eSign copy | PLT_LEGAL_REVIEWER (ADV) + [COUNSEL] | P1 | LG-001–LG-003 |
| V-002 | eSign | Capricorn and Protean CCA licence renewal evidence | CCA licensed-CA list; ESP letters | 2 | A, I | ESP routing (X-16); `sgn` signing go-live | PLT_SECURITY_OFFICER | P1 | LG-005 |
| V-003 | eSign | Second-ESP-within-one-month rule under API v3.3 and its application to aggregator-ASP structures; ESP availability of account eSign | CCA eSign API v3.3; aggregator/ESP written confirmation | 12 | P03, P08, P19, G, I(2), O(2), P, R, Web(2) | `sgn.esp.second_route_within_days`; P08/P19 ASP mode | Procurement + [COUNSEL] | P1 | LG-008 |
| V-004 | eSign | ESP/aggregator contract terms: consent wording, audit frequency, incident notice, log export, mobile SDK vs browser, page accessibility | Signed ESP/aggregator contracts | 11 | P08(4), P22(3), P23(2), G, P | P08 go-live checklist; P22 signing flow | P08 lead + Procurement | P1 | LG-006, LG-009, LG-010 |
| V-005 | eSign | Biometric RD-device rules and whether any ESP offers face-authentication eSign under a cited instrument | CCA/UIDAI; ESP product terms | 6 | P08(3), G(3) | `AADHAAR_BIO`, `AADHAAR_FACE` methods | PLT_LEGAL_REVIEWER | P2 | LG-013, LG-034 |
| V-006 | eSign | CCA Class 2 discontinuation date; DSC token-driver batch behaviour; organisation-seal CA terms | CCA notice; CA product terms | 11 | P08(3), G(3), I(2), M, P, R | `sgn.dsc.class_required`; `sgn.org_seal.enabled` | PLT_SECURITY_OFFICER | P2 | LG-011, LG-012 |
| V-007 | eSign | CA-operated RFC 3161 TSA provider and terms | CCA-licensed CA offering TSA | 5 | P04, P08(2), G, I | PAdES-B-LTA timestamps (`TSA_PORT`) | PLT_SECURITY_OFFICER | P1 | LG-006 |
| V-008 | eSign | Incremental-update certificate validation in common PDF readers | Test matrix (Acrobat, browser viewers) | 1 | P08 | `sgn.evidence.append_certificate_incremental` | QA lead | P2 | LG-006 |
| V-009 | Evidence | BSA s.63(4) Schedule field labels and *Pune Bar Assn.* (2026 SCC OnLine SC 1297) citation; Part B expert eligibility | e-Gazette BSA Schedule; SC judgment | 14 | P05(3), P08, P10, P15, P20, G, K, M, O, S, Y(2) | `sgn.bsa63.enabled`, `dix.bsa63.enabled`; NN-10 certificate | PLT_LEGAL_REVIEWER + [COUNSEL] | P1 | LG-091 |
| V-010 | Evidence | BSA ss.85–87 wording, s.86 presumption, s.132 privilege; related table entries | India Code (BSA 2023) | 8 | F(2), G(3), O(2), Web | Help text; App O privilege clause | PLT_LEGAL_REVIEWER (ADV) | P3 | LG-014, LG-246 |
| V-011 | Evidence | Admissibility of recorded calls by a party; current SC authority | SC/HC judgments | 2 | J, S | Consumer Help evidence guidance | PLT_LEGAL_REVIEWER (ADV) | P3 | LG-091 |
| V-012 | Aadhaar/identity | Aadhaar 2025 amendment regulations: gazette date, Reg 13A OVSE fees/documents, surrender duties | UIDAI e-Gazette; OVSE Playbook | 8 | P01(2), F, G, I, P(2), U | `kyc.ovse.avc.enabled` (Phase 2) | [OWNER] + [COUNSEL] | P2 | LG-029, LG-030 |
| V-013 | Aadhaar/identity | UIDAI secure-QR specification version; which QR versions embed the full number | UIDAI developer documentation | 2 | P01, P04 | `kyc.ovse.qr.enabled`; masking of legacy QR (NN-04) | Tech lead | P1 | LG-030, LG-026 |
| V-014 | Aadhaar/identity | Aadhaar Act 2019 amendment commencement and ss.3A–8A wording; UIDAI Circular 8 of 2025 text; AOV Regulations 2021 regulation numbers (consent revocation) | UIDAI circulars and regulations | 7 | P01(2), G(4), P | Privacy-centre "Revoke Aadhaar data" | PLT_DPO | P2 | LG-021–LG-025, LG-028, LG-031, LG-032 |
| V-015 | DigiLocker | NeGD written position on user-directed saving and onward display of DigiLocker documents; requester onboarding status | NeGD written reply; Requester ToU Jun 2025 | 16 | P01(2), P04(2), P14, P20, P23, B, G, I, O, Q, R(2), Web(2) | `kyc.digilocker.retain_copy`; share packs; exports (NN-42) | PLT_DPO + [OWNER] | P1 | LG-038 |
| V-016 | DigiLocker | Entity Locker requester API coverage, eligibility and terms | NeGD Entity Locker | 3 | G, I, Q | `ENTITY_LOCKER_PORT` | P01 lead | P2 | LG-039 |
| V-017 | DigiLocker | DigiLocker issuer availability for RC/DL; DPDP r.10/11 guardian-proof mechanism and acceptable proofs | DigiLocker issuer list; DPDP Rules | 7 | P01(2), P04, P15(3), G | RC/DL pulls (P15); guardian flows; `iam.age_assurance.mode` | PLT_DPO | P2 | LG-040, LG-066 |
| V-018 | Data protection | DPDP commencement/acceleration; Rule 3/4/7/14 texts; consent-manager availability; Board breach mechanism | e-Gazette; MeitY notifications | 23 | P01(2), P09, P21(2), P23, G(4), I, N(2), O(5), P(2), R, T, V | `dpdp.commencement_date`; `core.breach.dpdp_report_hours`; consent-manager flag | PLT_DPO | P1 | LG-061–LG-070 |
| V-019 | Data protection | DPDP s.7 clause letters (voluntary provision; employment purposes) | DPDP Act text | 8 | P01, P13, P18, F, O(3), P | ROPA bases; HRMS notices; App O | PLT_DPO + [COUNSEL] | P2 | LG-064 |
| V-020 | Data protection | DPDP s.5(3) notice-language sub-section | DPDP Act text | 5 | P01, G, O(2), P | Notice languages (P01, App O) | PLT_DPO | P2 | LG-432 |
| V-021 | Data protection | DPDP s.14 nomination wording and Rules procedure | DPDP Act/Rules | 2 | P04, G | `IND_NOMINEE` release flow | PLT_DPO + [COUNSEL] | P2 | LG-430 |
| V-022 | Data protection | DPDP s.17(1)(a) legal-claims exemption scope | DPDP Act; counsel note | 4 | P10, P15, G, O | Evidence processing basis (P10, P15) | [COUNSEL] | P2 | LG-431 |
| V-023 | Data protection | DPDP Rule 13 SDF content; Third-Schedule classes; penalty Schedule rows; TDSAT appeal period | DPDP Rules; Act Schedule | 8 | P20, G(2), O(2), P(2), T | Risk register; erasure notices; policy text | PLT_DPO | P2 | LG-067, LG-071, LG-433 |
| V-024 | Data protection | IT Rules 2021 as amended 2026: grievance (24 h/7 d), takedown 3 h, intimate imagery 2 h, reminders 3 months, SGI labels, r.3(1)(g) 180 days, r.3A appeal | e-Gazette Amendment Rules 2026 | 30 | P01(2), P03, P21(4), P23, G(4), O(12), P, R(2), X(2), Web | `kyc.grievance.resolve_days`; site footer; video labels; takedown on-call | PLT_LEGAL_REVIEWER + [COUNSEL] | P1 | LG-077, LG-078, LG-434, LG-435 |
| V-025 | Data protection | SPDI Rules 2011 rule numbers; IT Act s.66C/72A wording | India Code | 3 | G(2), O | Privacy policy; `cvl` copy | PLT_DPO | P3 | LG-075, LG-076 |
| V-026 | Data protection | CERT-In 2025 audit guidelines applicability; Directions effective date | CERT-In website | 4 | P23, G(2), P | P23 audit plan | PLT_SECURITY_OFFICER | P2 | LG-079, LG-080 |
| V-027 | Foreign privacy | GDPR/UK DUAA changes; CCPA CPI-adjusted threshold; EU adequacy position; other foreign items | EDPB/ICO/CPPA sites | 14 | P13, P21, F(2), G(2), O(2), P(2), T(4) | EU/UK/CA jurisdiction flags; App O supplements | PLT_DPO | P3 | LG-084–LG-086 |
| V-028 | AI provider | Bedrock India model availability (Claude 5.5, vision, embeddings), caching/batch/Files API on `in.`, retention and AWS human-review terms | AWS Bedrock India docs; AWS DPA | 18 | P04, P05(3), P09(4), H(2), I(4), O, P(3) | `LLM_PORT` routing; P05 vision; P04 semantic search | CTO | P1 | LG-069 |
| V-029 | AI provider | Anthropic Usage Policy high-risk legal requirements and 12 Nov 2026 effective text | Anthropic Usage Policy (final) | 16 | P05, P06, P21, G(2), H(2), I(2), O(2), P, R(2), X, Web | `drf.ai_custom.individual_delivery_mode`; `drf.template.ai_prefill.individuals`; AI disclosure | [OWNER] + [COUNSEL] | P1 | LG-450 |
| V-030 | Courts and procedure | Court render profiles (paper, margins, fonts), e-filing size/PDF rules, e-vakalatnama and digital-signature acceptance per forum | HC rules and practice directions; portals by test upload | 24 | P05, P10(7), P11(3), F(5), G(3), I, Q, R(3) | P10 render profiles; P11 bundle checks (`LD-LIT-026`) | PLT_LEGAL_REVIEWER | P2 | LG-094, LG-095, LG-234 |
| V-031 | Courts and procedure | Constitution Art. 348 and CPC s.137 wording; certified-translation rules per forum | India Code; HC rules | 4 | P05(2), P10, G | P05/P10 translation routing (NN-48) | PLT_LEGAL_REVIEWER + [COUNSEL] | P2 | LG-093, LG-094 |
| V-032 | Courts and procedure | Limitation Act articles and exclusions used in advisory seeds; *Kunvarjeet* citation; CPA s.69 condonation practice | India Code; SCC | 18 | P10(4), P11(2), P15, P21(2), A, E, G(4), L, S(2) | `IN.lit.limitation_advisory` rows (advisory) | PLT_LEGAL_REVIEWER | P2 | LG-092, LG-230–LG-232, LG-216 |
| V-033 | Courts and procedure | Special-statute clocks: GSTAT start date, ITAT section under ITA 2025, MV s.166(3), Commercial Courts s.12A | India Code; GSTAT notification | 20 | P10, P11(4), P13, E, F, G(12) | P11 clocks `GSTAT`, `ITAT` | PLT_LEGAL_REVIEWER + TAX | P2 | LG-233, LG-235, LG-237–LG-243, LG-410 |
| V-034 | Courts and procedure | CNR structure and eCourts QR content; eCourts Official API eligibility; operational benches | eCourts services documentation | 10 | P11(5), P19, G(3), K | Scan-to-add; `eCourtsOfficialApi` adapter (OFF) | Product analyst + [COUNSEL] | P2 | LG-096A |
| V-035 | Courts and procedure | BNSS/BNS sections and transition (ss.528, 530, 531; BNS ss.351, 358; CrPC equivalents) | India Code | 11 | P10(2), P11, E(2), G(2), O, S(2), Web | Pleadings pre-1 Jul 2024 toggle; Consumer Help notes | PLT_LEGAL_REVIEWER | P2 | LG-244, LG-436 |
| V-036 | Courts and procedure | Court-data vendor coverage, terms, residency and lawful-collection warranty | Vendor contracts (two) | 8 | P11(2), I(2), P, Web(3) | `COURT_DATA_PORT`; watch lists; "real-time" never claimed | Procurement + [COUNSEL] | P2 | LG-096A |
| V-037 | Courts and procedure | Party-in-person practice; SC direction on caste/religion in cause titles; minors/victim masking statutes | SC/HC directions; POCSO/JJ Acts | 6 | P10(4), G(2) | P10 lint rules V-9 | PLT_LEGAL_REVIEWER | P3 | LG-250, LG-251 |
| V-038 | Courts and procedure | Emergency and helpline numbers (112, 181, 1930); DLSA eligibility and income limits by State | MHA/NCW/NALSA sites | 13 | P01, P09, P11(2), P15, G(2), I, N, S(4) | Vidhi hand-off screens; Consumer Help banners | PLT_CONTENT_EDITOR | P1 | LG-245, LG-186 |
| V-039 | Courts and procedure | E-notarisation and remote oath status per State/forum | Notaries Act notifications; forum rules | 10 | P08, P10(2), F(2), G, I, M, O, Web | `pld.oath.remote.<forum>`; affidavit packs | PLT_LEGAL_REVIEWER | P2 | LG-106 |
| V-040 | Courts and procedure | India Post bulk API access and courier proof-of-delivery artefacts | India Post CEPT; courier contracts | 4 | P10(2), I(2) | `POSTAL_DISPATCH_PORT` | P10 lead | P2 | — |
| V-041 | Courts and procedure | Courts' acceptance of email/messaging service of notices | HC/SC judgments | 3 | F, Web(2) | Notice-dispatch guidance | PLT_LEGAL_REVIEWER | P3 | — |
| V-042 | Courts and procedure | IBC s.59(3)(a) declaration of solvency affidavit | IBC; IBBI regulations | 2 | F(2) | App F IF-11 rows | PLT_LEGAL_REVIEWER | P3 | LG-237 |
| V-043 | Stamp and registration | State stamp-duty rates, articles, concessions, surcharges, rounding and inter-State rules (all 36 States/UTs; launch States first) | State Stamp Acts and schedules; State notifications | 94 | P08(2), P10, P12, P15, E, F(49), G(4), O, Web(34) | `IN-<ST>.stamp.*` tables; duty calculator `ESTIMATE` banner | PLT_LEGAL_REVIEWER | P1 | LG-097, LG-267 |
| V-044 | Stamp and registration | State e-stamp channels and coverage (SHCIL list, State portals, GRAS/GRIPS, franking, physical-only States) | SHCIL; State treasury portals; vendor coverage letters | 42 | P03, F(29), G(2), P, S, Web(8) | State registry `channel` field; eStamp procurement | PLT_LEGAL_REVIEWER + Procurement | P1 | LG-098, LG-099 |
| V-045 | Stamp and registration | State e-registration acceptance of eSigned instruments | State registration departments | 4 | F(2), G, Web | `accepts_esigned`; `ESIGN_OK_REGISTRATION_ROUTE` | PLT_LEGAL_REVIEWER | P1 | LG-104 |
| V-046 | Stamp and registration | Registration Act wording (ss.17, 18, 23, 25, 32–33), State additions, witness and document checklists, fee schedules | India Code; State amendments | 20 | P08, F(11), G, L, N, O, R(2), Web(2) | `REGISTRATION_REQUIRED` rows; `AGR_REGISTRATION_PENDING` clock | PLT_LEGAL_REVIEWER | P1 | LG-104, LG-262 |
| V-047 | Stamp and registration | Maharashtra Rent Control Act s.55 leave-and-licence registration and online acceptance | Maharashtra IGR | 5 | F(2), G, Web(2) | `IN-MH` rent rows | PLT_LEGAL_REVIEWER | P1 | LG-263 |
| V-048 | Stamp and registration | Model Tenancy Act 2021 adopting States and State tenancy laws | State gazettes | 9 | G, Web(8) | Rent-agreement variants (P06; website) | PLT_LEGAL_REVIEWER | P2 | LG-264 |
| V-049 | Stamp and registration | Indian Stamp Act s.2(14) Finance Act 2019 text; ss.17, 18, 29, 35, 49–50 and State refund/cancellation rules | India Code; State rules | 13 | P06, P08(2), F(4), G, L, N, O, Web(2) | Stamp-before-sign lock text; refund clause (App O) | PLT_LEGAL_REVIEWER | P1 | LG-096, LG-260 |
| V-050 | Stamp and registration | Registration Bill 2025 status | DoLR; Parliament | 3 | F, G, Web | Draft rows stay `DRAFT` | PLT_LEGAL_REVIEWER | P3 | LG-105 |
| V-051 | Stamp and registration | NeSL DDE notification (30 Jun 2020) and aggregator access | MoF notification; NeSL | 5 | P19, G(2), I(2) | `NESL_DDE` adapter | Integration lead | P3 | LG-101 |
| V-052 | Stamp and registration | e-stamp UIN verification APIs per vendor; certificate number formats; GRAS/e-SBTR proofs for electronic instruments | Vendor docs; State portals | 7 | P08(2), F(2), G, I, K | `ESTAMP_VERIFY`; import patterns (App K) | P08 lead | P1 | LG-098, LG-100 |
| V-053 | Contracts and property | Contract Act s.27 case law on non-competes; s.11 minors | SC/HC judgments | 7 | P14, F, G(2), Web(3) | Template warnings | PLT_LEGAL_REVIEWER | P3 | LG-280, LG-282 |
| V-054 | Contracts and property | TPA provisions (ss.3, 53A, 54, 58–59, 105–107, 106 amended text, 123) and electronic attestation | India Code; counsel | 11 | P20(3), F(3), G(3), O, Web | Witness/attestation rules; notice templates | PLT_LEGAL_REVIEWER + [COUNSEL] | P1 | LG-283–LG-285 |
| V-055 | Contracts and property | Succession Act and Registration Act provisions for wills (s.63; ss.42–46) | India Code | 6 | P08, F(4), G | Will packs | PLT_LEGAL_REVIEWER | P2 | LG-262, LG-286 |
| V-056 | Contracts and property | Trusts Act wording; Waqf Act 2025 amendment status; public-trust recordal | India Code; State Acts | 7 | F(4), G(2), P | Trust/wakf rows (wet ink) | PLT_LEGAL_REVIEWER + [COUNSEL] | P2 | LG-287, LG-293 |
| V-057 | Contracts and property | Family-law grounds, forms and citations (HMA, DMMA, PCMA, PWDVA, HAMA/JJ adoption, *Rajnesh v. Neha*) | India Code; SCC | 11 | P06, E(3), F(5), G(2) | Family pleading and adoption rows | PLT_LEGAL_REVIEWER | P3 | LG-291, LG-292 |
| V-058 | Contracts and property | RERA s.13(1) wording, State model forms, s.31 complaint forms | RERA Act; State rules | 6 | E(2), F(2), G, Web | RERA agreement and complaint templates | PLT_LEGAL_REVIEWER | P2 | LG-241, LG-288 |
| V-059 | Contracts and property | Mediation Act 2023 commencement and online mediation; CPC O.XXIII r.3; s.12A PIMS; family settlements; 2023 seven-judge stamping case; *Emaar* citation | India Code; SCC | 15 | P11, P19, E(2), F(5), G(4), O(2) | Settlement/ODR templates; App F IF-49 | PLT_LEGAL_REVIEWER | P3 | LG-234–LG-236, LG-249, LG-261 |
| V-060 | Contracts and property | NI Act s.138/142 periods, cheque-validity circular; Advocates' Welfare Fund stamp | India Code; RBI circular; State Acts | 9 | P10(2), F(3), G, L, M, Web | Notice templates; vakalatnama rows | PLT_LEGAL_REVIEWER | P2 | LG-240, LG-248 |
| V-061 | Contracts and property | POA execution, notarisation and State registration/duty; *Suraj Lamp* citation | Powers-of-Attorney Act; Notaries Act; State Acts | 10 | F(6), G(2), Web(2) | POA rows (wet ink) | PLT_LEGAL_REVIEWER | P2 | LG-265, LG-266 |
| V-062 | Contracts and property | Receipt stamp threshold and electronic receipts; acknowledgement-of-debt and bond articles | State schedules | 5 | F(4), O | Receipt/bond rows | PLT_LEGAL_REVIEWER | P3 | LG-260 |
| V-063 | Contracts and property | Securities and corporate instruments: SH-4 practice, share-certificate duty, ESOP letters, FEMA reporting, CCPS/convertibles, charges/CERSAI | Companies Act; FEMA; State schedules | 6 | F(6) | Corporate instrument rows (App F) | CS reviewer + [COUNSEL] | P2 | LG-301, LG-302 |
| V-064 | Companies and governance | Companies Act thresholds, rule numbers, forms and timelines in governance and business-service seeds (rr.3, 4, 6, 8, 8A, 12A; MGT-14 list; MR-1; DIR-3 KYC; INC-20A; registers; exemptions) | India Code; MCA notifications; MCA21 forms | 98 | P04, P13(16), P14(10), B(2), E, F(9), G(22), K(2), L(2), M, T(29), Z, Web(2) | Governance blueprints (advisory badges); P14 calendars | CS reviewer | P2 | LG-155–LG-160, LG-300–LG-316 |
| V-065 | Companies and governance | SS-1/SS-2 paragraph references and electronic signing of minutes | ICSI SS-1, SS-2 (revised 1 Apr 2024) | 20 | P13(7), A(2), F(3), M(2), R(4), T, Web | `gov.minutes.*` days; minutes signing route | CS reviewer | P2 | LG-156 |
| V-066 | Companies and governance | LLP Act/Rules section, period and forms (Form 3, Form 24) | LLP Act; MCA | 7 | P14(4), F(2), T | LLP formation/closure services | CS reviewer | P3 | LG-316 |
| V-067 | Companies and governance | RBI NBFC directions titles and paragraphs used in finance-company structure (governance, compliance, IT, ALM, fraud, RBIA, IO, KYC, HFC, CIC) | RBI consolidated directions (2025–26) | 55 | P13(2), P19, G(4), L, T(45), Z, Web | App T overlay (ADVISORY); P13 finance template | Regulatory analyst (LDC SoR) | P2 | LG-161, LG-188, LG-319 |
| V-068 | Companies and governance | SEBI LODR Reg 24A, Reg 30/Schedule III item, SBEB applicability, woman-director rule for listed entities | SEBI regulations | 7 | P11, P14(4), G, T | Listed-company seeds; material-litigation flag | CS reviewer | P3 | LG-301, LG-310, LG-318 |
| V-069 | Companies and governance | Ind AS 37/AS 29/Ind AS 38 paragraphs; Schedule III divisions; Accounts Rules r.3(1)/r.3(5) | ICAI/MCA standards and rules | 5 | P11(2), P12, P14, I | Provisioning notes (P11); books back-up (P20) | CA reviewer | P3 | LG-307 |
| V-070 | Companies and governance | Registered Valuers Rules applicability to IP valuations | IBBI/MCA | 2 | P12, G | P12 valuation routing | CS reviewer | P3 | LG-317 |
| V-071 | Business registrations | Government fees and form versions for 48 business-service rows (DGFT/IEC, APEDA, Spices, AGMARK, BIS, pollution consent, GI, Nidhi, societies, Udyam, DPIIT, FCRA, ESI) | Authority portals | 48 | P01, P14(34), F(2), G(8), I(2), Web | `bsv.fee_schedule` rows; P14 catalogue | PLT_LEGAL_REVIEWER | P2 | LG-320–LG-324 |
| V-072 | RBI consumer rules | RB-IOS 2026 clause numbers (3(1)(c), 10(1)(b), 10(1)(g), 14(2), 15, 17) and representation rule; residual route for out-of-scope REs | RB-IOS 2026 text (RBI) | 28 | P03(3), P16, P18, G(4), M(3), N, O(2), Q, R(6), S(4), Web(2) | `rulepack.IN.chp.rbios_2026`; `chp.rbios.*` keys; Consumer Help copy | P15 content + PLT_LEGAL_REVIEWER | P1 | LG-171, LG-173–LG-177 |
| V-073 | RBI consumer rules | RBI Internal Ombudsman Directions 2026 effective date and thresholds | RBI directions | 5 | G(2), S, T(2) | IO clock CHR-A-11; App T IO role | P15 content | P2 | LG-178 |
| V-074 | RBI consumer rules | RBC Fourth/Third Amendment paragraph numbers; pre-2027 calling-hours guidance; microfinance para 91; call-record retention; no-referral rule final text | RBI directions (6 Aug 2026); earlier circulars | 13 | P15(2), G(3), M, R, S(5), Web | `chp.recovery_conduct_rules_effective`; harassment checklist | P15 content | P2 | LG-180, LG-181 |
| V-075 | RBI consumer rules | NBFC RBC 2025 paras 34–41 and application to vehicle hypothecation/Form 35 | RBI NBFC RBC Directions 2025 | 15 | P08, P15(4), G, S(8), Web | Closure-request playbook; vehicle hypothecation removal | P15 content | P2 | LG-182 |
| V-076 | RBI consumer rules | DL Directions KFS paragraph; CMS acceptance of eSigned authorisations | RBI DL Directions 2025; CMS help | 3 | P15, G, S | Legitimacy check; RBIO authority letter | P15 content | P2 | LG-179 |
| V-077 | RBI consumer rules | RBI compromise-settlement framework (8 Jun 2023) content | RBI notification (not fetched) | 5 | P15, F, G, S(2) | Settlement-support copy | P15 content | P2 | LG-184 |
| V-078 | RBI consumer rules | Official link registry URLs (Sachet, Bima Bharosa, e-Jagriti, NCH, cybercrime) | Official sites | 5 | G, S(4) | `chp` official-link registry and link-health monitor | PLT_CONTENT_EDITOR | P2 | LG-186, LG-219 |
| V-079 | RBI consumer rules | BUDS Act exposure; escrow-partner licensing | BUDS Act; counsel note | 3 | G, S(2) | Vehicle-sale escrow (OFF) | [COUNSEL] | P3 | LG-187 |
| V-080 | RBI consumer rules | CIC compensation framework copy on website | RBI/2023-24/72 | 1 | Web | Website copy | PLT_CONTENT_EDITOR | P3 | LG-183 |
| V-081 | Payments | RBI PA Directions paragraphs; Razorpay Route MCC approval, transfer fee and on-hold limits; OH8 readiness | RBI PA Directions 2025; Razorpay | 7 | P16(2), G(2), I, L, S | M2 marketplace payouts; duty pass-through | Finance + OH8 owner | P1 | LG-145, LG-455 |
| V-082 | Payments | RBI e-mandate Directions 2026 limits and pre-debit rules; CoFT; Razorpay plan-change limits | RBI directions; Razorpay docs | 9 | P17(3), G(2), O, P, Web(2) | Subscriptions (P17); renewal notices | Finance | P1 | LG-146, LG-147 |
| V-083 | Payments | PCI DSS SAQ A eligibility for the chosen Razorpay checkout mode | PCI SSC; acquirer/QSA letter | 4 | P23, G, P(2) | Hosted checkout; SAQ A attestation | OH8 owner + PLT_SECURITY_OFFICER | P1 | LG-148 |
| V-084 | Payments | Lawful third-party collection of government dues and challan model | RBI PA Directions; counsel | 2 | G, L | Challan payment deep-link only | [COUNSEL] | P2 | LG-150 |
| V-085 | Insurance | IRDAI PPHI 2024 / Master Circular TATs and ₹5,000/day source; Bima Bharosa routes | IRDAI regulations and master circular | 11 | P15, G(2), O(2), Q, S(5) | Claim-delay calculator; insurer-stage clocks | P15 content | P2 | LG-200, LG-201 |
| V-086 | Insurance | Insurance Ombudsman practice on representatives; Karnataka HC reach; complaint form; cap and window | CIO; Rules 2017; judgment | 16 | P10, P15(3), G(3), M, O, R(3), S(3), Web | `chp.insurance_ombudsman.*`; representation matrix | P15 content + [COUNSEL] | P2 | LG-202–LG-204 |
| V-087 | Insurance | Insurance Act intermediary rules (no selling/commissions) | IRDAI regulations | 3 | P15, G, S | Consumer Help may/may-not list | [COUNSEL] | P3 | LG-205 |
| V-088 | Consumer protection | CPA 2019 pecuniary limits, s.69 condonation, appeal periods, agent regulations form, *Anuj Kumar Chauhan* reach, unfair-terms powers, complaint fees | DoCA; CPA 2019 and Rules | 20 | P10(2), P15(3), F, G(6), L, N, O, Q, R, S(3) | Complaint drafting; representation matrix; App O terms | PLT_LEGAL_REVIEWER | P2 | LG-140, LG-215–LG-220 |
| V-089 | Consumer protection | E-Commerce Rules 2020 sub-rules (r.4, r.4(5), r.5) and any 2026 amendment | DoCA gazette | 22 | P16(4), P21(3), F(5), G, L, M(2), O(3), Q, Web(2) | Seller panel; ranking page; grievance SLAs; no pre-ticked boxes | [COUNSEL] | P1 | LG-141 |
| V-090 | Consumer protection | CCPA dark-pattern and misleading-ads wording; ASCI influencer guideline | CCPA; ASCI | 5 | E, G(3), O | NN-50 checks; influencer template | PLT_LEGAL_REVIEWER | P3 | LG-142, LG-143, LG-221 |
| V-091 | Professional conduct | BCI rule numbering (Rules 20, 36, 37, 49; fee-sharing), Rule 36 Schedule wording, COP Rules 2015 | BCI Rules (official) | 19 | P01, P16(3), D, G(5), M(4), N, O(4) | Directory fields `RULE36_V1`; marketplace switches (NN-21) | [COUNSEL] | P1 | LG-111, LG-112, LG-118, LG-461 |
| V-092 | Professional conduct | *BCI v. A.K. Balaji* (SC 2018) citation | SCC/SCR | 5 | P16, G, M, O, T | Policies, Vidhi disclaimers | PLT_LEGAL_REVIEWER | P3 | LG-110 |
| V-093 | Professional conduct | *Sulekha v. P.N. Vignesh* SC status; BCI 2025–26 directions | SC case status; BCI circulars | 2 | G, X | Advocate directory page (OFF) | [COUNSEL] | P1 | LG-113 |
| V-094 | Professional conduct | ICAI Code edition, ICSI/ICMAI/IBBI platform guidance | ICAI/ICSI/ICMAI/IBBI sites | 16 | P01, P16, P21, F, G(4), M(7), O | CA/CS/CMA listing switches (locked OFF) | [COUNSEL] | P2 | LG-114–LG-117, LG-463 |
| V-095 | Professional conduct | Trade marks agent (s.145) and patent agent rules; who may act under the Designs Act | IP India; Patents/Designs Acts | 14 | P12(3), P14(3), P16(4), G, M(3) | `TRADE_MARKS_AGENT`/`PATENT_AGENT` sub-types; TM filing services | [COUNSEL] | P2 | LG-462 |
| V-096 | Professional conduct | PCA 1988 s.9 adequate-procedures guidance | MHA/CVC guidance | 2 | G, X | Gifts and hospitality register (OH) | PLT_LEGAL_REVIEWER | P3 | LG-464 |
| V-097 | Tax | Income-tax Act 2025 / Rules 2026 section and form mapping (TDS s.393 entries, advance tax, tax audit, 12A/80G, 80-IAC, AR, late fees, due dates, tax-year labels) | Official ITA 2025 text; CBDT notifications | 55 | P04, P06, P11, P13, P14(18), P16(4), P17, P21, P23, E(3), G(7), L(3), N(3), R(3), T, Web(6) | `tax.calendar.rule_set`; P14 tax packs; TDS fields; App K labels | CA tax adviser | P2 | LG-123, LG-125, LG-352–LG-355 |
| V-098 | Tax | ERI scheme type, eligibility, security audit and API scope; re-notification under the 2025 Act | Income-tax e-filing ERI documents | 24 | P14(7), G(7), I(3), J(3), M(2), R, Web | `ERI_PORT`; P14 return filing | [OWNER] + CA | P2 | LG-124 |
| V-099 | Tax | GST positions: RCM/exemption entries, ECO TCS, pure agent r.33, e-invoice AATO, IFSC, s.36 retention, late fee/interest, return set | CBIC notifications; CGST Act/Rules | 45 | P00(2), P01, P08, P14(7), P16, P17(3), P20, B(2), G(11), L(7), M(3), N(2), O(2), X(2) | Invoice lines; tax hints; retention classes; M2 switch | CA tax adviser + [TAX MEMO] | P1 | LG-128, LG-130, LG-340–LG-351 |
| V-100 | Tax | TDS statement/TRACES forms, taxpayer verification modes and portal delegation terms | TRACES; e-filing portal | 4 | P14, G(3) | P14 TDS service | CA tax adviser | P3 | LG-126, LG-129 |
| V-101 | Tax | GSP selection and taxpayer API-consent flow | GSTN GSP list; contract | 3 | P14, G(2) | `GSP_PORT` | [OWNER] | P2 | LG-049 |
| V-102 | Labour | Labour Codes rule-level effects (IR Code forms, OSH contract labour, Apprentices Act, wages definition, ESI thresholds) and record-retention | Code texts; Central and State rules; labour rulepack | 22 | P04, P14(2), P18(2), B(2), F(8), G(3), Web(4) | HRMS rows; employment templates; retention | CS reviewer + labour rulepack owner | P2 | LG-162–LG-165, LG-372–LG-374 |
| V-103 | Labour | POSH s.4(2) composition, s.13(4), annual report and r.8(5)(x) disclosure | POSH Act; Accounts Rules | 6 | P13(3), G(2), T | IC module validators | CS reviewer | P2 | LG-370, LG-371 |
| V-104 | IP | Trade Marks Act/Rules 2017 periods, rule numbers, forms and Registry formats (r.33, rr.45–47, s.21(2)–(3), s.25(2)–(4), s.47, s.91, TM-A/TM-48, Journal schedule, status labels) | Trade Marks Act/Rules (as amended); IP India | 36 | P12(19), P14, F, G(7), K, L, Q, R(4), Web | `rulepack.IN.ipm.tm_timelines`; TM-A data sheet | IP domain analyst | P2 | LG-170, LG-380–LG-385 |
| V-105 | IP | TM government fee schedule and applicant categories (₹4,500/₹9,000) | Trade Marks Rules 2017 First Schedule | 12 | P12(2), P14(2), P16, G, L, M(2), Q, Web(2) | Fee table; price cards (P12, P16) | IP domain analyst | P2 | LG-386 |
| V-106 | IP | Nice Classification edition in force | IP India | 4 | P12(3), G | `ipm.nice.edition` | IP domain analyst | P3 | LG-387 |
| V-107 | IP | WIPO GBD reuse terms; IP India terms for Journal retrieval; licensed TM data/watch partner | WIPO terms; IP India terms; partner contract | 18 | P12(9), P19, G, I(2), L, Q(2), R, Web | `TRADEMARK_DATA_PORT`, `TM_JOURNAL_PORT` | Integration lead + [COUNSEL] | P2 | LG-393 |
| V-108 | IP | Copyright, Designs and Patents rules as amended 2024 (r.24B, r.24C, r.80, Form 27, s.60, Designs ss.11–12, Copyright objection window) | Patents/Designs/Copyright Acts and Rules | 27 | P06(2), P12(12), P14(3), E, F(2), G(4), Web(3) | P12 deadline seeds; P14 IP services | IP domain analyst | P2 | LG-388–LG-391 |
| V-109 | IP | Domain grace periods per TLD; UDRP/INDRP | Registry policies | 2 | P12(2) | Domain records (P12) | IP domain analyst | P3 | — |
| V-110 | IP | IP dispute forum and commercial-court status; TM s.134; Tribunals Reforms Act 2021 | India Code | 3 | P12(3) | Dispute routing (P12) | PLT_LEGAL_REVIEWER | P3 | LG-235, LG-385 |
| V-111 | Motor vehicles | MV Act s.50/s.51/s.157 and CMVR r.55/r.81 basis, form versions, fees, RTO practices; registered-owner liability case law | MoRTH; Vahan; India Code | 30 | P15(2), F(5), G(6), S(8), Web(9) | Vehicle-sale pack; RC deadlines; website copy | P15 content | P2 | LG-107, LG-400–LG-403, LG-411 |
| V-112 | Motor vehicles | State Virtual Court/physical-court timelines, Lok Adalat rules per sitting, record-update lag; CMVR r.167 | State notifications; Lok Adalat notices | 10 | P15(3), G(2), N, S(4) | Challan stage clocks (data rows) | P15 content | P2 | LG-405, LG-408 |
| V-113 | Motor vehicles | Lawful vehicle/challan data source (MoRTH/NIC/API Setu); blacklist source; fleet data | MoRTH/NIC written reply | 5 | P15(3), G, S | Fleet subscription (OFF); pre-sale checks | [OWNER] + [COUNSEL] | P2 | LG-409 |
| V-114 | Telecom | TCCCPR Third Amendment Gazette date and commencement; Reg 4 CLI declaration; 1600-series eligibility; DCA for non-banks; header format; RCS DLT; "service" category for invitations; DLT entity | TRAI Gazette; TSP confirmations | 23 | P01, P03, P09, P15, P19, G(4), I, J(9), R(3), X | Voice/AI-voice flags; `ntf.a2p_declarations`; counterparty invitations | Compliance + [COUNSEL] | P1 | LG-149, LG-415–LG-422 |
| V-115 | Telecom | JioCX/Jio terms: BSP status, rate cards, masking, IVR/OBD endpoints, Verify coverage, Haptik residency/DPA, Jio AI Cloud APIs | JioCX contracts and docs | 22 | P04, I(6), J(13), L, P | JioCX adapters (OFF until verified) | Procurement + Integration lead | P2 | — |
| V-116 | Accessibility | RPwD Act/Rules text, r.15 2023 amendment, *Raturi*/*Prasun* directions, s.46 period, grievance authority wording; non-liveness KYC basis | India Code; SC judgments | 23 | P01(4), G(6), O(3), U(10) | `a11y.standard_set`; accessibility statement; KYC alternatives | PLT_LEGAL_REVIEWER + [COUNSEL] | P1 | LG-133–LG-136, LG-441 |
| V-117 | Accessibility | IS 17802 clause numbering; GIGW 3.0; ISL interpreter credentials and video thresholds; tagged-PDF tooling | BIS; MeitY; ISLRTC | 10 | G, I(2), N, U(6) | App U test matrix; ISL content; PDF/UA checks | Accessibility lead | P2 | LG-134, LG-137, LG-440 |
| V-118 | Retention | Retention floors for income-tax (2025 Act), labour records, registers, service orders and consumer cases (limitation + tax) | ITA 2025; Labour Codes; Companies Act; CGST | 9 | P04(2), P14, P15, B(4), S | `dms.retention.*` classes; P14/P15 closure retention | PLT_LEGAL_REVIEWER + TAX | P2 | LG-092, LG-128, LG-307 |
| V-119 | Ecosystem contracts | Ecosystem contract confirmations: Spec domain names (security incident, engineering events), kernel schema versions, Equator clause API, LDC realm federation, OH ESignProvider wording | Ecosystem Spec v1.1/v1.2; companion packs | 9 | P19(2), P23, A, B, I(2), Y(2) | `int` wiring; Appendix Y | Integration lead / Spec owner | P2 | — |
| V-120 | Technology and vendors | Stack and standards versions: Node 24 LTS *(v1.1: the Node item is closed — 24.22.1 pinned by IPB-D-01/D-18; the rest of this row stays open)*, PostgreSQL major, Temporal residency, Keycloak (hash import, SCIM, DPoP), ZEN/CEL, Cerbos, Expo SDK, OWASP ASVS/MASVS/LLM Top 10 editions, ISO 27701/42001, AICPA TSC, IETF headers, A2A/MCP versions, GitHub plan | Vendor and standards bodies | 31 | P00(4), P01, P03, P09(2), P19(3), P21, P22(2), P23(4), D(2), H, I(2), P(8) | ADR-0001 and related ADRs; P23 frameworks | CTO / Security engineer | P1 | — |
| V-121 | Technology and vendors | Microsoft Graph/Google scopes and quotas, CSPP/WOPI eligibility, Teams app publishing, tracked-change round-trip, SES inbound region, Azure region evidence | Microsoft/Google/AWS docs | 26 | P00, P04(2), P05, P07(6), P18(3), P19, P20(4), P21, G, I(5), P | `WORKSPACE_PORT`; P07 co-edit; P20 BYO targets | Integration lead | P2 | LG-453 |
| V-122 | Technology and vendors | Apple and Google store rules for India (IAP/Play Billing, person-to-person services, external links, account deletion, privacy manifests, AI disclosure, OTA, encryption, listing limits, ANR) | Apple/Google policy pages | 34 | P10, P13, P16, P17(4), P21, P22(17), P23(3), G(2), N(2), Q, Z | `store.<platform>.digital_sales_mode`; `bil.mobile.purchase_mode`; P22 submission | Mobile lead + [COUNSEL] | P2 | LG-451, LG-452 |
| V-123 | Technology and vendors | Translation, speech and OCR providers: Bhashini terms/retention, Sarvam, Google/Azure zero-retention, glossary licences, WhatsApp export limits | Provider terms; device tests | 15 | P05(4), P06(2), P09(2), P11, P21, P22(3), I, L | `TRANSLATE_PORT`, `INDIC_SPEECH_PORT`; P05 imports | PLT_DPO + AI lead | P2 | — |
| V-124 | Technology and vendors | Other vendor terms and facts: KYB/MCA/Udyam vendors, e-voting formats, Tally/HRMS/CRM APIs, Zapier/Make, plagiarism, Search Console, YouTube embed cookies, crawler names, Shorts/Reels limits, observability residency, Adobe Express API | Vendor docs and contracts | 33 | P00, P01(2), P13(2), P17, P19, P21(6), G(4), I(7), N(2), P(2), Q, R, X(3) | Respective adapters (OFF until verified); P21 SEO settings | Integration lead / SEO lead | P2 | LG-047, LG-048 |
| V-125 | Technology and vendors | Legacy-stack facts: Railway/Atlas regions, PayU dispute window, test-data reservations | Legacy accounts; RFC 2606/IANA; numbering plan | 6 | P00(5), P | P00 migration plan | Tech lead | P1 | — |
| V-126 | Academy | Graphy API/feed and SSO capability for FinLegal Academy | Graphy documentation | 6 | P16(3), P19, I, R | `ACADEMY_PORT`; `aca.sso_deep_link` | Academy lead | P3 | — |
| V-127 | Website facts | Launch facts for website copy (hosting region, encryption, onboarding checks, security mailbox) | Production evidence at launch | 7 | O, Web(6) | Website claims (NN-20) | SEO lead + PLT_SECURITY_OFFICER | P1 | — |
| V-128 | Website facts | Content-calendar anchor dates (filing season, AGM season, Consumer Day, Lok Adalat dates) | Official calendars each year | 2 | N(2) | Social/blog calendar | OPS_CONTENT_PUBLISHER | P3 | — |
| V-129 | Market data | Competitor and benchmark prices and claims (R1/R6) | Live vendor pages | 5 | L, Q(2), Web(2) | Savings model benchmarks (excluded until verified) | Product analyst | P3 | — |
| V-130 | Umbrella markers | Umbrella and definitional markers (legend text, "review flags", "every row") — closed when the underlying topic item closes | — | 59 | P00(3), P03, P04, P08, P14, P23(2), A, B, C, E, F(2), G(5), I(2), J, L(2), N, O(2), P, Q(2), R, S, T, U, V(3), Z(3), Web(18) | — | Pack lead | P3 | — |


---

## W.4 Open-item register (consolidated)

**Scope.** All 342 open items declared in phase and appendix tables or lists (`OI-P00-01`…`OI-P23-08`, `OI-B-*`, `OI-F-*`, `OI-H-*`, `OI-I-*`, `OI-J-*`, `OI-K-*`, `OI-L-*`, `OI-M-*`, `OI-O-*`, `OI-P-*`, `OI-R-*`, `OI-X-*`, `OI-Y-*`, and R4's `OI-R4-*` carried in Appendix J) plus four R4 items referenced by phases (`OI-R4-04`, `-05`, `-08`, `-09`) — **346 IDs** (338 at compilation; `OI-B-01`…`04`, `OI-R-08` and `OI-Y-09`…`11` added at registry review G4, 25 Oct 2026). Duplicates are merged into one row; every ID appears once. Appendices A, C, D, E, N, Q, S, T, U, V, Z declare no `OI-` rows (Appendix B declares `OI-B-01`…`04` in §B.7); their open facts are in W.3. **Owner** uses `[OWNER]`, `[COUNSEL]`, `[TAX MEMO]` or the accountable team/role. **Due by** is the phase exit (and wave) that the item blocks. **Status** is `OPEN` unless stated; items settled by a cross-file resolution are marked `RESOLVED (X-nn)` and close formally at the wave's P23 run.

### W.4.1 Ecosystem, companion packs and Operations Hub

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-P00-09, OI-P19-01, OI-Y-01, OI-X-10, OI-P18-09 | Approval of Appendix Y (Spec v1.2): owner code `LD`, `TenantProvisioned` consumer, LawDocs-originated subjects, new OH contracts | [OWNER] + Spec owner | Cross-product events; manual interim channel, logged | P19 core (W1) | Y |
| OI-P07-03, OI-P11-07, OI-P13-01, OI-P14-10, OI-P21-05, OI-P01-12, OI-Y-09, OI-Y-10 | Specific Y items: `ADRReferralCreated`, agreement-executed summary, legal-domain projections to LDC, governance facts and `SystemOfRecordSwitched`, LDC service-order status, OH CRM/ticket/asset APIs (OH7 asset-library upload path and OH3 `crm/leads` field set for LawDocs as caller — OI-Y-10), token-exchange sign-in (acceptance by LDC, Finbyx and Udofin identity owners; Part 4.4 token lifetime and pairwise-subject parameters — OI-Y-09) and `PARTNER_ONBOARDING_PREFILL` | Pack lead / Spec owner; OH owner (OI-Y-10); identity owners (OI-Y-09) | Respective `int` contracts OFF; REST polling; customer's own enterprise IdP federated into both products, otherwise separate sign-in (OI-Y-09); manual asset download/upload by `OPS_CONTENT_PUBLISHER` and `POST /v1/crm/requests` only (OI-Y-10) | P19 full (W2) | Y; X-11 settles duplicate SoR keys in OI-P13-01 |
| OI-P09-07, OI-P19-09 | A2A agent-task contracts across products | Group architecture board | Ecosystem events only | W3 | V-120 |
| OI-P20-01, OI-K-01, OI-Y-07 | Archive profiles `ld_professional_v1`, `ld_consumer_help_v1`; `owner_readable` naming mode acceptance | [OWNER] / archive owners | `ids_only` for cross-product archives | P20 full (W2) | X-07, X-08 |
| OI-I-12, OI-P23-04, OI-Y-06, OI-B-02 | Spec domain names for engineering and security-incident events (including the domain segment for `ReleasePublished` / `ControlEvidenceCollected` and the incident-notification event name, Appendix B §B.4); kernel export schema versions | Integration lead / kernel maintainers | Use Spec v1.1 names verbatim; archive-standard export | P19, P23 | V-119 |
| OI-B-04, OI-Y-11 | Appendix Y registration of the Operations Hub addendum (`ops`) events raised by P18 and Appendix X, and the domain for `ServiceOrderRouted` / `ServiceOrderStatusChanged` (`ops` vs a new `engagement`-domain event; Appendix B §B.4.5) | Spec owner + LDC and OH owners | Events not published; manual interim order-status updates by the delivery lead | P18, P19 (W2) | Y |
| OI-P11-01, OI-P19-05, OI-Y-05 | LDC P26 legal-matter/CLM overlap with D-10; LDC v1.3 alignment | [OWNER] + LDC pack lead | `lit.sor.mode`, `legal_sor_link` per organisation | P11 (W2) | X-06 |
| OI-X-05 | Single client vault when LDC is present | [OWNER] + LDC product head | LawDocs `cvl` disabled for LDC-connected tenants | P18 (W2) | — |
| OI-P13-02 | Governance/HRMS kernel extension points for `lgo` (no fork) | Architecture lead | Extension tables only | P13 (W2) | NN-47 |
| OI-P13-10 | LawDocs-only listed companies: disclosure scope vs LDC | [OWNER] | Recommend LDC | P13 | — |
| OI-P19-11 | Equator clause API endpoint and model-clause licence | EQ lead | Manual reviewed import | P19 full | V-119 |
| OI-P15-09 | OH1.6 extension: `chp` machine client, HMAC epoch keys, response schema | Pack lead / OH | Manual conflict declaration | P15 (W3) | — |
| OI-P19-04, OI-Y-04 | Consumer Help conflict-check API and policy when respondent is a group client | [COUNSEL] + OH lead | Decline intake; signpost official routes | P15 (W3) | X-26 |
| OI-P01-08 | OH9 readiness for professional applications | Spec owner | LOCAL onboarding desk | P01 (W1) | — |
| OI-P02-04 | OH group-grant SCIM attributes for LawDocs roles; `AccessReviewCompleted` | Spec owner | Manual provisioning with maker-checker | P02 (W1) | X |
| OI-P17-01, OI-X-03 | OH8 live date vs P17 sprint 3; LOCAL billing adapter | [OWNER] + OH lead / CTO | LOCAL adapter behind flag, or Free tier only | P17 (W1) | — |
| OI-P17-08, OI-L-06 | New OH8 stream types and meters (CREDIT_PACK, MARKETPLACE_PLATFORM_FEE, RETAINER, REFERRAL_CREDIT, AFFILIATE, PARTNER_RESALE); `UsageRecorded` producer | OH lead | Nearest existing stream type | P17 (W1) | X, Y |
| OI-P18-02 | Group IdP and SCIM source for LawDocs staff | CTO / OH12 | Manual provisioning with maker-checker | P18 (W2) | — |
| OI-P22-08 | Native OH "ops approvals" space | Pack lead / OH owner | Web approvals | P22 (W2) | X |
| OI-P23-07 | OH13/OH14 availability for LawDocs onboarding | OH programme | Local `eng` SoR with back-fill | P23 | — |
| OI-X-02 | Production-grade Free/Personal accounts and Business trials vs OH8.9 | [OWNER] + OH product head | Business trials as sandboxes | P17 (W1) | — |
| OI-X-07 | Grievance ownership split: LawDocs desk vs OH6 mirror | [OWNER] + [COUNSEL] | LawDocs desk owns all user grievances | P21 core | LG-077 |
| OI-P19-03, OI-Y-03 | B2C billing identity to OH8 (`CONTRACT_PERFORMANCE_CUSTOMER`, PII ceiling) | [OWNER] + `PLT_DPO` + [TAX MEMO] | LawDocs issues B2C invoices itself (deviation from D-11) | P17 (W1) | X-13; TM-12 |

### W.4.2 Owner decisions — product, commercial, brand and entity

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-X-01 | One or two LawDocs selling entities (SaaS vs services) | [OWNER] / CS | Single entity, two invoice series | P17 (W1) | D-08 |
| OI-P15-01, OI-X-09, OI-P21-04 | Consumer Help entity: incorporate, name, domain, board COI policy, annual wall review | [OWNER] | `chp.brand.enabled` OFF | P15 (W3) | D-06, NN-23 |
| OI-P00-05 | Legacy "LawDocs Coins"/wallet/referral balances | [OWNER] | Honour as credits | P00 | — |
| OI-P00-06, OI-P21-02 | AI training-bot and `Google-Extended` policy | [OWNER] (board) | Block training bots | P21 core | NN-31 |
| OI-P00-12, OI-P21-01 | Single public phone number and contact identity | [OWNER] | Email-only contact | P21 core | — |
| OI-P00-07 | PayU dispute/chargeback window and account closure | [OWNER] with PayU | Keep account for refunds only | P00 | V-125 |
| OI-P02-01 | Solo-owner reading of NN-18 for one-person company tenants | Pack lead / [OWNER] | Cooling-off + notification | P02 (W1) | NN-18 |
| OI-P02-06 | Seat classes by role (FULL/LIGHT/FREE_GUEST) | [OWNER] with P17 | Seeds | P17 | — |
| OI-P03-04, OI-R-01 | Plan limits `[OWNER TO SET]` (custom fields, item types, sandboxes, templates) | [OWNER] with P17 | R6 seeds | P17 | App R |
| OI-P04-07 | Storage quotas and overage price | [OWNER] | Seeds | P17 | — |
| OI-P06-03 | Free clean-export quota and export price | [OWNER] | Watermarked export only | P06 (W1) | — |
| OI-P06-05 | Variant model for near-duplicate templates | [OWNER] | Keep separate | P06 | App E |
| OI-P02-05, OI-P07-04 | Default DoA templates for SMEs and NBFC clients aligned with LDC | [OWNER] / P13 / LDC owner | Generic DoA | P07 (W1) | NN-47 |
| OI-P08-12 | eSign/eStamp credit prices and plan allowances | [OWNER] | Seeds | P08 (W1) | App L |
| OI-P10-05 | Content-gap drafts commissioning; writ skeleton scope (advocate-only) | [OWNER] | Gap pages hidden | P10 (W2) | App E §4.3 |
| OI-P15-04 | Fleet challan subscription: entity placement and lawful data source | [OWNER] [VERIFY] | OFF | P15 (W3) | V-113 |
| OI-P15-05 | Escrow partner for vehicle sales or party-to-party only | [OWNER] | Party-to-party | P15 | LG-187 |
| OI-P15-08 | Comparator set ("ChallanWallah" vs challanwala.com) | [OWNER] | Neutral copy | P15 | — |
| OI-P16-07 | FinLegal Academy brand clean-up on live site | [OWNER] | `aca.display_name` | P16 (W2) | — |
| OI-P16-11 | Deemed acceptance, refund timelines, SLA credits, click-wrap threshold | [OWNER] | `[OWNER TO SET]` defaults | P16 | — |
| OI-P17-02, OI-L-01, OI-M-06 | Final price points, rounding, GST-inclusive B2C display; marketplace row prices | [OWNER] | R6 seeds | P17, P16 | App L, M |
| OI-L-07, OI-O-03 | Refund windows RF-01…RF-09 incl. first-purchase window; Academy refunds | [OWNER] + [COUNSEL] | 7-day first-purchase window | P17 | App O |
| OI-O-02 | Consumer liability cap and data-breach super-cap | [OWNER] + [COUNSEL] | Higher of 12 months' fees and ₹[amount]; 2× for business | P21 (policies) | LG-220 |
| OI-O-04 | Milestone deemed-acceptance period | [OWNER] | 5 business days after two reminders | P16 | — |
| OI-O-06 | Consumer Help withdrawal refund scale | [OWNER] | 50% of current stage if nothing filed | P15 | — |
| OI-O-07 | Seat city for arbitration and court jurisdiction | [OWNER] | Placeholder blocks publication of terms | P21 core (W1) | — |
| OI-P20-06 | Price and plan placement of `LD-ADD-BYO` | [OWNER] | Business add-on; Enterprise included | P20 | — |
| OI-P21-03 | Blog Word-file folder list and category mapping | [OWNER] | Import paused | P21 | — |
| OI-P22-01 | Bundle/application IDs, developer accounts, D-U-N-S | [OWNER] | Store submission blocked | P22 (W2) | LG-451 |
| OI-P22-06 | Store category and age rating | [OWNER] | Business; 18+ | P22 | — |
| OI-P04-05, OI-P18-03, OI-X-04 | Actual Microsoft 365 SKU held (CH-29); Intune availability | [OWNER] | Design for Business Standard without Intune | P04 (W1) | CH-29 |
| OI-P17-07 | Time-and-motion study to replace seed activity baselines | Product + ops | "Default estimate" labels | P17 | NN-36 |
| OI-L-02 | Court-data refresh allowances per plan and provider cost | [OWNER] + integration lead | Manual refresh only | P11 (W2) | — |

### W.4.3 Legal and counsel items

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-P00-03 | Migration to a new operating entity: fresh consent or notice | [COUNSEL] | Notice-based migration | P00 | CQ-01 |
| OI-P00-04 | Legacy chatbot logs and leads: disposition and retention | [OWNER] + `PLT_DPO` + [COUNSEL] | Quarantine, no reuse | P00 | CQ-02 |
| OI-P01-07, OI-M-05 | Professional verification sources (Bar Council rolls, ICAI/ICSI, IP India agents): access terms; COP Rules citation | [COUNSEL] / OH9 lead | Manual officer verification with evidence hash | P01, P16 | V-091, CQ-03 |
| OI-P01-09 | Acceptable guardianship and incapacity evidence (DPDP rr.10–11) | [COUNSEL] | Guardian flows OFF | P01 | V-017 |
| OI-P01-10, OI-P04-02 | Nominee release wording vs succession law; DPDP s.14 procedure | [COUNSEL] / `PLT_DPO` | Nominee release after verified documents only | P04 (W1) | V-021, CQ-04 |
| OI-P01-11 | Consumer Help as a separate fiduciary: account-sharing model | [COUNSEL] | Separate accounts | P15 | CQ-05 |
| OI-P01-13 | DigiLocker as a sign-in option | [OWNER] | Kept out (NN-03); revisit by ADR + counsel | — | RESOLVED (NN-03) |
| OI-P02-02 | Professional record-keeping vs client data ownership in firm workspaces | [COUNSEL] | Client owns; professional copy by engagement terms | P02 | CQ-06 |
| OI-P02-03 | Related-party and board-approval triggers for DoA flags (s.188) | P13 / [COUNSEL] | Advisory flag | P13 | LG-159 |
| OI-P03-05, OI-P09-04 | One confirmation of an itemised, bounded send plan satisfies NN-13 | [OWNER] + [COUNSEL] | `agt.send_plan.mode` `itemised_confirmation` (X-04) else per message | P03, P09 | X-04, CQ-07 |
| OI-P04-01 | Mask-before-commit adequacy for evidence containing Aadhaar | [COUNSEL] / `PLT_LEGAL_REVIEWER` | Masked rendition + pre-mask hash only (X-14) | P04 (W1) | X-14, CQ-08 |
| OI-P05-03 | Per-forum translation certification rules | [COUNSEL] / P10 | Certified-translation service route | P10 | V-031 |
| OI-P05-04 | Masking non-party phone numbers in chat type copies for filing | [COUNSEL] | Mask by default, unmask on reason | P05 (W2) | CQ-09 |
| OI-P05-01, OI-P05-09, OI-P08-04, OI-P20-03, OI-K-02, OI-Y-08 | BSA s.63(4) Schedule wording; who signs Part A for platform records; Part B expert criteria; *Pune Bar* citation | `PLT_LEGAL_REVIEWER` / [COUNSEL] | `sgn.bsa63.enabled`, `dix.bsa63.enabled` OFF; drafts "for review by your advocate" | P08 (W1) | V-009, CQ-10 |
| OI-P06-01, OI-P09-02, OI-R4-05 | Anthropic confirmation that template-lane AI pre-fill and fact extraction are outside the high-risk legal definition | [OWNER] + [COUNSEL] | `drf.template.ai_prefill.individuals` OFF | P06 (W1) | V-029 |
| OI-H-01, OI-R-07 | Final Anthropic Usage Policy text (12 Nov 2026) and per-agent AUP classes; `drf.ai_custom.individual_delivery_mode` | [OWNER] + [COUNSEL] | Treat individual-facing drafts as high-risk; `labelled_draft` + paid review | P09 (W1) | V-029, LG-450 |
| OI-P06-02 | In-app viewing and watermarked download of unreviewed AI drafts by individuals | [COUNSEL] | View-only | P06 | CQ-11 |
| OI-P06-04 | Agreements to sell/conveyance eSign rows after Entry 5 omission; State e-registration routing | P08 owner / [COUNSEL] | App F §9 governs | P08 | RESOLVED (X-02) — counsel confirmation pending |
| OI-P07-06 | Retention of abandoned negotiation data | `PLT_DPO` / [COUNSEL] | 3 years after last activity | P07 | V-118 |
| OI-P08-03 | Physical stamp paper with an electronically signed instrument; e-SBTR/GRAS proofs | [COUNSEL] | Procure e-stamp; physical paper → wet ink | P08 (W1) | V-052, CQ-12 |
| OI-P08-05 | White-label eSign for B2B tenants (RS-LD-17) vs no sub-letting | [COUNSEL] / ESP contract | LawDocs-branded hosted ceremony only | P08 | LG-007, CQ-13 |
| OI-P08-09, OI-F-03 | Adequacy of electronic/remote witnessing where attestation is required (TPA s.3) | [COUNSEL] | Wet-ink attestation | P08 (W1) | LG-283, CQ-14 |
| OI-P09-03, OI-H-05 | Reviewer-eligibility matrix (reserved vs non-reserved classes; employed professionals, BCI r.49) | [COUNSEL] | Practising advocates only | P09 (W1) | CQ-15 |
| OI-P09-10 | Privacy basis for sampled human review of free-tier answers | [COUNSEL] / `PLT_DPO` | Consented, de-identified items only | P09 | CQ-16 |
| OI-P10-06 | Party-in-person support boundaries for LawDocs staff | [COUNSEL] | Platform-mechanics help only | P10 (W2) | CQ-17 |
| OI-P11-02 | Platform vs client eligibility for eCourts Open APIs | Integration lead + [COUNSEL] | Adapter OFF | P11 (W2) | V-034 |
| OI-P11-08 | Internal counsel scorecards vs BCI Rule 36 | [COUNSEL] | Hidden by default | P11 | LG-111 |
| OI-P12-03, OI-I-05 | WIPO Global Brand Database reuse terms or licensed partner; TM Journal partner | Integration lead + [COUNSEL] | Own-portfolio screening; manual tracking | P12 (W2) | V-107 |
| OI-P12-04 | IP India website terms for automated Journal retrieval | [COUNSEL] | Manual upload | P12 | V-107 |
| OI-P12-07 | `TRADE_MARKS_AGENT`/`PATENT_AGENT` sub-types; marketplace rules for agents | App D/M owners + [COUNSEL] | Treat as regulated; listing OFF | P12, P16 | V-095 |
| OI-P13-06 | Managed Legal Department retainer structure (advocates' firm, invoicing) | [COUNSEL] + [TAX MEMO] | RS-LD-21 OFF | P13 (W2) | CQ-18, TM-11 |
| OI-P13-07 | DPDP basis for employee processing and employee notice | `PLT_DPO` + [COUNSEL] | Consent-based notice | P13 | V-019 |
| OI-P14-03 | Affiliated CA/CS/advocate firm delivering attest/certification services by direct engagement | [COUNSEL] | Independent practitioners engaged directly | P14 (W3) | CQ-19 |
| OI-P14-09 | DSC-handling authority letter wording | [COUNSEL] | DSC never held by LawDocs | P14 | NN-16 |
| OI-P15-02, OI-O-05 | Success fee (champerty, unfair terms, CCPA) and flat-fee case-management boundary | [COUNSEL] + [OWNER] | Success-fee switch OFF, Locked | P15 (W3) | LG-281, LG-460, CQ-20 |
| OI-P15-03 | CMS acceptance of eSigned authorisation; consumer-commission agent authorisation form | [VERIFY] | Wet-signed authority letter | P15 | V-076, V-088 |
| OI-P16-01, OI-X-06 | LawDocs Panel structure: affiliated advocates' firm vs contracted panel; invoicing with RCM | [OWNER] + [COUNSEL] | `mkp.model.m2.enabled` OFF; M1 non-reserved only | P16 (W2) | X-21, CQ-21 |
| OI-P16-02 | Assigned-professional model, buyer-side platform fee, published panel prices, Route collection of advocates' fees vs BCI r.36/r.37; *Sulekha* status | [COUNSEL] | M2 OFF; directory OFF | P16 (W2) | X-19, V-093, CQ-22 |
| OI-P16-03, OI-M-02 | DOCUMENTATION vs practice of law (*A.K. Balaji*); classification of SVC rows | [COUNSEL] | Bespoke drafting via panel | P16 | CQ-23 |
| OI-P16-05 | ICAI/ICSI/ICMAI current positions; CA/CS switches | [COUNSEL] | Locked OFF | P16 | V-094 |
| OI-P16-09, OI-P01-14 | E-Commerce Rules 2020 sub-rules and any 2026 amendment; current IT Rules grievance timelines | [COUNSEL] [VERIFY] | Adopt duties as policy; stricter clocks | P16, P21 | V-089, V-024 |
| OI-P16-10 | Trade Marks Act s.145 agent rules for platform listing | [COUNSEL] [VERIFY] | TM filings by panel advocates | P16 | V-095 |
| OI-P18-01 | Portal terms on sharing RBI CIMS/DAKSH/PRAVAAH, FIU-IND, CIC and CERSAI credentials | [COUNSEL] + client compliance | Client-only default + acknowledgement | P18 (W2) | LG-126, CQ-24 |
| OI-P18-06 | Whether LawDocs-employed advocates/CAs may issue work product in their professional capacity | [COUNSEL] | Company work product for non-reserved services | P18 | NN-41, CQ-25 |
| OI-P18-07 | Non-advocate case managers as RBIO authorised representatives | [OWNER] + [COUNSEL] | User self-files with LawDocs drafting | P15, P18 | LG-173, CQ-26 |
| OI-P18-10 | Outsourcing-register entry format for RE clients without LDC | [COUNSEL] | Downloadable record only | P18 | LG-188 |
| OI-P19-02, OI-Y-02 | ESP/aggregator confirmation that API-initiated, LawDocs-hosted ceremonies for a customer's own documents are within ASP terms | [COUNSEL] + procurement | `int.esign.api_initiation.enabled` OFF; UI-only signing | P19 core (W1) | X-05, LG-007, CQ-27 |
| OI-P19-06, OI-I-03 | Court-data aggregator contracts (two) with lawful-collection warranties, NCLT/DRT/e-Jagriti coverage, no-resale | Procurement + [COUNSEL] | Manual CNR | P11 (W2) | V-036, VC-11 |
| OI-P21-09 | Cookieless aggregate analytics under DPDP; "English prevails" clause for translated policies | [COUNSEL] | Consent-gated analytics | P21 core | CQ-28 |
| OI-F-04 | Vakalatnama as a POA under First Schedule entry 2; e-vakalatnama per forum | [COUNSEL] / P10 | Wet-ink vakalatnama | P10 | LG-003, CQ-29 |
| OI-F-05 | Public/religious trusts and wakf formalities; donation-to-trust treatment | [COUNSEL] | Conservative wet ink | P08 | LG-287, LG-293 |
| OI-F-07 | SH-4 electronic execution practice; duty collection on securities transfers | [COUNSEL] / `PLT_LEGAL_REVIEWER` | `FORUM_RULES`, wet ink default | P13, P14 | V-063 |
| OI-F-09 | Family settlement memoranda: registration test and citation | [COUNSEL] | Registration recommended | P08 | V-059 |
| OI-M-01 | Appendix M §M.9 templates and panel agreement | [COUNSEL] | M1-only services live | P16 | — |
| OI-M-03 | RESERVED_AGENT supply by LawDocs employees (GST practitioners, ERI) | [COUNSEL] + P14 | GSTP/ERI rows OFF | P14 | V-098 |
| OI-O-01, OI-P-07 | Fiduciary/processor characterisation of the marketplace workspace and of counterparty data | [COUNSEL] + `PLT_DPO` | LawDocs processor; partner independent fiduciary | P16, P21 | LG-072, CQ-30 |
| OI-O-08 | Security researcher safe-harbour wording | [COUNSEL] | Contractual undertaking only | P23 | — |
| OI-O-09 | GDPR Art. 27 representative | `PLT_DPO` | Not appointed; EU supplement OFF | — | LG-084 |
| OI-P-03 | DPDP acceleration status and Rule 13 SDF content before launch | [COUNSEL] | Build to full regime | P23 (W1) | V-018, V-023 |
| OI-P-04 | OVSE incident and surrender obligations (2025 amendment) | [COUNSEL] | Runbook placeholder | P01 Phase 2 | V-012 |
| OI-J-01 | Counterparty signing invitation as a TCCCPR "service" message | [COUNSEL] / compliance | Email + initiator's own share sheet only | P19 (W1) | V-114, CQ-31 |
| OI-J-02 | Human-initiated click-to-call through CPaaS outside "A2P" (Reg. 2(ea)) | Compliance with TSP | Declare C2C CLIs as A2P | P19 | V-114 |
| OI-J-03 | DCA availability for non-bank principal entities | Compliance | Consent captured and evidenced in LawDocs | P19 | V-114 |
| OI-P01-02 | UIDAI secure-QR specification; OVSE Reg 13A registration (fees, documents, Class 3 certificate) | [OWNER] + [COUNSEL] | QR flag OFF until spec verified; AVC Phase 2 | P01 (W1) | V-012, V-013 |
| OI-P01-06 | Vendor PAN API warranty or DigiLocker PAN only | [OWNER] + [COUNSEL] | DigiLocker PAN + format validation | P01 | LG-047, VC-07 |

### W.4.4 Tax-memo items

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-P00-08, OI-P20-07 | GST record retention (CGST s.36) and Companies Act s.128(5) for LawDocs' own archive; income-tax equivalents | [TAX MEMO] | 8 years | P00, P20 | TM-01 |
| OI-P08-08, OI-P14-04 | Pure-agent treatment of stamp duty and government fees; PA position for `PURE_AGENT_REIMBURSE` | [TAX MEMO] | Vendor-direct payment; pure-agent collection OFF (X-18) | P08 (W1) | TM-02 |
| OI-P11-06 | TDS section for professional fees under the Income-tax Act 2025 | [TAX MEMO] | Field captured; advisory validation | P11 | TM-07 |
| OI-P16-04 | SAC per class, ECO registration, s.52 TCS exclusion of RCM/exempt, s.393(1) Sl. 8(v) TDS, pure-agent duty lines | [TAX MEMO] | M2 OFF until signed | P16 (W2) | TM-03…TM-06 |
| OI-P17-03 | Credits as vouchers: PPI/closed-system analysis, time of supply, breakage, revenue recognition | [COUNSEL] + [TAX MEMO] | Credits limited to LawDocs services; refundable rule | P17 (W1) | TM-08 |
| OI-P17-04 | SAC per SKU (SaaS, facilitation, platform fee); TDS characterisation guidance for buyers | [TAX MEMO] | "18% — confirmed on invoice" hint | P17 (W1) | TM-04, TM-07 |
| OI-P22-02 | Digital sales mode on iOS/Android and GST on store sales | [OWNER] + [TAX MEMO] | `NOT_SOLD_IN_APP` / web hand-off | P22 (W2) | TM-10 |
| OI-P23-08 | ITR due dates under the Income-tax Act 2025 for release-freeze planning | [TAX MEMO] | Freeze set yearly by CAB | P23 | V-097 |
| OI-K-06, OI-P14-11 | Tax-year label under the Income-tax Act 2025 for `09 Tax/` | [TAX MEMO] / pack lead | "Tax Year YYYY-YY" + legacy AY alias | P20 | RESOLVED (X-12) — memo confirms terminology |
| OI-L-05 | Tax memo TX-01…TX-14 (Appendix L §L.13.1) | CFO + tax adviser | Tax hints "confirmed on invoice" | P17 (W1) | W.6 |

### W.4.5 Verification-type items (linked to W.3)

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-P01-03, OI-P04-03, OI-P20-05 | NeGD written position on retained DigiLocker copies, onward display and permitted retention purposes; Requester onboarding | `PLT_DPO` + [OWNER] with NeGD | URI + verification result only; reference-only exports | P01 (W1) | V-015 |
| OI-P01-04, OI-P19-12 | Entity Locker requester API eligibility, terms and coverage | P01 lead | Licensed MCA vendor + upload | P01 | V-016 |
| OI-P03-02, OI-P08-11, OI-F-02 | State stamp-duty tables, registration thresholds and e-stamp channels for launch States; vendor coverage letters | `PLT_LEGAL_REVIEWER` / P08 | Rows `SECONDARY_ONLY` → indicative; manual stamp route | P08 (W1) | V-043, V-044 |
| OI-P03-03, OI-R-03 | RB-IOS 2026 clause numbers for RE wait and filing windows; Insurance Ombudsman window | P15 content | Advisory clocks labelled | P15 (W3) | V-072, V-086 |
| OI-P03-06, OI-R-02 | TCCCPR 2026 calling windows, pre-declared numbers and AI-voice disclosure (`IN.ntf.tcccpr`) | P19 | Voice channel OFF | P19 | V-114 |
| OI-P04-08, OI-B-01 | Retention floors marked `[VERIFY]` (income-tax 2025 Act, labour records, registers); counsel/DPO confirmation of the Appendix B §B.6.2 floors `TAX_8Y`, `EMPLOYEE_RECORDS`, `CHP_CASE`, `OPS_10Y` and the minutes/register rule numbers | `PLT_LEGAL_REVIEWER` + `PLT_DPO` / [COUNSEL] | Longest plausible floor | P04 (W1) | V-118 |
| OI-P05-06 | Licensing of Legislative Department glossaries and authoritative Hindi texts | `PLT_CONTENT_EDITOR` | Own glossary | P05 | V-123 |
| OI-P05-07 | WhatsApp export limits and advanced chat privacy behaviour | QA (device test) | Screenshots route | P05 | V-123 |
| OI-P06-06 | State variant priority list (top 10) and Model Tenancy Act adoption list | `PLT_LEGAL_REVIEWER` | National variant with State warning | P06 (W1) | V-048 |
| OI-P07-01, OI-P07-02, OI-P18-04, OI-P20-02, OI-I-06, OI-K-03 | Graph delegated permissions and `Sites.Selected` consent; Teams app publishing; Google `drive.file`; tracked-change round-trip; upload limits; naming/path limits | Integration lead | Plain links; download/upload; stricter naming rules | P07 (W1), P20 | V-121 |
| OI-P08-02, OI-P-05 | Capricorn and Protean CCA licence renewal evidence at signing go-live | `PLT_SECURITY_OFFICER` / P08 tech lead | ESP blocked (X-16) | P08 (W1) | V-002 |
| OI-P08-07 | Face-authentication eSign availability and legal basis | `PLT_LEGAL_REVIEWER` | Method OFF | P08 | V-005 |
| OI-P08-10, OI-F-06 | State e-registration acceptance of eSigned instruments | `PLT_LEGAL_REVIEWER` | Wet-ink registration route | P08 (W1) | V-045 |
| OI-P10-01, OI-P11-10 | Render profiles for six HCs and top-10 States' district courts; forum filing-size limits | `PLT_LEGAL_REVIEWER` / legal analyst | "Indian courts — A4 general"; warning only | P10, P11 (W2) | V-030 |
| OI-P10-02, OI-P11-04 | Limitation and clock seed rows (Limitation Act articles, s.166(3) MV Act, Insurance Ombudsman, ITA 2025 appeal, GSTAT) | `PLT_LEGAL_REVIEWER` | Advisory badge | P10, P11 | V-032, V-033 |
| OI-P10-03 | Court Fees Act schedules by State (top 10 first) | `PLT_LEGAL_REVIEWER` | "Confirm with the court/advocate" | P10 | V-043, LG-247 |
| OI-P10-07 | e-Daakhil vs e-Jagriti state and file limits | P15 owner | Generic upload guidance | P10, P15 | V-088 |
| OI-P10-08 | BNS s.358 / BNSS s.531 savings and transition text | `PLT_LEGAL_REVIEWER` | Toggle hidden | P10 | V-035 |
| OI-P11-05 | Ind AS 37 / AS 29 paragraphs and Schedule III Division mapping | CA reviewer | Text without paragraph numbers | P11 | V-069 |
| OI-P11-09, OI-K-04 | CNR structure and QR content; TM application and eStamp certificate number formats | Product analyst / P11, P12, P08 | Manual entry; import patterns disabled | P11, P20 | V-034, V-104, V-052 |
| OI-P12-01, OI-R-05 | Deadline seeds (Trade Marks Act/Rules 2017 timelines incl. Appendix R pack; Copyright, Designs, Patents rules as amended 2024) | IP domain analyst | Advisory badges | P12 (W2) | V-104, V-108 |
| OI-P12-02 | Government fee schedule and applicant categories | IP domain analyst | "As at <date>, to be confirmed by your agent" | P12 | V-105 |
| OI-P13-03 | RBI NBFC Governance Directions title/paragraphs; IT, ALM, fraud-risk committee sources | Regulatory analyst | Overlay ADVISORY | P13 | V-067 |
| OI-P13-04, OI-R-04 | Companies Act thresholds and rule numbers in blueprint seeds; SS-1/SS-2 paras (Appendix R packs); MGT-14 list; MR-1; electronic registers | CS reviewer | Advisory badges | P13 (W2) | V-064, V-065 |
| OI-P14-01 | Every government fee row and form version (48 services) | `PLT_LEGAL_REVIEWER` | Fee shown "to be confirmed" | P14 (W3) | V-071 |
| OI-P14-02 | ERI registration type, eligibility, security audit, API scope; 2025-Act re-notification | [OWNER] + CA | Return filing OFF | P14 (W3) | V-098 |
| OI-P14-06 | Income-tax Act 2025 section map (return, verification, advance tax, audit, charity, startup, AR) | CA reviewer | Dual citation, advisory | P14 | V-097 |
| OI-P14-07 | DPIIT recognition criteria and benefits in force | [VERIFY] | "Subject to separate eligibility" | P14 | V-071 |
| OI-P14-08 | DIR-3 KYC periodicity; INC-20A; C-PACE; LLP Form 24 rule | CS reviewer | Advisory reminders | P14 | V-064, V-066 |
| OI-P15-06 | RBC amendment paragraphs (banks Fourth, NBFC Third, 6 Aug 2026); pre-2027 calling-hours guidance | [VERIFY] | Rules labelled by source date | P15 (W3) | V-074 |
| OI-P15-07 | State data: Virtual Court and physical-court timelines, Lok Adalat rules, vehicle-sale stamp duty, RTO physical-submission States | [VERIFY] per State | Data rows advisory | P15 | V-112, V-043 |
| OI-P15-10 | Licence to reuse RBI-published NBFC/DLA lists | [VERIFY] | Deep link to RBI pages | P15 | V-076 |
| OI-P16-08 | Razorpay Route MCC approval, transfer fee, on-hold limits | Finance [VERIFY] | M2 OFF | P16 | V-081, VC-15 |
| OI-P16-12, OI-P17-06, OI-P22-03, OI-P22-07, OI-P23-05 | Apple/Google store rules for India: services vs digital goods, subscriptions/credits, external links, OTA, AI data-sharing disclosure | Mobile lead [VERIFY] + [COUNSEL] | `bil.mobile.purchase_mode = WEB_HANDOFF`; no OTA beyond bug fixes | P22 (W2) | V-122 |
| OI-P17-05 | e-mandate limits and pre-debit rules; Razorpay plan-change constraints | Finance [VERIFY] | OH8 behaviour | P17 (W1) | V-082 |
| OI-P18-05 | Delegation routes per portal (GST practitioner, income-tax AR/CA, EPFO/ESIC sub-users, MCA professional users) | `PLT_LEGAL_REVIEWER` [VERIFY] | Generic "check the portal" text | P18 | V-100 |
| OI-P20-04 | Companies (Accounts) Rules r.3(5) current text (India back-up of books) | Content team | Treat books as India-only | P20 | V-069 |
| OI-P21-07 | Google FAQ rich-result deprecation, Shorts/Reels limits, YouTube privacy-enhanced mode, AI crawler user agents | SEO lead [VERIFY] | Conservative defaults | P21 | V-124 |
| OI-P21-08 | Plagiarism provider terms and data handling | `PLT_DPO` [VERIFY] | Manual originality review | P21 | V-124 |
| OI-P21-10 | IT Rules grievance and synthetic-media labelling text as amended 20 Feb 2026 for footer and video labels | [VERIFY] / [COUNSEL] | Stricter clocks; labels on all AI media | P21 core (W1) | V-024 |
| OI-P23-02, OI-P-06 | CERT-In 2025 audit guidelines applicability; empanelled auditor selection | `PLT_SECURITY_OFFICER` / [OWNER] | Annual audit regardless | P23 | V-026 |
| OI-P23-03 | ESP contract audit frequency and incident-notice terms | P08 lead | Annual ASP audit [REC] | P23 | V-004 |
| OI-P23-06, OI-P-02 | SAQ A eligibility with acquirer/QSA for Razorpay checkout mode | OH8 owner / [OWNER] | Redirect-only hosted checkout | P23 (W1) | V-083 |
| OI-F-01 | Statute wording cited in Appendix F §1 (TPA, Registration Act, Succession Act, Stamp Act, IT Act, RERA, A&C, IP) | `PLT_LEGAL_REVIEWER` | Rows `SECONDARY_ONLY` | P08 | V-001, V-046, V-054 |
| OI-F-08 | Receipt stamp threshold; electronic receipts; acknowledgement-of-debt article | `PLT_LEGAL_REVIEWER` | `CHECK` rows | P08 | V-062 |
| OI-F-10 | Registration Bill 2025 status | `PLT_LEGAL_REVIEWER` | Draft rows inactive | — | V-050 |
| OI-F-11 | 2023 seven-judge decision on unstamped arbitration agreements | `PLT_LEGAL_REVIEWER` | Note without citation | P08 | V-059, LG-261 |
| OI-R-06 | Registration Act presentation window and State variants for `AGR_REGISTRATION_PENDING` | P08 content | Advisory clock; manual entry | P08 (W1) | V-046 |
| OI-F-12 | Maharashtra leave-and-licence registration and e-registration of eSigned agreements | `PLT_LEGAL_REVIEWER` | Wet-ink/biometric registration route | P08 (W1) | V-047 |
| OI-K-05 | Prescribed layouts of statutory registers | P13 content | Plain register XLSX | P20 | V-064 |
| OI-L-03, OI-R4-08 | Benchmarks BM-11, BM-15, BM-16 re-verification; NyayGPT/LegalKart AI features | Product analyst / research | Excluded from "Money saved"; excluded from public comparisons | P17, P21 | V-129 |
| OI-L-04 | PX-01…PX-12 penalty rows (sections, amounts, periods) | `PLT_LEGAL_REVIEWER` | MODELLED tiles OFF; counts only | P17 | V-064, V-097, V-099, V-104 |
| OI-M-04 | RBIO representation clause and IRDAI routes for Consumer Help copy | P15 [VERIFY] | Generic "check the scheme" copy | P15 | V-072, V-086 |
| OI-P-01 | OWASP ASVS 5.0 chapter numbering and L3 mapping | Security engineer | Map by requirement text | P00 | V-120 |
| OI-P-10 | ISO/IEC 27701 current edition and transition | Readiness assessor | After 27001 | P23 | V-120 |
| OI-H-03, OI-P09-09 | Verified helpline numbers and legal-aid links per State | `PLT_CONTENT_EDITOR` | Show 112 and NALSA only | P09 (W1) | V-038 |
| OI-R4-09 | BCI rule numbers on fee-sharing; ICAI/ICSI rules on commissions to platforms | Legal | Flat-fee model only | P16 | V-091, V-094 |
| OI-R4-02, OI-R4-03, OI-R4-10 | TCCCPR Third Amendment Gazette date; 1600-series for non-BFSI; RCS DLT treatment | Compliance (+ Jio account manager) | Reg. 4 in force from 1 Dec 2026; declared 10-digit CLIs; RCS treated as SMS | P19 | V-114 |

### W.4.6 Technology, vendors and architecture

| OI IDs | Item | Owner | Blocks / fallback | Due by | Link |
|---|---|---|---|---|---|
| OI-P00-01 | Legacy stack facts and regions (Vite/React, Express chatbot, MongoDB Atlas, Railway, PayU) | Tech lead | Treat as non-India; disclose | P00 | V-125 |
| OI-P00-02 | Keycloak import of legacy password hashes | Tech lead | Forced reset | P00 | V-120 |
| OI-P00-10, OI-P-09 | Observability vendor India residency; Brevo and WhatsApp residency findings | Tech lead | Self-hosted LGTM; SES only | P00 | V-124 |
| OI-P00-11 | Temporal self-hosted vs Temporal Cloud residency | Tech lead | Self-host in ap-south-1 | P00 | V-120 |
| OI-P03-01 | ZEN Node binding maturity and licence; CEL JS implementation | CTO (ADR sprint 1) | JSON Logic behind `RULES_PORT` | P03 | V-120 |
| OI-P03-07 | External flag service vs in-house registry | CTO | In-house registry | P03 | — |
| OI-P04-06 | Microsoft CSPP (WOPI) eligibility vs Graph co-edit only | P00 ADR | Graph co-edit | P04 | V-121, LG-453 |
| OI-P04-09, OI-P05-05, OI-P09-01, OI-H-04, OI-P-08, OI-R4-04 | Bedrock India availability of Claude 5.5, vision and embedding models; caching/batch/citations on `in.`; retention; first-party API region | CTO / P09 lead | Opus 5/Sonnet 5/Haiku 4.5 on `in.`; self-hosted embeddings | P09 runtime (W1) | V-028 |
| OI-P09-05 | AWS human review of flagged content on Bedrock; DPA treatment | `PLT_DPO` | Exclude affected models from confidential classes | P09 | V-028 |
| OI-P04-04, OI-P19-10, OI-I-07, OI-R4-01, OI-R4-06, OI-R4-11 | JioCX account, auth/DLR/webhooks, India processing, BSP status, DPA and no-training; Haptik RFP; JioCX Verify coverage on other networks | Procurement / integration lead | Meta Cloud API direct; other DLT aggregator; Truecaller | P19 (W1–W2) | V-115, VC-18 |
| OI-R4-07 | Jio enterprise-AI API commitments | Research | Watch-list | — | V-115 |
| OI-P04-10 | `AGT_DMS_LIBRARIAN` L3 "moves with undo" = metadata/view moves only | Pack lead | Restrict to view moves | P04 | X-27 |
| OI-P05-08 | CER/chrF++ targets per language after first evaluation | Evaluation lead | §1 targets | P05 | — |
| OI-P05-02 | Bhashini terms, retention, residency; Google/Azure India zero-retention | `PLT_DPO` | Claude (Bedrock India) only for confidential | P05 | V-123, VC-20 |
| OI-P06-07, OI-H-02 | Translator panel and native-speaker legal reviewers (Hindi + next languages) | Ops (P16) / `PLT_LEGAL_REVIEWER` | Languages disabled for Vidhi | P06, P09 | — |
| OI-P06-08 | Appendix K `06 Policies and Registers/Contract Templates and Playbooks/` | Appendix K owner | — | — | RESOLVED (X-12) |
| OI-P06-09, OI-H-06 | Vidhi agent names consistent with Appendix H roster | P09 owner / pack lead | Appendix H wins | — | RESOLVED (X-27) |
| OI-P07-05 | WOPI editor licence ADR (ONLYOFFICE/Collabora) | Architecture | Graph/Google co-edit | P07 | — |
| OI-P07-07 | In-browser clause editor component and licence | Frontend lead | ProseMirror/Tiptap-class [REC] | P07 | — |
| OI-P08-01 | Vendor selection ADR: ASP of record, ESP count, residency, log export, price; aggregator vs direct ASP | P00 / [OWNER] | Aggregator first (D-12) | P08 (W1) | V-003, VC-01 |
| OI-I-01 | Aggregator ASP structure and second-ESP rule for Leegality/Digio routes | Procurement + [COUNSEL] | Direct ASP with one ESP + aggregator as second route | P08 (W1) | V-003 |
| OI-P08-06 | Organisation document-signer certificates; customer-held HSM | `PLT_SECURITY_OFFICER` | `sgn.org_seal.enabled` false | P08 | V-006 |
| OI-I-02 | eStamp vendor State coverage and verification APIs; SHCIL corporate channel | Procurement | Physical/franked upload with human UIN check | P08 (W1) | V-044, V-052, VC-03 |
| OI-P09-06 | MCP 2026-07-28 client support among target assistants | Integration lead | Serve 2025-11-25 for 12 months | P09 | V-120 |
| OI-P09-08, OI-P22-05 | Speech vendor bake-off; Indic ASR/TTS with India-resident processing | AI lead / P09 lead | Text-only Vidhi where no vendor passes | P09, P22 | V-123, VC-21 |
| OI-P10-04, OI-I-08 | Postal/courier dispatch partner; India Post bulk API | Ops / P10 lead | Courier APIs; user print-and-post | P10 (W2) | V-040, VC-13 |
| OI-P11-03 | Vendor party-search/new-filing alerts: contract terms, DPDP purpose | CLO advisor + `PLT_DPO` | Party watch OFF | P11 | V-036 |
| OI-P11-11, OI-P13-09 | New ID prefixes (`clk_`, `cnl_`, `lsi_`, `exa_`, `lrq_`; `LD-LRQ-`) | Pack lead | — | — | RESOLVED (X-01) |
| OI-P12-05 | Licensed TM data/watch partner selection | Integration lead | Manual upload | P12 | V-107, VC-12 |
| OI-P12-06 | `11 Trademarks and IP/` in the individual export taxonomy | Appendix K owner | `99 System Data/IP/` | P20 | App K |
| OI-P12-08 | `TRADEMARK_DATA_PORT` capabilities (`AssistedRefresh`, `RegistryMailParser`, optional methods) | Integration lead | Manual entry | — | RESOLVED (X-29) |
| OI-P13-05 | Teams/Google Chat intake app publication | Integration lead | Web/e-mail intake | P13 | V-121 |
| OI-P13-08 | HR role bundles mapped to `ORG_*` codes in Appendix D | Appendix D owner | `ORG_ADMIN` custom roles | P13 | App D |
| OI-P16-06, OI-P19-08, OI-I-09 | Academy checkout (Graphy vs OH8); Graphy API/feed and SSO | [OWNER] + Academy lead | Deep link; curated catalogue import | P16 (W2) | V-126, VC-24 |
| OI-P18-08 | E-mail bridge domain and DMARC alignment | CTO | In-app messaging only | P18 | — |
| OI-P19-07, OI-I-10 | Zapier, Make, Power Automate listing terms and residency | `PLT_DPO` | Webhooks + OpenAPI only | P19 | V-124 |
| OI-P21-06 | Content Studio placement in `apps/console` | Pack lead | — | — | RESOLVED (X-22) |
| OI-P21-11 | ISL interpreters and disabled-user testing panel | `OPS_QA_REVIEWER` | Captions + transcripts only | P21 (W1) | V-117, LG-137 |
| OI-P22-04 | ESP/aggregator mobile support (system browser vs SDK); ESP page accessibility | P08 lead [VERIFY] | System browser | P22 | V-004 |
| OI-P23-01 | GitHub plan and security add-ons pricing | CTO | Compensating controls | P23 | V-120 |
| OI-I-04, OI-P01-05 | KYB/MCA-data vendor contracts, lawful-sourcing warranties, display rights | [OWNER] / procurement | Manual entry with documents | P01 (W1) | V-124, VC-06 |
| OI-P14-05 | GSP selection and taxpayer API-consent flow | [OWNER] | Manual GSTIN + checksum | P14 | V-101, VC-08 |
| OI-I-11 | IETF RateLimit and Idempotency-Key header final status | P19 lead | Keep current headers | P19 | V-120 |
| OI-O-10 | Error range `LD-WEB-090`–`099` and `web.legal.*` keys | Pack lead | As proposed in App O | P21 | X-30 |
| OI-X-08 | Adobe Express scheduling API availability | Marketing ops [VERIFY] | Manual scheduling | OH | V-124 |
| OI-P01-01 | DLT principal-entity registration, headers and OTP templates for the operating entity | [OWNER] | Email OTP only | P01 (W1) | V-114, LG-149 |

| OI-B-03 | Ownership of the `NTF` error range (`LD-NTF-001…099`; 041–045 used by Appendix J): P19 channel adapters vs Appendix J | P19 lead + pack lead | Range as registered in Appendix B §B.5.2 (E-05) | P19 | B §B.5.4 |
| OI-R-08 | Settings naming normalisation found at registry review G4: P18 `wks.*` non-module prefix; P18 kill switches not in `<module>.kill.<target>` form; P11/P12 cite the column `int.connectors.kill_switch_key` instead of `int.kill.<adapter>` | P18, P11, P12 leads | Keys registered as named in Appendix R §R.9.31, §R.9.32, §R.9.32A; aliases if renamed | Next `appendix-r-sync` | R §R.15 |

---

### W.4.7 IPB adoption items (v1.1, 26 October 2026) *(v1.1)*

New open items raised by the Infrabyx Platform Baseline Standard adoption. Each unverified fact ships behind a flag that is OFF or advisory-only (NN-38). Phase-level items (`OI-P03-08…09`, `OI-P09-11…13`, `OI-P19-13…15`, `OI-P20-08…09`, `OI-P21-12…17`, `OI-P23-09…11`, `OI-H-07`, `OI-O-11…12`, `OI-R-09`) are declared in their files and summarised here under group IDs `OI-IPB-nn`.

| OI IDs | Item | Owner | Blocks / fallback (flag) | Due by | Link |
|---|---|---|---|---|---|
| OI-IPB-01, OI-P21-12, OI-O-11 | Investors page: publish for LawDocs; gated documents; IR contact; disclaimer wording [COUNSEL: Companies Act 2013 s.42, s.25–26; SEBI advertisement code] | [OWNER] + [COUNSEL] | `web.investors.enabled` OFF; POL-LD-22 draft | Before Wave 2 content | P21 FR-P21-147; IPB `00_README.md` §7 item 1 |
| OI-IPB-02, OI-P21-13 | Blog contributor programme: eligibility, advocate authorship under BCI Rule 36, moderation staffing, Blog & UGC Terms review | [OWNER] + [COUNSEL] | `web.blog.user_posts.enabled` OFF | Wave 2 | P21 FR-P21-82A/B; POL-LD-19 |
| OI-IPB-03, OI-P09-12, OI-P21-15 | Image-generation provider in ap-south-1 [VERIFY availability]; mandatory human review (pack default yes, locked); IT Rules synthetic-media label text [VERIFY] | AI lead + [OWNER] | `ai.image_gen.provider` unset → feature hidden | Wave 2 | P09 FR-P09-71; P21 FR-P21-80A; IPB §7 item 6 |
| OI-IPB-04, OI-P21-14 | Tag manager: `none` vs server-side GTM vs web GTM; `PLT_DPO` veto | [OWNER] + `PLT_DPO` | `mkt.tag_manager.adapter = none` | Wave 1 go-live | P21 FR-P21-108A; IPB §7 item 5 |
| OI-IPB-05, OI-P19-14, OI-P09-11 | Alternative adapters to contract first (second ESP, second CPaaS, second storage target, second `in_zero` LLM); zero-retention and residency terms of Azure OpenAI, Vertex Gemini, xAI, Sarvam [VERIFY] | [OWNER] + AI lead + `PLT_DPO` | Reference adapters only; contract tests against fakes; other LLMs `PUBLIC` only | P00 plan / Wave 1 | IPB-01 §01.3.C; `02` §4 row 25 |
| OI-IPB-06, OI-P19-13 | Commit the tagged Ecosystem Spec v1.2 under `docs/ecosystem/`; turn on `int.eco.v12_contracts.enabled` after Pact tests with OH v1.1 and LDC v1.3 | Integration lead | Flag OFF; MANUAL_INTERIM channel | P19 core | P19 §7.4; Appendix Y §Y.0 |
| OI-IPB-07, OI-P23-09, OI-P23-10 | OH14.6 Vendor Assurance Room availability and `TRUST_PORT` contract version; standard-answers library; counsel review of framework-preset checklist wording [INTERP] | OH programme + `PLT_SECURITY_OFFICER` + [COUNSEL] | Internal read-only mirror seeded manually; presets as document lists | Wave 1 go-live | P23 FR-P23-60…62 |
| OI-IPB-08, OI-P20-08, OI-P20-09 | Second cloud target to keep green (Azure Central India / GCP asia-south1 / self-hosted) and its Terraform owner; Supabase non-prod project region attestation [VERIFY] | CTO + `PLT_SRE` | AWS reference + MinIO/CloudNativePG drill only; self-hosted PG in non-prod | Wave 2 | P20 FR-P20-52…54 |
| OI-IPB-09, OI-P03-08, OI-P03-09 | NIST SP 800-63B revision and breached-password service for `sec.org.password.*` [VERIFY]; BYOK plan eligibility and key-loss liability wording [COUNSEL] | `PLT_SECURITY_OFFICER` + [OWNER] | Length ≥ 12 + local breach list; BYOK flag OFF | Wave 2 | P03 FR-P03-108 |
| OI-IPB-10, OI-P21-16 | Social profile URLs, office addresses (New Delhi, Noida, Jaipur) and `web.footer.group_url` for the footer | [OWNER] | Seeded placeholders; footer validator warns, CI fails only on mandatory regions | Wave 1 content | P21 FR-P21-16A |
| OI-IPB-11, OI-P21-17, OI-H-07, OI-P09-13, OI-R-09 | Technical migrations: "i" key migration map and alias window; 37 persona-bundle manifests and kernel version pin; shared-package prefix allow-list and §R.14 regeneration | Content engineer + AI lead + pack lead | Old keys as `superseded_by` aliases for one release; Wave-1 agents only | P09 / P21 exits | IPB-07 LD note; Appendix H §H.15; Appendix R OI-R-09 |
| OI-IPB-12, OI-P23-11, OI-O-12, OI-P19-15 | Policy and vendor verifications: beta-programme insert for POL-LD-02; RBI e-mandate pre-debit notice period for POL-LD-18 [VERIFY]; Google/Microsoft calendar scope verification requirements [VERIFY] | [COUNSEL] + Billing lead + Integration lead | Beta OFF; 24-hour pre-debit notice; internal calendar + ICS only | Wave 2 | Appendix O §O.17; P19 FR-P19-85 |

Common-to-all-products items that LawDocs inherits without a LawDocs-specific decision (IPB `00_README.md` §7): white-label resale entity (item 2 — not LawDocs in v1), WhatsApp BSP and Meta verification entity (item 4 — carried as OI-P19 messaging items), Microsoft 365 plan (item 9 — `02` §4 row 1), approval of the eighteen policy templates for counsel (item 10 — OI-O-11).

## W.5 Counsel question list

One written opinion per question (or per cluster), addressed to the owner, filed in `docs/legal/opinions/CQ-nn.pdf` and linked from the verification log and the gated flags. Questions are ordered by the wave they gate. "Gates" names the switch that stays OFF until the opinion is attached and a checker approves (NN-21, NN-38).

| CQ | Question for counsel | OI / V refs | Gates | Wave |
|---|---|---|---|---|
| CQ-01 | Does moving users from the legacy contracting entity to `[LawDocs Operating Entity]` need fresh consent or is notice sufficient? | OI-P00-03 | P00 cut-over | 1 |
| CQ-02 | May legacy chatbot logs and leads be retained or reused, and for how long? | OI-P00-04 | Legacy data import | 1 |
| CQ-03 | Which professional registers may be consulted for verification, on what terms, and is the BCI COP citation correct? | OI-P01-07, OI-M-05; V-091 | Professional onboarding badges | 1 |
| CQ-04 | Is the nominee release model consistent with succession law and DPDP s.14? | OI-P01-10, OI-P04-02; V-021 | `IND_NOMINEE` release | 1 |
| CQ-05 | How should the Consumer Help entity hold accounts as a separate data fiduciary while sharing platform services? | OI-P01-11 | `chp` account model | 3 |
| CQ-06 | In firm workspaces, who owns client records versus the professional's working papers? | OI-P02-02 | Firm workspace exports | 1 |
| CQ-07 | Does one confirmation of an itemised, bounded send plan satisfy NN-13 for reminders and nudges? | OI-P03-05, OI-P09-04; X-04 | `agt.send_plan.mode` | 1 |
| CQ-08 | Is mask-before-commit (masked rendition + pre-mask hash, user keeps the original) adequate for evidence containing Aadhaar numbers? | OI-P04-01; X-14 | Upload masking policy | 1 |
| CQ-09 | Should non-party phone numbers be masked in chat type copies filed in court? | OI-P05-04 | `dix` type-copy default | 2 |
| CQ-10 | BSA s.63(4): who signs Part A for platform-generated records, who qualifies for Part B beyond s.79A examiners, and is the certificate wording correct? | OI-P05-01, OI-P05-09, OI-P08-04, OI-P20-03, OI-K-02, OI-Y-08; V-009 | `sgn.bsa63.enabled`, `dix.bsa63.enabled` | 1 |
| CQ-11 | May individuals view or download watermarked AI drafts not yet reviewed by a professional? | OI-P06-02; V-029 | `drf.ai_custom.unreviewed_download` | 1 |
| CQ-12 | Is a physical stamp paper valid with an electronically signed instrument, and are e-SBTR/GRAS proofs acceptable for electronic instruments? | OI-P08-03; V-052 | Stamp proof types per State | 1 |
| CQ-13 | Can B2B tenants receive white-labelled eSign without sub-letting LawDocs' ASP access? | OI-P08-05; LG-007 | RS-LD-17 | 2 |
| CQ-14 | Where attestation is legally required (TPA s.3), is electronic or remote witnessing adequate? | OI-P08-09, OI-F-03; V-054 | Remote witness feature | 1 |
| CQ-15 | Which document classes need a practising advocate as reviewer, and may employed professionals review non-reserved classes? | OI-P09-03, OI-H-05 | Paid review routing | 1 |
| CQ-16 | What is the lawful basis for sampled human review of free-tier Vidhi answers? | OI-P09-10 | Quality sampling | 1 |
| CQ-17 | What help may LawDocs staff give a party-in-person without practising law? | OI-P10-06 | P10 assisted mode | 2 |
| CQ-18 | How should a Managed Legal Department retainer be structured and invoiced (advocates' firm vs LawDocs)? | OI-P13-06 | RS-LD-21 | 2 |
| CQ-19 | May an affiliated CA/CS/advocate firm deliver attest or certification work to LawDocs customers by direct engagement? | OI-P14-03 | `CERT_PRO_*` services | 3 |
| CQ-20 | Is a capped success fee lawful in the non-advocate Consumer Help entity (champerty, unfair terms, CCPA), and where is the line between case management and practice? | OI-P15-02, OI-O-05; LG-281, LG-460 | Success-fee switch (Locked OFF) | 3 |
| CQ-21 | Which panel structure is lawful: affiliated advocates' firm or contracted panel, and how are advocate bills and the LawDocs platform fee issued? | OI-P16-01, OI-X-06 | `mkp.model.m2.enabled` | 2 |
| CQ-22 | Are the assigned-professional model, buyer-side flat platform fee, published panel prices and Route collection of advocates' fees compatible with BCI Rules 36/37 and the fee-sharing bar, given *Sulekha* is pending? | OI-P16-02; X-19; V-093 | M2; advocate directory | 2 |
| CQ-23 | Where does DOCUMENTATION (bespoke drafting by LawDocs staff) end and practice of law (*A.K. Balaji*) begin, row by row? | OI-P16-03, OI-M-02; V-092 | SVC row classes | 2 |
| CQ-24 | May clients share RBI CIMS/DAKSH/PRAVAAH, FIU-IND, CIC and CERSAI credentials with service providers at all? | OI-P18-01; LG-126 | `cvl` for those portals | 2 |
| CQ-25 | May LawDocs-employed advocates or CAs issue work product in their professional capacity? | OI-P18-06 | Delivery Console sign-off roles | 2 |
| CQ-26 | May non-advocate case managers act as authorised representatives before the RBI Ombudsman, and with what authorisation? | OI-P18-07; LG-173 | Representative service | 3 |
| CQ-27 | Do API-initiated, LawDocs-hosted signing ceremonies for a customer's own documents stay within ASP terms (no sub-letting)? | OI-P19-02, OI-Y-02; X-05 | `int.esign.api_initiation.enabled` | 1 |
| CQ-28 | Is cookieless aggregate analytics permissible without consent under DPDP, and may an "English prevails" clause apply to translated policies? | OI-P21-09 | Analytics mode; policy translations | 1 |
| CQ-29 | Is a vakalatnama a "power of attorney" under First Schedule entry 2, and which forums accept e-vakalatnama? | OI-F-04 | Vakalatnama eSign route | 2 |
| CQ-30 | Is LawDocs processor or fiduciary for the marketplace engagement workspace and for counterparty data in agreements? | OI-O-01, OI-P-07 | DPA and notices | 1 |
| CQ-31 | Is a counterparty signing invitation a TCCCPR "service" message? | OI-J-01; V-114 | SMS/RCS invitations | 1 |
| CQ-32 | Confirm the reading that agreements to sell immovable property are eSign-eligible after Entry 5 was omitted (X-02). | OI-P06-04; V-001 | App F agreement-to-sell rows | 1 |
| CQ-33 | What conflict policy applies when a Consumer Help respondent is a group client? | OI-P19-04, OI-Y-04 | Consumer Help intake | 3 |
| CQ-34 | Do IP India and WIPO terms permit automated Journal retrieval and commercial reuse? | OI-P12-03, OI-P12-04; V-107 | `TM_JOURNAL_PORT` automation | 2 |
| CQ-35 | Is LawDocs (or only the client) eligible for eCourts Open APIs? | OI-P11-02; V-034 | `eCourtsOfficialApi` | 2 |
| CQ-36 | Which E-Commerce Rules 2020 duties (and any 2026 amendment) apply to a services marketplace? | OI-P16-09; V-089 | Marketplace go-live | 2 |
| CQ-37 | What are ICAI, ICSI and ICMAI's current positions on platform listings and fee models? | OI-P16-05, OI-R4-09; V-094 | CA/CS/CMA switches | 2 |
| CQ-38 | What conduct rules apply to non-advocate trade marks agents listed on a platform? | OI-P16-10, OI-P12-07; V-095 | Agent listing | 2 |
| CQ-39 | How far does DPDP s.17(1)(a) cover evidence and case processing? | V-022 | P10/P15 processing basis | 2 |
| CQ-40 | May internal counsel scorecards be shown to company tenants without breaching Rule 36? | OI-P11-08 | Scorecards | 2 |
| CQ-41 | What formalities apply to public/religious trusts and wakf instruments? | OI-F-05; V-056 | Trust/wakf rows | 1 |
| CQ-42 | Can SH-4 be executed electronically, and how is duty on securities transfers collected? | OI-F-07; V-063 | SH-4 rows | 2 |
| CQ-43 | When must a family settlement memorandum be registered? | OI-F-09; V-059 | Settlement rows | 1 |
| CQ-44 | Approve the Appendix M §M.9 templates and the panel agreement. | OI-M-01 | M2 services | 2 |
| CQ-45 | May LawDocs employees enrolled as GST practitioners or acting under LawDocs' ERI deliver reserved-agent services? | OI-M-03; V-098 | GSTP/ERI rows | 3 |
| CQ-46 | Approve security researcher safe-harbour wording. | OI-O-08 | Vulnerability disclosure page | 1 |
| CQ-47 | Has MeitY accelerated DPDP timelines, and what will Rule 13 require of an SDF? | OI-P-03; V-018, V-023 | DPDP effective dates | 1 |
| CQ-48 | What incident and surrender duties attach to OVSE registration? | OI-P-04, OI-P01-02; V-012 | `kyc.ovse.avc.enabled` | 2 |
| CQ-49 | Are the consumer liability cap, refund windows and cancellation parity fair under CPA 2019? | OI-O-02, OI-L-07, OI-O-03 | Terms publication | 1 |
| CQ-50 | Does the grievance split between the LawDocs desk and OH6 meet IT Rules and E-Commerce Rules duties? | OI-X-07 | Grievance routing | 1 |
| CQ-51 | Can the Anthropic Usage Policy high-risk requirements be met by template-lane pre-fill plus labelled drafts and paid review? | OI-P06-01, OI-P09-02, OI-R4-05, OI-H-01, OI-R-07; V-029 | `drf.*` individual delivery modes | 1 |
| CQ-52 | Is a fleet challan subscription lawful given the absence of an official data source, and in which entity? | OI-P15-04; V-113 | Fleet subscription | 3 |

---

## W.6 Tax-memo list

The CFO and the tax adviser sign one memo covering these points before Wave 1 billing go-live (items marked W2/W3 may follow in an addendum). Until signed, invoices and catalogue cards show tax hints labelled "confirmed on your invoice" and the dependent streams stay OFF (Appendix L §L.13.1).

| TM | Question | Refs | Gates | Wave |
|---|---|---|---|---|
| TM-01 | Retention of LawDocs' own GST and income-tax records (CGST s.36; Companies Act s.128(5); ITA 2025) | OI-P00-08, OI-P20-07; LG-128, LG-307 | Retention classes | 1 |
| TM-02 | Pure-agent treatment (CGST r.33) of stamp duty, government, court and registry fees, with Route split or vendor-direct payment; PA position | OI-P08-08, OI-P14-04; LG-345; X-18 | `PURE_AGENT_REIMBURSE`; duty payment route | 1 |
| TM-03 | ECO TCS under CGST s.52 (0.5%, Notification 15/2024-CT): registration, GSTR-8, exclusion of RCM and exempt supplies | OI-P16-04; LG-344; TX-05 | M2 | 2 |
| TM-04 | SAC per SKU for SaaS, credits, facilitation and platform fee; 18% forward charge | OI-P17-04; LG-343; TX-01 | Catalogue tax hints | 1 |
| TM-05 | RCM on advocates' services to business entities and exemption for individuals; invoices in the advocate's name; self-billing limits | LG-340, LG-341; TX-02, TX-03 | Panel invoicing | 2 |
| TM-06 | ECO TDS under ITA 2025 s.393(1) Table Sl. 8(v) on M2 payouts; thresholds and statements | OI-P16-04; LG-352; TX-06 | M2 payouts | 2 |
| TM-07 | TDS characterisation of LawDocs fees for business buyers (technical vs professional, Sl. 6(iii).D); TDS section for professional fees in matters | OI-P17-04, OI-P11-06; LG-353; TX-07 | Settings → Tax documents; P11 fields | 1 |
| TM-08 | Credit packs as vouchers (CGST s.2(118)): time of supply, breakage, refunds, revenue recognition; PPI/closed-system position (with counsel) | OI-P17-03; LG-346; TX-08 | `CREDIT_PACK` stream | 1 |
| TM-09 | E-invoicing threshold per selling entity, place of supply, SEZ/IFSC zero-rating with LUT, credit-note mechanics and time limits | LG-347–LG-349; TX-09–TX-12 | OH8 invoice templates | 1 |
| TM-10 | GST on app-store sales and the digital-sales mode chosen for iOS/Android | OI-P22-02 | `store.<platform>.digital_sales_mode` | 2 |
| TM-11 | Managed Legal Department retainer invoicing between LawDocs and an advocates' firm | OI-P13-06 | RS-LD-21 | 2 |
| TM-12 | B2C invoicing on OH8 under `CONTRACT_PERFORMANCE_CUSTOMER`; invoice identity fields | OI-P19-03, OI-Y-03; X-13 | B2C billing route | 1 |
| TM-13 | Revenue recognition (Ind AS 115 or AS 9) per selling entity | TX-14 | OH8.8 reports | 1 |
| TM-14 | Intra-group licence and service pricing between group entities at arm's length (Companies Act s.188 where applicable) | App X | Group charges | 1 |
| TM-15 | Referral credits, affiliate and partner-resale streams | App L `REFERRAL_CREDIT`, `AFFILIATE`, `PARTNER_RESALE` | Those streams | 2 |
| TM-16 | FinLegal Academy courses sold by the Academy merchant vs OH8 | OI-P16-06 | Academy checkout | 2 |
| TM-17 | "Tax year" terminology and labels under the Income-tax Act 2025 | OI-K-06, OI-P14-11; X-12 | Export folder labels | 1 |

---

## W.7 Vendor-contract list

Each contract is executed through OH procurement with `PLT_DPO` (DPA, sub-processor listing, transfer assessment — NN-25), `PLT_SECURITY_OFFICER` (security schedule, audit rights, incident notice) and, where marked, counsel. No adapter goes ON in production until its contract row is `SIGNED` and its `V-*` items are closed (NN-39 kill switch default per Appendix I).

| VC | Vendor class (candidates) | Port | Terms to secure | Blocks | Refs |
|---|---|---|---|---|---|
| VC-01 | eSign aggregator as ASP route (Leegality → Digio) | `ESIGN_PORT` | ASP of record and structure; two ESP routes within 30 days; consent and logs owned by LawDocs; no sub-letting; log export; India residency; CCA audit cooperation; incident notice; exit and data return; mobile browser flow and page accessibility | Wave 1 signing | OI-P08-01, OI-I-01; V-003, V-004; [COUNSEL] |
| VC-02 | Direct ESP (e.g., Protean, eMudhra) — later direct ASP | `ESIGN_PORT` | ASP agreement, licence-renewal evidence, audit frequency | Direct ASP mode | V-002, V-004 |
| VC-03 | eStamp procurement (Leegality BharatStamp, Surepass e-Stamping, Digio; SHCIL corporate channel/ACC) | `ESTAMP_PORT` | State coverage letters; agent-procurement model; UIN verification API; cancellation and refund; duty pass-through settlement | Wave 1 eStamp | OI-I-02; V-044, V-052 |
| VC-04 | NeSL DDE via aggregator | `NESL_DDE` | Enterprise RE use only; pricing | Optional | V-051 |
| VC-05 | Licensed CA for DSC tokens, organisation signer certificate and RFC 3161 TSA | `DSC_SIGN_PORT`, `TSA_PORT` | Class 3 issuance; TSA SLA; certificate terms | Wave 1 LTV | V-006, V-007 |
| VC-06 | KYB / MCA-data vendors (Probe42, Signzy, Surepass, Perfios-Karza) | `COMPANY_DATA_PORT` | Lawful-sourcing warranty; display rights; residency; processor terms | Company onboarding pre-fill | OI-P01-05, OI-I-04; V-124 |
| VC-07 | PAN verification aggregator (optional) | `PAN_VERIFY_PORT` | Written lawful-upstream warranty | Vendor PAN route | OI-P01-06; LG-047 |
| VC-08 | GSPs (primary and secondary) | `GSTIN_PORT`, `GSP_PORT` | Public search and OTP-consented taxpayer APIs; residency | GSTIN check; GST services | OI-P14-05; V-101 |
| VC-09 | NeGD — DigiLocker Requester and Entity Locker onboarding | `DIGILOCKER_PORT`, `ENTITY_LOCKER_PORT` | Onboarding; written position on retained copies; audit | Wave 1 DigiLocker | OI-P01-03, OI-P01-04; V-015, V-016 |
| VC-10 | UIDAI — OVSE registration | `AADHAAR_OFFLINE_PORT` | Reg 13A registration, Class 3 certificate, surrender duties | AVC (Phase 2) | OI-P01-02; V-012 |
| VC-11 | Court-data aggregators (two; eCourtsIndia API, Surepass eCourts, Claw/Legitquest-type) | `COURT_DATA_PORT` | Lawful-collection warranty; coverage (NCLT, DRT, e-Jagriti); no-resale; residency; "not real-time" wording | Watch lists | OI-P19-06, OI-I-03, OI-P11-03; V-036; [COUNSEL] |
| VC-12 | Trade-mark data and Journal-watch partner; WIPO data licence | `TRADEMARK_DATA_PORT`, `TM_JOURNAL_PORT` | Lawful source; residency; DPDP processor terms; SLA | TM watch | OI-P12-05, OI-I-05; V-107 |
| VC-13 | Postal and courier (India Post CEPT; courier APIs) | `POSTAL_DISPATCH_PORT` | Tracking API; proof-of-delivery artefacts | Notice dispatch | OI-P10-04, OI-I-08; V-040 |
| VC-14 | Notary-facilitation partner network | `NOTARY_FACILITATION` | Appointment SLA; identity checks; fees disclosure | Affidavit packs | LG-106 |
| VC-15 | Razorpay (through OH8): Standard Checkout, Subscriptions, Route, Smart Collect | `BILLING_PORT` | Route MCC approval for legal services; transfer fee; on-hold limits; SAQ A eligibility confirmation; e-mandate behaviour | Payments; M2 | OI-P16-08, OI-P23-06, OI-P17-05; V-081–V-083 |
| VC-16 | AWS (Bedrock India, S3 Object Lock, SES, KMS) | `LLM_PORT`, storage, `EMAIL_PORT` | DPA; India regions; model availability; human-review exception; zero data retention | Wave 1 runtime | OI-P09-05, OI-P-08; V-028 |
| VC-17 | Anthropic API (public, non-personal content only) | `LLM_PORT` | No training; retention; Usage Policy compliance | Public-content tasks | V-029; LG-450 |
| VC-18 | JioCX (SMS, RCS, WhatsApp BSP, voice, Verify) and Jio Haptik | `SMS_PORT`, `RCS_PORT`, `WHATSAPP_PORT`, `VOICE_PORT`, `VOICE_AGENT_PORT` | DPA; India processing; no training; HMAC webhooks; DLR; rate cards; telemarketer binding | Jio adapters | OI-P19-10, OI-I-07, OI-R4-01, OI-R4-06; V-115 |
| VC-19 | Other comms (DLT aggregator/MSG91, Exotel, Meta Cloud API, Brevo, Truecaller for Business) | comms ports | DLT binding; residency; template governance | Fallback channels | OI-P-09; V-124 |
| VC-20 | Translation (Bhashini, Google Cloud Translation, Azure Translator) | `TRANSLATE_PORT` | Terms, retention, residency, zero-retention | Non-confidential MT | OI-P05-02; V-123 |
| VC-21 | Indic speech (Sarvam, Bhashini, others) | `INDIC_SPEECH_PORT` | India-only processing in writing; WER results | Voice features | OI-P09-08, OI-P22-05; V-123 |
| VC-22 | Microsoft (Graph, Entra, CSPP) and Google Workspace (app verification) | `WORKSPACE_PORT`, `STORAGE_PORT` | Scopes; admin-consent process; app-store/marketplace listing; CSPP eligibility | Co-authoring; BYO export | OI-P07-01, OI-P04-06, OI-I-06; V-121 |
| VC-23 | Platform tooling where not self-hosted (observability, status paging, Temporal Cloud, GitHub Enterprise, flag service) | — | India residency; pricing; security add-ons | P00/P23 ADRs | OI-P00-10, OI-P00-11, OI-P23-01; V-120, V-124 |
| VC-24 | Graphy (FinLegal Academy) | `ACADEMY_PORT` | Catalogue feed/API; SSO; merchant of record | Academy integration | OI-P16-06, OI-P19-08, OI-I-09; V-126 |
| VC-25 | Automation platforms (Zapier, Make, Power Automate) | P19 §4M | Listing terms; residency; transfer assessment | Automation apps | OI-P19-07, OI-I-10; V-124 |
| VC-26 | Plagiarism and search-monitoring tools | `PLAGIARISM_PORT` | Terms; India data handling | Content Studio checks | OI-P21-08; V-124 |
| VC-27 | Customer-system adapters (TallyPrime, Zoho, Darwinbox, Keka, SAP SuccessFactors, Salesforce, HubSpot) | `ACCOUNTING_PORT`, `HRMS_SOURCE_PORT`, `CUSTOMER_CRM_PORT` | API terms and versions | Enterprise integrations | V-124 |
| VC-28 | E-voting agencies (NSDL, CDSL, KFin Technologies, MUFG Intime) | file hand-off | File formats | General-meeting hand-off | V-124 |
| VC-29 | Assurance providers (CERT-In-empanelled auditor, VAPT firm, PCI QSA, ISO certification body) | — | Scope; empanelment evidence; reporting | P23 gates | OI-P23-02, OI-P-06; V-026, V-083 |
| VC-30 | Accessibility partners (ISL interpreters, disabled-user testing panel) | — | Credentials; availability; confidentiality | ISL content; release gates | OI-P21-11; V-117 |
| VC-31 | ODR providers (Equator first; others as adapters) | `ODR_PORT` | Referral contract; model clauses licence | ODR referrals | OI-P19-11 |
| VC-32 | Escrow partner for vehicle sales (only if the owner chooses) | — | Licensed escrow; no pooling by LawDocs | Escrow option (OFF) | OI-P15-05; LG-187 |

---

## W.8 Closure workflow and change log

**Closing an item.** (1) Owner records evidence and outcome in `verification-log.yaml` (or attaches the opinion/memo/contract for `CQ`/`TM`/`VC` items); (2) a checker other than the owner approves (NN-18); (3) dependent rule rows (Appendix G) and settings (Appendix R) are updated by Governed release; (4) the flag owner requests ON with the `requires_verification_id` link; (5) P23 evidence pack picks up the closure. An item closed `CHANGED` triggers a content correction in every file listed in W.3 "Files affected".

**Weekly report.** The `eng` dashboard shows open `P1` items by wave, items past due, flags waiting on items, and counsel/tax/vendor items by owner; the owner receives it every Monday.

| Version | Date | Change |
|---|---|---|
| v1.0 | 25 Oct 2026 | First issue: census of 1,792 `[VERIFY]` markers in 50 files de-duplicated to 130 backlog items; 338 open-item IDs consolidated into one register; 52 counsel questions; 17 tax-memo points; 32 vendor contracts. Items settled by X-01, X-02, X-12, X-22, X-27 and X-29 marked `RESOLVED`. Status vocabulary reconciled between P00 (`OPEN`/`VERIFIED`/`REJECTED`) and P03 (`VERIFIED`/`SECONDARY_ONLY`/`NOT_CONFIRMED`) by the `outcome` field (W.1 step 3). |
| v1.0.1 | 25 Oct 2026 | §W.9 added: legal-accuracy review findings LA-01…LA-36 (corrections applied in F, G, M, O, S and the content deck; corrections for master, decision log, L, P12 and P15 reported). |
| v1.0.2 | 25 Oct 2026 | Registry review G4: §W.2 census refreshed by script over current phases, appendices (except W), content deck, `01` and `02` (see §W.2 totals); §W.4 gains `OI-B-01`…`04`, `OI-R-08`, `OI-Y-09`…`11` (346 IDs). |
| v1.1 *(v1.1)* | 26 Oct 2026 | IPB v1.0 adoption: §W.4.7 adds `OI-IPB-01…12` grouping 24 new phase/appendix open items (`OI-P03-08…09`, `OI-P09-11…13`, `OI-P19-13…15`, `OI-P20-08…09`, `OI-P21-12…17`, `OI-P23-09…11`, `OI-H-07`, `OI-O-11…12`, `OI-R-09`); the v1.0 `[VERIFY]` on the Node.js runtime (master §5.1) is closed by IPB-D-01 (Node 24.22.1); new `[VERIFY]` markers added in v1.1 are listed in `_review/v1.1_upgrade_review_log.md` §5 and are to be folded into §W.2/§W.3 at the next census run (V-131 onwards reserved). |

---

## W.9 Legal-accuracy review findings (25 Oct 2026)

Independent advocate's-eye review of statements of law and fact in Appendices F, G, M, O, S and W, the Website Content Deck v1.0, and master §4/§7 and decision-log §3 (read-only). Base: R2 and R3 research notes and the reviewer's knowledge of the Indian statutes. The web-search budget was exhausted before this review began. Three targeted fetches were made: two secondary sources on the IT Act First Schedule, which were retrieved, and the e-Gazette PDF, which was blocked. Nothing below is asserted as verified unless a source is named. Corrections that could not be checked against first-party text keep a `[VERIFY]` tag, and NN-38 applies to them. The review log is in `_review/F3_legal_review_log.md`.

**Status codes.** `CORRECTED` = fixed in this pack in a file the reviewer owns. `REPORTED` = needs a fix in a file the reviewer does not own (text and fix given). `CONFIRMED` = checked; no change needed. `OPEN` = cannot be verified now; stays `[VERIFY]` behind NN-38.

| ID | File(s) | Statement as found | Correction | Status |
|---|---|---|---|---|
| LA-01 | F §1 L1; G LG-003; O POL-LD-03 §6.1; content FP-03; master §7 eSign row | "as amended by S.O. 4720(E), 26 Sep 2022 (in force 4 Oct 2022) … entry 5 omitted"; "Since 26 September 2022" | The substance was re-checked against two independent secondary sources: Vinod Kothari, 12 Oct 2022, and the Leegality First Schedule explainer. **Entry 1** excludes negotiable instruments other than a cheque, or a demand promissory note/bill of exchange issued in favour of or endorsed by an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity. **Entry 2** excludes POAs, except those empowering such an entity. **Entries 3–4** (trusts, wills) are unchanged. **Entry 5** (contracts for sale or conveyance of immovable property) is **omitted**. The Gazette PDF could not be retrieved (robots block). The dates are not reconciled: S.O. dated 26 Sep 2022 against Gazette publication 4 Oct 2022 (Leegality says "October 2022"). Public copy no longer names a day. F and G carry `[VERIFY: Gazette text]` | CORRECTED (F, G, O, content); REPORTED (master §7, NN-07 — LA-22); OPEN for Gazette text (P1 before P08 launch) |
| LA-02 | G LG-215; S CHR-CC-01, CHR-B-05, fixture F-09 | Forum chosen by the claim value; "Claim ₹72 lakh → State Commission" | CPA 2019 ss.34(1), 47(1)(a)(i) and 58(1)(a)(i) fix pecuniary jurisdiction by the **value of goods or services paid as consideration**, not by the compensation claimed (2021 Rules: ₹50 lakh / ₹2 crore). For insurance this is the premium paid. F-09 now routes a ₹72 lakh claim on a ₹48,000 premium to the **District** Commission | CORRECTED; REPORTED: P15 FR-P15-35 and P15-AT-14 (see hand-back) [VERIFY: Rules title/date] |
| LA-03 | G LG-400; S CHR-D-02, F-11, F-12; F §1 L18; content FP-04 (key facts, FAQ) | "Transfer application within 14 days (same State) / 45 days"; "The buyer must apply within 14 days…" | Under MV Act s.50(1)(a)–(b) the **transferor** reports within 14 days (same State) or 45 days (another State, with NOC). The **transferee** reports within 30 days. Under s.50(2) with CMVR r.56, successors and auction purchasers act within the prescribed periods. The basis was wrongly put on CMVR r.55 alone | CORRECTED [VERIFY: current s.50 and rr.55–56 text]; REPORTED: P15 FR-P15-59 |
| LA-04 | G LG-382; content FP-13 | "Reply to examination report within one month" | One month from the date of receipt (Trade Marks Rules 2017, r.33(4)) | REVERSED at second review (G1-32): the IP India text says "within one month"; the original wording was right; P12, G LG-382 and content FP-13 now say one month |
| LA-05 | content FP-13 tracker copy and FAQ | "Status comes from the IP India public records, refreshed on a schedule"; "It checks the public IP India records on a schedule" | Scheduled automated retrieval from IP India conflicts with NN-05 and LG-393. Copy now says: licensed data partner where available, otherwise the user adds the status; "last updated" label | CORRECTED |
| LA-06 | content FP-13 | "Use ™ — Allowed from filing" | ™ may be used at any time; ® only after registration (s.107) | CORRECTED |
| LA-07 | content FP-10 FAQ | "we mask it to the last four digits" | This was inconsistent with POL-LD-01 §5.4 and NN-04. Correct position: the first eight digits are masked in every derived text; the original is retained encrypted and access-controlled, and can be replaced with a masked copy | CORRECTED |
| LA-08 | content FP-10 ("witnesses can eSign in the same ceremony"); FAQ ES-06 | Unqualified statement that witnesses can eSign | Legally required attestation (wills — ISA s.63; gifts and mortgages — TPA ss.123, 59) stays wet ink (App F IF-31, IF-38; OI-F-03). Only customary witnesses may eSign | CORRECTED [COUNSEL] |
| LA-09 | content FP-09 | Notice "within 30 days of the bank's return memo"; venue "payee's bank branch (where the cheque was presented)" | s.138 proviso (b): the 30 days run from **receipt of information** from the bank. Proviso (c): 15 days from receipt of the notice. Proviso (a): presentation within six months or the validity period. s.142(2)(a): court of the branch where the payee keeps the account through which the cheque was presented for collection. s.142(1)(b): complaint within one month (confirmed) | CORRECTED |
| LA-10 | content FAQ PR-02 | "a 2024 Madras High Court ruling found ranked and rated listings unlawful" | This overstated the holding. Now reads: the Court held that online platforms advertising advocates' services breach the Bar Council rule against advertising; appeal pending in the Supreme Court (LG-113) | CORRECTED [VERIFY SC status] |
| LA-11 | content FAQ PY-06 | "a State tax we collect and pay … on your behalf" | "We collect" conflicts with LG-100, NN-22 and the pure-agent position. Now reads: paid at actuals to the authorised channel through split settlement or vendor-direct | CORRECTED [TAX MEMO] |
| LA-12 | O POL-LD-03 §6.2 | Registration needed "to take effect against third parties or to be admissible" | Under Registration Act s.49, an unregistered compulsorily registrable document does not affect the property and is not evidence of the transaction, save the proviso purposes. Added s.17(1A) agreements to sell with possession (TPA s.53A) and leases reserving yearly rent | CORRECTED |
| LA-13 | content (messaging house, one-liner #16, Home card, FP-10 eyebrow) | "One OTP. One binding signature." | Whether a document is "binding" depends on lawful formation, the First Schedule and stamp duty; the line was an outcome claim. Replaced with "One OTP. One recognised signature." | CORRECTED |
| LA-14 | content ("Store once. Find forever." ×4; "Free forever"; "Keep every document in your vault for life") | Perpetual storage and free-forever claims | Unevidenced (NN-20); conflicts with the CH-15 retention position and POL-LD-11; risks a later bait-and-switch (NN-50). Replaced; Free-plan commitment marked `[OWNER]` | CORRECTED; OWNER |
| LA-15 | content ("Your legal officer, from day one." ×3; "RBI-ready, every quarter." ×3) | Implies LawDocs supplies a legal officer, or guarantees regulatory readiness | NN-41, CH-14 and D-17 (LawDocs does not practise law); NN-20 (outcome claim). Replaced with "Your legal desk…" and "Your RBI calendar, organised…" | CORRECTED |
| LA-16 | content FP-15 feature table; Appendix L l.51 and F-131 | "Professional consultations included" in subscription plans | Bundling advocates' consultations into a LawDocs plan price amounts to advocates on subscription, with LawDocs collecting their fee (CH-08; BCI Rules 36/37 and the fee-sharing bar; NN-21). Plan allowance limited to LawDocs documentation-team guided sessions (not legal advice). Advocate consultations are sold separately at a fixed fee paid to the advocate | CORRECTED (content) [COUNSEL]; REPORTED: Appendix L |
| LA-17 | content FP-15 | Plan cards ex-GST with GST "before you pay"; "Plans renew automatically"; trial "charged only if you keep the plan"; "one legal head can run what used to take a department" | Showing GST only at checkout risks drip pricing (Dark Patterns Guidelines 2023; NN-22): Personal card now GST-inclusive, others show the GST-inclusive total beneath. Auto-renewal statement aligned to POL-LD-05 §2 (opt-in at checkout). Trial conversion only on explicit opt-in. Unevidenced department-replacement claim removed (NN-20, NN-36) | CORRECTED [OWNER] |
| LA-18 | M M.4 GST cell; M.15.3 price card | "advocate's fee: exempt for individuals / reverse charge for registered businesses" | RCM (Notification 13/2017-CT(R) Sl. 2) applies to any **business entity**, registered or not. Exemption (Notification 12/2017-CT(R) entry 45) applies to non-business recipients and to business entities below the registration threshold | CORRECTED [TAX MEMO] |
| LA-19 | M MP-LD-03, M.19 item 5; Appendix L FAQ-18 | "assigned, verified professionals"; "A verified advocate from the LawDocs Panel"; L: "verified advocates and other professionals" | "Verified lawyers" is a barred claim (NN-20; content §2.4; M.6 forbids "verified expert"). Replaced with "advocate enrolled with a State Bar Council … (enrolment checked on [date])" | CORRECTED (M); REPORTED (L) |
| LA-20 | G LG-316 | LLP Act "s.11(1)(b)" for the incorporation statement | The professional's statement is in s.11(1)(c) (advocate, CA, CS or cost accountant engaged in formation, plus a subscriber) | CORRECTED [VERIFY] |
| LA-21 | master §7 Aadhaar row; decision log CH-01 | "s.57 struck" / "s.57 struck down" | *Puttaswamy* (Aadhaar), (2019) 1 SCC 1, struck down the contract-based part of s.57; the Aadhaar and Other Laws (Amendment) Act 2019 then **omitted** s.57. Citation added to G LG-023 | REPORTED [VERIFY citation] |
| LA-22 | master NN-07 | "negotiable instruments other than cheques" | Add the 2022 carve-out: and demand promissory notes/bills of exchange in favour of or endorsed by RBI/NHB/SEBI/IRDAI/PFRDA-regulated entities. Also "ordinary POAs" → "POAs other than those empowering such an entity" | REPORTED |
| LA-23 | content §7.1 eyebrow; one-liner #110 | "Rejected? Not the final word." | Implies reversal of the decision (NN-23 no outcome promise). Now "Rejected? You can still escalate." | CORRECTED |
| LA-24 | content §7.4 honest line | "There is no official API…" | Absence stated as fact beyond the research. Now "We know of no official API…; the transport ministry has said its data access is for government organisations" (LG-409) | CORRECTED |
| LA-25 | content §7.3 | "insurers must resolve complaints within 14 days" | Kept, and given a `[VERIFY: PPHI Master Circular 2024]` tag to match LG-200 | CORRECTED |
| LA-26 | content FP-07 | "neither the firm nor a partner can sue a third party" (s.69) | s.69(2): the firm cannot sue a third party. s.69(1): a partner cannot sue the firm or co-partners to enforce rights under the deed | CORRECTED |
| LA-27 | F IF-42, IF-49; G LG-261, LG-265 | Citations missing | *Suraj Lamp & Industries (P) Ltd v State of Haryana*, (2012) 1 SCC 656 (11 Oct 2011); *In re: Interplay* (7 judges, 13 Dec 2023), 2023 INSC 1066 | CORRECTED [VERIFY citations] |
| LA-28 | G LG-071 | DPDP penalties listed as ₹250/₹200/₹50 crore only | Schedule also has ₹150 crore (SDF obligations) and ₹10,000 (Data Principal duties) | CORRECTED [VERIFY Schedule rows] |
| LA-29 | O POL-LD-01 §5.3 | Last four digits retained, stated as [LAW] under s.8A(4) | That a masked last-four reference falls outside the s.8A(4) bar is an interpretation | CORRECTED [INTERP; COUNSEL] |
| LA-30 | content GB-08 Variant A | Class 3 DSC cited to "ss.3A and 5" | A DSC is a digital signature under s.3: cite ss.3, 3A and 5 | CORRECTED |
| LA-31 | O POL-LD-05 §1 | E-Commerce Rules "r.4" for cancellation-charge parity | Cite r.4(10) | CORRECTED [VERIFY sub-rule] |
| LA-32 | O POL-LD-13 trust page | "Production systems run in AWS Mumbai…"; "We report cyber incidents to CERT-In within 6 hours" | Hosting statement gated on recorded evidence (§2.4; NN-20). CERT-In duty limited to the incidents listed in the 2022 Directions, 6 hours from noticing | CORRECTED |
| LA-33 | content FP-09 notice table | TPA s.106 "15 days' notice" unqualified | s.106 applies "in the absence of a contract or local law or usage to the contrary"; State rent laws may add conditions | CORRECTED |
| LA-34 | content §3.7, §2.4–2.5, GB-05, GB-10; O.4, O.6 | Testimonials, AI labels, fee transparency, advocate advertising, dark patterns | Testimonials: all six formats marked PLACEHOLDER, block OFF, CMS blocks — compliant (NN-49). AI-draft label and disclosure — compliant (NN-14). Advocate display — Rule 36 fields only, no ratings — compliant, save LA-10, LA-16, LA-19. Fee lines — compliant, save LA-11, LA-17. Dark patterns — compliant, save LA-17 | CONFIRMED (with the listed exceptions corrected) |
| LA-35 | G, F, O, S, content (various) | Checked without change | s.138/s.142(1)(b) periods (LG-240). BSA s.63(4) Part A (party) / Part B (expert) with hash (NN-10, POL-LD-03 §10). Registration Act s.17(1)(b), (d), s.17(1A) from 24 Sep 2001, s.23 four months (LG-104). TPA ss.54, 59, 107, 123. ISA s.63. Stamp Act ss.17, 29, 33, 35. CERT-In 6 h / 180 days / NTP (LG-079). DPDP phases 13 Nov 2025 / 13 Nov 2026 / 13 May 2027 (LG-061–062), r.7 72 h, r.14(3) 90 days. Dark Patterns Guidelines 30 Nov 2023, 13 patterns (LG-142). E-Commerce Rules 23 Jul 2020, r.4(5) 48 h / one month (LG-141). Notification 13/2017-CT(R) Sl. 2 (LG-340); TCS 0.5% from 10 Jul 2024 (LG-344). Aadhaar ss.4(4), 8A(4), 29(4), 33A (LG-022, LG-025, LG-026). TM opposition four months, counter-statement two months, ten-year term, six-month surcharge, one-year restoration (LG-381, LG-384). Limitation Act arts. 54, 113, 116, 136, 137 (LG-230–232). CPC O.VIII r.1 (LG-233). IBC/SARFAESI/Companies Act appeal periods (LG-237–239). CrPC→BNSS and IPC→BNS mapping (content §5.4). Code on Wages s.17, OSH s.6(1)(f), POSH ss.4, 11(4), 13 (LG-163–166). Companies Act ss.117, 118, 173 (LG-155–157) | CONFIRMED (reviewer knowledge; first-party text not re-fetched in this pass) |
| LA-36 | G, S, content, master §7 | Items the review could not test | RB-IOS 2026 clause numbers and caps (₹30 lakh + ₹3 lakh); IT Rules 2026 amendment timelines (3 h / 7 days / 2 h); TCCCPR Third Amendment 2026; *Pune Bar Assn* (SC, 22 May 2026) on Part B signatories; Insurance Ombudsman ₹50 lakh cap as amended 2023; Income-tax Act 2025 s.393 mapping; Labour Codes commencement 21 Nov 2025 and Central Rules 8 May 2026; Madras HC case number and SLP status; Anthropic Usage Policy effective date; DigiLocker Requester Terms (June 2025) retained-copy position | OPEN — keep `[VERIFY]`; NN-38 flags stay OFF or advisory |

**Priority for the verification owner.** (1) LA-01 Gazette text, before P08 activates IF-29 `ESIGN_OK`. (2) LA-02 and LA-03 fixes in P15 before Wave 2 Consumer Help. (3) LA-16 counsel opinion before any plan includes a consultation allowance. (4) LA-36 items in W.3 order.

---

**Master integration note.** This appendix is read with master §4 (NN-38 in particular) and §18 (precedence; X-01…X-30). Where text above conflicts with them, the master prevails.
