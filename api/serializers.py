from rest_framework import serializers, status
from .models import Deck, Flashcard

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'name', 'description')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'answer', 'easiness', 'consec_correct_answers')
        read_only_fields = ('created_at', 'last_shown_at', 'next_due_date')

