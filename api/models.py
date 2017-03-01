from django.db import models

from datetime import datetime

class Deck(models.Model):
    owner = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharFiled(max_length=255)
    description = models.TextField()


class Flashcard(models.Model):
    owner = models.ForeignKey(Users,on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_shown_at = models.DateTimeField(auto_now_add=True)
    next_due_date = models.DateTimeField(auto_now_add=True)
    easiness = models.IntegerField(default=0)
    consec_correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return self.front

    def get_next_due_date(self, rating):
        """ Supermemo-2 algorithm realization.
        Args:
            easiness (int) - answer rating (0=worst, 5=best)

        Returns:
            next_due_date,easiness,consec_correct_answers (tuple) - information
                to update Flashcard data
        """

        correct = (easiness > 3)
        easiness = self.easiness - 0.8 + 0.28*rating + 0.02*rating**2

        if correct:
            consec_correct_answers = self.consec_correct_answers + 1
            interval = 6*easiness**(consec_correct_answers-1)
        else:
            consec_correct_answers = 0
            interval = 1

        next_due_date = datetime.now() + datetime.timedelta(days=interval)
        return next_due_date, easiness, consec_correct_answers









