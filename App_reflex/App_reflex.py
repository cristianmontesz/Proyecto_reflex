# Creacion app 
import reflex as rx
from componentes.navbar import navbar
from views.header.header import header
from views.links.links import links
from componentes.footer import footer
from views.sponsors.sponsors import sponsors
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
