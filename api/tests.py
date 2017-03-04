from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Deck, Flashcard

class TestDeck(object):

    def __init__(self,  user):
        self.deck = Deck.objects.create(owner = user,
                        name = 'name_' + str(user),
                        description = 'description_' + str(user))
        self.details = {'id': self.deck.id, 'name': self.deck.name,
                       'description': self.deck.description}


class APITestCase(TestCase):

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

    def test_get_deck_details_not_owner(self):
        self.client.force_authenticate(user=self.user2)
        deck1 = TestDeck(self.user1);
        deck2 = TestDeck(self.user2);

        response = self.client.get(reverse('deck-details', args=[1]))
        self.assertEqual(response.status_code, 404)

    # def test_create_deck(self):
    #     response = self.client.post(reverse('decks-list'), {'name':'new_name',
    #                                                          'description':'new_description'})
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data, {'id':1, 'name':'new_name',
    #                       'description': 'new_description'})

    # def test_get_cards_list(self):
    #     deck = Deck.objects.create(owner = self.user,
    #                                name = 'test_deck',
    #                                description = 'test_descriprion')
    #     deck = Flashcard.objects.create(owner = self.user,
    #                                deck = deck,
    #                                question = 'test_question',
    #                                answer = 'test_answer',
    #                                easiness = 0,
    #                                consec_correct_answers = 0)

    #     response = self.client.get(reverse('cards-list'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, [{'id':1, 'deck':deck.id, 'question':'test_question',
    #          'answer':'test_answer', 'easiness':0, 'consec_correct_answers':0}])

    # def test_get_cards_list_by_deck(self):
    #     deck1 = Deck.objects.create(owner = self.user,
    #                                name = 'test_deck1',
    #                                description = 'test_descriprion')
    #     deck2 = Deck.objects.create(owner = self.user,
    #                                name = 'test_deck2',
    #                                description = 'test_descriprion')
    #     card = Flashcard.objects.create(owner = self.user,
    #                                deck = deck1,
    #                                question = 'test_question',
    #                                answer = 'test_answer',
    #                                easiness = 0,
    #                                consec_correct_answers = 0)

    #     response = self.client.get(reverse('cards-by-deck-list', kwargs={'deck':'1'}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, [{'id':1, 'deck':deck1.id, 'question':'test_question',
    #          'answer':'test_answer', 'easiness':0, 'consec_correct_answers':0}])

    # def test_get_cards_list_by_deck_wrong_deck(self):
    #     deck1 = Deck.objects.create(owner = self.user,
    #                                name = 'test_deck1',
    #                                description = 'test_descriprion')
    #     deck2 = Deck.objects.create(owner = self.user,
    #                                name = 'test_deck2',
    #                                description = 'test_descriprion')
    #     card = Flashcard.objects.create(owner = self.user,
    #                                deck = deck1,
    #                                question = 'test_question',
    #                                answer = 'test_answer',
    #                                easiness = 0,
    #                                consec_correct_answers = 0)

    #     response = self.client.get(reverse('cards-by-deck-list', kwargs={'deck':'2'}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data, [] )

    # def test_create_card(self):
    #     response = self.client.post(reverse('decks-list'), {'name':'new_name',
    #                                                          'description':'new_description'})
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data, {'id':1, 'name':'new_name',
    #                       'description': 'new_description'})



