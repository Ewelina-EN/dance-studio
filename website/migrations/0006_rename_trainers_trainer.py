# Generated by Django 4.1.7 on 2023-04-27 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_pricelist_rename_content_1_offer_content_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Trainers",
            new_name="Trainer",
        ),
    ]
