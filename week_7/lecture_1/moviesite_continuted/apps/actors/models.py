# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models

class ActorManager(models.Manager):
    def say_first(self):
        # same as Actor.objects.first()
        print self.first()

    def nineties_babies(self):
        return self.exclude(dob__lt="1990-01-01").exclude(dob__gt="1999-12-31")

    def validate_new_actor(self, post_data):
        print post_data, "from manager"
        # no empty fields
        errors = []
        if len(post_data['first']) < 1 or len(post_data['last']) < 1 or len(post_data['dob']) < 1:
            errors.append("no empty fields")
        return errors

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    has_oscar = models.BooleanField()

    objects = ActorManager()

    def age(self):
        return (date.today() - self.dob).days/365

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre)
    release_date = models.DateField()
    cast = models.ManyToManyField(Actor, related_name="filmography")





# td => Traing Day
# dz = Actor.objects.get(id=7)
# td.cast.add(dz)
