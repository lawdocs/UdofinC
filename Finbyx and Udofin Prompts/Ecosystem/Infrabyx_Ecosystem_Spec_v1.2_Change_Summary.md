# Infrabyx Ecosystem Integration Specification v1.2 — Change Summary and Review Log

**Date:** 26 October 2026 · **Owner:** Company Secretary, Infrabyx Group · **Spec file:** `Infrabyx_Ecosystem_Integration_Spec_v1.2.md` (≈52,200 words; v1.1 was ≈33,400) · **Classification:** minor version (Part 14.1) — no parallel run.

## 1. What changed (pointer list)

See the Spec's "What changed in v1.2" (top of file) and Part 16.1. Headline items: IPB v1.0 registered as companion with the precedence chain (How to use; 14.1); LawDocs registered as owner code `LD` with the full LawDocs Appendix Y change request absorbed (Parts 1–6, 8, 11–15; every item marked *(v1.2, from LD App. Y)*); principles 14–16; new 3.12 (runtime, port and error-code alignment); 4.8 `product_scope[]`; 4.9 Vidhi delegation; 5.4 `brand_pack` and white-label contract; 27 IPB-proposed events registered and every other IPB proposal mapped in 6.17; new domains 6.31–6.40; 12.5 LawDocs archive profiles and layouts; 14.3 three certification groups; Part 15 waves; Appendix A.6–A.10; Appendix C cross-pack consistency table.

## 2. Events registered in v1.2 (cite as `in.infrabyx.[domain].[Event].v1`)

| Section (domain) | Events | Count |
|---|---|---|
| 6.13 Documents (`documents`) | `DocumentDeposited` | 1 |
| 6.15 Compliance and GRC (`grc`) | `PolicyEffective`, `VulnerabilityRecorded` | 2 |
| 6.16 Platform and module lifecycle (`platform`) | `ProviderIncident`, `ExitDrillCompleted` | 2 |
| 6.27 Plans, billing and usage (`billing`) | `CatalogueChanged` | 1 |
| 6.29 Operations Hub (`ops`) | `TenantRegistered`, `SystemOfRecordSwitched`, `MarketplacePayoutSettled`, `MarketplaceTransferInstructed`, `ServiceOrderRouted`, `ServiceOrderStatusChanged`, `TenantSelfServeCreated`, `ClientHealthSignal`, `SurveyResponseRecorded`, `TimesheetAggregated`, `DeliveryMetricsMonthly`, `ServiceCreditIssued`, `ContentPublished`, `GrievanceStatusChanged` | 14 |
| 6.31 Legal work (`legal`) | `AgreementExecuted`, `AgreementAmended`, `AgreementTerminated`, `ContractObligationRegistered`, `ContractObligationStatusChanged`, `LegalMatterOpened`, `LegalMatterUpdated`, `LegalMatterClosed`, `CourtCaseRegistered`, `CourtCaseUpdated`, `CourtHearingScheduled`, `CourtOrderRecorded` | 12 |
| 6.32 Signing and stamping — the eSign hosted hand-off (`esign`) | `SigningRequestCreated`, `SigningRequestCompleted`, `SigningRequestDeclined`, `SigningRequestExpired`, `SigningRequestWithdrawn`, `StampInstrumentVerified` | 6 |
| 6.33 IP assets and engagements (`ip`, `engagement`) | `IpAssetRegistered`, `IpAssetStatusChanged`, `EngagementCreated`, `EngagementStatusChanged`, `RetainerActivated`, `RetainerEnded` | 6 |
| 6.34 Trust and vendor assurance publication (`trust`) | `VendorAssuranceDocumentPublished`, `VendorAssuranceDocumentStateChanged`, `VendorAssuranceDocumentAcknowledged`, `VendorAssuranceRequestOpened`, `AuditorGrantChanged`, `ClaimRegisterChanged` | 6 |
| 6.35 Tenancy, brands and white-label (`tenancy`) | `WhiteLabelTenantProvisioned`, `WhiteLabelTenantExited`, `BrandPackPublished` | 3 |
| 6.36 Vidhi cross-product delegation (`vidhi`) | `VidhiTaskDelegated`, `VidhiTaskAccepted`, `VidhiTaskCompleted`, `VidhiTaskRejected` | 4 |
| 6.37 Engineering and release communication (`eng`) | `ReleaseNotePublished`, `RolledBack`, `ExportMapBumped` | 3 |
| 6.38 Content and CMS syndication (`cms`, `content`) | `BlogPostPublished`, `ResourcePublished`, `GlossaryEntryPublished` | 3 |
| 6.39 CRM, marketing consent and messaging (`crm`, `consent`, `messaging`, `workforce`) | `LeadCaptured`, `MarketingConsentUpdated`, `WhatsAppTemplateApproved`, `CareerApplicationReceived` | 4 |
| 6.40 Feedback and identity preferences (`feedback`, `identity`) | `FeedbackSubmitted`, `FeedbackStatusChanged`, `UserPreferencesSynced`, `UserDeactivated` | 4 |

Total: 71 new events (27 from IPB proposals, 44 from LawDocs Appendix Y) and 20 new API endpoints. Superseded or non-canonical names (never emitted) are listed in Spec 6.17 "v1.2 additions" — product agents must replace any of those names in their packs with the canonical ones above.

## 3. Adversarial self-review (brief §4)

| Issue walked | Finding → fix | Spec section |
|---|---|---|
| Tenancy bypass / IDOR via new objects (brand packs, vendor documents, feedback, leads, delegations) | Every new object carries `tenantid` or `brd_id` and a consumer-side scope; `product_scope[]` default deny added for Hub staff; mirrors read-only; feedback and leads carry hashes and `fields_ref` fetched under scope | 4.8, 6.34, 6.39, 6.40, 14.3 |
| Host-header attacks on white-label hosts | Group host registry (`PUT /v1/hosts/{host}`), one host per pack group-wide, unknown or spoofed `Host`/`X-Forwarded-Host` → default pack with `noindex`; `brand-host-unknown` | 5.4, 6.35, 3.9, 13.3 |
| File-upload abuse (brand SVG/logo) | Media by reference only in the shared shape; SVG sanitised at upload (IPB-04-21); fonts WOFF2 self-hosted | 5.4 |
| Super-admin publish without checker | Pack publish requires maker-checker and `PLT_LEGAL_REVIEWER` for legal fields; `WhiteLabelTenantProvisioned` only after OH4 maker-checker | 5.4, 6.35 |
| Prompt injection into Vidhi via delegated inputs | `inputs_ref` treated as untrusted data; guards per IPB-02-72 / IPB-03-42; only read skills delegable until ADR | 4.9, 13.3 |
| Locked action attempted by an agent | `locked-action` 403, `VidhiTaskRejected` LOCKED_ACTION, auto-demotion; Gherkin test | 4.9, 6.36, 14.3 |
| Scheduled task after permission or consent revoked | Skip rule and internal `ScheduleRunSkipped` noted | 13.3 |
| Pixel firing before consent | No tag or pixel before CMP consent; `MarketingConsentUpdated` WITHDRAWN propagates ≤ 60 s; certification test | 6.39, 13.3, 14.3 |
| Payment webhook forgery / marketplace money | OH8 holds and executes Route transfers; LawDocs only instructs; idempotent RELEASE; disputes block release | 6.29, 14.3 |
| WhatsApp template abuse | Marketing templates only under `MARKETING_WHATSAPP` consent; collections use barred | 6.39, 14.3 |
| XSS/SSRF in syndicated content | Events carry URLs and metadata only; claims gate before publish; consumers render nothing inline from events | 6.38 |
| Seed leakage to production | Not a Spec concern (IPB-11); `environment` extension prevents sandbox events reaching production inboxes | 3.2 |
| New state machines walked (happy, failure, concurrency, rollback) | Vidhi delegation (4.9), signing hand-off (6.32), vendor-assurance mirror (6.34), white-label exit (5.4) | as cited |
| ID and section collisions | No duplicate `##` numbers; 71 unique (N12) names; error-prefix collision table; `in.infrabyx.*` grammar lint over the file passes except for intentionally listed superseded names | 3.12, 6.17, Appendix C |

## 4. Open items added (owner decisions)

Carried in Part 16.1: LawDocs OI-Y-01 to OI-Y-11; IPB open items 2 (white-label resale entity) and 4 (WhatsApp BSP); Payment Aggregator Directions paragraph refs; each product's confirmation of error-code prefix and export package name (Appendix C, marked [VERIFY]); `owner_readable` naming-mode acceptance; token-exchange parameters.
