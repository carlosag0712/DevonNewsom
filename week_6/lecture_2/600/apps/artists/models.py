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