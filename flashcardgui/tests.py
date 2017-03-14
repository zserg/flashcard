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
        response = self.client.get('/accounts/login/')
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        response = self.client.get(reverse('signup'))
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual('form' in response.context, True)

    def test_signup_post(self):
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'}

        response = self.client.post(reverse('signup'), data)
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 301)
        self.assertEqual('form' in response.context, True)




# Create your tests here.
