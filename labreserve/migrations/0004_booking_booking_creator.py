# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('labreserve', '0003_auto_20170602_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
