import reflex as rx
from App_reflex.componentes.link_button import link_button
from App_reflex.componentes.link_icon import link_icon
from App_reflex.componentes.info_text import info_text
from App_reflex.componentes.title import title
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color


def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.flex(
                rx.chakra.avatar(
                src="Avatar.jpg",
                fallback="CM",
                padding="2px",
                border="4px",
                border_color=color.SECUNDARY.value,
                color= color.CONTENT.value,
                
            ),
                
            rx.chakra.vstack(
                rx.chakra.heading("CRISTIAN MONTES ", 
                           color=textcolor.HEADER.value,
                           spacing=size.MEDIUM.value,
                           ),
                rx.chakra.text(
                    "@CristianM ",
                    margin_top="0px !important",
                    color=textcolor.HEADER.value,
                    
                ),
                align_items="start",
                
            ),
        ),
        rx.chakra.flex(
            info_text("+6", "Meses de experiencia laboral"),
            
        ),
        rx.chakra.text("""Soy tecnologo en Analisis y Desarrollo de Software, 
                   Actualmente me encuentro desarrollando las practics en la empresa 
                   VC-MEDIOS, por lo cual me quedan 3 meses para la finaizacion. ¡Bienvenid@s! """,
                   color= textcolor.HEADER.value,
                   widht="100%"
                   ),
                align_items="start"
    )