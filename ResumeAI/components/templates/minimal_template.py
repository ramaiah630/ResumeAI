import reflex as rx

def minimal_template() -> rx.Component:
    return rx.box(
        rx.heading("Minimal Template", size="6"),
        rx.text("Minimal template coming soon."),
        padding="2em",
    )