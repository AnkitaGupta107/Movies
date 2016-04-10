from django.forms.models import ModelForm
from apps.movie.models import Movie, Director


class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['director']


class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['director_name']


class EditMovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ['director']


class EditDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['director_name']
