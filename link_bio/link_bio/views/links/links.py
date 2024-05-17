import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces de interés"),
        link_button(
            "Mi insta!",
            "Como una de mis mayores aficiones: la fotografía",
            "insta.svg",
            "https://www.instagram.com/juan_20_94"),
        link_button("Mi github!",
                    "Como mi profesión, el desarrollo.",
                    "github.svg",
                    "https://github.com/juan2094"),

        title("Contacto"),
        link_button("Mi correo!",
                    "Correo profesional.",
                    "mail.svg",
                    "mailto:juanantonio200594@gmail.com"),
        align="center",
        width="100%"
    )