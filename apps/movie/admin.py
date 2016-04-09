from django.contrib import admin
from apps.movie.models import *

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
