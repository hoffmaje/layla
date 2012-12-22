# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class MainTest(TestCase):
    def setUp(self):
        User.objects.create_user('john', email='john@john.com', password='dow')

    def test_login(self):
        response = Client().get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_status_200_after_login(self):
        response = Client().post('/login/', {'username': 'john', 'password': 'dow'})
        self.assertRedirects(response, '/')

    def test_logout(self):
        response = Client().post('/logout/')
        self.assertRedirects(response, '/')

