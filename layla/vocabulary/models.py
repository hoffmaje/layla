# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class Language(models.Model):
    value = models.CharField(max_length=80)

    def __unicode__(self):
        return self.value


class Phrase(models.Model):
    value = models.CharField(max_length=80)
    language = models.ForeignKey(Language)

    def __unicode__(self):
        return self.value

