# Dahab Guest App — Module Specifications (for Jira)

**Sources:** SRS v1.0 (`dahab_platform_srs.md`) · Figma file **Dahab** → page **New** (162 frames, 25 sections, exported as PNG into `images/`) · Stitch generation specs for the AI Concierge (not in Figma).
**Prepared:** 23 September 2026.

Each module file has the same structure, so it can be turned into an Epic with Stories directly:

1. Module summary · 2. SRS requirements covered (FR IDs, priority, MVP flag) · 3. Screen inventory · 4. Screen specifications — screenshots for every state × breakpoint (Desktop · Tablet · Mobile Web · Native App, each linked to its Figma frame), UI elements table, **step-by-step table (guest action → system response)**, states & errors · 5. Business rules · 6. **Story candidates** with acceptance criteria · 7. Gaps, inconsistencies & open questions · 8. Out of scope for MVP.

## Modules

| # | File | Figma sections | Frames | Epic key idea |
|---|---|---|---|---|
| 01 | [Account & Authentication](01-account-authentication.md) | Register, Login, Forgot Password, Verification OTP, Edit Profile | 28 | GUEST-AUTH |
| 02 | [Discovery Home](02-discovery-home.md) | Discovery Home Feed | 17 | GUEST-DISCOVERY |
| 03 | [Search Results & Map](03-search-results-and-map.md) | Property Search Results, Activity Search Results, Search Results (map) | 20 | GUEST-SEARCH |
| 04 | [Dahab Guide — Zones, POIs, Articles](04-dahab-guide-zones-pois-articles.md) | Zone Overview, POI Detail, Guide Article | 12 | GUEST-GUIDE |
| 05 | [Listing Detail — Property & Activity](05-listing-detail-property-activity.md) | Property Detail, Activity Detail | 25 | GUEST-LISTING |
| 06 | [Accommodation Booking & My Bookings](06-accommodation-booking-and-my-bookings.md) | Room Type & Date Selector, Booking Confirmation, My Bookings, Cancel Booking Confirmation, Modify Dates | 20 | GUEST-BOOK-STAY |
| 07 | [Activity Booking](07-activity-booking.md) | Activity Session Picker, Activity Booking Confirmation | 12 | GUEST-BOOK-ACTIVITY |
| 08 | [Reviews & Favorites](08-reviews-and-favorites.md) | Leave a Review, Favorites / Wishlist | 12 | GUEST-ENGAGE |
| 09 | [Notifications & Language](09-notifications-and-language.md) | Notification Center, Language Switcher | 12 | GUEST-NOTIFY-L10N |
| 10 | [AI Concierge](10-ai-concierge.md) | *not in Figma yet* | 0 (8 in Stitch) | GUEST-AI-CONCIERGE |

## Top findings across all modules (decide before writing stories)

### A. Screens required by the SRS but missing from Figma
| Missing screen | Blocks | Module |
|---|---|---|
| **Checkout — Guest details & payment (stays)** | FR-3.2, FR-5.1 (High, MVP) | 06 |
| **Checkout — Participant details & payment (activities)** | FR-4.2 (High, MVP) | 07 |
| **Set new password** (after reset link/code) | FR-1.2 | 01 |
| OTP error states (wrong / expired / too many attempts) | FR-1.5 | 01 |
| Activity search filter panel + empty state | FR-2.2, FR-2.6 | 03 |
| Activity cancel / reschedule | FR-4.3 | 07 |
| AI Concierge screens (exist in Stitch only) + launcher | FR-10.1, FR-10.2 | 10 |
| Logged-in web account menu (Profile, Bookings, Saved, Log out) | FR-1.2 | 01 |
| Stories/Guides index, Zones index | FR-2.4 | 04 |

### B. Designed features that the SRS marks "Later" (decide: hide for MVP or move into MVP)
In-app chat with host/instructor (FR-8.1) · host responses to reviews (FR-6.3) · review photo upload (FR-6.2) · currency selector (FR-20.3) · "Save to Itinerary" (AI trip planner FR-9) · plus features not in the SRS at all: audio article narration, wishlist collections/sharing & split deposits, extended profile (passport ID, emergency contact, dive certificates, permits), French/German/Russian + Hijri calendar settings, "Request Host Override" on date changes, host moderation of reviews.

### C. Data that must be defined once (currently inconsistent between screens)
- **Fee & tax model** for stays (5% fund vs fixed levies; 10% vs 14% tax) — module 06 G2.
- **Cancellation windows** (5 days vs 48 h for the same property; 48 h vs 24 h for the activity).
- **Activity price** (EGP 1,650 vs 2,400), time windows and add-on prices — module 07 G1–G3.
- **Emergency numbers** (several variants of the chamber, police and hospital numbers) — module 04 G1.
- **Password rule**, OTP validity, lockout policy — module 01.
- **Instant booking vs host confirmation** — module 03 G7 / module 05 G9.
- **Native tab bar** (4 tabs vs 5 with "Updates") and the web PWA banner wrongly shown on native frames.
- **Brand name** changes between modules: "DAHAB • دهب — Reservations • Touring • Trips" (auth, discovery, search, guide), "Dahab Sanctuary & Sea" / "Dahab Sanctuary & Sea Marketplace" (bookings, reviews, favourites, settings), "DAHAB LIFE" (native notifications).
- **Lead instructor** for the same freediving session: Youssef Ben-Ammar (detail, confirmation, notifications) vs Captain Zaki Mansour (session picker).
- **Review categories** for stays and activities (Leave a Review ≠ Reviews Expanded).
- **Live marine-conditions data source** (used on Home, Zone, POI, Activity, Concierge) — not in SRS §5.3.

### D. Figma housekeeping
- Discovery Home has 3 different filter panels on Native/Mobile Web and 2 on Tablet — pick one.
- Duplicate frame: Activity Detail — Reviews Expanded (Desktop) ×2.
- Desktop error states for Register/Login use a different header and misspell the brand in Arabic ("ذهب" instead of "دهب").
- Tablet frames are 1280 px wide in Figma (named 834 px).
- Desktop *Cancel Booking* dialog renders behind the page footer; broken glyphs in the header currency pill (later modules).

## How to use these files in Jira
1. One **Epic** per module (key idea in the table above).
2. One **Story** per row of section 6; paste the step-by-step table of the related screen into the story description and the Given/When/Then lines into acceptance criteria.
3. Attach the screenshots from `images/` (file name = Figma frame ID, e.g. `16-635.png`) or link the Figma frame.
4. Create **Spike/Decision** tickets from section 7 items marked "decide" before the related stories go into a sprint.
