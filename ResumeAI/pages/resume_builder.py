import reflex as rx

from ..components.template_selector import template_selector
from ..components.resume_preview import resume_preview
from .resume_form import resume_form


def resume_builder() -> rx.Component:
    return rx.box(
        rx.hstack(
            # Left Side - Form
            rx.box(
                resume_form(),
                width="40%",
            ),

            # Right Side - Preview
            rx.box(
                rx.vstack(
                    template_selector(),
                    resume_preview(),
                    spacing="4",
                    width="100%",
                ),
                rx.button(
                    "Cover Letter",
                    on_click=rx.redirect("/cover-letter"),
                ),
                
                width="60%",
            ),

            spacing="6",
            align="start",
            width="100%",
        ),
        padding="2em",
        width="100%",
    )