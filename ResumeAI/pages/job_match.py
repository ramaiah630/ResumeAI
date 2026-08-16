import reflex as rx
from ..resume_state import ResumeState
from ..components.ai_loading_card import ai_loading_card


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
                rx.cond(
                    ResumeState.is_analyzing_job,
                    "⏳ Analyzing...",
                    "🔎 Analyze Resume",
                ),
                on_click=ResumeState.analyze_job_description,
                color_scheme="blue",
                width="250px",
                disabled=ResumeState.is_analyzing_job,
            ),

            rx.cond(
                ResumeState.is_analyzing_job,
                ai_loading_card(
                    ResumeState.job_match_status,
                ),
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
                "✅ Matched Skills",
                size="5",
            ),

            rx.flex(
                rx.foreach(
                    ResumeState.matched_skills,
                    lambda skill: rx.badge(
                        skill.title(),
                        color_scheme="green",
                        variant="solid",
                    ),
                ),
                wrap="wrap",
                spacing="2",
            ),
            rx.heading(
                "❌ Missing Skills",
                size="5",
            ),

            rx.flex(
                rx.foreach(
                    ResumeState.missing_skills,
                    lambda skill: rx.badge(
                        skill.title(),
                        color_scheme="red",
                        variant="solid",
                    ),
                ),
                wrap="wrap",
                spacing="2",
            ),

            rx.heading(
                "📌 Extra Skills",
                size="5",
            ),

            rx.flex(
                rx.foreach(
                    ResumeState.extra_skills,
                    lambda skill: rx.badge(
                        skill.title(),
                        color_scheme="blue",
                        variant="soft",
                    ),
                ),
                wrap="wrap",
                spacing="2",
            ),

            rx.heading(
                "Suggestions",
                size="5",
            ),

            rx.text(
                ResumeState.job_match_feedback,
                white_space="pre-wrap",
            ),

            spacing="5",
            padding="2em",
            align="center",
        ),
        min_height="100vh",
    )