from django.db import models
from django.utils import timezone

class Score(models.Model):
    total_votes = models.IntegerField(
        'Total number of votes, unweighted',
        default=-1)
    total_weight = models.FloatField(
        'Total number of votes, weighted',
        default=-1)

    weight_update_incr = models.IntegerField(default=-1)
    # Frequency with which total weight is decayed in
    # seconds. 
    weight_decay_param = models.FloatField(default=-1)
    # Every weight_update_incr, the total_weight is
    # multiplied by weight_decay_param. It's probably
    # better, if the server can handle it, to update
    # at least once a day, so that new reviews don't
    # take big weight-hits immediately.
    #
    # Only supports exponential decay and non-decaying
    # weight, as well as exponential growth if you want
    # to do that for some reason.

    score = models.FloatField(
        'Average score, weighted', default=-1)

    def update_score(self, vote, valid_scores, empty_ok):
        '''Updates score to reflect new vote, if
        it is in the list valid_scores.'''
        if vote in valid_scores:
            self.total_votes += 1
            self.total_weight += 1
            self.score += (vote - self.score) / self.total_weight
            # Updates, using new total_weight.
        elif empty_ok:
            pass
        else:
            raise ValidationError # TODO: Catch this

    def get_date_weight(self, date):
        '''Gets the current weight of a vote at a certain DateTime
        object. Used when deleting a vote.'''
        seconds_since_writing = (datetime.utcnow() - date).total_seconds()
        periods = seconds_since_writing / self.weight_update_incr
        weight = (self.weight_decay_param) ** floor(periods)
        
        return weight

    def remove_score(self, vote, date):
        '''Removes the influence of a given vote at a given date.'''
        date_weight = self.get_date_weight(date)

        self.total_weight -= date_weight
        self.score -= (vote - self.score) * date_weight / total_weight
        self.total_votes -= 1

    def decay_weight(self):
        '''Set up a cron job to do this every so often'''
        self.weight *= self.weight_decay_param


