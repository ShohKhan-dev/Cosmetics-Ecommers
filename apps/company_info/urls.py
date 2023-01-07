from django.urls import path, include
from rest_framework.routers import DefaultRouter
from company_info.views.company_info import CompanyInfoViewSet


router = DefaultRouter()
router.register('company_info', CompanyInfoViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]