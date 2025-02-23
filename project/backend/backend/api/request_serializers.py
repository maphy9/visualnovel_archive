from rest_framework import serializers
from .models import *

class Request_get_best_visual_novels_serializer(serializers.Serializer):
    page_size = serializers.IntegerField(min_value=1, max_value=32)
    page_number = serializers.IntegerField(min_value=1)

class Request_get_best_discussions_serializer(Request_get_best_visual_novels_serializer):
    pass

class Request_get_best_users_serializer(Request_get_best_visual_novels_serializer):
    pass

class Request_find_by_phrase(Request_get_best_visual_novels_serializer):
    phrase = serializers.CharField(allow_blank=True)