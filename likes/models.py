from django.conf import settings
from django.db import models


class Like(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "comments.Comment",
        on_delete=models.CASCADE,
        related_name="like_user",
    )
    post = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
        related_name="like_post",
    )


# Create your models here.
