from django.urls import path
from ..views import comment_views

urlpatterns = [
    path('post/<int:pk>/comment/', comment_views.CommentCreateView.as_view(), name='add_comment_to_post'),
]
