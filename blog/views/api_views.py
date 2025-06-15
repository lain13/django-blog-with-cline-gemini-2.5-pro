from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..permissions import IsOwnerOrReadOnly
from ..models import Post, Comment, Category, Tag
from ..serializers import PostSerializer, CommentSerializer, CategorySerializer, TagSerializer

class PostListAPIView(generics.ListCreateAPIView):
    """
    모든 게시물을 나열하거나 새 게시물을 생성하는 API 뷰입니다.
    """
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    단일 게시물을 조회, 업데이트 또는 삭제하는 API 뷰입니다.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    """
    모든 댓글을 나열하거나 새 댓글을 생성하는 API 뷰입니다.
    """
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    단일 댓글을 조회, 업데이트 또는 삭제하는 API 뷰입니다.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CategoryListAPIView(generics.ListAPIView):
    """
    모든 카테고리를 나열하는 API 뷰입니다.
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    단일 카테고리를 조회하는 API 뷰입니다.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagListAPIView(generics.ListAPIView):
    """
    모든 태그를 나열하는 API 뷰입니다.
    """
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagDetailAPIView(generics.RetrieveAPIView):
    """
    단일 태그를 조회하는 API 뷰입니다.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
