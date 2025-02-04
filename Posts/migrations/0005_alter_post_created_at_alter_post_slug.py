# Generated by Django 5.1.4 on 2024-12-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
