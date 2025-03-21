from rest_framework import generics, viewsets

from movies.models import Movie, Category
from movies.serializers import MovieSerializer, CategorySerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
