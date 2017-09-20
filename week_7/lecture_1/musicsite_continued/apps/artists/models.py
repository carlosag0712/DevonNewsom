# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    date_formed = models.DateField()
    one_hit_wonder = models.BooleanField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Artist, related_name="groups_joined")
    # needs artist ref and album ref
    # ex: some_album.members.add(some_artist)

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    records_sold = models.IntegerField()
    num_songs = models.IntegerField()
   
    artist = models.ForeignKey(Artist, related_name="discography")

    def __str__(self):
        return self.title