from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.movie.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ShopSenseMovie.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^movies/$', view_movies, name='view_movies'),
    url(r'^movie/add/$', add_movies, name='add_movies'),
    url(r'^movie/(?P<movie_id>[-\w]+)/edit/$', edit_movies, name='edit_movies'),
)
