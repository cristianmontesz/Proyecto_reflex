import reflex as rx
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color

def footer() -> rx.component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text("2024 montestapiero0127@gmail.com "),
        margin_bottom=size.BIG.value,
        spacing=size.DEFAULT.value,
        position="absolute",
        bottom="0",
        width="100%",
        color=textcolor.HEADER.value
    )