import reflex as rx


def classic_preview() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                bg="gray.800",
                height="18px",
                width="100%",
            ),

            rx.box(
                bg="gray.300",
                height="8px",
                width="70%",
            ),

            rx.box(
                bg="gray.200",
                height="5px",
                width="90%",
            ),

            rx.box(
                bg="gray.200",
                height="5px",
                width="85%",
            ),

            rx.divider(),

            rx.box(
                bg="gray.300",
                height="8px",
                width="45%",
            ),

            rx.box(
                bg="gray.200",
                height="5px",
                width="95%",
            ),

            rx.box(
                bg="gray.200",
                height="5px",
                width="90%",
            ),

            rx.divider(),

            rx.box(
                bg="gray.300",
                height="8px",
                width="40%",
            ),

            rx.box(
                bg="gray.200",
                height="5px",
                width="92%",
            ),

            spacing="2",
            align="start",
            width="100%",
        ),
        width="180px",
        height="240px",
        padding="12px",
        border="1px solid",
        border_color="gray.300",
        border_radius="10px",
        background="white",
    )