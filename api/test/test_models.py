from django.test import SimpleTestCase, TestCase, Client
from api.models import Text

import random


class TestModels(TestCase):
    def setUp(self) -> None:
        self.slug="Name1"+str(random.randint(99,999))
        self.project1=Text.objects.create(
            name="Name1",
            num=10,
            slug=self.slug
        )

    def test_slug(self):
        self.assertEqual(self.project1.slug,self.slug)
