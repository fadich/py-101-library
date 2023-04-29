from django.test import TestCase

from .models import Country


def numbers_sum(a, b):
    return a + b


class TestExample(TestCase):

    def test_numbers_sum__one_plus_two__three_returned(self):
        sum_ = numbers_sum(1, 2)
        self.assertEqual(sum_, 3)

    def test_numbers_sum__two_plus_two__is_not_five(self):
        sum_ = numbers_sum(2, 2)
        self.assertNotEqual(sum_, 5)

    def test_books_url(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)

    def test_country_creation(self):
        self.assertEqual(Country.objects.count(), 0)

        country = Country()
        country.name = "UA"
        country.save()

        self.assertEqual(Country.objects.count(), 1)

    def test_country_creation_two(self):
        self.assertEqual(Country.objects.count(), 0)

        Country.objects.create(
            name="UK",
        )

        self.assertEqual(Country.objects.count(), 1)
