from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ProfileSerializer

from django.contrib.auth import get_user_model


from .models import Profile
from post.models import Post
from post.serializers import PostSerializer

User = get_user_model()


class UserPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            posts = Post.objects.filter(author=user)
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
