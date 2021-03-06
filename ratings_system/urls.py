from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from ratings_system import facility_urls, views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'rd.views.home', name='home'),
    # url(r'^rd/', include('rd.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^search/', include('ratings_system.search_urls')),
    url(r'^facility/', include('ratings_system.facility_urls')),
    url(r'^u/', include('ratings_system.user_urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^style/(?P<style_sheet_name>.*)', views.style, name='style'),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^new_facility/', views.new_facility, name='new_facility'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index),
)
