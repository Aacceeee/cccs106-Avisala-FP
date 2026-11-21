"""Empty and populated comparison history screens."""
import flet as ft
from app import theme


def comparison_history_view(router) -> ft.Control:
    header = ft.Row(
        [
            ft.IconButton(
                ft.Icons.ARROW_BACK,
                icon_color="#FFFFFF",
                on_click=lambda e: router.back(),
            ),
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
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    title = ft.Text(
        "Comparison History",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="#FFFFFF",
    )

    empty_card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.94, "#FFFFFF"),
        border_radius=24,
        padding=ft.Padding.all(18),
        content=ft.Column(
            [
                ft.Container(
                    width=132,
                    height=132,
                    border_radius=66,
                    bgcolor=ft.Colors.with_opacity(0.10, "#557A47"),
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.HISTORY_TOGGLE_OFF,
                                    size=76, color=theme.ACCENT),
                ),
                ft.Text("No comparisons history yet",
                        size=14, weight=ft.FontWeight.BOLD,
                        color=theme.TEXT),
                ft.Text(
                    "Your previous buyer comparisons will appear here once you start finding the best palay options.",
                    size=9,
                    color=theme.TEXT_MUTED,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Button(
                    content="Start Comparing",
                    on_click=lambda e: router.go("farmer_harvest"),
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        bgcolor=theme.ACCENT,
                        color="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
    )

    body = ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        header,
                        ft.Container(height=8),
                        ft.Row([
                            ft.Icon(ft.Icons.HISTORY, color="#FFFFFF", size=18),
                            title,
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("Your past buyer comparisons",
                                size=9, color="#FFFFFF",
                                text_align=ft.TextAlign.CENTER),
                        ft.Container(height=24),
                        empty_card,
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                    expand=True,
                ),
                padding=ft.Padding.symmetric(horizontal=18),
                expand=True,
            ),
            theme.bottom_nav(router),
        ],
        spacing=0,
        expand=True,
    )
    return theme.with_background(body, overlay=True)
