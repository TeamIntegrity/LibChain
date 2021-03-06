# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_number', models.IntegerField()),
                ('publish_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('branch', models.CharField(choices=[('cse', 'COMPUTER SCIENCE AND ENGINEERING'), ('et&t', 'ELECTRONICS AND TELECOMMUNICATIONS'), ('eee', 'ELECTRICAL AND ELCETRONICS ENGINEERING'), ('mech', 'MECHANICAL ENGINEERING'), ('civil', 'CIVIL ENGINEERING')], max_length=20)),
                ('sem', models.CharField(choices=[('1', '1st SEMESTER'), ('2', '2nd SEMESTER'), ('3', '3rd SEMESTER'), ('4', '4th SEMESTER'), ('5', '5th SEMESTER'), ('6', '6th SEMESTER'), ('7', '7th SEMESTER'), ('8', '8th SEMESTER')], max_length=1)),
                ('subject', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('initial_stock', models.IntegerField()),
                ('available_stock', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.BookDescription'),
        ),
    ]
