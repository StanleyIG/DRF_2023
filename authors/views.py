from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biography
from .serializers import AuthorModelSerializer, AuthorSerializer, BookModelSerializer, BiographyModelSerializer, BookSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, HttpResponseBadRequest
import io
from django.views.decorators.csrf import csrf_exempt



class AuthorModelViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer] можно настроить рендер, например отключить BrowsableAPIRenderer
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


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




