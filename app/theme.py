"""umAni design tokens and reusable UI pieces.

Owner: Dev 1 (UI/UX Lead). Keep ALL colors/spacing here so every view looks consistent.
Style: rice-field photo background + dark green overlay + light "glass" cards.

Put these files in /assets:
    assets/background.jpg -> rice-field background (sample filename)
    assets/logo.png       -> umAni logo
"""
import os
import flet as ft

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
SPLASH_BG_IMAGE = "bg.jpg"
APP_BG_IMAGE = "bg_app.jpg"
LEGACY_BG_IMAGE = "bg.jpg"
LOGO_IMAGE = "logo.png"      # Replace this file with your uploaded logo

# --- Colors (tweak after comparing with Figma; pick exact values with Figma's color picker)
BG = "#14301A"
OVERLAY = ft.Colors.with_opacity(0.58, "#103216")
CARD = ft.Colors.with_opacity(0.92, "#F4F7ED")
CARD_BORDER = ft.Colors.with_opacity(0.72, "#FFFFFF")
TEXT = "#183319"
TEXT_MUTED = "#667B60"
TEXT_ON_BG = "#FFFFFF"
TEXT_ON_BG_MUTED = "#DDE8D5"
ACCENT = "#3A742F"
ACCENT_TEXT = "#FFFFFF"
GREEN = "#2E7D32"
ERROR = "#C0392B"

STATUS_COLORS = {
    "Verified": "#2E7D32",
    "Pending Verification": "#B8860B",
    "Needs Confirmation": "#C0392B",
}


def has_asset(name: str) -> bool:
    return os.path.exists(os.path.join(ASSETS_DIR, name))


def logo(size: int = 100) -> ft.Control:
    """Logo image, or a placeholder icon until logo.png is replaced."""
    if has_asset(LOGO_IMAGE):
        return ft.Image(src=LOGO_IMAGE, width=size, height=size)
    return ft.Container(
        width=size,
        height=size,
        border_radius=size,
        bgcolor=ft.Colors.with_opacity(0.18, "#FFFFFF"),
        border=ft.Border.all(2, ft.Colors.with_opacity(0.55, "#FFFFFF")),
        alignment=ft.Alignment.CENTER,
        content=ft.Icon(ft.Icons.GRASS, size=int(size * 0.55), color="white"),
    )


def with_background(content: ft.Control, overlay: bool = True,
                    image_name: str | None = None,
                    wrap_glass: bool = False) -> ft.Control:
    """Full-bleed rice-field photo behind any content."""
    layers = []
    selected_image = image_name or APP_BG_IMAGE
    if has_asset(selected_image):
        layers.append(ft.Image(
            src=selected_image,
            fit=ft.BoxFit.COVER,
            expand=True,
        ))
    elif has_asset(SPLASH_BG_IMAGE):
        layers.append(ft.Image(
            src=SPLASH_BG_IMAGE,
            fit=ft.BoxFit.COVER,
            expand=True,
        ))
    else:
        layers.append(ft.Container(expand=True, gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_CENTER, end=ft.Alignment.BOTTOM_CENTER,
            colors=["#8A9A5B", "#4F7A2B", "#2F5A1E", "#1F3D14"])))
    if overlay:
        layers.append(ft.Container(expand=True, bgcolor=OVERLAY))
    if wrap_glass:
        layers.append(glass_panel(
            content,
            padding=14,
            border_radius=38,
        ))
    else:
        layers.append(content)
    return ft.Stack(layers, expand=True,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE)


def primary_button(label: str, on_click, expand: bool = True) -> ft.Button:
    return ft.Button(
        content=label, on_click=on_click, height=50, expand=expand,
        style=ft.ButtonStyle(
            bgcolor=ACCENT,
            color=ACCENT_TEXT,
            shape=ft.RoundedRectangleBorder(radius=16),
        ),
    )


def secondary_button(label: str, on_click) -> ft.OutlinedButton:
    return ft.OutlinedButton(
        content=label, on_click=on_click, height=50,
        style=ft.ButtonStyle(color=TEXT_ON_BG, side=ft.BorderSide(1, TEXT_ON_BG),
                             shape=ft.RoundedRectangleBorder(radius=25)),
    )


def card(content: ft.Control, on_click=None, border_color=CARD_BORDER) -> ft.Container:
    return ft.Container(
        content=content, padding=16, bgcolor=CARD, border_radius=20,
        border=ft.Border.all(1, border_color), on_click=on_click,
    )


def glass_panel(content: ft.Control, padding: int = 18,
                border_radius: int = 38) -> ft.Container:
    """One translucent, blurred, rounded panel used across the app."""
    if isinstance(content, ft.Column):
        content.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        content.main_axis_alignment = ft.MainAxisAlignment.CENTER
        if content.scroll is None:
            # Tall content scrolls inside the panel instead of overflowing,
            # so the bottom nav never has to move.
            content.scroll = ft.ScrollMode.AUTO
    return ft.Container(
        content=content,
        margin=ft.Margin.only(left=18, right=18, top=56, bottom=10),
        padding=ft.Padding.all(padding),
        bgcolor=ft.Colors.with_opacity(0.38, "#1A1F14"),
        blur=ft.Blur(14, 14),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.25, "#FFFFFF")),
        border_radius=border_radius,
        expand=True,
    )


def text_field_border(color: str = ACCENT, radius: float = 22):
    return ft.OutlineInputBorder(
        border_radius=radius,
        side=ft.BorderSide(1, color),
    )


def role_page(content: ft.Control, navigation: ft.Control) -> ft.Control:
    """Fixed bottom-navigation shell used by Farmer and Admin views."""
    panel = glass_panel(
        content,
        padding=16,
        border_radius=38,
    )
    body = ft.SafeArea(
        content=ft.Column(
            [panel, navigation],
            spacing=0,
            expand=True,
        ),
        expand=True,
    )
    return body


# (key, label, icon, route). Every role uses the same nav widget with its own items.
FARMER_NAV = [
    ("home", "Home", ft.Icons.HOME, "farmer_home"),
    ("results", "Results", ft.Icons.BAR_CHART_ROUNDED, "farmer_results"),
    ("profile", "Profile", ft.Icons.PERSON, "settings"),
]


def bottom_nav(router, active: str = "home", items: list | None = None) -> ft.Container:
    """Shared floating bottom navigation. Tabs use router.replace (no Back pile-up)."""
    cells = []
    for key, label, icon, route in (items or FARMER_NAV):
        is_active = key == active
        color = "#1F3D1B" if is_active else "#4A4A4A"
        cells.append(ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            on_click=None if is_active else (lambda e, r=route: router.replace(r)),
            content=ft.Column(
                [
                    ft.Icon(icon, size=22, color=color),
                    ft.Text(label, size=10, color=color,
                            weight=ft.FontWeight.BOLD if is_active else ft.FontWeight.W_500),
                    ft.Container(width=34, height=2, bgcolor=color if is_active else None),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=1,
            ),
        ))
    return ft.Container(
        height=64,
        margin=ft.Margin.only(left=16, right=16, bottom=8),
        padding=ft.Padding.symmetric(horizontal=8, vertical=6),
        bgcolor=ft.Colors.with_opacity(0.94, "#EDEDE6"),
        border_radius=30,
        shadow=ft.BoxShadow(spread_radius=0, blur_radius=12,
                            color=ft.Colors.with_opacity(0.18, "#000000")),
        content=ft.Row(cells, alignment=ft.MainAxisAlignment.SPACE_AROUND),
    )


def badge(text: str) -> ft.Container:
    return ft.Container(
        content=ft.Text(text, size=11, color="white", weight=ft.FontWeight.W_600),
        bgcolor=STATUS_COLORS.get(text, ACCENT),
        padding=ft.Padding.symmetric(horizontal=10, vertical=3), border_radius=12,
    )


def screen(router, title: str, controls: list, subtitle: str | None = None,
           step: str | None = None, back: bool = True) -> ft.Control:
    """Standard page frame: background photo, back button, title, scrollable body."""
    header = [
        ft.Row([
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color=TEXT_ON_BG,
                          on_click=lambda e: router.back())
            if back else ft.Container(width=48, height=48),
            ft.Text(step or "", size=12, color=TEXT_ON_BG_MUTED),
        ]),
        ft.Text(title, size=26, weight=ft.FontWeight.BOLD, color=TEXT_ON_BG),
    ]
    if subtitle:
        header.append(ft.Text(subtitle, size=14, color=TEXT_ON_BG_MUTED))
    content = glass_panel(
        ft.Column(header + [ft.Container(height=8)] + controls,
                  scroll=ft.ScrollMode.AUTO, spacing=12, expand=True),
        padding=18,
        border_radius=38,
    )
    body = ft.Column(
        [
            ft.Container(
                content=content,
                padding=ft.Padding.only(left=2, right=2, top=18, bottom=10),
                expand=True,
            ),
            bottom_nav(router),
        ],
        expand=True,
        spacing=0,
    )
    return with_background(body, wrap_glass=False)
