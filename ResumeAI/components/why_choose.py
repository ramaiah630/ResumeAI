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
                font_size="3em",
            ),

            rx.heading(
                title,
                size="5",
                text_align="center",
            ),

            rx.text(
                description,
                text_align="center",
                color="gray",
            ),

            spacing="4",
            align="center",
            width="100%",
        ),

        width="300px",
        min_height="260px",

        padding="2em",

        border_radius="18px",

        border="1px solid",
        border_color=rx.color("gray", 4),

        background=rx.color("gray", 1),

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        transition="all 0.25s ease",
    )


def why_choose() -> rx.Component:

    return rx.center(

        rx.vstack(

            rx.heading(
                "Why Choose ResumeAI?",
                size="8",
            ),

            rx.text(
                "Everything you need to create professional, ATS-friendly resumes powered by Gemini AI.",
                color="gray",
                text_align="center",
                max_width="700px",
            ),

            rx.hstack(

                feature(
                    "🤖",
                    "AI Powered",
                    "Generate summaries, improve experience and create cover letters using Gemini AI.",
                ),

                feature(
                    "🎯",
                    "ATS Optimized",
                    "Receive AI-powered resume analysis and improve your ATS score.",
                ),

                feature(
                    "📄",
                    "Export",
                    "Download professional resumes in PDF and DOCX formats.",
                ),

                spacing="6",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            rx.hstack(

                feature(
                    "⚡",
                    "Live Preview",
                    "Instantly preview every change while building your resume.",
                ),

                feature(
                    "💼",
                    "Job Matcher",
                    "Compare your resume with job descriptions and identify missing skills.",
                ),

                feature(
                    "📊",
                    "Resume Review",
                    "Get recruiter-style feedback and actionable AI suggestions.",
                ),

                spacing="6",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            spacing="7",
            align="center",
            width="100%",
        ),

        width="100%",
        padding_y="5em",
    )