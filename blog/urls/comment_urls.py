from django.urls import path
from ..views import comment_views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/comment/new/', comment_views.CommentCreateView.as_view(), name='comment_new'),
    path('comment/<int:pk>/edit/', comment_views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', comment_views.CommentDeleteView.as_view(), name='comment_delete'),
]
