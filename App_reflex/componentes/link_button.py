import reflex as rx
import App_reflex.styles.styles  as styles

def link_button(text: str, url: str) -> rx.component:
    return rx.link(
        rx.button(
                rx.hstack(
                     rx.icon(
                       tag="chevron_right",  
                     ),
                     rx.vstack(
                         rx.text(text, style=styles.Button_title_style),
                         
                         
                     )
                  )
                ),
        href= url,
        is_external=True,
        width="100%"
    )