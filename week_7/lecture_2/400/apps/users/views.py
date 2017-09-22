# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Friend

# Create your views here.
def index(request):
    return render(request, "users/registration.html")

def register(request):

    errors = Friend.objects.validate_registration(request.POST)
      
    if errors:
        for fail in errors:
            messages.error(request, fail)
        return redirect('/')
    print "no errors here"
    return redirect('/')

def success(request):
    pass