import reflex as rx
import link_bio.styles.styles as styles

def video(link: str, es_movil: bool) -> rx.Component:
    if es_movil:
        return rx.video(
            url=link,
            style=styles.video_mobile_style,
        )
    else:
        return rx.video(
            url=link,
            style=styles.video_style,
        )
