# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'layla.main.views.home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
)
