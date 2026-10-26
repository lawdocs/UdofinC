# Appendix V — Acceptance Tests and UAT Catalogue (binding)

> LawDocs Build Prompt Pack v1.0 · 25 October 2026 · Compiled by X2 from every phase file §12 (`tests/acceptance/pxx/*.feature`), the NN rules (conventions §7), Appendix C click budgets and Appendix U test protocol. The phase files' Gherkin is the detailed acceptance criteria; this appendix is the index the QA lead uses to build the acceptance suites, the NN suite, the journey suite and the UAT plan, and it adds the scenarios needed to close coverage gaps (§V.4).

---

## V.1 How tests are organised

| Suite | Location | Source | Gate |
|---|---|---|---|
| NN suite | `tests/nn/NN-xx_*.spec.ts` | At least one automated test per NN rule; every scenario tagged `@NN-xx` also runs in the NN job | `ci/nn` required on every PR; a failing NN test blocks release (P23) |
| Acceptance | `tests/acceptance/pxx/*.feature` | Phase §12 scenarios, tags `@Pxx-AT-nn` (582 scenarios, §V.8) | Phase exit gate; full run on `rc-*` tags (`ci/e2e-full`) |
| Appendix scenarios | `tests/acceptance/appendix/*.feature` | `@APPV-AT-nn` (§V.4, this appendix) and `@APPO-AT-nn` (Appendix O policies, X-30) | Same as acceptance |
| Journey (click budget) | `tests/journeys/J-xx.spec.ts` (Playwright), `apps/mobile/e2e/J-xx.yaml` (Maestro) | Appendix C §C.8 J-01–J-40 and supplementary budgets | Above-budget run or > 20% p50 regression blocks promotion beyond `ring1` |
| Golden fixtures | `tests/golden/` | Templates (P06), eligibility rows (Appendix F), duty and limitation rows (P08, P10), redline engine (P07), export archives `LD-EXPORT-1.0` (Appendix K, P20), tax rule packs (P14) | `ci/golden-archive-diff`, template golden sets |
| Contract tests | `tests/contract/` | OpenAPI 3.1, AsyncAPI 3.0, Ecosystem Spec v1.1 contracts and Appendix Y proposals (inert until approved, P19-AT-06) | `ci/openapi-breaking`, `ci/asyncapi-breaking` |
| Accessibility | axe on every route; manual scripts | Appendix U §U.8 | §V.6.2 |
| AI evaluation | `packages/ai/evals/` | Golden sets per skill, red-team suite (P09, P23 FR-P23-57) | Drop > 2 points or any High red-team failure blocks merge |
| Security | SAST, SCA, secrets, IaC, container, DAST, API fuzzing, MASVS, VAPT | P23 FR-P23-25, FR-P23-36/37 | §V.6.3 |
| Performance | k6/Gatling, Lighthouse CI, device lab | P00 FR-P00-58, P21 FR-P21-55, P22 FR-P22-96, P23 FR-P23-48 | §V.6.1 |
| UAT | `docs/uat/U-xx.md` scripts + evidence | §V.5 | Wave sign-off by the owner, the legal reviewer of record and the pilot tenant |

**Tag conventions.** Every scenario carries its ID tag first, then `@NN-xx` for each non-negotiable it proves, then optional `@CH-xx`, `@D-xx`, `@R-xxx`, `@role-<code>`, `@brand-consumer_help`, `@mobile`, `@wave-n`. A scenario that proves an NN rule must fail when the rule's guard is removed (mutation check in the NN job). Scenario titles are stable; renaming needs the phase owner's approval because UAT evidence references them.

---

## V.2 NN coverage matrix (NN-01…NN-50 × scenarios)

Counts are scenarios tagged `@NN-xx` in phase §12 (compiled 25 October 2026; recounted at registry review G4 after P08-AT-26…29). Scenario references are abbreviated `Pxx·nn` = `@Pxx-AT-nn`. **Status:** OK (≥ 4 scenarios across ≥ 2 phases), THIN (≤ 3 or one phase only) → supplementary scenarios in §V.4. **No NN rule has zero scenarios.**

| NN | Rule (short) | # | Phases | Scenarios | Supplementary | Status |
|---|---|---|---|---|---|---|
| NN-01 | Tenant isolation, RLS, IDOR/BOLA | 16 | P00 P02 P03 P04 P06 P07 P09 P11 P14 P16 P17 P18 P19 P22 | P00·01 P00·02 P02·21 P03·23 P04·04 P06·19 P07·20 P09·09 P09·10 P11·13 P14·19 P16·25 P17·21 P18·06 P19·01 P22·25 | APPV·25 | OK |
| NN-02 | Append-only hash-chained ledger; Correction Entries | 12 | P00 P02 P03 P06 P07 P09 P11 P13 P18 P21 P23 | P00·03 P00·05 P02·18 P03·20 P06·18 P07·23 P09·25 P11·22 P13·12 P18·07 P21·28 P23·20 | — | OK |
| NN-03 | Authentication ≠ identity ≠ signing; no Aadhaar login | 4 | P01 P08 P22 | P01·01 P08·10 P08·26 P22·01 | APPV·01 APPV·02 | OK (THIN at compilation; APPV·01–02 retained) |
| NN-04 | No Aadhaar number, biometrics, OTP or e-KYC stored; masking | 10 | P00 P01 P04 P05 P08 P09 P15 P20 P22 | P00·07 P01·03 P04·02 P05·06 P08·09 P08·10 P09·11 P15·11 P20·06 P22·05 | — | OK |
| NN-05 | No CKYC, bureau, PAN-database calls; no portal scraping | 10 | P01 P03 P08 P10 P11 P12 P14 P15 P19 | P01·06 P03·14 P08·06 P10·10 P11·03 P12·02 P14·11 P15·07 P19·19 P19·26 | — | OK |
| NN-06 | eSign only via licensed ESP; never sublet | 7 | P01 P08 P19 P22 | P01·21 P08·13 P08·24 P08·29 P19·07 P19·08 P22·10 | — | OK |
| NN-07 | Instrument eligibility gate | 14 | P03 P05 P06 P07 P08 P14 P15 P19 P21 P22 | P03·11 P05·15 P06·10 P07·15 P08·01 P08·02 P08·03 P08·27 P08·28 P14·06 P15·16 P19·09 P21·03 P22·08 | — | OK |
| NN-08 | Stamp before sign; authorised channels | 5 | P06 P07 P08 P22 | P06·11 P07·16 P08·04 P08·05 P22·09 | — | OK |
| NN-09 | Originals immutable; derived renditions labelled | 7 | P00 P04 P05 P10 P13 P15 P22 | P00·06 P04·01 P05·01 P10·06 P13·12 P15·10 P22·06 | — | OK |
| NN-10 | Evidence pack and BSA s.63(4) certificate draft | 5 | P05 P08 P10 P15 P20 | P05·12 P08·21 P10·07 P15·10 P20·05 | — | OK |
| NN-11 | Everything exportable in `LD-EXPORT-1.0` | 22 | 18 phases | P00·11 P02·24 P04·15 P06·21 P07·22 P09·23 P10·20 P11·23 P12·15 P13·25 P14·17 P16·19 P17·04 P18·13 P18·18 P19·25 P20·01 P20·02 P20·08 P20·09 P21·24 P22·22 | — | OK |
| NN-12 | Migration safety; paths are views over stable IDs | 7 | P00 P04 P13 P20 P23 | P00·12 P04·03 P13·08 P20·03 P20·04 P23·04 P23·05 | — | OK |
| NN-13 | Per-action human confirmation of irreversible external actions | 18 | 16 phases | P03·15 P04·08 P05·14 P06·23 P07·11 P08·15 P09·05 P09·16 P10·10 P10·14 P12·09 P14·10 P15·09 P16·23 P18·28 P19·16 P20·14 P22·26 | APPV·24 | OK |
| NN-14 | AI labelled, sourced; no fabricated citations; review lane | 12 | P05 P06 P09 P10 P11 P12 P16 P21 P22 | P05·02 P06·05 P06·08 P09·02 P09·03 P09·04 P10·16 P11·09 P12·07 P16·28 P21·04 P22·15 | APPV·14 | OK |
| NN-15 | No training on customer data; confidential classes in India route | 3 | P00 P05 P09 | P00·18 P05·07 P09·01 | APPV·03 APPV·04 APPV·19 | THIN → closed |
| NN-16 | Client-owned credential vault | 6 | P14 P18 | P14·08 P18·08 P18·09 P18·10 P18·11 P18·12 | APPV·19 | OK |
| NN-17 | Client-approved, scoped, time-bound delivery grants; break-glass | 14 | P01 P02 P04 P07 P14 P15 P16 P18 P20 | P01·20 P02·08 P02·09 P02·10 P02·11 P02·12 P04·18 P07·14 P14·18 P15·19 P16·14 P18·02 P18·03 P20·20 | — | OK |
| NN-18 | Maker-checker with SoD | 26 | 18 phases | P01·10 P02·01 P02·02 P02·06 P03·04 P03·05 P04·07 P04·12 P06·14 P07·12 P07·14 P09·06 P09·07 P11·15 P13·05 P14·13 P16·06 P17·11 P18·14 P18·15 P19·04 P20·07 P21·08 P22·13 P23·01 P23·02 | APPV·24 | OK |
| NN-19 | Only aggregates and commercial records to the Operations Hub | 10 | P11 P13 P15 P16 P17 P18 P19 P20 P21 | P11·20 P13·24 P15·24 P16·26 P17·19 P18·26 P19·10 P19·26 P20·19 P21·14 | — | OK |
| NN-20 | No unevidenced claims | 14 | 13 phases | P00·19 P01·13 P09·14 P10·02 P11·04 P12·06 P14·14 P15·08 P16·24 P17·15 P21·07 P22·14 P23·14 P23·23 | APPV·11 | OK |
| NN-21 | Marketplace professional rules | 11 | P01 P09 P11 P14 P15 P16 P17 P18 P21 | P01·12 P09·14 P11·14 P14·03 P15·13 P16·04 P16·05 P16·06 P17·12 P18·24 P21·05 | APPV·10 APPV·13 | OK |
| NN-22 | Money: hosted checkout, Route, separate fees, totals incl. GST | 8 | P08 P12 P14 P15 P16 P17 P21 P22 | P08·07 P12·09 P14·04 P15·06 P16·08 P17·07 P21·06 P22·16 | — | OK |
| NN-23 | Consumer Help brand, ethical wall, no outcome promises | 15 | P01 P02 P15 P16 P18 P19 P22 | P01·22 P02·13 P15·01 P15·02 P15·03 P15·04 P15·06 P15·24 P16·12 P18·21 P18·22 P18·23 P19·11 P19·26 P22·23 | — | OK |
| NN-24 | Cross-product data only via Ecosystem Spec contracts | 7 | P01 P04 P11 P16 P18 P19 | P01·20 P04·21 P11·19 P16·21 P18·26 P19·05 P19·27 | — | OK |
| NN-25 | India residency | 7 | P00 P05 P09 P18 P19 P20 P23 | P00·13 P05·07 P09·01 P18·19 P19·23 P20·10 P23·12 | APPV·03 | OK |
| NN-26 | DPDP notice, consent, retention, breach, children | 6 | P01 P15 P20 P21 P22 | P01·16 P01·18 P15·21 P20·18 P21·14 P22·29 | APPV·21 | OK |
| NN-27 | CERT-In 6-hour reporting, 180-day logs, NTP | 3 | P00 P23 | P00·21 P23·11 P23·13 | APPV·21 | THIN → closed |
| NN-28 | Accessibility WCAG 2.2 AA and IS 17802 | 13 | 12 phases | P01·23 P02·22 P03·07 P04·22 P05·19 P08·26 P09·24 P11·17 P18·30 P21·19 P21·25 P22·21 P23·16 | APPV·28 | OK |
| NN-29 | Settings registered, tiered, effective-dated; no Super Admin needed | 6 | P02 P03 P17 P21 | P02·05 P03·01 P03·02 P03·13 P17·17 P21·29 | APPV·06 APPV·27 | OK |
| NN-30 | Legal content is data with a reviewer of record | 5 | P03 P06 P21 P23 | P03·09 P03·10 P06·15 P21·13 P23·06 | — | OK |
| NN-31 | Public site SSR/static; private content never indexable | 3 | P00 P21 | P00·16 P00·17 P21·01 | APPV·05 APPV·06 | THIN → closed |
| NN-32 | No identifiers, secrets or content in logs and telemetry | 8 | P00 P01 P09 P18 P19 P21 P22 P23 | P00·08 P01·24 P09·11 P18·12 P19·24 P21·27 P22·18 P23·22 | — | OK |
| NN-33 | Proportionate, disclosed workforce measurement | 3 | P02 P13 P18 | P02·20 P13·22 P18·27 | APPV·07 APPV·08 | THIN → closed |
| NN-34 | Telecom: DLT, consent, one invitation, no automated calls without opt-in | 8 | P01 P03 P07 P09 P15 P19 P22 | P01·14 P03·15 P03·16 P07·05 P09·15 P15·20 P19·21 P22·27 | APPV·23 | OK |
| NN-35 | Advertising OFF by default; public content pages only | 3 | P16 P17 P21 | P16·22 P17·13 P21·23 | APPV·09 APPV·10 | THIN → closed |
| NN-36 | Savings show formula, inputs, evidence class; avoided exposure | 2 | P17 | P17·14 P17·15 | APPV·11 APPV·12 | THIN → closed |
| NN-37 | Deterministic redlining; internal comments never external | 5 | P07 P08 P22 | P07·03 P07·04 P07·09 P08·17 P22·12 | APPV·22 | OK |
| NN-38 | `[VERIFY]`-dependent features behind OFF/advisory flags | 17 | 16 phases | P00·09 P01·04 P03·12 P04·23 P06·09 P08·08 P09·19 P10·11 P11·10 P12·04 P12·13 P13·20 P14·09 P17·18 P19·06 P21·26 P23·17 | — | OK |
| NN-39 | Kill switches everywhere | 8 | P00 P03 P09 P16 P17 P18 P19 P23 | P00·10 P03·19 P09·08 P16·27 P17·11 P18·29 P19·22 P23·18 | — | OK |
| NN-40 | Formalities gate before Executed | 7 | P03 P07 P08 P14 P15 | P03·17 P07·16 P08·19 P08·20 P14·07 P15·17 P15·23 | APPV·12 APPV·20 | OK |
| NN-41 | Professional judgement stays with the professional | 3 | P14 P16 P18 | P14·02 P16·07 P18·25 | APPV·13 APPV·14 | THIN → closed |
| NN-42 | DigiLocker requester terms; URI and verification by default | 3 | P01 P04 P20 | P01·05 P04·09 P20·22 | — | OK (three phases; adequate) |
| NN-43 | Agents are makers only, sponsored, bounded | 11 | P02 P03 P04 P05 P07 P08 P09 P11 P13 P18 | P02·14 P03·18 P04·08 P05·14 P07·11 P08·15 P09·05 P09·06 P11·09 P13·13 P18·28 | APPV·19 | OK |
| NN-44 | Mobile device protections | 4 | P04 P22 | P04·20 P22·02 P22·03 P22·04 | APPV·15 APPV·16 | THIN (2 phases) → closed |
| NN-45 | Audit in the same transaction as the mutation | 9 | P00 P04 P06 P07 P09 P16 P17 P18 P21 | P00·04 P04·24 P06·18 P07·23 P09·25 P16·29 P17·22 P18·07 P21·28 | — | OK |
| NN-46 | Idempotency and reconciliation of external side effects | 9 | P05 P08 P16 P17 P18 P19 P20 P22 | P05·20 P08·23 P16·09 P17·10 P17·22 P18·18 P19·02 P20·12 P22·28 | — | OK |
| NN-47 | Shared kernels used, not forked; LDC SoR when present | 4 | P00 P13 P14 P19 | P00·20 P13·06 P14·12 P19·13 | — | OK |
| NN-48 | Machine translation labelled; certified for courts | 6 | P05 P06 P09 P10 P21 P22 | P05·08 P06·12 P09·20 P10·06 P21·18 P22·30 | APPV·22 | OK |
| NN-49 | Genuine, consented reviews; never about advocates; no photos by default | 2 | P16 P21 | P16·18 P21·05 | APPV·17 APPV·18 | THIN → closed |
| NN-50 | No dark patterns | 11 | P01 P06 P08 P14 P15 P16 P17 P21 P22 | P01·19 P06·22 P08·07 P14·05 P15·22 P16·02 P17·01 P17·02 P17·05 P21·16 P22·31 | APPV·26 | OK |

---

## V.3 Coverage analysis

1. **Zero-coverage NN rules:** none.
2. **Thin rules** (≤ 3 scenarios or one phase): NN-03 (now 4 phase scenarios with P08-AT-26, registry review G4; supplementary scenarios retained), NN-15, NN-27, NN-31, NN-33, NN-35, NN-36, NN-41, NN-44, NN-49 — closed by §V.4.
3. **Phase-owner gaps** (a phase whose own functional requirements rely on an NN rule with no scenario in that phase), closed by §V.4: P09 never tests that agents cannot reach `cvl` secrets (NN-16/NN-43 → APPV·19); P11 offline cause-list cache (NN-44 → APPV·16); P13 board approval as a formality (NN-40 → APPV·20); P14 penalty-avoided evidence (NN-36 → APPV·12); P15 protected evidence screens and no ads in cases (NN-44, NN-35 → APPV·15, APPV·09); P07 machine translation inside deal rooms (NN-48 → APPV·22); P10 WhatsApp dispatch rules (NN-34 → APPV·23); P23 DPDP breach intimation (NN-26 → APPV·21).
4. **Appendix C surfaces** (palette, universal search, home customisation, upsell, click budgets) had no scenarios in any phase → APPV·24–28.
5. **Scenarios with no NN tag** (functional only): 195 of 582 (registry review G4 recount) — acceptable; they prove phase FRs.

---
## V.4 Supplementary scenarios (`tests/acceptance/appendix/appv.feature`)

Owner column = the phase that implements the guard and keeps the scenario green. These scenarios have the same standing as phase §12 scenarios.

```gherkin
Feature: Appendix V supplementary acceptance scenarios

  @APPV-AT-01 @NN-03 @role-CP_GUEST
  Scenario: A guest's OTP opens the session but neither verifies identity nor signs   # owner P07/P08
    Given counterparty "Meera" receives a signing invitation for agreement "LD-AGR-2026-000123"
    When she opens the link and enters the e-mail OTP
    Then her session is authenticated at assurance level "guest"
    And her identity level remains "unverified" in kyc
    And no signature event exists until she completes Aadhaar eSign at the ESP or a DSC signature
    And the signer page states "Signing happens at {ESP}; your OTP here only opens this page"

  @APPV-AT-02 @NN-03 @role-OPS_RM
  Scenario: Staff realm accepts only enterprise SSO with MFA   # owner P01/P18
    Given a LawDocs staff account in realm "ld-staff"
    When a sign-in is attempted at work.lawdocs.in with a mobile OTP or a password alone
    Then the sign-in is refused and the user is sent to the group identity provider
    And a successful staff session records SSO, MFA and device posture in the audit ledger

  @APPV-AT-03 @NN-15 @NN-25
  Scenario: Confidential data cannot be routed to a model endpoint without in-region zero-retention attestation   # owner P09/P23
    Given a model route registered for data class "CONFIDENTIAL" without an India-region and zero-retention attestation in ai.models
    When Vidhi is asked to summarise a document of class "CONFIDENTIAL"
    Then the gateway refuses that route and uses the attested Bedrock India route
    And if no attested route is available the user sees "AI is unavailable for this document" and nothing is sent

  @APPV-AT-04 @NN-15
  Scenario: Evaluation and golden datasets contain no customer content   # owner P09/P23
    Given the evaluation datasets under packages/ai/evals
    When the dataset provenance check runs in CI
    Then every item carries provenance "synthetic" or "public-source" with a source reference
    And the build fails if any item hash matches a hash in any tenant's document or message store sample

  @APPV-AT-05 @NN-31
  Scenario: Private surfaces are never indexable   # owner P21 with P04/P08
    Given the routes my.lawdocs.in/*, sign.lawdocs.in/*, share-recipient viewer pages and signed file URLs
    When a crawler without a session requests each route
    Then the response is an authentication page or 404 with "X-Robots-Tag: noindex, nofollow"
    And signed file URLs expire within their configured lifetime and are absent from every sitemap
    And setting web.private.noindex cannot be switched off for these routes

  @APPV-AT-06 @NN-31 @NN-29
  Scenario: AI-crawler policy is a setting, not a code change   # owner P21
    Given web.crawl.ai_search_bots_allowed allows AI search bots and disallows AI training bots
    When PLT_SUPER_ADMIN changes the policy with a checker's approval
    Then robots.txt and response headers reflect the new policy within the revalidation window
    And no code release is involved and the change is in the audit ledger

  @APPV-AT-07 @NN-33 @role-ORG_DEPT_HEAD
  Scenario: Team workload widget shows assignment counts only   # owner P13 with Appendix C
    Given department head "Kiran" has widget w.lgo.team_workload on Home
    When the widget renders
    Then it shows per-person counts of open, due and overdue assignments and nothing else
    And no sign-in times, idle times, keystrokes, screenshots or activity timelines are queryable through its API

  @APPV-AT-08 @NN-33 @role-OPS_RM
  Scenario: Delivery staff metrics show own outcomes without ranking   # owner P18
    Given RM "Arjun" opens Me › My metrics (SCR-P18-24)
    Then he sees his SLA attainment, deliverables released and client approvals turnaround
    And no rank, leaderboard or comparison with named colleagues is displayed or available by API

  @APPV-AT-09 @NN-35 @brand-consumer_help
  Scenario: No advertising in private areas even when the advertising stream is ON   # owner P17/P21 with P15
    Given bil.streams.ads.enabled is ON for public blog pages
    When a signed-in user opens a vault folder, a matter, a Consumer Help case workspace and a Vidhi answer
    Then no ad slot is rendered and the page source contains no ad-network script
    And public blog pages show only labelled "Sponsored" contextual slots

  @APPV-AT-10 @NN-35 @NN-21
  Scenario: Advocate-related pages never carry sponsored content   # owner P16/P21
    Given web.ads.on_advocate_pages is LOCKED false
    When any page lists, profiles or describes advocates or an advocate-delivered service
    Then no ad slot or sponsored placement is rendered and the setting cannot be changed by any role

  @APPV-AT-11 @NN-36 @NN-20
  Scenario: Every savings figure shows its formula, inputs, assumptions and evidence class   # owner P17
    Given company "Alpha Pvt Ltd" has completed 40 signing requests this year
    When the CLO opens Savings & Value (SCR-P17-27)
    Then each tile shows the evidence class MEASURED, ESTIMATED or MODELLED as a word
    And opening "How we calculated this" shows the formula, the inputs with sources and the assumptions with dates
    And a tile without a valid benchmark is hidden with "Not enough evidence to show this figure"

  @APPV-AT-12 @NN-36 @NN-40
  Scenario: A licence renewal completed before its due date feeds avoided exposure only with evidence   # owner P14
    Given an FSSAI licence renewal obligation with a due date of 30-Nov-2026
    And the renewal acknowledgement is uploaded and verified on 15-Nov-2026
    When the savings ledger updates
    Then an "avoided exposure" entry is created with the obligation, due date and completion evidence
    And it is labelled "avoided exposure — not money saved" and excluded from the money-saved total
    And without the uploaded evidence no entry is created

  @APPV-AT-13 @NN-41 @NN-21
  Scenario: Hiring an advocate creates a direct engagement in the advocate's name   # owner P16/P21
    Given a visitor clicks "Hire a professional" on a pleading page for a written statement
    When she chooses an advocate's fixed-fee service and pays
    Then the engagement letter names the advocate as the service provider under direct engagement terms
    And LawDocs' invoice shows only the disclosed platform fee and GST
    And no page, invoice or message states that LawDocs provides the legal advice or representation

  @APPV-AT-14 @NN-41 @NN-14
  Scenario: Vidhi routes a matter-specific advice request to a professional   # owner P09
    Given an individual asks "Should I accept the bank's settlement offer in my case?"
    When Vidhi answers
    Then the answer gives general information with dated sources and the AI label
    And it offers a consultation with a professional and does not recommend accepting or rejecting the offer

  @APPV-AT-15 @NN-44 @mobile
  Scenario: Protected screens block screenshots and recents previews   # owner P22 with P15/P18
    Given the mobile app shows a Consumer Help evidence item, a signing consent screen or an approval diff
    When the user takes a screenshot or opens the app switcher
    Then the screenshot is blocked on Android and the iOS snapshot shows the privacy cover
    And the event is not logged with any content

  @APPV-AT-16 @NN-44 @mobile
  Scenario: Offline cause-list cache is encrypted and purged   # owner P11/P22
    Given "Cause List Today" (SCR-P11-07) was cached on the device for offline reading
    When the database file is inspected outside the app
    Then it is encrypted with a device-bound key
    And signing out, revoking the device or a remote wipe deletes the cache within one sync cycle

  @APPV-AT-17 @NN-49
  Scenario: Review invitation only after a verified, completed purchase   # owner P16
    Given buyer "Ravi" completed and accepted the deliverable of a LawDocs-delivered trademark search service
    When the review invitation is sent
    Then the review is about the LawDocs service, records Ravi's consent to publish and the order reference
    And the review is published only after moderation and never shows a photo by default
    And no invitation is possible for an engagement delivered by an advocate

  @APPV-AT-18 @NN-49
  Scenario: A testimonial submitted with a photo displays without it by default   # owner P21
    Given a consented testimonial with an attached photo is approved in the Content Studio
    When the testimonial block renders on a public page
    Then the photo is not displayed unless the reviewer of record enables it with a recorded reason
    And the block shows the purchase verification date

  @APPV-AT-19 @NN-16 @NN-15 @NN-43
  Scenario: No agent, Vidhi tool or MCP tool can read a credential secret   # owner P09/P18
    Given the credential vault is enabled for "Beta Finance Ltd" with a granted MCA21 entry
    When an agent mission, a Vidhi tool call or an MCP client requests that entry
    Then the tool registry has no tool that returns a secret and the request is refused
    And only metadata (portal, masked username, owner, rotation date) is available to retrieval
    And the refusal is logged without the secret

  @APPV-AT-20 @NN-40
  Scenario: A board-approval formality blocks Executed until the resolution is recorded   # owner P08/P13
    Given an agreement whose formalities plan includes "Board approval" from the DoA
    And both parties have signed
    When the maker tries to mark the agreement Executed
    Then the action is blocked with the open formality listed
    When the CS records the board resolution reference and the minutes are sealed
    Then the formality closes and the agreement can move to Executed

  @APPV-AT-21 @NN-26 @NN-27
  Scenario: A personal-data breach opens Data Protection Board and affected-principal tasks   # owner P23
    Given LawDocs is data fiduciary for individual users and a breach affecting 120 of them is confirmed
    When the incident commander classifies it as a personal-data breach
    Then tasks open for the CERT-In report within 6 hours of detection
    And for intimation to the Data Protection Board and affected principals without delay, with the detailed report clock per DPDP Rules 2025 r.7 [VERIFY commencement and timeline]
    And for each affected company tenant where LawDocs is processor, a notice to the tenant's privacy contact
    And every submission is made by a human and recorded with evidence

  @APPV-AT-22 @NN-48 @NN-37
  Scenario: A machine-translated counterparty message is labelled and never becomes agreed text   # owner P07
    Given counterparty "Suresh" writes in Marathi in the shared channel of a deal room
    When the maker views it with "Translate to English"
    Then the translation is labelled "Machine translation — check before relying on it"
    And it is a derived rendition linked to the original message
    And adopting text into the agreement uses the original-language source or a reviewed translation, never the unlabelled machine output

  @APPV-AT-23 @NN-34
  Scenario: WhatsApp notice dispatch needs an approved template and recipient opt-in   # owner P10
    Given a legal notice ready for dispatch with channels speed post, e-mail and WhatsApp selected
    And the recipient has not opted in to WhatsApp from the sender
    When the dispatch summary is built
    Then WhatsApp is removed with the reason "Recipient has not opted in"
    And the summary lists every message, recipient, channel and date for one explicit confirmation

  @APPV-AT-24 @NN-13 @NN-18
  Scenario: Command palette and quick actions never bypass confirmation   # owner P03 with Appendix C
    Given a maker types "Send for signature" in the command palette on an agreed version
    When she selects the command
    Then the same review screen as the "Send for signing" button opens with eligibility, stamp and participants
    And nothing is sent until she confirms on that screen
    And "Approve next" from the palette opens the diff and requires the same step-up as the button

  @APPV-AT-25 @NN-01
  Scenario: Universal search never returns content from another context   # owner P04/P03
    Given "Ananya" holds a Personal workspace and the context "Alpha Pvt Ltd — Legal maker"
    And a document titled "Noida flat lease" exists only in her Personal vault
    When she searches "Noida flat" while in the Alpha context
    Then no Personal result content is shown
    And the results show only "1 result in your Personal workspace — switch to view"
    And a user without the Personal context sees no such hint

  @APPV-AT-26 @NN-50
  Scenario: Upsell is non-modal, dismissible and absent from signing and deadline tasks   # owner P17 with Appendix C
    Given an individual on the Free plan opens a locked feature
    Then a non-modal "Not in your plan — see what it does" card appears
    When she dismisses it
    Then it does not reappear for 30 days
    And no upsell card, banner or Discover entry renders on the signer page, an approval dialog or a task with a legal deadline

  @APPV-AT-27 @NN-29
  Scenario: Home and navigation customisation needs neither an admin nor Super Admin   # owner P03
    Given user "Kiran" pins three items, removes a non-mandatory widget and reorders mobile tabs
    Then each change takes effect within 60 seconds and can be undone
    And ORG_ADMIN sets a default home layout for "Department user" without any platform involvement
    And a mandatory widget can be moved but its remove control is absent

  @APPV-AT-28 @NN-28
  Scenario: Top journeys meet their click budgets by keyboard and with a screen reader   # owner P23 with Appendix C
    Given journey tests J-01 to J-40 from Appendix C §C.8
    When each runs with pointer, keyboard-only and with NVDA (web) and TalkBack (Android)
    Then every journey completes within its budget using the counting rule in §C.8.1
    And no journey requires drag, hover-only controls or a time limit without extension
```

---
## V.5 UAT scripts per persona (end-to-end across phases)

Each script runs in the `uat` environment (P00 FR-P00-14; the same stage is called `pre-prod` in P23 FR-P23-07 — gap G-07) on synthetic seed data (§V.7), on web and on the mobile app where the parity matrix marks the step `F`. The tester records pass/fail per step, screenshots of non-protected screens, the click count for each J-journey and the audit-ledger extract for the run. A script passes only when every expected result holds and no NN scenario listed against it fails in the same build.

### V.5.1 Journey index

| # | Script | Personas | Wave | Phases crossed |
|---|---|---|---|---|
| U-01 | Individual: sign up → draft rent agreement → eStamp → eSign with landlord → store → reminder at renewal | `ANON` → `IND_OWNER`, `CP_GUEST` | 1 | P21 P06 P01 P08 P04 P03 P17 |
| U-02 | Company: onboard → legal intake → NDA negotiation → DSC signing → obligation tracking | `ORG_OWNER`, `ORG_MEMBER`, `ORG_LEGAL_MAKER`, `ORG_APPROVER`, `CP_GUEST` | 1 | P01 P02 P13 P07 P08 P04 |
| U-03 | NBFC retainer: RM as maker, client checker, credential vault reveal, deliverable | `OPS_DELIVERY_LEAD`, `OPS_RM`, `ORG_ADMIN`, `ORG_CHECKER` | 2 | P16 P18 P02 P10 P04 P20 |
| U-04 | Consumer Help: insurance claim rejection → Insurance Ombudsman complaint pack | Consumer, `OPS_CONSUMER_CASE_MANAGER` | 3 | P15 P05 P10 P04 P16 |
| U-05 | Litigant self-help: received notice → reply → case by CNR → hearing reminders | `IND_OWNER` | 2 | P09 P10 P11 P04 |
| U-06 | CLO portfolio: bulk import of matters → cause list → order digest → board section | `ORG_CLO`, `ORG_EXT_COUNSEL`, `ORG_KMP` | 2 | P11 P05 P13 |
| U-07 | WhatsApp evidence → type copy → translation → annexure → s.63 certificate → filing pack | `IND_OWNER`, `PRO_ADVOCATE` | 2 | P05 P10 P08 P16 |
| U-08 | Trademark: class finder → knock-out screen → hand-off to agent → Journal watch hit → opposition matter | `ORG_CLO`, `PRO_ADVOCATE` | 2 | P12 P11 P16 |
| U-09 | Board meeting: notice → pack → VC meeting → minutes draft → seal → resolution follow-on | `ORG_KMP` (CS), `ORG_DIRECTOR` | 2 | P13 P09 P08 |
| U-10 | Marketplace non-subscriber buys a fixed-price service → SLA → deliverable → invoice | `ANON` → buyer, `OPS_PROFESSIONAL` | 1 | P16 P17 P01 P18 |
| U-11 | Export everything to BYO OneDrive → open offline → re-import package into a new tenant | `ORG_ADMIN`, `ORG_CHECKER`, `IND_OWNER` | 1 | P20 P04 P19 |
| U-12 | Upload a folder of 2,000 files → mapping review → commit → undo | `ORG_ADMIN`, `IND_OWNER` | 1 | P04 P20 P05 |
| U-13 | Hire an AI agent → mission → approvals → kill switch → digest | `ORG_ADMIN`, `ORG_LEGAL_MAKER` | 3 | P09 P02 P03 |
| U-14 | Super Admin correction of a client's registered office → client approval → visibility | `PLT_SUPER_ADMIN`, `PLT_SECURITY_OFFICER`, `ORG_OWNER` | 1 | P00 P18 P03 |
| U-15 | Start a business: entity chooser → Pvt Ltd order → documents → filing preview → obligations | `ANON` → `ORG_OWNER`, `PRO_CS` | 3 | P14 P16 P17 P08 |
| U-16 | Personal tax: ERI consent guide → computation → approval → filing by taxpayer route | `IND_OWNER`, `PRO_TAX_PRACTITIONER` | 3 | P14 P18 |
| U-17 | Content publisher: Word folder → posts → legal review → schedule → SEO checks | `OPS_CONTENT_PUBLISHER`, `PLT_LEGAL_REVIEWER` | 1 | P21 P06 |
| U-18 | Mobile-first individual with a screen reader: scan → vault → sign → evidence | `IND_OWNER` (TalkBack, VoiceOver) | 2 | P22 P04 P08 Appendix U |
| U-19 | Ecosystem: Udofin deposit link; partner batch onboarding; LDC system-of-record switch | `IND_OWNER`, partner admin, `ORG_ADMIN` | 2 | P19 P13 P01 |
| U-20 | Plan lifecycle: trial → upgrade → credits → cancellation → lapse with export | `IND_OWNER`, `ORG_ADMIN` | 1 | P17 P20 |

### V.5.2 Scripts

**U-01 Individual — rent agreement end to end** *(J-01, J-05, J-11; P06-AT-01, P01-AT-02, P08-AT-04/05/07/10/21, P04-AT-01/16, P17-AT-01)*

| Step | Action | Expected result |
|---|---|---|
| 1 | Visitor opens `/documents/property-transactions/rent/rent-agreement-residential` on a phone | Server-rendered page; 50-word answer; eSign badge "Valid" with "i"; State selector; drafter above the fold (SCR-P21-05, SCR-P06-01) |
| 2 | Answers the interview (≤ 10 questions) anonymously; chooses 11-month term | Live preview; no account needed; lock-in clause appears only when chosen (P06-AT-03) |
| 3 | Taps "Save and continue"; signs up with mobile OTP inline | Account ≤ 3 taps + one OTP; consents unticked with equal choices (P01-AT-19); no Aadhaar login option (P01-AT-01) |
| 4 | Taps "Send for signing" | Eligibility card: eSign valid for this instrument (Appendix F); registration not compulsory for a lease under one year (Registration Act 1908 s.17(1)(d)) shown with "i" [LAW]; stamp panel opens (stamp before sign, NN-08) |
| 5 | Chooses "Buy e-stamp"; reviews checkout | Duty at actuals, LawDocs facilitation fee, GST and total shown separately before payment (P08-AT-07); unverified duty rows marked advisory (P08-AT-08) |
| 6 | Pays on the hosted page; e-stamp certificate attached | UIN verified and bound to the document hash (P08-AT-05) |
| 7 | Adds landlord; taps Send; counts clicks | J-01 ≤ 8 clicks + inputs + hosted payment for the buy path |
| 8 | Landlord (guest) signs from the SMS link with Aadhaar eSign | J-05 ≤ 4 taps + OTP; LawDocs stores no Aadhaar data (P08-AT-10); one invitation and stoppable reminders (P01-AT-14) |
| 9 | Tenant signs; completion | Evidence pack with hashes and s.63(4) certificate draft (P08-AT-21); signed PDF immutable in Vault › Property (P04-AT-01) |
| 10 | Opens the document; sets a reminder 60 days before expiry | J-11 ≤ 3; reminder chain scheduled (P04-AT-16); expiry appears in "Expiring soon" on Home |
| 11 | Time-travel the uat clock to 60 days before expiry | Reminder arrives in the chosen channel; "Renew" starts a new draft pre-filled from the old agreement |

**U-02 Company — onboarding to obligation tracking** *(J-13, J-14, J-17, J-18, J-04, J-19; P01-AT-07/09/10, P02-AT-01/02/03, P13-AT-01/03, P07-AT-01/03/04/09/12/16/17/19, P08-AT-11)*

| Step | Action | Expected result |
|---|---|---|
| 1 | Owner enters one GSTIN | Company discovered with provenance badges (P01-AT-07); directors listed; listed director becomes signatory (P01-AT-09) |
| 2 | Set-up wizard: departments, approval model, invites | SoD preview; invite ≤ 3 clicks; Home shows "Finish setting up" until done |
| 3 | Sales member raises "NDA with Vendor X" from Teams | Request created ≤ 3 clicks (P07-AT-01, P13-AT-01); self-service NDA offered within guardrails (P13-AT-03) |
| 4 | CLO assigns to maker | J-14 ≤ 2 |
| 5 | Maker drafts from the tenant playbook and shares with the counterparty | Leakage check passes; guest sees only the shared version (P07-AT-04), J-17 ≤ 3 |
| 6 | Counterparty returns a redline with an untracked edit | Silent edit detected (P07-AT-07); internal comments never visible externally (P07-AT-03); each decision logged (P07-AT-09) |
| 7 | Maker submits for approval | DoA routes by value and deviation (P07-AT-12); maker cannot approve (P02-AT-01); approver approves from push, J-04 ≤ 2 + step-up; approval bound to version (P02-AT-02) |
| 8 | Both parties confirm the agreed version; send for DSC signing | Gates checked (P07-AT-16); J-19 ≤ 6; DSC agent detected (SCR-P08-06); consent recorded per signer (P08-AT-11) |
| 9 | Execution complete | Obligations proposed with clause anchors; key dates need human verification (P07-AT-19); renewal widget shows the notice deadline |

**U-03 NBFC legal retainer — RM as maker, client checker, vault reveal, deliverable** *(J-35–J-38; P16-AT-14/15, P18-AT-01/02/08/09/12/18, P02-AT-08/09, P20-AT-20, P10-AT-14)*

Precondition: synthetic tenant "Beta Finance Ltd" (NBFC, Company workspace) with a signed legal retainer.

| Step | Action | Expected result |
|---|---|---|
| 1 | Retainer activation | SLA schedule eSigned before activation (P16-AT-15); activation proposes RM-as-maker grants (P16-AT-14) |
| 2 | Delivery lead proposes RM "Arjun" as delegated maker for Legal › Recovery notices, 6 months | J-36 ≤ 3; client approval required (P02-AT-08) |
| 3 | Client admin approves from the notification | J-37 ≤ 2 + step-up; access-transparency log entry visible to the client |
| 4 | Arjun opens the client section and acts in tenant | Delivery banner names role, checker and grant end (P18-AT-30); RM can never be checker (P18-AT-02, P02-AT-09) |
| 5 | Arjun drafts 25 SARFAESI s.13(2) demand notices from the verified template pack | Drafts created as maker items; dispatch requires the client's explicit confirmation of an itemised send plan (P10-AT-14, X-04) |
| 6 | Client checker returns 2 drafts with comments; approves 23 | Returned items reach Arjun's queue; approvals logged with diff |
| 7 | Client admin enables the credential vault (maker) and a second admin approves | Vault OFF by default; maker-checker to enable (P18-AT-08) |
| 8 | Arjun adds an MCA21 entry | Delegation route shown first (P18-AT-09); storing needs a reason |
| 9 | Arjun requests a just-in-time reveal | J-38 ≤ 3 + step-up + client approval; reveal logged, notified, secret absent from logs (P18-AT-12); not available on mobile web by default (`cvl.reveal_on_mobile`) |
| 10 | Arjun releases the final deliverable (notice batch report) | Filed in the client DMS and optionally copied to the client's drive (P18-AT-18) |
| 11 | Arjun attempts "Export everything" | Refused (P20-AT-20) |
| 12 | Grant end date passes | Access ends; vault lists credentials revealed by Arjun and prompts rotation (FR-P18-32) |

**U-04 Consumer Help — insurance claim rejection to Ombudsman pack** *(J-39; P15-AT-01/02/03/08/09/10/11/14/21/22, P05-AT-06)*

| Step | Action | Expected result |
|---|---|---|
| 1 | Consumer opens the brand host; taps "Health claim rejected" | Brand theme; "We never collect fines or dues"; fee sheet linked; conflict check runs against group lender/insurer clients (P15-AT-02); service unavailable → fails closed (P15-AT-03) |
| 2 | Completes triage | J-39 ≤ 6; result shows the ladder: insurer GRO → Bima Bharosa/IRDAI → Insurance Ombudsman → consumer commission; fee sheet before acceptance (P15-AT-22) |
| 3 | Uploads policy, rejection letter and hospital bills; mobile capture | Hashes recorded; Aadhaar masked in typed copies (P15-AT-11, P05-AT-06) |
| 4 | Case manager drafts the GRO letter | Banned phrases blocked (P15-AT-08); the user approves and sends — agent cannot send (P15-AT-09) |
| 5 | Time-travel past the insurer's reply period with a rejection | "Waiting on: Insurer" changes to "You"; Ombudsman window computed from the reply date (within one year, FR-P15-32) |
| 6 | Generate the Ombudsman complaint pack | Pack with evidence bundle, hashes and s.63 certificate draft (P15-AT-10); the user signs and files (R.14(1) lists no agents) |
| 7 | Claim value set to ₹62 lakh (premium paid far below ₹50 lakh) in a variant run | Ladder skips the Insurance Ombudsman (claim above ₹50 lakh) and shows the District Commission via e-Jagriti, because pecuniary jurisdiction follows the consideration paid (P15-AT-14) |
| 8 | User withdraws consent for advocate sharing | Sharing stops (P15-AT-21); no data visible in any lender tenant (P15-AT-01) |

**U-05 Litigant self-help** *(J-08, J-20, J-02; P09-AT-02/13, P10-AT-04/13/14/18, P11-AT-01/07/17/18)* — Individual asks Vidhi about a cheque-bounce notice received (cited answer, AI label, legal-aid card); drafts a reply (template lane); dispatch summary and confirmation; adds the complaint case by CNR in ≤ 3 taps; cause-list match triggers next-day alert; case explainer in Hindi read by screen reader; next date visible from Home in ≤ 2.

**U-06 CLO litigation portfolio** *(J-21, J-22; P11-AT-03/04/05/06/08/09/12/15/16/22/23)* — Bulk import 300 matters from XLSX with undo; vendor freshness chips; external counsel records outcomes via the 4-field form (J-21); missing outcome chased; order digest confirmed into tasks (J-22); invoice approver ≠ maker; exposure frozen for the quarter; board section generated; export folder structure verified.

**U-07 Evidence for a petition** *(J-25, J-26; P05-AT-01/02/04/08/11/12/17, P10-AT-06/07/08/09)* — WhatsApp export with ambiguous date format (asked, not guessed); type copy with low-confidence lines reviewed; translation labelled; certified translation ordered where filing requires; annexure trio with statuses; advocate attests the true typed copy; s.63 Part A draft; PDF/A filing pack with bookmarks.

**U-08 Trademark** *(J-23, J-24; P12-AT-01/03/07/08/09/10/11)* — Add mark by application number; assisted refresh from a status PDF; class finder with reasons; knock-out screen never concludes registrability; data sheet handed to the agent with separate fees; Journal hit with opposition last date; oppose → P11 matter created.

**U-09 Board meeting** *(P13-AT-09/10/11/12/13/14/16)* — Cadence warning; shorter-notice path; VC attendance checklist; minutes drafted by Vidhi without invented attendance or votes; sealed minutes immutable; special resolution creates the follow-on filing task; director signs on mobile in ≤ 3 taps.

**U-10 Marketplace without a plan** *(J-28; P16-AT-01/02/03/08/09/15/18/19, P17-AT-07/16)* — Browse without login; landed price card; buy with a Free account (≤ 7 taps mobile); hosted checkout confirmed by webhook, not the redirect; Route hold for the professional fee; deliverable accepted; GST invoice e-mailed by OH8; review invitation about the LawDocs service only (APPV-AT-17).

**U-11 Portability round trip** *(J-32; P20-AT-01/05/07/08/10/12/17/21, P04-AT-10)* — Company full export needs a second approver; delivered to BYO OneDrive; regulated data refused for Google Drive; offline verification detects a tampered file; package re-imported into a fresh tenant places every item exactly; individual exports everything without staff help.

**U-12 Folder intake** *(J-03; P04-AT-10/11, P20-AT-14/15/16, P05-AT-16)* — "Upload folder" with 2,000 synthetic files; mapping preview with confidence; "41 need your choice"; duplicates linked not copied; commit after human review; undo removes only what the import created.

**U-13 AI workforce** *(J-33, J-34; P09-AT-05/06/07/08/16/17/18, P03-AT-18)* — Hire Contract Drafter at L2 with sponsor and budget (≤ 6 clicks); mission prepares drafts; agent cannot send or approve; autonomy raise needs a different checker; kill switch stops within 60 s; budget hard stop; daily digest lists actions with undo.

**U-14 Super Admin correction** *(P00-AT-05, P02-AT-18, P18-AT-14/16, P03-AT-20)* — Correction drafted with client letter; self-approval impossible; second approver with step-up; client approval; "Changes made by LawDocs" shows old and new values with reason; owner e-mail change notifies both channels.

**U-15 Start a business** *(P14-AT-01/02/04/05/07/13/15/16, P16-AT-08)* — Entity chooser; Pvt Ltd order with full fee breakdown; government fee paid on the official portal, not into a LawDocs account; no pre-ticked add-ons; SLA clock pauses only while waiting on the customer; filing preview approved by the customer; certification only by a practising professional; licence renewal obligations created.

**U-16 Personal tax** *(P14-AT-08/09/10/11)* — ERI consent guide ("we never ask for your OTP"); unverified tax-year rule pack blocks upload; computation reviewed; filing completed by the taxpayer's EVC route; agent cannot file; no portal scraping.

**U-17 Content publisher** *(J-40; P21-AT-07/08/09/10/11/13/18/28, P06-AT-17)* — DOCX folder import creates drafts; outdated law flagged; copied competitor text blocked; claims lint; maker ≠ checker; legal review for flagged types; scheduled publish; page without reviewer not indexed; machine-translated version held for review.

**U-18 Accessible mobile journey** *(J-06, J-05; P22-AT-01/03/05/06/09/21, P04-AT-22, APPV-AT-15/28)* — Run with TalkBack and VoiceOver at 200% text: sign in with passkey; scan with spoken hints; Aadhaar masking preview described; save to vault; sign a document with the linear pre-sign summary (Appendix U §U.5.2); evidence pack opened; protected screens block screenshots.

**U-19 Ecosystem** *(P19-AT-05/07/08/12/13/18/19/20, P13-AT-06/08)* — Udofin deposit link in ≤ 3 taps; deposit verified and immutable; partner batch with KYB pre-fill and consent (no bureau/CKYC/PAN-database calls); individuals cannot be bulk-onboarded; sister product cannot use LawDocs' ESP route; hosted signing hand-off; LDC SoR switch loses nothing and reconciles sealed minutes.

**U-20 Plan lifecycle** *(J-29, J-30, J-31; P17-AT-01/03/04/05/06/08/14)* — Trial never auto-converts; upgrade with prorated quote; failed eSign returns the credit; invoice download ≤ 2; cancellation ≤ 3 with no confirm-shaming; after lapse, read and export still work.

---
## V.6 Release test gates

### V.6.1 Performance (P00 FR-P00-58 initial budgets, confirmed in P23; P21 FR-P21-55; P22 FR-P22-96; P23 FR-P23-48)

| Gate | Threshold | Tool / when |
|---|---|---|
| API latency | p95 ≤ 300 ms reads, ≤ 600 ms writes at 200 concurrent users per tenant | k6 in `staging` per `rc-*`; automatic rollback when p95 > 800 ms for 5 minutes in prod |
| Load | 5,000 concurrent users across 2,000 tenants within the API budgets | k6/Gatling pre-wave |
| Peak signing | 1,000 signing ceremonies per hour; FY-end renewal spike | Pre-wave; ESP sandboxes and simulators |
| Bulk | 10,000-file folder import ≤ 30 minutes; 50 GB export resumable | Pre-wave |
| Soak | 24 h at 60% peak without memory growth | Pre-wave |
| Search | ≤ 800 ms p95 on 10,000 documents (individual); ≤ 1.5 s p95 on 1 million documents (tenant) | Nightly on `load` seed |
| Public web (CWV, p75 mobile) | LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, TTFB ≤ 0.8 s; content-page JS ≤ 150 kB; drafter island ≤ 250 kB | Lighthouse CI per PR (lab) + field data weekly |
| `my.lawdocs.in` | First contentful paint ≤ 1.5 s | Lighthouse CI |
| Mobile | Cold start < 2.5 s mid-range Android, < 4.0 s low-end; warm < 1.0 s; 500-item vault list ≥ 55 fps median; 10-page scan to PDF ≤ 6 s; Android download ≤ 35 MB (arm64); iOS thinned ≤ 50 MB; crash-free ≥ 99.7% | Device lab per build; staged rollout halts on breach |
| Resilience | Loss of an AZ, Redis, OpenSearch (FTS fallback), primary ESP (failover), AI provider (deterministic fallbacks), court-data vendor (staleness labels) | Chaos runs pre-wave |
| Recovery | RPO ≤ 15 min, RTO ≤ 4 h; weekly restore test passes (P23-AT-09/10) | SRE |
| Click budgets | J-01–J-40 within budget; no > 20% p50 regression | Journey suite per `rc-*` (§V.1) |

### V.6.2 Accessibility (NN-28; Appendix U §U.8–U.9)

| Gate | Rule |
|---|---|
| Automated | axe on every route in CI (`ci/axe`), zero serious/critical violations; RN accessibility lint on mobile; contrast validation of every theme in four modes (P03-AT-07) |
| Manual expert audit | Each release: critical journeys (U.2 list plus J-01–J-10) with NVDA + Chrome, JAWS + Edge, VoiceOver + Safari (macOS, iOS), TalkBack + Chrome; keyboard-only; 400% zoom / 320 CSS px reflow; 200% text; forced colours; reduced motion |
| Disabled-user testing | Each wave with blind, low-vision, Deaf/hard-of-hearing, motor-impaired and cognitively disabled participants (U.8.3); findings triaged in SCR-P21-34 |
| Release block | Any open S1 accessibility defect blocks promotion to `ring2` (P23-AT-16); S2 needs a dated fix plan; the accessibility statement is updated per release (FR-P21-141) |
| Content | Captions on all videos, transcripts, ISL for core tutorials (`hlp.video.isl_required_for_core`); every chart has a data table |

### V.6.3 Security (P23 §4E, §4H; NN-01, NN-32, NN-44)

| Gate | Rule |
|---|---|
| Every PR | SAST, SCA, secrets (push protection), IaC, container scan, `ci/rls-lint`, IDOR/BOLA tests per endpoint generated from OpenAPI, log-scrubber tests |
| Every staging deploy | DAST baseline (OWASP ZAP); authenticated full scan weekly; API fuzzing nightly (Schemathesis) |
| Mobile build | MASVS-aligned static and dynamic checks: certificate pinning, root/jailbreak and tamper detection, no sensitive logs, protected screens (P22-AT-02/03/04/18, APPV-AT-15) |
| AI | Red-team suite on every change to `packages/ai/**`: prompt injection from uploads and e-mails, cross-tenant exfiltration canaries (P09-AT-09), tool misuse, fabricated citations, AI-label bypass; merge blocked on any High failure |
| Pre-release VAPT | Any release that materially changes authentication, authorisation, eSign/eStamp, payments, the credential vault, public APIs, mobile apps or the AI gateway stays in `ring1` until Critical/High findings are closed (FR-P23-37) |
| Vulnerability SLAs | Per P23 FR-P23-26 severity model; Critical follows the emergency lane (P23-AT-07); risk acceptances expire (P23-AT-08) |
| Payments | PCI DSS scope stays SAQ A — hosted/tokenised checkout only; never "PCI certified" wording (P23-AT-15, CH-19) |

### V.6.4 Legal-content and AI gates

- Every template, clause, rule row, eligibility row, glossary term and jurisdiction variant passes its golden tests and has a reviewer of record before publication (NN-30; P03-AT-09, P06-AT-16).
- Any feature that depends on a `[VERIFY]` fact ships OFF or advisory until the verification-log row is closed; go-live is blocked by a live `[VERIFY]`-dependent flag (NN-38; P23-AT-17).
- AI golden-set metrics (accuracy, citation resolution, refusal without source, AI-label presence) may not drop by more than 2 points (FR-P23-57); model changes need evaluation and canary (P23-AT-21).

---

## V.7 Test data rules (synthetic only)

1. **No production data outside production.** LOCKED rule (P23 §10): `dev`, `test`, `staging`, `uat` and `pre-prod` use synthetic seeds only (`demo`, `load`, `legacy-mirror` profiles, P00); a rehearsal on migrated data runs only in the isolated rehearsal VPC inside production with no human access.
2. **Generated identifiers.** PAN, GSTIN, CIN, DIN, CNR, trademark application numbers, IFSC and mobile numbers are generated with valid checksums or formats inside reserved synthetic ranges at runtime; Aadhaar-like 12-digit numbers are generated Verhoeff-valid at runtime and never stored in fixtures (P00-AT-07). A regex scan of fixtures and seeds blocks real-looking identifiers in CI.
3. **Synthetic people and organisations.** Names from a curated multilingual synthetic name list covering the ten launch languages; organisations named with a "(Test)" suffix in non-demo seeds; no real lender, insurer, court, advocate or public figure is used as a party. Court and IP data come from vendor sandboxes or synthetic generators labelled "synthetic".
4. **Documents.** Seed documents are generated from LawDocs templates with synthetic answers; handwriting and screenshot fixtures are produced by staff volunteers writing synthetic text or by generators, with release forms on file; WhatsApp fixtures are generated in the native export format per locale (P05-AT-05).
5. **Vendors.** ESP, eStamp, KYC/KYB, DigiLocker, payment, court-data, IP and telecom adapters run against sandboxes or LawDocs simulators in non-production; no live government portal is called from automated tests (NN-05); outbound messages go only to allow-listed test inboxes and numbers.
6. **AI.** Evaluation and golden sets are synthetic or public-source with provenance (APPV-AT-04); no customer prompt, document or message enters an evaluation set (NN-15).
7. **Tutorials and screenshots.** Captured only in the `demo` tenant; capture refuses a real tenant (P21-AT-21).
8. **UAT evidence.** Screenshots exclude protected screens; logs attached to UAT evidence pass the PII scrubber; evidence is stored in the `ld-uat` account with 180-day retention.
9. **Accessibility testing participants.** Use synthetic accounts; recordings only with written consent; stored in India; deleted after the findings are triaged unless the participant agrees otherwise.
10. **Time travel.** Clock-dependent scenarios (limitation, renewal, SLA, nominee waiting periods, grant expiry) use the Temporal test server and an injectable clock, never system-time changes on shared environments.

---

## V.8 Consolidated scenario catalogue (582 phase scenarios; 571 at compilation + 7 added at integration review F2 for FR-P15-70, FR-P19-84, FR-P23-58 and the Appendix Y inertness check + 4 added at registry review G4: P08-AT-26…29)

One line per `@Pxx-AT-nn`; "Tags" lists the NN rules and other tags the scenario carries in its phase file. Titles are verbatim from phase §12.

### V.8.1 P00 — Foundations, Repository Discovery and Migration (`tests/acceptance/p00/`; 22 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P00-AT-01 | Cross-tenant read is denied on every table | NN-01 |
| P00-AT-02 | IDOR attempt returns not found without leaking existence | NN-01 |
| P00-AT-03 | The ledger cannot be edited by any role | NN-02 |
| P00-AT-04 | Every mutating route writes a ledger event in the same transaction | NN-45 |
| P00-AT-05 | Super admin corrects a client's master data only with approval and visibility | NN-02 |
| P00-AT-06 | An original cannot be overwritten or deleted within retention | NN-09 |
| P00-AT-07 | Aadhaar numbers never reach stored derived text | NN-04 |
| P00-AT-08 | Logs contain no identifiers or secrets | NN-32 |
| P00-AT-09 | A flag that depends on an unverified fact cannot be turned on | NN-38 |
| P00-AT-10 | Kill switch stops an adapter within 60 seconds | NN-39 |
| P00-AT-11 | A new tenant table without an export-map entry fails CI | NN-11 |
| P00-AT-12 | A destructive migration in the same release as its replacement is rejected | NN-12 |
| P00-AT-13 | Infrastructure outside India is denied | NN-25 |
| P00-AT-14 | Migration cannot be promoted with a money mismatch | — |
| P00-AT-15 | A migrated customer finds their order and document after cut-over | — |
| P00-AT-16 | Every old sitemap URL redirects in one hop to a server-rendered page | NN-31 |
| P00-AT-17 | robots and sitemap never conflict | NN-31 |
| P00-AT-18 | Legacy chatbot logs never reach an AI store | NN-15 |
| P00-AT-19 | Unevidenced claims do not survive cut-over | NN-20 |
| P00-AT-20 | Shared kernels are used, not forked | NN-47 |
| P00-AT-21 | Clocks and logs meet CERT-In directions | NN-27 |
| P00-AT-22 | Decommissioning requires archive evidence | — |

### V.8.2 P01 — Identity, Onboarding, KYC/KYB and Consent (`tests/acceptance/p01/`; 25 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P01-AT-01 | Aadhaar is not offered as a way to sign in | NN-03 |
| P01-AT-02 | First draft in under two minutes | — |
| P01-AT-03 | Aadhaar offline verification stores no Aadhaar number | NN-04 |
| P01-AT-04 | Aadhaar Verifiable Credential stays off until OVSE registration is recorded | NN-38 |
| P01-AT-05 | DigiLocker PAN is recorded by reference | NN-42 |
| P01-AT-06 | Closed data sources cannot be configured | NN-05 |
| P01-AT-07 | Company discovered from one GSTIN with provenance | — |
| P01-AT-08 | Struck-off company cannot be badged as verified | — |
| P01-AT-09 | A listed director becomes signatory automatically | — |
| P01-AT-10 | Authority by board resolution needs two reviewers | NN-18 |
| P01-AT-11 | Signing as the entity is blocked beyond the recorded limit | — |
| P01-AT-12 | Advocate application captures Rule 36 fields only for any public profile | NN-21 |
| P01-AT-13 | Credential badge wording makes no quality claim | NN-20 |
| P01-AT-14 | Counterparty receives one invitation and can stop reminders | NN-34 |
| P01-AT-15 | Guest says "This is not me" | — |
| P01-AT-16 | A minor cannot create an account | NN-26 |
| P01-AT-17 | Nominee release is cancelled by the owner's sign-in | — |
| P01-AT-18 | Consent withdrawal propagates within one hour | NN-26 |
| P01-AT-19 | No pre-ticked consents and equal choices | NN-50 |
| P01-AT-20 | Onboarding on someone else's initiative gives the requester no tenant access | NN-17 NN-24 |
| P01-AT-21 | Partners cannot use LawDocs' eSign arrangement for their own documents | NN-06 |
| P01-AT-22 | Consumer Help account does not expose LawDocs profile data | NN-23 |
| P01-AT-23 | Verification has a non-visual alternative | NN-28 |
| P01-AT-24 | OTPs and identifiers never reach logs | NN-32 |
| P01-AT-25 | Migrated user activates their old account | — |

### V.8.3 P02 — Tenancy, Organisation Structure, User Types and Maker-Checker (`tests/acceptance/p02/`; 24 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P02-AT-01 | A maker cannot approve their own agreement | NN-18 |
| P02-AT-02 | Approval is bound to the version reviewed | NN-18 |
| P02-AT-03 | DoA routes by value and explains why | — |
| P02-AT-04 | No DoA row matches | — |
| P02-AT-05 | A tenant tightens maker-checker without LawDocs | NN-29 |
| P02-AT-06 | A tenant cannot relax a locked action | NN-18 |
| P02-AT-07 | Solo-owner company exports with cooling-off | — |
| P02-AT-08 | Delivery grant needs client approval and ends within 60 seconds of revocation | NN-17 |
| P02-AT-09 | LawDocs staff can never be a checker in a client tenant | NN-17 |
| P02-AT-10 | Break-glass needs two approvers and is reported within 24 hours | NN-17 |
| P02-AT-11 | Group-umbrella admin does not inherit child access | NN-17 |
| P02-AT-12 | Infrabyx staff group grant expires locally | NN-17 |
| P02-AT-13 | Consumer Help case manager cannot also serve lender clients | NN-23 |
| P02-AT-14 | Agents cannot approve | NN-43 |
| P02-AT-15 | Custom role cannot exceed its base ceiling | — |
| P02-AT-16 | Delegation inherits exclusions | — |
| P02-AT-17 | Position-based approver survives a personnel change | — |
| P02-AT-18 | Super admin's master-data change is client-approved and visible | NN-02 |
| P02-AT-19 | Access review auto-revokes unreviewed outsider grants | — |
| P02-AT-20 | No surveillance data exists | NN-33 |
| P02-AT-21 | Context switch changes the data wall | NN-01 |
| P02-AT-22 | Organisation tree is usable by keyboard and screen reader | NN-28 |
| P02-AT-23 | Role-based home meets click budgets | — |
| P02-AT-24 | Access records are exportable | NN-11 |

### V.8.4 P03 — Configuration Studio, Rule Engine and Settings (`tests/acceptance/p03/`; 25 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P03-AT-01 | Unregistered key fails the build | NN-29 |
| P03-AT-02 | Locked value cannot be changed | NN-29 |
| P03-AT-03 | Open change is effective within 60 seconds and undoable | — |
| P03-AT-04 | Maker cannot approve own governed change | NN-18 |
| P03-AT-05 | Critical keys are always maker-checker | NN-18 |
| P03-AT-06 | Plan bounds cascade | — |
| P03-AT-07 | Theme cannot break contrast | NN-28 |
| P03-AT-08 | Individual changes text size in two taps on mobile | — |
| P03-AT-09 | Rule set needs a reviewer of record who is not the maker | NN-30 |
| P03-AT-10 | Code release does not change published rules | NN-30 |
| P03-AT-11 | Excluded instrument is blocked by the eligibility rule | NN-07 |
| P03-AT-12 | Unverified computational row stays indicative | NN-38 |
| P03-AT-13 | Legal clock never pauses while waiting | NN-29 |
| P03-AT-14 | No automatic contact with courts or registries | NN-05 |
| P03-AT-15 | External chaser needs a human send by default | NN-13 NN-34 |
| P03-AT-16 | Pre-approved series stays bounded | NN-34 |
| P03-AT-17 | Agreement cannot be marked executed with an open formality | NN-40 |
| P03-AT-18 | Agent cannot waive or send | NN-43 |
| P03-AT-19 | Kill switch propagates and needs two people to release | NN-39 |
| P03-AT-20 | Super Admin change to a crucial detail needs client approval | NN-02 |
| P03-AT-21 | Configuration template applies with diff and undo | — |
| P03-AT-22 | Import rejects out-of-bound values | — |
| P03-AT-23 | Settings never leak across tenants | NN-01 |
| P03-AT-24 | RM proposes, client approves | — |
| P03-AT-25 | Display numbering never replaces the permanent reference | — |

### V.8.5 P04 — Legal Vault and DMS (`tests/acceptance/p04/`; 24 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P04-AT-01 | Original is immutable and hashed at ingest | NN-09 |
| P04-AT-02 | Aadhaar number masked before commit | NN-04 |
| P04-AT-03 | Folder view change moves no data | NN-12 |
| P04-AT-04 | Search never leaks across tenants or permissions | NN-01 |
| P04-AT-05 | Page-range, view-only, expiring share | — |
| P04-AT-06 | Revocation within 60 seconds | — |
| P04-AT-07 | External share of privileged document needs a checker | NN-18 |
| P04-AT-08 | Agent prepares but cannot send a share | NN-13 NN-43 |
| P04-AT-09 | DigiLocker pull stores URI and verification by default | NN-42 |
| P04-AT-10 | Bulk intake of an LD-EXPORT-1.0 package maps fully and never overwrites | — |
| P04-AT-11 | Conflict on intake becomes a new version | — |
| P04-AT-12 | Bulk delete requires approval | NN-18 |
| P04-AT-13 | Legal hold blocks purge | — |
| P04-AT-14 | Executed instrument cannot be deleted before its floor | — |
| P04-AT-15 | Every P04 record type is in the export map | NN-11 |
| P04-AT-16 | Renewal reminder chain | — |
| P04-AT-17 | Nominee release with cancellable waiting period | — |
| P04-AT-18 | Delivery staff need a grant | NN-17 |
| P04-AT-19 | Health check flags a missing stamp | — |
| P04-AT-20 | Offline cache is encrypted and wiped | NN-44 |
| P04-AT-21 | Share to an ecosystem app only with consent through int | NN-24 |
| P04-AT-22 | Folder tree and intake grid are keyboard and screen-reader operable | NN-28 |
| P04-AT-23 | WhatsApp inbound stays off until assessed | NN-38 |
| P04-AT-24 | Mutation without audit fails | NN-45 |

### V.8.6 P05 — Document Intelligence (`tests/acceptance/p05/`; 20 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P05-AT-01 | Type copy never replaces the original | NN-09 |
| P05-AT-02 | Low-confidence lines must be reviewed before submission | NN-14 |
| P05-AT-03 | Numbers are capped at MEDIUM until confirmed | — |
| P05-AT-04 | Ambiguous WhatsApp date format is asked, not guessed | — |
| P05-AT-05 | Native export parses all locale fixtures without loss | — |
| P05-AT-06 | Aadhaar in handwriting is masked in every derived output | NN-04 |
| P05-AT-07 | Confidential document never routes outside India | NN-15 NN-25 |
| P05-AT-08 | Machine translation cannot enter a filing that needs certification | NN-48 |
| P05-AT-09 | Locked legal terms survive translation | — |
| P05-AT-10 | Back-translation flags meaning drift | — |
| P05-AT-11 | TRUE TYPED COPY needs an advocate's attestation | — |
| P05-AT-12 | s.63 Part A draft for a chat export | NN-10 |
| P05-AT-13 | No s.63 offer for a scan of a paper document | — |
| P05-AT-14 | Agent cannot verify or attach | NN-13 NN-43 |
| P05-AT-15 | Classification tightens the eligibility gate | NN-07 |
| P05-AT-16 | Extraction writes nothing until confirmed | — |
| P05-AT-17 | Annexure pairs carry status | — |
| P05-AT-18 | Engine regression blocks rollout | — |
| P05-AT-19 | Editor is operable by keyboard and screen reader | NN-28 |
| P05-AT-20 | Engine calls are idempotent and reconciled | NN-46 |

### V.8.7 P06 — Template Library and AI Drafting Studio (`tests/acceptance/p06/`; 23 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P06-AT-01 | Anonymous visitor drafts a residential rent agreement for free | — |
| P06-AT-02 | Deterministic assembly (NN-14 template automation) | — |
| P06-AT-03 | Conditional lock-in clause | — |
| P06-AT-04 | Lane escalation warns before converting | — |
| P06-AT-05 | Individual cannot sign or clean-export an unreviewed AI draft | NN-14 |
| P06-AT-06 | One-click professional review | — |
| P06-AT-07 | Company reviewer approves an AI draft internally | — |
| P06-AT-08 | Unverified citation blocks review submission | NN-14 |
| P06-AT-09 | AI pre-fill is off for individuals until verified | NN-38 |
| P06-AT-10 | Will template routes to wet-ink pack | NN-07 |
| P06-AT-11 | Stamp duty is shown as an article reference until the State pack is verified | NN-08 |
| P06-AT-12 | Machine translation is labelled and not operative | NN-48 |
| P06-AT-13 | Bilingual export with governing-language clause | — |
| P06-AT-14 | Maker cannot approve own template | NN-18 |
| P06-AT-15 | Publishing content needs no code release | NN-30 |
| P06-AT-16 | Golden test failure blocks submission | — |
| P06-AT-17 | Open outdated-law item blocks publication and keeps page noindex | — |
| P06-AT-18 | Every content change is audited | NN-02 NN-45 |
| P06-AT-19 | Tenant templates are invisible to other tenants | NN-01 |
| P06-AT-20 | Analytics contain no answers | — |
| P06-AT-21 | Drafts, reviews and tenant templates are exportable | NN-11 |
| P06-AT-22 | No drip pricing on clean download | NN-50 |
| P06-AT-23 | Vidhi cannot export or share | NN-13 |

### V.8.8 P07 — Contract Lifecycle and Deal Rooms (`tests/acceptance/p07/`; 23 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P07-AT-01 | Business user requests an NDA from Teams | — |
| P07-AT-02 | Email from an unknown sender is held | — |
| P07-AT-03 | Internal comments never reach the counterparty | NN-37 |
| P07-AT-04 | Guest sees only shared versions | NN-37 |
| P07-AT-05 | Invitation limits | NN-34 |
| P07-AT-06 | Paste guard | — |
| P07-AT-07 | Silent edits are detected | — |
| P07-AT-08 | Accept all yields the counterparty text | — |
| P07-AT-09 | Each decision is logged | NN-37 |
| P07-AT-10 | Deterministic, versioned comparison | — |
| P07-AT-11 | Suggestions stay internal until adopted | NN-13 NN-43 |
| P07-AT-12 | DoA routes by value and deviation | NN-18 |
| P07-AT-13 | Change invalidates approval | — |
| P07-AT-14 | Delegated maker cannot approve | NN-17 NN-18 |
| P07-AT-15 | Excluded instrument cannot go to eSign | NN-07 |
| P07-AT-16 | Gates checked before signing | NN-08 NN-40 |
| P07-AT-17 | All parties confirm the agreed version | — |
| P07-AT-18 | Unlock voids pending signing | — |
| P07-AT-19 | Key dates need human verification | — |
| P07-AT-20 | Connected rooms replicate only shared artefacts | NN-01 |
| P07-AT-21 | Word check-in catches untracked co-authoring edits | — |
| P07-AT-22 | Agreement export folder | NN-11 |
| P07-AT-23 | Messages are corrected, not deleted | NN-02 NN-45 |

### V.8.9 P08 — eSign, eStamp, Execution and Evidence (`tests/acceptance/p08/`; 29 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P08-AT-01 | Will cannot be routed to eSign | NN-07 |
| P08-AT-02 | Power of attorney in favour of a verified regulated entity uses the carve-out | NN-07 |
| P08-AT-03 | Suspect classification tightens the gate | NN-07 |
| P08-AT-04 | Stamp before sign is locked | NN-08 |
| P08-AT-05 | Attached e-stamp is verified and bound to one document | NN-08 |
| P08-AT-06 | No scraping when no verification API exists | NN-05 |
| P08-AT-07 | Checkout shows duty, fee and GST separately | NN-22 NN-50 |
| P08-AT-08 | Unverified duty row is advisory | NN-38 |
| P08-AT-09 | Aadhaar number in an instrument blocks freezing | NN-04 |
| P08-AT-10 | Aadhaar eSign without Aadhaar data at LawDocs | NN-03 NN-04 |
| P08-AT-11 | Consent version recorded per signer per document | — |
| P08-AT-12 | Name mismatch holds for review | — |
| P08-AT-13 | ESP with lapsed licence is blocked | NN-06 |
| P08-AT-14 | Failover to an alternative method on degraded OTP eSign | — |
| P08-AT-15 | Agent cannot send or sign | NN-13 NN-43 |
| P08-AT-16 | Assisted operator cannot sign for a signer | — |
| P08-AT-17 | Internal notes never reach counterparties | NN-37 |
| P08-AT-18 | Request changes voids the request | — |
| P08-AT-19 | Registration pending prevents Executed | NN-40 |
| P08-AT-20 | Stamp cannot be waived on the electronic route | NN-40 |
| P08-AT-21 | Evidence pack and s.63 draft on completion | NN-10 |
| P08-AT-22 | Signature validation failure blocks Executed | — |
| P08-AT-23 | eSign credits charged once and only on success | NN-46 |
| P08-AT-24 | No sign-on-behalf API for ecosystem apps | NN-06 |
| P08-AT-25 | Affidavit approved for swearing is not presented as sworn | — |
| P08-AT-26 | Visually impaired signer signs with a helper and witness; consent recorded | NN-28 NN-03 |
| P08-AT-27 | Signer who cannot perform the signing step is routed to wet ink, not signed for | NN-07 |
| P08-AT-28 | Agreement for sale follows Appendix F, not the R5 flag | NN-07 |
| P08-AT-29 | Ecosystem product hands off to a LawDocs-hosted signing page | NN-06 |

### V.8.10 P09 — Vidhi AI Employee and Agent Workforce (`tests/acceptance/p09/`; 25 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P09-AT-01 | Confidential data never leaves the India route | NN-15 NN-25 |
| P09-AT-02 | Fabricated citation is blocked from display as verified | NN-14 |
| P09-AT-03 | AI-custom draft for an individual cannot be signed before qualified review | NN-14 |
| P09-AT-04 | Qualified review stamps and releases the draft | NN-14 |
| P09-AT-05 | Agent cannot send an external legal notice | NN-13 NN-43 |
| P09-AT-06 | Agent tokens are rejected on approval endpoints | NN-18 NN-43 |
| P09-AT-07 | Autonomy raise needs a different checker | NN-18 |
| P09-AT-08 | Tenant kill switch stops agents within 60 seconds | NN-39 |
| P09-AT-09 | Retrieval never returns another tenant's canary | NN-01 |
| P09-AT-10 | Retrieval respects document permissions | NN-01 |
| P09-AT-11 | Aadhaar number is masked before any model call and absent from logs | NN-04 NN-32 |
| P09-AT-12 | Prompt injection inside an uploaded WhatsApp export is ignored | — |
| P09-AT-13 | Emergency triage bypasses the payment wall | — |
| P09-AT-14 | Outcome promises and advocate rankings are filtered | NN-20 NN-21 |
| P09-AT-15 | Outbound AI call blocked for an undeclared CLI | NN-34 |
| P09-AT-16 | Enumerated send plan change needs fresh confirmation | NN-13 |
| P09-AT-17 | Daily digest lists actions with undo | — |
| P09-AT-18 | Budget hard stop | — |
| P09-AT-19 | Unverified provider stays off | NN-38 |
| P09-AT-20 | Machine translation is labelled | NN-48 |
| P09-AT-21 | MCP server exposes no prohibited tool | — |
| P09-AT-22 | MCP client tool description change suspends the tool | — |
| P09-AT-23 | AI work products are exportable | NN-11 |
| P09-AT-24 | Vidhi chat is screen-reader operable | NN-28 |
| P09-AT-25 | Agent action and audit entry are atomic | NN-02 NN-45 |

### V.8.11 P10 — Pleadings, Notices and Court Drafting (`tests/acceptance/p10/`; 20 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P10-AT-01 | Supreme Court profile tokens | — |
| P10-AT-02 | Unverified profile is never "court-ready" | NN-20 |
| P10-AT-03 | Annexure index matches text | — |
| P10-AT-04 | Old section search maps to BNSS | — |
| P10-AT-05 | Old law cannot be cited as current | — |
| P10-AT-06 | WhatsApp screenshot with typed copy and translation | NN-09 NN-48 |
| P10-AT-07 | s.63(4) certificate for electronic records | NN-10 |
| P10-AT-08 | Certified translation required | — |
| P10-AT-09 | PDF/A with bookmarks and split | — |
| P10-AT-10 | No automated filing | NN-05 NN-13 |
| P10-AT-11 | Unverified limitation row shows no date | NN-38 |
| P10-AT-12 | Verified row computes an advisory date | — |
| P10-AT-13 | s.138 timeline | — |
| P10-AT-14 | Notice dispatch needs explicit confirmation | NN-13 |
| P10-AT-15 | Advocate notice is in the advocate's name | — |
| P10-AT-16 | AI-assisted pleading for an individual needs review | NN-14 |
| P10-AT-17 | Criminal applications always need review | — |
| P10-AT-18 | Legal aid prompt | — |
| P10-AT-19 | Affidavit mismatch | — |
| P10-AT-20 | Export folders | NN-11 |

### V.8.12 P11 — Litigation and Matter Management (`tests/acceptance/p11/`; 23 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P11-AT-01 | Add a district-court case by CNR with a licensed source | — |
| P11-AT-02 | Duplicate CNR is refused | — |
| P11-AT-03 | No court portal automation exists | NN-05 |
| P11-AT-04 | Vendor data is never labelled official or real-time | NN-20 |
| P11-AT-05 | Counsel entry prevails over vendor data | — |
| P11-AT-06 | Failover to Vendor B and then to manual mode | — |
| P11-AT-07 | Cause-list match triggers next-day alert | — |
| P11-AT-08 | Missing outcome is chased and escalated | — |
| P11-AT-09 | Order digest creates tasks only after human confirmation | NN-14 NN-43 |
| P11-AT-10 | Unverified limitation rule is advisory | NN-38 |
| P11-AT-11 | Clock never pauses while waiting for documents | — |
| P11-AT-12 | Matter cannot close with an open clock | — |
| P11-AT-13 | External counsel sees only assigned matters | NN-01 |
| P11-AT-14 | Contingency fee for an advocate is blocked | NN-21 |
| P11-AT-15 | Invoice approver must differ from maker | NN-18 |
| P11-AT-16 | Exposure class is human-set and schedule freezes | — |
| P11-AT-17 | Plain-language status in Hindi with screen reader | NN-28 |
| P11-AT-18 | Add a case in three taps on mobile | — |
| P11-AT-19 | Recovery Suite case is read-only | NN-24 |
| P11-AT-20 | No matter content reaches the Operations Hub | NN-19 |
| P11-AT-21 | ADR referral uses the interim manual channel until v1.2 contracts are enabled | — |
| P11-AT-22 | Import undo uses correction entries | NN-02 |
| P11-AT-23 | Litigation export folder structure | NN-11 |

### V.8.13 P12 — IP and Trademark Portfolio (`tests/acceptance/p12/`; 15 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P12-AT-01 | Add a mark by application number | — |
| P12-AT-02 | No IP India portal automation | NN-05 |
| P12-AT-03 | Assisted refresh from a status PDF | — |
| P12-AT-04 | Examination reply clock is advisory until verified | NN-38 |
| P12-AT-05 | Validity computed from filing date | — |
| P12-AT-06 | Status wording is honest | NN-20 |
| P12-AT-07 | Class finder suggests classes with reasons and a disclaimer | NN-14 |
| P12-AT-08 | Screening never concludes registrability | — |
| P12-AT-09 | LawDocs prepares, the agent files, fees are separate | NN-13 NN-22 |
| P12-AT-10 | Similar mark in the Journal creates a hit with opposition last date | — |
| P12-AT-11 | Oppose from a hit creates a P11 matter | — |
| P12-AT-12 | Undecided hit escalates | — |
| P12-AT-13 | Automated Journal fetching stays off | NN-38 |
| P12-AT-14 | Ownership gap is detected and closed by recordal | — |
| P12-AT-15 | IP export folder structure | NN-11 |

### V.8.14 P13 — Legal Department OS, Governance and HRMS (`tests/acceptance/p13/`; 25 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P13-AT-01 | Business user raises a request in three clicks | — |
| P13-AT-02 | Sensitive request is never auto-triaged | — |
| P13-AT-03 | Self-service NDA within guardrails, escalation outside | — |
| P13-AT-04 | SLA pauses only for permitted reasons and never for statutory clocks | — |
| P13-AT-05 | Approval within DoA, maker cannot approve | NN-18 |
| P13-AT-06 | LDC is system of record when linked | NN-47 |
| P13-AT-07 | LDC unavailable blocks finalising actions | — |
| P13-AT-08 | Switch to LDC reconciles sealed minutes before cutover | NN-12 |
| P13-AT-09 | Board meeting cadence warning | — |
| P13-AT-10 | Shorter notice requires the urgency path | — |
| P13-AT-11 | VC attendance checklist | — |
| P13-AT-12 | Sealed minutes cannot be altered by anyone | NN-02 NN-09 |
| P13-AT-13 | Minutes writer cannot invent attendance or votes | NN-43 |
| P13-AT-14 | Circular resolution referred to a meeting | — |
| P13-AT-15 | Meeting-only matter blocked from circulation | — |
| P13-AT-16 | Follow-on filing task from a special resolution | — |
| P13-AT-17 | KMP vacancy clock | — |
| P13-AT-18 | Duties follow the position | — |
| P13-AT-19 | Adopt NBFC-ML template and customise | — |
| P13-AT-20 | RBI overlay is advisory until verified | NN-38 |
| P13-AT-21 | Segregation-of-duties warning | — |
| P13-AT-22 | No surveillance data can be captured | NN-33 |
| P13-AT-23 | Wage base 50 percent rule | — |
| P13-AT-24 | POSH content stays sealed | NN-19 |
| P13-AT-25 | Governance and HR export folders | NN-11 |

### V.8.15 P14 — Business Services and Tax (`tests/acceptance/p14/`; 20 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P14-AT-01 | Non-subscriber buys Pvt Ltd incorporation with a full fee breakdown | — |
| P14-AT-02 | Certification blocked for a non-practising performer | NN-41 |
| P14-AT-03 | Practising CA cannot be listed or paid a referral | NN-21 |
| P14-AT-04 | Government fee is not collected in advance into a LawDocs account | NN-22 |
| P14-AT-05 | Startup bundle has no pre-ticked or hidden recurring item | NN-50 |
| P14-AT-06 | Trust deed routed to wet-ink pack | NN-07 |
| P14-AT-07 | Partnership deed cannot be marked executed without stamp | NN-40 |
| P14-AT-08 | ITR flow never requests an OTP or password | NN-16 CH-10 |
| P14-AT-09 | Unverified tax-year rule pack blocks upload | NN-38 |
| P14-AT-10 | Agent cannot file | NN-13 |
| P14-AT-11 | No portal scraping for status | NN-05 |
| P14-AT-12 | LDC is system of record for obligations | NN-47 |
| P14-AT-13 | Fee schedule change needs a checker | NN-18 |
| P14-AT-14 | Claims lint | NN-20 |
| P14-AT-15 | SLA clock pauses while waiting on the customer | — |
| P14-AT-16 | Renewal obligation from FSSAI licence | — |
| P14-AT-17 | Export includes orders and tax files | NN-11 |
| P14-AT-18 | BYO professional access is scoped and time-bound | NN-17 |
| P14-AT-19 | Cross-tenant order access is denied | NN-01 |
| P14-AT-20 | Udyam guided flow states that registration is free | — |

### V.8.16 P15 — Consumer Help (`tests/acceptance/p15/`; 24 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P15-AT-01 | Consumer Help data never reaches a lender tenant | NN-23 |
| P15-AT-02 | Conflict hit limits the case to self-serve | NN-23 |
| P15-AT-03 | Conflict service unavailable fails closed | NN-23 |
| P15-AT-04 | Advocate cannot be the representative before the RBI Ombudsman | NN-23 |
| P15-AT-05 | RBIO window uses the later-of rule | — |
| P15-AT-06 | LawDocs never collects a challan fine | NN-22 NN-23 |
| P15-AT-07 | Challan lookup is user-initiated on the official portal | NN-05 |
| P15-AT-08 | Banned phrase blocks a letter | NN-20 |
| P15-AT-09 | Agent cannot send a letter | NN-13 |
| P15-AT-10 | Evidence bundle with hashes and s.63 certificate | NN-09 NN-10 |
| P15-AT-11 | Aadhaar masked in typed copies | NN-04 |
| P15-AT-12 | Success fee cannot be switched on without counsel and checker | CH-31 |
| P15-AT-13 | No advocate shares in a success fee | NN-21 |
| P15-AT-14 | Claim above the ombudsman cap routes by consideration paid, not claim value | — |
| P15-AT-15 | Credit report compensation tracker | — |
| P15-AT-16 | RTO power of attorney goes to wet-ink | NN-07 |
| P15-AT-17 | Vehicle sale agreement not executed without stamp where duty applies | NN-40 |
| P15-AT-18 | RC transfer deadline alerts | — |
| P15-AT-19 | Case manager sees only cases in the Consumer Help scope | NN-17 |
| P15-AT-20 | No automated calls | NN-34 |
| P15-AT-21 | Consent withdrawal stops advocate sharing | NN-26 |
| P15-AT-22 | Fee sheet before acceptance | NN-50 |
| P15-AT-23 | Vehicle-loan papers and hypothecated sale (FR-P15-70) | NN-40 |
| P15-AT-24 | No loan sourcing, comparison or referral from the vehicle-loan journey (FR-P15-70) | NN-23 NN-19 |

### V.8.17 P16 — Marketplace, Registry, Retainers and Academy (`tests/acceptance/p16/`; 29 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P16-AT-01 | Browse and read a landed price card without login | — |
| P16-AT-02 | Price card lint blocks drip pricing | NN-50 |
| P16-AT-03 | Buy a fixed-price service with a Free account | R-040 |
| P16-AT-04 | Advocate commercial fields cannot be enabled | NN-21 |
| P16-AT-05 | Advocate responses never contain ratings or fees per person | NN-21 |
| P16-AT-06 | CA listing switch needs counsel opinion and a different checker | NN-18 NN-21 |
| P16-AT-07 | Reserved service cannot be supplied by LawDocs | NN-41 |
| P16-AT-08 | Professional fee goes only through Route on hold | NN-22 |
| P16-AT-09 | Duplicate release is idempotent | NN-46 |
| P16-AT-10 | Consult no-show auto-refund | — |
| P16-AT-11 | Conflict hit blocks the offer | — |
| P16-AT-12 | Consumer Help request routes behind the ethical wall | NN-23 |
| P16-AT-13 | Success fee is unavailable where an advocate acts | CH-31 |
| P16-AT-14 | Retainer activation proposes RM-as-maker grants | NN-17 R-064 |
| P16-AT-15 | SLA schedule is eSigned before activation | — |
| P16-AT-16 | Hour bank hard stop | — |
| P16-AT-17 | SLA breach creates a service credit request | — |
| P16-AT-18 | Review is about the LawDocs service and shows no photo | NN-49 R-088 |
| P16-AT-19 | Engagement records appear in the export | NN-11 |
| P16-AT-20 | Stale Academy feed hides prices | D-16 |
| P16-AT-21 | LawDocsComply listing routes only with consent | NN-24 |
| P16-AT-22 | No sponsored placement exists | NN-35 |
| P16-AT-23 | Agent cannot send an offer | NN-13 |
| P16-AT-24 | Prohibited claim words fail lint | NN-20 |
| P16-AT-25 | Engagement of another tenant is not reachable | NN-01 |
| P16-AT-26 | Quote-request lead carries contact data only | NN-19 |
| P16-AT-27 | Profession kill switch stops new assignments | NN-39 |
| P16-AT-28 | AI-drafted deliverable for an individual stays labelled until reviewed | NN-14 |
| P16-AT-29 | State change and audit entry are atomic | NN-45 |

### V.8.18 P17 — Plans, Billing, Revenue Streams and Savings (`tests/acceptance/p17/`; 22 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P17-AT-01 | Pricing card shows total including GST | NN-50 |
| P17-AT-02 | No strike-through without price history | NN-50 |
| P17-AT-03 | Upgrade with prorated quote | — |
| P17-AT-04 | Lapse never blocks read or export | NN-11 |
| P17-AT-05 | Cancellation is as easy as purchase | NN-50 |
| P17-AT-06 | Trial never converts automatically | — |
| P17-AT-07 | Browser redirect is not proof of payment | NN-22 |
| P17-AT-08 | Failed eSign returns the credit | — |
| P17-AT-09 | Credits cannot pay third parties | — |
| P17-AT-10 | Usage statement is idempotent and aggregate only | NN-46 |
| P17-AT-11 | Stream switch needs a checker and kills within 5 minutes | NN-18 NN-39 |
| P17-AT-12 | Deny-listed streams cannot be enabled | NN-21 |
| P17-AT-13 | Advertising off by default and never in private areas | NN-35 |
| P17-AT-14 | Avoided exposure is labelled and excluded from savings | NN-36 |
| P17-AT-15 | Stale benchmark excluded | NN-20 NN-36 |
| P17-AT-16 | Invoice e-mailed and filed | — |
| P17-AT-17 | Tenant changes credit consumption order without Super Admin | NN-29 |
| P17-AT-18 | Mobile purchase mode stays web hand-off until verified | NN-38 |
| P17-AT-19 | OH8 rejects a statement with a document identifier | NN-19 |
| P17-AT-20 | Purchase approval for companies | — |
| P17-AT-21 | Billing documents are tenant-isolated | NN-01 |
| P17-AT-22 | Credit consumption is atomic with the business event | NN-45 NN-46 |

### V.8.19 P18 — Delivery Console and Operations Hub Interface (`tests/acceptance/p18/`; 30 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P18-AT-01 | LawDocs proposes, client approves, RM works as maker | — |
| P18-AT-02 | A delivery user can never be a checker | NN-17 |
| P18-AT-03 | Super Admin cannot approve a grant for the client | NN-17 |
| P18-AT-04 | Standing authorisation activates a maker with notice | — |
| P18-AT-05 | Multiple makers across departments | — |
| P18-AT-06 | Federated inbox never crosses tenants | NN-01 |
| P18-AT-07 | Leaver sweep | NN-02 NN-45 |
| P18-AT-08 | Vault is OFF by default and needs maker-checker to enable | NN-16 |
| P18-AT-09 | Delegation is offered first | NN-16 |
| P18-AT-10 | OTP seeds and DSC PINs cannot be stored | NN-16 |
| P18-AT-11 | RBI CIMS credential is client-only by default | NN-16 |
| P18-AT-12 | Just-in-time reveal is logged, notified and absent from logs | NN-16 NN-32 |
| P18-AT-13 | Export carries vault metadata, never secrets | NN-11 |
| P18-AT-14 | Registered office change needs client approval and a second Super Admin | NN-18 |
| P18-AT-15 | Maker cannot be checker | NN-18 |
| P18-AT-16 | Owner email change notifies both channels | — |
| P18-AT-17 | Reviewer must differ from author | — |
| P18-AT-18 | Final deliverable is filed in the DMS and optionally copied to the client's drive | NN-11 NN-46 |
| P18-AT-19 | Residency guard blocks regulated working copies on Google Workspace | NN-25 |
| P18-AT-20 | Billing tab equals the client's billing page | — |
| P18-AT-21 | People wall | NN-23 |
| P18-AT-22 | Conflict check returns only a flag | NN-23 |
| P18-AT-23 | No dues collection and no outcome promises | NN-23 |
| P18-AT-24 | Advocate profile shows Rule 36 fields only | NN-21 |
| P18-AT-25 | LawDocs cannot edit an advocate's released opinion | NN-41 |
| P18-AT-26 | No content to the Hub | NN-19 NN-24 |
| P18-AT-27 | No monitoring settings exist | NN-33 |
| P18-AT-28 | RM-started agent output needs the client's checker | NN-13 NN-43 |
| P18-AT-29 | Emergency stop for reveals | NN-39 |
| P18-AT-30 | Delivery banner is accessible | NN-28 |

### V.8.20 P19 — Integration Gateway and Developer Platform (`tests/acceptance/p19/`; 27 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P19-AT-01 | Cross-tenant id is rejected | NN-01 |
| P19-AT-02 | Idempotency key reuse with a different body | NN-46 |
| P19-AT-03 | Webhook retries then DLQ | — |
| P19-AT-04 | DLQ replay needs a different approver | NN-18 |
| P19-AT-05 | Personal data without consent or legal basis is rejected | NN-24 |
| P19-AT-06 | Appendix Y contracts are inert until approved | NN-38 |
| P19-AT-07 | A sister product cannot use LawDocs' ESP route | NN-06 |
| P19-AT-08 | Hosted signing hand-off keeps the ceremony in LawDocs | NN-06 |
| P19-AT-09 | Ineligible instrument via API gets a wet-ink pack | NN-07 |
| P19-AT-10 | The Operations Hub receives aggregates only | NN-19 |
| P19-AT-11 | No ecosystem client can reach Consumer Help | NN-23 |
| P19-AT-12 | Udofin deposit is verified and immutable | — |
| P19-AT-13 | Kernel system-of-record switch to LawDocsComply loses nothing | NN-47 |
| P19-AT-14 | Finbyx recovery litigation is read-only in LawDocs | — |
| P19-AT-15 | Equator is shown neutrally with disclosure | — |
| P19-AT-16 | Referral pack needs human approval | NN-13 |
| P19-AT-17 | Award arrives in the vault with advisory clocks | — |
| P19-AT-18 | Partner batch with KYB pre-fill and consent | — |
| P19-AT-19 | No scraping and no bureau, CKYC or PAN-database calls during onboarding | NN-05 |
| P19-AT-20 | Individuals cannot be bulk-onboarded by an ecosystem client | — |
| P19-AT-21 | Counterparty contact limit on API-created signing requests | NN-34 |
| P19-AT-22 | Adapter kill switch | NN-39 |
| P19-AT-23 | Automation platform data ceiling | NN-25 |
| P19-AT-24 | Integration logs carry no personal data | NN-32 |
| P19-AT-25 | Sharing ledger is exportable | NN-11 |
| P19-AT-26 | LawDocs is not a lender, RE, LSP or DSA (FR-P19-84) | NN-05 NN-19 NN-23 |
| P19-AT-27 | Proposed service-order and OH metric events stay inert until Appendix Y is merged | NN-24 |

### V.8.21 P20 — Data Preservation and Portability (`tests/acceptance/p20/`; 22 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P20-AT-01 | Every record type is exportable | NN-11 |
| P20-AT-02 | Missing export mapping fails CI | NN-11 |
| P20-AT-03 | Paths are stable across a release with schema changes | NN-12 |
| P20-AT-04 | Renaming a department does not move files | NN-12 |
| P20-AT-05 | Offline verification detects tampering | NN-10 |
| P20-AT-06 | No Aadhaar number in any export | NN-04 |
| P20-AT-07 | Company full export needs a second approver | NN-18 |
| P20-AT-08 | Individual exports everything without staff help | NN-11 |
| P20-AT-09 | Export is never blocked by billing state | NN-11 |
| P20-AT-10 | Regulated data refused for Google Drive | NN-25 |
| P20-AT-11 | Customer-modified file is never overwritten | — |
| P20-AT-12 | Mirror is idempotent after a release | NN-46 |
| P20-AT-13 | Revoked credential pauses safely | — |
| P20-AT-14 | Import commits only after human review | NN-13 |
| P20-AT-15 | Duplicates are linked not copied | — |
| P20-AT-16 | Import undo removes only what it created | — |
| P20-AT-17 | LD package round trip places exactly | — |
| P20-AT-18 | Individual closure honours erasure with notice and retention exceptions | NN-26 |
| P20-AT-19 | Ops Hub receives counts only | NN-19 |
| P20-AT-20 | RM cannot run a full export | NN-17 |
| P20-AT-21 | Path rules keep archives openable | — |
| P20-AT-22 | DigiLocker document exported as reference | NN-42 |

### V.8.22 P21 — Public Website, CMS, Help Centre and Accessibility (`tests/acceptance/p21/`; 29 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P21-AT-01 | Every sitemap URL renders without JavaScript | NN-31 |
| P21-AT-02 | Legacy URLs resolve in one hop | — |
| P21-AT-03 | Non-eligible instrument shows a wet-ink pack instead of eSign | NN-07 |
| P21-AT-04 | AI-custom lane output is labelled | NN-14 |
| P21-AT-05 | Testimonial about an advocate is rejected | NN-21 NN-49 |
| P21-AT-06 | Fee breakdown is shown before payment | NN-22 |
| P21-AT-07 | Unapproved claim blocks publication | NN-20 |
| P21-AT-08 | Maker cannot approve own post | NN-18 |
| P21-AT-09 | DOCX import from categorised folders creates drafts | — |
| P21-AT-10 | Outdated law is flagged | — |
| P21-AT-11 | Copied competitor content is blocked | — |
| P21-AT-12 | State variant without material differences is blocked | — |
| P21-AT-13 | Page without a reviewer is not indexed | NN-30 |
| P21-AT-14 | Lead hand-off carries consent and no draft content | NN-19 NN-26 |
| P21-AT-15 | Sensitive intent is excluded from ad conversions | — |
| P21-AT-16 | Countdown without a real event is blocked | NN-50 |
| P21-AT-17 | Video loads nothing from YouTube before activation | — |
| P21-AT-18 | Machine-translated page is not published without review | NN-48 |
| P21-AT-19 | "i" popover meets content-on-hover rules | NN-28 |
| P21-AT-20 | Untagged jargon fails the build | — |
| P21-AT-21 | Tutorial capture refuses a real tenant | — |
| P21-AT-22 | Stale tutorial is flagged after a UI change | — |
| P21-AT-23 | Advertising slot stays empty when the stream is OFF | NN-35 |
| P21-AT-24 | Tenant help notes and accessibility preferences are exported | NN-11 |
| P21-AT-25 | Accessibility feedback is acknowledged on time | NN-28 |
| P21-AT-26 | Free tool with an unverified rule stays disabled | NN-38 |
| P21-AT-27 | Drafter answers never reach analytics or logs | NN-32 |
| P21-AT-28 | Publishing writes the audit ledger in the same transaction | NN-02 NN-45 |
| P21-AT-29 | Unregistered setting cannot be read | NN-29 |

### V.8.23 P22 — Mobile Apps and Store Release (`tests/acceptance/p22/`; 31 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P22-AT-01 | Aadhaar is never offered as a login method | NN-03 |
| P22-AT-02 | Biometric enrolment change forces re-login | NN-44 |
| P22-AT-03 | Offline cache is encrypted and wiped on revoke | NN-44 |
| P22-AT-04 | Integrity failure restricts the app | NN-44 |
| P22-AT-05 | Aadhaar number is masked before upload | NN-04 |
| P22-AT-06 | Capture hashes are preserved | NN-09 |
| P22-AT-07 | WhatsApp export becomes a transcript rendition | — |
| P22-AT-08 | Excluded instrument cannot be routed to eSign on mobile | NN-07 |
| P22-AT-09 | Stamp before sign | NN-08 |
| P22-AT-10 | Signing status comes only from the server | NN-06 |
| P22-AT-11 | Guest signs from a link without installing the app | — |
| P22-AT-12 | Internal comment cannot reach the counterparty | NN-37 |
| P22-AT-13 | Approval from push requires step-up and maker is not checker | NN-18 |
| P22-AT-14 | Court status is labelled with freshness | NN-20 |
| P22-AT-15 | Vidhi voice session discloses AI and confirms transcript | NN-14 |
| P22-AT-16 | Marketplace payment shows full breakdown and confirms by webhook | NN-22 |
| P22-AT-17 | Digital items are not sold in the iOS app by default | — |
| P22-AT-18 | Crash report contains no personal data | NN-32 |
| P22-AT-19 | OTA cannot change purchase behaviour | — |
| P22-AT-20 | Staged OTA rolls back on crash regression | — |
| P22-AT-21 | Critical journeys pass screen-reader scripts | NN-28 |
| P22-AT-22 | Export everything from mobile | NN-11 |
| P22-AT-23 | Consumer Help flavour excludes lender-facing modules | NN-23 |
| P22-AT-24 | Account deletion explains retention and offers export | — |
| P22-AT-25 | Workspace switch never shows another tenant's cached data | NN-01 |
| P22-AT-26 | Vidhi cannot share a document without confirmation | NN-13 |
| P22-AT-27 | Counterparty receives one invitation and no automated calls | NN-34 |
| P22-AT-28 | Retried approval from the outbox is applied once | NN-46 |
| P22-AT-29 | Analytics wait for consent | NN-26 |
| P22-AT-30 | Listening to a machine translation carries a spoken disclaimer | NN-48 |
| P22-AT-31 | Store subscription shows renewal terms and an equally easy cancellation | NN-50 |

### V.8.24 P23 — Engineering Governance and Go-Live (`tests/acceptance/p23/`; 25 scenarios)

| Tag | Title | Tags |
|---|---|---|
| P23-AT-01 | Deployment without ChangeApproved is refused | NN-18 |
| P23-AT-02 | Author cannot approve own release | NN-18 |
| P23-AT-03 | Unsigned commit blocked on main | — |
| P23-AT-04 | Destructive migration in the same release is blocked | NN-12 |
| P23-AT-05 | Migration touching an export-mapped column without mapping update fails | NN-12 |
| P23-AT-06 | Code release does not alter published content | NN-30 |
| P23-AT-07 | Critical vulnerability follows the emergency lane | — |
| P23-AT-08 | Risk acceptance expires | — |
| P23-AT-09 | Weekly restore test proves recoverability | — |
| P23-AT-10 | Missed restore test counts as failed | — |
| P23-AT-11 | Log retention floor is enforced | NN-27 |
| P23-AT-12 | Infrastructure outside India is blocked | NN-25 |
| P23-AT-13 | CERT-In clock starts at detection | NN-27 |
| P23-AT-14 | Public page cannot claim certification without evidence | NN-20 |
| P23-AT-15 | PCI scope stays SAQ A | — |
| P23-AT-16 | Accessibility blocks ring2 promotion | NN-28 |
| P23-AT-17 | Go-live blocked by a live VERIFY-dependent flag | NN-38 |
| P23-AT-18 | Kill-switch drills are part of go-live | NN-39 |
| P23-AT-19 | Hypercare exit requires stability | — |
| P23-AT-20 | Region failover keeps the audit chain intact | NN-02 |
| P23-AT-21 | AI model change needs evaluation and canary | — |
| P23-AT-22 | No secrets or Aadhaar in logs | NN-32 |
| P23-AT-23 | Phase completion report cannot claim unevidenced results (FR-P23-58) | NN-20 |
| P23-AT-24 | Proposal before material implementation (FR-P23-58) | — |
| P23-AT-25 | Traceability and verification checks are required | — |

---

## V.9 Gaps found in phases at compilation

| # | Gap | Effect | Resolution | Owner |
|---|---|---|---|---|
| G-01 | Ten NN rules had ≤ 3 scenarios or a single phase: NN-03, NN-15, NN-27, NN-31, NN-33, NN-35, NN-36, NN-41, NN-44, NN-49. | Weak proof of non-negotiables. | 28 supplementary scenarios `@APPV-AT-01…28` (§V.4). | QA lead + named owners |
| G-02 | Phase-owner gaps: P09 (agents vs credential vault), P11 (offline cause-list cache), P13 (board approval as a formality), P14 (penalty-avoided evidence), P15 (protected screens, no ads in cases), P07 (deal-room machine translation), P10 (WhatsApp dispatch), P23 (DPDP breach intimation). | Rules relied on in FRs but untested in the owning phase. | Closed by APPV-AT-09, -12, -15, -16, -19, -20, -21, -22, -23. Phase authors may move them into their §12 at integration, keeping the tags. | Phase authors |
| G-03 | No phase tests the Appendix C shell surfaces (command palette, universal search, home customisation, upsell rules, click-budget gates). | Palette could bypass confirmations; search could leak across contexts. | APPV-AT-24–28 and the journey suite J-01–J-40. | P03, P23 |
| G-04 | No phase scenario carries `@role-<code>` tags. | UAT and access tests cannot be filtered by persona. | Add role tags when the `.feature` files are written; QA lint warns on scenarios without a role tag. | Phase authors |
| G-05 | Only four phase scenarios assert click budgets (P02-AT-23, P03-AT-08, P11-AT-18, P13-AT-01) although every phase §6 states budgets. | Budgets unenforced. | Journey suite (§V.1) is the gate; phase budgets are compiled in Appendix C §C.8. | P23 |
| G-06 | 195 of 582 scenarios carry no NN tag (registry review G4 recount); several of them do prove an NN rule in substance (for example P04-AT-05/06 share expiry and revocation, P11-AT-11 clock never pauses). | NN suite under-counts. | Phase authors review untagged scenarios and add NN tags where the scenario proves a rule. | Phase authors |
| G-07 | Environment names differ: P00 FR-P00-14 (`local`, `dev`, `staging`, `uat`, `prod`, `dr`, `mig`) vs P23 FR-P23-07 (`local`, `dev`, `test`, `staging`, `pre-prod`, `prod`, `dr`). | UAT location ambiguous; IaC naming drift. | Owner decision [OWNER]; recommended: keep P00's account `ld-uat` and name the stage `uat`, add `test` as in P23, treat `pre-prod` as the `uat` stage's release-rehearsal use. | P00, P23 |
| G-08 | P10 and P23 §6 tables omit template columns (P10 lacks "Empty / error states"; P23 lacks mobile and accessibility columns); P11–P13 merge the screen name into the ID column. | Cosmetic; compiled correctly into Appendix C §C.15. | Align at integration. | P10, P11, P12, P13, P23 |
| G-09 | Thin persona coverage for `ORG_AUDITOR_RO` and `ORG_BOARD_OBSERVER` in scenarios (read-only scope and watermarking asserted only indirectly). | Read-only roles could gain write controls unnoticed. | Add a P02 or P13 scenario: auditor and board observer see no mutate controls and receive watermarked downloads. | P02, P13 |
| G-10 | No scenario covers counterparties who are blind or Deaf completing signing via assisted routes without extra charge (Appendix U §U.7.4). | Accessibility of the signing ceremony is not proved end to end. | Covered by UAT U-18 and APPV-AT-28; recommend a P08 scenario for the second-ESP or assisted route at no extra charge. | P08 |
| G-11 | FR-P15-70, FR-P19-84 and FR-P23-58 (added at traceability review) had no scenarios. | Requirements unproved. | Added P15-AT-23/24, P19-AT-26/27, P23-AT-23/24/25 (integration review F2). | Closed |

---

*End of Appendix V.*
