from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, audit_log_view

from usersapp.views import UsersViewSet

router = DefaultRouter()
router.register('management', UsersViewSet)

urlpatterns = [
    path('logs/', audit_log_view, name='audit_log_view'),
    path('', include(router.urls), name='users'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

