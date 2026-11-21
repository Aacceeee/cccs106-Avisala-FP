"""Farmer location selection view."""
import flet as ft
from app import theme


def farmer_location_view(router) -> ft.Control:
    s = router.session
    manual = ft.TextField(
        hint_text="Enter Manually",
        value=s.location,
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border(theme.ACCENT, 22),
        height=44,
        text_align=ft.TextAlign.CENTER,
    )

    def next_(e):
        s.location = (manual.value or "").strip()
        if not s.location:
            manual.error = "Location is required"
            router.page.update()
            return
        router.go("assistant")

    header = ft.Row(
        [
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                          on_click=lambda e: router.back()),
            ft.Column(
                [
                    ft.Text("umAni", size=23, weight=ft.FontWeight.BOLD,
                            color="#FFFFFF"),
                    ft.Text("Smarter Choices for Every Palay Harvest.",
                            size=8, italic=True, color="#FFFFFF"),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                expand=True,
            ),
            ft.Container(width=48),
        ],
    )

    card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.92, "#FFFFFF"),
        border_radius=24,
        padding=ft.Padding.symmetric(horizontal=22, vertical=24),
        content=ft.Column(
            [
                ft.Icon(ft.Icons.LOCATION_ON, size=42, color=theme.ACCENT),
                ft.Text("Your Location", size=17, weight=ft.FontWeight.BOLD,
                        color=theme.TEXT),
                ft.Text("Allow location access for a more accurate & precise calculation.",
                        size=9, color=theme.TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER),
                ft.Container(height=8),
                ft.Button(
                    content="📍  Use My Current Location",
                    height=44,
                    style=ft.ButtonStyle(
                        bgcolor=theme.ACCENT,
                        color="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Text("or", size=11, color=theme.TEXT_MUTED),
                manual,
                ft.Text("Location will only be used to find nearby palay buyers",
                        size=8, color=theme.TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER),
                ft.Container(height=8),
                ft.OutlinedButton(
                    content="Next",
                    on_click=next_,
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        bgcolor=ft.Colors.with_opacity(0.12, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )

    content = ft.Column(
                    [
                        header,
                        ft.Container(height=14),
                        ft.Row([
                            ft.Icon(ft.Icons.LOCATION_ON_OUTLINED,
                                    color="#FFFFFF", size=18),
                            ft.Text("Your Location", size=18,
                                    weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("Allow location access for more accurate & precise calculation.",
                                size=9, color="#FFFFFF",
                                text_align=ft.TextAlign.CENTER),
                        ft.Container(height=22),
                        card,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    expand=True,
    )
    body = theme.role_page(content, theme.bottom_nav(router, active="home"))
    return theme.with_background(body, overlay=False)
