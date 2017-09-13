# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Friend
from django.shortcuts import render, redirect

# Create your views here.
# Create your views here.
def index(request):
    context = {
        "friends": Friend.objects.all()
    }
    return render(request, "newfriends/index.html", context)

def create(request):
    print request.POST
    new_friend = Friend.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    print new_friend.id
    return redirect('/friend/{}'.format(new_friend.id))

def friend(request, friend_id):
    context = {
        "friend": Friend.objects.get(id=friend_id)
    }
    return render(request, 'newfriends/show.html', context)
