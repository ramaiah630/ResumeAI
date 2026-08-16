import reflex as rx


def navigation_card(
    title: str,
    description: str,
    emoji: str,
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
                text_align="center",
                color="gray",
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
        min_height="340px",
        padding="2em",
        border_radius="18px",
        border="1px solid",
        border_color=rx.color("gray", 4),
        background=rx.color("gray", 1),
        box_shadow="0 8px 25px rgba(0,0,0,0.08)",
        transition="all .25s ease",
    )


def feature_cards() -> rx.Component:

    return rx.vstack(

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
                "Resume Builder",
                "Create, edit and export your professional resume.",
                "📄",
                "/resume",
            ),

            navigation_card(
                "AI Tools",
                "Job Matcher, Cover Letter and Resume Review.",
                "🤖",
                "/ai-tools",
            ),

            navigation_card(
                "Templates",
                "Choose from Classic, Modern and Minimal templates.",
                "🎨",
                "/templates",
            ),

            spacing="6",
            wrap="wrap",
            justify="center",
            width="100%",
        ),

        spacing="6",
        width="100%",
        align="center",
        padding_bottom="5em",
    )