import reflex as rx
import App_reflex.styles.styles  as styles

def link_icon(url: str) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.icon(
            tag="external_link"
        ),
        href= url,
        is_external=True,
        width="100%"
    )