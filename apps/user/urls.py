# Django
from django.urls import path, include

# Views
from rest_framework.routers import DefaultRouter

from .views.address import AddressViewSet
from .views.forgot_password import SendForgotPasswordAPIView, CheckForgotPasswordCodeView, ForgotPasswordView
from .views.login import LoginAPIView
from .views.me import UserMeAPIVIew
from .views.signup import SignupView, CheckUsernameView
from .views.user_list import UserViewSet
from .views.verify import VerifyUserAPIView, ReSendVerifyUserAPIView
from .views.feedback import FeedbackViewSet
from .views.subscription import SubscriptionViewSet

router = DefaultRouter()
router.register('address', AddressViewSet, basename='address')
router.register('feedback', FeedbackViewSet, basename='feedback')
router.register('subscription', SubscriptionViewSet, basename='subscription')
router.register('user_list', UserViewSet, basename='user_list')

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', SignupView.as_view()),
    path('check_username/', CheckUsernameView.as_view()),
    path('me/', UserMeAPIVIew.as_view()),
    path('verify_user/', VerifyUserAPIView.as_view()),
    path('resend_verify_code/', ReSendVerifyUserAPIView.as_view()),
    path('send_forgot_password/', SendForgotPasswordAPIView.as_view()),
    path('check_forgot_password/', CheckForgotPasswordCodeView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('', include(router.urls)),
]
