import reflex as rx

from .components.navbar import navbar
from .components.hero import hero
from .components.feature_cards import feature_cards
from .pages.resume_builder import resume_builder
from .pages.templates import templates
from .pages.job_match import job_match
#from .pages.cover_letter import cover_letter

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
    resume_builder,
    route="/resume",
)
app.add_page(
    templates,
    route="/templates",
)
#app.add_page(
    #cover_letter,
    #route="/cover-letter",
#)
app.add_page(
    job_match,
    route="/job-match",
)