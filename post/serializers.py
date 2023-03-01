from rest_framework import serializers
from .models import Post, PostType, CarCountry, CarProblemLocation, CarType
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
    # created_at = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username

    def get_car_type(self, obj):
        return obj.car_type.name

    def get_problem_location(self, obj):
        return obj.problem_location.location

    def get_post_type(self, obj):
        return obj.post_type.name

    # def get_created_at(self, obj):
    #     created_at_str = obj.created_at
    #     created_at = datetime.fromisoformat(created_at_str[:-1] + "+00:00")
    #     date_str = created_at.strftime("%Y-%m-%d")
    #     time_str = created_at.strftime("%-I%p").lower()
    #     formatted_str = f"{date_str} at {time_str}"

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'car_type', 'problem_location',
                  'post_type', 'created_at', 'updated_at', 'author', 'main_image', 'image_2', 'image_3', 'image_4', 'image_5']
