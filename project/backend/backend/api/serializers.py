from rest_framework import serializers
from .models import *

class VisualNovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisualNovel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "profile_picture", "role"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = '__all__'