import reflex as rx
from ...resume_state import ResumeState
from ..copy_button import copy_button
from ..ai_loading_card import ai_loading_card

FORM_WIDTH = "400px"


def summary_section() -> rx.Component:
    return rx.vstack(

        rx.heading(
            "Professional Summary",
            size="4",
            width=FORM_WIDTH,
            align="left",
        ),

        rx.text_area(
            placeholder="Write a short professional summary...",
            value=ResumeState.summary,
            on_change=ResumeState.set_summary,
            width=FORM_WIDTH,
            height="120px",
        ),

        rx.hstack(

            rx.button(
                rx.cond(
                    ResumeState.is_generating_summary,
                    "⏳ Generating...",
                    "✨ Generate AI Summary",
                ),
                on_click=ResumeState.generate_ai_summary,
                color_scheme="green",
                width="250px",
                disabled=ResumeState.is_generating_summary,
            ),

            copy_button(
                ResumeState.summary,
            ),

            spacing="3",
        ),

        rx.cond(
            ResumeState.is_generating_summary,
            ai_loading_card(
                ResumeState.summary_status,
            ),
        ),

        spacing="3",
        align="start",
        width="100%",
    )