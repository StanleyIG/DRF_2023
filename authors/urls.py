from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet

app_name = 'authors'

router = DefaultRouter()
# router = SimpleRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)
router.register('biographies', BiographyModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
