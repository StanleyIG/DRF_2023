from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField, Serializer, IntegerField, StringRelatedField
from authapp.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'