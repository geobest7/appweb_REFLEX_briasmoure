import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AF", size="9", radius="full"),
        rx.text(
            "Soy un chico italiano que vive en Barcelona desde 2020 y estoy en el camino de convertirme en programador. "
            "He realizado cursos de Python y además tengo conocimientos en Reflex, Flask, Django, Numpy y Pandas. "
            "También he explorado el mundo de JavaScript, trabajando con Vue.js y Adonis.js. Me gusta experimentar "
            "con inteligencia artificial y manejo herramientas como Windsurf AI, en especial el modelo Claude Sonnet 4. "
            "Sé que el camino para ser programador es largo y requiere mucha práctica y aprendizaje constante, "
            "por eso he creado esta web con Reflex: un espacio donde puedo poner en práctica mis conocimientos "
            "y seguir creciendo paso a paso.",
            text_align="center",
            margin_top="1em"
        ),
        align="center"
    )