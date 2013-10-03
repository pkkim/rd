# Search: by name, type, tags, ratings, publication date,
# location description, building, coordinates
# What's not googleable? type, tags, ratings,
# publication date, building, coordinates

from django.conf.urls import patterns, include, url
from ratings_system import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'rd.views.home', name='home'),
    # url(r'^rd/', include('rd.foo.urls')),

    url(r'^results/q?(?P<field_name>[a-z_]+)=(?P<value>.*)',
        views.search_results, name='search_results'),

    url(r'^', views.search_index,
        name='search_index'),
)
