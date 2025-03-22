import reflex as rx
from typing import TypedDict
import re


class TestimonialEntry(TypedDict):
    name: str
    title: str
    company: str
    quote: str
    avatar: str


class PricingTier(TypedDict):
    name: str
    price: str
    description: str
    features: list[str]
    highlight: bool
    cta_text: str


def validate_email(email: str) -> bool:
    pattern = (
        "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    )
    return bool(re.match(pattern, email))


class LandingState(rx.State):
    show_modal: bool = False
    show_toast: bool = False
    toast_message: str = ""
    selected_plan: str = ""
    email: str = ""
    testimonials: list[TestimonialEntry] = [
        {
            "name": "Alex Thompson",
            "title": "Head of AI",
            "company": "TechVision",
            "quote": "This AI platform has revolutionized our development workflow. The results are simply outstanding.",
            "avatar": "/professional_headshot_alex.webp",
        },
        {
            "name": "Sarah Chen",
            "title": "CTO",
            "company": "DataFlow",
            "quote": "The speed and accuracy of the AI models have given us a significant competitive advantage.",
            "avatar": "/professional_headshot_sarah.webp",
        },
        {
            "name": "Marcus Rodriguez",
            "title": "ML Engineer",
            "company": "AILabs",
            "quote": "Implementation was seamless. The support team is exceptional and always ready to help.",
            "avatar": "/professional_headshot_marcus.webp",
        },
    ]
    pricing_tiers: list[PricingTier] = [
        {
            "name": "Basic",
            "price": "$49",
            "description": "Perfect for individuals and small teams",
            "features": [
                "5 AI model deployments",
                "Basic API access",
                "Community support",
                "1M API calls/month",
            ],
            "highlight": False,
            "cta_text": "Start Free Trial",
        },
        {
            "name": "Pro",
            "price": "$149",
            "description": "Ideal for growing businesses",
            "features": [
                "Unlimited deployments",
                "Advanced API access",
                "Priority support",
                "5M API calls/month",
                "Custom model training",
            ],
            "highlight": True,
            "cta_text": "Go Pro",
        },
        {
            "name": "Enterprise",
            "price": "Custom",
            "description": "For large organizations",
            "features": [
                "Dedicated infrastructure",
                "Full API access",
                "24/7 support",
                "Unlimited API calls",
                "Custom solutions",
                "SLA guarantee",
            ],
            "highlight": False,
            "cta_text": "Contact Sales",
        },
    ]

    @rx.event
    def toggle_modal(self):
        self.show_modal = not self.show_modal

    @rx.event
    def select_plan(self, plan: str):
        self.selected_plan = plan
        self.show_modal = True

    @rx.event
    def handle_signup(self, form_data: dict):
        email = form_data.get("email", "")
        if not validate_email(email):
            self.toast_message = (
                "Please enter a valid email address"
            )
            self.show_toast = True
            return
        self.toast_message = (
            "Thanks for signing up! We'll be in touch soon."
        )
        self.show_toast = True
        self.show_modal = False
        self.email = ""

    @rx.event
    def hide_toast(self):
        self.show_toast = False