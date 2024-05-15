import reflex as rx
import datetime 

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link("Repositorio de esta página.",
                href="https://github.com/juan2094/Python_Web_Con_Reflex"),
        rx.text(f"Web portfolio desarrollada en su totalidad en python usando Reflex. v0.1, {datetime.date.today().year}"),
        align="center"
    )