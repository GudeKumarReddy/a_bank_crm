from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserSession
import requests
from django.contrib.auth import get_user_model

MyUsers = get_user_model()
@receiver(user_logged_in, sender=MyUsers)
def log_user_login(sender, request, user, **kwargs):
    print("im in ...")
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    UserSession.objects.create(user=user, login_time=now(), ip_address=ip_address, system_details=user_agent)

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    session = UserSession.objects.filter(user=user, logout_time__isnull=True).last()
    if session:
        session.logout_time = now()
        session.save()
