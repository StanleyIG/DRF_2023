from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Author, Book, Biography
from .serializers import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BiographyModelSerializer, BookSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from django.http import HttpResponse, HttpResponseBadRequest
import io
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, \
     DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
"""
Рассмотрим основные виды прав, встроенных в DRF:
1. AllowAny — доступ есть у всех пользователей, включая неавторизованных.
2. IsAuthenticated — доступ есть только у авторизованных пользователей.
3. IsAdminUser — доступ есть только у администратора.
4. IsAuthenticatedOrReadOnly — доступ есть у авторизованных пользователей, у
неавторизованных — доступ только на просмотр данных.
5. DjangoModelPermissions — использует систему прав Django на модели. Для каждой модели у
пользователя могут быть права add, change, delete, view.
6. DjangoModelPermissionsOrReadOnly — аналогично DjangoModelPermissions, но с правом на
просмотр у пользователей, не обладающих другими правами.
"""


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
        #return request.user.username == 'admin' либо так как вариант


class AuthorLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4

class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer] можно настроить рендер, например отключить BrowsableAPIRenderer
    pagination_class = AuthorLimitOffsetPagination
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    #permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    
    @action(detail=True, methods=['get'])
    def get_author_name(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return Response({'name': str(author)})
    
    def get_queryset(self):
        last_name = self.request.query_params.get('last_name', None)
        if last_name:
            return Author.objects.filter(last_name__icontains=last_name)
        return Author.objects.all()



class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class BookApiView(APIView):
    #renderer_classes = [JSONRenderer]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    

class BookModelLimitedViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    #mixins.CreateModelMixin,
    GenericViewSet
):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
    pagination_class = BookLimitOffsetPagination
    

class BookListAPIView(ListAPIView):
    #renderer_classes = [JSONRenderer]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def book_api_get(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def book_get(request, pk=None):
    if pk is not None:
        books = Book.objects.get(pk=pk)
        serializer = BookSerializer(books)
    else:
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)    
    
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


def author_get(request, pk=None):
    if pk is not None:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
    else:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
    
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

@csrf_exempt
def author_post(request, pk=None):
    json_data = JSONParser().parse(io.BytesIO(request.body))
    #serializer = AuthorSerializer(data=json_data)
    if request.method == 'POST':
        serializer = AuthorSerializer(data=json_data)

    elif request.method == 'PUT':
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=json_data)
 

    elif request.method == 'PATCH':      
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=json_data, partial=True)
        

    if serializer.is_valid():
       author = serializer.save()

       serializer = AuthorSerializer(author)
       json_data = JSONRenderer().render(serializer.data)
       return HttpResponse(json_data)

    return HttpResponseBadRequest()




