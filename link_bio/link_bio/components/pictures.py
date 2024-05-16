import reflex as rx 
import link_bio.styles.styles as styles



def pictures(text: str) -> rx.Component:
    return rx.image(
        src=text,
        alt=text,
        width="15em",
        margin_x=styles.Size.BIG,
        height="auto"
       
    )