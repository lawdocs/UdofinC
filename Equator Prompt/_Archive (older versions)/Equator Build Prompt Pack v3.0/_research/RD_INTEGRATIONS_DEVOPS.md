# RD — Productivity-suite integration, open CRM/marketing integrations, data portability, and engineering change/audit management

**Research stream:** v3.0 — Integrations & DevOps · **Prepared:** 23 October 2026 · **For:** Equator Resolution v3.0 writers (Operations Platform, HRMS, export, P00/P14 extensions)
**Extends (does not repeat):** Appendix D (ports, provider registry, `CRM_PORT`), Appendix F (append-only ledgers, `deny_mutation`), Appendix Q (SC-01…SC-22, ISO Annex A owner table, §7.3 change management), P00 FR-P00-04…09, FR-P00-20, ADR-0025, P14 FR-P14-04/06/11.

> Legend: **[V]** verified from the cited official page on 23 Oct 2026 · **[M]** vendor marketing claim · **[S]** secondary source · **[R]** recommendation · **[NC]** not confirmed.

## Sources
All accessed 23 October 2026.
1. Microsoft — Compare all Microsoft 365 business plans (India) — https://www.microsoft.com/en-in/microsoft-365/business/compare-all-microsoft-365-business-products — vendor doc / company self-description (prices)
2. Microsoft Learn — Exchange Online limits (service description) — https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits — vendor doc (official)
3. Microsoft Learn — Microsoft 365 for business security overview — https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-security-overview?view=o365-worldwide — vendor doc
4. Microsoft Learn — What is Microsoft 365 for business — https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/what-is-microsoft-365-for-business?view=o365-worldwide — vendor doc
5. Microsoft Graph — user: assignLicense — https://learn.microsoft.com/en-us/graph/api/user-assignlicense?view=graph-rest-1.0 — vendor doc
6. Microsoft Graph — Create user — https://learn.microsoft.com/en-us/graph/api/user-post-users?view=graph-rest-1.0 — vendor doc
7. Microsoft Graph — Configure application access policy (online meetings) — https://learn.microsoft.com/en-us/graph/cloud-communication-online-meeting-application-access-policy — vendor doc
8. Microsoft Graph — Create onlineMeeting — https://learn.microsoft.com/en-us/graph/api/application-post-onlinemeetings?view=graph-rest-1.0 — vendor doc
9. Microsoft Teams platform — Meeting transcripts and recordings overview — https://learn.microsoft.com/en-us/microsoftteams/platform/graph-api/meeting-transcripts/overview-transcripts — vendor doc
10. Microsoft Support — Restrictions and limitations in OneDrive and SharePoint — https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa — vendor doc
11. Microsoft Support — What are the file path length limits? — https://support.microsoft.com/en-us/onedrive/what-are-file-path-length-limits — vendor doc
12. Microsoft Learn — Naming files, paths, and namespaces (Win32) — https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file — vendor doc
13. Microsoft Graph — Throttling limits — https://learn.microsoft.com/en-us/graph/throttling-limits — vendor doc
14. Microsoft Learn — Microsoft 365 data residency overview — https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-overview?view=o365-worldwide — vendor doc
15. Microsoft Learn — Microsoft Purview service description (licensing guidance) — https://learn.microsoft.com/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description — vendor doc
16. Google Workspace — Pricing / compare editions — https://workspace.google.com/pricing — vendor doc / company self-description
17. Google for Developers — Google Meet REST API overview — https://developers.google.com/workspace/meet/api/guides/overview — vendor doc
18. Google for Developers — Directory API: Manage user accounts — https://developers.google.com/workspace/admin/directory/v1/guides/manage-users — vendor doc
19. Google Workspace Admin Help — Choose a geographic location for your data (data regions) — https://knowledge.workspace.google.com/admin/compliance/choose-a-geographic-location-for-your-data (redirected from https://support.google.com/a/answer/7630496) — vendor doc
20. Microsoft Learn — What is group-based licensing in Microsoft Entra ID — https://learn.microsoft.com/en-us/entra/fundamentals/concept-group-based-licensing — vendor doc
21. Brevo Developers — API rate limits — https://developers.brevo.com/docs/api-limits — vendor doc
22. Brevo Developers — How to use webhooks — https://developers.brevo.com/docs/how-to-use-webhooks — vendor doc
23. Brevo Developers — Secure webhook calls — https://developers.brevo.com/docs/secured-webhooks — vendor doc
24. Brevo API reference — Create a webhook — https://developers.brevo.com/reference/create-webhook — vendor doc
25. Brevo — Pricing — https://www.brevo.com/pricing/ — company self-description
26. Brevo Help Center — Data storage location — https://help.brevo.com/hc/en-us/articles/360001005510-Data-storage-location — company self-description
27. Brevo API reference — Create a deal — https://developers.brevo.com/reference/create-a-deal — vendor doc
28. Brevo Developers — OAuth scopes — https://developers.brevo.com/docs/oauth-scopes — vendor doc
29. Adobe HelpX — Schedule and publish social posts (Adobe Express, India) — https://helpx.adobe.com/in/express/using/schedule-and-publish-social-posts.html — vendor doc
30. Adobe Developer — Adobe Express Embed SDK docs — https://developer.adobe.com/express/embed-sdk/docs/ — vendor doc
31. Meta for Developers — Instagram Platform: Content Publishing — https://developers.facebook.com/docs/instagram-platform/content-publishing/ — vendor doc
32. Microsoft Learn (LinkedIn) — Community Management API overview — https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview — vendor doc
33. Google for Developers — YouTube Data API: Videos: insert — https://developers.google.com/youtube/v3/docs/videos/insert — vendor doc
34. X Developer Platform — Pricing — https://docs.x.com/x-api/getting-started/pricing — vendor doc
35. IETF — RFC 8493, The BagIt File Packaging Format (V1.0) — https://www.rfc-editor.org/rfc/rfc8493.html — primary/official standard
36. PDF Association — ISO 19005 (PDF/A) resource page — https://pdfa.org/resource/iso-19005-pdfa — secondary (standards body liaison)
37. PKWARE — APPNOTE.TXT .ZIP File Format Specification v6.3.10 — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT — primary (format owner)
38. ISO — ISO/IEC 29500-1 Edition 5 (project page, French) — https://www.iso.org/fr/standard/85626.html — primary/official
39. IETF — RFC 4180, Common Format and MIME Type for CSV Files — https://www.rfc-editor.org/rfc/rfc4180 — primary (Informational RFC)
40. GitHub Docs — Deployments and environments — https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments — vendor doc
41. GitHub Docs — Available rules for rulesets — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets — vendor doc
42. GitHub Docs — Configuring OpenID Connect in Amazon Web Services — https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws — vendor doc
43. GitHub Docs — About GitHub Advanced Security — https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security — vendor doc
44. Semantic Versioning 2.0.0 — https://semver.org/ — primary (specification)
45. Atlassian — Types of changes in change management (ITIL) — https://www.atlassian.com/itsm/change-management/types — secondary
46. FIRST — CVSS v4.0 Specification Document — https://www.first.org/cvss/v4-0/specification-document — primary (specification owner)
47. AWS Docs — AWS Backup restore testing — https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing.html — vendor doc
48. AWS Docs — AWS Backup Vault Lock — https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html — vendor doc
49. AWS Docs — Aurora Global Database disaster recovery (switchover/failover) — https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html — vendor doc
50. AWS Docs — Locking objects with Object Lock — https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html — vendor doc
51. AWS Docs — AWS Backup feature availability by resource and Region — https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html — vendor doc
52. ICAI Navi Mumbai Branch — Rule 3, Manner of books of account to be kept in electronic mode (reproduction of Companies (Accounts) Rules 2014 r.3 with amendment history) — https://navimumbai.icai.org/detail/18052.aspx — secondary (professional body branch)
53. ca2013.com — Rule 13, Companies (Accounts) Rules 2014 (internal auditor) — https://ca2013.com/rule-13-companies-accounts-rules2014/ — secondary
54. TaxGuru — Applicability of CARO 2020 — https://taxguru.in/company-law/applicability-caro-2020-financial-year-2021-22.html — secondary
55. TaxGuru — FAQs on audit trail reporting under Rule 11(g) — https://taxguru.in/company-law/reporting-paragraphs-audit-report-faqs-audit-trail-rule-11g.html — secondary
56. AZB & Partners — CERT-In's new cyber security audit guidelines decoded (1 Aug 2025) — https://www.azbpartners.com/bank/strengthening-indias-cyber-defence-cert-ins-new-cyber-security-audit-guidelines-decoded/ — secondary (law firm)
57. CERT-In — Directions under s.70B(6) of the IT Act, 28 April 2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf — primary/official
58. ISO — ISO/IEC 27001:2022 — https://www.iso.org/standard/27001 — primary/official (catalogue page)
59. TaxGuru — Internal audit applicability under Companies Act 2013 and CARO reporting — https://taxguru.in/company-law/internal-audit-applicability-companies-act-2013-caro-reporting.html — secondary

## Findings

### F1. Microsoft 365 — the plan Equator actually has, and what Microsoft Graph can automate

#### F1.1 "Business Starter" is not a Microsoft plan name
- **[V]** Microsoft's India comparison page (23 Oct 2026) lists only: Business Basic (₹170/user/month annual, GST extra), Business Basic (no Teams) (₹130), Business Standard with Copilot (₹1,955), Business Premium with Copilot (₹2,660), the no-Teams variants of those, and Apps for business (₹830). No plan is called "Business Starter" [1]. A search for the exact name found only reseller pages, no Microsoft page [search log].
- **"Business Starter" is a Google Workspace edition name** (F2). Management's "Microsoft 365 Business Starter" is therefore most likely **Microsoft 365 Business Basic**, the entry plan with Exchange, Teams, OneDrive/SharePoint and web-only Office apps. **[R]** The CS should confirm the SKU from Microsoft 365 admin centre → Billing → Your products, or from `GET /subscribedSkus` (the SKU part number for Basic is commonly `O365_BUSINESS_ESSENTIALS`; **[NC]** confirm against the tenant). This research assumes **Business Basic**.

#### F1.2 Business Basic — contents and limits (verified)
| Item | Business Basic | Business Standard | Business Premium | Source |
|---|---|---|---|---|
| Seat cap (all "for business" plans) | 300 users | 300 | 300 | [3] |
| Primary mailbox | **100 GB** | 100 GB | 100 GB | [2] [1] |
| Archive mailbox | 50 GB | 50 GB | 100 GB, auto-expanding to 1.5 TB | [2] |
| Recipient rate limit | 10,000 recipients/24 h per mailbox | same | same | [2] |
| Recipients per message | admin-configurable, 1–1,000 | same | same | [2] |
| Max message size | 150 MB internal; 112 MB once routed outside Microsoft (encoding); OWA 112 MB; default 35 MB send / 36 MB receive | same | same | [2] |
| OneDrive | 1 TB per user | 1 TB | 1 TB | [1] [4] |
| Teams meetings | online meetings for up to 300 attendees | — | — | [4] |
| Webinars | not listed for Basic; "included with Teams" for Standard/Premium | ✓ | ✓ | [1] |
| Office apps | web and mobile only | desktop | desktop | [4] |
| Identity | **Entra ID Free with security defaults** (MFA on by default) | Entra ID Free | **Entra ID P1 (Conditional Access)** | [3] |
| Device management | "Basic Mobility and Security" (a limited subset of Intune) | same | **Intune Plan 1** | [3] |
| Endpoint security | — | — | **Defender for Business** (≈ MDE P1 + some P2 features) | [3] |
| Email security | built-in anti-malware, anti-spam, anti-phishing (EOP) | same | **Defender for Office 365 Plan 1** (Safe Links, Safe Attachments) | [3] |
| Retention policies (Purview DLM) | **Teams chats/channels only**; org-wide/location-wide retention policies for Exchange/SharePoint/OneDrive are **not** licensed | Teams only | ✓ (Business Premium listed) | [15] |
| Audit (Standard) | ✓ | ✓ | ✓ | [15] |

**Inconsistency noted:** Microsoft's admin overview article still says Basic hosts "a 50-GB mailbox" [4], while the Exchange Online limits service description and the India price page say 100 GB [2][1]. The service description is the contractual reference; treat 100 GB as current and check the tenant's actual `ProhibitSendReceiveQuota`.

**Answers to the brief's direct questions:**
- **Conditional Access / Entra ID P1 included? No**; only Business Premium includes P1 [3]. Basic has security defaults (all-or-nothing MFA, no per-app/device/location policies).
- **Intune? No**; only Basic Mobility and Security [3].
- **Defender? No** Defender for Business or Defender for Office 365 P1; only built-in EOP [3].
- **Consequence for Appendix Q:** SC-01 (workforce IdP), SC-03 (FIDO2 MFA everywhere), SC-14 (workforce email DLP for Aadhaar/PAN) and SC-15 (MDM + EDR on all company devices) **cannot be met on Business Basic alone**. Either (a) upgrade staff with privileged or Tier-High access to Business Premium, or add **Entra ID P1 + Intune P1 + Defender for Business** add-ons to the Basic seats (add-on availability and India price **[NC]**), or (b) use Keycloak/AWS IAM Identity Center as the control point for the Equator consoles and treat M365 as mail-only. **[R]** Option (a) for the ≤ 30 staff with console access (Business Premium); Basic for the rest.

#### F1.3 Microsoft Graph — operations Equator needs
| Operation | Endpoint (v1.0) | Least-privileged **application** permission | Notes | Source |
|---|---|---|---|---|
| Create user | `POST /users` (`accountEnabled`, `displayName`, `mailNickname`, `userPrincipalName` on a verified domain, `passwordProfile`) | `User.Create` (higher: `User.ReadWrite.All`, `Directory.ReadWrite.All`) | 201 Created; the page says nothing about when the mailbox appears; mailbox creation follows licence assignment (poll `GET /users/{id}/mailboxSettings` until 200; delay **[NC]**) | [6] |
| Assign / remove licence | `POST /users/{id}/assignLicense` with `addLicenses[{skuId, disabledPlans}]`, `removeLicenses[]` | `LicenseAssignment.ReadWrite.All` | Delegated callers need License Administrator / User Administrator / Directory Writers. Group-based licensing is the alternative (`POST /groups/{id}/assignLicense`). Whether group-based licensing needs Entra ID P1 is **[NC]** (not stated on the Entra page [20]). **[R]** Use direct assignment on Basic. Set `usageLocation = "IN"` on the user before assignment (Microsoft requirement; not stated on the fetched page **[NC]**). | [5] [20] |
| Groups / distribution lists | `POST /groups` (M365 or security group), `POST /groups/{id}/members/$ref` | `Group.Create` / `GroupMember.ReadWrite.All` | Use for department DLs (`ops@`, `hr@`) driven by HRMS org units. | **[NC]** (not fetched; standard Graph) |
| Mail (send as system / user) | `POST /users/{id}/sendMail` | `Mail.Send` | **[R]** Scope down with an Exchange **application RBAC** / application access policy so the app can only send from named mailboxes. Never use M365 for case notices; case notices stay on `EMAIL_PORT` (SES) per Appendix D. | **[NC]** (scoping mechanism not fetched) |
| Calendar event with Teams link | `POST /users/{id}/events` with `isOnlineMeeting: true`, `onlineMeetingProvider: "teamsForBusiness"` | `Calendars.ReadWrite` | **Calendar-backed meetings are required for later transcript retrieval** [8] | [8] |
| Standalone Teams meeting | `POST /users/{userId}/onlineMeetings` → `joinWebUrl` | `OnlineMeetings.ReadWrite.All` **plus a tenant application access policy** (`New-CsApplicationAccessPolicy` / `Grant-CsApplicationAccessPolicy`, per user or `-Global`; up to 30 min to propagate) | "Isn't shown on the user's calendar"; custom meeting templates are a **Teams Premium** feature | [7] [8] |
| Recordings / transcripts | `GET /communications/onlineMeetings/{id}/transcripts` (`.vtt`), `/recordings` (`.mp4`); tenant-wide `getAllTranscripts` / `getAllRecordings` change notifications | `OnlineMeetingTranscript.Read.All`, `OnlineMeetingRecording.Read.All` (same access policy); meeting-scoped RSC alternative | **Not metered since 25 Aug 2025**. A tenant admin can disable Graph access to transcripts (403 `GraphAccessToTranscriptsDisabled`). The Graph page does not say whether recording itself is licensed on Basic **[NC]**. | [9] [7] |
| Files | `PUT /drives/{id}/items/{parent}:/{name}:/content` (≤ 250 MB); `POST …/createUploadSession` for larger files; `POST /drives/{id}/items/{id}/createLink` (sharing link); `POST …/children` (folder) | `Sites.Selected` (**[R]**, grant per site) rather than `Files.ReadWrite.All` | Max file 250 GB; ≤ 50,000 sub-items per shared folder; sync recommended ≤ 300,000 items | [10] (limits); endpoints **[NC]** (not fetched) |

**Application vs delegated.** Application permissions (client-credentials, no user) suit JML automation. They are tenant-wide unless narrowed: `Sites.Selected` for SharePoint, application access policies for Teams [7], and Exchange RBAC for mail **[NC]**. Delegated permissions suit "act as the signed-in staff member" features, such as adding a hearing to *my* calendar. **[R]** Two Entra app registrations: `eq-hrms-provisioner` (application; `User.Create`, `User.ReadWrite.All` for disable, `LicenseAssignment.ReadWrite.All`, `GroupMember.ReadWrite.All`; certificate credential, no secret) and `eq-ops-collab` (application; `Sites.Selected`, `Calendars.ReadWrite` scoped, `OnlineMeetings.ReadWrite.All` with a per-user access policy limited to an `eq-meeting-hosts` group). Both credentials live in AWS Secrets Manager (SC-08); both apps are reviewed in the quarterly access review (Q §7.3).

**Throttling (verified [13]).** Global: 130,000 requests per 10 s per app across all tenants. Identity and access: a token bucket in resource units. For a 50–500-user tenant ("M") that is 5,000 RU per 10 s per app+tenant, write quota 3,000 requests per 2 min 30 s, and tenant-wide 18,000 writes per 5 min. `GET users` costs 2 RU; Conditional Access APIs allow 1 request/s per tenant. Teams meeting information: 2,000 meetings per user per month. Responses: `429` with `x-ms-throttle-scope` / `x-ms-throttle-information`; honour `Retry-After` when present and otherwise use exponential backoff. Graph maps to `ProviderErrorKind = RATE_LIMITED` (Appendix D §D.0.2). Equator's JML volumes are far below these limits; bulk backfills should run at `x-ms-throttle-priority: low`.

**Data residency India (verified [14]).** India is a Microsoft 365 **Local Region Geography** (datacentres Chennai, Mumbai, Pune). The **Product Terms data-residency commitment** covers Exchange Online, SharePoint/OneDrive, Teams and Microsoft 365 Copilot data at rest for India-default tenants. **Advanced Data Residency** (add-on) and **Multi-Geo** are available for India. The tenant's Default Geography is fixed at creation and cannot be changed. **[R]** Record the tenant's data location (admin centre → Settings → Org profile → Data location) as evidence in `ops.transfer_register` (Q §2.6), and do not assume ADR is held.

#### F1.4 What Equator can automate on Business Basic, and what Basic cannot do
**Can automate (application permissions):**
1. **Joiner:** on HRMS `employee.activated` (offer accepted and background check passed, SC-21), create the user (`POST /users`, UPN `firstname.lastname@<domain>` per the naming rule; collision → append middle initial or number), set `usageLocation = IN`, assign the Basic SKU (or Premium for console staff), add to department and location groups (Delhi/Noida/Jaipur/remote), and create a temporary password sent to the personal email or mobile on file through `EMAIL_PORT`/`MESSAGING_PORT`, with `forceChangePasswordNextSignIn`.
2. **Mover:** group membership and licence changes on role change; manager attribute update.
3. **Leaver:** at the HRMS exit effective time: `PATCH /users/{id}` `accountEnabled=false`; `POST /users/{id}/revokeSignInSessions`; remove from groups; convert the mailbox to a **shared mailbox** for continuity. Conversion uses Exchange Online PowerShell, not Graph **[NC]**. A shared mailbox needs no licence up to a size limit **[NC]**. Then remove the licence. OneDrive access goes to the manager (retention window per tenant setting **[NC]**). All of this falls within the Q SC-01 leaver SLA (≤ 4 h).
4. Calendar-backed Teams meetings for internal operations (sales demos, onboarding calls) with `joinWebUrl` stored on the CRM activity.
5. Publishing exported packages into a SharePoint document library (F4) using `Sites.Selected`.

**Basic cannot (or should not) do:**
- Conditional Access, device-compliance gating, risk-based sign-in (needs Entra ID P1, Business Premium) [3].
- Intune device management or Defender for Business EDR (Business Premium) [3]; this blocks SC-15.
- Org-wide retention policies on Exchange/SharePoint/OneDrive (Business Premium or E3+) [15]. So **M365 must never be the system of record** for any record that Appendix Q §2.8 retains; it is a collaboration surface only.
- Teams Premium features such as custom meeting templates [8]. Webinars are not listed for Basic [1].
- **Hearings must not move to Teams.** Hearings stay on `VIDEO_PORT` (LiveKit India) because of the evidence, recording and residency controls in P04 and Appendix D §D.5.1. Teams is for Equator's internal and commercial meetings only.

### F2. Google Workspace — equivalents for a future switch
- **[V] Editions and limits** [16]: Business Starter USD 7/user/month (INR not shown on the page fetched), **30 GB pooled storage per user**, **Meet 100 participants, no Meet recording**, fundamental endpoint management, no Vault. Business Standard (USD 14): 2 TB pooled, 150 participants, recording. Business Plus (USD 22): 5 TB, 500 participants, Vault, advanced endpoint management. The 300-user cap applies to all three.
- **[V] Data regions** [19]: supported editions include Business Standard and Plus but **not Business Starter**, and the only selectable regions are **United States, European Union or "No preference". India is not offered.** Compare Microsoft's India commitment in F1.3. This is a material residency difference for a DPDP-sensitive institution. Workforce mail is not case data, but staff correspond about cases.
- **[V] Directory API** [18]: `POST https://admin.googleapis.com/admin/directory/v1/users` (password 8–100 ASCII characters, or a hash with `hashFunction`). A mailbox is assigned automatically when mail licences exist and "may take a few minutes". `DELETE …/users/{userKey}` fails for users under a Vault legal hold. `POST …/users/{id}/undelete` restores a user within 20 days (super-admin only). Suspension uses the `suspended` field on the user resource. Server-to-server calls use a service account with domain-wide delegation impersonating an admin (standard Google pattern; not on the fetched page **[NC]**).
- **[V] Meet REST API** [17]: create and configure meeting spaces (access type, moderation, auto-recording/transcription), manage members and co-hosts, end conferences, read conference records, participants and sessions, and fetch artifacts (recordings, transcripts, transcript entries, smart notes). **Artifacts are saved to the organiser's Drive.** Google states the API "isn't intended for performance tracking or user evaluation", which is relevant to HRMS: do not feed Meet attendance into appraisal scoring.
- Gmail API (send, labels), Calendar API (`events.insert` with `conferenceData.createRequest` for a Meet link) and Drive API (resumable upload, `permissions.create` for sharing, shared drives) are the counterparts of the Graph rows above (**[NC]** endpoint details not fetched this round; standard public APIs).
- **Licence assignment** in Google uses the Enterprise License Manager API **[NC]**.

### F3. Open CRM / marketing integrations — Brevo, Adobe Express, social platforms

#### F3.1 Brevo API (v3)
**Objects and endpoints (verified where cited):**
- **Contacts and attributes, lists, segments:** under `/v3/contacts/{…}` (rate class "contacts") [21]. Contact attributes are typed custom fields; lists hold static membership, segments are dynamic. Bulk `POST /v3/contacts/import` (CSV body or URL, or JSON) and asynchronous `POST /v3/contacts/export` exist in Brevo's reference (**[NC]**: endpoint pages not fetched this round; confirm field limits at the adapter spike).
- **Campaigns:** email, SMS and WhatsApp campaigns. OAuth scopes are `campaigns.email`, `campaigns.sms`, `campaigns.whatsapp` [28].
- **Transactional:** `POST /v3/smtp/email` (email), `POST /v3/transactionalSMS/send` (SMS), and transactional WhatsApp (scope `transactional.whatsapp`) [21][28].
- **CRM:** companies, deals, tasks, notes, pipelines under one OAuth scope `crm` [28]. `POST /v3/crm/deals` takes `name`, `attributes` (`deal_owner`, `pipeline`, `deal_stage`; stage IDs come from `/crm/pipeline/details/{id}`), `linkedContactsIds[]` and `linkedCompaniesIds[]`, and returns `201 {id}` [27]. Bulk deal import exists ("Import deals (creation and updation)") (search result; page not fetched).
- **Webhooks:** `POST /v3/webhooks` with `type ∈ {transactional, marketing, inbound}`, `channel ∈ {email, sms}`, `events[]`, `batched`, `auth`, `headers` [24].
  - Transactional events: `sent/request, delivered, hardBounce, softBounce, blocked, spam, invalid, deferred, click, opened, uniqueOpened, unsubscribed`.
  - Marketing events: `spam, opened, click, hardBounce, softBounce, unsubscribed, listAddition, delivered, contactUpdated, contactDeleted`.
  - Inbound event: `inboundEmailProcessed` [24].
  - Brevo's webhook overview also lists Sales CRM, Payment, Loyalty, Meeting/Phone and Push categories [22]. These are configured outside the `create-webhook` type enum (mechanism **[NC]**).
- **Webhook security (verified [23]):** IP allow-listing of Brevo ranges, Basic auth embedded in the URL, a **Bearer token** (`auth: {type: "bearer", token}`) or custom headers. **No HMAC payload signature is documented.** So the Appendix D `WebhookVerifier` for Brevo must check a per-subscription bearer token plus the source IP allow-list, and must **re-fetch state from the API before acting** on any event that changes consent (`unsubscribed`, `contactDeleted`). Retry behaviour is on a separate page not read **[NC]**.

**Rate limits (verified [21]; three tiers: General = all plans, Advanced = Professional/Enterprise, Extended = Enterprise):**
| Endpoint class | General | Advanced | Extended |
|---|---|---|---|
| `POST /v3/smtp/email` | 3.6 M/h, 1,000 rps | 7.2 M/h, 2,000 rps | 6,000 rps |
| `/v3/contacts/{…}` | 36,000/h, 10 rps | 72,000/h, 20 rps | 60 rps |
| `POST /v3/transactionalSMS/send` | 540,000/h, 150 rps | 720,000/h, 200 rps | 250 rps |
| `POST /v3/events` | 36,000/h, 10 rps | 72,000/h, 20 rps | 60 rps |
| **All other endpoints** | **100/h** | 200/h | 600/h |

Campaign and CRM endpoints are not listed separately, so on a non-Enterprise plan they appear to fall under the **100 requests/hour** catch-all **[V for the table; NC that CRM is in the catch-all]**. **Design consequence:** CRM sync to Brevo must be batched (bulk import endpoints), incremental, and queue-based. It must never be a synchronous call per UI action. This matches the Appendix D `CrmSyncWorkflow` 5-minute cadence, but the batch size must respect the hourly budget. A 429 maps to `RATE_LIMITED`; Brevo's limits page gives no Retry-After guidance [21].

**Plans and pricing:** the pricing page fetched on 23 Oct 2026 renders plan names without prices (dynamic pricing by contact and email volume) [25].
- **Free:** 300 emails/day after account approval.
- **Starter:** from 5,000 emails/month; no automation or A/B testing listed.
- **Standard:** unlimited automated workflows, A/B testing, send-time optimisation, web and event tracking.
- **Professional:** from 150,000 emails/month; WhatsApp, push, 10 seats, contact scoring.
- **Enterprise:** multi-account, dedicated IP, **SSO/SAML**, custom objects.
- **Sales plans:** "Sales Essentials" (with Starter/Standard) and "Sales Advanced" (per user, with Professional/Enterprise).

All plans include the transactional API and SMTP [25]. **Prices: not confirmed**; obtain an INR quote. **[M]** Feature descriptions are vendor statements.

**Data residency and DPA:** Brevo states that servers are "located within the European Union", with OVH (France, Germany) as primary host and Google Cloud in Belgium, at least two geographic locations, and encrypted backups [26]. **No India region is offered.** Brevo's DPA and sub-processor list were not read **[NC]**. Under DPDP s.16, cross-border transfer is permitted unless the destination is restricted by notification (Appendix Q §2.6 transfer register applies). Under GDPR, Brevo is an EU processor, so INT-matter EU contacts pose no transfer issue in that direction.

**India SMS and WhatsApp through Brevo:** TRAI DLT (principal-entity and template registration) and Meta WABA template approval apply regardless of vendor. Whether Brevo supports Indian DLT template IDs is **[NC]**. **[R]** Keep India SMS and WhatsApp on the Appendix D `MESSAGING_PORT` providers (MSG91, Gupshup) and use Brevo for **email marketing and CRM only** until DLT support is confirmed in writing.

#### F3.2 Adobe Express (Premium / Teams)
- **Content Scheduler** (in-product) schedules and publishes to **Facebook, Instagram (business accounts), LinkedIn, TikTok, Pinterest and X**. YouTube is not listed. The help page mentions **no API**, plan requirement or approval workflow [29].
- **Embed SDK** embeds the Adobe Express editor, quick actions (image and video edits) and modules (text-to-image, edit image) in a third-party web app. Projects can be saved back to the host app. Production use requires an Adobe Developer Console project and **Adobe review** before public release [30]. The SDK page mentions **no social scheduling or publishing** [30].
- **Conclusion:** there is **no public API to create, schedule or publish posts through Adobe Express Content Scheduler** (verified absent from the scheduler and Embed SDK docs; Adobe could still offer a private partner API **[NC]**). **Integration pattern [R]:**
  1. **Asset hand-off.** Equator's Social Calendar item holds the brief, copy, approvals and target channels. The designer creates the asset in Adobe Express, either via the Embed SDK inside the Ops Platform (asset returned to the DAM with its design link) or natively in Express (designer pastes the share link, and the exported file is uploaded to the DAM with SHA-256).
  2. **Publishing**, by one of two routes. (a) Manual publish in Adobe Content Scheduler, where the operator records the scheduled time and post URL back on the calendar item ("hand-off, manual confirmation"). (b) Equator publishes through its own `SOCIAL_PORT` adapters (F3.3), for channels where API access is approved.
  3. **Brand governance stays in Equator:** maker-checker approval of copy (legal claims, BCI advertising limits for neutrals and advocates, no case data per NN-16) before an asset is marked "ready to schedule".

#### F3.3 Social platform APIs — eligibility and constraints
| Platform | Publish capability | Access gate | Key limits | Source |
|---|---|---|---|---|
| **LinkedIn** (organisation page) | Community Management API: create and manage company posts, comments, reactions; page, follower, share and video analytics; member-profile posting | **Vetted product**: apply. Development tier first (500 requests/app, 100/member/day defaults), then Standard tier after a **screencast per use case**. Must be a new developer app with no other API product. `r_member_social` closed to new requests | Versioned Marketing APIs; old versions sunset (202406 sunset) | [32] |
| **Instagram** (professional account) | Content Publishing: images (JPEG only), videos, Reels, carousels (≤ 20), Stories | Advanced/Standard access; permissions `instagram_business_content_publish` (Instagram Login) or `instagram_content_publish` (Facebook Login). Media must be at a **public URL** at publish time. Page Publishing Authorization may be required | **100 API-published posts per 24 h** per account (the page also states 50 in the carousel section, an inconsistency to resolve at the spike); no shopping tags or filters | [31] |
| **Facebook Pages** | Page posts via Graph API | `pages_manage_posts` with Meta App Review and Business Verification (**[NC]**: not fetched this round) | — | — |
| **X** | `POST /2/tweets` | **Pay-per-use credits, no subscriptions**; Developer Console | Post create USD 0.015; with URL USD 0.200; post reads USD 0.005 per resource; 3 M post reads/month cap on pay-per-use | [34] |
| **YouTube** | `videos.insert` | OAuth scopes `youtube.upload` (or broader) | **1 unit from a separate "Video Uploads" bucket, 100 calls/day**; ≤ 256 GB; the page now states videos from unverified API projects are **not** restricted to private viewing | [33] |

**[R]** Build `SOCIAL_PORT` with adapters `linkedin_cm`, `meta_graph` (FB+IG), `x_v2`, `youtube_data`, plus `manual_handoff` as the default. Each adapter's flag stays OFF until its app review and access tier are granted. Analytics are pulled daily into the growth database only (NN-16).

### F4. Portable exports — formats, packaging, naming, size and migration

#### F4.1 Formats
| Need | Format and standard | Verified facts | Equator use |
|---|---|---|---|
| Editable documents, sheets, decks | **Office Open XML**: DOCX/XLSX/PPTX, **ISO/IEC 29500** | ISO/IEC 29500-1:2016 is in force. **Edition 5 of 29500-1 is at stage 60.00 "being published" (13 Oct 2026) and will replace the 2016 edition** [38] | Working copies (drafts, registers, MIS). **[R]** Write *Transitional* conformance (what Word and Excel open by default); strict-only output risks compatibility (**[NC]** that current Office defaults are unchanged) |
| Archival, non-editable | **PDF/A, ISO 19005**: A-1 (PDF 1.4; levels a/b); A-2 (PDF 1.7, ISO 32000-1); A-3 (as A-2 but **arbitrary attachments permitted**); A-4 (2020, PDF 2.0 / ISO 32000-2) [36]. PDF/A-2 attachments must themselves be PDF/A or plain text [36] | Record copies of awards, orders, settlements, minutes, invoices, payslips. **[R]** Default **PDF/A-2b** for generated record copies and **PDF/A-3b** only where a machine-readable source must be embedded (e.g. an XLSX ledger extract inside a PDF statement) |
| Tabular data | **CSV** per RFC 4180 (Informational): CRLF records, optional header, quote fields with comma/quote/line break, escape `"` as `""`; MIME `text/csv; charset; header=present` [39] | Every register in the export also as CSV (UTF-8 **with BOM** for Excel compatibility in Indian-language text **[R]**; the BOM is not RFC-mandated) alongside XLSX |
| Structured, lossless | **JSON** (RFC 8259 **[NC]**, not fetched) with JSON Schema per entity | Machine portability (DPDP and GDPR Art. 20 portability, Appendix Q PC-39) |
| Packaging and fixity | **BagIt 1.0, RFC 8493**: `bagit.txt` (two lines, UTF-8, no BOM); payload under `data/`; ≥ 1 `manifest-<alg>.txt` listing **every** payload file exactly once; optional `tagmanifest-<alg>.txt` and `bag-info.txt` (reserved labels `Source-Organization`, `Contact-Email`, `External-Identifier`, `Bagging-Date`, `Bag-Size`, `Payload-Oxum`, `Bag-Group-Identifier`, `Bag-Count`); tools MUST support SHA-256 and SHA-512, SHA-512 by default; only CR, LF and `%` are percent-encoded in manifest paths; "complete" vs "valid" definitions; reject `/` and `..` paths [35] | Export container: a BagIt bag zipped for transfer |
| Large archives | **ZIP64** (PKWARE APPNOTE 6.3.10, 1 Nov 2022): needed when any size or offset exceeds 0xFFFFFFFF (4 GiB) or entry count exceeds 0xFFFF (65,535); ZIP64 EOCD record and locator; **general-purpose bit 11** = UTF-8 names [37] | Always write ZIP64-capable archives and set bit 11. Split by `Bag-Group-Identifier` / `Bag-Count` when > 20 GB **[R]** |

#### F4.2 Naming and path limits (cross-platform)
- **Windows** [12]: no `< > : " / \ | ? *`, no control characters 0–31, no reserved device names `CON, PRN, AUX, NUL, COM1–9, LPT1–9` (even with an extension, e.g. `NUL.txt`), no trailing space or period, names case-insensitive. `MAX_PATH` = 260 characters unless long paths are enabled (Windows 10 1607+) [12][11]. File Explorer 260; component ≤ 255; **Windows Office desktop apps 256 characters** [11].
- **SharePoint / OneDrive** [10][11]: the decoded path including the file name ≤ **400 characters**; same invalid characters `" * : < > ? / \ |`; reserved names such as `.lock`, `CON`, `PRN`, `desktop.ini`; `_vti_` anywhere; names starting `~$`; no leading or trailing spaces; file ≤ 250 GB; sync error beyond 520 characters (local path plus root); share ≤ 50,000 sub-items; sync ≤ 300,000 items recommended.
- **macOS** [11]: Office 1,024 UTF-8 bytes; Finder 1,024 characters, names ≤ 255.
- **Binding constraint:** a recipient who unzips to `C:\Users\<name>\Downloads\<zip-name>\` and opens in Word is limited to about 256 characters. **[R]** Equator's export path budget is **≤ 180 characters relative to the bag root**, which leaves ≥ 70 characters for the user's local prefix. File names ≤ 80 characters; folder depth ≤ 6.
- Devanagari and other Indic names: UTF-8 bytes ≠ characters; macOS counts bytes [11]. **[R]** Keep folder and file names in **ASCII English** (transliterated slugs). Put the native-language title in the manifest and the README instead.

#### F4.3 Preserving e-signatures and audit trails
- **[R]** Never re-render, flatten, OCR or convert a signed PDF after signing; any byte change invalidates the signature. Export the **original signed bytes** (`…_signed.pdf`) exactly as stored in the evidence bucket. Their SHA-256 must equal the `core.evidence_ledger` hash. Add a separate **human-readable PDF/A rendition** (`…_rendition.pdf`) labelled "rendition — not the signed original".
- Include the ESP signing evidence: signer certificate chain, ESP transaction ID, timestamps, and the eSign audit-trail PDF from Leegality, Setu or Digio. Include the eStamp certificate. Include the BSA 2023 s.63(4) certificate already required by NN-10 (Appendix F `BUNDLE_CERTIFICATE_MISSING`).
- **Audit trail export:** an extract of the NN-22 hash-chain rows for the exported scope (`audit_trail.csv` plus `audit_trail.json`, with `seq`, `row_hash`, `prev_hash`) and the daily signed anchor JSONs covering those rows. With these, a recipient can verify continuity offline using the published verification script (`verify_audit.py`, included in `/_tools/`).
- Long-term signature validation (PAdES-LTV / ETSI EN 319 142) should be confirmed with each ESP **[NC]**: whether its output embeds OCSP/CRL data for India CCA certificates.

#### F4.4 Migration into SharePoint / Google Drive
- **SharePoint:** use `createUploadSession` for files > 250 MB. Preserve folder structure from the bag. Map manifest metadata to library columns (`EQ_Record_Class`, `EQ_Case_No`, `EQ_SHA256`, `EQ_Retention_Class`). On Basic, set retention as a **library label only if licensed** (F1.2: Basic has no org-wide retention). Otherwise retention is enforced by Equator, not SharePoint.
- **Google Drive:** resumable upload, shared drive per export, and file `properties` / `appProperties` for metadata (**[NC]**, not fetched).
- **Post-migration verification:** re-download a sample (≥ 2 % or ≥ 50 files) and compare SHA-256 with the BagIt manifest. Record the result in `ops.export_runs`.

### F5. GitHub-based change and patch management

#### F5.1 Plan gating — a correction to P00
- **[V] Environments** [40]: on GitHub Free, Pro or Team, **required reviewers, wait timers, admin-bypass control and custom deployment protection rules are available only for public repositories**. Deployment branch/tag restrictions and environment variables on private repositories need Pro or Team. Environment secrets on private repositories need Pro, Team or Enterprise.
- **Implication:** P00 FR-P00-08 ("Prod requires GitHub Environment approval by 2 reviewers") and Q SC-12 assume environment required reviewers on a **private** repository. That requires **GitHub Enterprise Cloud** (the page names only the Free/Pro/Team restriction; read with the plans page, Enterprise is the tier that lifts it; **[NC]** exact wording for Enterprise). **[R]** Licence GitHub Enterprise Cloud for the Equator organisation. Without it, implement the production approval gate outside GitHub: a Temporal `ReleaseApprovalWorkflow` plus an AWS IAM condition. That is weaker and harder to audit.
- **[V] Rulesets** [41] are available on private repositories for Pro, Team and Enterprise Cloud. Push rulesets (restrict file paths and extensions, across forks) are available on Team for private and internal repositories. Available rules:
  - restrict creations, updates and deletions;
  - require linear history;
  - **require deployments to succeed** before merge;
  - **require signed commits**;
  - require pull request, with required approvals, dismiss stale approvals, **require code-owner review**, and **require approval of the most recent push** (approver ≠ last pusher);
  - require conversation resolution;
  - required status checks (strict or loose);
  - block force pushes;
  - **require code scanning results** at a severity threshold;
  - require code-quality results;
  - tag rulesets;
  - bypass lists by role, team or GitHub App.
- **[V] Security features** [43]:
  - **Secret Protection**: secret scanning, **push protection**, custom patterns, delegated bypass.
  - **Code Security**: CodeQL code scanning, Copilot Autofix, dependency review, security campaigns.
  - Both are available for private repositories on **Team and Enterprise Cloud** as paid products (price **[NC]**). Code and secret scanning are enabled by default on public repositories. **Dependabot alerts are included in all plans**; premium Dependabot auto-triage rules need Code Security.
  - P00 FR-P00-07 already runs CodeQL in CI. For a private repository that requires the **Code Security** licence, or Semgrep alone if it is not bought.

#### F5.2 OIDC to AWS (verified [42])
The provider is `https://token.actions.githubusercontent.com` with audience `sts.amazonaws.com`. The role trust policy uses `StringEquals` on `token.actions.githubusercontent.com:aud` and `…:sub`. Example `sub` values are `repo:ORG/REPO:environment:ENV` and `repo:ORG/REPO:ref:refs/heads/BRANCH`. The workflow needs `permissions: id-token: write` and uses `aws-actions/configure-aws-credentials`.
**[R]** The prod deploy role must trust **only** `repo:equator-org/equator:environment:prod`. Branch-based subjects are never trusted for prod, so the environment gate (F5.1) becomes the cryptographic precondition for prod credentials. The dev role trusts `…:ref:refs/heads/main`.

#### F5.3 Versioning, branching and release
- **SemVer 2.0.0** [44]: MAJOR = incompatible API change, MINOR = backward-compatible feature, PATCH = backward-compatible fix; pre-release `-rc.1` has lower precedence; build metadata `+sha` is ignored for precedence; 0.y.z is unstable; a public API must be declared. **[R]** Equator's public API is the OpenAPI document plus webhook event schemas (P00 FR-P00-07 already runs `oasdiff breaking`). Version tags: `api-vX.Y.Z`, `web-vX.Y.Z`, `mobile-vX.Y.Z` (existing), and an umbrella platform release `rel-YYYY.MM.DD-N` that maps to the image digests deployed.
- **Trunk-based vs GitFlow:** P00 FR-P00-09 already chooses trunk-based development with squash merges and Changesets. **[R]** Keep it, with short-lived branches (≤ 2 days). Use *release branches only for hotfixing a deployed release* (`release/rel-…`, cherry-pick from `main`, never the reverse). Unfinished work ships dark behind Unleash release flags (P00 FR-P00-26); legal flags stay DB-authoritative. GitFlow's long-lived `develop` branch adds merge debt with no audit benefit.
- **Database migrations:** forward-only with expand/contract (P00 ADR-0002) and a one-off ECS migration task. Add four rules [R]:
  1. Each migration PR carries a `migration-risk` label (`additive`, `backfill`, `contract`).
  2. A `contract` migration (drop or rename) may deploy only after the release that stopped reading the old column has been in prod for ≥ 7 days.
  3. Backfills run as Temporal batch jobs, not inside the migration.
  4. Every migration has a tested **roll-forward fix** script in place of a rollback.

#### F5.4 Change classes and patch SLAs
- **ITIL change types** ([45], secondary):
  - **Standard**: pre-approved, low-risk, documented, often automatable.
  - **Normal**: assessed; high-risk changes go to a CAB, lower-risk ones to a designated change authority or automated checks and peer review.
  - **Emergency**: an immediate fix to restore service or close a threat, on a compressed timeline.
- Appendix Q §7.3 already defines `standard`, `normal`, `high` and `emergency`, with emergency retro-review ≤ 2 working days. Below, F5 adds the mapping to GitHub mechanics and patch SLAs.
- **CVSS v4.0** [46] qualitative scale: None 0.0; Low 0.1–3.9; Medium 4.0–6.9; High 7.0–8.9; Critical 9.0–10.0. CVSS measures *severity relative to other vulnerabilities*; regulatory and monetary factors are outside its scope [46]. So Equator's SLA uses **CVSS-BTE** (base + threat + environmental) plus overrides for a known-exploited vulnerability (KEV) or internet exposure. Appendix Q SC-11 SLAs remain authoritative: Critical ≤ 7 days (≤ 72 h if KEV or internet-exposed), High ≤ 30, Medium ≤ 45, Low ≤ 90. The P14 VAPT SLAs (Critical blocks go-live; High ≤ 15 days post-launch) apply to VAPT findings.

### F6. Backups and disaster recovery on AWS (ap-south-1 → ap-south-2)
The pack already fixes: Aurora PITR 35 days, an Aurora Global Database secondary in ap-south-2, AWS Backup daily/35-day and monthly/13-month plans with vault lock and cross-region copy, S3 CRR with Object Lock, RPO ≤ 15 min, RTO ≤ 2 h, monthly restore and quarterly DR drills (P00 FR-P00-06/20, ADR-0025, Q SC-17, P14 FR-P14-11). Verified facts that refine it:
- **Regions** [51]: AWS Backup cross-Region copy, **logically air-gapped vaults** and **restore testing** are all available in Mumbai and Hyderabad. **Hyderabad (ap-south-2) is an opt-in Region**, so it must be enabled in every account before Terraform applies (add this to the P00 `org_scp` module checklist).
- **Aurora cross-Region copies are snapshots, not PITR** [51]: "When a cross-Region … copy of a continuous backup is made, the copied recovery point becomes a snapshot (periodic) backup. PITR is not available for these copies." **Consequence:** in ap-south-2, point-in-time recovery to the minute exists only through the **Global Database secondary**, which replicates corruption too. Backup copies give only snapshot granularity. **[R]** Add an **hourly Aurora snapshot copy** for the `core` and `sealed` clusters during business hours (or rely on the Global DB for continuity and on snapshots for corruption recovery). State this two-mechanism model explicitly in ADR-0025.
- **Global Database** [49]:
  - **Switchover** (planned): RPO 0; read/write recovery typically < 30 s on qualifying versions.
  - **Failover** (unplanned): RPO "typically … measured in seconds"; RTO "in the order of minutes".
  - Aurora PostgreSQL's **`rds.global_db_rpo`** (20 s minimum) **blocks commits** when every secondary lags beyond the bound.
  - The promoted cluster does **not** inherit parameter groups, alarms or integrations.
  - **[R]** Set `rds.global_db_rpo = 600` s (comfortably inside the 15-min RPO), alarm at 60 s lag, and keep the ap-south-2 parameter groups, alarms and secrets **pre-created by Terraform**. Use the global writer endpoint so applications do not change endpoints.
- **Vault Lock** [48]: governance mode is removable by privileged IAM users. **Compliance mode becomes immutable after a grace time of ≥ 72 h** ("cannot be changed or deleted by any user or by AWS"). `MinRetentionDays` (≥ 1) and `MaxRetentionDays` (≤ 36,500) make non-conforming backup and copy jobs fail. Vault Lock was assessed by Cohasset for SEC 17a-4/CFTC/FINRA. **[R]** Prod and DR vaults use compliance mode with `MinRetentionDays = 35` and `MaxRetentionDays = 400`, and a separate **logically air-gapped vault** for monthly copies (13 months), owned by the `eq-security` account.
- **S3 Object Lock** [50]: requires versioning. In compliance mode a version "can't be overwritten or deleted by any user, including the root user"; "the only way to delete an object under the compliance mode before its retention date expires is to delete the associated AWS account". Legal holds have no expiry. **[R]** SCP: deny `account:CloseAccount` and `organizations:LeaveOrganization` / `RemoveAccountFromOrganization` for `eq-prod`, `eq-log-archive` and the backup accounts.
- **Restore testing** [47]:
  - Scheduled plans (cron, timezone, 1–168 h start window) select a recovery point (latest or random within `SelectionWindowDays`).
  - Restored resources are retained 1–168 h for validation and then deleted automatically. Validation is programmatic only.
  - Supported resources: Aurora, RDS, S3, EBS, EC2, EFS, FSx, DynamoDB, DocumentDB, Neptune.
  - Results: jobs listed as restore type "Test"; AWS Backup Audit Manager control "Restore time for resources meet target".
  - **[R]** This closes the "monthly restore test" in P14 FR-P14-11 automatically: weekly random-point restore of `core` with a validation Lambda that runs `audit.verify_chain()` on the restored copy and compares row counts and checksums. Evidence goes to `ops.restore_tests`.

**RPO/RTO tiers [R]** (refines ADR-0025 without loosening it):
| Tier | Systems | RPO | RTO | Mechanism |
|---|---|---|---|---|
| T0 | core Aurora, sealed Aurora, evidence S3, audit anchors, Temporal DB | ≤ 15 min (target ≤ 1 min) | ≤ 2 h | Global DB + CRR; snapshot copies for corruption |
| T1 | Ops Platform (CRM, tickets), HRMS, payroll ledger | ≤ 1 h | ≤ 8 h | Same Aurora pattern (separate cluster or schema); hourly snapshot copy |
| T2 | OpenSearch, Redis, analytics, growth DB | ≤ 24 h | ≤ 24 h (rebuild) | Rebuild from source or snapshots |
| T3 | Workforce SaaS (M365/Google mail and files) | Vendor-defined | Vendor-defined | **No native backup on Basic** (F1.2: no retention policies). **[R]** Third-party M365 backup, or accept vendor recycle-bin windows only; decision **OFF pending CS** |

### F7. Assurance — VAPT, CERT-In, ISO 27001, IS audit, internal/statutory audit, accounting audit trail

#### F7.1 CERT-In
- **Directions of 28 Apr 2022 under IT Act s.70B(6)** (primary [57]):
  - (i) synchronise ICT clocks to **NIC or NPL NTP** (or a source traceable to them);
  - (ii) report Annexure I incidents (including unauthorised access, data breach and data leak) **within 6 hours** of noticing;
  - (iii) designate a **Point of Contact** (Annexure II);
  - (iv) enable logs of all ICT systems and keep them **for a rolling 180 days within Indian jurisdiction**, produced on request.
  - Effective 60 days after issue (27 Jun 2022).
  - Already implemented in P14 FR-P14-05 and Q SC-09, with 400-day log retention.
  - **New for v3:** the **Equator Operations Platform, HRMS and the M365 tenant are ICT systems too**. Their logs (Entra sign-in and audit logs, Exchange audit, SharePoint audit, Brevo account activity) fall within scope. On Business Basic, Audit (Standard) is available [15], but its retention period was not confirmed this round **[NC]**. **[R]** Export Entra and M365 audit logs daily via Graph and the Office 365 Management Activity API to `eq-log-archive` (Object Lock, India), so the 180-day obligation never depends on the M365 plan.
- **Comprehensive Cyber Security Audit Policy Guidelines, 25 Jul 2025** ([56], secondary summary; the CERT-In original was not opened this round):
  - **Applicability:** empanelled auditors and auditees.
  - **Frequency:** audits **at least annually** and after major change.
  - **Audit types:** compliance audit, VA, penetration testing, configuration and network audit, source-code review, application security, cloud, IoT, **AI system and AI-BOM audits**, red team.
  - **Auditor independence:** fees must not depend on outcomes; written consent before high-risk tests; critical findings reported immediately to the auditee **and CERT-In**.
  - **Auditee data:** to be **stored only on systems in India**; no sharing with foreign entities without written authorisation; audit metadata to CERT-In **within 5 days** of completion.
  - **Report contents:** CVSS severity **supplemented by EPSS**, CWE/CVE mapping, three-level signatures; the final report only after closure and follow-up. A **staging-only test must say production was not tested**.
  - This last point conflicts with P14 FR-P14-04 ("staging environment identical to production; no production sealed data"). **[R]** Add a limited, consented production test window (non-destructive, test tenants only) so the report covers production, or accept the "production not tested" caveat with Board-noted risk acceptance.
- **Empanelled auditor list:** P14 already requires checking CERT-In's current list on the engagement date. **[R]** Store the list snapshot (PDF and SHA-256) with the engagement record.

#### F7.2 ISO/IEC 27001:2022 controls in scope of this stream
ISO/IEC 27001:2022 (Ed. 3, published 25 Oct 2022) is current, with **Amd 1:2024 "Climate action changes"**; the 2013 edition is withdrawn [58]. Appendix Q §6.2 already assigns owners for A.5.30, A.8.8, A.8.9, A.8.13, A.8.14, A.8.15, A.8.25, A.8.28, A.8.29 and A.8.32. Evidence this stream adds:
| Control | Evidence added by v3 (Ops Platform, HRMS, workspace) |
|---|---|
| **A.8.32 Change management** | GitHub ruleset export (JSON) per quarter; PR ↔ change record ↔ deployment linkage incl. Ops Platform and HRMS repos; emergency-change retro-reviews; **SaaS configuration changes** (M365 admin, Brevo account, Adobe Teams admin) recorded as `standard` change records |
| **A.8.13 Information backup** | AWS Backup job reports; Vault Lock configuration; restore-testing job results [47]; M365 backup decision record (T3) |
| **A.8.15 Logging** | Log-source coverage including Entra/M365/Brevo; 180-day CERT-In probe (Q §7.3 `log_retention_probe`) |
| A.5.15–5.18 / A.8.2 (access, identities, privileged access) | JML evidence from the HRMS → Graph connector: time from HR exit to `accountEnabled=false` (SLA ≤ 4 h) |
| A.8.31 Separation of dev/test/prod | GitHub environment and OIDC `sub` binding (F5.2); no prod credentials outside the `prod` environment |

#### F7.3 Companies Act audit duties that the platform must support
- **Accounting audit trail.** Companies (Accounts) Rules 2014 **r.3(1) proviso**: "for the financial year commencing on or after the 1st day of April, 2023, every company which uses accounting software for maintaining its books of account, shall use only such accounting software which has a feature of recording audit trail of each and every transaction, creating an edit log of each change made in books of account along with the date when such changes were made and ensuring that the audit trail cannot be disabled" ([52], ICAI branch reproduction of the rule text; secondary).
- **Books accessible in India.** **r.3(1)** requires electronic books to be "accessible in India, at all times". **r.3(5) proviso** requires backups, including of books kept outside India, "in servers physically located in India on a daily basis" [52].
- **Annual intimation to the Registrar.** **r.3(6)** requires, with the financial statements, the service provider's name, IP address, location, and the cloud address where books are kept on cloud [52].
- **Statutory auditor reporting.** Companies (Audit and Auditors) Rules **r.11(g)**: the auditor reports whether the audit trail feature operated throughout the year for all transactions, was not tampered with, and was preserved. Direct database-level changes affect the books, so the trail must exist at the database level as well. A log keeping only the latest change, or an editable error log, is inadequate ([55], secondary FAQ referring to the Implementation Guide).
- **Relevance to Equator.** If Equator's billing, invoicing, escrow-ledger or payroll modules are, or feed, the **books of account** of Equator Resolution Service Pvt Ltd (or of a Chambers tenant that keeps books on the platform), they are "accounting software" for this rule. Appendix F append-only ledgers (`deny_mutation`) plus the NN-22 hash chain satisfy "cannot be disabled" **only if** the following hold.
  1. Corrections are new reversing entries, never updates (already the pack rule, RB-08).
  2. **Master-data edits** on customers, vendors, GSTIN, rate cards, employee pay components and bank accounts are captured in an edit log with old and new values and timestamp.
  3. **DBA-level changes** are logged by `pgaudit` (or equivalent) on ledger schemas and shipped to the log archive, and no role, `eq_migrator` included, can disable triggers on ledger tables without a break-glass event.
  4. Logs are retained for the books' statutory retention: **8 years under s.128(5)** (**[NC]**: section text not re-read this round; the pack already uses an 8-year case-record default).
  5. Daily backup in India (r.3(5)) is met by ap-south-1/ap-south-2.
- **Internal audit (s.138).** Companies (Accounts) Rules **r.13** ([53], secondary reproduction). A **private company** must appoint an internal auditor if, in the preceding FY, it has **turnover ≥ ₹200 crore**, or **outstanding loans or borrowings from banks/PFIs > ₹100 crore at any point**. For unlisted public companies the thresholds are paid-up ≥ ₹50 crore, turnover ≥ ₹200 crore, borrowings > ₹100 crore, or deposits ≥ ₹25 crore. Listed companies must always appoint one. The Board or Audit Committee sets scope, periodicity and methodology (r.13(2)).
- **CARO 2020** (S.O. 849(E), 25 Feb 2020; [54], secondary) applies to every company except banking, insurance, s.8 companies, OPCs, **small companies**, and private companies that meet **all** of these tests:
  - not a holding or subsidiary of a public company;
  - paid-up capital plus reserves ≤ ₹1 crore at the balance-sheet date;
  - borrowings from banks/FIs ≤ ₹1 crore at any point in the year;
  - total revenue ≤ ₹10 crore.
- **CARO internal-audit reporting.** Where CARO applies, the statutory auditor reports whether an internal audit system commensurate with size exists and whether internal audit reports were considered ([59], secondary). The clause number was not confirmed on that page.
- **Configurable facts.** All these thresholds are **configurable facts** (`audit.applicability.*`) with source and effective date. The "small company" thresholds have been amended over time and were **not re-verified this round [NC]**.
- **IS audit evidence for regulated clients.** Lender tenants (RBI-regulated entities) will ask for the CERT-In audit report, SOC 2 or ISO certificate, BCP/DR test results and sub-processor lists under their outsourcing and IT-governance obligations. The Q §7.3 collectors already produce most of these. v3 adds an **"Assurance pack" export** (F4 format) per client request, with an NDA watermark.

## Design implications for Equator

### DI-A. Workspace connector port (suite-neutral)
1. **New port `WORKSPACE_PORT`** (add to the Appendix D §D.0.4 CHECK list and the master §4.4 port list via ADR). It is used only by the `hrms` and `ops` bounded contexts and never receives case data (NN-16 extended to workforce systems).
```ts
export interface WorkspacePort {
  capabilities(): WorkspaceCapabilities;                       // see matrix below; resolved per tenant + SKU
  createAccount(a: { employeeId: string; givenName: string; surname: string; upnLocalPart: string; domain: string;
                     skuCode: string; usageLocation: 'IN'; groups: string[]; tempSecretChannel: 'email'|'sms' }): Promise<{ externalId: string; upn: string }>;
  setLicences(externalId: string, add: string[], remove: string[]): Promise<void>;
  setGroups(externalId: string, add: string[], remove: string[]): Promise<void>;
  suspend(externalId: string, reason: 'exit'|'investigation'|'leave'): Promise<void>;   // disable + revoke sessions
  convertToShared?(externalId: string, delegateTo: string[]): Promise<void>;           // M365 only (PowerShell runner)
  transferFiles?(externalId: string, toExternalId: string): Promise<{ transferRef: string }>;
  deleteAccount(externalId: string): Promise<void>;           // only after retention/legal-hold check (DI-A6)
  createMeeting(m: { hostExternalId: string; subject: string; start: Date; end: Date; attendees: string[]; calendarBacked: true }): Promise<{ joinUrl: string; eventId: string }>;
  uploadFile(f: { siteOrDriveRef: string; path: string; sha256: string; stream: NodeJS.ReadableStream }): Promise<{ itemId: string; webUrl: string }>;
  createShareLink?(itemId: string, scope: 'organization'|'specific_people', expiresAt: Date): Promise<{ url: string }>;
  pullAuditLogs(since: Date): AsyncIterable<NormalisedEvent>;  // to eq-log-archive (CERT-In 180 d)
}
```
   Adapters: `m365_graph` (P1, default), `google_workspace` (stub, flag `ops.workspace.google.enabled` OFF), `manual_it_desk` (fallback: creates an IT ticket with a checklist). Failover is `none` (identity is stateful).
2. **Capability matrix.** Seed `core.integration_providers.capabilities` with this matrix. The UI hides any action whose capability is false.
| Capability | M365 Business Basic | M365 Business Premium | Google Business Starter | Google Business Standard/Plus |
|---|---|---|---|---|
| Create/disable user, groups, licences via API | ✓ [5][6] | ✓ | ✓ (Directory API) [18] | ✓ |
| Conditional Access / context-aware access | ✗ (security defaults only) [3] | ✓ Entra ID P1 [3] | ✗ [16] | ✗ (Enterprise) [16] |
| MDM / EDR | Basic Mobility only [3] | Intune P1 + Defender for Business [3] | Fundamental endpoint mgmt [16] | Fundamental / Advanced (Plus) [16] |
| Retention / legal hold on mail and files | Teams only [15] | ✓ [15] | ✗ (no Vault) [16] | Plus: Vault [16] |
| Meetings: max attendees | 300 [4] | 300 | 100 [16] | 150 / 500 [16] |
| Recording and transcript retrieval via API | Graph API ✓ (not metered) [9]; licence for recording on Basic **[NC]** | ✓ | ✗ recording [16] | ✓ (artifacts to organiser's Drive) [17] |
| Webinars | not listed [1] | ✓ [1] | — | — |
| Data at rest in India | ✓ Product Terms commitment [14] | ✓ | ✗ (US/EU/no-preference only; not on Starter) [19] | ✗ India region [19] |
| Mailbox / storage | 100 GB mail [2], 1 TB OneDrive [1] | 100 GB + archive to 1.5 TB [2] | 30 GB pooled [16] | 2 TB / 5 TB pooled [16] |
3. **Default licence policy [R]** (`hrms.workspace.sku_rules`, configurable, maker-checker): roles with staff-console, Tier-High, sealed or finance access get **Business Premium**. Everyone else gets **Business Basic**. Contractors get no mailbox (guest access only). A **locked rule** prevents assigning a privileged Equator console role to a user whose workspace SKU lacks Conditional Access plus MDM (`WORKSPACE_SKU_INSUFFICIENT_FOR_ROLE`), unless the security lead records an exception with an expiry of ≤ 90 days.
4. **JML workflow** (`WorkspaceJmlWorkflow`, Temporal; triggered by HRMS events):
   - **Joiner:** `employee.activated` requires background check passed plus NDA and AUP e-signed (Q SC-21). The UPN is generated by the configurable pattern `{first}.{last}` with a collision suffix; ASCII transliteration of Indic names follows a stored transliteration table. The temporary credential goes only to the personal channel on file.
   - **Mover:** `employee.role_changed` diffs groups and SKU.
   - **Leaver:** `employee.exit_effective` triggers disable, session revoke and group removal in ≤ **4 h** (`iam.leaver_revoke_hours`, Q SC-01; locked minimum, tenant may only tighten), then mailbox conversion, file transfer to manager, and licence removal at T+1 day.
   - **Gross-misconduct exit** (`exit_type = termination_for_cause`) runs immediately and requires HR plus a second approver (maker-checker).
   - Every step writes `audit.append_event` and an `ops.jml_events` row (`employee_id`, `step`, `requested_at`, `completed_at`, `provider_ref`, `sla_met`).
5. **Graph app registrations:** two apps (F1.3), certificate credentials in Secrets Manager, rotation ≤ 90 days. `Sites.Selected` only. Teams application access policy granted to the `eq-meeting-hosts` group, not `-Global`. Admin consent is recorded as a `normal` change.
6. **Deletion guard:** `deleteAccount` is blocked while any `legal_hold`, open grievance, POSH matter or disciplinary case references the employee (`WORKSPACE_DELETE_BLOCKED_HOLD`). Default delay after exit: 90 days (configurable 30–365).
7. **No case work in the workforce suite (locked):** hearings stay on `VIDEO_PORT`; case notices stay on `EMAIL_PORT`/SES; case documents never sync to SharePoint or Drive except through a governed export (DI-C) with a recorded purpose.

### DI-B. Marketing, CRM and social connectors
8. **`CRM_PORT` gains a `brevo` adapter** (sync-only; native CRM remains source of truth per D.9). Mapping:
   - `growth.leads` → Brevo contacts (attributes: persona, source, consent flags, language);
   - `growth.accounts` → companies;
   - `growth.opportunities` → deals (pipeline and stage IDs stored in the provider config);
   - tasks one-way, Equator → Brevo.
   Rate-limit budget: `brevo.crm.max_requests_per_hour` defaults to **80** (headroom under 100/h [21]). Bulk import is used for > 50 records. Contacts use the 10 rps class.
9. **New `MARKETING_PORT`** covering campaign create/schedule, list/segment sync and transactional *marketing-class* email. The adapter is `brevo`. **Locked:** never used for case notices or OTPs; never sent to respondents unless they gave separate marketing consent (P07 suppression check); India SMS and WhatsApp marketing stays on DLT-registered MSG91/Gupshup unless Brevo DLT support is confirmed (flag `growth.brevo.sms_whatsapp.enabled` OFF).
10. **Brevo webhook ingress:** a per-subscription bearer token (rotated ≤ 90 days), an IP allow-list from Brevo's published ranges, and an event re-fetch before applying `unsubscribed`/`contactDeleted`. Unsubscribe in Brevo creates a consent withdrawal in Equator within 15 min (D.9 rule), and vice versa.
11. **Residency record:** Brevo hosts in the EU [26]. Add a transfer-register row `BREVO_EU` (data class `personal`, growth data only) plus a residency ADR (D.0.4 resolver step 3). Obtain the DPA and sub-processor list before activation. Contracting is CS-owned.
12. **`SOCIAL_PORT`** adapters (all OFF until app review or access tier is granted): `linkedin_cm` (Standard tier), `meta_graph` (IG publish limit counter per account per 24 h, configurable default 50 to stay below both documented figures [31]), `x_v2` (credit budget per month, configurable), `youtube_data` (100 uploads per day ceiling [33]), plus the default `manual_handoff`.
13. **Adobe Express integration = asset hand-off** (no publish API [29][30]). The Social Calendar item stores `design_link`, exported asset (DAM, SHA-256), approval chain, `published_via ∈ {adobe_scheduler, equator_social_port, native_app}`, `post_url` and `published_at` (operator-confirmed for Adobe). The Embed SDK route is optional (`ops.adobe_embed.enabled` OFF; requires Adobe review [30]).
14. **Content governance (locked):** every outbound post passes maker-checker. Checks include: no case-identifying data; neutral/advocate promotion within Bar Council advertising limits (Appendix N/P rules; counsel sign-off); "paid preference" placements labelled as sponsored. Equator never auto-publishes AI-generated copy without human approval.

### DI-C. Portable export package specification (`EQ-EXPORT-1.0`)
15. **Container:** a BagIt 1.0 bag [35], zipped with ZIP64 and UTF-8 names (bit 11) [37]. File name `EQX_{scope}_{scopeRef}_{yyyymmdd}_{seq}.zip`, e.g. `EQX_CASE_EQR-FIN-2026-000123_20261023_01.zip`. Split above `export.max_part_gb` (default 20) using `Bag-Group-Identifier` / `Bag-Count`.
16. **Bag root (fixed):**
```
bagit.txt
bag-info.txt                 # Source-Organization: Equator Resolution Service Private Limited; Contact-Email; External-Identifier=<export_run_id>;
                             # Bagging-Date; Bag-Size; Payload-Oxum; Bag-Group-Identifier; Bag-Count; EQ-Export-Spec: EQ-EXPORT-1.0; EQ-Scope; EQ-Requested-By (role, not name, for DSR exports)
manifest-sha256.txt          # every payload file (SHA-256 = evidence-ledger hash for evidence)
manifest-sha512.txt          # BagIt default algorithm [35]
tagmanifest-sha256.txt
data/
  00_READ_ME_FIRST.pdf       # PDF/A-2b, English + Hindi (+ tenant language): what this is, folder guide, how to verify, legal notices
  00_READ_ME_FIRST.html
  01_Index.xlsx              # one row per file: path, title (native script allowed), record class, date, parties' roles (no PII for anonymised scopes), source system ID, SHA-256, signed? , retention class
  01_Index.csv               # RFC 4180, UTF-8 with BOM
  02_Records/                # DOCX/XLSX working copies + PDF/A record copies, by record class
  03_Signed_Originals/       # byte-exact signed PDFs + ESP audit trail + eStamp certificates (never re-rendered)
  04_Data/                   # JSON (+ JSON Schema in 04_Data/_schemas) and CSV per entity
  05_Audit_Trail/            # audit_trail.csv/json (seq,row_hash,prev_hash,...), anchors/*.json (KMS-signed), BSA s.63(4) certificate
  06_Certificates/           # export certificate (PDF/A) signed with Equator DSC: scope, counts, manifest SHA-256, generation time (IST)
  _tools/                    # verify_bag.py, verify_audit.py, public keys
```
17. **Folder taxonomy rules (locked spec, configurable labels):**
   - Max depth 6 under `data/`.
   - Folder names are `NN_Title_Case_English` (two-digit ordinal prefix for sort order). Record-class folders come from `core.record_classes` (e.g. `02_Records/03_Pleadings/`, `…/05_Orders_and_Awards/`, `…/07_Fees_and_Invoices/`).
   - For HRMS exports: `02_Records/01_Employment/`, `02_Payroll/{FY}/`, `03_Leave_Attendance/`, `04_Appraisals/`.
   - For Ops exports: `CRM/`, `Tickets/`, `Grievances/`.
18. **File naming rule (validator `EXPORT_NAME_INVALID`):** `{yyyy-mm-dd}_{docType}_{shortRef}_{v##}.{ext}`, ASCII `[A-Za-z0-9._-]` only, ≤ 80 characters. Reject Windows reserved names and characters, trailing dot or space, `~$` and `_vti_` prefixes, and `.lock`/`desktop.ini` [10][12]. **Full relative path ≤ 180 characters** (DI rationale F4.2). Native-script titles go in `01_Index` and the PDF metadata only.
19. **Manifest fields (`01_Index`, `04_Data/files.json`):** `path`, `sha256`, `bytes`, `media_type`, `record_class`, `title`, `title_native`, `language`, `document_date`, `created_at_ist`, `source_system`, `source_id`, `version`, `is_signed_original`, `signature_type ∈ {aadhaar_esign, dsc, none}`, `esp_txn_ref`, `evidence_ledger_seq`, `retention_class`, `legal_hold`, `confidentiality_tier`, `redaction_profile`, `rendition_of` (links a PDF/A rendition to its signed original).
20. **Format defaults per record class (configurable within the allowed set):**
   - Narrative records: DOCX plus PDF/A-2b.
   - Registers and ledgers: XLSX plus CSV plus JSON.
   - Signed instruments: original bytes plus PDF/A rendition.
   - Media: original (MP4/M4A) plus transcript (DOCX/VTT).
   - Embedding sources inside PDFs: PDF/A-3b only.
   - **Locked:** sealed-store data is never exported except via break-glass (Q SC-14). Tier-High exports carry a watermark (requester role and time) on PDF renditions, never on signed originals.
21. **Scopes:** `CASE`, `PARTY_DSR` (DPDP/GDPR portability, JSON first), `TENANT_EXIT` (90-day window per App. O), `CHAMBERS_PRACTICE`, `EMPLOYEE_FILE`, `PAYROLL_FY`, `OPS_CRM`, `ASSURANCE_PACK`, `STATUTORY_BOOKS` (F7.3 r.3(6)). Each scope has a permission (`*.export`), a step-up (aal2 ≤ 10 min, App. S), maker-checker for `TENANT_EXIT`/`PAYROLL_FY`/`STATUTORY_BOOKS`, and an `ops.export_runs` row (`run_id`, `scope`, `requested_by`, `approved_by`, `counts`, `manifest_sha256`, `bag_valid`, `delivered_to`, `expires_at`).
22. **Delivery:** the `exports` bucket (7-day lifecycle, P00 FR-P00-20), presigned links ≤ 5 min issued on demand, optional push to the tenant's SharePoint or Drive via `WORKSPACE_PORT.uploadFile`. After any push, sample re-hash (≥ 2 % or 50 files) and record `migration_verified`.
23. **Validation gate:** an export is `ready` only when the bag is **valid** (all checksums match [35]), every signed original's SHA-256 equals its evidence-ledger hash, the audit-trail extract verifies against its anchors, and the path and name validators pass. Otherwise it fails with `EXPORT_BAG_INVALID` / `EXPORT_SIGNATURE_HASH_MISMATCH`.

### DI-D. CI/CD and change-management workflow
24. **GitHub plan (governed decision, Board/CTO):** **GitHub Enterprise Cloud** is required for environment required reviewers and deployment protection on private repositories [40]. Buy **Secret Protection and Code Security** for private-repo CodeQL and push protection [43]. Until then, FR-P00-08's two-approver gate is implemented by `ReleaseApprovalWorkflow` and recorded as a Q §7.3 compensating control.
25. **Repositories:** `equator` (platform monorepo), `equator-ops` (Operations Platform + HRMS; may live in the monorepo as bounded contexts, decided by ADR), `equator-infra` (Terraform), `equator-mobile` (if split). Every repository gets the same org-level rulesets.
26. **Org rulesets (`main`, `release/*`)** [41]:
   - require PR with **≥ 1 approval** (≥ 2 where CODEOWNERS marks `rules`, `auth`, `payments`, `sealed`, `payroll`, `ledger`, `rls`, `infra/prod`);
   - dismiss stale approvals; **require code-owner review**; **require approval of most recent push**; require conversation resolution;
   - required status checks: the full FR-P00-07 suite plus `export-spec-tests` and `ledger-audit-trail-tests`;
   - **require code scanning results** (no High+); require signed commits; linear history; block force pushes; restrict deletions;
   - **require deployments to succeed** to `staging` before merge to `release/*`.
   - Bypass list is empty except a `break-glass` team with time-boxed membership (every use is an emergency change).
   - Tag ruleset: `rel-*`, `api-v*`, `mobile-v*` creation is restricted to the release-manager team.
   - Push ruleset: block `*.pem`, `*.p12`, `.env*`.
27. **CODEOWNERS additions:** `apps/api/src/modules/hrms/payroll/**` and `**/ledger/**` → finance-systems owner + security; `apps/api/src/integrations/adapters/m365_graph/**` → identity owner; `packages/export-spec/**` → records owner + DPO delegate.
28. **Environments:** `dev`, `staging`, `uat`, `prod`, `dr`. `prod` and `dr`: required reviewers = 2 from `release-managers` + `tech-leads`, **prevent self-review**, deployment branches restricted to `release/*` and tags `rel-*`, and a custom protection rule that calls Equator's change-record API (a deployment is approved only if `ops.change_records.status = approved` and the change window is open).
29. **OIDC:** AWS role trust `sub = repo:<org>/equator:environment:prod` only [42]. No static AWS keys anywhere (SCP plus IAM Access Analyzer finding is Critical).
30. **Change record (`ops.change_records`):** `id`, `class ∈ {standard, normal, high, emergency}` (Q §7.3), `title`, `services[]`, `risk_assessment`, `rollback_or_rollforward_plan`, `test_evidence_url`, `pr_urls[]`, `image_digests[]`, `migration_risk`, `window_start/end`, `requested_by`, `approved_by[]` (≥ 2 for high; never the requester), `cab_note` (high), `deployed_at`, `verified_at`, `retro_review_due` (emergency, +2 working days), `outcome ∈ {successful, failed, rolled_forward, backed_out}`.
   - **Standard changes** come from a pre-approved catalogue (`ops.standard_change_catalogue`): dependency patch with green CI, content and copy updates, SaaS user admin, certificate renewal. These auto-create the record.
   - **SaaS admin changes** (M365, Brevo, Adobe, GitHub org settings) are change records too. Graph and GitHub audit logs reconcile weekly against records (`UNRECORDED_SAAS_CHANGE` opens a ticket).
31. **Patch SLA engine** (`vuln.sla.*`, Q SC-11 values, locked floor): severity from CVSS-BTE [46] with overrides (KEV or internet-exposed → Critical ≤ 72 h). Dependabot and Renovate PRs for Critical/High are auto-labelled `emergency` or `normal` per SLA, and SLA breach pages security. An emergency change permits one approver plus post-deploy retro review; it never bypasses CI security gates (only the `break-glass` team can, and that is logged as Sev-2).
32. **Release versioning:** SemVer per deployable [44], umbrella `rel-YYYY.MM.DD-N` tag, release notes from Changesets. The `/admin/env` screen and `GET /v1/meta/version` expose the release tag, image digests and migration version. Every change record links to its tag.
33. **Migrations:** F5.3 migration rules are enforced by CI (`migration-risk` label required; `contract` migrations blocked unless the referenced release has been in prod ≥ 7 days, checked via deployment history).

### DI-E. Backup and restore policy (extends Q SC-17; values are defaults, floors locked)
| Asset | Backup | Retention (default; floor) | Copy | Restore test |
|---|---|---|---|---|
| Aurora `core`, `sealed`, `ops`, `hrms` | PITR (continuous) + daily snapshot + hourly snapshot copy (business hours) | PITR 35 d; daily 35 d; monthly 13 mo; **ledger/payroll yearly snapshot 8 y** (r.3(5), s.128(5) [NC]) | ap-south-2 (snapshots; PITR not copyable [51]) + air-gapped vault (monthly) | Weekly automated (AWS Backup restore testing [47]) with `verify_chain()`; quarterly full DR drill |
| S3 evidence, documents | Versioning + Object Lock (evidence compliance mode) + CRR | per record class (8 y evidence default) | ap-south-2 | Monthly sample restore and hash check |
| Log archive | Object Lock 400 d | 400 d; floor 180 d (CERT-In [57]) | ap-south-2 | Monthly oldest-object probe |
| Workforce SaaS (M365) | **Decision OFF pending CS:** third-party backup vs vendor recycle bins only | — | — | If adopted: quarterly mailbox and OneDrive item restore |
| Brevo / growth | Nightly API export of contacts and deal records to growth DB snapshot | 13 mo | — | Quarterly |
- Vault Lock **compliance mode** on prod/DR vaults after a 72 h grace [48]. `rds.global_db_rpo = 600` [49]. ap-south-2 opt-in enabled [51]. SCP denies account closure for prod, log and backup accounts [50].
- The **RPO/RTO tiers T0–T3** (F6) are stored in `ops.service_catalogue` and drive alerting and drill scope.

### DI-F. Accounting audit-trail controls (billing, escrow ledger, payroll)
34. **Locked:** ledger and master-data tables in `billing`, `payments`, `escrow`, `payroll` are append-only (corrections by reversal). Master-data tables keep a temporal history table (`*_history`: `old`, `new`, `changed_by`, `changed_at` IST, `reason`, `change_request_id`). `pgaudit` covers DDL/DML on these schemas. Any `ALTER TABLE … DISABLE TRIGGER` or role change on them raises a Critical alert (SC-10 rule), so the trail "cannot be disabled" (r.3(1) proviso [52]).
35. **Auditor access:** role `statutory_auditor` / `internal_auditor` (read-only, time-boxed, MFA). Available exports: `STATUTORY_BOOKS` and an audit-trail report per FY in the DI-C format, plus the r.3(6) disclosure data (AWS as provider, region addresses, IP ranges as provided) generated for the CS each year.
36. **Configurable facts** (`audit.applicability.*`, CS-owned, source and effective date, reviewed each April): s.138/r.13 thresholds [53], CARO 2020 exemption tests [54], small-company definition **[NC]**. The Compliance Cockpit shows per group company whether internal audit, CARO and IFC reporting apply, and feeds BestComply (D.7).

### DI-G. Audit-evidence catalogue (additions to Q §7.3 collectors)
| Collector | Control refs | Frequency | Output |
|---|---|---|---|
| `github_ruleset_export` | A.8.32, CC8.1 | Weekly + on change | Rulesets/environments JSON, diff vs baseline |
| `change_record_reconciliation` | A.8.32 | Weekly | Deploys without approved record (must be 0); emergency retro-reviews overdue |
| `saas_admin_change_recon` | A.8.32, A.8.9 | Weekly | M365/Brevo/GitHub admin events vs change records |
| `jml_sla_report` | A.5.18, SC-01 | Daily | Leaver revoke times; joiners without completed checks (must be 0) |
| `workspace_sku_role_check` | A.8.2, SC-15 | Daily | Privileged users on SKUs without CA/MDM (must be 0 or excepted) |
| `m365_audit_log_ingest` | A.8.15, CERT-In (iv) | Hourly | Entra sign-in/audit + M365 unified audit into log archive |
| `restore_test_results` | A.8.13, A1.3 | Weekly | AWS Backup restore-test jobs + validation outcome |
| `vault_lock_state` | A.8.13 | Daily | Vault lock mode/grace, Object Lock config |
| `ledger_audit_trail_check` | r.3(1) proviso, r.11(g) | Daily | Trigger/pgaudit enabled on ledger schemas; no mutation attempts unexplained |
| `export_run_register` | A.5.33, PC-39 | Per run | Bag validity, approvals, delivery, expiry |
| `vapt_engagement_record` | A.8.8, CERT-In guidelines | Per engagement | Empanelment list snapshot + hash, scope, CERT-In 5-day submission proof, closure report |
| `marketing_consent_sync` | PC-xx consent, NN-16 | Daily | Brevo ↔ Equator consent diffs (must be 0 after 15 min) |

### DI-H. Governed vs configurable vs OFF (summary)
- **Locked:**
  - leaver SLA floor 4 h;
  - no case data in workforce, marketing or social tools;
  - export validation gate;
  - signed originals never re-rendered;
  - ledger append-only, with an audit trail that cannot be disabled;
  - Vault Lock compliance mode in prod;
  - patch SLA floors;
  - prod OIDC bound to the environment;
  - no bypass outside break-glass.
- **Configurable (maker-checker):**
  - SKU rules;
  - UPN pattern;
  - deletion delay;
  - export labels, part size and format choices within the allowed set;
  - Brevo request budget;
  - social posting caps;
  - backup retention above floors;
  - audit-applicability facts.
- **OFF pending counsel or decision:**
  - `ops.workspace.google.enabled`;
  - `growth.brevo.sms_whatsapp.enabled` (DLT confirmation);
  - all `SOCIAL_PORT` publish adapters (platform approvals; BCI advertising review for neutral promotion);
  - `ops.adobe_embed.enabled`;
  - M365 third-party backup;
  - production-window VAPT testing (CS/CTO risk decision).

## Open points
1. **Which Microsoft SKU Equator holds.** No Microsoft plan is named "Business Starter" [1]. The CS should confirm from the admin centre or `subscribedSkus`. This report assumes Business Basic.
2. **Microsoft licensing details not confirmed:**
   - whether group-based licensing needs Entra ID P1 [20];
   - whether `usageLocation` is mandatory before `assignLicense`;
   - the mailbox provisioning delay after licensing;
   - shared-mailbox size and licence limits;
   - Audit (Standard) log retention on Basic;
   - whether Teams meeting **recording** is licensed on Basic;
   - India price and availability of Entra ID P1, Intune P1 and Defender for Business add-ons for Basic seats;
   - the Exchange application-RBAC mechanism for scoping `Mail.Send`.
3. **Mailbox size inconsistency:** 100 GB [1][2] vs 50 GB [4]. Check the tenant's quota.
4. **Google Workspace:** INR pricing; Admin SDK OAuth scopes and domain-wide delegation details; Gmail, Calendar and Drive endpoint specifics; Enterprise License Manager. Endpoint pages were not fetched.
5. **Brevo:**
   - INR prices for every tier [25];
   - whether CRM and campaign endpoints fall under the 100/h catch-all [21];
   - webhook retry policy;
   - CRM webhook configuration;
   - DPA and sub-processor list;
   - API-key IP restriction;
   - Indian DLT support for SMS and WhatsApp;
   - contact import/export field limits.
6. **Adobe:** whether a private or partner scheduling API exists; which Express plans include Content Scheduler.
7. **Social platforms:**
   - the Instagram 100 vs 50 posts/24 h inconsistency [31];
   - Facebook Pages publishing permissions and App Review (not fetched);
   - LinkedIn permission names and Standard-tier criteria beyond the screencast;
   - X API price volatility ("subject to change") [34].
8. **GitHub:** exact Enterprise Cloud wording for environment protections on private repositories; Secret Protection and Code Security prices.
9. **ESP long-term validation:** whether Leegality, Setu or Digio outputs embed LTV data (OCSP/CRL) for India CCA chains; preferred PDF/A part for signed outputs.
10. **Companies Act:**
    - r.3, r.13, CARO and r.11(g) texts were read from secondary reproductions. Re-verify against MCA or India Code gazette texts before citing in Board papers.
    - s.128(5) 8-year retention not re-read.
    - Current "small company" thresholds not verified.
    - Whether Equator Resolution Service Pvt Ltd is a subsidiary of a public company, which removes the CARO private-company exemption. This is a CS fact.
11. **CERT-In:** the original text of the 25 Jul 2025 audit guidelines and the current empanelment list were not opened (secondary summary [56] only). How the "production not tested" statement interacts with P14 FR-P14-04 needs a CTO/CS decision.
12. **ISO/IEC 29500-1 Edition 5:** publication expected after stage 60.00 (13 Oct 2026) [38]. Recheck in Q1 2027 and confirm Office's default conformance class.
13. **M365 backup:** whether to buy third-party backup for workforce mail and files (T3). This is a CS/CTO decision.
14. **Search budget:** 15 WebSearch calls used (≤ 30). Several official pages failed to load: the Microsoft 365 business service description, Brevo companies-CRM doc, and Brevo "secure-webhook-calls"; alternatives were used.
