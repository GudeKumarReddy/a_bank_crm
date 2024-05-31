from rest_framework import serializers

from customers.models import Customers, Address
from usersapp.serializers import UserSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CustSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()

    class Meta:
        model = Customers
        fields = "__all__"
