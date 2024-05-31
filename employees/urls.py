from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees.views import EmpViewSet, ProductViewSet

router = DefaultRouter()
router.register('management', EmpViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
