# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-20 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='hash',
            field=models.CharField(default='0xasdfg12345', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='return_time',
            field=models.DateTimeField(blank='True'),
        ),
    ]
