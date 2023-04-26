from django.db import models


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        unique_together = [
            ["name", "country"]
        ]
    def __str__(self):
        return f"{self.name}, {self.country}"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    year_publishing = models.SmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.name}, {self.authors.first()}, {self.year_publishing}"
