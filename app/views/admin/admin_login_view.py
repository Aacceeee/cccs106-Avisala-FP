import flet as ft
from app import theme


def admin_login_view(router) -> ft.Control:
    username = ft.TextField(
        hint_text="Admin Email or Username",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        height=44,
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border(theme.ACCENT, 22),
    )
    password = ft.TextField(
        hint_text="Password",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        height=44,
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border(theme.ACCENT, 22),
    )

    def sign_in(e):
        account = (username.value or "").strip().lower()
        if (account in ("admin", "admin@umani.com")
                and (password.value or "") == "admin123"):
            router.go("admin_dashboard")
            return
        password.error = "Invalid admin credentials"
        router.page.update()

    content = ft.Column([
        ft.Container(height=36),
        ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                      on_click=lambda e: router.back()),
        ft.Container(expand=True),
        theme.logo(82),
        ft.Container(height=8),
        ft.Text("Admin Portal", size=21, weight=ft.FontWeight.BOLD,
                color="#FFFFFF"),
        ft.Text("Restricted Administrator Access", size=9, color="#FFFFFF"),
        ft.Container(height=12),
        ft.Container(
            width=306,
            bgcolor=theme.CARD,
            border_radius=24,
            padding=ft.Padding.all(18),
            content=ft.Column([
                username,
                password,
                ft.Container(height=4),
                ft.OutlinedButton(
                    content="Sign in",
                    on_click=sign_in,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        bgcolor=theme.ACCENT,
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
            ], spacing=10),
        ),
        ft.Container(expand=True),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
    return theme.with_background(
        ft.Container(content=content, expand=True),
        overlay=True,
    )
