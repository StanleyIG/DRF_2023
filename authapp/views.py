from rest_framework.viewsets import ModelViewSet, GenericViewSet
from authapp.models import User
from authapp.serializers import UserModelSerializer
from rest_framework import mixins
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination


#class UserLimitOffsetPagination(LimitOffsetPagination):
#    default_limit = 2


class UserModelViewSet(mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    #pagination_class = UserLimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = UserModelSerializer