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
            rx.input(
                placeholder="Education (e.g. B.Tech in Computer Science)",
                value=ResumeState.education,
                on_change=ResumeState.set_education,
                width="400px",
            ),
            rx.text_area(
                placeholder="Skills (comma separated)\nExample: Python, React, SQL",
                value=ResumeState.skills,
                on_change=ResumeState.set_skills,
                width="400px",
                height="100px",
            ),
            rx.heading(
                "Experience",
                size="4",
            ),

            rx.input(
                placeholder="Company Name",
                value=ResumeState.company,
                on_change=ResumeState.set_company,
                width="400px",
            ),

            rx.input(
                placeholder="Job Title",
                value=ResumeState.job_title,
                on_change=ResumeState.set_job_title,
                width="400px",
            ),

            rx.input(
                placeholder="Duration (e.g. Jan 2025 - Present)",
                value=ResumeState.duration,
                on_change=ResumeState.set_duration,
                width="400px",
            ),

            rx.text_area(
                placeholder="Describe your work...",
                value=ResumeState.experience_description,
                on_change=ResumeState.set_experience_description,
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