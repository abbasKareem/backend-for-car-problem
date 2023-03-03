from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class CarCountry(models.Model):
    country_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.country_name


class CarType(models.Model):
    name = models.CharField(max_length=100)
    car_country = models.ForeignKey(
        CarCountry, on_delete=models.CASCADE, related_name="car_country")
    photo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class CarProblemLocation(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


class PostType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    car_type = models.ForeignKey(
        CarType, on_delete=models.CASCADE, related_name="car_type_post")
    problem_location = models.ForeignKey(
        CarProblemLocation, on_delete=models.CASCADE, related_name="problem_location_post")
    post_type = models.ForeignKey(
        PostType, on_delete=models.CASCADE, related_name="type_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.CharField(max_length=200, null=True, blank=True)
    image_2 = models.CharField(max_length=200, null=True, blank=True)
    image_3 = models.CharField(max_length=200, null=True, blank=True)
    image_4 = models.CharField(max_length=200, null=True, blank=True)
    image_5 = models.CharField(max_length=200, null=True, blank=True)

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
