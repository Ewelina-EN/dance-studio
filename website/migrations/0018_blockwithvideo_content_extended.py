# Generated by Django 4.1.7 on 2023-05-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_remove_trainer_profile_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockwithvideo',
            name='content_extended',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
