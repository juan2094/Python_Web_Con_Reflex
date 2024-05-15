import reflex as rx


def header() -> rx.Component:
        return rx.flex(
            rx.avatar(src="logo.jpg",fallback="cc", size="5",color_scheme="orange",align="center"),
            rx.text("@juan2094",align="center"),
            rx.card("Mi nombre es  Juan Antonio soy desarrollador, fotógrafo y técnico audiovisual.",align="center"),
            direction="column",
            align="center"
        )
