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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorModelViewSet, author_get, author_post, book_get, BookModelViewSet, BiographyModelViewSet, BookListAPIView, BookModelLimitedViewSet
from authors.views import book_api_get, BookApiView
from authapp.views import UserModelViewSet
from toDoapp.views import ProjectModelViewSet, ToDoModelViewSet
from django.views.generic import RedirectView
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact
from django.views.generic import TemplateView


#response = requests.post('http://127.0.0.1:8000/api-token-auth/', data={'username':
#'admin', 'password': 'admin'})

#print(response.status_code)
#print(response.json())

schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='2.0',
        description='description',
        license=License(name='MIT'),
        contact=Contact(email='test@example.ru')
    )
)


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
    #path('api/2.0/', include((router.urls, 'library'), namespace='2.0')), # способ NamespaceVersioning c общим namecpace(общая версия) для всех urls
    #path('api/2.0/', include('authors.urls', namespace='2.0')),
    path('api/authors_2.0/', include('authors.urls', namespace='2.0')), # отдельный вариант когда нужен отдельный апи
    path('api/authors_v2/', include('authors.urls', namespace='2.0')), # названия адреса может быть разным
    path('api/authors_v1/', include('authors.urls', namespace='1.0')), # допустим нужен апи с который имеет другую версию и отдаёт иные данные
    #path('api/users_2.0/', include('authapp.urls', namespace='3.0')),                                                                 
    path('author_get', author_get),
    path('book_get', book_get),
    path('book_get/<int:pk>', book_get),
    path('author_get/<int:pk>', author_get),
    path('author_post', author_post),
    path('author_post/<int:pk>', author_post),
    path('book_list_api', BookListAPIView.as_view()),
    path('book_view_api', BookApiView.as_view()),
    #re_path('swagger', schema_view.with_ui()),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    #re_path('swagger', schema_view.without_ui()),
    #path('redoc/', TemplateView.as_view(
    #    template_name='redoc.html',
    #    extra_context={'schema_url':'openapi-schema'}
    #), name='redoc'),
    #path('openapi-schema/', schema_view.without_ui(cache_timeout=0), name='openapi-schema'),
    #path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc'),
    #re_path(r'api/(?P<version>\d.\d)/authors', AuthorModelViewSet.as_view({'get': 'list', 'post': 'create'})),  #способ URLPathVersioning

]