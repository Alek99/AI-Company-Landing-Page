import reflex as rx
from app.states.landing_state import LandingState


def pricing_card(tier: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                tier["highlight"],
                rx.el.div(
                    "MOST POPULAR",
                    class_name="absolute -top-5 left-1/2 transform -translate-x-1/2 bg-yellow-400 text-black px-6 py-1 font-black border-2 border-black",
                ),
            ),
            rx.el.div(
                rx.el.h3(
                    tier["name"],
                    class_name="text-2xl font-black text-black mb-4 uppercase",
                ),
                rx.el.div(
                    rx.el.span(
                        tier["price"],
                        class_name="text-4xl font-black text-black",
                    ),
                    rx.el.span(
                        "/month",
                        class_name="text-black ml-2 font-mono",
                    ),
                    class_name="mb-6",
                ),
                rx.el.p(
                    tier["description"],
                    class_name="text-black mb-8 font-mono",
                ),
                rx.el.ul(
                    rx.foreach(
                        tier["features"],
                        lambda feature: rx.el.li(
                            rx.el.div(
                                rx.icon(
                                    "check",
                                    class_name="w-5 h-5 stroke-black mr-2",
                                ),
                                feature,
                                class_name="flex items-center text-black mb-4 font-mono",
                            )
                        ),
                    ),
                    class_name="mb-8",
                ),
                rx.el.button(
                    tier["cta_text"],
                    on_click=lambda: LandingState.select_plan(
                        tier["name"]
                    ),
                    class_name=rx.cond(
                        tier["highlight"],
                        "w-full px-6 py-4 bg-yellow-400 text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                        "w-full px-6 py-4 bg-white text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                    ),
                ),
                class_name="p-8 h-full flex flex-col justify-between",
            ),
            class_name=rx.cond(
                tier["highlight"],
                "relative bg-yellow-400 border-4 border-black h-full",
                "relative bg-white border-4 border-black h-full",
            ),
        )
    )


def pricing() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "SIMPLE, ",
                rx.el.span(
                    "TRANSPARENT",
                    class_name="text-yellow-400",
                ),
                " PRICING",
                class_name="text-4xl font-black text-white mb-6 text-center uppercase",
            ),
            rx.el.p(
                "CHOOSE THE PERFECT PLAN FOR YOUR NEEDS",
                class_name="text-xl text-white mb-16 text-center font-mono",
            ),
            rx.el.div(
                rx.foreach(
                    LandingState.pricing_tiers, pricing_card
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20",
        ),
        class_name="bg-black border-b-4 border-white",
    )