from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from netapp.serializers import UserSerializer, GroupSerializer, MoviesSerializer, FilmSerializer, MoviesSerializer2
from rest_framework.response import Response
from netapp.models import Movies, Film
import requests
import json
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def post(self, request):

        bill_data = request.data
        print(bill_data)

        return Response("just a test", status=status.HTTP_200_OK)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        first_title = serializer.validated_data
        title = first_title['Title']
        print(title)
        if_exists = Movies.objects.filter(Title=title).exists()
        print(if_exists)
        if if_exists==True:
            queryset = Movies.objects.filter(Title=title)
            serializer_class = MoviesSerializer
            return Response(serializer.data)
        else:
            apikey = "81b6b98e"
            service = "http://www.omdbapi.com/"
            payload = {'apikey': apikey, 't': title}
            r = requests.get(service, params=payload)
            print(r)
            response_json = r.json()
            income_response = response_json["Response"]
            if income_response:
                print(response_json["Year"])
                income_year = int(response_json["Year"])
                #income_imdbRating = int(response_json["imdbRating"])
                #income_imdbVotes = int(response_json["imdbVotes"])
                film_add = Movies(Title=response_json["Title"],
                                Year = income_year,
                                Rated = response_json["Rated"],
                                Released=response_json["Released"],
                                Runtime=response_json["Runtime"],
                                Genre=response_json["Genre"],
                                Director=response_json["Director"],
                                Writer=response_json["Writer"],
                                Actors=response_json["Actors"],
                                Plot=response_json["Plot"],
                                Language=response_json["Language"],
                                Country=response_json["Country"],
                                Awards=response_json["Awards"],
                                Poster=response_json["Poster"],
                                Metascore=response_json["Metascore"],
                                imdbRating=response_json["imdbRating"],
                                imdbVotes=response_json["imdbVotes"],
                                imdbID=response_json["imdbID"],
                                Type=response_json["Type"],
                                DVD=response_json["DVD"],
                                BoxOffice=response_json["BoxOffice"],
                                Production=response_json["Production"],
                                Website=response_json["Website"],
                                Response=response_json["Response"],
                                  )
                film_add.save()
                print(response_json["Title"])
                print(response_json)
                return Response(response_json)
            else:
                return Response(response_json)



        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MoviesViewSet2(viewsets.ModelViewSet):
    def get(self, request):
        pass