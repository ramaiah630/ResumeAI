import reflex as rx
from ...resume_state import ResumeState


def section_heading(title: str) -> rx.Component:
    """Reusable section heading."""
    return rx.heading(
        title,
        size="4",
        margin_top="20px",
        margin_bottom="10px",
    )


def preview_text(value, placeholder) -> rx.Component:
    """Show placeholder when value is empty."""
    return rx.text(
        rx.cond(
            value != "",
            value,
            placeholder,
        )
    )

def classic_template() -> rx.Component:
    return rx.card(
        rx.box(
            rx.vstack(

               

                # ==========================
                # Header
                # ==========================
                rx.heading(
                    rx.cond(
                        ResumeState.full_name != "",
                        ResumeState.full_name,
                        "Your Name",
                    ),
                    size="8",
                    text_align="center",
                    width="100%",
                ),

                rx.hstack(
                    preview_text(
                        ResumeState.email,
                        "email@example.com",
                    ),

                    rx.spacer(),

                    preview_text(
                        ResumeState.phone,
                        "+91 XXXXX XXXXX",
                    ),

                    width="100%",
                ),

                # ==========================
                # Summary
                # ==========================
                section_heading("Professional Summary"),

                preview_text(
                    ResumeState.summary,
                    "Write a short professional summary...",
                ),

                # ==========================
                # Education
                # ==========================
                section_heading("Education"),

                preview_text(
                    ResumeState.education,
                    "Bachelor of Technology",
                ),

                # ==========================
                # Skills
                # ==========================
                section_heading("Skills"),

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

                # ==========================
                # Experience
                # ==========================
                section_heading("Experience"),

                rx.text(
                    rx.cond(
                        ResumeState.job_title != "",
                        ResumeState.job_title,
                        "Software Engineer",
                    ),
                    font_weight="bold",
                ),

                preview_text(
                    ResumeState.company,
                    "ABC Technologies",
                ),

                rx.text(
                    rx.cond(
                        ResumeState.duration != "",
                        ResumeState.duration,
                        "Jan 2025 - Present",
                    ),
                    color="gray",
                ),

                preview_text(
                    ResumeState.experience_description,
                    "Worked on AI-powered web applications and automation tools.",
                ),

                section_heading("Projects"),

                rx.text(
                    rx.cond(
                        ResumeState.project_title != "",
                        ResumeState.project_title,
                        "AI Resume Builder",
                    ),
                    font_weight="bold",
                ),

                preview_text(
                    ResumeState.project_technologies,
                    "Python • Reflex • Gemini AI",
                ),

                preview_text(
                    ResumeState.project_github,
                    "https://github.com/username/resumeai",
                ),

                preview_text(
                    ResumeState.project_description,
                    "An AI-powered resume builder with live preview and PDF export.",
                ),

                # ==========================
                # Certifications
                # ==========================
                rx.cond(
                    ResumeState.certification_name != "",
                    rx.vstack(
                        section_heading("Certifications"),

                        rx.text(
                            ResumeState.certification_name,
                            font_weight="bold",
                        ),

                        preview_text(
                            ResumeState.certification_organization,
                            "Issuing Organization",
                        ),

                        preview_text(
                            ResumeState.certification_issue_date,
                            "Issue Date",
                        ),

                        rx.cond(
                            ResumeState.certification_credential_id != "",
                            rx.text(
                                f"Credential ID: {ResumeState.certification_credential_id}",
                                color="gray",
                            ),
                        ),

                        align="start",
                        spacing="2",
                        width="100%",
                    ),
                ),


                # ==========================
                # Languages
                # ==========================

                rx.cond(
                    ResumeState.languages != "",
                        rx.vstack(
                            section_heading("Languages"),

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

                        align="start",
                        spacing="2",
                        width="100%",
                ),
            ),       


                # ==========================
                # ATS Score
                # ==========================
                section_heading("ATS Score"),

                rx.progress(
                    value=ResumeState.ats_score,
                    width="100%",
                ),

                rx.text(
                    ResumeState.ats_score,
                    " % Match",
                    color_scheme="green",
                    font_weight="bold",
                ),

                # ==========================
                # ATS Suggestions
                # ==========================
                section_heading("ATS Suggestions"),

                rx.vstack(

                    rx.cond(
                        ResumeState.summary == "",
                        rx.text("• Add a professional summary.", color="orange"),
                    ),

                    rx.cond(
                        ResumeState.skills == "",
                        rx.text("• Add your skills.", color="orange"),
                    ),

                    rx.cond(
                        ResumeState.company == "",
                        rx.text("• Add work experience.", color="orange"),
                    ),

                    rx.cond(
                        ResumeState.project_title == "",
                        rx.text("• Add at least one project.", color="orange"),
                    ),

                    rx.cond(
                        ResumeState.certification_name == "",
                        rx.text("• Add certifications.", color="orange"),
                    ),

                    rx.cond(
                        ResumeState.languages == "",
                        rx.text("• Add languages you know.", color="orange"),
                    ),

                    align="start",
                    spacing="2",
                    width="100%",
                ),

                spacing="5",
                width="100%",
            ),

            width="210mm",
            min_height="297mm",
            bg="white",
            color="black",
            padding="40px",
            border_radius="8px",
            box_shadow="lg",
            overflow="hidden",
        ),

        width="100%",
        max_width="900px",
    )