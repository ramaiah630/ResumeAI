import reflex as rx
from ..resume_state import ResumeState


def form_heading(title: str) -> rx.Component:
    """Reusable section heading."""
    return rx.heading(
        title,
        size="4",
        width="400px",
        align="left",
    )


def resume_form() -> rx.Component:
    return rx.center(
        rx.vstack(

            # ==========================
            # Page Title
            # ==========================
            rx.heading(
                "Resume Builder",
                size="8",
            ),

            # ==========================
            # Personal Information
            # ==========================
            form_heading("Personal Information"),

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

            # ==========================
            # Professional Summary
            # ==========================
            form_heading("Professional Summary"),

            rx.text_area(
                placeholder="Write a short professional summary...",
                value=ResumeState.summary,
                on_change=ResumeState.set_summary,
                width="400px",
                height="120px",
            ),

            # ==========================
            # Education
            # ==========================
            form_heading("Education"),

            rx.input(
                placeholder="B.Tech in Computer Science",
                value=ResumeState.education,
                on_change=ResumeState.set_education,
                width="400px",
            ),

            # ==========================
            # Skills
            # ==========================
            form_heading("Skills"),

            rx.text_area(
                placeholder="Python, React, SQL, Git",
                value=ResumeState.skills,
                on_change=ResumeState.set_skills,
                width="400px",
                height="100px",
            ),

            # ==========================
            # Experience
            # ==========================
            form_heading("Experience"),

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
                placeholder="Describe your responsibilities and achievements...",
                value=ResumeState.experience_description,
                on_change=ResumeState.set_experience_description,
                width="400px",
                height="120px",
            ),

            form_heading("Projects"),

            rx.input(
                placeholder="Project Title",
                value=ResumeState.project_title,
                on_change=ResumeState.set_project_title,
                width="400px",
            ),

            rx.input(
                placeholder="Technologies Used",
                value=ResumeState.project_technologies,
                on_change=ResumeState.set_project_technologies,
                width="400px",
            ),

            rx.input(
                placeholder="GitHub Repository",
                value=ResumeState.project_github,
                on_change=ResumeState.set_project_github,
                width="400px",
            ),

            rx.text_area(
                placeholder="Describe the project...",
                value=ResumeState.project_description,
                on_change=ResumeState.set_project_description,
                width="400px",
                height="120px",
            ),

            # ==========================
            # Generate Button
            # ==========================
            rx.button(
                "Generate Resume",
                color_scheme="purple",
                width="400px",
            ),

            spacing="5",
            padding_y="2em",
        ),
        min_height="100vh",
    )