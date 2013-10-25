from django.contrib import admin
from ratings_system.models import Facility, Review, User
from score.models import Score
from graticule.models import Graticule

#class FacilityAdmin(admin.ModelAdmin):
#    Facility()
#    fieldsets = [
#        (None, {'fields': ['loc_name', 'pub_date',
#                           'loc_type']}),
#        ('Location', {'fields': [
#                    'building_code', 'loc_desc', 'coords',]}),
#        ('Ratings', {'fields': [
#                    'tf', 'accs', 'maint', 'overall'
#                    ]}),
#        ]

class ReviewAdmin(admin.ModelAdmin):
            fieldsets = [
                (None, {'fields': [
                            'title', 'pub_date', 'facility', 'user']}),
                ('Scores', {'fields': [
                            'tf_vote', 'accs_vote',
                            'maint_vote', 'overall_vote']}),
                ('Body', {'fields': [
                            'bads', 'goods']})
]

# class CustomUserAdmin(admin.ModelAdmin):
#             fieldsets = [
#                 (None, {'fields': [
#                             'nick', 'real_name',
#                             'creation_date']}),
#                 ('Record', {'fields': [
#                             'facilities', 'points']}),
# ]

admin.site.register(Facility)
admin.site.register(Review)
# admin.site.register(User)
admin.site.register(Graticule)

