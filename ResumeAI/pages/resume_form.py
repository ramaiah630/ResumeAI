import reflex as rx
from ..resume_state import ResumeState

def resume_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "Resume Builder",
                size="8",
            ),
            rx.input(
               placeholder="Full Name",
               value=ResumeState.full_name,
               on_change=ResumeState.set_full_name,
               width="400px",
            ),

            rx.input(
                placeholder="Email",
                value=ResumeState.email,
                on_change=ResumeState.set_email,
                width="400px",
            ),

            rx.input(
                placeholder="Phone Number",
                value=ResumeState.phone,
                on_change=ResumeState.set_phone,
                width="400px",
            ),

            rx.text_area(
                placeholder="Professional Summary",
                value=ResumeState.summary,
                on_change=ResumeState.set_summary,
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