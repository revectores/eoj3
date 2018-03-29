# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-18 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0025_auto_20180313_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityparticipant',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('d', 'Declined to answer')], max_length=5),
        ),
        migrations.AddField(
            model_name='activityparticipant',
            name='graduate_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activityparticipant',
            name='major',
            field=models.CharField(blank=True, choices=[('cs', 'Computer Science'), ('se', 'Software Engineering'), ('ee', 'Electrical Engineering'), ('math', 'Math Science'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('business', 'Business'), ('literature', 'Literature'), ('art', 'Art')], max_length=30),
        ),
    ]