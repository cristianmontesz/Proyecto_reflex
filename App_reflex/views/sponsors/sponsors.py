import reflex as rx
import App_reflex.constants as const
from App_reflex.componentes.title import title
from App_reflex.componentes.link_sponsor import link_sponsor



def sponsors() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
            rx.chakra.hstack(
               link_sponsor(
               "MPV.png",
               const.MVP_URL
           ),
               link_sponsor(
               "GITHUB.png",
               const.GITHUB_URL
        ),
    )
        )
       