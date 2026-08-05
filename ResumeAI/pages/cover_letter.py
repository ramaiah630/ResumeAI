import reflex as rx
from ..resume_state import ResumeState
from ..components.copy_button import copy_button
from ..components.ai_loading_card import ai_loading_card

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
                rx.cond(
                    ResumeState.is_generating_cover_letter,
                    "⏳ Generating...",
                    "✨ Generate Cover Letter",
                ),
                on_click=ResumeState.generate_cover_letter,
                color_scheme="green",
                width="300px",
                disabled=ResumeState.is_generating_cover_letter,
            ),
            rx.cond(
                ResumeState.is_generating_cover_letter,
                ai_loading_card(
                    ResumeState.cover_letter_status,
                ),
            ),

            rx.vstack(

                rx.hstack(

                    rx.heading(
                        "Generated Cover Letter",
                        size="5",
                    ),

                    copy_button(
                        ResumeState.cover_letter,
                    ),

                    justify="between",
                    width="100%",
                ),

                rx.text_area(
                    value=ResumeState.cover_letter,
                    width="800px",
                    height="500px",
                    read_only=True,
                ),

                spacing="3",
                width="800px",
            ),

            spacing="5",
            padding="2em",
            align="center",
        ),
        min_height="100vh",
    )