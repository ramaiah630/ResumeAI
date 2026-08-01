import reflex as rx
from ..resume_state import ResumeState


def theme_selector() -> rx.Component:
    return rx.vstack(

        rx.heading(
            "Theme Color",
            size="4",
        ),
        rx.select(
            ["Blue", "Green", "Purple", "Red", "Black"],
            value=ResumeState.selected_theme,
            on_change=ResumeState.change_theme,
            width="250px",
        ),

        spacing="3",
        align="start",
    )