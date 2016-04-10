import django_tables2 as tables
from apps.movie.models import Movie


class MovieTable(tables.Table):

    class Meta:
        model = Movie
        per_page = 25

    def __init__(self, *args, **kwargs):
        kwargs['template'] = 'table_small.html'
        super(MovieTable, self).__init__(*args, **kwargs)
