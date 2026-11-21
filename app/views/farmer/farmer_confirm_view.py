"""Edit the original preference message and update extracted criteria."""
import flet as ft
from app import theme
from app.services.mock_data import extract_preferences


def farmer_confirm_view(router) -> ft.Control:
    s = router.session
    message = ft.TextField(
        multiline=True,
        min_lines=5,
        value=s.pref_text,
        hint_text="Type your preferences here...",
        bgcolor="#FFFFFF",
        border_radius=18,
        border=theme.text_field_border("#D9E1D5", 18),
    )

    def update(e):
        s.pref_text = message.value or ""
        s.preferences = extract_preferences(s.pref_text, [])
        router.go("farmer_preferences")

    card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.94, "#FFFFFF"),
        border_radius=24,
        padding=ft.Padding.all(16),
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.EDIT_OUTLINED, size=18, color=theme.ACCENT),
                ft.Text("Edit Your Message", size=15,
                        weight=ft.FontWeight.BOLD, color=theme.TEXT),
            ], alignment=ft.MainAxisAlignment.CENTER),
            message,
            ft.Text("The AI will extract your preferences again.",
                    size=9, color=theme.TEXT_MUTED),
        ], spacing=10),
    )

    content = ft.Column([
                ft.Row([
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                                  on_click=lambda e: router.back()),
                    ft.Column([
                        ft.Text("umAni", size=23, weight=ft.FontWeight.BOLD,
                                color="#FFFFFF"),
                        ft.Text("Smarter Choices for Every Palay Harvest.",
                                size=8, italic=True, color="#FFFFFF"),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0, expand=True),
                    ft.Container(width=48),
                ]),
                ft.Container(expand=True),
                card,
                ft.Container(height=10),
                ft.OutlinedButton(
                    content="Update Preferences",
                    on_click=update,
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Button(
                    content="Cancel",
                    on_click=lambda e: router.go("farmer_preferences"),
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        bgcolor="#FFFFFF",
                        color=theme.ACCENT,
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Container(expand=True),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, theme.bottom_nav(router, active="home"))
    return theme.with_background(body, overlay=False)
