import reflex as rx
import link_bio.styles.styles as styles

def navbar()-> rx.Component:
    return rx.hstack(
        rx.text(
            "Portfolio",
            height="30px"
            ),
            position="sticky",
            bg="yellow",
            padding_x=styles.Size.DEFAULT,
            padding_y=styles.Size.DEFAULT,
            z_index="999"
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