import reflex as rx
from App_reflex.componentes.title import title
from App_reflex.componentes.link_sponsor import link_sponsor


def header() -> rx.Component:
    return rx.chakra.vstack(
        title("Colaboran"),
        
        rx.chakra.hstack(
           link_sponsor(
               "MPV.png"
           )
        ),
    )