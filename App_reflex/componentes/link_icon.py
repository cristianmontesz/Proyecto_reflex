import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size as size

def link_icon(image: str, url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.image(
            src=image,
            width= size.DEFAULT.value
        ),
        href= url,
        is_external=True,
        width="100%"
    )