# Infrabyx Ecosystem Prompt Upgrade — Summary (26 October 2026)

Owner: Company Secretary, Infrabyx Group. Prepared by the pack lead (Claude) from the owner's instruction of 25 October 2026 to assess, cross-pollinate, harden and future-proof all build-prompt packs, add the public website / super-admin / blog / resources / policy layer, Vidhi AI everywhere, accessibility, provider / cloud / database / payment neutrality, environment and credential files, adversarial review, and archive the previous versions.

## 1. What was done

1. **Audit.** Three parallel inventories (34 criteria × 7 documents) established what each pack had, lacked, and did best. Findings are recorded in the IPB README §1 and in each pack's "What changed" list.
2. **New shared baseline — Infrabyx Platform Baseline Standard (IPB) v1.0** (`Finbyx and Udofin Prompts/Ecosystem/Infrabyx Platform Baseline Standard v1.0/`, 14 files, ≈132,000 words, consolidated Word copy). Every product inherits it by a one-paragraph adoption clause; it carries the stack lock (Node 24.22.1, NestJS 11 modular monolith, Next.js 16, PostgreSQL-only, 42 + 22 ports with ≥2 adapters each), the security and certification map (CERT-In, ISO 27001/27701/42001/22301, SOC 2, PCI DSS v4.0.1 SAQ A, DPDP, RBI/SEBI/IRDAI outsourcing, OWASP ASVS 5.0 / LLM / Agentic), the multi-provider AI gateway and Vidhi AI kernel (Claude, OpenAI/Azure, Gemini, Grok, Sarvam/Bhashini, self-hosted; image generation; MCP; scheduled tasks; notebooks; autonomy L0–L4 with locked human-approval lists), the public website and super-admin Studio (CMS, Brand Studio with logo/favicon/colours/application name, Pricing Studio, blog with toggle/bulk import/user posts, vlog, Resources library, cookie CMP, binding footer with Delhi/Noida/Jaipur addresses and social buttons, About/Team/Leadership/Investors/Careers/Press/Partners/Contact/Documentation/Trust Centre pages, tag manager/UTM/pixels consent-gated, feedback widget), eighteen policy templates, accessibility (WCAG 2.2 AA, IS 17802, hearing and vision provisions), the UX system and binding 20-node settings tree with the "i" help registry, the Vendor Assurance Room (cadenced uploads; tenant download room), engineering governance (preview environments, flags and rings, zero-downtime migrations, patch SLAs, release notes, tenant beta programme, Claude Code branch convention), the API/event standard, the environment and seed standard, the 2028–2030 technology watchlist (46 items with flags), and optional Claude artefact uses.
3. **Ecosystem Integration Specification v1.2** — IPB registered, LawDocs change request absorbed, 71 canonical events (27 new), `product_scope` staff segregation, shared `brand_pack` for white-label resale, Vidhi cross-product delegation contract, vendor-assurance publication contract, cross-pack consistency appendix.
4. **Every product bumped one version, previous version archived whole, IPB adopted, product deltas applied:**
   - **LawDocs v1.1** — Investors page, social footer, application display name, blog toggle and user posts, Resources library, multi-provider AI and image generation, vendor assurance mirror, feedback/idea board, calendar port, env/seeds, design brief, content deck v1.1, session-prompt addendum.
   - **LawDocsComply v1.3** — the full policy set drafted (new Appendix AD), public Brand Studio, vlog, blog toggle/bulk/user posts, Resources library, Team/Investors pages, vendor assurance room with cadence (core value for RE tenants), feedback, multi-provider AI, env/seeds, design brief, website content deck (new).
   - **Equator v3.2** — new phase P22 Vidhi AI Employee & Knowledge Notebooks (NN-01 preserved; 12 locked actions each with a passing scenario), per-field "i" registry, Jupitice-inspired website content deck (≈18,700 words incl. Governance, Advisory Council, Team/Leadership, Investors, Documentation hub, Resources), blog toggle/bulk/user posts, cloud/DB portability, env/seeds, design brief.
   - **Finbyx v1.6** — Node pin, IPB port mapping, new Phase 18A Vidhi AI Employee and Phase 21 Public Website/Studio/Blog/Resources/Policies, white-label brand packs for resale, "i" registry with regulatory-reference panel (≥400 terms), vendor assurance mirror, captions/low-literacy accessibility, env/seeds, design brief, website content deck.
   - **Udofin v1.3** — new Phases 20A Vidhi Borrower Assistant, 22 Public Website, 23 White-Label Brand Packs & DLA resale (decision 3 / model 4 resolved with RBI DL 2025 role rules), "i" registry (262 seed terms), RE due-diligence cadence room, 12-locale accessibility, env/seeds, design brief, website content deck.
   - **Operations Hub v1.1** (largest delta) — product workspaces and `product_scope` segregation, HR expansion (remote work, intern programme, attendance, payroll engine, expenses), new phases O14 Project Management & Work OS, O15 Knowledge Hub (RBI/SEBI/IFSCA/IRDAI/MCA/Labour/Tax/Data Protection/Policy-drafting notebooks) & Vidhi AI, O16 Marketing/Brand/Media/WhatsApp-Meta, O17 Group Website/CMS/Vendor Assurance system of record; MS 365 deep integration; env/seeds; design brief; group-site content deck.
5. **Adversarial review and logic tests** — each product agent self-reviewed; then three independent reviewers covered IPB+Spec, OH/FBX/UDF and LD/LDC/EQ (red-team scenarios, state-machine walks, ID collisions, regulatory sanity, markdown). Totals: High 6 (all fixed; e.g., LD FR-P20 ID collision, IPB data-class taxonomy mismatch, environment-name mismatch letting seeds into pre-prod, API-key scope escalation gap, MCP write on locked action gap), Medium ≈30 (all fixed), Low ≈25 (most fixed). Logs: `IPB …/_review/IPB_v1.0_adversarial_review_log.md`, each pack's `_review/<version>_upgrade_review_log.md`, OH Appendix F, FBX Appendix E.6, UDF Appendix E.5, Spec Part 16.1.
6. **Cross-pack reconciliation** — Node 24.22.1 string identical in all seven documents; all superseded event names replaced by the canonical Spec v1.2 names; Equator and Udofin extra proposals tagged `[PROPOSED for Spec v1.3]`; IPB-01 port catalogue extended with Hub and lending ports.
7. **Outputs regenerated** — 21 Word files (pandoc, house reference: A4, navy headings): consolidated pack docx for LD/LDC/EQ, master+runbook pairs for FBX/UDF/OH, Spec, IPB, content decks, condensed LD/LDC editions, supplements. Credentials files are deliberately excluded from every docx.

## 2. Where everything is

| Product | Current | Archived previous |
|---|---|---|
| IPB (new) | `Finbyx and Udofin Prompts/Ecosystem/Infrabyx Platform Baseline Standard v1.0/` | — |
| Ecosystem Spec | `Ecosystem/Infrabyx_Ecosystem_Integration_Spec_v1.2.md/.docx` (+ `_Change_Summary.md`) | `Ecosystem/Earlier versions/…v1.1` |
| LawDocs | `LawDocs Prompt/LawDocs Build Prompt Pack v1.1/` | `LawDocs Prompt/_Archive (older versions)/…v1.0/` |
| LawDocsComply | `LawDocsComply Prompt/LawDocsComply Build Prompt Pack v1.3/` | `…/_Archive (older versions)/…v1.2/` |
| Equator | `Equator Prompt/Equator Build Prompt Pack v3.2/` | `…/_Archive (older versions)/…v3.1/` |
| Finbyx | `Finbyx/…_v1.6.md/.docx` + `Finbyx/v1.6 supplements/` | `Finbyx/Earlier versions/` |
| Udofin | `Udofin/…_v1.3.md/.docx` + `Udofin/v1.3 supplements/` | `Udofin/Earlier versions/` |
| Operations Hub | `Operations Hub/…_v1.1.md/.docx` + `Operations Hub/v1.1 supplements/` | `Operations Hub/Earlier versions/` |

The v1.0/v1.2/v3.1/v1.5/v1.2/v1.0 files that sat beside the new ones at the top level were left in place (nothing is deleted; deletion needs your approval on the computer). You may delete those top-level duplicates — the archive folders hold identical copies.

Per product, the new supplements are: `env/.env.example`, `env/SEED_CREDENTIALS.md`, `env/README.md`, `design/UI_UX_Design_Brief_<v>.md`, `content/<Product>_Website_Content_v1.x.md`, new phase files, and (LD/LDC) `condensed/<v>_Session_Prompt_Addendum.md`.

## 3. How to run a build with Claude Code

1. Create the product repository; commit the IPB folder as `docs/ipb/`, the Ecosystem Spec as `docs/ecosystem/`, and the product pack under `docs/` as its README describes.
2. First session: *"Read docs/ipb/00_README.md, then IPB-01, IPB-02, IPB-09 and IPB-11 in full, then the product master prompt and Phase 0/P00. Write the Phase 0 plan and stop for my approval."*
3. Copy `env/.env.example` to `.env.local` and fill it; run `pnpm seed --profile dev` — the seed reads `SEED_CREDENTIALS.md` and refuses to run with `APP_ENV=production`.
4. Follow the phase runbook; every phase stops at its exit gate.

## 4. Seed credentials (non-production only)

Seeds work only in local/dev/test/staging/demo/preview. Production refuses seed profiles; the first production login forces a password change and MFA enrolment. Keep this file and the per-product `SEED_CREDENTIALS.md` out of git (already in `.gitignore` per IPB-11).

**LawDocs v1.1**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `^qkiDA!WC8jrxc##i88PU30L=M` |
| test.tenant_admin | test.tenant_admin@lawdocs.test | `un8%OZ8pHD=Ek^xG1o*tayJ1NO` |
| test.maker | test.maker@lawdocs.test | `gkX4lO6hCma7ZH2UV_JY&lN8o4` |
| test.checker | test.checker@lawdocs.test | `^BOG%5l%lN0gULbatYswaMU2L1` |
| test.individual | test.individual@lawdocs.test | `hOSSLS5nTNAv*_5VQ^8Y%f#08s` |
| test.professional | test.professional@lawdocs.test | `d-yGthAw!sXW&G47aLA4*!#eTF` |
| test.counterparty | test.counterparty@lawdocs.test | `j$g4YLd*J=%9O%8fyYJzMg-xk*` |
| test.auditor_ro | test.auditor_ro@lawdocs.test | `kScMP6gWUi+yqIOJ$*mJB+xUGh` |
| test.content_editor | test.content_editor@lawdocs.test | `!Dan8__7iijDOYAVq$J3aI92%8` |

**LawDocsComply v1.3**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `!kbgGzJLo+DRv7P1sn=kVC+5pN` |
| test.tenant_admin | test.tenant_admin@lawdocscomply.test | `Z$vakEEJ@=Q%QeZzXNF2%K#JDJ` |
| test.compliance_maker | test.compliance_maker@lawdocscomply.test | `F&GZ8S4FJ@@pUieLo23SlVOSt9` |
| test.compliance_checker | test.compliance_checker@lawdocscomply.test | `5^Db%4_kmh5QGvJi8cPSqQm5KA` |
| test.cro | test.cro@lawdocscomply.test | `&C1z&qxao4-5JYfz*meG%_y#vT` |
| test.board_member | test.board_member@lawdocscomply.test | `68#ltman6=njvNIS!b2M$&dJyW` |
| test.auditor_ro | test.auditor_ro@lawdocscomply.test | `G4Ot^Fy#VnDadbN+wSfC60sPkJ` |
| test.content_editor | test.content_editor@lawdocscomply.test | `7niA3dNL96KF*-ALm*mr3JegvU` |

**Equator Resolution v3.2**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `DcZYc7@Ida5kqfgXFb-LclJI^r` |
| test.tenant_admin | test.tenant_admin@equator.test | `JG7Zbos&kHhn$lT^&#O-UsAPfE` |
| test.claimant | test.claimant@equator.test | `HZbyfTY%w9qg9DGw@C$d=PcLkf` |
| test.respondent | test.respondent@equator.test | `O-FN^LIfoFt3B#PKZ_*iKDqVAL` |
| test.neutral | test.neutral@equator.test | `mZbvs*K4TSM=ldphJevM3$3xy_` |
| test.case_manager | test.case_manager@equator.test | `eE#YJQ%Z#Z*v5kO6A0lH3G7=#W` |
| test.enterprise_admin | test.enterprise_admin@equator.test | `=r5O=xe-Q59Y*@a4-MO%8oZtNR` |
| test.auditor_ro | test.auditor_ro@equator.test | `$EFf7CJWt_%4GUvZzC&hWvBKxS` |
| test.content_editor | test.content_editor@equator.test | `34gFyh8T@XHE5RsJa-zPwM+Mt3` |

**Finbyx v1.6**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `CBV3MfuX-hnv1!KIoa2DU6vSiI` |
| test.tenant_admin | test.tenant_admin@finbyx.test | `*MCYS&9waaSt=dXokjGeGBsaUe` |
| test.credit_maker | test.credit_maker@finbyx.test | `yrccZZy6R#q6o4JJXqKF$GJV2Z` |
| test.credit_checker | test.credit_checker@finbyx.test | `mt--4YF-8qo-*X3=y^TuTe7iO8` |
| test.branch_user | test.branch_user@finbyx.test | `S^TnsDE_TOAx9gmM-dqjV70kF0` |
| test.collections | test.collections@finbyx.test | `!r1!$hLymHEu4w1TF$@SS7X_Sv` |
| test.finance | test.finance@finbyx.test | `!muR26qFs=HUbMarcz6WNUk#qd` |
| test.borrower_portal | test.borrower_portal@finbyx.test | `x1zZQ3S4J+p!xuJDuqKL6PAaXX` |
| test.auditor_ro | test.auditor_ro@finbyx.test | `BeL^_r%ICM^QtlQUkpdkZEi^$8` |
| test.content_editor | test.content_editor@finbyx.test | `7pSB4-=ATfu37Aas!%YzC%%gJL` |

**Udofin v1.3**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `jUwAf3i32^9Ien*6ga8NbGO=b6` |
| test.tenant_admin | test.tenant_admin@udofin.test | `sY7yD4Do3=&UL3moNm0Ev0&@A3` |
| test.re_admin | test.re_admin@udofin.test | `Vg^tWe3sKZPKAW6PmDiWobrHu8` |
| test.borrower | test.borrower@udofin.test | `#HRZyJ2yUL9Jd^xnmD!D#$a%-q` |
| test.grievance_officer | test.grievance_officer@udofin.test | `EZimWE0mDN8V-m48MGPLI^ZQv3` |
| test.ops | test.ops@udofin.test | `25X5MWSf+fYfQl0fbwB1IRCHdu` |
| test.auditor_ro | test.auditor_ro@udofin.test | `&=+2*Otn9rwej6TuaOJoV$&Kqk` |
| test.content_editor | test.content_editor@udofin.test | `zxRQ2DzzK6l=^SxYrcei6-oAOp` |

**Operations Hub v1.1**

| Persona | Email | Password (non-production only) |
|---|---|---|
| super_admin | rjnprajapati@gmail.com | `s@sV-*1-KUA5os4yU@Chj74DFn` |
| test.ops_admin | test.ops_admin@opshub.test | `JsBveaC7WOmv^Ef8dnMAq7g+KP` |
| test.rm | test.rm@opshub.test | `!BMyKX7WTFj&_RY*hawgZgsnK+` |
| test.support_agent | test.support_agent@opshub.test | `BCUaW_c_eWa#OjvwlOOpT4WSR=` |
| test.hr_admin | test.hr_admin@opshub.test | `69AcqOnGd&_2MM%jIVFKthwiFK` |
| test.payroll_maker | test.payroll_maker@opshub.test | `tl-FcMlN*=Juo83-LnYxtyvsav` |
| test.payroll_checker | test.payroll_checker@opshub.test | `M^9iEo=VmFWnL9VClvq7wsxTcQ` |
| test.marketing | test.marketing@opshub.test | `-Pb#^eGVoBn^nf2FAb9VSy#MFJ` |
| test.intern | test.intern@opshub.test | `dGuO1Um@AMn^1=xOC!R!DqY&4z` |
| test.employee | test.employee@opshub.test | `HfjI&D1Xp_l@3W4aqYJ&D2Y9*g` |
| test.auditor_ro | test.auditor_ro@opshub.test | `TGUeXAENjgkyOHMKinLJVQqp7+` |
## 5. Open questions for the owner (new in this upgrade; each pack README has the full list)

1. **Investors page** — publish for which products; which documents are gated; counsel to approve wording (Companies Act private-placement safe) before the toggle goes ON.
2. **White-label resale entity** and commercial terms for Udofin and Finbyx brand packs; for Udofin, confirm the RE remains DLA/CIMS owner (RBI Digital Lending Directions 2025) and obtain the legal note before Phase 23 is built.
3. **Payroll** — in-house engine (OH10) or payroll-provider adapter first; intern stipend policy and certificate wording.
4. **WhatsApp BSP** (Gupshup / JioCX / Meta direct) and the entity for Meta business verification.
5. **Tag management** — GTM web container vs server-side tagging vs none (privacy-first default is server-side).
6. **Image generation** provider for marketing and whether human review is mandatory before publishing synthetic images (recommended yes; labelling is mandatory under the IT Rules).
7. **Alternative adapters to contract first** — one alternative per Tier-0 port must be live in CI (e.g., a second object store, a second payment gateway, a second LLM provider).
8. **Microsoft 365 plan actually held** (carried over from every pack — "Business Starter" is a Google Workspace name).
9. **Policy drafts** — approve IPB-05 / LDC Appendix AD / LD Appendix O for counsel review; supply entity particulars (CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer).
10. **Blog contributor programme** — which user roles may post (customers, verified professionals, educators, neutrals) and the moderation SLA.
11. **Vidhi AI display name** on white-label plans (kernel stays Vidhi; tenants may override).
12. **Preview-environment database provider** (Neon/Supabase branch vs Testcontainers) and preview domain.

## 6. Items left for later editions

- IPB v1.1: unify the requirement-table "Tier" column semantics; add `PLT_ACCESSIBILITY_LEAD` to the role registry.
- Ecosystem Spec v1.3: consider `lending.LenderDisclosurePublished`, `vidhi.LockedActionAttempted`, `cms.UserPostModerated`, `content.HelpTermPublished`.
- LawDocs: Appendix Z/V census rows for FR-P20-52…55; Appendix R §R.14 index.
- LawDocsComply: Appendix AC totals recompute; pre-existing duplicate FR-P07-54…59 / FR-P14-30…32 from v1.1/v1.2.
- Equator: re-run the Appendix C/S extraction script for the new P22 screens and roles.
- Condensed LD/LDC editions are the previous edition carried forward with the new changes in front; a full re-condensation is a later task.
