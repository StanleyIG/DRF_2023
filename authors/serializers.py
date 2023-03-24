from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField, Serializer, IntegerField
from rest_framework import serializers
from .models import Author, Book, Biography


class AuthorSerializer(Serializer):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    birthday_year = IntegerField()

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday_year = validated_data.get('birthday_year', instance.birthday_year)
        instance.save()
        return instance

    def create(self, validated_data):
        author = Author(**validated_data)
        author.save()
        return author
    
    def validate_birthday_year(self, value):
        if value > 2004:
            raise serializers.ValidationError('18+')
        return value
    def validate(self, attrs):
        if attrs['last_name'] == 'Пушкин' and attrs['birthday_year'] != 1799:
            raise serializers.ValidationError('Неверный год рождения Пушкина')
        return attrs
    

class BookSerializer(Serializer):
    name = CharField(max_length=64)
    authors = AuthorSerializer(many=True)


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    #authors = AuthorModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BiographyModelSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer()

    class Meta:
        model = Biography
        fields = ['text', 'author']








