# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.db import models

from ratings_system.models import *
from graticule.models import *
from score.models import *

import datetime

def new_facility(request):
    critlist = [
        ('tf', 'Trans*-friendliness',
         'Is this facility friendly for people who don\'t neatly fit into the gender-sex binary?'),
        ('accs', 'Accessiility',
         'How usable is this facility for disabled people?'),
        ('maint', 'Maintenance',
         'Is this facility clean, stocked with necessities if applicable, etc.?'),
        ('overall', 'Overall',
         'Overall, how is your experience of using this facility?')
                ]
    valid_values = range(1, 6)
    return render(request, 'ratings_system/new_facility.html',
                  {'typelist': Facility.LOC_TYPE_CHOICES,
                   'critlist': critlist,
                   'valid_values': valid_values,})

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
    
    error_message = ""

    try:
        tf_val = int(request.POST['tf'])
        accs_val = int(request.POST['accs'])
        maint_val = int(request.POST['maint'])
        overall_val = int(request.POST['overall'])
    except:
        error_message = "Error: All votes must be between 1 and 5."
    try:
        thisuser = request.POST['user']
        customuser = CustomUser.Objects.get(thisuser)
    except:
        error_message = "Username error, probably user not found."

    review = Review.objects.create(
        pub_date = datetime.datetime.utcnow(),
        facility_id = facility,
        user = customuser,
        title = request.POST['title'],
        karma = 0,
        tf_vote = tf_val,
        accs_vote = accs_val,
        maint_vote = maint_val,
        overall_vote = overall_val,)

    facility.add_review(review)

    return render(
        request, 'ratings_system/facility_review_posted.html',
        {'facility': facility, 'error_message': error_message})

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
    facility_list = Facility.objects.all()
    return render(
        request, 'ratings_system/index.html',
        {'facility_list': facility_list})

# search/ (search_urls.py)

def search_results(request, field_name, value):
    return render(
        request, 'ratings_system/search_results.html',
        {'field_name': field_name, 'value': value})

def search_index(request):
    return render(
        request, 'ratings_system/search_index.html')
