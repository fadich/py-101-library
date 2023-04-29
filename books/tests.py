from django.test import TestCase

from .models import Country, Book, Publisher, Genre


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


class TestUrls(TestCase):
    def test_book_details_not_exist(self):
        self.assertEqual(Book.objects.count(), 0)
        response = self.client.get("/books/1/")
        self.assertEqual(response.status_code, 404)

    def test_create_book(self):
        country = Country.objects.create(name="UA")
        publisher = Publisher.objects.create(name="", country=country)
        genre = Genre.objects.create(name="", description="")
        book = Book.objects.create(
            id=1,
            name = "book1",
            ISBN = "1234",
            description = "man",
            year_publishing = 1973,
            publisher = publisher,
            genre = genre
        )

        self.assertEqual(Country.objects.count(), 1)

        response = self.client.get(f'/books/{book.id}/')
        self.assertEqual(response.status_code, 200)