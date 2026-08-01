import reflex as rx
from ...resume_state import ResumeState


def modern_template() -> rx.Component:
    return rx.box(
        rx.hstack(

            # ==========================
            # LEFT SIDEBAR
            # ==========================
            rx.box(
                rx.center(
                    rx.vstack(

                        rx.avatar(
                            fallback="👤",
                            size="8",
                        ),

                        rx.text(
                            ResumeState.full_name,
                            font_size="1.3em",
                            font_weight="bold",
                            text_align="center",
                        ),

                        rx.text(
                            ResumeState.professional_title,
                            text_align="center",
                        ),

                        spacing="3",
                        align="center",
                    ),
                ),

                rx.divider(margin_y="1.5em"),

                rx.heading(
                    "Contact",
                    size="4",
                    color="#2563eb",
                ),

                rx.vstack(

                    rx.hstack(
                        rx.text("📧"),
                        rx.text(ResumeState.email),
                    ),

                    rx.hstack(
                        rx.text("📱"),
                        rx.text(ResumeState.phone),
                    ),

                    spacing="2",
                    align="start",
                ),

                rx.divider(),

                rx.heading(
                    "Skills",
                    size="4",
                    color="#2563eb",
                ),

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

                rx.divider(),

                rx.heading(
                    "Languages",
                    size="4",
                    color="#2563eb",
                ),

                rx.flex(
                    rx.foreach(
                        ResumeState.languages_list,
                        lambda language: rx.badge(
                            language,
                            variant="soft",
                            radius="full",
                        ),
                    ),
                    wrap="wrap",
                    spacing="2",
                ),

                rx.divider(),

                rx.heading(
                    "Certifications",
                    size="4",
                    color="#2563eb",
                ),

                rx.text(ResumeState.certification_name),
                rx.text(ResumeState.certification_organization),
                rx.text(
                    ResumeState.certification_issue_date,
                    color="gray",
                ),

                width="30%",
                min_height="297mm",
                bg="#0f172a",
                color="white",
                padding="2em",
            ),

            # ==========================
            # RIGHT CONTENT
            # ==========================
            rx.box(

                # Header
                rx.text(
                    ResumeState.full_name,
                    font_size="2.3em",
                    font_weight="bold",
                    color="#2563eb",
                ),

                rx.text(
                    ResumeState.professional_title,
                    font_size="1.2em",
                    color="black",
                ),

                rx.divider(margin_y="1em"),

                # Professional Summary
                rx.heading(
                    "Professional Summary",
                    size="4",
                    color="#2563eb",
                ),

                rx.text(
                    ResumeState.summary,
                    white_space="pre-wrap",
                ),

                rx.divider(margin_y="1.5em"),

                # Education
                rx.heading(
                    "Education",
                    size="4",
                    color="#2563eb",
                ),

                rx.text(
                    ResumeState.education,
                    white_space="pre-wrap",
                ),

                rx.divider(margin_y="1.5em"),

                # Experience
                rx.heading(
                    "Experience",
                    size="4",
                    color="#2563eb",
                ),

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
                rx.heading(
                    "Projects",
                    size="4",
                    color="#2563eb",
                ),

                rx.text(
                    ResumeState.project_title,
                    font_weight="bold",
                ),

                rx.text(
                    ResumeState.project_technologies,
                    color="gray",
                ),

                rx.link(
                    ResumeState.project_github,
                    href=ResumeState.project_github,
                ),

                rx.text(
                    ResumeState.project_description,
                    white_space="pre-wrap",
                ),

                width="70%",
                padding="2em",
                bg="white",
                color="black",
            ),

            spacing="0",
            align="start",
            width="100%",
        ),

        width="100%",
        border="1px solid #d1d5db",
        border_radius="10px",
        overflow="hidden",
        background="white",
    )