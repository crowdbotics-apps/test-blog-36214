# Generated by Django 2.2.26 on 2022-07-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
