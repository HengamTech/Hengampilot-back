# Generated by Django 4.2.16 on 2025-01-02 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0004_user_user_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_picture",
        ),
    ]
