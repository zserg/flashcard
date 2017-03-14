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
        response = self.client.get('/accounts/register/')
        #import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIn('username', response.context['form'].fields)
        self.assertIn('email', response.context['form'].fields)
        self.assertIn('password1', response.context['form'].fields)
        self.assertIn('password2', response.context['form'].fields)

    def test_signup_post(self):
        data = {'username': 'testuser', 'password1': 'Testpassword',
                'password2': 'Testpassword', 'email': 'test@example.com'}

        response = self.client.post('/accounts/register', data)
        import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 301)
        self.assertEqual('form' in response.context, True)




# Create your tests here.
