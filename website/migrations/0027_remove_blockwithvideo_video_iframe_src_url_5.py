# Generated by Django 4.1.7 on 2023-06-27 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_blockwithvideo_video_iframe_src_url_4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockwithvideo',
            name='video_iframe_src_url_5',
        ),
    ]
