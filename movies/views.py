from rest_framework import generics

from . import models
from . import serializers


class ListMovie(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class GetMovie(generics.RetrieveAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer