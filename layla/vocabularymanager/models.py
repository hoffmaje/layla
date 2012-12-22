# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class Language(models.Model):
    label = models.CharField(max_length=80)


class Word(models.Model):
    label = models.CharField(max_length=80)
    language = models.ForeignKey(Language)

