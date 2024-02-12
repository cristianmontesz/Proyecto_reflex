import reflex as rx
from enum import Enum
from .Colors import color as color
from .Colors import TextColor as TextColor

#constants
max_width="600px",

#size
class size(Enum): 
     SMALL="0.2em"
     MEDIUM="0.8em"
     DEFAULT="1em"
     LARGE="1.5em"
     BIG="2em"
     
#BASES
BASE_STYLE = {
    "background_color": color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": size.SMALL.value,
        "border_radius": size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": color.PRIMARY.value,
        "_hover": {
            "background_color": color.SECUNDARY.value,
        }
    },
}     

#styke_button
Button_title_style = dict(
    fond_size=size.DEFAULT.value,
    color=TextColor.HEADER.value
)

Navbar_title_style = dict(
    font_family="comfortaa-Medium",
    fond_size=size.LARGE.value,
    
)

Button_body_style = dict(
    fond_size=size.MEDIUM.value,
    color=TextColor.HEADER.value
)

title_style= dict(
    width="100%",
    padding_top = size.DEFAULT.value,
    color=TextColor.HEADER.value
    
    )



