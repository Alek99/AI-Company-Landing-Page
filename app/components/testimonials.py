import reflex as rx
from app.states.landing_state import LandingState


def testimonial_card(testimonial: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=testimonial["avatar"],
                class_name="w-16 h-16 mb-6 border-4 border-black",
            ),
            rx.el.p(
                testimonial["quote"],
                class_name="text-black mb-6 font-mono",
            ),
            rx.el.div(
                rx.el.p(
                    testimonial["name"],
                    class_name="font-black text-black uppercase",
                ),
                rx.el.p(
                    f"{testimonial['title']} at {testimonial['company']}",
                    class_name="text-black font-mono",
                ),
                class_name="text-center",
            ),
            class_name="p-8 bg-yellow-400 border-4 border-black",
        )
    )


def testimonials() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "TRUSTED BY ",
                rx.el.span(
                    "INDUSTRY LEADERS",
                    class_name="text-yellow-400",
                ),
                class_name="text-4xl font-black text-white mb-6 text-center uppercase",
            ),
            rx.el.p(
                "SEE WHAT OUR CUSTOMERS HAVE TO SAY ABOUT US",
                class_name="text-xl text-white mb-16 text-center font-mono",
            ),
            rx.el.div(
                rx.foreach(
                    LandingState.testimonials,
                    testimonial_card,
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20",
        ),
        class_name="bg-black border-b-4 border-white",
    )