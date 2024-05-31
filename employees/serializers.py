from rest_framework import serializers

from employees.models import Employees, Product
from usersapp.serializers import UserSerializer


class EmpSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employees
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
