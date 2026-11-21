"""umAni AI assistant preference screen."""
import flet as ft
from app import theme
from app.services.mock_data import extract_preferences


def assistant_view(router) -> ft.Control:
    message = ft.TextField(
        hint_text="Type your preference here...",
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border("#D9E1D5", 22),
        expand=True,
        height=44,
    )

    def send(e):
        text = (message.value or "").strip()
        if text:
            router.session.pref_text = text
            router.session.preferences = extract_preferences(text, [])
            router.go("farmer_preferences")

    def continue_(e):
        text = message.value or ""
        router.session.pref_text = text
        router.session.preferences = extract_preferences(text, [])
        router.go("farmer_preferences")

    def compare_buyers(e):
        text = (message.value or "").strip()
        if not text:
            message.error = "Tell umAni what matters most to you"
            router.page.update()
            return
        message.error = None
        router.session.pref_text = text
        router.session.preferences = extract_preferences(text, [])
        router.go("farmer_preferences")

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

    content = ft.Column(
        [
            header,
            ft.Container(height=10),
            ft.Container(
                            width=194,
                            height=194,
                            border_radius=97,
                            bgcolor=ft.Colors.with_opacity(0.35, "#E6EDD9"),
                            border=ft.Border.all(
                                2, ft.Colors.with_opacity(0.45, "#FFFFFF")),
                            alignment=ft.Alignment.CENTER,
                            content=ft.Column(
                                [
                                    ft.Icon(ft.Icons.SMART_TOY_OUTLINED,
                                            size=54, color="#FFFFFF"),
                                    ft.Container(
                                        bgcolor="#FFFFFF",
                                        border_radius=12,
                                        padding=ft.Padding.symmetric(
                                            horizontal=10, vertical=4),
                                        content=ft.Text("umAni AI Assistant",
                                                        size=10,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=theme.ACCENT),
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=6,
                            ),
            ),
            ft.Container(height=12),
            ft.Text("Tell us what you're\nlooking for in a buyer.",
                    size=17, weight=ft.FontWeight.BOLD,
                    color="#FFFFFF", text_align=ft.TextAlign.CENTER),
            ft.Text("You can type it in\nyour own words.",
                    size=10, color="#FFFFFF",
                    text_align=ft.TextAlign.CENTER),
            ft.Container(height=10),
            ft.Container(
                            bgcolor=ft.Colors.with_opacity(0.88, "#FFFFFF"),
                            border_radius=18,
                            padding=ft.Padding.all(10),
                            content=ft.Column([
                                ft.Text("Your Message", size=8,
                                        weight=ft.FontWeight.BOLD,
                                        color=theme.TEXT_MUTED),
                                ft.Row([
                                    message,
                                    ft.IconButton(
                                        ft.Icons.ARROW_UPWARD,
                                        icon_color="#FFFFFF",
                                        bgcolor=theme.ACCENT,
                                        on_click=send,
                                    ),
                                ], spacing=6),
                                ft.Button(
                                    content="Compare Buyers",
                                    on_click=compare_buyers,
                                    height=36,
                                    style=ft.ButtonStyle(
                                        bgcolor=theme.ACCENT,
                                        color="#FFFFFF",
                                        shape=ft.RoundedRectangleBorder(radius=18),
                                    ),
                                ),
                            ], spacing=5),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=8,
        expand=True,
    )
    body = theme.role_page(
        content,
        theme.bottom_nav(router, active="home"),
    )
    return theme.with_background(body, overlay=True)
