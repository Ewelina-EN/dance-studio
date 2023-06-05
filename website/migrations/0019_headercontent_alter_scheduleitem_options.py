# Generated by Django 4.1.7 on 2023-06-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_blockwithvideo_content_extended'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True, help_text='Czy to ma się wyświetlać na stronie?', verbose_name='aktywne?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='scheduleitem',
            options={'ordering': ['start_time']},
        ),
    ]