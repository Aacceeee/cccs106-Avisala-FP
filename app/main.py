"""umAni entry point.  Run from the project root:  flet run app/main.py"""
import flet as ft

from app import theme
from app.router import Router
from app.views.shared.splash_view import splash_view
from app.views.shared.auth_view import welcome_view, signup_view
from app.views.farmer.farmer_home_view import farmer_home_view
from app.views.farmer.comparison_history_view import comparison_history_view
from app.views.farmer.farmer_location_view import farmer_location_view
from app.views.farmer.assistant_view import assistant_view

from app.views.farmer.farmer_harvest_view import farmer_harvest_view
from app.views.farmer.farmer_preferences_view import farmer_preferences_view
from app.views.farmer.farmer_confirm_view import farmer_confirm_view
from app.views.farmer.farmer_results_view import farmer_results_view
from app.views.farmer.farmer_results_view import ranking_loading_view
from app.views.farmer.farmer_buyer_view import (
    buyer_details_view,
    buyer_contact_view,
    settings_view,
)
from app.views.buyer.buyer_dashboard_view import buyer_dashboard_view
from app.views.buyer.buyer_offers_view import buyer_offers_view
from app.views.buyer.buyer_profile_view import buyer_profile_view, buyer_profile_edit_view
from app.views.admin.admin_login_view import admin_login_view
from app.views.admin.admin_dashboard_view import admin_dashboard_view
from app.views.admin.admin_buyers_view import (
    admin_buyers_view,
    admin_buyer_detail_view,
    admin_register_buyer_view,
)
from app.views.admin.admin_offers_view import (
    admin_offers_view,
    admin_offer_detail_view,
    admin_offer_management_view,
)
from app.views.admin.admin_settings_view import admin_settings_view


def main(page: ft.Page):
    page.title = "umAni"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = theme.BG
    page.padding = 0
    page.spacing = 0          # no gap between page children
    page.window.width = 390   # default Android-style phone preview
    page.window.height = 844
    page.window.resizable = True
    page.window.min_width = 390
    page.window.min_height = 700

    router = Router(page)
    router.register("splash", splash_view)
    router.register("welcome", welcome_view)
    router.register("signup", signup_view)
    router.register("farmer_home", farmer_home_view)
    router.register("comparison_history", comparison_history_view)
    router.register("farmer_location", farmer_location_view)
    router.register("assistant", assistant_view)
    router.register("buyer", welcome_view)
    router.register("buyer_login", welcome_view)
    router.register("buyer_dashboard", buyer_dashboard_view)
    router.register("buyer_offers", buyer_offers_view)
    router.register("buyer_profile", buyer_profile_view)
    router.register("buyer_profile_edit", buyer_profile_edit_view)
    router.register("admin_login", admin_login_view)
    router.register("admin_dashboard", admin_dashboard_view)
    router.register("admin_buyers", admin_buyers_view)
    router.register("admin_offers", admin_offers_view)
    router.register("admin_offer_detail", admin_offer_detail_view)
    router.register("admin_offer_management", admin_offer_management_view)
    router.register("admin_buyer_detail", admin_buyer_detail_view)
    router.register("admin_register_buyer", admin_register_buyer_view)
    router.register("admin_settings", admin_settings_view)
    router.register("admin", admin_login_view)
    router.register("farmer_harvest", farmer_harvest_view)
    router.register("farmer_preferences", farmer_preferences_view)
    router.register("farmer_confirm", farmer_confirm_view)
    router.register("farmer_results", farmer_results_view)
    router.register("ranking_loading", ranking_loading_view)
    router.register("buyer_details", buyer_details_view)
    router.register("buyer_contact", buyer_contact_view)
    router.register("settings", settings_view)

    router.go("splash")


if __name__ == "__main__":
    ft.run(main, assets_dir=theme.ASSETS_DIR)
