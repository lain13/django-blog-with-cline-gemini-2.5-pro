from django.conf import settings
from django.db import models

class Vote(models.Model):
    """
    사용자가 게시물에 대해 한 투표(좋아요/싫어요)를 나타냅니다.
    """
    LIKE = 1
    DISLIKE = -1
    VOTE_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=VOTE_CHOICES)

    class Meta:
        # 사용자는 하나의 게시물에 한 번만 투표할 수 있습니다.
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} voted {self.get_value_display()} on '{self.post.title}'"
