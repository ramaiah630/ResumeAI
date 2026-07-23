import reflex as rx
from .components.navbar import navbar

class State(rx.State):
    """Application state."""
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.heading(
                    "Build AI-Powered Professional Resumes",
                    size="9",
                    text_align="center",
                ),
                rx.text(
                    "Create ATS-friendly resumes in minutes using AI.",
                    size="5",
                    text_align="center",
                ),
                rx.hstack(
                    rx.button(
                        "Create Resume",
                        size="3",
                    ),
                    rx.button(
                        "View Templates",
                        variant="outline",
                        size="3",
                    ),
                    spacing="4",
                ),
                spacing="6",
                align="center",
            ),
            height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
