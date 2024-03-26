# Creacion app 
import reflex as rx
from App_reflex.componentes.navbar import navbar
from App_reflex.views.header.header import header
from App_reflex.views.links.links import links
from App_reflex.componentes.footer import footer
from App_reflex.views.sponsors.sponsors import sponsors
import App_reflex.styles.styles as styles


class State(rx.State):
  pass


def index() -> rx.Component:
  return rx.chakra.box(
    navbar(),
      rx.chakra.center(
        rx.chakra.vstack(
          header(),
          links(),
          sponsors(),
          max_width=styles.max_width,
          width="100%",
          margin_y=styles.size.DEFAULT.value,
          padding_bottom="30em"
        ),
      ),
      footer()
  )




# Create app instance and add index page.
app = rx.App(
   style=styles.BASE_STYLE,
   
)
app.add_page(index)
app.compile()