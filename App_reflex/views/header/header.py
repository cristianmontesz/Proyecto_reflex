import reflex as rx
from App_reflex.componentes.link_button import link_button
from App_reflex.componentes.link_icon import link_icon
from App_reflex.componentes.info_text import info_text
from App_reflex.componentes.title import title
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color
from App_reflex.styles.styles import size, Spacing
import App_reflex.constants as const




def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
              rx.chakra.box( 
                rx.chakra.avatar(
                    name="Cristian Montes",
                    src="/Avatar.jpg",
                    radius="full",
                    color=textcolor.BODY.value,
                    bg=color.CONTENT.value,
                    padding="2px",
                    border=f"2px solid {color.SECUNDARY.value}"
                ), 
                position="relative"
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
                rx.chakra.hstack(
                 link_icon(
                      "/iconos/github.svg",
                      const.GITHUB_URL,
                    ),
                 link_icon(
                      "/iconos/facebook.svg",
                      const.FACEBOOK_URL,
                    ),
                 link_icon(
                      "/iconos/youtube.svg",
                      const.YOUTUBE_URL,
                    ),
                 link_icon(
                      "/iconos/linkedin.svg",
                      const.LINKEDIN_URL,
                      ),
                    spacing=Spacing.LARGE.value,
                    padding_top=size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.chakra.flex(
            info_text("+6", "Meses de experiencia laboral"),
            
        ),
        rx.chakra.text("""Soy tecnologo en Analisis y Desarrollo de Software, 
                           Actualmente me encuentro desarrollando las practics en la empresa 
                           VC-MEDIOS, por lo cual me quedan 3 meses para la finaizacion. ¡Bienvenid@s! """,
                   font_size= size.MEDIUM.value,
                   color= textcolor.HEADER.value,
                   widht="100%"
                   ),
                align_items="start"
                
    )