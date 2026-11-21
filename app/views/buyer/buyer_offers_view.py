from datetime import datetime

import flet as ft
from app import theme
from app.views.buyer.buyer_components import (
    GREEN_TEXT,
    PAYMENT_OPTIONS,
    action_button,
    buyer_page,
    input,
    light_card,
    offer,
    section_title,
    tab,
)


def buyer_offers_view(router) -> ft.Control:
    o = offer(router)
    price = input(
        hint_text="Enter buying price (e.g., 23.00)",
        value=o["price"],
        prefix=ft.Text("₱ "),
        keyboard_type=ft.KeyboardType.NUMBER,
        height=44,
    )
    quantity = input(
        hint_text="Enter accepted quantity (e.g., 2000)",
        value=o["quantity"],
        suffix=ft.Text(" kg"),
        keyboard_type=ft.KeyboardType.NUMBER,
        height=44,
    )
    options = (PAYMENT_OPTIONS if o["payment"] in PAYMENT_OPTIONS
               else [o["payment"], *PAYMENT_OPTIONS])
    payment = ft.Dropdown(
        value=o["payment"],
        hint_text="Select payment method",
        options=[ft.dropdown.Option(x) for x in options],
        bgcolor="#FFFFFF",
        border_radius=12,
        border=theme.text_field_border(theme.ACCENT, 12),
        text_size=12,
        height=44,
        expand=True,
    )
    notes = input(
        hint_text="Enter purchasing requirements / notes...",
        value=o["requirements"],
        multiline=True,
        min_lines=2,
        max_lines=3,
    )

    def label(text):
        return ft.Text(text, size=10, weight=ft.FontWeight.BOLD,
                       color=GREEN_TEXT)

    def submit(e):
        price.error = quantity.error = None
        try:
            p_val = float(price.value)
            if p_val <= 0:
                raise ValueError
        except (TypeError, ValueError):
            price.error = "Enter a price greater than 0"
        try:
            q_val = float(quantity.value)
            if q_val <= 0:
                raise ValueError
        except (TypeError, ValueError):
            quantity.error = "Enter a quantity greater than 0"
        if price.error or quantity.error:
            router.page.update()
            return
        router.session.buyer_offer = {
            "price": f"{p_val:.2f}",
            "quantity": f"{q_val:g}",
            "payment": payment.value or PAYMENT_OPTIONS[0],
            "requirements": (notes.value or "").strip() or "None",
            "status": "Pending Admin Verification",
            "updated": datetime.now().strftime("%b %d, %Y"),
        }
        tab(router, "buyer_dashboard")

    form = light_card(ft.Column([
        ft.Text("Update Purchasing Offer", size=14,
                weight=ft.FontWeight.BOLD, color=GREEN_TEXT),
        label("Buying Price (PHP per kg)"),
        price,
        label("Max Accepted Quantity (kg)"),
        quantity,
        label("Payment Method"),
        payment,
        label("Purchasing Requirements / Notes"),
        notes,
        ft.Row([
            ft.Icon(ft.Icons.INFO_OUTLINE, size=13, color=theme.ACCENT),
            ft.Text("Submitting updates will send your offer for admin verification.",
                    size=9, color=theme.TEXT_MUTED, expand=True),
        ], spacing=5),
    ], spacing=6))

    return buyer_page(router, "offers", [
        section_title(ft.Icons.LOCAL_OFFER, "Purchasing Offers",
                      "Update your current buying offer."),
        form,
        action_button("Submit Offer for Verification", submit, width=270),
    ])
