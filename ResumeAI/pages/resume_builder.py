import reflex as rx

from ..components.template_selector import template_selector
from ..components.resume_preview import resume_preview
from .resume_form import resume_form
from ..components.theme_selector import theme_selector


def resume_builder() -> rx.Component:
    return rx.box(

        rx.hstack(

            # ==========================
            # Left Side - Form
            # ==========================

            rx.box(
                resume_form(),
                width="40%",
            ),

            # ==========================
            # Right Side - Preview
            # ==========================

            rx.box(

                rx.vstack(

                    # Template & Theme Controls
                    rx.hstack(

                        template_selector(),
                        theme_selector(),

                        spacing="4",
                        align="center",
                        width="100%",
                    ),

                    # Resume Preview
                    resume_preview(),

                    spacing="4",
                    width="100%",
                ),

                rx.hstack(

                    rx.button(
                        "📊 Analyze Resume",
                        on_click=rx.redirect("/resume-review"),
                        
                    ),

                    rx.button(
                        "💼 Job Matcher",
                        on_click=rx.redirect("/job-match"),
                    ),

                    rx.button(
                        "✉️ Cover Letter",
                        on_click=rx.redirect("/cover-letter"),
                    ),

                    spacing="4",
                ),

                width="60%",

                position="sticky",
                top="80px",

                align_self="flex-start",

                max_height="calc(100vh - 100px)",
                overflow_y="auto",
            ),

            spacing="6",
            align="start",
            width="100%",
        ),

        padding="2em",
        width="100%",
    )