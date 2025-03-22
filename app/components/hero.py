import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "AI-POWERED SOLUTIONS",
                    class_name="text-sm font-black tracking-widest text-yellow-400 mb-6 block border-2 border-yellow-400 p-2 inline-block",
                ),
                rx.el.h1(
                    "HARNESS THE POWER OF ",
                    rx.el.span(
                        "ARTIFICIAL INTELLIGENCE",
                        class_name="text-yellow-400",
                    ),
                    class_name="text-5xl md:text-7xl font-black text-white tracking-tight mb-8 uppercase",
                ),
                rx.el.p(
                    "Transform your business with our state-of-the-art AI platform. Build, deploy, and scale AI solutions with unprecedented ease.",
                    class_name="text-xl text-white max-w-2xl mb-10 font-mono",
                ),
                rx.el.div(
                    rx.el.button(
                        "GET STARTED",
                        class_name="px-8 py-4 bg-yellow-400 text-black font-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] border-2 border-black hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                    ),
                    rx.el.button(
                        "SCHEDULE DEMO",
                        class_name="ml-4 px-8 py-4 bg-white text-black font-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] border-2 border-black hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                    ),
                    class_name="flex flex-wrap gap-4 justify-center",
                ),
                class_name="max-w-4xl mx-auto text-center flex flex-col items-center",
            ),
            class_name="px-4 sm:px-6 lg:px-8 py-20 md:py-28 min-h-[80vh] flex items-center justify-center",
        ),
        class_name="bg-black border-b-4 border-white",
    )