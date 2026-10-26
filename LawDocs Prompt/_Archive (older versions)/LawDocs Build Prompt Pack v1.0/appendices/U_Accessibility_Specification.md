# Appendix U — Accessibility Specification

> **Status:** Binding for every phase and every surface (`apps/public`, `apps/web`, `apps/delivery`, `apps/console`, `apps/mobile`, generated documents, emails, SMS/WhatsApp/RCS templates, PDFs, videos). Enforces NN-28.
> **Used by:** P00 (tooling in CI), P01 (accessible authentication and KYC), P04 (vault tables, upload), P05 (renditions, TTS, translation), P06/P07 (drafter, redline viewer, deal rooms), P08 (signing ceremony, eStamp), P10/P11 (pleadings, calendars), P13 (board packs), P15 (Consumer Help), P16/P17 (marketplace, pricing, checkout), P21 (owner of the public statement, help centre, tutorials), P22 (native mobile), P23 (release gate and audit evidence).
> **Prepared:** 25 October 2026. Legal baseline from R3 §11 (LG-133–LG-137); research items keep their [VERIFY] tags.
>
> **How to use.** §U.1 states the legal floor. §U.3 maps every WCAG 2.2 Level A and AA success criterion and the IS 17802 additions to the shared components that satisfy them, so a feature built from `packages/ui` inherits conformance. §U.5 gives the screen-reader patterns for LawDocs' complex widgets. §U.6–§U.7 cover media, easy-read, text-to-speech, voice input, themes and cognitive accessibility. §U.8–§U.9 define the test protocol (including testing with disabled users), severities and the release gate. §U.10 is the accessibility statement template. A phase may not exit with an open S1 accessibility defect on a critical journey.

---

## U.1 Legal and standards baseline

| Rule ID | Instrument / provision | What LawDocs does | Confidence |
|---|---|---|---|
| LG-133 | **Rights of Persons with Disabilities Act 2016**: s.40 (accessibility standards, including information and communication technology), s.42 (accessible electronic content; audio description, sign-language interpretation and close captioning), s.44 (mandatory observance), s.46 (service providers to provide services per the rules within the time stated [VERIFY period]), s.89 (fines: ₹10,000 first contravention; ₹50,000 to ₹5 lakh for subsequent contraventions) | Treat accessibility as a legal floor; publish a statement and a grievance route; keep audit evidence per release | [VERIFY text] |
| LG-134 | **RPwD Rules 2017, r.15** (as amended [VERIFY 2023 amendment]): websites per **GIGW 3.0**; ICT products and services per **IS 17802 Parts 1–2** | Target **WCAG 2.2 Level AA** (W3C Recommendation, 5 October 2023) **plus IS 17802** requirements beyond WCAG, and GIGW 3.0 where applicable to public-facing content | [VERIFY] |
| LG-135 | ***Rajive Raturi v. Union of India*** (SC, 8 Nov 2024): guideline-only approach of r.15 inconsistent with the Act; mandatory rules to be framed [VERIFY directions] | `a11y.standard_set` is a governed setting so new mandatory rules can be adopted without code changes | [VERIFY] |
| LG-136 | ***Pragya Prasun v. Union of India*** (SC, 30 Apr 2025): digital access part of Article 21; directions for accessible digital KYC (alternatives to blink/liveness, accessible formats), revision of KYC norms, accessibility audits [VERIFY] | KYC and eSign journeys offer non-visual, non-liveness options and an assisted route (§U.7.4) | [VERIFY] |
| LG-137 | **Indian Sign Language** (ISLRTC); s.42 captions and interpretation | Captions and transcripts on all video; ISL renditions of core tutorials; ISL video-call option for assisted help and consultations | [VERIFY] |
| — | Consumer Protection (E-Commerce) Rules 2020 r.4 grievance clocks (R3 LG-141) | Accessibility feedback acknowledged ≤ 48 h, resolved or planned ≤ 1 month | [VERIFY] |

**Principles (binding):**
1. **Native accessibility, no overlays.** No third-party "accessibility widget" or overlay script on any surface (NN-28).
2. **Shift left.** Accessibility is built into `packages/ui`, `packages/a11y` and `packages/tokens`; feature teams compose accessible components rather than retrofit.
3. **Equivalent journeys.** Every critical journey has an accessible path of equal security and cost; an assisted human route never costs extra.
4. **Documents count.** Generated PDFs are tagged (PDF/UA where feasible; PDF/A-2a or 3a for archival copies where the conversion pipeline supports tagging [VERIFY Gotenberg/LibreOffice tagged output]); DOCX outputs use real headings, lists, tables with header rows, alt text and document language.
5. **Language.** Accessibility applies in every D-07 language: screen-reader pronunciation, `lang` attributes, TTS voices and captions per locale.

## U.2 Scope and critical journeys

**Critical journeys** (tested manually every release on web and mobile; S1 if blocked):

| ID | Journey | Phases |
|---|---|---|
| CJ-01 | Sign up / sign in (OTP, passkey) and recover access | P01 |
| CJ-02 | Verify identity (Aadhaar offline verification, DigiLocker, assisted route) | P01 |
| CJ-03 | Draft a document from a template (questionnaire → preview → save) | P06, P21 |
| CJ-04 | Review changes and comment in a negotiation | P07 |
| CJ-05 | Pay stamp duty or buy a service (fee breakdown → hosted checkout) | P08, P16, P17 |
| CJ-06 | Sign a document (eligibility → pre-sign summary → ESP → confirmation) | P08, P22 |
| CJ-07 | Find, open and share a document in the vault; download or export | P04, P20 |
| CJ-08 | Approve or return an item as checker | P02, P13 |
| CJ-09 | Track a case or hearing and receive a reminder | P11 |
| CJ-10 | Get help: help panel, "i" term, contact support, accessibility feedback | P21 |
| CJ-11 | Scan or import a document on mobile, with Aadhaar masking | P22, P05 |
| CJ-12 | Consumer Help: open a case and follow its status (brand flavour) | P15 |

## U.3 Success-criteria mapping

### U.3.1 WCAG 2.2 Level A and AA → LawDocs components

Components are in `packages/ui` (web, React) and `packages/ui/native` (React Native). "Auto" = automated test (axe-core, eslint-plugin-jsx-a11y, RN accessibility lint, Maestro label assertions); "Man" = manual test in §U.8.

| SC | Level | Component(s) and rule | Test |
|---|---|---|---|
| 1.1.1 Non-text Content | A | `Image` requires `alt` or `decorative`; icon buttons require accessible names; charts have data-table alternatives; CMS blocks publish without alt text (P21) | Auto + Man |
| 1.2.1 Audio-only and Video-only | A | `MediaPlayer` requires transcript for audio-only (voice notes: labelled machine transcript) and description for silent video | Man |
| 1.2.2 Captions (Prerecorded) | A | `MediaPlayer` refuses publish without a caption track (`LD-HLP-003`) | Auto |
| 1.2.3 Audio Description or Media Alternative | A | Full transcript including visual information | Man |
| 1.2.4 Captions (Live) | AA | Webinars and live consultations: live captions (human CART or labelled ASR) where offered | Man |
| 1.2.5 Audio Description (Prerecorded) | AA | Described or extended version where visuals carry meaning not in narration | Man |
| 1.3.1 Info and Relationships | A | Semantic headings, lists, `Table` with `th scope`, `Fieldset`/`legend` for radio and checkbox groups, form labels programmatically associated | Auto + Man |
| 1.3.2 Meaningful Sequence | A | DOM order = visual order; RN `accessibilityElements`/order match reading order | Man |
| 1.3.3 Sensory Characteristics | A | Copy rule: no "click the green button" (Appendix N §N.1.3) | Man |
| 1.3.4 Orientation | AA | Web and mobile support portrait and landscape; scanner works in both | Man |
| 1.3.5 Identify Input Purpose | AA | `autocomplete` tokens on name, email, tel, address, `one-time-code`; RN `textContentType`/`autoComplete` | Auto |
| 1.4.1 Use of Color | A | Status chips carry text and icon; redline insert/delete use underline/strikethrough plus labels, not colour alone | Auto (lint on chip) + Man |
| 1.4.2 Audio Control | A | No autoplay with sound anywhere | Auto |
| 1.4.3 Contrast (Minimum) | AA | Token pairs validated ≥ 4.5:1 (text) and ≥ 3:1 (large text) in all themes; CI token test | Auto |
| 1.4.4 Resize Text | AA | Rem-based type; 200% without loss; mobile Dynamic Type/font scale | Man |
| 1.4.5 Images of Text | AA | No text in images except logos; OG images are decorative duplicates of visible text | Man |
| 1.4.10 Reflow | AA | Layout works at 320 CSS px (400% zoom) without two-dimensional scrolling, except data tables and redline side-by-side, which offer a single-column mode | Man |
| 1.4.11 Non-text Contrast | AA | Focus ring, input borders, toggles, chart marks ≥ 3:1 | Auto |
| 1.4.12 Text Spacing | AA | No clipping with increased line, letter, word and paragraph spacing | Man |
| 1.4.13 Content on Hover or Focus | AA | `Popover` ("i"), `Tooltip`: dismissible (Escape), hoverable, persistent | Auto + Man |
| 2.1.1 Keyboard | A | All actions keyboard-operable, including drag-and-drop alternatives, signature placement, redline accept/reject, calendar navigation | Man |
| 2.1.2 No Keyboard Trap | A | `Dialog` traps focus only while open; Escape closes | Auto + Man |
| 2.1.4 Character Key Shortcuts | A | Single-key shortcuts (e.g., `?` for help) can be turned off or remapped in accessibility preferences | Man |
| 2.2.1 Timing Adjustable | A | Session time-out warning ≥ 120 s ahead (`a11y.session_timeout_warning_seconds`) with "Extend"; OTP validity extendable by resend without losing entered data; no time limits on questionnaires | Man |
| 2.2.2 Pause, Stop, Hide | A | Carousels and animations have pause; no auto-advancing content | Man |
| 2.3.1 Three Flashes | A | Motion tokens; video pipeline flash check | Auto (video) |
| 2.4.1 Bypass Blocks | A | "Skip to main content" link; landmarks | Auto |
| 2.4.2 Page Titled | A | Unique titles per route; SPA route changes update title and announce | Auto |
| 2.4.3 Focus Order | A | Logical order; focus moves to new content (dialogs, step changes) and returns on close | Man |
| 2.4.4 Link Purpose | A | Link text lint (no "click here", "read more" without context) | Auto |
| 2.4.5 Multiple Ways | AA | Navigation + search + sitemap + breadcrumbs | Man |
| 2.4.6 Headings and Labels | AA | Descriptive headings and labels; CMS heading-order check | Auto |
| 2.4.7 Focus Visible | AA | Focus ring token (2 px, ≥ 3:1, offset) never removed | Auto |
| 2.4.11 Focus Not Obscured (Minimum) | AA | Sticky headers, bottom bars (P21 FR-P21-15), toasts and cookie banners never cover the focused element; `scroll-padding` set | Man |
| 2.5.1 Pointer Gestures | A | Pinch/zoom in viewers also via buttons; no path gestures | Man |
| 2.5.2 Pointer Cancellation | A | Actions on up-event; signing and payment buttons require confirm | Man |
| 2.5.3 Label in Name | A | Visible label text included in accessible name (voice control) | Auto |
| 2.5.4 Motion Actuation | A | No shake-to-undo or tilt actions | Man |
| 2.5.7 Dragging Movements | AA | Folder moves, file reorder, signature-field placement, scanner corner adjustment all have non-drag alternatives (buttons, menus, numeric entry) | Man |
| 2.5.8 Target Size (Minimum) | AA | ≥ 24 × 24 CSS px on web; 44 pt / 48 dp on mobile | Auto (lint) + Man |
| 3.1.1 Language of Page | A | `lang` per locale | Auto |
| 3.1.2 Language of Parts | AA | `lang` on quoted Hindi/other-script passages, legal Latin maxims and bilingual documents | Man |
| 3.2.1 On Focus / 3.2.2 On Input | A | No context change on focus or selection; State selectors update content in place and announce | Man |
| 3.2.3 Consistent Navigation / 3.2.4 Consistent Identification | AA | Shared shell and icon set; same names for same functions across apps | Man |
| 3.2.6 Consistent Help | A | Help button in the same place on every screen (P21 FR-P21-112) | Man |
| 3.3.1 Error Identification / 3.3.3 Error Suggestion | A / AA | `Form` error summary at top with links to fields; field-level messages with `LD-…` code, plain text and help key | Auto + Man |
| 3.3.2 Labels or Instructions | A | Visible labels (no placeholder-only), required markers in text, format hints (PAN, dates) | Auto |
| 3.3.4 Error Prevention (Legal, Financial, Data) | AA | Review step before signing, paying, filing, sharing outside tenant or deleting; reversible where possible; confirmation pages show what will happen | Man |
| 3.3.7 Redundant Entry | A | Profile, party and address data reused across questionnaires; never asked twice in a flow | Man |
| 3.3.8 Accessible Authentication (Minimum) | AA | OTP paste and autofill allowed; passkeys; password managers supported; no puzzle CAPTCHA (privacy-preserving checks with an email/SMS fallback) | Man |
| 4.1.2 Name, Role, Value | A | All custom widgets follow WAI-ARIA Authoring Practices or native roles; RN `accessibilityRole/State/Value` | Auto + Man |
| 4.1.3 Status Messages | AA | `LiveRegion` for save confirmations, upload progress, payment "Confirming…", search counts, signing status | Man |

### U.3.2 IS 17802 additions beyond WCAG (mapped to LawDocs) [VERIFY clause numbering against IS 17802 Parts 1–2; it follows the EN 301 549 structure]

| Area (EN 301 549-style clause) | Requirement in brief | LawDocs implementation |
|---|---|---|
| Generic — biometrics (5.3) | Biometrics not the only means of identification or control | Biometric unlock is optional; OTP and passkey alternatives always available (P22 FR-P22-14); no liveness-only KYC (§U.7.4) |
| Generic — preservation of accessibility information in conversion (5.4) | Conversions keep structure | DOCX → PDF keeps tags, headings, alt text; OCR renditions produce structured text; translations keep headings |
| Two-way voice/video communication (Clause 6) | Real-time text alongside voice; video quality sufficient for sign language | In-app consultations (WebRTC) offer chat alongside voice; video profile supports sign language (target ≥ 20 fps at QVGA or better [VERIFY threshold]); captions where enabled |
| Video capabilities (Clause 7) | Caption and audio-description playback, user controls for captions | `MediaPlayer` caption toggle, size and background options, audio-description track selection |
| Web (Clause 9) | WCAG 2.x AA | §U.3.1 |
| Non-web documents (Clause 10) | Documents accessible (WCAG applied to documents) | Tagged PDF, accessible DOCX/XLSX exports (header rows, sheet names, no merged-cell headers), `00 READ ME FIRST.pdf` of `LD-EXPORT-1.0` tagged |
| Software (Clause 11) — platform accessibility services, user preferences (11.7) | Use platform APIs; honour OS settings | Respect OS text size, reduced motion, high contrast/forced colours, dark mode |
| Software — authoring tools (11.8) | Authoring tools support creation of accessible content | Content Studio: alt-text prompts, heading checks, table header settings, caption editor, accessibility checker that blocks publish (P21 FR-P21-80) |
| Documentation and support services (Clause 12) | Product documentation accessible; support services accommodate communication needs | Help centre conforms; support via chat, email, phone, WhatsApp and ISL video on request (P21 FR-P21-117) |
| Closed functionality (5.2) | Kiosk-like closed systems | Not applicable (no kiosks) |

## U.4 Component and token rules (`packages/ui`, `packages/a11y`, `packages/tokens`)

1. **Tokens:** colour pairs pre-validated for contrast in four themes (default, dark, high contrast light, high contrast dark); type scale in rem with a minimum body size of 16 px web / 16 pt mobile; line-height ≥ 1.5 for body; motion durations with a reduced-motion variant of 0 ms.
2. **Focus:** visible 2 px ring with offset in all themes; `:focus-visible` used; never `outline: none` without replacement (lint).
3. **Forms:** `Field` = label + control + hint + error, wired with `aria-describedby`; required in text ("required"), not only by asterisk; input masks never block paste; PAN, IFSC, pincode and date inputs accept common formats and normalise.
4. **OTP input:** a single input with `autocomplete="one-time-code"` and `inputmode="numeric"` (not six separate boxes); paste allowed; resend timer announced politely; voice-call OTP option where available.
5. **Dialogs:** native `<dialog>` or ARIA dialog pattern with focus trap, initial focus on the title or first control, Escape closes, focus returns.
6. **"i" popover:** per P21 FR-P21-121; non-modal; not hover-only.
7. **Toasts:** never the only place for important information; persist until dismissed for errors; announced via `role="status"` or `alert` as appropriate.
8. **File upload:** button-based selection with drag-and-drop as an enhancement; progress announced; errors linked to the file.
9. **Signature capture:** drawn signatures (where a tenant uses them for internal acknowledgement) always offer typed-name or click-to-adopt alternatives; Aadhaar eSign and DSC are not drawn.
10. **Charts:** every chart has a visible or toggleable data table and a text summary; patterns plus colour.
11. **Lint and test helpers:** `packages/a11y` exports `expectNoAxeViolations`, focus-order helpers, RN label assertions; ESLint rules `jsx-a11y/*` at error level; custom rules for `term=` "i" keys (P21 `LD-HLP-001`) and banned patterns (`aria-hidden` on focusable, positive `tabindex`).

## U.5 Screen-reader patterns for complex widgets

### U.5.1 Redline viewer (P07)

- **Structure:** document rendered as headed regions per clause (`h2`/`h3` from clause numbering); each tracked change is an inline element with role `mark`-like semantics announced as "Insertion by {author}: {text}" / "Deletion by {author}: {text}" (implemented with visually hidden prefixes, not colour); comments are linked footnote-style ("Comment 3 by {author}").
- **Navigation:** a "Changes" panel lists all changes as a navigable list ("Change 4 of 17, clause 7.2, insertion by Meera, pending"); keyboard shortcuts `n`/`p` for next/previous change (remappable, U.3.1 2.1.4); Enter jumps focus to the change in the document; actions "Accept", "Reject", "Comment" are buttons on the focused change.
- **Side-by-side compare** has a single-column "Before / After" mode for screen readers and reflow.
- **Status:** accepting or rejecting announces the result and the remaining count via live region.
- **Internal vs external comments** (NN-37): the audience is part of the accessible name ("Internal comment — not visible to counterparty").

### U.5.2 Signing ceremony (P08, P22)

1. Pre-sign summary is a linear page: heading "Review before you sign", then document title, reference, pages, signer, document hash prefix (read in groups of four characters), stamp status, the legal statement, and the consent checkbox with a full-text label.
2. "Read the document" opens the accessible text rendition generated from the source DOCX (not OCR) with clause navigation; a "Listen" control reads it via TTS (§U.6.4).
3. Signature-field placement (for the initiator) has a form alternative: choose page and position from a list ("Page 3, below 'Signed by the Tenant'") instead of dragging.
4. The ESP step opens in the system browser; LawDocs announces before leaving ("You will now go to {ESP} to complete Aadhaar eSign. You will return here automatically.") and on return announces the server-confirmed result. ESP page accessibility is a vendor requirement (§U.11).
5. Time-outs on the LawDocs side are extendable; if the ESP session times out, the user can restart without re-entering data.
6. Completion page lists next steps (evidence pack, stamp/registration tasks) as a list of links.

### U.5.3 Calendars (legal calendar, hearings, deadlines, meeting scheduling)

- Default **list view** (agenda) for screen readers and mobile: grouped by date headings, each item with time, type, matter and status in text.
- Month grid uses the ARIA grid pattern: arrow keys move by day, Page Up/Down by month, Home/End to week start/end; each cell's name includes the date and count ("Tuesday 12 May 2026, 2 hearings").
- Date pickers accept typed dates in the user's locale format with validation; the calendar popup is optional.
- Time zones: IST shown explicitly; reminders announced with absolute times.

### U.5.4 Data tables (vault lists, matters, approvals, invoices)

- Native `<table>` with `caption`, `th scope="col"`, row headers for the primary column (document name), sort buttons inside headers announcing sort state (`aria-sort`).
- Selection via checkboxes with labels including the row name; bulk actions bar announces selection count.
- Pagination or "Load more" (no infinite scroll without a keyboard path); results count in a live region after filtering.
- Responsive: at narrow widths, switch to a card list that preserves header–value pairs, rather than horizontal scroll.
- Large tables (≥ 1,000 rows) virtualise with correct `aria-rowcount`/`aria-rowindex`.

### U.5.5 Document viewer and renditions (P04, P05)

- Originals (PDF/images) viewed with a tagged-PDF-aware viewer where tags exist; scanned images offer the OCR or type-copy rendition as the accessible alternative, labelled with confidence ("Machine-read text, 92% confidence — check against the original").
- Zoom controls as buttons; page navigation by number; the viewer never traps keyboard focus.

### U.5.6 Questionnaires and the drafter (P06, P21)

- One question per step with a heading that includes the step ("Question 3 of 7: Monthly rent"); progress announced; Back preserves answers.
- Answers explained by "i" popovers; examples in hints; errors summarised.
- Preview available as accessible HTML with headings, not only as page images.

### U.5.7 Chat and deal rooms (P07, P09, P22)

- Message list as a `log` region with polite announcements of new messages (rate-limited); each message announced with sender, time and audience; composer clearly labelled with audience; voice notes with transcripts.
- Vidhi chat: the AI disclosure is the first message and is read; streaming responses are announced once complete (not token by token).

### U.5.8 Maker-checker diff and approval views (P02, P13)

- Field-level diffs presented as "Field: old value → new value" text rows; the approve/return controls follow the diff and require confirmation (3.3.4).

### U.5.9 Drag-and-drop folder upload (P04)

- Primary path: "Choose folder" button (directory picker where supported) or ZIP upload; drag-and-drop only as an enhancement; the mapping preview is a table; progress per file announced in batches.

## U.6 Media, easy-read, text-to-speech and voice input

### U.6.1 Captions and transcripts

All prerecorded video: accurate captions (≥ 99%), speaker labels, sound cues; on-page transcripts in HTML; captions on by default for in-app tutorials (`hlp.video.captions_default_on`); user controls for caption size and background. Production rules in Appendix N §N.10.4.

### U.6.2 Sign-language video

ISL renditions for the core tutorial set (Appendix N §N.10.3 ★), recorded by qualified interpreters; picture-in-picture or side-by-side with the interpreter ≥ 1/4 of frame height; separate ISL file linked from each standard video. Assisted help and professional consultations can be booked with an ISL interpreter on request (scheduling through the Operations Hub support desk); the cost of interpretation for LawDocs-run sessions is borne by LawDocs [REC].

### U.6.3 Easy-read mode

- A user preference (`hlp.user_prefs.easy_read`) and per-page toggle on public legal explainers, help articles, notices received in the app and Consumer Help pages.
- Easy-read versions: short sentences (≤ 15 words), one idea per line, common words, defined terms inline, supporting icons with text, numbered steps.
- **Plain-language summaries of documents** (cognitive accessibility): for agreements and notices, a summary ("What this agreement says: …; What you must do: …; Key dates: …") generated from template metadata (template lane: deterministic, from clause tags) or by Vidhi (labelled "AI summary — not legal advice; the document is what counts", NN-14). Summaries are derived renditions, never replace the document, and carry the version they summarise.

### U.6.4 Text-to-speech (TTS) of documents

- "Listen" on documents (accessible text rendition), summaries, help articles, glossary definitions, notices and Vidhi answers; controls for play/pause, speed (0.75×–2×), skip by heading; highlight of the sentence being read (sync) where feasible.
- Voices per D-07 language through `TTS_PORT` (India-resident providers; on-device fallback); machine-translated text carries a spoken disclaimer (NN-48); confidential classes use on-device TTS only (P22 FR-P22-60).
- Pronunciation lexicon for legal terms and abbreviations (BNSS, CNR, GSTIN read as letters; "s.138" read as "section 138").

### U.6.5 Voice input

- Push-to-talk dictation on all free-text fields and Vidhi; the transcript is shown for confirmation before submission; voice is never the only input method.
- Supports platform voice control (Voice Control on iOS/macOS, Voice Access on Android, Dragon on Windows) through correct labels (2.5.3).

## U.7 Themes, cognitive accessibility and accessible identity flows

### U.7.1 Themes and display preferences

Default, dark, high contrast (light and dark), forced-colours support (Windows), text size 100–200% within the app plus OS scaling, increased line and paragraph spacing, dyslexia-friendly font option, reduced motion, underline all links option. Stored per user (`hlp.user_prefs`) and synchronised across web and mobile; available before login on the public site (preference cookie, strictly necessary).

### U.7.2 Cognitive accessibility

| Need | Design rule |
|---|---|
| Understanding legal terms | "i" glossary everywhere (P21 §4N); plain definitions ≤ 40 words at grade ≤ 8 |
| Knowing where you are | Breadcrumbs, step indicators, consistent layouts and names (3.2.3/3.2.4) |
| Avoiding costly mistakes | Review-and-confirm before sign, pay, file, share externally, delete (3.3.4); undo for non-legal actions; drafts autosave |
| Memory load | No re-entry of data (3.3.7); summaries of previous steps visible; reminders by notification |
| Time pressure | No timed questions; extendable sessions; no false urgency (NN-50) |
| Reading load | Easy-read mode; summaries; numbered steps; one primary action per screen |
| Authentication | No cognitive tests (3.3.8); OTP paste/autofill; passkeys; magic links |
| Error recovery | Plain-language errors with the fix and an "i" link; error codes for support but not as the only message |

### U.7.3 Accessible notifications and communications

Emails use semantic HTML, sufficient contrast, plain-text alternative, meaningful link text and no image-only content; SMS/WhatsApp/RCS templates avoid unexplained abbreviations and include a clear action link; notices sent to counterparties offer an accessible web view and a "Listen" option.

### U.7.4 Accessible KYC and eSign (LG-136)

- KYC options that do not depend on sight or on blink/liveness: Aadhaar offline verification (QR/XML via the Aadhaar App flow as built in P01 [VERIFY OVSE route]), DigiLocker documents, DSC, and an **assisted video KYC** with a trained human who can accommodate screen-reader users, Deaf users (ISL interpreter or chat) and users with motor impairments; extended time-outs; labelled OTP fields; no image-only CAPTCHA.
- Where a vendor flow requires liveness, LawDocs offers an alternative route of equal standing and records the accommodation without disadvantaging the user.
- eSign: ESP OTP flows must be screen-reader operable (§U.11); where an ESP flow fails accessibility, LawDocs routes the user to a second ESP or to assisted signing (DSC or wet-ink with appointment) without extra charge [REC].

## U.8 Testing protocol

### U.8.1 Automated (every pull request and nightly)

| Layer | Tool | Gate |
|---|---|---|
| Web components | jest-axe / Testing Library; eslint-plugin-jsx-a11y | Zero violations at error level |
| Web pages | axe-core with Playwright on every route template, in all themes and at 320 px width; Lighthouse accessibility | Zero serious/critical; Lighthouse ≥ 95 (advisory) |
| Mobile | RN accessibility lint; Maestro/Detox assertions that every touchable has a role and label; snapshot tests at max font scale | Zero missing labels; no truncation in snapshots |
| Content | CMS checker (alt text, heading order, link text, table headers, captions) | Blocks publish |
| Documents | PDF tag check (veraPDF-type PDF/UA checks where available [VERIFY tooling]); DOCX structure check | Advisory in Wave 1; blocking from Wave 2 for generated legal documents |
| Tokens | Contrast test over all token pairs and themes | Blocking |

Automated tests catch a minority of issues; they never replace §U.8.2–§U.8.3.

### U.8.2 Manual expert audit (each release, critical journeys; full audit each wave)

| Assistive technology / condition | Platforms |
|---|---|
| NVDA (current) | Windows + Firefox and Chrome |
| JAWS (current) | Windows + Chrome |
| VoiceOver | macOS + Safari; iOS (current and n-1) |
| TalkBack | Android (current and n-2), including a low-end device |
| Keyboard only | All web apps |
| Zoom 200% and 400% / reflow at 320 CSS px | Web |
| Forced colours / Windows high contrast | Web |
| Voice control | iOS Voice Control, Android Voice Access, Dragon (sample) |
| Switch access | iOS Switch Control, Android Switch Access (sample) |
| Largest text sizes | iOS Dynamic Type accessibility sizes; Android font scale maximum |
| Captions and media | Every new video |
| Indic locales | Screen-reader pronunciation and `lang` in Hindi plus one other enabled language per release |

Auditor: the squad's accessibility specialist (IAAP CPACC/WAS) plus `OPS_QA_REVIEWER`; an external audit by an independent accessibility firm before each wave go-live [REC], with the report stored as P23 audit evidence.

### U.8.3 Testing with disabled users

- **Panel:** at least 8 participants per round (`a11y.user_test.min_participants`), covering: blind screen-reader users (2), low-vision magnification users (1), Deaf ISL users (1), hard-of-hearing users (1), users with motor impairments using keyboard/switch/voice (1), users with cognitive or learning disabilities (1), older first-time smartphone users or low-literacy users (1). Include at least two languages other than English across the panel.
- **Recruitment:** through disability organisations and networks; participants are paid at fair rates; consent forms in accessible formats (ISL video explanation for Deaf participants); data minimised and handled under DPDP (consent artefacts; recordings only with explicit consent; retention 12 months).
- **Rounds:** before each wave go-live and after any major redesign of a critical journey; mobile and web.
- **Tasks:** the critical journeys (U.2) with realistic synthetic data; think-aloud where suitable; facilitator trained in disability etiquette; sessions remote or in person (Delhi, Noida, Jaipur offices) with accessible premises.
- **Outputs:** issues logged with severity (U.9), video highlights (consented), task success, time and satisfaction; findings reviewed with product owners within 5 working days; fixes verified with the same participant where possible.

## U.9 Severity, SLAs and release gate

| Severity | Definition | SLA | Release effect |
|---|---|---|---|
| S1 Blocker | A user of assistive technology cannot complete a critical journey, or a legal/financial action happens without an accessible confirmation | Fix before release; hotfix ≤ 5 working days if found in production | Blocks release of the affected surface |
| S2 Major | Journey completable only with significant difficulty or workaround; non-critical journey blocked | Next sprint | Release allowed with documented workaround and statement entry |
| S3 Moderate | Inconvenience; minor non-conformance | Within 2 sprints | — |
| S4 Minor | Cosmetic or best-practice improvement | Backlog | — |

**Release gate (P23, every release; Locked `a11y.release_gate.enabled`):** zero automated serious/critical violations; zero open S1 on critical journeys; manual scripts passed for changed journeys; captions present for new videos; conformance report updated; accessibility statement updated if limitations changed. Each wave go-live additionally needs the full manual audit and a disabled-user round.

**Accessibility feedback from the public** (P21 FR-P21-142): acknowledged ≤ 48 h (`hlp.a11y.feedback_ack_hours`), resolved or a dated plan ≤ 30 days (`hlp.a11y.feedback_resolve_days`), escalation to the Grievance Officer if unresolved; the reporter is told the outcome.

## U.10 Accessibility statement template (`/accessibility`, per brand)

> **Accessibility statement for {{brand.name}}**
>
> {{entity.legal_name}} wants everyone to be able to use {{brand.name}} — our website, web apps and mobile apps — including people who use screen readers, magnifiers, voice control, switch devices, captions or sign language.
>
> **Standards we follow.** We design and test to the Web Content Accessibility Guidelines (WCAG) 2.2 Level AA and to IS 17802 (Parts 1 and 2), as required for ICT under the Rights of Persons with Disabilities Rules 2017 [VERIFY current rule text]. We do not use accessibility overlays.
>
> **Conformance status.** {{surface}}: {{Fully / Partially}} conformant as of {{audit.date}}. Partially conformant means some parts do not yet meet the standard; they are listed below.
>
> **Known limitations.** {{list: item, impact, workaround, planned fix date}} (for example: "Some third-party eSign provider pages may not work fully with screen readers. Workaround: choose 'Assisted signing' and we will help you sign another way at no extra cost.")
>
> **Accessibility features.** Captions and transcripts on our videos; Indian Sign Language versions of core tutorials; easy-read summaries; "Listen" to documents and help; voice input; high-contrast, dark and large-text themes; reduced motion; the "i" button that explains legal terms in plain language in {{languages}}.
>
> **Getting help and giving feedback.** Use the accessibility feedback form at {{url}} (no CAPTCHA), email {{email}}, call {{phone}}, message us on WhatsApp at {{number}}, or ask for an Indian Sign Language video call. We will acknowledge you within 48 hours and resolve the issue or tell you our plan within 30 days.
>
> **If you are not satisfied.** Contact our Grievance Officer, {{grievance_officer.name}}, at {{grievance_officer.contact}}. You may also approach the authorities under the Rights of Persons with Disabilities Act 2016 [VERIFY appropriate authority wording with counsel].
>
> **How we test.** Automated checks on every release; manual testing with NVDA, JAWS, VoiceOver and TalkBack; keyboard and zoom testing; and testing with disabled users before each major release. Last independent audit: {{auditor}}, {{date}}.
>
> This statement was last reviewed on {{date}}.

## U.11 Vendors, embeds and procurement

- Every vendor surface a user touches (ESP/aggregator signing pages, Razorpay hosted checkout, DigiLocker, YouTube player, assisted-KYC video tool, webinar platform) is assessed before contracting: request an Accessibility Conformance Report (VPAT-style) against WCAG 2.2 AA, test the critical journey with NVDA and VoiceOver, and record results in the P23 vendor file.
- Contracts include an accessibility clause: conformance target, defect remediation timelines, and notice of changes [REC; COUNSEL to draft].
- Where a vendor surface fails, LawDocs provides an equivalent alternative route (§U.7.4) and lists the limitation in the statement.

## U.12 Settings, help keys and ownership

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `a11y.standard_set` | PLATFORM | list | WCAG22_AA, IS17802_P1_P2, GIGW3 | `PLT_SUPER_ADMIN` | Y (checker `OPS_QA_REVIEWER`) |
| `a11y.release_gate.enabled` | PLATFORM | bool | true (Locked) | — | — |
| `a11y.session_timeout_warning_seconds` | PLATFORM | int | 120 | `PLT_SECURITY_OFFICER` | Y |
| `a11y.user_test.min_participants` | PLATFORM | int | 8 | `OPS_QA_REVIEWER` | N |
| `a11y.easy_read.enabled` | PLATFORM, TENANT | bool | true | `PLT_SUPER_ADMIN`, `ORG_ADMIN` | N |
| `a11y.tts.enabled` | PLATFORM, TENANT | bool | true | `PLT_SUPER_ADMIN`, `ORG_ADMIN` | N |
| `a11y.shortcuts.single_key_enabled` | USER | bool | true | user | N |
| `hlp.user_prefs.*` (theme, text_scale, spacing, motion, font, underline_links, captions_default, easy_read, inline_terms) | USER | various | defaults per §U.7.1 | user | N |

Help keys: `hlp.gen.accessibility_preferences`, `hlp.gen.easy_read`, `hlp.gen.listen`, `hlp.gen.isl_video`, `hlp.gen.assisted_signing`, `hlp.gen.assisted_kyc`, `hlp.gen.accessibility_feedback`.

Acceptance tests tagged `@NN-28` live in each phase's feature files (e.g., P21-AT-19, P21-AT-25, P22-AT-21); `tests/nn/NN-28_accessibility.spec.ts` runs the automated suite across all route templates and the mobile label checks.

**Ownership:** standard and tooling — P21 accessibility specialist; component conformance — `packages/ui` owners; release gate — `PLT_RELEASE_MANAGER` with `OPS_QA_REVIEWER`; statement and feedback — `PLT_CONTENT_EDITOR` with `PLT_GRIEVANCE_OFFICER`; vendor assessments — P23.
