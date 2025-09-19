"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.text("hello World", color="orange")


app = rx.App()
app.add_page(index)
