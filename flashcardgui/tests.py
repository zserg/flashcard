from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

from api.models import Deck, Flashcard



class FlashcardsTestCase(TestCase):

    def setUp(self):
        self.user_name = 'user1'
        self.user_pass = 'pass1'
        self.user1 = User.objects.create_user(self.user_name, password=self.user_pass)
        Flashcard.objects.create_flashcard(self.user1, 'q1', 'a1', 'deck1')
        Flashcard.objects.create_flashcard(self.user1, 'q2', 'a2', 'deck1')
        Flashcard.objects.create_flashcard(self.user1, 'q3', 'a3', 'deck2')

        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse('login'))
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('username', response.context['form'].fields)
        self.assertIn('email', response.context['form'].fields)
        self.assertIn('password1', response.context['form'].fields)
        self.assertIn('password2', response.context['form'].fields)

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)

    def test_home_auth(self):
        status = self.client.login(username=self.user_name, password=self.user_pass)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('decks', response.context)
        self.assertEqual(response.context['user'].username, self.user_name)

    def test_add_card(self):
        status = self.client.login(username=self.user_name, password=self.user_pass)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('decks', response.context)
        self.assertEqual(response.context['user'].username, self.user_name)
        self.assertEqual(len(response.context['decks']), 2)




# Create your tests here.
