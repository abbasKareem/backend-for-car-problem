from django.db.models import Q
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import permissions, status, authentication, pagination
from .serializers import *
from .models import *

from account.serializers import UserCreateSerializer, ProfileSerializer
from account.models import Profile

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response({
            # 'current_page': self.page.number,
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            # 'last_page': self.page.paginator.num_pages,
            # 'next': self.get_next_link(),
            # 'previous': self.get_previous_link(),
            'total': self.page.paginator.count,
            'results': data
        })


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(id=request.user.id)
            user_serializer = UserCreateSerializer(user)

            profile = Profile.objects.get(user=request.user)
            profile_serializer = ProfileSerializer(profile)

            posts = Post.objects.filter(author=request.user)
            post_serializer = PostSerializer(posts, many=True)

            data = {
                'user_information': user_serializer.data,
                'user_profile': profile_serializer.data,
                'user_posts': post_serializer.data
            }

            return Response(data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class PostView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    pagination_class = CustomPagination


class AllCarsView(ListAPIView):
    queryset = CarType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AllCarsSerializer
    pagination_class = None


class CarProblemLocationView(ListAPIView):
    queryset = CarProblemLocation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarProblemLocationSerializer
    pagination_class = None


class AllCarCountryView(ListAPIView):
    queryset = CarCountry.objects.all().order_by('id')
    permission_classes = [permissions.AllowAny]
    serializer_class = CarCountrySerializer


class AllCarByCountryIdView(ListAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        id = self.kwargs['id']
        return self.queryset.filter(car_country__pk=id)


class PostListView(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination

    def get(self, request, name=None):
        location = request.query_params.get('location', None)
        if location:
            posts = Post.objects.filter(Q(car_type__name=name) & Q(
                problem_location__location=location)).order_by('-id')
            paginator = self.pagination_class()
            paginated_posts = paginator.paginate_queryset(posts, request)
            serialized_posts = PostSerializer(paginated_posts, many=True)
            return paginator.get_paginated_response(serialized_posts.data)
        else:
            posts = Post.objects.filter(car_type__name=name).order_by('-id')
            paginator = self.pagination_class()
            paginated_posts = paginator.paginate_queryset(posts, request)
            serialized_posts = PostSerializer(paginated_posts, many=True)
            return paginator.get_paginated_response(serialized_posts.data)


class GetPostByIdView(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination

    def get(self, request, post_id=None):
        post = Post.objects.get(id=post_id)

        serializered_data = PostSerializer(post, many=False)
        return Response(serializered_data.data)


class GetAllCommentsOfPostView(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = CustomPagination

    def get(self, request, post_id=None):
        comments = Comment.objects.filter(post=post_id)
        paginator = self.pagination_class()
        paginated_comments = paginator.paginate_queryset(comments, request)
        serialized_comments = CommentSerializer(paginated_comments, many=True)
        return paginator.get_paginated_response(serialized_comments.data)


class CreateCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        content = request.data.get('content')
        user = request.user
        try:
            print(post_id)
            post = Post.objects.get(id=post_id)
            comment = Comment.objects.create(
                content=content, post=post, user=user)
            comment.save()
            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)

        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)


class CreateLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        user = request.user
        like_from_db = Like.objects.filter(user=user)
        if like_from_db.exists():
            like_from_db.delete()
            return Response({"message": "Unlike successfully"}, status=status.HTTP_200_OK)
        like = Like.objects.create(post_id=post_id, user=user)
        like.save()
        return Response({'message': 'Like create Successfully'}, status=status.HTTP_201_CREATED)


class CheckIsLikedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id=None):
        is_liked = Like.objects.filter(
            post_id=post_id, user=request.user).exists()
        if is_liked:
            return Response({'is_liked': is_liked})
        return Response({'is_liked': is_liked})
