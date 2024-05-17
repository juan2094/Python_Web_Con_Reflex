import reflex as rx
from enum import Enum
from .colors import Color as Colors
from .colors import TextColor as TextColors

#Constantes
MAX_WIDTH = 800


#Tamaños 

class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"
    LARGE="3em"
    XBIG="10em"
    VIDEO_SIZE="50em"


#Stilos

BASE_STYLE = {
    "background_color": Colors.BACKGROUND.value,

    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.DEFAULT.value,
        "border_radius": Size.DEFAULT.value,
        "color" : TextColors.BODY.value,
        "background_color": Colors.PRIMARY.value,
        "_hover": {
            "background_color": Colors.SECONDARY.value
        },
        "font_family" : "Rubik",
    },
    rx.link: {
        "text_decoration": "none",
        "_hover":{}
    }
}


navbar_title_style = dict(
        font_family = "Rubik",
        width="100%",
        color=TextColors.HEADER.value,
        font_size= Size.DEFAULT,
)


title_style = dict(
        
        width="100%",
        padding_top=Size.MEDIUM.value,
        color=TextColors.HEADER.value,
)

button_tittle_style = dict(
    font_size=Size.DEFAULT.value,
     color=TextColors.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColors.BODY.value,
)

video_style=dict(
     
        widht=Size.VIDEO_SIZE,
        height="auto",
        aling="center",
        color = TextColors.BODY.value,
)

