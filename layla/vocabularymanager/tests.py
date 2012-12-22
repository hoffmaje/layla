# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class VocabularyManagerTest(TestCase):

    def setUp(self):
        User.objects.create_user('john', email='john@dow.com', password='dow')

    def test_home_url_status_200(self):
        client = Client()
        client.login(username='john', password='dow')
        response = client.get('/vocabularymanager/')
        self.assertEqual(response.status_code, 200)

    def test_status_code_550_for_anonymous_user(self):
        response = Client().get('/vocabularymanager/')
        self.assertRedirects(response, '/login/?next=/vocabularymanager/')
