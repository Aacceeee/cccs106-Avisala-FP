import flet as ft
from app import theme
from app.views.admin.admin_components import admin_header, admin_nav


def admin_settings_view(router) -> ft.Control:
    def row(icon, title, subtitle):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=14,
            padding=ft.Padding.all(11),
            content=ft.Row([
                ft.Container(
                    width=30, height=30, border_radius=15,
                    bgcolor="#E9F0DF", alignment=ft.Alignment.CENTER,
                    content=ft.Icon(icon, size=17, color=theme.ACCENT),
                ),
                ft.Column([
                    ft.Text(title, size=10, weight=ft.FontWeight.BOLD,
                            color=theme.TEXT),
                    ft.Text(subtitle, size=8, color=theme.TEXT_MUTED),
                ], spacing=1, expand=True),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=16,
                        color=theme.TEXT_MUTED),
            ], spacing=8),
        )

    content = ft.Column([
                ft.Row([
                    ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                                  on_click=lambda e: router.back()),
                    ft.Container(expand=True),
                ]),
                ft.Row([
                    ft.Icon(ft.Icons.SETTINGS_OUTLINED,
                            size=18, color="#FFFFFF"),
                    ft.Text("Settings", size=18,
                            weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text("Manage your administrator account.",
                        size=8, color="#FFFFFF"),
                ft.Text("Account Info", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                row(ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                    "System Administrator", "Administrator account"),
                ft.Text("Account", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                row(ft.Icons.PERSON_OUTLINE,
                    "Account Information", "View administrator details"),
                row(ft.Icons.LOCK_OUTLINE,
                    "Change Password", "Update account password"),
                ft.Text("Support & Information", size=10,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                row(ft.Icons.INFO_OUTLINE,
                    "About umAni", "Application information and version"),
                ft.OutlinedButton(
                    content="Log Out",
                    on_click=lambda e: router.go("welcome"),
                    width=220,
                    height=44,
                    style=ft.ButtonStyle(
                        bgcolor="#FFFFFF",
                        color=theme.ERROR,
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.Text("umAni Version 1.0.0", size=8, color="#FFFFFF"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=7, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Dashboard"))
    return theme.with_background(body, overlay=False)
