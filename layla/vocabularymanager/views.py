# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from layla.vocabularymanager.models import Phrase


@login_required
def home(request):
    return render(request, 'vocabularymanager/home.html')


@login_required
def phrase(request):
    phrases = Phrase.objects.all()
    return render(request, 'vocabularymanager/phrase.html',
        { 'phrases': phrases })

