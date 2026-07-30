import reflex as rx


def hero() -> rx.Component:
    return rx.center(
        rx.hstack(

            rx.vstack(
                rx.badge(
                    "🚀 AI Powered",
                    color_scheme="purple",
                    variant="soft",
                ),

                rx.heading(
                    "Build AI-Powered Professional Resumes",
                    size="9",
                ),

                rx.text(
                    "Create ATS-friendly resumes in minutes with the help of AI.",
                    size="5",
                    color_scheme="gray",
                ),

                rx.hstack(
                    rx.button(
                        "Create Resume",
                        color_scheme="purple",
                        on_click=rx.redirect("/resume"),
                    ),
                    rx.button(
                        "View Templates",
                        variant="outline",
                    ),
                    spacing="4",
                ),

                spacing="6",
                align="start",
                width="50%",
            ),


            spacing="9",
            align="center",
            width="100%",
        ),
        min_height="80vh",
        padding="3em",
    )