from django.db import models


class Tag(models.Model):
    """태그 모델"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """블로그 게시글 모델"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """블로그 댓글 모델"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
