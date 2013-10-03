# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from ratings_system.models import *
from graticule.models import *
from score.models import *

import datetime

# SECTION about/
def about(request):
    return render(request, 'ratings_system/about.html')

# SECTION u/<handle>/ (user_urls.py):

# Takes care of all unary things except index pages.
# Should probably namespace this at least a little
def facility_unary_view(request, gid, html_name):
    location = 'ratings_system/' + html_name + '.html'
    facility = Facility.objects.get(pk=gid)
    return render(
        request, location, {'facility': facility})

def facility_review_posted(request, gid):
    facility = Facility.objects.get(pk=gid)

    review = Review()
    review.pub_date = datetime.datetime.utcnow()
    review.facility = facility
    review.user = request.POST['user'] #probably need to do a lookup
    review.title = request.POST['title']
    
    review.karma = 0

    review.tf_vote = request.POST['tf']
    review.accs_vote = request.POST['accs']
    review.maint_vote = request.POST['maint']
    review.overall_vote = request.POST['overall']

    return render(
        request, 'ratings_system/facility_review_posted.html',
        {'facility': facility})

def style(request, style_sheet_name):
    return render(
        request, 'rd/style/mainstyle.css')

def user_unary_view(request, gid, html_name):
    location = 'ratings_system/' + html_name + '.html'
    user = User.objects.get(pk=gid)
    return render(
        request, location, {'user': user})

def facility_index(request, gid):
    facility = Facility.objects.get(pk=gid)
    return render(
        request, 'ratings_system/facility_index.html',
        {'facility': facility})

def user_index(request, gid):
    return render(
        request, 'ratings_system/user_index.html',
        {'gid': gid})

def index(request):
    return render(
        request, 'ratings_system/index.html',)

# search/ (search_urls.py)

def search_results(request, field_name, value):
    return render(
        request, 'ratings_system/search_results.html',
        {'field_name': field_name, 'value': value})

def search_index(request):
    return render(
        request, 'ratings_system/search_index.html')
