# LawDocs — UI/UX Design Brief v1.1

> **Status:** Binding design brief for every LawDocs surface (`apps/public`, `apps/web`, `apps/delivery`, `apps/console`, `apps/mobile`, generated documents, e-mails). Version 1.1, 26 October 2026 (first issue — created with the Infrabyx Platform Baseline Standard adoption). · **Owner:** Company Secretary, Infrabyx Group. · **Companions:** IPB-06 (accessibility), IPB-07 §07.3.1 (design-system rules) and §07.4.1 (per-product identity); Appendix C §C.9 (design tokens — this brief restates and names them; on conflict Appendix C's contrast values win), Appendix U (accessibility specification), P03 FR-P03-31/31A (themes and brand packs), P21 (public site), content deck v1.1. · **Decision:** D-28 (= IPB-D-11) — distinct visual identity per product within WCAG 2.2 AA contrast guard-rails.
> **Feel in three words:** trustworthy legal · warm · minimal. LawDocs should look like a careful solicitor's office that has been redesigned by a good product team: serious where it must be, never cold, never cluttered.

---

## 1. Identity

| Element | Value | Notes |
|---|---|---|
| Product | LawDocs (`LD`) | Display name may be overridden only on white-label plans (`brand.app_name`); the Consumer Help brand has its own pack (D-06) |
| Primary colour | **Deep navy `#0B2545`** | Headings, primary buttons, navigation rail, footer background (public), document chrome |
| Accent colour | **Saffron `#E07A1F`** | One accent per screen: the primary action, focus ring on dark, progress, "Draft free with Vidhi" block border. Never used for body text on white (contrast 3.4:1 — fails AA for text); used as a fill with white or navy text only where the pair passes |
| Typography | **Inter** (UI, body, tables, forms) · **Source Serif 4** (document previews, legal headings on public document pages, quotations of statute) | Both self-hosted (`brand.fonts.self_hosted_only`), variable fonts, `font-display: swap`; Noto Sans/Noto Serif for Devanagari, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Gurmukhi (D-07) with matched x-height |
| Logo | Wordmark "LawDocs" in Inter SemiBold, navy; saffron dot on the "i" is the only mark | SVG sanitised; monochrome variants; minimum 24 px height; clear space = cap height |
| Vidhi mark | A rounded speech-bubble outline with a small saffron spark; never a humanoid or robot | Appears with the text "Vidhi AI" and the AI label on every output (IPB-03-60) |
| Voice | Plain, direct, warm; British/Indian spelling; no exclamation marks; no legal Latin without a plain gloss | Content deck §2 |

### 1.1 Colour tokens (light theme; contrast measured against the surface named)

| Token | Hex | Use | Contrast |
|---|---|---|---|
| `--ld-navy-900` | `#0B2545` | Primary text on light, primary buttons, rail | 14.9:1 on `#FFFFFF` |
| `--ld-navy-700` | `#13376B` | Links, hover of primary | 10.0:1 on white |
| `--ld-navy-500` | `#2F5597` | Secondary emphasis, chart series 1 | 6.4:1 on white |
| `--ld-navy-100` | `#E6ECF5` | Selected row, info surface | — (surface) |
| `--ld-saffron-600` | `#E07A1F` | Primary action fill (with `#0B2545` text, 4.7:1) and focus ring on dark | Not for text on white |
| `--ld-saffron-700` | `#B85F0E` | Saffron text on white where an accent word is needed | 5.1:1 on white |
| `--ld-saffron-100` | `#FBEBDD` | Highlight surface (Vidhi block, "new" badges) | — |
| `--ld-ink-800` | `#1F2937` | Body text | 13.5:1 |
| `--ld-ink-600` | `#4B5563` | Secondary text, captions | 7.0:1 |
| `--ld-ink-400` | `#9CA3AF` | Disabled text (not for essential content) | 2.8:1 — decorative only |
| `--ld-paper` | `#FFFFFF` | Page surface | — |
| `--ld-paper-warm` | `#F8F6F2` | App background behind cards; gives the "warm" feel without lowering contrast | — |
| `--ld-line` | `#D9DEE7` | Dividers, input borders (3.1:1 against paper — passes 1.4.11 for UI boundaries) | — |
| `--ld-success` | `#1B7F4D` | Signed, verified, published | 4.9:1 |
| `--ld-warning` | `#9A5B00` | Pending, expiring, "verify" | 5.3:1 |
| `--ld-danger` | `#B42318` | Errors, legal clocks breached, kill switch | 6.2:1 |
| `--ld-info` | `#13376B` | Informational banners (same as navy-700) | 10.0:1 |
| `--ld-evidence` | `#5B21B6` | Evidence-class badges on dashboards (IPB-07 LD note) with text label | 7.6:1 |

Status is never colour alone: every status chip carries text and an icon; eSign eligibility badges use text ("Valid for eSign", "Needs wet ink") with icon.

### 1.2 Dark theme

Dark theme is **user-chosen or system-following**, never forced. Surfaces: `--ld-paper` → `#0F1A2B` (not pure black), `--ld-paper-warm` → `#141F31`, cards `#1A2740`; body text `#E7ECF3` (14.1:1); secondary `#B4BFCF`; navy-900 becomes the surface, so **primary buttons flip to saffron fill with navy text** (`#E07A1F` on `#0B2545` 4.7:1) and links become `#9DB9FF` (8.3:1). Focus ring: saffron 3 px with a 1 px navy inner line so it is visible on both themes. Document previews stay light (paper white) inside a dark frame — documents are read as paper. Images and logos switch to the dark variant from the brand pack. All contrast guard-rails (`brand.contrast.min_text` 4.5, `min_ui` 3.0) apply in both themes; the validator runs on both.

## 2. Layout, spacing, density

- **Grid:** 8 px base; 4 px half-step for icon alignment. Breakpoints 360 / 600 / 905 / 1240 / 1440 px (Appendix C §C.9.5). Reflow to 400 % zoom with no horizontal scroll at 320 CSS px.
- **Reading measure:** 60–75 characters for prose and document previews (IPB-07 LD note); tables may be wider with sticky first column.
- **Shell (`apps/web`):** left navigation rail 240 px (collapsible to 64 px icons + labels on hover and focus), top bar with workspace switcher (always visible — P02), universal search `/`, "+" quick actions, Vidhi (`Ctrl/Cmd+J`), notifications, help "?", avatar. Content area max 1200 px for forms, fluid for tables.
- **Density:** `comfortable` (default; 44 px row height), `compact` (36 px — never below the 24×24 px target of WCAG 2.5.8 for controls), `spacious` (52 px). Density is a user setting (Appearance node); tenants may set a default.
- **Simple mode (`ux.simple_mode`):** one primary action per screen, secondary actions behind "More", widgets reduced to the mandatory set, larger type (112.5 %). Default ON for Consumer Help consumers and for the first-run of individuals; a toggle in Appearance.
- **Radius:** 8 px cards and inputs, 6 px chips, 12 px dialogs, full for avatars. **Elevation:** two levels only (card, dialog); no drop shadows on the public site; borders do the separating.
- **Click budgets** are a design requirement (OP-10; Appendix C §C.8): the top journeys (create matter, draft from template, send for eSign, upload to vault, hire a professional, export) must meet their budgets in the design file before build.

## 3. Components and tone

| Component | Rule |
|---|---|
| Buttons | One primary per screen (saffron fill, navy text; or navy fill, white text on the public site hero). Secondary: navy outline. Tertiary: text link. Destructive: danger outline, confirm dialog with the IPB-07 §07.4.8 anatomy (what will happen, what cannot be undone, the record reference, the undo window if any). Labels are verbs: "Send for signature", not "Submit" |
| Forms | Label above field; required marked with text "(required)" not only an asterisk; help "i" immediately after the label in tab order; inline validation on blur; error summary at the top with links to fields; never clear a form on error |
| "i" popover | 24×24 px target, accessible name "Help: `{label}`"; plain definition ≤ 40 words; "Learn more"; **regulatory-reference panel** (instrument · provision · as-of date · reviewer) when the term enforces a rule; "Ask Vidhi about this" when enabled (FR-P21-120A) |
| Tables | Column `helpKey` on every header; sticky header; row actions in a kebab; selection with bulk bar; empty, loading and error states (below); export to CSV always available where data is the user's |
| Status chips | Text + icon + colour; tooltips never carry essential information |
| Cards | Title, one-line meta, one primary action; no more than three cards across on desktop for decision screens |
| Dialogs | Focus trapped, Esc closes, returns focus; title states the action; no nested dialogs |
| Toasts | Polite live region; 6 s or until dismissed for actionable ones; never for errors that need a decision |
| Stepper (drafting, signing, hire agent) | Steps named as outcomes ("Who is signing?"), progress announced; a review step before any irreversible action |
| Vidhi panel | Right-side panel 400 px (bottom sheet on mobile); four mandatory indicators always visible: AI label, data class of the context, autonomy level of the acting skill, sources; streaming output announced once; every answer has "Sources", thumbs up/down with reason, "Use as reference" |
| Approval screen (locked actions) | One screen: what Vidhi proposes, the diff, consequences, inputs used, the approver's role; Approve / Edit / Reject; the agent's own token can never approve |
| Document preview | Paper white, Source Serif, page breaks shown, clause numbering preserved; redlines in navy (insert) and danger (delete) with underline/strike plus a side list of changes for screen readers |
| Evidence-class badge | Text badge "E1 statement · E2 sourced · E3 document-backed" on dashboard figures and Trust Centre facts (IPB-07) |

**Iconography:** Lucide outline icons at 20 px (24 px on mobile), 1.75 px stroke, navy; filled variants only for active navigation. No emoji in UI. Legal-specific icons (stamp, seal, gavel) are used sparingly and never to imply court approval. Every icon-only control has a visible label on hover/focus and an accessible name.

**Motion:** 150–200 ms ease-out for state changes; 250 ms for panels; no parallax, no autoplay, no looping decoration; `prefers-reduced-motion` removes all non-essential motion and replaces progress spinners with text ("Working… 3 of 5 pages"). Signing-complete and stamp-applied moments get one gentle confirmation (check draws in 300 ms) — the only "celebration" in the product.

## 4. Imagery and illustration

- **Style:** flat illustrations in navy, saffron, warm paper and one grey; everyday Indian settings (a rented flat, a small office, a courtroom corridor, a family table) drawn plainly; no caricature, no gender or regional stereotypes, no "lawyer with gavel" clichés, no stock photos of handshakes.
- **Photos:** real team, real offices, real screenshots with synthetic data only. Testimonials never carry photos (content deck GB-07).
- **AI-generated images:** permitted only for marketing illustrations on `apps/public` and the console, labelled "AI-generated image" with provenance, human-reviewed before publish (P21 FR-P21-80A); never of real people, courts, regulators or documents.
- **Placeholders the owner replaces from Brand Studio** (alt text binding; sizes recommended):

| Placeholder | Where | Size | Alt text (draft) |
|---|---|---|---|
| `IMG-home-hero` | Public home | 1600×900 | "Illustration of a person signing a rent agreement on a phone while the signed copy files itself into a vault" |
| `IMG-home-how-it-works-[1-4]` | Public home steps | 480×360 each | "Step 1: answer plain questions" / "Step 2: preview the draft" / "Step 3: stamp and sign" / "Step 4: keep it in your vault" |
| `IMG-vault-empty` | App empty state | 320×240 | "Illustration of an open, empty folder with a dotted outline of a document" |
| `IMG-vidhi-intro` | Vidhi first run | 400×300 | "Vidhi AI speech-bubble mark next to a short list of things it can help with" |
| `IMG-esign-eligibility` | eSign page | 800×500 | "Diagram: which documents can be signed electronically and which need wet ink" (also a table) |
| `IMG-dashboard-empty-[widget]` | Dashboards | 240×180 | "No `[items]` yet — illustration of a calm desk" |
| `IMG-settings-security` | Security node | 320×240 | "Illustration of a key and a passkey device" |
| `IMG-trust-hero` | Trust Centre | 1600×900 | "Illustration of a locked vault door with a document inside and an outline map of India" |
| `IMG-consumer-help-hero` | Consumer Help brand | 1600×900 | "Illustration of a person holding a letter at a kitchen table, phone in hand" (brand pack colours) |
| `IMG-404` | Error page | 480×360 | "Illustration of a misplaced folder tab" |
| `IMG-office-[delhi]`, `IMG-office-[noida]`, `IMG-office-[jaipur]` | Contact, Careers | 1200×800 | "Photograph of the LawDocs `[city]` office" |
| `IMG-og-default` | Social sharing | 1200×630 | "LawDocs — draft, sign, store and track your legal work" |
| `IMG-app-icon` | Mobile | 1024×1024 | Wordmark "LD" on navy with saffron dot |
| `IMG-email-header` | Transactional e-mail | 600×120 | LawDocs wordmark, navy on white |

## 5. States

- **Empty states** say what the space is for, show one primary action and, where useful, a sample ("See a sample vault"): "No agreements yet. Draft one free, or upload the ones you already have." Never a blank table.
- **Loading:** skeletons for lists and cards (no spinners longer than 400 ms without text); long jobs (OCR, export, import) show a progress card with step names and an estimate, plus "We'll notify you when it's done".
- **Errors:** the four-part message (what happened · why · what to do · reference code with "i") per IPB-07 §07.4.7; never blame the user; legal-rule errors show the regulatory reference ("Wills cannot be signed electronically — IT Act 2000, First Schedule").
- **Offline (mobile):** read-only vault and cached help; actions queue with a visible "will send when online" badge; signing is never attempted offline.
- **Degraded AI:** "Vidhi is temporarily unavailable for documents; your request is queued" — never a silent fallback to a non-India route (P09 FR-P09-08).

## 6. Accessibility notes (summary; Appendix U and IPB-06 govern)

WCAG 2.2 AA and IS 17802 on every surface; focus visible (saffron ring, 3 px, both themes); 24×24 px minimum targets; keyboard-only operation of every journey including signing and the Vidhi panel; live regions for streaming and progress; captions and transcripts on every video; visual alerts for every sound; ISL on core tutorials; dyslexia-friendly font option (Atkinson Hyperlegible or OpenDyslexic, self-hosted); text scale 100–200 %; plain-language mode for Vidhi (CEFR B1); no accessibility overlays; manual testing with NVDA, JAWS, VoiceOver and TalkBack before each wave; a disabled-user testing panel (Appendix U §U.8). Hearing journeys: live captions in Vidhi voice and support calls; motor: no drag-only interactions (keyboard alternatives for reorder and signature placement); cognitive and low literacy: simple mode, icon + text labels, read-aloud on document pages, one primary action.

## 7. Sample screens (described)

**Public home (`apps/public`, 1240 px).** Top bar: wordmark, seven disclosure menus, language, "Sign in", saffron "Draft free" button. Hero on warm paper: Source Serif headline "Draft it. Sign it. Keep it." (navy), one-line sub-head, two buttons (saffron "Draft a document free", navy outline "Hire a professional"), the hero illustration right. Below: issue-first tiles ("Renting out a flat?", "Cheque bounced?"…) as six cards; "How it works" four steps; trust strip with E-class badges ("Independently tested", "India-hosted", "Export any time") — no certification badges unless held; Vidhi block (saffron-100 surface); pricing teaser; resources teaser; FAQ accordion; footer per content deck GB-02A. Everything readable with JavaScript off.

**Dashboard (`apps/web`, Company admin).** Rail: Home, Vault, Agreements, Matters, Vidhi, Marketplace, Settings. Top bar with workspace switcher "Acme Pvt Ltd ▾". Home grid: "Today" (items due, approvals waiting — mandatory), "Agreements by stage" (chart with table alternative), "Open items", "What Vidhi did today" (list with autonomy level per row), "Savings this quarter" (E2 badge, method link), "Compliance clocks" (text + icon). One saffron primary: "+ New". Every widget has an "i" and a drill-down; empty widgets show the calm-desk illustration and one action.

**Settings (`apps/web`).** Left: the twenty IPB-07 nodes in order, grouped USER / ORGANISATION / PLATFORM-mirrored, with LawDocs additions at the end of each group; search-first header ("Find a setting… try 'reminders'") and the natural-language assistant (FR-P03-30). Right: a node page with sections as cards, each row = label, "i", control, "Changed by … on …" meta; GOVERNED rows show a "Needs a checker" chip; LOCKED rows show the lock icon with the legal reason text. Security node: user section on top, tenant policy below in a read-only card with "Edit policy (admins)".

**Vidhi panel (any app).** Header: Vidhi mark + "Vidhi AI" + the four indicators (AI · Data class: Confidential · Level: L1 Draft · Sources: 3). Body: conversation with citations as numbered chips that open a source drawer; outputs have "Insert into draft", "Save to vault", thumbs with reason. Footer: input with "Attach from vault", language selector, voice (with consent and disclosure), and the standing line "Vidhi assists; it is not legal advice."

**Public Resources library.** Filter rail left (type, topic, sector, language, access), cards right with type badge, date, version and access badge ("Free" / "E-mail required"); detail page with abstract, "what's inside", cite-as, version history and the inline gate form with the unticked consent box and the Resources Download Terms link.

**Settings › Security & trust › Vendor documents.** Table grouped by type with cadence filter; each row: title, version, issued, valid until, status chip ("Current" / "Expiring in 42 days" / "Expired — retained"), "Download (watermarked)", "Subscribe"; right panel: "Evidence pack" preset picker, "Grant auditor access", "Request a document"; footer line: "Downloads are watermarked and recorded."

## 8. Tenant overrides (white-label and Customisation node)

Tenants on eligible plans may change: logo and favicon, primary and accent colours, `brand.app_name`, terminology labels, default landing page and navigation order within limits, e-mail sender identity (DMARC-verified), document letterheads. They may **not** change: the contrast guard (every colour pair is validated at save — `LD-CFG-003` with a suggested nearest compliant colour), the fonts allow-list (self-hosted only), the AI label, autonomy and data-class indicators, legal texts and "i" definitions, the Vidhi display name on LawDocs core plans, the footer entity and officers lines, or any accessibility behaviour. Overrides are previewed in both themes before save and are maker-checker where the brand pack is platform-tier. The Consumer Help brand pack is a full pack (its own palette within the same guard-rails) — the wall between brands is visible: no LawDocs wordmark on Consumer Help surfaces (D-06).

## 9. Do and don't

| Do | Don't |
|---|---|
| One primary action per screen; verbs on buttons | "Submit", "OK", "Click here" |
| Explain why a rule applies, with the instrument and date | Hide a refusal behind a generic error |
| Show the AI label, data class and autonomy level on every Vidhi surface | Let an AI output look like a human's or a lawyer's |
| Use saffron for the one thing that matters on the screen | Use saffron for body text on white, or on more than one control |
| Serif for documents and statute quotations; sans for everything else | Serif body text in the app |
| Text + icon + colour for every status | Colour-only meaning; tooltips with essential content |
| Real photos of real people with consent; plain illustrations | Stock "lawyer" photos; AI images of people, courts, regulators |
| Say "in progress" or "available on request" | Imply certification, court approval or guaranteed outcomes (NN-20) |
| Dark theme as a choice; documents stay paper-white | Forced dark mode; pure black surfaces |
| Design to click budgets and test them | Add a confirmation step that is not a legal or safety need |
| Empty states that teach one action | Blank tables and spinners |

## 10. Deliverables from design to build

Figma library "LD Tokens v1.1" (light and dark, both density sets), component sheet matched to `packages/ui`, the fourteen placeholder illustrations above in SVG, icon set subset, motion spec (durations and easings as tokens), accessibility annotations (focus order, names, live regions) per screen, and a click-budget sheet per Appendix C §C.8 journey. Tokens are exported to `packages/tokens` as JSON and validated by the contrast guard in CI; any token change is a `GOVERNED` configuration change (P03 FR-P03-31A).

*End of design brief v1.1.*
