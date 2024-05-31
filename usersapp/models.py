from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from bankcrm.settings import AUTH_USER_MODEL
from usersapp.utils.usermanager import CustomUserManager
# x=AUTH_USER_MODEL

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class MyUsers(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'My Users'


class AuditLog(models.Model):
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    api = models.TextField()
    description = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    status_code = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.action} - {self.timestamp}'


class UsersLog(models.Model):
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    description = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    status_code = models.CharField(max_length=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)
    changes = models.CharField(max_length=255, blank=True)
    object_repr = models.TextField(blank=True)


class UserSession(models.Model):
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    system_details = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.login_time}'


    
