# Generated by Django 3.2.8 on 2021-10-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20211020_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=254, verbose_name='Электронная почта'),
        ),
    ]
