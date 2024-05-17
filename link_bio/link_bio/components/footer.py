import reflex as rx
import datetime 
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Colors
from link_bio.styles.colors import TextColor as TextColors

def footer()-> rx.Component:
    return rx.vstack(
        rx.image(src="favicon1.ico"),
        rx.link("Enlace para ir al repositorio de esta página.",
                href="https://github.com/juan2094/Python_Web_Con_Reflex",
                color=TextColors.FOOTER.value),
        rx.text(f"Web portfolio desarrollada en su totalidad en python usando Reflex. v0.10, {datetime.date.today().year}",color=TextColors.FOOTER.value),
        margin_top=styles.Size.XBIG.value,
        padding_bottom=styles.Size.BIG.value,
        padding_x=styles.Size.BIG.value,
        align="center",
    )