import random
from datetime import timedelta

from apps.announcement.models import Announcement
from apps.immobile.models import Immobile
from apps.reserve.models import Reserve
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from faker import Faker

fake = Faker(['pt_BR'])


class ReserveViewTestCase(TestCase):

    def setUp(self):

        _ = dict(
            limit_guests=random.randint(1, 10),
            qty_bathrooms=random.randint(1, 10),
            accept_pet=random.randint(0, 1),
            cleaning_value=random.randint(1, 100000)
        )

        _i = Immobile.objects.create(**_)

        _ = dict(
            immobile=_i,
            platform_name="AirBnb",
            platform_tax=1.3
        )

        _a = Announcement.objects.create(**_)

        data = dict(
            announcement=_a,
            check_in=timezone.now().date().strftime('%Y-%m-%d'),
            check_out=(timezone.now() + timedelta(days=2)
                       ).strftime('%Y-%m-%d'),
            price_total=random.randint(1, 100000),
            comment=fake.text(),
            number_quests=random.randint(1, 1000)
        )

        Reserve.objects.create(**data)

    def test_status_list_code_200(self):
        response = self.client.get(reverse('reserve-list'))
        self.assertEqual(response.status_code, 200)

    def test_have_code_list(self):
        response = self.client.get(reverse('reserve-list'))

        result = response.data['results'][0]

        self.assertTrue(result['code'])

    def test_have_url_detail(self):
        response = self.client.get(reverse('reserve-list'))

        result = response.data['results'][0]

        self.assertTrue(result["url"])

    def test_have_code_in_detail(self):
        _ = self.client.get(reverse('reserve-list'))

        _result = _.data['results'][0]

        response = self.client.get(
            reverse(
                'reserve-detail', kwargs={'pk': _result['id']}
            )
        )

        self.assertEqual(response.data['id'], _result['id'])

    def test_have_url_detail_announcement(self):
        response = self.client.get(reverse('reserve-list'))

        result = response.data['results'][0]

        self.assertTrue(result["announcement"])
