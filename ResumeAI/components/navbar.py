import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("ResumeAI", size="7"),
        rx.spacer(),
        rx.hstack(
            rx.link("Features", href="#"),
            rx.link("Templates", href="#"),
            rx.button("Login"),
            spacing="5",
        ),
        width="100%",
        padding="1.5em",
    )