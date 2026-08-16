import reflex as rx

from ...resume_state import ResumeState


def minimal_template() -> rx.Component:
    return rx.box(

        # ==========================
        # Header
        # ==========================

        rx.text(
            rx.cond(
                ResumeState.full_name != "",
                ResumeState.full_name,
                "Your Name",
            ),
            font_size="2.4em",
            font_weight="bold",
            color=ResumeState.theme_color,
        ),

        rx.text(
            rx.cond(
                ResumeState.professional_title != "",
                ResumeState.professional_title,
                "Professional Title",
            ),
            color="black",
            font_size="1.2em",
        ),

        rx.hstack(

            rx.cond(
                ResumeState.email != "",
                rx.text(ResumeState.email),
            ),

            rx.cond(
                (ResumeState.email != "")
                & (ResumeState.phone != ""),
                rx.text("|"),
            ),

            rx.cond(
                ResumeState.phone != "",
                rx.text(ResumeState.phone),
            ),

            spacing="3",
        ),

        rx.divider(
            margin_y="1.5em",
        ),

        # ==========================
        # Professional Summary
        # ==========================

        rx.cond(
            ResumeState.summary != "",

            rx.vstack(

                rx.heading(
                    "Professional Summary",
                    color=ResumeState.theme_color,
                    size="4",
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
                    color=ResumeState.theme_color,
                    size="4",
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
                    color=ResumeState.theme_color,
                    size="4",
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
                    color=ResumeState.theme_color,
                    size="4",
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
                        #color="gray",
                    ),
                ),

                rx.cond(
                    ResumeState.project_description != "",
                    rx.text(
                        ResumeState.project_description,
                        white_space="pre-wrap",
                    ),
                ),

                rx.divider(
                    margin_y="1.5em",
                ),

                width="100%",
                align="start",
                spacing="2",
            ),
        ),

        # ==========================
        # Skills
        # ==========================

        rx.cond(
            ResumeState.skills_list.length() > 0,

            rx.vstack(

                rx.heading(
                    "Skills",
                    color=ResumeState.theme_color,
                    size="4",
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
                    
                    rx.divider(
                        margin_y="1.5em",
                    ),

                    wrap="wrap",
                    spacing="2",
                ),

                width="100%",
                align="start",
                spacing="2",
            ),
        ),


        # ==========================
        # Certifications
        # ==========================

        rx.cond(
            ResumeState.certification_name != "",
            rx.vstack(

                rx.heading(
                    "Certifications",
                    color=ResumeState.theme_color,
                    size="4",
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
                        #color="gray",
                    ),
                ),

                rx.cond(
                    ResumeState.certification_credential_id != "",
                    rx.text(
                        "Credential ID: "
                        + ResumeState.certification_credential_id,
                        #color="gray",
                    ),
                ),

                rx.divider(
                    margin_y="1.5em",
                ),

                width="100%",
                align="start",
                spacing="2",
            ),
        ),

        # ==========================
        # Languages
        # ==========================

        rx.cond(
            ResumeState.languages != "",
            rx.vstack(

                rx.heading(
                    "Languages",
                    color=ResumeState.theme_color,
                    size="4",
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
                spacing="2",
            ),
        ),

        width="100%",
        max_width="850px",
        padding="3em",
        background="white",
        color="black",
        border="1px solid #e5e7eb",
        border_radius="8px",
    )