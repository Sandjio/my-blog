# Generated by Django 5.1.4 on 2024-12-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/'),
        ),
    ]