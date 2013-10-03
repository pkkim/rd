from ratings_system.models import *
from score.models import *

f, r = Facility().prepare(), Review()

print f.tf
print '==='
f.add_review(r)
