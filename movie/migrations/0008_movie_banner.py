# Generated by Django 2.2.5 on 2019-09-23 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner'),
        ),
    ]
