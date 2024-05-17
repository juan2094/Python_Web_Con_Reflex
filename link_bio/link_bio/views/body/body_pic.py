import reflex as rx
from link_bio.components.pictures import pictures
import link_bio.styles.styles as styles
from link_bio.components.title import title
from link_bio.components.video import video
from link_bio.styles.colors import Color as Colors
from link_bio.styles.colors import TextColor as TextColors

def body_pics() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        title("Muestra de fotografías"),
        ),
        rx.mobile_only(
            rx.vstack(
                pictures("foto1.jpg"),
                pictures("foto2.jpg"),
                pictures("foto3.jpg"),
                margin_y=styles.Size.DEFAULT,
            ),
            rx.vstack(
                pictures("foto4.jpg"),
                pictures("foto5.jpg"),
                pictures("foto6.jpg"),
                margin_y=styles.Size.DEFAULT,
            ),
        ),
        rx.desktop_only(
            rx.hstack(
                pictures("foto1.jpg"),
                pictures("foto2.jpg"),
                pictures("foto3.jpg"),
                margin_y=styles.Size.DEFAULT,
            ),
            rx.hstack(
                pictures("foto4.jpg"),
                pictures("foto5.jpg"),
                pictures("foto6.jpg"),
                margin_y=styles.Size.DEFAULT,
            ),
        ),
        rx.vstack(
        rx.hstack(
        title("Muestra de Videos"),
        ),
        rx.text("Aquí un video de cuando grababa bodas antes de dedicarme grabar y emitir en televisión",color = TextColors.BODY.value,),
        video("https://www.youtube.com/watch?v=HakHjHVnM24"),
        direction="column",
        align="center",
        width="100%"
        ),
        #SEGUIR HACIENDO RESPONSIVE, QUEDA EL VIDEO
        
        margin_top=styles.Size.BIG.value,
        direction="column",
        align="center",
        width="100%"
    )