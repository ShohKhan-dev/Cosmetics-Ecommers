# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters import rest_framework as filters

# Project
from blog.serializers import TagSerializer, BlogListSerializer
from blog.models import Tag, Blog


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super(TagViewSet, self).get_permissions()


class BlogViewSet(ModelViewSet):
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('tag',)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super(BlogViewSet, self).get_permissions()


__all__ = ['BlogViewSet', 'TagViewSet']
