import reflex as rx
from ..resume_state import ResumeState


def score_card() -> rx.Component:

    return rx.card(

        rx.vstack(

            rx.text(
                "Resume Score",
                color="gray",
                size="3",
            ),

            rx.heading(
                ResumeState.resume_score,
                size="9",
                color=ResumeState.resume_score_color,
            ),

            rx.progress(
                value=ResumeState.resume_score_value,
                max=100,
                width="100%",
                color_scheme=ResumeState.resume_score_color,
            ),

            rx.badge(
                "AI Powered ATS Analysis",
                color_scheme="green",
                variant="soft",
            ),

            spacing="5",
            align="center",
            width="100%",
        ),

        flex="1",
        min_width="340px",

        padding="2em",

        border_radius="18px",

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        border="1px solid",

        border_color=rx.color("gray", 4),

        background=rx.color("gray", 1),

        transition="all 0.25s ease",
    )