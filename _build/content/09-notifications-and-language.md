# 09 · Notifications & Language Settings — Guest App

| | |
|---|---|
| **Module** | Notification Center (EN + Arabic RTL) · Language Switcher (Settings) |
| **Apps** | Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (390) |
| **Figma** | Page **New** → sections *Notification Center* (8 frames: EN + Arabic RTL) and *Language Switcher* (4 frames) |
| **SRS** | FR-8.3, FR-4.4 (Later), FR-20.1, FR-20.2, FR-20.3 (Later), NFR-7, §5.3 Email/SMS/WhatsApp, Push (FCM/APNs) |
| **Screens** | 2 screens · 12 frames |

> Content checked against the exported Desktop screenshots (the Figma text API limit was reached for this module).

---

## 1. Module summary

- **Notification Center:** an in-app inbox of everything that happened to the guest's trips — booking confirmations, host messages, waitlist releases, safety/weather advisories, wishlist updates and review prompts — with filters, unread markers, "mark all as read" and channel settings (WhatsApp, SMS, weekly digest). Also delivered as push/email/SMS/WhatsApp.
- **Language Switcher:** settings page to switch the whole app between **English (LTR)** and **العربية (RTL)**, with currency display preference and formatting preview. The Arabic Notification Center is the reference proof that RTL works on a content-heavy screen.

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where |
|---|---|---|---|---|
| FR-8.3 | Push/email/SMS notifications for confirmations, cancellations, reminders | H | ✅ | Notification Center + channel settings |
| FR-4.4 | Reminders before activities | M | Later | "Weather advisory" / reminders appear in the design |
| FR-20.1 | UI in English and Arabic at launch | H | ✅ | Language Switcher + RTL Notification Center |
| FR-20.2 | Switch language any time from settings | H | ✅ | Language Switcher |
| FR-20.3 | Preferred currency alongside EGP/USD | M | **Later** | Currency selector is designed — §7 G2 |
| NFR-7 | All user-facing text externalised for translation | — | ✅ | All screens |

## 3. Screen inventory

| # | Screen | States | Breakpoints |
|---|---|---|---|
| 4.1 | Notification Center | English (LTR) · Arabic (RTL) | All 4 |
| 4.2 | Language Switcher — Settings | Default | All 4 |

---

## 4. Screen specifications

### 4.1 Notification Center

**Entry:** bell icon with unread badge (web header), "Updates" tab (native bottom bar), push notification tap. **Exit:** the item's target screen.

**State: Arabic RTL**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-23093.png"><img src="images/42-23093.png" width="230" alt="Arabic RTL – Desktop"></a> | <a href="images/42-22222.png"><img src="images/42-22222.png" width="230" alt="Arabic RTL – Tablet"></a> | <a href="images/42-21721.png"><img src="images/42-21721.png" width="150" alt="Arabic RTL – Mobile Web"></a> | <a href="images/42-21192.png"><img src="images/42-21192.png" width="150" alt="Arabic RTL – Native App"></a> |
| [Figma 42:23093](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-23093) | [Figma 42:22222](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-22222) | [Figma 42:21721](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-21721) | [Figma 42:21192](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-21192) |

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-23618.png"><img src="images/42-23618.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-22668.png"><img src="images/42-22668.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-21996.png"><img src="images/42-21996.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-21460.png"><img src="images/42-21460.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:23618](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-23618) | [Figma 42:22668](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-22668) | [Figma 42:21996](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-21996) | [Figma 42:21460](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-21460) |


#### UI elements

| Element | Content | Behaviour / rule |
|---|---|---|
| Header | Bell icon with red dot (web), "Updates" tab (native); breadcrumb Marketplace › Personal Account › Notifications; title "Notification Center" + badge **3 New**; "Syncing Realtime • Dahab (GMT+3) 17:56" | Unread count. |
| Filter chips (with counts) | **All Notifications (6 total, 3 unread) · Bookings & Stays (2) · Host Messages (2) · Expeditions & Diving (1) · Safety & Weather (1)** | Filter by type. |
| Mark all as read · settings icon | Links top-right | Clears unread state / opens settings. |
| Unread styling | Terracotta dot + left accent border (right border in RTL) | Read items plain. |
| Notification cards (Figma) | ① **Confirmed Stay** (12 minutes ago) — "Booking Confirmed: Dar Tarabin Coastal Ecolodge… Booking Reference #DHB-2025-8841-ARB" + booking thumbnail → **View Reservation** · **Message Sheikh Salama** ② **Direct Host Message** (45 min ago) — Sheikh Salama Tarabin, quoted message → **Reply to Host** · **Call via WhatsApp** ③ **Waitlist Released** — "Morning Glass Slot Released: Blue Hole Arch & Bells Deep Freediving… with Master Guide Youssef Ben-Ammar. 2 divers max on line buoy.", specs (Max depth line to 60 m · Water 26°C · Safety ratio 1:2 dedicated · Special rate EGP 2,400), timer **Expires in 58 mins** → **Claim Slot (EGP 2,400)** · **Pass Slot** ④ **Conditions Advisory** (yesterday) — "Red Sea Marine Conditions: Lighthouse & Blue Hole", clarity rating 35 m → **View Live Dahab Wind & Tides** ⑤ **Price & Availability** — wishlist item update ⑥ review prompt | Each card: type chip, title, body, time, CTAs deep-linking to the target (My Bookings, WhatsApp, Session Picker with slot pre-selected, conditions page, listing, Leave a Review). |
| Delivery Channels (sidebar, "3 Active") | Toggles **WhatsApp Alerts · SMS Urgent Notices · Weekly Digest** · **Manage Notification Settings** | Stored per user; transactional emails always sent. Settings page not designed. |
| Side cards | "Sinai Marine Safety Net" (chamber line +20 (0)69 364 0530, VHF Ch 16, **Direct Chamber Dispatch Link**) · "Host Concierge Desk" → **Chat with Dahab Desk** | Shared config / support channel. |

#### Arabic (RTL) state — what must mirror
Navigation shell flows right-to-left; in the bottom bar **استكشف (Explore)** is right-most and **حسابي (Profile)** left-most; unread dots/borders on the right; avatars/thumbnails on the right; primary CTA on the right (e.g. **عرض الحجز**, **حجز المقعد الآن**); Arabic numerals in badges (٣) and prices (٢,٤٠٠ ج.م); translated notification bodies.

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Receives an event (booking, message, waitlist…) | Creates notification record; sends push/email/SMS/WhatsApp per type and settings (FR-8.3). |
| 2 | Opens Notification Center | Lists newest first; unread styled; badge count. |
| 3 | Filters by type | Shows matching items. |
| 4 | Taps an item / its CTA | Marks it read; deep-links to target. |
| 5 | Taps **Claim Slot** on a waitlist item | Opens Session Picker with slot pre-selected; if already taken → sold-out state (07). Countdown shows claim window. |
| 6 | Taps **Mark all as read** | All read; badge cleared. |
| 7 | Toggles a channel | Saves preference immediately. |

---

### 4.2 Language Switcher — Settings

**Entry:** Profile/Settings; also reachable from header EN | عربي toggle (quick switch). **Exit:** back to Settings.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-25095.png"><img src="images/42-25095.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-24701.png"><img src="images/42-24701.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-24423.png"><img src="images/42-24423.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-24099.png"><img src="images/42-24099.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:25095](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-25095) | [Figma 42:24701](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-24701) | [Figma 42:24423](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-24423) | [Figma 42:24099](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-24099) |


| Element | Content | Behaviour / rule |
|---|---|---|
| Page | Breadcrumb Settings › Preferences › Language & Region; title "Language & Regional Settings"; "Active Locale: English (US) • EGP (EGP)" | — |
| Primary Language | **English** (United Kingdom / International) — DEFAULT · **العربية** (Arabic Egypt) "Auto Right-to-Left (RTL)" · **Français** · **Deutsch** · **Русский** | Selecting applies strings, direction and fonts (Plus Jakarta Sans + Arabic fallback). **Only EN and AR are MVP** (§7 G8). |
| Layout & Reading Orientation | Cards **Left-to-Right (LTR)** (selected) · **Auto-Match RTL** ("mirrors entire viewport… when Arabic is active") | Should follow language automatically (§7 G9). |
| Display Currency | **EGP (£E)** Local Native · **USD ($)** · **EUR (€)** · **GBP (£)**; note "Sinai Fair Exchange Assurance — all checkout transactions settle in EGP…" | FR-20.3 is Later — see §7 G2. Settlement always EGP. |
| Calendar & Week Cycle | Calendar system **Gregorian** / **Hijri • Lunar**; first day of week **Saturday** (Egypt standard) / Sunday / Monday | Not in SRS (§7 G10). |
| Live Experience Preview | Sample listing card (Dar Tarabin, dates, host welcome, "EGP 2,400 / night", "Free cancellation up to 48h") + summary (Layout orientation, Currency identifier, Calendar engine) | Re-renders as options change. |
| Actions | **Save Preferences** · **Reset**; info "Language changes will automatically apply across all search filters, booking itineraries, and host messages." | Saved to the account (and device for logged-out users). |

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Opens Language settings | Shows current language selected. |
| 2 | Picks Arabic and taps **Save Preferences** | Re-renders the app in Arabic RTL without losing navigation state; saves to profile (same field as Edit Profile "Preferred language"). |
| 3 | (If in scope) picks currency | Updates price display site-wide with conversion note. |
| 4 | Returns | Preference applied everywhere, incl. emails/SMS/notifications language. |

---

## 5. Cross-screen business rules

1. **Notification catalogue (MVP):** booking confirmed, booking modified, booking cancelled + refund issued, payment failed, host message (if messaging in scope), waitlist slot released, safety/weather advisory, review prompt after completion. Each type defines channels (push, email, SMS, WhatsApp) and template in EN + AR.
2. Transactional messages (confirmation, cancellation, refund) are always sent by email; opt-out applies only to marketing/digest.
3. Notification language = user's preferred language.
4. Language preference is one field shared by Edit Profile (01), header toggle and this screen.
5. RTL rules: logical CSS properties, mirrored icons/chevrons, numbers/phone numbers kept LTR inside RTL text.
6. Retention of notifications in the inbox (e.g. 90 days) — define.

## 6. Story candidates for Jira

**Epic:** GUEST-NOTIFY-L10N — Notifications & Localization

| Key idea | Story | Acceptance criteria |
|---|---|---|
| NOTIF-1 | As a guest, I want an in-app notification center. | List, unread badge, filters, mark all as read, deep links. |
| NOTIF-2 | As a guest, I want booking confirmations/cancellations by push, email and SMS. | Sent on each event in the user's language (FR-8.3). |
| NOTIF-3 | As a guest, I want to be alerted when a waitlisted slot opens and claim it. | Alert via chosen channel; Claim opens picker with slot; handles already-taken. |
| NOTIF-4 | As a guest, I want to choose my alert channels. | WhatsApp, SMS, digest toggles saved; transactional email always on. |
| NOTIF-5 | As a guest, I want safety/weather advisories for my upcoming trips. | Advisory items linked to booking/zone (data source TBD). |
| L10N-1 | As a guest, I want to switch the whole app to Arabic or English at any time. | Immediate re-render; RTL mirrored; preference saved to profile and device. |
| L10N-2 | As an Arabic guest, I want notifications and emails in Arabic. | Templates in AR; numerals and dates localised. |
| L10N-3 (tech) | All strings externalised; RTL layout support. | No hard-coded strings (NFR-7); logical CSS; RTL QA checklist passes on the 12 RTL specimen screens. |

## 7. Gaps, inconsistencies & open questions

| # | Finding | Suggested decision |
|---|---|---|
| G1 | Native tab bar here has **5 tabs (Explore · Saved · Bookings · Updates · Profile)**, other modules have 4 (no Updates). The native Notification screen is also branded "DAHAB LIFE". | Decide final tab set and brand; apply to all native/mobile frames. |
| G2 | **Currency selector (EGP/USD/EUR)** is designed, but FR-20.3 is Later; also shown as "EGP" in the web header. | Hide for MVP or move FR-20.3 into MVP. |
| G3 | **Host message notifications with Reply** depend on in-app messaging (FR-8.1/8.2, Phase 2). | MVP: WhatsApp deep link only. |
| G4 | Waitlist "Claim Slot (EGP 2,400)" price ≠ activity detail price (EGP 1,650). | See module 07 G1. |
| G5 | Weather/marine advisories need a data source and a trigger rule. | See module 02 G3. |
| G6 | Only the Notification Center has full Arabic designs; other modules have none (except auth tablet errors). | Plan an RTL QA pass for all modules. |
| G7 | Notification preferences for email/push per type are not designed (only WhatsApp/SMS/digest); "Manage Notification Settings" page not designed. | Extend settings or keep minimal. |
| G8 | **Language list shows 5 languages** (EN, AR, FR, DE, RU); SRS MVP = EN + AR (others later, architecture-ready). | Show EN/AR only for MVP. |
| G9 | Separate "Layout & Reading Orientation" setting lets a user pick LTR while in Arabic. | Tie direction to language; remove the setting. |
| G10 | Calendar system (Hijri) and first-day-of-week settings are not in the SRS. | Phase 2 or remove. |
| G11 | Broken glyphs in the header currency pill (")▯.▯EGP(") and next to "Arabic Egypt" on the language card. | Font/icon fix in Figma. |
| G12 | Waitlist card says "line to 60m"; the activity is 30–45 m elsewhere. | Copy fix. |

## 8. Out of scope for MVP
- Reminders 24 h before activities (FR-4.4), preferred currency (FR-20.3), additional languages (German, Russian, Italian — architecture must allow them).
