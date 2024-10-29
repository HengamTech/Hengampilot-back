# Generated by Django 4.2.16 on 2024-10-29 05:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business",
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
                    "status",
                    models.CharField(
                        choices=[
                            ("golden", "GOLDEN"),
                            ("silver", "SILVER"),
                            ("tan", "TAN"),
                        ],
                        default="tan",
                        max_length=20,
                    ),
                ),
                ("business_name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("website_url", models.CharField(blank=True, max_length=50, null=True)),
                ("average_rank", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]