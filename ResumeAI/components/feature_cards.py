import reflex as rx


def feature_card(title: str, description: str, emoji: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(emoji, font_size="2em"),
            rx.heading(title, size="5"),
            rx.text(
                description,
                color_scheme="gray",
                text_align="center",
            ),
            spacing="3",
            align="center",
        ),
        padding="1.5em",
        width="260px",
    )


def feature_cards() -> rx.Component:
    return rx.center(
        rx.hstack(
            feature_card(
                "AI Resume Writing",
                "Generate professional resume content with AI.",
                "🤖",
            ),
            feature_card(
                "PDF Export",
                "Download beautiful ATS-friendly PDF resumes.",
                "📄",
            ),
            feature_card(
                "Modern Templates",
                "Choose from elegant professional designs.",
                "🎨",
            ),
            feature_card(
                "Cloud Sync",
                "Access your resumes from anywhere.",
                "☁️",
            ),
            spacing="5",
            wrap="wrap",
            justify="center",
        ),
        padding_bottom="4em",
    )