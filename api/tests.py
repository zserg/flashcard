from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from itertools import count
from datetime import datetime

from .models import Deck, Flashcard


class TestDeck(object):
    _ids = count(1)

    def __init__(self,  user, create=True):
        self.name = 'name_'+str(user)+' '+str(self._ids)
        self.description = 'description_'+str(user)+' '+str(self._ids)
        self.data = {'name': self.name, 'description': self.description}
        next(self._ids)
        if create:
            self.deck = Deck.objects.create(owner=user, name=self.name, description=self.description)
            self.details = {'id': self.deck.id, 'name': self.deck.name,
                           'description': self.deck.description}


class TestCard(object):
    _ids = count(1)

    def __init__(self, user, deck, easiness=0, consec_correct_answers=0, create=True):
        #import ipdb; ipdb.set_trace()
        self.question = 'question_'+str(user)+' '+str(self._ids)
        self.answer = 'answer_'+str(user)+' '+str(self._ids)
        self.data = {'question': self.question, 'answer': self.answer,
                'easiness': easiness,
                'consec_correct_answers': consec_correct_answers}
        if create:
            self.card = Flashcard.objects.create(owner = user, deck=deck,
                    question = self.question, answer = self.answer,
                    easiness = easiness, consec_correct_answers = consec_correct_answers)
            self.details = {'id': self.card.id, 'question': self.card.question,
                           'answer': self.card.answer, }

    # owner = models.ForeignKey(User,on_delete=models.CASCADE)
    # deck = models.ForeignKey(Deck)
    # question = models.TextField()
    # answer = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # last_shown_at = models.DateTimeField(auto_now_add=True)
    # next_due_date = models.DateTimeField(auto_now_add=True)
    # easiness = models.IntegerField(default=0)
    # consec_correct_answers = models.IntegerField(default=0)

def get_inteval(resp_data):
    #import ipdb; ipdb.set_trace()
    last_shown = datetime.strptime(resp_data['last_shown_at'],  "%Y-%m-%dT%H:%M:%S.%fZ")
    next_due = datetime.strptime(resp_data['next_due_date'],  "%Y-%m-%dT%H:%M:%S.%fZ")
    return (next_due - last_shown).days

class APITestCase(TestCase):

    def assertDictContainsSubset(self, subset, dictionary, *args):
        #import ipdb; ipdb.set_trace()
        for key, value in subset.items():
            self.assertIn(key, dictionary)
            self.assertEqual(dictionary[key], value)

    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.client = APIClient()

    def test_get_decks_list_anonymous(self):
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user1);

        response = self.client.get(reverse('decks-list'))
        self.assertEqual(response.status_code, 401)

    def test_get_decks_list(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user1);

        response = self.client.get(reverse('decks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(deck1.details in response.data, True)
        self.assertEqual(deck2.details in response.data, True)

    def test_get_decks_list_another_user(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user2);

        response = self.client.get(reverse('decks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(deck1.details in response.data, True)
        self.assertEqual(deck2.details in response.data, False)

    def test_get_deck_details(self):
        self.client.force_authenticate(user=self.user2)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user2);

        response = self.client.get(reverse('deck-details', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, deck2.details)

    def test_get_deck_details_nonexisted(self):
        self.client.force_authenticate(user=self.user2)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user2);

        response = self.client.get(reverse('deck-details', args=[3]))
        self.assertEqual(response.status_code, 404)

    def test_get_deck_details_not_owner(self):
        self.client.force_authenticate(user=self.user2)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user2);

        response = self.client.get(reverse('deck-details', args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_create_deck(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1, create=False);
        response = self.client.post(reverse('decks-list'),deck1.data)

        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(deck1.data, response.data)

    def test_create_deck_noauth(self):
        deck1 = TestDeck(self.user1, create=False);
        response = self.client.post(reverse('decks-list'),deck1.data)

        self.assertEqual(response.status_code, 401)

    def test_get_cards_list(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck, 0, 0)

        response = self.client.get(reverse('cards-list', args=[deck1.deck.id]))
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(card1.details, response.data[0])

    def test_get_cards_list_multiple(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck, 0, 0)
        card2 = TestCard(self.user1, deck1.deck, 0, 0)
        card3 = TestCard(self.user1, deck1.deck, 0, 0)

        response = self.client.get(reverse('cards-list', args=[deck1.deck.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_get_cards_list_nonexisting_deck(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.get(reverse('cards-list', args=[2]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_create_card(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1, create=False)
        response = self.client.post(reverse('cards-list', args=[deck1.deck.id]),card1.data)

        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(card1.data, response.data)

    def test_card_details(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck)
        response = self.client.get(reverse('card-details',
             args=[deck1.deck.id, card1.card.id]))

        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(card1.details, response.data)

    def test_card_ratings(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck)
        response = self.client.get(reverse('card-ratings',
             args=[deck1.deck.id, card1.card.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual('easiness' in response.data, True)
        self.assertEqual('last_shown_at' in response.data, True)
        self.assertEqual('next_due_date' in response.data, True)

    def test_card_set_rating(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck)
        response = self.client.post(reverse('card-ratings',
            args=[deck1.deck.id, card1.card.id]), {'rating': 5})

        self.assertEqual(response.status_code, 202)
        self.assertEqual('easiness' in response.data, True)
        self.assertEqual('last_shown_at' in response.data, True)
        self.assertEqual('next_due_date' in response.data, True)
        self.assertEqual(get_inteval(response.data), 6)

    def test_card_set_rating_unauth(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck)
        self.client.force_authenticate(user=self.user2)
        response = self.client.post(reverse('card-ratings',
            args=[deck1.deck.id, card1.card.id]), {'rating': 5})

        self.assertEqual(response.status_code, 404)

    def test_card_set_rating_0(self):
        self.client.force_authenticate(user=self.user1)
        deck1 = TestDeck(self.user1)
        card1 = TestCard(self.user1, deck1.deck)
        response = self.client.post(reverse('card-ratings',
            args=[deck1.deck.id, card1.card.id]), {'rating': 0})

        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 202)
        self.assertEqual('easiness' in response.data, True)
        self.assertEqual('last_shown_at' in response.data, True)
        self.assertEqual('next_due_date' in response.data, True)
        self.assertEqual(get_inteval(response.data), 0)

