import reflex as rx
from ..resume_state import ResumeState


def job_match() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.heading(
                "Job Description Matcher",
                size="8",
            ),

            rx.text(
                "Paste a job description below to compare it with your resume.",
                color_scheme="gray",
            ),

            rx.text_area(
                placeholder="Paste the job description here...",
                value=ResumeState.job_description,
                on_change=ResumeState.set_job_description,
                width="800px",
                height="220px",
            ),

            rx.button(
                "Analyze Resume",
                on_click=ResumeState.analyze_job_description,
                color_scheme="blue",
                width="250px",
            ),

            rx.divider(width="800px"),

            rx.heading(
                "ATS Match",
                size="5",
            ),

            rx.progress(
                value=ResumeState.job_match_score,
                max=100,
                width="800px",
            ),

            rx.text(
                ResumeState.job_match_score,
                "% Match",
            ),

            rx.heading(
                "Suggestions",
                size="5",
            ),

            rx.text_area(
                value=ResumeState.job_match_feedback,
                read_only=True,
                width="800px",
                height="180px",
            ),

            spacing="5",
            padding="2em",
            align="center",
        ),
        min_height="100vh",
    )