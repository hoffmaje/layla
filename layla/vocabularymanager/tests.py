"""
Copyright 2012 Jens Hoffmann (hoffmaje).
"""
from django.test import TestCase
from django.test.client import Client


class VocabularyManagerTest(TestCase):
    def test_foo(self):
        client = Client()
        response = client.get('/vocabularymanager/')
        self.assertEqual(response.status_code, 200)

