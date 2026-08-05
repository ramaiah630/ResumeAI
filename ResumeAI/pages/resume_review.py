import reflex as rx
from ..resume_state import ResumeState
from ..components.ai_loading_card import ai_loading_card


def resume_review() -> rx.Component:
    return rx.center(

        rx.vstack(

            rx.heading(
                "📊 AI Resume Review",
                size="8",
            ),

            rx.text(
                "Analyze your resume with Gemini AI.",
                color="gray",
            ),

            rx.button(
                rx.cond(
                    ResumeState.is_generating_review,
                    "⏳ Analyzing...",
                    "🤖 Analyze Resume",
                ),
                on_click=ResumeState.analyze_resume,
                color_scheme="green",
                width="250px",
                disabled=ResumeState.is_generating_review,
            ),
            rx.cond(
                ResumeState.is_generating_review,
                ai_loading_card(
                    ResumeState.review_status,
                ),
            ),

            rx.cond(

                ResumeState.resume_review != "",

                rx.vstack(

                    # Resume Score Card
                    rx.card(

                        rx.vstack(

                            rx.heading(
                                "Resume Score",
                                size="6",
                            ),

                            rx.heading(
                                ResumeState.resume_score,
                                size="9",
                                color=ResumeState.resume_score_color,
                            ),

                             rx.progress(
                                value=ResumeState.resume_score_value,
                                max=100,
                                width="100%",
                                color_scheme=ResumeState.resume_score_color,
                            ),

                            rx.text(
                                "AI-powered ATS analysis",
                                color="gray",
                            ),

                            spacing="4",
                            align="center",
                            width="100%",
                        ),

                        width="400px",
                        padding="2em",
                    ),


                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "📝 Overall Summary",
                                size="5",
                            ),

                            rx.divider(),

                            rx.text(
                                ResumeState.overall_summary,
                                white_space="pre-wrap",
                            ),

                            spacing="3",
                            align="start",
                            width="100%",
                        ),

                        width="900px",
                        padding="2em",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "✅ Strengths",
                                size="5",
                            ),

                            rx.divider(),

                            rx.foreach(

                                ResumeState.strengths,
                                lambda item: rx.text(
                                "• " + item,
                                ),
                            ),

                            spacing="3",
                            align="start",
                            width="100%",
                        ),

                        width="900px",
                        padding="2em",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "⚠️ Improvements",
                                size="5",
                            ),

                            rx.divider(),

                            rx.foreach(

                                ResumeState.improvements,
                                lambda item: rx.text(
                                "• " + item,
                                ),
                            ),

                            spacing="3",
                            align="start",
                            width="100%",
                        ),

                        width="900px",
                        padding="2em",
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading(
                                "🎯 Missing Keywords",
                                size="5",
                            ),

                            rx.divider(),

                            rx.flex(

                                rx.foreach(

                                    ResumeState.missing_keywords,

                                    lambda keyword: rx.badge(
                                        keyword,
                                        color_scheme="purple",
                                        variant="soft",
                                        size="2",
                                    ),
                                ),

                                wrap="wrap",
                                spacing="2",
                            ),

                            spacing="3",
                            align="start",
                            width="100%",
                        ),

                        width="900px",
                        padding="2em",
                    ),

                    # Analysis

                    spacing="6",
                    align="center",
                ),
            ),

            spacing="6",
            padding="3em",
        ),

        width="100%", 
    )