from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

from api.models import Deck, Flashcard



class FlashcardsTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse('login'))
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        response = self.client.get(reverse('signup'))
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)



# Create your tests here.
