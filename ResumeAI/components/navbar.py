import reflex as rx


def nav_button(
    text: str,
    route: str,
) -> rx.Component:

    return rx.button(
        text,
        on_click=rx.redirect(route),
        variant="ghost",
        size="3",
        color="white",
        border_radius="10px",
    )


def navbar() -> rx.Component:

    return rx.box(

        rx.hstack(

            rx.hstack(

                rx.text(
                    "🚀",
                    font_size="1.8em",
                ),

                rx.heading(
                    "ResumeAI",
                    size="7",
                ),

                spacing="2",
                align="center",
            ),

            rx.spacer(),

            rx.hstack(

                nav_button(
                    "🏠 Home",
                    "/",
                ),

                nav_button(
                    "📝 Resume Builder",
                    "/resume",
                ),

                nav_button(
                    "🎨 Templates",
                    "/templates",
                ),

                nav_button(
                    "🤖 AI Tools",
                    "/ai-tools",
                ),

                spacing="3",
            ),

            align="center",
            width="100%",
        ),

        position="sticky",
        top="0",
        z_index="1000",

        width="100%",

        padding="1em 2em",

        background="rgba(15,23,42,0.95)",

        backdrop_filter="blur(12px)",

        border_bottom="1px solid",

        border_color=rx.color("gray", 7),

        box_shadow="0 4px 15px rgba(0,0,0,0.15)",
    )