from django.utils.text import slugify
from unidecode import unidecode


def generate_slug(string):
    return slugify(unidecode(string))
