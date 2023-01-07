from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from user.models.address import Address
from user.serializers.address import AddressSerializer


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)

        is_last = self.request.query_params.get('is_last', None)

        if is_last:
            return queryset.filter(is_default=True)[0:1]

        return queryset

    def perform_create(self, serializer):
        serializer.is_valid()
        is_default = serializer.validated_data['is_default']
        if is_default is True:
            self.get_queryset().update(is_default=False)
        return serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.is_valid()
        is_default = serializer.validated_data['is_default']
        if is_default is True:
            self.get_queryset().update(is_default=False)
        return serializer.save(user=self.request.user)
