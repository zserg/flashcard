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

class RatingSeriallizer(serializers.Serializer):
    rating = serializers.IntegerField(write_only=True, min_value=0, max_value=5)
    easiness = serializers.FloatField(read_only=True)
    cca = serializers.IntegerField(read_only=True)
    last_shown_at = serializers.DateTimeField(read_only=True)
    next_due_date = serializers.DateTimeField(read_only=True)

    def update(self, card, validated_data):
        #import ipdb; ipdb.set_trace()
        card.save(rating=int(validated_data['rating']))
        return card

