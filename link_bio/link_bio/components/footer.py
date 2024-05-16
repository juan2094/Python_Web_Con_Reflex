import reflex as rx
import datetime 
import link_bio.styles.styles as styles

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link("Repositorio de esta página.",
                href="https://github.com/juan2094/Python_Web_Con_Reflex"),
        rx.text(f"Web portfolio desarrollada en su totalidad en python usando Reflex. v0.10, {datetime.date.today().year}"),
        align="center",
        margin_y=styles.Size.BIG.value,
    )