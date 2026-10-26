# Cross-file resolutions (pack lead, 25 Oct 2026) — binding; recorded as X-01…X-30 in master §18

| ID | Conflict | Resolution |
|---|---|---|
| X-01 | ID prefixes introduced by phase authors not in conventions §5 | Accepted and registered in Appendix B: `aev_ cor_ anc_ mig_ bkf_ brd_ ope_ mbr_ ivt_ dev_ ntv_ onb_ pcr_ gdn_ brn_ tem_ apr_ dlg_` (P00–P02), `shr_ hld_ svw_ nom_ sgb_` (P04/P08), `nbk_ qrv_` (P09), `dlv_ tme_ dls_` (P18), `tfl_` (P14), `clk_ cnl_ lsi_ exa_ lrq_` (P11/P13); business refs `LD-ORD-`, `LD-LRQ-`. |
| X-02 | R5 CSV eSign flags vs R3 LG-003 | IT Act First Schedule entry for "contract for sale or conveyance of immovable property" was omitted on 26 Sep 2022 [VERIFY/COUNSEL] → agreements for sale are eSign-eligible (conveyance/sale deeds still need registration). Affidavits, vakalatnamas, pleadings, adoption deeds are not plain "Valid" (oath/notary/forum rules). **Appendix F §9 governs; R5 CSV eSign column is superseded.** |
| X-03 | R4 §11.6 flat listing fee for advocates | Rejected. No fee of any kind from advocates (D-05, NN-21). |
| X-04 | NN-13 per-action confirmation vs bounded reminder/nudge plans | One confirmation of an **itemised, bounded send-plan** (every message, recipient, channel and date listed) satisfies NN-13; any change re-requires confirmation; setting `agt.send_plan.mode` default `itemised_confirmation`; [OWNER]/[COUNSEL] OI. |
| X-05 | OH v1.0, LDC FR-P18-22/-40 and EQ AC treat "LawDocs eSign" as a provider other products call | Breaches NN-06. Replaced by **hosted hand-off**: signing always happens on a LawDocs-hosted page within a LawDocs customer relationship; other products receive status/evidence only. Companion change requests to OH, LDC v1.3, EQ v3.2 (master §19). [COUNSEL] confirm. |
| X-06 | LDC v1.2 P26/D-41 builds its own legal-matter and contract register vs D-10 | When a tenant uses both, LawDocs is SoR for legal matters, contracts, IP; LDC P26 registers become projections (`lit.sor.mode`). Companion change request to LDC; [OWNER] confirms. |
| X-07 | Conventions §14 export layout vs Ecosystem Spec §12.1 | Appendix K governs (follows Appendix Y §Y.11.2: `00 Start Here/` folder, spec root naming with `owner_readable` naming mode; personal data in folder names only when the owner enables readable naming). Conventions §14 superseded. |
| X-08 | Archive profiles | Appendix Y registers `ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1`. |
| X-09 | `lgo.waiting_items` (P13) vs `wf.items` (P03) | `wf.items` is the single engine; P13 uses a read view. |
| X-10 | Help-key namespace overlaps `hlp.*` settings | Help keys and settings are separate registries; general jargon uses `hlp.gen.<term>` (replace any `hlp.hlp.`). |
| X-11 | Appendix R defaults vs owning phases | Owning phase wins: `kyc.digilocker.retain_copy` default OFF; `org.master_data.change_policy` has no `owner_only` option (NN-18); `gov.mode`/`hr.mode` replaced by `int.eco.ldc.sor_mode.governance` / `.hrms`; OVSE flag split into `kyc.ovse.qr.enabled` and `kyc.ovse.avc.enabled`. |
| X-12 | Appendix K gaps | Add `06 Policies and Registers/Contract Templates and Playbooks/`; add company tax folder; individual tax folders labelled "Tax Year <YYYY-YY>" (Income-tax Act 2025 terminology [VERIFY]) with legacy "AY" alias for pre-2026 years. |
| X-13 | Consumer invoicing on OH8 vs Spec data class INTERNAL | Only billing fields (name, email, phone, optional GSTIN/address, amounts, SKU) go to OH8 under legal basis `CONTRACT_PERFORMANCE_CUSTOMER`; no case content; DPO sign-off [OI]. |
| X-14 | Aadhaar in uploads | Store only the masked rendition plus a pre-mask SHA-256; no unmasked option for any role; [COUNSEL]. |
| X-15 | NN-06 wording vs D-12 aggregator-first | NN-06 reads: "eSign only through a licensed ESP, via a contracted aggregator acting as ASP or LawDocs' own ASP arrangement (`asp_mode` per vendor), never sublet". |
| X-16 | ESP licence status | Routing blocks any ESP whose CCA licence is lapsed (Capricorn lapsed 15 May 2026) or expires (Protean 26 Oct 2026) unless renewal evidence is recorded [VERIFY]. |
| X-17 | Consumer Help storage | P15's separate database (logical cell) for the Consumer Help brand is the default; cost is an [OWNER] decision. |
| X-18 | Government fees | Default: customer pays the official portal directly; LawDocs collects only its own and the professional's fee; optional pure-agent collection OFF pending [TAX MEMO]. |
| X-19 | Assigned-professional model vs client choice (R3 LG-113) | Buyer may request a different professional (once by default, configurable); counsel confirms the model. |
| X-20 | Ops creating maker users for a client | Client-approved standing authorisation, OFF by default. |
| X-21 | Marketplace model letters | LawDocs: M1 LawDocs-delivered, M2 Route-collected third-party, M3 direct engagement (differs from LDC lettering — note in Appendix M). |
| X-22 | Content Studio location | `apps/console` "Content Studio" area, restricted to `OPS_CONTENT_PUBLISHER`, `PLT_CONTENT_EDITOR`, `PLT_LEGAL_REVIEWER`; Super Admin not required. |
| X-23 | Pleading page count | 70 consolidated pleading pages (P10/Appendix E) supersede R5's ≈68. |
| X-24 | Copied content list | Add "StartupSeven" mention (Compliance manual l.1060) to the rewrite list. |
| X-25 | Phase lengths over target | Accepted; precision preferred over brevity. |
| X-26 | `chp` Consumer Help case manager and ethical wall | `int.chp.ecosystem_clients.allowlist` empty by default; no Udofin grievance is routed to the Consumer Help brand. |
| X-27 | Agent names across phases | Appendix H roster (37 agents) is canonical; phases use those codes. |
| X-28 | Error code ranges | `LD-WF-001–099` P02 (maker-checker/DoA), `LD-WF-100–149` P03 (items engine). Other module ranges as declared in each phase. |
| X-29 | Court/TM data ports | Appendix I `COURT_DATA_PORT` and `TRADEMARK_DATA_PORT` include the operations P11/P12 use; no WIPO scraping actor (NN-05). |
| X-30 | Appendix O gherkin tags `@APPO-AT-nn` and POL-LD-01…17 policy register | Accepted; P21 renders policies from the POL register. |
