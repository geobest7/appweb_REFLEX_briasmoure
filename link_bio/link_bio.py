"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles



class State(rx.State):
    """The app state."""
pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                padding="20px",
                margin_y=styles.Spacer.BIG.value,
                align="center"
            )
        ),
        footer()
    )



    


app = rx.App()
app.add_page(index)

