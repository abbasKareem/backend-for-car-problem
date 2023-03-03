from rest_framework import serializers
from .models import Post, PostType, CarCountry, CarProblemLocation, CarType, Comment
from datetime import datetime


class CarCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCountry
        fields = ['country_name', 'id']


class CarProblemLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarProblemLocation
        fields = "__all__"


class CarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = ['name', 'id', 'car_country']


class AllCarsSerializer(serializers.ModelSerializer):
    car_country = serializers.SerializerMethodField()

    def get_car_country(self, obj):
        return obj.car_country.country_name

    class Meta:
        model = CarType
        fields = ['name', 'id', 'car_country']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    car_type = serializers.SerializerMethodField()
    problem_location = serializers.SerializerMethodField()
    post_type = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    def get_like_count(self, post):
        return post.likes.count()

    def get_comment_count(self, post):
        return Comment.objects.filter(post=post).count()

    def get_author(self, obj):
        return obj.author.username

    def get_car_type(self, obj):
        return obj.car_type.name

    def get_problem_location(self, obj):
        return obj.problem_location.location

    def get_post_type(self, obj):
        return obj.post_type.name

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'car_type', 'problem_location',
                  'post_type', 'created_at', 'updated_at', 'author', 'main_image', 'image_2', 'image_3', 'image_4', 'image_5', 'like_count', 'comment_count']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = ['id', 'content', 'create_at', 'user', 'post']
