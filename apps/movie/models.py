from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255, help_text='Name of the movie')
    imdb_score = models.FloatField(default=0, help_text='Ratings')
    genre = models.TextField(help_text="Drama, History, Romance (Comma separated values)")
    popularity99 = models.FloatField(default=0.0, help_text="How popular the movie is? (in %)")
    director = models.ForeignKey("Director", on_delete=models.SET_NULL, related_name='movie_director', null=True, blank=True)

    def __unicode__(self):
        return str(self.pk) + ":" + self.name + "," + self.director

class Director(models.Model):
    director_name = models.CharField(max_length=255, help_text="Name of the film Director")

    def __unicode__(self):
        return self.director_name
