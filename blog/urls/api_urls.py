from django.urls import path
from ..views import api_views

app_name = 'blog-api'

urlpatterns = [
    path('', api_views.PostListAPIView.as_view(), name='post-list-api'),
    path('<int:pk>/', api_views.PostDetailAPIView.as_view(), name='post-detail-api'),
]
