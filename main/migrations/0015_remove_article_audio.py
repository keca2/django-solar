# Generated by Django 3.1.4 on 2020-12-24 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='audio',
        ),
    ]