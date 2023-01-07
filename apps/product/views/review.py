from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from product.serializers.review import ProductReviewListSerializer
from product.models.review import ProductReview


class ProductReviewListViewSet(ModelViewSet):
    serializer_class = ProductReviewListSerializer
    queryset = ProductReview.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('product', 'stars')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(ProductReviewListViewSet, self).get_permissions()


__all__ = ['ProductReviewListViewSet']
