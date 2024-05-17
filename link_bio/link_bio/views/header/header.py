import reflex as rx
from link_bio.styles.colors import Color as Colors
from link_bio.styles.colors import TextColor as TextColors


def header() -> rx.Component:
        return rx.vstack(
                    rx.flex(
                        rx.avatar(src="logo.jpg",fallback="cc", size="7",color_scheme="orange",align="center"),
                        rx.card("Mi nombre es  Juan Antonio soy desarrollador, fotógrafo y técnico audiovisual.",align="center",background_color=Colors.PRIMARY,color=TextColors.HEADER),
                        align="center"
                    ),
            margin_top="5em",
            direction="column",
            align="center"
        )
