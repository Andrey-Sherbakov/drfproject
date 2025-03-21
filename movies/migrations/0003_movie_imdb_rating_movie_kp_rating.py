# Generated by Django 5.1.7 on 2025-03-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='imdb_rating',
            field=models.FloatField(blank=True, null=True, verbose_name='IMDb'),
        ),
        migrations.AddField(
            model_name='movie',
            name='kp_rating',
            field=models.FloatField(blank=True, null=True, verbose_name='Кинопоиск'),
        ),
    ]
