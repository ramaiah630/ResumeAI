import reflex as rx


def tool_card(title: str, description: str, route: str) -> rx.Component:
    return rx.card(
        rx.vstack(

            rx.heading(
                title,
                size="5",
            ),

            rx.text(
                description,
                color="gray",
            ),

            rx.button(
                "Open",
                on_click=rx.redirect(route),
                width="100%",
            ),

            spacing="3",
            align="start",
        ),

        width="320px",
        padding="1.5em",
    )


def ai_tools() -> rx.Component:
    return rx.center(

        rx.vstack(

            rx.heading(
                "🤖 AI Tools",
                size="8",
            ),

            rx.text(
                "AI-powered tools to improve your resume and job applications.",
                color="gray",
            ),

            rx.grid(

                tool_card(
                    "🎯 Job Matcher",
                    "Compare your resume with a job description.",
                    "/job-match",
                ),

                tool_card(
                    "✉️ Cover Letter",
                    "Generate personalized cover letters with Gemini AI.",
                    "/cover-letter",
                ),

                tool_card(
                    "📊 Resume Review",
                    "Get AI feedback on your complete resume.",
                    "/resume-review",
                ),

                columns="3",
                spacing="6",
                width="100%",
            ),

            spacing="6",
            width="100%",
            max_width="1100px",
            padding="2em",
        ),

        width="100%",
    )