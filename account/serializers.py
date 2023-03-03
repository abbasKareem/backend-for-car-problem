from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from post.models import Post
from post.serializers import PostSerializer

from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["first_name", "last_name",
                  "bio", "image"]
    # def update(self, instance, validated_data):
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email",
                  "start_date"]
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user

    # def update(self, instance, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     profile = instance.profile

    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.save()

    #     profile.city = profile_data.get('city', profile.city)
    #     profile.save()

    #     return instance
