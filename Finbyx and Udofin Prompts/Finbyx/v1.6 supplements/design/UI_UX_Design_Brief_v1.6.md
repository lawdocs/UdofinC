# Finbyx — UI/UX Design Brief v1.6

**Product code:** FBX · **Date:** 26 October 2026 · **Status:** binding for Phases 1 (tokens, shell), 8b (field app), 15 (borrower portal), 18A (Vidhi surfaces) and 21 (public site, Studio) · **Governs:** `packages/tokens/fbx/*`, `packages/ui`, `apps/web`, `apps/public`, `apps/console`, `apps/field`, borrower portal · **Companions:** IPB-06 (accessibility), IPB-07 §07.3.1 and §07.4.1 (design-system rules and identity table), IPB-04 §04.3.2 (Brand Studio and contrast guard), master prompt Part 10.5 and Appendix G *(v1.6)*.

Finbyx is used eight hours a day by credit officers, collectors, accountants and compliance teams who read thousands of numbers and approve decisions that carry regulatory and financial consequences. The interface must feel **banking-grade, calm and dense-but-legible**: nothing decorative competes with a figure, every number is exact, every irreversible step is explained, and the screen never shouts. The feel in one line (IPB-D-11): *precise, ledger-like, dense tables.*

## 1. Palette

| Token | Light | Dark | Use |
|---|---|---|---|
| `--color-primary` | `#1E3A8A` slate blue | `#93C5FD` (text) / `#1E3A8A` (filled) | primary action, active navigation, links on surfaces where underline alone is weak |
| `--color-on-primary` | `#FFFFFF` | `#0B1220` | text on primary |
| `--color-accent` | `#10B981` emerald | `#34D399` | positive status, "balanced", "filed", success toasts; never for primary buttons |
| `--color-on-accent` | `#052E1C` | `#052E1C` | text on accent chips |
| `--color-bg` | `#F8FAFC` | `#0B1220` | page |
| `--color-surface` | `#FFFFFF` | `#111A2E` | cards, tables |
| `--color-surface-raised` | `#FFFFFF` + `--shadow-1` | `#172238` | popovers, drawers |
| `--color-text` | `#0F172A` | `#E5EAF3` | body |
| `--color-text-muted` | `#475569` (≥ 4.5:1 on surface) | `#A3B1C6` | secondary labels; never lighter than this |
| `--color-border` / `-strong` | `#E2E8F0` / `#94A3B8` | `#243049` / `#64748B` | dividers; control borders (strong ≥ 3:1) |
| `--color-focus` | `#1D4ED8` 2 px ring + 2 px offset | `#60A5FA` | focus; visible on every surface |
| `--color-success` / `-bg` | `#047857` / `#ECFDF5` | `#34D399` / `#0A2E22` | status with icon + text |
| `--color-warning` / `-bg` | `#B45309` / `#FFFBEB` | `#FBBF24` / `#3A2A05` | SMA-1, due soon, business-date differs |
| `--color-danger` / `-bg` | `#B91C1C` / `#FEF2F2` | `#F87171` / `#3B0F0F` | NPA, breach, floor violation, COB running |
| `--color-info` / `-bg` | `#1E40AF` / `#EFF6FF` | `#93C5FD` / `#122039` | informational banners |
| `--color-link` | `#1E3A8A` underlined | `#93C5FD` underlined | links are always underlined in body text |

Rules. Slate blue carries hierarchy and action; emerald carries *good state* only, so a user never confuses "this is a button" with "this is fine". Red, amber and green are never the only carrier of meaning (G.9: RAG always with text; status chips carry an icon and a label). The contrast guard (IPB-04-24) runs on every token pair in light, dark, high-contrast light and high-contrast dark; the four theme files live in `packages/tokens/fbx/{light,dark,hc_light,hc_dark}.json`. Hover and active variants are derived by lightness steps (−6 % / −12 %) and re-checked.

## 2. Typography

- **Body and headings:** Inter (variable; self-hosted WOFF2 under the brand host; `font-display: swap` with size-adjusted fallback to system-ui). No Google Fonts request on any route (IPB-04-25).
- **Numerals and amounts:** **JetBrains Mono** for every number that a user compares or reconciles — amounts, rates, DPD, account and loan ids, dates in tables, hashes, run ids. Tabular figures, `font-variant-numeric: tabular-nums slashed-zero`. Inter keeps prose numerals inside sentences ("3 working days").
- **Indic scripts:** Noto Sans Devanagari and the Noto family for the Eighth Schedule languages in borrower outputs; RTL for Urdu.
- **Scale (base 16 px):** `--text-xs` 12 (table meta only, never body), `sm` 14 (table cells, dense lists), `base` 16, `lg` 18, `xl` 20, `2xl` 24, `3xl` 30, `4xl` 36, `5xl` 48 (public hero only). Line height 1.5 body, 1.25 headings, 1.35 table cells.
- **Weights:** 400 body, 500 labels and table headers, 600 headings and amounts that are totals, 700 only for the single page title. No italics for emphasis; use weight or colour-with-text.
- **Dyslexia mode:** `a11y.text.font` swaps Inter for Atkinson Hyperlegible or OpenDyslexic (self-hosted); JetBrains Mono stays for numerals.

## 3. Spacing, grid, density

8-point grid: `--space-1 … --space-16` = 4 … 64 px. Three densities (IPB-04-26): **compact** is the default for back-office roles (32 px table rows, 12 px cell padding), **comfortable** for tenant admins, Studio and the public site (40 px rows), **spacious** for the borrower portal and the field app (48 px rows, 44 px targets). Density is a user setting (Appearance node) with a role default; it never drops targets below 24 × 24 CSS px (WCAG 2.5.8) and borrower screens never go below 44 px.

Breakpoints follow Appendix G.9: ≥ 1440 px dense three-pane (sidebar 240 px, list, detail drawer 480 px); 1024–1439 two-pane; 768–1023 single pane with drawers; 360–767 card lists; 320 px reflow floor with grids scrolling inside their region, never the page.

## 4. Components and tone

- **Tables are the core.** Sticky header and first column, right-aligned mono amounts with Indian grouping (₹12,34,56,789.50), negatives in parentheses in statements, row hover, keyboard navigation (`j`/`k`/`x`/`Enter`), saved views, column chooser, inline filters, 50/100/500 page sizes, and a totals row that is computed server-side. Charts always have a table alternative.
- **One primary action per screen** (UDF cross-pollination, IPB-07 §07.3.1): one filled slate-blue button; secondary actions are outlined; destructive actions are outlined red and open a confirmation that states consequence, reversibility and the rule (IPB-07 §07.4.8).
- **Explain-why everywhere:** every refusal, disabled control and floor badge has a sentence and a link to the fixing screen (G.1.4). Error messages follow the four-part standard (what happened, why, what to do, help key).
- **Status chips:** icon + text + colour; lifecycle chips (DRAFT, PENDING_APPROVAL, ACTIVE, READ_ONLY) share one component.
- **"i" popover** on every labelled field (G.2.4): term, plain definition, regulatory-reference panel, "Ask Vidhi about this", key footer. Opens on click/Enter/Space; Esc returns focus.
- **Maker-checker screens:** two-column diff (before/after), consequences list, risk flags, approver identity; approve/reject with reason; never inline for sanctions, settlements, filings, payouts or floor-class settings.
- **Forms:** labels above inputs, help key on every field, inline validation on blur, paste allowed in OTP and password fields, no re-entry, autosaved drafts with a visible "saved 12:04 IST" chip.
- **Banners:** SANDBOX/STAGING watermark, COB running, viewing-as, break-glass open — persistent and not dismissible while true.
- **Tone of copy:** plain English, active voice, no exclamation marks, no humour in regulated flows, Indian and British spelling, dates DD-MM-YYYY with "IST".

## 5. Iconography

Lucide icon set (ISC licence), 20 px in dense tables, 24 px elsewhere, 1.75 px stroke, currentColor. Every icon that stands alone has an `aria-label`; icons beside text are `aria-hidden`. Finbyx-specific glyphs (NPA bucket, KFS, mandate, return filed, bureau file) are drawn on the same grid and added to `packages/ui/icons` with names, never inline SVG in pages. No emoji anywhere in product UI or public copy.

## 6. Imagery placeholders

The owner replaces these from Brand Studio › Media. All images are PNG or WebP (no SVG for photos), with alt text stored in the CMS; synthetic or stock images are labelled in the media record and never show a real borrower, PAN card or Aadhaar.

| Placeholder id | Where | Dimensions | Alt text (default) |
|---|---|---|---|
| `img.public.home.hero` | Home hero (right of headline) | 1440 × 900, focal left | "Finbyx dashboard showing loan portfolio by bucket and approvals awaiting, on a laptop" |
| `img.public.home.proof` | Home proof band | 6 × 320 × 120 logos (SVG from partner brand packs with permission) | "<Partner name> logo" |
| `img.public.product.los` … `.colending` | Seven product pages | 1200 × 800 | "Screenshot of the Finbyx <module> screen with synthetic data" |
| `img.public.solution.nbfc` … `.ifsc` | Seven solution pages | 1200 × 600 | "Illustration: <entity type> workflow from onboarding to regulatory return" |
| `img.public.trust.hero` | Security & Trust | 1200 × 600 | "Diagram of India-resident deployment with primary and disaster-recovery regions" |
| `img.public.about.timeline` | About | 8 × 400 × 300 | "Milestone: <year> <event>" |
| `img.public.team.*` | Team, Leadership | 400 × 400 square | "<Name>, <role>" (photo consent recorded) |
| `img.public.og.default` | Open Graph default | 1200 × 630 | "Finbyx — lending operations software for regulated lenders" |
| `img.public.resource.cover.*` | Resource covers | 800 × 1000 | "Cover of <resource title>" |
| `img.public.blog.default` | Blog default cover | 1600 × 900 | "Abstract slate-blue grid" |
| `img.app.empty.*` | Empty states (12) | 240 × 160 line illustrations | "No <items> yet" |
| `img.app.login.side` | Login side panel | 960 × 1200 | "Slate blue gradient with Finbyx wordmark" |
| `img.field.onboarding.*` | Field-app onboarding (3) | 1080 × 1920 | "Field officer capturing documents with the Finbyx app" |

Office map images on Contact are static click-to-load PNGs (1200 × 400) so no map provider is called before consent.

## 7. Dark mode

Full parity, not an afterthought: tokens above, surfaces stepped by elevation rather than shadow, mono numerals at the same weight, charts re-coloured from the dark categorical palette, and emerald/amber/red re-tuned for 4.5:1 on dark surfaces. System preference by default; user override in Appearance; high-contrast variants add 1 px stronger borders and remove subtle backgrounds. Printed and PDF outputs (KFS, statements, Board packs) are always light.

## 8. Empty, loading, error and permission states

Every list and dashboard tile ships four states from the same component: **empty** (line illustration, one sentence, one primary action the user is allowed to take, or "Nothing due" for queues); **loading** (skeleton rows of the real column widths, never spinners over tables; business-date chip shows COB progress); **error** (what failed, correlation id, retry, "Report a problem"); **permission-denied / not-entitled / read-only** (reason code, who can grant it, link to Plan or Modules). Read-only modules show a grey badge with date and reason and keep registers and exports visible (G.1.2).

## 9. Motion

`--duration-fast/base/slow` = 100/200/300 ms, ease-out; used for drawers, popovers, row expansion and toast entry only. No parallax, no autoplay video, no animated numbers in financial views (a changing total must be exact at every frame or static). `prefers-reduced-motion` sets every duration to 0 and replaces transitions with instant state changes; the field app honours the OS setting.

## 10. Accessibility notes (IPB-06; G.9)

WCAG 2.2 AA on every surface, IS 17802 for the public site, and the G.9 v1.6 additions: captions on every tutorial and tour, live captions on recorded calls and transcribed field voice notes, visual and haptic equivalents for every audible alert, low-literacy field-app mode (icon-led, one question per screen, read-aloud of labels and amounts, photo receipts), ISL interpreter booking. Keyboard-only paths for onboarding, sanction, disbursement, return sign-off, meeting votes and every approval; focus never hidden by sticky headers; live regions for status; 200 % zoom and 320 px reflow; timeout warning two minutes ahead with draft saved. axe-core on every story and page template blocks serious and critical issues; NVDA, JAWS, VoiceOver and TalkBack scripts run each release; a manual audit before Phase P and yearly. Plain-language mode for Vidhi rewrites at about CEFR B1 with the same citations.

## 11. Do and don't

| Do | Don't |
|---|---|
| Use JetBrains Mono tabular figures for every amount, rate, id and date in tables | Use proportional figures or round amounts in any financial view |
| Show Indian grouping and "lakh/crore" only with the exact amount in the tooltip and accessible name | Use million or billion for INR, or hide paise |
| Put one filled primary button per screen | Fill several buttons, or make a destructive action primary |
| Pair every colour with an icon and text | Use red/green alone for NPA/standard |
| Explain every refusal with the rule and a fixing link | Show a bare "Forbidden" or disable a control silently |
| Keep regulatory text blocks (KFS, APR, cooling-off, grievance officer) in the locked layout | Let a brand pack restyle, reorder or shorten regulatory text |
| Render captions, transcripts and table alternatives | Publish a video or chart without them |
| Keep the public site free of third-party requests until consent | Load fonts, maps, pixels or chat widgets before the CMP answer |
| Use "designed to support compliance with …" with an evidenced claim | Say "RBI-approved", "RBI-compliant", "100% secure", "guaranteed" |
| Label the AI, its data class and autonomy level on every Vidhi surface | Present AI output as a decision, or hide that it is AI |

## 12. Sample screens

**Public Home (`apps/public`).** Comfortable density. Header: wordmark (slate blue), Products, Solutions, Pricing, Resources, Security & Trust, Sign in, one primary "Book a demo". Hero on `--color-bg`: h1 "Lending operations software built for India's regulated lenders", one sentence, two buttons (primary demo; outlined "See how returns are prepared"), hero image placeholder. Then: feature grid (seven products, icon + two lines), who-it-is-for strip (seven entity types as links), proof band (partner logos with permission or sourced stats), how-it-works steps (onboard → originate → service → collect → report), security teaser linking `/trust` (no badges unless held), pricing teaser, resources teaser, FAQ, footer per IPB-04 §04.3.8 with the entity and officers lines.

**Tenant Home dashboard (`apps/web`).** Compact density, three panes. Left sidebar 240 px with workspace switcher and entity chip; top bar with business-date chip (amber when it differs), global search, Create, Inbox, Notifications, Help, user menu. Content: mandatory tiles first — Approvals awaiting (count, oldest age), Overdue EMIs by bucket (mono amounts, stacked bar with table toggle), Limit utilisation (gauge with number), Returns due this week (list with T−n chips) — then role tiles. Every tile has a title, an "i", a last-refreshed time in IST and a table alternative. Right pane: Vidhi side panel collapsed to a 40 px rail until opened.

**Settings (`apps/web`).** Two-pane: IPB-07 twenty nodes in binding order in the left list, grouped USER / ORG / platform-mirrored; right pane shows the node with sections and each setting as a row: label with "i", current value, class badge (Regulatory floor — lock icon, cited; Commercial — pencil), effective date, maker-checker indicator. Floors are read-only with the citation in the popover; editing a commercial setting opens an effective-dated drawer with preview of impact and the checker route. "All settings" search by key.

**Vidhi panel (Phase 18A).** 400 px side panel on `--color-surface-raised`. Header: "Vidhi" (or brand display name) + "an AI assistant" label, data-class chip (REGULATED in slate), autonomy chip (L1 Draft), kill-switch state. Body: conversation with streamed answers announced through a live region; each answer carries a citations block (REQ-ID, instrument, paragraph, source link), a "Why this answer?" expander (model family, run id, inputs), thumbs up/down with reason. Footer: input with "Ask about this screen", attach (documents go through the injection detector; a chip shows "scanned"), plain-language toggle. Approval cards (`<VidhiApproval>`) render as a one-screen diff with consequences and the approver's role check; nothing in the panel is a primary action against the ledger.

**Field app (Expo).** Spacious density, bottom tabs Today / Tasks / Onboard / Collect / Sync, offline banner, provisional-receipt watermark, low-literacy mode toggle in the header, voice-note button with caption rendering, large mono amounts, haptic and visual confirmation of every sync.

**Studio (`apps/console`).** Comfortable density, left navigation CMS · Brand Studio · Pricing Studio · Blog · Resources · Footer & Contact · CMP · Marketing · Feedback · Tutorials · What's new · Claims Register · Compliance Documents · Tenants & plans · Flags & releases · Platform audit. Brand Studio shows the six reference screens plus the KFS rendition side by side with the live contrast-guard report; publish button disabled with the failing pair named.

## 13. Tenant overrides within guard-rails

Tenants (and white-label packs) may change: primary and accent colours, logo, favicon, app display name, fonts from the self-hosted allow-list (Inter, IBM Plex Sans, Plus Jakarta Sans, Manrope, Noto families; JetBrains Mono fixed for numerals), density default, radius (`sm/md/lg` = 4/8/12), e-mail identity, terminology map (including the Vidhi display name with the mandatory "an AI assistant"). Every override is compiled to a CSS-variable layer applied after the product theme and must pass the contrast guard for all four themes; a failing pair blocks publish with `IPB-BRD-003` and names the pair. Tenants may not change: focus ring visibility, status semantics (red/amber/green meaning), the mono numerals rule, target sizes, the regulatory text blocks, the AI label, the footer's mandatory regions, or any accessibility setting's availability. Previews render on the six reference screens plus Finbyx's KFS, sanction letter and statement so a brand admin sees the locked blocks unchanged before publishing.

## 14. Deliverables and checks

Phase 1 delivers `packages/tokens/fbx` (four themes), `packages/ui` primitives with Storybook stories carrying axe-core, the shell, the four states component, the "i" popover and the settings row; Phase 21 delivers the public templates and the Studio; Phase 18A the Vidhi components. CI checks: contrast guard on token PRs, axe on stories and page templates, Lighthouse accessibility 100 and performance ≥ 90 on Home, Pricing, Trust, an article, Login and the tenant Home (budgets in `infra/policy/budgets.json`), bundle budgets 250 KB (`apps/web`) and 150 KB (`apps/public`), no third-party request before consent (network assertion), captions present on every published video.
