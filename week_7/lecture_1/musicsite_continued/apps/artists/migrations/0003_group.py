# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(related_name='groups_joined', to='artists.Artist')),
            ],
        ),
    ]
