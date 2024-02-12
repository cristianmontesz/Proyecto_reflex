import reflex as rx
import App_reflex.styles.styles as Styles

def title(text: str) -> rx.component:
    return rx.heading(
        text,
        size="lg",
        style= Styles.title_style
    )