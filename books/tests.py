from django.test import TestCase
from .models import Country, Book, Publisher, Genre


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