# Phase P10 — Pleadings, Notices and Court Drafting Studio

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P06 (template engine, questionnaire engine, clause library, lanes, review gate, export, Template Studio — reused, not rebuilt); P05 (originals, OCR, handwriting/WhatsApp type copies, translations as derived renditions `drv_`); P04 (Vault, Object Lock, hashes); P08 (eSign where permitted, BSA s.63(4) certificate drafts, evidence packs); P09 runtime (Vidhi, citation resolver); P16 (advocate review and "hire an advocate" SKUs); P03 (rule packs: limitation, court fees, forum profiles). Consumer: P11 (a filed pleading becomes a court case record).
> **Sequencing:** Sprint 1–2: forum render profiles, document anatomy, annexure builder, index/pagination, PDF/A e-filing pack. Sprint 3: pleading interview + library load (Appendix E §4 wave 1). Sprint 4: legal notices and replies with dispatch and proof of delivery. Sprint 5: limitation and jurisdiction prompts, party-in-person mode, advocate review gate. Sprint 6: affidavit/verification routes, vakalatnama, P11 hand-off, hardening. **Freeze point:** render-profile token schema at the end of sprint 1 (P11 and P15 reuse it).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (§4 pleadings taxonomy; §7 outdated-law backlog), F (eligibility gate — affidavits and verifications are never eSign-only), H (agents), K (`LD-EXPORT-1.0`), M (marketplace rules for advocate SKUs), R (settings), W (open items).
> **Requirements covered:** R-012 (pre-filing part), R-044, R-045, R-061, R-079, R-084 (notice and court-drafting part), R-087, R-090, R-091.
> **Decisions applied:** D-05, D-06, D-07, D-17 · **Challenges applied:** CH-11, CH-14, CH-28, CH-30 · **Non-negotiables tested:** NN-05, NN-07, NN-09, NN-10, NN-11, NN-13, NN-14, NN-20, NN-28, NN-34, NN-38, NN-41, NN-48
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 2, frontend 2, docgen/PDF 1, AI 1, QA 1, legal content analyst 1) plus advocate reviewers from the `PLT_LEGAL_REVIEWER` panel.

---

## 1. Objective and business outcome

Individuals facing a dispute and companies running litigation need court-ready documents: a properly formatted plaint or petition, a list of dates, a verified affidavit, a vakalatnama, annexures marked P-1, P-2 with typed copies of handwritten notes and WhatsApp screenshots and their translations, and a legal notice sent with proof of delivery. P10 delivers a Pleadings, Notices and Court Drafting Studio on the P06 engine, loaded from the owner's Pleadings manual (13 areas, 89 drafts → 70 consolidated pages — X-23 supersedes R5 §8.2's ≈68; FR-P10-01; Appendix E §4), **updated to the new criminal laws** (BNS, BNSS, BSA in force 1 July 2024), CPC 1908, Commercial Courts Act 2015 and Consumer Protection Act 2019.

Two lines we hold (and say plainly to the owner):
1. **LawDocs prepares documents; it does not file, argue or advise.** Filing, appearance and advice are for the party in person or an enrolled advocate (Advocates Act 1961 ss.29, 33 — R3 LG-110; NN-41). No auto-filing on any court portal and no portal automation (NN-05, NN-13). The manual's line "file directly before any High Court and Supreme Court" is withdrawn.
2. **AI-assisted court documents for individuals pass a qualified-review gate** before final download (NN-14, R4 §6.4 "pleadings self-help" row), and every AI-assisted document carries a disclosure line.

| Outcome | Exit-gate measure |
|---|---|
| Correct format | Exports validate against the selected forum render profile (page size, margins, font, spacing, numbering); unverified profiles never labelled "court-ready" |
| Correct law | 0 published pleading templates citing CrPC/IPC/Evidence Act/CPA 1986 as current law; old→new mapping shown where users search old sections |
| Annexures right | Every annexure referenced in the text exists in the index and vice versa; typed copies and translations sit next to their originals with labels; BSA s.63(4) certificate draft generated for each electronic-record annexure |
| Filing pack | PDF/A-2b, OCR text layer, bookmarks from index, continuous pagination, size split per profile — validated by veraPDF in CI |
| Notices with proof | Legal notices dispatched only after human confirmation, with dispatch evidence (India Post tracking, email delivery) attached to the notice record |
| Safe self-help | Party-in-person mode shows forum-specific disclaimers, legal-aid route and "hire an advocate" path at every final step |

---

## 2. Scope (in / out)

**In scope:** pleadings library (13 areas, consolidated, variants as toggles — Appendix E §4); court-format render profiles and document anatomy (cover, index, synopsis and list of dates, memo of parties, body, prayer, verification, affidavit, vakalatnama, annexures, certificates); forum and jurisdiction prompts; limitation prompts (advisory); legal notices and replies (s.138 NI Act, s.80 CPC, money recovery, consumer, RERA, tenancy/eviction, employment dues, IP infringement, defamation, others from Appendix E) with dispatch and proof of delivery; party-in-person mode; annexure builder linking originals, type copies and translations from P05; e-filing preparation packs; advocate review gate and disclosure stamp; affidavit swearing route and verification signing route; hand-off to P11.

**Out of scope (owner phase):** case tracking, hearings, orders, cause lists — **P11**; filing on any portal — **never automated** (user or advocate files); OCR/type copy/translation engines — **P05**; consumer grievances before ombudsmen and regulators (RBI-IOS, Insurance Ombudsman) — **P15** (reuses P10 notices and formats); arbitration statements and Equator proceedings — **Equator** (EQ App. M) via `int`; criminal FIRs and police complaints drafting for others by LawDocs staff — not offered as a staff service (templates for self-use only, with review gate).

---

## 3. Personas and permissions touched

| Role code | P10 permissions |
|---|---|
| `IND_OWNER` (party in person) | Draft pleadings and notices for own matters; approve own facts; download after review gate where AI-assisted; dispatch own notices; request advocate review or engagement |
| `IND_GUARDIAN`, `IND_DELEGATE` | Draft for the ward/principal within scope; signatures and verification remain the party's or guardian's as the law requires |
| `ORG_LEGAL_MAKER`, `ORG_CLO` | Draft for the company; assign to external counsel; approve internally; dispatch company notices (with DoA if configured) |
| `ORG_EXT_COUNSEL`, `PRO_ADVOCATE`, `OPS_PROFESSIONAL` (advocate) | Review, edit in tracked changes, approve (review certificate), prepare vakalatnama, sign notices on their letterhead in their own name, prepare the filing pack; file outside LawDocs |
| `PLT_CONTENT_EDITOR` / `PLT_LEGAL_REVIEWER` | Author/approve pleading templates, render profiles, limitation rows, court-fee rows, notice templates (maker-checker) |
| `OPS_CONSUMER_CASE_MANAGER` | Consumer Help brand only (P15): prepare non-advocate documents where the forum allows (NN-23) |
| `AGT_*` (pleadings drafting skill) | Maker-only: chronology, list of dates, synopsis drafts, annexure index suggestions; never approves, files, sends or swears (NN-13, NN-43) |

---

## 4. Functional requirements

### 4A. Pleadings library

**FR-P10-01 — Library from Appendix E §4.** Load the consolidated pleadings list (13 areas; 89 manual drafts consolidated to 64 canonical pages — R5 estimated ≈68 before four further merges — plus 6 court documents imported from the Documents manual = 70 pages, and 10 commissioned gap drafts; re-filed items — DV complaint to Family; consumer complaints out of "Corporate Law"; "Award by an Arbitral Tribunal" moved to ADR documents with an Equator cross-link). Each pleading is a P06 template of `document_class = pleading | application | petition | complaint | appeal | affidavit | caveat | written_statement` with `lane_eligibility = PLD`.

**FR-P10-02 — Variants as toggles, not pages.** Duplicate-intent clusters become one page with toggles: forum (e.g., Magistrate / Sessions / High Court for bail), personal law (Hindu Marriage Act / Special Marriage Act / Muslim law / Indian Divorce Act), petitioner (husband / wife / joint), commercial vs non-commercial suit, State. Toggles change clause slots and the render profile.

**FR-P10-03 — New-law mapping.** Every template cites current law and shows an "Old → new" box where users search the old section: CrPC s.125 → BNSS s.144; s.167(2) → s.187; s.200 → s.223 (with the pre-cognizance hearing of the accused); s.205 → s.228; s.256 → s.279; s.311 → s.348; s.317 → s.355; s.320 → s.359; s.437 → s.480; s.438 → s.482; s.439 → s.483; IPC s.498A → BNS ss.85/86; s.406 → s.316; s.420 → s.318; ss.499/500 → s.356; s.506 → s.351; Evidence Act s.65B → BSA s.63 (R5 §5) [LAW; each mapping re-checked by `PLT_LEGAL_REVIEWER` before publication — VERIFY]. A transition toggle "offence/proceeding before 1 July 2024" switches to the old provisions where the savings clause applies (BNSS s.531 [LAW]; BNS s.358 [VERIFY]), with an explanation.

**FR-P10-04 — Content gaps commissioned.** The manual's intro promises writ, NCLT, energy and arbitration drafts with none delivered (R5 §3.1). Appendix E §4.3 lists the commissioned additions (e.g., Companies Act 2013 ss.241–242 oppression/mismanagement petition; IBC s.7/s.9 applications; s.252 restoration; Commercial Courts Act s.12A pre-institution mediation application; CPC O.XXXVII summary suit; waiver of the HMA s.13B(2) cooling-off period; writ petition (Art. 226) skeleton for advocate use only). Until published, hubs show no promise of them (NN-20).

### 4B. Court formats: render profiles and document anatomy

**FR-P10-05 — Render profiles as data.** `pld.render_profile` with tokens: page size, orientation, margins, body/heading/quote fonts and sizes, Indic font map, line spacing, paragraph numbering style, alignment, page-number position and start, header/footer, duplex, PDF standard, OCR required, scan DPI, bookmarks, max file size and split rule, filename rules, annexure series, translation requirement, signature style. Profiles have status `draft → in_review → verified | unverified_published → superseded`; only `PLT_LEGAL_REVIEWER` sets `verified` with `source_ref` and `verified_on` (pattern from EQ App. L §5.2). Exports from unverified profiles carry the cover-sheet notice "Formatting based on [source]; check the current rules of [forum] before filing" and the UI never says "court-ready".

**FR-P10-06 — Seed profiles** (values from the Equator v3.1 verified rows where available; everything else [VERIFY]):

| Code | Forum | Seed status | Key values |
|---|---|---|---|
| `SC_2020_PRINT` | Supreme Court of India (and default court style) | verified (SC notice 12 Mar 2020, effective 1 Apr 2020 — EQ App. L §5.1) | A4, both sides, Times New Roman 14, line spacing 1.5, quotations 12 single, margins L/R 4 cm, T/B 2 cm |
| `SC_EFILING` | SC e-filing | unverified | As print; size/PDF rules [VERIFY by test upload] |
| `HC_TS_EFILING_2020` | Telangana HC and district judiciary (e-Committee model rules) | verified in EQ (Notification 15/SO/2020) | A4; margins 38.1/38.1/44.45/25.4 mm; TNR 14; 2.0 spacing; 20 MB per file; OCR text; bookmarks; filename ≤ 45 chars |
| `HC_RJ_EFILING` | Rajasthan HC | verified in EQ (hcraj.nic.in e-filing guidelines) | Legal size (216 × 356 mm); all pages numbered incl. front page; running header; 20 MB |
| `HC_DL` | Delhi HC | unverified | A4 [VERIFY Delhi HC (Original Side) Rules 2018 and practice directions] |
| `HC_GENERIC` | Other High Courts | unverified | A4, TNR 14, 2.0 spacing; per-HC verification backlog |
| `DIST_CIVIL` / `DIST_COMMERCIAL` | District and Commercial Courts | unverified | Per State HC rules; plaintiff/defendant document labels; exhibit numbers assigned by court (CPC O.XIII r.4) |
| `FAMILY_COURT` | Family Courts | unverified | Per State rules |
| `MAGISTRATE` | Criminal courts | unverified | Per State rules |
| `CONSUMER_COMMISSION` | District/State/National Commissions | unverified | Online filing format for e-Daakhil / e-Jagriti [VERIFY current portal and file limits] |
| `NCLT` | NCLT/NCLAT | unverified | NCLAT Rules 2016 r.19(1) margins per EQ seed [VERIFY]; A4; 2.0 spacing |
| `RERA_<STATE>` | State RERA authorities | unverified | Form per State RERA rules [VERIFY] |

Tenants (law-firm workspaces, company legal teams) may add custom profiles through maker-checker; exports from custom profiles are labelled "Custom layout — not a court profile".

**FR-P10-07 — Document anatomy.** Components assembled in profile order (EQ App. L §5.3 adapted): (1) cover/title page (court name, jurisdiction, case type and number or "to be numbered", cause title, document title, "with" list of applications, filed by — advocate block or party-in-person block); (2) index (S. No. · Particulars · Annexure · Page No. · Remarks, each annexure on its own row); (3) synopsis and list of dates (where the forum uses them — chronological two-column Date · Event, each event linked to an annexure page; unlinked rows flagged); (4) memo of parties (addresses for service; no caste or religion of parties unless legally required [VERIFY SC direction cited in EQ App. L §5.3 — applied as LawDocs policy]); (5) body with continuous numbered paragraphs (grounds lettered where the forum style uses it); (6) prayer (numbered reliefs); (7) verification (CPC O.VI r.15 paragraph-wise: true to knowledge / based on information believed true / based on legal advice; place and date) or, for commercial disputes, the statement of truth under CPC O.VI r.15A as inserted by the Commercial Courts Act 2015 [LAW; VERIFY verbatim Appendix form before activation]; (8) supporting affidavit where rules require; (9) vakalatnama or party-in-person memo; (10) annexures with separator pages; (11) certificate of translation (only from certified translation — never machine translation, NN-48); (12) BSA s.63(4) certificate (Part A for the party; Part B request to an expert) for electronic-record annexures (NN-10; R3 LG-091); (13) applications (IAs), each with its own affidavit; (14) AI-disclosure line where AI assisted.

**FR-P10-08 — Locked tokens.** Users may edit text, reorder optional components where the profile allows, toggle optional components (synopsis, IAs), choose language layout; they cannot change locked tokens of a verified profile (margins, font, spacing, page size). Page references in body and index are fields bound to the page map; any unresolved reference blocks export (LD-PLD-021).

**FR-P10-09 — Court language.** The profile sets the court language (Constitution Art. 348(1) — SC and HC proceedings in English, Art. 348(2) Hindi/State language in a High Court with Presidential authorisation; CPC s.137 — subordinate court language set by the State [LAW; VERIFY wording — R3 LG-093]). Non-court-language annexures require a certified translation for filing (R3 LG-094 [VERIFY rule numbers]); machine translations may be attached only as "Translation for convenience — not certified" where the forum tolerates it (profile flag), otherwise the export blocks with an order-certified-translation CTA (P16).

### 4C. Pleading interview, forum and jurisdiction prompts

**FR-P10-10 — Interview structure.** Sections: parties (with capacity — minor through next friend/guardian, CPC O.XXXII; person of unsound mind; company through authorised signatory with board resolution; firm through partner, CPC O.XXX); facts (chronology builder — events with dates, amounts, documents); cause of action and date; relief(s) and valuation; forum selection; limitation; court fee; documents and annexures; advocate or party-in-person; language.

**FR-P10-11 — Forum and jurisdiction prompts (advisory).** The Studio asks the questions and shows the rule the user must apply; it does not decide.

| Prompt | Rule shown (examples) |
|---|---|
| Territorial jurisdiction | CPC ss.16–20 (immovable property where situated; defendant resides/carries on business; cause of action arises) [LAW] |
| Pecuniary jurisdiction | State civil courts acts and valuation [VERIFY per State]; consumer: by the **value of the goods or services paid as consideration**, not the compensation claimed (CPA 2019 ss.34(1), 47(1)(a)(i), 58(1)(a)(i); LG-215; W.9 LA-02) — District Commission ≤ ₹50 lakh, State > ₹50 lakh up to ₹2 crore, National > ₹2 crore (Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules 2021 [VERIFY: Rules title/date]) |
| Commercial dispute? | Commercial Courts Act 2015 s.2(1)(c) (commercial dispute) and specified value ≥ ₹3 lakh (s.2(1)(i) as amended 2018) [LAW; VERIFY]; if yes and no urgent interim relief is sought, pre-institution mediation under s.12A is mandatory (*Patil Automation v Rakheja Engineers*, SC 2022 — R5 §5) and the plaint must state compliance |
| Suit against Government/public officer | CPC s.80: two months' notice before suit; s.80(2) leave for urgent relief [LAW] → offers the s.80 notice (§4E) |
| Family matters | Family Courts Act 1984 s.7 where a Family Court is established; personal-law petition toggles |
| Cheque dishonour complaint | NI Act s.142(2) (inserted by the NI (Amendment) Act 2015): (a) cheque delivered for collection through an account — court within whose jurisdiction the branch of the bank where the payee (or holder in due course) **maintains that account** is situated; (b) cheque presented for payment otherwise than through an account — court of the drawer's branch (W.9 LA-09) [LAW; VERIFY wording] |

**FR-P10-12 — Valuation and court fee.** Valuation prompts per relief (money claim, declaration, injunction, possession) and a court-fee calculator only for States whose Court Fees Act schedule is verified in the rule pack (`pld.court_fee.<state>` status); otherwise "Court fee as per the [State] Court Fees Act — confirm with the court/advocate" [VERIFY per State]. Consumer complaint fee per CPA Rules [VERIFY current schedule].

**FR-P10-13 — Grounded facts.** Every factual paragraph links to a source: a chronology event the user typed, or a document page/region (P05 anchor). Unlinked factual sentences are highlighted as gaps before review (pattern from EQ App. M PS-03). Amounts and dates in prose must equal chronology/relief-table values (deterministic validator).

### 4D. Limitation prompts (advisory)

**FR-P10-14 — Limitation engine.** `pld.limitation_rule` rows: subject, statute/article, period, start event ("from the date of refusal", "when the facts become known"), notes, exclusions applicable, status (`VERIFIED` / `UNVERIFIED`), reviewer, verified_on. The engine computes a "last date (advisory)" from the user's dates with deterministic date arithmetic and shows the rule text; it **never** says "time-barred" or "within limitation" as a conclusion — it says "On the dates you entered, the advisory last date is [date]. Confirm with an advocate." Every row ships `UNVERIFIED` and is activated row by row by `PLT_LEGAL_REVIEWER` (NN-38; [VERIFY] each).

**FR-P10-15 — Seed rows (all [VERIFY]; advisory).**

| Subject | Seed reference | Period (seed) | Start (seed) |
|---|---|---|---|
| Specific performance of a contract | Limitation Act 1963, Sch. Art. 54 | 3 years | Date fixed for performance or, if none, when plaintiff has notice of refusal |
| Compensation for breach of contract | Art. 55 | 3 years | When the contract is broken |
| Cancel or set aside an instrument | Art. 59 | 3 years | When facts entitling cancellation first become known |
| Malicious prosecution | Art. 74 | 1 year | When the plaintiff is acquitted or the prosecution otherwise terminated |
| Libel / slander | Arts. 75 / 76 | 1 year | Publication / words spoken (or special damage for slander where required) |
| Price of goods sold and delivered (no fixed credit period) | Art. 14 | 3 years | Date of delivery |
| Appeal from a decree | Art. 116 | 90 days (to HC) / 30 days (other court) | Date of decree |
| Set aside ex parte decree | Art. 123 | 30 days | Date of decree or knowledge where summons not duly served |
| Residuary suits / applications | Arts. 113 / 137 | 3 years | When the right to sue / apply accrues |
| Probate / letters of administration | Art. 137 as applied by *Kunvarjeet Singh Khandpur v Kirandeep Kaur* (SC 2008) [VERIFY citation] | 3 years | When the right to apply accrues (need arises) |
| Consumer complaint | CPA 2019 s.69 | 2 years | Date cause of action arises (delay condonable for sufficient cause) |
| Cheque dishonour complaint | NI Act s.142(1)(b) | 1 month | Date cause of action arises under s.138 proviso (c) |
| Motor accident claim | MV Act 1988 s.166(3) as amended 2019 | 6 months [VERIFY commencement] | Date of accident |
| Insurance Ombudsman complaint | Insurance Ombudsman Rules 2017 | 1 year (with conditions — P15) | Insurer's rejection/reply |
| Promissory notes / bills of exchange | Arts. 34–38 (by type) [VERIFY: article range — the earlier seed "Arts. 28–38" could not be confirmed] | Reviewer to set per row | Reviewer to set |
| Possession of immovable property / against tenant | Arts. 64, 65, 67 | Reviewer to set | Reviewer to set |

**FR-P10-16 — Exclusions and condonation prompts.** Prompts for exclusion of time: s.4 (court closed on last day), s.12 (time for obtaining copies), s.14 (bona fide proceedings in a wrong court) [LAW]; condonation of delay under s.5 for appeals and applications (not suits) [LAW] — offers the "Application for condonation of delay" template. Commercial s.12A mediation period exclusion (s.12A(3)) noted [VERIFY].

### 4E. Legal notices and replies

**FR-P10-17 — Notice library.** From Appendix E (Documents D3.5, D11.5, D11.9, D11.10, D12.5, D10.4 and pleadings cross-links): s.138 NI Act demand notice; s.80 CPC notice; money recovery/payment demand; breach of contract damages; consumer complaint notice (pre-litigation); RERA refund/possession notice; tenancy — notice to quit (TPA s.106 notice periods: 15 days for month-to-month tenancies as amended 2002, subject to contract and State rent law [LAW; VERIFY State overrides]), arrears of rent, eviction; employment dues; copyright/trademark infringement cease-and-desist; defamation notice; reply to legal notice; reply to cheque-bounce notice; secured-creditor notices (e.g., SARFAESI s.13(2)) **professional-only** for eligible secured creditors and normally produced in the lender's own system (Recovery Suite owns `in.infrabyx.recovery.LegalNoticeIssued.v1` — ECO A.3; LawDocs does not emit it).

**FR-P10-18 — s.138 NI Act timeline helper.** Inputs: cheque date, presentation date, date of bank memo, date the payee received the memo. Computes (advisory, verified rows): notice deadline = 30 days from receipt of information of dishonour (s.138 proviso (b)); payment window = 15 days from receipt of notice by the drawer (proviso (c)); complaint window = within one month from the date the cause of action arises (s.142(1)(b)); cheque validity three months (RBI instruction [VERIFY]); notes on interim compensation (s.143A) and appeal deposit (s.148) [LAW]. The page notes that High Courts have considered BNSS s.223 pre-cognizance hearing in cheque complaints — verify the State position (R5 §5).

**FR-P10-19 — Who sends the notice.** Notice modes: (a) **party notice** — signed by the individual/company in its own name; (b) **advocate notice** — on an advocate's letterhead, signed by the advocate in the advocate's own name after engagement through P16 (LawDocs never issues notices "by LawDocs" as a law firm — NN-41). The template adjusts the voice ("Under instructions from my client…" only for advocate notices).

**FR-P10-20 — Dispatch with proof (human-confirmed).** Dispatch options: registered post/speed post (via a postal booking partner where contracted, or the user posts and uploads the receipt and tracking number), courier, email (with delivery/read evidence where available), hand delivery (acknowledgement upload). Each dispatch requires the sender's explicit confirmation on a summary screen (recipient, address, mode, cost) — NN-13. WhatsApp is not a dispatch channel for legal notices (R6 D-31 rule); SMS only as a courtesy alert if the recipient has consented. Tracking numbers are entered or received from the partner; LawDocs never scrapes India Post or courier sites (NN-05) — status refresh only through a licensed/partner API or manual entry. The notice record (`ntc_`, `LD-NTC-…`) keeps the PDF, hash, dispatch proof and delivery status; delivery date drives reply and s.138 timelines.

**FR-P10-21 — Replies.** "Reply to a notice": upload the received notice (P05 OCR), Vidhi extracts allegations and demands into a structured list (maker suggestion), the user marks each as admitted / denied / not known, and the reply template assembles paragraph-wise responses. AI-written reply text follows the P06 lane rules and review gate (NN-14).

**FR-P10-22 — Bulk notices (companies).** Companies may generate notices in bulk from a sheet (e.g., rent arrears across tenants) with per-row validation and per-batch human confirmation; each notice is an individual record; dispatch via partner only; no automated calls (NN-34).

### 4F. Party-in-person mode (individuals)

**FR-P10-23 — Mode switch.** At the "Who will file?" step the user chooses "I will file myself (party in person)" or "An advocate will file". Party-in-person mode adds: (a) a forum-specific information panel (what to carry, filing counter/portal, fees, copies, service on the other side) marked with "verified on" dates; (b) the party-in-person block on the cover and signature pages; (c) the verification/affidavit route (§4I); (d) the legal-aid prompt — eligibility categories under the Legal Services Authorities Act 1987 s.12 with links to NALSA/State legal services authorities [LAW]; (e) the "Hire an advocate" path (P16 SKUs: review, settle and sign, appear) at every final step. Appearance in person is permitted by CPC O.III r.1 [LAW]; some forums require prior procedures for parties in person (e.g., Supreme Court practice of assessing a party-in-person [VERIFY]) — shown as forum notes.

**FR-P10-24 — Disclaimers (approved strings, versioned).** Shown at start, before review and on the cover sheet of the download: "LawDocs is not a law firm and does not give legal advice. This document was prepared by you using LawDocs templates[ and AI assistance]. Check it with an advocate before filing. Courts may reject documents that do not follow their rules." Copy passes the NN-20 banned-claims lint (no "court-approved", "guaranteed acceptance").

**FR-P10-25 — Area restrictions.** For criminal-law pleadings (bail, compounding, recall of witness, exemption) the advocate review gate is **mandatory for all users** (`pld.criminal.review_required` locked ON) and party-in-person download shows "Bail and criminal applications are usually filed through an advocate; free legal aid may be available."

### 4G. Annexures: originals, type copies, translations (P05)

**FR-P10-26 — Annexure builder.** Pick documents from the Vault or upload; each annexure links to the **original** (immutable, hashed — NN-09) and optionally to its **type copy** (handwriting, WhatsApp screenshot, photo — `drv_` from P05, status per P05 FR-P05-19: handwriting used in a filing reaches `VERIFIED` only by independent verification, or self-attestation with zero unresolved `LOW` lines) and **translation** (MT draft or certified). The builder orders annexures chronologically (default) or as referenced, assigns labels per profile — petitioner `P-1, P-2 …`, respondent `R-1 …`, applications `A-1` where the forum uses it, "(Colly)" for compiled sets — and places type copy and translation immediately after the original as `P-3(T)` / `P-3(Tr)` (the P05 FR-P05-22 annexure-pair contract) with their own index rows labelled "Type copy" / "Translation — for convenience" / "Certified translation".

**FR-P10-27 — Labels on derived pages.** Every type-copy page carries the P05 fixed header (FR-P05-13, FR-P05-20): "TYPE COPY of Annexure P-3, original at pages x–y" plus the status line (`lbl.typecopy.machine` / `.corrected` / `.verified`); "TRUE TYPED COPY" only under FR-P05-15; no other wording (lint `LBL-TC-01`). Machine translations carry "Machine translation — not certified" (NN-48). Low-confidence words stay marked `[?word]`; illegible text `[illegible]` (EQ App. L §6.5 conventions). Users correct errors in the side-by-side editor (R-044, R-046).

**FR-P10-28 — Electronic records.** For WhatsApp chats, emails, screenshots and recordings, the builder generates a BSA 2023 s.63(4) certificate draft: Part A for the party (device, source, hash value computed at upload) and a Part B request to an expert (marketplace expert engaged through P16, preferably an Examiner of Electronic Evidence notified under IT Act s.79A, scope per *Pune Bar Assn. v UoI* (SC, 22 May 2026) [VERIFY citation] — R3 LG-091) (NN-10, CH-28).

**FR-P10-29 — True copy endorsement.** Annexure separator pages carry "True copy" endorsement text per forum practice with a signature placeholder for the party/advocate; the Studio never signs on the user's behalf.

### 4H. E-filing preparation pack

**FR-P10-30 — Pack contents.** One action "Prepare filing pack" produces: (a) the compiled PDF in the profile's standard (PDF/A-2b default), fonts embedded, OCR hidden text on scanned pages at 300 dpi, bookmarks from the index (level 1 index rows; level 2 sub-documents), continuous pagination in a reserved footer band, split into parts at bookmark boundaries when above the size limit (e.g., 20 MB per file for profiles that state it), filenames sanitised (≤ 45 characters, banned characters removed) — EQ App. L §5.6; (b) separate files the portal may require (vakalatnama, court-fee receipt placeholder, affidavit); (c) a filing checklist (copies, fees, service on the other side, signatures and oath still pending); (d) a manifest (file list, page counts, SHA-256). Validation: veraPDF profile check, font embedding, no encryption/JavaScript/annotations/forms, bookmark count = index rows (+ sub-items).

**FR-P10-31 — No filing by LawDocs.** The pack is downloaded or handed to the advocate; there is no "submit to court" button, no use of anyone's portal credentials, no CAPTCHA solving or portal automation (NN-05, NN-13; R3 LG-095). Portal names and limits shown are labelled with "verified on" dates; unverified ones say "check the portal's current limits" [VERIFY per portal: SC e-filing, eCourts e-filing, High Court portals, e-Daakhil/e-Jagriti, NCLT e-filing].

**FR-P10-32 — After filing.** "I have filed this" records the filing date, forum, filing/diary number or CNR (user-entered), and creates the P11 case record (`cas_`, `LD-CAS-…`) with the filed pack attached; hearing tracking is P11's job (licensed data partners + user-entered CNR, no "real-time" claims — conventions §13.6).

### 4I. Advocate review gate, signatures, oath

**FR-P10-33 — Review gate.** Reuses P06 FR-P06-27–30 with pleading specifics: for individuals, any AI-assisted pleading or notice requires `REVIEWED` before final (unwatermarked) download or dispatch; criminal pleadings require review for all users (FR-P10-25); company pleadings require review by an attested in-house advocate/CLO or external counsel before dispatch/final export. The reviewing advocate signs off in their own name; review certificate stored; footer: "Prepared with AI assistance; reviewed by [Name], Advocate (Enrolment No. [x]) on [date]." Template-only pleadings (no AI text) carry "Prepared by [party] using the LawDocs template [title] v[n]."

**FR-P10-34 — Verification and signatures.** Pleadings are signed and verified by the party (CPC O.VI rr.14–15) [LAW]. The Studio prepares the verification paragraph-mapping (user assigns paragraphs to knowledge / information / legal advice) and signature blocks. eSign of a pleading is offered only where the forum's e-filing rules accept it (profile flag `signature`), and **never** substitutes for an oath.

**FR-P10-35 — Affidavit route.** Affidavits are sworn before a notary or oath commissioner (Notaries Act 1952; Oaths Act 1969; CPC s.139 [LAW] — R3 LG-106). States: `draft_approved → print_ready (QR + stamp-duty line from the State pack or "check with the notary") → appointment_booked (optional, P16 notarisation facilitation if enabled) → sworn_uploaded (scan + jurat fields) → verified (OCR similarity to the approved text ≥ 0.98 excluding the jurat; mismatch shown) → attached`. The Studio never fills the jurat (EQ App. M §2.4.17 pattern). Remote oath/e-notarisation flags default OFF per forum until verified [VERIFY].

**FR-P10-36 — Vakalatnama.** Generator for the forum's vakalatnama/memo of appearance (Appendix E D11.12 language versions), with client and advocate particulars, acceptance by the advocate, and the State advocates' welfare-fund stamp note (Advocates' Welfare Fund Act 2001 s.23 and State equivalents [VERIFY]). Party-in-person filings use the memo of appearance in person.

### 4J. Hand-offs and reuse

**FR-P10-37 — Reuse in other phases.** P15 (Consumer Help) uses notices, consumer complaint formats and annexure builder under its own brand (NN-23); P11 uses render profiles for written statements, replies and applications in tracked cases; P07 uses P10 dispatch for contract notices.

**FR-P10-38 — Equator cross-link.** Where the dispute arises from an agreement with an Equator clause, or the user prefers mediation, the Studio shows "Consider mediation" with Commercial Courts Act s.12A notes and an Equator link (deep link with consent; data transfer only via `int` contracts once approved — Appendix Y; NN-24).

---

## 5. Workflows and state machines

### 5.1 Pleading project

| State | Transitions | Guard |
|---|---|---|
| `DRAFTING` | → `VALIDATING` | Required sections answered |
| `VALIDATING` | → `DRAFTING` (findings), → `READY_FOR_REVIEW`, → `READY` (template-only, review not required) | Validators V-1…V-10 (below) pass |
| `READY_FOR_REVIEW` | → `IN_REVIEW` | Review ordered (P16) or company reviewer assigned |
| `IN_REVIEW` | → `REVIEWED`, → `RETURNED` | Reviewer grant active |
| `REVIEWED` / `READY` | → `PACKED` | Filing pack built and validated |
| `PACKED` | → `SIGNED_SWORN` | Verification signed; affidavits sworn and verified (if any) |
| `SIGNED_SWORN` | → `FILED` | User records filing details |
| `FILED` | terminal → P11 case | `PleadingFiled` |

**Validators:** V-1 mandatory components present for the profile; V-2 every factual paragraph anchored or own-knowledge; V-3 amounts/dates reconcile with chronology and relief table; V-4 every legal citation resolved (no CrPC/IPC/Evidence Act cited as current unless the pre-1 July 2024 toggle is on); V-5 annexure index ↔ text references consistent; V-6 BSA s.63(4) Part A present for each electronic-record annexure; V-7 non-court-language annexures have certified translation or permitted convenience translation; V-8 format tokens match the profile; V-9 PII lint (Aadhaar masked, minors' identities masked where law requires — e.g., POCSO, JJ Act contexts [VERIFY]); V-10 banned-claims lint.

### 5.2 Notice

`DRAFT → (REVIEWED where required) → READY_TO_SEND → SENT (dispatch evidence) → DELIVERED | RETURNED_UNDELIVERED | DELIVERY_UNKNOWN → REPLY_RECEIVED (optional) → CLOSED`; timers from delivery date (reply window per notice; s.138 payment window; s.80 two months).

### 5.3 Affidavit

As FR-P10-35. `REJECTED_MISMATCH` returns to `print_ready` with the differing pages highlighted.

---

## 6. Screens and UX

| ID | App | Purpose | Key components | Mobile | Accessibility |
|---|---|---|---|---|---|
| SCR-P10-01 | public | Pleading/notice page widget | Who files? choice, area facts, "Prepare first draft", "File through an advocate" CTA, old→new section box | Above fold | SSR text |
| SCR-P10-02 | web/mobile | Pleading interview | Parties, chronology builder, relief table, forum/jurisdiction prompts, limitation panel | Step-by-step | Date inputs with text alternative |
| SCR-P10-03 | web | Draft and section review | Section list with approve ticks, source panel, gaps highlighted | Read and approve sections | Gaps announced |
| SCR-P10-04 | web | Validation report | V-1…V-10 findings with jump links | List | — |
| SCR-P10-05 | web | Annexure builder | Drag order, labels, original/type copy/translation trio, certificate status | Reorder via buttons | Non-drag alternative |
| SCR-P10-06 | web | Render preview | Page view with profile tokens, page map, index preview | Page thumbnails | Zoom 400% |
| SCR-P10-07 | web/mobile | Filing pack | Validation results, manifest, download, checklist, "I have filed" | Download sheet | — |
| SCR-P10-08 | web/mobile | Notice composer and dispatch | Template, timeline helper, sender mode, dispatch summary confirmation | Confirmation full-screen | — |
| SCR-P10-09 | web/mobile | Notice tracker | Status, proof, timers, reply upload | List | — |
| SCR-P10-10 | web/mobile | Affidavit route | Steps, notary booking, scan upload, mismatch view | Camera capture | — |
| SCR-P10-11 | delivery | Advocate review workbench | Tracked edits, validators, approve/return, vakalatnama | Tablet | — |
| SCR-P10-12 | console | Render profile and limitation-row manager | Token editor, verification fields, maker-checker | Desktop | — |

Click budgets: pleading page → first question ≤ 3 taps; notice page → dispatch summary ≤ 6 steps for a template notice; "I have filed" → P11 case created ≤ 2 taps.

"i" keys: `hlp.pld.plaint`, `hlp.pld.written_statement`, `hlp.pld.verification`, `hlp.pld.affidavit`, `hlp.pld.vakalatnama`, `hlp.pld.annexure`, `hlp.pld.list_of_dates`, `hlp.pld.synopsis`, `hlp.pld.cause_of_action`, `hlp.pld.limitation`, `hlp.pld.court_fee`, `hlp.pld.party_in_person`, `hlp.pld.pre_institution_mediation`, `hlp.pld.type_copy`, `hlp.pld.certified_translation`, `hlp.pld.s63_certificate`, `hlp.pld.cnr`, `hlp.ntc.s138_notice`, `hlp.ntc.s80_notice`, `hlp.ntc.proof_of_delivery`.

---

## 7. Backend design

### 7.1 Modules

`pld` (pleading projects, render profiles, components, annexure maps, validators, limitation and court-fee rows, notices `ntc_`, dispatch) on top of `tpl`/`drf` (P06 engine), `dix` (P05), `dms` (P04), `sgn` (P08 certificates/evidence), `ai` (P09), `rul` (P03), `lit` (P11 hand-off).

### 7.2 Tables (schema `pld`; tenant rows RLS-scoped)

| Table | Key columns | Retention |
|---|---|---|
| `pld.project` | `pld_id`, `tpl_version_id`, `drf_id`, `profile_code`, `forum`, `state_code`, `who_files`, `status`, `cas_id` | Matter life + limitation buffer |
| `pld.render_profile` | `code`, `tokens jsonb`, `status`, `source_ref`, `verified_on`, `verified_by`, `tenant_id` null for platform | Permanent |
| `pld.component_instance` | `pld_id`, `kind`, `order`, `content_ref`, `approved_by` | as project |
| `pld.annexure_map` | `pld_id`, `label`, `source_doc_ver_id`, `kind` (original/type_copy/translation/certificate), `page_from`, `page_to` | as project |
| `pld.validation_run` | `pld_id`, `findings jsonb`, `ran_at` | as project |
| `pld.limitation_rule` | `id`, `subject`, `reference`, `period`, `start_event`, `exclusions`, `status`, `verified_by`, `verified_on` | Permanent |
| `pld.court_fee_rule` | `state_code`, `relief_kind`, `formula`, `status`, `source_ref` | Permanent |
| `pld.notice` | `ntc_id`, `ref`, `kind`, `sender_mode`, `recipient_enc`, `doc_ver_id`, `status`, `delivered_at` | ≥ 8 years |
| `pld.dispatch` | `ntc_id`, `mode`, `partner_ref`, `tracking_no`, `evidence_doc_ver_id`, `confirmed_by`, `confirmed_at` | as notice |
| `pld.affidavit` | `id`, `pld_id`, `state`, `jurat jsonb`, `sworn_scan_ver_id`, `similarity` | as project |
| `pld.filing_pack` | `pld_id`, `manifest jsonb`, `validation jsonb`, `doc_ver_ids` | as project |

### 7.3 APIs (`/v1/pld`; Idempotency-Key on POST)

`POST /pld/projects` · `PATCH /pld/projects/{id}/answers` · `POST /pld/projects/{id}/validate` · `POST /pld/projects/{id}/annexures` · `POST /pld/projects/{id}/filing-pack` · `POST /pld/projects/{id}:mark-filed` (creates P11 case) · `POST /pld/notices` · `POST /pld/notices/{id}/dispatch` (requires `confirm=true` + step-up; NN-13) · `POST /pld/notices/{id}/delivery` · `POST /pld/affidavits/{id}/sworn-scan` · `GET /pld/limitation:compute` (advisory; returns rule + computed date + status) · Studio: `POST /pld/studio/profiles|limitation-rules|court-fee-rules` with `:submit/:approve` (maker-checker).

### 7.4 Domain events

`in.lawdocs.pld.PleadingProjectCreated.v1` · `PleadingValidated.v1` · `PleadingReviewed.v1` · `FilingPackBuilt.v1` · `PleadingFiled.v1` · `AffidavitSworn.v1` · `NoticeDrafted.v1` · `NoticeDispatched.v1` · `NoticeDelivered.v1` · `NoticeReturnedUndelivered.v1` · `RenderProfileVerified.v1` · `LimitationRuleVerified.v1` (all prefixed `in.lawdocs.pld.`). No cross-product event is introduced (Recovery Suite owns `LegalNoticeIssued`).

### 7.5 Jobs

`FilingPackWorkflow` (Temporal: assemble → OCR check → PDF/A → bookmarks → split → veraPDF → manifest); `NoticeDeliveryWorkflow` (Temporal: dispatch confirmation → partner booking → tracking updates or manual entry reminders → timers); `AffidavitVerificationJob` (OCR similarity); `ProfileReverificationSweep` (quarterly).

---

## 8. Integrations

| Port | Use | Failure / fallback |
|---|---|---|
| `packages/docgen` + Gotenberg + veraPDF | Rendering and validation | Block pack until valid; DOCX still downloadable |
| P05 `dix` | OCR, type copies, translations | Annexure marked "type copy pending"; manual typing allowed |
| `TRANSLATE_PORT` / certified translation SKU (P16) | Convenience vs certified translations | Block where certified is mandatory |
| Postal/courier booking partner (`DISPATCH_PORT`) [VERIFY vendor and API] | Notice dispatch and tracking | User posts and uploads receipt; manual tracking entry |
| Email (`packages/notify`, SES) | Email notices with delivery evidence | Retry; record failure |
| P16 marketplace | Advocate review, settle-and-sign, appearance, notarisation facilitation | Wait-list with ETA |
| P11 `lit` | Case creation on filing | Queue and retry |
| Court portals | **None** — no integration, no automation (NN-05) | — |

---

## 9. Settings and configuration

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `pld.profiles.allow_unverified_export` | PLATFORM | bool | true (with cover notice) | `PLT_LEGAL_REVIEWER` | Y |
| `pld.profiles.tenant_custom_enabled` | PLAN | bool | Pro+ | P17 | Y |
| `pld.criminal.review_required` | PLATFORM | bool (locked) | true | — | — |
| `pld.review.required_for_ai_individuals` | PLATFORM | bool (locked) | true (NN-14) | — | — |
| `pld.review.required_for_company_dispatch` | TENANT | bool | true | `ORG_CLO` | Y |
| `pld.limitation.show_advisory_dates` | PLATFORM | bool | true (only VERIFIED rows) | `PLT_LEGAL_REVIEWER` | Y |
| `pld.court_fee.<state>.enabled` | PLATFORM | bool | false until verified | `PLT_LEGAL_REVIEWER` | Y |
| `pld.translation.convenience_allowed.<profile>` | PLATFORM | bool | per profile | `PLT_LEGAL_REVIEWER` | Y |
| `pld.affidavit.similarity_min` | PLATFORM | decimal | 0.98 | `PLT_LEGAL_REVIEWER` | Y |
| `pld.oath.remote.<forum>` | PLATFORM | bool | false [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `pld.notice.dispatch_modes` | TENANT | list | [SPEED_POST, REGISTERED_POST, COURIER, EMAIL, HAND] | `ORG_ADMIN` | N |
| `pld.notice.whatsapp_dispatch` | PLATFORM | bool (locked) | false | — | — |
| `pld.notice.bulk_max_rows` | PLAN | int | 500 | P17 | N |
| `pld.legal_aid.prompt_enabled` | BRAND | bool | true | `PLT_SUPER_ADMIN` | N |
| `pld.pack.max_mb_default` | PLATFORM | int | 20 | `PLT_LEGAL_REVIEWER` | Y |
| `pld.pack.pdf_standard` | TENANT | enum | PDF/A-2b | `ORG_ADMIN` | N |
| `pld.transition.pre_2024_toggle_enabled` | PLATFORM | bool | true | `PLT_LEGAL_REVIEWER` | Y |

---

## 10. Security, privacy and audit

- **Sensitive data:** pleadings contain family, criminal, health and financial facts — class `LEGAL_SENSITIVE`; envelope-encrypted; Bedrock India only (NN-15); never in logs/analytics (NN-32); minors' and victims' identities masked in exports where law requires [VERIFY statute list per area].
- **Third-party personal data in evidence:** processed for establishing/defending legal claims (DPDP Act 2023 s.17(1)(a) exemption scope [VERIFY with counsel]); purpose-limited; not reused for analytics.
- **Originals immutable**; type copies/translations derived and labelled (NN-09, NN-48); every annexure hash in the manifest; BSA s.63(4) certificates (NN-10).
- **No portal automation, no credentials** (NN-05); notices dispatched only after human confirmation (NN-13); dispatch partner calls idempotent and reconciled (NN-46).
- **Audit:** project create/approve sections/validate/review/pack/mark filed; notice draft/dispatch/delivery; affidavit uploads and similarity results; profile and limitation-row verification (maker-checker IDs).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Autonomy | Human step | Guardrail |
|---|---|---|---|
| Chronology and list of dates from uploaded documents | L1 | User confirms each event | Every event anchored to a source page; no invented dates |
| Synopsis and section drafts | L1 | Section approval by the party/advocate | Grounded-facts validator; no merits opinion; no prediction of outcome |
| Allegation extraction from a received notice | L1 | User classifies each allegation | Data, not instructions (injection defence) |
| Annexure index suggestions | L1 | User reorders/approves | Deterministic labelling |
| Legal citations | — | — | Resolver-verified only; otherwise "No verified authority found" (NN-14) |
| Never | — | — | No filing, sending, swearing, signing, paying; no advice on merits, strategy or whether to sue (NN-13, NN-41, NN-43) |

Evaluation: citation fabrication rate 0 on red-team set; unanchored-fact rate 0 in exported documents; old-law citation rate 0 unless transition toggle on; per-language checks for Hindi pleadings.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p10/*.feature`)

```gherkin
Feature: Court formats

  @P10-AT-01
  Scenario: Supreme Court profile tokens
    Given render profile "SC_2020_PRINT" is verified
    When I export a petition
    Then page size is 210 x 297 mm with margins 40 mm left and right and 20 mm top and bottom
    And body text is Times New Roman 14 pt with 1.5 line spacing

  @P10-AT-02 @NN-20
  Scenario: Unverified profile is never "court-ready"
    Given profile "HC_GENERIC" is unverified_published
    When I build a filing pack
    Then the cover sheet says "Formatting based on" the source and asks me to check the current rules
    And the UI does not display "court-ready"

  @P10-AT-03
  Scenario: Annexure index matches text
    Given the petition text refers to Annexure P-4 which is not in the index
    When I validate
    Then validator V-5 blocks export with "LD-PLD-015"

Feature: New criminal laws

  @P10-AT-04
  Scenario: Old section search maps to BNSS
    When I search "anticipatory bail 438 CrPC"
    Then I land on "Anticipatory Bail Application under Section 482 BNSS (formerly s.438 CrPC)"
    And the old→new box shows "CrPC s.438 → BNSS s.482"

  @P10-AT-05
  Scenario: Old law cannot be cited as current
    Given the transition toggle "proceeding before 1 July 2024" is off
    When a section draft cites "Section 125 CrPC"
    Then validator V-4 flags it and suggests "BNSS s.144"

Feature: Annexures and evidence

  @P10-AT-06 @NN-09 @NN-48
  Scenario: WhatsApp screenshot with typed copy and translation
    Given a Hindi WhatsApp screenshot uploaded as Annexure P-3
    And its type copy is VERIFIED and its English translation is machine-made
    When I build the annexures
    Then P-3, P-3(T) labelled "Type copy" and P-3(Tr) labelled "Machine translation — not certified" appear in order
    And the original file hash is unchanged

  @P10-AT-07 @NN-10
  Scenario: s.63(4) certificate for electronic records
    Given Annexure P-3 is an electronic record
    Then a BSA s.63(4) Part A draft with the file's hash value is generated
    And a Part B request option is shown

  @P10-AT-08
  Scenario: Certified translation required
    Given profile "SC_2020_PRINT" requires certified translations
    And Annexure P-5 is in Marathi with only a machine translation
    When I build the filing pack
    Then export is blocked with "LD-PLD-018" and the certified-translation SKU is offered

Feature: Filing pack

  @P10-AT-09
  Scenario: PDF/A with bookmarks and split
    Given a compiled paper book of 64 MB under profile "HC_TS_EFILING_2020"
    When I build the filing pack
    Then each part is at most 20 MB and split at bookmark boundaries
    And veraPDF validation passes for PDF/A-2b
    And the bookmark count equals the index rows plus sub-items

  @P10-AT-10 @NN-05 @NN-13
  Scenario: No automated filing
    Then no API, button or agent action exists to submit a filing pack to any court portal

Feature: Limitation (advisory)

  @P10-AT-11 @NN-38
  Scenario: Unverified limitation row shows no date
    Given limitation row "Art. 67" is UNVERIFIED
    When I compute limitation for eviction of a tenant
    Then no advisory date is shown and the text says "Confirm the limitation period with an advocate"

  @P10-AT-12
  Scenario: Verified row computes an advisory date
    Given limitation row "Art. 54" is VERIFIED
    And the date fixed for performance was 15-01-2024
    When I compute
    Then the advisory last date is 15-01-2027
    And the result is labelled "advisory"

Feature: Notices

  @P10-AT-13
  Scenario: s.138 timeline
    Given the payee received the bank's dishonour memo on 02-11-2026
    Then the advisory last date to send notice is 02-12-2026
    When the drawer receives the notice on 10-11-2026
    Then the payment window ends on 25-11-2026
    And the cause of action is shown as arising on 26-11-2026 if payment is not made
    And the advisory complaint deadline is one month from 26-11-2026, labelled "advisory — confirm with an advocate"

  @P10-AT-14 @NN-13
  Scenario: Notice dispatch needs explicit confirmation
    Given a reviewed demand notice
    When Vidhi is asked to "send it now"
    Then no dispatch happens
    And the user sees the dispatch summary requiring their confirmation

  @P10-AT-15
  Scenario: Advocate notice is in the advocate's name
    Given sender mode "advocate notice"
    Then the letterhead and signature are the engaged advocate's
    And "LawDocs" does not appear as the sender

Feature: Party in person and review

  @P10-AT-16 @NN-14
  Scenario: AI-assisted pleading for an individual needs review
    Given an individual's petition with AI-drafted synopsis
    When they request the final download
    Then it is blocked with "LD-DRF-003" until an advocate approves

  @P10-AT-17
  Scenario: Criminal applications always need review
    Given a company user drafts a regular bail application from the template only
    Then review is required before final export

  @P10-AT-18
  Scenario: Legal aid prompt
    Given party-in-person mode
    Then the legal-aid panel lists Legal Services Authorities Act 1987 s.12 categories with links

  @P10-AT-19
  Scenario: Affidavit mismatch
    Given an approved affidavit text
    When the sworn scan's similarity is 0.93
    Then the state becomes REJECTED_MISMATCH and the differing page is highlighted

  @P10-AT-20 @NN-11
  Scenario: Export folders
    When an individual exports
    Then the filed pack, annexures, certificates and notices appear under "07 Disputes and Court Cases/<Year>/<Forum>/<Case title>/" with unfiled drafts under "07 Disputes and Court Cases/Drafts not yet filed/"
```

---

## 13. Exit gate, deliverables and open items

**Exit checklist**
- [ ] Render profiles seeded; `SC_2020_PRINT` verified; others flagged; profile manager with maker-checker.
- [ ] Appendix E §4 wave-1 pleadings published on the new laws with reviewer of record; outdated-law backlog for pleadings at zero for published items.
- [ ] Annexure builder with originals/type copies/translations and s.63(4) Part A drafts.
- [ ] Filing pack validated by veraPDF; splits and bookmarks correct.
- [ ] Notices with dispatch confirmation and proof; s.138 and s.80 helpers on verified rows.
- [ ] Limitation engine with verified rows only showing dates; court-fee calculators only for verified States.
- [ ] Party-in-person mode with legal aid and advocate paths; review gate and criminal-area rule.
- [ ] Settings (§9) in Appendix R; "i" keys registered; errors LD-PLD-001…040 registered.
- [ ] Export-map entries: `pld.project` + filing pack + annexures + certificates → Company `03 Litigation and Disputes/<Year>/<Forum>/<Case title> (LD-CAS-…)/` (pre-filing drafts in `03 Litigation and Disputes/Drafts not yet filed/`); `pld.notice` + dispatch proof → `08 Notices and Correspondence/<Year>/<Counterparty> – <Notice type> (LD-NTC-…)/`; Individual `07 Disputes and Court Cases/…` and notices under `07 Disputes and Court Cases/Notices/`; AI work products labelled in `11 AI Work Products (labelled)/` for companies.
- [ ] Gherkin §12 green; NN tests NN-05, NN-09, NN-10, NN-13, NN-14, NN-38, NN-48 green; accessibility audit on SCR-P10-02/05/07/08.

**Error codes (initial set)**

| Code | Message |
|---|---|
| LD-PLD-001 | Choose the forum before continuing. |
| LD-PLD-010 | Some facts have no source. Link a document or mark as your own knowledge. |
| LD-PLD-012 | Amounts or dates do not match your chronology. |
| LD-PLD-014 | A legal reference could not be verified. |
| LD-PLD-015 | An annexure referenced in the text is missing from the index (or the reverse). |
| LD-PLD-016 | Add the s.63(4) certificate for this electronic record. |
| LD-PLD-018 | This court needs a certified translation for this annexure. |
| LD-PLD-021 | A page reference could not be resolved. |
| LD-PLD-025 | The page layout does not match the selected court profile. |
| LD-PLD-031 | Confirm the dispatch details to send this notice. |
| LD-PLD-035 | The sworn affidavit does not match the approved text. |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P10-01 | Verify render profiles for Delhi HC, Bombay HC, Karnataka HC, Madras HC, Allahabad HC, Punjab & Haryana HC and district courts of the top 10 States [VERIFY] | `PLT_LEGAL_REVIEWER` |
| OI-P10-02 | Verify each limitation seed row (Limitation Act articles; s.166(3) MV Act commencement; Insurance Ombudsman conditions) | `PLT_LEGAL_REVIEWER` |
| OI-P10-03 | Court Fees Act schedules by State (top 10 first) | `PLT_LEGAL_REVIEWER` |
| OI-P10-04 | Postal/courier dispatch partner with tracking API and proof-of-delivery artefacts [VERIFY vendor] | Ops / integrations |
| OI-P10-05 | Commission the content-gap drafts (Appendix E §4.3) and decide writ skeleton scope (advocate-only) | `[OWNER]` |
| OI-P10-06 | Counsel view on party-in-person support boundaries (staff help limited to platform mechanics; no drafting for the user by LawDocs staff who are not engaged advocates) | `[COUNSEL]` |
| OI-P10-07 | Consumer Commission portal: e-Daakhil vs e-Jagriti current state and file limits [VERIFY] | P15 owner |
| OI-P10-08 | BNS s.358 / BNSS s.531 savings and transition text for the pre-1 July 2024 toggle [VERIFY] | `PLT_LEGAL_REVIEWER` |
