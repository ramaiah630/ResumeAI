import reflex as rx


def hero() -> rx.Component:
    return rx.center(
        rx.vstack(

            rx.badge(
                "🚀 Powered by Gemini AI",
                color_scheme="purple",
                variant="soft",
                size="3",
            ),

            rx.heading(
                "Create ATS-Friendly Resumes with AI",
                size="9",
                text_align="center",
            ),

            rx.text(
                "Build professional resumes in minutes using AI. "
                "Generate cover letters, analyze ATS score, match job descriptions, "
                "review your resume and export to PDF or DOCX.",
                text_align="center",
                max_width="800px",
                color="gray",
                size="4",
            ),

            rx.hstack(

                rx.button(
                    "🚀 Build Resume",
                    on_click=rx.redirect("/resume"),
                    color_scheme="purple",
                    size="4",
                ),

                rx.button(
                    "🤖 AI Tools",
                    on_click=rx.redirect("/ai-tools"),
                    variant="outline",
                    size="4",
                ),

                rx.button(
                    "🎨 Templates",
                    on_click=rx.redirect("/templates"),
                    variant="outline",
                    size="4",
                ),

                spacing="4",
                justify="center",
            ),

            rx.flex(

                rx.badge(
                    "✨ Gemini AI",
                    color_scheme="purple",
                    variant="soft",
                ),

                rx.badge(
                    "🎯 ATS Score",
                    color_scheme="green",
                    variant="soft",
                ),

                rx.badge(
                    "📄 PDF Export",
                    color_scheme="blue",
                    variant="soft",
                ),

                rx.badge(
                    "📘 DOCX Export",
                    color_scheme="orange",
                    variant="soft",
                ),

                rx.badge(
                    "⚡ Live Preview",
                    color_scheme="cyan",
                    variant="soft",
                ),

                rx.badge(
                    "💼 Job Matcher",
                    color_scheme="red",
                    variant="soft",
                ),

                rx.badge(
                    "✉️ Cover Letter",
                    color_scheme="yellow",
                    variant="soft",
                ),

                spacing="3",
                justify="center",
            ),

            spacing="7",
            align="center",
            max_width="1000px",
            width="100%",
        ),

        min_height="75vh",
        padding="4em",
        width="100%",
    )