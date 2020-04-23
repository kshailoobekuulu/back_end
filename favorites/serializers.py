from rest_framework import serializers
from .models import FavoritePost
from django.contrib.auth.models import User
from companies.serializers import PostSerializer


class ListFavoriteSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = FavoritePost
        fields = ['post', ]


class UserDataSerializer(serializers.ModelSerializer):
    favorites = ListFavoriteSerializer(many=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'favorites']
