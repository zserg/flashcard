from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

class APIFactoryTestCase(APITestCase):

    def setUp(self):
        self.factory=APIRequestFactory()
        self.user = User.objects.create(username='test')

    def test_devices_list_empty(self):
        request = self.factory.get('fake-path')
        force_authenticate(request, user=self.user)
        response = device_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['fullsize'], 0)
        self.assertEqual(response.data['items'], [])

    def test_devices_list_one_required(self):
        Device.objects.create_device({'name':'some-dev'})

        request = self.factory.get('fake-path', HTTP_HOST='localhost')
        force_authenticate(request, user=self.user)
        response = device_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['fullsize'], 1)
        self.assertNotEqual(response.data['items'][0]['dev_id'],'')
        self.assertEqual(response.data['items'][0]['name'],'some-dev')

