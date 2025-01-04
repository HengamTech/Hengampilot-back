# Generated by Django 4.2.17 on 2025-01-02 09:16

import business_management.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_management', '0005_category_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_image',
            field=models.ImageField(blank=True, null=True, upload_to='business_images/', validators=[business_management.models.validate_image_size, business_management.models.validate_image_dimensions]),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image/', validators=[business_management.models.validate_image_size, business_management.models.validate_image_dimensions]),
        ),
    ]
