from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Book
from .models import BookInfo


class TestUsedTemplate(TestCase):
    def setUp(self):
        self.book = Book.objects.create()
        self.info = BookInfo.objects.create(book=self.book)
        self.user = User.objects.create(email='test@rgpkorea.co.kr')
        self.client.force_login(self.user)

    def test_home_should_response_template(self):
        response = self.client.get(reverse('list'))
        self.assertTemplateUsed(response, 'list.html')

    def test_list_should_response_template(self):
        response = self.client.get(reverse('info', kwargs={
            'book_id': self.book.id
        }))
        self.assertTemplateUsed(response, 'info.html')
