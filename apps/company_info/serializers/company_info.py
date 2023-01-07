from rest_framework import serializers
from company_info.models import CompanyInfo


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = [
            "id",
            "name", 
            "address", 
            "city", 
            "contact_number", 
            "latitude", 
            "longitude",
        ]
        extra_kwargs = {
            "longitude": {'required': True}, 
            "latitude":{'required': True}
        }
