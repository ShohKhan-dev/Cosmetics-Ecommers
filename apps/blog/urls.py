from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet, TagViewSet

router = DefaultRouter()
router.register('blog', BlogViewSet, 'blog')
router.register('tag', TagViewSet, 'tag')

urlpatterns = [
    path('', include(router.urls))
]
