from enum import Enum 

class Color(Enum):
    PRIMARY = "#151530" #azul menos oscurisimo
    SECONDARY = "#0056AE" #celeste oscuro
    BACKGROUND = "#0b0b1f" #azul oscurisimo
    ##2D2D30 #9B9B9B 0b0b1f AZUL OSCURO B3B3B3 no se ffB400 mostaza
    CONTENT = "#FFFFFF"

class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#FFFFFF"
    FOOTER = "#A3ABB2"