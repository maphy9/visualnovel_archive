from rest_framework import serializers
from .models import *

class Request_get_visualnovel_serializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255, trim_whitespace=True)

class Request_get_visualnovels_by_genre_serializer(serializers.Serializer):
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), required=True
    )
    page_size = serializers.IntegerField(min_value=1, max_value=50, required=True)
    page_number = serializers.IntegerField(min_value=1, required=True)

class Request_get_visualnovels_by_developer_serializer(serializers.Serializer):
    developer = serializers.PrimaryKeyRelatedField(
        queryset=Developer.objects.all(), required=True
    )
    page_size = serializers.IntegerField(min_value=1, max_value=50, required=True)
    page_number = serializers.IntegerField(min_value=1, required=True)

class Request_get_visualnovels_by_publisher_serializer(serializers.Serializer):
    publisher = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), required=True
    )
    page_size = serializers.IntegerField(min_value=1, max_value=50, required=True)
    page_number = serializers.IntegerField(min_value=1, required=True)


class Request_get_user_by_username_serializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=150, trim_whitespace=True)


class Request_search_serializer(serializers.Serializer):
    phrase = serializers.CharField(required=True, max_length=255, trim_whitespace=True, allow_blank=True)
    count = serializers.IntegerField(required=True, min_value=1, max_value=32)


class Request_create_visualnovel_serializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=255, trim_whitespace=True)
    content = serializers.CharField(required=True, trim_whitespace=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=True
    )
    developer = serializers.PrimaryKeyRelatedField(
        queryset=Developer.objects.all(), allow_null=True, required=True
    )
    publishers = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), many=True, required=True
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, required=True
    )

class Request_create_genre_serializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=32, trim_whitespace=True)

class Request_create_developer_serializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=128, trim_whitespace=True)

class Request_create_publisher_serializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=128, trim_whitespace=True)