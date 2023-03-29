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
from authors.views import AuthorModelViewSet, author_get, author_post, book_get, BookModelViewSet, BiographyModelViewSet, BookListAPIView, BookModelLimitedViewSet
from authors.views import book_api_get, BookApiView
from authapp.views import UserModelViewSet
from toDoapp.views import ProjectModelViewSet, ToDoModelViewSet
from django.views.generic import RedirectView
from rest_framework.authtoken import views
import requests


#response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
#'admin', 'password': 'admin'})

#print(response.status_code)
#print(response.json())


router = DefaultRouter()
#router = SimpleRouter() отличается только тем, что нет разводящей страницы api c api ссылками
router.register('authors', AuthorModelViewSet)
router.register('user', UserModelViewSet)
router.register('biographies', BiographyModelViewSet)
#router.register('books', BookModelViewSet)
router.register('books', BookModelLimitedViewSet)
router.register('Project', ProjectModelViewSet)
router.register('ToDo_notes', ToDoModelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="api/")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('author_get', author_get),
    path('book_get', book_get),
    path('book_get/<int:pk>', book_get),
    path('author_get/<int:pk>', author_get),
    path('author_post', author_post),
    path('author_post/<int:pk>', author_post),
    path('book_list_api', BookListAPIView.as_view()),
    path('book_view_api', BookApiView.as_view())
    
]