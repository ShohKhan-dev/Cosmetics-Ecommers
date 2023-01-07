# Rest-Framework
from rest_framework import serializers

# Project
from user.models import User


class UserMeSerializer(serializers.ModelSerializer):
    # phone_number = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'user_type',
            'speciality',
            'phone_number',
            'company_name',
        ]

    # def get_phone_number(self, obj: User):
    #     address = obj.addresses.filter(is_default=True).first()
    #     if address is not None:
    #         return address.phone_number

    def get_company_name(self, obj: User):
        if obj.user_type == User.ENTITY:
            address = obj.addresses.filter(is_default=True).first()
            if address is not None:
                return address.company_name


class UserAddressSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()
    billing_address = serializers.SerializerMethodField()
    shipping_address = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'user_type',
            'speciality',
            'phone_number',
            'billing_address',
            'shipping_address',
        ]

    def get_phone_number(self, obj: User):
        if obj.user_type == User.BEAUTICIAN:
            address = obj.addresses.filter(is_default=True).first()
            if address is not None:
                return address.phone_number

    def get_billing_address(self, obj: User):
        address = obj.addresses.filter(is_default=True).first()
        if address:
            return {
                "first_name": address.first_name,
                "last_name": address.last_name,
                "company_name": address.company_name,
                "street_name": address.street_name,
                "house_number": address.house_number,
                "city": address.city,
                "email": address.email,
                "zip_code": address.zip_code,
                "phone_number": address.phone_number,
            }

    def get_shipping_address(self, obj: User):
        address = obj.addresses.filter(is_default=True).first()
        if address:
            if address.is_different_shipping_address:
                return {
                    "shipping_first_name": address.shipping_first_name,
                    "shipping_last_name": address.shipping_last_name,
                    "shipping_company_name": address.shipping_company_name,
                    "shipping_street_name": address.shipping_street_name,
                    "shipping_house_number": address.shipping_house_number,
                    "shipping_city": address.shipping_city,
                    "shipping_email": address.shipping_email,
                    "shipping_zip_code": address.shipping_zip_code,
                    "shipping_phone_number": address.shipping_phone_number,
                }
