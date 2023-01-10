from django.urls import reverse, reverse_lazy
from django.test import TestCase
import random

from apps.immobile.models import Immobile


class ImmobileViewTestCase(TestCase):

    def setUp(self):

        data = dict(
            code="12345678",
            limit_guests=random.randint(1, 10),
            qty_bathrooms=random.randint(1, 10),
            accept_pet=random.randint(0, 1),
            cleaning_value=random.randint(1, 100000),
        )

        Immobile.objects.create(**data)

    def test_status_list_code_200(self):
        response = self.client.get(reverse('immobile-list'))
        self.assertEqual(response.status_code, 200)

    def test_have_code_in_list(self):
        response = self.client.get(reverse('immobile-list'))

        result = response.data['results'][0]

        self.assertEqual(result['code'], '12345678')

    def test_have_url_detail(self):
        response = self.client.get(reverse('immobile-list'))

        result = response.data['results'][0]

        self.assertTrue(result["url"])

    def test_haver_code_in_detail(self):
        _ = self.client.get(reverse('immobile-list'))

        _result = _.data['results'][0]

        response = self.client.get(
            reverse(
                'immobile-detail', kwargs={'pk': _result['id']}
            )
        )

        self.assertEqual(response.data['code'], '12345678')
