from django.db import models

# Create your models here.
class bookslist(models.Model):
    title: models.CharField(max_length=20)
    author: models.CharField(max_length=100)
    published_date: models.DateField
    isbn: models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title


