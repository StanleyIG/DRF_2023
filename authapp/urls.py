from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserModelViewSet

app_name = 'authapp'

router = DefaultRouter()
# router = SimpleRouter()
router.register('user', UserModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
