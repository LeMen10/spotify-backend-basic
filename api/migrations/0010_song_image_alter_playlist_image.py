# Generated by Django 5.1.7 on 2025-04-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_playlist_description_playlist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='song_images/'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='playlist_images/'),
        ),
    ]
