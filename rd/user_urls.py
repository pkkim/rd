from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'rd.views.home', name='home'),
    # url(r'^rd/', include('rd.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^[0-9]+/', include('facility_urls')),
    url(r'^u/', include('user_urls')),
    url(r'^search/', include('search_urls')),
    url(r'^about/', views.about, name='about'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'/', index)
)
