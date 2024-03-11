import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size as size

def link_sponsor(  imagen: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=imagen,
            height=size.BIG.value,
            width="auto",
            alt=alt
        ),
        href=url,
        is_external=True
    )