# Generated by Django 5.2.3 on 2025-06-24 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_services', '0021_remove_introsection_background_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introsection',
            name='video_url',
        ),
        migrations.AddField(
            model_name='introsection',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='intro_videos/'),
        ),
    ]
