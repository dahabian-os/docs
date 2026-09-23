# 06 · Accommodation Booking & My Bookings — Guest App

| | |
|---|---|
| **Module** | Room Type & Date Selector → *Guest details & payment (not designed)* → Booking Confirmation → My Bookings → Cancel booking → Modify dates |
| **Apps** | Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (390) |
| **Figma** | Page **New** → sections *Room Type & Date Selector*, *Booking Confirmation*, *My Bookings*, *Cancel Booking Confirmation*, *Modify Dates* (20 frames). Example: Dar Tarabin Coastal Ecolodge, booking **DHB-2025-8841-ARB** |
| **SRS** | §3.3 FR-3.1–3.6, §3.5 FR-5.1, 5.3, 5.5, FR-8.3, FR-13.4, NFR-5, NFR-6, NFR-8, NFR-10, NFR-12 |
| **Screens** | 5 screens designed + 1 missing (checkout) · 20 frames |

---

## 1. Module summary

Takes a guest from "Reserve" on a property page to a confirmed, paid stay, and lets them manage it afterwards.

**Step 1 – Select room & dates** → **Step 2 – Guest details & accords + payment** *(no screen in the new Figma — see §7 G1)* → **Step 3 – Confirmation** (voucher, offline QR check-in pass, host contact, arrival logistics) → **My Bookings** (upcoming / past / cancelled; view voucher; modify; cancel) → **Cancel** (refund per policy) / **Modify dates** (with sold-out conflict handling).

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where |
|---|---|---|---|---|
| FR-3.1 | Select room type, dates, guests; live price & availability before booking | H | ✅ | Room Type & Date Selector |
| FR-3.2 | Complete booking with online payment | H | ✅ | **Checkout step 2 — missing** |
| FR-3.3 | View booking confirmation; receive it by email/notification | H | ✅ | Booking Confirmation ("Voucher dispatched to …") |
| FR-3.4 | View, modify (where policy allows), or cancel an upcoming booking | H | ✅ | My Bookings, Modify Dates, Cancel |
| FR-3.5 | Enforce cancellation policy; calculate refunds | H | ✅ | Cancel dialog (refund eligibility & amount) |
| FR-3.6 | Prevent double booking (atomic availability decrement) | H | ✅ | Backend; "Units left" badges; sold-out conflict on Modify |
| FR-5.1 | Pay by card via integrated gateway | H | ✅ | Missing checkout; confirmation shows "Paid in full (Visa •••• 9012)" |
| FR-5.3 | Automatic refund to original payment method | H | ✅ | Cancel dialog ("returned to Visa / Apple Pay •••• 9012 within 3–5 business days") |
| FR-5.5 | Receipt/invoice for each completed payment | M | ✅ | "Download PDF", "Print Voucher" |
| FR-8.3 | Push/email/SMS for confirmations, cancellations | H | ✅ | Confirmation email + notifications (module 09) |
| NFR-6 | First-time guest books in ≤ 5 screens/steps | — | ✅ | 3-step progress bar |
| NFR-12 | Full audit trail of booking/payment transactions | — | ✅ | Backend |

## 3. Screen inventory

| # | Screen | States | Breakpoints |
|---|---|---|---|
| 4.1 | Room Type & Date Selector (Step 1) | Default | All 4 |
| 4.2 | Guest Details & Payment (Step 2) | — | **Not designed** |
| 4.3 | Booking Confirmation (Step 3) | Default | All 4 |
| 4.4 | My Bookings | Default (upcoming booking selected) | All 4 |
| 4.5 | Cancel Booking Confirmation | Dialog / bottom sheet | All 4 |
| 4.6 | Modify Dates | Sold-out collision error | All 4 |

---

## 4. Screen specifications

### 4.1 Room Type & Date Selector — Step 1 of 3

**Entry:** Reserve on Property Detail (values carried over). **Exit:** Continue → Step 2; back → Property Detail.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-5279.png"><img src="images/42-5279.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-4719.png"><img src="images/42-4719.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-4364.png"><img src="images/42-4364.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-3947.png"><img src="images/42-3947.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:5279](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-5279) | [Figma 42:4719](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-4719) | [Figma 42:4364](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-4364) | [Figma 42:3947](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-3947) |


#### UI elements

| Element | Content (Figma) | Behaviour / rule |
|---|---|---|
| Progress | Step 1 Select Room & Dates · Step 2 Guest Details & Accords · Step 3 Confirmation (native "STEP 1 OF 3") | Shows position; previous steps clickable. |
| Property summary | Name, "100% OFF-GRID SOLAR & REEF CERTIFIED", rating 4.99 (67), "SANCTUARY CAPACITY — Low Impact (3/5 Units Left)" | Units left = live inventory. |
| **1. Dates** | Two-month calendar (Oct/Nov 2025); legend Selected · Stay span · Past / Full; preset chips **Weekend Escape (2N) · Lunar Stargazing (4N) · Deep Reef Dive (7N)** (native: 3 Nights · 4 Nights · 7 Nights (10% off) · Custom); CHECK-IN "Thu, Oct 16, 2025 — After 2:00 PM", CHECK-OUT "Mon, Oct 20, 2025 — Before 11:00 AM"; note "New Moon Night: Oct 18 (Best Milky Way view)" | Past and fully booked dates disabled. Preset = check-in + N nights. Min/max stay per property (to define). |
| **2. Guest allocation** | Steppers: Adults (13+) · Children (2–12) · Extra Cot / Majlis (+EGP 300/night) ; "Off-grid sanctuary preserves strict max capacity per hut" | Total guests ≤ selected tier capacity; extra cot adds a nightly fee. |
| **3. Room tier** | 3 tier cards (see module 05) with "MOST POPULAR", "2 Units Left" / "ONLY 1 LEFT", specs, inclusions, **TIER SELECTED / Select Suite / Select Hut**; tablet shows price difference ("+EGP 3,200 total difference") and **Switch Room** | One tier per booking (multi-room not designed). |
| Arrival note | "Arrival via Camel or Coastal Footpath — accessible only by a 1.5-hour coastal walk from the Blue Hole or Bedouin camel transfer" | Property-specific access info. |
| **Reservation summary** (sticky) | Tier, dates, "4 Nights · 2 Adults"; lines: EGP 2,400 × 4 = 9,600 · Eco-Conservation Reef Fund (5%) 480 · Solar Microgrid & Desal Water 350 · Bedouin Hearth Breakfast "EGP 0 (Included)" · Subtotal 10,430 · Sinai Eco Tourism Tax (10%) 1,043 · **Total Payable EGP 11,473** · "Approx. $240 USD" · "Free cancellation up to 5 days before check-in — 100% refund until 2:00 PM on Oct 11, 2025" | Recalculates on every change. Refund deadline = check-in − policy days. |
| Primary CTA | **Continue to Guest Details & Accords** (tablet: "Continue to Guest Details (EGP 11,473)"; native: "Continue") | Re-validates availability, places a short **hold** on the unit (see rules), goes to Step 2. |
| Host contact | "Questions for Sheikh Salama? Message on WhatsApp" | See module 05 G1. |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Arrives from Reserve | Pre-fills tier, dates, guests from the property page. |
| 2 | Picks check-in, then check-out (or a preset) | Highlights span; disables unavailable dates; recalculates nights and total. |
| 3 | Adjusts adults / children / extra cot | Enforces tier capacity (disables "+" at max, message); adds cot fee. |
| 4 | Switches tier | Re-checks availability for the dates; shows difference; updates total. |
| 5 | Taps **Continue** | Server re-prices and re-checks availability; creates a pending reservation with a hold (e.g. 15 min); opens Step 2. |
| 5b | Unit no longer available | Shows error and suggests other tiers/dates (reuse Modify-dates conflict pattern 4.6). |

---

### 4.2 Guest Details & Payment — Step 2 of 3 (**NOT DESIGNED**)

The new Figma has no screen for Step 2 although both progress bars reference it ("Guest Details & Accords"). An older version exists in the first Stitch project (*Coral Coast Camp – Checkout & Payment* / *Confirm & Pay*). Minimum content required by the SRS:

| Block | Required content | SRS |
|---|---|---|
| Lead guest details | Full name, email, phone (+20 default), nationality; pre-filled from profile | FR-1.3 |
| Special requests / arrival transfer choice | Camel caravan vs boat shuttle (shown later on confirmation) | — |
| Accords | Accept house rules, cancellation policy, Environmental Charter (checkbox) | FR-13.4 |
| Price summary | Same breakdown as Step 1 | FR-3.1 |
| Payment | Card via PCI-DSS gateway (Paymob/Fawry/Stripe), tokenised; 3-D Secure; **Pay EGP 11,473** | FR-5.1, NFR-3, NFR-8 |
| Coupon code | *Later* (FR-5.4) | — |
| Cash on arrival | *Later* (FR-5.2) | — |
| Errors | Card declined, 3DS failed, timeout, hold expired | — |

---

### 4.3 Booking Confirmation — Step 3 of 3

**Entry:** successful payment. **Exit:** My Bookings, Discovery, Browse Expeditions.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-7053.png"><img src="images/42-7053.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-6658.png"><img src="images/42-6658.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-6368.png"><img src="images/42-6368.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-6147.png"><img src="images/42-6147.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:7053](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-7053) | [Figma 42:6658](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-6658) | [Figma 42:6368](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-6368) | [Figma 42:6147](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-6147) |


#### UI elements

| Element | Content (Figma) | Behaviour / rule |
|---|---|---|
| Progress | Step 1 ✓ · Step 2 ✓ · **Step 3: Confirmed** | — |
| Success message | "Mabrouk! Your Sanctuary is Secured" / "Reservation Confirmed!" / "Booking Confirmed • مبروك!" | Bilingual celebration line. |
| Booking reference | **DHB-2025-8841-ARB** + **Copy Pass / Copy / Copy Ref**; "Voucher dispatched to guest@redseadive.com" | Unique reference format DHB-YYYY-NNNN-XXX; confirmation email sent (FR-3.3). |
| Stay voucher | Property, tier (Stargazing Palm Arish, Tier 01), CHECK-IN Thu Oct 16 from 2:00 PM, CHECK-OUT Mon Oct 20 until 11:30 AM, 2 Adults, 4 nights, board (Bedouin breakfast), meeting point "Blue Hole Camel Staging Hub" | From the booking record. |
| **Offline check-in pass** | QR code + **PIN 4192**, "Present this digital token to the Ras Abu Galum Protectorate Gate rangers…", "Valid without mobile reception", "Sinai Park Entry Taxes Pre-cleared"; native **Add to Wallet**, **Trailhead Map** | QR encodes booking ref + signature; must work offline; Apple/Google Wallet pass. |
| Host card | Sheikh Salama Tarabin, rating, message; **Chat on WhatsApp (+20 10 2481 9920)** · **Direct Call** · **In-App Chat** | Host contact revealed after booking. In-app chat is FR-8.1 (Later). |
| Arrival protocol | "NO PAVED ROADS" — Option A Bedouin camel caravan (1.5 h), Option B coastal boat shuttle (20 min, weather-dependent, 250 EGP paid to captain); "Open Blue Hole Staging on GPS" / "Get Directions" | Property-specific arrival instructions (provider content). |
| Payment summary | "Paid in Full (Visa •••• 9012)": 4 nights 9,600 · Reef restoration 480 · Solar desal 350 · EEAA levies 1,043 · **Total Settled EGP 11,473** | Must match Step 1 total. |
| Utilities | **Print Voucher** · **Download PDF** · **Add to Calendar** (mobile: Add to Cal · Directions · Save PDF) | PDF = voucher + receipt (FR-5.5); .ics calendar event. |
| Emergency channels | Deco Chamber +20 69 3640 530 · Ranger coastal rescue 1909 / VHF 16 | Shared config. |
| Charter accord | Zero single-use plastics · mineral sunscreen · silent hours after 22:30 | — |
| Cross-sell | "Enhance Your Stay with Marine & Desert Safaris" · **Browse Expeditions** · **Return to Discovery** | Opens activity search (03). |

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Payment succeeds (gateway webhook) | Confirms booking, decrements availability atomically (FR-3.6), generates reference, QR/PIN, voucher PDF, receipt; sends email + push (FR-3.3, FR-8.3); notifies provider (FR-15.3). |
| 2 | Sees confirmation | Shows voucher, pass, host contact, arrival options. |
| 3 | Copies reference / adds to wallet / calendar / downloads PDF | Performs action with feedback toast. |
| 4 | Taps **Go to My Bookings** / Bookings tab | Opens My Bookings with this booking selected. |

---

### 4.4 My Bookings

**Entry:** "My Bookings" in the web header, Bookings tab (native/mobile), confirmation screen, notifications. **Exit:** booking actions (voucher, modify, calendar, cancel), host contact, Book Again.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-8654.png"><img src="images/42-8654.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-8124.png"><img src="images/42-8124.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-7829.png"><img src="images/42-7829.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-7539.png"><img src="images/42-7539.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:8654](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-8654) | [Figma 42:8124](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-8124) | [Figma 42:7829](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-7829) | [Figma 42:7539](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-7539) |


#### UI elements (checked against the exported Desktop screen)

| Element | Content (Figma) | Behaviour / rule |
|---|---|---|
| Header | "My Bookings" active in the top nav (native: Bookings tab) | — |
| Title & tabs | "My Sanctuary Bookings" · segmented **Upcoming (1) · Past Stays (2) · Cancelled (0)** · search "Search ref, lodge, guide…" | Counts per status; search by reference, property or guide name. |
| Upcoming card (left list) | "Confirmed & Secured", #DHB-2025-8841, zone, Dar Tarabin Coastal Ecolodge, "Stargazing Palm Arish • 2 Guests", Thu Oct 16 – Mon Oct 20 2025, 4 Nights, countdown "In 14 Days • New Moon Tide", **EGP 11,473 Paid in Full** | Selecting a card opens its detail on the right (desktop/tablet) or a new screen (mobile/native). |
| Past journeys | "2 Completed": Canyon Dune Camp (White Canyon Stargazer Expedition, Sep 4–7 2025, 3 nights, EGP 6,800, **Receipt & Tax Leaf**, **Book Again**); Bells & Arch Guided Freediving (Aug 18 2025, EGP 2,400, **Dive Log Certificate**, **Book Again**) | Stays and activities in one list. Receipt = FR-5.5. Book Again → the listing with new dates. |
| Impact card | "Your completed 2025 stays have contributed 350 sqm of coral reef surveillance…" | Informational; needs a data source or static copy. |
| Detail header | BOOKING REFERENCE **DHB-2025-8841-ARB** + COPY REF, status "Confirmed • 100% Off-Grid Solar Sanctuary"; actions **Download PDF Voucher** · **Modify Dates** · **Add to Calendar** · **Cancel Stay** | Actions shown only when allowed by status/policy. |
| Stay block | Photo, rating 4.96 (64 reviews), CHECK-IN Thu Oct 16 from 2:00 PM (habak tea welcome at Blue Hole), CHECK-OUT Mon Oct 20 until 11:30 AM (camel footpath escort), room "Stargazing Palm Arish • 34 m²", "2 Adults (Private Sanctuary)", inclusions (breakfast, solar, spring water) | Same data as confirmation. |
| Offline check-in pass | QR + **PIN 4192**, "Valid at Ras Abu Galum Checkpoint — No cellular coverage needed", "EEAA Sinai Marine Reserve Permit pre-cleared", "Port Police coastal clearance logged"; native: **Add to Apple / Google Wallet** | Cached for offline use. |
| Settled financials | Receipt #4810-RC: 4 nights 9,600 · Eco-Conservation Reef Fund (5%) 480 · Solar microgrid 350 · EEAA levy 1,043 · **TOTAL PAID EGP 11,473** via Visa •••• 9012 | Matches Step 1/Step 3. |
| Host card | Sheikh Salama Tarabin, message, **WhatsApp Sheikh Salama (+20 10 2481 9920)** · **Call Host** · **In-App Chat** | In-app chat = FR-8.1 (Later). |
| Arrival logistics | 3 steps (Blue Hole taxi drop → coastal canyon passage 1.5 h trek or 15 min boat → Dar Tarabin arish), map with coordinates, **Open Trailhead in GPS** | Provider content. |
| Policy box | "Free cancellation until Saturday, Oct 11, 2025 (5 days prior to arrival). 100% refund… **Cancellations within 5 days retain the 5% Eco-Conservation Reef Fund**" | This is the refund rule after the deadline (FR-3.5). |

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Opens My Bookings | Lists the guest's bookings by tab; the nearest upcoming booking is selected. |
| 2 | Searches by reference/lodge/guide | Filters the list. |
| 3 | Selects a booking | Shows detail, pass, financials, host, logistics, policy. |
| 4 | Taps **Download PDF Voucher** / **Add to Calendar** | PDF voucher + receipt / .ics event. |
| 5 | Taps **Cancel Stay** | Opens Cancel dialog (4.5). |
| 6 | Taps **Modify Dates** | Opens Modify Dates (4.6). |
| 7 | On a past item taps **Receipt / Dive Log Certificate / Book Again** | Downloads document / opens the listing to rebook. |

---

### 4.5 Cancel Booking Confirmation

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-9905.png"><img src="images/42-9905.png" width="230" alt="Default – Desktop"></a> | <a href="images/42-9601.png"><img src="images/42-9601.png" width="230" alt="Default – Tablet"></a> | <a href="images/42-9448.png"><img src="images/42-9448.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/42-9291.png"><img src="images/42-9291.png" width="150" alt="Default – Native App"></a> |
| [Figma 42:9905](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-9905) | [Figma 42:9601](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-9601) | [Figma 42:9448](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-9448) | [Figma 42:9291](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-9291) |


| Element | Content (Figma) | Behaviour / rule |
|---|---|---|
| Presentation | Desktop/Tablet: centred modal over dimmed My Bookings. Mobile/Native: bottom sheet with drag handle and ✕ | — |
| Title & reference | "Cancel Reservation?" · REFERENCE DHB-2025-8841-ARB | — |
| Booking summary | Dar Tarabin, Oct 16–20 2025 (4 nights), Stargazing Palm Arish • 2 Adults, **Total paid / Settled charge EGP 11,473** (Visa •••• 9012) | — |
| Refund status | Badge "Full 100% Refund Eligible" / "100% Full Refund Guarantee"; "Grace period valid until Oct 11, 2025, 2:00 PM (5 days prior to arrival)"; native: "the entire amount of EGP 11,473 will be refunded to Apple Pay (•••• 9012). Zero penalty or conservation levy withheld." | Refund % from policy + time (FR-3.5); after the deadline the 5% reef fund is retained (see 4.4). |
| Refund ledger (desktop) | Accommodation & Breakfast +9,600 (100%) · Solar microgrid +350 (100%) · EEAA levy +1,043 (100%) · Eco-Conservation Reef Fund (5%) +480 "Fully refunded to card" · TOTAL REFUND AMOUNT | Line-by-line refundability. |
| Cancellation reason (native) | "Why are you cancelling? (Optional)": Change in dates · Trip postponed · Found another stay · Other | Optional; stored for reporting. |
| Host note | "Sheikh Salama and your Bedouin guide will be notified to release your reserved Arish and trailhead camel." | Provider notified (FR-15). |
| Actions | **Confirm Cancellation** (destructive) · **Keep My Stay** | Confirm is irreversible. |

**Step-by-step:** 1) Guest taps Cancel Stay → 2) system computes refund lines with policy + current time → 3) guest (optionally) picks a reason and taps **Confirm Cancellation** → 4) system cancels the booking, releases inventory, refunds via gateway to the original method (FR-5.3), logs the audit trail (NFR-12), sends cancellation email/push (FR-8.3), notifies the provider → 5) booking moves to **Cancelled** with refund status.

---

### 4.6 Modify Dates — Sold-out collision

**State: Sold-Out Collision Error**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-11458.png"><img src="images/42-11458.png" width="230" alt="Sold-Out Collision Error – Desktop"></a> | <a href="images/42-10893.png"><img src="images/42-10893.png" width="230" alt="Sold-Out Collision Error – Tablet"></a> | <a href="images/42-10581.png"><img src="images/42-10581.png" width="150" alt="Sold-Out Collision Error – Mobile Web"></a> | <a href="images/42-10267.png"><img src="images/42-10267.png" width="150" alt="Sold-Out Collision Error – Native App"></a> |
| [Figma 42:11458](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-11458) | [Figma 42:10893](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-10893) | [Figma 42:10581](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-10581) | [Figma 42:10267](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-10267) |


| Element | Content (Figma) | Behaviour / rule |
|---|---|---|
| Header | "Modify Stay Dates" · DHB-2025-8841-ARB · "Dar Tarabin Coastal Ecolodge • Unit: Stargazing Palm Arish" · ✕ | — |
| Collision alert | "Selected Dates Unavailable — FULL MOON HIGH TIDE SURGE — Stargazing Palm Arish is fully booked on Friday, Oct 24 and Saturday, Oct 25…" · "Requested Window Oct 23 → Oct 27 (4N)" | Lists conflicting nights. |
| Calendar | Two months (Oct "Peak Season", Nov "Open Season"); legend Current Stay (Oct 16–20) · Sold Out / Collision · Requested Range (Broken) · Suggested Open Window; **View full lodge calendar** | Sold-out nights struck through and disabled. |
| Conflict resolutions ("3 instant solutions") | ① RECOMMENDED • ZERO FEE — Shift 2 days earlier Oct 14–18, "Fare Difference: EGP 0" — **Select Window →** ② KEEP REQUESTED DATES — Upgrade to Limestone Canyon Suite +EGP 800/night, "Total Stay Delta (4 nights) +EGP 3,200", "Only 1 suite remaining" — **Switch Room Tier** ③ AUTOMATED WAITLIST — "Hold Oct 23–27 Cancellation Alert", WhatsApp number field — **Join Waitlist** | Price difference charged/refunded; waitlist stores an alert subscription. |
| Host override | "Need specific dates…? Sheikh Salama can coordinate a bespoke tent setup" — **Request Host Override** | Sends a request to the provider (not in SRS — see §7). |
| Footer | "Reservation In Conflict (2 unavailable nights selected)" · **Revert to Original (Oct 16–20)** · **Update Reservation** (disabled until conflict resolved) | Original booking untouched until Update. |

**Step-by-step:** 1) Guest taps Modify Dates → 2) picks new dates → 3) system checks availability for the same tier → 4a) available → shows new total and difference → **Update Reservation** → booking updated, difference charged/refunded, new voucher, notifications → 4b) conflict → this state: guest selects an alternative window, switches tier, joins the waitlist, requests a host override, or reverts.

---

## 5. Cross-screen business rules

1. **Price formula (as designed):** nights × nightly rate (with date overrides) + eco-conservation fund (5%) + fixed solar/desal fee + extra-cot fee → subtotal → + Sinai eco-tourism tax (10%) = total. Breakfast included. Fee names/percentages must be configurable per property/zone.
2. **Availability hold:** at Continue (Step 1) the unit is held for a limited time; released if payment is not completed.
3. **Double booking:** availability decremented atomically on payment confirmation (FR-3.6); if two guests pay for the last unit, the second payment is voided/refunded automatically.
4. **Policy snapshot:** the cancellation policy is copied onto the booking at payment time; later policy edits don't affect existing bookings.
5. **Refund:** amount = paid × refund % by time before check-in (FR-3.5); design rule for Dar Tarabin: 100% until 5 days before arrival (2:00 PM), after that everything except the 5% Eco-Conservation Reef Fund; refund to original method (FR-5.3); status tracked (pending → refunded).
6. **Modify:** allowed only if the policy allows and before the refund deadline (to confirm); price difference charged or refunded.
7. **Offline pass:** QR/PIN must be verifiable offline by the provider/ranger (signed token).
8. **Notifications:** confirmation, modification, cancellation → email + push (+ SMS/WhatsApp) (FR-8.3).
9. **Audit:** every state change and payment event is logged (NFR-12).

## 6. Story candidates for Jira

**Epic:** GUEST-BOOK-STAY — Accommodation booking & management

| Key idea | Story | Acceptance criteria |
|---|---|---|
| STAY-1 | As a guest, I want to choose dates with a calendar showing unavailable nights. | Past/full dates disabled; presets set N nights; check-in/out times shown. |
| STAY-2 | As a guest, I want to set adults, children and extra cot within the room's capacity. | "+" disabled at capacity with message; cot adds EGP 300/night. |
| STAY-3 | As a guest, I want to switch room tier and see the price difference. | Availability per tier for chosen dates; total updates. |
| STAY-4 | As a guest, I want a transparent price breakdown before paying. | Lines & total as designed; USD approximation; refund deadline date computed. |
| STAY-5 | As a guest, I want my selected unit held while I pay. | Hold created on Continue; expiry handled with message. |
| STAY-6 | As a guest, I want to enter guest details and pay by card securely. | *Needs design.* PCI gateway, 3DS, tokenisation, error states. |
| STAY-7 | As a guest, I want a confirmation with reference, voucher, QR pass and host contact. | Email sent; reference copy; PDF/print; calendar; wallet pass (native). |
| STAY-8 | As a guest, I want my check-in pass to work offline. | QR + PIN visible without network after first load; signed token. |
| STAY-9 | As a guest, I want to see my upcoming, past and cancelled bookings. | Tabs with counts; detail view; stays and activities both listed. |
| STAY-10 | As a guest, I want to cancel and see my refund before confirming. | Refund % & amount per policy; confirm → cancelled, refund issued, emails, provider notified, inventory released. |
| STAY-11 | As a guest, I want to change my dates. | Availability check; price difference charged/refunded; new voucher. |
| STAY-12 | As a guest, I want alternatives when new dates are sold out. | Conflict nights shown; alternative dates, upgrade option, waitlist toggle; original kept until confirm. |
| STAY-13 (tech) | Double-booking protection & audit log. | Concurrent payments for last unit → one succeeds, other auto-voided; all events logged. |

## 7. Gaps, inconsistencies & open questions

| # | Finding | Suggested decision |
|---|---|---|
| G1 | **Step 2 "Guest Details & Accords" + payment is not in the new Figma** — required for FR-3.2 / FR-5.1 (High, MVP). | Design Step 2 (all 4 breakpoints) incl. payment errors. |
| G2 | **Fee lines differ by breakpoint although the total is always EGP 11,473:** Desktop 9,600 + 480 (5% fund) + 350 + 1,043 (10% tax) = 11,473 ✓; Tablet selector lists 520 + 310 + "14% tax" (10,430 × 1.14 would be 11,890, not 11,473); Mobile Web shows a single "EGP 830" levy; Tablet confirmation uses 8,800 for 4 nights (EGP 2,200/night) + 920 + 640 + 1,113; Property page shows "Total before taxes 10,350" with other fees. | Define one fee/tax model (names, % vs fixed, taxable base) — needs finance/legal input (SRS §7.1 VAT) — and use it on every breakpoint. |
| G3 | **Cancellation window differs:** 5 days (desktop/tablet/native) vs 48 hours (mobile web). | Use the property's policy only. |
| G4 | **Check-out time differs:** 11:00 AM vs 11:30 AM. | Property field. |
| G5 | Mobile Web calendar shows October **2024** and weekdays "Wed/Sun" for Oct 16/20 (other breakpoints Thu/Mon 2025). | Fix copy. |
| G6 | Tablet selector shows host "Sheikh Salem Tarabin"; elsewhere "Sheikh Salama". Review count 142/218 vs 67. | Fix copy. |
| G7 | Activity bookings appear in My Bookings (past list) but there is no activity-specific booking detail/cancel design. | Reuse this pattern for activities (module 07). |
| G8 | Refundability of third-party fees (EEAA permit, eco tax) after cancellation is undefined. | Business decision. |
| G9 | Modify rules (allowed until when? fee?) undefined. | Define in policy model. |
| G12 | **Desktop Cancel dialog is rendered behind the page footer** (title and total cut off) — layout bug in Figma. | Fix the modal z-order/height. |
| G13 | Refund destination shown as Visa (desktop) vs Apple Pay (native) for the same booking. | Copy fix — always the original payment method. |
| G14 | Cancel dialog says "Half-Board Bedouin Dining Included"; everywhere else breakfast only. | Copy fix. |
| G15 | "Request Host Override" (bespoke dates) and "Impact" card are not in the SRS. | Decide scope. |
| G16 | Past items in My Bookings have **Book Again** but **no Leave a Review** button (module 08 depends on it). | Add "Leave a Review" to completed bookings. |
| G17 | My Bookings uses a different brand lockup ("DAHAB SANCTUARY & SEA") from the rest of the app ("DAHAB • دهب RESERVATIONS • TOURING • TRIPS"). | Pick one brand name. |
| G10 | "Approx. $240 USD" conversion shown — multi-currency is FR-20.3 (Later). | Keep as informational or remove. |
| G11 | Multi-room booking ("2 Rooms" appears in search) — selector supports one tier/unit only. | Decide MVP: one unit per booking. |

## 8. Out of scope for MVP
- Cash on arrival (FR-5.2), coupon codes (FR-5.4 / FR-21), booking reminders (FR-4.4-like for stays), in-app messaging (FR-8.1).
