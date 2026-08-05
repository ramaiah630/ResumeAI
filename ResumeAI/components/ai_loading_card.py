import reflex as rx


def ai_loading_card(message: str) -> rx.Component:
    return rx.card(

        rx.hstack(

            rx.spinner(
                size="3",
            ),

            rx.vstack(

                rx.heading(
                    "🤖 Gemini AI",
                    size="4",
                ),

                rx.text(
                    message,
                    color="gray",
                ),

                rx.text(
                    "This usually takes 5–15 seconds.",
                    color="gray",
                    font_size="0.85em",
                ),

                spacing="1",
                align="start",
            ),

            spacing="4",
            align="center",
        ),

        width="400px",
        padding="1.2em",
        border_radius="12px",
    )