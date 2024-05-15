import reflex as rx 
import link_bio.styles.styles as styles



def link_button(title: str,body: str, url: str) -> rx.Component:
    return rx.link(
                rx.button(
                    rx.hstack(
                        rx.icon(
                            tag="arrow-right",
                            widht=styles.Size.BIG.value
                        ),
                        rx.vstack(
                            rx.text(title,style=styles.button_tittle_style),
                            rx.text(body,style=styles.button_body_style)
                        ),
                    )

                ),
                href=url,
                is_external=True,
                width="100%",
                aling="center",
                
                    )




