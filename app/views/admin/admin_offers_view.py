import flet as ft
from app import theme
from app.views.admin.admin_components import admin_header, admin_nav


def admin_offers_view(router) -> ft.Control:
    search = ft.TextField(
        hint_text="Search by buyer name...",
        prefix_icon=ft.Icons.SEARCH,
        height=42,
        bgcolor="#FFFFFF",
        border_radius=20,
        border=theme.text_field_border("#A9C99B", 20),
        expand=True,
    )

    def offer_row(name, type_name, price, quantity, status, status_color):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=14,
            padding=ft.Padding.all(8),
            content=ft.Row([
                ft.Container(
                    width=44, height=44, border_radius=22,
                    bgcolor="#C7D2AA", alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.STORE_OUTLINED,
                                    size=24, color=theme.ACCENT),
                ),
                ft.Column([
                    ft.Text(name, size=10, weight=ft.FontWeight.BOLD,
                            color=theme.TEXT),
                    ft.Text(type_name, size=7, color=theme.TEXT_MUTED),
                    ft.Row([
                        ft.Column([
                            ft.Text("Buying Price", size=7, color=theme.TEXT_MUTED),
                            ft.Text(price, size=9, weight=ft.FontWeight.BOLD),
                        ], spacing=0, expand=True),
                        ft.Column([
                            ft.Text("Quantity", size=7, color=theme.TEXT_MUTED),
                            ft.Text(quantity, size=9, weight=ft.FontWeight.BOLD),
                        ], spacing=0, expand=True),
                    ], spacing=4),
                ], spacing=2, expand=True),
                ft.Text(status, size=7, color=status_color),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=14,
                        color=theme.TEXT_MUTED),
            ], spacing=7),
            on_click=lambda e: router.go("admin_offer_detail"),
        )

    content = ft.Column([
                admin_header(),
                ft.Text("Offer Management", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("View and manage all buyer offers.",
                        size=8, color="#FFFFFF"),
                ft.Row([
                    search,
                    ft.OutlinedButton(
                        content="Filter",
                        height=42,
                        style=ft.ButtonStyle(
                            bgcolor="#FFFFFF",
                            color=theme.TEXT,
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    ),
                ], spacing=6),
                offer_row("Piii Rice Mill", "Rice Mill", "P18.50/kg",
                          "500 kg", "Verified", theme.ACCENT),
                offer_row("ABC Rice Trading", "Palay Trader", "P17.80/kg",
                          "1,000 kg", "Verified", theme.ACCENT),
                offer_row("Farmers Cooperative", "Cooperative", "P17.20/kg",
                          "800 kg", "Needs Confirmation", "#A97816"),
                offer_row("CamSur Rice Mill", "Rice Mill", "P16.50/kg",
                          "600 kg", "Inactive", "#7A8176"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=6, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Offers"))
    return theme.with_background(body, overlay=False)


def admin_offer_detail_view(router) -> ft.Control:
    card = ft.Container(
        bgcolor="#FFFFFF",
        border_radius=20,
        padding=ft.Padding.all(16),
        content=ft.Column([
            ft.Text("ABC Rice Trading", size=16,
                    weight=ft.FontWeight.BOLD, color=theme.TEXT),
            ft.Text("Palay Trader", size=9, color=theme.TEXT_MUTED),
            ft.Text("Buying Price: P18.50/kg", size=9, color=theme.TEXT),
            ft.Text("Accepted Quantity: 500 kg", size=9, color=theme.TEXT),
            ft.Text("Payment Method: Cash on Delivery",
                    size=9, color=theme.TEXT),
            ft.Row([
                ft.OutlinedButton(
                    content="Return for Correction",
                    on_click=lambda e: router.go("admin_offers"),
                    expand=True,
                ),
                ft.Button(
                    content="Approve Offer",
                    on_click=lambda e: router.go("admin_offers"),
                    expand=True,
                    style=ft.ButtonStyle(
                        bgcolor=theme.ACCENT,
                        color="#FFFFFF",
                    ),
                ),
            ], spacing=8),
        ], spacing=8),
    )
    content = ft.Column([
                admin_header(),
                ft.Text("Buyer Offer Details", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                card,
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Offers"))
    return theme.with_background(body, overlay=False)


def admin_offer_management_view(router) -> ft.Control:
    return admin_offers_view(router)
