# Generated by Django 4.2.16 on 2024-10-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Ehsan', max_length=50, unique=True),
        ),
    ]