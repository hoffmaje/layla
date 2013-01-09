# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    language = models.CharField(max_length=80)

    def __unicode__(self):
        return self.language


class Phrase(models.Model):
    value = models.CharField(max_length=80)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.value

