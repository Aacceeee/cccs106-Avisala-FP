"""Splash screen, styled after the Figma 'Get Started' frame.

Assets (in /assets, all optional - fallbacks are provided):
    splash_bg.jpg  sunset rice-field photo   (theme.SPLASH_BG_IMAGE)
    logo.png       umAni logo                (theme.LOGO_IMAGE)
"""
import flet as ft
from app import theme

BTN_GREEN = "#2C5E10"       # same dark green as the Sign In button
CHECK_GREEN = "#2E9B3A"
SHOW_WORDMARK = True        # set False if logo.png already contains the "umAni" text

BENEFITS = ["Compare prices", "Check distance", "See payment terms", "Make better decision"]


def _benefit(text: str) -> ft.Control:
    return ft.Row(
        [
            ft.Container(
                content=ft.Icon(ft.Icons.CHECK, size=11, color="#FFFFFF"),
                width=15, height=15, bgcolor=CHECK_GREEN, border_radius=4,
                alignment=ft.Alignment.CENTER,
            ),
            ft.Text(text, size=12, color="#FFFFFF"),
        ],
        spacing=8,
        tight=True,
    )


def splash_view(router) -> ft.Control:
    header = [theme.logo(84)]
    if SHOW_WORDMARK:
        header.append(ft.Text("umAni", size=30, weight=ft.FontWeight.BOLD, color="#6DAF58"))
    header.append(ft.Text("Smarter Choices for Every Palay Harvest.", size=11,
                          italic=True, color="#FFFFFF", text_align=ft.TextAlign.CENTER))

    panel = ft.Container(
        expand=True,
        margin=ft.Margin.only(left=18, right=18, top=24, bottom=18),
        padding=ft.Padding.symmetric(horizontal=24, vertical=28),
        bgcolor=ft.Colors.with_opacity(0.22, "#0B1A0B"),
        blur=ft.Blur(12, 12),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.25, "#FFFFFF")),
        border_radius=40,
        content=ft.Column(
            [
                *header,
                ft.Container(expand=1),
                ft.Text("Find and compare\npalay buyers based\non what matters\nmost to you.",
                        size=20, weight=ft.FontWeight.W_300, color="#FFFFFF",
                        text_align=ft.TextAlign.CENTER),
                ft.Container(expand=1),
                ft.Column([_benefit(b) for b in BENEFITS], spacing=8, tight=True),
                ft.Container(height=14),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
            expand=True,
        ),
    )

    button = ft.Container(
        margin=ft.Margin.only(left=28, right=28, bottom=30),
        content=ft.Button(
            content=ft.Text("Get Started", size=15, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
            on_click=lambda e: router.go("welcome"),
            height=50,
            expand=True,
            style=ft.ButtonStyle(
                bgcolor=BTN_GREEN,
                side=ft.BorderSide(1.5, "#FFFFFF"),
                shape=ft.RoundedRectangleBorder(radius=26),
            ),
        ),
    )
    # Button is a Row child so it stretches to the container width.
    button.content = ft.Row([button.content])

    body = ft.SafeArea(content=ft.Column([panel, button], expand=True), expand=True)
    return theme.with_background(
        body,
        overlay=False,
        image_name=theme.SPLASH_BG_IMAGE,
        wrap_glass=False,
    )
