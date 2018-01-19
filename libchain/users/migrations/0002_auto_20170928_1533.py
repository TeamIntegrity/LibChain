# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='libcard',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='entity',
            field=models.CharField(blank=True, choices=[('student', 'STUDENT'), ('librarian', 'LIBRARIAN'), ('faculty', 'FACULTY'), ('staff', 'STAFF')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.BigIntegerField(blank=True),
        ),
    ]