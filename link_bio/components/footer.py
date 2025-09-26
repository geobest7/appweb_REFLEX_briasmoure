import reflex as rx

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link("Fooooooooooter", href="https://www.youtube.com/watch?v=n2YrGsXJC6Y", is_external=True),
        rx.text("footer")
    )