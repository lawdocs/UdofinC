# LawDocsComply — UI/UX Design Brief v1.3

> LawDocsComply Build Prompt Pack v1.3 · 26 October 2026 · Owner: Company Secretary, Infrabyx Group · Binding on: Appendix C §C.8 (tokens), P23 §4V (Brand Studio), P02 §4M (tenant branding), `apps/web`, `apps/public`, `apps/console`, `apps/delivery` · Baseline: IPB-07 §07.3.1 (design-system rules), §07.4.1 (per-product identity, IPB-D-11), IPB-06 (accessibility) · Decision: D-69.
>
> **Purpose.** One page the designer, the front-end lead and the owner can agree on before the first screen is built: what LawDocsComply looks and feels like, which tokens carry that identity, how the public site and the three authenticated apps share it, where placeholders sit until the owner replaces them from Brand Studio, and the rules a tenant may bend. Everything here is implemented as tokens in `packages/tokens/ldc/{light,dark,hc_light,hc_dark}.json` and compiled into the shared `brand_pack` (IPB-D-10); nothing is hard-coded in components.

## 1. Feel in one line

**Regulatory, calm, precise.** LawDocsComply is a register: it shows what applies, what is due, what is done and who is responsible. The interface should feel like a well-kept compliance file — ordered, legible, unhurried, exact — not like a dashboard that competes for attention. Status, dates and identifiers are the heroes; decoration is absent. The IPB describes the LDC identity as "calm, register-like, status-driven"; this brief turns that into rules.

## 2. Palette (IPB-D-11; D-69)

| Token | Light | Dark | Role | Guard |
|---|---|---|---|---|
| `--color-primary` | `#0F4C3A` forest green | `#7FC8A9` (lightened primary) | Primary action, active navigation, selected tab, links on surface in dark mode | on-primary white `#FFFFFF` on `#0F4C3A` = 9.1:1 ✔; dark: `#0B1F19` text on `#7FC8A9` = 9.4:1 ✔ |
| `--color-on-primary` | `#FFFFFF` | `#0B1F19` | Text and icons on primary | ≥ 4.5:1 |
| `--color-accent` | `#C9A227` gold | `#E3C35A` | Highlights, "due today" markers, stars/bookmarks, premium badges — never for body text | gold on white 2.3:1 ✘ as text → used only as fill behind `--color-on-accent #1F1A05` (10.6:1 ✔) or as a 3 px rule; never as text colour |
| `--color-on-accent` | `#1F1A05` | `#1F1A05` | Text on gold chips | ≥ 4.5:1 |
| `--color-bg` | `#F7F8F6` warm off-white | `#0E1412` | Page background | — |
| `--color-surface` | `#FFFFFF` | `#141C19` | Cards, table rows | — |
| `--color-surface-raised` | `#FFFFFF` + `--shadow-1` | `#1B2522` | Popovers, drawers | — |
| `--color-text` | `#1A1F1D` | `#E8ECEA` | Body | 15.5:1 ✔ |
| `--color-text-muted` | `#4B5551` | `#A7B2AD` | Secondary text, timestamps | 7.4:1 ✔ (muted is still ≥ 4.5:1; no light grey text) |
| `--color-border` | `#D9DED9` | `#2A3632` | Dividers | — |
| `--color-border-strong` | `#8A948F` | `#5C6964` | Control borders | ≥ 3:1 ✔ |
| `--color-focus` | `#0F4C3A` with 2 px offset ring `#C9A227` | `#E3C35A` | Focus ring (two-tone so it is visible on both light and dark surfaces) | ≥ 3:1 against bg and surface |
| `--color-link` | `#0B5E47` | `#8FD3B6` | Links | 6.9:1 ✔ and underlined |
| `--color-success` / `-bg` | `#1B7F4D` / `#E3F3EA` | `#5CCB8E` / `#12271C` | Green status (icon + word always) | text on bg ≥ 4.5:1 ✔ |
| `--color-warning` / `-bg` | `#9A6400` / `#FFF3D6` | `#E2B457` / `#2B2110` | Amber status | ✔ |
| `--color-danger` / `-bg` | `#B42318` / `#FEE4E2` | `#F28B82` / `#2E1412` | Red status (RAG red per Appendix C §C.8.1A: 5.45:1 ✔) | ✔ |
| `--color-info` / `-bg` | `#0B5E8A` / `#E1F0FA` | `#7FB8E0` / `#0F2230` | Blue informational | ✔ |
| RAG tokens | `rag.red #B42318`, `rag.amber #9A6400`, `rag.green #1B7F4D`, `rag.grey #6B746F`, `rag.blue #0B5E8A` | lightened equivalents | Deterministic urgency (D-54, NN-58); always icon + word + pattern | Appendix C §C.8.1A binding |

Rules: colour never carries meaning alone (icon + word always; stripe pattern on RAG chips for colour-blind users); gold is an accent, never a text colour; the v1.0 corrected palette (X-20) remains the fallback for any token this brief does not redefine; every pair is contrast-checked at token build and at Brand Studio save (`LDC-WEB-053`).

## 3. Typography

| Token | Value | Notes |
|---|---|---|
| `--font-body`, `--font-heading` | **IBM Plex Sans** (self-hosted WOFF2, weights 400/500/600) | One family for headings and body — the register look; headings differ by size and weight, not by face |
| `--font-mono` | **IBM Plex Mono** 400/500 | CompIDs, RiskIDs, GovIDs, clause numbers, dates in tables, amounts, API samples — anything a user may quote or compare |
| Dyslexia and legibility options | OpenDyslexic, Atkinson Hyperlegible (self-hosted; licences [VERIFY] OI-P23-38) replace body and heading when `a11y.text.font` is set | IPB-06 §06.3.4; P23 FR-P23-231 |
| Devanagari | IBM Plex Sans Devanagari for `hi-IN` | Same metrics family; no fallback to system fonts |
| Scale (`--text-xs … --text-5xl`) | 12 / 14 / 16 / 18 / 20 / 24 / 30 / 36 / 48 px; base 16; line-height 1.5 body, 1.25 headings | Users may scale to 200% without loss (WCAG 1.4.4); tables reflow with the column chooser |
| Measure | 60–75 characters for reading pages (help, legal, blog); tables are full width | — |
| Numerals | Tabular figures in tables and chips (`font-variant-numeric: tabular-nums`) | Dates and amounts align |

Tone of type: headings are sentence case, never all caps; labels are nouns; buttons are verbs ("Approve", "Request evidence"); no exclamation marks anywhere in the product.

## 4. Spacing, shape, elevation, density

- 8-point grid (`--space-1 … --space-16` = 4–64 px). Table rows 40 px (comfortable) / 32 px (compact; `ux.appearance.density`).
- Radii `--radius-sm/md/lg` = 4 / 8 / 12 px. Chips and status pills use `sm`; cards `md`; drawers and dialogs `lg`. No pill-shaped buttons (they read as marketing).
- Elevation: `--shadow-1` for raised surfaces, `--shadow-2` for the CompID drawer and dialogs only. No decorative shadows on cards in lists.
- Borders over shadows for structure: the register metaphor prefers hairlines (`--color-border`) and clear table grid lines on hover.
- Density default comfortable; compact mode is a first-class setting for checkers who work through 300-row registers; both modes keep 44 × 44 px touch targets on controls (WCAG 2.5.8 minimum 24 px, our rule 44 px).

## 5. Component tone

| Component | Rule |
|---|---|
| Primary button | One per screen (Appendix C §C.0 "one primary action per screen"); forest green fill, white text; disabled state keeps text legible (no washed-out grey below 4.5:1) and shows "why" on hover/focus (explain-why) |
| Secondary / tertiary | Outline forest green / text link; destructive = red outline with confirmation dialog that states what will happen and what cannot be undone |
| Status chips | Icon + word + colour + pattern; RAG chips use tabular mono for days-to-due; never animated |
| Tables (`DataTable`) | Sticky header, frozen first two columns (S. No., CompID), column chooser, saved views, inline bulk edit with preview and undo, 320 px responsive card fallback (IPB-06-18); the 9-column list view of D-50 is the default |
| CompID drawer | Right-side drawer at 560 px (desktop) / full screen (mobile); tabs Overview, Do, Maker, Checker, Auditor, Conversation, History, Links, Accountability; the drawer never covers the row's CompID |
| Forms | One column; labels above fields; "i" popover beside every term a non-specialist may not know (`hlp.<module>.<term>`), with the regulatory-reference panel; errors in text under the field and summarised at top; no placeholder-as-label |
| Work Inbox | Item kinds, priority, deterministic next-best action (Appendix C §C.5–C.6); keyboard first (`j/k`, `Enter`, `a` approve with confirm) |
| Dialogs and confirmations | Title states the action; body states the effect, the records affected (count and IDs) and the undo window; primary button repeats the verb |
| Toasts | Bottom-left, 6 s, with an "Undo" action where NN-49 gives an undo window; also written to the notification centre so nothing is lost |
| Empty states | One sentence of what belongs here, one primary action, one link to a tutorial; an illustration only in the public site and onboarding, never inside registers |
| Vidhi panel | Right side panel, 400 px; header shows the display name, the model family and the "AI-generated — review before use" label; every answer shows citations or "no source"; action proposals appear as cards with "Approve", "Edit", "Reject" — never auto-applied |
| Charts | Through the `Chart` contract (IPB-06-25): data table toggle, patterns, direct labels, no 3-D, no pie charts for more than four categories |

## 6. Iconography

Lucide icon set (outline, 1.5 px stroke, 20 px in controls, 16 px inline), consistent metaphors: calendar = due; shield-check = complied; file-check = evidence; scale = regulation; landmark = regulator; users = board; bot = Vidhi (with the label, never the icon alone); star = bookmark (gold fill when active). Every icon that conveys meaning has a text label or `aria-label`; decorative icons are `aria-hidden`. No emoji anywhere in the product or the public site.

## 7. Imagery and placeholders (owner replaces from Brand Studio › Media)

Photography is sparse and documentary — offices, paper registers, boardrooms, Indian regulatory settings — never stock "handshake" imagery. Illustrations are flat, two-tone (forest green and gold on off-white), used only on the public site and onboarding. Every image has alt text written as a sentence; decorative images have empty alt. AI-generated illustrations are allowed on the public site only, with a named reviewer and a visible "AI-generated image" caption (NN-63).

| Placeholder id | Where | Recommended size | Alt text (draft) | Replace with |
|---|---|---|---|---|
| `img.home.hero` | Public home hero | 1600 × 900 (16:9), WebP ≤ 180 KB, with 2× | "A compliance register on screen showing obligations, due dates and status for an NBFC" | Product screenshot of the compliance list (synthetic data) or documentary photo |
| `img.home.how-it-works.1–4` | Home "how it works" steps | 640 × 480 each | "Step 1: answer twelve applicability questions" … | Product screenshots (synthetic) |
| `img.about.story` | About page | 1200 × 800 | "The LawDocsComply team at the Noida office" | Real team photo with consent recorded |
| `img.about.offices.delhi/noida/jaipur` | About, Contact offices block | 800 × 600 each | "The Delhi office entrance" … | Real photos or static map images (click-to-load) |
| `img.team.<slug>` | Team and Leadership | 600 × 600 (1:1), face centred | "Portrait of {name}, {role}" | Portraits with `photo_consent` recorded (`LDC-WEB-055`) |
| `img.solutions.<family>` | Solution pages (NBFC, UCB, listed, AIF, insurer, co-operative, company, LLP) | 1200 × 675 | "{Family} obligations grouped by department in LawDocsComply" | Screenshots per family |
| `img.health-check.hero` | Health Check landing | 1200 × 675 | "A sample Health Check report with a score and a prioritised action list" | Synthetic sample report render |
| `img.trust.residency` | Trust Centre | 1200 × 600 | "Diagram: data stored in Mumbai with disaster recovery in Hyderabad" | SVG diagram (text alternative in page) |
| `img.vidhi.panel` | Vidhi module page | 1200 × 800 | "The Vidhi side panel drafting board minutes with citations shown" | Screenshot with the AI label visible |
| `img.og.default` | Open Graph default | 1200 × 630 | "LawDocsComply — governance, risk and compliance for regulated entities" | Brand Studio OG editor |
| `img.logo.light/dark` | Header, footer, emails | SVG + PNG 512 px; monochrome variants | "LawDocsComply" | Brand Studio › Logo |
| `img.favicon` | Favicons | SVG, 32/180/512 PNG | — | Brand Studio › Favicon |
| `img.press.kit.*` | Press media kit | Logos SVG/PNG, leadership portraits 1200 × 1200, product screens 1920 × 1080 | per item | Brand Studio › Press kit |
| `img.resources.cover.<slug>` | Resources library cards | 800 × 1035 (A4 ratio) | "Cover of {resource title}" | Generated from the PDF first page |
| `img.blog.cover.default` | Blog posts without a cover | 1200 × 630 | "LawDocsComply blog" | Two-tone illustration set (6 variants) |

Until replaced, every placeholder renders a labelled two-tone illustration, never a grey box; the Studio publish queue lists remaining placeholders before go-live.

## 8. Dark mode and high contrast

Four themes ship from day one: light, dark, high-contrast light, high-contrast dark (`packages/tokens/ldc/*.json`). Dark mode lightens primary and accent (see §2) rather than inverting; surfaces are green-tinted charcoals, not pure black, to keep hairlines visible. High-contrast themes raise every text pair to ≥ 7:1 and borders to ≥ 4.5:1, remove shadows and use 2 px borders. Theme follows the system by default; the user may pin one (Settings › Appearance; shortcut from Settings › Accessibility). Status colours are re-tuned per theme and re-checked by the token build. Charts and RAG chips carry patterns so they survive any theme.

## 9. Motion

`--duration-fast/base/slow` = 100 / 200 / 300 ms; easing standard; motion is used for state change only (drawer open, row expand, toast) and never for attention (no pulsing, no auto-advancing carousels, no parallax). `prefers-reduced-motion` and `a11y.motion.reduced` set every duration to 0 and replace transitions with instant state changes. Loading uses skeletons that match the final layout, not spinners, for lists; spinners only inside buttons.

## 10. Accessibility notes (IPB-06; NN-21)

WCAG 2.2 AA is the release gate on every phase. In addition to the rules above: skip links; focus order follows reading order; the two-tone focus ring is visible everywhere; keyboard shortcuts documented on `?`, remappable, never single-key without a modifier; captions and transcripts on every video (release gate), live captions for webinars; visual alerts for every audible one; forms with error text and summaries; time limits only with extension; language tags per locale; the dyslexia-font option, letter and line spacing steps, reading ruler and text-to-speech in Settings › Accessibility; `gov_facing` mode adds the GIGW 3.0 checklist to the conformance report; third-party components are procured only with a VPAT/ACR (IPB-06 §06.3.10). The Accessibility Statement (Appendix AD §AD.10) is generated from the backlog and never over-claims.

## 11. Do and don't

| Do | Don't |
|---|---|
| Show status as icon + word + colour + pattern | Use colour alone, or gold as text |
| One primary action per screen; explain why a control is disabled | Stack three primary buttons; grey-out without explanation |
| Use IBM Plex Mono for every ID, date and amount in tables | Mix fonts for emphasis |
| Keep the CompID visible when the drawer opens | Open modals over registers |
| Write labels as nouns and buttons as verbs, sentence case | Shout in caps; use exclamation marks or emoji |
| Prefer hairlines and tables to cards and shadows in registers | Decorate registers with illustrations or gradients |
| Let the user undo (NN-49) and say what cannot be undone | Confirm with "Are you sure?" alone |
| Label every AI output and show its citations | Let Vidhi look like a human colleague or hide the provider |
| Use documentary photography with recorded consent | Use stock handshakes, regulator logos or official seals |
| Claim only what the Claims Register evidences (NN-19) | Show badges for standards "in progress" |

## 12. Sample screens (described)

**Public home.** Off-white page; header with logo (left), seven items max, "Free Health Check" as the only primary button (forest green), "Sign in" as text. Hero: one h1 ("Know what applies. Prove what you did."), one sentence, two buttons (primary Health Check, secondary "See how it works"), product screenshot of the compliance list on the right with synthetic data. Below: four steps with mono-numbered labels; a "who it is for" strip of family cards (NBFC, UCB, listed company, AIF, insurer, co-operative, company, LLP); a proof strip that shows only Claims-Registered numbers with sources and as-of dates; a security and trust teaser linking the Trust Centre (no badges unless held); pricing teaser; resources teaser; FAQ; the binding footer (officers line, entity line, social links, legal column).

**Tenant home (`apps/web`).** Left navigation (module names as nouns), top bar with Cmd+K search, notifications bell, Vidhi toggle, user menu. Row 1 widgets per role (Appendix C §C.6.2): "Urgent & upcoming" radar (RAG chips with days-to-due in mono), "Awaiting my approval" (checkers), "Compliance calendar" (owners, mandatory). Row 2: "What changed" (regulatory updates with "affects 12 of your obligations"), "Open findings". One primary action in the top-right: "Work Inbox". No charts above the fold except the radar.

**Compliance list and CompID drawer.** The 9-column list (D-50) in comfortable density, sticky header, frozen S. No. and CompID (mono), status chips with pattern, "Next due" and "Days to due" chips; filter bar with saved views; group-by up to three levels; export builder. Clicking a CompID opens the right drawer (560 px) with the Overview tab: question, instrument and clause (with "i" reference panel), department, due rule, RAG explanation ("Red because due in 2 days and risk High — rule R-04"), maker/checker/auditor status, evidence count, conversation count, accountability summary. Primary action in the drawer footer depends on role ("Mark as done — needs checker approval" for makers).

**Settings (twenty-node tree).** Two-pane: node list in IPB-07 order on the left (Profile … About), content on the right; each node header has a one-sentence purpose and an "i"; nodes outside the plan render with the explanation and upgrade path, never hidden. Security & trust shows the Vendor documents table (type, issuer, period, valid until, gating, download) with the evidence-pack export as the primary action.

**Vidhi panel.** Opened from the top bar; header "Vidhi · Claude via Bedrock (India)" with the AI label; a thread of answers, each with a "Sources" strip (citations to instrument, clause, version) or "No source"; action proposals as cards ("Draft evidence request to Finance — Approve / Edit / Reject"); a footer line "Vidhi drafts; people decide. Locked actions always need approval." Autonomy level and sponsor shown on hover.

**Console › Studio › Brand.** Three-pane: token editor (left), live preview of home, a register and an email (centre), contrast report and host map (right); publish button disabled until the contrast report is clean and a checker is named; version history with one-click rollback.

## 13. Tenant overrides (within guard-rails)

Tenants may change, in Settings › Customisation › Branding (the tenant layer of the `brand_pack`): primary and accent colours (each pair re-checked; failing pairs refused with a suggested shade — `LDC-CFG-094`), logo and favicon, letterhead and PDF cover, email sender identity (after SPF/DKIM/DMARC), custom subdomain or domain, login message. Tenants may not change typography, spacing, status and RAG colours, the AI label, legal disclaimers or statutory form layouts. White-label plans may additionally set `brand.app_name` and the Vidhi display name (`brand.terminology.vidhi`) and receive their own host map; the operating and selling entities still appear on every legal page. Overrides compile to a CSS variable layer applied after the product theme; the product theme is never edited by a tenant.

## 14. Deliverables for the design squad (P23 sprint 1)

Token files for four themes; Figma library mirroring `packages/ui` (buttons, chips, DataTable, drawer, forms, "i" popover, Vidhi panel, toasts, dialogs, empty states); the twelve placeholder illustrations; the public home, Health Check, Trust Centre, pricing and About pages; tenant home, compliance list and drawer, Settings shell, Vidhi panel; accessibility annotations (focus order, names, roles) on every frame; contrast report attached to every colour change. Review with the owner against this brief before Brand Studio is seeded.
