# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreatPSapp', '0008_auto_20170926_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduling',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
