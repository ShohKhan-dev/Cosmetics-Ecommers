# Django
from django.urls import path

# Project
from .views.stripe import StripeWebhookAPIView, StripeCheckoutAPIView
from .views.paypal import PaypalCheckoutAPIView, PaypalReturnAPIView, PaypalCancelAPIView

urlpatterns = [
    path('stripe/webhook/', StripeWebhookAPIView.as_view()),
    path('stripe/checkout/', StripeCheckoutAPIView.as_view()),
    path('paypal/checkout/', PaypalCheckoutAPIView.as_view()),
    path('paypal/return/<int:pk>/', PaypalReturnAPIView.as_view()),
    path('paypal/cancel/<int:pk>/', PaypalCancelAPIView.as_view()),
]
