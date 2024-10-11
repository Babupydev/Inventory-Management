from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):
    def test_create_item(self):
        url = reverse('create_item')
        data = {'name': 'Item1', 'description': 'Test item', 'quantity': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = Item.objects.create(name="Item2", description="Another test", quantity=5)
        url = reverse('read_item', args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
