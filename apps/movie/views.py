from django.shortcuts import render
from django_tables2.config import RequestConfig
from rest_framework.decorators import api_view
from apps.movie.models import *
from apps.movie.tables import MovieTable


@api_view(['GET'])
def view_movies(request, *args, **kwargs):
    template = 'show_movies.html'

    filter_dict = dict()
    if request.GET.get('name'):
        filter_dict['name__icontains'] = request.GET.get('name')

    if request.GET.get('director'):
        filter_dict['director__name__icontains'] = request.GET.get('director')

    movies = Movie.objects.filter(**filter_dict)
    movie_table = MovieTable(movies)
    RequestConfig(request).configure(movie_table)
    context_dict = {'movies': movies}
    return render(request, template, context_dict)

@api_view(['GET', 'POST'])
def manage_movies(request, *args, **kwargs):
    pass