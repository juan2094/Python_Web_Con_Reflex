import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.views.body.body_pic import body_pics
import link_bio.styles.styles as styles




class State(rx.State):
    pass

def index() -> rx.Component:
    return  rx.box(
        navbar(),
        rx.center(
            rx.vstack( 
                header(),
                links(),
                
                max_width=styles.MAX_WIDTH,
                margin_top=styles.Size.BIG.value,
                margin_bottom=styles.Size.BIG.value,
                align="center",
                width="100%"
            )
        ),
        body_pics(),
        footer(),
        
    )



       
    







app = rx.App(
    style=styles.BASE_STYLE
)

app.add_page(index,title="Mi portfolio en python web")

