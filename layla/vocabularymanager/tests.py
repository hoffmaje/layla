# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class VocabularyManagerTest(TestCase):
    def test_home_url_status_200(self):
        client = Client()
        response = client.get('/vocabularymanager/')
        self.assertEqual(response.status_code, 200)

