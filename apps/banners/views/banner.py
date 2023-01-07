# Rest-Framework
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

# Project
from banners.models import Banner
from banners.serializers import BannerSerializer
from core.permissions import IsAdminOrReadOnly


class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('language', 'tag')

    def get_queryset(self):
        if self.request.query_params.get('is_active', None):
            return self.queryset.filter(is_active=True)
        return self.queryset

    @action(methods=['POST'], detail=False)
    def admin(self, request):
        queryset = Banner.objects.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


__all__ = (
    'BannerViewSet',
)
