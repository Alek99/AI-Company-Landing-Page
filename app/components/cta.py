import reflex as rx
from app.states.landing_state import LandingState


def signup_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    f"GET STARTED WITH {LandingState.selected_plan}",
                    class_name="text-2xl font-black text-black mb-4 uppercase",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "EMAIL",
                            class_name="block text-sm font-black text-black mb-2 uppercase",
                        ),
                        rx.el.input(
                            type="email",
                            name="email",
                            placeholder="you@example.com",
                            required=True,
                            class_name="w-full px-4 py-3 border-2 border-black font-mono",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "GET STARTED",
                            type="submit",
                            class_name="w-full px-6 py-3 bg-yellow-400 text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                        ),
                        rx.el.button(
                            "CANCEL",
                            type="button",
                            on_click=LandingState.toggle_modal,
                            class_name="w-full mt-3 px-6 py-3 bg-white text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none",
                        ),
                        class_name="space-y-3",
                    ),
                    on_submit=LandingState.handle_signup,
                ),
                class_name="bg-white p-8 border-4 border-black max-w-md w-full",
            ),
            class_name="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50",
        ),
        open=LandingState.show_modal,
    )


def toast() -> rx.Component:
    return rx.cond(
        LandingState.show_toast,
        rx.el.div(
            rx.el.div(
                LandingState.toast_message,
                rx.el.button(
                    "✕",
                    on_click=LandingState.hide_toast,
                    class_name="ml-4",
                ),
                class_name="bg-yellow-400 px-6 py-3 border-2 border-black font-mono flex items-center justify-between",
            ),
            class_name="fixed top-4 right-4 z-50",
        ),
    )


def cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "READY TO ",
                    rx.el.span(
                        "TRANSFORM",
                        class_name="text-yellow-400",
                    ),
                    " YOUR BUSINESS?",
                    class_name="text-4xl font-black text-white mb-6 text-center uppercase",
                ),
                rx.el.p(
                    "JOIN THOUSANDS OF COMPANIES ALREADY USING OUR AI PLATFORM",
                    class_name="text-xl text-white mb-10 text-center font-mono",
                ),
                rx.el.button(
                    "GET STARTED NOW",
                    on_click=lambda: LandingState.select_plan(
                        "Basic"
                    ),
                    class_name="px-8 py-4 bg-yellow-400 text-black font-black border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[3px] hover:translate-y-[3px] hover:shadow-none mx-auto block",
                ),
                signup_modal(),
                toast(),
                class_name="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20",
        ),
        class_name="bg-black border-b-4 border-white",
    )