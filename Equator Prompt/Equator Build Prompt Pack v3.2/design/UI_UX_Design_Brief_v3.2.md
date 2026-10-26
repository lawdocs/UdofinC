# Equator Resolution — UI/UX Design Brief v3.2 *(v3.2, 26 October 2026)*

**Owner:** Company Secretary, Infrabyx Group · **Product code:** EQ · **Binding sources:** IPB-07 (design-system rules, per-product identity, settings tree, help), IPB-06 (accessibility), IPB-04 (Brand Studio, contrast guard), IPB-D-11 (distinct identity per product), Appendix C (screen inventory), Appendix P §5 (UI copy and minimalist principles), Appendix AG (shells, menus, Work Inbox, palette, patterns), Appendix S (personas and portals) · **Precedence:** master → IPB → this brief → Appendix C where the two differ on visual treatment; Appendix AG prevails on where things sit.

---

## 1. Feel and intent

Equator is an institution first and a product second. The interface should feel **neutral, balanced and institutionally calm**: nothing shouts, nothing rushes, nothing nudges. A party arriving after a notice is anxious; a neutral is working; a registrar is accountable. The design lowers the temperature. Three words to test every screen against: *steady, legible, even-handed*. If a screen looks like it is selling, it is wrong. If a screen could be read as favouring one side, it is wrong.

What this means in practice: generous whitespace, one primary action per screen (IPB-07 click budget; UDF "one-primary-action" pattern cross-pollinated), text that reads at B1 level in plain-language mode, colour used as a signal and never as the only cue, and the same visual weight for both parties' content wherever two sides are shown.

## 2. Palette (IPB-D-11; tokens in `packages/design-tokens`)

| Token | Light | Dark | Use |
|---|---|---|---|
| `colour.primary` | Teal `#0E6E6E` | Teal `#5FB8B4` | Primary actions, links, active nav, focus ring base |
| `colour.primary.on` | `#FFFFFF` | `#06302F` | Text on primary |
| `colour.accent` | Coral `#F26B5B` | Coral `#F7917F` | Attention that is *not* an error: deadlines approaching, "needs you", pending approvals; never for destructive actions |
| `colour.accent.on` | `#1A1A1A` | `#1A1A1A` | Text on accent (coral fails 4.5:1 with white — never put white text on coral) |
| `colour.surface` | `#FAFAF8` (warm off-white) | `#121615` | Page background |
| `colour.surface.raised` | `#FFFFFF` | `#1A201F` | Cards, panels |
| `colour.on_surface` | `#1A1F1E` | `#E8ECEB` | Body text (≥ 12.6:1 light) |
| `colour.on_surface.muted` | `#5A6563` | `#A3ADAB` | Secondary text (≥ 4.6:1 both schemes) |
| `colour.border` | `#D9DEDC` | `#2E3736` | Hairlines; 3:1 against surface for UI components |
| `colour.success` | `#1F7A4D` | `#6CCB94` | Completed, signed, settled |
| `colour.warning` | `#9A6B00` | `#E3B341` | Clock at T-30, unverified sources |
| `colour.danger` | `#B3261E` | `#F2847B` | Destructive actions, breaches, Critical incidents |
| `colour.info` | `#2F5D8A` | `#8FB6E6` | Informational banners, identity strip |
| `colour.ai` | `#5B4B8A` (muted violet) | `#B3A4E0` | AI label, Vidhi panel header, "AI-generated draft" watermark tint |
| `colour.sealed` | `#4A4A4A` with hatched pattern | `#8A8A8A` | Sealed (POSH, health, safety) indicators; pattern plus text, never colour alone |

Rules: coral is an *attention* colour, not an action colour — primary buttons are teal, destructive buttons are the danger red with a typed confirmation, and coral is reserved for badges, deadline chips and the "needs your decision" state. Every text/background pair is checked by the contrast guard (IPB-04-24): 4.5:1 for normal text, 3:1 for large text and UI components, in both schemes; publish is blocked below that. Tenants on white-label plans may replace primary and accent within the same guard; they may not change the semantic colours (success, warning, danger, sealed, ai).

Party and respondent content is never colour-coded by side. Where two sides appear (negotiation room, brief, settlement builder), both use the neutral surface tokens and are distinguished by position and label.

## 3. Typography

- **Family:** Manrope (variable, self-hosted WOFF2 from `STORAGE_PORT`; licence note in the brand pack — IPB-04-25). No third-party font CDN on any route.
- **Devanagari:** Noto Sans Devanagari (self-hosted) paired for Hindi and other Indic scripts; same vertical rhythm; tested for mixed-script lines.
- **Mono:** JetBrains Mono for case numbers, hashes, codes and keys.
- **Dyslexia option:** Atkinson Hyperlegible switchable from Accessibility settings (IPB-06), applied to body and UI text.
- **Scale (desktop / mobile):** display 40/32 · h1 32/28 · h2 24/22 · h3 20/18 · body 16/16 · small 14/14 · caption 12 (never below 12; never for legal text). Line height 1.5 body, 1.25 headings. Max measure 70 characters for reading columns.
- **Weights:** 400 body, 500 labels and UI, 600 headings and buttons. No 300 or 800.
- **Text scaling:** layouts hold at 200% browser zoom without horizontal scroll (WCAG 1.4.4, 1.4.10); long Hindi labels are tested at 200%.

## 4. Spacing, layout and density

- 4-pt base; spacing scale 4, 8, 12, 16, 24, 32, 48, 64. Content column 1,120 px max on desktop; 16 px side gutters on mobile.
- Three densities from the brand pack and the user's Appearance settings: `comfortable` (default for parties and public), `compact` (default for console, ops and chambers staff), `spacious` (large-text and low-literacy modes). Density changes padding and row height, never font size below 16 for body.
- Shell anatomy per Appendix AG §AG.1.2: left rail (collapsible) · top bar with context switcher, search/palette (`Ctrl/Cmd+K`), Work Inbox bell, help "?", Vidhi · content · optional right panel (Vidhi, help, item detail). Public site: header with ten groups (AG §AG.2.1), responsive to a drawer under 1,024 px.
- Grid: 12 columns desktop, 8 tablet, 4 mobile. Cards never nest more than two levels.

## 5. Components and tone

- **Buttons.** One primary per screen (teal, 600, 44 px min height, 24 px side padding). Secondary = outlined teal. Tertiary = text link. Destructive = outlined red, confirmation dialog with a typed word for irreversible actions (sign, issue, delete, delist). Disabled states keep 3:1 contrast and explain why in a tooltip ("Needs approval from the Registrar").
- **Forms.** Label above the field; helper text below; every field has an "i" help button (IPB-07-44) 24×24 after the label; errors are four-part (what happened, why, what to do, code) and inline; required marked by text "(required)", not an asterisk alone. Pre-filled values from documents show a dotted underline and "from your document — please confirm".
- **Tables and lists.** Saved views, column help keys, bulk actions with preview and undo window (AG §AG.7). Row density follows the setting. Deadline chips use coral with an icon and the date in text.
- **Status chips.** Text plus icon plus colour; the Appendix C §G.2 labels; the "sealed" chip uses a hatched pattern.
- **Banners.** Identity strip (info blue, left border, never dismissible on public dispute pages); AI-generated banner (violet, with "Why this answer?"); clock banner (warning or danger with the owner's name).
- **Cards.** Raised surface, 12 px radius (`radius.md`), 1 px border, no drop shadow in light mode, subtle shadow in dark mode.
- **Dialogs.** Centre modal for decisions; side sheet for detail and Vidhi; bottom sheet on mobile. Focus trapped only while modal; Escape closes (as Reject for consent).
- **Tone of microcopy.** Appendix P §4 and §5: short, concrete, no exclamation marks, no "oops", no humour on regulated screens. Empty states say what to do next. Confirmations restate what will happen ("You are about to issue the award. The parties will be notified and the s.34 period will start.").

## 6. Iconography

- Lucide icon set (outlined, 1.5 px stroke) at 20 px in UI and 24 px in navigation; filled variants only for active states.
- No gavel. No scales as a brand mark (used generically it implies a court). No handcuffs, no judges' wigs. The process icons are: handshake (negotiation), bridge (conciliation), two chairs (mediation), a single seat with a document (arbitration), stepped path (hybrid), a magnifier over a figure (expert determination).
- Every icon that carries meaning has a text label or `aria-label`; decorative icons are `aria-hidden`.
- The Vidhi mark: a small, rounded speech-mark glyph in `colour.ai`, always beside the word "Vidhi" or the tenant's display name; never a humanoid face.

## 7. Imagery placeholders (owner replaces from Brand Studio; list mirrors the content deck §33)

| ID | Where | Placeholder | Alt text | Size |
|---|---|---|---|---|
| IMG-01 | Public home hero | Abstract: two paths meeting at a horizon, teal and coral, no people | Two lines converging on a horizon, representing agreement | 1600×900 |
| IMG-05 | Vertical hubs | Six muted context photographs, licensed, faces avoided | Described per hub | 1200×675 |
| IMG-06 | About, Contact | Delhi, Noida, Jaipur office photographs (consented or empty rooms) | Equator office, {city} | 1200×800 |
| IMG-08 | Team, Leadership | Portraits with recorded consent, else initials tile | {Name}, {Role} | 600×600 |
| IMG-12 | Press kit | Logo on light and dark | Equator Resolution logo | 1200×630 |
| IMG-18 | OG default | Mark on teal with the brand line | Equator Resolution — Resolve disputes, not relationships | 1200×630 |
| IMG-19 | Favicon set | Mark, maskable | Equator Resolution | 16–512 |
| APP-01 | Party dashboard empty state | Line illustration: an open folder and a calendar | No cases yet | 480×320 |
| APP-02 | Neutral dashboard empty state | Line illustration: a desk with a lamp | No appointments yet | 480×320 |
| APP-03 | Vidhi panel empty state | The Vidhi glyph with three example prompts as text | Ask Vidhi | 240×160 |
| APP-04 | Hearing room waiting | Soft gradient, clock, "The session will start when the neutral admits you" | Waiting room | full-bleed |
| APP-05 | Settings hero | None (text only) | — | — |

No stock photography of courtrooms, gavels or people shaking hands in suits. No images of real parties ever.

## 8. Dark mode

Full dark scheme from the token table; respects `prefers-color-scheme` with a manual override in Appearance. Hearing rooms default to dark to reduce glare on camera. Sealed and danger indicators keep pattern and text so they survive both schemes. Document viewers keep paper white by default with an optional dark reading mode (never applied to PDFs destined for signature).

## 9. Empty, loading and error states

- **Empty:** one sentence on what this is, one on what to do, one primary action. Example (Decisions Library): "No published outcomes match. Only consented, redacted awards and settlements appear here. Clear filters."
- **Loading:** skeletons, not spinners; trust-bearing sections (badges, council, governance, investors) are server-rendered and never show a loading state in the public site (Appendix AF W10).
- **Error:** four-part message with the code and a help key; never a bare stack or a smiling illustration on a regulated screen. Outage: the FR-P14 outage banner with the statutory-clock statement ("Statutory periods are not extended by an outage").

## 10. Motion

Purposeful only: 150–200 ms ease-out for panels and sheets; no bounce; no parallax; no autoplay; `prefers-reduced-motion` removes all non-essential animation and replaces streaming Vidhi text with a completed block. Live regions announce changes for screen readers. No confetti on settlement — a calm success state with next steps.

## 11. Accessibility notes (IPB-06; NN-23)

- WCAG 2.2 AA throughout; IS 17802; GIGW 3.0 for court-facing deployments; EN 301 549 referenced for international parties.
- Keyboard: every shell, panel and approval operable; visible 2 px focus ring in `colour.primary` with 3:1 against adjacent colours; skip links; focus not obscured (2.4.11).
- Target size ≥ 24×24 (2.5.8); 44×44 for primary actions on mobile.
- Hearing room: live captions (consented, ephemeral), speaker identification, raise-hand, visual alerts for audio events, ISL interpreter booking, transcript only through the consented flow (IPB-06 EQ note). The hearing room is the one route permitted to exceed the single-primary-action rule under a recorded `IPB-DEV` (join · raise hand · captions grouped in one action bar).
- Low literacy and occasional users: simple mode offered at first login to parties and witnesses; plain-language mode rewrites Vidhi outputs at ~B1 with the same citations; voice input on intake; icons paired with words.
- Forms: errors announced; time limits extendable; no CAPTCHA that requires vision alone (use proof-of-work or audio alternative).
- Quick exit (FAM, safety-flagged): a persistent button on every page in the section; keyboard shortcut; clears the view and goes to a configurable neutral page (X-25).
- Typed confirmations for settlement acceptance and award acknowledgement; the typed word is shown, not hidden.

## 12. Do and don't

| Do | Don't |
|---|---|
| Show both parties' content with identical weight and layout | Colour-code sides or place one side above the other without a neutral reason |
| Use coral for "needs your attention" | Use coral for buttons or for errors |
| Put the identity strip on every dispute page | Hide "not a court" in a footer only |
| Render trust sections on the server with honest empty states | Show spinners for governance, council or badges |
| State the fee total with GST before any booking control | Show "from ₹…" or reveal fees after a choice |
| Label every AI output with the four indicators | Blend AI text into human text |
| Use words plus icons plus colour for status | Rely on colour alone |
| Offer simple mode and Hindi up front | Bury language and accessibility in settings |
| Keep one primary action per screen | Stack three equal buttons |
| Use the hatched sealed pattern and the word "Sealed" | Show sealed content thumbnails anywhere |
| Date everything | Publish undated statistics or "coverage walls" |

## 13. Sample screens described

**Public home.** Header with ten groups and the utility bar (Understand your options · Respond · Track · Language · Log in). Hero on the warm surface: H1 "Resolve disputes, not relationships.", one-liner, two buttons (teal primary, outlined secondary), the small "Not a court. Not a regulator." line. Below: four process tiles with the process icons; three audience columns; the five-step line diagram; the proof row in its honest empty state; three institution proof points with links; trust teaser with the readiness statement; pricing teaser without figures; three resource cards; the organisations strip; a six-item FAQ; final CTA. Footer per the content deck §28 with the entity and officers lines in text.

**Party dashboard (`/app`).** Left rail: Home · My cases · Documents · Payments · Messages · Settings. Top: context switcher (if the party is in more than one case), bell, "?", Vidhi. Content: a "Next step" card (one primary action, e.g., "Confirm your extracted details"), then case cards with status chips and a deadline chip in coral where one is within 30 days, then a quiet "Need help understanding this?" link to Vidhi's party explainer. Empty state APP-01.

**Neutral workspace (case).** Tabs: Overview · Brief · Documents · Sessions · Drafts · Notes (sealed to the neutral). The Brief tab shows the AI-generated banner (violet) with "Why this answer?", both parties' positions in two equal columns, chronology with page citations, issues list. Right panel: Vidhi with the data-class badge "Confidential" and the autonomy badge "L1 Draft". Primary action: "Open draft procedural order" when due.

**Settings (`/settings`).** One rail per Appendix AG §AG.3.1: Personal first, then Organisation, Rules and legal, (Chambers/Enterprise/Operations as applicable), AI & Vidhi, Security & trust, Feedback, Tutorials & help, What's new, About; Approvals · History · Health last. Each row shows the tier badge (🔒 Locked / ⚖ Governed / ✎ Tenant), "Who can change this", and a Save or Submit-for-approval button whose label follows the tier. The AI & Vidhi node shows skills with ceiling and operating level, the locked list (read-only), schedules with plain-English RRULE previews, and connections.

**Vidhi panel.** Header: glyph + "Vidhi" (or display name) + AI label; sub-header: data class · autonomy level. Body: streaming answer with citations as chips; "Why this answer?" expander (sources, model family, run ID); feedback thumbs; "Open in chat". Footer: plain-language toggle, voice push-to-talk with captions, "Vidhi does not give legal advice" line. For a locked action: a one-screen approval card (diff, consequences, inputs audit, Approve/Reject/Edit) rendered only for a human with the right role.

**Hearing room.** Dark by default; video grid; captions bar; action bar (join/leave · mic · camera · raise hand · captions · interpreter) grouped; side panel for documents and private chat with the tribunal where the Rules allow; recording indicator with consent state in text; no Vidhi on the main stage during a live session.

## 14. Tenant overrides within guard-rails (IPB-04 Brand Studio; Appendix AG §AG.8)

White-label and chambers tenants may change: logo and favicon (sanitised SVG), primary and accent colours (contrast guard enforced in both schemes), font (self-hosted WOFF2 from an allow-list), density default, `brand.app_name` (T tier; the G guard blocks names implying a court, regulator or government body — "Court", "Tribunal", "Authority", "Govt", "RBI", "SEBI" fail the lint — Appendix P LINT rules apply), the Vidhi display name (white-label plans only), menu labels (terminology overrides within AG §AG.8.1), and the public footer's social links and offices. They may not change: semantic colours, the identity strip, the AI label and the four indicators, sealed indicators, legal pages' structure, the fee display rules, or the locked footer lines. Preview renders six reference screens (home, pricing, article, form, console sidebar, email) before publish; publish is maker-checker with rollback.

## 15. Deliverables for the design squad

Token file (`packages/design-tokens/eq.json`, light and dark); Figma or Penpot library with the components above and the four indicators; Storybook with axe checks; the twelve placeholder images at the stated sizes; the six reference screens for Brand Studio preview; the hearing-room `IPB-DEV` record; a contrast report for every token pair in both schemes; a screen-reader script for the party filing journey, the neutral brief and the Vidhi approval card.
