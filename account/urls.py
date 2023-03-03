from django.urls import path
from .views import UserPostsAPIView
urlpatterns = [
    path('users/<int:user_id>/posts/',
         UserPostsAPIView.as_view(), name='user_posts'),
]
