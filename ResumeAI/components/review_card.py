import reflex as rx


def review_card(
    title: str,
    body: rx.Component,
) -> rx.Component:

    return rx.card(

        rx.vstack(

            rx.heading(
                title,
                size="5",
            ),

            rx.divider(),

            body,

            spacing="4",
            align="start",
            width="100%",
        ),

        flex="1",
        min_width="340px",

        padding="1.8em",

        border_radius="18px",

        box_shadow="0 8px 25px rgba(0,0,0,0.08)",

        border="1px solid",

        border_color=rx.color("gray", 4),

        background=rx.color("gray", 1),

        transition="all 0.25s ease",
    )