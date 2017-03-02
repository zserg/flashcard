from rest_framework import serializers, status
from .models import Deck, Flashcard

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'name', 'description')



