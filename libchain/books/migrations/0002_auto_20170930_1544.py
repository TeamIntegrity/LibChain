# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 15:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publish_year',
        ),
        migrations.RemoveField(
            model_name='bookdescription',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='bookdescription',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='bookdescription',
            name='subject',
        ),
    ]
