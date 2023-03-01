from django.db.models import Q
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import permissions, status, authentication, pagination
from .serializers import *
from .models import *

# pagination.PageNumberPagination()


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

# class CustomPagination(PageNumberPagination):
#     page_size = 2

#     def get_paginated_response(self, data):
#         return Response(data)
#         # return Response({
#         #     'results': data
#         # })


class PostView(ListAPIView):
    queryset = Post.objects.all()
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
    queryset = CarCountry.objects.all()
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
