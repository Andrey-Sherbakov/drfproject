from django.db import models
from django_extensions.db import fields

from .utils import generate_slug


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = fields.AutoSlugField(populate_from=['title'], slugify_function=generate_slug, unique=True,
                                verbose_name='Slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    kp_rating = models.FloatField(blank=True, null=True, verbose_name='Кинопоиск')
    imdb_rating = models.FloatField(blank=True, null=True, verbose_name='IMDb')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=False, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=155, db_index=True, verbose_name='Название категории')
    slug = fields.AutoSlugField(populate_from=['name'], slugify_function=generate_slug, unique=True,
                                verbose_name='Slug')

    def __str__(self):
        return self.name
