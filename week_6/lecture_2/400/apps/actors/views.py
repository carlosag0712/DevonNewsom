# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Actor
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

def new(request):
    return render(request, 'actors/new.html')

def create(request):

    actor_has_oscar = False
    if "has_oscar" in request.POST:
        actor_has_oscar = True

    Actor.objects.create(
        first_name = request.POST['first'],
        last_name = request.POST['last'],
        dob = request.POST['dob'],
        has_oscar = actor_has_oscar
        #has_oscar = True if "has_oscar" in request.POST else False
    )

    return redirect('/')

def show(request, actor_id):
    pass

def destroy(request, actor_id):
    actor_to_delete = Actor.objects.get(id=actor_id)
    actor_to_delete.delete()
    return redirect('/')