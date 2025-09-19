import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AF", size="9", radius="full")

    )