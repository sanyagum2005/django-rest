from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()
    summary = models.TextField()
    genre = models.CharField(max_length=50)