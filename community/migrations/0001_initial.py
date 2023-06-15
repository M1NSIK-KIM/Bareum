# Generated by Django 4.2.1 on 2023-06-15 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="test",
            fields=[
                ("test_id", models.IntegerField(primary_key=True, serialize=False)),
                ("test_date", models.DateField()),
                ("test_contents", models.CharField(max_length=100)),
                ("test_like", models.IntegerField()),
            ],
            options={
                "db_table": "test",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.IntegerField(primary_key=True, serialize=False)),
                ("post_date", models.DateField()),
                ("post_title", models.CharField(max_length=100)),
                ("post_contents", models.CharField(max_length=100)),
                ("post_like", models.IntegerField()),
                ("post_category", models.CharField(max_length=9)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "post",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("comments_id", models.IntegerField(primary_key=True, serialize=False)),
                ("comment_date", models.DateField()),
                ("comment_contents", models.CharField(max_length=100)),
                ("comment_like", models.IntegerField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="community.post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "comments",
                "managed": True,
            },
        ),
    ]
