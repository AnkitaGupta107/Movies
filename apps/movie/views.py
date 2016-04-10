from django.shortcuts import render
from django_tables2.config import RequestConfig
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from apps.movie.forms import *
from apps.movie.models import *
from apps.movie.tables import MovieTable
from utils.general_methods import get_json_response


@api_view(['GET'])
@permission_classes((AllowAny, ))
def view_movies(request, *args, **kwargs):
    template = 'show_movies.html'

    filter_dict = dict()
    if request.GET.get('name'):
        filter_dict['name__icontains'] = request.GET.get('name')

    if request.GET.get('director'):
        filter_dict['director__director_name__icontains'] = request.GET.get('director')

    movies = Movie.objects.filter(**filter_dict)
    movie_table = MovieTable(movies)
    RequestConfig(request).configure(movie_table)
    context_dict = {'movies': movies}
    return render(request, template, context_dict)

@api_view(['GET', 'POST'])
@permission_classes((IsAdminUser, ))
def add_movies(request, *args, **kwargs):
    template = 'add_movie.html'

    if request.method == 'GET':
        movie_form = AddMovieForm()
        director_form = AddDirectorForm()
        context_dict = {'movie_form': movie_form, 'director_form': director_form}
        return render(request, template, context_dict)

    elif request.method == 'POST':
        movie_form = AddMovieForm(request.POST)
        director_form = AddDirectorForm(request.POST)
        if director_form.is_valid() and movie_form.is_valid():
            director = director_form.save()
            movie = movie_form.save(commit=False)
            movie.director = director
            movie.save()
            context_dict = {'movie_form': movie_form, 'director_form': director_form, 'form_saved': 'Movie added successfully.'}
            return render(request, template, context_dict)
        else:
            return render(request, template, {'movie_form': movie_form, 'director_form': director_form})
    return render(request, template, {'msg': 'Cannot create Movies at present'})

@api_view(['GET', 'POST'])
@permission_classes((IsAdminUser,))
def edit_movies(request, *args, **kwargs):
    template = 'edit_movie.html'
    movie_pk = kwargs.get('movie_id')
    movie = Movie.objects.get(pk=int(movie_pk))
    director = Director.objects.filter(pk=movie.director.pk).first()

    if request.method == 'GET':
        movie_form = EditMovieForm(instance=movie)
        director_form = EditDirectorForm(instance=director)
        context_dict = {'movie_form': movie_form, 'director_form': director_form}
        return render(request, template, context_dict)

    if request.method == 'POST':
        if request.is_ajax() and request.POST.get('delete'):
            movie.delete()
            context_msg = {'message': 'Movie deleted successfully!!', 'status': 'ok'}
            return get_json_response(context_msg)

        movie_form = EditMovieForm(request.POST, instance=movie)
        director_form = EditDirectorForm(request.POST, instance=director)

        if director_form.is_valid() and movie_form.is_valid():
            direc = director_form.save()
            mov = movie_form.save(commit=False)
            mov.director = direc
            mov.save()
            context_dict = {'movie_form': movie_form, 'director_form': director_form, 'form_saved': 'Movie updated successfully.'}
            return render(request, template, context_dict)
        else:
            return render(request, template, {'movie_form': movie_form, 'director_form': director_form})
    return render(request, template, {'msg': 'Cannot create Movies at present'})



