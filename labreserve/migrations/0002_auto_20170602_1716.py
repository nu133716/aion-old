# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreserve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_client',
            field=models.CharField(max_length=200, verbose_name='Reserved For'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(verbose_name='Reservation Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_period',
            field=models.IntegerField(choices=[(1, '1st Period'), (2, '2nd Period'), (3, '3rd Period'), (4, '4th Period'), (5, '5th Period'), (6, '6th Period'), (7, '7th Period'), (8, '8th Period')], default=1, verbose_name='Period'),
        ),
    ]
