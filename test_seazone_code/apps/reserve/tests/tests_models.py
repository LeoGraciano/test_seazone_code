import random
from datetime import timedelta

from apps.announcement.models import Announcement
from apps.immobile.models import Immobile
from apps.reserve.models import Reserve
from django.test import TestCase
from django.utils import timezone
from faker import Faker

fake = Faker(['pt_BR'])


class ReserveTestCase(TestCase):

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

    def test_created(self):

        a = Reserve.objects.all()

        self.assertEqual(a.count(), 1)

    def test_code(self):

        a = Reserve.objects.first()

        self.assertTrue(a.code)
