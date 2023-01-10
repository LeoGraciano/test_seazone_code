import random
from django.test import TestCase

from apps.immobile.models import Immobile


class ImmobileTestCase(TestCase):

    def setUp(self):

        data = dict(
            limit_guests=random.randint(1, 10),
            qty_bathrooms=random.randint(1, 10),
            accept_pet=random.randint(0, 1),
            cleaning_value=random.randint(1, 100000),
            is_active=False,
        )

        Immobile.objects.create(**data)

    def test_created(self):

        i = Immobile.objects.all()

        self.assertEqual(i.count(), 1)

    def test_random_code(self):

        i = Immobile.objects.first()

        self.assertIsNotNone(i.code)

    def test_not_is_active(self):

        i = Immobile.objects.first()

        self.assertFalse(i.is_active)

    def test_auto_active_at_in_active(self):

        _ = Immobile.objects.first()

        _.is_active = True

        _.save()

        i = Immobile.objects.first()

        self.assertTrue(i.active_at)
