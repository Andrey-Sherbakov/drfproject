# Generated by Django 5.1.7 on 2025-03-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
