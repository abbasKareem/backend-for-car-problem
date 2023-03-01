
from django.urls import path, include
from .views import *


urlpatterns = [
    path('countries/', AllCarCountryView.as_view()),
    path('countries/<int:id>', AllCarByCountryIdView.as_view()),
    path('posts/', PostView.as_view()),
    path('all-cars/', AllCarsView.as_view()),
    path('car-problem-location/', CarProblemLocationView.as_view()),
    path('cars/<str:name>/', PostListView.as_view(), name='post_list'),

]
