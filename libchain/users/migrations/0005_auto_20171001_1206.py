# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('users', '0004_auto_20170928_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='department.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(blank=True, choices=[('COMPUTER SCIENCE AND ENGINEERING', 'COMPUTER SCIENCE AND ENGINEERING'), ('ELECTRONICS AND TELECOMMUNICATIONS', 'ELECTRONICS AND TELECOMMUNICATIONS'), ('ELECTRICAL AND ELCETRONICS ENGINEERING', 'ELECTRICAL AND ELCETRONICS ENGINEERING'), ('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'), ('CIVIL ENGINEERING', 'CIVIL ENGINEERING')], max_length=10, null=True),
        ),
    ]
