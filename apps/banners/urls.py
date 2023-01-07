from django.urls import path
from rest_framework.routers import DefaultRouter
from banners.views.banner import BannerViewSet
# from banners.views.instagram import InstagramPosts

router = DefaultRouter()
router.register("banner", BannerViewSet, "banner")

urlpatterns = [
    # path("instagram/", InstagramPosts.as_view())
]

urlpatterns += router.urls
