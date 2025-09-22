"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links



class State(rx.State):
    """The app state."""
pass


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        spacing="6",            
        align="center",       
        width="100%"
        )
    


app = rx.App()
app.add_page(index)

