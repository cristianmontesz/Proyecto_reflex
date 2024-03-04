import reflex as rx
from App_reflex.componentes.link_icon import link_icon
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as Textcolor
from App_reflex.styles.Colors import color as color

def info_text(title:str, body:str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(title, 
            font_weight="bold",
            color="red"),
        f" {body}", 
        font_size=size.MEDIUM.value,
        color=Textcolor.HEADER.value
    )