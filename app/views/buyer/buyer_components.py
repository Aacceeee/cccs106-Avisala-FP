"""Shared data and UI components for Buyer screens."""
from datetime import datetime

import flet as ft
from app import theme

BTN_GREEN = "#2C5E10"
GREEN_TEXT = "#1F3D1B"
BRAND_GREEN = "#6DAF58"
LIGHT_CARD = ft.Colors.with_opacity(0.92, "#EDEDE6")

PAYMENT_OPTIONS = ["Cash upon weighing", "Cash", "Installment", "Cash / Installment"]
BUYER_NAV = [
    ("dashboard", "Dashboard", ft.Icons.HOME, "buyer_dashboard"),
    ("offers", "Offers", ft.Icons.LOCAL_OFFER, "buyer_offers"),
    ("profile", "Profile", ft.Icons.PERSON, "buyer_profile"),
]

DEFAULT_PROFILE = {
    "name": "ABC Traders",
    "type": "Rice Mill",
    "address": "Pili, Camarines Sur",
    "phone": "09123456789",
    "email": "abc@gmail.com",
}

DEFAULT_OFFER = {
    "price": "23.50",
    "quantity": "2000",
    "payment": "Cash upon weighing",
    "requirements": "Clean & dry palay",
    "status": "Pending Admin Verification",
    "updated": "Nov 18, 2026",
}


def profile(router) -> dict:
    return {key: getattr(router.session, f"buyer_{key}", value)
            for key, value in DEFAULT_PROFILE.items()}


def offer(router) -> dict:
    return getattr(router.session, "buyer_offer", DEFAULT_OFFER)


def tab(router, route: str) -> None:
    getattr(router, "replace", router.go)(route)


def brand_header(router=None) -> ft.Control:
    left = (ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                          on_click=lambda e: router.back())
            if router else ft.Container(width=48))
    brand = ft.Column([
        ft.Row([
            theme.logo(52),
            ft.Text("umAni", size=30, weight=ft.FontWeight.BOLD,
                    color=BRAND_GREEN),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=4),
        ft.Text("Smarter Choices for Every Palay Harvest.", size=10,
                italic=True, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=2)
    return ft.Row([left, ft.Container(brand, expand=True), ft.Container(width=48)])


def portal_chip() -> ft.Control:
    return ft.Row([ft.Container(
        content=ft.Text("Buyer Portal  ·  Palay Purchasing",
                        size=11, color="#FFFFFF"),
        padding=ft.Padding.symmetric(horizontal=18, vertical=6),
        bgcolor=ft.Colors.with_opacity(0.30, "#000000"),
        border_radius=16,
    )], alignment=ft.MainAxisAlignment.CENTER)


def section_title(icon, title: str, subtitle: str) -> ft.Control:
    return ft.Column([
        ft.Row([
            ft.Icon(icon, size=26, color="#FFFFFF"),
            ft.Text(title, size=17, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
        ], spacing=8),
        ft.Text(subtitle, size=10, color="#FFFFFF"),
    ], spacing=2)


def light_card(content: ft.Control) -> ft.Container:
    return ft.Container(
        content=content,
        padding=14,
        bgcolor=LIGHT_CARD,
        border_radius=20,
    )


def pill(text: str, bg: str, fg: str, icon=None) -> ft.Container:
    row = ([ft.Icon(icon, size=12, color=fg)] if icon else [])
    row += [ft.Text(text, size=9, weight=ft.FontWeight.BOLD, color=fg)]
    return ft.Container(
        content=ft.Row(row, spacing=3, tight=True),
        bgcolor=bg,
        padding=ft.Padding.symmetric(horizontal=8, vertical=3),
        border_radius=10,
    )


def kv(label: str, value: str, value_color: str = GREEN_TEXT,
       bold_value: bool = False) -> ft.Text:
    return ft.Text(
        spans=[
            ft.TextSpan(f"{label}: ", ft.TextStyle(color=theme.TEXT_MUTED)),
            ft.TextSpan(value, ft.TextStyle(
                color=value_color,
                weight=ft.FontWeight.BOLD if bold_value else ft.FontWeight.W_500,
            )),
        ],
        size=11,
    )


def action_button(label: str, on_click, icon=None, width: int = 230) -> ft.Control:
    content = [ft.Text(label, size=13, weight=ft.FontWeight.BOLD, color="#FFFFFF")]
    if icon:
        content.append(ft.Icon(icon, size=16, color="#FFFFFF"))
    return ft.Row([ft.Button(
        content=ft.Row(content, alignment=ft.MainAxisAlignment.CENTER,
                       spacing=8, tight=True),
        on_click=on_click,
        width=width,
        height=46,
        style=ft.ButtonStyle(
            bgcolor=BTN_GREEN,
            side=ft.BorderSide(1.5, "#FFFFFF"),
            shape=ft.RoundedRectangleBorder(radius=26),
        ),
    )], alignment=ft.MainAxisAlignment.CENTER)


def white_button(label: str, on_click, color: str = BTN_GREEN,
                 width: int = 230) -> ft.Control:
    return ft.Row([ft.Button(
        content=ft.Text(label, size=13, weight=ft.FontWeight.BOLD, color=color),
        on_click=on_click,
        width=width,
        height=46,
        style=ft.ButtonStyle(
            bgcolor="#FFFFFF",
            shape=ft.RoundedRectangleBorder(radius=26),
        ),
    )], alignment=ft.MainAxisAlignment.CENTER)


def buyer_page(router, active: str, controls: list,
               back: bool = False) -> ft.Control:
    panel = theme.glass_panel(
        ft.Column(
            [brand_header(router if back else None), *controls],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        padding=16,
        border_radius=38,
    )
    body = ft.SafeArea(
        content=ft.Column([
            panel,
            theme.bottom_nav(router, active=active, items=BUYER_NAV),
        ], spacing=0, expand=True),
        expand=True,
    )
    return theme.with_background(body, overlay=False)


def input(**kwargs) -> ft.TextField:
    return ft.TextField(
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        text_size=12,
        color="#1F1F1F",
        **kwargs,
    )
