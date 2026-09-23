# 07 · Activity Booking — Guest App

| | |
|---|---|
| **Module** | Activity Session Picker → *Checkout (not designed)* → Activity Booking Confirmation (+ Sold-out slot state) |
| **Apps** | Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (390) |
| **Figma** | Page **New** → sections *Activity Session Picker* (8 frames: Default + Sold-Out Slot) and *Activity Booking Confirmation* (4 frames). Example: **Blue Hole Arch & Bells Deep Freediving Session**, booking **DHB-ACT-2025-9042** |
| **SRS** | §3.4 FR-4.1–4.4, §3.5 FR-5.1, 5.3, 5.5, FR-8.3, FR-15.3, NFR-6, NFR-12 |
| **Screens** | 2 screens designed + checkout missing · 12 frames |

> Content checked against the exported Desktop screenshots (the Figma text API limit was reached for this module).

---

## 1. Module summary

Books a guided activity (dive, trek, safari) for a number of participants on a specific date and time window, with optional gear rentals, then shows a confirmation with an offline check-in pass, meeting point and instructor contact. If the chosen slot fills up, the picker shows a sold-out state that keeps the guest's selections and proposes other windows or a waitlist.

**Flow:** Activity Detail (05) → **Session & Gear (Step 1)** → **Checkout (Step 2 — not designed)** → **Confirmed (Step 3)** → My Bookings (06).

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where |
|---|---|---|---|---|
| FR-4.1 | Select session (date/time), participants; live slot availability | H | ✅ | Session Picker |
| FR-4.2 | Complete activity booking with online payment | H | ✅ | **Checkout missing** · confirmation shows paid |
| FR-4.3 | Cancel/reschedule per activity policy | H | ✅ | Policy shown; cancel/reschedule screens **not designed for activities** (reuse module 06 pattern) |
| FR-4.4 | Reminders before the activity (24 h) | M | Later | — |
| FR-5.1 / 5.5 | Card payment; receipt | H / M | ✅ | Confirmation ledger, Download PDF |
| FR-15.3 | Provider notified of every new booking | H | ✅ | Backend |

## 3. Screen inventory

| # | Screen | States | Breakpoints |
|---|---|---|---|
| 4.1 | Activity Session Picker (Step 1 · Session & Gear) | Default · Sold-out slot | All 4 |
| 4.2 | Activity Checkout (Step 2) | — | **Not designed** |
| 4.3 | Activity Booking Confirmation (Step 3) | Default | All 4 |

---

## 4. Screen specifications

### 4.1 Activity Session Picker — Step 1 · Session & Gear

**Entry:** Reserve on Activity Detail (date/slot/divers carried over). **Exit:** Continue to Checkout; back to Activity Detail.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-15644.png"><img src="images/42-15644.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-14743.png"><img src="images/42-14743.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-14110.png"><img src="images/42-14110.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-13502.png"><img src="images/42-13502.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:15644](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-15644) | [Figma 42:14743](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-14743) | [Figma 42:14110](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-14110) | [Figma 42:13502](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-13502) |


#### UI elements

| Element | Content | Behaviour / rule |
|---|---|---|
| Progress | `1 Session & Gear` (active) → `2 Review & Checkout`; back link "Back to Blue Hole Arch & Bells Deep Freediving Session" | 2-step flow here, but the confirmation shows 3 steps (see §7 G9). |
| Activity summary | Thumbnail, badge "AIDA & Apnea Academy Certified", ★ 4.98 (184 divers), location, "Standard Rate EGP 2,400 / diver" | Price must equal the detail page (see §7 G1). |
| **Step 1 · Date selection** | Month calendar "October 2025 (Red Sea Autumn Season)" with an availability dot under each day (green = open, orange = few spots), selected **Sat, Oct 18, 2025**; badge "Optimal High Tide & Calm Sea Forecast" | Days without sessions or full days disabled. |
| Marine forecast | Water 26°C · Wind calm 4 kts · High tide 07:15 | Data source — see module 02 G3. |
| **Step 2 · Time slot** | "3.5 Hours Duration • Max 4 Divers per Instructor"; radio cards **Morning Glass 07:00–10:30** "MOST POPULAR • 2 SPOTS LEFT • Lead: Capt. Zaki" (selected) · **Midday Sunrays 11:30–15:00** "4 SPOTS AVAILABLE • Lead: Tarek Bedouin Diver" · **Late Afternoon Drift 15:30–19:00** "3 SPOTS AVAILABLE • Lead: Capt. Zaki" | Live remaining spots per window; a window is selectable only if spots ≥ participants. Lead guide per window. |
| **Step 3 · Capacity** | "Divers / Participants" stepper `[-] 2 [+]` | Max = min(remaining spots, per-booking max); min 1. |
| Certification notice | "Certified divers — min AIDA 2, Molchanovs Wave 1 or equivalent verified certification required for Arch passage" | Guest must confirm they meet it (checkbox — not designed) and/or upload C-Card. |
| **Step 4 · Technical equipment** ("Freediving Gear & Rental Add-ons (Optional)") | Carbon Freedive Bi-Fins (Leaderfins Pure Carbon) +EGP 350/person ✓ — sizing "Diver 1: EU 42–43, Diver 2: EU 39–40" · Sinai 3 mm Hydrodynamic Wetsuit +EGP 250/person ✓ — sizing "Diver 1: Men's L, Diver 2: Women's M" · Low-Volume Mirrored Apnea Mask & Snorkel +EGP 150/person · "Weight belts, safety lanyards, bottom plate & dive depth sonar tracking are included free of charge" | Quantity = participants; a size is required per diver for each selected item. |
| Reservation summary (sticky, "LIVE TOTAL") | Sat Oct 18 2025, 07:00–10:30 (Morning Glass), "Lead Guide & Safety Marshal: Captain Zaki Mansour"; Deep Session 2 × 2,400 = 4,800 · Carbon Bi-Fins 2 × 350 = 700 · 3 mm Wetsuits 2 × 250 = 500 · EEAA Marine Protected Permit 400 · Reef Conserv. & Bedouin Tribal Fee 240 · **Total Payable EGP 6,640** (≈ $138 USD) "Inclusive of all South Sinai taxes"; guide card "Captain Zaki Mansour — 15+ years" with message icon; "Instant confirmation — direct booking with captain" | Recalculates live. Activities are **instant-confirm** in this design. |
| Policy | "100% Free Cancellation until 48 hours prior to session. Full refund guaranteed under Dahab Sanctuary Accords." | From the activity's policy. |
| CTA | **Continue to Checkout (EGP 6,640) →** (mobile: fixed bottom dock) | Re-checks capacity, holds the spots, opens Step 2. |

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Arrives from Reserve | Pre-selects date, window and participants from the detail page. |
| 2 | Changes date | Loads windows and remaining spots for that date. |
| 3 | Picks a window | Validates spots ≥ participants. |
| 4 | Adjusts participants | Bounded by remaining spots; add-on quantities follow. |
| 5 | Toggles gear add-ons / sizes | Adds per-diver prices. |
| 6 | Taps **Continue to Checkout** | Server re-checks capacity and price, holds spots for N minutes, opens Step 2. |
| 6b | Slot filled meanwhile | Shows the **Sold-out slot** state (below). |

#### State: Sold-out slot

**State: Sold-Out Slot**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-16277.png"><img src="images/42-16277.png" width="230" alt="Sold-Out Slot – Desktop"></a> | <a href="images/42-15205.png"><img src="images/42-15205.png" width="230" alt="Sold-Out Slot – Tablet"></a> | <a href="images/42-14448.png"><img src="images/42-14448.png" width="150" alt="Sold-Out Slot – Mobile Web"></a> | <a href="images/42-13821.png"><img src="images/42-13821.png" width="150" alt="Sold-Out Slot – Native App"></a> |
| [Figma 42:16277](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-16277) | [Figma 42:15205](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-15205) | [Figma 42:14448](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-14448) | [Figma 42:13821](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-13821) |


| Element | Content | Behaviour / rule |
|---|---|---|
| Alert banner | "Selected Time Slot Just Filled Up — The Morning Glass (07:00–10:30) window for Saturday, Oct 18, 2025 was just booked by another diver (Safety Buoy & Guide Line Capacity Reached: 4/4 Divers)." + **View Recommended Midday Window (4 Open Lines)** + **Instant WhatsApp Buoy Waitlist**; progress step 1 marked "Action Required" | Shown when capacity check fails. |
| Sold-out window | Dimmed, lock icon, badge **SOLD OUT (0 SPOTS LEFT)**, radio disabled | — |
| Inline waitlist | **WhatsApp Release Alert** on the sold-out card; sidebar card "Morning Glass Waitlist" with WhatsApp mobile field (+20) and **Request WhatsApp Alert**, "Avg. cancellation turnaround: 4 hours" | Subscribes guest to release alerts for that slot. |
| Recommended alternative | Midday Sunrays badge **RECOMMENDED ALTERNATIVE • 4 SPOTS OPEN**, **pre-selected** | Keeps participants and gear. |
| Other alternative | Late Afternoon Drift "3 SPOTS LEFT" | — |
| Summary & CTA | "Midday Sunrays Selected"; Freedive Session 4,800 · Bi-Fins & Suits Rental 1,200 · Ras Abu Galum Marine Permit 640 · Bedouin Coastal Council Eco-Tax Free · **Total payable now EGP 6,640** · **Continue with Midday Sunrays →** · "Full refund up to 24h before water entry"; **Change Date**; live conditions (wind, water temp, tide slack, visibility); "Free Pre-Dive Equalization Check Included"; guide profile Captain Zaki Mansour | Total unchanged unless window price differs. |

---

### 4.2 Activity Checkout — Step 2 (**NOT DESIGNED**)
Same requirements as module 06 §4.2, plus per-participant details: name of each diver, certification level/number (and optional C-Card upload), age (16+), medical declaration / waiver, gear sizes.

---

### 4.3 Activity Booking Confirmation — Step 3

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-13027.png"><img src="images/42-13027.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-12626.png"><img src="images/42-12626.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-12306.png"><img src="images/42-12306.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-11991.png"><img src="images/42-11991.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:13027](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-13027) | [Figma 42:12626](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-12626) | [Figma 42:12306](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-12306) | [Figma 42:11991](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-11991) |


| Element | Content | Behaviour / rule |
|---|---|---|
| Progress | 1. Session & Gear ✓ → 2. Checkout ✓ → **3. Confirmed** | — |
| Header | "Expedition Confirmed & Certified" + "EEAA Eco-Gate Pass Active"; BOOKING REFERENCE **DHB-ACT-2025-9042** + copy; "Settled via Visa •••• 9012" | Activity refs use the prefix DHB-ACT. Email sent (FR-3.3 equivalent). |
| Session summary | Date Sat Oct 18 2025 · Dive window 07:00–10:30 · Duration 3.5 h; **Divers & Equipment Allocation** cards per diver: Diver 1 (Primary) AIDA 2 / VERIFIED — bi-fins 42–43, wetsuit M; Diver 2 Molchanovs W1 / VERIFIED — bi-fins 39–40, wetsuit S | Sizes differ from the picker (see §7). |
| Offline check-in pass | QR code for the Ras Abu Galum / Blue Hole ranger checkpoint (works without 4G), **Ranger PIN 5821**, **Add to Apple / Google Wallet**, **Download Voucher (PDF)**, **Print Pass** | Same pass rules as stays. |
| Meeting point (replaces check-in/out) | "EXPEDITION LOGISTICS — Blue Hole North Camels & Marine Outpost", map pin "North Marine Outpost (Buoy 3) 28.5722° N, 34.5369° E — ASSEMBLY ZONE", **Get Directions**; "Arrival Time: 06:30 AM" (30 min before for fitting, medical check, briefing); "Dahab 4×4 Shuttle Option" leaving Lighthouse at 06:00 | Meeting point + arrival offset are activity fields. |
| Diver briefing | Certification Verification · Signed Medical Declaration ("completed online") · Fasting Guidelines · Reef-Safe Sunscreen Only | Medical declaration implies a form in checkout (not designed). |
| Instructor contact | **Captain Youssef Ben-Ammar** — AIDA Master Instructor; **WhatsApp Youssef (+20 10 9341 8832)**; **Direct Emergency Call** | Revealed after booking. |
| Ledger | Deep freediving session, bi-fins & wetsuit rentals, EEAA protected-area pass, Dahab Hyperbaric Chamber emergency fund; total 6,640 | Must equal Step 1. |
| Next actions | **View in My Bookings** · **Back to Explore Dahab** | — |

**Step-by-step:** payment success → system confirms booking, decrements slot capacity atomically, generates reference/QR/PIN/PDF, emails guest, notifies provider (FR-15.3) → confirmation shown → guest adds to wallet / gets directions / opens My Bookings.

---

## 5. Cross-screen business rules

1. **Capacity:** each time window has a fixed capacity (design: 4 divers per buoy line, 1 instructor : 2 divers); remaining = capacity − confirmed − held.
2. **Participants** 1 … min(remaining, max per booking); each participant must meet prerequisites (certification, age 16+, medical).
3. **Price** = participants × per-person rate + add-ons × participants + permits/levies. Must match detail page.
4. **Hold & double-booking:** spots held at Continue; confirmed atomically on payment (same as FR-3.6); if lost → sold-out state.
5. **Waitlist:** subscribing stores (guest, activity, date, window, channel); when a spot frees, first-in-queue is notified (WhatsApp/push) — booking still first-come-first-served (define).
6. **Cancellation/reschedule:** per the activity's policy (48 h refund window in design) **plus weather guarantee** (wind > 18 kn or swell > 0.8 m → free reschedule — module 05). Provider triggers weather cancellation (Provider module).
7. **Reminders 24 h before** are Later (FR-4.4) but the meeting-point data should be ready for them.

## 6. Story candidates for Jira

**Epic:** GUEST-BOOK-ACTIVITY — Activity booking

| Key idea | Story | Acceptance criteria |
|---|---|---|
| ACT-1 | As a guest, I want to pick a date and time window with live remaining spots. | Disabled full windows; remaining counts; forecast shown. |
| ACT-2 | As a guest, I want to set the number of participants. | Bounded by remaining spots and max per booking; prices update. |
| ACT-3 | As a guest, I want to add rental gear per diver with sizes. | Add-ons priced per diver; sizes required when selected. |
| ACT-4 | As a guest, I want to see the total and cancellation policy before paying. | Breakdown lines + total; policy text from activity. |
| ACT-5 | As a guest, I want to be told if my slot filled up and be offered alternatives. | Sold-out banner; slot locked; recommended alternative pre-selected; selections kept. |
| ACT-6 | As a guest, I want to join a waitlist for a sold-out slot. | WhatsApp/push alert subscription; confirmation; unsubscribe. |
| ACT-7 | As a guest, I want to enter participant details and pay. | *Needs design* — per-diver details, certification, waiver, card payment. |
| ACT-8 | As a guest, I want a confirmation with pass, meeting point and instructor contact. | Ref DHB-ACT-…; QR + PIN offline; wallet; directions; PDF; email sent. |
| ACT-9 | As a guest, I want to cancel or reschedule an activity per its policy. | Reuse module 06 cancel/modify pattern for activities; weather-guarantee reschedule free. |

## 7. Gaps, inconsistencies & open questions

| # | Finding | Suggested decision |
|---|---|---|
| G1 | **Per-person price differs:** EGP 1,650 (search, detail) vs EGP 2,400 (session picker, notifications). | One price. |
| G2 | **Time windows differ:** detail page 07:30–11:00 / 11:30–15:00 / 15:30–18:30 vs picker 07:00–10:30 / 11:30–15:00 / 15:30–19:00. | Session times come from provider schedule; fix Figma copy. |
| G3 | Add-on prices differ: detail bi-fins +250, wetsuit +200, goggles +100 vs picker bi-fins +350, wetsuit +250, mask +150. | One price list. |
| G4 | **Checkout step for activities not designed.** | Design (can share module 06 Step 2 layout). |
| G5 | Activity cancel / reschedule screens not designed (FR-4.3). | Reuse Cancel & Modify patterns from module 06. |
| G6 | Prerequisite confirmation (checkbox / upload) not part of the picker. | Add to picker or checkout. |
| G7 | Remaining spots shown on detail vs picker differ for the same slot (2/3/4 vs 2/4/3). | Live data — note only. |
| G8 | Rating/review count differs (86 vs 184 divers). | Live data — note only. |
| G9 | **Step naming differs:** picker shows 2 steps ("Session & Gear → Review & Checkout"; sold-out state: "Bedouin Briefing & Payment — Permits, Medical Waiver & Confirmation"), confirmation shows 3 ("Session & Gear → Checkout → Confirmed"). | One stepper for the flow. |
| G10 | **Lead guide differs:** picker/sold-out name **Captain Zaki Mansour** (and "Tarek"), confirmation and detail page name **Youssef Ben-Ammar**. | Guide assigned per session from the provider's staff; fix Figma copy. |
| G11 | Cancellation window differs inside this module: 48 h (picker) vs 24 h (sold-out state). | Use the activity's policy only. |
| G12 | Ratio differs: "Max 4 Divers per Instructor" (picker) vs "1:2 safety pairing" (detail, notifications). | Define capacity model (per instructor vs per buoy line). |
| G13 | Gear sizes chosen in the picker (wetsuit L / M) differ from the confirmation (M / S). | Copy fix. |
| G14 | Activities are "Instant confirmation" here, while stays say "Direct host confirmation". | Confirm the confirmation mode per listing type. |

## 8. Out of scope for MVP
- Reminders (FR-4.4), cash on arrival (FR-5.2), coupons (FR-5.4), AI trip planner conversion (FR-9.3).
