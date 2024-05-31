from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from customers.models import Customers, Address
from customers.serializers import CustSerializer
from usersapp.serializers import create_user_service


class CustViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user, password = create_user_service(data['user'])
        data['user'] = user
        if 'address' in data:
            data['address'] = Address.objects.create(**data['address'])
        cust = Customers.objects.create(**data)
        serializer = self.serializer_class(cust)

        return Response(serializer.data)


