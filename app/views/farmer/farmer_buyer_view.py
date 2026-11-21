"""Buyer details, contact, and settings screens."""
import flet as ft
from app import theme


def _header(router) -> ft.Row:
    return ft.Row([
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


def buyer_details_view(router) -> ft.Control:
    b = getattr(router.session, "selected_buyer", None) or {
        "name": "ABC Traders",
        "price": 23.50,
        "distance_km": 2.4,
        "status": "Verified",
    }
    card = ft.Container(
        bgcolor="#FFFFFF",
        border_radius=24,
        padding=ft.Padding.all(16),
        content=ft.Column([
            ft.Row([
                ft.Container(
                    width=60, height=60, border_radius=12,
                    bgcolor="#BFC9A8", alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.STORE, color=theme.ACCENT, size=38),
                ),
                ft.Column([
                    ft.Text(b["name"], size=16, weight=ft.FontWeight.BOLD,
                            color=theme.TEXT),
                    ft.Container(
                        bgcolor="#DDEACF", border_radius=8,
                        padding=ft.Padding.symmetric(horizontal=8, vertical=3),
                        content=ft.Text("Verified Buyer", size=8, color=theme.ACCENT),
                    ),
                ], spacing=4, expand=True),
            ], spacing=10),
            ft.Container(
                bgcolor="#ECF1E7", border_radius=12,
                padding=ft.Padding.all(10),
                content=ft.Column([
                    ft.Text("Offer Details", size=10,
                            weight=ft.FontWeight.BOLD, color=theme.TEXT),
                    ft.Row([
                        ft.Column([
                            ft.Text("Offered Price", size=8, color=theme.TEXT_MUTED),
                            ft.Text(f"PHP {b['price']:.2f}/kg", size=15,
                                    weight=ft.FontWeight.BOLD, color=theme.ACCENT),
                        ], expand=True),
                        ft.Column([
                            ft.Text("Accepted Quantity", size=8, color=theme.TEXT_MUTED),
                            ft.Text("Up to 2,000 kg", size=11,
                                    weight=ft.FontWeight.BOLD, color=theme.TEXT),
                        ], expand=True),
                    ]),
                ], spacing=6),
            ),
            ft.Container(
                bgcolor="#ECF1E7", border_radius=12,
                padding=ft.Padding.all(10),
                content=ft.Column([
                    ft.Text("Payment Condition", size=10,
                            weight=ft.FontWeight.BOLD, color=theme.TEXT),
                    ft.Text("Prefer Immediate", size=11,
                            weight=ft.FontWeight.BOLD, color=theme.ACCENT),
                ], spacing=4),
            ),
            ft.Row([
                ft.Icon(ft.Icons.LOCATION_ON, color=theme.ACCENT, size=18),
                ft.Column([
                    ft.Text("Distance", size=8, color=theme.TEXT_MUTED),
                    ft.Text(f"{b['distance_km']:.1f} km away", size=11,
                            weight=ft.FontWeight.BOLD, color=theme.TEXT),
                ], spacing=1, expand=True),
                ft.Icon(ft.Icons.DIRECTIONS_CAR_OUTLINED,
                        color=theme.ACCENT, size=22),
            ]),
            ft.Container(
                bgcolor="#ECF1E7", border_radius=12,
                padding=ft.Padding.all(10),
                content=ft.Row([
                    ft.Icon(ft.Icons.CIRCLE, size=10, color="#5A8B45"),
                    ft.Column([
                        ft.Text("Offer Status", size=8, color=theme.TEXT_MUTED),
                        ft.Text("Active", size=11,
                                weight=ft.FontWeight.BOLD, color=theme.TEXT),
                    ], spacing=1),
                ]),
            ),
        ], spacing=8),
    )

    content = ft.Column([
                _header(router),
                ft.Container(height=10),
                ft.Text("Buyer Details", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("View verified information about this buyer.",
                        size=9, color="#FFFFFF"),
                ft.Container(height=8),
                card,
                ft.Container(height=8),
                ft.OutlinedButton(
                    content="Contact Buyer",
                    on_click=lambda e: router.go("buyer_contact"),
                    width=220, height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF", side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=6, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, theme.bottom_nav(router, active="results"))
    return theme.with_background(body, overlay=False)


def buyer_contact_view(router) -> ft.Control:
    card = ft.Container(
        bgcolor="#FFFFFF", border_radius=24,
        padding=ft.Padding.all(18),
        content=ft.Column([
            ft.Container(
                width=74, height=74, border_radius=37,
                bgcolor="#ECF1E7", alignment=ft.Alignment.CENTER,
                content=ft.Icon(ft.Icons.PHONE_IN_TALK,
                                size=38, color=theme.ACCENT),
            ),
            ft.Text("Contact ABC Traders", size=16,
                    weight=ft.FontWeight.BOLD, color=theme.TEXT),
            ft.Container(
                bgcolor="#ECF1E7", border_radius=12,
                padding=ft.Padding.symmetric(horizontal=12, vertical=10),
                content=ft.Text("09123456789", size=20,
                                weight=ft.FontWeight.BOLD,
                                color=theme.TEXT, text_align=ft.TextAlign.CENTER),
            ),
            ft.Text("Registered buyer contact number",
                    size=8, color=theme.TEXT_MUTED),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
    )
    content = ft.Column([
                _header(router),
                ft.Container(expand=True),
                ft.Icon(ft.Icons.PHONE, size=42, color="#FFFFFF"),
                ft.Text("Contact ABC Traders", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Container(height=8),
                card,
                ft.Container(height=10),
                ft.Row([
                    ft.OutlinedButton(
                        content="Cancel", on_click=lambda e: router.back(),
                        expand=True, height=44,
                        style=ft.ButtonStyle(
                            color="#FFFFFF", side=ft.BorderSide(1, "#FFFFFF"),
                            shape=ft.RoundedRectangleBorder(radius=22),
                        ),
                    ),
                    ft.Button(
                        content="Call", on_click=lambda e: None,
                        expand=True, height=44,
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF", color=theme.ACCENT,
                            shape=ft.RoundedRectangleBorder(radius=22),
                        ),
                    ),
                ], spacing=10),
                ft.Text("You can call the buyer to discuss the offer.",
                        size=8, color="#FFFFFF"),
                ft.Container(expand=True),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, theme.bottom_nav(router, active="results"))
    return theme.with_background(body, overlay=False)


def settings_view(router) -> ft.Control:
    def setting(icon, title, subtitle):
        return ft.Container(
            bgcolor="#FFFFFF", border_radius=14,
            padding=ft.Padding.all(11),
            content=ft.Row([
                ft.Icon(icon, size=20, color=theme.ACCENT),
                ft.Column([
                    ft.Text(title, size=11, weight=ft.FontWeight.BOLD,
                            color=theme.TEXT),
                    ft.Text(subtitle, size=8, color=theme.TEXT_MUTED),
                ], spacing=1, expand=True),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18,
                        color=theme.TEXT_MUTED),
            ], spacing=8),
        )

    content = ft.Column([
                _header(router),
                ft.Text("Settings", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("Manage your app preferences and account settings.",
                        size=9, color="#FFFFFF"),
                ft.Container(height=4),
                ft.Text("App Preferences", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                setting(ft.Icons.LANGUAGE, "Language",
                        "Manage app language: English"),
                setting(ft.Icons.NOTIFICATIONS_OUTLINED, "Notifications",
                        "Manage app notifications"),
                ft.Text("Account", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                setting(ft.Icons.LOCK_OUTLINE, "Change Password",
                        "Update your account password"),
                ft.Text("Support & Information", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                setting(ft.Icons.HELP_OUTLINE, "Help & Support",
                        "Get help or contact support"),
                setting(ft.Icons.INFO_OUTLINE, "About umAni",
                        "Learn more about umAni"),
                ft.OutlinedButton(
                    content="Log Out",
                    on_click=lambda e: router.go("welcome"),
                    width=220, height=44,
                    style=ft.ButtonStyle(
                        color=theme.ERROR, side=ft.BorderSide(1, "#FFFFFF"),
                        bgcolor="#FFFFFF",
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Text("umAni version 1.0.0", size=8, color="#FFFFFF"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=6, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, theme.bottom_nav(router, active="profile"))
    return theme.with_background(body, overlay=False)
