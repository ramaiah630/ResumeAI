import reflex as rx
from ..resume_state import ResumeState


def cover_letter() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.heading(
                "AI Cover Letter Generator",
                size="8",
            ),

            rx.text_area(
                placeholder="Paste the Job Description here (Optional)",
                value=ResumeState.job_description,
                on_change=ResumeState.set_job_description,
                width="800px",
                height="180px",
            ),

            rx.button(
                "✨ Generate Cover Letter",
                on_click=ResumeState.generate_cover_letter,
                color_scheme="green",
                width="300px",
            ),

            rx.text_area(
                value=ResumeState.cover_letter,
                width="800px",
                height="500px",
                read_only=True,
            ),

            spacing="5",
            padding="2em",
            align="center",
        ),
        min_height="100vh",
    )