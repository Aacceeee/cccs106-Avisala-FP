import flet as ft
from app import theme
from app.views.admin.admin_components import admin_header, admin_nav


def admin_buyers_view(router) -> ft.Control:
    search = ft.TextField(
        hint_text="Search buyer by business name...",
        prefix_icon=ft.Icons.SEARCH,
        height=44,
        bgcolor="#FFFFFF",
        border_radius=22,
        border=theme.text_field_border("#A9C99B", 22),
    )

    def buyer_card(name, type_name, status, offer_status):
        active = status == "Active"
        status_color = theme.ACCENT if active else "#737D6E"
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=16,
            padding=ft.Padding.all(10),
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        width=44, height=44, border_radius=10,
                        bgcolor="#C7D2AA", alignment=ft.Alignment.CENTER,
                        content=ft.Icon(ft.Icons.STORE_OUTLINED,
                                        size=26, color=theme.ACCENT),
                    ),
                    ft.Column([
                        ft.Text(name, size=12, weight=ft.FontWeight.BOLD,
                                color=theme.TEXT),
                        ft.Text(type_name, size=8, color=theme.TEXT_MUTED),
                    ], spacing=2, expand=True),
                    ft.Container(
                        bgcolor="#DDEACF" if active else "#DFE3DC",
                        border_radius=10,
                        padding=ft.Padding.symmetric(horizontal=7, vertical=3),
                        content=ft.Text(status, size=7, color=status_color),
                    ),
                ], spacing=8),
                ft.Row([
                    ft.Icon(ft.Icons.SHIELD_OUTLINED, size=14, color=theme.ACCENT),
                    ft.Text(f"Offer: {offer_status}", size=8,
                            weight=ft.FontWeight.BOLD, color=theme.TEXT),
                    ft.Container(expand=True),
                    ft.TextButton(
                        content="View Details",
                        on_click=lambda e: router.go("admin_buyer_detail"),
                        style=ft.ButtonStyle(color=theme.ACCENT),
                    ),
                ]),
            ], spacing=6),
        )

    content = ft.Column([
                admin_header(),
                ft.Text("Buyer Management", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("View and manage registered buyers.",
                        size=8, color="#FFFFFF"),
                search,
                ft.OutlinedButton(
                    content="Register New Buyer",
                    on_click=lambda e: router.go("admin_register_buyer"),
                    width=250,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                ft.OutlinedButton(
                    content="Review Pending Offers",
                    on_click=lambda e: router.go("admin_offers"),
                    width=250,
                    height=44,
                    style=ft.ButtonStyle(
                        color="#FFFFFF",
                        side=ft.BorderSide(1, "#FFFFFF"),
                        shape=ft.RoundedRectangleBorder(radius=22),
                    ),
                ),
                buyer_card("ABC Traders", "Rice Trader", "Active", "Verified"),
                buyer_card("DEF Traders", "Rice Trader", "Active", "Pending"),
                buyer_card("GHI Traders", "Rice Trader", "Inactive", "Inactive"),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=6, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Buyers"))
    return theme.with_background(body, overlay=False)


def admin_buyer_detail_view(router) -> ft.Control:
    def info(title, rows):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=16,
            padding=ft.Padding.all(12),
            content=ft.Column([
                ft.Text(title, size=10, weight=ft.FontWeight.BOLD,
                        color=theme.TEXT),
                *[
                    ft.Row([
                        ft.Text(label, size=8, color=theme.TEXT_MUTED, expand=True),
                        ft.Text(value, size=8, weight=ft.FontWeight.BOLD,
                                color=theme.TEXT),
                    ], spacing=4)
                    for label, value in rows
                ],
            ], spacing=5),
        )

    content = ft.Column([
                admin_header(),
                ft.Text("Buyer Details", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("View detailed information about the buyer.",
                        size=8, color="#FFFFFF"),
                info("Business Information", [
                    ("Business Name:", "ABC Traders"),
                    ("Business Type:", "Rice Trader"),
                    ("Address / Location:", "Pili, Camarines Sur"),
                    ("Contact Number:", "09123456789"),
                    ("Email Address:", "example@gmail.com"),
                ]),
                info("Account Information", [
                    ("Account Status:", "Active"),
                    ("Buyer Verification:", "Verified"),
                ]),
                info("Purchasing Offers", [
                    ("Current Price:", "P23.50/kg"),
                    ("Accepted Quantity:", "Up to 2,000 kg"),
                    ("Payment Conditions:", "Cash upon weighing"),
                ]),
                ft.Row([
                    ft.OutlinedButton(
                        content="Edit Details",
                        on_click=lambda e: router.go("admin_register_buyer"),
                        expand=True,
                    ),
                    ft.OutlinedButton(
                        content="Deactivate",
                        on_click=lambda e: router.go("admin_buyers"),
                        expand=True,
                        style=ft.ButtonStyle(color=theme.ERROR),
                    ),
                ], spacing=8),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=8, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Buyers"))
    return theme.with_background(body, overlay=False)


def admin_register_buyer_view(router) -> ft.Control:
    business_name = ft.TextField(
        hint_text="Enter business name...",
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        height=44,
        text_size=12,
        expand=True,
    )
    business_type = ft.Dropdown(
        hint_text="Select business type...",
        options=[
            ft.dropdown.Option("Rice Mill"),
            ft.dropdown.Option("Rice Trader"),
            ft.dropdown.Option("Cooperative"),
        ],
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        text_size=12,
        height=44,
        expand=True,
    )
    address = ft.TextField(
        hint_text="Enter address or location...",
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        height=44,
        text_size=12,
        expand=True,
    )
    phone = ft.TextField(
        hint_text="Enter phone number...",
        prefix_icon=ft.Icons.PHONE_OUTLINED,
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        height=44,
        text_size=12,
        expand=True,
    )
    email = ft.TextField(
        hint_text="Enter email address...",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        height=44,
        text_size=12,
        expand=True,
    )

    card = ft.Container(
        bgcolor="#FFFFFF",
        border_radius=24,
        padding=ft.Padding.all(14),
        border=ft.Border.all(1, "#FFFFFF"),
        expand=True,
        content=ft.Column([
            ft.Text("Register New Buyer", size=15,
                    weight=ft.FontWeight.BOLD, color=theme.TEXT),
            ft.Text("Business Name *", size=9, weight=ft.FontWeight.BOLD),
            business_name,
            ft.Text("Business Type *", size=9, weight=ft.FontWeight.BOLD),
            business_type,
            ft.Text("Address / Location *", size=9, weight=ft.FontWeight.BOLD),
            address,
            ft.Text("Contact Number *", size=9, weight=ft.FontWeight.BOLD),
            phone,
            ft.Text("Email Address *", size=9, weight=ft.FontWeight.BOLD),
            email,
        ], spacing=6),
    )

    def register(e):
        if not (business_name.value or "").strip():
            business_name.error = "Business Name is required"
            router.page.update()
            return
        success = ft.AlertDialog(
            modal=True,
            title=ft.Text("Registration Successful!", text_align=ft.TextAlign.CENTER),
            content=ft.Text(
                f"New buyer '{business_name.value}' has been registered.",
                text_align=ft.TextAlign.CENTER,
            ),
            actions=[
                ft.Button(
                    content="Go to Buyers List",
                    on_click=lambda e: (router.page.pop_dialog(),
                                        router.go("admin_buyers")),
                    style=ft.ButtonStyle(
                        bgcolor=theme.ACCENT,
                        color="#FFFFFF",
                    ),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        router.page.show_dialog(success)

    content = ft.Column([
                admin_header(),
                ft.Text("Register New Buyer", size=18,
                        weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                ft.Text("Create a new buyer account for umAni.",
                        size=8, color="#FFFFFF"),
                card,
                ft.Row([
                    ft.OutlinedButton(
                        content="Reset",
                        on_click=lambda e: router.go("admin_register_buyer"),
                        expand=True,
                        height=44,
                        style=ft.ButtonStyle(
                            color=theme.ACCENT,
                            side=ft.BorderSide(1.5, theme.ACCENT),
                            shape=ft.RoundedRectangleBorder(radius=22),
                        ),
                    ),
                    ft.Button(
                        content="Register Buyer",
                        on_click=register,
                        expand=True,
                        height=44,
                        style=ft.ButtonStyle(
                            bgcolor=theme.ACCENT,
                            color="#FFFFFF",
                            shape=ft.RoundedRectangleBorder(radius=22),
                        ),
                    ),
                ], spacing=8),
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
       spacing=7, scroll=ft.ScrollMode.AUTO, expand=True)
    body = theme.role_page(content, admin_nav(router, "Buyers"))
    return theme.with_background(body, overlay=False)
