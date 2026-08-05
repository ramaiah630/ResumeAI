import reflex as rx


def feature(
    emoji: str,
    title: str,
    description: str,
) -> rx.Component:

    return rx.card(

        rx.vstack(

            rx.text(
                emoji,
                font_size="2.5em",
            ),

            rx.heading(
                title,
                size="5",
            ),

            rx.text(
                description,
                text_align="center",
                color="gray",
            ),

            spacing="3",
            align="center",
        ),

        width="280px",
        padding="1.5em",
    )


def why_choose() -> rx.Component:

    return rx.center(

        rx.vstack(

            rx.heading(
                "Why Choose ResumeAI?",
                size="8",
            ),

            rx.text(
                "Everything you need to create professional, ATS-friendly resumes.",
                color="gray",
                text_align="center",
            ),

            rx.hstack(

                feature(
                    "🤖",
                    "AI Powered",
                    "Generate summaries, improve experience and create cover letters with Gemini AI.",
                ),

                feature(
                    "🎯",
                    "ATS Optimized",
                    "Analyze your resume and improve your ATS score for better job applications.",
                ),

                feature(
                    "📄",
                    "Export",
                    "Download your resume in PDF and DOCX formats with one click.",
                ),

                spacing="5",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            rx.hstack(

                feature(
                    "⚡",
                    "Live Preview",
                    "See every change instantly while editing your resume.",
                ),

                feature(
                    "💼",
                    "Job Matcher",
                    "Compare your resume against job descriptions and identify missing skills.",
                ),

                feature(
                    "📊",
                    "Resume Review",
                    "Receive AI-powered recruiter feedback and actionable improvements.",
                ),

                spacing="5",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            spacing="6",
            width="100%",
        ),

        padding_y="5em",
    )