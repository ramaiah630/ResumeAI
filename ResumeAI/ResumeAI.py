import reflex as rx

from .components.navbar import navbar
from .components.hero import hero
from .components.feature_cards import feature_cards
from .pages.resume_form import resume_form

class State(rx.State):
    """Application state."""
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        feature_cards(),
        background="""
        linear-gradient(
            180deg,
            #0f172a 0%,
            #111827 40%,
            #1e1b4b 100%
        )
        """,
        min_height="100vh",
    )

app = rx.App()

app.add_page(index)
app.add_page(
    resume_form,
    route="/resume",
)