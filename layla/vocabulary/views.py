# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Copyright 2012 Jens Hoffmann (hoffmaje)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from layla.vocabulary.models import Phrase


@login_required
def home(request):
    data = {
        'phrases': Phrase.objects.all()
    }
    return render(request, 'vocabulary/home.html', data)

