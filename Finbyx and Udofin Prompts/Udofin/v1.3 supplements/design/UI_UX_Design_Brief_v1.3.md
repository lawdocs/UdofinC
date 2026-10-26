# Udofin — UI/UX Design Brief v1.3

**26 October 2026 · Product code UDF · Companion to the Udofin Master Prompt v1.3 (Part 3.3, Part 10.7, Part 7I, Appendix G) and IPB-07 (design system), IPB-06 (accessibility), IPB-04 (Brand Studio) · Palette per IPB-D-11**

## 1. Who this is for and what it must feel like

Udofin is used by people on mid-range Android phones, often on patchy networks, often for the first serious financial decision of their lives, often in a language other than English. Many will read slowly; some will not read at all and will rely on icons, read-aloud and a relative beside them. The product is also a regulated disclosure surface: the lender decides, Udofin facilitates, and every screen must make that true at a glance.

**Feel:** consumer-friendly, trustworthy, calm, unhurried. **Not:** fintech-flashy, gamified, urgent, salesy. The emotional promise is "you understand what is happening and you are in control". The design proof is: one primary action per screen, an explain-why before every ask, and nothing that pushes.

**Three design laws (from the master prompt, binding):**
1. **One primary action per screen** (Part 3.3; G.1 rule 1). Lint enforces one `primary` button on every journey screen.
2. **Explain why, never dead-end** (G.1 rule 7). Every data request, permission and disabled control states the reason and the next step.
3. **The lender is named on every loan screen** (G.1 rule 5). The lender strip is a fixed component; nothing may say "Udofin loan".

## 2. Palette (tokens in `packages/tokens`; contrast guard enforced in Brand Studio)

| Token | Light | Dark | Use |
|---|---|---|---|
| `colour.primary` | `#4338CA` (indigo 700) | `#818CF8` (indigo 400) | Primary action, active tab, links, focus ring |
| `colour.primary.hover` | `#3730A3` | `#A5B4FC` | Pressed/hover |
| `colour.on_primary` | `#FFFFFF` | `#1E1B4B` | Text on primary |
| `colour.accent` | `#F59E0B` (amber 500) | `#FBBF24` | Attention that is *not* an alarm: next due, resume banner, highlights; never for body text on white |
| `colour.on_accent` | `#1F1300` | `#1F1300` | Text on amber |
| `colour.surface` | `#FFFFFF` | `#0F0F17` | Page |
| `colour.surface.raised` | `#F8F8FC` | `#17172A` | Cards |
| `colour.on_surface` | `#111827` | `#F3F4F6` | Body text |
| `colour.on_surface.muted` | `#4B5563` | `#B8BCC8` | Secondary text (≥ 4.5:1 still) |
| `colour.border` | `#E5E7EB` | `#2A2A40` | Dividers |
| `colour.success` | `#15803D` | `#4ADE80` | Paid, verified |
| `colour.warning` | `#B45309` | `#FCD34D` | Due soon, action needed (text on light uses the 700 shade) |
| `colour.danger` | `#B91C1C` | `#F87171` | Overdue, failed, destructive |
| `colour.info` | `#1D4ED8` | `#93C5FD` | Informational |
| `colour.regulatory.bg` / `.text` | `#FFFFFF` / `#111827` | `#0F0F17` / `#F3F4F6` | KFS, consent, disclosures — **not themeable** (G.1 rule 6) |

**Contrast rules.** Body text ≥ 4.5:1; large text and UI components ≥ 3:1 (WCAG 2.2 SC 1.4.3, 1.4.11), computed for light and dark; publish blocked otherwise (`IPB-BRD-003`). Amber is an accent: use it as a fill behind dark text or as an icon colour, never as body text on white (3.0:1 fails). Status is never colour-only: every status chip has an icon and a label. Indigo on white for links is 8.6:1; indigo focus ring 3 px with 2 px offset.

**Per-RE colour.** RE logos appear in the offer view at equal size on a neutral card; RE colours never tint the shell in the Udofin app. In a white-label pack the RE's tokens replace the shell colours through Brand Studio within the same contrast guard; regulatory tokens stay fixed.

## 3. Typography

| Role | Face | Size (mobile / web) | Weight | Line height |
|---|---|---|---|---|
| Display (home greeting, amounts) | Plus Jakarta Sans | 28 / 32 | 700 | 1.2 |
| Title | Plus Jakarta Sans | 22 / 24 | 600 | 1.25 |
| Section | Plus Jakarta Sans | 18 / 20 | 600 | 1.3 |
| Body | Plus Jakarta Sans | 16 / 16 | 400 | 1.5 |
| Body strong | Plus Jakarta Sans | 16 | 600 | 1.5 |
| Caption | Plus Jakarta Sans | 14 | 400 | 1.4 |
| Legal/regulatory body | Plus Jakarta Sans | 16 (never below) | 400 | 1.6 |
| Numbers (amounts, APR) | Plus Jakarta Sans tabular (`font-variant-numeric: tabular-nums`) | as role | 600 | — |
| Code/ids (UTR, references) | JetBrains Mono | 14 | 400 | 1.4 |

**Indic scripts.** Noto Sans (Devanagari, Bengali, Telugu, Tamil, Gujarati, Kannada, Malayalam, Gurmukhi, Oriya) self-hosted as WOFF2 with `size-adjust` fallbacks; line height 1.6 for Indic body; never synthesise bold. Dyslexia-friendly option (Atkinson Hyperlegible) in Accessibility. Text scales to 200% without loss of function; layouts use `rem` and intrinsic sizing. Amounts always `₹1,00,000` grouping; dates `DD-MM-YYYY`; time IST.

**Minimum sizes.** Body 16 px; captions 14 px; nothing smaller anywhere, including the KFS, which renders at body size with 1.6 line height and amounts in words beneath the figure.

## 4. Spacing, grid and density

4-pt base. Spacing scale 4, 8, 12, 16, 24, 32, 48. Mobile: 16 px side gutters, 12 px between cards, 24 px between sections. Web: 12-column grid, max content width 1,120 px for borrower web, fluid for portals. Touch targets 48 dp (44 pt iOS) with ≥ 8 px spacing (WCAG 2.5.8 and Udofin's stricter 48). Density tokens: `comfortable` for borrower surfaces (fixed), `compact` default for portal queues (user may change). Radius: `md` 12 px cards, `sm` 8 px inputs, `full` chips. Elevation: one soft shadow level for cards; no stacked shadows.

## 5. Components and tone

| Component | Rule |
|---|---|
| **Primary button** | Indigo fill, white text, 48 dp, full width on mobile, label is a verb ("Accept KFS", "Pay ₹2,450 to [RE]", "Continue"); exactly one per journey screen; never "Submit" |
| **Secondary** | Outlined indigo; same size; equal weight with the primary where a choice is real (accept/decline consent, exit/stay in cooling-off) — the dark-pattern rule forbids shrinking "decline" |
| **Tertiary/text** | Indigo text link; used for "Why do we ask?" and "i" |
| **Lender strip** | Fixed: RE logo (24 px), "Loan from [RE] · facilitated by Udofin, a lending service provider", chevron to the RE disclosure page; appears above the title on every loan-context screen; not collapsible |
| **Explain-why sheet** | Bottom sheet before every OS prompt and data request: icon, "Why we ask", recipient RE(s), retention, CF basis via "i", one primary ("Continue") and one equal secondary ("Not now") |
| **"i" popover** | Plain text (≤ 40 words), "Why we ask", regulatory reference panel (instrument, provision, plain summary), "Read aloud", "Ask Vidhi" |
| **Offer card** | Equal size and layout per lender; lender logo at fixed size; amount, tenor, APR, monthly repayment, penal charge summary, KFS link; no badges, no "recommended"; ranking metric shown once above the list with a link |
| **KFS viewer** | Regulatory tokens; line items each with "i"; amounts with words; read-aloud; acknowledge control at the end only after scroll; validity shown as a plain date |
| **Status chip** | Icon + label + colour; six states (Done, In progress, Waiting on lender, Action needed, Failed, Cancelled) |
| **Resume banner** | Amber fill, dark text, "Continue your application — step 3 of 6", one action |
| **Cooling-off card** | Indigo outline, plain date end, "Exit this loan" as a real secondary of equal weight |
| **Timeline** | Vertical, icons, as-of time, "source: [RE]" on mirror items |
| **Forms** | One question per screen in journeys; labels above; helper text; inline errors that say what happened and what to do; OTP paste and autofill; no CAPTCHA puzzles |
| **Empty state** | One sentence why, one next action, no promotional card |
| **Error state** | What happened, whether data was saved, what to do, reference code; never a raw provider message |
| **Disabled control** | Visible reason text ("Escalation opens on 14-11-2026, when [RE]'s 30-day period ends") |
| **Toast/alert** | Visual + optional haptic; never sound-only; persists until dismissed for anything the user must act on |
| **Bottom tabs** | Exactly five: Home, Loans, Pay, Help, Account; icons with labels always visible |
| **Vidhi entry** | Floating pill on Help and the journey Help shortcut, never a tab; chat bubbles with sources; captions bar above the voice control |

**Tone of copy.** Second person, present tense, short sentences, no jargon without an "i", numbers as numerals, no exclamation marks, no "congratulations", no "unlock", no "instant". Verbs on buttons. Reading age 12 checked by the copy linter.

## 6. Iconography and imagery

**Icons.** Lucide (outline, 2 px stroke, 24 px) with a small custom set for domain objects (KFS, lender, mandate, cooling-off, grievance, DLG). Every icon has a label (low-literacy rule); icons never carry meaning alone. Status icons: check-circle, clock, hourglass, alert-circle, x-circle, slash.

**Illustration.** Flat, two-tone (indigo + amber on neutral), people drawn inclusively (varied ages, regions, abilities, dress), no money-rain or coin imagery, no celebratory confetti. Photography only on the public site (real offices and team with consent); no stock "happy borrower" images.

**Placeholder image list (owner replaces from Brand Studio; alt text mandatory; WebP/AVIF with PNG fallback):**

| Id | Where | Dimensions | Alt text (draft) |
|---|---|---|---|
| `img.public.home.hero` | Home hero | 1600×900 (16:9), mobile crop 900×1200 | "A person reading a Key Facts Statement on a phone, with the lender's name visible" |
| `img.public.howitworks.step1–4` | How it works | 800×600 each | Step illustrations: "tell us what you need", "lenders check and offer", "read and sign", "repay the lender" |
| `img.public.safety.permissions` | Safety & your data | 1200×800 | "A phone showing the permissions Udofin never asks for, crossed out" |
| `img.public.safety.kfs_sample` | Safety / Resources | 1240×1754 (A4 PDF preview) | "Sample Key Facts Statement with annotations" |
| `img.public.lenders.logo.[re]` | Lenders page | 400×160 (logo on transparent) | "[RE] logo" |
| `img.public.about.team` | About / Team | 1600×900 | "Udofin team at the Noida office" |
| `img.public.about.offices.[delhi\|noida\|jaipur]` | Contact | 800×600 | "Udofin office, [city]" |
| `img.public.leadership.[person]` | Leadership | 600×600 | "[Name], [role]" (photo consent recorded) |
| `img.public.press.kit.logo` | Press kit | SVG + 2000×800 PNG | "Udofin logo, horizontal" |
| `img.public.og.default` | Open Graph | 1200×630 | "Udofin — loans from regulated lenders, explained clearly" |
| `img.app.empty.loans` | Loans empty state | 320×240 | "An empty folder with a gentle smile" |
| `img.app.empty.complaints` | Help empty state | 320×240 | "A quiet inbox" |
| `img.app.tutorial.[journey].[step]` | Picture tutorials | 720×1280 | One step per picture, described |
| `img.app.icon` | App icon | 1024×1024 (adaptive layers) | — |
| `img.app.splash` | Splash | 1284×2778 | Wordmark on indigo |
| `img.store.screenshot.[1–8]` | Store listings | 1080×1920 (Android), 1290×2796 (iOS 6.7") | Described per screenshot in the store copy item |
| `img.brandpack.[re].logo` | White-label packs | SVG (sanitised) + PNG set 32/64/192/512 | "[RE] logo" |

## 7. Dark mode

System-following by default with a manual override in Appearance. Dark surfaces are deep indigo-black (`#0F0F17`), not pure black, to keep indigo and amber legible; primary moves to indigo 400, accent to amber 400; body text `#F3F4F6`; all pairings re-checked by the contrast guard. Regulatory components keep their own token set in both schemes. Lender logos get a neutral light chip behind them in dark mode so brand marks remain legible without altering the logo. Screenshots and PDFs (KFS, certificates) always render in light scheme.

## 8. Motion

Purposeful and brief: 150–200 ms for state changes, 250 ms for sheets; easing `cubic-bezier(0.2, 0, 0, 1)`. No looping animations, no countdown animations ever (dark-pattern rule), no celebratory bursts. Skeletons within 300 ms of navigation; named progress for provider waits ("Checking with [RE]…"). `prefers-reduced-motion` disables all non-essential motion and replaces transitions with fades ≤ 100 ms. Haptics: light tick on success, double on failure, single long on attention; user-switchable; never the only signal.

## 9. Accessibility notes (IPB-06; Udofin IB6)

- WCAG 2.2 AA incl. 2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8; TalkBack and VoiceOver scripts per borrower journey; focus order follows reading order; focus never obscured by the lender strip or sheets.
- **Hearing:** captions on every video; live captions and text twin in voice support; visual alerts for everything audible; chat and email alternatives to every phone route.
- **Vision:** 200% text scaling; high-contrast theme; dyslexia font; colour-blind-safe status palette (icons carry meaning); screen-reader labels on amounts read as "rupees twelve thousand four hundred".
- **Low literacy (easy-read on by default for borrowers):** icon + label everywhere, one question per screen, read-aloud on every screen, amounts in words on KFS and acceptance, picture tutorials, assisted mode with borrower-held OTP, consistent placement of Help.
- **Motor and cognitive:** 48 dp targets, no drag-only interactions, no time limits except security ones with warnings and extensions, consistent help, redundant entry avoided (prefill from consented data).
- **Low bandwidth:** Lite mode automatically on 2G/slow 3G/Save-Data: no images, system fonts, text-first.

## 10. Do / don't

| Do | Don't |
|---|---|
| Name the lender on every loan screen | Say "Udofin loan", "approved by Udofin", "pre-approved" |
| One primary action; equal-weight real choices | Shrink, grey out or hide "decline", "exit", "not now" |
| Explain why before every ask | Fire an OS permission prompt cold |
| Show validity as a plain date | Show countdowns, timers, "only today" |
| Show the RE as source and the as-of time on balances | Compute or imply a balance Udofin owns |
| Use amber for attention, indigo for action | Use red for marketing or amber for body text on white |
| Keep regulatory text in its own tokens | Let a theme restyle the KFS or disclosures |
| Icons with labels, read-aloud, amounts in words | Icon-only controls, abbreviations without "i" |
| Empty states with one next step | Promotional cards in empty states or on Home |
| Plain language, reading age 12 | Jargon, exclamation marks, superlatives |

## 11. Sample screens (described)

**Borrower Home (app).** Header: "Good morning, Asha" (display), language switch, bell. Lender strip absent (not a loan-context screen). Cards in fixed order: *Action needed* (indigo outline: "Your KFS from [RE] is ready to read" → primary "Read KFS"); *Next due* with lender strip and amount in tabular numerals, "Pay ₹2,450 to [RE]" primary; *Cooling-off* card with plain end date and equal-weight "Exit this loan" / "Keep loan"; *Complaint status* chip; *Apply for a loan* as the last card (secondary). No banners, no offers, no non-loan cards. Bottom tabs with labels.

**Offer view (app).** Title "Offers for you"; one line "Sorted by APR, lowest first · How we sort" (link); cards of identical height: RE logo (fixed size), amount, tenor, APR (tabular), monthly repayment, penal charge summary, "Read KFS" primary per card; below the list "Lenders that did not match" with one-line reasons; "Not available in this app — available on the web" for store-filtered lenders. Nothing highlighted; no badge.

**KFS screen.** Lender strip; regulatory tokens; sections with "i" per line; amounts with words; read-aloud control at top; validity date; after scrolling to the end, "I have read and understood" explanation step, then the single primary "Accept KFS" with step-up; equal-weight "Not now".

**Lender portal dashboard (web, compact).** Left nav (20-node Settings at the bottom); Work Inbox as the landing page: SLA-sorted items with deterministic next action, filters, saved views, Cmd+K (masked identifiers; refuses Aadhaar/PAN/card patterns with a plain explanation); KPI tiles with as-of time; Vidhi prepared actions panel at the right with Approve/Edit/Reject.

**Settings (borrower).** Grouped list following G.14.1: Security, Privacy & consents, Accessibility, Appearance, Notifications and marketing, AI assistant; then Feedback, Tutorials & help, What's new, About. Each row: icon, label, one-line description, chevron. Accessibility opens the IPB-06 sub-section with large toggles and an "i" per setting.

**Vidhi panel (app).** Sheet from Help: first turn is the disclosure in the user's language with an "i"; chat bubbles; sources under each answer ("From your KFS, version 3"); voice button with a live-caption bar above; "Talk to a person" always visible; thumbs with reasons.

**Public Home (web).** Indigo wordmark, calm hero with one h1 ("Loans from regulated lenders, explained clearly") and one primary ("See how it works"), secondary "Get the app"; LSP statement under the hero; four steps; lenders teaser generated from the register; safety teaser; resources; FAQ; footer with the regulated blocks. No autoplay, no popups beyond the CMP.

## 12. Tenant and brand-pack overrides (Brand Studio)

| May change | Within |
|---|---|
| Primary, accent, surface, text tokens | Contrast guard (4.5:1 / 3:1) in both schemes; regulatory tokens excluded |
| Type family | Approved self-hosted list (Plus Jakarta Sans, Inter, Noto Sans families, Atkinson Hyperlegible); sizes fixed |
| Logo, favicon, OG image, display name, terminology | SVG sanitised; name passes the copy linter; "an AI assistant" fixed |
| Footer content | Required blocks locked (LSP statement, GRO, nodal officer, policies, Sachet) |
| Imagery, tours, RE help articles | Alt text and captions gates |
| Nothing else | Five tabs, one primary action, explain-why, permissions, ranking engine, regulatory components, density on borrower surfaces |

## 13. Design QA checklist (per screen, in Storybook and device tests)

One primary action · lender strip where loan context · explain-why present before any ask · "i" on every regulated field · amounts tabular and in words where required · contrast pass in light and dark · 48 dp targets · labels on icons · empty, loading, error, offline, permission-denied states · TalkBack/VoiceOver pass · reduced-motion pass · Lite-mode render · 12-locale string presence or hidden locale · no banned phrase (linter) · no countdown or scarcity element · screenshot blocking where sensitive.
