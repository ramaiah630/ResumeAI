import reflex as rx

from ...resume_state import ResumeState


def section_heading(title: str) -> rx.Component:
    return rx.heading(
        title,
        size="4",
        color=ResumeState.theme_color,
        margin_top="20px",
        margin_bottom="10px",
    )


def preview_text(
    value,
    placeholder: str,
) -> rx.Component:
    return rx.text(
        rx.cond(
            value != "",
            value,
            placeholder,
        ),
        white_space="pre-wrap",
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
                    color=ResumeState.theme_color,
                    text_align="center",
                    width="100%",
                ),

                rx.text(
                    rx.cond(
                        ResumeState.professional_title != "",
                        ResumeState.professional_title,
                        "Professional Title",
                    ),
                    font_size="1.2em",
                    color="black",
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

                rx.cond(
                    ResumeState.summary != "",
                    rx.vstack(
                        section_heading("Professional Summary"),
                        rx.text(
                            ResumeState.summary,
                            white_space="pre-wrap",
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

                        section_heading("Education"),

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

                                # Years + Qualification + Course + Grade
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

                        width="100%",
                        align="start",
                        spacing="3",
                    ),
                ),

                

                # ==========================
                # Skills
                # ==========================

                rx.cond(
                    ResumeState.skills_list.length() > 0,
                    rx.vstack(
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

                        width="100%",
                        align="start",
                    ),
                ),

                # ==========================
                # Experience
                # ==========================

                rx.cond(
                    ResumeState.experiences.length() > 0,

                    rx.vstack(

                        section_heading("Experience"),

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
                                        #font_weight="bold",
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

                        align="start",
                        spacing="3",
                        width="100%",
                    ),
                ),

                
                # ==========================
                # Projects
                # ==========================

                rx.cond(
                    (ResumeState.project_title != "")
                    | (ResumeState.project_description != ""),

                    rx.vstack(

                        section_heading("Projects"),

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
                            ),
                        ),

                        rx.cond(
                            ResumeState.project_github != "",
                            rx.text(
                                ResumeState.project_github,
                                color="gray",
                            ),
                        ),

                        rx.cond(
                            ResumeState.project_description != "",
                            rx.text(
                                ResumeState.project_description,
                                white_space="pre-wrap",
                            ),
                        ),

                        align="start",
                        spacing="2",
                        width="100%",
                    ),
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
                            ),
                        ),

                        rx.cond(
                            ResumeState.certification_credential_id != "",
                            rx.text(
                                "Credential ID: "
                                + ResumeState.certification_credential_id,
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

                spacing="5",
                width="100%",
            ),

            width="210mm",
            min_height="297mm",
            background="white",
            color="black",
            padding="40px",
            border_radius="8px",
            box_shadow="lg",
            overflow="hidden",
        ),

        width="100%",
        max_width="900px",
    )