from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.id}. {self.name} ({self.country})"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    biography = models.TextField()

    def __str__(self):
        return f"{self.id}. {self.first_name} ({self.last_name})"


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
