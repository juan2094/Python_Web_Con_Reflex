import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.colors import Color as Colors
from link_bio.styles.colors import TextColor as TextColors


def navbar()-> rx.Component:
    return rx.hstack(
        rx.hstack(rx.avatar(fallback="RD",color="#ffB400"),
                  rx.flex(
                        rx.text("Realiza, ",color=TextColors.HEADER.value,high_contrast=True),
                        rx.text("desarrolla;",color=Colors.SECONDARY.value),    
                        direction="column",
                        align="start",
                        style=styles.navbar_title_style,
                    ),
                    align="center"
                ),
            position="fixed",
            bg=Colors.PRIMARY.value,
            padding_x=styles.Size.DEFAULT,
            padding_y=styles.Size.DEFAULT,
            z_index="999",
            width="100%",
    )
    




    """return rx.box( 
        rx.hstack(
            rx.image(src="favicon.ico"),
            rx.heading("My test app")
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button("Menu"),
        ),
        position="fixed",
        width="100%",
        top="1px",
        z_index="5" 
        """