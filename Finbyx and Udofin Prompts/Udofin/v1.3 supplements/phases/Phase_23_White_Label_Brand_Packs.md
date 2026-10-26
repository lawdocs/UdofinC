# Phase 23 — White-Label Brand Packs and DLA Resale

**Udofin Master Prompt v1.3 · Part 7I IB3 · 26 October 2026 · Product code UDF**

**Binding files:** Udofin Master Prompt v1.3 (Part 7I IB3; Part 3.1 operating model 4; Part 4.6–4.7; U23; Part 7B UP1, UP2 sections 7 and 11, UP5; Part 7H RA4.2; Part 10.3; Appendix B items 3, 48–50; Appendix G); IPB-04 §04.3.2 (Brand Studio and `brand_pack`), §04.3.8 (footer), §04.3.9 (CMP); IPB-05 (policy instances); IPB-08 (Trust Centre under tenant hosts); IPB-09 (release pipeline); IPB-10 (`WhiteLabelTenantProvisioned`); IPB-02 (host validation, isolation); `Agreements/Udofin_LSP_Agreement_Model` (schedule WL). Precedence: master prompt → IPB → Ecosystem Spec → this file → appendices; Part 8A prevails on regulatory points.

**Branch:** `cc/p23-brand-packs` · **Depends on:** P, 3c, 17, 22, 20b (OH8) · **Gate:** Appendix B item 48 (resale entity and commercial terms) and the §2 legal note recorded in `docs/decisions/`; the phase stops after the verification step if either is missing · **Position in order:** after 20d, before 21.

---

## 1. Purpose and what is being resolved

Udofin v1.2 left three open points: Appendix B decision 3 (one Udofin-branded app or also RE-branded white-label apps), Part 3.1 operating model 4 ("White-label DLA [assess]: produce an ADR and a legal note before building it"), and U23 ("White-label build pipeline [assess]"). IPB-D-10 fixes the mechanism group-wide: a shared `brand_pack` object keyed by host, used by Udofin and Finbyx for resale. This phase turns the mechanism into Udofin's full specification: the legal frame, the pack object with Udofin's fields, the guard-rails that no pack can override, co-branding rules, the provisioning and exit workflows, store identity and signing by the RE, the CIMS and DLA register consequences, OH8 billing, settings, screens and the acceptance tests — including host-header spoofing.

**Decision recorded (resolves Appendix B item 3).** The default remains one Udofin-branded multi-lender app on Udofin's developer accounts. RE white-label packs are an optional, RE-paid service built only as `brand_pack` instances published under the RE's own store accounts and domains, single-RE by default, after the owner records item 48 and counsel's note. `theme_config` is superseded by `brand_pack`; token names migrate one-to-one.

## 2. Legal frame [LAW] [INTERP] [COUNSEL]

| # | Point | Position built into the product | Basis | Status |
|---|---|---|---|---|
| L1 | Whose DLA is a white-label app? | An app published under the RE's brand and store accounts is the **RE's own DLA** (CF Annex-I owner: "self"). Udofin is the technology service provider and, where it also sources or services through that app, the LSP for those activities. The DLA register line carries owner = RE, the RE's GRO, and Udofin's nodal officer as the LSP contact where LSP activity exists | CF para 4(1)(x), (xix); para 18(1)–(4) and Annex-I footnotes | [VERIFY: Annex-I owner semantics and whether the LSP nodal officer column is populated for RE-owned DLAs] |
| L2 | Does the multi-lender neutrality rule (CF para 7) apply? | **Single-RE pack:** the DLA shows one RE's products only; there is no offer comparison and para 7's comparison duties do not arise, while the RE's own disclosure duties (KFS, APR, GRO) do. **Multi-RE pack** (an RE-branded marketplace showing other REs' offers): para 7 applies in full; the RE is a listed lender like any other; ranking by the published metric; no self-preference. Multi-RE packs are blocked until a written legal opinion is recorded | CF para 7(1)–(4); Part 4.6 default | [INTERP: legal opinion required for multi-RE packs; Appendix B item 49] |
| L3 | Who is the data fiduciary? | The RE for borrower data processed through its pack; Udofin is the processor and keeps only basic minimal data within the LSP agreement (CF para 14(1)); RE-controlled keys where the RE requires (OUT para 97(vii)(b)); the pack's policy set names the RE as fiduciary and Udofin as processor | CF para 14; DPDP s.2(i), (k), s.8; OUT para 97 | [COUNSEL: policy wording] |
| L4 | Store accounts and signing | The RE owns the Google Play developer account and Apple Developer Program membership, completes the Play financial-features and personal-loan declarations and App Store financial information for its own app, and holds the signing authority (Play App Signing under the RE's account; Apple distribution certificate owned by the RE's team). Udofin is invited as a developer with least privilege and never publishes under its own account for a pack | Google Play Financial Services policy; Apple Developer Program Licence Agreement; RA4.2 | [VERIFY: current store policies on third-party-built lending apps and account ownership] |
| L5 | Contract | The LSP agreement gains schedule WL (white-label): scope, store-account duties, build and release obligations, data ownership and keys, incident notice, brand licence (RE → Udofin for rendering only), exit cooperation, fees (OH8), audit rights, CIMS duties | OUT paras 17, 34, 74, 97; CF para 18 | [COUNSEL: schedule WL in `Agreements/Udofin_LSP_Agreement_Model`] |
| L6 | Outsourcing | The RE's board-approved outsourcing policy must cover the arrangement; Udofin supplies the IB5 due-diligence pack and the per-pack SBOM, permission manifest and release notes | OUT paras 17, 34, 61, 74 | [RE] |
| L7 | Udofin identity | Where Udofin performs LSP activity through a pack, the LSP identity is disclosed in the About screen, the footer and the disclosure page ("Technology and lending services by Udofin, a Lending Service Provider") and Udofin's nodal officer is reachable; no Infrabyx group mark appears on borrower screens of a pack | CF paras 9(5), 18(6); OUT para 46 | [VERIFY: exact wording with counsel] |
| L8 | Co-operative societies | No white-label pack for a non-RE society tenant (`NON_RE_COOP`) until app-store policy for non-RE lenders is confirmed (Appendix B item 32) | Store policy; UP4 | [GATE] |

## 3. Functional requirements

### 3.1 Pack object, hosts and resolution

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-23-01 | `brand_pack` follows the IPB-04 §04.3.2 shape plus Udofin fields: `re_tenant_id`, `dla_register_ids[]`, `lender_scope` (`single` \| `multi`), `cims_owner` (= `RE`, FIXED), `gro_contact_ref`, `lsp_disclosure_mode` (`lsp_active` \| `tech_only`), `lsp_schedule_ref`, `release_channel`, `store_identity.signing_owner` (= `RE`, FIXED), `store_identity.play_developer_account`, `store_identity.apple_team_id`, `status`. The default Udofin pack has `re_tenant_id = null`, `lender_scope = multi`, `cims_owner = LSP`. | M | AT-23-01 |
| FR-23-02 | `theme_config` records migrate to `brand_pack.tokens` one-to-one; a compatibility view keeps the old reads working until Phase 23 exit; no new write to `theme_config`. | M | AT-23-02 |
| FR-23-03 | Hosts: RE-owned domains only; each host is verified by DNS CNAME to the Udofin edge plus HTTP-01 certificate issuance through `DNS_CDN`; a host may belong to one published pack only (save-time error `IPB-BRD-011`); preview hosts (`*.preview.udofin.in`) are never valid pack hosts; `localhost` and IP literals are refused. | M | AT-23-03 |
| FR-23-04 | Host resolution: the edge validates `Host` and `X-Forwarded-Host` against the published host allow-list before any application code runs; the application resolves the pack only from the validated host; an unknown or spoofed host receives the default Udofin pack with `noindex` and `IPB-BRD-010` logged; the pack id never comes from a cookie, query string or header set by the client. | M | AT-23-04 |
| FR-23-05 | Mobile apps resolve the pack from the build-time `EXPO_PUBLIC_BRAND_PACK_ID` injected per EAS channel; the API cross-checks the app's bundle id against the pack's `store_identity` on every authenticated call (`IPB-BRD-012` on mismatch). | M | AT-23-05 |
| FR-23-06 | Per host the renderer serves the pack's favicon set, web manifest, OG image, self-hosted fonts, email identity, footer, consent banner configuration, policy set, sitemap and robots; cross-pack asset URLs are host-bound (signed with the host) so that pack A's assets cannot be fetched from pack B's host. | M | AT-23-06 |

### 3.2 Guard-rails, co-branding and regulatory text

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-23-10 | **Non-themeable set** (render in the default reading style regardless of pack): KFS and its line items, consent notices and purpose screens, cooling-off card and exit control, grievance block and escalation chain, LSP identity strip and disclosure page, AI disclosure, DLG disclosure, store-filter notices, error and permission-denied texts. The renderer applies `tokens.regulatory` from the default pack and ignores pack overrides for these components (unit test per component). | M | AT-23-10 |
| FR-23-11 | **Structural set** (unchangeable by pack): the five-tab shell; one primary action per screen; consent-first and explain-why flows; permission manifest (a pack cannot add a permission or an SDK); the ranking engine and offer-view layout for multi packs; the DLA register line per pack per platform; the Claims Register and copy linter; the contrast guard; the forced-update and minimum-version rules. | M | AT-23-11 |
| FR-23-12 | **Changeable by pack**: colour, type (from the approved self-hosted font list), logo, display name, terminology map (including `vidhi`), hosts, email identity, footer content within required blocks, policy particulars, store identity, RE help-centre articles, tours and imagery, Resources selection. Every change passes the contrast guard and the linter. | M | AT-23-12 |
| FR-23-13 | Co-branding (IB3.4): in the Udofin-branded app RE logos appear only in the offer view (equal size) and on RE artefacts; in an RE pack the RE brand owns the shell and the LSP identity line appears in About, footer and the disclosure page when `lsp_disclosure_mode = lsp_active`; no Infrabyx group mark on borrower screens; the Trust Centre is shown under the RE host only when `trust_centre_visible` is on and content stays Infrabyx's statements about Infrabyx. | M | AT-23-13 |
| FR-23-14 | Single-RE packs hide the loan chooser's lender comparison and the unmatched-lender list; the RE's products render as the RE's own catalogue with KFS, APR, GRO; multi-RE packs render the full neutral offer view with the RE as a listed lender and pass the para 7 neutrality suite. | M | AT-23-14 |
| FR-23-15 | Vidhi display name per pack through `terminology.vidhi`; the first-turn disclosure keeps "an AI assistant" verbatim; borrower answers in a pack name the RE as lender exactly as in the Udofin app. | M | AT-23-15 |

### 3.3 Pack lifecycle, provisioning and exit

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-23-20 | Pack states: DRAFT → LEGAL_REVIEW → RE_COUNTERSIGN → STORE_PENDING → PUBLISHED → SUSPENDED → PUBLISHED; PUBLISHED \| SUSPENDED → EXITING → EXITED; any pre-PUBLISHED state → CANCELLED. Every transition is maker-checker and audited; a published revision is immutable; rollback creates a new published revision from a prior body. | M | AT-23-20 |
| FR-23-21 | Entry to LEGAL_REVIEW requires: deal in PILOT or ACTIVE with UP2 sections 7 (branding) and 11 (DLA listing) approved, schedule WL countersigned, `lender_scope = single` or a recorded legal opinion for `multi`, policy set drafted with the RE as fiduciary, no Infrabyx mark on borrower screens, contrast guard and linter clean, six-screen preview rendered. | M | AT-23-21 |
| FR-23-22 | Entry to RE_COUNTERSIGN requires the legal reviewer's approval of the guard-rail checklist (§6) and the L7 disclosure wording; the RE countersigns in the lender portal under its own maker-checker. | M | AT-23-22 |
| FR-23-23 | Entry to STORE_PENDING requires: hosts verified and certificates issued; email identity verified (SPF, DKIM, DMARC) or `IPB-BRD-005`; policy set published; DLA register lines created per platform with owner RE and `LenderDlaLineCreated` emitted; store identity recorded with the RE as account owner and Udofin as least-privilege developer; EAS channel created; build from the current protected tag with the pack's identifiers injected at build time. | M | AT-23-23 |
| FR-23-24 | Entry to PUBLISHED requires: the RE's written CIMS confirmation for each DLA line uploaded and checked (Appendix B item 1 rule applied per pack); store review passed per platform (web may publish first; a store platform publishes when its review passes and its CIMS confirmation exists); `in.infrabyx.tenancy.WhiteLabelTenantProvisioned.v1` emitted exactly once per publish (idempotency key = pack id + revision). | M | AT-23-24 |
| FR-23-25 | Failure paths: host verification fails (stay DRAFT, 30-day timer `brand.pack.host_verification_days`, then CANCELLED unless extended); store rejection (STORE_PENDING with reason; resubmission only after legal review of any change); CIMS confirmation missing (blocked with explain-why); deal SUSPENDED (pack SUSPENDED: the app shows the UP5 hold text, no new applications, servicing view readable); deal TERMINATING (pack EXITING). | M | AT-23-25 |
| FR-23-26 | Exit (IB3.6): EXITING triggers the exit runbook to the RE (unpublish listings, 15-day in-app borrower notice, fallback host offer), keeps the servicing view and downloads for the UP5 post-exit window on the RE host or a Udofin fallback host with the RE's consent, runs data return and purge per UP5, releases hosts and certificates, emits `BrandPackExited`, and delivers the CIMS cessation notice to the RE (CF para 18(2)); after EXITED the pack host returns 410 and the fallback servicing view remains until the window ends. | M | AT-23-26 |
| FR-23-27 | Release pipeline: a pack build uses the same protected tag and SBOM as the Udofin app; the store-declaration gate (RA4.2) compares the pack's manifest, Info.plist, privacy manifest, Data safety form and partner list against the approved versions per pack; OTA updates apply per channel under the same OTA policy (JS and assets only; never permissions, consent, disclosures, payments, security). | M | AT-23-27 |
| FR-23-28 | Billing (IB3.7): on PUBLISHED, stream S08 one-time build fee and a monthly platform fee per pack under the deal's pricing model are recorded as `UsageRecorded` (`meter_kind = USAGE`, pack id as the meter key) to OH8; nothing is charged to borrowers; the ranking engine has no access to pack fees. | M | AT-23-28 |

### 3.4 Tenancy, security and operations

| ID | Requirement | Tier | Test |
|---|---|---|---|
| FR-23-30 | Publish and rollback are maker-checker (`PLT_SUPER_ADMIN` or `PLT_RELEASE_MANAGER` as checker; the RE countersign is a separate approval); the author cannot approve. | M | AT-23-30 |
| FR-23-31 | Pack-scoped isolation: assets, policies, help articles, tours, email identity and users are reachable only under the pack's hosts and the RE's tenant; cross-pack fetches return 404; RLS on `brand.*` tables by `re_tenant_id`; the default pack is readable by all hosts for the fallback case only. | M | AT-23-31 |
| FR-23-32 | Secrets: signing keys, store API keys and the RE's developer credentials are never stored by Udofin; EAS credentials for a pack channel are the RE's, granted to the CI through a scoped, expiring token held in the per-RE vault; pack identifiers are injected at build time and never committed. | M | AT-23-32 |
| FR-23-33 | Observability per pack: host health, certificate expiry, store review state, OTA adoption, crash-free rate per channel; alerts to the ops Work Inbox; the RE sees its pack's status in `Settings › Customisation › Branding`. | S | AT-23-33 |
| FR-23-34 | Vendor assurance: each pack publishes its SBOM, permission manifest and release notes to the RE's `Settings › Security & trust › Vendor documents` (IB5) on every release. | M | AT-23-34 |

## 4. Data model (schema `brand`)

| Table | Fields | Notes |
|---|---|---|
| `brand.pack` | `brd_id`, `product` (UDF), `re_tenant_id?`, `status`, `lender_scope`, `cims_owner`, `lsp_disclosure_mode`, `app_name`, `terminology jsonb`, `legal_entity jsonb` (RE: name, CIN, RBI CoR, registered office), `tokens jsonb`, `logo jsonb`, `favicon_set_id`, `og_default_media_id`, `fonts_self_hosted bool`, `email_identity jsonb`, `policy_set_id`, `consent_banner jsonb`, `footer_id`, `sitemap jsonb`, `analytics jsonb` (always none for packs in v1.3), `trust_centre_visible bool`, `lsp_schedule_ref`, `release_channel`, `published_revision_id`, `created_by`, `approved_by`, timestamps | RLS by `re_tenant_id`; default pack `re_tenant_id null` |
| `brand.pack_revision` | `rev_id`, `brd_id`, body jsonb (immutable), `published_at`, `published_by`, `checker_id`, `rollback_of?` | Immutable |
| `brand.host` | `host`, `brd_id`, `verification_state` (PENDING, VERIFIED, FAILED, RELEASED), `cname_checked_at`, `cert_state`, `cert_expires_at`, unique(host) | One host, one pack |
| `brand.store_identity` | `brd_id`, `platform` (android, ios, web), `bundle_id`, `store_listing_name`, `developer_account_ref` (RE), `signing_owner` (RE), `review_state`, `store_url`, `cims_confirmation_doc_ref`, `cims_confirmed_at`, `dla_register_id` | Links to `dla_register` |
| `brand.provisioning_run` | `run_id`, `brd_id`, Temporal workflow id, step states, blockers jsonb, timers | Workflow mirror |
| `brand.exit_run` | `brd_id`, exit plan ref, notice sent at, fallback host, data return cert ref, purge cert ref, cims cessation notice ref, `state` | UP5 linkage |
| `brand.guardrail_check` | `brd_id`, `rev_id`, checklist jsonb (each item pass/fail with evidence), `reviewer_id`, `approved_at` | §6 |
| `brand.usage_meter` | `brd_id`, period, meter kind, amount ref | OH8 feed |

## 5. State machines and scenario tables

### 5.1 Pack

| From | To | Guard | Event |
|---|---|---|---|
| DRAFT | LEGAL_REVIEW | FR-23-21 | `BrandPackStateChanged` |
| LEGAL_REVIEW | RE_COUNTERSIGN | FR-23-22 (guard-rail checklist approved) | " |
| LEGAL_REVIEW | DRAFT | changes requested | " |
| RE_COUNTERSIGN | STORE_PENDING | RE countersign recorded; FR-23-23 | " |
| STORE_PENDING | PUBLISHED | FR-23-24 per platform; web may publish first | `WhiteLabelTenantProvisioned` (once), `BrandPackPublished` |
| PUBLISHED | PUBLISHED | new revision through the same path | `BrandPackPublished` |
| PUBLISHED | SUSPENDED | deal SUSPENDED or security incident | " |
| SUSPENDED | PUBLISHED | deal resumed | " |
| PUBLISHED / SUSPENDED | EXITING | deal TERMINATING or RE request | " |
| EXITING | EXITED | FR-23-26 complete | `BrandPackExited` |
| any pre-PUBLISHED | CANCELLED | timer or decision | " |

| Scenario | Path | Expected |
|---|---|---|
| Happy | DRAFT → … → PUBLISHED (web first, Android after Play review and CIMS confirmation, iOS later) | Three `BrandPackPublished` revisions; one `WhiteLabelTenantProvisioned` per publish (idempotent); DLA lines active per platform with activation dates |
| Host verification never completes | DRAFT for 30 days | CANCELLED unless extended by ops with reason; hosts RELEASED |
| Play rejects the listing | STORE_PENDING (android: REJECTED) | Reason stored; resubmission requires legal review of any change; web stays PUBLISHED |
| CIMS confirmation missing for iOS | iOS cannot publish; Android and web unaffected | Explain-why on the blocked control; Work Inbox task to the RE |
| Deal suspended mid-life | PUBLISHED → SUSPENDED | App shows UP5 hold text within 15 minutes; no new applications; servicing readable |
| Two ops users publish the same revision | Optimistic lock | Second gets 409; one `WhiteLabelTenantProvisioned` |
| Event bus down at publish | Outbox | Event delivered on recovery; consumers idempotent on key |
| Rollback after a token mistake | New PUBLISHED revision from prior body | Maker-checker; audited; CDN purge |
| Exit | EXITING → EXITED | 15-day notice, listings unpublished by RE, fallback host serving read-only, data returned and purged per UP5, CIMS cessation notice, hosts 410 |

### 5.2 Host

PENDING → VERIFIED (CNAME and HTTP-01) → RELEASED (exit) ; PENDING → FAILED (72-hour retry window) → PENDING.

| Scenario | Expected |
|---|---|
| CNAME points elsewhere | FAILED with the observed record; retry |
| Certificate renewal fails 14 days before expiry | Alert to Work Inbox; fallback to default pack with `noindex` only after expiry, never silent |
| Host added to a second pack | `IPB-BRD-011` at save |
| Spoofed `X-Forwarded-Host` from an untrusted hop | Edge strips and validates; default pack + `noindex`; `IPB-BRD-010` logged |

### 5.3 Provisioning workflow (Temporal `WhiteLabelProvisioning`)

Steps: `gateCheck` → `legalReview` (signal) → `reCountersign` (signal) → `verifyHosts` (activity with retry) → `verifyEmailIdentity` → `publishPolicySet` → `createDlaLines` → `recordStoreIdentity` → `createEasChannel` → `buildPerPlatform` → `awaitStoreReview` (signal per platform) → `awaitCimsConfirmation` (signal per platform) → `publish` (per platform) → `emitProvisioned` → `startBilling`. Compensation: on CANCELLED release hosts, revoke CI token, deactivate DLA lines (cessation date), notify the RE.

## 6. Guard-rail checklist (legal reviewer; stored in `brand.guardrail_check`)

1. No Infrabyx group mark on any borrower screen; LSP identity line present where `lsp_active`.
2. KFS, consent, cooling-off, grievance, DLG, AI disclosure render in the default reading style on the pack (snapshot comparison).
3. Five tabs; no added tab; no promotional card on Home.
4. Permission manifest identical to the Udofin app; no additional SDK in the bundle (static scan).
5. `lender_scope` matches the opinion on file; single packs show no comparison; multi packs pass the neutrality suite.
6. Policy set names the RE as fiduciary and Udofin as processor; privacy, grievance and terms published; footer required blocks present (RE GRO, Udofin nodal officer where LSP activity, RBI Sachet, storage policy, ranking metric for multi packs).
7. Store identity owned by the RE; declarations completed by the RE; Udofin least-privilege developer.
8. DLA register lines drafted per platform with owner RE; CIMS confirmation process agreed with the RE.
9. Contrast guard and copy linter clean; display name and terminology contain no banned phrase; Vidhi disclosure intact.
10. Schedule WL countersigned; billing items mapped to OH8; exit runbook acknowledged by the RE.

## 7. Screens (Appendix G)

| Channel | Path | Content and actions | States |
|---|---|---|---|
| F | `Brand Studio › Packs` | List by RE and status with blockers; create wizard (RE, scope, hosts, legal entity, policy set, store identity, tokens, logo, display name, terminology, email identity); six-screen preview; guard-rail checklist view; submit for legal review; publish and rollback (maker-checker); exit | Empty; blocked with explain-why; conflict |
| F | `Brand Studio › Packs › [pack] › Hosts` | Host list with verification and certificate state, add/remove, DNS instructions | FAILED with observed record |
| F | `… › Store identity` | Per platform: bundle id, account owner, review state, CIMS confirmation upload check, DLA line link | Missing confirmation |
| F | `… › Releases` | Channel, builds, OTA adoption, crash-free, store-declaration gate results | — |
| D | `Settings › Customisation › Branding` | Pack view (read), request change, countersign queue (maker-checker), store-account checklist, CIMS confirmation upload, SBOM and release notes (links to Security & trust), pack status and timers | Pending countersign; suspended |
| C | `Partners › [deal] › White-label` | Status, timers, blockers, legal review link, billing items, exit runbook | — |
| A, B (pack) | `Account › About` | RE legal entity, app version, "Technology [and lending services] by Udofin" line where applicable, nodal officer, policies | — |

## 8. Settings keys (`brand.*`)

| Key | Default | Nature | Notes |
|---|---|---|---|
| `brand.packs.enabled` | false | GATE (Appendix B 48) | |
| `brand.pack.lender_scope.multi_allowed` | false | GATE (legal opinion; App B 49) | |
| `brand.pack.cims_owner` | RE | FIXED | |
| `brand.pack.signing_owner` | RE | FIXED | |
| `brand.pack.require_cims_confirmation` | true | FIXED | |
| `brand.pack.host_verification_days` | 30 | CEILING | |
| `brand.pack.cert_expiry_alert_days` | 14 | FLOOR | |
| `brand.pack.trust_centre_visible` | false per pack | COMMERCIAL (App B 50) | |
| `brand.pack.vidhi_display_name` | per pack | COMMERCIAL (disclosure FIXED) | |
| `brand.pack.analytics_allowed` | false | HARD_BLOCK in v1.3 | packs carry no marketing tooling |
| `brand.pack.exit_notice_days` | 15 | FLOOR | UP5 |
| `brand.pack.post_exit_servicing_days` | 90 | FLOOR | UP5 |
| `brand.pack.billing.stream` | S08 + platform fee | COMMERCIAL per deal | OH8 |
| `brand.pack.coop_tenants_allowed` | false | GATE (App B 32) | |

## 9. Events and error codes

**Internal (`in.udf.brand.*`, v1):** `BrandPackStateChanged`, `BrandPackPublished`, `BrandPackRolledBack`, `BrandPackSuspended`, `BrandPackExited`, `HostVerified`, `HostVerificationFailed`, `HostSpoofDetected` (no content), `CertificateExpiring`, `StoreReviewUpdated`, `CimsConfirmationRecorded`, `GuardrailCheckApproved`, `PackBuildCompleted`, `PackUsageRecorded`. **Existing:** `LenderDlaLineCreated`, `LenderDlaLineCeased` (U18), `LenderDealSuspended`/`Terminated` consumed (UP5).

**Ecosystem:** `in.infrabyx.tenancy.WhiteLabelTenantProvisioned.v1` (payload per IPB-10: `tenant_id`, `brd_id`, `hosts[]`, `legal_entity_ref`, `plan_id`, `store_identity`, `email_domain`, `provisioned_by`); `in.infrabyx.tenancy.BrandPackPublished.v1` (proposed; IB8); `UsageRecorded` to OH8.

**Errors:** `IPB-BRD-003` (contrast), `IPB-BRD-005` (email identity), `IPB-BRD-010` (host spoof → default pack), `IPB-BRD-011` (duplicate host), `IPB-BRD-012` (bundle id does not match pack), `UDF-BRD-020` (gate: item 48 or legal note missing), `UDF-BRD-021` (multi scope without opinion), `UDF-BRD-022` (CIMS confirmation missing), `UDF-BRD-023` (policy set not published), `UDF-BRD-024` (DLA line missing), `UDF-BRD-025` (regulatory component theming attempted — refused at save), `UDF-BRD-026` (coop tenant pack refused), `UDF-BRD-027` (host after EXITED → 410).

## 10. Acceptance tests (Gherkin; representative)

```gherkin
Feature: Host resolution and spoofing

  Scenario: AT-23-04 Spoofed Host header
    Given pack P1 is PUBLISHED for app.partnerbank.in
    When a request arrives with Host: app.partnerbank.in but X-Forwarded-Host: evil.example from an untrusted hop
    Then the edge rejects the forwarded host, the application serves the default Udofin pack with noindex
    And HostSpoofDetected and IPB-BRD-010 are logged without the request body

  Scenario: AT-23-04b Unknown host
    When a request arrives with Host: unknown.example
    Then the default Udofin pack is served with noindex and no pack tokens, legal entity or policies of any RE appear

  Scenario: AT-23-03 Duplicate host
    Given app.partnerbank.in belongs to PUBLISHED pack P1
    When an ops user adds app.partnerbank.in to draft pack P2
    Then the save is refused with IPB-BRD-011

  Scenario: AT-23-31 Cross-pack isolation
    Given packs P1 (RE_A) and P2 (RE_B) are PUBLISHED
    When P1's logo URL, policy page and help article are requested under P2's host
    Then every response is 404 and the assets' host-bound signatures fail

  Scenario: AT-23-05 Bundle id mismatch
    Given a mobile build with EXPO_PUBLIC_BRAND_PACK_ID = P1 but bundle id of P2
    When it calls the API
    Then the call is refused with IPB-BRD-012 and an alert is raised

Feature: Publish gates

  Scenario: AT-23-24 Publish without CIMS confirmation
    Given pack P1 at STORE_PENDING with Android review passed and no CIMS confirmation for the Android DLA line
    When the ops user tries to publish Android
    Then publish is refused with UDF-BRD-022 and the control explains the missing confirmation
    And web, whose confirmation exists, can publish

  Scenario: AT-23-23 Policy set not published
    Given pack P1 whose policy set is DRAFT
    Then the transition to STORE_PENDING is refused with UDF-BRD-023

  Scenario: AT-23-21 Multi-RE pack without opinion
    Given no legal opinion is recorded for RE_A
    When an ops user sets lender_scope = multi on RE_A's pack
    Then the save is refused with UDF-BRD-021

  Scenario: AT-23-30 Author approves own publish
    When the author of revision r3 attempts to approve it
    Then the approval is refused and r3 stays unpublished

Feature: Guard-rails

  Scenario: AT-23-10 Theme attempts to restyle the KFS
    Given pack P1 tokens set regulatory text to 9 px grey on grey
    When the KFS renders under P1's host and in the P1 app
    Then the KFS renders in the default reading style and the token save was refused with UDF-BRD-025

  Scenario: AT-23-11 Pack attempts to add a permission
    Given a pack configuration requesting READ_CONTACTS
    Then the build pipeline fails the permission manifest gate and no build is produced

  Scenario: AT-23-14 Single-RE pack shows no comparison
    Given pack P1 with lender_scope = single
    When a borrower opens Apply in the P1 app
    Then no offer comparison, ranking metric or unmatched-lender list is shown and every product carries RE_A's KFS and GRO

  Scenario: AT-23-15 Vidhi renamed
    Given P1 terminology.vidhi = "Sahayak"
    Then every surface says Sahayak and the first-turn disclosure still contains "an AI assistant"

Feature: Events and billing

  Scenario: AT-23-24b Idempotent provisioning event
    Given pack P1 publishes revision r1 and the bus redelivers the publish command
    Then exactly one WhiteLabelTenantProvisioned with key P1:r1 is observed by OH

  Scenario: AT-23-28 Billing never touches borrowers or ranking
    Given P1 PUBLISHED
    Then UsageRecorded for P1 reaches OH8 with meter_kind USAGE and no borrower key
    And the ranking engine's input schema has no field for pack fees (schema test)

Feature: Exit

  Scenario: AT-23-26 After exit
    Given P1 reached EXITED on 1 March with a 90-day post-exit window
    When app.partnerbank.in is requested on 2 March
    Then the response is 410 with the exit notice
    And an existing borrower can still open the servicing view and downloads on the fallback host until 30 May
    And the CIMS cessation notice to RE_A is on file
```

Further tests: AT-23-01 schema and FIXED fields; AT-23-02 `theme_config` migration equality; AT-23-06 per-host favicon, manifest and fonts; AT-23-12 contrast guard and linter on pack fields; AT-23-13 no Infrabyx mark in pack screenshots (image diff); AT-23-20 every transition audited and maker-checker; AT-23-22 RE countersign under RE maker-checker; AT-23-25 each failure path; AT-23-27 OTA policy and store-declaration gate per pack; AT-23-32 no RE credentials at rest in Udofin (secret scan + vault audit); AT-23-33 certificate alert at 14 days; AT-23-34 SBOM and release notes published to the RE's vendor documents on release.

## 11. Exit gate

- [ ] Appendix B item 48 and the legal note (L1–L7) recorded; `brand.packs.enabled` on for the pilot RE only.
- [ ] All FR-23 **M** requirements implemented with passing acceptance tests, including spoofing, duplicate hosts, cross-pack isolation, bundle-id mismatch, gates (CIMS, policy set, DLA lines, legal review, countersign), guard-rails, idempotent provisioning, billing and exit.
- [ ] `theme_config` fully migrated; no writes remain.
- [ ] One pilot pack published on web (and Android where the RE's Play review and CIMS confirmation are complete) with DLA lines owner RE and the RE's CIMS confirmation on file.
- [ ] Vendor documents (SBOM, permission manifest, release notes) visible to the RE; OH8 receives usage.
- [ ] Settings of §8 present as `module_setting` records; screens of §7 present with states; Appendix G and the DLA register documentation updated.
- [ ] Regulatory register updated (CF 4(1)(x), 7, 9(5), 14, 18 and Annex-I; OUT 17, 34, 46, 74, 97; store policies) with [VERIFY] items resolved or carried; ADR "White-label as RE-owned DLA; brand_pack supersedes theme_config" merged; runbook review gate evidenced.

## 12. Schedule WL — clause list for `Agreements/Udofin_LSP_Agreement_Model` [COUNSEL]

The LSP agreement model gains a white-label schedule. Clause headings and the product control that evidences each; counsel drafts the wording.

| WL clause | Content | Product evidence |
|---|---|---|
| WL-1 Scope and ownership | The white-label app is the RE's DLA; Udofin provides the technology and, where appointed, LSP services; the RE is the publisher of record on both stores and the owner of the domains | `brand.pack.cims_owner`, `store_identity.developer_account_ref`, `brand.host` |
| WL-2 Brand licence | The RE licenses its marks to Udofin solely for rendering the pack; Udofin's LSP identity line is permitted and required where LSP activity exists | `lsp_disclosure_mode`; guard-rail checklist item 1 |
| WL-3 Store accounts and declarations | The RE opens and maintains the developer accounts, completes the Play financial-features and personal-loan declarations and App Store financial information, holds signing authority, and grants Udofin least-privilege developer access | `store_identity`; RA4.2 gate; AT-23-32 |
| WL-4 CIMS and DLA register | The RE reports the pack's DLAs on CIMS as owner before any store submission and on every change; Udofin supplies the Annex-I extract and change notices | `dla_register` lines; `cims_confirmation_doc_ref`; `LenderDlaLineCreated/Ceased` |
| WL-5 Data roles | The RE is data fiduciary; Udofin is processor with basic minimal data; RE-controlled keys on request; India-only storage; sub-processor list and consents | Policy set; RE-scoped vault; IB5 documents |
| WL-6 Build and release | Same protected tags, SBOM and OTA policy as the Udofin app; store-declaration gate per pack; release notes to the RE's internal-audit contact; the RE may freeze releases on its pack | FR-23-27; IB7; REQ-IAF-23 |
| WL-7 Non-themeable and structural sets | The RE accepts that regulatory text and the structural set cannot be changed by the pack | FR-23-10, FR-23-11; guard-rail checklist |
| WL-8 Lender scope | Single-RE by default; multi-RE only with a written legal opinion and the para 7 duties accepted | FR-23-14; `UDF-BRD-021` |
| WL-9 Incidents | Notice to the RE within the OUT para 61 target (2 hours from detection) for incidents affecting the pack; joint CERT-In and DPDP handling | U24; IB5 `incident_notice_tenant` |
| WL-10 Fees | S08 one-time build fee; monthly platform fee per pack; paid by the RE; never charged to borrowers; invoiced by OH8 | FR-23-28 |
| WL-11 Audit and inspection | RE auditor and RBI access to pack-related records through RA2 grants; evidence pack per IB5 | RA2; IB5 |
| WL-12 Suspension and exit | Suspension mirrors the deal; exit runbook (listings, notice, fallback host, data return, purge, CIMS cessation); post-exit servicing window | FR-23-25, FR-23-26; UP5 |
| WL-13 Liability and indemnity | Counsel | — |
| WL-14 Term and termination | Counsel; aligned with the deal term | UP5 |

## 13. CIMS, DLA register and multi-lender implications (what changes versus the Udofin-branded app)

| Topic | Udofin-branded app | RE white-label pack (single) | RE white-label pack (multi) |
|---|---|---|---|
| CIMS Annex-I owner | LSP (Udofin) on each RE's line | RE ("self") | RE ("self") for its own line; each other RE listed on the pack reports the pack as a DLA on which it is present through its LSP agreement with Udofin [VERIFY] |
| GRO columns | RE's GRO; LSP nodal officer per para 18(4)(ii) [VERIFY] | RE's GRO; Udofin nodal officer where LSP activity | As single plus each listed RE's GRO in the app's disclosure page |
| Para 7 neutrality | Applies in full | Not triggered (one lender); RE product disclosures apply | Applies in full; RE is one listed lender; no self-preference |
| Offer view | Neutral comparison | RE catalogue (no comparison) | Neutral comparison with the published metric |
| Ranking metric publication | On udofin.com | Not applicable | On the pack's host and udofin.com |
| Store declarations | Udofin's accounts | RE's accounts and declarations | RE's accounts; partner list includes other REs |
| Store policy on personal-loan apps | Udofin complies | RE complies; Udofin supplies the evidence | RE complies; each listed RE's CIMS entry needed before listing |
| Data fiduciary | Each RE for its loan data; Udofin for its own minimal data | RE | RE for its own data; each other RE for its own loan data; policy set states this |
| DLG disclosure | Udofin's page per RE | RE's pack page if the RE has DLG arrangements through Udofin | As single plus each RE's disclosure |
| Vidhi | Vidhi | Renamed allowed; disclosure fixed | Same |
| Billing | Deal streams | Deal streams + S08 + platform fee | Same |

## 14. RE onboarding runbook for a pack (ops; delivered through `Partners › [deal] › White-label`)

1. Deal in PILOT or ACTIVE; UP2 sections 7 and 11 approved; schedule WL countersigned.
2. RE provides: legal entity particulars (CIN, RBI CoR, registered office), domains, brand assets (SVG logo, colours), display name, email domain, GRO contacts, policy particulars.
3. Ops drafts the pack; preview shared with the RE; legal reviewer runs the guard-rail checklist.
4. RE creates or confirms its Google Play developer account (organisation, D-U-N-S) and Apple Developer Program membership, completes the declarations, invites Udofin's CI identity with least privilege, and records the account references in the lender portal.
5. Hosts verified; email identity verified; policy set published; DLA lines created; the RE reports the DLAs on CIMS and uploads the confirmation.
6. Builds per platform; store review; publish per platform as confirmations arrive; web may lead.
7. Billing starts on first publish; vendor documents (SBOM, manifest, release notes) appear in the RE's Security & trust.
8. Quarterly: certificate and store-account health, CIMS line review, guard-rail re-check on major releases.

## 15. Open items carried into the decision log

| # | Item | Owner | Default until decided |
|---|---|---|---|
| 1 | Resale entity and commercial terms (Appendix B 48) | Owner | Packs disabled |
| 2 | Multi-RE pack legal opinion (Appendix B 49) | Counsel | Single only |
| 3 | Annex-I owner semantics and nodal-officer column for RE-owned DLAs | Compliance reviewer | Owner = RE; nodal officer shown where LSP activity |
| 4 | Store policy on third-party-built lending apps and account ownership | Mobile release lead | RE-owned accounts mandatory |
| 5 | Trust Centre under RE hosts (Appendix B 50) | Owner | Off |
| 6 | LSP identity wording in packs (L7) | Counsel | "Technology and lending services by Udofin, a Lending Service Provider" |
| 7 | Co-operative society packs (Appendix B 32) | Owner | Blocked |

## 16. Operational KPIs and KRIs for packs (feed RA1 and the ops Work Inbox)

| Measure | Target | Alert |
|---|---|---|
| Time from DRAFT to PUBLISHED (web) | ≤ 20 working days with a cooperative RE | > 30 days → ops review |
| Hosts with certificate expiring ≤ 14 days | 0 | Any |
| Packs with a DLA line lacking CIMS confirmation while a store listing is live | 0 (hard block) | Any → incident |
| Host spoof attempts per day per pack | — | > 50 → security review |
| Guard-rail snapshot regressions per release | 0 | Any → release halt |
| Crash-free sessions per pack channel | ≥ 99.5% | Below → staged rollout halt (RA4.2) |
| Exit runbooks completed within the UP5 window | 100% | Any slip → compliance |
