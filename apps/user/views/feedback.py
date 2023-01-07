from datetime import datetime, timedelta

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from user.serializers.feedback import FeedBackSerializer
from user.models import FeedBack
from rest_framework.permissions import AllowAny


class FeedbackViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]

        return super().get_permissions()

    def get_queryset(self):
        queryset = self.queryset
        six_months_ago = datetime.now() - timedelta(days=180)
        return queryset.filter(created_datetime__gte=six_months_ago)


__all__ = ['FeedbackViewSet']
