# Generated by Django 3.1.4 on 2020-12-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
    ]
