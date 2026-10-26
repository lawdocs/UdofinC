# A9_ID_VENDOR — summary (22 Oct 2026)

87 items: 14 verified, 4 corrected, 2 provisional, 21 counsel sign-off, 30 vendor confirmation, 13 product decision, 3 watch. 42 edits proposed, each `old` string checked unique.

**Limitation:** the shared web-search budget ran out partway through. Items not re-searched say so and stay open: India Post, ONDC IGM, MSME ODR API, ReBIT purpose codes, r.8B, Income-tax Act 2025 sections, CICRA, Advocates Act s.33, ICAO PKD.

## Key findings
- **BCI CoP Rules 2015 r.9.1:** a CoP is valid 5 years and verified every 5 years (apply up to 6 months before expiry). Use "verification", not "renewal". Annual re-checks are stricter Equator policy.
- **ElevenLabs:** paths and India base URL `api.in.residency.elevenlabs.io` confirmed. Corrected: simulate-conversation is deprecated; use Agent Testing (`/agents/{id}/run-tests`).
- **Callbacks:**
  - Sarvam sends a static token in `X-SARVAM-JOB-CALLBACK-TOKEN`, not an HMAC.
  - Exotel and MSG91 are unsigned.
  - MSG91's reference field is `CRQID` (corrected).
  - Digio uses `X-Digio-Checksum` (HMAC-SHA256) plus fixed IPs.
  - Setu shows only an unsigned redirect; its headers are confirmed.
- **Setu eStamp:** 17 States/UTs digital; MH, TG and WB physical-only, matching the pack. Leegality shows 31.
- **Razorpay:** capture within 3 days or automatic refund, so capture-then-refund is right.
- **Bedrock:**
  - `in.` profiles for Opus 5, Sonnet 5 and Haiku 4.5 route only Mumbai–Hyderabad. Prompt caching confirmed; per-model Citations not stated.
  - New risks: Haiku 4.5 on the India profile has no structured outputs. Haiku 5.5 is Global-only and unfit for personal data.
- **Expo:** SDKs 56–58 need iOS 16.4 / Android 7. Latest SDK is 58.
- **Cashfree:** `x-idempotency-key` confirmed.
- **Aadhaar:**
  - G.S.R. 88(E) of 31 Jan 2025 verified on eGazette.
  - 9 Dec 2025 OVSE amendment: HQ-30011/5/2025-AU-HO per secondary sources (reg.13A OVSE registration, AVC, offline face verification). Fees and credential retention not public.
- **Sahamati (corrected):** no "Vikalp" programme. It is the "Inter-Member dispute resolution framework"; empanelment CLOSED.

## The other AI's claims
- **Face-match:** thresholds are rightly provisional. Add one rule: a low score never auto-rejects; it routes to retry, manual review or video KYC. Calibrate thresholds per vendor (FMR/FNMR, ISO/IEC 19795-1). This is Equator policy, not law.
- **Bar Council roll lookups:** right that scraping is barred and enablement goes State by State. Official portals (e.g., Delhi) publish no API or automated-use terms, and Delhi's portal faced a Delhi HC privacy challenge (Sept 2026). Enable only with each Council's written permission.
- **BCI r.36:** substantially right. The 2008 Schedule allows only name, contact, enrolment particulars, qualifications and practice areas. Madras HC (*P.N. Vignesh*, 2024) and BCI tightened enforcement; SC appeal pending. Reach to neutral profiles is untested, so counsel sign-off.
- **Escrow:** right. Escrow+ is a bank escrow with a trustee (launch: Axis Trustee, RBL, ICICI). A Razorpay hold is not escrow and must not be labelled one.

## Pack errors beyond my items
1. Rename "Vikalp" everywhere (P09 FR-P09-47 title, lines 15, 33, 698).
2. `advocate_restricted` profiles must also drop fee range (FR-P03-13).
3. Don't route JSON-schema agent tasks to Haiku 4.5 on the India profile.
4. FR-P01-22 says "renewal"; change to "verification".

## Launch blockers
- Gupshup, Setu and 100ms webhook signing unconfirmed: re-fetch status before acting.
- Escrow term sheets (`ESCROW_PORT` OFF).
- Vendor face-match and liveness calibration reports, needed before K2 auto-pass.
- Azure Document Intelligence Central India unconfirmed.
- Counsel opinions: r.36 profiles, LoA vs PoA (S-D1 stays), s.42A publication.
