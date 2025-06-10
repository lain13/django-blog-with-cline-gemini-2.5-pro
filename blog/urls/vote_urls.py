from django.urls import path
from ..views.vote_views import VoteView

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/vote/', VoteView.as_view(), name='post_vote'),
]
