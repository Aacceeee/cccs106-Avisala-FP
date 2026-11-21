import flet as ft
from app import theme
from app.views.buyer.buyer_components import (
    GREEN_TEXT,
    action_button,
    buyer_page,
    input,
    pill,
    profile,
    section_title,
    white_button,
)


def avatar_header(title: str) -> ft.Control:
    return ft.Row([
        ft.Container(
            content=ft.Icon(ft.Icons.PERSON, size=36, color=theme.ACCENT),
            width=64,
            height=64,
            border_radius=32,
            bgcolor="#BFC9A8",
            alignment=ft.Alignment.CENTER,
        ),
        ft.Column([
            ft.Text(title, size=15, weight=ft.FontWeight.BOLD,
                    color=GREEN_TEXT),
            pill("Verified Buyer", "#8DC76B", GREEN_TEXT, ft.Icons.VERIFIED),
        ], spacing=5, expand=True),
    ], spacing=12)


def buyer_profile_view(router) -> ft.Control:
    p = profile(router)

    def row(label, value):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=12,
            border=ft.Border.all(1, theme.ACCENT),
            padding=ft.Padding.symmetric(horizontal=12, vertical=8),
            content=ft.Column([
                ft.Text(label, size=9, color=theme.TEXT_MUTED),
                ft.Text(value, size=12, weight=ft.FontWeight.BOLD,
                        color=GREEN_TEXT),
            ], spacing=1),
            expand=True,
        )

    card = ft.Container(
        content=ft.Column([
            avatar_header("Buyer Profile"),
            row("Business Details", p["name"]),
            row("Business Type", p["type"]),
            row("Address / Location", p["address"]),
            row("Contact Information", p["phone"]),
            row("Email Address", p["email"]),
        ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
        padding=14,
        bgcolor="#F5F6F1",
        border=ft.Border.all(1, theme.ACCENT),
        border_radius=20,
        expand=True,
    )

    return buyer_page(router, "profile", [
        section_title(ft.Icons.PERSON, "Buyer Profile",
                      "View and confirm your profile information."),
        card,
        action_button(
            "Edit Profile",
            lambda e: router.go("buyer_profile_edit"),
            ft.Icons.EDIT,
        ),
        white_button("Log Out", lambda e: router.go("welcome"),
                     color=theme.ERROR),
    ])


def buyer_profile_edit_view(router) -> ft.Control:
    p = profile(router)
    fields = {
        "name": input(label="Business Details", value=p["name"],
                      prefix_icon=ft.Icons.STORE_OUTLINED, height=48),
        "type": input(label="Business Type", value=p["type"],
                      prefix_icon=ft.Icons.CATEGORY_OUTLINED, height=48),
        "address": input(label="Address / Location", value=p["address"],
                         prefix_icon=ft.Icons.LOCATION_ON_OUTLINED, height=48),
        "phone": input(label="Contact Information", value=p["phone"],
                       prefix_icon=ft.Icons.PHONE_OUTLINED, height=48),
        "email": input(label="Email Address", value=p["email"],
                       prefix_icon=ft.Icons.EMAIL_OUTLINED, height=48),
    }

    def save(e):
        for key, field in fields.items():
            setattr(router.session, f"buyer_{key}",
                    (field.value or "").strip())
        router.back()

    card = ft.Container(
        content=ft.Column([
            avatar_header("Edit Buyer Profile"),
            *fields.values(),
        ], spacing=8, horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
        padding=14,
        bgcolor="#F5F6F1",
        border=ft.Border.all(1, theme.ACCENT),
        border_radius=20,
        expand=True,
    )

    return buyer_page(router, "profile", [
        section_title(ft.Icons.EDIT, "Edit Buyer Profile",
                      "Update your business information."),
        card,
        action_button("Save Profile Changes", save, width=250),
        white_button("Cancel", lambda e: router.back()),
    ], back=True)
