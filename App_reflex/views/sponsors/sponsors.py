import reflex as rx
from App_reflex.componentes.title import title


def header() -> rx.Component:
    return rx.chakra.Vstack(
        title("Colaboran"),
        
        rx.chakra.hstack(
           scr="" 
        ),
    )