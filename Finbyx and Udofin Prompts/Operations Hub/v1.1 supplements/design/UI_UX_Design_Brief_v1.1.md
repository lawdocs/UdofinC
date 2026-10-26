# Infrabyx Operations Hub — UI/UX Design Brief v1.1

**Date:** 26 October 2026 · **Product code:** OH · **Binding references:** IPB-06 (accessibility), IPB-07 (design system, settings tree, help), IPB-04 (public site, footer, CMP), IPB-D-11 (distinct identity within WCAG 2.2 AA guard-rails); master prompt Part 3.5, Part 7.5, Part 7.7.3. Tags: [REC] recommendation; [OWNER] owner choice; [VERIFY] to confirm.

## 1. Purpose and audience

The Hub is an internal operations platform used all day by staff across eight product scopes and several legal entities, with small external surfaces (client status pages and support portal, professional portal, auditor grants, the group public site). The design goal is **calm density**: operators clear queues quickly, approvals are unmistakable, the acting legal entity and product scope are always visible, and nothing on the screen implies a claim the group cannot evidence. Everything inherits the Infrabyx shared design tokens and IPB-07 components; this brief fixes the Hub's identity and the choices the shared system leaves open.

## 2. Palette

| Token | Value | Use | Contrast notes |
|---|---|---|---|
| `oh.primary` (charcoal) | `#1F2937` | App chrome (sidebar, top bar in dark variant), primary text on light surfaces, headings | 13.6:1 on white; use as text on `#F9FAFB` and `#FFFFFF` only |
| `oh.accent` (electric blue) | `#2563EB` | Primary action buttons, links, focus ring, active navigation, product switcher highlight for `GRP` | 5.2:1 on white (AA for text ≥ 14 px and UI); white text on accent 5.2:1 (AA); do not use accent text on grey surfaces darker than `#E5E7EB` |
| `oh.accent.hover` | `#1D4ED8` | Hover and pressed states | 6.6:1 on white |
| `oh.surface` | `#FFFFFF` / `#F9FAFB` | Page and card surfaces | — |
| `oh.border` | `#E5E7EB` | Dividers, table rules | Non-text; 1.3:1 is acceptable for decorative rules; focus and state borders use `oh.accent` or semantic colours (≥ 3:1) |
| `oh.text.secondary` | `#4B5563` | Secondary text, metadata | 7.6:1 on white |
| `oh.text.disabled` | `#9CA3AF` | Disabled labels (never for required information) | 2.8:1; allowed only for disabled controls per WCAG 1.4.3 exception |
| Semantic | success `#15803D`, warning `#B45309`, danger `#B91C1C`, info `#1D4ED8` | State badges, clocks, SLA bars | Each ≥ 4.5:1 on white; badges pair colour with an icon and text label (never colour alone) |
| Product-scope badges | Read from each product's brand pack accent (LD, LDC, EQ, FBX, UDF); `TRN` and `HSP` placeholders `#0F766E` and `#7C2D12` [OWNER]; `GRP` uses `oh.accent` | Scope badge on every record header and list row | The contrast guard (IPB-07) rejects any pack accent below 3:1 against `oh.surface` for badge fills; text in badges is white or charcoal, whichever reaches 4.5:1 |

**Dark mode.** Surfaces `#111827` and `#1F2937`, text `#F9FAFB` and `#D1D5DB`, accent lightened to `#60A5FA` for text and links (8.6:1 on `#111827`) while buttons keep `#2563EB` with white text; semantic colours shift one step lighter; the legal-entity and scope badges keep their fills with an automatic text-colour switch. Dark mode is a user Appearance setting and a system-preference default; charts re-tokenise through the shared palette (no hard-coded hex in components).

**Legal-entity (tenant) overrides.** A group company may set its logo, favicon and one accent for its own entity view. The Brand Studio contrast guard refuses an accent that fails 4.5:1 for text or 3:1 for UI against the fixed surfaces; it never permits changes to semantic colours, focus ring, charcoal chrome, badge rules or the mandatory indicators (AI label, data class, autonomy level, acting entity).

## 3. Typography

- **Family:** Inter (variable), self-hosted under the Google Fonts licence [VERIFY: licence file in `packages/ui`]; Devanagari fallback **Noto Sans Devanagari** for Hindi strings with matched x-height; monospace **JetBrains Mono** for identifiers, hashes, amounts in tables [REC].
- **Scale (desktop):** 12 (meta), 13 (dense table cells — compact density only), 14 (body in compact), 16 (body in comfortable; minimum on public and self-service pages), 18 (section titles), 22 (page titles), 28 (public hero sub-head), 36–44 (public hero). Line height 1.45 body, 1.25 headings. Numbers in tables use tabular figures; amounts right-aligned with the ₹ sign and Indian grouping (lakh and crore) through the shared formatter.
- **Weights:** 400 body, 500 labels and table headers, 600 headings and primary buttons. No italics for emphasis in UI; use weight or colour.
- **Text scaling:** layouts must survive 200% browser zoom and the Accessibility setting "Larger text" without horizontal scrolling on desktop and without clipping on 360 px mobile.

## 4. Spacing, grid and density

- **4 px base unit**; spacing scale 4, 8, 12, 16, 24, 32, 48. Content max width 1,440 px with a 240 px collapsible sidebar (64 px rail when collapsed); 12-column grid at ≥ 1,024 px, 4 columns on mobile; 16 px side gutter on phones.
- **Density modes:** *Compact* (default for `OPS_*` roles; 36 px rows, 13–14 px text) and *Comfortable* (44 px rows, 16 px text; default for self-service, interns, the public site and external portals). Density is a per-user Appearance setting and is never forced below comfortable on public routes.
- **Tables:** sticky header, frozen first column (reference and scope badge), row hover, 10-second undo toast for non-financial bulk edits, column chooser saved with the view, empty state inside the table frame.

## 5. Component tone and interaction rules

- **One primary action per screen** (electric-blue filled); secondary actions outlined charcoal; destructive actions outlined danger with a confirmation dialog that states consequences and names the record. Approvals use a dedicated approval card: what changes (diff), who asked, evidence links, consequences, fresh-MFA prompt, Approve or Reject with reason.
- **Explain-why messages:** every refusal names the rule and its source in plain English ("Cannot schedule: claims gate blocked the phrase 'RBI approved' — OH7.5"). Error text is never red-only; it carries an icon and a label.
- **Acting context bar:** legal-entity switcher, product switcher (hidden when the user holds one scope), environment ribbon (synthetic data environments show a persistent amber ribbon "Synthetic data — not production"), and the Vidhi side-panel toggle. The acting entity and scope badge also appear in every record header and approval card.
- **Work Inbox** is the landing route for operators: items grouped by time to breach, each with one deterministic next-best-action button; keyboard `J`/`K`, `A`, `E`, `/`, `M`; the inbox never shows RESTRICTED snippets.
- **Clocks and SLAs:** horizontal bars with remaining time in words ("1 h 40 m to breach"), colour plus icon; breached items pin to the top.
- **Forms:** inline validation on blur, "i" help on every field (IPB-07 popover with plain text, regulatory reference panel and "Learn more"), never a disabled submit without an explanation of what is missing.
- **Vidhi surfaces:** side panel 400 px (collapsible), palette results with the AI label, inline suggestions as dashed-outline chips; every surface shows the four mandatory indicators (AI label, data class chip, autonomy level, "Why this answer?") in a fixed footer; streaming output announced to screen readers through a live region.
- **Motion:** 150–200 ms ease-out for panels and toasts; no parallax, no auto-play; `prefers-reduced-motion` disables all non-essential motion; progress uses determinate bars where the system knows the total.

## 6. Iconography

Lucide icon set (outline, 1.5 px stroke) at 16 and 20 px [REC]; icons always carry a text label or `aria-label`; product scopes use a two-letter monogram badge rather than product logos inside the Hub (logos appear on public pages and invoices only); state icons are consistent across modules (clock = SLA, shield = trust or security, scale = legal or Equator, receipt = billing, people = HR). No icon implies certification or endorsement.

## 7. Imagery and placeholders

Internal screens use no decorative imagery. The group public site (OH18) uses a small set of owner-replaceable placeholders managed in Brand Studio; all photos need recorded consent for identifiable people; no stock imagery implying regulators, courts or banks endorsing the group; no imagery of currency notes or "guaranteed returns" motifs.

| Placeholder id | Page and position | Recommended size | Alt text (draft) |
|---|---|---|---|
| `img.home.hero` | Home hero right | 1,600 × 1,000 px (2x), WebP ≤ 180 KB | "Abstract illustration of connected modules representing the Infrabyx group's products" |
| `img.home.products.{ld,ldc,eq,fbx,udf,trn,hsp}` | Group companies cards | 640 × 400 px each | "{Product} wordmark on a neutral background" |
| `img.about.timeline.{n}` | About milestones | 480 × 320 px | "Photograph or illustration for the {year} milestone: {event}" |
| `img.team.{person}` | Team and leadership grids | 600 × 600 px, square | "{Name}, {role}" (photo only with recorded consent) |
| `img.offices.{delhi,noida,jaipur}` | Contact offices | 800 × 500 px | "Exterior or reception of the Infrabyx {city} office" |
| `img.offices.map.{city}` | Contact static map (click-to-load) | 800 × 400 px | "Static map showing the {city} office location; opens the map provider on click" |
| `img.careers.culture.{n}` | Careers | 800 × 500 px | "Infrabyx team members working together at the {city} office" (consent recorded) |
| `img.trust.residency` | Trust Centre | 960 × 480 px diagram | "Diagram showing production data hosted in Mumbai with disaster recovery in Hyderabad" |
| `img.press.kit.logo.{variant}` | Media kit | SVG and PNG 2,000 px | "Infrabyx group logo, {variant}" |
| `img.og.default` | Open Graph default | 1,200 × 630 px | "Infrabyx Group — software and services for regulated India" |
| `img.favicon` | Favicon set | 32, 180, 512 px | — |
| `img.help.tutorial.{slug}.poster` | Tutorial posters | 1,280 × 720 px | "Poster frame for the tutorial '{title}'" |

Every image has alt text or is marked decorative; EXIF is stripped on upload; SVGs are sanitised.

## 8. Accessibility notes (IPB-06)

- WCAG 2.2 AA and IS 17802 on every surface; GIGW 3.0 principles on the public site.
- **Hearing:** captions and transcripts on all tutorials and audio overviews; live captions on support calls; visual alerts for mandatory notifications (badge pulse plus toast, never sound alone).
- **Vision:** contrast guard at build time; text scaling to 200%; dyslexia-friendly font option (Atkinson Hyperlegible or OpenDyslexic [OWNER]); TTS for long texts; focus ring 2 px electric blue with 2 px white offset visible on every surface including dark mode.
- **Motor:** targets ≥ 24 × 24 px (44 px on mobile check-in and approvals); keyboard operability for every action; remappable keyboard map for operators; no drag-only interactions (Gantt and kanban have keyboard move commands).
- **Cognitive and low literacy:** plain-language mode rewrites Vidhi outputs at about CEFR B1; Hindi for self-service with payslip explanations; no time-outs on approvals without a warning and an extension; consistent placement of primary actions.
- **Testing:** axe-core zero critical in CI; manual screen-reader scripts (NVDA, VoiceOver) at each phase gate; the accessibility statement (IPB-05 Template 10) lists known issues from the backlog.

## 9. Empty, loading and error states

- Empty states explain what will appear and the first action ("No vendor documents yet — upload the ISO 27001 certificate or run the cadence calendar").
- Loading uses skeletons that match the final layout; never spinners over whole pages.
- Integration outages show a banner with the last successful sync and never block unrelated work; blocked writes name the rule and the permitted alternative ("HR data cannot be stored in Google Workspace; save it in the Hub records service").
- Denied scope or entity reads show a neutral "Not available in your current scope" message (no record details) and offer the switcher where the user holds another scope.

## 10. Sample screens (described)

1. **Home (Work Inbox, operator):** context bar with entity and scope switchers; left rail; main column of inbox groups (Breaching, Today, This week) with one-line items and a next-best-action button; right column of role tiles (My Queue count, approvals waiting, clocks); Vidhi panel collapsed with a "What Vidhi did today" count.
2. **Per-product dashboard (for example FBX scope):** KPI tiles (clients, renewals in 120 days, open Sev 1–2, projects RAG, marketing calendar this week, cadence items due, invoices overdue) each linking to its governed metric; group roles see the same layout with "aggregate only" badges.
3. **Record detail (ticket, project, invoice):** header with reference, state, owner, entity badge, scope badge and clocks; tabs; timeline; audit trail; right rail of linked records and the "i" help; one primary action.
4. **Approval queue:** list of approval cards; opening a card shows diff, evidence and consequences; fresh-MFA step inline; Approve is primary, Reject requires a reason.
5. **Settings (IPB-07 tree):** left tree with the twenty nodes in binding order and platform-only nodes below for `PLT_*`; each setting shows level, default, floor and nature, with maker-checker where required.
6. **Vidhi panel:** context header (record, data class), conversation, citations drawer, the four indicators footer, feedback controls, approval cards for L2 actions.
7. **Payroll variance review:** two-pane layout (variance list with reasons to clear; line detail with inputs and formula versions); release button disabled with the reasons listed until every variance is cleared; RESTRICTED watermark.
8. **Public home (group site):** charcoal top bar with white logo, hero with one h1 and a single CTA, product cards with consistent monograms, trust teaser linking to the Trust Centre (badges only for certifications held), footer per IPB-04 with entity and officer lines; CMP banner with three equal buttons on first visit.

## 11. Do and don't

| Do | Don't |
|---|---|
| Show the acting legal entity and product scope on every record | Rely on colour alone for state, scope or severity |
| One primary action per screen; explain every refusal with its rule | Place two filled accent buttons on one screen |
| Pair every badge and icon with text | Use product logos inside internal lists (monograms only) |
| Keep public body text ≥ 16 px and comfortable density | Use charcoal `#1F2937` text on mid-grey surfaces or accent text on dark grey |
| Use the shared formatter for ₹, dates (DD-MM-YYYY) and IST | Hard-code hex values, date formats or currency symbols in components |
| Label AI output on every surface with the four indicators | Show AI text without citations or without the autonomy level |
| Use "designed to align with" wording for standards in progress | Show certification badges, "secure", "compliant" or "RBI approved" anywhere |
| Respect quiet hours and reduced motion | Auto-play media or animate on load |
| Provide keyboard commands for every drag interaction | Build drag-only Gantt or kanban moves |
| Mark synthetic environments with the amber ribbon | Let a demo screenshot look like production |

## 12. Tenant override envelope (summary)

Group companies may change: logo, favicon, one accent colour (contrast-guarded), display name on their entity view, e-mail sender identity, footer office lines. They may not change: charcoal chrome, semantic colours, focus ring, typography family and scale, density floors, mandatory indicators, the IPB-04 footer structure, consent UI, or any text governed by the claims gate. White-label packs for Finbyx and Udofin resale are governed by their own products and only read by the Hub.

## 13. Deliverables for Phase O1 and O17

- `packages/ui` tokens file with the Hub theme (`theme.oh.json`) and dark variant; contrast-guard test fixtures for every token pair in §2.
- Storybook stories for: context bar, scope badge, approval card, Work Inbox item, clock bar, Vidhi panel footer, empty states, CMP banner, footer.
- Figma or Claude Design file mirroring the eight sample screens with annotations for keyboard and screen-reader behaviour [OWNER: tool choice; IPB-13].
- Public-site templates for the standard pages with the placeholder table of §7 wired to Brand Studio.
