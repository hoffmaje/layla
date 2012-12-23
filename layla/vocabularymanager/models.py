# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=80)


class Phrase(models.Model):
    phrase = models.CharField(max_length=80)
    language = models.ForeignKey(Language)

