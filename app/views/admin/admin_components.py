import flet as ft
from app import theme


def admin_header() -> ft.Row:
    return ft.Row([
        theme.logo(46),
        ft.Column([
            ft.Text("umAni", size=23, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
            ft.Text("Smarter Choices for Every Palay Harvest.",
                    size=8, italic=True, color="#FFFFFF"),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
           spacing=0, expand=True),
        ft.Container(width=46),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)


ADMIN_NAV = [
    ("dashboard", "Dashboard", ft.Icons.DASHBOARD, "admin_dashboard"),
    ("buyers", "Buyers", ft.Icons.GROUPS, "admin_buyers"),
    ("offers", "Offers", ft.Icons.LOCAL_OFFER, "admin_offers"),
]


def admin_nav(router, active: str) -> ft.Container:
    """`active` may be a label ("Dashboard") or a key ("dashboard")."""
    return theme.bottom_nav(router, active=active.lower(), items=ADMIN_NAV)


def detail_placeholder(label, value):
    return ft.Row([
        ft.Text(label, size=9, color=theme.TEXT_MUTED, expand=True),
        ft.Text(value, size=9, weight=ft.FontWeight.BOLD, color=theme.TEXT),
    ])
