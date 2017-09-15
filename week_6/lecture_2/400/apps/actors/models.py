# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    has_oscar = models.BooleanField()

    def age(self):
        return (date.today() - self.dob).days/365

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)