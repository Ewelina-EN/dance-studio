# Generated by Django 4.1.7 on 2023-04-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0006_rename_trainers_trainer"),
    ]

    operations = [
        migrations.AddField(
            model_name="offer",
            name="photo",
            field=models.ImageField(default="", upload_to="offer"),
            preserve_default=False,
        ),
    ]