# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Friend, Crew

def verify_session_user(request):
    try:
        request.session['id']
    except KeyError:
        return redirect('/')

# Create your views here.
def index(request):

    return render(request, "users/index.html")

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/registration.html')

def login(request):
    errors_or_user = Friend.objects.validate_login(request.POST)

    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/login_view')
    request.session['id'] = errors_or_user[1].id
    return redirect('/success')


def register(request):
    errors_or_user = Friend.objects.validate_registration(request.POST)

    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/register_view')
    request.session['id'] = errors_or_user[1].id
    return redirect('/success')

# LOGIN REQUIRED
def success(request):
    # check for request.session['id']
    verify_session_user(request)
    context = {
        "user": Friend.objects.get(id = request.session['id']),
        # other_crews: crews that don't include logged-user
        "other_crews": Crew.objects.exclude(members__id = request.session['id'])
    }
        
    return render(request, "users/success.html", context)

def logout(request):
    del request.session['id']
    return redirect('/')

# LOGIN REQUIRED
def create_crew(request):
    verify_session_user(request)

    new_crew = Crew.objects.create(
        name = request.POST['name'],
        slogan = request.POST['slogan'],
    )
    # to add new crew => some_crew.members.add(some_friend)
    new_crew.members.add(Friend.objects.get(id = request.session['id']))
    return redirect('/success')

def join_crew(request):
    verify_session_user(request)
    # request.POST['crew_id']
    Crew.objects.get(id=request.POST['crew_id']).members.add(
        Friend.objects.get(id=request.session['id'])
    )
    return redirect('/success')
