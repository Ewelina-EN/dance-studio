# Generated by Django 4.1.7 on 2023-05-08 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0018_blockwithvideo_content_extended"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blockwithvideo",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="contactdata",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="offer",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="pricelist",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="scheduleitem",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="trainer",
            old_name="title",
            new_name="title1",
        ),
        migrations.RenameField(
            model_name="weekday",
            old_name="title",
            new_name="title1",
        ),
    ]
