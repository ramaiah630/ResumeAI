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

            rx.heading(
                title,
                size="6",
                text_align="center",
            ),

            rx.text(
                description,
                color="gray",
                text_align="center",
            ),

            rx.spacer(),

            rx.button(
                "Use Template",
                color_scheme="purple",
                width="100%",
                on_click=[
                    ResumeState.choose_template(template_name),
                    rx.redirect("/resume"),
                ],
            ),

            spacing="4",
            align="center",
            width="100%",
            height="100%",
        ),

        width="340px",
        min_height="500px",

        padding="2em",

        border_radius="18px",

        border="1px solid",
        border_color=rx.color("gray", 4),

        background=rx.color("gray", 1),

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        transition="all 0.25s ease",
    )


def templates() -> rx.Component:

    return rx.center(

        rx.vstack(

            rx.heading(
                "🎨 Resume Templates",
                size="8",
            ),

            rx.text(
                "Choose a professional template before creating your resume.",
                color="gray",
                text_align="center",
                max_width="700px",
            ),

            rx.hstack(

                template_card(
                    "Classic",
                    "Traditional ATS-friendly resume suitable for most industries.",
                    "classic",
                ),

                template_card(
                    "Modern",
                    "A clean and professional design with a contemporary layout.",
                    "modern",
                ),

                template_card(
                    "Minimal",
                    "Simple, elegant and distraction-free for maximum readability.",
                    "minimal",
                ),

                spacing="6",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            spacing="7",
            align="center",
            width="100%",
            max_width="1200px",
            padding="3em",
        ),

        width="100%",
        min_height="100vh",
    )