# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_formed', models.DateField()),
                ('one_hit_wonder', models.BooleanField()),
            ],
        ),
    ]