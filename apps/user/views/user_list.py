# Rest-Framework
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework import filters, status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Project
from user.models import User
from user.serializers.me import UserMeSerializer


class UserViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    GenericViewSet
):
    permission_classes = [IsAdminUser]
    serializer_class = UserMeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username', 'phone_number']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        user_list = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        return user_list
