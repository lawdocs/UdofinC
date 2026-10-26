# Appendix R — Configuration Framework and Settings Catalogue

> **Status:** Binding. LawDocs Build Prompt Pack v1.0, 25 October 2026. Owner: P03.
> **Used by:** P00–P23 (every phase registers its settings here before code reads them — NN-29), Appendix D (who may change), Appendix K (configuration export), Appendix W (open items).
>
> **How to use.** §R.1–§R.5 define the framework: key naming, tiers, control classes, merge rules and resolution order. §R.6–§R.7 list seed rule sets and configuration templates. §R.8 is the canonical item state graph. §R.9 is the master settings catalogue, grouped by module in the order of conventions §4. §R.10 says what each user type can customise. §R.11 is the open / interim / waiting item-type catalogue; §R.12 the waiting-party and chase defaults; §R.13 summarises who can change what. §R.14 is the compiled index of every further key registered in the phase files' §9 tables (609 keys; type and default live in the owner phase), so that §R.9 (586 rows, of which 2 are retired aliases) + §R.14 together form the complete registry seed (1,193 active keys after registry review G4, 25 Oct 2026; key families with a `<placeholder>` segment count once; duplicate-key check: none). A phase that needs a new key adds a row here in the same pull request as the code (`appendix-r-sync`). Where a phase file and this appendix disagree on a key's tier, class, default or maker-checker flag, the owning phase wins (master §18, X-11) and this appendix is corrected at the next `appendix-r-sync`; a disagreement that would weaken an NN rule is resolved in favour of the NN rule. Values marked [OWNER TO SET] are seeds; values marked [VERIFY] depend on a fact that must be logged in `docs/compliance/verification-log.md` before the key leaves its fallback (NN-38).

---

## R.1 Key naming, definition schema and abbreviations

- **Key:** `<module>.<area>.<key>`, snake_case, module code from conventions §4 only. Feature flags: `<module>.flag.<feature>`. Kill switches: `<module>.kill.<target>` (NN-39). Per-item families use a placeholder segment, e.g., `agt.autonomy.agent.<agent_code>`, `bil.streams.<stream_code>.enabled`.
- **Definition fields** (P03 FR-P03-02): tier, allowed scopes, control class and sub-class, type, default, bounds, merge strategy, child direction, maker-checker, effective dating, instance pinning, sensitivity, owner role, citation required, `depends_on_verify`, fallback kind, UI metadata (section, label key, help key `hlp.<module>.<term>`, user types), lifecycle versions.
- **Deprecation:** a deprecated key keeps `alias_of` or a migration for two releases; reads log a warning; removal follows expand-migrate-contract (NN-12).

**Abbreviations used in §R.9**

| Column | Values |
|---|---|
| Tier (owning tier → lowest scope that may override) | `PLT` platform · `BRD` brand · `PLN` plan · `TEN` tenant (Company, Personal or practice workspace) · `ENT` legal entity · `DEP` department · `USR` user. Example `TEN→USR` = set by tenant, overridable at entity, department and user. |
| Class | `L` LOCKED · `G` GOVERNED (`G-leg` legal, `G-elv` elevated: money/privilege/security/data-sharing, `G-prv` privacy, `G-int` integration) · `O` OPEN. Direction marks: `↑` raise-only, `↓` lower-only, `⊂` narrow-only |
| Type | `bool`, `int`, `dec`, `enum`, `menum` (multi), `dur` (ISO 8601), `win` (time window), `rrule`, `money` (₹, paise), `pct`, `colour`, `ref` (catalogue or rule-set reference), `json`, `text`, `list` |
| Changed by | Role codes (conventions §6). "user" = the user for their own scope. "—" = nobody in the product (LOCKED). "release" = platform release under a P23 `REGULATED` change |
| MC | Maker-checker: `Y` forces the GOVERNED pipeline with maker ≠ checker (NN-18); `N` = no checker (OPEN changes are still audited and undoable) |

---

## R.2 Tiers and control classes

### R.2.1 Tier tree

```
PLATFORM (LawDocs baseline; one)
 ├─ BRAND (LawDocs · [Consumer Help Brand] · white-label brands of firms)   — tokens, legal-entity profile, verticals, domains
 │   └─ PLAN (Free · Personal · Pro · Business · Enterprise; from OH8 entitlements) — limits and availability
 │       └─ TENANT (Company workspace · Personal workspace · practice workspace)
 │           └─ ENTITY (legal entity; hidden for Personal)
 │               └─ DEPARTMENT (hidden for Personal)
 │                   └─ USER (personal preferences; accessibility follows the person)
```

PLAN is a bounds layer, not an organisational parent: it sets limits and feature availability that cap every scope below. A Consumer Help tenant never inherits from a LawDocs tenant (NN-23).

### R.2.2 Control classes

| Aspect | LOCKED (L) | GOVERNED (G) | OPEN (O) |
|---|---|---|---|
| Content | NN rules; statutory protections of signers, counterparties, consumers, data principals and employees; audit and evidence integrity; security baselines; India residency; canonical state machines | Legal parameters and rule sets; retention floors; money, price, fee, payout and revenue-stream switches; privilege and data-sharing controls; vendor and outbound-channel settings; anything in the NN-18 list | Operational choices inside the tenant or for the user |
| Change path | Release + ADR + NN test (P23 `REGULATED`) | Change request: preview, citation (legal), effective date, impact, step-up approval by a different person | Immediate, audited, undoable |
| Badge | "Locked" + padlock + reason link | "Needs approval" + approver role | "Editable" |

### R.2.3 Decision test (first "yes" wins)

| # | Question | Result |
|---|---|---|
| Q1 | Does the value implement an NN rule, protect a third party's statutory right, keep audit/evidence integrity, enforce a security baseline or residency? | **L** (or L floor + bounded O margin) |
| Q2 | Does it move money, set a price or fee, grant a privilege, open data to another party, or appear in the NN-18 list? | **G-elv**, MC = Y |
| Q3 | Does it derive from a statute, rule, regulator direction, court rule, professional rule or standard, or change a deadline, eligibility, formality, filing or retention? | **G-leg**, citation required |
| Q4 | Does it depend on an unconfirmed external fact? | **G**, flag OFF or advisory-only, declared fallback (NN-38) |
| Q5 | Is it operational, reversible and confined to the tenant's or user's own work? | **O** |

Tie-break: the stricter class. Split floor and margin.

### R.2.4 NN-18 critical keys (MC = Y regardless of tier; CI check `nn18-keys`)

Approval matrices and authority limits (`clm.approval.*`, `lgo.spend.approval_threshold_inr`) · payment, refund and credit settings (`bil.refund.*`, `bil.credits.*` grants) · access and delivery grants (`sdc.grant.*`, `iam.ip_allowlist`, `iam.sso.enforce_for_domain`) · tenant data-export approval (`xpt.export.*` approval keys) · role elevation and break-glass (`iam.breakglass.*`) · master-data change policy (`org.master_data.change_policy`) · template, rule and content publication (`tpl.publish.*`, `rul.*` publication) · prices, plan limits and revenue streams (`bil.price.*`, `bil.streams.*`, `mkp.fees.*`, `sgn.estamp.facilitation_fee_inr`) · bulk delete (`dms.bulk_delete.*`) · agent autonomy (`agt.autonomy.*`) · kill-switch release · outbound channels (`ntf.channels.*`) · BYO targets for regulated classes (`xpt.targets.*`) · credential vault enablement and reveal policy (`cvl.*`).

---

## R.3 Merge strategies and direction constraints

| Strategy | Used for | Rule |
|---|---|---|
| `most_specific` | Labels, templates, branding, defaults | Deepest scope with a valid value wins |
| `strictest` | Clocks, thresholds, limits, internal SLAs with floors | Most protective per `protective_direction` |
| `intersection` | Allowed channels, login methods, enabled modules, allowed file types, allowed signing methods | Only what every layer allows |
| `union` | Block lists, mandatory disclosures, required evidence, escalation recipients | Everything any layer requires |
| `longest` | Retention, cooling-off, record-keeping | Longest applicable; legal hold overrides deletion |
| `additive` | Tags, custom fields, saved views, widgets, quick actions | Combined; children hide but cannot delete parent items |

Direction: `⊂` narrow-only (quiet hours, channels), `↑` raise-only (reminder lead days, retention, warning days), `↓` lower-only (session length, chase counts, upload limits). The validator compares against the parent's resolved value.

---

## R.4 Resolution order

1. LOCKED value. 2. Active kill switch or emergency block. 3. Instance pin (`instance_pinned` and an instance context). 4. Most specific valid value USER → DEPARTMENT → ENTITY → TENANT, combined by merge strategy. 5. PLAN value. 6. BRAND value. 7. PLATFORM value, then the definition default. 8. Declared fallback if the value is unapproved, past review, or depends on an unverified fact.

Bounds = PLATFORM ∩ BRAND ∩ PLAN ∩ parent locks. Each read returns `{value, source_tier, source_scope_id, source_version, control_class, fallback_applied}`.

---

## R.5 Brand and plan seeds

| Brand | Purpose | Notable values |
|---|---|---|
| `LD` | LawDocs | All verticals except Consumer Help; Vidhi persona; lawdocs.in domains |
| `CH` | `[Consumer Help Brand]` (D-06) | Own legal-entity profile, domains, sender identities, help space; `chp.*` verticals; ethical wall; `xpt.naming.person_mode = ids_only` (L) |
| `WL-<firm>` | White-label workspace for a law, CA or CS firm (`LD-ADD-WL`) | Firm logo and domain; LawDocs legal footer and policies remain (L) |

Plan limits seeded from R6 §R6.2.2 [OWNER TO SET]: vault 1/10/50/250 GB/1 TB+; AI credits 30/300/1,500/6,000/25,000+ per month; Aadhaar eSign credits 0/2/10/50/contracted per month; litigation 1/5/50/300/unlimited by band; trademarks 1/3/10/50/unlimited; entities —/—/1/3/groups.

---

## R.6 Rule-set catalogue (seed; P03 FR-P03-54)

| Rule set | Domain | Effect class | Content owner | Volatile |
|---|---|---|---|---|
| `rulepack.IN.core.legal_register` | Runtime rows for R3 `LG-xxx` used by code paths | mixed | P03 | — |
| `rulepack.IN.sgn.eligibility` | Instrument eligibility (Appendix F; IT Act First Schedule as amended 26 Sep 2022 — R3 LG-003) | protective | P08 | — |
| `rulepack.IN.sgn.formalities` | Witness, notarisation, registration (Registration Act 1908 s.17), board approval per instrument | protective | P08 | — |
| `rulepack.IN-<ST>.stamp.duty_table` | Stamp duty per article per State (data only) | computational | P08 | Yes (budget months) |
| `rulepack.IN-<ST>.estamp.channels` | Authorised eStamp/e-SBTR/franking routes per State (NN-08) | permissive | P08 | Yes |
| `rulepack.IN-<ST>.registration.thresholds` | Registration requirements per instrument (e.g., lease terms) [VERIFY per State] | protective | P08 | — |
| `rulepack.IN.esp.registry` | ESP list with licence validity (R3 LG-005) | protective | P08 | Yes |
| `rulepack.IN.lit.limitation_advisory` | Limitation Act 1963 Schedule mapping (advisory) | computational (advisory) | P11 | — |
| `rulepack.IN.lit.court_formats` | Page setup and format rules per court [VERIFY per court] | computational | P10 | — |
| `rulepack.IN.ipm.tm_timelines` | TM examination reply, opposition, renewal windows [VERIFY sections] | computational | P12 | — |
| `rulepack.IN.mca.board_meetings` | Companies Act 2013 s.173 meeting rules | computational | P13 | — |
| `rulepack.IN.icsi.ss1_ss2` | Secretarial Standards timelines [VERIFY paras] | computational | P13 | — |
| `rulepack.IN.chp.rbios_2026` | RB-IOS 2026 timelines and representation rules [VERIFY clauses] | protective | P15 | Yes |
| `rulepack.IN.chp.insurance_ombudsman` | Insurance Ombudsman cap and window (R2) | computational | P15 | — |
| `rulepack.IN.chp.consumer_commission` | Consumer Protection Act 2019 forum and pecuniary limits [VERIFY current limits] | computational | P15 | — |
| `rulepack.IN.chp.challans` | Deep-link map to official challan portals; no payment routing | protective | P15 | Yes |
| `rulepack.IN.privacy.dpdp` | DPDP Act/Rules clocks and commencement (R3 LG-061–072) | protective | P01 | Yes |
| `rulepack.IN.it.intermediary` | IT Rules 2021 as amended 2026 grievance and takedown (R3 LG-077) | protective | P21 | Yes |
| `rulepack.IN.certin.incident` | CERT-In 6-hour clock, log retention (R3 LG-079) | protective | P23 | — |
| `rulepack.IN.ntf.tcccpr` | DLT, consent, calling windows, AI-voice disclosure [VERIFY 2026 amendment] | protective | P19 | Yes |
| `rulepack.IN.mkp.profession_rules` | BCI Rule 36 directory fields; advocate fee restrictions; CA/CS switches (NN-21) | protective | P16 | — |
| `rulepack.IN.tax.calendars` | GST/TDS/ITR due dates [VERIFY under Income-tax Act 2025] | computational | P14 | Yes |
| `rulepack.IN.hr.labour` | Pointer to shared `infrabyx-labour-rulepack` (pinned) | computational | P13 | Yes |
| `rulepack.IN.default.reminders` | Default reminder offsets per object | computational | P03 | — |
| `rulepack.IN.default.sla` | Internal SLA defaults and business calendars (national + State holidays) | computational | P03 | Annual |
| `rulepack.IN.retention.classes` | Retention classes and floors (§R.9 `dms.retention.*`) | protective | P04 | — |

---

## R.7 Configuration template library (seed; P03 FR-P03-94)

| Template | For | Contents (highlights) |
|---|---|---|
| `TPL-IND-FAMILY` | Individual and family vault | Personal categories (Property, Family and Succession, Vehicles, Finance and Insurance, Employment, Disputes, Tax, Receipts), expiry reminders, nominee policy prompts, home widgets for individuals |
| `TPL-STARTUP-LEAN` | Startups (Pro) | Founders as admins, single checker, startup agreement statuses, ESOP/SHA item types, 3 quick actions |
| `TPL-SME-TWO-PERSON` | SMEs | Maker-checker on all agreements above ₹1 lakh, renewal desk, vendor intake form, numbering `{ENTITY}/{FY}/{SEQ:4}` |
| `TPL-LEGAL-DEPT` | Company legal department (Business/Enterprise) | Legal intake desk, triage SLAs, approval matrix by value bands, CLO dashboard, counsel panel, litigation item types, spend approvals |
| `TPL-NBFC-LEGAL` | Lenders and other regulated entities | As `TPL-LEGAL-DEPT` + loan-document item types, recovery notice item types, LDC SoR mode for governance (D-10), India-only BYO targets |
| `TPL-LAW-PRACTICE` | Advocate or firm practice workspace | Matter numbering, hearing reminders, client-intake forms, letterheads, engagement deliverable items |
| `TPL-CA-CS-PRACTICE` | CA/CS practice | Compliance-service deliverables, client document requests (waiting on `CLIENT`), filing evidence items |
| `TPL-CH-DESK` | Consumer Help case desk | Grievance item types with forum clocks, non-advocate case-manager routing, ids-only naming |

---

## R.8 Canonical item states and transitions (LOCKED; P03 FR-P03-68)

| From \ To | IN_PROGRESS | INTERIM | WAITING | ON_HOLD | RESOLVED | WAIVED | CANCELLED | SUPERSEDED |
|---|---|---|---|---|---|---|---|---|
| `OPEN` | ✓ | — | ✓ | ✓ | ✓ (if no work needed) | ✓ (authorised) | ✓ | ✓ |
| `IN_PROGRESS` | — | ✓ | ✓ | ✓ | ✓ | ✓ (authorised) | ✓ | ✓ |
| `INTERIM` | ✓ | ✓ (new interim) | ✓ | ✓ | ✓ | ✓ (authorised) | ✓ | ✓ |
| `WAITING` | ✓ (response/resume) | ✓ | ✓ (new party) | ✓ | ✓ (if response completes it) | ✓ (authorised) | ✓ | ✓ |
| `ON_HOLD` | ✓ | — | ✓ | — | — | ✓ (authorised) | ✓ | ✓ |
| `RESOLVED` | ✓ (reopen with reason, within `wf.items.reopen_days`) | — | — | — | — | — | — | — |
| `WAIVED`, `CANCELLED`, `SUPERSEDED` | terminal | | | | | | | |

Legal clocks continue in every non-terminal state. `INTERIM` and `WAITING` never count as complete. Waive is never available to `AGT_*` principals (NN-43).

---

## R.9 Master settings catalogue (by module)

Owner phase in brackets after each module heading. Rows are the minimum registry seed; phases may add keys through `appendix-r-sync`.

### R.9.1 `core` — tenancy, audit, IDs, privacy clocks (P00, P01, P23)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `core.audit.append_only` | PLT | L | bool | true (NN-02) | — | — |
| `core.audit.anchor_frequency` | PLT | G | enum daily/hourly | daily | `PLT_SECURITY_OFFICER` | Y |
| `core.audit.same_txn_required` | PLT | L | bool | true (NN-45) | — | — |
| `core.correction.dual_approval` | PLT | L | bool | true | — | — |
| `core.correction.reason_min_chars` | PLT | L | int | 20 | — | — |
| `core.correction.client_approval_crucial_details` | PLT | L | bool | true (CH-26) | — | — |
| `core.ids.business_ref_pattern` | PLT | L | text | `LD-<TYPE>-<YYYY>-<6 digits>` | — | — |
| `core.residency.primary_region` | PLT | L | enum | ap-south-1; DR ap-south-2 (NN-25) | — | — |
| `core.residency.transfer_assessment_required` | PLT | L | bool | true | — | — |
| `core.time.ntp_sources` | PLT | L | list | NIC/NPL servers (CERT-In Directions 2022) | — | — |
| `core.logs.pii_scrubbing` | PLT | L | bool | true (NN-32) | — | — |
| `core.operating_entity.profile` | PLT | G-elv | ref | `[LawDocs Operating Entity]` (D-08) | `PLT_SUPER_ADMIN` | Y |
| `core.timezone.default` | TEN→USR | O | enum IANA | Asia/Kolkata | `ORG_ADMIN`, user | N |
| `core.locale.date_format` | TEN→USR | O | enum | DD-MMM-YYYY | `ORG_ADMIN`, user | N |
| `core.locale.number_grouping` | TEN→USR | O | enum indian/international | indian | `ORG_ADMIN`, user | N |
| `core.fy.start_month` | ENT | G-leg | int 1–12 | 4 (April) | `ORG_ADMIN` → `ORG_CLO` | Y |
| `core.privacy.grievance_ack_hours` | PLT | G-leg (L floor) | int ≤ 24 | 24 (R3 LG-077) | `PLT_DPO` | Y |
| `core.privacy.grievance_resolution_days` | PLT | G-leg (L floor) | int ≤ 7 | 7 [VERIFY post-2026 text] | `PLT_DPO` | Y |
| `core.privacy.dsr_max_days` | PLT | L | int | 90 (DPDP Rules r.14(3)) | — | — |
| `core.privacy.dsr_internal_target_days` | PLT→TEN ↓ | G-prv | int ≤ 90 | 30 | `PLT_DPO`; tenant privacy contact | Y |
| `core.privacy.erasure_notice_hours` | PLT | G-prv | int ≥ 48 | 48 (r.8; applied to all) | `PLT_DPO` | Y |
| `core.privacy.min_account_age_years` | PLT | G-leg | int | 18 (s.9; R3 LG-066) | `PLT_DPO` | Y |
| `core.privacy.foreign_regime_triggers` | PLT | G-prv | menum EU_RESIDENT/UK/US_CA | off until trigger (CH-18) | `PLT_DPO` | Y |
| `core.breach.certin_hours` | PLT | L | int | 6 | — | — |
| `core.breach.dpdp_report_hours` | PLT | G-leg (L floor) | int | 72 (r.7) [VERIFY commencement] | `PLT_DPO` | Y |
| `core.breach.tenant_notice_target_hours` | PLT ↓ | G | int | 2 | `PLT_SECURITY_OFFICER` | Y |
| `core.breach.negd_hours` | PLT | G-leg | int | 24 (DigiLocker terms) [VERIFY] | `PLT_DPO` | Y |

### R.9.2 `iam` — accounts, sessions, MFA, grants (P01, P02)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `iam.login.aadhaar_as_login` | PLT | L | bool | false (NN-03, CH-01) | — | — |
| `iam.login.methods` | BRD→TEN ∩ | G-elv | menum mobile_otp/email_otp/passkey/password_mfa/sso | OTP, passkey, password+MFA; SSO on Business+ | `ORG_ADMIN` | Y |
| `iam.passkeys.enabled` | BRD→USR | O | bool | true | user | N |
| `iam.mfa.required_roles` | TEN (add only) | G-elv | menum | admins, approvers, KMP, delegated makers, auditors | `ORG_ADMIN` | Y |
| `iam.mfa.staff_phishing_resistant` | PLT | L | bool | true | — | — |
| `iam.password.min_length` | PLT→TEN ↑ | G | int ≥ 12 | 12 | `ORG_ADMIN` | N |
| `iam.session.idle_timeout_minutes` | PLT→TEN ↓ | G-elv | int 5–60 | 30 (web), 15 (console) | `ORG_ADMIN` | Y |
| `iam.session.absolute_hours` | PLT→TEN ↓ | G-elv | int 1–24 | 12 | `ORG_ADMIN` | Y |
| `iam.session.mobile_reauth_days` | TEN ↓ | G | int 1–90 | 30 | `ORG_ADMIN` | N |
| `iam.stepup.max_age_minutes` | PLT | L | int | 10 | — | — |
| `iam.sso.enforce_for_domain` | TEN | G-elv | bool | false | `ORG_OWNER` | Y |
| `iam.scim.enabled` | PLN→TEN | G-int | bool | false (Business+ add-on) | `ORG_ADMIN` | Y |
| `iam.ip_allowlist` | TEN | G-elv | list CIDR | none | `ORG_ADMIN` | Y |
| `iam.guest.magic_link_hours` | TEN ↓ | G | int 1–168 | 72 | `ORG_ADMIN` | N |
| `iam.guest.otp_required` | PLT | L | bool | true | — | — |
| `iam.delegation.max_days` | TEN ↓ | G | int 1–90 | 30 (P02 §9) | `ORG_ADMIN` | N |
| `iam.breakglass.dual_approval` | PLT | L | bool | true | — | — |
| `iam.breakglass.client_report_hours` | PLT | L | int | 24 (NN-17) | — | — |
| `iam.devices.max_per_user` | TEN ↓ | G | int 1–10 | 5 | `ORG_ADMIN` | N |

### R.9.3 `kyc` — verification and consent artefacts (P01)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `kyc.aadhaar.store_full_number` | PLT | L | bool | false (NN-04) | — | — |
| `kyc.aadhaar.keep_last_digits` | PLT | L | int | 4 | — | — |
| `kyc.aadhaar.mask_first_digits_in_derived_text` | PLT | L | int | 8 | — | — |
| `kyc.ckyc.enabled` | PLT | L | bool | false (NN-05, CH-03) | — | — |
| `kyc.bureau_pull.enabled` | PLT | L | bool | false (CH-05) | — | — |
| `kyc.portal_scraping.enabled` | PLT | L | bool | false (NN-05) | — | — |
| `kyc.methods` | BRD→TEN ∩ | G | menum digilocker/aadhaar_offline_qr/aadhaar_offline_xml/pan_vendor/gstin_vendor/cin_vendor | digilocker, aadhaar_offline_qr | `ORG_ADMIN` | Y |
| `kyc.ovse.qr.enabled` | PLT | G | flag (verify-gated) | false until the secure-QR/e-Aadhaar offline route is verified (NN-38; X-11) | `PLT_SUPER_ADMIN` + `PLT_DPO` | Y |
| `kyc.ovse.avc.enabled` | PLT | G | flag (verify-gated) | false until OVSE registration is recorded (NN-38; X-11) | `PLT_SUPER_ADMIN` + `PLT_DPO` | Y |
| `kyc.digilocker.retain_copy.enabled` | PLT | G-prv | flag (verify-gated, NeGD requester terms) | false — store URI and verification result only (X-11; NN-42) | `PLT_SUPER_ADMIN` + `PLT_DPO` | Y |
| `kyc.kyb.vendor_primary` / `kyc.kyb.vendor_secondary` | PLT | G-int | ref | licensed MCA-data vendors (R6 D-15) [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `kyc.counterparty.verification_level` | TEN→DEP | O | enum none/otp/digilocker/aadhaar_offline | otp | `ORG_ADMIN` | N |
| `kyc.reverify.company_months` | TEN | O | int 6–60 | 24 | `ORG_ADMIN` | N |
| `kyc.consent.notice_version` | PLT | G-prv | ref | current notice per purpose | `PLT_DPO` | Y |
| `kyc.consent.bundling_allowed` | PLT | L | bool | false (DPDP s.6) | — | — |

### R.9.4 `org` — organisation, user types, limits (P02)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `org.entities.max` | PLN | G-elv | int | Pro 1 · Business 3 · Enterprise by band | `PLT_SUPER_ADMIN` | Y |
| `org.seats.working` | PLN | G-elv | int | Pro 3 · Business 10 | `PLT_SUPER_ADMIN` | Y |
| `org.seats.free_viewers_approvers` | PLN | G-elv | bool | Business true | `PLT_SUPER_ADMIN` | Y |
| `org.family.max_members` | PLN | G-elv | int | Personal 5 (+5 add-on) | `PLT_SUPER_ADMIN` | Y |
| `org.user_types.enabled` | TEN | O | menum | per template | `ORG_ADMIN` | N |
| `org.departments.max` | PLN | G | int | Business 25 · Enterprise 200 | `PLT_SUPER_ADMIN` | N |
| `org.delegated_maker.allowed` | TEN | G-elv | bool | true | `ORG_OWNER` | Y |
| `org.delegated_maker.client_checker_required` | PLT | L | bool | true (R-064) | — | — |
| `org.master_data.change_policy` | TEN | G-elv | enum `maker_checker` / `maker_checker_plus_owner` (tighten only) | `maker_checker` (no `owner_only` option exists — X-11, NN-18; staff changes follow Appendix A §A.56) | `ORG_OWNER` | Y |
| `org.kmp.roles` | ENT | G-leg | menum | MD/CEO, CFO, CS (Companies Act s.2(51)) | `ORG_ADMIN` → `ORG_CLO` | Y |
| `org.maker_checker.sod_enforced` | PLT | L | bool | true (NN-18) | — | — |

### R.9.5 `cfg` — settings registry and Configuration Studio (P03)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `cfg.registry.require_registration` | PLT | L | bool | true (NN-29) | — | — |
| `cfg.change_requests.expiry_days` | TEN | O | int 7–30 | 14 | `ORG_ADMIN` | N |
| `cfg.change_requests.approval_sla_working_days` | TEN | O | int 1–10 | 2 | `ORG_ADMIN` | N |
| `cfg.change_requests.legal_lead_time_hours` | PLT | G-leg | int ≥ 0 | 24 | `PLT_LEGAL_REVIEWER` | Y |
| `cfg.batches.undo_window_hours` | TEN | O | int 1–168 | 24 | `ORG_ADMIN` | N |
| `cfg.toast_undo_seconds` | USR | O | int 5–30 | 10 | user | N |
| `cfg.tenant.require_approval_keys` | TEN | G-elv | menum | [] | `ORG_OWNER` | Y |
| `cfg.delegation.department_sections` | TEN | O | menum | labels, reminders, dashboards | `ORG_ADMIN` | N |
| `cfg.user.follow_person_preferences` | USR | O | bool | true | user | N |
| `cfg.custom_fields.max_per_object` | PLN | G-elv | int | 5 / 10 / 25 / 75 / 150 | `PLT_SUPER_ADMIN` | Y |
| `cfg.item_types.max_tenant_defined` | PLN | G-elv | int | 3 / 10 / 25 / 100 / 300 | `PLT_SUPER_ADMIN` | Y |
| `cfg.sandbox.enabled` | PLN→TEN | O | bool | Business+ true | `ORG_ADMIN` | N |
| `cfg.templates.offer_by_staff` | PLT | G | bool | true (maker only) | `PLT_SUPER_ADMIN` | N |
| `cfg.theme.mode_default` | BRD→USR | O | enum light/dark/high_contrast/system | system | `ORG_ADMIN`, user | N |
| `cfg.theme.high_contrast_available` | PLT | L | bool | true | — | — |
| `cfg.theme.primary_colour` / `cfg.theme.accent_colour` | BRD→TEN | O | colour (contrast-validated) | brand tokens | `ORG_ADMIN` | N |
| `cfg.theme.logo` | BRD→ENT | O | ref asset | brand logo | `ORG_ADMIN` | N |
| `cfg.ui.density` | TEN→USR | O | enum comfortable/compact/spacious | comfortable | `ORG_ADMIN`, user | N |
| `cfg.ui.text_scale_percent` | USR | O | int 100–200 | 100 | user | N |
| `cfg.ui.reduced_motion` | USR | O | bool | system | user | N |
| `cfg.ui.underline_links` | USR | O | bool | false | user | N |
| `cfg.ui.dyslexia_font` | USR | O | bool | false | user | N |
| `cfg.ui.screen_reader_hints` | USR | O | enum standard/verbose | standard | user | N |
| `cfg.ui.language` | TEN→USR | O | enum (D-07 set) | en | `ORG_ADMIN`, user | N |
| `cfg.ui.shortcuts_enabled` | USR | O | bool | true (WCAG 2.1.4 remap/off) | user | N |
| `cfg.home.layout` | BRD→USR | O (mandatory widgets L) | json | per user type | `ORG_ADMIN`, user | N |
| `cfg.nav.hidden_modules` | TEN→DEP | O | menum | [] | `ORG_ADMIN` | N |
| `cfg.nav.order` | TEN→USR | O | list | per user type | `ORG_ADMIN`, user | N |
| `cfg.nav.max_pinned_items` | PLT | G | int | 8 | `PLT_SUPER_ADMIN` | N |
| `cfg.nav.landing_page` | TEN→USR | O | ref | Home | `ORG_ADMIN`, user | N |
| `cfg.quick_actions.set` | TEN→USR | O | list | per user type | `ORG_ADMIN`, user | N |
| `cfg.quick_actions.max_per_user` | PLT | G | int | 6 | `PLT_SUPER_ADMIN` | N |
| `cfg.terminology.overrides` | BRD→DEP | O (statutory terms L) | json per locale | none | `ORG_ADMIN` | N |
| `cfg.statuses.sets` | TEN→DEP | O (canonical map L) | json | platform sets | `ORG_ADMIN` | N |
| `cfg.reason_codes.lists` | TEN | O (minimum entries L) | json | platform lists | `ORG_ADMIN` | N |
| `cfg.numbering.display_reference_enabled` | TEN→ENT | O | bool | false | `ORG_ADMIN` | N |
| `cfg.numbering.patterns` | ENT | O | json | none | `ORG_ADMIN` | N |
| `cfg.numbering.reset` | ENT | O | enum none/FY/CY | FY | `ORG_ADMIN` | N |
| `cfg.forms.publish_requires_a11y_lint` | PLT | L | bool | true | — | — |
| `cfg.letterhead.default` | ENT | O | ref | brand default | `ORG_ADMIN` | N |
| `cfg.letterhead.min_font_pt` | PLT | L | int | 9 | — | — |
| `cfg.sender.domain` | TEN | G-int | text | brand domain "on behalf of" | `ORG_ADMIN` | Y |
| `cfg.flags.release_flag_max_age_days` | PLT | G | int | 90 | `PLT_RELEASE_MANAGER` | N |
| `cfg.kill_switch.release_second_person` | PLT | L | bool | true | — | — |
| `cfg.kill_switch.propagation_seconds` | PLT | L | int | 60 | — | — |
| `cfg.kill_switch.drill_frequency_days` | PLT | G | int 30–180 | 90 | `PLT_SECURITY_OFFICER` | Y |
| `cfg.support_session.max_hours` | PLT→TEN ↓ | G | int 1–24 | 2 | `ORG_ADMIN` | N |
| `cfg.nl_assistant.enabled` | TEN→USR | O | bool | true (L2; no writes) | `ORG_ADMIN`, user | N |

### R.9.6 `rul` — rule engine and content versions (P03)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `rul.engine.primary` | PLT | G-int | enum zen/json_logic | zen | CTO (ADR) | Y |
| `rul.evaluation.deterministic` | PLT | L | bool | true | — | — |
| `rul.evaluation.cel_cost_budget` | PLT | G | int | 10,000 units | CTO | N |
| `rul.reviewer_of_record.required` | PLT | L | bool | true (NN-30) | — | — |
| `rul.reviewer.must_differ_from_maker` | PLT | L | bool | true | — | — |
| `rul.publish.requires_golden_pass` | PLT | L | bool | true | — | — |
| `rul.review.default_days` | PLT | G | int 30–365 | 180 | `PLT_LEGAL_REVIEWER` | Y |
| `rul.review.secondary_only_days` | PLT | G | int | 90 | `PLT_LEGAL_REVIEWER` | Y |
| `rul.review.volatile_days` | PLT | G | int | 30 | `PLT_LEGAL_REVIEWER` | Y |
| `rul.adoption.max_pin_days` | PLT | G-leg | int 0–90 | 30 (0 for protective) | `PLT_LEGAL_REVIEWER` | Y |
| `rul.tenant_rules.enabled` | PLN→TEN | O | bool | Business+ true | `ORG_ADMIN` | N |
| `rul.unverified.computational_label` | PLT | L | text | "Indicative — under verification" | — | — |
| `rul.challenge.response_working_days` | PLT | G | int | 10 | `PLT_LEGAL_REVIEWER` | N |
| `rul.what_changed.ack_required` | TEN | O | bool | true | `ORG_ADMIN` | N |

### R.9.7 `wf` — approvals, SLAs and open/interim/waiting items (P02, P03)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `wf.approval.maker_not_checker` | PLT | L | bool | true (NN-18) | — | — |
| `wf.approval.expiry_days` | TEN | O | int 3–30 | 14 | `ORG_ADMIN` | N |
| `wf.approval.sla_working_days` | TEN→DEP | O | int 1–10 | 2 | `ORG_ADMIN`, `ORG_DEPT_HEAD` | N |
| `wf.approval.agents_may_approve` | PLT | L | bool | false (NN-43) | — | — |
| `wf.sod.self_sign_threshold_inr` | TEN | G-elv | money | 0 — warn on every document an authorised signatory made and signs as the entity; tenant may raise the threshold or switch the rule to Block [OWNER TO SET] (Appendix D SoD-14; registered at registry review G4, P02 to confirm) | `ORG_OWNER` | Y |
| `wf.sla.business_calendar` | ENT | O | ref | national + State holidays (State of entity) | `ORG_ADMIN` | N |
| `wf.sla.working_week` | ENT | O | enum Mon–Fri/Mon–Sat | Mon–Sat | `ORG_ADMIN` | N |
| `wf.items.legal_clock_pausable` | PLT | L | bool | false | — | — |
| `wf.items.legal_warning_days` | TEN→DEP ↑ | O (floor 3) | int 3–60 | 7 | `ORG_CLO` | N |
| `wf.items.default_chase_cadence` | TEN→DEP | O | dur P1D–P14D | P3D | `ORG_ADMIN`, `ORG_DEPT_HEAD` | N |
| `wf.items.max_chases_internal` | TEN | O | int 1–20 | 5 | `ORG_ADMIN` | N |
| `wf.items.max_chases_external` | PLT→TEN ↓ | G | int 1–5 | 3 | `ORG_ADMIN` | Y |
| `wf.items.external_chase_mode` | TEN | G-elv | enum CONFIRM_EACH/PRE_APPROVED_SERIES | CONFIRM_EACH (OI-P03-05) | `ORG_ADMIN` → `ORG_CLO` | Y |
| `wf.items.auto_contact_courts_registries_regulators` | PLT | L | bool | false (NN-05) | — | — |
| `wf.items.internal_sla_pause_reasons` | TEN | O | menum | counterparty, client, vendor outage | `ORG_ADMIN` | N |
| `wf.items.escalation.l2_after` | TEN→DEP | O | dur | P2D after expected_by | `ORG_ADMIN` | N |
| `wf.items.escalation.l3_mandatory_for_legal` | PLT | L | bool | true | — | — |
| `wf.items.stalled_after_days` | TEN→USR | O | int 3–60 | 14 | `ORG_ADMIN`, user | N |
| `wf.items.reopen_days` | TEN | O | int 0–90 | 30 | `ORG_ADMIN` | N |
| `wf.items.waive_roles` | TEN | G-elv | menum | `ORG_CLO`, `ORG_APPROVER` (Company); `IND_OWNER` (Personal) | `ORG_OWNER` | Y |
| `wf.items.waive_reason_min_chars` | PLT | L | int | 20 | — | — |
| `wf.items.shared_external_label_required` | PLT | L | bool | true | — | — |
| `wf.items.bulk_preview_threshold` | TEN | O | int | 50 | `ORG_ADMIN` | N |
| `wf.formalities.gate_enforced` | PLT | L | bool | true (NN-40) | — | — |
| `wf.reminders.my_items_digest_time` | USR | O | time | 08:30 | user | N |

### R.9.8 `ntf` — notifications, channels, telecom (P00, P19)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `ntf.channels.enabled` | BRD→TEN ∩ | G-elv | menum in_app/email/push/sms/whatsapp/rcs/voice/teams/gchat | in_app, email, push; others opt-in | `ORG_ADMIN` | Y |
| `ntf.dlt.require_template_id` | PLT | L | bool | true (NN-34) | — | — |
| `ntf.dlt.entity_id` | BRD | G-int | text | [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `ntf.counterparty.max_invitations` | PLT | L | int | 1 (NN-34) | — | — |
| `ntf.counterparty.max_reminders` | PLT→TEN ↓ | G | int 0–5 | 3 | `ORG_ADMIN` | Y |
| `ntf.counterparty.opt_out_link` | PLT | L | bool | true | — | — |
| `ntf.voice.automated_calls_require_opt_in` | PLT | L | bool | true | — | — |
| `ntf.voice.ai_disclosure_and_handoff` | PLT | L | bool | true | — | — |
| `ntf.voice.predeclared_numbers_only` | PLT | L | bool | true [VERIFY TCCCPR 2026] | — | — |
| `ntf.voice.calling_window` | PLT→TEN ⊂ | G-leg | win | 10:00–19:00 IST [REC]; statutory window [VERIFY TCCCPR] | `PLT_LEGAL_REVIEWER` | Y |
| `ntf.quiet_hours.window` | TEN→USR ⊂ | O | win | 21:00–08:00 IST | `ORG_ADMIN`, user | N |
| `ntf.budget.daily_interruptive` | TEN→USR ↓ | O | int 5–50 | 15 | `ORG_ADMIN`, user | N |
| `ntf.digest.times` | TEN→USR | O | list | 09:00, 17:00 | `ORG_ADMIN`, user | N |
| `ntf.dedupe.window_minutes` | TEN | O | int 5–1440 | 60 | `ORG_ADMIN` | N |
| `ntf.push.lockscreen_preview` | USR | O | bool | false (NN-44) | user | N |
| `ntf.templates.variable_whitelist_only` | PLT | L | bool | true (NN-32) | — | — |
| `ntf.marketing.consent_required` | PLT | L | bool | true | — | — |
| `ntf.kill.<channel>` | PLT/BRD/TEN | G | bool | off | `PLT_SECURITY_OFFICER`; `ORG_ADMIN` (tenant channels) | Release Y |

### R.9.9 `msg` — messaging, threads, deal-room chat (P07)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `msg.deal_room.chat_enabled` | TEN→DEP | O | bool | true | `ORG_ADMIN` | N |
| `msg.internal_comments.visible_externally` | PLT | L | bool | false (NN-37) | — | — |
| `msg.external_participants.allowed` | TEN | G-elv | bool | true | `ORG_ADMIN` | Y |
| `msg.attachments.max_mb` | PLN | G | int | 25 / 50 / 100 | `PLT_SUPER_ADMIN` | N |
| `msg.edit_window_minutes` | PLT | G | int 0–60 | 5 (edits keep history; P07 §9) | `PLT_SUPER_ADMIN` | N |
| `msg.read_receipts` | TEN→USR | O | bool | true | `ORG_ADMIN`, user | N |
| `msg.retention_class` | TEN | G-leg | ref | as parent record | `ORG_CLO` | Y |
| `msg.ai_summary.enabled` | TEN→USR | O | bool | true (labelled) | `ORG_ADMIN`, user | N |

### R.9.10 `dms` — Legal Vault and DMS (P04)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `dms.originals.object_lock_mode` | PLT | L | enum | compliance (NN-09) | — | — |
| `dms.hash.algorithm` | PLT | L | enum | SHA-256 | — | — |
| `dms.versions.keep_all` | PLT | L | bool | true | — | — |
| `dms.folders.views_over_ids` | PLT | L | bool | true (NN-12) | — | — |
| `dms.storage.quota_gb` | PLN | G-elv | int | 1 / 10 / 50 / 250 / 1,024+ | `PLT_SUPER_ADMIN` | Y |
| `dms.upload.max_file_mb` | PLN | G | int | 200 (plan-dependent; P04 §9) | `PLT_SUPER_ADMIN` | Y |
| `dms.upload.av_scan` | PLT | L | bool | true | — | — |
| `dms.duplicate.detect_by_hash` | PLT | L | bool | true | — | — |
| `dms.categories.default_set` | BRD→TEN | O | ref | Company / Individual sets (Appendix K) | `ORG_ADMIN`, `IND_OWNER` | N |
| `dms.retention.default_class` | TEN→DEP | G-leg | ref | `CONTRACT_STD` | `ORG_CLO` | Y |
| `dms.retention.contract_min_years` | PLT | G-leg (L floor 7) | int | 7 after expiry [REC; R3 LG-092] | `PLT_LEGAL_REVIEWER` | Y |
| `dms.retention.tax_docs_years` | PLT | G-leg | int | 8 [REC; CGST s.36 VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `dms.retention.individual_default` | TEN | O (↑) | enum keep_until_deleted/years | keep until the user deletes | `IND_OWNER` | N |
| `dms.legal_hold.roles` | TEN | G-elv | menum | `ORG_CLO`, `ORG_ADMIN` | `ORG_OWNER` | Y |
| `dms.bulk_delete.requires_checker` | PLT | L | bool | true (NN-18) | — | — |
| `dms.share.external_link_days` | TEN→USR ↓ | O | int 1–30 | 7 | `ORG_ADMIN`, user | N |
| `dms.share.external_otp_required` | TEN | G-elv | bool | true | `ORG_ADMIN` | Y |
| `dms.share.public_links` | PLT→TEN | G-elv | bool | false; never for confidential classes | `ORG_OWNER` | Y |
| `dms.share.watermark_external` | TEN→USR | O | bool | true | `ORG_ADMIN`, user | N |
| `dms.share.download_default` | TEN→USR | O | bool | false (view-only) | `ORG_ADMIN`, user | N |
| `dms.expiry_reminders.offsets_days` | TEN→USR ↑ | O | list | [90, 30, 7] | `ORG_ADMIN`, user | N |
| `dms.search.index_ocr_text` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `dms.redaction.aadhaar_images_prompt` | PLT | L | bool | true (NN-04) | — | — |
| `dms.nominee.enabled` | TEN | O | bool | true (Personal) | `IND_OWNER` | N |

### R.9.11 `dix` — OCR, type copy, translation (P05)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `dix.ocr.languages` | PLT | G | menum | 22 Eighth-Schedule + 6 UN languages (D-07) | `PLT_SUPER_ADMIN` | N |
| `dix.handwriting.route` | PLT | G-int | enum | Claude vision via Bedrock India (NN-15) | CTO | Y |
| `dix.confidence.review_threshold` | TEN | O | dec 0.5–0.99 | 0.85 | `ORG_ADMIN` | N |
| `dix.typecopy.label` | PLT | L | text | "Typed copy prepared from the original — check against the original" | — | — |
| `dix.translation.machine_label` | PLT | L | text | "Machine translation — not reviewed" (NN-48) | — | — |
| `dix.translation.court_filing_requires_certified` | PLT | L | bool | true (R3 LG-093/094) | — | — |
| `dix.translation.target_default` | TEN→USR | O | enum | en | `ORG_ADMIN`, user | N |
| `dix.aadhaar.mask_derived` | PLT | L | bool | true | — | — |
| `dix.anchors.required` | PLT | L | bool | true (page/region anchors) | — | — |
| `dix.auto_run_on_upload` | TEN→USR | O | enum off/ask/auto | ask | `ORG_ADMIN`, user | N |
| `dix.credits.per_page` | PLN | G-elv | int | [OWNER TO SET] | `PLT_SUPER_ADMIN` | Y |

### R.9.12 `tpl` — templates, clauses, questionnaires (P06)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `tpl.publish.reviewer_of_record` | PLT | L | bool | true (NN-30) | — | — |
| `tpl.publish.requires_checker` | PLT→TEN | G-elv | bool | true | `ORG_CLO` (tenant templates) | Y |
| `tpl.jurisdiction.default_state` | TEN→USR | O | enum State | user's State | user | N |
| `tpl.tenant_templates.max` | PLN | G | int | 0 / 10 / 50 / 500 / unlimited | `PLT_SUPER_ADMIN` | N |
| `tpl.clause_library.tenant_enabled` | PLN→TEN | O | bool | Business+ true | `ORG_ADMIN` | N |
| `tpl.output.languages` | TEN | O | menum | en, hi | `ORG_ADMIN` | N |
| `tpl.questionnaire.save_progress` | TEN→USR | O | bool | true | user | N |
| `tpl.newer_version.prompt` | TEN→USR | O | bool | true | user | N |
| `tpl.ai_suggested_clauses` | TEN→USR | O | bool | true (labelled) | `ORG_ADMIN`, user | N |

### R.9.13 `drf` — AI Drafting Studio (P06)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `drf.template_assembly.free` | PLT | L | bool | true (CH-30) | — | — |
| `drf.ai_custom.label` | PLT | L | text | "AI draft — not reviewed by a professional" (NN-14) | — | — |
| `drf.ai_custom.individual_delivery_mode` | PLT | G-leg | enum labelled_draft/review_required | labelled_draft [VERIFY Anthropic Usage Policy high-risk requirements; switch to review_required if required] | `PLT_LEGAL_REVIEWER` | Y |
| `drf.ai_custom.paid_review_offer` | PLT | L | bool | true | — | — |
| `drf.citations.unresolved_display` | PLT | L | text | "unverified" | — | — |
| (retired `drf.free_plan.clean_downloads_per_month`; duplicate) | — | — | — | Read `drf.template.free_clean_exports_per_month` (second review, G3 R-1) | — | — |
| `drf.default_output_format` | USR | O | enum docx/pdf | docx | user | N |
| `drf.track_changes_default` | TEN→USR | O | bool | true | user | N |
| `drf.vidhi.tone` | TEN→USR | O | enum plain/formal | plain | user | N |
| `drf.vidhi.answer_language` | USR | O | enum (D-07) | UI language | user | N |

### R.9.14 `clm` — contract lifecycle (P07)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `clm.approval.matrix` | ENT→DEP | G-elv | json (value bands, types, approvers) | Pro: 1 approver; Business: value-band matrix | `ORG_ADMIN` → `ORG_OWNER` | Y |
| `clm.approval.board_threshold_inr` | ENT | G-elv | money | none | `ORG_OWNER` | Y |
| `clm.intake.form` | TEN→DEP | O | ref form | platform form | `ORG_ADMIN` | N |
| `clm.renewal.reminder_offsets_days` | TEN→USR ↑ | O | list | [90, 60, 30, 7] | `ORG_ADMIN`, user | N |
| `clm.renewal.auto_item` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `clm.obligation.extraction` | PLN→TEN | O | bool | Business+ true (labelled AI) | `ORG_ADMIN` | N |
| `clm.negotiation.round_versioning` | PLT | L | bool | true (NN-37) | — | — |
| `clm.negotiation.redline_engine` | PLT | L | enum | deterministic (`packages/redline`) | — | — |
| `clm.negotiation.counterparty_sees_only_shared` | PLT | L | bool | true | — | — |
| `clm.counterparty.account_upgrade_offer` | TEN | O | bool | true (no dark patterns, NN-50) | `ORG_ADMIN` | N |
| `clm.status.auto_expire` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `clm.suite.coauthoring` | TEN | O | enum none/m365/google | none | `ORG_ADMIN` | N |
| `clm.agreements.max_active` | PLN | G | int | by plan [OWNER TO SET] | `PLT_SUPER_ADMIN` | N |

### R.9.15 `sgn` — eSign, DSC, eStamp, execution, evidence (P08)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `sgn.eligibility.block_excluded_instruments` | PLT | L | bool | true (NN-07; LG-003) | — | — |
| `sgn.eligibility.rule_set` | PLT | G-leg | ref | `rulepack.IN.sgn.eligibility` | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.stamp_before_sign` | PLT | L | bool | true (NN-08) | — | — |
| `sgn.asp.sublet` | PLT | L | bool | false (NN-06; LG-007) | — | — |
| `sgn.esp.routes` | PLT | G-int | list | primary + secondary aggregator/ESP (D-12) | `PLT_SECURITY_OFFICER` | Y |
| `sgn.esp.second_route_within_days` | PLT | G-leg | int | 30 (API v3.3; LG-008) [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.esp.licence_expiry_block` | PLT | L | bool | true (LG-005) | — | — |
| `sgn.consent.screen_version` | PLT | G-leg | ref | current versioned consent (LG-006) | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.hash.final_pdf_after_stamp` | PLT | L | bool | true | — | — |
| `sgn.methods.allowed` | TEN | G | list (subset of the Appendix F row; tenants remove, never add) | all row-permitted methods except biometric and face (P08) | `ORG_CLO` / `IND_OWNER` | Y (company) |
| `sgn.e_acceptance.label` | PLT | L | text | "Electronic acceptance — not an electronic signature under IT Act s.3A" (LG-001) | — | — |
| `sgn.biometric.assisted_only` | PLT | G | bool | true (LG-013) | `PLT_SUPER_ADMIN` | N |
| `sgn.dsc.class_required` | PLT | L | enum | Class 3 (LG-011) [VERIFY] | — | — |
| `sgn.request.expiry_days` | TEN→USR ↓ | O | int 1–60 | 15 | `ORG_ADMIN`, user | N |
| `sgn.order.default` | TEN→USR | O | enum sequential/parallel | sequential | `ORG_ADMIN`, user | N |
| `sgn.reminders.offsets_days` | TEN→USR | O (≤ `ntf.counterparty.max_reminders`) | list | [2, 5, 10] | `ORG_ADMIN`, user | N |
| `sgn.signer.message_while_signing` | TEN | O | bool | true (R-077) | `ORG_ADMIN` | N |
| `sgn.witness.rule_set` | PLT | G-leg | ref | `rulepack.IN.sgn.formalities` | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.evidence.retention_years_after_closure` | PLT ↑ | G-leg (L floor 7) | int | 7 (LG-008, LG-092) | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.evidence.s63_certificate_auto` | PLT | L | bool | true (NN-10) | — | — |
| `sgn.estamp.channels` | PLT | G-int | json per State | `rulepack.IN-<ST>.estamp.channels` | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.estamp.states_enabled` | PLT | G-leg | menum State | only VERIFIED States | `PLT_LEGAL_REVIEWER` | Y |
| `sgn.estamp.duty_at_actuals` | PLT | L | bool | true | — | — |
| `sgn.estamp.facilitation_fee_inr` | PLT | G-elv | money | ₹49 [OWNER TO SET] | `PLT_SUPER_ADMIN` | Y |
| `sgn.estamp.uin_verification` | PLT | L | bool | true | — | — |
| `sgn.physical_stamp.courier_enabled` | PLT→TEN | G | bool | false until State routes verified | `PLT_SUPER_ADMIN` | Y |
| `sgn.credits.included_per_month` | PLN | G-elv | int | 0 / 2 / 10 / 50 / contracted | `PLT_SUPER_ADMIN` | Y |
| `sgn.kill.<adapter>` | PLT | G | bool | off | `PLT_SECURITY_OFFICER` | Release Y |

### R.9.16 `ai` — Vidhi runtime, gateway, guardrails (P09)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `ai.vidhi.enabled` | TEN→USR | O | bool | true | `ORG_ADMIN`, user | N |
| `ai.training_on_customer_data` | PLT | L | bool | false (NN-15) | — | — |
| `ai.route.confidential_classes` | PLT | L | enum | Bedrock India (zero retention) | — | — |
| `ai.route.public_content` | PLT | G-int | enum bedrock_india/anthropic_api | anthropic_api for public/non-personal only | CTO | Y |
| `ai.pii_scrubber` | PLT | L | bool | true | — | — |
| `ai.retrieval.permission_scoped` | PLT | L | bool | true | — | — |
| `ai.output.label_and_sources` | PLT | L | bool | true (NN-14) | — | — |
| `ai.citations.resolve_or_mark_unverified` | PLT | L | bool | true | — | — |
| `ai.disclosure.ai_use_notice` | PLT | L | bool | true [VERIFY Usage Policy text] | — | — |
| `ai.credits.monthly` | PLN | G-elv | int | 30 / 300 / 1,500 / 6,000 / 25,000+ | `PLT_SUPER_ADMIN` | Y |
| `ai.credits.overage_mode` | TEN | O | enum stop/ask/auto_pack | ask (no auto top-up) | `ORG_ADMIN` | N |
| `ai.languages` | BRD→USR | O | menum (D-07) | UI language | user | N |
| `ai.prompt_logs.retention_days` | PLT | G-prv | int 0–90 | 30 (scrubbed) | `PLT_DPO` | Y |
| `ai.suggestions.proactive` | USR | O | bool | true | user | N |
| `ai.sgi.label_audio_video` | PLT | L | bool | true (IT Rules 2026 SGI; LG-078) | — | — |
| `ai.fabricate_official_records` | PLT | L | bool | false (LG-078) | — | — |
| `ai.kill.vidhi` | PLT/TEN | G | bool | off | `PLT_SECURITY_OFFICER`; `ORG_ADMIN` | Release Y |

### R.9.16A `vidhi` and IPB `ai.*` keys — shared kernel (P09 §4N; IPB-03 §03.5) *(v1.1)*

The kernel's keys are registered here with LawDocs tiers. `vidhi.*` is a shared-package prefix (IPB-03), accepted alongside the module prefixes of conventions §4 (recorded in OI-R-08's normalisation list as a sanctioned exception).

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `vidhi.brand.display_name` | BRD | G | text | "Vidhi" (override only on white-label plans) | brand admin | N |
| `vidhi.persona.version` | PLT | G | text | `vidhi.persona@1` | `PLT_CONTENT_EDITOR` | Y |
| `vidhi.surfaces.<surface>.enabled` | TEN | O | bool | panel/palette/inline/chat on; voice/whatsapp/email off | `ORG_ADMIN` | N |
| `vidhi.skill.<key>.enabled` | TEN | O | bool | per LD floor (P09 FR-P09-64) | `ORG_ADMIN` | N |
| `vidhi.skill.<key>.autonomy_level` | TEN | G-elv | enum L0–L4 | L1 | `ORG_OWNER` (promotion flow) | Y (L3/L4) |
| `vidhi.autonomy.promotion_min_runs` | PLT | G-elv ↑ | int | 200 (IPB floor 50) | `PLT_SECURITY_OFFICER` | Y |
| `vidhi.autonomy.l3_delay_min` | TEN | O ↑ | int | 15 | `ORG_OWNER` | N |
| `vidhi.sched.enabled` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `vidhi.sched.max_skips` | PLT | G | int | 3 | `PLT_RELEASE_MANAGER` | N |
| `vidhi.sched.templates.<key>.enabled` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `vidhi.a2a.enabled` | PLT | G-int | bool | false (alias `int.a2a.enabled`) | `PLT_SUPER_ADMIN` | Y |
| `vidhi.mcp.client_allowlist` | PLT→TEN ⊂ | G-int | json | [] | `PLT_SECURITY_OFFICER`; `ORG_OWNER` (subset) | Y |
| `vidhi.connectors.calendar.enabled` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `vidhi.notebooks.enabled` | PLN→TEN | O | bool | true | `ORG_ADMIN` | N |
| `vidhi.notebooks.audio_overview` | PLN | G | bool | false | `PLT_SUPER_ADMIN` | N |
| `vidhi.digest.hour_local` | USR | O | int 0–23 | 8 | user | N |
| `vidhi.qa.sample_rate` | PLT | G | pct | 2 % (10 % new skills 30 days) | `PLT_SECURITY_OFFICER` | N |
| `vidhi.a11y.plain_language` | USR | O | bool | false | user | N |
| `vidhi.feedback.enabled` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `ai.byok.enabled` | PLN | G-elv | bool | false | `PLT_SUPER_ADMIN` | Y |
| `ai.byok.adapter.<key>` | TEN | G-elv | ref (secret) | null | `ORG_OWNER` | Y |
| `ai.kill.all` · `ai.kill.adapter.<key>` · `ai.kill.feature.<key>` · `ai.kill.tenant` | PLT / TEN | G-elv | bool | false | `PLT_SECURITY_OFFICER`; `ORG_OWNER` (tenant) | Activate N / Release Y |
| `ai.mcp.server_enabled` | TEN | G-int | bool | false | `ORG_OWNER` | Y |
| `ai.a2a.agent_card` | PLT | G-int | bool | false | `PLT_SUPER_ADMIN` | Y |
| `ai.image_gen.provider` | PLT | G | enum | unset (feature hidden) | `PLT_CONTENT_EDITOR` (`PLT_DPO` veto) | Y |
| `ai.image_gen.label_style` | PLT | L | enum | `visible_plus_sidecar` | — | — |
| `ai.image_gen.allowed_apps` | PLT | L | menum | `[public, console]` | — | — |
| `ai.routing.policy.<feature>.<band>` | PLT | G-elv | json | seeded from P09 FR-P09-02 | `PLT_SECURITY_OFFICER` | Y |
| `ai.cost.tenant_daily_cap` | PLN→TEN ↓ | O | money | plan-defined | `ORG_OWNER` | N |
| `ai.obs.capture_content` | PLT | G-prv | bool | false | `PLT_SECURITY_OFFICER` | Y |
| `ai.obs.run_retention_days` | PLT | G-prv | int | 180 | `PLT_DPO` | Y |

### R.9.17 `agt` — agent workforce (P09)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `agt.maker_only` | PLT | L | bool | true (NN-43) | — | — |
| `agt.irreversible_actions_need_human` | PLT | L | bool | true (NN-13) | — | — |
| `agt.sponsor.required` | PLT | L | bool | true | — | — |
| `agt.autonomy.platform_ceiling.<agent>` | PLT | G | enum L0–L4 | L2 (Appendix H) | release + `PLT_SECURITY_OFFICER` | Y |
| `agt.autonomy.tenant_ceiling` | TEN | G-elv | enum ≤ platform | L1 | `ORG_ADMIN` → `ORG_OWNER` | Y |
| `agt.autonomy.agent.<agent>` | TEN→USR ↓ | G-elv (raise) / O (lower) | enum | inherit | sponsor + `ORG_ADMIN` | Y (raise) |
| `agt.seats.included` | PLN | G-elv | int | 0 / 0 / 1 / 3 / band | `PLT_SUPER_ADMIN` | Y |
| `agt.budget.monthly_credits.<agent>` | TEN | O | int | 400 per seat | `ORG_ADMIN` | N |
| `agt.tools.allowlist.<agent>` | TEN ⊂ | G-elv | menum | Appendix H defaults | `ORG_ADMIN` | Y |
| `agt.mission.max_hours` | PLT→TEN ↓ | G | int 1–72 | 24 | `ORG_ADMIN` | N |
| `agt.sealed_contexts.autonomy` | PLT | L | enum | L0 for restricted classes | — | — |
| `agt.kill.<agent>` | PLT/TEN | G | bool | off | `PLT_SECURITY_OFFICER`; `ORG_ADMIN` | Release Y |

### R.9.18 `pld` — pleadings, notices, court drafting (P10)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `pld.court_format.rule_set` | PLT | G-leg | ref | `rulepack.IN.lit.court_formats` [VERIFY per court] | `PLT_LEGAL_REVIEWER` | Y |
| `pld.page.size` | TEN→USR | O | enum A4/legal | A4 | user | N |
| `pld.typecopy.annex_label` | PLT | L | text | "Typed copy of Annexure … (original attached)" (CH-28) | — | — |
| `pld.translation.filing_requires_certified` | PLT | L | bool | true (NN-48) | — | — |
| `pld.affidavit.notary_pack` | PLT | L | bool | true (no eSign for affidavits) | — | — |
| `pld.notice.dispatch_modes` | TEN | O | menum email/registered_post_checklist/whatsapp | email, registered post checklist | `ORG_ADMIN` | N |
| `pld.s63_certificate.offer_on_annex` | PLT | L | bool | true (NN-10) | — | — |
| `pld.ai_draft.professional_review_offer` | PLT | L | bool | true | — | — |

### R.9.19 `lit` — litigation and matters (P11)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `lit.matters.max` | PLN | G-elv | int | 1 / 5 / 50 / 300 / band | `PLT_SUPER_ADMIN` | Y |
| `lit.court_data.adapters` | PLT | G-int | list | two licensed aggregators (R6) | `PLT_SECURITY_OFFICER` | Y |
| `lit.court_data.realtime_claim` | PLT | L | bool | false (NN-20) | — | — |
| `lit.court_data.portal_scraping` | PLT | L | bool | false (NN-05) | — | — |
| `lit.court_data.staleness_label_hours` | PLT→TEN ↓ | G | int 1–72 | 24 | `ORG_ADMIN` | N |
| `lit.court_data.manual_refresh_per_day` | PLN | G | int | 1 / 5 / 20 / 100 / band | `PLT_SUPER_ADMIN` | N |
| `lit.hearing.reminder_offsets_days` | TEN→USR ↑ | O | list | [7, 2, 1] | `ORG_ADMIN`, user | N |
| `lit.cause_list.alert_time` | USR | O | time | 07:00 | user | N |
| `lit.limitation.advisory_label` | PLT | L | text | "Advisory — confirm with counsel" | — | — |
| `lit.order.auto_ocr` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `lit.counsel_panel.enabled` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `lit.matter.default_team_roles` | TEN→DEP | O | menum | lead, associate, client contact | `ORG_ADMIN` | N |

### R.9.20 `ipm` — IP and trademarks (P12)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `ipm.marks.max` | PLN | G-elv | int | 1 / 3 / 10 / 50 / unlimited | `PLT_SUPER_ADMIN` | Y |
| `ipm.data.sources` | PLT | G-int | list | WIPO Global Brand Database + licensed partner [VERIFY] | `PLT_SECURITY_OFFICER` | Y |
| `ipm.ip_india_scraping` | PLT | L | bool | false (CH-27) | — | — |
| `ipm.timelines.rule_set` | PLT | G-leg | ref | `rulepack.IN.ipm.tm_timelines` [VERIFY sections] | `PLT_LEGAL_REVIEWER` | Y |
| `ipm.renewal.reminder_offsets_months` | TEN→USR ↑ | O | list | [12, 6, 3, 1] | `ORG_ADMIN`, user | N |
| `ipm.journal_watch.enabled` | PLN→TEN | O | bool | Pro+ add-on | `ORG_ADMIN` | N |
| `ipm.watch.similarity_threshold` | TEN | O | dec 0.5–0.95 | 0.75 | `ORG_ADMIN` | N |
| `ipm.status.manual_refresh_label` | PLT | L | bool | true (shows source and fetched-at) | — | — |

### R.9.21 `gov` — governance kernel mount (P13)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| (retired `gov.mode`; X-11) | — | — | — | Read `int.eco.ldc.sor_mode.governance` (§R.9.33; P19) | — | — |
| `gov.board.min_meetings_per_year` | PLT | G-leg | int | 4 (Companies Act s.173(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.board.max_gap_days` | PLT | G-leg | int | 120 (s.173(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.board.notice_min_days` | PLT | G-leg | int | 7 (s.173(3)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.minutes.circulation_days` | PLT | G-leg | int | 15 (SS-1) [VERIFY para] | `PLT_LEGAL_REVIEWER` | Y |
| `gov.minutes.entry_days` | PLT | G-leg | int | 30 (SS-1) [VERIFY para] | `PLT_LEGAL_REVIEWER` | Y |
| `gov.agm.deadline_months` | PLT | G-leg | int | 6 after FY end (s.96(1)) | `PLT_LEGAL_REVIEWER` | Y |
| `gov.resolution.numbering` | ENT | O | ref pattern | `{ENTITY}/BR/{FY}/{SEQ:3}` | `ORG_ADMIN` | N |
| `gov.board_portal.director_access` | ENT | O | enum app/email_pack | app | `ORG_ADMIN` | N |
| `gov.registers.enabled` | ENT | O | menum | members, directors and KMP, charges | `ORG_ADMIN` | N |

### R.9.22 `hr` — HRMS kernel mount for client companies (P13)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| (retired `hr.mode`; X-11) | — | — | — | Read `int.eco.ldc.sor_mode.hrms` (§R.9.33; P19) | — | — |
| `hr.labour_rulepack.version` | PLT | G-leg | ref (pinned) | latest signed `infrabyx-labour-rulepack` | `PLT_LEGAL_REVIEWER` | Y |
| `hr.monitoring.keylogging` | PLT | L | bool | false (NN-33) | — | — |
| `hr.monitoring.screenshots_webcam` | PLT | L | bool | false (NN-33) | — | — |
| `hr.attendance.sessions_for_attendance_only` | PLT | L | bool | true (CH-32) | — | — |
| `hr.employees.max` | PLN | G-elv | int | add-on per employee | `PLT_SUPER_ADMIN` | Y |
| `hr.payroll.enabled` | PLN→ENT | G | bool | false (add-on) | `ORG_ADMIN` | Y |
| `hr.policy_ack.reminder_days` | ENT | O | int 1–30 | 7 | `ORG_ADMIN` | N |
| `hr.duties.assignment_notice` | ENT | O | bool | true | `ORG_ADMIN` | N |
| `hr.export.restricted_archive` | PLT | L | bool | true (P20 FR-P20-08) | — | — |

### R.9.23 `lgo` — Company Legal Department OS (P13)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `lgo.intake.enabled` | TEN | O | bool | true (Business+) | `ORG_ADMIN` | N |
| `lgo.intake.channels` | TEN | O | menum web/email/teams/gchat | web, email | `ORG_ADMIN` | N |
| `lgo.intake.request_types` | TEN→DEP | O | list | contract review, new agreement, notice received, dispute, IP, general advice | `ORG_CLO` | N |
| `lgo.triage.sla_hours` | TEN→DEP | O | int 1–120 | 24 | `ORG_CLO` | N |
| `lgo.assignment.policy` | TEN→DEP | O | enum manual/round_robin/least_loaded | round_robin | `ORG_CLO` | N |
| `lgo.spend.tracking` | TEN | O | bool | true | `ORG_CLO` | N |
| `lgo.spend.approval_threshold_inr` | ENT | G-elv | money | ₹50,000 | `ORG_OWNER` | Y |
| `lgo.counsel_panel.enabled` | TEN | O | bool | false | `ORG_CLO` | N |
| `lgo.calendar.include_obligations` | TEN | O | bool | true | `ORG_CLO` | N |
| `lgo.clo_dashboard.mandatory_widgets` | BRD | L | list | legal deadlines, overdue items | — | — |

### R.9.24 `bsv` — Business Services (P14)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `bsv.catalogue.visible` | BRD→TEN | G | menum | LawDocs service catalogue | `PLT_SUPER_ADMIN` | N |
| `bsv.fees.government_separate` | PLT | L | bool | true (NN-22) | — | — |
| `bsv.startup_desk.enabled` | TEN | O | bool | true (Pro) | `ORG_ADMIN` | N |
| `bsv.order.status_channel` | USR | O | enum in_app/email/whatsapp | in_app + email | user | N |
| `bsv.checklists.rule_set` | PLT | G-leg | ref | per service | `PLT_LEGAL_REVIEWER` | Y |
| `bsv.legal_officer_retainer.enabled` | BRD | G-elv | bool | true | `PLT_SUPER_ADMIN` | Y |

### R.9.25 `tax` — tax workspace (P14)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `tax.flag.module` | PLT | G | bool | false until Wave 3 verification | `PLT_RELEASE_MANAGER` | Y |
| `tax.filing.route` | PLT | G-int | enum eri/gsp/none | none until ERI/GSP route verified (CH-10) | `PLT_SECURITY_OFFICER` | Y |
| `tax.client_portal_passwords.stored` | PLT | L | bool | false (only `cvl` with NN-16) | — | — |
| `tax.verification.by_taxpayer` | PLT | L | bool | true (EVC/DSC by the taxpayer) | — | — |
| `tax.calendar.rule_set` | PLT | G-leg | ref | `rulepack.IN.tax.calendars` [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `tax.reminder_offsets_days` | TEN→USR ↑ | O | list | [15, 7, 2] | user | N |
| `tax.year_label` | TEN | O | enum AY/FY/TY | per Income-tax Act 2025 terminology [VERIFY] | `ORG_ADMIN` | N |
| `tax.practitioner_roles` | TEN | G-elv | menum | `PRO_CA`, `PRO_TAX_PRACTITIONER` | `ORG_ADMIN` | Y |

### R.9.26 `chp` — Consumer Help brand (P15)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `chp.brand.separate_entity` | PLT | L | bool | true (D-06) | — | — |
| `chp.ethical_wall.enabled` | PLT | L | bool | true (NN-23) | — | — |
| `chp.conflict_check.before_acceptance` | PLT | L | bool | true | — | — |
| `chp.outcome_promises` | PLT | L | bool | false | — | — |
| `chp.collect_fines_or_dues` | PLT | L | bool | false (CH-22) | — | — |
| `chp.challan.payment_deep_link_only` | PLT | L | bool | true | — | — |
| `chp.verticals.enabled` | BRD | G | menum loan/insurance/credit_report/challan/vehicle | all OFF until counsel sign-off per vertical | `PLT_SUPER_ADMIN` | Y |
| `chp.rbios.rule_set` | PLT | G-leg | ref | `rulepack.IN.chp.rbios_2026` [VERIFY clauses] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.rbios.re_wait_days` | PLT | G-leg | int | 30 [VERIFY clause] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.rbios.filing_window_days` | PLT | G-leg | int | 90 after reply/expiry [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.rbios.advocate_as_authorised_rep` | PLT | L | bool | false (Cl. 10(1)(b) [VERIFY]) | — | — |
| `chp.insurance_ombudsman.cap_inr` | PLT | G-leg | money | ₹50,00,000 (R2) [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.insurance_ombudsman.window_months` | PLT | G-leg | int | 12 (R2) [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.success_fee.enabled` | PLT | G-elv | bool | false; locked until counsel opinion + checker (CH-31) | `PLT_SUPER_ADMIN` | Y |
| `chp.success_fee.cap_pct` | PLT | G-elv | pct | [COUNSEL] | `PLT_SUPER_ADMIN` | Y |
| `chp.case.status_update_days` | BRD→USR | O | int 3–30 | 7 | `OPS_DELIVERY_LEAD`, user | N |
| `chp.recovery_conduct_rules_effective` | PLT | G-leg | date | 2027-01-01 [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `chp.kill.<vertical>` | PLT/BRD | G | bool | off | `PLT_SECURITY_OFFICER` | Release Y |

### R.9.27 `mkp` — marketplace and professional registry (P16)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `mkp.browse_without_login` | PLT | L | bool | true (D-11) | — | — |
| `mkp.advocate.commission` | PLT | L | bool | false (NN-21) | — | — |
| `mkp.advocate.listing_fee` | PLT | L | bool | false | — | — |
| `mkp.advocate.paid_ranking` | PLT | L | bool | false | — | — |
| `mkp.advocate.ratings_testimonials` | PLT | L | bool | false (Madras HC 2024; NN-49) | — | — |
| `mkp.advocate.profile_fields` | PLT | L | ref | BCI Rule 36 permitted fields only | — | — |
| `mkp.directory.rule36_enabled` | PLT | G-leg | bool | false | `PLT_LEGAL_REVIEWER` | Y |
| `mkp.ordering` | PLT | L | enum | neutral (alphabetical/random/proximity by user choice) | — | — |
| `mkp.fees.buyer_platform_fee_inr` | PLT | G-elv | money | ₹99 within ₹49–₹199 [OWNER TO SET] | `PLT_SUPER_ADMIN` | Y |
| `mkp.ca_cs.practising_listing` | PLT | G-elv | bool | false; locked until ICAI/ICSI-compliant structure + counsel (CH-09) | `PLT_SUPER_ADMIN` | Y |
| `mkp.ca_cs.percentage_model` | PLT | G-elv | bool | false; locked (NN-21) | `PLT_SUPER_ADMIN` | Y |
| `mkp.payouts.route_only` | PLT | L | bool | true (Razorpay Route; NN-22) | — | — |
| `mkp.pooling_third_party_money` | PLT | L | bool | false | — | — |
| `mkp.reviews.verified_purchase_only` | PLT | L | bool | true (NN-49) | — | — |
| `mkp.reviews.photos_default` | PLT→BRD | O | bool | false | `PLT_CONTENT_EDITOR` | N |
| `mkp.retainer.sla_esign_required` | PLT | L | bool | true (R-039) | — | — |
| `mkp.engagement.direct_terms_with_professional` | PLT | L | bool | true (NN-41) | — | — |

### R.9.28 `aca` — FinLegal Academy (P16)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `aca.catalogue_feed.enabled` | PLT | G-int | bool | true | `PLT_SUPER_ADMIN` | N |
| `aca.feed.refresh_hours` | PLT | O | int 1–72 | 24 | `PLT_CONTENT_EDITOR` | N |
| `aca.sso_deep_link` | PLT | G-int | bool | false until Graphy SSO verified [VERIFY] | `PLT_SECURITY_OFFICER` | Y |
| `aca.copy_paid_content` | PLT | L | bool | false (D-16) | — | — |
| `aca.listing_requires_login` | PLT | L | bool | false | — | — |

### R.9.29 `bil` — plans, billing UI, entitlements mirror, revenue streams (P17)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `bil.engine` | PLT | L | enum | OH8 via `BILLING_PORT` (D-02) | — | — |
| `bil.card_data_stored` | PLT | L | bool | false (NN-22; SAQ A) | — | — |
| `bil.price.plans` | PLT | G-elv | json | R6 seeds [OWNER TO SET] | `PLT_SUPER_ADMIN` + OH8 finance | Y |
| `bil.price.monthly_uplift_pct` | PLT | G-elv | pct | 20 [OWNER TO SET] | `PLT_SUPER_ADMIN` | Y |
| `bil.display.total_incl_gst_before_payment` | PLT | L | bool | true (NN-22) | — | — |
| `bil.display.statutory_fees_separate` | PLT | L | bool | true | — | — |
| `bil.renewal.terms_before_payment` | PLT | L | bool | true (NN-50) | — | — |
| `bil.cancellation.self_serve_parity` | PLT | L | bool | true (NN-50) | — | — |
| `bil.renewal.reminder_days` | PLT→TEN ↑ | G | int ≥ 3 | 7 | `PLT_SUPER_ADMIN` | N |
| `bil.trial.days` | PLT | G-elv | int | 14 | `PLT_SUPER_ADMIN` | Y |
| `bil.credits.auto_topup` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `bil.refund.policy` | PLT | G-elv | ref | published refund policy | `PLT_SUPER_ADMIN` | Y |
| `bil.streams.<stream>.enabled` | PLT/BRD | G-elv | bool | per RS-LD registry (R6 §R6.5) | `PLT_SUPER_ADMIN` | Y |
| `bil.streams.ads.enabled` | PLT | G-elv | bool | false (D-13, NN-35) | `PLT_SUPER_ADMIN` | Y |
| `bil.dunning.blocks_export_or_read` | PLT | L | bool | false (NN-11) | — | — |
| `bil.entitlement.offline_grace_days` | PLT | G | int | 30 (Spec §6.27) | CTO | Y |
| `bil.invoices.email_to` | TEN | O | list | billing contact | `ORG_ADMIN` | N |
| `bil.kill.<stream>` | PLT | G | bool | off | `PLT_SUPER_ADMIN` | Release Y |

### R.9.30 `sav` — savings and value ledger (P17)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `sav.formula_inputs_shown` | PLT | L | bool | true (NN-36) | — | — |
| `sav.evidence_class_label` | PLT | L | bool | true (MEASURED/ESTIMATED/MODELLED) | — | — |
| `sav.penalty_avoided.requires_evidence` | PLT | L | bool | true | — | — |
| `sav.hourly_rate_inr` | TEN→DEP | O | money | ₹1,500 [OWNER TO SET] | `ORG_ADMIN` | N |
| `sav.benchmark_prices.source` | PLT | G | ref | R6 benchmarks with dates | `PLT_CONTENT_EDITOR` | Y |
| `sav.dashboard.enabled` | TEN→USR | O | bool | true | `ORG_ADMIN`, user | N |

### R.9.31 `sdc` — Delivery Console and client sections (P18)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `sdc.grant.client_approval_required` | PLT | L | bool | true (NN-17) | — | — |
| `sdc.grant.max_days` | TEN ↓ | G-elv | int 1–365 | 365 (retainer term) | `ORG_OWNER` | Y |
| `sdc.grant.scopes_default` | TEN | G-elv | menum | read, propose, maker | `ORG_ADMIN` | Y |
| `sdc.access_log.client_visible` | PLT | L | bool | true | — | — |
| `sdc.breakglass.client_report_hours` | PLT | L | int | 24 | — | — |
| `sdc.rm.as_checker` | PLT | L | bool | false (R-064) | — | — |
| `sdc.deliverable.client_acceptance` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `sdc.common_drive.types` | TEN | O | menum sharepoint/onedrive/gdrive | per suite | `ORG_ADMIN` | N |
| `sdc.client_section.billing_visible` | TEN | O | bool | true | `ORG_ADMIN` | N |
| `sdc.sla.first_response_hours` | TEN | G-elv | int | per eSigned retainer SLA | `ORG_OWNER` + `OPS_DELIVERY_LEAD` | Y |
| `sdc.breakglass.enabled` | PLT | G | bool | true — off = no break-glass session can start (NN-39; P18 §9 kill-switch list) | `PLT_SECURITY_OFFICER` (release by a second person) | Release Y |
| `sdc.email.bridge.global_enabled` | PLT | G | bool | true — platform-wide stop for the email bridge; tenant opt-in stays `sdc.email.bridge_enabled` (default false) (NN-39; P18 §9) | `PLT_SECURITY_OFFICER` (release by a second person) | Release Y |
| `sdc.delivery.agent_runs.global_enabled` | PLT | G | bool | true — platform-wide stop for RM-started agent runs; tenant opt-in stays `sdc.delivery.agent_runs.enabled` (default false) (NN-39, NN-43; P18 §9) | `PLT_SECURITY_OFFICER` (release by a second person) | Release Y |

The four P18 kill switches above (`sdc.breakglass.enabled`, `sdc.email.bridge.global_enabled`, `sdc.delivery.agent_runs.global_enabled`, `cvl.reveal.enabled` in §R.9.32) are named in P18 §9 without table values; tier, type, default and changed-by were set at registry review G4 consistent with @P18-AT-29 and the platform kill-switch rows of this section. Their names do not follow the `<module>.kill.<target>` convention (§R.1); they are registered as P18 named them and are `cfg.kill_switches` rows of scope `FEATURE` (OI-R-08). `sdc.grant.max_days` (tenant cap, lower-only) is bounded above by the P18 platform caps `sdc.grants.max_months.retainer` (12) and `sdc.grants.max_months.implementation` (3) (§R.14).

### R.9.32 `cvl` — client-owned credential vault (P18)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `cvl.enabled` | TEN | G-elv | bool | false (D-03, CH-07) | `ORG_OWNER`/`ORG_ADMIN` (maker) + a second client admin (checker; `LD-CVL-002`; P18 §9) | Y |
| `cvl.reveal.enabled` | PLT | G | bool | true — platform-wide emergency stop; off = every pending and new reveal fails with `LD-CVL-010` (NN-39; P18 §9 kill-switch list, @P18-AT-29) | `PLT_SECURITY_OFFICER` (release by a second person, `cfg.kill_switch.release_second_person`) | Release Y |
| `cvl.encryption.client_scoped_keys` | PLT | L | bool | true | — | — |
| `cvl.masked_by_default` | PLT | L | bool | true | — | — |
| `cvl.store_otp_pin_recovery_codes` | PLT | L | bool | false | — | — |
| `cvl.delegation_first_prompt` | PLT | L | bool | true | — | — |
| `cvl.reveal.reason_required` | PLT | L | bool | true | — | — |
| `cvl.reveal.client_approval` | — | — | — | **Retired at registry review G4** — `alias_of` `cvl.per_reveal_approval.default` (P18 §9: TEN, default true for client-only types, false otherwise; `ORG_ADMIN`; MC Y) | — | — |
| `cvl.reveal.max_minutes` | — | — | — | **Retired at registry review G4** — `alias_of` `cvl.reveal_seconds` (P18 §9: PLT, int 10–60 s, default 30; `PLT_SECURITY_OFFICER`; MC Y; Appendix A §A.55 uses it) | — | — |
| `cvl.rotation.reminder_days` | TEN | O | int 30–365 | 90 | `ORG_ADMIN` | N |
| `cvl.access_log.client_visible` | PLT | L | bool | true | — | — |
| `cvl.export.secrets` | PLT | L | bool | false (metadata only) | — | — |

### R.9.32A `wks` — workspace-suite provider switches (P18; `WORKSPACE_PORT`)

`wks` is not a conventions §4 module code; P18 §9 registers these keys under it for the suite adapters reached through P19 `WORKSPACE_PORT` (FR-P18-46, FR-P18-84). Registered as named by the owner phase (registry review G4); normalisation to a standard module prefix is OI-R-08. `wks.<provider>.enabled` doubles as the provider kill switch (P18 §9 kill-switch list; NN-39).

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `wks.m365.enabled` | PLT | G-int | bool | true | `PLT_SUPER_ADMIN` | Y |
| `wks.google.enabled` | PLT | G-int | bool | false | `PLT_SUPER_ADMIN` | Y |
| `wks.residency.allow_regulated_on_google` | PLT | L | bool | false | — | — |

### R.9.33 `int` — integration gateway and ecosystem (P19)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `int.ecosystem.consentref_or_legalbasis` | PLT | L | bool | true (NN-24) | — | — |
| `int.ecosystem.ops_hub_aggregates_only` | PLT | L | bool | true (NN-19) | — | — |
| `int.ecosystem.links` | TEN | G-elv | menum LDC/EQ/FX/UD | none | `ORG_OWNER` | Y |
| `int.ecosystem.esign_sublet` | PLT | L | bool | false (NN-06) | — | — |
| `int.suite.provider` | TEN | O | enum none/m365/google | none | `ORG_ADMIN` | N |
| `int.webhooks.enabled` | PLN→TEN | O | bool | Pro+ | `ORG_ADMIN` | N |
| `int.webhooks.signature` | PLT | L | enum | HMAC-SHA256 + timestamp | — | — |
| `int.api.rate_limit_per_min` | PLN | G | int | 60 / 300 / 1,200 / band | `PLT_SUPER_ADMIN` | N |
| `int.mcp.server_enabled` | TEN | G-elv | bool | false | `ORG_ADMIN` | Y |
| `int.mcp.external_clients_allowlist` | TEN | G-elv | list | none | `ORG_ADMIN` | Y |
| `int.connectors.certification_required` | PLT | L | bool | true (Spec §14.3) | — | — |
| `int.kill.<adapter>` | PLT/TEN | G | bool | off (not engaged); court and trade-mark adapters additionally start disabled until certified or terms cleared (P11 §9, P12 §9) | `PLT_SUPER_ADMIN` engages; re-enable needs `PLT_SECURITY_OFFICER` as checker (FR-P19-81); `ORG_ADMIN` may engage for the tenant's own connectors with no checker | Release Y (NN-39) |
| `int.eco.ldc.sor_mode.governance` | ENT (defaults from TEN) | G-int | enum `LOCAL`/`LDC` | `LOCAL`; set only by the P19 kernel SoR switch (Appendix A §A.48; D-10, NN-47; replaces `gov.mode`, X-11) | `ORG_ADMIN` (maker), `ORG_OWNER` (checker) | Y |
| `int.eco.ldc.sor_mode.hrms` | ENT (defaults from TEN) | G-int | enum `LOCAL`/`LDC` | `LOCAL`; set only by the P19 kernel SoR switch (replaces `hr.mode`, X-11) | `ORG_ADMIN` (maker), `ORG_OWNER` (checker) | Y |

### R.9.34 `xpt` — export, import, portability, BYO storage (P20)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `xpt.export.never_blocked_by_billing` | PLT | L | bool | true | — | — |
| `xpt.export.tenant_full_requires_checker` | PLT | L | bool | true (companies; NN-18) | — | — |
| (retired `xpt.export.small_company_cooling_minutes`) | — | — | — | Read `wf.mc.solo_owner.cooling_off_hours` (P02 governs; G3 R-2) | — | — |
| `xpt.export.view_scope_cap` | TEN | O | int | 10,000 records | `ORG_ADMIN` | N |
| `xpt.download.link_validity_days` | TEN ↓ | O | int 1–30 | 7 | `ORG_ADMIN`, `IND_OWNER` | N |
| `xpt.download.part_size_gb` | TEN | O | int 1–16 | 4 | `ORG_ADMIN` | N |
| `xpt.folder.year_label` | TEN | O | enum FY_LONG/FY_SHORT/CY | follows `dms.views.year_basis` (P04): FY_LONG for INDIAN_FY, CY for CALENDAR | `ORG_ADMIN`, `IND_OWNER` | N |
| `xpt.folder.entity_level` | TEN | O | enum auto/always/never | auto | `ORG_ADMIN` | N |
| `xpt.folder.department_level` | TEN | O | bool | true (agreements) | `ORG_ADMIN` | N |
| `xpt.folder.name_mode` | TEN | O | enum historical/current | historical | `ORG_ADMIN` | N |
| `xpt.folder.path_script` | TEN | O | enum latin/original | latin | `ORG_ADMIN` | N |
| `xpt.folder.individual_agreements_mode` | TEN | O | enum by_life_area/all_in_08 | by_life_area | `IND_OWNER` | N |
| `xpt.naming.root_owner_label` | TEN | O | enum display_name/account_ref | display_name (Individual); legal name (Company) | `IND_OWNER`, `ORG_ADMIN` | N |
| `xpt.folder.max_path_chars` | PLT | L | int | 240 | — | — |
| `xpt.naming.person_mode` | BRD→TEN | G-prv | enum full_name/masked_name/ids_only | Individual full_name; Company/Professional masked_name; CH ids_only (L) | `ORG_OWNER` | Y |
| `xpt.readme.languages` | TEN | O | menum | [en] | `ORG_ADMIN` | N |
| `xpt.restricted.second_approver` | PLT | L | bool | true | — | — |
| `xpt.targets.regulated_classes_india_only` | PLT | L | bool | true | — | — |
| `xpt.targets.connect_requires_checker` | TEN | G-elv | bool | true for regulated classes | `ORG_OWNER` | Y |
| `xpt.mirror.max_lag_minutes` | PLN→TEN ↑ | O | int 5–1440 | 15 | `ORG_ADMIN` | N |
| `xpt.mirror.propagate_deletions` | TEN | G-elv | bool | false | `ORG_ADMIN` | Y |
| `xpt.mirror.latest_copy_folder` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `xpt.import.max_zip_gb` | PLN | G | int | 2 (Free) … 20 (Business+) | `PLT_SUPER_ADMIN` | N |
| `xpt.import.confidence_auto` | TEN | O | dec | 0.85 | `ORG_ADMIN` | N |
| `xpt.import.confidence_confirm` | TEN | O | dec | 0.50 | `ORG_ADMIN` | N |
| `xpt.import.undo_window_days` | TEN | O | int 1–30 | 7 | `ORG_ADMIN` | N |
| `xpt.import.never_overwrite` | PLT | L | bool | true | — | — |
| `xpt.flag.ai_import_classification` | PLT→TEN | G | bool | false (W1) / true (W2) | `PLT_RELEASE_MANAGER`; tenant may switch off | N |
| `xpt.restore_test.frequency` | TEN | O | enum monthly/quarterly/half_yearly/annual | quarterly | `ORG_ADMIN` | N |
| `xpt.exit.read_only_days` | PLT→TEN | G | int 30–180 | 90 | `ORG_OWNER` | Y |
| `xpt.profile.major_change_notice_days` | PLT | G | int ≥ 30 | 30 | `PLT_SUPER_ADMIN` | Y |
| `xpt.offline_viewer.enabled` | TEN | O | bool | true for FULL/EXIT | `ORG_ADMIN` | N |

### R.9.35 `web` — public site and CMS (P21)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `web.render.ssr_ssg` | PLT | L | bool | true (NN-31) | — | — |
| `web.private.noindex` | PLT | L | bool | true | — | — |
| `web.crawl.ai_search_bots_allowed` | BRD | G | bool | true — AI search-retrieval bots allowed on public content; private routes always disallowed (P21 FR-P21-51; NN-31) | `PLT_SUPER_ADMIN` | Y (checker `PLT_SECURITY_OFFICER`) |
| `web.crawl.ai_training_bots_allowed` | BRD | G | bool | false [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.crawl.google_extended_allowed` | BRD | G | bool | false [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.ads.placements` | BRD | G-elv | menum blog/vlog/learning | none (D-13) | `PLT_SUPER_ADMIN` | Y |
| `web.ads.personal_targeting` | PLT | L | bool | false (NN-35) | — | — |
| `web.ads.on_advocate_pages` | PLT | L | bool | false | — | — |
| `web.cms.publish_requires_review` | BRD | G | bool | true | `PLT_CONTENT_EDITOR` | N |
| `web.claims.registered_only` | PLT | L | bool | true (NN-20; P23 claims register) | — | — |
| `web.testimonials.photos_enabled` | BRD | G | bool | false; locked OFF on advocate and court pages (R-088; NN-49; P21) | `PLT_CONTENT_EDITOR` | Y |
| `web.draft_with_ai_block` | BRD | O | bool | true (R-087) | `PLT_CONTENT_EDITOR` | N |
| `web.hire_professional_block` | BRD | O | bool | true | `PLT_CONTENT_EDITOR` | N |
| `web.video.privacy_enhanced_embed` | BRD | O | bool | true [VERIFY behaviour] | `PLT_CONTENT_EDITOR` | N |
| `web.cookies.consent_banner` | PLT | L | bool | true (no non-essential cookies before consent) | — | — |

#### R.9.35A IPB-04 additions — `web.*`, `brand.*`, `cms.*`, `mkt.*`, `fb.*` (P21 §4A, §4I, §4L, §4R, §4S) *(v1.1)*

`brand`, `cms`, `mkt` and `fb` are shared-package prefixes (IPB-04) sanctioned like `vidhi` (OI-R-08).

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `web.blog.enabled` | BRD | O | bool | true | `PLT_SUPER_ADMIN` | N |
| `web.blog.user_posts.enabled` | BRD | G-leg | bool | false | `PLT_SUPER_ADMIN` | Y |
| `web.blog.user_posts.eligible_roles` | BRD | G-leg | menum | ORG_OWNER, ORG_ADMIN, ORG_MEMBER, IND_OWNER, PRO_CA, PRO_CS, PRO_TAX_PRACTITIONER, PRO_OTHER | `PLT_SUPER_ADMIN` | Y |
| `web.blog.user_posts.min_account_age_days` | BRD | G | int | 30 | `PLT_SUPER_ADMIN` | N |
| `web.blog.user_posts.daily_limit` | BRD | G | int | 3 | `PLT_SUPER_ADMIN` | N |
| `web.blog.comments.enabled` | BRD | G | bool | false | `PLT_SUPER_ADMIN` | N |
| `web.blog.feed.full_text` | BRD | O | bool | false | `PLT_CONTENT_EDITOR` | N |
| `web.vlog.enabled` | BRD | O | bool | true | `PLT_SUPER_ADMIN` | N |
| `web.resources.enabled` | BRD | O | bool | true | `PLT_SUPER_ADMIN` | N |
| `web.resources.review_due_months` | BRD | O | int | 12 | `PLT_CONTENT_EDITOR` | N |
| `web.resources.expired_behaviour` | BRD | O | enum banner/withdraw | banner | `PLT_CONTENT_EDITOR` | N |
| `web.investors.enabled` | BRD | G-leg | bool | false | `PLT_SUPER_ADMIN` (checker `PLT_LEGAL_REVIEWER`) | Y |
| `web.docs.url` | BRD | O | text | `https://developers.lawdocs.in` | `PLT_CONTENT_EDITOR` | N |
| `web.footer.group_url` | PLT | G | text | [OWNER] | `PLT_SUPER_ADMIN` | Y |
| `web.legal.payment_terms.enabled` | BRD | G-leg | bool | true | `PLT_LEGAL_REVIEWER` | Y |
| `web.legal.blog_ugc_terms.version_required` · `web.legal.resources_terms.version_required` · `web.legal.investors_disclaimer.locked` | PLT | L | bool | true | — | — |
| `brand.app_name` | BRD→TEN (white-label plan) | G | text | "LawDocs" | `PLT_SUPER_ADMIN`; `ORG_OWNER` (white-label) | Y |
| `brand.terminology` | BRD→TEN (white-label plan) | G | json | {} | as above | Y |
| `brand.contrast.min_text` · `brand.contrast.min_ui` | PLT | G ↑ | dec | 4.5 · 3.0 | `PLT_SUPER_ADMIN` | Y |
| `brand.fonts.self_hosted_only` | PLT | L | bool | true | — | — |
| `brand.email.require_dmarc` | PLT | G-elv | bool | true | `PLT_SECURITY_OFFICER` | Y |
| `brand.hosts.unknown_behaviour` | PLT | G-elv | enum | `default_pack_noindex` | `PLT_SECURITY_OFFICER` | Y |
| `cms.publish.legal_review_types` | PLT | G-leg ⊂ (add only) | menum | legal_page, pricing_copy, footer, redirect, brand_pack, investors, trust, document, pleading, service, regulated_entity | `PLT_LEGAL_REVIEWER` | Y |
| `cms.media.ai_images.require_review` | PLT | L | bool | true | — | — |
| `cms.import.zip_ratio_max` | PLT | G-elv | int | 10 | `PLT_SECURITY_OFFICER` | Y |
| `cms.review.stale_days` | PLT | O | int | 365 | `PLT_SUPER_ADMIN` | N |
| `cms.soft_delete.restore_days` | PLT | G | int | 30 | `PLT_SUPER_ADMIN` | Y |
| `mkt.tag_manager.adapter` | BRD | G-prv | enum none/gtm_server/gtm_web | none | `PLT_SUPER_ADMIN` (`PLT_DPO` veto) | Y |
| `mkt.tag_manager.container_id` | BRD | G | text | null | `PLT_SUPER_ADMIN` | Y |
| `mkt.analytics.adapter` | BRD | G-prv | enum matomo/posthog/plausible/ga4/none | matomo | `PLT_SUPER_ADMIN` | Y |
| `mkt.pixels.enabled` | BRD | G-prv | menum | [] | `PLT_SUPER_ADMIN` (`PLT_DPO` veto) | Y |
| `mkt.sensitive_routes` | PLT | G-prv ⊂ (add only) | list | locked list + additions | `PLT_DPO` | Y |
| `mkt.attribution.window_days` | BRD | O | int | 90 | `PLT_CONTENT_EDITOR` | N |
| `mkt.forms.retain_payload_hours` | PLT | G-prv | int | 72 | `PLT_DPO` | Y |
| `mkt.webhooks` | BRD | G-int | json | [] | `PLT_SUPER_ADMIN` | Y |
| `fb.widget.floating` | BRD | O | bool | false (public) / true (apps) | `PLT_CONTENT_EDITOR` | N |
| `fb.nps.interval_days` | PLT | O | int | 90 | `PLT_SUPER_ADMIN` | N |
| `fb.screenshot.enabled` | PLT | G-prv | bool | false | `PLT_DPO` | Y |
| `fb.idea_board.enabled` | BRD | O | bool | false | `PLT_SUPER_ADMIN` | N |
| `hlp.reg_reference_panel.enabled` | PLT | O | bool | true | `PLT_CONTENT_EDITOR` | N |

### R.9.36 `hlp` — help centre, "i" glossary, tutorials (P21)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `hlp.i_buttons.enabled` | PLT | L | bool | true (R-019) | — | — |
| `hlp.help_key.required_for_new_terms` | PLT | L | bool | true (`help-key-lint`) | — | — |
| `hlp.glossary.languages` | BRD | O | menum (D-07) | en, hi | `PLT_CONTENT_EDITOR` | N |
| `hlp.tutorials.reviewer_of_record` | PLT | L | bool | true for legal content (NN-30) | — | — |
| `hlp.video.captions_default_on` | PLT→USR | O (platform default locked ON; a user may switch captions off for themselves only) | bool | true (NN-28; P21) | user | N |
| `hlp.tours.auto_start_first_run` | TEN→USR | O | bool | true (P21) | `ORG_ADMIN`, user | N |
| `hlp.contextual_vidhi_help` | TEN→USR | O | bool | true | user | N |
| `hlp.accessibility_statement_url` | BRD | G | text | published statement | `PLT_CONTENT_EDITOR` | N |

### R.9.37 `rpt` — dashboards and reports (P13, P17)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `rpt.accessible_table_alternative` | PLT | L | bool | true | — | — |
| `rpt.scheduled_reports.max` | PLN | G | int | 0 / 2 / 10 / 50 / band | `PLT_SUPER_ADMIN` | N |
| `rpt.async_threshold_rows` | PLT | G | int | 10,000 | CTO | N |
| `rpt.export.formats` | TEN | O | menum xlsx/csv/pdf | xlsx, pdf | `ORG_ADMIN` | N |
| `rpt.ops_hub.aggregate_sharing` | TEN | G-elv | bool | aggregates only; tenant may opt out of optional metrics | `ORG_OWNER` | Y |
| `rpt.default_period` | TEN→USR | O | enum FY/CY/last_90_days | FY (Company), CY (Personal) | user | N |

### R.9.38 `mob` — mobile BFF and device trust (P22)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| (retired `mob.min_supported_version`; duplicate) | — | — | — | Read `mob.version.min_supported` (second review, G3 R-1) | — | — |
| `mob.screenshot_block_protected` | PLT | L | bool | true (NN-44) | — | — |
| `mob.cert_pinning` | PLT | L | bool | true | — | — |
| `mob.device_logs_sensitive` | PLT | L | bool | false | — | — |
| `mob.root_jailbreak.action` | PLT→TEN | G | enum warn/block_vault/block_app | block_vault | `ORG_ADMIN` | Y |
| `mob.offline_cache.enabled` | TEN→USR | O | bool | true (encrypted, device-bound keys) | `ORG_ADMIN`, user | N |
| `mob.offline_cache.max_mb` | TEN→USR ↓ | O | int 50–2,000 | 500 | user | N |
| `mob.biometric_unlock` | USR | O | bool | false (opt-in; device-local) | user | N |
| `mob.push.content_preview` | USR | O | bool | false | user | N |
| `mob.nav.tab_order` | USR | O | list per workspace (order within the group; P22 governs) | Personal: Home · Vault · Create · Activity · Me; Company: Home · Inbox · Contracts · Matters · More (P22 FR-P22-03) | user | N |
| `mob.bottom_bar.items` | TEN | O | list (exactly 2 — the Company tab bar's middle slots; Home, Inbox and More are fixed; P22 FR-P22-03 governs) | `[Contracts, Matters]` | `ORG_ADMIN` | N |

### R.9.39 `eng` — engineering governance (P23)

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `eng.branch.max_age_days_block` | PLT | G | int 2–10 | 5 | CTO | N |
| `eng.deploy.required_approvers` | PLT | L | int | 2 | — | — |
| `eng.deploy.require_change_approved` | PLT | L | bool | true | — | — |
| `eng.deploy.windows` | PLT | G | rrule | Tue, Thu 22:00–24:00 IST | `PLT_RELEASE_MANAGER` | Y |
| `eng.freeze.default_windows` | PLT | G | list | P23 FR-P23-14 | CAB | Y |
| `eng.notice.behaviour_change_working_days` | PLT ↑ | G | int ≥ 5 | 5 | `PLT_RELEASE_MANAGER` | Y |
| `eng.notice.maintenance_hours` | PLT ↑ | G | int ≥ 72 | 72 | `PLT_RELEASE_MANAGER` | N |
| `eng.notice.api_deprecation_months` | PLT ↑ | G | int ≥ 12 | 12 (P19 FR-P19-06) | CTO | Y |
| `eng.notice.subprocessor_days` | PLT ↑ | G-prv | int ≥ 30 | 30 | `PLT_DPO` | Y |
| `eng.patch.sla_critical_hours` | PLT ↓ | G (outer 72 L) | int | 72 | `PLT_SECURITY_OFFICER` | Y |
| `eng.patch.sla_high_days` | PLT ↓ | G (outer 15 L) | int | 7 | `PLT_SECURITY_OFFICER` | Y |
| `eng.patch.sla_medium_days` | PLT ↓ | G (outer 45 L) | int | 30 | `PLT_SECURITY_OFFICER` | Y |
| `eng.patch.sla_low_days` | PLT ↓ | G (outer 90 L) | int | 90 | `PLT_SECURITY_OFFICER` | Y |
| `eng.patch.secret_rotation_hours` | PLT | L | int | 24 | — | — |
| `eng.patch.dependency_cooldown_days` | PLT | G | int 0–14 | 7 | `PLT_SECURITY_OFFICER` | N |
| `eng.risk_acceptance.max_days` | PLT | L | int | 90 | — | — |
| `eng.backup.pitr_days` | PLT ↑ | G (floor 35 L) | int | 35 | `PLT_SRE` | Y |
| `eng.backup.t0_rpo_minutes` | PLT | L | int | 15 | — | — |
| `eng.backup.t0_rto_hours` | PLT | L | int | 4 | — | — |
| `eng.backup.fy_end_retention_years` | PLT | G | int | 8 [REC] | CTO | Y |
| `eng.restore_test.db_frequency` | PLT | G (floor monthly L) | enum | weekly | `PLT_SRE` | N |
| `eng.dr.drill_frequency_months` | PLT | G | int 3–12 | 6 | CTO | N |
| `eng.logs.retention_days_india` | PLT ↑ | G (floor 180 L; 365 for personal-data logs) | int | 400 | `PLT_SECURITY_OFFICER` | Y |
| `eng.vapt.external_frequency_months` | PLT | G | int 1–6 | 3 | `PLT_SECURITY_OFFICER` | N |
| `eng.vapt.certin_annual` | PLT | L | bool | true | — | — |
| `eng.flag.bug_bounty` | PLT | G-elv | bool | false | CTO | Y |
| `eng.hypercare.days` | PLT | G | int | 14 (W1, W2); 21 (W3) | product owner | N |
| `eng.claims.require_evidence` | PLT | L | bool | true (NN-20) | — | — |
| `eng.ai.eval_max_drop_points` | PLT | G | dec | 2.0 | AI lead | Y |
| `eng.rings.early_access_opt_in` | TEN | O | bool | false | `ORG_ADMIN` | N |
| `eng.rings.pin_days` | TEN | G | int 0–30 | 0 (Enterprise up to 30) | `ORG_OWNER` | N |

---

#### R.9.39A IPB-08/09/11 additions — `eng.*`, `trust.*`, `sec.org.*`, `xpt.portability.*`, `int.calendar.*` (P03 §4P, P19, P20, P23) *(v1.1)*

| Key | Tier | Class | Type | Default | Changed by | MC |
|---|---|---|---|---|---|---|
| `eng.branch.allowed_prefixes` | PLT | L | list | feat, fix, hotfix, release, chore, docs, refactor, perf, test, ci, deps, cc | — | — |
| `eng.beta.enabled` | TEN | O | bool | false | `ORG_OWNER` | N |
| `eng.beta.flag_overrides` | TEN | G | json | {} | `PLT_RELEASE_MANAGER` | Y |
| `eng.release_notes.notice_days.normal` · `.pricing` | PLT | G | int | 7 · 30 | `PLT_RELEASE_MANAGER` | Y |
| `eng.release_notes.require_legal_review_tags` | PLT | L | list | `reg:*` | — | — |
| `trust.mirror.enabled` | PLT | L | bool | true | — | — |
| `trust.public.show_vapt_summary` | PLT | G | bool | true | `PLT_SECURITY_OFFICER` | Y |
| `trust.grant.max_days` | PLT | G-elv | int 1–180 | 180 | `PLT_SECURITY_OFFICER` | Y |
| `trust.request.ack_hours` · `trust.request.fulfil_days` | PLT | G | int | 24 · 10 | `PLT_SECURITY_OFFICER` | N |
| `trust.watermark.enabled` | PLT | L | bool | true | — | — |
| `sec.org.password.min_length` | TEN | G-elv ↑ (floor 12) | int 12–64 | 12 | `ORG_ADMIN` | Y |
| `sec.org.mfa.required_roles` | TEN | G-elv | menum | all `ORG_*` admin roles | `ORG_ADMIN` | Y |
| `sec.org.session.idle_minutes` · `sec.org.session.max_concurrent` | TEN | G | int | 60 · 5 | `ORG_ADMIN` | Y |
| `sec.org.ip_allowlist` | TEN | G-elv | list (CIDR) | [] | `ORG_OWNER` | Y (24 h notice) |
| `sec.org.byok.kms_key_ref` | TEN (Enterprise) | G-elv | ref (secret) | null | `ORG_OWNER` | Y |
| `cfg.settings_tree` | PLT | G | json | IPB-07 20-node seed + LD additions | `PLT_SUPER_ADMIN` | Y |
| `cfg.palette.pii_refusal` | PLT | L | bool | true | — | — |
| `ux.simple_mode` · `ux.appearance.density` | USR | O | bool · enum | false · comfortable | user | N |
| `tut.whats_new.suppress` | TEN | O | enum none/minor/all_but_regulatory | none | `ORG_ADMIN` | N |
| `xpt.portability.drill_interval_months` | PLT | G | int 3–12 | 6 | `PLT_RELEASE_MANAGER` | Y |
| `xpt.portability.rto_hours.<port>` | PLT | G | int | per P20 FR-P20-53 | `PLT_SRE` | Y |
| `xpt.storage.object_lock_mode` · `xpt.db.engine` | PLT | L | enum | COMPLIANCE · postgresql | — | — |
| `int.calendar.providers_enabled` · `int.calendar.sync_interval_minutes` | TEN | O | list · int | [internal] · 15 | `ORG_ADMIN` | N |
| `int.webhooks.standard_webhooks` · `int.api.problem_details_rfc9457` | PLT | L | bool | true | — | — |
| `int.connectors.marketplace.enabled` | PLT | G-int | bool | true | `PLT_SUPER_ADMIN` | Y |
| `int.connectors.install.requires_checker_for_write` | TEN | G-int | bool | true | `ORG_OWNER` | Y |
| `int.<port>.primary` · `int.<port>.secondary` (every IPB-01 port) | PLT | G-int | enum | master §21.1 | `PLT_RELEASE_MANAGER` | Y |

## R.10 Customisation catalogue by user type (R-047, R-028, R-030)

"On their own" = OPEN, immediate, undoable. "With a checker" = GOVERNED tenant change approved by another person. "Never" = LOCKED or platform-only.

| User type | On their own | With a checker | Never (and why) |
|---|---|---|---|
| **Individual** (`IND_OWNER`) | Language, text size, theme, density, reduced motion, dyslexia font, screen-reader hints; home widgets; pinned menu items; quick actions; vault categories and folder names (views); tags; expiry and renewal reminder timing; quiet hours and digest times; channels for their own notices; family members' labels and folder sharing; nominee and legacy settings; Vidhi on/off, answer language and tone; offline cache and biometric unlock on their phone; export and storage destinations; signing order and request expiry for documents they send | Not applicable (single-person workspace). A guardian acts for a ward within guardianship scope | Aadhaar login (NN-03); eSign of excluded instruments (NN-07); stamp-before-sign (NN-08); AI labels (NN-14); counterparty reminder caps (NN-34); deletion of eSign evidence before its retention floor |
| **Family member / delegate** (`IND_FAMILY_MEMBER`, `IND_DELEGATE`) | Own preferences; items on shared records | — | Owner's workspace settings |
| **Company owner / admin** (`ORG_OWNER`, `ORG_ADMIN`) | All OPEN tenant settings: terminology and labels, custom fields, status labels, reason codes, numbering, forms, letterheads, themes, menus, home layouts per user type, quick-action defaults, item types, chase cadences, internal SLAs above floors, notification templates (non-legal text), sender domain, export folder policy (non-privacy options), sandbox, configuration templates (OPEN parts) | Approval matrices, authority limits, retention above floors, export approvals, delivery-grant scopes, outbound channels, BYO targets for regulated data, pre-approved reminder series, credential vault enablement, autonomy raises, person-naming mode in exports, master-data changes | LOCKED keys; platform prices; legal rule rows (rule challenge instead) |
| **Chief legal officer** (`ORG_CLO`) | Legal intake request types, triage SLAs, assignment policy, legal warning days (raise only), counsel panel, legal calendar contents, CLO dashboard (mandatory widgets stay) | Checker for legal-workflow GOVERNED keys; formalities waivers (per item) | As above |
| **Department head** (`ORG_DEPT_HEAD`) | Within delegated sections for the department: labels, default owners, reminder and chase cadence, dashboards and quick actions for members, intake defaults | Department-level GOVERNED proposals | Other departments; tenant-wide security |
| **Maker / checker / approver / member / director / KMP** | Personal preferences; saved views; personal quick actions and pins; delegation when away; own reminders | — | Tenant configuration |
| **Professional** (`PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`) | Personal preferences; practice templates' non-legal text; hearing reminder offsets; matter views | Firm-level changes via `PRO_FIRM_ADMIN` | Marketplace fee, ranking and rating rules (NN-21); directory fields beyond BCI Rule 36 |
| **Firm admin** (`PRO_FIRM_ADMIN`) | Practice workspace OPEN settings: letterhead, numbering, item types, intake forms, white-label branding within brand rules | Member role elevation; data export of the practice | Client-owned workspace settings |
| **RM / delegated maker** (`OPS_RM`, `ORG_DELEGATED_MAKER`) | Own preferences | **Proposes** client changes under a delivery grant with `cfg:propose`; client user approves (R-064, CH-26) | Approving anything in the client tenant |
| **Consumer case manager** (`OPS_CONSUMER_CASE_MANAGER`) | Own preferences; case item views | Desk-level chase and status-update cadence (with `OPS_DELIVERY_LEAD`) | Forum timelines, representation rules, success-fee switch, ethical wall |
| **Super Admin** (`PLT_SUPER_ADMIN`) | Platform and brand defaults and bounds (with platform checker) | Tenant changes only via Correction Entry with second platform approver; crucial client details also need client approval | LOCKED keys; reading tenant documents through configuration tools |

---

## R.11 Open / interim / waiting item-type catalogue (platform seed)

Columns: **Code** · **Parent** · **Default owner** · **Typical waiting party** · **Clocks** (L legal, C contractual, E earliest-action, S internal SLA) · **Resolve needs** · **Gate** (participates in the formalities gate, NN-40).

| Code | Parent | Default owner | Typical waiting party | Clocks | Resolve needs | Gate |
|---|---|---|---|---|---|---|
| `AGR_INTERNAL_REVIEW` | Agreement | Legal maker | `INTERNAL_DEPARTMENT` | S | Reviewer decision | — |
| `AGR_COUNTERPARTY_REVIEW` | Agreement / negotiation round | Agreement owner | `COUNTERPARTY` | S, C (offer validity) | Counterparty response or round | — |
| `AGR_APPROVAL_PENDING` | Agreement | Approver per matrix | `INTERNAL_USER` | S | Approval record | Yes (if matrix requires) |
| `AGR_BOARD_APPROVAL_PENDING` | Agreement | Company secretary / `ORG_KMP` | `INTERNAL_DEPARTMENT` (board) | S | Resolution reference | Yes |
| `AGR_STAMP_PENDING` | Agreement | Agreement owner | `VENDOR` (eStamp channel) / `PAYMENT` | S | Certificate UIN verified and linked to hash (NN-08) | Yes |
| `AGR_SIGNATURE_PENDING` | Signing request | Sender | `SIGNATORY` | C (request expiry), S | All signatures with evidence | Yes |
| `AGR_WITNESS_PENDING` | Agreement | Sender | `WITNESS` | S | Witness attestation | Yes |
| `AGR_NOTARISATION_PENDING` | Agreement / affidavit | Owner | `NOTARY` | S | Notarised copy uploaded | Yes |
| `AGR_REGISTRATION_PENDING` | Agreement | Owner | `REGISTRY` (Sub-Registrar) | L (presentation window [VERIFY Registration Act s.23]), S | Registered copy + registration number | Yes |
| `AGR_COUNTERPARTY_STAMP_SHARE` | Agreement | Owner | `COUNTERPARTY` / `PAYMENT` | S | Payment confirmation | — |
| `AGR_RENEWAL_DECISION` | Agreement | Agreement owner | `INTERNAL_USER` | C (notice window), S | Renew / terminate / let expire | — |
| `AGR_TERMINATION_NOTICE` | Agreement | Owner | `COUNTERPARTY` | C | Notice served with proof | — |
| `OBL_OBLIGATION_DUE` | Obligation | Obligation owner | any | C | Evidence of performance | — |
| `OBL_PAYMENT_DUE` | Obligation | Finance contact | `PAYMENT` | C | Payment reference | — |
| `DOC_EXPIRY` | Document (ID, licence, insurance) | Document owner | — | C | Renewed document | — |
| `DOC_REQUESTED_FROM_PARTY` | Any record | Requester | `CLIENT` / `COUNTERPARTY` | S | Upload received | — |
| `DMS_IMPORT_REVIEW` | Import job | Importer | — | S | All files placed or skipped | — |
| `DIX_TYPECOPY_REVIEW` | Derived rendition | Document owner | `INTERNAL_USER` | S | Reviewer confirms or edits (NN-09) | — |
| `DIX_TRANSLATION_REVIEW` | Translation | Document owner | `PROFESSIONAL` (certified translator for filing) | S | Reviewed/certified version (NN-48) | — |
| `DRF_AI_DRAFT_REVIEW` | Draft | Drafter | `PROFESSIONAL` (paid review) | S | Reviewer approval removes AI label (NN-14) | — |
| `LGO_REQUEST_TRIAGE` | Legal request | Legal intake desk | — | S | Triage decision | — |
| `LGO_INFO_FROM_BUSINESS` | Legal request | Assignee | `INTERNAL_DEPARTMENT` | S | Information received | — |
| `LIT_FILING_PREPARATION` | Case | Matter lead | `PROFESSIONAL` / `CLIENT` | L (limitation advisory), S | Filed with diary number | — |
| `LIT_DEFECT_CURE` | Case | Matter lead | `COURT` | L (cure period per court rules [VERIFY]) | Defect cured, listing date | — |
| `LIT_NEXT_HEARING_PREP` | Hearing | Matter lead | `PROFESSIONAL` | L (hearing date) | Hearing outcome recorded | — |
| `LIT_ORDER_AWAITED` | Hearing | Matter lead | `COURT` | S | Order obtained (source + fetched-at) | — |
| `LIT_CERTIFIED_COPY_AWAITED` | Order | Matter lead | `COURT` | L (appeal limitation advisory) | Certified copy uploaded | — |
| `LIT_APPEAL_DECISION` | Order | `ORG_CLO` / individual | `PROFESSIONAL` | L (limitation advisory) | Decision recorded | — |
| `LIT_NOTICE_REPLY` | Notice received | Assignee | `PROFESSIONAL` | C/L (reply period stated in notice) | Reply sent with proof | — |
| `IPM_TM_FILING_STATUS` | Trademark | IP owner | `REGISTRY` (TM Registry) | S | Application number recorded | — |
| `IPM_EXAMINATION_REPLY` | Trademark | IP owner | `PROFESSIONAL` | L (reply window [VERIFY]) | Reply filed | — |
| `IPM_OPPOSITION_WINDOW` | Trademark | IP owner | `REGISTRY` | L (from journal date [VERIFY s.21]) | Window closed or opposition handled | — |
| `IPM_RENEWAL_DUE` | Trademark | IP owner | — | L (renewal date) | Renewal filed | — |
| `GOV_MINUTES_SIGNATURE` | Meeting | Company secretary | `INTERNAL_USER` (chair) | L (SS-1 [VERIFY]) | Signed minutes | — |
| `GOV_FILING_PENDING` | Resolution / event | Company secretary | `REGISTRY` (MCA) | L (form due date) | SRN/acknowledgement | — |
| `HR_POLICY_ACK` | Policy | HR | `INTERNAL_USER` | S | Acknowledgements | — |
| `BSV_GOVT_APPLICATION` | Service order | Delivery owner | `REGISTRY` / `GOVERNMENT_PORTAL` | S | Registration/certificate issued | — |
| `BSV_CLIENT_DOCUMENTS` | Service order | Delivery owner | `CLIENT` | S | Documents received | — |
| `TAX_DOCS_AWAITED` | Tax engagement | Practitioner | `CLIENT` | L (due date) | Documents received | — |
| `TAX_TAXPAYER_VERIFICATION` | Tax return | Practitioner | `CLIENT` (EVC/DSC by taxpayer) | L (verification window [VERIFY]) | Verification acknowledgement | — |
| `TAX_REFUND_STATUS` | Tax return | Taxpayer | `GOVERNMENT_PORTAL` | S | Refund status recorded | — |
| `CHP_RE_COMPLAINT_RESPONSE` | Consumer case | Case manager / user | `REGULATOR`-adjacent: the regulated entity (`COUNTERPARTY`) | E (30-day wait, RB-IOS [VERIFY]), L (filing window) | RE reply or wait expiry | — |
| `CHP_OMBUDSMAN_STATUS` | Consumer case | User / case manager | `REGULATOR` (RBI CMS) | S | Status/outcome recorded | — |
| `CHP_INSURER_RESPONSE` | Consumer case | Case manager | `COUNTERPARTY` (insurer) | E, L (Ombudsman window) | Insurer reply | — |
| `CHP_INSURANCE_OMBUDSMAN` | Consumer case | User / case manager | `REGULATOR` | L | Award/outcome | — |
| `CHP_CREDIT_REPORT_DISPUTE` | Consumer case | User | `COUNTERPARTY` (credit bureau via user) | S | Bureau response uploaded by user | — |
| `CHP_CHALLAN_COURT_DATE` | Challan record | User | `COURT` (Virtual Court) | L (court date) | Disposal recorded; payment made by user on official portal | — |
| `CHP_VEHICLE_RC_TRANSFER` | Vehicle record | Seller/buyer | `GOVERNMENT_PORTAL` (Vahan) | S | Transfer status recorded (CH-23) | — |
| `MKP_CLIENT_INPUT` | Engagement | Professional | `CLIENT` | S (SLA from engagement) | Input received | — |
| `MKP_DELIVERABLE_DUE` | Engagement | Professional | `PROFESSIONAL` | C (eSigned SLA) | Deliverable accepted | — |
| `SDC_CLIENT_CHECKER_APPROVAL` | Delivery task | RM (maker) | `CLIENT` (checker) | S | Client approval (R-064) | — |
| `SDC_GRANT_RENEWAL` | Delivery grant | `OPS_DELIVERY_LEAD` | `CLIENT` | C (grant expiry) | Renewed or ended | — |
| `CVL_REVEAL_APPROVAL` | Credential entry | Requester | `CLIENT` | S (10 minutes) | Approval or expiry (NN-16) | — |
| `KYC_DOCUMENT_AWAITED` | Verification | User / onboarding | `CLIENT` / `COUNTERPARTY` | S | Verification result | — |
| `PRIV_DSR_RESPONSE` | Privacy request | `PLT_DPO` / tenant privacy contact | — | L (≤ 90 days; internal 30) | Response sent | — |
| `PRIV_GRIEVANCE_RESPONSE` | Grievance | Grievance officer | — | L (24 h ack; 7 days resolve [VERIFY]) | Resolution sent | — |
| `XPT_TARGET_CONFLICT` | Storage target | Target owner | `INTERNAL_USER` | S | Conflict resolved | — |
| `XPT_EXPORT_APPROVAL` | Export job | Requester | `INTERNAL_USER` (checker) | S (72 h expiry) | Approval or rejection | — |
| `VENDOR_ADAPTER_OUTAGE` | Adapter incident | `PLT_SRE` | `VENDOR` | S | Adapter healthy; kill switch released | — |
| `CFG_CHANGE_REQUEST` | Setting / lock | Locker or admin | `INTERNAL_USER` | S | Change decided | — |
| `ECO_AWAITING_PRODUCT` | Any record | Owner | `ECOSYSTEM_SYSTEM` (LDC/EQ/FX/UD) | S | Matching event received | — |

Tenants and individuals add their own types within plan limits (`cfg.item_types.max_tenant_defined`), choosing parent types, owners, waiting parties, clocks (internal SLA and contractual only — legal clocks come from rule sets), evidence and chase policies.

---

## R.12 Waiting-party types and chase defaults

| Party type | Auto-chase allowed | Default channels | Default cadence / max | Mode |
|---|---|---|---|---|
| `INTERNAL_USER`, `INTERNAL_DEPARTMENT` | Yes | in-app, email, push | P2D / 5 | Automatic |
| `CLIENT` | Yes | client portal item, email | P3D / 5 | Automatic (client is a tenant user) |
| `COUNTERPARTY`, `SIGNATORY`, `WITNESS`, `NOTARY` (external persons) | Yes, within NN-34 | email; SMS/WhatsApp only with DLT/registered template | P3D / 3 | `CONFIRM_EACH` (default) or `PRE_APPROVED_SERIES` (GOVERNED, transactional only) |
| `PROFESSIONAL` | Yes | engagement thread, email | P2D / 5 | Automatic |
| `COURT`, `REGISTRY`, `REGULATOR`, `GOVERNMENT_PORTAL` | **No** (LOCKED) | Internal "check status" task to owner with deep link | P7D task | n/a |
| `VENDOR` | Status polling via adapter; no messages | — | Adapter-specific | Automatic poll |
| `ECOSYSTEM_SYSTEM` | Event correlation | — | — | Automatic resume |
| `PAYMENT` | Payment status from OH8 | — | — | Automatic resume |

---

## R.13 Who can change what without a super admin (summary, R-047)

1. Every user changes their own preferences, layouts, pins, quick actions, reminders and notifications at once, with undo.
2. Company admins change every OPEN tenant setting at once; GOVERNED tenant settings need another tenant user's approval — never LawDocs.
3. Department heads change delegated department settings at once.
4. Individuals are their own administrators for their Personal workspace.
5. RMs and delegated makers propose; client users approve.
6. LawDocs staff change tenant configuration only through a dual-approved Correction Entry visible to the tenant, with client approval for crucial details (CH-26).
7. LOCKED values change only through a platform release with an ADR and NN test.

---

## R.14 Compiled phase registrations (index)

Generated from the §9 settings tables of every phase file on 25 October 2026 (keys not already listed in §R.9). **Type, default, bounds and changed-by are as registered in the owner phase §9 table, which is authoritative for these rows**; tier and maker-checker are copied here so that the registry seed, `appendix-r-sync` and `nn18-keys` can be generated from one index. A key listed in both §R.9 and a phase table follows §R.9; the differences found in this compilation were resolved in favour of the owner phase (`dms.upload.max_file_mb`, `iam.delegation.max_days`, `msg.edit_window_minutes`), and the nominee waiting and access periods are the P01 keys `iam.nominee.release_waiting_days` and `iam.nominee.access_days` (Appendix A §A.8 uses them; P04 `dms.nominee.waiting_days` / `dms.nominee.access_days` are withdrawn; `dms.nominee.inactivity_days` stays with P04). Integration review F1 (25 Oct 2026) removed every key that appeared in both §R.9 and this index (the §R.9 row now carries the owner phase's definition) and replaced retired names per X-11. Non-standard prefixes found in phase tables (`api`, `auth`, `my`, `work`, `www`) are host or route names, not settings, and are excluded; `wks.*` (P18) are settings and are registered in §R.9.32A (registry review G4). `int.connectors.kill_switch_key` (cited in P11 §9 and P12 §9) is a column of table `int.connectors` (P19 §7.2) that holds the `int.kill.<adapter>` key of each adapter, not a setting; the adapter kill switches themselves are the `int.kill.<adapter>` family in §R.9.33. Rows whose tier text is non-standard are copied verbatim for the owner phase to normalise at the next sync.

### `core` (16 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `core.audit.anchor_time_ist` | P00 | PLT | — |
| `core.audit.anchor_tsa.enabled` | P00 | PLT | Y |
| `core.audit.retention_years` | P00 | PLT (tenant may lengthen) | Y |
| `core.break_glass.max_minutes` | P00 | PLT | Y |
| `core.break_glass.tenant_report_hours` | P00 | PLT | — |
| `core.correction.escalation_working_days` | P00 | TEN | N |
| `core.correction.justification_min_chars` | P00 | PLT | — |
| `core.correction.tenant_ack_mode` | P00 | PLT | Y |
| `core.migration.ai_assist.enabled` | P00 | PLT | Y (checker `PLT_DPO`) |
| `core.migration.max_defect_rate` | P00 | PLT | Y |
| `core.migration.money_tolerance` | P00 | PLT | — |
| `core.migration.unverified_retention_months` | P00 | PLT | Y |
| `core.provider_routing.nonprod` | P00 | PLT | — |
| `core.tenant.number_format` | P00 | USR | N |
| `core.tenant.timezone` | P00 | TEN | N |
| `core.tenant.year_basis` | P00 | TEN | N |

### `iam` (23 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `iam.access_review.auto_revoke_unreviewed` | P02 | TEN | Y |
| `iam.access_review.cadence.<grant_type>` | P02 | TEN | Y |
| `iam.age_assurance.mode` | P01 | PLT | Y |
| `iam.anonymous_draft.ttl_hours` | P01 | PLT | Y |
| `iam.break_glass.prior_consent` | P02 | TEN | Y |
| `iam.delegate.max_days` | P02 | USR (≤ 365) | N |
| `iam.grant.auditor.max_days` | P02 | PLT | — |
| `iam.grant.delivery.max_months` | P02 | PLT | Y |
| `iam.grant.engagement.read_tail_days` | P02 | TEN | N |
| `iam.grant.renewal_notice_days` | P02 | TEN | N |
| `iam.guest.invite_ttl_days` | P01 | TEN | N |
| `iam.nominee.access_days` | P01 | PLT | Y |
| `iam.nominee.max` | P01 | PLT | Y |
| `iam.nominee.release_waiting_days` | P01 | USR (bounded 7–90) | N |
| `iam.otp.max_sends_per_30min` | P01 | PLT | Y |
| `iam.otp.ttl_seconds` | P01 | PLT | Y |
| `iam.otp.voice.enabled` | P01 | BRD | Y |
| `iam.otp.whatsapp.enabled` | P01 | BRD | Y |
| `iam.session.idle_minutes.<class>` | P01 | PLT (tenant may shorten) | N (tenant shorten) |
| `iam.sod.<rule>.enforcement` | P02 | TEN (WARN → BLOCK only) | Y |
| `iam.sso.enforce` | P01 | TEN | Y |
| `iam.stepup.<action>` | P01 | PLT (tenant may tighten) | Y |
| `iam.support_session.max_minutes` | P02 | PLT | Y |

### `kyc` (15 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `kyc.consent.withdrawal_propagation_minutes` | P01 | PLT | — |
| `kyc.consent_manager.enabled` | P01 | PLT | Y |
| `kyc.digilocker.enabled` | P01 | PLT | Y |
| `kyc.discovery.quota.<tier>` | P01 | PLT / PLN | Y |
| `kyc.entity_locker.enabled` | P01 | PLT | Y |
| `kyc.grievance.resolve_days` | P01 | BRD | Y |
| `kyc.kyb.refresh_cadence` | P01 | PLT | Y |
| `kyc.kyb.review_sla_hours` | P01 | PLT | N |
| `kyc.level_validity_months` | P01 | PLT | Y |
| `kyc.min_level.<role>` | P01 | TEN (≥ platform floor) | Y |
| `kyc.name_match.threshold.<purpose>` | P01 | PLT | Y |
| `kyc.pan.vendor.enabled` | P01 | PLT | Y |
| `kyc.professional.reverify_months` | P01 | PLT | Y |
| `kyc.professional.verification_desk` | P01 | PLT | Y |
| `kyc.rights.internal_sla_days` | P01 | PLT | Y |

### `org` (4 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `org.context.colour_band` | P02 | TEN | N |
| `org.department_template` | P02 | TEN | N |
| `org.dept_head.can_manage_members` | P02 | TEN | Y |
| `org.levels_enabled` | P02 | TEN | N |

### `wf` (9 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `wf.away.escalation_hours` | P02 | TEN | N |
| `wf.doa.apply_to_pending_default` | P02 | TEN | N |
| `wf.mc.<action>.approvals_required` | P02 | TEN | Y |
| `wf.mc.<action>.min_aal` | P02 | TEN (≥ platform) | Y |
| `wf.mc.<action>.mode` | P02 | TEN (≥ platform mode) | Y (LOCKED action `cfg.mc_policy.change`) |
| `wf.mc.payment_threshold_inr` | P02 | TEN | Y |
| `wf.mc.request_expiry_working_days` | P02 | TEN | N |
| `wf.mc.solo_owner.cooling_off_hours` | P02 | PLT | Y |
| `wf.sod.agent_sponsor_cannot_check` | P02 | TEN | Y |

### `msg` (1 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `msg.paste_guard_similarity` | P07 | PLT | N |

### `dms` (40 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `dms.aadhaar.mask_at_ingest` | P04 | PLT | — |
| `dms.channel.email_in.enabled` | P04 | TEN | N |
| `dms.channel.whatsapp_in.enabled` | P04 | PLT→TEN | Y |
| `dms.checkout.max_hours` | P04 | TEN | N |
| `dms.classify.auto_apply_threshold` | P04 | TEN | N |
| `dms.closure.grace_days` | P04 | PLT | Y |
| `dms.coedit.keep_working_copy` | P04 | TEN | N |
| `dms.coedit.provider` | P04 | TEN | N |
| `dms.dataroom.enabled` | P04 | PLN | — |
| `dms.delete.bulk_threshold` | P04 | TEN | Y |
| `dms.digilocker.retain_copy.enabled` | P04 | PLT | Y |
| `dms.embedded_editor.enabled` | P04 | PLT | Y |
| `dms.health.initials_every_page` | P04 | TEN | N |
| `dms.health.rule_pack_version` | P04 | PLT | Y |
| `dms.intake.duplicate_policy` | P04 | TEN | N |
| `dms.intake.max_zip_gb` | P04 | PLN | Y |
| `dms.naming.pattern.<doc_type>` | P04 | TEN | N |
| `dms.nominee.inactivity_days` | P04 | USR | N |
| `dms.offline.blocked_classes` | P04 | TEN | N |
| `dms.offline.enabled` | P04 | TEN | N |
| `dms.offline.max_age_days` | P04 | TEN | N |
| `dms.originals.retention_years` | P00 | TEN | N |
| `dms.quota.gb` | P04 | PLN | Y |
| `dms.recycle.retention_days` | P04 | TEN | N |
| `dms.reminder.offsets.<doc_type>` | P04 | TEN/USR | N |
| `dms.retention.class_overrides` | P04 | TEN | Y |
| `dms.search.semantic.enabled.<lang>` | P04 | PLT | Y |
| `dms.share.always_current_allowed` | P04 | TEN | N |
| `dms.share.confidential_legal_needs_checker` | P04 | TEN | Y |
| `dms.share.default_access_mode` | P04 | TEN | N |
| `dms.share.default_expiry_days` | P04 | TEN/USR | N |
| `dms.share.max_expiry_days` | P04 | PLN | Y |
| `dms.share.require_otp` | P04 | PLT | — |
| `dms.share.watermark_default` | P04 | TEN | N |
| `dms.upload.allow_macro_office` | P00 | TEN | N |
| `dms.upload.allowed_types` | P04 | PLT | Y |
| `dms.upload.max_mb` | P00 | PLT (tenants may lower) | N |
| `dms.views.pack_version` | P04 | PLT | Y |
| `dms.views.tenant_overlay` | P04 | TEN | Y (company) |
| `dms.views.year_basis` | P04 | TEN | N |

### `dix` (21 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `dix.bsa63.enabled` | P05 | PLT | Y |
| `dix.chat.mask_nonparty_numbers` | P05 | TEN | Y |
| `dix.confidence.high_min` | P05 | PLT | Y |
| `dix.confidence.vision_cer_high_max` | P05 | PLT | Y |
| `dix.credits.confirm_above` | P05 | USR | N |
| `dix.engine.<id>.enabled` | P05 | PLT | N (kill) / Y (enable) |
| `dix.eval.max_regression_pct` | P05 | PLT | Y |
| `dix.extract.auto_propose_on_upload` | P05 | TEN | N |
| `dix.glossary.tenant_overlay` | P05 | TEN | N |
| `dix.glossary.version` | P05 | PLT | Y |
| `dix.lid.min_confidence_set` | P05 | PLT | Y |
| `dix.mt.backtranslation.min_cosine` | P05 | PLT | Y |
| `dix.mt.backtranslation.required_for` | P05 | PLT | Y |
| `dix.mt.regional_cloud.enabled` | P05 | PLT | Y |
| `dix.redact.auto_card_numbers` | P05 | TEN | N |
| `dix.route.regional_cloud.enabled` | P05 | PLT | Y |
| `dix.route.table_version` | P05 | PLT | Y |
| `dix.route.tenant_restrictions` | P05 | TEN | Y |
| `dix.tier.<lang>.<task>` | P05 | PLT | Y |
| `dix.typecopy.show_anchors_in_print` | P05 | TEN/USR | N |
| `dix.typecopy.verification_policy` | P05 | TEN | Y |

### `tpl` (14 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `tpl.authoring.auto_noindex_unreviewed` | P06 | PLT | Y |
| `tpl.authoring.golden_tests_min` | P06 | PLT | Y |
| `tpl.authoring.review_cycle_months` | P06 | PLT | Y |
| `tpl.authoring.two_person_publish` | P06 | PLT | — |
| `tpl.backlog.block_publish_if_outdated` | P06 | PLT | — |
| `tpl.backlog.sla_days_copied` | P06 | PLT | Y |
| `tpl.backlog.sla_days_outdated_law` | P06 | PLT | Y |
| `tpl.health.max_review_return_rate` | P06 | PLT | N |
| `tpl.health.min_completion_rate` | P06 | PLT | N |
| `tpl.library.public_catalogue_enabled` | P06 | PLT | Y |
| `tpl.tenant.department_template_sets` | P06 | DEP | Y |
| `tpl.tenant.one_sided_allowed` | P06 | TEN | Y |
| `tpl.tenant.private_templates_enabled` | P06 | PLN | Y |
| `tpl.tenant.publish_maker_checker` | P06 | TEN | — |

### `drf` (19 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `drf.ai.credits.first_draft` | P06 | PLT | Y |
| `drf.ai_custom.company_self_review_roles` | P06 | TEN | Y |
| `drf.ai_custom.enabled` | P06 | PLN → TEN | N |
| `drf.ai_custom.unreviewed_download` | P06 | PLT | Y |
| `drf.analytics.min_cohort` | P06 | PLT | Y |
| `drf.autosave_seconds` | P06 | PLT | N |
| `drf.bilingual.governing_language_default` | P06 | TEN / USR | N |
| `drf.draft.retention_days_anonymous` | P06 | PLT | Y |
| `drf.export.house_style` | P06 | ENT | N |
| `drf.export.pdfa_default` | P06 | TEN | N |
| `drf.language.ui_languages` | P06 | BRD | Y |
| `drf.preview.watermark_text` | P06 | BRD | N |
| `drf.review.accept_sla_hours` | P06 | PLT | N |
| `drf.review.upsell_enabled` | P06 | BRD | N |
| `drf.template.ai_prefill.companies` | P06 | TEN | N |
| `drf.template.ai_prefill.individuals` | P06 | PLT | Y |
| `drf.template.anonymous_start` | P06 | BRD | Y |
| `drf.template.export_price_inr` | P06 | PLN | Y (NN-18 price) |
| `drf.template.free_clean_exports_per_month` | P06 | PLN | Y |

### `clm` (31 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `clm.approval.reapprove_on_change` | P07 | TEN | Y |
| `clm.approval.sla_hours` | P07 | TEN | N |
| `clm.approval.stepup_value_inr` | P07 | TEN | Y |
| `clm.bulk.max_rows` | P07 | PLN | N |
| `clm.coedit.delete_temp_copy` | P07 | TEN | N |
| `clm.coedit.provider` | P07 | TEN | Y |
| `clm.coedit.wopi_enabled` | P07 | PLT | Y |
| `clm.dealroom.download_default` | P07 | TEN | N |
| `clm.dealroom.guest_can_add_members` | P07 | TEN | N |
| `clm.dealroom.guest_link_ttl_days` | P07 | TEN | N |
| `clm.dealroom.guest_otp_required` | P07 | PLT | — |
| `clm.dealroom.invite_reminders_max` | P07 | PLT | Y |
| `clm.dealroom.nda_clickthrough_default` | P07 | TEN | N |
| `clm.dealroom.watermark_default` | P07 | TEN | N |
| `clm.doa.matrix` | P07 | ENT | **Y** (NN-18) |
| `clm.intake.allowed_sender_domains` | P07 | TEN | Y |
| `clm.intake.channels` | P07 | TEN | N |
| `clm.intake.email_alias` | P07 | TEN | N |
| `clm.intake.self_serve_types` | P07 | TEN | Y |
| `clm.intake.sla_hours.<type>` | P07 | TEN | N |
| `clm.lock.require_all_party_confirmation` | P07 | PLT | — |
| `clm.negotiation.reject_reason_required` | P07 | TEN | N |
| `clm.negotiation.round_nudge_days` | P07 | TEN | N |
| `clm.negotiation.silent_edit_detection` | P07 | PLT | — |
| `clm.notify.whatsapp_enabled` | P07 | TEN | Y |
| `clm.obligations.extraction_enabled` | P07 | TEN | N |
| `clm.obligations.verify_required` | P07 | PLT | — |
| `clm.redline.ai_author_label` | P07 | PLT | — |
| `clm.redline.ai_suggestions_enabled` | P07 | PLN → TEN | N |
| `clm.redline.normalise_quotes_dashes` | P07 | TEN | N |
| `clm.repository.fiscal_year_start` | P07 | ENT | N |

### `sgn` (41 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `sgn.bsa63.enabled` | P08 | PLT | Y |
| `sgn.accessibility.assisted_signing.enabled` | P08 | TEN | N |
| `sgn.accessibility.helper_declaration_required` | P08 | PLT (locked) | — |
| `sgn.accessibility.witness_required_above_inr` | P08 | TEN | Y |
| `sgn.accessibility.extended_session_minutes` | P08 | PLT | N |
| `sgn.bulk.max_rows` | P08 | PLN | Y |
| `sgn.chat.enabled` | P08 | TEN | N |
| `sgn.credits.charge_on_success_only` | P08 | PLT | Y |
| `sgn.credits.counterparty_pays_allowed` | P08 | TEN | N |
| `sgn.dsc.batch_max` | P08 | PLT | N |
| `sgn.duty.calculator.mode` | P08 | PLT | Y |
| `sgn.e_acceptance.enabled` | P08 | TEN | N |
| `sgn.e_acceptance.max_value_inr` | P08 | TEN | Y |
| `sgn.eligibility.rule_set_version` | P08 | PLT | Y |
| `sgn.esign.account_based_enabled` | P08 | PLT | Y |
| `sgn.esign.biometric_enabled` | P08 | PLT | Y |
| `sgn.esign.face_enabled` | P08 | PLT | Y |
| `sgn.esign.max_attempts` | P08 | PLT | N |
| `sgn.estamp.state.<code>.enabled` | P08 | PLT | Y |
| `sgn.evidence.append_certificate_incremental` | P08 | TEN | N |
| `sgn.evidence.retention_years_min` | P08 | PLT | Y |
| `sgn.formalities.waiver_roles` | P08 | TEN | Y |
| `sgn.identity.name_match_threshold` | P08 | TEN | Y |
| `sgn.identity.on_mismatch` | P08 | TEN | Y |
| `sgn.ltv.retimestamp_before_days` | P08 | PLT | N |
| `sgn.org_seal.enabled` | P08 | PLT | Y |
| `sgn.provider.degraded_threshold` | P08 | PLT | N |
| `sgn.provider.licence_alert_days` | P08 | PLT | N |
| `sgn.provider.preferred` | P08 | TEN | N |
| `sgn.public_verify.enabled` | P08 | PLT | N |
| `sgn.request.approval_threshold_inr` | P08 | TEN | Y |
| `sgn.request.default_expiry_days` | P08 | TEN / PLT | N / Y |
| `sgn.request.reminder_days` | P08 | TEN | N |
| `sgn.signer_controls.selfie` | P08 | TEN | Y |
| `sgn.stamp.duty_payment_route` | P08 | PLT | Y |
| `sgn.stamp.number_on_every_page` | P08 | TEN | N |
| `sgn.stamp.physical_with_esign.enabled` | P08 | PLT | Y |
| `sgn.stamp.purchase_checker_threshold_inr` | P08 | TEN | Y |
| `sgn.stamp.required_before_sign` | P08 | PLT | — |
| `sgn.whitelabel.full.enabled` | P08 | PLT | Y |
| `sgn.witness.electronic_allowed` | P08 | TEN | N |

### `ai` (23 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `ai.batch.window` | P09 | PLT | N |
| `ai.cache.enabled` | P09 | PLT | N |
| `ai.credits.plan_allowance` | P09 | PLN | Y |
| `ai.credits.rate_table` | P09 | PLT | Y [OWNER TO SET] |
| `ai.languages.enabled` | P09 | PLT | Y (per language after eval) |
| `ai.marketplace_suggestions.enabled` | P09 | TEN | N |
| `ai.mcp_client.enabled` | P09 | TEN | Y |
| `ai.mcp_server.client_basis` | P09 | TEN | Y |
| `ai.mcp_server.enabled` | P09 | TEN | Y |
| `ai.metering.retainer_billing` | P09 | TEN | Y |
| `ai.models.pins` | P09 | PLT | Y + eval gate |
| `ai.notebooks.audio_overview_enabled` | P09 | PLT | Y |
| `ai.plan.auto_approve_read_only` | P09 | TEN | N |
| `ai.public_widget.daily_credits` | P09 | BRD | N |
| `ai.qrg.internal_reviewers_enabled` | P09 | TEN | Y |
| `ai.qrg.sla_hours` | P09 | PLT | Y |
| `ai.retention.content_days` | P09 | TEN | Y |
| `ai.routing.india_only_all_classes` | P09 | TEN | Y (to false) / N (to true) |
| `ai.routing.policy` | P09 | PLT | Y |
| `ai.speech.jio_enabled` | P09 | PLT | Y (NN-38) |
| `ai.speech.provider_by_language` | P09 | PLT | Y |
| `ai.user.language` | P09 | USR | N |
| `ai.voice_agent.haptik_enabled` | P09 | PLT | Y (NN-38) |

### `agt` (17 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `agt.autonomy.agent.<code>` | P13 | TEN | Y |
| `agt.autonomy.agent.<id>` | P09 | TEN | Y (raise) |
| `agt.autonomy.agent.AGT_LITIGATION_CLERK` | P11 | TEN | Y |
| `agt.autonomy.agent.AGT_ORDER_DIGEST` | P11 | TEN | Y |
| `agt.autonomy.agent.AGT_TM_WATCH` | P12 | TEN | Y |
| `agt.autonomy.plan_ceiling` | P09 | PLN | Y |
| `agt.autonomy.platform_ceiling.<code>` | P09 | PLT | Y |
| `agt.budget.monthly.<id>` | P09 | TEN | Y above `single_approval_limit` |
| `agt.budget.single_approval_limit` | P09 | TEN | Y |
| `agt.digest.channels` | P09 | USR | N |
| `agt.digest.time` | P09 | USR | N |
| `agt.induction.supervised_days` | P09 | TEN | N |
| `agt.killswitch.drill_frequency_days` | P09 | TEN | N |
| `agt.memory.auto_learn` | P09 | TEN / USR | N |
| `agt.missions.enabled` | P09 | PLN | Y |
| `agt.send_plan.mode` | P09 | PLT | Y [OWNER/COUNSEL] |
| `agt.undo.window_hours` | P09 | TEN | N |

### `pld` (16 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `pld.affidavit.similarity_min` | P10 | PLT | Y |
| `pld.court_fee.<state>.enabled` | P10 | PLT | Y |
| `pld.criminal.review_required` | P10 | PLT | — |
| `pld.legal_aid.prompt_enabled` | P10 | BRD | N |
| `pld.limitation.show_advisory_dates` | P10 | PLT | Y |
| `pld.notice.bulk_max_rows` | P10 | PLN | N |
| `pld.notice.whatsapp_dispatch` | P10 | PLT | — |
| `pld.oath.remote.<forum>` | P10 | PLT | Y |
| `pld.pack.max_mb_default` | P10 | PLT | Y |
| `pld.pack.pdf_standard` | P10 | TEN | N |
| `pld.profiles.allow_unverified_export` | P10 | PLT | Y |
| `pld.profiles.tenant_custom_enabled` | P10 | PLN | Y |
| `pld.review.required_for_ai_individuals` | P10 | PLT | — |
| `pld.review.required_for_company_dispatch` | P10 | TEN | Y |
| `pld.transition.pre_2024_toggle_enabled` | P10 | PLT | Y |
| `pld.translation.convenience_allowed.<profile>` | P10 | PLT | Y |

### `lit` (28 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `lit.alerts.whatsapp.enabled` | P11 | TEN | N |
| `lit.calendar.include_titles` | P11 | DEP | N |
| `lit.cause_list.match_time` | P11 | PLT | Y |
| `lit.clocks.internal_buffer_days` | P11 | TEN | N |
| `lit.clocks.reminder_offsets_days` | P11 | TEN ↑ | N |
| `lit.clocks.rule_set` | P11 | PLT | Y (NN-30) |
| `lit.counsel_panel.portal_invoices` | P11 | TEN | N |
| `lit.court_data.failover_error_rate` | P11 | PLT | Y |
| `lit.court_data.lookahead_days` | P11 | TEN | N |
| `lit.court_data.manual_cooldown_minutes` | P11 | PLT | Y |
| `lit.court_data.official_api_client_credentials` | P11 | ENT | Y |
| `lit.court_data.recent_hours` | P11 | TEN ↓ | N |
| `lit.court_data.sync_time` | P11 | PLT | Y |
| `lit.exposure.frequency` | P11 | ENT | Y |
| `lit.exposure.open_days_before_qe` | P11 | ENT | N |
| `lit.exposure.pct_guidance_bands` | P11 | ENT | Y |
| `lit.hearing.escalate_after_hours` | P11 | TEN | N |
| `lit.hearing.outcome_due_hours` | P11 | TEN | N |
| `lit.import.checker_threshold_rows` | P11 | TEN | Y |
| `lit.import.undo_hours` | P11 | TEN | N |
| `lit.matter.dormant_days` | P11 | TEN | N |
| `lit.matter.lessons_required` | P11 | TEN | N |
| `lit.matter.required_fields.<type>` | P11 | TEN | N |
| `lit.party_watch.enabled` | P11 | TEN | Y |
| `lit.risk.weights` | P11 | TEN | Y |
| `lit.sor.mode` | P11 | ENT | Y |
| `lit.spend.alert_pct` | P11 | TEN | N |
| `lit.spend.invoice_validation_strict` | P11 | TEN | Y |

### `ipm` (15 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `ipm.data.recent_days` | P12 | TEN | N |
| `ipm.data.stale_days` | P12 | TEN ↓ | N |
| `ipm.extract.min_confidence` | P12 | PLT | Y |
| `ipm.fees.table_version` | P12 | PLT | Y |
| `ipm.filing.checker_required` | P12 | TEN | Y |
| `ipm.flag.logo_similarity` | P12 | PLT | Y |
| `ipm.nice.edition` | P12 | PLT | Y |
| `ipm.plan.watch_limit` | P12 | PLN | Y |
| `ipm.refresh.prompt_days` | P12 | TEN | N |
| `ipm.reminders.<clock_code>` | P12 | TEN ↑ | N |
| `ipm.use_evidence.reminder_month` | P12 | TEN | N |
| `ipm.watch.auto_dismiss_below` | P12 | TEN | Y |
| `ipm.watch.auto_fetch.enabled` | P12 | PLT | Y |
| `ipm.watch.escalate_days_before_deadline` | P12 | TEN | N |
| `ipm.watch.journal_source` | P12 | PLT | Y |

### `gov` (10 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `gov.board.notice_days_charter` | P13 | ENT ↑ | Y |
| `gov.circular.response_days` | P13 | ENT | Y |
| `gov.flag.offline_pack` | P13 | ENT | Y |
| `gov.meeting.transcription` | P13 | ENT | Y |
| `gov.minutes.comment_days` | P13 | PLT | Y |
| `gov.pack.interested_director_access` | P13 | ENT | N |
| `gov.portal.download` | P13 | ENT | N |
| `gov.rulepack.overlay_status` | P13 | PLT | Y |
| `gov.rulepack.overlays` | P13 | ENT | Y |
| `gov.sod.hard_block_rules` | P13 | ENT | Y |

### `hr` (6 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `hr.attendance.geo_at_checkin` | P13 | ENT | Y |
| `hr.attendance.methods` | P13 | ENT | N |
| `hr.leave.auto_approval_rules` | P13 | ENT | N |
| `hr.payroll.checker_required` | P13 | ENT | — |
| `hr.posh.ai_assist.enabled` | P13 | ENT | Y |
| `hr.posh.enabled` | P13 | ENT | N |

### `lgo` (11 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `lgo.calendar.include_titles` | P13 | DEP | N |
| `lgo.digest.board_monthly.enabled` | P13 | TEN | Y |
| `lgo.digest.weekly.enabled` | P13 | TEN | N |
| `lgo.doa.matrix` | P13 | ENT | Y |
| `lgo.licences.default_lead_days` | P13 | ENT | N |
| `lgo.routing.table` | P13 | TEN | Y |
| `lgo.selfservice.enabled` | P13 | TEN | Y |
| `lgo.selfservice.limits` | P13 | TEN | Y |
| `lgo.sla.business_calendar` | P13 | ENT | N |
| `lgo.sla.policies` | P13 | TEN | Y |
| `lgo.template.adopted` | P13 | ENT | Y |

### `bsv` (13 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `bsv.assignment.ordering` | P14 | PLT | Y |
| `bsv.attest.sourcing_mode` | P14 | PLT | Y |
| `bsv.catalogue.enabled_groups` | P14 | BRD | Y |
| `bsv.dataroom.download_default` | P14 | TEN | N |
| `bsv.deliverable.auto_accept_days` | P14 | TEN | N |
| `bsv.fees.govt_fee_mode` | P14 | PLT | Y |
| `bsv.fees.variance_alert_pct` | P14 | PLT | Y |
| `bsv.order.approval_threshold_inr` | P14 | TEN | Y |
| `bsv.order.max_resubmissions` | P14 | PLT | N |
| `bsv.order.who_can_buy` | P14 | TEN | N |
| `bsv.renewal.reminder_days` | P14 | TEN | N |
| `bsv.rework.free_if_lawdocs_error` | P14 | PLT | Y |
| `bsv.startup.bundle_discount_pct` | P14 | PLT | Y |

### `tax` (6 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `tax.eri.enabled` | P14 | PLT | Y |
| `tax.gst.route` | P14 | TEN | N |
| `tax.notice.reminder_days` | P14 | TEN | N |
| `tax.review.required_for` | P14 | PLT | Y |
| `tax.rulepack.block_unverified` | P14 | PLT | Y |
| `tax.year.label_mode` | P14 | USR | N |

### `chp` (23 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `chp.ads.enabled` | P15 | BRD | Y |
| `chp.brand.enabled` | P15 | PLT | Y |
| `chp.case.abandon_days` | P15 | BRD | N |
| `chp.challan.reminder_days` | P15 | USR | N |
| `chp.conflict.fail_mode` | P15 | PLT | Y |
| `chp.conflict.key_rotation_days` | P15 | PLT | Y |
| `chp.conflict.on_hit_policy` | P15 | BRD | Y |
| `chp.copy.banned_phrases` | P15 | BRD | Y |
| `chp.deadline.alert_days` | P15 | USR | N |
| `chp.deadline.transit_days` | P15 | BRD | Y |
| `chp.fee.flat_packs.enabled` | P15 | BRD | Y |
| `chp.fee.success.enabled` | P15 | BRD | Y |
| `chp.fee.success_cap_inr` | P15 | BRD | Y |
| `chp.fee.success_cap_pct` | P15 | BRD | Y |
| `chp.isolation.dedicated_cluster` | P15 | PLT | Y |
| `chp.lokadalat.calendar` | P15 | BRD (content) | Y |
| `chp.representation_matrix` | P15 | PLT (content) | Y |
| `chp.retention.third_party_months` | P15 | BRD | Y |
| `chp.vertical.vehicle.brand_surface` | P15 | PLT | Y |
| `chp.wall.advocate_cooling_months` | P15 | BRD | Y |
| `chp.withdrawal.cooling_hours` | P15 | BRD | Y |

### `mkp` (32 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `mkp.acceptance.deemed_days` | P16 | PLT | Y |
| `mkp.assignment.accept_window_hours` | P16 | PLT | N |
| `mkp.category.adr.equator_link` | P16 | PLT | Y |
| `mkp.consult.followup_hours` | P16 | PLT | N |
| `mkp.consult.no_show_minutes` | P16 | PLT | N |
| `mkp.contract.clickwrap_max_value` | P16 | PLT | Y |
| `mkp.directory.advocates.enabled` | P16 | PLT | Y |
| `mkp.disputes.show_adr_options` | P16 | PLT | Y |
| `mkp.disputes.supplier_response_bd` | P16 | PLT | N |
| `mkp.grievance.ack_hours` | P16 | PLT | — |
| `mkp.intake.retention_days` | P16 | PLT | Y |
| `mkp.model.m2.enabled` | P16 | PLT | Y |
| `mkp.model.m3.enabled` | P16 | PLT | Y |
| `mkp.offer.validity_days` | P16 | PLT | N |
| `mkp.platform_fee.flat_inr` | P16 | PLT | Y |
| `mkp.practitioner.post_close_access_days` | P16 | PLT | Y |
| `mkp.price_guardrail.<category>` | P16 | PLT | Y |
| `mkp.profession.<code>.buyer_platform_fee_mode` | P16 | PLT | Y |
| `mkp.profession.<code>.commission_pct_allowed` | P16 | PLT | Y |
| `mkp.profession.<code>.listing_mode` | P16 | PLT | Y |
| `mkp.profession.<code>.ratings_display_allowed` | P16 | PLT | Y |
| `mkp.providers.third_party.enabled` | P16 | PLT | Y |
| `mkp.public.enabled` | P16 | PLT | Y |
| `mkp.qa.review_required` | P16 | PLT | Y |
| `mkp.retainer.hour_rollover_months` | P16 | PLT | Y |
| `mkp.retainer.show_staff_names` | P16 | TEN | N |
| `mkp.retainer.sla_credit_pct` | P16 | PLT | Y |
| `mkp.sponsored.enabled` | P16 | PLT | — |
| `mkp.tenant.contextual_offers` | P16 | TEN / USR | N |
| `mkp.tenant.purchase_approval_threshold` | P16 | TEN | N |
| `mkp.tenant.who_can_buy` | P16 | TEN | N |
| `mkp.user.service_suggestions` | P16 | USR | N |

### `aca` (4 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `aca.cache_max_age_days` | P16 | PLT | N |
| `aca.certificate_import.enabled` | P16 | TEN | N |
| `aca.display_name` | P16 | BRD | Y |
| `aca.feed.mode` | P16 | PLT | Y |

### `bil` (20 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `bil.billing_port.mode` | P17 | PLT | Y |
| `bil.credits.allowance_rollover` | P17 | PLN | Y |
| `bil.credits.consumption_order` | P17 | TEN | N |
| `bil.credits.pack_validity_months` | P17 | PLT | Y |
| `bil.credits.user_cap.<type>` | P17 | TEN | N |
| `bil.exit.read_only_days` | P17 | PLT | — |
| `bil.family.allowance_mode` | P17 | TEN (Personal) | N |
| `bil.mobile.purchase_mode` | P17 | PLT | Y |
| `bil.notifications.recipients.<type>` | P17 | TEN | N |
| `bil.pricing.display_mode` | P17 | BRD | Y |
| `bil.pricing.monthly_uplift_pct` | P17 | PLT | Y |
| `bil.refund.annual_prorata_window_days` | P17 | PLT | Y |
| `bil.refund.personal_cooling_off_days` | P17 | PLN | Y |
| `bil.stream.<code>.enabled` | P17 | PLT / BRD / segment | Y |
| `bil.tenant.overage_opt_in` | P17 | TEN | N |
| `bil.tenant.po_required` | P17 | TEN | N |
| `bil.tenant.purchase_approval_threshold` | P17 | TEN | N |
| `bil.trial.default_days` | P17 | PLN | Y |
| `bil.trial.extension_max_days_without_checker` | P17 | PLT | Y |
| `bil.upsell.dismiss_days` | P17 | USR | N |

### `sav` (6 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `sav.benchmark.max_age_days` | P17 | PLT | Y |
| `sav.enabled` | P17 | TEN | N |
| `sav.marketing.min_workspaces` | P17 | PLT | — |
| `sav.penalty_rule.max_unverified_days` | P17 | PLT | Y |
| `sav.share_with_rm` | P17 | TEN | N |
| `sav.user.show_estimates` | P17 | USR | N |

### `sdc` (28 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `sdc.access_review.cadence_months` | P18 | PLT | Y |
| `sdc.anomaly.downloads_per_hour` | P18 | PLT | Y |
| `sdc.breakglass.max_hours` | P18 | PLT | Y |
| `sdc.calendar.sync_detail_level` | P18 | PLT | Y |
| `sdc.client_visibility.metrics` | P18 | TEN | N |
| `sdc.delivery.agent_runs.enabled` | P18 | TEN | Y |
| `sdc.email.bridge_enabled` | P18 | TEN | N |
| `sdc.email.outbound_mode` | P18 | PLT | Y |
| `sdc.grants.alternate_approvers` | P18 | TEN | Y |
| `sdc.grants.engagement_grace_days` | P18 | PLT | Y |
| `sdc.grants.expiry_notice_days` | P18 | PLT | N |
| `sdc.grants.include_sealed_classes` | P18 | TEN | Y |
| `sdc.grants.max_months.implementation` | P18 | PLT | Y |
| `sdc.grants.max_months.retainer` | P18 | PLT | Y |
| `sdc.grants.standing_authorisation` | P18 | TEN | Y |
| `sdc.grants.support_session_max_hours` | P18 | PLT | Y |
| `sdc.health.weights` | P18 | PLT | Y |
| `sdc.masterdata.recovery_hold_hours` | P18 | PLT | Y |
| `sdc.masterdata.review_window_days` | P18 | PLT | Y |
| `sdc.masterdata.sla_hours` | P18 | PLT | Y |
| `sdc.meetings.recording_default` | P18 | TEN | N |
| `sdc.notes.client_visible` | P18 | TEN | N |
| `sdc.reminders.max_per_day` | P18 | PLT | N |
| `sdc.rm.backup_required_for` | P18 | PLT | Y |
| `sdc.rm.max_clients` | P18 | PLT | Y |
| `sdc.session.idle_timeout_min` | P18 | PLT | N |
| `sdc.sla.alert_thresholds_pct` | P18 | PLT | N |
| `sdc.time.edit_window_days` | P18 | PLT | Y |

### `cvl` (10 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `cvl.allowed_hours` | P18 | TEN | N |
| `cvl.anomaly.reveals_per_hour` | P18 | PLT | Y |
| `cvl.blocked_types` | P18 | PLT (locked) | — |
| `cvl.client_only_types` | P18 | PLT | Y |
| `cvl.grant.max_days` | P18 | TEN | Y |
| `cvl.notify_mode` | P18 | TEN | N |
| `cvl.per_reveal_approval.default` | P18 | TEN | Y |
| `cvl.personal_workspace_enabled` | P18 | PLT | Y |
| `cvl.reveal_on_mobile` | P18 | TEN | Y |
| `cvl.reveal_seconds` | P18 | PLT | Y |

### `int` (40 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `int.a2a.enabled` | P09 | PLT | Y (after Appendix Y approval) |
| `int.adapter.<adapter_id>.enabled` | P19 | PLT | Y |
| `int.auth.access_token_ttl_seconds` | P19 | PLT | Y |
| `int.auth.api_keys.production_scopes` | P19 | PLT | Y |
| `int.auth.client_max_validity_months` | P19 | PLT | Y |
| `int.auth.secret_rotation_days` | P19 | PLT | Y |
| `int.automation.data_class_max` | P19 | TEN | Y |
| `int.automation.platforms_allowed` | P19 | TEN | Y |
| `int.chp.ecosystem_clients.allowlist` | P19 | BRD | — |
| `int.connector.<connector_id>.tenant_enabled` | P19 | TEN | Y (on) |
| `int.devportal.sandbox.auto_reset_hours` | P19 | PLT | N |
| `int.dlq.replay_requires_checker` | P19 | PLT | — |
| `int.dlq.retention_days` | P19 | PLT | Y |
| `int.eco.equator.referral.enabled` | P19 | TEN | Y |
| `int.eco.equator.show_alternatives` | P19 | PLT | — |
| `int.eco.finbyx.litigation_projection.enabled` | P11/P19 | TEN | Y |
| `int.eco.finbyx.signing_handoff.enabled` | P19 | TEN | Y |
| `int.eco.ldc.projections.enabled` | P11/P19 | TEN | Y |
| `int.eco.udofin.deposit.default_folder` | P19 | USR | N |
| `int.eco.udofin.deposit.enabled` | P19 | PLT | Y |
| `int.eco.v12_contracts.enabled` | P19 | PLT | Y |
| `int.ecosystem.proposed_subjects.enabled` | P00 | PLT | Y |
| `int.esign.api_initiation.enabled` | P19 | TEN | Y |
| `int.esign.hosted_ceremony.framing_allowed` | P19 | PLT | — |
| `int.gateway.public_api.enabled` | P19 | PLT | Y |
| `int.health.alert_recipients` | P19 | TEN | N |
| `int.kill.storage_<provider>` | P20 | PLT/TEN | Release Y |
| `int.partner.individual_bulk.enabled` | P19 | PLT | Y |
| `int.partner.onboarding.invite_expiry_days` | P19 | PLT | N |
| `int.partner.onboarding.kyb_prefill.enabled` | P19 | PLT | Y |
| `int.partner.onboarding.max_batch_rows` | P19 | PLT | Y |
| `int.quota.soft_block_at_pct` | P19 | PLN | Y |
| `int.ratelimit.override` | P19 | TEN | Y |
| `int.ratelimit.tier` | P19 | PLN | Y |
| `int.sharing_ledger.user_visible` | P19 | PLT | — |
| `int.status_page.enabled` | P19 | PLT | N |
| `int.webhooks.auto_pause_after_hours` | P19 | PLT | N |
| `int.webhooks.data_class_max_default` | P19 | TEN | Y |
| `int.webhooks.max_endpoints` | P19 | PLN | Y |
| `int.webhooks.retry_window_hours` | P19 | PLT | Y |

### `web` (31 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `web.authors.advocate_bio_mode` | P21 | PLT | — |
| `web.brand.consumer_help.enabled` | P21 | PLT | Y |
| `web.brand.host_map` | P21 | PLT | Y |
| `web.city_pages.enabled` | P21 | BRD | Y |
| `web.cms.docx_import.max_mb` | P21 | PLT | N |
| `web.cms.folder_category_map` | P21 | BRD | Y |
| `web.cms.legal_review.auto_types` | P21 | PLT | Y |
| `web.consent.categories` | P21 | BRD | Y |
| `web.contact.public_phone` | P21 | BRD | Y |
| `web.cwv.budgets` | P21 | PLT | Y |
| `web.drafter.anon_runs_per_day` | P21 | BRD | N |
| `web.experiments.enabled` | P21 | BRD | N |
| `web.facts.max_age_days` | P21 | PLT | Y |
| `web.host.canonical` | P00/P21 | BRD | Y |
| `web.indexnow.enabled` | P21 | BRD | N |
| `web.js_budget_kb` | P21 | PLT | Y |
| `web.kill.drafter` | P21 | BRD | N (audited) |
| `web.kill.lead_capture` | P21 | BRD | N (audited) |
| `web.kill.video_embeds` | P21 | BRD | N (audited) |
| `web.kill.landing_pages` | P21 | BRD | N (audited) |
| `web.lead.form.max_fields` | P21 | BRD | N |
| `web.lead.local_retention_days` | P21 | PLT | Y |
| `web.llms_txt.enabled` | P21 | BRD | N |
| `web.locale.<code>.sections` | P21 | BRD | Y |
| `web.mt.publish_requires_human_review` | P21 | PLT | — |
| `web.plagiarism.max_similarity_pct` | P21 | PLT | Y |
| `web.redirects.freeze_days_before_cutover` | P00 | PLT | N |
| `web.render.revalidate_seconds` | P21 | PLT | N |
| `web.review.auto_noindex_without_reviewer` | P21 | PLT | — |
| `web.review.max_age_days` | P21 | PLT | Y |
| `web.schema.faqpage_mode` | P21 | BRD | N |
| `web.state_variant.min_distinct_facts` | P21 | PLT | Y (checker `PLT_LEGAL_REVIEWER`) |
| `web.testimonials.advocate_related_allowed` | P21 | PLT | — |
| `web.video.embed_host` | P21 | PLT | Y |

### `hlp` (9 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `hlp.a11y.feedback_ack_hours` | P21 | PLT | Y |
| `hlp.a11y.feedback_resolve_days` | P21 | PLT | Y |
| `hlp.article.stale_after_days` | P21 | PLT | N |
| `hlp.inline.explanations` | P21 | USR | N |
| `hlp.tenant_notes.enabled` | P21 | TEN | N |
| `hlp.tours.whats_new_per_session` | P21 | PLT | N |
| `hlp.tutorial.screenshot_diff_threshold_pct` | P21 | PLT | N |
| `hlp.video.isl_required_for_core` | P21 | PLT | Y |
| `hlp.vidhi_help_mode.enabled` | P21 | PLT, TEN | N |

### `rpt` (1 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `rpt.home.default_layout.<role>` | P02 | TEN | N |

### `mob` (25 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| `mob.analytics.enabled` | P22 | PLT | Y |
| `mob.deeplink.invite_expiry_days` | P22 | TEN | N |
| `mob.devices.max_active` | P22 | TEN | N |
| `mob.export.device_save_allowed` | P22 | TEN | Y |
| `mob.integrity.policy` | P22 | PLT | Y |
| `mob.kill.<feature>` | P22 | PLT | N (audited) |
| `mob.lock.background_minutes` | P22 | TEN, USR | N |
| `mob.offline.auto_cache_recent` | P22 | TEN, USR | N |
| `mob.offline.enabled` | P22 | TEN | N |
| `mob.offline.max_days_without_contact` | P22 | TEN | Y |
| `mob.offline.max_mb` | P22 | USR | N |
| `mob.ota.auto_rollback_crash_delta_pp` | P22 | PLT | Y |
| `mob.ota.enabled` | P22 | PLT | Y |
| `mob.push.digest_threshold` | P22 | PLT | N |
| `mob.push.quiet_hours` | P22 | USR | N |
| `mob.release.train_weeks` | P22 | PLT | N |
| `mob.screen.allow_capture_classes` | P22 | TEN | Y |
| `mob.stepup.window_seconds` | P22 | PLT | Y |
| `mob.store.android.digital_sales_mode` | P22 | BRD | Y (build-time) |
| `mob.store.ios.digital_sales_mode` | P22 | BRD | Y (build-time) |
| `mob.upload.wifi_only_over_mb` | P22 | USR | N |
| `mob.version.min_supported` | P22 | PLT (per platform, brand) | Y |
| `mob.version.recommended` | P22 | PLT | N |
| `mob.vidhi.retain_audio` | P22 | USR | N |
| `mob.vidhi.voice_locales` | P22 | PLT | Y |

### `eng` (1 keys)

| Key | Owner | Tier | MC |
|---|---|---|---|
| (retired `eng.logs.retention_days`; duplicate of `eng.logs.retention_days_india`) | — | — | — |

---

## R.15 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-R-01 | Plan limits marked [OWNER TO SET] | [OWNER] with P17 | R6 seeds |
| OI-R-02 | TCCCPR 2026 calling window and pre-declared number rules | P19 | Voice channel OFF |
| OI-R-03 | RB-IOS 2026 clause numbers and filing window; Insurance Ombudsman window | P15 content | Advisory clocks labelled [VERIFY] |
| OI-R-04 | Secretarial Standards paragraph references | P13 content | `SECONDARY_ONLY` labels |
| OI-R-05 | Trade Marks Act timelines (examination reply, opposition, renewal) | P12 content | Advisory clocks |
| OI-R-06 | Registration Act presentation window and State variants for `AGR_REGISTRATION_PENDING` | P08 content | Advisory clock; manual entry |
| OI-R-07 | Anthropic Usage Policy high-risk requirements and effective date (`drf.ai_custom.individual_delivery_mode`) | [OWNER] + [COUNSEL] | `labelled_draft` with paid review offer; switch flag if required |
| OI-R-08 | Naming normalisation found at registry review G4: P18 `wks.*` uses a non-module prefix; P18 kill switches `sdc.breakglass.enabled`, `sdc.email.bridge.global_enabled`, `sdc.delivery.agent_runs.global_enabled`, `cvl.reveal.enabled` do not follow `<module>.kill.<target>`; P11 §9/P12 §9 cite the column `int.connectors.kill_switch_key` instead of the `int.kill.<adapter>` keys | P18, P11, P12 (next `appendix-r-sync`) | Keys registered as named (§R.9.32A, §R.9.31, §R.9.32); aliases added if renamed (§R.1 deprecation rule) |
| OI-R-09 *(v1.1)* | Shared-package prefixes `vidhi.*`, `brand.*`, `cms.*`, `mkt.*`, `fb.*`, `trust.*`, `sec.*`, `ux.*`, `a11y.*`, `tut.*` introduced by the IPB sit outside conventions §4 module codes; the registry lint allow-list is extended accordingly; §R.14 compiled index to be regenerated by script at the next registry review | Pack lead | Keys registered in §R.9.16A, §R.9.35A, §R.9.39A are authoritative until §R.14 is regenerated |
