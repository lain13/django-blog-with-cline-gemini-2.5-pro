from django.db import models


class Tag(models.Model):
    """태그 모델"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
