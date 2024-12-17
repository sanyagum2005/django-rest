from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    summary = models.TextField()
    genre = models.CharField(max_length=50)