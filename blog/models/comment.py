from django.conf import settings
from django.db import models
from django.urls import reverse

from .post import Post


class Comment(models.Model):
    """블로그 댓글 모델"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )

    def __str__(self):
        return f'{self.author.username}: {self.text}'

    def get_absolute_url(self):
        """댓글이 달린 포스트의 상세 페이지로 이동"""
        return reverse('blog:post_detail', kwargs={'pk': self.post.pk})
