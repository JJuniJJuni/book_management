from django.contrib import admin
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=45)
    isbn10 = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    book_type = models.CharField(max_length=45)
    publisher = models.CharField(max_length=45)
    author = models.CharField(max_length=45)


class BookInfo(models.Model):
    book = models.OneToOneField(Book, on_delete=True)
    publication_at = models.DateField(null=True, blank=True)
    registration_at = models.DateTimeField(auto_now_add=True)
    book_writing = models.TextField(blank=True)
    book_contents = models.TextField(blank=True)
    star_point = models.PositiveSmallIntegerField(null=True, blank=True)
    author_writing = models.TextField(blank=True)


admin.site.register(Book)
admin.site.register(BookInfo)
