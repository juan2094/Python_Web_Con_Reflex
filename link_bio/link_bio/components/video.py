import reflex as rx 
import link_bio.styles.styles as styles



def video(link: str) -> rx.Component:
    return rx.video(
        url=link,
        style=styles.video_style
    )