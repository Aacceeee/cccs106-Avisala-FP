"""Farmer dashboard, styled after the Figma 'Hello, Mark!' frame."""
import flet as ft
from app import theme

BTN_GREEN = "#2C5E10"
GREEN_TEXT = "#1F3D1B"
FARMER_NAME = "Mark"   # TODO: replace with the logged-in farmer's first name


def _header() -> ft.Control:
    return ft.Column(
        [
            ft.Row(
                [theme.logo(52),
                 ft.Text("umAni", size=28, weight=ft.FontWeight.BOLD, color="#6DAF58")],
                spacing=4, vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Text("Smarter Choices for Every Palay Harvest.", size=10, italic=True,
                    weight=ft.FontWeight.BOLD, color="#FFFFFF"),
        ],
        spacing=2,
    )


def _greeting() -> ft.Control:
    return ft.Container(
        padding=ft.Padding.symmetric(horizontal=16, vertical=12),
        bgcolor=ft.Colors.with_opacity(0.28, "#000000"),
        border_radius=20,
        content=ft.Column(
            [
                ft.Text(
                    spans=[ft.TextSpan("Hello, ", ft.TextStyle(weight=ft.FontWeight.W_300)),
                           ft.TextSpan(f"{FARMER_NAME}!", ft.TextStyle(weight=ft.FontWeight.BOLD))],
                    size=22, color="#FFFFFF"),
                ft.Text("Let's find the best buyer for your harvest.", size=11, color="#FFFFFF"),
            ],
            spacing=2,
        ),
    )


def _start_button(router) -> ft.Control:
    return ft.Row([ft.Button(
        content=ft.Row(
            [ft.Icon(ft.Icons.BALANCE, size=20, color="#FFFFFF"),
             ft.Text("Start Comparing", size=15, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
             ft.Icon(ft.Icons.ARROW_FORWARD, size=20, color="#FFFFFF")],
            alignment=ft.MainAxisAlignment.CENTER, spacing=10,
        ),
        on_click=lambda e: router.go("farmer_harvest"),
        height=50, expand=True,
        style=ft.ButtonStyle(bgcolor=BTN_GREEN, side=ft.BorderSide(1.5, "#FFFFFF"),
                             shape=ft.RoundedRectangleBorder(radius=26)),
    )])


def _recent_card(router) -> ft.Control:
    # TODO: when comparison history exists, list the latest 3 here instead of the empty state.
    empty_state = ft.Container(
        width=float("inf"),
        padding=ft.Padding.symmetric(horizontal=16, vertical=18),
        bgcolor=ft.Colors.with_opacity(0.92, "#F1F1EA"),
        border_radius=22,
        content=ft.Column(
            [
                ft.Text("No comparisons yet", size=13, weight=ft.FontWeight.BOLD,
                        color=GREEN_TEXT),
                ft.Text("Your previous buyer comparisons will appear here once you start comparing.",
                        size=10, color="#3F4F3F", text_align=ft.TextAlign.CENTER),
                ft.TextButton(
                    content=ft.Text("Start your first comparison", size=11,
                                    weight=ft.FontWeight.BOLD, color=GREEN_TEXT,
                                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)),
                    on_click=lambda e: router.go("farmer_harvest"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4,
        ),
    )
    return ft.Container(
        padding=ft.Padding.all(12),
        bgcolor=ft.Colors.with_opacity(0.30, "#0B1A0B"),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.2, "#FFFFFF")),
        border_radius=26,
        content=ft.Column(
            [
                ft.Row(
                    [ft.Row([ft.Icon(ft.Icons.HISTORY, size=18, color="#FFFFFF"),
                             ft.Text("Recent Comparisons", size=12, weight=ft.FontWeight.BOLD,
                                     color="#FFFFFF")], spacing=6),
                     ft.TextButton(
                         content=ft.Text("View All >", size=10, color="#FFFFFF"),
                         on_click=lambda e: router.go("comparison_history"))],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                empty_state,
            ],
            spacing=6,
        ),
    )


def farmer_home_view(router) -> ft.Control:
    body = theme.role_page(
        ft.Column(
            [_header(), ft.Container(height=6), _greeting(),
             ft.Container(height=4), _start_button(router),
             ft.Container(height=4), _recent_card(router)],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        ),
        theme.bottom_nav(router, active="home"),
    )
    return theme.with_background(body, overlay=False)
