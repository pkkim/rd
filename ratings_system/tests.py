from django.template import RequestContext, loader
from django.db import models

from ratings_system.models import *
from graticule.models import *
from score.models import *

import datetime

from django.utils import unittest
from django.test import TestCase

class InitializeTestCase(TestCase):
    def setUp(self):
        g = Graticule.objects.create()
        score = Score.objects.create()
        Facility.objects.create(
            id = 1,
            pub_date = datetime.datetime.today(),
            coords_id = g.id,
            tf_id = score.id,
            accs_id = score.id,
            maint_id = score.id,
            overall_id = score.id
            )

        cu = CustomUser.objects.create(
            points_id = 1)
        facility = Facility.objects.get(id=1)
        cu.facilities.add(facility)
 
        review = Review.objects.create(
            id = 1,
            pub_date = datetime.datetime.today(),
            facility_id = 1,
            user_id = 1,
            title = "My test review",
            karma_id = 1,
            tf_vote = 1,
            accs_vote = 1,
            maint_vote = 1,
            overall_vote = 1,
            body = "Some bullshit")

    def test_facility_created(self):
        facility = Facility.objects.get(id=1)
        g = Graticule.objects.all()[0]
        score = Score.objects.all()[0]
        cu = CustomUser.objects.get(id=1)
        review = Review.objects.get(id=1)

        self.assertEqual(facility.id, 1)
        self.assertEqual(facility.coords_id, g.id)
        self.assertEqual(facility.tf_id, score.id)
        self.assertEqual(facility.accs_id, score.id)
        self.assertEqual(facility.maint_id, score.id)
        self.assertEqual(facility.overall_id, score.id)

        self.assertEqual(review.id, 1)
        self.assertEqual(review.facility_id, facility.id)
        self.assertEqual(review.user_id, cu.id)
        self.assertEqual(review.karma_id, 1)
        self.assertEqual(review.tf_vote, 1)
        self.assertEqual(review.accs_vote, 1)
        self.assertEqual(review.maint_vote, 1)
        self.assertEqual(review.overall_vote, 1)
        self.assertEqual(review.body, "Some bullshit")

