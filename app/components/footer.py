import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "AI PLATFORM",
                        class_name="text-xl font-black text-white mb-4 uppercase",
                    ),
                    rx.el.p(
                        "Building the future of AI, one model at a time.",
                        class_name="text-white font-mono",
                    ),
                ),
                rx.el.div(
                    rx.el.h4(
                        "LINKS",
                        class_name="text-lg font-black text-white mb-4 uppercase",
                    ),
                    rx.el.a(
                        "About",
                        href="#",
                        class_name="text-white hover:text-yellow-400 block mb-2 font-mono",
                    ),
                    rx.el.a(
                        "Features",
                        href="#",
                        class_name="text-white hover:text-yellow-400 block mb-2 font-mono",
                    ),
                    rx.el.a(
                        "Pricing",
                        href="#",
                        class_name="text-white hover:text-yellow-400 block mb-2 font-mono",
                    ),
                ),
                rx.el.div(
                    rx.el.h4(
                        "LEGAL",
                        class_name="text-lg font-black text-white mb-4 uppercase",
                    ),
                    rx.el.a(
                        "Privacy",
                        href="#",
                        class_name="text-white hover:text-yellow-400 block mb-2 font-mono",
                    ),
                    rx.el.a(
                        "Terms",
                        href="#",
                        class_name="text-white hover:text-yellow-400 block mb-2 font-mono",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 AI Platform. All rights reserved.",
                    class_name="text-white text-center font-mono",
                ),
                class_name="border-t border-white pt-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-black border-t-4 border-white",
    )