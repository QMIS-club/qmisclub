# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-07 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date_and_time', models.DateTimeField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('event_description', models.TextField(default='description here ', max_length=500)),
                ('event_pictures', models.ManyToManyField(blank=True, to='club.Picture', verbose_name='event pictures')),
                ('event_videos', models.ManyToManyField(blank=True, to='club.Video', verbose_name='event videos')),
            ],
        ),
    ]
