from django.conf.urls import patterns, include, url
from ratings_system import views 

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'rd.views.home', name='home'),
    # url(r'^rd/', include('rd.foo.urls')),

    url(r'^(?P<gid>[a-zA-Z0-9-_.]+)/(?P<html_name>user_reviews)/',
        views.user_unary_view, name='user_reviews'),
    url(r'^(?P<gid>[a-zA-Z0-9-_.]+)/(?P<html_name>user_send_message)/',
        views.user_unary_view, name='user_send_message'),
    url(r'^(?P<gid>[a-zA-Z0-9-_.]+)/(?P<html_name>user_facilities)/',
        views.user_unary_view, name='user_facilities'),
    url(r'^(?P<gid>[a-zA-Z0-9-_.]+)/', views.user_index, name='user_index'),
)
