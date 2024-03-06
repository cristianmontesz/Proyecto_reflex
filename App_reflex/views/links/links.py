import reflex as rx
from App_reflex.componentes.link_button import link_button
from App_reflex.componentes.title import title
from App_reflex.styles.styles import size as size
import App_reflex.constants as const

def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Redes Sociales"),
        link_button(
            "GitHub", 
            "iconos/github.svg",
            const.GITHUB_URL
                    ),
        link_button(
            "Youtube",
            "/iconos/youtube.svg",
            const.YOUTUBE_URL
            ),
        link_button(
            "Facebook", 
            "iconos/facebook.svg",
            const.FACEBOOK_URL
             ),
        link_button(
            "linkedin", 
            "iconos/linkedin.svg",
            const.LINKEDIN_URL
            ),
        width="100%",
        spacing=size.MEDIUM.value,
        
    )
    
   