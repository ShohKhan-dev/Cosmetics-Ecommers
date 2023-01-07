# Rest Framework
from rest_framework import serializers

# Project
from banners.models import Banner
from file.serializers import FileSerializer


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        exclude = ('created_datetime', 'modified_datetime')

    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(context=self.context)
        return super(BannerSerializer, self).to_representation(instance)


__all__ = (
    'BannerSerializer',
)
