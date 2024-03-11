import reflex as rx
from enum import Enum
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color
import App_reflex.styles.styles  as styles
from App_reflex.styles.styles import size, Spacing

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="iconos/footer.svg",
            height=size.BIG.value,
            weight=size.BIG.value,
            alt="logotipo"
            ),
        rx.chakra.text("2024 montestapiero0127@gmail.com ",
                       font_size=size.DEFAULT.value,
                       margin_top=size.SMALL.value,
                       ),
        margin_bottom=size.BIG.value,
        padding_bottom=size.BIG.value,
        padding_y=size.SMALL.value,
        spacing=size.DEFAULT.value,
        width="100%",
        color=textcolor.HEADER.value
    )