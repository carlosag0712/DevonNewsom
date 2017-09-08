# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print request
    return render(request, "first_app/index.html")

def thing(request):
    print request.POST
    return redirect('/')