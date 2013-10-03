from django.db import models
from math import acos, cos, sin, radians

# Create your models here.

class Graticule(models.Model): 
    lat = models.FloatField(default=41.789569)
    lon = models.FloatField(default=-87.599654)

    def distance(self, other):
        lat1 = radians(self.lat)
        lon1 = radians(self.lon)
        lat2 = radians(other.lat)
        lon2 = radians(other.lon)

        return acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon2 - lon1))

    def __unicode__(self):
        return '(%f, %f)' % (self.lat, self.lon)

    # 40.800491,-73.958: Central Park West and 110th st
    # 40.768029,-73.981854: Central Park West and 59th st
    # Expect 2.55 miles
    # acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon2 - lon1)) * 3963
    # is 2.5694588071704456, which is good enough.
