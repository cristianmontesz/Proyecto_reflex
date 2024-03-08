import reflex as rx
import App_reflex.styles.styles  as styles
from App_reflex.componentes.link_button import link_button
from App_reflex.componentes.title import title
from App_reflex.styles.styles import size as size
import App_reflex.constants as const

def links() -> rx.Component:
    return rx.chakra.vstack(
        title("Cursos de programacion: "),
        link_button(
            "Capacitate para el empleo",
            "Curso programacion orientada a objetos", 
            "capacitate.png",
            const.CAPACITATE_URL,
            
        ),
        link_button(
            "Youtube",
            "Curso basico de linux(ubuntu)",
            "/iconos/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        link_button(
            "Python",
            "Aprende a programar en python ", 
            "iconos/python.svg",
            const.PYTHON_COURSE_URL
        ),
        link_button(
            "Github",
            "Ingresa a github para guardar tu repositorio", 
            "iconos/github.svg",
            const.GIT_COURSE_URL
        ),
        title("Recursos y mas: "),
        link_button(
            "Github",
            "Ingresa a github para guardar tu repositorio", 
            "iconos/github.svg",
            const.GITHUB_URL
        ),
        link_button(
            "Python",
            "Curso Fundamentos de Python ",
            "/iconos/python.svg",
            const.CISCO_URL
        ),
        link_button(
            "Redes",
            "Aprende Conceptos Basicos en Redes ", 
            "iconos/Redes.svg",
            const.CISCO_SECUNDARY_URL
        ),
        title("Evaulacion: "),
        link_button(
            "Retos de Programacion",
            "Desarrolla tu logica y Acepta el reto  ", 
            "iconos/Retos.svg",
            const.CODE_CHALLENGES_URL
        ),
        width="100%",
        align_items="start",  
        spacing=size.MEDIUM.value,
    )

   