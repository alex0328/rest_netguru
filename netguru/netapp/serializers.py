from django.contrib.auth.models import User, Group
from rest_framework import serializers
from netapp.models import Movies, Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    Title = serializers.CharField(required=True)
    Year = serializers.IntegerField(required=False)
    Rated = serializers.IntegerField(required=False)
    Released = serializers.IntegerField(required=False)
    class Meta:
        model = Movies
        fields = ['Title',
                  'Year',
                  'Rated',
                  'Released',
                  ]

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['tytul','is_true']

class MoviesSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ['Title']