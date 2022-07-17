from django.conf import settings
from django.db import models


class Like(models.Model):
    "Generated Model"
    post = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
        related_name="like_post",
    )
    user = models.OneToOneField(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="like_user",
    )


# Create your models here.
