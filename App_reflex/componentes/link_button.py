import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color


def link_button(text: str, url: str) -> rx.component:
    return rx.link(
        rx.button(
                rx.hstack(
                     rx.icon(
                       tag="chevron_right",
                       width= size.MEDIUM.value,
                       height=size.MEDIUM.value,
                       margin=size.MEDIUM.value 
                     ),
                     rx.vstack(
                         rx.text(text, style=styles.Button_title_style),
                         margin=size.MEDIUM.value
                         
                     ),
                  )
                ),
        href= url,
        is_external=True,
        width="100%"
    )