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
        #self.client.force_authenticate(user=self.user)

    def test_get_decks_list(self):
        #import ipdb; ipdb.set_trace()
        deck = Deck.objects.create(owner = self.user,
                                   name = 'test_deck',
                                   description = 'test_descriprion')

        response = self.client.get(reverse('decks-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id':1, 'name':'test_deck',
                          'description': 'test_descriprion'})


        # node = Datanode.objects.filter(name='Temperature')
        # self.assertEqual(response.status_code, 201)
        # self.assertEqual(len(node), 1)
        # self.assertEqual(node[0].node_path, 'Some/Path')
        # self.assertEqual(node[0].unit, 'c')
        # self.assertEqual(node[0].device.name, 'test_device')

        # point = Datapoint.objects.filter(node__name='Temperature')
        # self.assertEqual(len(point), 1)
        # self.assertEqual(point[0].value, '42')

