import reflex as rx
from enum import Enum
from .Colors import color as color
from .Colors import TextColor as TextColor
from .fonts import font, FontWeight


#constants
max_width="600px",

#size
class size(Enum): 
     SMALL="0.2em"
     MEDIUM="0.8em"
     DEFAULT="1em"
     LARGE="1.5em"
     BIG="2em"
     
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"
    
# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    "/css/styles.css"
],
    


         
     
#BASES
BASE_STYLE = {
    "font_family": font.DEFAUL.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": color.BACKGROUND.value,
    "width": "100%",
    
    
     rx.chakra.heading:{
         "size":"lg",
         "color": TextColor.HEADER.value,
         "font_family": font.TITLE.value,
         "font_weight": FontWeight.MEDIUM.value,
         "text_align": "left"
     },
    rx.chakra.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": size.SMALL.value,
        "border_radius": size.SMALL.value,
        "color": TextColor.HEADER.value,
        "background_color": color.SECUNDARY.value,
        "_hover": {
        "background_color": color.PRIMARY.value,
        }
    },
}     

#styke_button
Button_title_style = dict(
    font_family= font.DEFAUL.value,
    font_weight=FontWeight.MEDIUM.value,
    fond_size=size.BIG.value,
    color=TextColor.HEADER.value,
    size= size.DEFAULT.value
)

Navbar_title_style = dict(
    font_family= font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    fond_size=size.MEDIUM.value,
    
)

Button_body_style = dict(
    font_family= font.DEFAUL.value,
    font_weight=FontWeight.MEDIUM.value,
    fond_size=size.MEDIUM.value,
    color=TextColor.HEADER.value
)

title_style= dict(
    width="100%",
    font_family= font.DEFAUL.value,
    font_weight=FontWeight.MEDIUM.value,
    padding_top = size.MEDIUM.value,
    color=TextColor.HEADER.value,
    
    
    )



