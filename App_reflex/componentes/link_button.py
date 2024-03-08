import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size, Spacing
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as Textcolor
from App_reflex.styles.Colors import color as color


def link_button(title: str,
                body: str, 
                image:str, 
                url: str) -> rx.Component:
    return rx.chakra.link(
              rx.chakra.button(
                rx.chakra.hstack(
                  rx.chakra.image(
                    src=image,
                       width= size.DEFAULT.value,
                       height=size.DEFAULT.value,
                       margin=size.DEFAULT.value,
                       alt=title 
                       ),
                            rx.chakra.vstack(
                                rx.chakra.text(
                                title, 
                                 size=Spacing.SMALL.value,
                                   style=styles.Button_title_style,
                                       ),
                                      rx.chakra.text(
                                        body,
                                         size=Spacing.VERY_SMALL.value,
                                           style=styles.Button_body_style,
                                            ),
                       align_items="start",
                       spacing= Spacing.VERY_SMALL.value,
                       padding_y= size.SMALL.value,
                       padding_right=size.DEFAULT.value
                      ),
                            width="100%",
                            href= url,
                            is_external=True,

                )
              )
    )