import reflex as rx

from ..resume_state import ResumeState
from ..components.copy_button import copy_button
from ..components.form_sections.personal_section import personal_section
from ..components.form_sections.summary_section import summary_section
from ..components.ai_loading_card import ai_loading_card


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
            # ==========================

            rx.box(
                rx.vstack(

                    rx.heading(
                        "Resume Completion",
                        size="4",
                    ),

                    rx.progress(
                        value=ResumeState.completion_percentage,
                        max=100,
                        width="100%",
                    ),

                    rx.hstack(
                        rx.text("Completed Sections:"),
                        rx.text(ResumeState.completed_sections),
                        rx.text("/"),
                        rx.text("10"),
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

            personal_section(),

            # ==========================
            # Professional Summary
            # ==========================

            summary_section(),

            # ==========================
            # Education
            # ==========================

            form_heading("Education"),

            rx.vstack(

                rx.foreach(
                    ResumeState.education_entries,

                    lambda entry, index: rx.box(

                        rx.vstack(

                            rx.hstack(

                                rx.heading(
                                    "Education",
                                    size="3",
                                ),

                                rx.cond(
                                    ResumeState.education_entries.length()
                                    > 1,

                                    rx.button(
                                        "🗑 Remove",
                                        on_click=lambda: (
                                            ResumeState.remove_education(
                                                index
                                            )
                                        ),
                                        color_scheme="red",
                                        size="2",
                                    ),
                                ),

                                justify="between",
                                width="100%",
                            ),

                            # ==========================
                            # Institution
                            # ==========================

                            rx.input(
                                placeholder=(
                                    "School / College / University"
                                ),
                                value=entry["institution"],
                                on_change=lambda value: (
                                    ResumeState.set_education_field(
                                        index,
                                        "institution",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Location
                            # ==========================

                            rx.input(
                                placeholder="Location",
                                value=entry["location"],
                                on_change=lambda value: (
                                    ResumeState.set_education_field(
                                        index,
                                        "location",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Qualification
                            # ==========================

                            rx.input(
                                placeholder=(
                                    "Qualification "
                                    "(e.g. B.Tech, Class XII, Class X)"
                                ),
                                value=entry["qualification"],
                                on_change=lambda value: (
                                    ResumeState.set_education_field(
                                        index,
                                        "qualification",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Course / Specialization / Stream
                            # ==========================

                            rx.input(
                                placeholder=(
                                    "Course / Specialization / Stream "
                                    "(e.g. Computer Science, MPC)"
                                ),
                                value=entry["course"],
                                on_change=lambda value: (
                                    ResumeState.set_education_field(
                                        index,
                                        "course",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Years
                            # ==========================

                            rx.hstack(

                                rx.input(
                                    placeholder="Start Year",
                                    value=entry["start_year"],
                                    on_change=lambda value: (
                                        ResumeState.set_education_field(
                                            index,
                                            "start_year",
                                            value,
                                        )
                                    ),
                                    width="50%",
                                ),

                                rx.input(
                                    placeholder="End Year",
                                    value=entry["end_year"],
                                    on_change=lambda value: (
                                        ResumeState.set_education_field(
                                            index,
                                            "end_year",
                                            value,
                                        )
                                    ),
                                    width="50%",
                                ),

                                spacing="3",
                                width="100%",
                            ),

                            # ==========================
                            # Grade
                            # ==========================

                            rx.input(
                                placeholder=(
                                    "CGPA / Percentage "
                                    "(e.g. 7.85/10 or 86.99%)"
                                ),
                                value=entry["grade"],
                                on_change=lambda value: (
                                    ResumeState.set_education_field(
                                        index,
                                        "grade",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            spacing="3",
                            width="100%",
                        ),

                        width=FORM_WIDTH,
                        padding="1em",
                        border="1px solid",
                        border_color="gray.300",
                        border_radius="10px",
                    ),
                ),

                # ==========================
                # Add Another Education
                # ==========================

                rx.button(
                    "➕ Add Education",
                    on_click=ResumeState.add_education,
                    color_scheme="blue",
                    width=FORM_WIDTH,
                ),

                spacing="4",
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

            rx.vstack(

                rx.foreach(
                    ResumeState.experiences,

                    lambda experience, index: rx.box(

                        rx.vstack(

                            # ==========================
                            # Experience Header
                            # ==========================

                            rx.hstack(

                                rx.heading(
                                    "Experience",
                                    size="3",
                                ),

                                rx.cond(
                                    ResumeState.experiences.length()
                                    > 1,

                                    rx.button(
                                        "🗑 Remove",
                                        on_click=lambda: (
                                            ResumeState.remove_experience(
                                                index
                                            )
                                        ),
                                        color_scheme="red",
                                        size="2",
                                    ),
                                ),

                                justify="between",
                                width="100%",
                            ),

                            # ==========================
                            # Company
                            # ==========================

                            rx.input(
                                placeholder="Company Name",
                                value=experience["company"],
                                on_change=lambda value: (
                                    ResumeState.set_experience_field(
                                        index,
                                        "company",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Job Title
                            # ==========================

                            rx.input(
                                placeholder="Job Title",
                                value=experience["job_title"],
                                on_change=lambda value: (
                                    ResumeState.set_experience_field(
                                        index,
                                        "job_title",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Duration
                            # ==========================

                            rx.input(
                                placeholder=(
                                    "Duration "
                                    "(e.g. Jan 2025 - Present)"
                                ),
                                value=experience["duration"],
                                on_change=lambda value: (
                                    ResumeState.set_experience_field(
                                        index,
                                        "duration",
                                        value,
                                    )
                                ),
                                width="100%",
                            ),

                            # ==========================
                            # Description
                            # ==========================

                            rx.text_area(
                                placeholder=(
                                    "Describe your responsibilities "
                                    "and achievements..."
                                ),
                                value=experience["description"],
                                on_change=lambda value: (
                                    ResumeState.set_experience_field(
                                        index,
                                        "description",
                                        value,
                                    )
                                ),
                                width="100%",
                                height="120px",
                            ),

                            # ==========================
                            # Improve with AI
                            # ==========================

                            rx.button(
                                rx.cond(
                                    ResumeState.is_generating_experience,
                                    "⏳ Analyzing...",
                                    "✨ Improve with AI",
                                ),
                                on_click=lambda: (
                                    ResumeState.improve_experience(
                                        index
                                    )
                                ),
                                color_scheme="green",
                                width="250px",
                                disabled=(
                                    ResumeState.is_generating_experience
                                ),
                            ),

                            # ==========================
                            # AI Loading Card
                            # ==========================

                            rx.cond(
                                (
                                    ResumeState.is_generating_experience
                                )
                                & (
                                    ResumeState.improving_experience_index
                                    == index
                                ),

                                ai_loading_card(
                                    ResumeState.experience_status,
                                ),
                            ),

                            # ==========================
                            # AI Improved Experience
                            # ==========================

                            rx.cond(
                                (
                                    ResumeState.improved_experience
                                    != ""
                                )
                                & (
                                    ResumeState.improving_experience_index
                                    == index
                                ),

                                rx.vstack(

                                    rx.hstack(

                                        rx.heading(
                                            "AI Improved Experience",
                                            size="4",
                                        ),

                                        copy_button(
                                            ResumeState.improved_experience,
                                        ),

                                        justify="between",
                                        width="100%",
                                    ),

                                    rx.button(
                                        "Use This Version",
                                        on_click=lambda: (
                                            ResumeState.accept_improved_experience(
                                                index
                                            )
                                        ),
                                        color_scheme="blue",
                                    ),

                                    rx.text_area(
                                        value=(
                                            ResumeState.improved_experience
                                        ),
                                        read_only=True,
                                        width="100%",
                                        height="180px",
                                    ),

                                    spacing="3",
                                    width="100%",
                                ),
                            ),

                            spacing="3",
                            width="100%",
                        ),

                        width=FORM_WIDTH,
                        padding="1em",
                        border="1px solid",
                        border_color="gray.300",
                        border_radius="10px",
                    ),
                ),

                # ==========================
                # Add Another Experience
                # ==========================

                rx.button(
                    "➕ Add Another Experience",
                    on_click=ResumeState.add_experience,
                    color_scheme="blue",
                    width=FORM_WIDTH,
                ),

                spacing="4",
                width=FORM_WIDTH,
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
            # Languages
            # ==========================

            form_heading("Languages"),

            rx.text_area(
                placeholder="English, Telugu, Hindi",
                value=ResumeState.languages,
                on_change=ResumeState.set_languages,
                width=FORM_WIDTH,
                height="80px",
            ),

            # ==========================
            # Export Buttons
            # ==========================

            rx.hstack(

                rx.button(
                    "📄 Export PDF",
                    on_click=ResumeState.export_pdf,
                    color_scheme="purple",
                    width="195px",
                    size="3",
                ),

                rx.button(
                    "📝 Export DOCX",
                    on_click=ResumeState.export_docx,
                    color_scheme="green",
                    width="195px",
                    size="3",
                ),

                spacing="3",
                width=FORM_WIDTH,
            ),

            # ==========================
            # Save Resume
            # ==========================

            rx.button(
                "💾 Save Resume",
                on_click=ResumeState.save_resume,
                color_scheme="blue",
                width=FORM_WIDTH,
                size="3",
            ),

            # ==========================
            # Load Resume
            # ==========================

            rx.button(
                "📂 Load Resume",
                on_click=ResumeState.load_resume,
                color_scheme="orange",
                width=FORM_WIDTH,
                size="3",
            ),

            # ==========================
            # New Resume
            # ==========================

            rx.button(
                "🆕 New Resume",
                on_click=ResumeState.reset_resume,
                color_scheme="red",
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