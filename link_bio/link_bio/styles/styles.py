import reflex as rx
from enum import Enum


#Constantes
MAX_WIDTH = 800


#Tamaños 

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"

#Stilos

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.DEFAULT.value,
        "border_radius": Size.DEFAULT.value
        
    },
    rx.link: {
        "text_decoration": "none",
        "_hover":{}
    }
}

title_style = dict(
        
        width="100%",
        padding_top=Size.MEDIUM.value
)

button_tittle_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)


