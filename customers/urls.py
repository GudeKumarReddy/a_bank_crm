from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customers.views import CustViewSet

router = DefaultRouter()
router.register("management", CustViewSet)

urlpatterns = [
    path('', include(router.urls))
]
