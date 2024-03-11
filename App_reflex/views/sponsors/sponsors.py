import reflex as rx
import App_reflex.constants as const
from App_reflex.styles.styles import size as size
from App_reflex.componentes.title import title
from App_reflex.componentes.link_sponsor import link_sponsor



def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran: "),
            rx.chakra.responsive_grid(
               link_sponsor(
               "MPV.png",
               const.MVP_URL,
               
           ),
               link_sponsor(
               "GITHUB.png",
               const.GITHUB_URL
        ),
               link_sponsor(
               "Cisco.png",
               const.CISCONW_URL
        ),
                link_sponsor(
               "Empleo.png",
               const.CISCONW_URL
        ),
        
        spacing=size.DEFAULT.value,
        columns=[1, 4]       
    ),
        width="100%",
        align_items="start",
              
)
       