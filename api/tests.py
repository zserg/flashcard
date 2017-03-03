from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Deck, Flashcard

class APITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_decks_list(self):
        #import ipdb; ipdb.set_trace()
        deck = Deck.objects.create(owner = self.user,
                                   name = 'test_deck',
                                   description = 'test_descriprion')

        response = self.client.get(reverse('decks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id':1, 'name':'test_deck',
                          'description': 'test_descriprion'}])

    def test_get_deck(self):
        deck = Deck.objects.create(owner = self.user,
                                   name = 'test_deck',
                                   description = 'test_descriprion')

        response = self.client.get(reverse('deck-details', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id':1, 'name':'test_deck',
                          'description': 'test_descriprion'})

    def test_create_deck(self):
        response = self.client.post(reverse('decks-list'), {'name':'new_name',
                                                             'description':'new_description'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'id':1, 'name':'new_name',
                          'description': 'new_description'})

    def test_get_cards_list(self):
        deck = Deck.objects.create(owner = self.user,
                                   name = 'test_deck',
                                   description = 'test_descriprion')
        deck = Flashcard.objects.create(owner = self.user,
                                   deck = deck,
                                   question = 'test_question',
                                   answer = 'test_answer',
                                   easiness = 0,
                                   consec_correct_answers = 0)

        response = self.client.get(reverse('cards-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id':1, 'deck':deck.id, 'question':'test_question',
             'answer':'test_answer', 'easiness':0, 'consec_correct_answers':0}])

    # owner = models.ForeignKey(User,on_delete=models.CASCADE)
    # deck = models.ForeignKey(Deck)
    # question = models.TextField()
    # answer = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # last_shown_at = models.DateTimeField(auto_now_add=True)
    # next_due_date = models.DateTimeField(auto_now_add=True)
    # easiness = models.IntegerField(default=0)
    # consec_correct_answers = models.IntegerField(default=0)

