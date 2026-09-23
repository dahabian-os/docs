# 01 · Account & Authentication — Guest App

| | |
|---|---|
| **Module** | Guest Account & Authentication |
| **Apps** | Guest app — Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (iOS/Android, 390) |
| **Figma** | File "Dahab" → page **New** → sections *Register, Login, Forgot Password, Verification OTP, Edit Profile* |
| **SRS** | §3.1 Guest Account & Authentication, §3.20 Localization, NFR-3, NFR-6, NFR-9, NFR-11 |
| **Screens** | 5 screens · 9 states · 28 frames |

---

## 1. Module summary

Lets a tourist create a Dahab account (email/password, Google or Apple), verify it with a 6-digit code (SMS, with WhatsApp as a fallback), log in, recover a forgotten password, and maintain a profile. Every screen exists in English (LTR) and must work in Arabic (RTL); the Tablet error states in Figma are the Arabic reference specimens.

**Happy path:** Register → Verification OTP → (logged in) → Discovery Home.
**Returning user:** Login → Discovery Home (or back to the page that required login).
**Recovery:** Login → Forgot password → Recovery link/code sent → *Set new password (not designed — see §7)* → Login.

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where in the design |
|---|---|---|---|---|
| FR-1.1 | Register via email/password, Google, or Apple | H | ✅ | Register |
| FR-1.2 | Log in, log out, reset a forgotten password | H | ✅ | Login, Forgot Password, Edit Profile (Log out on native only) |
| FR-1.3 | Edit profile: name, photo, nationality, preferred language, phone | M | ✅ | Edit Profile |
| FR-1.4 | Delete account / request data deletion | M | Later | Not designed (correct for MVP) |
| FR-1.5 | Email/SMS verification on registration | H | ✅ | Verification OTP |
| FR-20.2 | Switch language at any time from settings | H | ✅ | Language toggle in every header + Edit Profile language toggle |
| NFR-3 | HTTPS/TLS, hashed passwords (bcrypt/argon2) | — | ✅ | Backend; "256-bit encrypted" badges on screens |
| NFR-6 | First-time guest can book without > 5 setup steps | — | ✅ | Register + OTP = 2 steps |
| NFR-9 | Personal data encrypted at rest; export/deletion supported | — | ✅ | Edit Profile collects passport/ID data → in scope of NFR-9 |
| NFR-11 | WCAG 2.1 AA where practical | — | ✅ | All forms (labels, error text, contrast) |

## 3. Screen inventory

| # | Screen | States in Figma | Breakpoints |
|---|---|---|---|
| 4.1 | Register | Default · Validation error | All 4 (Tablet error state is the Arabic RTL specimen) |
| 4.2 | Login | Default · Wrong-credentials error | All 4 (Tablet error state is Arabic RTL) |
| 4.3 | Forgot Password | Default · Recovery link dispatched | All 4 |
| 4.4 | Verification OTP | 6-digit entry | All 4 |
| 4.5 | Edit Profile | Default | All 4 |

**Shared shell (all web screens):** top header — logo *DAHAB • دهب*, links *Discover Stays · Diving & Safari Trips · Bedouin Stories · Dahab Zones Map*, language toggle *EN | عربي*, *HOST PORTAL* link, profile icon; footer with destination links, legal links and the 24/7 emergency block (Dahab Hyperbaric Chamber +20 69 364 0530, VHF Ch 16). Mobile Web adds a PWA "Install" banner at the top. **Native App:** iOS-style nav bar (*Cancel* · title · *عربي*); screens reached after login show the bottom tab bar *Explore · Saved · Bookings · Profile*.

---

## 4. Screen specifications

### 4.1 Register

**Purpose:** create a guest account. **Entry points:** "Create account / Register" links on Login; header profile icon when logged out; any action that requires an account (Reserve, Save to favorites). **Exit:** Verification OTP (success) · Login (via "Log in" link) · previous screen (Cancel on native).

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-635.png"><img src="images/16-635.png" width="230" alt="Default – Desktop"></a> | <a href="images/16-414.png"><img src="images/16-414.png" width="230" alt="Default – Tablet"></a> | <a href="images/16-141.png"><img src="images/16-141.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/16-5.png"><img src="images/16-5.png" width="150" alt="Default – Native App"></a> |
| [Figma 16:635](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-635) | [Figma 16:414](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-414) | [Figma 16:141](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-141) | [Figma 16:5](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-5) |

**State: Validation Error**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-823.png"><img src="images/16-823.png" width="230" alt="Validation Error – Desktop"></a> | <a href="images/16-515.png"><img src="images/16-515.png" width="230" alt="Validation Error – Tablet"></a> | <a href="images/16-278.png"><img src="images/16-278.png" width="150" alt="Validation Error – Mobile Web"></a> | <a href="images/16-87.png"><img src="images/16-87.png" width="150" alt="Validation Error – Native App"></a> |
| [Figma 16:823](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-823) | [Figma 16:515](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-515) · Arabic RTL | [Figma 16:278](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-278) | [Figma 16:87](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-87) |


#### UI elements

| Element | Type | Behaviour / rule |
|---|---|---|
| Continue with **Google** | Button (SSO) | Starts Google OAuth. On success creates/links account and skips the password fields. |
| Continue with **Apple** | Button (SSO) | Starts Sign in with Apple. Required on iOS whenever another social login is offered. *Missing on Tablet design.* |
| Full Name / اسم الضيف | Text input, required | Error copy: "Name is required for Bedouin permits & guest checks." *Missing on Tablet design.* |
| Email Address | Email input, required | Must be a valid address with a top-level domain. Error: "Please enter a valid email address with top-level domain." |
| Password | Password input, required, show/hide toggle (mobile web) | Helper text: "Must be at least 8 characters with 1 number." (see §7 — rule differs between breakpoints) |
| Create Dahab Account / Agree & Register | Primary button | Validates all fields; on success sends the verification code and opens Verification OTP. |
| Consent text | Static text with links | "By signing up, you agree to Dahab's Terms & honor the Environmental Charter". Tapping "Agree & Register" = acceptance. |
| Already have an account? **Log in** | Link | Opens Login. |
| عربي / EN toggle | Toggle | Switches UI language and direction instantly; form content is kept. |
| Cancel (native) | Nav button | Closes the flow without saving. |
| Install (mobile web) | Banner button | Offers "Add to home screen" (PWA). Dismissible. |
| Hero panel, testimonial, "Join 12,000+ …" (desktop) | Marketing content | Static; managed as content, no logic. |

#### Step-by-step — email registration (happy path)

| # | Guest does | System does |
|---|---|---|
| 1 | Opens Register | Shows empty form; SSO buttons on top (web) or below the form (native). |
| 2 | Types full name, email, password | Inline validation on blur (format, password rule). |
| 3 | Taps **Create Dahab Account / Agree & Register** | Validates all fields server-side; checks email not already registered. |
| 4 | — | Creates the account in *unverified* state, stores password hashed (bcrypt/argon2), records consent timestamp + terms version. |
| 5 | — | Sends a 6-digit verification code (SMS; WhatsApp available as fallback; email per FR-1.5) and opens **Verification OTP**. |
| 6 | Enters the code (see 4.4) | Marks account verified, signs the guest in, returns them to the page they came from (or Discovery Home). |

#### Step-by-step — Google / Apple

| # | Guest does | System does |
|---|---|---|
| 1 | Taps Google or Apple | Opens the provider's consent sheet. |
| 2 | Approves | If the email already exists → links the provider to that account and signs in. If new → creates the account using the provider's name/email (Apple "Hide my email" relay addresses must be accepted). |
| 3 | Cancels at provider | Returns to Register with no error message. |

#### States & errors

- **Validation error** (Figma state): summary alert at the top — Desktop "Please correct 2 highlighted fields"; Native "Missing required fields — Check full name & email before submitting."; Mobile Web "Please correct highlighted fields before submitting". Each invalid field gets a coral-red border (#C24338) and an inline message under it. Focus moves to the first invalid field (accessibility).
- **Email already registered** — *not designed.* Proposed: inline under email "An account with this email already exists. Log in or reset your password."
- **SSO failure / network error** — *not designed.*
- **Loading** — button shows a spinner and is disabled to prevent double submission (not designed).

#### Breakpoint differences
- Desktop: split screen — marketing hero (left, teal) + form (right).
- Tablet: centred card; *only Google SSO, only Email + Password fields* (see §7).
- Mobile Web: SSO buttons first, then "OR SIGN IN WITH EMAIL", then fields; PWA install banner.
- Native: nav bar with Cancel/title/عربي; CTA reads "Agree & Register"; SSO below the CTA.

---

### 4.2 Login

**Purpose:** sign in a returning guest. **Entry:** header profile icon, "Log in" links, protected actions (Reserve, Saved, Bookings, Profile tabs). **Exit:** previous page / Discovery Home; Forgot Password; Register.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-1654.png"><img src="images/16-1654.png" width="230" alt="Default – Desktop"></a> | <a href="images/16-1394.png"><img src="images/16-1394.png" width="230" alt="Default – Tablet"></a> | <a href="images/16-1135.png"><img src="images/16-1135.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/16-987.png"><img src="images/16-987.png" width="150" alt="Default – Native App"></a> |
| [Figma 16:1654](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1654) | [Figma 16:1394](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1394) | [Figma 16:1135](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1135) | [Figma 16:987](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-987) |

**State: Wrong-Credentials Error**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-1815.png"><img src="images/16-1815.png" width="230" alt="Wrong-Credentials Error – Desktop"></a> | <a href="images/16-1509.png"><img src="images/16-1509.png" width="230" alt="Wrong-Credentials Error – Tablet"></a> | <a href="images/16-1275.png"><img src="images/16-1275.png" width="150" alt="Wrong-Credentials Error – Mobile Web"></a> | <a href="images/16-1074.png"><img src="images/16-1074.png" width="150" alt="Wrong-Credentials Error – Native App"></a> |
| [Figma 16:1815](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1815) | [Figma 16:1509](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1509) · Arabic RTL | [Figma 16:1275](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1275) | [Figma 16:1074](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1074) |


#### UI elements

| Element | Type | Behaviour / rule |
|---|---|---|
| Google / Apple | SSO buttons | Same as Register; logs in or creates the account. |
| Email or Phone Number | Text input | Accepts an email **or** an Egyptian mobile number (+20). |
| Password | Password input | — |
| Forgot password? | Link | Opens Forgot Password, pre-filling the email/phone typed so far. |
| Keep me signed in for 30 days / Remember me | Checkbox (web) / switch (native) | If on: session refresh token valid 30 days; if off: session ends when the browser/app session ends. |
| Log In to Dahab | Primary button | Authenticates. |
| Don't have an account? Create account | Link | Opens Register. |
| Contact Bedouin Support | Link (error state) | Opens support channel (WhatsApp/help page — target not defined). |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Enters email/phone + password | — |
| 2 | Optionally ticks "Keep me signed in for 30 days" | — |
| 3 | Taps **Log In** | Verifies credentials. |
| 4a | — (correct) | Creates session, returns to the originating page (deep-link return), otherwise Discovery Home. If the account is not yet verified → opens Verification OTP. |
| 4b | — (wrong) | Shows the wrong-credentials state, keeps the email, clears the password, decrements remaining attempts. |
| 5 | After the last failed attempt | Temporarily locks the account; shows lockout message and "Reset password now". |

#### States & errors
- **Wrong credentials** (Figma state): alert "Incorrect email or password — The credentials provided do not match our Sinai records. Please check your spelling or reset your password." + inline "Wrong password. 3 attempts remaining before lockout." + "Trouble accessing your account? Contact Bedouin Support". Native: "Incorrect credentials — The password entered is incorrect. 3 attempts remaining before temporary lockout." + "Reset password now".
- **Account locked** — *not designed* (message, duration, unlock by reset).
- **Unverified account** — redirect to OTP (not designed as a separate message).

---

### 4.3 Forgot Password

**Purpose:** let a guest recover access by email or Egyptian mobile number. **Entry:** "Forgot password?" on Login, "Reset password now" in the error state. **Exit:** "Back to Log In", or the reset link/code.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-2916.png"><img src="images/16-2916.png" width="230" alt="Default – Desktop"></a> | <a href="images/16-2590.png"><img src="images/16-2590.png" width="230" alt="Default – Tablet"></a> | <a href="images/16-2184.png"><img src="images/16-2184.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/16-1939.png"><img src="images/16-1939.png" width="150" alt="Default – Native App"></a> |
| [Figma 16:2916](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2916) | [Figma 16:2590](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2590) | [Figma 16:2184](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2184) | [Figma 16:1939](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-1939) |

**State: Recovery Link Dispatched**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-3130.png"><img src="images/16-3130.png" width="230" alt="Recovery Link Dispatched – Desktop"></a> | <a href="images/16-2757.png"><img src="images/16-2757.png" width="230" alt="Recovery Link Dispatched – Tablet"></a> | <a href="images/16-2404.png"><img src="images/16-2404.png" width="150" alt="Recovery Link Dispatched – Mobile Web"></a> | <a href="images/16-2071.png"><img src="images/16-2071.png" width="150" alt="Recovery Link Dispatched – Native App"></a> |
| [Figma 16:3130](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-3130) | [Figma 16:2757](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2757) | [Figma 16:2404](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2404) | [Figma 16:2071](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-2071) |


#### UI elements

| Element | Type | Behaviour / rule |
|---|---|---|
| Back to Login | Link | Returns to Login. |
| Email or Phone Number | Input; Mobile Web adds tabs **Email Address / SMS / WhatsApp** | Accepts email or +20 number (placeholder "eg. +20 10X XXX XXXX"). |
| Quick fill chips (mobile web) | Chips with previous identifiers | Pre-fills from values remembered on this device only (see §7 privacy note). |
| Off-grid tip | Info callout | "If SMS signals are weak along the gulf, choose email recovery…" |
| Send Reset Instructions | Primary button | Sends link and/or code. |
| Remember your password? Log in | Link | Back to Login. |
| **Dispatched state:** Open Email App | Button | Opens the default mail app (native/mobile). |
| Resend code (0:54) | Button with countdown | Disabled until the countdown ends. |
| Reference code "DHB-792-XPR", "Valid for 15 minutes", "Dispatched via Sinai SMS Gateway + Email" | Info block | Shows channel, expiry and a support reference. |
| Contact Assalah Desk / WhatsApp Desk | Link | Human support fallback. |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Enters email or phone, taps **Send Reset Instructions** | Validates format. |
| 2 | — | If an account exists: sends a one-time reset link (email) and/or 6-digit code (SMS/WhatsApp), valid **15 minutes**. The response is identical whether or not the account exists (no account enumeration). |
| 3 | — | Shows **Recovery link dispatched** with masked destination (e.g. +20 ••• ••• 4182), expiry, reference code, resend countdown. |
| 4 | Opens the link or enters the code | *Set new password screen — not designed.* |
| 5 | Sets a new password | Invalidates old sessions, confirms success, signs in or returns to Login. |

---

### 4.4 Verification OTP

**Purpose:** verify the guest's phone/email after registration (FR-1.5); reused for password-reset codes and phone changes. **Entry:** after Register; after login of an unverified account. **Exit:** logged-in destination; "Edit contact" returns to the previous form.

**State: 6-Digit**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-3832.png"><img src="images/16-3832.png" width="230" alt="6-Digit – Desktop"></a> | <a href="images/16-3671.png"><img src="images/16-3671.png" width="230" alt="6-Digit – Tablet"></a> | <a href="images/16-3476.png"><img src="images/16-3476.png" width="150" alt="6-Digit – Mobile Web"></a> | <a href="images/16-3366.png"><img src="images/16-3366.png" width="150" alt="6-Digit – Native App"></a> |
| [Figma 16:3832](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-3832) | [Figma 16:3671](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-3671) | [Figma 16:3476](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-3476) | [Figma 16:3366](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-3366) |


#### UI elements

| Element | Type | Behaviour / rule |
|---|---|---|
| Destination line | Text | "We sent a 6-digit code to +20 10****5432" (masked). |
| Wrong number or email? Edit contact / Change number | Link | Returns to edit the destination; a new code is sent. |
| 6-digit code boxes | OTP input (6 cells) | Auto-advance, paste of the full code, numeric keyboard, SMS auto-fill (iOS one-time-code / Android SMS Retriever). |
| Time remaining 04:32 | Countdown | Code validity (≈5 min on desktop). |
| Confirm & Continue / Confirm & Login / Verify Code | Primary button | Enabled only when 6 digits are entered ("6 digits entered • Ready to proceed"). |
| Resend SMS in 37s | Button with cooldown | Re-sends after cooldown. |
| Send code via WhatsApp | Secondary option | Sends the same/new code over WhatsApp Business API. |
| العرض بالعربية (RTL) (mobile web) | Toggle | Switches to Arabic. |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Arrives from Register | Code already sent; countdown starts. |
| 2 | Types / pastes / auto-fills the 6 digits | Enables the confirm button. |
| 3 | Taps Confirm | Validates code and expiry. |
| 4a | Correct | Marks phone/email verified, signs in, redirects. |
| 4b | Wrong / expired | *Error state not designed* — proposed inline "Incorrect code. 2 attempts left." / "Code expired — resend a new one." |
| 5 | Taps Resend (after cooldown) or WhatsApp | Sends new code, invalidates the previous one, restarts timers. |

---

### 4.5 Edit Profile

**Purpose:** manage personal details used by hosts and for Sinai permits. **Entry:** Profile tab (native), avatar menu (web). **Exit:** Save Changes / Done; Discard / Cancel.

**State: Default**

| Desktop | Tablet | Mobile Web | Native App |
|---|---|---|---|
| <a href="images/16-4772.png"><img src="images/16-4772.png" width="230" alt="Default – Desktop"></a> | <a href="images/16-4421.png"><img src="images/16-4421.png" width="230" alt="Default – Tablet"></a> | <a href="images/16-4239.png"><img src="images/16-4239.png" width="150" alt="Default – Mobile Web"></a> | <a href="images/16-4059.png"><img src="images/16-4059.png" width="150" alt="Default – Native App"></a> |
| [Figma 16:4772](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-4772) | [Figma 16:4421](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-4421) | [Figma 16:4239](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-4239) | [Figma 16:4059](https://www.figma.com/design/JeROg9VP2nDmcMHfGjXmLy/Dahab?node-id=16-4059) |


#### UI elements (union of all breakpoints)

| Element | Type | SRS | Behaviour / rule |
|---|---|---|---|
| Profile photo — Upload New Image / Change Photo / Remove | Image upload | FR-1.3 | JPG or PNG, max 4 MB (mobile web copy). Visible to hosts. |
| Full legal name (as in passport) | Text, required | FR-1.3 | Used on bookings and permit manifests. |
| Nationality | Select | FR-1.3 | Helper: "Determines protectorate gate fee exemption rates." |
| WhatsApp & mobile number (+20 default, country code picker) | Phone input, required, "Verified" badge | FR-1.3 | Changing it must trigger OTP re-verification (4.4). |
| Preferred language — English (LTR) / العربية (RTL) | Segmented toggle | FR-1.3, FR-20.2 | Changes app language and the language of notifications/manifests. |
| Emergency contact in Dahab — Update Contact | Sub-form | *not in SRS* | Name, relation, phone. |
| Passport / National ID ("Tourism Manifest", "Permits ID") | Select + ID field | *not in SRS* | Sensitive → encrypt at rest (NFR-9). |
| Dive certifications (e.g. "PADI Advanced Open Water #219084", "AIDA 3 • PADI Rescue") — Update Certification | Sub-form | *not in SRS* | Could feed the activity prerequisite check (module 07). |
| Reef Guardian pledge — View Pledge / Download Certificate PDF | Badge + link | *not in SRS* | — |
| "Sinai Checkpoint Clearance 85% complete" | Progress indicator | *not in SRS* | Profile completeness. |
| Save Changes / Done / Save / Save Credentials | Primary action | FR-1.3 | Validates & saves; success toast (not designed). |
| Discard / Cancel | Secondary | — | Reverts unsaved changes (confirm if dirty — not designed). |
| Log Out of Dahab Account | Destructive link (native only) | FR-1.2 | Ends session, returns to Discovery Home. |

#### Step-by-step

| # | Guest does | System does |
|---|---|---|
| 1 | Opens Profile → Edit | Loads current values. |
| 2 | Changes photo | Uploads to object storage/CDN, shows preview. |
| 3 | Edits name / nationality / language | Marks form dirty; Save enabled. |
| 4 | Changes phone number | On save, sends OTP to the new number; the number is only replaced after verification. |
| 5 | Taps **Save Changes** | Validates, saves, confirms. If language changed, UI re-renders in the new language/direction. |
| 6 | Taps Discard / Cancel | Reverts to stored values. |

---

## 5. Cross-screen business rules

1. **One account per email and per verified phone number.**
2. **Password policy (to confirm, see §7):** minimum 8 characters incl. at least 1 number; stored with bcrypt/argon2 (NFR-3).
3. **Verification:** a new account can browse but must be verified before completing a booking (NFR-6 keeps this to Register + OTP).
4. **OTP:** 6 digits, single use, expires (≈5 min registration; 15 min password reset), resend cooldown ≈60 s, max attempts before a new code is required (to define). Channels: SMS first, WhatsApp as fallback (SRS §5.3).
5. **Lockout:** after N failed logins (design implies 5 — "3 attempts remaining") lock temporarily; unlock via reset or timeout (duration to define).
6. **Session:** "Keep me signed in" = 30-day refresh token; otherwise session-only.
7. **Language:** EN/AR toggle available on every auth screen; switching keeps typed values; Arabic flips layout to RTL.
8. **Privacy:** error messages must not reveal whether an email/phone is registered (login and forgot password).
9. **Accessibility:** every input has a visible label, errors are announced to screen readers, OTP cells are a single labelled group.

## 6. Story candidates for Jira

**Epic:** GUEST-AUTH — Guest Account & Authentication

| Key idea | Story | Acceptance criteria (Given / When / Then) |
|---|---|---|
| AUTH-1 | As a guest, I want to register with my name, email and password so that I can book stays and trips. | • Given valid data, when I tap Create Account, then an unverified account is created and I land on Verification OTP.<br>• Given an invalid email or missing name, when I submit, then I see the summary alert and inline errors from the design and no account is created.<br>• Given an email that already exists, when I submit, then I am told to log in or reset my password.<br>• Password stored hashed; consent (terms version + timestamp) recorded. |
| AUTH-2 | As a guest, I want to sign up / log in with Google. | • New email → account created and signed in.<br>• Existing email → provider linked, signed in.<br>• Cancel at Google → back on the form, no error. |
| AUTH-3 | As a guest, I want to sign up / log in with Apple. | Same as AUTH-2; supports Apple private relay email; available on iOS, Android and web. |
| AUTH-4 | As a new guest, I want to verify my phone with a 6-digit code so that my account is trusted. | • Code sent after registration; masked destination shown.<br>• Paste and SMS auto-fill work; confirm enabled at 6 digits.<br>• Correct code → verified + signed in.<br>• Wrong/expired code → error message, attempts limited.<br>• Resend available after cooldown; WhatsApp alternative sends a code. |
| AUTH-5 | As a returning guest, I want to log in with my email or phone and password. | • Correct → signed in and returned to the page I came from.<br>• "Keep me signed in" keeps me logged in 30 days. |
| AUTH-6 | As a guest, I want clear feedback when my credentials are wrong so that I can recover. | • Generic "Incorrect email or password" message.<br>• Remaining attempts shown; lockout after the limit with "Reset password now". |
| AUTH-7 | As a guest, I want to request a password reset by email or phone. | • Same confirmation shown whether or not the account exists.<br>• Link/code valid 15 minutes; resend after countdown; reference code shown. |
| AUTH-8 | As a guest, I want to set a new password from the reset link/code. | *Needs design.* New password + confirm, same policy; old sessions invalidated; success message. |
| AUTH-9 | As a guest, I want to edit my profile (photo, name, nationality, language, phone). | • Changes saved and shown after reload.<br>• Photo JPG/PNG ≤ 4 MB.<br>• Phone change requires OTP on the new number.<br>• Language change re-renders UI (LTR/RTL). |
| AUTH-10 | As a guest, I want to log out on any platform. | Log out available on native (designed) and web (avatar menu — needs design); session revoked. |
| AUTH-11 | As an Arabic-speaking guest, I want all auth screens in Arabic RTL. | All labels, errors and placeholders translated; layout mirrored as in the Tablet RTL specimens; strings externalised (NFR-7). |
| AUTH-12 (tech) | Security baseline for auth (NFR-3). | HTTPS only, argon2/bcrypt, rate limiting on login/OTP/reset endpoints, OTP and reset tokens single-use. |

## 7. Gaps, inconsistencies & open questions (from comparing SRS ↔ Figma)

| # | Finding | Screens | Suggested decision |
|---|---|---|---|
| G1 | **"Set new password" screen is missing** — the reset flow ends at "Recovery link dispatched". | Forgot Password | Design a Set New Password screen + success state (all 4 breakpoints). |
| G2 | **OTP error states missing** (wrong code, expired code, too many attempts). | Verification OTP | Add sibling states. |
| G3 | **Where does the phone number come from?** OTP says "We sent a code to +20 10 9876 5432", but Register has no phone field. | Register → OTP | Either add a phone field to Register, or verify email first and phone later. SRS FR-1.5 allows email *or* SMS. |
| G4 | **Password rule differs by breakpoint:** "8+ chars" (native), "Min. 8 characters" (mobile web), "at least 8 characters with 1 number" (desktop), "8 letters & numbers with at least one symbol" (Arabic tablet). | Register | Pick one rule and use identical copy in EN/AR. |
| G5 | **Tablet Register** has no Full Name field and no Apple button; Tablet Login has both SSO buttons. | Register (Tablet) | Align Tablet with other breakpoints. |
| G6 | **Error-state desktop screens use a different header/footer** (nav "Cottages & Camps · Freedive & Scuba · Bedouin Treks · Environmental Charter · HOST A REEF CHALET · Sign In") and the brand written **"ذهب" (gold) instead of "دهب" (Dahab)**. | Register & Login desktop error states | Use the standard shell; fix Arabic spelling. |
| G7 | Wrong-credentials native copy says "The **password** entered is incorrect" → reveals the account exists. | Login (Native) | Use the generic web copy. |
| G8 | Lockout policy not defined (attempt count, duration). | Login | Define, e.g. 5 attempts → 15-minute lock. |
| G9 | OTP timer/validity differs (04:32 desktop, 0:51/0:27/0:44 resend on others; reset says 15 min). | OTP, Forgot Password | Define: registration code validity, reset link validity, resend cooldown. |
| G10 | **Native app screens show the web "INSTALL" PWA banner** (Edit Profile, OTP native). | Native frames | Remove from native. |
| G11 | Tablet OTP copy is written for hosts ("Two-Step Host Security", "Protecting bedouin dive trips…"). | OTP (Tablet) | Use guest copy. |
| G12 | Edit Profile collects much more than FR-1.3 (passport/national ID, emergency contact, dive certifications, permits, reef pledge, profile completeness). | Edit Profile | Decide MVP scope; if kept, update SRS and treat IDs as sensitive data (NFR-9). |
| G13 | Log out exists only on native; no web avatar/account menu is designed. | Edit Profile / header | Design the logged-in header menu (Profile, Bookings, Saved, Log out). |
| G14 | "Quick fill" chips on Forgot Password show stored emails/phones — privacy risk on shared devices. | Forgot Password (Mobile Web) | Only show values from this device, or remove. |
| G15 | "Contact Bedouin Support" target is undefined. | Login error, Forgot Password | Define support channel (WhatsApp Business number / help centre). |

## 8. Out of scope for MVP (per SRS)
- FR-1.4 Delete account / data-deletion request (Later) — note NFR-9 still requires the backend to support deletion requests.
- Provider staff/admin login (Provider Portal / Admin Panel modules).
