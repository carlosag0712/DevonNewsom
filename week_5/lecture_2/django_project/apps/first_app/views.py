# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"first_app/index.html")

def friends(request):
    my_friends = [
        'alicia',
        'shy-money',
        'jerry',
        'eric',
        'godzilla',
        'sean'
    ]
    return render(request,"first_app/friends.html", {"friends": my_friends})    

def one_friend(request, friend):
    print friend
    return HttpResponse("Hello {} is a great friend".format(friend))