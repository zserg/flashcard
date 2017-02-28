from django.db import models

class Flashcard(models.Model):
    front = models.TextField()
    back = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    shown_at = models.DateTimeField(auto_now_add=True)




