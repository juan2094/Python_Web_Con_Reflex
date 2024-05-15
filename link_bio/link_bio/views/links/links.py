import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button(
            "Mi insta!",
            "Como una de mis mayores aficiones: la fotografía",
            "https://www.instagram.com/juan_20_94"),
        link_button("Mi github!",
                    "Como mi profesión, el desarrollo.",
                    "https://github.com/juan2094"),
        align="center",
        width="100%"
    )