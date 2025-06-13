from django.urls import path
from ..feeds import LatestPostsFeed, CategoryFeed

urlpatterns = [
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('rss/category/<slug:category_slug>/', CategoryFeed(), name='category_feed'),
]
