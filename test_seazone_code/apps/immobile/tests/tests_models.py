import random
from django.test import TestCase

from apps.immobile.models import Immobile


class ImmobileTestCase(TestCase):

    def setUp(self):

        data = dict(
            limit_guests=random.randint(1, 10),
            qty_bathrooms=random.randint(1, 10),
            accept_pet=random.randint(0, 1),
            cleaning_value=random.randint(1, 100000)
        )

        Immobile.objects.create(**data)

    def test_created(self):

        i = Immobile.objects.all()

        self.assertEqual(i.count(), 1)

    def test_random_code(self):

        i = Immobile.objects.first()

        self.assertIsNotNone(i.code)

    def test_code_eith(self):

        i = Immobile.objects.first()

        self.assertEqual(len(i.code), 8)
