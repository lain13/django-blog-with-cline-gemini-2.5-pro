from django.urls import path
from ..views import comment_views

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/comment/', comment_views.add_comment_to_post, name='add_comment_to_post'),
]
