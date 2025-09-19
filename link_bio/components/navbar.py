import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Alessandro Febbrai",
            height="40px",
            color="white"
        ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        adding_y="8px",
        z_index="999"
    )