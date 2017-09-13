# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Friend
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "friends": Friend.objects.all()
    }
    return render(request, 'friends/index.html', context)

def create(request):

    # INSERT INTO friends (first_name,last_name,created_at,updated_at)
    # VALUES (:request.POST['first']...)

    Friend.objects.create(
        first_name = request.POST['first'],
        last_name = request.POST['last']
    )

    return redirect('/')

def show(request, friend_id):

    # this will query ANY id passed to it by way of a url string (see urls.py)
    print Friend.objects.get(id=friend_id)
    return redirect('/')