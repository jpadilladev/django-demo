from rest_framework import serializers
from . import models


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = models.Movie