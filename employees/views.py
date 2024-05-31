from django.db import transaction
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from employees.models import Employees, Product
from employees.serializers import EmpSerializer, ProductSerializer
from usersapp.serializers import create_user_service


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        data = request.data
        user = data['user']
        if 'phone' not in user:
            raise ValidationError({"error": "phone field is required"})
        if 'email' not in user:
            raise ValidationError({"error": "email field is required"})

        emp, password = create_user_service(user)
        data['user'] = emp
        if Employees.objects.filter(user=data['user']).exists():
            raise ValidationError({"error": "Employee already exists"})
        create_employee = Employees.objects.create(**data)
        serializer = self.serializer_class(create_employee)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
