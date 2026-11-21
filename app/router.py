"""Tiny screen router: keeps a history stack so the Back button works.

Views never import each other. They call router.go("name"), and main.py
registers which function builds which name.

    go(name)       push a screen (Back returns to the previous one)
    replace(name)  swap the current screen (used by bottom-nav tabs)
    back()         pop to the previous screen
    home()         clear farmer data and return to the Farmer home screen
"""
import flet as ft
from app.state import FarmerSession

HOME_ROUTE = "farmer_home"


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.session = FarmerSession()
        self._builders: dict = {}
        self._stack: list[str] = []

    def register(self, name: str, builder) -> None:
        self._builders[name] = builder

    def go(self, name: str) -> None:
        self._stack.append(name)
        self._render()

    def replace(self, name: str) -> None:
        """Swap the current screen without growing the Back history."""
        if self._stack:
            self._stack.pop()
        self.go(name)

    def back(self) -> None:
        if len(self._stack) > 1:
            self._stack.pop()
            self._render()

    def home(self) -> None:
        """Clear farmer data and return to the Farmer home screen."""
        self.session.reset()
        self._stack = [HOME_ROUTE]
        self._render()

    def _render(self) -> None:
        name = self._stack[-1]
        builder = self._builders.get(name) or self._coming_soon(name)
        self.page.controls.clear()
        self.page.add(builder(self))
        self.page.update()

    @staticmethod
    def _coming_soon(name: str):
        """Fallback so an unregistered route shows a stub instead of crashing."""
        def view(router):
            from app import theme
            return theme.screen(router, name.replace("_", " ").title(), [
                theme.card(ft.Text("Coming soon.", color=theme.TEXT_MUTED))])
        return view
