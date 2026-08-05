import reflex as rx
from ...resume_state import ResumeState

FORM_WIDTH = "400px"


def personal_section() -> rx.Component:
    return rx.vstack(

        rx.heading(
            "Personal Information",
            size="4",
            width=FORM_WIDTH,
            align="left",
        ),

        rx.input(
            placeholder="Full Name",
            value=ResumeState.full_name,
            on_change=ResumeState.set_full_name,
            width=FORM_WIDTH,
        ),

        rx.input(
            placeholder="Email Address",
            value=ResumeState.email,
            on_change=ResumeState.set_email,
            width=FORM_WIDTH,
        ),

        rx.input(
            placeholder="Phone Number",
            value=ResumeState.phone,
            on_change=ResumeState.set_phone,
            width=FORM_WIDTH,
        ),

        rx.input(
            placeholder="Professional Title",
            value=ResumeState.professional_title,
            on_change=ResumeState.set_professional_title,
            width=FORM_WIDTH,
        ),

        spacing="3",
        align="start",
        width="100%",
    )