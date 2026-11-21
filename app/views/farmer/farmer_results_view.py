"""Farmer final: Display Ranked Buyers and Offer Details."""
import flet as ft
from app import theme
from app.services import mock_data


def _buyer_card(router, rank: int, b: dict) -> ft.Container:
    return ft.Container(
        bgcolor="#FFFFFF",
        border_radius=16,
        padding=ft.Padding.all(10),
        content=ft.Row(
            [
                ft.Container(
                    width=42,
                    height=42,
                    border_radius=21,
                    bgcolor=theme.ACCENT,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Text(str(rank), size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color="#FFFFFF"),
                ),
                ft.Column(
                    [
                        ft.Text(b["name"], size=12,
                                weight=ft.FontWeight.BOLD, color=theme.TEXT),
                        ft.Text(f"PHP {b['price']:.2f}/kg",
                                size=10, color=theme.ACCENT),
                        ft.Row([
                            ft.Icon(ft.Icons.LOCATION_ON, size=11,
                                    color=theme.TEXT_MUTED),
                            ft.Text(f"{b['distance_km']:.1f} km away",
                                    size=8, color=theme.TEXT_MUTED),
                            ft.Container(expand=True),
                            ft.Container(
                                bgcolor="#DDEACF",
                                border_radius=8,
                                padding=ft.Padding.symmetric(horizontal=6, vertical=2),
                                content=ft.Text(b["status"], size=7,
                                                color=theme.ACCENT),
                            ),
                        ], spacing=3),
                    ],
                    spacing=2,
                    expand=True,
                ),
            ],
            spacing=8,
        ),
        on_click=lambda e: (
            setattr(router.session, "selected_buyer", b),
            router.go("buyer_details"),
        ),
    )


def farmer_results_view(router) -> ft.Control:
    s = router.session
    buyers = mock_data.get_ranked_buyers(s)
    if not buyers:
        buyers = [
            {"name": "ABC Traders", "price": 23.50,
             "distance_km": 2.4, "status": "Verified", "age_days": 1},
        ]

    header = ft.Row([
        ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                      on_click=lambda e: router.back()),
        ft.Column([
            ft.Text("umAni", size=23, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
            ft.Text("Smarter Choices for Every Palay Harvest.",
                    size=8, italic=True, color="#FFFFFF"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
           spacing=0, expand=True),
        ft.Container(width=48),
    ])

    trophy = ft.Container(
        height=58,
        bgcolor="#F2CB62",
        border_radius=18,
        alignment=ft.Alignment.CENTER,
        content=ft.Row([
            ft.Icon(ft.Icons.EMOJI_EVENTS, color="#FFFFFF", size=34),
            ft.Column([
                ft.Text("Here are your top buyers!",
                        size=13, weight=ft.FontWeight.BOLD, color="#4A421D"),
                ft.Text("Based on your confirmed preferences.",
                        size=8, color="#6D6437"),
            ], spacing=1),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8),
    )

    list_card = ft.Container(
        bgcolor=ft.Colors.with_opacity(0.94, "#FFFFFF"),
        border_radius=24,
        padding=ft.Padding.all(12),
        content=ft.Column(
            [_buyer_card(router, i, b) for i, b in enumerate(buyers, start=1)],
            spacing=8,
        ),
    )

    content = ft.Column([
                header,
                ft.Container(height=12),
                trophy,
                ft.Container(height=10),
                list_card,
                ft.Container(expand=True),
                ft.OutlinedButton(
                    content="New Comparison",
                    on_click=lambda e: router.go("farmer_harvest"),
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
    ], spacing=8, scroll=ft.ScrollMode.AUTO, expand=True,
       horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    body = theme.role_page(content, theme.bottom_nav(router, active="results"))
    return theme.with_background(body, overlay=False)


def ranking_loading_view(router) -> ft.Control:
    content = ft.Column([
        ft.Row([
            ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                          on_click=lambda e: router.back()),
            ft.Column([
                ft.Text("umAni", size=23, weight=ft.FontWeight.BOLD,
                        color="#FFFFFF"),
                ft.Text("Smarter Choices for Every Palay Harvest.",
                        size=8, italic=True, color="#FFFFFF"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               spacing=0, expand=True),
            ft.Container(width=48),
        ]),
        ft.Container(expand=True),
        ft.Container(
            bgcolor=ft.Colors.with_opacity(0.94, "#FFFFFF"),
            width=306,
            border_radius=24,
            padding=ft.Padding.all(24),
            content=ft.Column([
                ft.Icon(ft.Icons.AUTO_AWESOME,
                        size=54, color=theme.ACCENT),
                ft.Text("Ranking Eligible Buyers",
                        size=17, weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=theme.TEXT),
                ft.ProgressBar(
                    value=None,
                    color=theme.ACCENT,
                    bgcolor="#E7EEDF",
                    height=8,
                    border_radius=4,
                ),
                ft.Text("Analyzing your preference using AHP",
                        size=9, color=theme.TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER),
                ft.Text("This will only take a moment.",
                        size=8, color=theme.TEXT_MUTED),
                ft.Button(
                    content="View Ranked Buyers",
                    on_click=lambda e: router.go("farmer_results"),
                    height=44,
                    style=ft.ButtonStyle(
                        bgcolor=theme.ACCENT,
                        color="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               spacing=12),
        ),
        ft.Container(expand=True),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=8, expand=True)
    body = theme.role_page(
        content,
        theme.bottom_nav(router, active="results"),
    )
    return theme.with_background(body, overlay=False)
