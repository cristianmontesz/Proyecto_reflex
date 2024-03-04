import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size as size

def link_sponsor(  imagen: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            height=size.BIG.value,
            src=imagen
        ),
        href=url,
        is_external=True
    )