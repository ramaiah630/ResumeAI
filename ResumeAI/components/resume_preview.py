import reflex as rx
from ..resume_state import ResumeState

def resume_preview() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.avatar(name="John Smith"),
                rx.vstack(
                    rx.heading(
                        rx.cond(
                            ResumeState.full_name != "",
                            ResumeState.full_name,
                            "John Smith",
                        ),
                        size="4",
                    ),
                    rx.text(
                        ResumeState.email,
                        color_scheme="gray"
                    ),
                    spacing="1",
                    align="start",
                ),
                width="100%",
            ),

            rx.divider(),

            rx.heading("Skills", size="3"),

            rx.badge("Python"),
            rx.badge("React"),
            rx.badge("SQL"),
            rx.badge("Git"),
            rx.badge("AI"),

            rx.divider(),

            rx.text("ATS Score", weight="bold"),

            rx.progress(value=98),

            rx.text(
                "98% Match",
                color_scheme="green",
                weight="bold",
            ),

            spacing="4",
            width="100%",
        ),
        width="360px",
        padding="2em",
    )