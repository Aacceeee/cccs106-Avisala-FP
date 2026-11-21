# umAni: User Stories

**Author:** Dev 1, Requirements Engineer & UI/UX Lead
**Priority key:** M = Must have, S = Should have, C = Could have

## Farmer

| ID | Story | Acceptance Criteria | Priority |
|---|---|---|---|
| US-F1 | As a farmer, I want to start a buyer comparison so that I can find where to sell my palay. | "Get Started" leads to role selection; Farmer path opens crop selection. | M |
| US-F2 | As a farmer, I want to select palay as my crop so that I only see palay buyers. | Palay is selectable; results only include palay buyers. | M |
| US-F3 | As a farmer, I want to enter my harvest quantity and location so that results fit my situation. | Quantity must be a positive number; location is required. | M |
| US-F4 | As a farmer, I want to enter my selling preferences so that rankings reflect what matters to me. | Preferences can be entered in free text or guided input. | M |
| US-F5 | As a farmer, I want to review and confirm the AI-extracted preferences so that I can fix mistakes. | Extracted preferences are shown and editable; ranking only runs after confirmation. | M |
| US-F6 | As a farmer, I want to see ranked buyers with offer details so that I can choose where to sell. | List shows rank, buyer, price, distance, and offer status. | M |
| US-F7 | As a farmer, I want to see only current offers so that I am not misled by old prices. | Only offers within the 7-day validity period are included. | M |

## Buyer

| ID | Story | Acceptance Criteria | Priority |
|---|---|---|---|
| US-B1 | As a buyer, I want to log in so that I can manage my own information. | Valid credentials open the Buyer Dashboard. | M |
| US-B2 | As a buyer, I want to view my profile and current offers so that I know what farmers see. | Dashboard shows own profile and offers only. | M |
| US-B3 | As a buyer, I want to submit a price or offer update so that my offer stays current. | Submission is saved as "Pending Verification". | M |
| US-B4 | As a buyer, I want to be marked inactive when I stop buying palay so that I don't appear in comparisons. | Inactive buyers are excluded from results. | S |
| US-B5 | As a buyer, I want to reconfirm an expired offer so that it becomes visible again. | Reconfirmation sends the offer back to verification. | S |

## Admin

| ID | Story | Acceptance Criteria | Priority |
|---|---|---|---|
| US-A1 | As an admin, I want to log in securely so that only authorized people manage data. | Valid admin credentials open the Admin Dashboard. | M |
| US-A2 | As an admin, I want to manage buyer profiles and accounts so that buyer data stays accurate. | Admin can add, edit, and deactivate buyers. | M |
| US-A3 | As an admin, I want to record actual buyer offers so that farmers have real data. | Admin-recorded offers are saved with source and date. | M |
| US-A4 | As an admin, I want to verify offer source and details so that only trustworthy offers are shown. | Offer is marked Verified, or kept Pending / returned for correction. | M |
| US-A5 | As an admin, I want offers older than 7 days marked "Needs Confirmation" so that prices stay current. | Status changes automatically after 7 days from confirmation date. | M |
| US-A6 | As an admin, I want to mark a buyer inactive if they no longer buy palay so that results stay relevant. | Buyer is excluded from comparisons for palay. | S |

## Traceability to Flowchart

| Flowchart Step | User Story |
|---|---|
| Start Buyer Comparison, Select Crop | US-F1, US-F2 |
| Enter Harvest Quantity and Location | US-F3 |
| Enter / AI Extracts / Confirm Preferences | US-F4, US-F5 |
| Retrieve, Filter, Haversine, AHP, Display | US-F6, US-F7 |
| Buyer Login to Update Submitted | US-B1 to US-B3 |
| Still Purchasing Palay? | US-B4, US-A6 |
| Verify Offer, Mark Verified | US-A3, US-A4 |
| 7-Day Validity, Needs Confirmation | US-A5, US-B5 |
