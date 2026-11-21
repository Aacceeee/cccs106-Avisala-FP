"""Review preferences extracted from the farmer's message."""
import flet as ft
from app import theme


def farmer_preferences_view(router) -> ft.Control:
    s = router.session
    preference_items = [
        ("Offered Price", "Prioritize buyers offering better prices."),
        ("Payment Conditions", "Prefer immediate or convenient payment."),
        ("Geographic Distance", "Prefer buyers close to your location."),
    ]

    def criterion(title, description):
        return ft.Container(
            bgcolor="#F1F4ED",
            border_radius=14,
            padding=ft.Padding.all(10),
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.CIRCLE, size=8, color=theme.ACCENT),
                    ft.Text(title, size=11, weight=ft.FontWeight.BOLD, color=theme.TEXT),
                ], spacing=6),
                ft.Text(description, size=8, color=theme.TEXT_MUTED),
            ], spacing=2),
        )

    card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.94, "#FFFFFF"),
        border_radius=24,
        padding=ft.Padding.all(16),
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.AUTO_AWESOME, size=18, color=theme.ACCENT),
                ft.Text("Review Your Preferences", size=15,
                        weight=ft.FontWeight.BOLD, color=theme.TEXT),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Please confirm the criteria extracted from your message.",
                    size=9, color=theme.TEXT_MUTED,
                    text_align=ft.TextAlign.CENTER),
            ft.Container(height=4),
            *[criterion(title, description) for title, description in preference_items],
            ft.Container(height=4),
            ft.Row([
                ft.Icon(ft.Icons.INFO_OUTLINE, size=16, color="#FFFFFF"),
                ft.Container(
                    bgcolor=theme.ACCENT,
                    border_radius=10,
                    padding=ft.Padding.all(8),
                    expand=True,
                    content=ft.Text(
                        "These preferences will be used by umAni to rank and compare buyers.",
                        size=8, color="#FFFFFF",
                    ),
                ),
            ], spacing=8),
        ], spacing=8),
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
                    content="Confirm Preferences",
                    on_click=lambda e: router.go("ranking_loading"),
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Button(
                    content="Edit Message",
                    on_click=lambda e: router.go("farmer_confirm"),
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
