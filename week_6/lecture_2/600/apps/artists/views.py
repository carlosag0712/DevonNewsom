# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Artist
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "artists": Artist.objects.all()
    }
    return render(request, "artists/index.html", context)

def new(request):
    return render(request, "artists/new.html")

def show(request, artist_id):
    context = {
        "artist": Artist.objects.get(id=artist_id)
    }
    return render(request, 'artists/show.html', context)

def create(request):
    print request.POST

    print("ohw" in request.POST)
    if "ohw" in request.POST:
        print("we have one hits")
    else:
        print("we have many hits")

    Artist.objects.create(
        name = request.POST['name'],
        date_formed = request.POST['formed'],
        one_hit_wonder = "ohw" in request.POST
    )
    print("we have created artist!!")

    return redirect('/')

def delete(request, artist_id):
    artist_to_delete = Artist.objects.get(id=artist_id)
    artist_to_delete.delete()

    return redirect('/')