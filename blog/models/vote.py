from django.db import models
from django.conf import settings

class Vote(models.Model):
    """
    Represents a vote (like/dislike) on a Post by a User.
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
        # A user can only vote once on a single post
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} voted {self.get_value_display()} on '{self.post.title}'"
