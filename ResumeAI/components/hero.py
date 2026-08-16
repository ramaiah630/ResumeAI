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
                "Build Smarter Resumes with AI",
                size="9",
                text_align="center",
            ),

            rx.text(
                "Create ATS-friendly resumes, generate professional cover letters, "
                "analyze resume quality, match jobs, and export to PDF or DOCX — all powered by Gemini AI.",
                text_align="center",
                color="gray",
                max_width="850px",
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

            rx.hstack(

                rx.badge(
                    "⚡ 10+ AI Features",
                    color_scheme="purple",
                    variant="soft",
                ),

                rx.badge(
                    "📄 ATS Optimized",
                    color_scheme="green",
                    variant="soft",
                ),

                rx.badge(
                    "🤖 Gemini AI",
                    color_scheme="blue",
                    variant="soft",
                ),

                rx.badge(
                    "📥 PDF & DOCX",
                    color_scheme="orange",
                    variant="soft",
                ),

                spacing="3",
                justify="center",
                wrap="wrap",
            ),

            spacing="7",
            align="center",
            max_width="1000px",
            width="100%",
        ),

        min_height="80vh",
        width="100%",
        padding="4em",
    )