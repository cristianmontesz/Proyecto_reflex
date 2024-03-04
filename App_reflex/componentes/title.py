import reflex as rx
import App_reflex.styles.styles as Styles

def title(text: str) -> rx.Component:
    return rx.chakra.heading(
        text,
        size="sm",
        style= Styles.title_style
    )