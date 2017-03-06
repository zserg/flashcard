from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class Deck(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()


class Flashcard(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_shown_at = models.DateTimeField(auto_now_add=True)
    next_due_date = models.DateTimeField(auto_now_add=True)
    easiness = models.FloatField(default=2.5)
    consec_correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def get_next_due_date(self, rating):
        """ Supermemo-2 algorithm realization.
        http://www.blueraja.com/blog/477/a-better-spaced-repetition-learning-algorithm-sm2
        Args:
            easiness (int) - answer rating (0=worst, 5=best)

        Returns:
            next_due_date,easiness,consec_correct_answers (tuple) - information
                to update Flashcard data
        """

        correct = (rating >= 3)
        easiness = self.easiness - 0.8 + 0.28*rating + 0.02*rating**2
        if easiness < 1.3:
            easiness = 1.3
        if correct:
            consec_correct_answers = self.consec_correct_answers + 1
            interval = 6*easiness**(consec_correct_answers-1)
        else:
            consec_correct_answers = 0
            interval = 1

        next_due_date = datetime.now() + datetime.timedelta(days=interval)
        return next_due_date, easiness, consec_correct_answers

    def save(self, rating=None, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        if rating:
            self.next_due_date, self.easiness, self.consec_correct_answers =  self.get_next_due_date(self, rating)
        super(Flashcard, self).save(*args, **kwargs) # Call the "real" save() method.








