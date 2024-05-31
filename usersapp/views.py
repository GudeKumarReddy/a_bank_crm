from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from usersapp.models import AuditLog
from usersapp.serializers import UserSerializer, CustomTokenObtainPairSerializer

MyUsers = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@staff_member_required
def audit_log_view(request):
    logs = AuditLog.objects.all()
    user = request.GET.get('user')
    # if user:
    #     logs = logs.filter(user__username=user)

    return render(request, 'auditlog/audit_log.html', {'logs': logs})