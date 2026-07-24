import reflex as rx
from ..resume_state import ResumeState

# ==========================
# Constants
# ==========================
FORM_WIDTH = "400px"


def form_heading(title: str) -> rx.Component:
    """Reusable section heading."""
    return rx.heading(
        title,
        size="4",
        width=FORM_WIDTH,
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
            # Resume Completion Card
        rx.box(
    rx.vstack(
        rx.heading(
            "Resume Completion",
            size="4",
        ),

        rx.progress(
            ResumeState.completion_percentage,
            max=100,
            width="100%",
        ),

        rx.hstack(
            rx.text("Completed Sections:"),
            rx.text(ResumeState.completed_sections),
            rx.text("/"),
            rx.text("9"),
        ),

        rx.hstack(
            rx.text("Completion:"),
            rx.text(ResumeState.completion_percentage),
            rx.text("%"),
            spacing="2",
        ),

        spacing="3",
        width="100%",
        align="start",
    ),

    width=FORM_WIDTH,
    padding="1em",
    border="1px solid",
    border_color="gray.300",
    border_radius="12px",
),

            # ==========================
            # Personal Information
            # ==========================
            form_heading("Personal Information"),

            rx.input(
                placeholder="Full Name",
                value=ResumeState.full_name,
                on_change=ResumeState.set_full_name,
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="Email Address",
                value=ResumeState.email,
                on_change=ResumeState.set_email,
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="Phone Number",
                value=ResumeState.phone,
                on_change=ResumeState.set_phone,
                width=FORM_WIDTH,
            ),

            # ==========================
            # Professional Summary
            # ==========================
            form_heading("Professional Summary"),

            rx.text_area(
                placeholder="Write a short professional summary...",
                value=ResumeState.summary,
                on_change=ResumeState.set_summary,
                width=FORM_WIDTH,
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
                width=FORM_WIDTH,
            ),

            # ==========================
            # Skills
            # ==========================
            form_heading("Skills"),

            rx.text_area(
                placeholder="Python, React, SQL, Git",
                value=ResumeState.skills,
                on_change=ResumeState.set_skills,
                width=FORM_WIDTH,
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
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="Job Title",
                value=ResumeState.job_title,
                on_change=ResumeState.set_job_title,
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="Duration (e.g. Jan 2025 - Present)",
                value=ResumeState.duration,
                on_change=ResumeState.set_duration,
                width=FORM_WIDTH,
            ),

            rx.text_area(
                placeholder="Describe your responsibilities and achievements...",
                value=ResumeState.experience_description,
                on_change=ResumeState.set_experience_description,
                width=FORM_WIDTH,
                height="120px",
            ),

            # ==========================
            # Projects
            # ==========================
            form_heading("Projects"),

            rx.input(
                placeholder="Project Title",
                value=ResumeState.project_title,
                on_change=ResumeState.set_project_title,
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="Technologies Used",
                value=ResumeState.project_technologies,
                on_change=ResumeState.set_project_technologies,
                width=FORM_WIDTH,
            ),

            rx.input(
                placeholder="GitHub Repository",
                value=ResumeState.project_github,
                on_change=ResumeState.set_project_github,
                width=FORM_WIDTH,
            ),

            rx.text_area(
                placeholder="Describe the project...",
                value=ResumeState.project_description,
                on_change=ResumeState.set_project_description,
                width=FORM_WIDTH,
                height="120px",
            ),

            # ==========================
            # Certifications
            # ==========================
            form_heading("Certifications"),

rx.input(
    placeholder="Certification Name",
    value=ResumeState.certification_name,
    on_change=ResumeState.set_certification_name,
    width=FORM_WIDTH,
),

rx.input(
    placeholder="Issuing Organization",
    value=ResumeState.certification_organization,
    on_change=ResumeState.set_certification_organization,
    width=FORM_WIDTH,
),

rx.input(
    placeholder="Issue Date",
    value=ResumeState.certification_issue_date,
    on_change=ResumeState.set_certification_issue_date,
    width=FORM_WIDTH,
),

rx.input(
    placeholder="Credential ID (Optional)",
    value=ResumeState.certification_credential_id,
    on_change=ResumeState.set_certification_credential_id,
    width=FORM_WIDTH,
),

            # ==========================
            # Generate Resume Button
            # ==========================
            rx.button(
                "Generate Resume",
                color_scheme="purple",
                width=FORM_WIDTH,
                size="3",
            ),

            spacing="6",
            padding_y="2em",
            align="center",
        ),
        min_height="100vh",
        padding="2em",
    )