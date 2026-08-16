import reflex as rx

from ..resume_state import ResumeState
from ..components.ai_loading_card import ai_loading_card
from ..components.review_card import review_card
from ..components.score_card import score_card


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

                    # ---------------- Row 1 ----------------

                    rx.hstack(

                        score_card(),

                        review_card(

                            "📝 Overall Summary",

                            rx.text(
                                ResumeState.overall_summary,
                                white_space="pre-wrap",
                            ),
                        ),

                        spacing="6",
                        width="100%",
                        align="stretch",
                    ),

                    # ---------------- Row 2 ----------------

                    rx.hstack(

                        review_card(

                            "✅ Strengths",

                            rx.vstack(

                                rx.foreach(
                                    ResumeState.strengths,
                                    lambda item: rx.text(
                                        "• " + item,
                                    ),
                                ),

                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                        ),

                        review_card(

                            "⚠️ Improvements",

                            rx.vstack(

                                rx.foreach(
                                    ResumeState.improvements,
                                    lambda item: rx.text(
                                        "• " + item,
                                    ),
                                ),

                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                        ),

                        spacing="6",
                        width="100%",
                        align="stretch",
                    ),

                    # ---------------- Row 3 ----------------

                    rx.hstack(

                        review_card(

                            "🎯 Missing Keywords",

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
                        ),

                        review_card(

                            "💡 ATS Suggestions",

                            rx.vstack(

                                rx.foreach(
                                    ResumeState.ai_ats_suggestions,
                                    lambda item: rx.text(
                                        "• " + item,
                                    ),
                                ),

                                spacing="2",
                                align="start",
                                width="100%",
                            ),
                        ),

                        spacing="6",
                        width="100%",
                        align="stretch",
                    ),

                    # ---------------- Row 4 ----------------

                    review_card(

                        "👨‍💼 Recruiter Advice",

                        rx.text(
                            ResumeState.recruiter_advice,
                            white_space="pre-wrap",
                        ),
                    ),

                    spacing="6",
                    width="100%",
                    align="stretch",
                ),
            ),

            spacing="6",
            padding="3em",
            width="100%",
            max_width="1400px",
        ),

        width="100%",
    )