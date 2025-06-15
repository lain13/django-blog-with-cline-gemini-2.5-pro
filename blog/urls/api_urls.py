from django.urls import path
from ..views import api_views

app_name = 'blog-api'

urlpatterns = [
    path('posts/', api_views.PostListAPIView.as_view(), name='post-list-api'),
    path('posts/<int:pk>/', api_views.PostDetailAPIView.as_view(), name='post-detail-api'),
    path('comments/', api_views.CommentListCreateAPIView.as_view(), name='comment-list-api'),
    path('comments/<int:pk>/', api_views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail-api'),
    path('categories/', api_views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('categories/<int:pk>/', api_views.CategoryDetailAPIView.as_view(), name='category-detail-api'),
    path('tags/', api_views.TagListAPIView.as_view(), name='tag-list-api'),
    path('tags/<int:pk>/', api_views.TagDetailAPIView.as_view(), name='tag-detail-api'),
]
