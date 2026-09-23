# 05 · Listing Detail — Property & Activity — Guest App

| | |
|---|---|
| **Module** | Property Detail Page (PDP) · Activity / Expedition Detail Page · Photo gallery lightbox · Reviews expanded |
| **Apps** | Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (390) |
| **Figma** | Page **New** → sections *Property Detail* (12 frames, example **Dar Tarabin Coastal Ecolodge**) and *Activity Detail* (13 frames, example **Blue Hole Arch & Bells Deep Freediving Session**) |
| **SRS** | FR-2.3, FR-3.1 (entry), FR-4.1 (entry), FR-6.1 (display), FR-7.1, FR-13.4 (cancellation policy), FR-8.1 (Later), NFR-1, NFR-11 |
| **Screens** | 2 screens · 3 states each (Default, Photo gallery lightbox, Reviews expanded) · 25 frames |

---

## 1. Module summary

The detail page is where a guest decides to book. The **Property** page shows the stay, host, room tiers with prices, amenities, location, house rules, cancellation policy and reviews, with a sticky booking box. The **Activity** page shows the session, guides, schedule/time slots with live capacity, prerequisites, inclusions and add-ons, safety protocol and reviews, with a sticky booking box. Both open a full-screen photo lightbox and an expanded reviews view.

Next step after "Reserve": Property → Room Type & Date Selector (module 06); Activity → Session Picker (module 07).

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where |
|---|---|---|---|---|
| FR-2.3 | Detail page with photos, description, pricing, availability, amenities, cancellation policy, reviews | H | ✅ | Both detail pages |
| FR-3.1 | Select room type, dates, guest count; see live price & availability | H | ✅ | Property booking box + room tiers (full flow in 06) |
| FR-4.1 | Select session (date/time), participants; see live slot availability | H | ✅ | Activity slot selector + booking box (full flow in 07) |
| FR-6.1 | Ratings (1–5) and written reviews after completed bookings | H | ✅ | Reviews section + Reviews Expanded (display) |
| FR-7.1 | Save to favourites | M | ✅ | Save / heart |
| FR-13.4 | Provider sets cancellation policy per property | M | ✅ | Displayed ("Full refund up to 5 days prior") |
| FR-8.1 | Guest messages provider | M | **Later** | Design shows Chat / WhatsApp buttons — see §7 G1 |
| FR-6.3 | Provider publicly responds to a review | M | **Later** | Design shows host responses — see §7 G2 |

## 3. Screen inventory

| # | Screen | States | Breakpoints |
|---|---|---|---|
| 4.1 | Property Detail | Default · Photo gallery lightbox · Reviews expanded | All 4 |
| 4.2 | Activity Detail | Default · Photo gallery lightbox · Reviews expanded | All 4 (+1 duplicate desktop "Reviews expanded" frame) |

---

## 4. Screen specifications

### 4.1 Property Detail — Dar Tarabin Coastal Ecolodge

**Entry:** listing cards (home, search, map, zone, POI, favourites). **Exit:** Room Type & Date Selector (06), lightbox, reviews, WhatsApp host, back to results.

**State: Dar Tarabin Coastal Ecolodge**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-25591.png"><img src="images/16-25591.png" width="230" alt="Dar Tarabin Coastal Ecolodge – Desktop"></a> | <a href="images/16-24395.png"><img src="images/16-24395.png" width="230" alt="Dar Tarabin Coastal Ecolodge – Tablet"></a> | <a href="images/16-23946.png"><img src="images/16-23946.png" width="150" alt="Dar Tarabin Coastal Ecolodge – Mobile Web"></a> | <a href="images/16-23499.png"><img src="images/16-23499.png" width="150" alt="Dar Tarabin Coastal Ecolodge – Native App"></a> |
| [Figma 16:25591](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-25591) | [Figma 16:24395](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-24395) | [Figma 16:23946](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-23946) | [Figma 16:23499](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-23499) |


#### Page sections (desktop order)

| # | Section | Content (Figma) | Behaviour / rule |
|---|---|---|---|
| 1 | Conditions strip | "Red Sea Marine Conditions: Lighthouse 24°C • Blue Hole visibility optimal…", "Protectorates Eco-Permit active" | See module 02 G3. |
| 2 | Breadcrumb + actions | Stays › North Canyon Shore › Dar Tarabin Coastal Ecolodge · **Share** · **Save** | Save → favourites (login). Share → link/share sheet. |
| 3 | Title block | Badges (RARE FIND, SOLAR POWERED ECO-SANCTUARY, MARINE REEF SLOT 0M), "Authentic Tarabin Clan Land • Zone 01 Reserve", rating **4.99 (67 verified reviews)**, "Verified Bedouin Heritage Host", address | Rating links to Reviews section. |
| 4 | Photo mosaic | 5 captioned photos + **View all 28 photos** (native/mobile: swipe carousel "1 / 28 Photos") | Opens Lightbox (state 2). |
| 5 | Key facts chips | 2 Guests · 1 Bedroom · 1 King Bed · Open-Air Bath · Fringing Reef Slot 0m (tablet: Type / Capacity / Access / Grid) | Values of the selected tier. |
| 6 | Host card | "Hosted by Sheikh Salama & Family — Tribal Elder & Eco-Builder — Tarabin Clan Stewards … since 1984", quote, Response rate 100%, response time within 1 hour, languages (English, Arabic) · **WhatsApp / Chat / Contact Host** | See §7 G1 for messaging scope. |
| 7 | Highlights | 100% Off-Grid Solar & Well · Zero Light Pollution Sky · Private Fringing Reef Entry · Daily Hearth-Baked Meals | Admin/provider-managed highlights (max 4). |
| 8 | Story | "The Story of Dar Tarabin — Where Red Sea Reefs Meet the Silence of Sinai" + "Sinai Protectorate Permitted — Official eco-concession #SIN-842" | Provider description + licence number. |
| 9 | **Room tiers** "Select Your Sanctuary Tier" | 3 tiers with photo, availability badge (AVAILABLE / ONLY 1 LEFT), location in lodge, description, price/night, specs (max guests, m², beds, bath) and **Selected / Select Room**: <br>• Stargazing Palm Arish — EGP 2,400 — max 2 — 38 m² — King<br>• Limestone Canyon Suite — EGP 3,200 — max 4 — 54 m² — 2 Queen<br>• Shoreline Sanctuary Hut — EGP 2,850 — 42 m² — private tide deck | Selecting a tier updates the booking box price. Availability based on the chosen dates (FR-3.1). |
| 10 | Amenities | Grouped: Scenic Views · Eco & Sustainable Energy · Open-Air Bathing · Bedouin Culinary Hearth · Diving & Reef Sanctuary · Mindful Connectivity | Amenity list from the listing (FR-13.1). |
| 11 | Location | Map "Zone 01 Eco-Buffer — North Canyon Shoreline", distances (The Canyon dive site 400 m walk; Blue Hole 2.2 km / 7 min 4x4), **Open Satellite Trail** | Exact address shown after booking? (decide). |
| 12 | House rules "Sinai Marine & Desert Accord" | Mineral Sunscreen Only · Never Walk on Reef Flat · Quiet Hours 10 PM–7 AM · Check-in 2:00–8:00 PM · Check-out 11:00 AM | Structured fields: check-in/out times + free-text rules. |
| 13 | Cancellation policy | "Flexible Policy: Full refund up to 5 days prior to arrival" | From the property's policy (FR-13.4); drives refunds (FR-3.5). |
| 14 | Reviews | Overall 4.99 · 67 reviews, sub-scores (House Reef 5.0, Cleanliness 4.9, Hospitality…), 3 review cards (name, city, month, text, room stayed), **Read All / View All** | Opens Reviews Expanded (state 3). |
| 15 | **Sticky booking box** (desktop sidebar; mobile/native bottom bar) | Price "EGP 2,400 / night", rating, selected tier (**CHANGE**), CHECK-IN / CHECK-OUT (Oct 14 → Oct 18, 2025), GUESTS (2 Guests, 1 Private Room), price lines (EGP 2,400 × 4 nights = 9,600; Eco-Conservation Fee 400; Cleaning & Solar Upkeep 350; **Total before taxes EGP 10,350**), CTA **Reserve Your Sanctuary Stay** (mobile: **Reserve** + "Oct 14 – 18 (4 nights)"; tablet: **Edit Dates** + **Reserve Stay**), notes "You won't be charged yet • Direct host confirmation", "100% Fair-Trade Bedouin Direct Compensation", "Questions for Sheikh Salama? WhatsApp" | Changing dates/guests/tier recalculates live. Reserve → module 06 (Room Type & Date Selector) with these values. |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Opens the page | Loads listing, availability for any dates carried from search, reviews summary. |
| 2 | Browses photos / taps "View all 28 photos" | Opens Lightbox. |
| 3 | Picks a room tier | Highlights "Selected", updates booking box price and facts. |
| 4 | Picks dates and guests in booking box | Checks availability; if tier unavailable shows "Sold out for these dates" (not designed); recalculates total incl. fees. |
| 5 | Taps **Reserve** | If logged-out → Login/Register then returns; opens Room Type & Date Selector (06) pre-filled. |
| 6 | Taps **Save** / **Share** | Favourite toggle / share. |
| 7 | Taps **Read All** reviews | Opens Reviews Expanded. |
| 8 | Taps WhatsApp host | Opens WhatsApp (see §7 G1). |

---

### 4.2 Activity Detail — Blue Hole Arch & Bells Deep Freediving Session

**State: Blue Hole Arch & Bells Deep Freediving Session**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-29648.png"><img src="images/16-29648.png" width="230" alt="Blue Hole Arch & Bells Deep Freediving Session – Desktop"></a> | <a href="images/16-28300.png"><img src="images/16-28300.png" width="230" alt="Blue Hole Arch & Bells Deep Freediving Session – Tablet"></a> | <a href="images/16-27807.png"><img src="images/16-27807.png" width="150" alt="Blue Hole Arch & Bells Deep Freediving Session – Mobile Web"></a> | <a href="images/16-27313.png"><img src="images/16-27313.png" width="150" alt="Blue Hole Arch & Bells Deep Freediving Session – Native App"></a> |
| [Figma 16:29648](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-29648) | [Figma 16:28300](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-28300) | [Figma 16:27807](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-27807) | [Figma 16:27313](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-27313) |


#### Page sections

| # | Section | Content (Figma) | Behaviour / rule |
|---|---|---|---|
| 1 | Conditions strip | "Mild Current (0.4 kts) • Visibility 30m+", "COASTGUARD STATION 4 ACTIVE", "DAN Egypt: 19123" | — |
| 2 | Breadcrumb + actions | Protected Marine Reserve Zone 01 › session name · "CDWS Active Float #BH-402" · Share · Save | — |
| 3 | Title block | Badges (AIDA / SSI CERTIFIED, ZONE 01 MARINE SANCTUARY, MUZAYNA BEDOUIN PARTNER), "Depth: 30m–45m Custom Line", rating **4.98 (86 verified divers)**, "100% Zero-Decompression Dive Safety Record", meeting area | — |
| 4 | Gallery | Captioned photos + **View all 16 photos & log** | Lightbox. |
| 5 | Key facts | Duration 3.5 hours · Max depth 30–45m · Ratio & cap "Max 4 (1:2 safety)" · Prerequisite AIDA 2 / SSI Lvl 1 · Languages English & Arabic | Structured activity fields (FR-13.2). |
| 6 | Guides | **Youssef Ben-Ammar** — Master Instructor (AIDA & SSI, 12 years in Dahab, 3,200+ dives) · **Chat with Instructor** · "Responds < 15 mins"; **Salem Abu-Muzayna** — Bedouin elder & boat safety | Guide profiles belong to the provider. |
| 7 | Session route | 4 phases with duration: Majlis breathwork (45 min) → Bells chimney entry 0–26 m (45 min) → Arch drift & line 30–45 m (60 min) → Habak tea debrief (30 min) | Itinerary steps field. |
| 8 | **Slot selector** "Select Session Date & Window" | Month (October 2025), day chips (TUE … SAT) with capacity ("Full", "1 left", "3 left", "4 left"), 3 windows: **Morning Glass 07:30–11:00** (2 spots left, "Recommended for depth PBs") · **Midday Sunrays 11:30–15:00** (3 left) · **Late Afternoon Drift 15:30–18:30** (4 left); rule "Limited strictly to 4 spots per time slot to protect the 1:2 safety diver ratio" | Live capacity per session (FR-4.1). Full days disabled. |
| 9 | Prerequisites | Certification level (min AIDA 2 / SSI Level 1 / Molchanovs Wave 1 / PADI Advanced Freediver) · Medical clearance · Age 16+ & ID · **Upload C-Card** | Upload optional before booking; verified by instructor ("No charge until instructor verifies your C-Card"). |
| 10 | Inclusions & add-ons | Included (buoy + bottom plate, counter-ballast, O2 kit, Bedouin tent & tea, 4K media) · Optional rentals: Carbon bi-fins +EGP 250 · 5 mm wetsuit +EGP 200 · Noseclip & fluid goggles +EGP 100 | Add-ons selectable here or in module 07. |
| 11 | Safety & sanctuary accords | Mineral sunscreen · Hyperbaric chamber link · Lanyard mandate below 20 m · **Weather reschedule guarantee** (wind > 18 kn or swell > 0.8 m → free reschedule) | Weather rule affects module 07/06 cancellation logic. |
| 12 | Reviews | "Diver Reviews & Logbook Notes", 86 sessions, 2 cards | Opens Reviews Expanded. |
| 13 | **Sticky booking box** | EGP 1,650 / person, LIVE AVAILABILITY, Date (Thu, Oct 16, 2025), Time (Morning Glass 07:30), Ratio, **Number of certified divers** stepper ("Max 2 per safety line"), lines (Dive session 1 × 1,650; Ras Abu Galum eco-reserve entry EGP 150; Hyperbaric chamber support levy EGP 50; **Total due EGP 1,850**), CTA **Reserve Your Dive Spot**, "Free cancellation up to 48 hours prior • Weather guarantees apply", "Message Youssef on WhatsApp" | Recalculates on divers/slot change. Reserve → Session Picker / checkout (07). |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Opens the activity | Loads details, next 5–7 days of sessions with live remaining spots. |
| 2 | Picks a day | Shows the 3 windows with remaining spots; "Full" days disabled. |
| 3 | Picks a window | Updates booking box date/time. |
| 4 | Sets number of divers | Stepper limited by remaining spots and per-line max; recalculates total. |
| 5 | Optionally uploads C-Card | Stores file for instructor verification. |
| 6 | Taps **Reserve Your Dive Spot** | Login if needed → Activity Session Picker / checkout (07) pre-filled. |
| 7 | Chosen slot fills meanwhile | Shows the Sold-out slot state (module 07). |

---

### 4.3 Photo gallery lightbox (both pages)

**State: Photo Gallery Lightbox**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-26397.png"><img src="images/16-26397.png" width="230" alt="Photo Gallery Lightbox – Desktop"></a> | <a href="images/16-24965.png"><img src="images/16-24965.png" width="230" alt="Photo Gallery Lightbox – Tablet"></a> | <a href="images/16-24338.png"><img src="images/16-24338.png" width="150" alt="Photo Gallery Lightbox – Mobile Web"></a> | <a href="images/16-23884.png"><img src="images/16-23884.png" width="150" alt="Photo Gallery Lightbox – Native App"></a> |
| [Figma 16:26397](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-26397) | [Figma 16:24965](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-24965) | [Figma 16:24338](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-24338) | [Figma 16:23884](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-23884) |

**State: Photo Gallery Lightbox**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-30464.png"><img src="images/16-30464.png" width="230" alt="Photo Gallery Lightbox – Desktop"></a> | <a href="images/16-28926.png"><img src="images/16-28926.png" width="230" alt="Photo Gallery Lightbox – Tablet"></a> | <a href="images/16-28223.png"><img src="images/16-28223.png" width="150" alt="Photo Gallery Lightbox – Mobile Web"></a> | <a href="images/16-27725.png"><img src="images/16-27725.png" width="150" alt="Photo Gallery Lightbox – Native App"></a> |
| [Figma 16:30464](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-30464) | [Figma 16:28926](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-28926) | [Figma 16:28223](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-28223) | [Figma 16:27725](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-27725) |


| Element | Behaviour |
|---|---|
| Header: title, "Photo 3 of 28", **Back to Lodge** / ✕ | Close returns to the same scroll position. |
| Category tabs (Property: All 28 · Suites & Arish 12 · Reef & Water 8 · Bedouin Majlis & Food 5 · Around the Property 3; Activity: All 16 · The Bells Chimney 5 · The Blue Hole Arch 4 · Coral Saddle & Reef 4 · Bedouin Shoreline Camp 3) | Filters photos; counts per category (photo category = field on each photo). |
| Main image + prev/next arrows; keyboard arrows & Esc (desktop); swipe, pinch-to-zoom, double-tap (mobile/native) | Standard gallery controls. |
| Caption block (room/tier name, description, host quote; activity: EXIF "Sony α7S III • 16 mm", instructor note) | Caption per photo. |
| Filmstrip thumbnails "+23 more" | Jump to photo. |
| Activity only: **Download RAW** / "Full 4K", "Exif & Safety" | See §7 G6. |
| Native/Mobile only: price line ("EGP 2,400 / night") and **Book** | Shortcut to booking. |

### 4.4 Reviews expanded (both pages)

**State: Reviews Expanded**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-1027.png"><img src="images/42-1027.png" width="230" alt="Reviews Expanded – Desktop"></a> | <a href="images/42-647.png"><img src="images/42-647.png" width="230" alt="Reviews Expanded – Tablet"></a> | <a href="images/42-328.png"><img src="images/42-328.png" width="150" alt="Reviews Expanded – Mobile Web"></a> | <a href="images/42-3.png"><img src="images/42-3.png" width="150" alt="Reviews Expanded – Native App"></a> |
| [Figma 42:1027](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-1027) | [Figma 42:647](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-647) | [Figma 42:328](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-328) | [Figma 42:3](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-3) |

**State: Reviews Expanded**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/42-2626.png"><img src="images/42-2626.png" width="230" alt="Reviews Expanded – Desktop"></a> | <a href="images/42-2165.png"><img src="images/42-2165.png" width="230" alt="Reviews Expanded – Tablet"></a> | <a href="images/42-1840.png"><img src="images/42-1840.png" width="150" alt="Reviews Expanded – Mobile Web"></a> | <a href="images/42-1510.png"><img src="images/42-1510.png" width="150" alt="Reviews Expanded – Native App"></a> |
| [Figma 42:2626](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-2626) | [Figma 42:2165](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-2165) | [Figma 42:1840](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-1840) | [Figma 42:1510](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-1510) |

**State: Reviews Expanded (duplicate)**

| Desktop |
|---|
| <a href="images/42-3292.png"><img src="images/42-3292.png" width="230" alt="Reviews Expanded (duplicate) – Desktop"></a> |
| [Figma 42:3292](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=42-3292) |


| Element | Property (Figma) | Activity (Figma) | Behaviour |
|---|---|---|---|
| Summary | 4.99 / 5.0 "Top 1% in South Sinai", 67 verified reviews | 4.98, 86 verified sessions, certification distribution (AIDA 3 42%, AIDA 2 38%, Molchanovs 15%) | Average of all published reviews. |
| Sub-ratings | Reef Quality & Cleanliness · Eco-Living & Solar · Bedouin Hospitality · Listing Accuracy · Coordination & Logistics · Value for Conservation | Instructor Safety · Line Rig Stability · Equalization Coaching · Bedouin Tea & Debrief · 4K Media Quality | Averages per category — **same categories must be used in "Leave a Review" (module 08)**. |
| Search | "Search reviews by keyword…" | "Search by technique (mouthfill, Frenzel, 30m)…" | Full-text search in review text. |
| Sort | Most Recent | Most Helpful | Options: Most recent, Most helpful, Highest, Lowest. |
| Filter chips | All (67) · With Photos (24) · per room tier (31/18/18) · Solo Travelers (15) · Divers (28) | All · With 4K Video Clips (34) · Chimney & Bells (52) · The Arch (24) · First Deep Dives (19) | Tier filter uses the booked room type. |
| Review card | Name, "Verified Stay", city, room, month, score, text, **Helpful (19)**, **Report**, "Reviewed 3 weeks ago"; host response block | Name, verified diver, certification, date, logged PB depth, text, tags, **Helpful**, **Share Log**, "Verified Dive Logbook #D-8941", **Watch Clip** | Helpful = one vote per user; Report → moderation queue (FR-17.3 Later). |
| Pagination | **Show 10 More Verified Reviews** / Load More (63 remaining) | **Load More Diver Logbook Reviews** | Append. |
| Sticky CTA (mobile/native) | EGP 2,400 / night · **Reserve Now** | EGP 1,650 / diver · **Reserve Spot** | Returns into booking flow. |

---

## 5. Cross-screen business rules

1. **Only verified reviews** (guest had a completed booking — FR-6.1) are shown; label "Verified Stay / Verified Diver".
2. Prices displayed = base rate for the selected dates (incl. date overrides FR-14.2) + mandatory fees; the total line wording must be consistent ("before taxes" vs "total due" — see §7 G4).
3. Room tier availability and activity slot capacity are **live** and re-checked at Reserve (FR-3.6 prevents double booking).
4. The property's cancellation policy (FR-13.4) is shown on the page and copied onto the booking at reservation time.
5. Activity participants ≤ remaining spots and ≤ per-line maximum; certification prerequisites must be acknowledged before paying.
6. Gallery categories and captions are provider-managed with the listing (FR-13.1/13.2).

## 6. Story candidates for Jira

**Epic:** GUEST-LISTING — Listing detail pages

| Key idea | Story | Acceptance criteria |
|---|---|---|
| LIST-1 | As a guest, I want a property page with photos, description, host, amenities, location, rules, cancellation policy and reviews. | All sections of §4.1 on 4 breakpoints; rating + review count link to reviews; loads < 2 s. |
| LIST-2 | As a guest, I want to compare and select room tiers with live availability and price. | Selecting a tier updates booking box; unavailable tiers disabled for chosen dates; "Only 1 left" when 1 unit remains. |
| LIST-3 | As a guest, I want a sticky booking box that calculates my total. | Nights × rate + fees; updates on date/guest/tier change; Reserve → module 06 with values. |
| LIST-4 | As a guest, I want an activity page with guides, route, prerequisites, inclusions and safety info. | Sections of §4.2; prerequisites visible before booking. |
| LIST-5 | As a guest, I want to pick an activity day and time window with live spots left. | Full days disabled; remaining spots shown; max 4 per slot enforced. |
| LIST-6 | As a guest, I want to choose number of divers and optional rentals. | Stepper bounded; add-on prices added to total. |
| LIST-7 | As a guest, I want to upload my certification card. | JPG/PNG/PDF upload; stored with booking; optional at this step. |
| LIST-8 | As a guest, I want a full-screen photo gallery with categories. | Tabs with counts, arrows/keyboard/swipe/zoom, captions, filmstrip; Esc/✕ closes to same position. |
| LIST-9 | As a guest, I want to read, search, filter and sort all reviews. | Sub-ratings, keyword search, filter chips, sort, load more, Helpful votes, Report. |
| LIST-10 | As a guest, I want to save or share a listing. | Save toggles favourite (login); share link opens same listing. |

## 7. Gaps, inconsistencies & open questions

| # | Finding | Suggested decision |
|---|---|---|
| G1 | **Messaging buttons** (Chat with Instructor, In-App Chat, Contact Host, WhatsApp host) — in-app messaging is **FR-8.1 Phase 2**. | MVP: WhatsApp deep link only (or hide); in-app chat in Phase 2. Also confirm whether exposing hosts' phone numbers before booking is allowed. |
| G2 | **Host responses to reviews** are shown — FR-6.3 is Later. | Hide in MVP or pull FR-6.3 into MVP. |
| G3 | **Activity price inconsistent:** EGP 1,650 on detail/search, EGP 2,400 in Session Picker (module 07); totals EGP 1,850 (desktop) vs 1,700 (tablet). | Single source price; fees defined once. |
| G4 | **Cancellation window inconsistent:** Property 5 days (most) vs "48 hours" (mobile web room selector); Activity 48 h (desktop) vs 24 h (tablet). | Policy comes from the listing — fix copy. |
| G5 | **Guide names inconsistent:** Tablet shows "Salem Muzayna — AIDA Master Instructor" and review text "Guide: Youssef Barakat"; native says "9 Yrs"; desktop "12 Years". Host name "Sheikh Salama" vs "Sheikh Salem Tarabin" (tablet room selector). | Data from provider profile; fix Figma copy. |
| G6 | Activity lightbox **"Download RAW"** of marketing photos. | Remove, or restrict to guests' own session media after the activity. |
| G7 | Review counts differ (67 vs 142 vs 218 for the same lodge; 86 vs 142 for the activity). | Real data; note only. |
| G8 | Duplicate frame *Activity Detail — Reviews Expanded (Desktop)* (42:2626 and 42:3292). | Keep one. |
| G9 | "You won't be charged yet • Direct host confirmation" implies request-to-book; "Instant Reserve" elsewhere implies instant. | Decide confirmation mode (see module 03 G7). |
| G10 | Unavailable-tier / sold-out-date state on the property page not designed. | Add "Not available for your dates" state. |
| G11 | C-Card upload & medical clearance — storage of certificates/medical info (sensitive). | Define retention & access (NFR-9). |

## 8. Out of scope for MVP
- In-app guest ↔ provider messaging (FR-8.1/8.2), review photos (FR-6.2), provider review responses (FR-6.3), AI review sentiment (FR-6.4).
