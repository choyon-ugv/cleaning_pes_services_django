# Generated by Django 5.2.3 on 2025-06-24 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cleaning_services', '0019_herosection'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='intro/')),
                ('heading', models.CharField(max_length=255)),
                ('video_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
