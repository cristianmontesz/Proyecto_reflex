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
from typing import Literal as Literal



def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.hstack(
              rx.chakra.box( 
                rx.chakra.avatar(
                    name="Cristian Montes",
                    src="/aprender.png",
                    fallback="RU",
                    sizes="40",
                    width="100px",  
                    height="100px",
                    color=textcolor.BODY.value,
                    padding="2px",
                    border=f"2px solid {color.SECUNDARY.value}"
                ), 
                position="relative",
                widht="100%",
            ),
                
            rx.chakra.vstack(
                rx.chakra.heading("APRENDE A PROGRAMAR ", 
                           color=textcolor.HEADER.value,
                           spacing=size.MEDIUM.value,
                           ),
                rx.chakra.text(
                    "@Aprogramar ",
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
            info_text("+3", "Meses de aprendizaje en cursos totalmente gratis  "),
            
        ),
        rx.chakra.text("""En esta pagina tendras un recorrido por diferentes paginas web que te ayudaran
                       con tu proceso de aprendizaje y te aportaran conocimientos escenciales en el area 
                       de analisis y desarrollo web. ¡Bienvenid@s! """,
                   font_size= size.MEDIUM.value,
                   color= textcolor.HEADER.value,
                   widht="100%"
                   ),
                align_items="start"
                
    )