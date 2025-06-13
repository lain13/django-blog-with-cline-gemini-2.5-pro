from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Post
from ..serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
