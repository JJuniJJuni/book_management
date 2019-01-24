from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestUsedTemplate(TestCase):
    def test_user_should_response_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_user_should_login_by_right_email(self):
        right_user = User.objects.create(email="test@rgpkorea.co.kr")
        self.client.force_login(right_user)
        response = self.client.get(reverse('home_page'))
        self.assertTemplateUsed(response, 'home.html')

    def test_user_should_not_login_by_wrong_email(self):
        wrong_user = User.objects.create(email="test@gmail.com")
        self.client.force_login(wrong_user)
        response = self.client.get(reverse('home_page'))
        self.assertTemplateNotUsed(response, 'home.html')
