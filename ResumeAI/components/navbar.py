import reflex as rx


def nav_button(text: str, route: str) -> rx.Component:
    return rx.button(
        text,
        on_click=rx.redirect(route),
        variant="ghost",
        size="3",
    )


def navbar() -> rx.Component:
    return rx.box(

        rx.hstack(

            rx.heading(
                "ResumeAI",
                size="7",
            ),

            rx.spacer(),

            nav_button(
                "🏠 Home",
                "/",
            ),

            nav_button(
                "📝 Resume",
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

            spacing="4",
            align="center",
            width="100%",
        ),

        padding="1em 2em",
        border_bottom="1px solid #2d3748",
        position="sticky",
        top="0",
        background="#0f172a",
        z_index="100",
    )