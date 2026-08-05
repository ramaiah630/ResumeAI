import reflex as rx


def navigation_card(
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
            ),

            rx.text(
                description,
                text_align="center",
                color="gray",
            ),

            rx.button(
                "Open",
                on_click=rx.redirect(route),
                color_scheme="purple",
                width="100%",
            ),

            spacing="4",
            align="center",
        ),

        width="320px",
        padding="2em",
    )


def feature_cards() -> rx.Component:

    return rx.center(

        rx.vstack(

            rx.heading(
                "Choose What You Want To Do",
                size="8",
            ),

            rx.text(
                "Everything you need to build professional resumes with AI.",
                color="gray",
            ),

            rx.hstack(

                navigation_card(
                    "📝",
                    "Resume Builder",
                    "Create, edit and export your professional resume.",
                    "/resume",
                ),

                navigation_card(
                    "🤖",
                    "AI Tools",
                    "Job Matcher, Cover Letter and Resume Review.",
                    "/ai-tools",
                ),

                navigation_card(
                    "🎨",
                    "Templates",
                    "Choose from Classic, Modern and Minimal templates.",
                    "/templates",
                ),

                spacing="6",
                wrap="wrap",
                justify="center",
                width="100%",
            ),

            spacing="6",
            width="100%",
        ),

        padding_bottom="5em",
        width="100%",
    )