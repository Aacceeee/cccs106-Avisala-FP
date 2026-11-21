# umAnI: Software Requirements Specification (SRS)

**Author:** Dev 1, Requirements Engineer & UI/UX Lead
**Version:** 0.1 (draft)

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for umAni, an application that helps palay farmers compare buyers.

### 1.2 Scope
See `01-scope.md`.

### 1.3 Definitions

| Term | Meaning |
|---|---|
| Palay | Unmilled rice |
| AHP | Analytic Hierarchy Process, a multi-criteria decision method used for ranking |
| Haversine | Formula for great-circle distance between two coordinates |
| Offer | A buyer's price and terms for palay |
| Verified | Offer confirmed by an admin |
| Needs Confirmation | Verified offer older than 7 days |

## 2. Overall Description

### 2.1 Product Perspective
A Flet (Python) application with three role-based paths (Farmer, Buyer, Admin), a data store for buyers and offers, and an AI component for preference extraction.

### 2.2 User Classes
Farmer, Buyer, Admin (see Scope).

### 2.3 Operating Environment
Flet app on mobile and/or web. *(TODO: confirm target platforms)*

### 2.4 Assumptions and Dependencies
- Reliable data from admins and buyers.
- AI service available for preference extraction. *(TODO: confirm which service)*
- Internet connection required.

## 3. Functional Requirements

### 3.1 General
| ID | Requirement |
|---|---|
| FR-01 | The system shall display a splash screen with a "Get Started" action. |
| FR-02 | The system shall let the user choose an access role: Buyer or Farmer. |

### 3.2 Farmer
| ID | Requirement |
|---|---|
| FR-F1 | The system shall let a farmer start a buyer comparison without logging in. *(TODO: confirm)* |
| FR-F2 | The system shall let a farmer select a crop; only palay is supported. |
| FR-F3 | The system shall accept harvest quantity (positive number) and location. |
| FR-F4 | The system shall accept the farmer's selling preferences. |
| FR-F5 | The system shall use AI to extract structured preferences from the farmer's input. |
| FR-F6 | The system shall show extracted preferences and require farmer confirmation before ranking. |
| FR-F7 | The system shall retrieve buyer offers and filter by crop, quantity, and offer status. |
| FR-F8 | The system shall compute distance between farmer and each buyer using the Haversine formula. |
| FR-F9 | The system shall rank eligible buyers using AHP. |
| FR-F10 | The system shall display ranked buyers with offer details. |

### 3.3 Buyer
| ID | Requirement |
|---|---|
| FR-B1 | The system shall authenticate buyers before access. |
| FR-B2 | The system shall show a buyer only their own profile and offers. |
| FR-B3 | The system shall let a buyer submit a price or offer update. |
| FR-B4 | The system shall set new submissions to "Pending Verification". |
| FR-B5 | The system shall let a buyer reconfirm an offer marked "Needs Confirmation". |

### 3.4 Admin
| ID | Requirement |
|---|---|
| FR-A1 | The system shall authenticate admins before access. |
| FR-A2 | The system shall let admins manage buyer profiles and accounts. |
| FR-A3 | The system shall let admins record actual buyer offers. |
| FR-A4 | The system shall let admins verify offer source and details. |
| FR-A5 | If a buyer is no longer purchasing palay, the system shall mark them inactive for palay. |
| FR-A6 | If an offer is not verified, the system shall keep it pending or request correction. |
| FR-A7 | When an offer is verified, the system shall record its confirmation date. |
| FR-A8 | The system shall mark offers older than 7 days from confirmation as "Needs Confirmation". |
| FR-A9 | Only verified offers within the 7-day period shall appear in farmer comparisons. |

## 4. Offer Status Lifecycle

`Pending Verification` -> `Verified` -> (after 7 days) `Needs Confirmation` -> (reconfirmed) `Pending Verification`

Buyers can also be `Inactive` for palay.

## 5. Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Usability | Screens shall use simple language and large touch targets suitable for farmers with limited tech experience. |
| NFR-02 | Usability | Core farmer flow shall be completable in under 2 minutes. *(TODO: validate)* |
| NFR-03 | Performance | Ranked results shall display within 5 seconds of confirming preferences. |
| NFR-04 | Security | Buyer and admin accounts shall require authentication; passwords shall be stored hashed. |
| NFR-05 | Security | Role-based access shall prevent buyers from viewing other buyers' data. |
| NFR-06 | Reliability | Offer status changes shall be consistent and auditable. |
| NFR-07 | Maintainability | Code shall be organized by views, services, and models, and documented in the repo. |
| NFR-08 | Localization | UI text should support Filipino/English. *(TODO: confirm)* |

## 6. UI Requirements

Dark-navy theme matching the flowchart; green rice-field splash with the umAni logo and tagline. One Flet view per screen:

| Role | Views |
|---|---|
| Shared | Splash, Role Select |
| Farmer | Crop Select, Harvest Input, Preferences, Confirm Preferences, Ranked Results |
| Buyer | Login, Dashboard, Submit Offer |
| Admin | Login, Dashboard, Buyer Management, Offer Verification |

## 7. Open Questions

1. How are farmer locations captured (manual, GPS, map pin)?
2. What AHP criteria and weights are used (price, distance, payment terms, ...)?
3. Which AI service extracts preferences?
4. Which database and hosting will be used?
5. Do farmers need accounts?
