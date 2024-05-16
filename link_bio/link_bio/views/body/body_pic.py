import reflex as rx
from link_bio.components.pictures import pictures
import link_bio.styles.styles as styles
from link_bio.components.title import title


def body_pics() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        title("Muestra de algunas de mis fotografías"),
        ),
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
        direction="column",
        align="center",
        width="100%"
    )