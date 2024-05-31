from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from usersapp.models import UserSession

MyUsers = get_user_model()
import random
import string


def create_user_service(data):
    email = data.get('email')
    phone = data.get('phone')
    password = ''.join(random.choice(string.ascii_letters) for _ in range(8))
    user = MyUsers.objects.filter(Q(phone=phone) | Q(email=email))
    print("password is", password)

    if not user:
        user = MyUsers.objects.create(**data)
        user.set_password(password)
        user.save()
        return user, password
    return user.first(), None


class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the input username is an email or a phone number
            if '@' in username:
                user = MyUsers.objects.get(email=username)
            else:
                user = MyUsers.objects.get(phone=username)
        except MyUsers.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user


class UserSerializer(ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=False)

    def create(self, validated_data):
        user, temp_password = create_user_service(validated_data)
        return user

    class Meta:
        fields = "__all__"
        model = MyUsers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return data