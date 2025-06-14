from django.conf import settings
from django.db import models
from django.urls import reverse

from .category import Category
from .tag import Tag


class Post(models.Model):
    """블로그 게시글 모델"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    view_count = models.PositiveIntegerField(default=0, verbose_name="조회수")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """게시글의 상세 페이지 URL을 반환합니다."""
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def get_vote_count(self):
        """게시글의 총 투표 수를 반환합니다. (좋아요 - 싫어요 아님)"""
        return self.votes.count()

    def increase_view_count(self):
        """조회수를 1 증가시킵니다."""
        self.view_count += 1
        self.save(update_fields=['view_count'])

    @property
    def like_count(self):
        """게시글의 좋아요 수를 반환합니다."""
        return self.votes.filter(value=1).count()

    @property
    def dislike_count(self):
        """게시글의 싫어요 수를 반환합니다."""
        return self.votes.filter(value=-1).count()
