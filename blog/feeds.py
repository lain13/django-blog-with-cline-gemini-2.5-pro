from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Category, Post

class LatestPostsFeed(Feed):
    title = "My Django Blog"
    link = "/feed/"
    description = "블로그의 새로운 게시물"

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog:post_detail', args=[item.pk])

    def item_author_name(self, item):
        return item.author.username

    def item_pubdate(self, item):
        return item.created_at

class CategoryFeed(LatestPostsFeed):
    """카테고리별 RSS 피드"""

    def get_object(self, request, category_slug):
        return get_object_or_404(Category, slug=category_slug)

    def link(self, obj):
        return reverse('blog:post_list_by_category', args=[obj.slug])

    def title(self, obj):
        return f"Posts in category '{obj.name}'"

    def description(self, obj):
        return f"The latest posts in category '{obj.name}'."

    def items(self, obj):
        return Post.objects.filter(category=obj).order_by('-created_at')[:5]
