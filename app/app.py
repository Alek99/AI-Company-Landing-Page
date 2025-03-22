import reflex as rx
from app.components.hero import hero
from app.components.features import features
from app.components.pricing import pricing
from app.components.testimonials import testimonials
from app.components.cta import cta
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.div(
        hero(),
        features(),
        pricing(),
        testimonials(),
        cta(),
        footer(),
        class_name="min-h-screen bg-black",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index)