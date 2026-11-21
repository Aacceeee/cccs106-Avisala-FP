"""Farmer step 2: Enter Harvest Quantity and Location."""
import flet as ft
from app import theme


def farmer_harvest_view(router) -> ft.Control:
    s = router.session
    qty = ft.TextField(
        hint_text="Enter quantity...",
        keyboard_type=ft.KeyboardType.NUMBER,
        value="" if s.quantity_kg is None else str(s.quantity_kg),
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border(theme.ACCENT, 22),
        suffix=ft.Text("kg"),
        height=44,
        expand=True,
    )

    def next_(e):
        qty.error = None
        try:
            value = float(qty.value)
            if value <= 0:
                raise ValueError
        except (TypeError, ValueError):
            qty.error = "Enter a quantity greater than 0"
        if qty.error:
            router.page.update()
            return
        s.quantity_kg = value
        router.go("farmer_location")

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
        padding=ft.Padding.all(16),
        content=ft.Column(
            [
                ft.Container(
                    bgcolor="#F1D391",
                    border_radius=14,
                    padding=ft.Padding.all(10),
                    content=ft.Row([
                        ft.Icon(ft.Icons.GRAIN, color="#A66A13", size=28),
                        ft.Text("Palay Harvest", size=15,
                                weight=ft.FontWeight.BOLD, color=theme.TEXT),
                        ft.Container(height=10),
                    ]),
                ),
                ft.Container(height=6),
                ft.Text("Harvest Quantity (kg)", size=11,
                        weight=ft.FontWeight.BOLD, color=theme.TEXT),
                qty,
                ft.Container(
                    bgcolor="#ECF1E7",
                    border_radius=12,
                    padding=ft.Padding.all(10),
                    content=ft.Row([
                        ft.Icon(ft.Icons.INFO_OUTLINE,
                                color=theme.ACCENT, size=18),
                        ft.Text("This is needed to help you find buyers who can accept your quantity.",
                                size=9, color=theme.TEXT_MUTED, expand=True),
                    ]),
                ),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        expand=True,
    )

    content = ft.Column(
                    [
                        header,
                        ft.Container(height=12),
                        ft.Row([
                            ft.Icon(ft.Icons.GRAIN, color="#FFFFFF", size=18),
                            ft.Text("Your Harvest Details", size=18,
                                    weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("Fill us about your harvest",
                                size=9, color="#FFFFFF"),
                        ft.Container(height=26),
                        card,
                        ft.Container(height=12),
                        ft.OutlinedButton(
                            content="Next",
                            on_click=next_,
                            width=220,
                            height=44,
                            style=ft.ButtonStyle(
                                color="#FFFFFF",
                                side=ft.BorderSide(1, "#FFFFFF"),
                                shape=ft.RoundedRectangleBorder(radius=22),
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    expand=True,
    )
    body = theme.role_page(content, theme.bottom_nav(router, active="home"))
    return theme.with_background(body, overlay=False)
