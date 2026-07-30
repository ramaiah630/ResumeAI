import reflex as rx

def modern_template() -> rx.Component:
    return rx.box(
        rx.heading("Modern Template", size="6"),
        rx.text("Modern template coming soon."),
        padding="2em",
    )