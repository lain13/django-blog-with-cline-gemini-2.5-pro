from django.urls import path
from ..feeds import LatestPostsFeed

urlpatterns = [
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
