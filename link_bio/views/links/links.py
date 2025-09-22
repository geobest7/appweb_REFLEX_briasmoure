import reflex as rx
from link_bio.components.link_button import  link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub", "https://github.com/geobest7"),
        link_button("LinkedIn", "https://www.linkedin.com/in/alessandro-febbrai-b239021a2/"),
        link_button("Infojobs", "https://www.linkedin.com/in/alessandro-febbrai-b239021a2/")
    )