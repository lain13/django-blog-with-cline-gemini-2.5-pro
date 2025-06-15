from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..permissions import IsOwnerOrReadOnly
from ..models import Post, Comment, Category, Tag
from ..serializers import PostSerializer, CommentSerializer, CategorySerializer, TagSerializer

class PostListAPIView(generics.ListCreateAPIView):
    """
    API view to list all posts or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a single post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    API view to list all comments or create a new comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a single comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CategoryListAPIView(generics.ListAPIView):
    """
    API view to list all categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagListAPIView(generics.ListAPIView):
    """
    API view to list all tags.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a single tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
