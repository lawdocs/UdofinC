# A3_COM — research summary (22 Oct 2026)

67 items: 9 verified, 6 corrected, 20 provisional, 24 counsel sign-off, 6 product decision, 2 watch. 24 items carry proposed edits; every `old` string is unique.

**Limitation.** The shared search budget ran out partway. Reporter checks and some Gazette items were not searched. They are provisional, as the residual field states: J-119, J-136, J2-003/004/005/007, J2-129–134, J2-138, J2-146, State RERA, SAROD.

## Key findings
1. **Mediation Act commencement (verified).** S.O. 4384(E) of 9 Oct 2023 commenced only ss.1, 3, 26, 31–38, 45–47, 50–54 and 56–57. S.O. 4781(E) of 27 Aug 2026 established the Mediation Council of India (s.31(1); head office Delhi) and commenced nothing else. Not in force: s.40 (mediation service providers), s.61 (replaces A&C Part III), s.62 (MSMED s.18), s.63 (s.442), s.64 (CCA s.12A), and the rest.
2. **CCA s.12A (verified).** Only LSAs are authorised (S.O. 3232(E), 3 Jul 2018). The PIMS Rules are G.S.R. 606(E). The new s.12A(2)(ii) allowing a mediation service provider is not in force.
3. **MSMED (pack error).** The mediation-service-provider referral is **Mediation Act s.62 + Seventh Schedule**. MSMED (Amendment) Act 2026 (Act 16; assent 13 Aug 2026) s.8 *amends* it. S.O. 5575(E) of 12 Oct 2026 commences ss.2–7, 11 and 13–17 from 15 Oct, and s.12 (new s.21, Council composition) from 15 Dec. **ss.8–10 (ss.18, 18A, 19) have no date.** The original s.18 operates.
4. **IBC Amendment (verified from the Gazette).** Act 6 of 2026: s.8 substitutes s.12A; s.34(a)(iii) and (b) set the 51% threshold in s.54A(2)(e) and (3). S.O. 2625(E) was read from a reproduction.
5. **Reg 30A (pack out of date).** It was substituted by REG152 (1 Jun 2026; secondary sources) to match s.12A, and NCLAT has applied the bar. The proposed pre-s.9 mediation regulation is **Reg 2BA**, not notified.
6. **Liquidation Reg 2B (verified).** In force. The proposal must come within 30 days of liquidation commencement, on CoC recommendation. REG151 adds a liquidation-value test.
7. **GLAS Trust** is 2024 INSC 811.
8. **A&C Amendment Bill.** Not introduced (PRS 2026 session lists). Watch it after the Winter Session.

## Other AI's claims
- **Mediation Act commencement and s.12A: right.** Commencement is provision by provision. The amended s.12A would allow mediation-service-provider authorisation but is not in force, so Equator must not claim s.12A compliance.
- **Two-tier arbitration: partly right.** *Centrotrade* upholds two-tier arbitration. No Supreme Court ruling decides the s.34(3) trigger or s.29A for the appellate tribunal; "s.34 from final award" is an inference. Recommended default: compute s.34 from the final award, plus a protective warning from first-tier receipt.

## Errors beyond the items
- V2 line 376 and 02 D2-26 credit the mediation-service-provider referral to the Amendment Act; fix as in J2-006/J2-292.
- The A&C Part III default (B05, FR-P04-33) needs a sunset on Mediation Act s.61.
- The s.442 track needs a sunset on Mediation Act s.63.
- LR-IBC-007 and V2 §3.8.4 omit the Reg 2B 30-day filing limit.

## Launch blockers
- `arb_appeal_tier_contractual` OFF in production until counsel opinion (J-003/034/148).
- `com.msefc_referral_msp` OFF until Mediation Act s.62 **and** Amendment Act s.8 commence and Mediation Council recognition regulations issue.
- `com.s12a_equator_authorised` OFF.
- AI-assisted awards: clerical only, with disclosure, consent and attestation (J-156).
- Post-settlement consent-award variant stays flagged.
