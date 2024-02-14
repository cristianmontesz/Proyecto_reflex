import reflex as rx
from App_reflex.styles.styles import size as size
from App_reflex.styles.Colors import TextColor as textcolor
from App_reflex.styles.Colors import color as color
import App_reflex.styles.styles as Styles

def navbar() -> rx. component: 
   return rx.hstack(
       rx.box(
         rx.span("APP - ", color=color.BACKGROUND.value),
         rx.span("REFLEX", color=color.BACKGROUND.value),
         styles=Styles.Navbar_title_style
          
       ),
       position="sticky",
       bg= color.PRIMARY.value,
       padding_x=size.SMALL.value,
       padding_y=size.SMALL.value,
       z_index="999",
       top="0"
       
    )
