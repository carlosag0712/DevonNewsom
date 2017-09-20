# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Actor, Movie
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        'actors': Actor.objects.all()
    }
    return render(request, "actors/index.html", context)

def filtered(request):
    context = {
        'actors': Actor.objects.exclude(has_oscar=True)
    }
    return render(request, "actors/index.html", context)

def show(request, actor_id):
    context = {
        "actor": Actor.objects.get(id=actor_id),
        "all_movies": Movie.objects.all()
    }
    return render(request, "actors/show_actor.html", context)

def add_to_filmog(request, actor_id):
    the_actor = Actor.objects.get(id=actor_id)
    the_movie = Movie.objects.get(id=request.POST['movie'])

    # this is how we add a relationship
    the_actor.filmography.add(the_movie)

    # this is how we remove a relationship
    # the_actor.filmography.remove(the_movie)

    return redirect('/')

def new(request):
    return render(request, 'actors/new.html')

def create(request):

    actor_has_oscar = False
    if "has_oscar" in request.POST:
        actor_has_oscar = True

    error_list = Actor.objects.validate_new_actor(request.POST)
    if not error_list:
        Actor.objects.create(
            first_name = request.POST['first'],
            last_name = request.POST['last'],
            dob = request.POST['dob'],
            has_oscar = actor_has_oscar
            #has_oscar = True if "has_oscar" in request.POST else False
        )

    return redirect('/')

def destroy(request, actor_id):
    actor_to_delete = Actor.objects.get(id=actor_id)
    actor_to_delete.delete()
    return redirect('/')

#############################################
# Movies
#############################################

def new_movie(request):
    return render(request, 'actors/new_movie.html')

def create_movie(request):
    Movie.objects.create(
        title=request.POST['title'],
        genre=request.POST['genre'],
        release_date=request.POST['release_date'],
    )
    return redirect('/movies/new')
