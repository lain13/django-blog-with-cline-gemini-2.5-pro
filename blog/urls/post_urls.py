from django.urls import path
from ..views import post_views

app_name = 'blog'

urlpatterns = [
    path('', post_views.post_list, name='post_list'),
    path('post/<int:pk>/', post_views.post_detail, name='post_detail'),
    path('post/new/', post_views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_views.post_delete, name='post_delete'),
    path('search/', post_views.search, name='search'),
    path('tag/<str:tag_name>/', post_views.post_list_by_tag, name='post_list_by_tag'),
]
