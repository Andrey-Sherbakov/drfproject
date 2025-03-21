from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer


# Create your views here.
class MovieAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
