from django.urls import path
from ..views import post_views

urlpatterns = [
    path('', post_views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', post_views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', post_views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', post_views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', post_views.PostDeleteView.as_view(), name='post_delete'),
    path('search/', post_views.SearchView.as_view(), name='search'),
    path('tag/<str:tag_name>/', post_views.TagFilteredPostListView.as_view(), name='post_list_by_tag'),
]
