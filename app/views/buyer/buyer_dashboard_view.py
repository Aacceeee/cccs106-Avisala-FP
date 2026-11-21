import flet as ft
from app import theme
from app.views.buyer.buyer_components import (
    GREEN_TEXT,
    LIGHT_CARD,
    action_button,
    buyer_page,
    kv,
    light_card,
    offer,
    pill,
    portal_chip,
    profile,
    section_title,
    tab,
)


def buyer_dashboard_view(router) -> ft.Control:
    p, o = profile(router), offer(router)
    overview = light_card(ft.Row([
        ft.Container(
            content=ft.Icon(ft.Icons.IMAGE_OUTLINED, size=30, color="#C9C9C9"),
            width=60, height=60, bgcolor="#4A4A4A", border_radius=12,
            alignment=ft.Alignment.CENTER,
        ),
        ft.Column([
            ft.Text("Business Overview", size=10, weight=ft.FontWeight.BOLD,
                    color=theme.TEXT_MUTED),
            ft.Row([
                ft.Text(p["name"], size=15, weight=ft.FontWeight.BOLD,
                        color=GREEN_TEXT),
                pill("Verified Buyer", "#8DC76B", GREEN_TEXT,
                     ft.Icons.VERIFIED),
            ], spacing=6, wrap=True),
            ft.Text(f"{p['type']}  ·  {p['address']}", size=10,
                    color=theme.TEXT_MUTED),
            ft.Row([ft.TextButton(
                content=ft.Text("View Profile >", size=10,
                                weight=ft.FontWeight.BOLD, color=GREEN_TEXT),
                on_click=lambda e: tab(router, "buyer_profile"),
            )], alignment=ft.MainAxisAlignment.END),
        ], spacing=2, expand=True),
    ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.START))

    status = light_card(ft.Column([
        ft.Text("Offer Submission Status", size=12,
                weight=ft.FontWeight.BOLD, color=GREEN_TEXT),
        ft.Row([pill(o["status"], "#F5D98B", "#7A5600")]),
        ft.Text(f"Last Updated: {o['updated']}  ·  Visible to farmers once verified.",
                size=9, color=theme.TEXT_MUTED),
    ], spacing=6))

    qty = f"Up to {int(float(o['quantity'])):,} kg"
    current = ft.Container(
        content=ft.Column([
            ft.Text("Current Purchasing Offer", size=12,
                    weight=ft.FontWeight.BOLD, color=GREEN_TEXT),
            kv("Buying Price", f"₱ {float(o['price']):.2f} / kg",
               theme.ACCENT, bold_value=True),
            kv("Accepted Quantity", qty),
            kv("Payment Method", o["payment"]),
            kv("Requirements", o["requirements"]),
        ], spacing=4),
        padding=14,
        bgcolor=LIGHT_CARD,
        border=ft.Border.all(1, theme.ACCENT),
        border_radius=20,
        expand=True,
        alignment=ft.Alignment.TOP_LEFT,
    )

    return buyer_page(router, "dashboard", [
        portal_chip(),
        section_title(ft.Icons.GROUPS, "Buyer Dashboard",
                      "Manage your purchasing offers and business profile."),
        overview,
        status,
        current,
        action_button(
            "Manage / Update Offer",
            lambda e: tab(router, "buyer_offers"),
            ft.Icons.EDIT,
        ),
    ])
