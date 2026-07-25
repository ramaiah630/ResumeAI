import reflex as rx
from ..resume_state import ResumeState


def template_selector() -> rx.Component:
    return rx.vstack(

        rx.heading(
            "Choose Resume Template",
            size="4",
        ),

        rx.select(
            ["classic", "modern", "minimal"],
            value=ResumeState.selected_template,
            on_change=ResumeState.set_selected_template,
            width="250px",
        ),

        spacing="3",
        align="start",
    )