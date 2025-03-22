import reflex as rx


def feature_card(
    icon: str, title: str, description: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                icon,
                class_name="w-12 h-12 stroke-white mb-6",
            ),
            rx.el.h3(
                title,
                class_name="text-2xl font-black text-white mb-4 uppercase",
            ),
            rx.el.p(
                description,
                class_name="text-white font-mono",
            ),
            class_name="p-8 bg-black border-4 border-white",
        )
    )


def features() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "ADVANCED FEATURES FOR MODERN ",
                    rx.el.span(
                        "AI SOLUTIONS",
                        class_name="text-yellow-400",
                    ),
                    class_name="text-4xl font-black text-white mb-6 text-center uppercase",
                ),
                rx.el.p(
                    "EVERYTHING YOU NEED TO BUILD AND DEPLOY AI MODELS AT SCALE",
                    class_name="text-xl text-white mb-16 text-center font-mono",
                ),
                rx.el.div(
                    feature_card(
                        "brain",
                        "Neural Networks",
                        "Build and train custom neural networks with our intuitive interface",
                    ),
                    feature_card(
                        "cpu",
                        "GPU Acceleration",
                        "Leverage powerful GPU infrastructure for faster training and inference",
                    ),
                    feature_card(
                        "chart",
                        "Real-time Analytics",
                        "Monitor model performance and get insights with advanced analytics",
                    ),
                    feature_card(
                        "code",
                        "API Integration",
                        "Seamlessly integrate AI capabilities into your existing applications",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="py-20",
        ),
        class_name="bg-black border-b-4 border-white",
    )