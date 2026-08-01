import reflex as rx
from ..resume_state import ResumeState
from ..components.template_previews import classic_preview


def template_card(
    title: str,
    description: str,
    template_name: str,
) -> rx.Component:
    return rx.card(
        rx.vstack(
            classic_preview(),

            rx.heading(title, size="5"),

            rx.text(
                description,
                color_scheme="gray",
            ),

            rx.button(
                "Use Template",
                color_scheme="purple",
                on_click=[
                    ResumeState.choose_template(template_name),
                    rx.redirect("/resume"),
                ],
            ),

            spacing="4",
            align="center",
        ),
        width="340px",
        padding="1.5em",
    )


def templates() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.heading(
                "Resume Templates",
                size="8",
            ),

            rx.text(
                "Choose a template before creating your resume.",
                color_scheme="gray",
            ),

            rx.hstack(

                template_card(
                    "Classic",
                    "Traditional ATS-friendly template.",
                    "classic",
                ),

                template_card(
                    "Modern",
                    "Professional modern design.",
                    "modern",
                ),

                template_card(
                    "Minimal",
                    "Clean and elegant layout.",
                    "minimal",
                ),

                spacing="6",
                wrap="wrap",
                justify="center",
            ),

            spacing="8",
            padding_y="2em",
        ),
        min_height="100vh",
    )