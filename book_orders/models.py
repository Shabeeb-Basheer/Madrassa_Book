# book_orders/models.py

from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    available_classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name

class BookOrder(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    selected_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='book_orders')
    books = models.ManyToManyField(Book)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name
