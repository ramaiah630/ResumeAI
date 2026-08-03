import reflex as rx


def copy_button(text_to_copy):
    return rx.button(
        "📋 Copy",
        on_click=rx.set_clipboard(text_to_copy),
        size="2",
        color_scheme="blue",
        variant="soft",
    )