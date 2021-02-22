from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Film

def film(request, name):
    def pager(name):
        for film in Film.objects.all():
            if int(name) == film.id:
               return film

    return render(request, "APLIKACJA/film.html", {
        'name': int(name),
        'film': pager(name)
    })

def index(request):
    return render(request, "APLIKACJA/index.html", {
        'Film': Film.objects.all(),
    })


