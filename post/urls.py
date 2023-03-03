
from django.urls import path, include
from .views import *


urlpatterns = [
    path('countries/', AllCarCountryView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('countries/<int:id>', AllCarByCountryIdView.as_view()),
    path('posts/', PostView.as_view()),
    path('all-cars/', AllCarsView.as_view()),
    path('car-problem-location/', CarProblemLocationView.as_view()),
    path('cars/<str:name>/', PostListView.as_view(), name='post_list'),
    path('posts/<int:post_id>/comments/',
         GetAllCommentsOfPostView.as_view(), name='comment_list'),
    path('posts/<int:post_id>/', GetPostByIdView.as_view(), name='post_details'),
    path('posts/comments/', CreateCommentView.as_view(), name='create_comment'),
    path('posts/add-like/', CreateLikeView.as_view(), name='create_like'),
    path('posts/<int:post_id>/is-liked/',
         CheckIsLikedView.as_view(), name='check_is_liked'),

]
