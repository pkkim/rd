# TODO: Make appropriate fields nullable, figure out why
# adding facility returns error, add total vote weight

from django.db import models
from score.models import Score
from graticule.models import Graticule

# Create your models here.
class Facility(models.Model):
    pub_date = models.DateTimeField('Date published') # date of first creation #

    SU_BATHROOM = "Single-user bathroom"
    MU_BATHROOM = "Multi-user bathroom"
    ELEVATOR = "Elevator"
    PATH = "Path or shortcut"
    LOC_TYPE_CHOICES = [
        (SU_BATHROOM, "Single-user bathroom"),
        (MU_BATHROOM, "Multi-user bathroom"),
        (ELEVATOR, "Elevator"),
        (PATH, "Path or shortcut"),
        ]

    loc_name = models.CharField( #
        'Location name', max_length=50)
    loc_type = models.CharField( #
        'Location type', max_length=50,
        choices=LOC_TYPE_CHOICES, default=SU_BATHROOM)
    building_code_url = 'http://registrar.uchicago.edu/page/building-abbreviations-addresses'
    building_code_help_text = 'Use building codes at \
<a href="' + building_code_url + '">' + building_code_url + '</a>, or OTHER.'
    loc_desc = models.CharField( #
        'Location description', max_length=500,
        help_text="Describe the location of the facility and how to get there.")
    # Location description.
    building_code = models.CharField( #
        'Building code', max_length=20,
        help_text=building_code_help_text)
    # use building code or OTHER

    coords = models.ForeignKey(Graticule) #
    # Default latitude is = 41.789569, default longitude is -87.599654.
    # To change this, go to graticule.models and change default values
    # for Graticule.lon and Graticule.lat.

    # Don't mess with these next lines
    tf = models.ForeignKey(Score, related_name='tf_id')
    accs = models.ForeignKey(Score, related_name='accs_id')
    maint = models.ForeignKey(Score, related_name='maint_id')
    overall = models.ForeignKey(Score, related_name='overall_id')
    #ASPECT_1 = models.ForeignKey(Score, related_name='#ASPECT_2_id')
    #ASPECT_1 = models.ForeignKey(Score, related_name='#ASPECT_2_id')
    #ASPECT_1 = models.ForeignKey(Score, related_name='#ASPECT_2_id')
    # Need to explain this

    # score_fields = ['tf', 'accs', 'maint', 'overall']
    # Trans*-friendly, accessible, well-maintained, overall exp.
    decay_increment = 604800
    decay_factor = 0.99
    # 604800 seconds in one week. Works out to a score decaying to
    # 60 percent of its value over 52 weeks. Feel free to change.

    valid_scores = (1, 2, 3, 4, 5)
    # <score>.score must be in valid_scores to be counted as a score.

    def __unicode__(self):
        return self.loc_name

    def is_bathroom(self):
        return self.loc_type in (self.SU_BATHROOM, self.MU_BATHROOM, )

    def is_su_bathroom(self):
        return self.loc_type in (self.SU_BATHROOM, )

    def add_review(self, review):
        '''Registers Review with the Facility.'''
        # There's nothing we have to do to the self object here,
        # since key is from Review to Facility. We can also update
        # the tags via the Tag method.
        # UNCOMMENT THE FOLLOWING EVENTUALLY
        # review.save()

        for aspect in self.score_fields:
            print vars(self)[aspect]
            vars(self)[aspect].update_score( # should be aspect_id?
                vote=vars(review)[aspect+'_vote'], valid_scores=self.valid_scores,
                empty_ok=True)

    def remove_review(self, review):
        '''Removes Review from the Facility.'''
        pass

class Bathroom(Facility):
    gender_type = models.CharField(max_length=5) # M, W, A, etc?

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique = True)
    # tag content

    facilities = models.ManyToManyField(Facility)

class Bad(Tag):
    pass

class Good(Tag):
    pass

class Review(models.Model):
    pub_date = models.DateTimeField() # Publication date.
    facility = models.ForeignKey('Facility') # foreign key to Facility
    user = models.ForeignKey('User') # foreign key to user
    title = models.CharField(max_length=50) # review title

    karma = models.ForeignKey(Score, related_name='review_karma')
    # Score, determined by +/-, like Reddit post karma

    # All *_vote are votes valued 1, 2, or 3.
    tf_vote = models.IntegerField()
    accs_vote = models.IntegerField()
    maint_vote = models.IntegerField()
    overall_vote = models.IntegerField()
    #ASPECT_3_vote = models.IntegerField()
    #ASPECT_3_vote = models.IntegerField()
    #ASPECT_3_vote = models.IntegerField()

    bads = models.ManyToManyField(Bad, verbose_name='Warnings')
    goods = models.ManyToManyField(Good, verbose_name='Features')

    body = models.TextField() # Review body text.

class User(models.Model):
    creation_date = models.DateTimeField()
    nick = models.CharField(max_length=20, unique = True)
    real_name = models.CharField(max_length=120)

    points = models.ForeignKey(Score)
    
    facilities = models.ManyToManyField(Facility)
