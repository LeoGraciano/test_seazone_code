from django.urls import reverse, reverse_lazy
from django.test import TestCase
import random

from apps.immobile.models import Immobile
from apps.announcement.models import Announcement


class AnnouncementViewTestCase(TestCase):

    def setUp(self):

        _ = dict(
            limit_guests=random.randint(1, 10),
            qty_bathrooms=random.randint(1, 10),
            accept_pet=random.randint(0, 1),
            cleaning_value=random.randint(1, 100000)
        )

        _i = Immobile.objects.create(**_)

        data = dict(
            immobile=_i,
            platform_name="AirBnb",
            platform_tax=1.3
        )

        Announcement.objects.create(**data)

    def test_status_list_code_200(self):
        response = self.client.get(reverse('announcement-list'))
        self.assertEqual(response.status_code, 200)

    def test_have_platform_name_list(self):
        response = self.client.get(reverse('announcement-list'))

        result = response.data['results'][0]

        self.assertEqual(result['platform_name'], 'AirBnb')

    def test_have_url_detail(self):
        response = self.client.get(reverse('announcement-list'))

        result = response.data['results'][0]

        self.assertTrue(result["url"])

    def test_have_code_in_detail(self):
        _ = self.client.get(reverse('announcement-list'))

        _result = _.data['results'][0]

        response = self.client.get(
            reverse(
                'announcement-detail', kwargs={'pk': _result['id']}
            )
        )

        self.assertEqual(response.data['id'], _result['id'])

    def test_have_url_detail_immobile(self):
        response = self.client.get(reverse('announcement-list'))

        result = response.data['results'][0]

        self.assertTrue(result["immobile"])
