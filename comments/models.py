from django.conf import settings
from django.db import models


class Comment(models.Model):
    "Generated Model"
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="comment_post",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment_user",
    )
    comment = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )


# Create your models here.
