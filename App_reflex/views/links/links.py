import reflex as rx
from App_reflex.componentes.link_button import link_button
from App_reflex.componentes.title import title
from App_reflex.styles.styles import size as size


def links() -> rx.component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button("GitHub", "https://github.com/"),
        link_button("Youtube", "https://www.youtube.com"),
        link_button("Facebook", "https://www.facebook.com"),
        link_button("linkedin", "https://co.linkedin.com/"),
        width="100%",
        spacing=size.MEDIUM.value,
        
    )
    
   