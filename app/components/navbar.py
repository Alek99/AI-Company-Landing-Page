import reflex as rx
from app.states.landing_state import LandingState


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "AI PLATFORM",
                    href="#",
                    class_name="text-2xl font-black text-white hover:text-yellow-400",
                ),
                rx.el.div(
                    rx.el.a(
                        "Features",
                        href="#features",
                        class_name="text-white hover:text-yellow-400 font-mono",
                    ),
                    rx.el.a(
                        "Pricing",
                        href="#pricing",
                        class_name="text-white hover:text-yellow-400 font-mono ml-8",
                    ),
                    rx.el.a(
                        "Testimonials",
                        href="#testimonials",
                        class_name="text-white hover:text-yellow-400 font-mono ml-8",
                    ),
                    rx.el.button(
                        "GET STARTED",
                        on_click=lambda: LandingState.select_plan(
                            "Basic"
                        ),
                        class_name="ml-8 px-6 py-2 bg-yellow-400 text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex justify-between items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4",
        ),
        class_name="bg-black border-b-4 border-white sticky top-0 z-40",
    )