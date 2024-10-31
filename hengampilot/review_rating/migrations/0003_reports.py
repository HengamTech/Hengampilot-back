# Generated by Django 4.2.16 on 2024-10-29 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("review_rating", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reports",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "resson_select",
                    models.CharField(
                        choices=[
                            ("sexual", "SEXUAL"),
                            ("violence", "VIOLENCE"),
                            ("accusations", "ACCUSATIONS"),
                            ("terrorism", "TERRORISM"),
                        ],
                        max_length=20,
                    ),
                ),
                ("reason", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "review_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_report",
                        to="review_rating.review",
                    ),
                ),
                (
                    "review_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_report",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
