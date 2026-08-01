import reflex as rx
from ...resume_state import ResumeState


def minimal_template() -> rx.Component:
    return rx.box(

        rx.text(
            ResumeState.full_name,
            font_size="2.4em",
            font_weight="bold",
        ),

        rx.text(
            ResumeState.professional_title,
            color="black",
            font_size="1.2em",
        ),

        rx.hstack(
            rx.text(ResumeState.email),
            rx.text("|"),
            rx.text(ResumeState.phone),
            spacing="3",
        ),

        rx.divider(margin_y="1.5em"),

        # Summary
        rx.heading("Professional Summary", size="4"),
        rx.text(
            ResumeState.summary,
            white_space="pre-wrap",
        ),

        rx.divider(margin_y="1.5em"),

        # Education
        rx.heading("Education", size="4"),
        rx.text(
            ResumeState.education,
            white_space="pre-wrap",
        ),

        rx.divider(margin_y="1.5em"),

        # Experience
        rx.heading("Experience", size="4"),

        rx.text(
            ResumeState.job_title,
            font_weight="bold",
        ),

        rx.text(ResumeState.company),

        rx.text(
            ResumeState.duration,
            color="gray",
        ),

        rx.text(
            ResumeState.experience_description,
            white_space="pre-wrap",
        ),

        rx.divider(margin_y="1.5em"),

        # Projects
        rx.heading("Projects", size="4"),

        rx.text(
            ResumeState.project_title,
            font_weight="bold",
        ),

        rx.text(
            ResumeState.project_technologies,
            color="gray",
        ),

        rx.text(
            ResumeState.project_description,
            white_space="pre-wrap",
        ),

        rx.divider(margin_y="1.5em"),

        # Skills
        rx.heading("Skills", size="4"),

        rx.box(height="10px"),

        rx.flex(
            rx.foreach(
                ResumeState.skills_list,
                lambda skill: rx.badge(
                    skill,
                    variant="soft",
                    radius="full",
                ),
            ),
            wrap="wrap",
            spacing="2",
        ),

        width="100%",
        max_width="850px",
        padding="3em",
        background="white",
        color="black",
        border="1px solid #e5e7eb",
        border_radius="8px",
    )