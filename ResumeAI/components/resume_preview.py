import reflex as rx

from .templates.classic_template import classic_template
from .templates.modern_template import modern_template
from .templates.minimal_template import minimal_template
from ..resume_state import ResumeState


def resume_preview() -> rx.Component:
    return rx.match(
        ResumeState.selected_template,
        ("classic", classic_template()),
        ("modern", modern_template()),
        ("minimal", minimal_template()),
        classic_template(),  # Default
    )