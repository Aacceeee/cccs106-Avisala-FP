"""Shared app state passed between views (what the farmer entered so far)."""
from dataclasses import dataclass, field


@dataclass
class FarmerSession:
    crop: str = "Palay"
    quantity_kg: float | None = None
    location: str = ""
    pref_text: str = ""
    pref_tags: list[str] = field(default_factory=list)
    # Confirmed preferences after AI extraction, e.g. {"highest_price": True, ...}
    preferences: dict[str, bool] = field(default_factory=dict)

    def reset(self) -> None:
        self.__init__()
