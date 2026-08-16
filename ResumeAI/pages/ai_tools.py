import reflex as rx


def tool_card(
    emoji: str,
    title: str,
    description: str,
    route: str,
) -> rx.Component:

    return rx.card(

        rx.vstack(

            rx.text(
                emoji,
                font_size="3em",
            ),

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
                "Open",
                on_click=rx.redirect(route),
                color_scheme="purple",
                width="100%",
            ),

            spacing="4",
            align="center",
            width="100%",
            height="100%",
        ),

        width="320px",
        min_height="320px",

        padding="2em",

        border_radius="18px",

        border="1px solid",
        border_color=rx.color("gray", 4),

        background=rx.color("gray", 1),

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        transition="all 0.25s ease",
    )


def ai_tools() -> rx.Component:

    return rx.center(

        rx.vstack(

            rx.heading(
                "🤖 AI Tools",
                size="8",
            ),

            rx.text(
                "Choose an AI-powered tool to improve your resume and job applications.",
                color="gray",
                text_align="center",
                max_width="700px",
            ),

            rx.hstack(

                tool_card(
                    "📊",
                    "Resume Review",
                    "Receive ATS analysis, recruiter feedback, strengths, improvements and missing keywords.",
                    "/resume-review",
                ),

                tool_card(
                    "✉️",
                    "Cover Letter",
                    "Generate professional, personalized cover letters using Gemini AI.",
                    "/cover-letter",
                ),

                tool_card(
                    "🎯",
                    "Job Matcher",
                    "Compare your resume with a job description and discover missing skills.",
                    "/job-match",
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
    )