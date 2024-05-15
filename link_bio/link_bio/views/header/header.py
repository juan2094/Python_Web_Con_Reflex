import reflex as rx


def header() -> rx.Component:
        return rx.hstack(
            rx.avatar(scr="logo.jpg",fallback="cc", size="5",color_scheme="orange"),
            rx.text("@juan2094"),
            rx.text("Mi nombre es  juan antonio, desarrollador, fotógrafo y técnico audiovisual.")
        )
