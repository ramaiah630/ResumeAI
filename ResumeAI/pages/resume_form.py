import reflex as rx


def resume_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Resume Builder",
                size="8",
            ),

            rx.input(
                placeholder="Full Name",
                width="400px",
            ),

            rx.input(
                placeholder="Email",
                width="400px",
            ),

            rx.input(
                placeholder="Phone Number",
                width="400px",
            ),

            rx.text_area(
                placeholder="Professional Summary",
                width="400px",
                height="120px",
            ),

            rx.button(
                "Generate Resume",
                color_scheme="purple",
                width="400px",
            ),

            spacing="5",
        ),
        min_height="100vh",
    )