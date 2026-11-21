"""PLACEHOLDER logic so the UI works end-to-end.

Backend devs: replace these functions with the real implementations (AI extraction,
database queries, Haversine, AHP) but KEEP the function names/return shapes so the
views do not need to change.
"""

PREF_LABELS = {
    "highest_price": "Highest price",
    "nearest": "Nearest buyer",
    "cash": "Cash payment",
    "pickup": "Buyer picks up",
}

_KEYWORDS = {
    "highest_price": ["price", "highest", "best", "mahal", "presyo"],
    "nearest": ["near", "close", "malapit"],
    "cash": ["cash"],
    "pickup": ["pick up", "pickup", "pick-up", "sundo"],
}
_TAG_TO_KEY = {v: k for k, v in PREF_LABELS.items()}


def extract_preferences(text: str, tags: list[str]) -> dict[str, bool]:
    """Stand-in for the AI preference extractor (keyword matching only)."""
    lowered = text.lower()
    prefs = {k: any(w in lowered for w in words) for k, words in _KEYWORDS.items()}
    for tag in tags:
        prefs[_TAG_TO_KEY[tag]] = True
    return prefs


def get_ranked_buyers(session) -> list[dict]:
    """Stand-in for: retrieve offers -> filter -> Haversine -> AHP rank."""
    buyers = [
        {"name": "Sample Rice Mill A", "price": 22.50, "distance_km": 4.2, "status": "Verified", "age_days": 1},
        {"name": "Sample Trader B", "price": 23.10, "distance_km": 12.8, "status": "Verified", "age_days": 3},
        {"name": "Sample Cooperative C", "price": 21.80, "distance_km": 2.5, "status": "Verified", "age_days": 6},
    ]
    if session.preferences.get("highest_price"):
        buyers.sort(key=lambda b: -b["price"])
    elif session.preferences.get("nearest"):
        buyers.sort(key=lambda b: b["distance_km"])
    return buyers
