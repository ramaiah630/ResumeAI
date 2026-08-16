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
                            rx.cond(
                                ResumeState.full_name != "",
                                ResumeState.full_name,
                                "Your Name",
                            ),
                            font_size="1.3em",
                            font_weight="bold",
                            text_align="center",
                        ),

                        rx.text(
                            rx.cond(
                                ResumeState.professional_title != "",
                                ResumeState.professional_title,
                                "Professional Title",
                            ),
                            text_align="center",
                        ),

                        spacing="3",
                        align="center",
                    ),
                ),

                rx.divider(
                    margin_y="1.5em",
                ),

                # ==========================
                # Contact
                # ==========================

                rx.cond(
                    (ResumeState.email.strip() != "")
                    | (ResumeState.phone.strip() != ""),

                    rx.vstack(

                        rx.divider(
                            margin_y="1.5em",
                        ),

                        rx.heading(
                            "Contact",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.vstack(

                            rx.cond(
                                ResumeState.email.strip() != "",
                                rx.hstack(
                                    rx.text("📧"),
                                    rx.text(ResumeState.email),
                                    spacing="2",
                                ),
                            ),

                            rx.cond(
                                ResumeState.phone.strip() != "",
                                rx.hstack(
                                    rx.text("📱"),
                                    rx.text(ResumeState.phone),
                                    spacing="2",
                                ),
                            ),

                            spacing="2",
                            align="start",
                        ),

                        width="100%",
                        align="start",
                    ),
                ),

                # ==========================
                # Skills
                # ==========================

                rx.cond(
                    ResumeState.skills_list.length() > 0,

                    rx.vstack(

                        rx.divider(),

                        rx.heading(
                            "Skills",
                            size="4",
                            color=ResumeState.theme_color,
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

                        width="100%",
                        align="start",
                    ),
                ),

                # ==========================
                # Languages
                # ==========================

                rx.cond(
                    ResumeState.languages != "",

                    rx.vstack(

                        rx.divider(),

                        rx.heading(
                            "Languages",
                            size="4",
                            color=ResumeState.theme_color,
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

                        width="100%",
                        align="start",
                    ),
                ),

                # ==========================
                # Certifications
                # ==========================

                rx.cond(
                    ResumeState.certification_name != "",

                    rx.vstack(

                        rx.divider(),

                        rx.heading(
                            "Certifications",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.text(
                            ResumeState.certification_name,
                            font_weight="bold",
                        ),

                        rx.cond(
                            ResumeState.certification_organization != "",
                            rx.text(
                                ResumeState.certification_organization,
                            ),
                        ),

                        rx.cond(
                            ResumeState.certification_issue_date != "",
                            rx.text(
                                ResumeState.certification_issue_date,
                                color="gray",
                            ),
                        ),

                        width="100%",
                        align="start",
                        spacing="2",
                    ),
                ),

                # Sidebar width/height
                width="30%",
                
                background="#0f172a",
                color="white",
                padding="2em",
            ),

            # ==========================
            # RIGHT CONTENT
            # ==========================

            rx.box(

                # ==========================
                # Header
                # ==========================

                rx.text(
                    rx.cond(
                        ResumeState.full_name != "",
                        ResumeState.full_name,
                        "Your Name",
                    ),
                    font_size="2.3em",
                    font_weight="bold",
                    color=ResumeState.theme_color,
                ),

                rx.text(
                    rx.cond(
                        ResumeState.professional_title != "",
                        ResumeState.professional_title,
                        "Professional Title",
                    ),
                    font_size="1.2em",
                    color="black",
                ),

                rx.divider(
                    margin_y="1em",
                ),

                # ==========================
                # Professional Summary
                # ==========================

                rx.cond(
                    ResumeState.summary != "",

                    rx.vstack(

                        rx.heading(
                            "Professional Summary",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.text(
                            ResumeState.summary,
                            white_space="pre-wrap",
                        ),

                        rx.divider(
                            margin_y="1.5em",
                        ),

                        width="100%",
                        align="start",
                    ),
                ),

                # ==========================
                # Education
                # ==========================

                rx.cond(
                    ResumeState.education_entries.length() > 0,
                    rx.vstack(
                        rx.heading(
                            "Education",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.foreach(
                            ResumeState.education_entries,

                            lambda entry: rx.vstack(

                                # Institution
                                rx.cond(
                                    entry["institution"] != "",
                                    rx.text(
                                        entry["institution"],
                                        #font_weight="bold",
                                        font_size="1.05em",
                                    ),
                                ),

                                # Location
                                rx.cond(
                                    entry["location"] != "",
                                    rx.text(
                                        entry["location"],
                                        #color="gray",
                                    ),
                                ),

                                # Education details
                                rx.cond(
                                    (
                                        (entry["start_year"] != "")
                                        | (entry["end_year"] != "")
                                        | (entry["qualification"] != "")
                                        | (entry["course"] != "")
                                        | (entry["grade"] != "")
                                    ),

                                    rx.text(
                                        entry["start_year"]
                                        + rx.cond(
                                            (
                                                (entry["start_year"] != "")
                                                & (entry["end_year"] != "")
                                            ),
                                            " – ",
                                            "",
                                        )
                                        + entry["end_year"]
                                        + rx.cond(
                                            (
                                                (entry["qualification"] != "")
                                                | (entry["course"] != "")
                                            ),
                                            " | ",
                                            "",
                                        )
                                        + entry["qualification"]
                                        + rx.cond(
                                            (
                                                (entry["qualification"] != "")
                                                & (entry["course"] != "")
                                            ),
                                            " in ",
                                            "",
                                        )
                                        + entry["course"]
                                        + rx.cond(
                                            entry["grade"] != "",
                                            " | " + entry["grade"],
                                            "",
                                        ),
                                        white_space="pre-wrap",
                                    ),
                                ),

                                spacing="1",
                                width="100%",
                                align="start",
                                padding_bottom="10px",
                            ),
                        ),

                        rx.divider(
                            margin_y="1.5em",
                        ),

                        width="100%",
                        align="start",
                        spacing="3",
                    ),
                ),

                # ==========================
                # Experience
                # ==========================

                rx.cond(
                    ResumeState.experiences.length() > 0,

                    rx.vstack(

                        rx.heading(
                            "Experience",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.foreach(
                            ResumeState.experiences,

                            lambda experience: rx.vstack(

                                # Company
                                rx.cond(
                                    experience["company"] != "",
                                    rx.text(
                                        experience["company"],
                                        font_weight="bold",
                                    ),
                                ),

                                # Job Title
                                rx.cond(
                                    experience["job_title"] != "",
                                    rx.text(
                                        experience["job_title"],
                                    ),
                                ),

                                # Duration
                                rx.cond(
                                    experience["duration"] != "",
                                    rx.text(
                                        experience["duration"],
                                        #color="gray",
                                    ),
                                ),

                                # Description
                                rx.cond(
                                    experience["description"] != "",
                                    rx.text(
                                        experience["description"],
                                        white_space="pre-wrap",
                                    ),
                                ),

                                width="100%",
                                align="start",
                                spacing="2",
                                padding_bottom="12px",
                            ),
                        ),

                        rx.divider(
                            margin_y="1.5em",
                        ),

                        width="100%",
                        align="start",
                        spacing="3",
                    ),
                ),

                # ==========================
                # Projects
                # ==========================

                rx.cond(
                    (ResumeState.project_title != "")
                    | (ResumeState.project_description != ""),

                    rx.vstack(

                        rx.heading(
                            "Projects",
                            size="4",
                            color=ResumeState.theme_color,
                        ),

                        rx.cond(
                            ResumeState.project_title != "",
                            rx.text(
                                ResumeState.project_title,
                                font_weight="bold",
                            ),
                        ),

                        rx.cond(
                            ResumeState.project_technologies != "",
                            rx.text(
                                ResumeState.project_technologies,
                                color="gray",
                            ),
                        ),

                        rx.cond(
                            ResumeState.project_github != "",
                            rx.link(
                                ResumeState.project_github,
                                href=ResumeState.project_github,
                                color=ResumeState.theme_color,
                            ),
                        ),

                        rx.cond(
                            ResumeState.project_description != "",
                            rx.text(
                                ResumeState.project_description,
                                white_space="pre-wrap",
                            ),
                        ),

                        width="100%",
                        align="start",
                        spacing="2",
                    ),
                ),

                width="70%",
                min_height="297mm",
                padding="2em",
                background="white",
                color="black",
            ),

            # ==========================
            # MAIN LAYOUT
            # ==========================

            spacing="0",
            align="stretch",
            width="100%",
        ),

        width="100%",
        border="1px solid #d1d5db",
        border_radius="10px",
        overflow="hidden",
        background="white",
    )