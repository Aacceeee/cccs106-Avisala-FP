import flet as ft
from app import theme
from app.views.admin.admin_components import admin_header, admin_nav


def admin_dashboard_view(router) -> ft.Control:
    def metric(title, value, icon):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=16,
            padding=ft.Padding.all(12),
            expand=True,
            content=ft.Column([
                ft.Row([
                    ft.Icon(icon, size=16, color=theme.ACCENT),
                    ft.Text(title, size=8, color=theme.TEXT_MUTED, expand=True),
                ], spacing=4),
                ft.Text(str(value), size=20, weight=ft.FontWeight.BOLD,
                        color=theme.TEXT),
            ], spacing=3),
        )

    content = ft.Column([
                ft.Container(height=8),
                admin_header(),
                ft.Container(height=8),
                ft.Row([
                    ft.Icon(ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                            size=18, color="#FFFFFF"),
                    ft.Text("Admin Portal", size=18,
                            weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                    ft.Container(
                        bgcolor="#FFFFFF",
                        border_radius=12,
                        padding=ft.Padding.symmetric(horizontal=8, vertical=3),
                        content=ft.Icon(ft.Icons.SETTINGS_OUTLINED,
                                        size=16, color=theme.ACCENT),
                        on_click=lambda e: router.go("admin_settings"),
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text("System Overview", size=9, color="#FFFFFF"),
                ft.Row([
                    metric("Registered Buyers", 28, ft.Icons.GROUPS_OUTLINED),
                    metric("Pending Verification", 3, ft.Icons.PENDING_ACTIONS),
                ], spacing=8),
                ft.Row([
                    metric("Active Verified Offers", 24,
                           ft.Icons.LOCAL_OFFER_OUTLINED),
                    metric("Inactive Buyers", 1, ft.Icons.PERSON_OFF_OUTLINED),
                ], spacing=8),
                ft.Text("Quick Actions", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.OutlinedButton(
                    content="Review Pending Offers",
                    on_click=lambda e: router.go("admin_offers"),
                    width=250,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        bgcolor=ft.Colors.with_opacity(0.10, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.OutlinedButton(
                    content="Register New Buyer Account",
                    on_click=lambda e: router.go("admin_buyers"),
                    width=250,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        bgcolor=ft.Colors.with_opacity(0.10, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=7, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Dashboard"))
    return theme.with_background(body, overlay=False)
