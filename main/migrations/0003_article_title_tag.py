# Generated by Django 3.1.4 on 2020-12-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201214_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_tag',
            field=models.CharField(default='title', max_length=100),
        ),
    ]
