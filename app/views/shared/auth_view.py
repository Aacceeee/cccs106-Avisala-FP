"""Welcome (login) and Create Account views, styled after the Figma login screen.

Assets used (put in /assets, all optional - fallbacks are provided):
    bg.jpg      rice-grain background (see theme.py)
    logo.png    umAni logo (see theme.py)
    google.png  small Google "G" logo (falls back to a blue "G")
"""
import flet as ft
from app import theme

# --- Colors sampled by eye from the Figma login frame; tweak here if needed.
PILL_BG = "#DADADA"          # light-gray input / secondary buttons
PILL_TEXT = "#1F1F1F"
PILL_HINT = "#777777"
BTN_GREEN = "#2C5E10"        # dark green "Sign In" button
GREEN_ICON = "#2C5E10"
ERROR_ON_GLASS = "#FFB4A8"


# ---------------------------------------------------------------- shared pieces
def _glass_panel(children: list, logo_size: int = 84) -> ft.Control:
    """Translucent blurred panel with the logo overlapping its top edge."""
    overlap = logo_size // 2
    panel = ft.Container(
        margin=ft.Margin.only(top=overlap),
        padding=ft.Padding.only(left=22, right=22, bottom=22, top=overlap + 8),
        bgcolor=ft.Colors.with_opacity(0.38, "#1A1F14"),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.25, "#FFFFFF")),
        border_radius=38,
        content=ft.Column(children, spacing=10,
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER),
    )
    logo = ft.Row([theme.logo(logo_size)], alignment=ft.MainAxisAlignment.CENTER)
    return ft.Container(
        margin=ft.Margin.symmetric(horizontal=26),
        content=ft.Stack([panel, logo]),
    )


def _pill_field(hint: str, icon, password: bool = False):
    """Light-gray pill with green icon, divider, and a borderless text field."""
    field = ft.TextField(
        hint_text=hint,
        password=password,
        can_reveal_password=password,
        border=ft.NoInputBorder(),
        text_size=13,
        color=PILL_TEXT,
        hint_style=ft.TextStyle(color=PILL_HINT, size=13),
        content_padding=ft.Padding.symmetric(horizontal=6, vertical=0),
        expand=True,
        height=46,
    )
    error = ft.Text("", size=10, color=ERROR_ON_GLASS, visible=False)
    pill = ft.Container(
        height=48,
        bgcolor=PILL_BG,
        border_radius=26,
        content=ft.Row(
            [
                ft.Container(ft.Icon(icon, size=20, color=GREEN_ICON),
                             padding=ft.Padding.only(left=16, right=6)),
                ft.Container(width=1, height=22, bgcolor="#9A9A9A"),
                field,
            ],
            spacing=6,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )
    return ft.Column([pill, error], spacing=2, tight=True), field, error


def _set_error(field: ft.TextField, error_text: ft.Text, message: str | None) -> bool:
    error_text.value = message or ""
    error_text.visible = bool(message)
    return bool(message)


def _outlined_green_button(label: str, on_click, icon=None) -> ft.Button:
    row = [ft.Text(label, size=15, weight=ft.FontWeight.BOLD, color="#FFFFFF")]
    if icon:
        row.append(ft.Icon(icon, size=20, color="#FFFFFF"))
    return ft.Button(
        content=ft.Row(row, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
        on_click=on_click,
        height=48,
        expand=True,
        style=ft.ButtonStyle(
            bgcolor=BTN_GREEN,
            side=ft.BorderSide(1.5, "#FFFFFF"),
            shape=ft.RoundedRectangleBorder(radius=26),
        ),
    )


def _gray_button(label: str, leading: ft.Control, on_click=None, height: int = 48) -> ft.Button:
    return ft.Button(
        content=ft.Row(
            [leading, ft.Text(label, size=13, weight=ft.FontWeight.BOLD, color=PILL_TEXT)],
            alignment=ft.MainAxisAlignment.CENTER, spacing=8,
        ),
        on_click=on_click,
        height=height,
        expand=True,
        style=ft.ButtonStyle(bgcolor=PILL_BG,
                             shape=ft.RoundedRectangleBorder(radius=26)),
    )


def _google_icon() -> ft.Control:
    if theme.has_asset("google.png"):
        return ft.Image(src="google.png", width=18, height=18)
    return ft.Text("G", size=16, weight=ft.FontWeight.BOLD, color="#4285F4")


def _or_divider() -> ft.Control:
    line = ft.Container(height=1, bgcolor=ft.Colors.with_opacity(0.7, "#FFFFFF"), expand=True)
    return ft.Row([line, ft.Text("or", size=11, color="#FFFFFF"), line], spacing=8)


def _title(text: str, subtitle: str) -> list[ft.Control]:
    return [
        ft.Text(text, size=22, weight=ft.FontWeight.BOLD, color="#FFFFFF",
                text_align=ft.TextAlign.CENTER),
        ft.Text(subtitle, size=11, color="#FFFFFF", text_align=ft.TextAlign.CENTER),
        ft.Container(height=6),
    ]


def _page(panel: ft.Control, top_gap: int = 60) -> ft.Control:
    body = ft.SafeArea(
        content=ft.Column([ft.Container(height=top_gap), panel],
                          scroll=ft.ScrollMode.AUTO, expand=True),
        expand=True,
    )
    # No dark-green overlay here: the Figma background is light and blurred.
    return theme.with_background(body, overlay=False, wrap_glass=False)


# ---------------------------------------------------------------- Welcome / login
def welcome_view(router) -> ft.Control:
    user_box, username, user_err = _pill_field(
        "Email or Username", ft.Icons.PERSON)
    pass_box, password, pass_err = _pill_field(
        "Password", ft.Icons.LOCK, password=True)

    def sign_in(e):
        bad_user = _set_error(username, user_err,
                              None if (username.value or "").strip() else "Username or email is required")
        bad_pass = _set_error(password, pass_err,
                              None if (password.value or "").strip() else "Password is required")
        if bad_user or bad_pass:
            router.page.update()
            return

        account = (username.value or "").strip().lower()
        supplied_password = password.value or ""
        # TODO: Replace this demo role lookup with a database authentication query.
        admin_accounts = {"admin": {"admin123"}, "admin@umani.com": {"admin123"}}
        buyer_accounts = {
            "buyer": {"buyer123"}, "abc": {"buyer123"},
            "abc_traders": {"buyer123"}, "abc@gmail.com": {"buyer123"},
        }
        if account in admin_accounts and supplied_password in admin_accounts[account]:
            route = "admin_dashboard"
        elif account in buyer_accounts and supplied_password in buyer_accounts[account]:
            route = "buyer_dashboard"
        else:
            route = "farmer_home"  # TODO: should be "invalid credentials" once real auth exists
        router.go(route)

    forgot = ft.Row(
        [ft.TextButton(
            content=ft.Text("Forgot Password?", size=11, color="#FFFFFF",
                            style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)),
            # TODO: on_click -> forgot-password view
        )],
        alignment=ft.MainAxisAlignment.END,
    )

    panel = _glass_panel(
        _title("Welcome Back!", "Log in to continue your umAni account.")
        + [
            user_box,
            pass_box,
            forgot,
            ft.Row([_outlined_green_button("Sign In", sign_in, ft.Icons.ARROW_FORWARD)]),
            _or_divider(),
            ft.Row([_gray_button("Sign In with Google", _google_icon())]),  # TODO: Google sign-in
            ft.Text("Don't have an account?", size=11, color="#FFFFFF"),
            ft.Row([_gray_button("Register as a Farmer",
                                 ft.Icon(ft.Icons.ECO_OUTLINED, size=18, color=GREEN_ICON),
                                 on_click=lambda e: router.go("signup"), height=38)]),
        ]
    )
    return _page(panel)


# ---------------------------------------------------------------- Create account
def signup_view(router) -> ft.Control:
    specs = [
        ("Full Name", ft.Icons.PERSON, False),
        ("Email Address", ft.Icons.EMAIL, False),
        ("Username", ft.Icons.BADGE, False),
        ("Password", ft.Icons.LOCK, True),
        ("Confirm Password", ft.Icons.LOCK, True),
    ]
    rows = [_pill_field(h, i, p) for h, i, p in specs]
    boxes = [r[0] for r in rows]
    fields = {h: r[1] for (h, _, _), r in zip(specs, rows)}
    errors = {h: r[2] for (h, _, _), r in zip(specs, rows)}

    def create(e):
        bad = False
        for label, field in fields.items():
            msg = None if (field.value or "").strip() else f"{label} is required"
            bad |= _set_error(field, errors[label], msg)
        if not bad and fields["Password"].value != fields["Confirm Password"].value:
            bad = _set_error(fields["Confirm Password"], errors["Confirm Password"],
                             "Passwords do not match")
        if bad:
            router.page.update()
            return
        # TODO: save the new farmer account to the database.
        router.go("farmer_home")

    back = ft.Row(
        [ft.IconButton(ft.Icons.ARROW_BACK, icon_color="#FFFFFF",
                       on_click=lambda e: router.back())],
    )
    panel = _glass_panel(
        _title("Create Your Account", "Join umAni and start comparing palay buyers.")
        + boxes
        + [
            ft.Row([_outlined_green_button("Create Account", create)]),
            ft.Row(
                [ft.Text("Already have an account?", size=11, color="#FFFFFF"),
                 ft.TextButton(
                     content=ft.Text("Sign in", size=11, weight=ft.FontWeight.BOLD,
                                     color="#FFFFFF"),
                     on_click=lambda e: router.go("welcome"))],
                alignment=ft.MainAxisAlignment.CENTER, spacing=2,
            ),
        ],
        logo_size=64,
    )
    body = ft.SafeArea(
        content=ft.Column([back, panel], scroll=ft.ScrollMode.AUTO, expand=True),
        expand=True,
    )
    return theme.with_background(body, overlay=False, wrap_glass=False)
