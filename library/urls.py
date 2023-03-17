"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorModelViewSet, author_get, author_post, book_get, BookModelViewSet, BiographyModelViewSet
from authapp.views import UserModelViewSet
from django.views.generic import RedirectView


router = DefaultRouter()
#router = SimpleRouter() отличается только тем, что нет разводящей страницы api c api ссылками
router.register('authors', AuthorModelViewSet)
router.register('user', UserModelViewSet)
router.register('biographies', BiographyModelViewSet)
router.register('books', BookModelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="api/")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('author_get', author_get),
    path('book_get', book_get),
    path('book_get/<int:pk>', book_get),
    path('author_get/<int:pk>', author_get),
    path('author_post', author_post),
    path('author_post/<int:pk>', author_post)
    
]