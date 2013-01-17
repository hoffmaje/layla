# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db import models


class Language(models.Model):
    value = models.CharField(max_length=80)
    country_code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.value


class Phrase(models.Model):
    class Meta:
        ordering = ['language__country_code']

    language = models.ForeignKey(Language)
    value = models.CharField(max_length=80)
    translations = models.ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return "%s - %s" % (self.language.country_code, self.value)

