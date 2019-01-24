from books.models import Book
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Rental(models.Model):
    lender = models.ForeignKey(User, on_delete=True)
    book = models.OneToOneField(Book, on_delete=True)
    rental_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(null=True, blank=True)
    return_standby = models.BooleanField(default=False)


admin.site.register(Rental)
