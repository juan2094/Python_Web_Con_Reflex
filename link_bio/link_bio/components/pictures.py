import reflex as rx 
import link_bio.styles.styles as styles



def pictures(text: str) -> rx.Component:
    return rx.image(
        src=text,
        alt=text,
        width="auto",
        margin_x=styles.Size.BIG,
        margin_y=styles.Size.DEFAULT,
        height="10em",
        ratio=16/9,
    )