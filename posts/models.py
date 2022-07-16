from django.conf import settings
from django.db import models


class Post(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        max_length=250,
    )
    image = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="post_user",
    )


# Create your models here.
