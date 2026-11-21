# umAnI: Project Scope

**Author:** Dev 1, Requirements Engineer & UI/UX Lead; Dev 2, Data & Systems Architect (Database, APIs, UML Class/Sequence, Model-View-Controller (MVC));Dev 3, QA & DevOps Lead (GitFlow, Automated Testing, PyInstaller Packaging)
**Version:** 0.1 (draft)

## 1. Purpose

umAnI is a Flet-based application that helps palay (rice) farmers find and compare buyers based on their harvest details and selling preferences. Tagline: *"Smarter Choices for Every Palay Harvest."*

## 2. Problem Statement

Palay farmers often sell to whichever buyer is nearest or most familiar, with little visibility into competing offers. umAnI gives farmers a ranked, transparent comparison of verified buyer offers so they can decide where to sell.

## 3. Objectives

1. Let farmers compare palay buyers using quantity, location, and personal selling preferences.
2. Keep buyer offers trustworthy through admin verification.
3. Keep prices current through a 7-day offer validity rule.

## 4. Users

| Role | Description |
|---|---|
| Farmer | Enters harvest details and preferences, then reviews ranked buyers. |
| Buyer | Maintains own profile and submits price/offer updates. |
| Admin | Manages buyer profiles, records and verifies offers, enforces validity. |

## 5. In Scope

- Three role-based access paths: Farmer, Buyer, Admin
- Buyer comparison for **palay only**
- Farmer inputs: harvest quantity, location, selling preferences
- AI extraction of preferences from the farmer's input, followed by farmer confirmation
- Buyer price/offer submission (pending until verified)
- Admin buyer management, offer recording, and offer verification
- Offer validity of 7 days, after which offers are marked "Needs Confirmation"
- Buyer filtering by crop, quantity, and offer status
- Distance calculation using the Haversine formula
- Buyer ranking using AHP (Analytic Hierarchy Process)
- Display of ranked buyers with offer details

## 6. Out of Scope

- Crops other than palay
- Payments, contracts, or transactions
- In-app chat or negotiation
- Delivery and logistics
- Real-time market price feeds

## 7. Assumptions and Constraints

- Frontend is built with **Flet** (Python).
- Buyer offers are verified by an admin before farmers can see them.
- Farmers provide location manually or via device location. *(TODO: confirm with team)*
- Project is hosted and versioned on GitHub.

## 8. Team Roles

| Dev | Name | Role |
|---|---|---|
| Dev 1 | Marc Ace T. Evangelista| Requirements Engineer & UI/UX Lead (Scope, SRS, User Stories, Flet Views) |
| Dev 2 | Mark Paul B. Calvelo| Data & Systems Architect (Database, APIs, UML Class/Sequence, Model-View-Controller (MVC)) |
| Dev 3 | Janline B. Lerio| QA & DevOps Lead (GitFlow, Automated Testing, PyInstaller Packaging) |
