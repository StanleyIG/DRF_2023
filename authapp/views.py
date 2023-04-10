from rest_framework.viewsets import ModelViewSet, GenericViewSet
from authapp.models import User
from authapp.serializers import UserModelSerializer, UserModelBaseSerializer
from rest_framework import mixins
#from rest_framework.response import Response
#from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class UserModelViewSet(mixins.ListModelMixin, 
                       mixins.RetrieveModelMixin, 
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    pagination_class = UserLimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = UserModelBaseSerializer


    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializer
        return UserModelBaseSerializer