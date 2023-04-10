from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField, Serializer, IntegerField, StringRelatedField
from authapp.models import User


class UserModelBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'#['username', 'first_name', 'last_name', 'email']


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']