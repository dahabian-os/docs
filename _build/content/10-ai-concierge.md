# 10 · AI Concierge Chat — Guest App

| | |
|---|---|
| **Module** | AI Concierge chatbot (drawer / bottom sheet) |
| **Apps** | Desktop Web (1440), Tablet Web (834), Mobile Web, Native App (390) |
| **Figma** | **Not in the Figma file yet.** The screens exist in Stitch ("AI Concierge — Chat Drawer Empty State" and "AI Concierge — Active Conversation State", 4 breakpoints each) but were not added to page *New*. Screenshots will be added once they are in Figma. |
| **SRS** | §3.10 FR-10.1, FR-10.2 (FR-10.3 Later), §3.11 FR-11.2, §5.3 LLM API, §2.6 LLM provider dependency |
| **Screens** | 1 component · 2 states · 8 Stitch screens |

---

## 1. Module summary

A chat assistant, opened from anywhere in the guest app, that answers practical questions about Dahab (visibility and currents, wind, safety, transport, what to pack, culture) in the guest's language, and **surfaces bookable listings and guide articles inline** as tappable cards. It is a slide-over drawer (desktop/tablet) or bottom sheet (mobile/native), not a full page, so the guest keeps their browsing context.

## 2. Business requirements covered (SRS)

| ID | Requirement | Priority | MVP | Where |
|---|---|---|---|---|
| FR-10.1 | Chat with an AI assistant in their language about practical Dahab questions | H | ✅ | Empty state + conversation |
| FR-10.2 | Chatbot surfaces relevant properties/activities/guide articles inline | M | ✅ | Inline listing cards in answers |
| FR-10.3 | Escalate to human support | M | Later | Not designed (safety disclaimer only) |
| FR-11.2 | Popular / similar suggestions for new users | M | ✅ | Suggested starter questions |
| §5.3 | LLM/AI API | — | ✅ | Backend |

## 3. Screen inventory

| # | State | Breakpoints (Stitch) | Presentation |
|---|---|---|---|
| 4.1 | Chat drawer — Empty state | All 4 | Desktop: right slide-over, full height, 460 px wide, blurred page behind · Tablet: 420 px slide-over with scrim · Mobile Web: bottom sheet with drag handle · Native: iOS-style modal sheet |
| 4.2 | Chat drawer — Active conversation | All 4 | Same containers; desktop drawer 480 px |

---

## 4. Screen specifications

### 4.1 Empty state

*Screenshots pending — not in Figma.*

| Element | Content (Stitch spec) | Behaviour / rule |
|---|---|---|
| Launcher | Entry point to open the concierge (floating button / header icon) | **Not specified in the designs** — see §7 G2. |
| Header | Title, language quick switch **عربي**, close **✕** (native: grabber bar + close) | Close keeps the conversation in memory for the session. |
| Greeting | "Marhaban! I'm your Dahab Coastal Guide" / "Ahlan! What can I guide you to?" — capabilities: tides, Blue Hole visibility, wind, Bedouin safaris, transport | Greeting in the UI language. |
| Live conditions pills | "Laguna: 14 kts NNE · High tide at 16:40 · Blue Hole: 35m+ visibility · Chamber standby 24/7" | Same data source as module 02. |
| Suggested starter questions (4 cards) | 🌊 "What's the visibility and drift like at Blue Hole today?" · 🤿 "Find me a beginner-friendly dive site near Eel Garden or Lighthouse" · 🎒 "What should I pack for an overnight Bedouin desert safari in Wadi Ghnai?" · ☕ "Where can I enjoy authentic campfire habak tea at sunset with locals?" | One tap sends the question. |
| Input bar | Placeholder "Ask about dive spots, wind, treks, or stays…", voice dictation, terracotta send button | Send disabled when empty. |
| Disclaimer | "Data verified by local Bedouin guides & CDWS certified dive masters. For marine emergencies call VHF Ch 16." | Always visible. |

### 4.2 Active conversation

*Screenshots pending — not in Figma.*

| Element | Content (Stitch spec) | Behaviour / rule |
|---|---|---|
| Guest message | "Find me a beginner-friendly dive site near Eel Garden or Lighthouse" · 10:24 AM | Timestamp; delivered state. |
| AI answer | Local greeting, comparison (Lighthouse Reef sheltered pebble entry & zero drift vs Eel Garden surge today), live metrics (35m+ visibility, calm, 26°C) | Answer in guest's language; grounded in platform data (listings, guide content, conditions). |
| Inline activity card | "Lighthouse Reef Guided Beginner Scuba & Skills Refresher" — instructor Youssef Ben-Ammar, CDWS badge, 12 m, gear included, ★ 4.95, 1,200 EGP/person — **Book Slot / View Session** | Card → Activity Detail / Session Picker (05/07). Only real, approved listings. |
| Inline stay card | "Dar Tarabin Coastal Ecolodge" — host Sheikh Salama, "4 minutes from Lighthouse dive center", ★ 4.96, 2,400 EGP/night — **Explore Stay** | Card → Property Detail (05). Native shows cards as a horizontal carousel. |
| Follow-up chips | Suggested next questions | One tap sends. |
| Input | "Ask follow-up or request booking…", voice, photo attachment, send | Photo attachment — see §7 G4. |
| Typing / loading state | AI "typing" indicator | Required while waiting for the LLM. |

#### Step-by-step
| # | Guest does | System does |
|---|---|---|
| 1 | Opens the concierge | Opens drawer/sheet over the current page; shows greeting, conditions, 4 starter questions. |
| 2 | Taps a starter or types a question | Shows the message; shows typing indicator; calls the LLM with context (language, current page/listing, conditions, catalogue search). |
| 3 | — | Streams the answer; attaches up to N listing/article cards from the catalogue (FR-10.2). |
| 4 | Taps a card CTA | Navigates to detail/booking; drawer closes (desktop may keep it open). |
| 5 | Asks a follow-up | Keeps conversation context. |
| 6 | Asks something unsafe/unknown | Answers with safety guidance and emergency contacts; (escalation to human is Later — FR-10.3). |
| 7 | Closes the drawer | Conversation kept for the session (history persistence — decide). |

---

## 5. Business rules

1. Answers must only recommend **approved, active** listings and published guide content; prices and availability come from the platform, never generated by the model.
2. Answer language = UI language (EN/AR), or the language the guest writes in.
3. Safety: medical/diving-emergency questions always include the hyperbaric chamber and VHF 16 contacts and a "not a substitute for a certified guide" note.
4. Store chat sessions (entity **AI Chat Session**, SRS §6) for quality review; retention and privacy rules per NFR-9.
5. Rate limits per user/device to control LLM cost.
6. Works logged-out (read-only answers); booking still requires login.

## 6. Story candidates for Jira

**Epic:** GUEST-AI-CONCIERGE

| Key idea | Story | Acceptance criteria |
|---|---|---|
| AI-1 | As a guest, I want to open a chat assistant from any page. | Drawer (desktop/tablet) / bottom sheet (mobile/native); close keeps context; launcher defined. |
| AI-2 | As a guest, I want suggested questions to start. | 4 starter cards; tap sends. |
| AI-3 | As a guest, I want answers about Dahab in my language. | EN/AR answers; typing indicator; streamed response; error state if LLM fails. |
| AI-4 | As a guest, I want the assistant to show bookable stays/activities and articles as cards. | Cards link to detail/booking; only live catalogue items; correct price. |
| AI-5 | As a guest, I want safety-critical answers to include emergency contacts. | Chamber + VHF 16 shown for safety topics; disclaimer visible. |
| AI-6 (tech) | LLM integration with catalogue retrieval, logging and rate limiting. | Prompt includes language + retrieved listings/articles; sessions logged; per-user limits. |

## 7. Gaps & open questions

| # | Finding | Suggested decision |
|---|---|---|
| G1 | **Concierge screens are not in the Figma file** (only in Stitch). | Copy the 8 Stitch screens into Figma page *New* (section "AI Concierge"). |
| G2 | **Launcher** (where the guest opens the chat) is not designed on any screen. | Add floating button / header icon to the shell. |
| G3 | Error, offline and "can't answer" states not designed. | Add sibling states. |
| G4 | Photo attachment & voice dictation in the input are not in the SRS. | Phase 2 or confirm scope. |
| G5 | Human escalation (FR-10.3) is Later — define fallback (WhatsApp desk link?). | Show "Chat with the Dahab desk on WhatsApp" link. |
| G6 | Conversation history persistence across sessions not specified. | Decide (session only for MVP). |

## 8. Out of scope for MVP
- Human escalation (FR-10.3), AI trip planner (FR-9, Phase 2), personalised recommendations (FR-11.1).
