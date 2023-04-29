from django.test import TestCase
from .models import Genre, Publisher, Country


class GenreTest(TestCase):

    def test_name(self):
        p = Genre.objects.create(
            name='Novel',
            description='Some test description'
        )

        self.assertEqual(p.name, 'Novel')

    def test_description(self):
        p = Genre.objects.create(
            name='Novel',
            description='Some test description'
        )

        self.assertNotEqual(p.description, ' ')


class PublisherTest(TestCase):

    def setUp(self) -> None:
        self.country = Country.objects.create(
            name='Ukraine'
        )

    def test_country(self):
        p = Publisher.objects.create(
            name='АБАБАГАЛАМАГА',
            country=self.country
        )

        self.assertEqual(p.country.name, 'Ukraine')

    def test_name(self):
        p = Publisher.objects.create(
            name='АБАБАГАЛАМАГА',
            country=self.country
        )

        self.assertEqual(p.name, 'АБАБАГАЛАМАГА')
